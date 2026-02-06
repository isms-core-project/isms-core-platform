**ISMS-IMP-A.8.31.1-TG - Environment Architecture Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.31: Separation of Development, Test and Production Environments

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.31.1-TG |
| **Version** | 1.0 |
| **Assessment Area** | Environment Architecture & Separation Mechanisms |
| **Related Policy** | ISMS-POL-A.8.31, Section 2.1 (Environment Architecture Requirements) |
| **Purpose** | Document environment architecture, assess separation mechanisms against policy requirements, and identify gaps in environment isolation |
| **Target Audience** | IT Operations, Cloud Architects, DevOps Engineers, Security Engineers, Compliance Officers, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Quarterly or After Major Infrastructure Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Environment Architecture assessment workbook | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.8.31.1-UG.

---

# Technical Specification

## Workbook Structure

### Overview

The Environment Architecture Assessment workbook consists of 10 sheets:

1. **Instructions_Legend** - Metadata, instructions, status legend
2. **Environment_Inventory** - All environments (dev, test, staging, prod)
3. **Network_Separation** - VLANs, VPCs, firewall rules
4. **Infrastructure_Separation** - Compute, cloud accounts, databases, storage
5. **Data_Separation** - Verification of no production data in dev/test
6. **Credential_Separation** - Unique credentials per environment, PAM vault
7. **Configuration_Consistency** - Staging vs production drift
8. **Gap_Analysis** - Non-compliance identification and remediation
9. **Evidence_Register** - Supporting documentation inventory
10. **Approval_Sign_Off** - Multi-level approval workflow and signatures

---

## Sheet 1: Instructions & Legend

### Header Section

- **Row 1 (Merged A1:G1):** Title
  - Text: "ISMS-IMP-A.8.31.1 — Environment Architecture Assessment"
  - Style: Dark blue header (003366), white text, bold, centered, 40px height
  
- **Row 2 (Merged A2:G2):** Subtitle
  - Text: "ISO/IEC 27001:2022 - Control A.8.31: Separation of Development, Test and Production Environments"
  - Style: Medium blue header (4472C4), white text, centered, 30px height

### Document Information Block (Rows 4-12)

| Row | Column A (Label) | Column B (Value) | Column B Style |
|-----|------------------|------------------|----------------|
| 4 | Document ID: | ISMS-IMP-A.8.31.1 | Plain text |
| 5 | Assessment Area: | Environment Architecture & Separation | Plain text |
| 6 | Related Policy: | ISMS-POL-A.8.31, Section 2.1 | Plain text |
| 7 | Version: | 1.0 | Plain text |
| 8 | Assessment Date: | [USER INPUT] | Yellow fill (FFEB9C), bold |
| 9 | Completed By: | [USER INPUT] | Yellow fill (FFEB9C), bold |
| 10 | Organization: | [USER INPUT] | Yellow fill (FFEB9C), bold |
| 11 | Review Cycle: | Quarterly | Plain text |

**Column A:** Bold labels  
**Column B:** User input cells (rows 8-10) with yellow fill

### How to Use This Workbook (Rows 14-24)

- **Row 14:** "How to Use This Workbook" (bold, underlined)
- **Rows 15-24:** Numbered instructions (1-10)

```
1. Complete Environment_Inventory for ALL environments (including shadow/decommissioned)
2. Document Network_Separation (VLANs, VPCs, firewall rules)
3. Document Infrastructure_Separation (compute, cloud accounts, databases)
4. Verify Data_Separation (NO production data in dev/test)
5. Verify Credential_Separation (unique per environment, prod in PAM)
6. Assess Configuration_Consistency (staging vs production drift)
7. Complete Gap_Analysis for all non-compliance areas
8. Collect Evidence (network diagrams, firewall exports, screenshots)
9. Update Evidence_Register with all supporting documentation
10. Obtain three-level approval (Operations → Security → Executive)
```

### Status Legend (Rows 26-32)

| Symbol | Status | Description | Color Code |
|--------|--------|-------------|------------|
| ✅ | Compliant | Fully compliant with policy requirement | Green (C6EFCE) |
| ⚠️ | Partial | Partially compliant or compensating controls in place | Yellow (FFEB9C) |
| ❌ | Non-Compliant | Not compliant, remediation required | Red (FFC7CE) |
| 📋 | Planned | Remediation planned with target date | Blue (B4C7E7) |
| N/A | Not Applicable | Requirement not applicable to this environment | Gray (D9D9D9) |

### Acceptable Evidence (Rows 34-48)

- **Row 34:** "Acceptable Evidence (Examples)" (bold, underlined)
- **Rows 35-48:** Bulleted list with checkmarks

```
✓ Network architecture diagrams showing environment segmentation
✓ Firewall rule exports demonstrating default deny between environments
✓ Cloud account/subscription inventory (AWS, Azure, GCP)
✓ Database instance inventory (separate per environment)
✓ PAM vault configuration screenshots
✓ Infrastructure as Code (IaC) configurations (Terraform, CloudFormation)
✓ Penetration testing reports (network isolation verification)
✓ Data discovery scan results (confirming no prod data in dev/test)
✓ Configuration drift reports (terraform plan, AWS Config)
✓ Credential inventory (demonstrating separation)
✓ Access logs (cross-environment access attempts)
✓ Change management records (environment promotions)
✓ Exception approvals (documented deviations with compensating controls)
✓ Compliance dashboards (continuous monitoring results)
```

---

## Sheet 2: Environment_Inventory

### Purpose
Document all environment tiers in SDLC (development, testing, staging, production), including purpose, users, data type, and status.

### Header Section (Rows 1-2)

- **Row 1 (Merged A1:H1):** "ENVIRONMENT INVENTORY"
  - Style: Dark blue (003366), white text, bold, centered, 35px height
  
- **Row 2 (Merged A2:H2):** "Document ALL environments in SDLC - include shadow environments and decommissioned systems"
  - Style: Light blue (B4C7E7), dark text, centered, 25px height

### Column Headers (Row 4)

| Column | Header | Width | Data Type |
|--------|--------|-------|-----------|
| A | Environment Name | 20 | Text |
| B | Environment Tier | 18 | Dropdown |
| C | Purpose | 40 | Text |
| D | Primary Users | 30 | Text |
| E | Data Type | 20 | Dropdown |
| F | Availability Target | 18 | Dropdown |
| G | Status | 15 | Dropdown |
| H | Notes | 40 | Text |

**Row 4 Style:** Medium blue header (4472C4), white text, bold, centered, text wrap

### Data Validation (Dropdowns)

**Column B: Environment Tier**

- Development
- Testing/QA
- Staging/Pre-Production
- Production
- Sandbox/Developer
- Hotfix/Emergency
- Decommissioned
- Other

**Column E: Data Type**

- Synthetic (generated test data)
- Anonymized (production data anonymized)
- Production Data
- Mixed (VIOLATION if prod + non-prod)
- None

**Column F: Availability Target**

- Best Effort (no SLA)
- 95% (business hours)
- 99% (24x7)
- 99.5% (24x7)
- 99.9% (24x7 production)
- 99.99% (mission critical)

**Column G: Status**

- ✅ Deployed
- ⚠️ Partial
- ❌ Decommissioned
- 📋 Planned
- N/A

### Sample Data (Rows 5-8)

| Environment Name | Tier | Purpose | Primary Users | Data Type | Availability | Status | Notes |
|------------------|------|---------|---------------|-----------|--------------|--------|-------|
| Production | Production | Live customer operations | Operations team only | Production Data | 99.9% | ✅ Deployed | Zero developer access (policy) |
| Staging | Staging/Pre-Production | Final validation before production | Operations + Senior Devs (read-only) | Anonymized | 99% | ✅ Deployed | Mirrors production configuration |
| Testing | Testing/QA | QA testing, UAT | QA team, business users | Synthetic | 95% (business hours) | ✅ Deployed | Separate test data only |
| Development | Development | Active code development | Developers, DevOps engineers | Synthetic | Best Effort | ✅ Deployed | No production data allowed |

### User Input Rows (9+)

Yellow-filled cells (FFEB9C) for user data entry.

**Critical Notes to Include:**

- Document ALL environments, including:
  - Shadow environments (developer sandboxes)
  - Temporary environments (hotfix, demo)
  - Decommissioned environments (for audit trail)
- Note any environments where production data is present (VIOLATION if dev/test)
- Document access restrictions per environment

---

## Sheet 3: Network_Separation

### Purpose
Document network segmentation mechanisms (VLANs, VPCs, firewall rules) that separate environments.

### Header Section (Rows 1-2)

- **Row 1 (Merged A1:H1):** "NETWORK SEPARATION"
  - Style: Dark blue (003366), white text, bold, centered, 35px height
  
- **Row 2 (Merged A2:H2):** "Document VLANs/VPCs, firewall rules, and network isolation mechanisms - verify default DENY between environments"
  - Style: Light blue (B4C7E7), dark text, centered, 25px height

### Column Headers (Row 4)

| Column | Header | Width | Data Type |
|--------|--------|-------|-----------|
| A | Environment | 18 | Dropdown (from Sheet 2) |
| B | Network Segment | 20 | Text |
| C | VLAN / VPC ID | 20 | Text |
| D | IP Address Range | 18 | Text |
| E | Firewall Rules | 40 | Text |
| F | Default Policy to Other Envs | 25 | Dropdown |
| G | Allowed Exceptions | 40 | Text |
| H | Separation Quality | 18 | Dropdown |
| I | Evidence | 30 | Text |

**Row 4 Style:** Medium blue header (4472C4), white text, bold, centered, text wrap

### Data Validation (Dropdowns)

**Column A: Environment**

- Dynamically populated from Sheet 2, Column A (environment names)

**Column F: Default Policy to Other Envs**

- ✅ DENY (all traffic blocked - correct)
- ⚠️ ALLOW (traffic allowed - VIOLATION)
- ⚠️ Partial (some traffic allowed without justification)
- N/A

**Column H: Separation Quality**

- ✅ Strong (physical/account-level separation)
- ⚠️ Adequate (VLAN/namespace separation)
- ❌ Weak (logical only, shared infrastructure)
- ❌ None (no separation - VIOLATION)

### Sample Data (Rows 5-8)

| Environment | Network Segment | VLAN/VPC | IP Range | Firewall Rules | Default Policy | Allowed Exceptions | Separation | Evidence |
|-------------|-----------------|----------|----------|----------------|----------------|--------------------|------------|----------|
| Production | Corporate-Prod | VLAN 400 / vpc-prod-main | 10.400.0.0/16 | Default DENY from all other VLANs | ✅ DENY | Monitoring: 10.250.10.5, CI/CD: 10.250.20.10 | ✅ Strong | firewall-export-2024-01.txt, network-diagram.pdf |
| Staging | Corporate-Staging | VLAN 300 / vpc-staging-main | 10.300.0.0/16 | Default DENY from dev/test | ✅ DENY | Monitoring, CI/CD | ✅ Strong | firewall-export-2024-01.txt |
| Testing | Corporate-Test | VLAN 200 / vpc-test-main | 10.200.0.0/16 | Default DENY from dev/prod | ✅ DENY | Monitoring only | ✅ Strong | firewall-export-2024-01.txt |
| Development | Corporate-Dev | VLAN 100 / vpc-dev-main | 10.100.0.0/16 | Default DENY from all other VLANs | ✅ DENY | None (fully isolated) | ⚠️ Adequate | firewall-export-2024-01.txt |

### Critical Requirements

**Firewall Rules must demonstrate:**

- Default DENY between dev/test → production
- Default DENY between test → production
- Only explicitly allowed exceptions (monitoring, backup, CI/CD)
- All exceptions must have business justification

**Evidence Required:**

- Actual firewall rule export (not documentation)
- Network diagram showing segmentation
- Penetration test results (network isolation verification)

---

## Sheet 4: Infrastructure_Separation

### Purpose
Document infrastructure separation mechanisms (compute, cloud accounts, databases, storage).

### Header Section (Rows 1-2)

- **Row 1 (Merged A1:I1):** "INFRASTRUCTURE SEPARATION"
  - Style: Dark blue (003366), white text, bold, centered, 35px height
  
- **Row 2 (Merged A2:I2):** "Document compute, cloud accounts, databases, and storage - verify NO shared infrastructure between environments"
  - Style: Light blue (B4C7E7), dark text, centered, 25px height

### Column Headers (Row 4)

| Column | Header | Width | Data Type |
|--------|--------|-------|-----------|
| A | Environment | 18 | Dropdown (from Sheet 2) |
| B | Compute Resources | 30 | Text |
| C | Cloud Account/Subscription | 30 | Text |
| D | Database Instances | 30 | Text |
| E | Storage | 30 | Text |
| F | Shared Infrastructure? | 20 | Dropdown |
| G | Separation Level | 20 | Dropdown |
| H | Compliance Status | 18 | Dropdown |
| I | Evidence | 30 | Text |

**Row 4 Style:** Medium blue header (4472C4), white text, bold, centered, text wrap

### Data Validation (Dropdowns)

**Column F: Shared Infrastructure?**

- ❌ No (completely separate - correct)
- ⚠️ Yes (shared compute - weak separation)
- ⚠️ Yes (shared database instance - VIOLATION)
- ⚠️ Yes (shared storage - risk)

**Column G: Separation Level**

- ✅ Account-Level (separate AWS account/Azure subscription)
- ✅ Strong (separate VMs/instances, separate databases)
- ⚠️ Namespace-Level (Kubernetes namespaces, VMs on shared hardware)
- ❌ Logical Only (shared database, logical schema separation - VIOLATION)

**Column H: Compliance Status**

- ✅ Compliant
- ⚠️ Partial
- ❌ Non-Compliant
- 📋 Remediation Planned

### Sample Data (Rows 5-8)

| Environment | Compute | Cloud Account | Database | Storage | Shared? | Separation | Compliance | Evidence |
|-------------|---------|---------------|----------|---------|---------|------------|------------|----------|
| Production | 10 EC2 instances (dedicated) | AWS 444444444444 | RDS prod-db-01 (separate) | S3: myorg-prod-data | ❌ No | ✅ Account-Level | ✅ Compliant | aws-account-list.txt, rds-inventory.csv |
| Staging | 5 EC2 instances (dedicated) | AWS 333333333333 | RDS staging-db-01 (separate) | S3: myorg-staging-data | ❌ No | ✅ Account-Level | ✅ Compliant | aws-account-list.txt, rds-inventory.csv |
| Testing | 3 EC2 instances (shared hardware) | AWS 222222222222 | RDS test-db-01 (separate) | S3: myorg-test-data | ❌ No | ✅ Account-Level | ✅ Compliant | aws-account-list.txt, rds-inventory.csv |
| Development | Docker containers (K8s) | AWS 111111111111 | PostgreSQL dev-db (separate) | S3: myorg-dev-data | ❌ No | ⚠️ Namespace-Level | ⚠️ Partial | aws-account-list.txt, kubectl-get-ns.txt |

### Critical Requirements

**Infrastructure Separation must ensure:**

- Separate cloud accounts/subscriptions per environment (AWS, Azure, GCP)
- Separate database instances (NOT logical separation on same instance)
- Separate storage (S3 buckets, file shares, volumes)
- No shared compute between production and non-production

**Evidence Required:**

- Cloud account/subscription list (AWS CLI, Azure CLI, gcloud)
- Database instance inventory (separate instances verified)
- Storage inventory (separate buckets/shares verified)
- Virtualization/container platform inventory (namespace/cluster list)

---

## Sheet 5: Data_Separation

### Purpose
Verify NO production data in development/testing environments. Critical compliance requirement.

### Header Section (Rows 1-2)

- **Row 1 (Merged A1:H1):** "DATA SEPARATION VERIFICATION"
  - Style: Dark red (8B0000), white text, bold, centered, 35px height
  
- **Row 2 (Merged A2:H2):** "CRITICAL REQUIREMENT: Production data MUST NOT be present in development or testing environments"
  - Style: Light red (FFC7CE), dark text, bold, centered, 25px height

### Column Headers (Row 4)

| Column | Header | Width | Data Type |
|--------|--------|-------|-----------|
| A | Environment | 18 | Dropdown (from Sheet 2) |
| B | Production Data Present? | 22 | Dropdown |
| C | Data Type Used | 25 | Dropdown |
| D | Anonymization Used? | 20 | Dropdown |
| E | Anonymization Technique | 30 | Text |
| F | Verification Method | 30 | Text |
| G | Violations Found | 35 | Text |
| H | Compliance Status | 18 | Dropdown |
| I | Evidence | 30 | Text |

**Row 4 Style:** Dark red header (8B0000), white text, bold, centered, text wrap

### Data Validation (Dropdowns)

**Column B: Production Data Present?**

- ❌ No (correct for dev/test)
- ✅ Yes (only acceptable for production)
- ⚠️ Unknown (requires verification)
- ❌ Yes (VIOLATION if dev/test)

**Column C: Data Type Used**

- Synthetic (generated test data)
- Anonymized (production data anonymized per policy)
- Production Data (only acceptable in production)
- None

**Column D: Anonymization Used?**

- N/A (synthetic data, no anonymization needed)
- ✅ Yes (production data anonymized)
- ❌ No (using production data without anonymization - VIOLATION)

**Column H: Compliance Status**

- ✅ Compliant (no prod data in dev/test)
- ❌ MAJOR VIOLATION (prod data in dev/test)
- ⚠️ Verification Needed
- 📋 Remediation In Progress

### Sample Data (Rows 5-8)

| Environment | Prod Data? | Data Type | Anonymization? | Technique | Verification | Violations | Compliance | Evidence |
|-------------|------------|-----------|----------------|-----------|--------------|------------|------------|----------|
| Production | ✅ Yes (authorized) | Production Data | N/A | N/A | N/A | None | ✅ Compliant | N/A |
| Staging | ❌ No | Anonymized | ✅ Yes | k-anonymity (k=5), PII masking | Data discovery scan | None | ✅ Compliant | data-anon-procedure.pdf, scan-results.pdf |
| Testing | ❌ No | Synthetic | N/A | N/A | Data discovery scan | None | ✅ Compliant | synthetic-data-generator.yaml, scan-results.pdf |
| Development | ❌ No | Synthetic | N/A | N/A | Data discovery scan, code review | None | ✅ Compliant | scan-results.pdf, code-review-checklist.pdf |

### Critical Violations to Document

**MAJOR VIOLATIONS** (immediate remediation required):

- ❌ Production database dumps restored to dev/test
- ❌ Production backups used for testing
- ❌ Production customer data copied to dev/test
- ❌ Production API keys in dev configuration files

**Verification Methods:**

- Data discovery tool scans (Informatica, BigID, OneTrust)
- Database content analysis (sample queries)
- Configuration file review (grep for production credentials)
- Application code review (search for production API keys)

**Evidence Required:**

- Data discovery scan results
- Data anonymization procedure documentation
- Synthetic data generator configuration
- Verification test results

---

## Sheet 6: Credential_Separation

### Purpose
Verify unique credentials per environment and production credentials in PAM vault.

### Header Section (Rows 1-2)

- **Row 1 (Merged A1:I1):** "CREDENTIAL SEPARATION VERIFICATION"
  - Style: Dark blue (003366), white text, bold, centered, 35px height
  
- **Row 2 (Merged A2:I2):** "Verify unique credentials per environment - production credentials MUST be in PAM vault (NOT in code/config files)"
  - Style: Light blue (B4C7E7), dark text, centered, 25px height

### Column Headers (Row 4)

| Column | Header | Width | Data Type |
|--------|--------|-------|-----------|
| A | Credential Type | 25 | Text |
| B | Development | 20 | Text |
| C | Testing | 20 | Text |
| D | Staging | 20 | Text |
| E | Production | 20 | Text |
| F | Unique Per Environment? | 22 | Dropdown |
| G | Production in PAM Vault? | 22 | Dropdown |
| H | Compliance Status | 18 | Dropdown |
| I | Evidence | 30 | Text |

**Row 4 Style:** Medium blue header (4472C4), white text, bold, centered, text wrap

### Data Validation (Dropdowns)

**Column F: Unique Per Environment?**

- ✅ Yes (unique credentials per environment - correct)
- ❌ No (shared credentials - VIOLATION)
- ⚠️ Partial (some shared, some unique)
- ⚠️ Unknown (requires audit)

**Column G: Production in PAM Vault?**

- ✅ Yes (stored in PAM vault - correct)
- ❌ No (in code/config files - MAJOR VIOLATION)
- ❌ No (in environment variables - VIOLATION)
- ⚠️ Partial (some in vault, some not)
- N/A (not production)

**Column H: Compliance Status**

- ✅ Compliant
- ❌ MAJOR VIOLATION (shared credentials)
- ❌ MAJOR VIOLATION (prod credentials not in PAM)
- ⚠️ Partial
- 📋 Remediation In Progress

### Sample Data (Rows 5-10)

| Credential Type | Dev | Test | Staging | Production | Unique? | Prod in PAM? | Compliance | Evidence |
|-----------------|-----|------|---------|------------|---------|--------------|------------|----------|
| Database Password | dev_db_pass_xyz | test_db_pass_abc | staging_db_pass_def | [IN VAULT] | ✅ Yes | ✅ Yes | ✅ Compliant | pam-vault-screenshot.png |
| AWS Access Keys | AKIA...DEV | AKIA...TEST | AKIA...STAGING | [IN VAULT] | ✅ Yes | ✅ Yes | ✅ Compliant | aws-iam-policy-export.json |
| API Keys (3rd Party) | dev_api_123 | test_api_456 | staging_api_789 | [IN VAULT] | ✅ Yes | ✅ Yes | ✅ Compliant | pam-vault-screenshot.png |
| Service Accounts | dev_svc@example.com | test_svc@example.com | staging_svc@example.com | prod_svc@example.com | ✅ Yes | ✅ Yes | ✅ Compliant | gcp-iam-export.json |
| SSH Keys | ssh-dev-key | ssh-test-key | ssh-staging-key | [IN VAULT] | ✅ Yes | ✅ Yes | ✅ Compliant | ssh-key-inventory.txt |

### Critical Violations to Document

**MAJOR VIOLATIONS** (immediate remediation required):

- ❌ Same database password used in dev and production
- ❌ Production credentials hardcoded in application code
- ❌ Production credentials in environment variables (not PAM vault)
- ❌ Production API keys committed to source code repository

**PAM Vault Requirements:**

- All production credentials stored in PAM vault (HashiCorp Vault, CyberArk, AWS Secrets Manager, Azure Key Vault)
- Production credentials NEVER in:
  - Application code (hardcoded)
  - Configuration files (config.yaml, .env)
  - Environment variables (unless retrieving from PAM)
  - Source code repositories (Git)

**Evidence Required:**

- PAM vault configuration screenshots
- Credential inventory showing separation
- Application code review (no hardcoded credentials)
- Source code repository scan results (no secrets)

---

## Sheet 7: Configuration_Consistency

### Purpose
Assess configuration drift between staging and production environments.

### Header Section (Rows 1-2)

- **Row 1 (Merged A1:H1):** "CONFIGURATION CONSISTENCY ASSESSMENT"
  - Style: Dark blue (003366), white text, bold, centered, 35px height
  
- **Row 2 (Merged A2:H2):** "Staging SHOULD mirror production configuration (target ≤5% drift) - measure and document drift"
  - Style: Light blue (B4C7E7), dark text, centered, 25px height

### Column Headers (Row 4)

| Column | Header | Width | Data Type |
|--------|--------|-------|-----------|
| A | Configuration Item | 30 | Text |
| B | Production Value | 25 | Text |
| C | Staging Value | 25 | Text |
| D | Match? | 12 | Dropdown |
| E | Drift % | 12 | Number (%) |
| F | IaC Managed? | 15 | Dropdown |
| G | Drift Acceptable? | 18 | Dropdown |
| H | Compliance Status | 18 | Dropdown |
| I | Evidence | 30 | Text |

**Row 4 Style:** Medium blue header (4472C4), white text, bold, centered, text wrap

### Data Validation (Dropdowns)

**Column D: Match?**

- ✅ Yes (identical)
- ⚠️ Partial (intentional difference, e.g., instance size)
- ❌ No (unintentional drift)

**Column F: IaC Managed?**

- ✅ Yes (Terraform, CloudFormation, ARM template)
- ⚠️ Partial (some IaC, some manual)
- ❌ No (manual configuration - risk)

**Column G: Drift Acceptable?**

- ✅ Yes (intentional, e.g., cost optimization)
- ❌ No (should be identical, drift is issue)
- ⚠️ Under Review

**Column H: Compliance Status**

- ✅ Compliant (≤5% drift or justified)
- ⚠️ Acceptable (5-10% drift, documented)
- ❌ Non-Compliant (>10% drift or critical mismatch)

### Sample Data (Rows 5-10)

| Configuration Item | Production | Staging | Match? | Drift % | IaC? | Acceptable? | Compliance | Evidence |
|--------------------|------------|---------|--------|---------|------|-------------|------------|----------|
| Instance Type | t3.xlarge | t3.large | ⚠️ Partial | N/A | ✅ Yes | ✅ Yes (cost optimization) | ✅ Compliant | terraform-main.tf |
| Security Group Rules | sg-prod-app (22 rules) | sg-staging-app (22 rules) | ✅ Yes | 0% | ✅ Yes | ✅ Yes | ✅ Compliant | terraform-sg.tf |
| Database Version | PostgreSQL 15.4 | PostgreSQL 15.4 | ✅ Yes | 0% | ✅ Yes | ✅ Yes | ✅ Compliant | rds-inventory.csv |
| Application Version | app-v2.3.1 | app-v2.2.8 | ❌ No | 8% | ⚠️ Partial | ❌ No | ❌ Non-Compliant | deployment-log.txt (FINDING) |
| Load Balancer Config | 3 target groups | 3 target groups | ✅ Yes | 0% | ✅ Yes | ✅ Yes | ✅ Compliant | terraform-alb.tf |

### Configuration Drift Calculation

**Drift % = (Number of Different Configurations / Total Configurations) × 100**

**Example:**

- Total configuration items: 50
- Items that differ: 3
- Drift % = (3 / 50) × 100 = 6%

**Acceptable Drift:**

- ✅ ≤5% = Compliant (minor differences, mostly intentional)
- ⚠️ 5-10% = Acceptable (document justification)
- ❌ >10% = Non-Compliant (remediation required)

**Evidence Required:**

- IaC configuration files (Terraform, CloudFormation)
- `terraform plan` output showing drift detection
- AWS Config drift reports
- Configuration comparison reports

---

## Sheet 8: Gap_Analysis

### Purpose
Document all non-compliance areas, risk severity, and remediation plans.

### Header Section (Rows 1-2)

- **Row 1 (Merged A1:J1):** "GAP ANALYSIS & REMEDIATION PLANNING"
  - Style: Dark red (8B0000), white text, bold, centered, 35px height
  
- **Row 2 (Merged A2:J2):** "Document ALL gaps in environment separation - prioritize by risk severity and create remediation plans"
  - Style: Light red (FFC7CE), dark text, bold, centered, 25px height

### Column Headers (Row 4)

| Column | Header | Width | Data Type |
|--------|--------|-------|-----------|
| A | Gap ID | 10 | Text |
| B | Gap Description | 40 | Text |
| C | Policy Requirement Violated | 35 | Text |
| D | Risk Severity | 15 | Dropdown |
| E | Current Risk | 30 | Text |
| F | Proposed Remediation | 40 | Text |
| G | Estimated Effort (hours) | 15 | Number |
| H | Target Completion Date | 18 | Date |
| I | Assigned Owner | 20 | Text |
| J | Status | 15 | Dropdown |

**Row 4 Style:** Dark red header (8B0000), white text, bold, centered, text wrap

### Data Validation (Dropdowns)

**Column D: Risk Severity**

- 🔴 High (immediate remediation required)
- 🟡 Medium (remediation within 90 days)
- 🟢 Low (remediation within 180 days)
- ⚪ Info (awareness, no remediation)

**Column J: Status**

- 📋 Identified (not started)
- 🔄 In Progress (remediation underway)
- ✅ Remediated (completed, verified)
- ⏸️ On Hold (dependencies or approvals)
- ❌ Risk Accepted (executive decision to accept)

### Sample Data (Rows 5-10)

| Gap ID | Description | Policy Violated | Severity | Current Risk | Remediation | Effort | Target Date | Owner | Status |
|--------|-------------|-----------------|----------|--------------|-------------|--------|-------------|-------|--------|
| GAP-001 | Developer workstations can ping production database (firewall misconfiguration) | ISMS-POL-A.8.31, Section 2.1 | 🔴 High | Direct network access from dev to prod | Update firewall rule to DENY dev network → prod database | 2h | 2024-01-30 | Network Admin | 🔄 In Progress |
| GAP-002 | Production database password stored in application config file (not PAM vault) | ISMS-POL-A.8.31, Section 2.1 | 🔴 High | Credential exposure risk | Migrate to HashiCorp Vault, update app to retrieve from vault | 16h | 2024-02-28 | Security Eng | 📋 Identified |
| GAP-003 | Staging database has 15% configuration drift from production | ISMS-POL-A.8.31, Section 2.4 | 🔴 High | Testing doesn't validate production | Update Terraform config, apply to staging | 8h | 2024-02-15 | DevOps Lead | 📋 Identified |
| GAP-004 | No automated configuration drift detection | ISMS-POL-A.8.31, Section 2.4 | 🟡 Medium | Manual drift detection (inconsistent) | Implement AWS Config rules or Terraform drift check (scheduled) | 12h | 2024-03-15 | DevOps Lead | 📋 Identified |
| GAP-005 | Development environment uses namespace-level separation (not account-level) | ISMS-POL-A.8.31, Section 2.1 | 🟢 Low | Adequate but not strong separation | Evaluate separate AWS account for dev (cost/benefit) | 40h | 2024-06-30 | Cloud Architect | 📋 Identified |

### Gap Prioritization Matrix

| Severity | Definition | Remediation Timeline |
|----------|------------|---------------------|
| 🔴 High | Production access from dev/test, shared credentials, production data in dev/test | Immediate (within 30 days) |
| 🟡 Medium | Configuration drift >10%, weak separation mechanisms, missing monitoring | Within 90 days |
| 🟢 Low | Namespace-level separation (adequate but not strong), manual processes | Within 180 days |

**Evidence Required:**

- Gap identification documentation
- Risk assessment justification
- Remediation plan documentation
- Completion verification (before/after screenshots)

---

## Sheet 9: Evidence_Register

### Purpose
Central registry of all supporting evidence for audit traceability.

### Header Section (Rows 1-2)

- **Row 1 (Merged A1:H1):** "EVIDENCE REGISTER"
  - Style: Dark blue (003366), white text, bold, centered, 35px height
  
- **Row 2 (Merged A2:H2):** "Document ALL supporting evidence - organize in structured folder with descriptive filenames and dates"
  - Style: Light blue (B4C7E7), dark text, centered, 25px height

### Column Headers (Row 4)

| Column | Header | Width | Data Type |
|--------|--------|-------|-----------|
| A | Evidence ID | 12 | Text |
| B | Evidence Type | 20 | Dropdown |
| C | Description | 45 | Text |
| D | File Name | 35 | Text |
| E | Date Collected | 15 | Date |
| F | Related Requirement | 30 | Text |
| G | Related Sheet | 15 | Dropdown |
| H | File Location | 40 | Text |

**Row 4 Style:** Medium blue header (4472C4), white text, bold, centered, text wrap

### Data Validation (Dropdowns)

**Column B: Evidence Type**

- Network Diagram
- Firewall Export
- Screenshot
- Configuration Export
- Inventory Report
- Penetration Test Report
- Scan Results
- Policy Document
- Approval Record
- Other

**Column G: Related Sheet**

- Sheet 2: Environment_Inventory
- Sheet 3: Network_Separation
- Sheet 4: Infrastructure_Separation
- Sheet 5: Data_Separation
- Sheet 6: Credential_Separation
- Sheet 7: Configuration_Consistency
- Sheet 8: Gap_Analysis
- Multiple Sheets

### Sample Data (Rows 5-15)

| Evidence ID | Type | Description | File Name | Date | Related Requirement | Sheet | Location |
|-------------|------|-------------|-----------|------|---------------------|-------|----------|
| EVD-001 | Network Diagram | Complete network architecture showing VLAN segmentation | network-architecture-2024-01.pdf | 2024-01-15 | ISMS-POL-A.8.31, Section 2.1 | Sheet 3 | ./evidence/EVD-001/ |
| EVD-002 | Firewall Export | Firewall rules demonstrating default deny between environments | firewall-rules-export-2024-01.txt | 2024-01-15 | ISMS-POL-A.8.31, Section 2.1 | Sheet 3 | ./evidence/EVD-002/ |
| EVD-003 | Screenshot | AWS Organizations showing separate accounts per environment | aws-accounts-screenshot-2024-01.png | 2024-01-15 | ISMS-POL-A.8.31, Section 2.1 | Sheet 4 | ./evidence/EVD-003/ |
| EVD-004 | Inventory Report | RDS instance list showing separate instances per environment | rds-instance-list-2024-01.csv | 2024-01-15 | ISMS-POL-A.8.31, Section 2.1 | Sheet 4 | ./evidence/EVD-004/ |
| EVD-005 | Screenshot | HashiCorp Vault configuration showing production credentials stored | vault-config-screenshot-2024-01.png | 2024-01-16 | ISMS-POL-A.8.31, Section 2.1 | Sheet 6 | ./evidence/EVD-005/ |
| EVD-006 | Penetration Test | Network isolation testing results | pentest-report-network-isolation-2024-01.pdf | 2024-01-18 | ISMS-POL-A.8.31, Section 2.1 | Sheet 3 | ./evidence/EVD-006/ |
| EVD-007 | Scan Results | Data discovery scan confirming no production data in dev/test | data-discovery-scan-2024-01.pdf | 2024-01-19 | ISMS-POL-A.8.31, Section 2.3 | Sheet 5 | ./evidence/EVD-007/ |
| EVD-008 | Configuration Export | Terraform configuration files for all environments | terraform-configs-2024-01.zip | 2024-01-20 | ISMS-POL-A.8.31, Section 2.4 | Sheet 7 | ./evidence/EVD-008/ |
| EVD-009 | Configuration Export | Terraform drift detection output (staging vs production) | terraform-plan-drift-2024-01.txt | 2024-01-20 | ISMS-POL-A.8.31, Section 2.4 | Sheet 7 | ./evidence/EVD-009/ |
| EVD-010 | Approval Record | Environment separation assessment approval signatures | assessment-approval-2024-01.pdf | 2024-01-25 | ISO 27001 audit requirement | Multiple | ./evidence/EVD-010/ |

### Evidence Organization Best Practices

**Folder Structure:**
```
evidence/
├── EVD-001-network-architecture-2024-01.pdf
├── EVD-002-firewall-rules-export-2024-01.txt
├── EVD-003-aws-accounts-screenshot-2024-01.png
├── EVD-004-rds-instance-list-2024-01.csv
├── EVD-005-vault-config-screenshot-2024-01.png
├── EVD-006-pentest-report-2024-01.pdf
├── EVD-007-data-discovery-scan-2024-01.pdf
├── EVD-008-terraform-configs-2024-01.zip
├── EVD-009-terraform-plan-drift-2024-01.txt
└── EVD-010-assessment-approval-2024-01.pdf
```

**File Naming Convention:**
`[Evidence-ID]-[description]-[YYYY-MM].[extension]`

**Evidence Quality Checklist:**

- [ ] Time-stamped (date visible in file or filename)
- [ ] Descriptive filename (not "screenshot.png")
- [ ] Organized in evidence folder
- [ ] Accessible to reviewers/auditors
- [ ] Supports specific requirement

---

## Sheet 10: Approval_Sign_Off

### Purpose
Multi-level approval workflow and formal sign-off for the assessment.

### Header Section (Rows 1-2)

- **Row 1 (Merged A1:F1):** "APPROVAL & SIGN-OFF"
  - Style: Dark blue (003366), white text, bold, centered, 35px height

- **Row 2 (Merged A2:F2):** "Formal approval workflow - Assessment requires three-level approval before finalization"
  - Style: Light blue (B4C7E7), dark text, centered, 25px height

### Assessment Summary (Rows 4-10)

| Row | Attribute | Value |
|-----|-----------|-------|
| 4 | Assessment ID: | ISMS-IMP-A.8.31.1 |
| 5 | Assessment Name: | Environment Architecture Assessment |
| 6 | Assessment Date: | [From Sheet 1] |
| 7 | Completed By: | [From Sheet 1] |
| 8 | Total Environments Assessed: | [Count from Sheet 2] |
| 9 | Total Gaps Identified: | [Count from Sheet 8] |
| 10 | Overall Compliance Status: | [Summary status] |

### Approval Workflow (Rows 12-25)

**Level 1: Technical Review (Rows 14-17)**

| Column | Header | Width | Data Type |
|--------|--------|-------|-----------|
| A | Reviewer Role | 25 | Text |
| B | Reviewer Name | 25 | Text (user input) |
| C | Review Date | 15 | Date (user input) |
| D | Decision | 15 | Dropdown |
| E | Comments | 50 | Text (user input) |
| F | Signature | 20 | Text (user input) |

**Dropdown for Decision:**
- Approved
- Approved with Comments
- Request Changes
- Rejected

**Level 1 Reviewers:**
| Role | Name | Date | Decision | Comments | Signature |
|------|------|------|----------|----------|-----------|
| IT Operations Manager | [User Input] | [User Input] | [Dropdown] | [User Input] | [User Input] |
| Cloud Architect | [User Input] | [User Input] | [Dropdown] | [User Input] | [User Input] |

**Level 2: Security Review (Rows 19-21)**

| Role | Name | Date | Decision | Comments | Signature |
|------|------|------|----------|----------|-----------|
| Information Security Manager | [User Input] | [User Input] | [Dropdown] | [User Input] | [User Input] |
| CISO | [User Input] | [User Input] | [Dropdown] | [User Input] | [User Input] |

**Level 3: Executive Approval (Rows 23-25)**

| Role | Name | Date | Decision | Comments | Signature |
|------|------|------|----------|----------|-----------|
| CTO / VP Engineering | [User Input] | [User Input] | [Dropdown] | [User Input] | [User Input] |

### Approval Status Summary (Rows 27-30)

| Metric | Value | Status |
|--------|-------|--------|
| Level 1 (Technical) Status | [Auto-calculated] | [✅/⚠️/❌] |
| Level 2 (Security) Status | [Auto-calculated] | [✅/⚠️/❌] |
| Level 3 (Executive) Status | [Auto-calculated] | [✅/⚠️/❌] |
| **Overall Approval Status** | [Auto-calculated] | [✅ Approved / ⚠️ Pending / ❌ Not Approved] |

### Conditional Approval Notes (Rows 32-38)

**Row 32:** "Conditional Approval Notes" (bold, underlined)

**Rows 33-38:** User input text area (yellow fill)
- Document any conditions attached to approval
- Document required follow-up actions
- Document timeline for conditional requirements

### Next Assessment Date (Rows 40-42)

| Attribute | Value |
|-----------|-------|
| Next Scheduled Assessment: | [User Input: Date] |
| Assessment Frequency: | Quarterly |
| Trigger-Based Review: | After major infrastructure changes |

---

## Cell Styling Reference

### Color Codes

| Style | Background | Font Color | Usage |
|-------|------------|------------|-------|
| Header (dark blue) | #003366 | White (#FFFFFF) | Sheet titles, major headers |
| Header (medium blue) | #4472C4 | White (#FFFFFF) | Column headers |
| Subheader (light blue) | #B4C7E7 | Dark (#000000) | Sheet instructions |
| User Input | #FFEB9C (yellow) | Dark (#000000) | Cells user must complete |
| Compliant | #C6EFCE (green) | Dark (#000000) | ✅ status |
| Partial | #FFEB9C (yellow) | Dark (#000000) | ⚠️ status |
| Non-Compliant | #FFC7CE (red) | Dark (#000000) | ❌ status |
| Planned | #B4C7E7 (blue) | Dark (#000000) | 📋 status |
| Read-Only | #D9D9D9 (gray) | Dark (#000000) | Calculated or locked cells |

### Font Styles

| Element | Font | Size | Weight | Alignment |
|---------|------|------|--------|-----------|
| Sheet Title (Row 1) | Calibri | 18pt | Bold | Center |
| Subtitle (Row 2) | Calibri | 12pt | Regular | Center |
| Column Headers | Calibri | 11pt | Bold | Center |
| Data Cells | Calibri | 10pt | Regular | Left |
| User Input | Calibri | 10pt | Bold | Left |

### Border Styles

- **Headers:** Thick bottom border (#003366)
- **Column headers:** Medium border all sides (#4472C4)
- **Data rows:** Thin border all sides (#D9D9D9)
- **Section separators:** Medium border top (#000000)

---

## Integration Points

### Input from Other Assessments

**None** - This is the first assessment in the A.8.31 series.

### Output to Other Assessments

**To ISMS-IMP-A.8.31.2 (Access Control):**

- Environment list from Sheet 2 (Environment_Inventory)
- Required for access control matrix

**To ISMS-IMP-A.8.31.3 (Compliance Dashboard):**

- All gap data from Sheet 8 (Gap_Analysis)
- Compliance status from all sheets
- Required for consolidated compliance scoring

### Output to Python Scripts

**generate_a831_1_environment_architecture.py** generates this workbook:

- Creates all 9 sheets with proper structure
- Applies cell styling and data validation
- Includes sample data for reference
- Exports to `.xlsx` format

---

## Workbook Metadata

**File Name:** `A831-1-Environment-Architecture-Assessment-YYYY-MM-DD.xlsx`

**Properties:**

- Title: ISMS-IMP-A.8.31.1 - Environment Architecture Assessment
- Subject: ISO/IEC 27001:2022 Control A.8.31
- Author: [Organization] ISMS Team
- Comments: Technology-agnostic environment separation assessment
- Keywords: ISO27001, A.8.31, environment separation, SDLC, dev/test/prod

**Protection:**

- Sheet structure protected (prevent accidental deletion)
- User input cells unlocked (yellow cells editable)
- Formula cells locked
- Header rows locked

---

**END OF SPECIFICATION**

---

*"The security of a cryptographic system lies entirely in the key."*
— Ron Rivest

<!-- QA_VERIFIED: 2026-02-06 -->
