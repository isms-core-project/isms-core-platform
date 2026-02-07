**ISMS-IMP-A.8.31.1-UG - Environment Architecture Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.31: Separation of Development, Test and Production Environments

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.31.1-UG |
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

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.8.31.1-TG.

---

## Assessment Overview

### Purpose & Scope

**Assessment Name:** ISMS-IMP-A.8.31.1 - Environment Architecture Assessment

#### What This Assessment Covers

This assessment documents the ARCHITECTURE and SEPARATION MECHANISMS for your development, test, staging, and production environments. This is the foundational "HOW are environments separated?" assessment that answers:

- What environments exist? (dev, test, staging, production)
- How are environments separated? (network, infrastructure, data, credentials)
- What separation mechanisms are deployed? (VLANs, cloud accounts, firewall rules)
- Are environments properly isolated from each other?
- What gaps exist between deployed architecture and policy requirements?

#### Key Principle

This assessment is **completely technology-agnostic and platform-independent**. You document YOUR specific infrastructure (whether on-premises VLANs, AWS multi-account, Azure subscriptions, Kubernetes namespaces, or hybrid), and verify separation against generic policy requirements.

#### What You'll Document

- Every environment tier in your SDLC (dev, test, staging, prod)
- Network separation mechanisms (VLANs, VPCs, firewall rules)
- Infrastructure separation (separate servers, cloud accounts, databases)
- Data separation (production data never in dev/test)
- Credential separation (unique per environment, production in PAM)
- Configuration consistency (staging mirrors production)
- Separation compliance gaps and remediation plans
- Supporting evidence for audit

#### How This Relates to Other A.8.31 Assessments

| Assessment            | Focus                      | Relationship to A.8.31.1                |
|-----------------------|----------------------------|-----------------------------------------|
| **ISMS-IMP-A.8.31.1** | **Architecture**           | **HOW environments are separated**      |
| ISMS-IMP-A.8.31.2     | Access Control             | WHO can access WHICH environment        |
| ISMS-IMP-A.8.31.3     | Compliance Dashboard       | Consolidated view across architecture + access |

This assessment (A.8.31.1) MUST be completed first - you can't assess access control compliance until you know what environment architecture exists!

### Who Should Complete This Assessment

#### Primary Stakeholders

1. **IT Operations** - Infrastructure deployment, environment management
2. **Cloud Architects** - Multi-account/subscription architecture
3. **Network Engineers** - VLAN segmentation, firewall rules
4. **DevOps Engineers** - CI/CD pipeline, deployment architecture
5. **Security Engineers** - Separation verification, penetration testing
6. **Database Administrators** - Database separation, data handling

#### Required Skills

- Understanding of network architecture (VLANs, VPCs, firewall rules)
- Familiarity with deployed infrastructure (on-prem, AWS, Azure, GCP, Kubernetes)
- Knowledge of environment separation concepts
- Access to infrastructure admin consoles
- Understanding of data classification and handling

#### Time Commitment

- **Initial assessment:** 8-12 hours per application/system (for comprehensive architecture review)
- **Quarterly updates:** 2-3 hours per system (update configurations, verify separation)

### Expected Outputs

Upon completion, you will have:

1. ✅ **Complete environment inventory** - All environments documented (dev, test, staging, prod)
2. ✅ **Network separation documentation** - VLANs, VPCs, subnets, firewall rules
3. ✅ **Infrastructure separation matrix** - Separate compute, storage, databases per environment
4. ✅ **Data separation verification** - Confirmed NO production data in dev/test
5. ✅ **Credential separation tracking** - Unique credentials per environment, production in PAM
6. ✅ **Configuration consistency** - Staging mirrors production configuration
7. ✅ **Separation gap analysis** - Identified gaps with remediation plans
8. ✅ **Evidence register** - Supporting documentation for audit
9. ✅ **Approved assessment** - Multi-level approval workflow completed

---

## Prerequisites

### Information You'll Need

Before starting this assessment, gather:

#### 1. Infrastructure Access

- Administrator access to all environment infrastructures
- Access to cloud management consoles (AWS, Azure, GCP)
- Access to network infrastructure (firewall, router configs)
- Access to virtualization platforms (VMware, Hyper-V, Kubernetes)
- Database admin access (for database instance inventory)

#### 2. Documentation

- Current network architecture diagrams
- Cloud account/subscription structure
- VLAN assignment documentation
- Firewall rule documentation
- Infrastructure as Code (IaC) configurations (Terraform, CloudFormation, ARM templates)

#### 3. Configuration Data

- Firewall rule exports
- Cloud account/subscription list
- VPC/VNet configuration exports
- Kubernetes namespace configurations
- Database instance inventory
- Secret management system inventory (PAM vault, HashiCorp Vault, etc.)

#### 4. Policy Requirements

- ISMS-POL-A.8.31, Section 2.1 (Environment Architecture Requirements)
- ISMS-POL-A.8.31, Section 2.3 (Data Handling Requirements)
- ISMS-POL-A.8.31, Section 2.4 (Environment Promotion Requirements)
- ISMS-POL-00 (Regulatory Applicability Framework)

### Required Tools

- Microsoft Excel (2016 or later) for workbook completion
- Access to cloud management consoles
- Network diagram tools (Visio, Lucidchart, draw.io)
- CLI tools (AWS CLI, Azure CLI, gcloud, kubectl)
- Screen capture tools (for evidence screenshots)
- Firewall/network scanner (optional, for verification testing)

### Dependencies

This assessment has NO dependencies - it's the first assessment in the A.8.31 series and must be completed before others.

However, outputs from this assessment are INPUT to:

- A.8.31.2 (Access Control) - Needs environment list from Sheet 1
- A.8.31.3 (Compliance Dashboard) - Consolidates architecture + access data

---

## Workflow

### High-Level Process

```
1. PREPARE
   ↓
2. INVENTORY ENVIRONMENTS (Sheet 1)
   ↓
3. DOCUMENT NETWORK SEPARATION (Sheet 2)
   ↓
4. DOCUMENT INFRASTRUCTURE SEPARATION (Sheet 3)
   ↓
5. VERIFY DATA SEPARATION (Sheet 4)
   ↓
6. VERIFY CREDENTIAL SEPARATION (Sheet 5)
   ↓
7. ASSESS CONFIGURATION CONSISTENCY (Sheet 6)
   ↓
8. IDENTIFY GAPS (Sheet 7)
   ↓
9. COLLECT EVIDENCE (Sheet 8)
   ↓
10. REVIEW & APPROVE
   ↓
11. MAINTAIN & UPDATE
```

### Detailed Workflow

#### Phase 1: Preparation (30-60 minutes)

**Activities:**

- Gather all prerequisite information
- Obtain necessary infrastructure access
- Review policy requirements (ISMS-POL-A.8.31, Section 2.1)
- Identify team members to involve
- Schedule assessment completion timeline

**Outputs:**

- Assessment team identified
- Access credentials obtained
- Documentation collected
- Timeline established

#### Phase 2: Environment Inventory (1-2 hours)

**Activities:**

- Complete Sheet 1: Environment Inventory
- Document every environment tier (dev, test, staging, prod)
- Identify all applications/systems in scope
- Define environment purpose and characteristics
- Document environment naming conventions

**Outputs:**

- Complete environment inventory
- Environment tier definitions
- Naming convention documentation

**Common Pitfalls to Avoid:**

- ❌ Forgetting "shadow" environments (developer sandbox, hotfix)
- ❌ Not documenting decommissioned environments (security risk)
- ❌ Inconsistent naming (prod1, production, live-app)

#### Phase 3: Network Separation Assessment (2-3 hours)

**Activities:**

- Complete Sheet 2: Network Separation
- Document VLANs, VPCs, subnets per environment
- Export firewall rules showing inter-environment blocking
- Verify default deny between environments
- Document allowed cross-environment traffic (monitoring, CI/CD)

**Outputs:**

- Network segmentation matrix
- Firewall rule documentation
- Network isolation verification results

**Common Pitfalls to Avoid:**

- ❌ Assuming firewall rules are correct without verification
- ❌ Missing allowed exceptions (monitoring, backup, CI/CD)
- ❌ Not testing actual network isolation

#### Phase 4: Infrastructure Separation Assessment (2-3 hours)

**Activities:**

- Complete Sheet 3: Infrastructure Separation
- Document compute resources per environment (servers, VMs, containers)
- Document cloud accounts/subscriptions per environment
- Document database separation (separate instances per environment)
- Document storage separation (S3 buckets, file shares)

**Outputs:**

- Infrastructure inventory matrix
- Cloud account/subscription structure
- Database instance inventory
- Storage separation documentation

**Common Pitfalls to Avoid:**

- ❌ Shared database instances with logical separation only (weak)
- ❌ Missing backup/DR infrastructure separation
- ❌ Shared storage buckets across environments

#### Phase 5: Data Separation Verification (1-2 hours)

**Activities:**

- Complete Sheet 4: Data Separation
- Verify NO production data in development environments
- Verify NO production data in testing environments
- Document data anonymization procedures (if used in test)
- Document synthetic data generation (if used in test)

**Outputs:**

- Data separation compliance matrix
- Data anonymization documentation
- Production data leak verification

**Common Pitfalls to Avoid:**

- ❌ Production database dumps in dev/test (MAJOR VIOLATION)
- ❌ Production backups used for testing
- ❌ Production API keys in dev configuration files

#### Phase 6: Credential Separation Verification (1-2 hours)

**Activities:**

- Complete Sheet 5: Credential Separation
- Verify unique credentials per environment
- Verify production credentials stored in PAM vault (NOT in code)
- Verify no shared credentials between environments
- Document secret management system

**Outputs:**

- Credential inventory per environment
- PAM vault documentation
- Shared credential violations identified

**Common Pitfalls to Avoid:**

- ❌ Same database password in dev and production (MAJOR VIOLATION)
- ❌ Production API keys hardcoded in application code
- ❌ Shared service accounts across environments

#### Phase 7: Configuration Consistency Assessment (1-2 hours)

**Activities:**

- Complete Sheet 6: Configuration Consistency
- Compare staging configuration to production
- Measure configuration drift
- Verify Infrastructure as Code (IaC) usage
- Document configuration management process

**Outputs:**

- Configuration drift report
- IaC compliance assessment
- Configuration management documentation

**Common Pitfalls to Avoid:**

- ❌ Significant drift between staging and production (>10%)
- ❌ Manual changes to production not reflected in IaC
- ❌ No automated drift detection

#### Phase 8: Gap Analysis (1-2 hours)

**Activities:**

- Complete Sheet 7: Gap Analysis
- Review all previous sheets for non-compliance
- Document each gap with severity rating
- Propose remediation for each gap
- Estimate remediation effort and timeline

**Outputs:**

- Comprehensive gap analysis
- Risk-prioritized remediation plan
- Timeline for gap closure

#### Phase 9: Evidence Collection (1-2 hours)

**Activities:**

- Complete Sheet 8: Evidence Register
- Collect network diagrams
- Export firewall rules
- Screenshot cloud account structure
- Export database instance lists
- Document PAM vault configuration

**Outputs:**

- Complete evidence package
- Audit-ready documentation

#### Phase 10: Review & Approval (variable)

**Activities:**

- Internal team review
- IT Operations Manager approval
- Cloud Architect approval
- CISO approval

**Outputs:**

- Approved assessment
- Action items assigned

#### Phase 11: Maintenance (ongoing)

**Activities:**

- Quarterly assessment updates
- Update after infrastructure changes
- Track gap remediation progress
- Monitor continuous compliance

**Outputs:**

- Up-to-date assessment
- Compliance trend analysis

---

## Completing Each Sheet

### Sheet 1: Instructions & Legend

**What to do:**
1. Fill in assessment metadata (date, completed by, organization)
2. Review the status legend
3. Review acceptable evidence examples
4. Understand the workflow

**Time:** 5-10 minutes

**Tips:**

- Use current date for "Assessment Date"
- Include your name and role for "Completed By"
- Read the full instructions before starting

---

### Sheet 2: Environment Inventory

**What to do:**
1. List every environment tier (dev, test, staging, prod)
2. For each environment, document:

   - Environment name
   - Purpose (what it's used for)
   - Primary users (who accesses it)
   - Data type (synthetic, anonymized, production)
   - Availability target (SLA)
   - Status (deployed, planned, decommissioned)

**Time:** 30-60 minutes

**Tips:**

- Include ALL environments, even temporary ones
- Document shadow environments (developer sandboxes)
- Use consistent naming convention
- Note decommissioned environments (for historical audit trail)

**Example Entry:**
| Environment | Purpose | Primary Users | Data Type | Availability | Status |
|-------------|---------|---------------|-----------|--------------|--------|
| Production | Live customer operations | Operations team | Production data | 99.9% | ✅ Deployed |
| Staging | Pre-production validation | Ops + Senior Devs | Anonymized | 99% | ✅ Deployed |
| Testing | QA, UAT | QA team, business users | Synthetic | 95% business hours | ✅ Deployed |
| Development | Active code development | Developers, DevOps | Synthetic only | Best effort | ✅ Deployed |

---

### Sheet 3: Network Separation

**What to do:**
1. Document network segmentation per environment
2. For on-premises: VLAN assignments, subnets
3. For cloud: VPC/VNet per environment
4. Document firewall rules preventing cross-environment access
5. Document allowed exceptions (monitoring, CI/CD, backup)

**Time:** 2-3 hours

**Tips:**

- Export actual firewall rules (don't assume they're correct)
- Test network isolation (ping, telnet from dev to prod should FAIL)
- Document ALL allowed exceptions with business justification
- Use network diagrams as supporting evidence

**Example Entry:**
| Environment | Network Segment | VLAN/VPC | Firewall Rules | Allowed From | Evidence |
|-------------|-----------------|----------|----------------|--------------|----------|
| Production | 10.400.0.0/16 | VLAN 400 / vpc-prod-main | Default DENY from all other environments | Monitoring (10.250.10.5), CI/CD (10.250.20.10) | firewall-rules-export-2024-01.pdf |
| Staging | 10.300.0.0/16 | VLAN 300 / vpc-staging-main | Default DENY from dev/test | Monitoring, CI/CD | firewall-rules-export-2024-01.pdf |
| Testing | 10.200.0.0/16 | VLAN 200 / vpc-test-main | Default DENY from dev/prod | Monitoring only | firewall-rules-export-2024-01.pdf |
| Development | 10.100.0.0/16 | VLAN 100 / vpc-dev-main | Default DENY from test/staging/prod | None | firewall-rules-export-2024-01.pdf |

---

### Sheet 4: Infrastructure Separation

**What to do:**
1. Document compute resources per environment
2. Document cloud accounts/subscriptions per environment
3. Document database instances per environment
4. Document storage separation
5. Verify NO shared infrastructure between environments

**Time:** 2-3 hours

**Tips:**

- For cloud: Separate AWS accounts or Azure subscriptions = STRONG separation
- For on-premises: Separate physical/virtual servers per environment
- Check for shared database instances (WEAK separation)
- Verify backup infrastructure is also separated

**Example Entry:**
| Environment | Compute | Cloud Account | Database | Storage | Separation Quality |
|-------------|---------|---------------|----------|---------|-------------------|
| Production | 10 VMs (dedicated hosts) | AWS account 444444444444 | RDS prod-db-01 (separate instance) | S3 bucket: myorg-prod-data | ✅ Strong (account-level) |
| Staging | 5 VMs (shared hardware) | AWS account 333333333333 | RDS staging-db-01 (separate instance) | S3 bucket: myorg-staging-data | ✅ Strong (account-level) |
| Testing | 3 VMs (shared hardware) | AWS account 222222222222 | RDS test-db-01 (separate instance) | S3 bucket: myorg-test-data | ✅ Strong (account-level) |
| Development | Docker containers (shared K8s) | AWS account 111111111111 | PostgreSQL dev-db (separate instance) | S3 bucket: myorg-dev-data | ✅ Adequate (namespace-level) |

---

### Sheet 5: Data Separation

**What to do:**
1. Verify NO production data in development
2. Verify NO production data in testing
3. Document data anonymization procedures (if used)
4. Document synthetic data generation
5. Document any violations and remediation

**Time:** 1-2 hours

**Tips:**

- This is a CRITICAL compliance requirement
- Production database dumps in dev/test = MAJOR VIOLATION
- Use data discovery tools to scan for production data
- Document data anonymization technique (if used in test)

**Example Entry:**
| Environment | Production Data Present? | Data Type | Anonymization Used? | Violations | Evidence |
|-------------|-------------------------|-----------|---------------------|------------|----------|
| Production | ✅ Yes (authorized) | Real production data | N/A | None | N/A |
| Staging | ❌ No | Anonymized production subset | ✅ Yes (k-anonymity=5) | None | data-anonymization-procedure.pdf |
| Testing | ❌ No | Synthetic test data | N/A | None | synthetic-data-generator-config.yaml |
| Development | ❌ No | Synthetic test data | N/A | None | dev-database-schema.sql |

**CRITICAL VIOLATIONS TO DOCUMENT:**

- ❌ Production database dumps restored to dev/test
- ❌ Production API keys in dev configuration
- ❌ Production customer data used for testing

---

### Sheet 6: Credential Separation

**What to do:**
1. Document credentials per environment
2. Verify unique credentials per environment (NO sharing)
3. Verify production credentials in PAM vault
4. Document secret management system
5. Identify any shared credentials (VIOLATION)

**Time:** 1-2 hours

**Tips:**

- Same password in dev and prod = MAJOR VIOLATION
- Production credentials must be in PAM vault (NOT in code, config files, environment variables)
- Check application code for hardcoded credentials
- Verify secret rotation policies

**Example Entry:**
| Credential Type | Dev | Test | Staging | Production | Shared? | Prod in PAM? | Evidence |
|-----------------|-----|------|---------|------------|---------|--------------|----------|
| Database password | dev_db_pass_xyz | test_db_pass_abc | staging_db_pass_def | [IN VAULT] | ❌ No (unique per env) | ✅ Yes | pam-vault-screenshot.png |
| API keys (3rd party) | dev_api_key_123 | test_api_key_456 | staging_api_key_789 | [IN VAULT] | ❌ No (unique per env) | ✅ Yes | pam-vault-screenshot.png |
| Service account | dev_svc@example.com | test_svc@example.com | staging_svc@example.com | prod_svc@example.com | ❌ No (unique per env) | ✅ Yes | iam-policy-export.json |

**CRITICAL VIOLATIONS TO DOCUMENT:**

- ❌ Same database password used in dev and production
- ❌ Production API keys hardcoded in application code
- ❌ Production credentials in environment variables (not PAM vault)

---

### Sheet 7: Configuration Consistency

**What to do:**
1. Compare staging configuration to production
2. Measure configuration drift percentage
3. Verify Infrastructure as Code (IaC) usage
4. Document configuration management process
5. Identify areas where staging doesn't mirror production

**Time:** 1-2 hours

**Tips:**

- Staging should mirror production configuration (≤5% drift)
- Use IaC (Terraform, CloudFormation) to enforce consistency
- Detect drift with automated tools (terraform plan, AWS Config)
- Document intentional differences (e.g., smaller instance sizes in staging)

**Example Entry:**
| Configuration Item | Production | Staging | Match? | Drift % | IaC Managed? | Evidence |
|--------------------|------------|---------|--------|---------|--------------|----------|
| Instance type | t3.xlarge | t3.large | ⚠️ Partial (intentional cost optimization) | N/A | ✅ Yes (Terraform) | main.tf |
| Security group rules | sg-prod-app (22 rules) | sg-staging-app (22 rules) | ✅ Yes | 0% | ✅ Yes (Terraform) | terraform-plan-output.txt |
| Database version | PostgreSQL 15.4 | PostgreSQL 15.4 | ✅ Yes | 0% | ✅ Yes (Terraform) | terraform-plan-output.txt |
| Application config | app-config-v2.3 | app-config-v2.2 | ❌ No (staging outdated) | 5% | ⚠️ Partial | FINDING: Update staging to v2.3 |

---

### Sheet 8: Gap Analysis

**What to do:**
1. Review all previous sheets
2. Identify any non-compliance with policy requirements
3. Document each gap with:

   - Description of gap
   - Policy requirement violated
   - Risk severity (High/Medium/Low)
   - Proposed remediation
   - Estimated effort
   - Target completion date

4. Prioritize gaps by risk severity

**Time:** 1-2 hours

**Tips:**

- Be honest about gaps (audit will find them anyway)
- Prioritize High severity gaps first
- Provide realistic remediation timelines
- Include compensating controls if remediation delayed

**Example Entry:**
| Gap ID | Description | Policy Violated | Severity | Remediation | Effort | Target Date | Owner |
|--------|-------------|-----------------|----------|-------------|--------|-------------|-------|
| GAP-001 | Staging database has 15% configuration drift from production | ISMS-POL-A.8.31, Section 2.4 | 🔴 High | Update Terraform to match prod, apply to staging | 8 hours | 2024-02-15 | DevOps Lead |
| GAP-002 | Developer workstations can ping production database (firewall misconfiguration) | ISMS-POL-A.8.31, Section 2.1 | 🔴 High | Update firewall rule to DENY dev network → prod database | 2 hours | 2024-01-30 | Network Admin |
| GAP-003 | Production database password stored in application config file (not PAM vault) | ISMS-POL-A.8.31, Section 2.1 | 🔴 High | Migrate to HashiCorp Vault, update app to retrieve from vault | 16 hours | 2024-02-28 | Security Eng |
| GAP-004 | No automated configuration drift detection between staging and production | ISMS-POL-A.8.31, Section 2.4 | 🟡 Medium | Implement AWS Config rules or terraform drift detection | 12 hours | 2024-03-15 | DevOps Lead |

---

### Sheet 9: Evidence Register

**What to do:**
1. Document all supporting evidence
2. For each evidence item, record:

   - Evidence type (diagram, export, screenshot, report)
   - Description
   - File name/location
   - Date collected
   - Related requirement

3. Attach evidence files or provide accessible links

**Time:** 1-2 hours

**Tips:**

- Organize evidence in a shared folder
- Use descriptive file names (network-diagram-2024-01.pdf, not diagram.pdf)
- Include date in file names for version control
- Screenshot cloud console views with timestamp visible

**Example Entry:**
| Evidence ID | Type | Description | File Name | Date | Related Requirement | Location |
|-------------|------|-------------|-----------|------|---------------------|----------|
| EVD-001 | Network Diagram | Complete network architecture showing VLAN segmentation | network-architecture-2024-01.pdf | 2024-01-15 | ISMS-POL-A.8.31, Section 2.1 | ./evidence/EVD-001/ |
| EVD-002 | Firewall Export | Firewall rules showing default deny between environments | firewall-rules-export-2024-01.txt | 2024-01-15 | ISMS-POL-A.8.31, Section 2.1 | ./evidence/EVD-002/ |
| EVD-003 | Screenshot | AWS Organizations showing separate accounts per environment | aws-accounts-screenshot-2024-01.png | 2024-01-15 | ISMS-POL-A.8.31, Section 2.1 | ./evidence/EVD-003/ |
| EVD-004 | Database Inventory | RDS instance list showing separate instances per environment | rds-instance-list-2024-01.csv | 2024-01-15 | ISMS-POL-A.8.31, Section 2.1 | ./evidence/EVD-004/ |
| EVD-005 | PAM Vault Config | HashiCorp Vault configuration showing production credentials | vault-config-screenshot-2024-01.png | 2024-01-16 | ISMS-POL-A.8.31, Section 2.1 | ./evidence/EVD-005/ |
| EVD-006 | Penetration Test | Network isolation test results | pentest-report-2024-01.pdf | 2024-01-18 | ISMS-POL-A.8.31, Section 2.1 | ./evidence/EVD-006/ |

---

## Evidence Collection

### Required Evidence Types

| Requirement Area | Evidence Type | Examples | How to Collect |
|------------------|---------------|----------|----------------|
| **Network Separation** | Network diagrams, firewall exports | VLAN configuration, VPC architecture, firewall rules | Export from firewall admin console, create diagram in Visio/Lucidchart |
| **Infrastructure Separation** | Cloud inventory, server list | AWS account list, VM inventory, Kubernetes namespace list | AWS CLI: `aws organizations list-accounts`, `kubectl get namespaces` |
| **Data Separation** | Database inventory, data scan results | Database instance list, data discovery scan | `aws rds describe-db-instances`, data discovery tool report |
| **Credential Separation** | PAM vault config, credential inventory | HashiCorp Vault policy, AWS Secrets Manager inventory | Screenshot vault configuration, export secret list |
| **Configuration Consistency** | IaC configuration, drift reports | Terraform state, CloudFormation templates | `terraform plan` output, AWS Config compliance report |

### Evidence Quality Standards

**Good Evidence:**

- ✅ Time-stamped (shows when collected)
- ✅ Attributed (who collected it)
- ✅ Verifiable (auditor can reproduce)
- ✅ Complete (covers all requirements)
- ✅ Organized (easy to find and review)

**Poor Evidence:**

- ❌ Undated screenshots
- ❌ Unclear what it demonstrates
- ❌ Missing context
- ❌ Can't be verified

### Evidence Collection Tips

**Network Diagrams:**
```bash
# Create network diagram showing:
# - VLAN/VPC per environment
# - Firewall placement
# - Allowed/denied traffic flows
# - IP address ranges per environment
# Tools: Visio, Lucidchart, draw.io
```

**Firewall Rule Export:**
```bash
# Export firewall rules to text file
# Example (iptables):
sudo iptables-save > firewall-rules-export-2024-01.txt

# Example (AWS Security Groups):
aws ec2 describe-security-groups --region us-east-1 > sg-export-2024-01.json

# Include date in filename for version control
```

**Cloud Account Structure:**
```bash
# AWS - List all accounts in organization
aws organizations list-accounts --output table > aws-accounts-2024-01.txt

# Azure - List all subscriptions
az account list --output table > azure-subscriptions-2024-01.txt

# GCP - List all projects
gcloud projects list > gcp-projects-2024-01.txt
```

**Database Instance Inventory:**
```bash
# AWS RDS
aws rds describe-db-instances --query 'DBInstances[*].[DBInstanceIdentifier,Engine,EngineVersion,DBInstanceStatus]' --output table

# Azure SQL
az sql db list --output table

# GCP Cloud SQL
gcloud sql instances list
```

**PAM Vault Configuration:**
```bash
# HashiCorp Vault - List secrets (metadata only, not values!)
vault kv list secret/prod/

# Screenshot vault UI showing:
# - Production credentials stored
# - Access policies
# - Audit logging enabled
```

---

## Common Pitfalls

### Pitfall 1: Incomplete Environment Inventory

**Problem:** Missing shadow environments, developer sandboxes, or decommissioned environments

**Impact:** Audit finding, incomplete security posture

**Solution:**

- Survey all teams for undocumented environments
- Check cloud account/subscription list for orphaned accounts
- Include decommissioned environments (mark as "Decommissioned" but document them)

---

### Pitfall 2: Assuming Firewall Rules Are Correct

**Problem:** Documenting firewall rules from outdated documentation without verification

**Impact:** False sense of security, audit finding if rules don't match documentation

**Solution:**

- Export ACTUAL firewall rules from devices
- Test network isolation (ping/telnet from dev to prod should FAIL)
- Schedule penetration testing to verify isolation

---

### Pitfall 3: Missing Production Data in Dev/Test

**Problem:** Production database dumps in development/testing environments

**Impact:** MAJOR compliance violation, data breach risk, regulatory penalty

**Solution:**

- Use data discovery tools to scan dev/test environments
- Implement data anonymization for any production data used in test
- Strictly prohibit production database dumps in dev/test
- Generate synthetic test data instead

---

### Pitfall 4: Shared Credentials Between Environments

**Problem:** Same database password used in dev and production

**Impact:** MAJOR security vulnerability, audit finding

**Solution:**

- Generate unique credentials per environment
- Store production credentials in PAM vault only
- Rotate production credentials immediately
- Scan application code for hardcoded credentials

---

### Pitfall 5: Not Testing Network Isolation

**Problem:** Documenting network separation without verification testing

**Impact:** False sense of security if separation doesn't actually work

**Solution:**
```bash
# Test network isolation from dev workstation:
ping prod-db.internal  # Should TIMEOUT or UNREACHABLE

# Test from test server:
telnet prod-db.internal 5432  # Should FAIL (connection refused)

# Verify allowed exception (monitoring server):
curl http://prod-app:9090/metrics  # Should SUCCEED (allowed)
```

---

### Pitfall 6: Significant Configuration Drift

**Problem:** Staging configuration significantly different from production (>10% drift)

**Impact:** Testing in staging doesn't validate production changes, deployment failures

**Solution:**

- Use Infrastructure as Code (Terraform, CloudFormation) for both staging and prod
- Detect drift with `terraform plan` regularly
- Document intentional differences (e.g., instance size for cost optimization)
- Keep application configuration identical (different instance size OK, different app config NOT OK)

---

### Pitfall 7: Poor Evidence Organization

**Problem:** Evidence files scattered, unclear naming, missing dates

**Impact:** Difficult to find evidence during audit, incomplete evidence package

**Solution:**
```
evidence/
├── EVD-001-network-architecture-2024-01.pdf
├── EVD-002-firewall-rules-export-2024-01.txt
├── EVD-003-aws-accounts-screenshot-2024-01.png
├── EVD-004-rds-instance-list-2024-01.csv
├── EVD-005-vault-config-screenshot-2024-01.png
└── EVD-006-pentest-report-2024-01.pdf

# Use: [Evidence ID]-[description]-[YYYY-MM].ext
```

---

## Quality Checklist

Before submitting your assessment for approval, verify:

### Completeness

- [ ] All sheets completed (1-9)
- [ ] All environments documented (including shadow/decommissioned)
- [ ] All separation mechanisms documented (network, infrastructure, data, credentials)
- [ ] All gaps identified and documented
- [ ] All evidence collected and organized

### Accuracy

- [ ] Network separation verified by actual firewall rule export (not assumptions)
- [ ] Infrastructure separation verified by actual cloud account/VM inventory
- [ ] Data separation verified (no production data in dev/test confirmed)
- [ ] Credential separation verified (unique per environment, prod in PAM confirmed)
- [ ] Configuration consistency measured (actual drift % calculated)

### Evidence Quality

- [ ] All evidence files time-stamped
- [ ] Evidence organized in structured folder
- [ ] Evidence file names descriptive and dated
- [ ] Evidence register complete with file locations
- [ ] Evidence accessible to reviewers/auditors

### Risk Assessment

- [ ] All gaps documented with severity rating
- [ ] High severity gaps have remediation plans
- [ ] Remediation timelines realistic
- [ ] Gap owners assigned
- [ ] Compensating controls documented (if remediation delayed)

### Policy Compliance

- [ ] Assessment addresses all requirements from ISMS-POL-A.8.31, Section 2.1
- [ ] Any policy deviations documented as gaps
- [ ] Exceptions properly documented with approvals
- [ ] Regulatory requirements addressed (FINMA, DORA, NIS2 if applicable)

---

## Review & Approval

### Three-Level Approval Workflow

#### Level 1: Technical Review

- **Reviewer:** IT Operations Manager or Cloud Architect
- **Focus:** Technical accuracy, completeness
- **Timeline:** 2-3 business days
- **Outcome:** Approve, Request Changes, or Reject

**Review Criteria:**

- Is the environment inventory complete?
- Are separation mechanisms accurately documented?
- Is evidence sufficient and verifiable?
- Are gaps realistic and properly prioritized?

#### Level 2: Security Review

- **Reviewer:** CISO or Information Security Manager
- **Focus:** Security compliance, risk assessment
- **Timeline:** 2-3 business days
- **Outcome:** Approve, Request Changes, or Reject

**Review Criteria:**

- Do gaps represent acceptable risk?
- Are remediation timelines appropriate for risk severity?
- Is evidence sufficient for audit?
- Are compensating controls adequate?

#### Level 3: Executive Approval

- **Reviewer:** CTO or VP Engineering
- **Focus:** Strategic alignment, resource allocation
- **Timeline:** 1-2 business days
- **Outcome:** Approve or Request Changes

**Review Criteria:**

- Are remediation resource requirements acceptable?
- Do timelines align with business priorities?
- Is risk posture acceptable?
- Are there budget implications?

### Approval Documentation

Document approvals in Sheet 9 (Evidence Register):

| Role | Name | Date | Signature | Comments |
|------|------|------|-----------|----------|
| Assessment Completed By | [Your Name] | [Date] | _____________ | Initial assessment |
| IT Operations Manager | [Name] | [Date] | _____________ | Technical review approved |
| CISO | [Name] | [Date] | _____________ | Security review approved |
| CTO | [Name] | [Date] | _____________ | Executive approval |

---

## Maintenance & Updates

### Quarterly Updates

**Every 3 months, update:**

- Sheet 2: Environment Inventory (new environments added?)
- Sheet 3: Network Separation (firewall rule changes?)
- Sheet 4: Infrastructure Separation (new infrastructure deployed?)
- Sheet 7: Gap Analysis (gaps remediated? new gaps?)
- Sheet 9: Evidence Register (refresh dated evidence)

**Time required:** 2-3 hours

### Trigger-Based Updates

**Update immediately after:**

- New environment deployed (add to inventory)
- Infrastructure change (cloud account added, VM deployed)
- Firewall rule change (refresh network separation documentation)
- Security incident (document as gap if related to environment separation)
- Audit finding (document as gap, track remediation)

### Continuous Compliance Monitoring

**Automated monitoring:**

- AWS Config rules for VPC peering (should be zero between dev/test and prod)
- Azure Policy for VNet peering restrictions
- IaC drift detection (terraform plan scheduled weekly)
- Data discovery scans (scan dev/test for production data monthly)

**Manual spot checks:**

- Quarterly penetration testing (network isolation verification)
- Quarterly credential audit (verify unique per environment)
- Quarterly configuration drift assessment (staging vs production)

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
