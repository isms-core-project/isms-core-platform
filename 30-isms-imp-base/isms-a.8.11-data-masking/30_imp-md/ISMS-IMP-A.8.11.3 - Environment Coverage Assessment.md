**ISMS-IMP-A.8.11.3 - Environment Coverage Assessment**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.11: Data Masking

# PART I: USER COMPLETION GUIDE

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.11.3 |
| **Version** | 1.0 |
| **Assessment Area** | Environment Coverage & Deployment Verification |
| **Related Policy** | ISMS-POL-A.8.11, Section 2.3 (Environment Coverage Requirements) |
| **Purpose** | Guide users through assessing WHERE data masking is deployed across all organizational environments to ensure comprehensive coverage |
| **Target Audience** | IT Operations Managers, Database Administrators, Cloud Architects, DevOps Engineers, Security Engineers, Compliance Officers, Auditors |
| **Assessment Type** | Environment Coverage & Gap Analysis |
| **Review Cycle** | Quarterly (Environment Inventory Updates) / After Major System Deployments |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial workbook layout specification only | ISMS Implementation Team |

---

# PART I: USER COMPLETION GUIDE

**Target Audience:** IT Operations Managers, Database Administrators, Cloud Architects, DevOps Engineers, Security Engineers, Compliance Officers, Data Governance Teams

**Purpose of This Guide:** Enable systematic assessment of masking coverage across ALL organizational environments - production, non-production, cloud, analytics, backup, and external sharing - to identify gaps and ensure compliance.

**What This Document Does:**

- Explains environment discovery methodology (finding ALL environments, including shadow IT)
- Provides decision frameworks for determining masking requirements per environment type
- Guides through workbook completion for comprehensive coverage assessment
- Defines validation criteria for masking deployment effectiveness
- Establishes gap identification and remediation workflows


**What This Document Does NOT Do:**

- Replace data inventory assessment (prerequisite: complete IMP-A.8.11.1 first)
- Replace masking technique selection (prerequisite: complete IMP-A.8.11.2 first)
- Provide masking tool implementation guides (see vendor documentation)
- Define data classification criteria (see IMP-A.8.11.1)


---

# Assessment Overview

## What This Assessment Measures

This assessment evaluates [Organization]'s **masking deployment coverage** across the complete IT environment landscape to ensure:

1. **Environment Inventory Completeness** - ALL environments cataloged (production, non-production, cloud, analytics, backup, external)
2. **Non-Production Coverage** - 100% of non-production environments masked (MANDATORY policy requirement)
3. **Production Role-Based Masking** - Dynamic Data Masking (DDM) deployed where needed for role-based access
4. **Analytics/Reporting Coverage** - BI, data warehouses, ML platforms have appropriate masking
5. **Cloud Environment Coverage** - Cloud-hosted environments follow same masking rules as on-premises
6. **External Sharing Controls** - Data shared with vendors, partners, auditors is properly masked
7. **Data Flow Mapping** - Data flows between environments have masking checkpoints
8. **Gap Identification** - Unmasked environments requiring remediation are documented

**Core Principle:** *"Every environment where sensitive data resides MUST have appropriate masking controls. No exceptions without formal risk acceptance."*

**Assessment Scope:** Complete organizational IT landscape including:
1. **Production Environments** (live operational systems)
2. **Non-Production Environments** (development, testing, UAT, staging, training, sandbox)
3. **Analytics & Reporting** (BI tools, data warehouses, data lakes, ML/AI platforms)
4. **Backup & Archive** (disaster recovery, long-term retention, offline backups)
5. **Cloud Environments** (AWS, Azure, GCP, SaaS platforms)
6. **External Data Sharing** (vendor access, auditor data, customer data exports)
7. **Data Flow Mapping** (ETL pipelines, data refresh processes, replication flows)

**Assessment Output:** Excel workbook documenting ~50-200 environments with masking coverage status, compliance verification, gap analysis, and remediation roadmap.

**Coverage-Centric Approach:** This assessment is **WHERE-focused** (which environments are masked) not WHAT-focused (which data elements are masked - that's IMP-A.8.11.1) or HOW-focused (which techniques are used - that's IMP-A.8.11.2).

## Why This Matters

**ISO 27001:2022 Control A.8.11 Requirement:**
> *"Data masking should be used in accordance with the organization's topic-specific policy on access control and other related topic-specific policies, and business requirements, taking applicable legislation into consideration."*

**The Critical Coverage Problem:**

Organizations often implement masking in some environments while leaving critical gaps:

- **Development/Test environments** contain production data clones WITHOUT masking (80% of data breaches in test systems)
- **Analytics platforms** have raw PII for reporting (violated GDPR/FADP minimization principles)
- **Cloud sandbox environments** forgotten during compliance initiatives (shadow IT blind spot)
- **Vendor data shares** lack masking (third-party risk exposure)
- **Backup systems** contain unmasked archives (disaster recovery = compliance disaster)


**Regulatory Context:**

- **Swiss nFADP (Art. 8):** Data controllers must implement appropriate technical measures (masking) across ALL data processing
- **EU GDPR (Art. 32):** Security measures must be applied wherever personal data is processed (all environments, not just production)
- **EU GDPR (Art. 25):** Data protection by design requires masking in non-production by default
- **PCI-DSS v4.0 (Req. 3.4):** Cardholder data MUST be masked in non-production environments (no exceptions)
- **HIPAA (§164.514):** De-identification required for test/development use of Protected Health Information (PHI)


**Business Impact:**

- **Data Breaches Prevented:** 80% of preventable data leaks occur in non-production environments (Verizon DBIR)
- **Regulatory Compliance:** Non-production masking is MANDATORY under GDPR Art. 32, not optional
- **Audit Findings:** "Why does your UAT environment have production customer data?" - common audit failure
- **Third-Party Risk:** Unmasked data shared with vendors = your compliance violation, their potential breach
- **Development Velocity:** Properly masked environments enable faster development without compliance delays


## Who Should Complete This Assessment

**Primary Responsibility:** IT Operations Manager, Infrastructure Lead, or DevOps Manager (owns environment landscape)

**Required Knowledge:**

- [Organization]'s IT environment architecture (all systems, databases, applications, cloud resources)
- Environment lifecycle (dev, test, UAT, staging, production promotion flows)
- Data refresh/copy processes (how production data gets to non-production)
- Cloud infrastructure (AWS, Azure, GCP accounts, resource groups, subscriptions)
- External data sharing arrangements (vendors, auditors, partners)


**Required Authority:**

- Ability to inventory ALL environments (including shadow IT)
- Access to environment documentation and configuration management databases (CMDBs)
- Authority to request masking implementation for non-compliant environments
- Ability to approve/reject environment deployment without masking


**Support Roles:**

- **Database Administrators (DBAs):** Database inventory, data refresh scripts, masking tool deployment status
- **Cloud Architects:** Cloud environment inventory (AWS RDS, Azure SQL, GCP BigQuery, etc.)
- **DevOps Engineers:** CI/CD pipelines, environment provisioning, infrastructure-as-code
- **Application Owners:** Business context for environment usage, data sensitivity confirmation
- **Security Engineers:** Masking technique validation, DDM configuration, access controls
- **Data Owners:** Approval for environment-specific masking requirements and exceptions
- **Compliance Officers:** Regulatory requirement validation, exception approval process
- **Third-Party Risk Team:** Vendor data sharing agreements, external access controls


## Time Estimate

**Total Assessment Time:** 8-16 hours (depending on environment complexity and existing documentation)

**Breakdown:**

- **Environment Inventory:** 3-5 hours (if CMDB exists: 2 hours; if manual discovery: 5+ hours)
- **Production Environment Assessment:** 2-3 hours (DDM configuration review, role-based access verification)
- **Non-Production Coverage Analysis:** 2-4 hours (dev/test/UAT/sandbox masking verification)
- **Analytics/Reporting Assessment:** 1-2 hours (BI tool access, data warehouse masking)
- **Cloud Environment Discovery:** 2-3 hours (AWS/Azure/GCP inventory, SaaS platforms)
- **External Sharing Review:** 1-2 hours (vendor agreements, data export procedures)
- **Data Flow Mapping:** 2-3 hours (ETL pipelines, data movement tracking)
- **Gap Analysis & Prioritization:** 1-2 hours
- **Evidence Collection:** 1-2 hours
- **Quality Review:** 1 hour


**Pro Tip for Large Organizations (>100 environments):**

- **Phase 1 (Week 1):** Production + critical non-production (top 20-30 environments)
- **Phase 2 (Week 2):** All non-production environments (dev/test/UAT/staging/training)
- **Phase 3 (Week 3):** Cloud environments, analytics platforms, backup systems
- **Phase 4 (Ongoing):** External sharing, data flow mapping, continuous monitoring


## Connection to Policy and Other Assessments

**Policy Hierarchy:**
```
ISMS-POL-A.8.11 (Data Masking Policy)
    │
    ├─► ISMS-POL-A.8.11, Section 2.1 (Data Classification and Identification) (Data Classification) ◄── Prerequisite
    ├─► ISMS-POL-A.8.11, Section 2.2 (Masking Technique Standards) (Masking Techniques) ◄── Prerequisite  
    ├─► ISMS-POL-A.8.11, Section 2.3 (Environment Coverage Requirements) ◄── YOU ARE HERE
    └─► ISMS-POL-A.8.11, Section 2.4 (Testing and Validation) (Testing & Validation)
```

**Assessment Dependencies:**

**Prerequisites (MUST complete first):**

- ✅ **ISMS-IMP-A.8.11.1** (Data Inventory & Classification) - You must know WHAT data exists and WHERE before assessing masking coverage
- ✅ **ISMS-IMP-A.8.11.2** (Masking Technique Selection) - You should have approved masking techniques before verifying deployment


**Feeds Into (complete next):**

- ➡️ **ISMS-IMP-A.8.11.4** (Testing & Validation Framework) - Tests masking effectiveness in environments identified here
- ➡️ **ISMS-IMP-A.8.11.5** (Compliance Dashboard) - Consolidates environment coverage metrics with other assessments


**Integration Points:**

- Uses data inventory from IMP-A.8.11.1 to verify which environments contain sensitive data
- Uses technique selections from IMP-A.8.11.2 to validate appropriate techniques deployed per environment
- Provides environment list to IMP-A.8.11.4 for masking effectiveness testing


**Policy Requirements Implemented:**

This assessment implements **ISMS-POL-A.8.11, Section 2.3 (Environment Coverage Requirements)** which defines mandatory requirements for:

**REQ-ENV-001:** Maintain complete inventory of ALL environments where data is processed/stored/transmitted  
**REQ-ENV-010:** ALL non-production environments SHALL be masked (100% coverage target)  
**REQ-ENV-011:** Production data SHALL NOT be copied to non-production without masking  
**REQ-ENV-020:** Production environments MAY use DDM for role-based access (conditional)  
**REQ-ENV-030:** Analytics/reporting environments SHALL mask individual-level PII  
**REQ-ENV-040:** Cloud environments SHALL follow same masking rules as on-premises  
**REQ-ENV-050:** External data sharing SHALL be masked unless contractually required and risk-accepted  
**REQ-ENV-060:** Backup environments encryption required; masking conditional based on feasibility  
**REQ-ENV-070:** Data flows SHALL have documented masking checkpoints  
**REQ-ENV-080:** Environment exceptions require Data Owner + CISO approval  
**REQ-ENV-090:** Exception limit: ≤5% of total environments

**Policy Authority:** Chief Information Security Officer (CISO), IT Operations Director  
**Compliance Status:** Mandatory for all environments processing Internal, Confidential, or Restricted data

## Critical Success Factors

**Assessment Quality Indicators:**

✅ **Comprehensive Environment Discovery:**

- ALL production environments documented (no missed critical systems)
- ALL non-production environments discovered (including shadow IT, developer workstations)
- Cloud accounts/subscriptions fully inventoried (AWS, Azure, GCP, multi-cloud)
- SaaS platforms included (Salesforce, Workday, ServiceNow, etc.)
- Backup/DR systems documented (what's backed up = what exists)
- External sharing destinations cataloged (vendors, auditors, partners)


✅ **100% Non-Production Masking Coverage:**

- Development environments: 100% masked (no production data copies)
- Testing/QA environments: 100% masked
- UAT environments: 100% masked
- Staging environments: 100% masked (unless production-identical with same access controls)
- Training environments: 100% masked + synthetic data preferred
- Sandbox/POC environments: 100% masked


✅ **Production Environment Role-Based Masking:**

- DDM deployed for role-based access where applicable
- Unmasked access logged and monitored
- Privileged access requires business justification
- Production reports use masked views for non-privileged users


✅ **Clear Gap Identification:**

- Every unmasked environment documented as gap
- Gap risk levels assigned (Critical/High/Medium/Low)
- Gap owners assigned with remediation target dates
- Critical gaps (unmasked non-production) have ≤30 day remediation SLA


✅ **Audit-Ready Evidence:**

- Environment discovery methodology documented
- Masking deployment verification evidence collected
- Exception approvals formally documented
- Review dates and next actions clearly defined


---

# Prerequisites

## Completed Assessments (MANDATORY)

**Before starting this assessment, you MUST have completed:**

✅ **ISMS-IMP-A.8.11.1 (Data Inventory & Classification)**

- System inventory populated (all databases, applications, file shares)
- Sensitive data elements identified at field level
- Data sensitivity classifications assigned (Critical/High/Medium/Low)
- Data owners assigned per category
- Workbook available for reference


✅ **ISMS-IMP-A.8.11.2 (Masking Technique Selection)**  

- Approved masking techniques documented per data type
- Technique configuration requirements defined
- Masking tool inventory (if tools already deployed)
- Workbook available for reference


**Quality Check:** Verify completion of prerequisites:

- Open IMP-A.8.11.1 workbook → Check System_Inventory sheet populated
- Open IMP-A.8.11.1 workbook → Verify Sensitive_Data_Inventory has ≥10 data elements
- Open IMP-A.8.11.2 workbook → Confirm approved techniques documented


**If Prerequisites Incomplete:** STOP. Complete data inventory and technique selection first. You cannot assess environment coverage without knowing:
1. Which systems contain sensitive data (from IMP-A.8.11.1)
2. Which masking techniques should be deployed (from IMP-A.8.11.2)

## Access Required

**Infrastructure Documentation:**

- [ ] Configuration Management Database (CMDB) or IT asset inventory
- [ ] Network architecture diagrams
- [ ] Data flow diagrams (ETL pipelines, data replication)
- [ ] Cloud infrastructure documentation (AWS, Azure, GCP resource lists)
- [ ] SaaS application inventory (Salesforce, Workday, etc.)
- [ ] Backup/DR system documentation


**System Access:**

- [ ] Read access to environment configuration (database servers, application servers)
- [ ] Cloud console access (AWS Console, Azure Portal, GCP Console) - read-only minimum
- [ ] Masking tool administration console (if tools deployed)
- [ ] CI/CD pipeline access (to understand environment provisioning)
- [ ] Data refresh script repository (how production data gets to non-production)


**Stakeholder Access:**

- [ ] IT Operations team availability (environment inventory validation)
- [ ] DBA team availability (database environment details, refresh schedules)
- [ ] Cloud team availability (cloud resource inventory)
- [ ] DevOps team availability (CI/CD pipelines, infrastructure-as-code)
- [ ] Application Owner contact list (business context for environments)
- [ ] Third-Party Risk team (external data sharing agreements)


## Knowledge Required

**Essential Understanding:**

- [Organization]'s IT environment landscape (all datacenters, cloud providers, hosting locations)
- Environment lifecycle management (how environments are provisioned, refreshed, decommissioned)
- Data copy/refresh processes (production → non-production data movement)
- Cloud architecture (resource groups, subscriptions, accounts, VPCs, regions)
- Regulatory requirements for environment masking (GDPR Art. 32, PCI-DSS Req. 3.4, etc.)


**Technical Skills:**

- Infrastructure discovery methodologies (CMDB queries, cloud inventory tools, network scanning)
- Understanding of environment types (production vs. non-production, staging vs. UAT)
- Data flow analysis (ETL/ELT pipelines, data replication, API integrations)
- Cloud resource management (AWS RDS, Azure SQL, GCP BigQuery inventory)


**NOT Required (but helpful):**

- Deep masking tool configuration expertise (Security Engineers handle technical implementation)
- Database administration expertise (DBAs provide environment details)
- Cloud platform certifications (Cloud Architects provide cloud inventory)


## Tools Needed

**Environment Discovery Tools (Recommended):**

**Configuration Management Databases (CMDBs):**

- **Commercial:** ServiceNow CMDB, BMC Helix CMDB, Device42
- **Open Source:** Ralph, netbox, Collins
- **Purpose:** Authoritative source for environment inventory


**Cloud Resource Discovery:**

- **AWS:** AWS Config, AWS Systems Manager Inventory, CloudMapper
- **Azure:** Azure Resource Graph, Azure Advisor
- **GCP:** Cloud Asset Inventory, GCP Resource Manager
- **Multi-Cloud:** CloudHealth, Morpheus, Flexera


**Network Discovery (if no CMDB):**

- **Commercial:** Nmap, SolarWinds Network Discovery, Lansweeper
- **Open Source:** Nmap, Netdisco, OpenAudIT
- **Purpose:** Discover databases, servers, services on network


**Data Flow Mapping:**

- **Commercial:** Collibra Lineage, Informatica Enterprise Data Catalog, Alation
- **Open Source:** Apache Atlas, DataHub (LinkedIn), Amundsen (Lyft)
- **Purpose:** Map data movement between environments


**Evidence Collection:**

- **Screenshot tool:** For capturing environment configuration, masking status
- **Export capability:** CMDB exports, cloud resource inventory CSV/JSON
- **Secure storage:** Evidence repository (some evidence contains infrastructure details)


**Critical Tool Selection Note:**
This assessment is **tool-agnostic**. [Organization] may use any environment discovery methodology (CMDB, cloud APIs, manual inventory, network scanning). The IMPORTANT part is documenting WHICH environments exist and WHETHER they are masked, not HOW you discovered them.

## Pre-Assessment Checklist

**Before You Begin (Mandatory Steps):**

✅ **Stakeholder Alignment:**

- [ ] CISO/IT Operations Director has approved assessment scope
- [ ] IT Operations team committed to provide environment inventory
- [ ] Cloud team committed to provide cloud resource lists
- [ ] DBA team committed to provide database refresh schedules
- [ ] Assessment timeline communicated to affected teams


✅ **Technical Preparation:**

- [ ] CMDB access provisioned (read-only minimum)
- [ ] Cloud console access configured (AWS, Azure, GCP read-only)
- [ ] Assessment workbook downloaded and unprotected
- [ ] Evidence repository created (folder structure for screenshots, exports)
- [ ] IMP-A.8.11.1 and IMP-A.8.11.2 workbooks available for reference


✅ **Coordination:**

- [ ] IT Operations notified (may need input on environment classification)
- [ ] DBAs notified (data refresh schedule questions)
- [ ] Cloud team notified (cloud resource inventory validation)
- [ ] DevOps team notified (CI/CD pipeline review)
- [ ] Change freeze awareness (avoid running during critical deployments)
- [ ] Escalation path defined (for environment discovery disputes, masking gaps)


---

**END OF PART I - SECTION 1**

**Next Sections to Deliver:**

- Section 2: Assessment Workflow (Phase-by-Phase Process)
- Section 3: Sheet-by-Sheet Completion Guide
- Section 4: Evidence Collection
- Section 5: Common Pitfalls & Troubleshooting
- Section 6: Quality Checklist
- Section 7: Review & Approval Process
- Section 8: Maintenance & Updates
- Section 9: Integration with Other Assessments


**Shall I continue with Section 2: Assessment Workflow?**

# ISMS-IMP-A.8.11.3 - Environment Coverage Assessment
# PART I: USER COMPLETION GUIDE - SECTION 2

---

# Assessment Workflow

## High-Level Process Flow

```
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 1: ENVIRONMENT INVENTORY (Complete "Environment_Inventory" sheet) │
│          Discover ALL environments (production, non-prod, cloud) │
└────────────────────┬────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 2: PRODUCTION ENVIRONMENT ASSESSMENT                       │
│          Complete "Production_Environment" sheet                 │
│          (DDM for role-based access, access logging)            │
└────────────────────┬────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 3: NON-PRODUCTION COVERAGE (CRITICAL!)                    │
│          Complete "NonProduction_Environments" sheet             │
│          (Dev/Test/UAT/Staging/Training/Sandbox - 100% coverage)│
└────────────────────┬────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 4: ANALYTICS & REPORTING COVERAGE                         │
│          Complete "Analytics_Reporting" sheet                    │
│          (BI, data warehouses, ML/AI platforms)                 │
└────────────────────┬────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 5: CLOUD ENVIRONMENT COVERAGE                             │
│          Complete "Cloud_Environments" sheet                     │
│          (AWS, Azure, GCP, SaaS platforms)                      │
└────────────────────┬────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 6: BACKUP & ARCHIVE ASSESSMENT                            │
│          Complete "Backup_Archive" sheet                         │
│          (DR systems, offline backups, long-term retention)     │
└────────────────────┬────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 7: EXTERNAL SHARING REVIEW                                │
│          Complete "External_Sharing" sheet                       │
│          (Vendor access, auditor data, customer exports)        │
└────────────────────┬────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 8: DATA FLOW MAPPING                                      │
│          Complete "Data_Flow_Mapping" sheet                      │
│          (ETL pipelines, data refresh, replication)             │
└────────────────────┬────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 9: GAP ANALYSIS & REMEDIATION PLANNING                    │
│          Complete "Gap_Analysis" sheet                           │
│          (Identify unmasked environments, prioritize remediation)│
└────────────────────┬────────────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 10: EVIDENCE & APPROVAL                                   │
│          Complete "Evidence_Register" + "Summary_Dashboard"      │
│          (Collect evidence, obtain sign-off)                    │
└─────────────────────────────────────────────────────────────────┘
```

## Phase 1: Environment Inventory (3-5 hours)

**Objective:** Discover and document ALL environments where data is processed, stored, or transmitted.

**Sheet:** `Environment_Inventory`

**Critical Principle:** *"If an environment exists, it must be in this inventory. No environment is too small, too temporary, or too forgotten to document."*

**Step-by-Step:**

**1. Extract from CMDB (if exists):**

   - Export all systems classified as: Database Server, Application Server, Virtual Machine, Container, Cloud Resource
   - Include: Environment Name, Environment Type, Hosting Location, Owner
   - Filter to systems that potentially store or process data (exclude pure network devices, load balancers)


**2. Supplement with Cloud Provider Inventory:**
   
   **AWS Discovery:**
   ```bash
   # List all RDS databases across all regions
   aws rds describe-db-instances --query 'DBInstances[*].[DBInstanceIdentifier,Engine,Endpoint.Address]'
   
   # List all EC2 instances with "database" or "app" tags
   aws ec2 describe-instances --filters "Name=tag:Environment,Values=*"
   
   # List all S3 buckets
   aws s3 ls
   ```
   
   **Azure Discovery:**
   ```bash
   # List all SQL databases
   az sql server list --output table
   az sql db list --server <server-name> --resource-group <rg-name>
   
   # List all VMs
   az vm list --output table
   
   # List all storage accounts
   az storage account list --output table
   ```
   
   **GCP Discovery:**
   ```bash
   # List all Cloud SQL instances
   gcloud sql instances list
   
   # List all Compute Engine instances
   gcloud compute instances list
   
   # List all BigQuery datasets
   bq ls
   ```

**3. Discover Non-Production Environments (CRITICAL - Often Missed):**
   
   Interview key stakeholders:

   - **Developers:** "Where do you test code changes?" → Dev database
   - **QA Team:** "Where do you run regression tests?" → Test/QA database
   - **Business Analysts:** "Where do users validate new features?" → UAT database
   - **Training Team:** "Where do you train new employees?" → Training environment
   - **Data Scientists:** "Where do you build ML models?" → Analytics sandbox
   - **DevOps:** "What CI/CD test environments exist?" → Ephemeral test environments


**4. Identify Shadow IT (High Risk Area):**

   - Developer workstations with local database copies
   - Personal cloud accounts (AWS free tier, Azure trial subscriptions)
   - Forgotten POC/pilot environments (never decommissioned)
   - Old staging environments (replaced but still running)
   - Contractor/vendor-managed environments (out of sight, out of mind)


**5. Document SaaS Platforms:**

   - Salesforce (contains customer PII)
   - Workday (contains HR data)
   - ServiceNow (may contain customer data in tickets)
   - Jira/Confluence (may contain sensitive project data)
   - Office 365/Google Workspace (SharePoint, OneDrive, Drive contain files)


**6. Don't Forget Backup & DR:**

   - Backup systems (what's backed up = what exists in production)
   - Disaster Recovery sites (hot standby, warm standby, cold standby)
   - Archive systems (long-term retention, compliance archives)
   - Decommissioned systems awaiting deletion (retention period not yet expired)


**7. Complete Excel Rows (8-57, 50 row template):**
   
   For EACH environment discovered:

   - **Environment Name:** Descriptive name (e.g., "CRM Production DB", "Dev-Test-UAT-MySQL-01")
   - **Environment Type:** Production / Development / Testing / UAT / Staging / Training / Sandbox / Analytics / Cloud / Backup / Archive / External
   - **Classification:** Sensitive / Confidential / Internal / Public (based on data it contains)
   - **Hosting Location:** On-Premises / AWS / Azure / GCP / Hybrid / Other Cloud
   - **Data Sensitivity:** PII / Financial / Health / Credentials / Proprietary / Mixed / None
   - **Masking Required?:** ✅ Mandatory / ⚠️ Conditional / ❌ Not Required / N/A
   - **Masking Deployed?:** Yes / No / Partial / Planned / N/A
   - **Masking Technique:** SDM / DDM / Tokenization / Encryption / Redaction / Substitution / Anonymization / None
   - **Masking Tool/Solution:** [Tool name if deployed]
   - **Coverage %:** Percentage of sensitive fields masked (0-100%)
   - **Last Verified Date:** When masking status last checked
   - **Environment Owner:** IT Operations contact
   - **Data Owner:** Business contact from IMP-A.8.11.1
   - **Exception Approved?:** Yes / No / N/A (if unmasked, is there formal exception?)
   - **Compliance Status:** ✅ Compliant / ⚠️ Partial / ❌ Non-Compliant / N/A
   - **Notes/Comments:** Any special considerations
   - **Evidence ID:** Link to Evidence_Register (e.g., EV-ENV-001)


**Quality Checks:**

- [ ] All production systems from IMP-A.8.11.1 System_Inventory present
- [ ] At least 3-5 non-production environments per production system (dev, test, UAT minimum)
- [ ] Cloud accounts inventoried (check billing dashboards for active resources)
- [ ] SaaS platforms included (Salesforce, Workday, ServiceNow, etc.)
- [ ] Backup/DR systems documented
- [ ] No "Unknown" masking status without gap entry
- [ ] Environment owners assigned to all environments


**Common Mistakes to Avoid:**

- ❌ Only documenting production (80% of data breach risk is non-production)
- ❌ Forgetting cloud sandbox/dev accounts (shadow IT blind spot)
- ❌ Missing contractor/vendor-managed environments (third-party risk)
- ❌ Not including SaaS platforms (they store YOUR sensitive data)
- ❌ Overlooking decommissioned systems still running (retention compliance issue)


## Phase 2: Production Environment Assessment (2-3 hours)

**Objective:** Verify Dynamic Data Masking (DDM) deployment in production for role-based access control.

**Sheet:** `Production_Environment`

**Policy Requirement:** Production environments MAY contain unmasked data IF access is role-based and logged. DDM is the preferred technique.

**Step-by-Step:**

**1. Identify Production Environments Requiring DDM:**
   
   Review IMP-A.8.11.1 Sensitive_Data_Inventory:

   - Which production systems contain Critical/High sensitivity data?
   - Do non-privileged users need access? (customer service, helpdesk, business analysts)
   - Example: Customer service reps need to VIEW customer records but NOT see full credit card numbers


**2. Verify DDM Implementation:**
   
   For EACH production environment:

   - **Is DDM configured?** Check masking tool configuration, database views, application layer masking
   - **Which user roles see masked data?** Customer service, helpdesk, reports
   - **Which fields are masked?** Credit card (last 4 digits visible), SSN (XXX-XX-1234), Email (j***@example.com)
   - **Is unmasked access logged?** Audit trail for privileged users accessing full data
   - **Access control method?** RBAC (Role-Based), ABAC (Attribute-Based), ACL, Database roles


**3. Document in Excel (Rows 8-37, 30 row template):**
   
   Standard columns A-Q, PLUS extended columns:

   - **User Role/Group:** Which role sees masked data? (e.g., "Customer Service Representative")
   - **Masked Fields:** List of fields masked for this role (e.g., "credit_card_number, ssn, date_of_birth")
   - **Unmasked Access Logged?:** Yes / No / N/A
   - **Access Control Method:** RBAC / ABAC / ACL / Manual / None
   - **Exception Justification:** Why unmasked access needed (e.g., "Finance team reconciliation")
   - **Risk Level:** High / Medium / Low / None
   - **Remediation Target Date:** If gaps identified


**4. Verify Access Logging:**
   
   - Are privileged users accessing unmasked production data logged?
   - Log format: Who, What (which table/field), When, Why (business justification)
   - Log review frequency: Monthly minimum
   - Anomaly detection: Unusual access patterns flagged


**Quality Checks:**

- [ ] All production systems with sensitive data assessed
- [ ] DDM deployed for non-privileged user access (where applicable)
- [ ] Masked fields documented per user role
- [ ] Unmasked access logged and reviewed
- [ ] Privileged access requires business justification
- [ ] Exceptions documented with Data Owner + CISO approval


**Common Mistakes to Avoid:**

- ❌ "We don't need DDM, only admins access production" → Customer service? Helpdesk? Business analysts?
- ❌ DDM configured but not enabled (configuration drift)
- ❌ Logging unmasked access but never reviewing logs (checkbox compliance)
- ❌ Assuming production can be unmasked (policy is conditional, not automatic exemption)


## Phase 3: Non-Production Coverage - CRITICAL! (2-4 hours)

**Objective:** Verify 100% masking coverage in ALL non-production environments. This is MANDATORY, not optional.

**Sheet:** `NonProduction_Environments`

**Policy Requirement:** ALL non-production environments SHALL be masked. No exceptions without formal risk acceptance.

**Critical Principle:** *"If production data exists in non-production, it MUST be masked. No 'we'll mask it later' excuses."*

**Step-by-Step:**

**1. Identify ALL Non-Production Environments:**
   
   From Phase 1 Environment_Inventory, filter for:

   - Development
   - Testing/QA
   - UAT (User Acceptance Testing)
   - Staging/Pre-Production
   - Training
   - Sandbox/POC
   - Performance Testing
   - Integration Testing


**2. Verify Masking Status:**
   
   For EACH non-production environment:
   
   **Question 1:** Does this environment contain production data?

   - If NO → Still document, but masking requirement = N/A
   - If YES → Masking is MANDATORY
   

   **Question 2:** Is masking deployed?

   - Check data refresh scripts (do they include masking step?)
   - Visual inspection (connect to database, SELECT * from sensitive tables, verify masked)
   - Automated validation (run masking verification script)
   

   **Question 3:** Coverage percentage?

   - % of sensitive fields masked = (Masked Fields / Total Sensitive Fields) × 100
   - Target: 100%
   - Anything <100% is a gap requiring remediation


**3. Understand Data Refresh Process:**
   
   Critical to know HOW production data gets to non-production:
   
   **Compliant Data Refresh:**
   ```
   Production DB → Export → Masking Step → Import → Non-Prod DB
   ```
   
   **Non-Compliant Data Refresh (CRITICAL GAP):**
   ```
   Production DB → Direct Copy → Non-Prod DB (NO MASKING!)
   ```
   
   **Ask DBAs:**

   - "How do you refresh dev/test data?"
   - "What's the masking step in your data refresh script?"
   - "If I connect to dev database right now, will I see real customer names?"


**4. Document in Excel (Rows 8-37, 30 row template):**
   
   Standard columns A-Q, PLUS extended columns:

   - **Data Refresh Frequency:** Daily / Weekly / Monthly / Ad-hoc / Never
   - **Refresh Process:** Automated / Manual / Hybrid
   - **Masking in Refresh Script?:** Yes / No / N/A
   - **Last Data Refresh Date:** When was data last copied from production?
   - **Next Refresh Date:** When is next refresh scheduled?
   - **Developer Access Count:** How many people have access?
   - **Contractor Access?:** Yes / No (third-party risk)


**5. Red Flags (Immediate Escalation to CISO):**
   
   ⚠️ **CRITICAL GAP:** Non-production contains unmasked production data

   - Compliance violation: GDPR Art. 32, PCI-DSS Req. 3.4, HIPAA §164.514
   - Audit finding: Guaranteed ISO 27001 certification failure
   - Data breach risk: 80% of preventable breaches occur in test systems
   

   **Immediate Actions:**

   - Document as P1 gap (highest priority)
   - Restrict access to environment (emergency ACL change)
   - Schedule masking implementation (≤30 day SLA for non-production)
   - Notify CISO and Data Owner


**Quality Checks:**

- [ ] ALL non-production environments assessed (no forgotten dev/test systems)
- [ ] 100% coverage target for environments with production data
- [ ] Data refresh scripts include masking step (not manual afterthought)
- [ ] Developer/contractor access counts documented (know who has access)
- [ ] Any <100% coverage documented as gap with remediation plan
- [ ] Critical gaps (unmasked non-prod) have ≤30 day remediation SLA


**Common Mistakes to Avoid:**

- ❌ "It's just dev, we trust our developers" → Trust is not a control, policy requires masking
- ❌ "We're planning to mask it next quarter" → Policy says SHALL mask, not "will mask someday"
- ❌ "UAT needs real data for realistic testing" → Use masked data with realistic patterns
- ❌ Missing developer workstations (they copy production data locally)
- ❌ Forgetting ephemeral CI/CD environments (they may contain test data from production)


## Phase 4: Analytics & Reporting Coverage (1-2 hours)

**Objective:** Verify masking in BI tools, data warehouses, data lakes, ML/AI platforms.

**Sheet:** `Analytics_Reporting`

**Policy Requirement:** Analytics environments SHALL mask individual-level PII. Aggregation and anonymization preferred.

**Step-by-Step:**

**1. Identify Analytics Platforms:**

   - Business Intelligence: Tableau, Power BI, Looker, Qlik, Sisense
   - Data Warehouses: Snowflake, Redshift, BigQuery, Azure Synapse, Teradata
   - Data Lakes: AWS S3 + Athena, Azure Data Lake, Databricks
   - ML/AI Platforms: SageMaker, Azure ML, Vertex AI, custom Jupyter notebooks
   - Reporting: SSRS, Crystal Reports, custom dashboards


**2. Assess Data Granularity:**
   
   **Individual-Level Data (Requires Masking):**

   - Customer records with names, emails, phone numbers
   - Employee records with salaries, performance reviews
   - Transaction details with account numbers
   

   **Aggregate Data (May Not Require Masking):**

   - "Total sales by region" (no individual identification)
   - "Average salary by department" (>5 people per group)
   - "Customer count by age range" (no PII)


**3. Verify Masking or Anonymization:**
   
   **Option 1: Masking at Source**

   - Analytics platform queries masked production views
   - Data warehouse ETL includes masking step
   - Example: Analysts see "Customer ID: 12345" not "John Smith"
   

   **Option 2: Aggregation**

   - Data is aggregated before storage in analytics platform
   - k-anonymity: Each record indistinguishable from ≥4 others
   - Example: "Age range 30-40, ZIP 12XXX, Male" not individual records
   

   **Option 3: Anonymization**

   - Irreversible transformation (not just masking)
   - Statistical disclosure control
   - Example: Differential privacy, data synthesis


**4. Document in Excel (Rows 8-37, 30 row template):**
   
   Extended columns:

   - **Platform Type:** BI Tool / Data Warehouse / Data Lake / ML Platform / Reporting
   - **Data Granularity:** Individual-level / Aggregated / Anonymized / Mixed
   - **Analyst Access Count:** How many people have access?
   - **External Access?:** Vendors / Consultants (Yes / No)
   - **PII Visible?:** Yes / No / Partial (if yes, requires masking or exception)


**Quality Checks:**

- [ ] All analytics platforms inventoried (don't forget personal Excel exports)
- [ ] Individual-level PII masked or aggregated
- [ ] Data warehouse ETL includes masking step (verify scripts)
- [ ] BI dashboards use masked views (test by logging in as analyst)
- [ ] ML platforms anonymize training data (model outputs don't leak PII)


## Phase 5: Cloud Environment Coverage (2-3 hours)

**Objective:** Verify cloud environments follow same masking rules as on-premises.

**Sheet:** `Cloud_Environments`

**Policy Requirement:** Cloud environments SHALL follow same masking rules as on-premises (no cloud exemption).

**Step-by-Step:**

**1. Inventory Cloud Environments:**

   - AWS: RDS, DynamoDB, S3, Redshift, Athena
   - Azure: SQL Database, Cosmos DB, Blob Storage, Synapse
   - GCP: Cloud SQL, BigQuery, Cloud Storage, Datastore
   - SaaS: Salesforce, Workday, ServiceNow (vendor-hosted)


**2. Classify by Environment Type:**

   - Cloud Production → Same rules as on-prem production (DDM conditional)
   - Cloud Non-Production → MANDATORY masking (same as on-prem non-prod)
   - Cloud Analytics → Masking or aggregation required
   - Cloud Backup → Encryption required, masking conditional


**3. Verify Masking Coverage:**

   - Do cloud dev/test databases have masked data?
   - Do S3 buckets contain masked exports?
   - Do cloud-based BI tools query masked views?


**4. Document in Excel (Rows 8-37, 30 row template):**
   Extended columns:

   - **Cloud Provider:** AWS / Azure / GCP / Multi-Cloud / SaaS
   - **Cloud Service:** RDS, S3, BigQuery, etc.
   - **Region/Location:** us-east-1, eu-central-1 (data residency)
   - **Multi-Tenant?:** Yes / No (SaaS platforms)


**Common Mistakes:**

- ❌ "Cloud is vendor's responsibility" → NO, you're data controller, vendor is processor
- ❌ Forgetting cloud sandbox accounts (developers spin up test databases)
- ❌ S3 buckets with unmasked exports (accessible to anyone with URL if misconfigured)


---

**END OF PART I - SECTION 2**

**Next Sections:**

- Section 3: Sheet-by-Sheet Completion Guide (External Sharing, Backup/Archive, Data Flow Mapping, Gap Analysis)
- Section 4: Evidence Collection
- Section 5: Common Pitfalls & Troubleshooting
- Section 6: Quality Checklist


**Shall I continue with Section 3?**

# ISMS-IMP-A.8.11.3 - Environment Coverage Assessment
# PART I: USER COMPLETION GUIDE - SECTION 3

---

# Assessment Workflow (Continued)

## Phase 6: Backup & Archive Assessment (1-2 hours)

**Objective:** Assess masking feasibility in backup/DR systems and verify encryption at minimum.

**Sheet:** `Backup_Archive`

**Policy Requirement:** Backup environments MAY contain unmasked data IF encrypted and access-controlled. Masking conditional based on technical feasibility.

**The Backup Dilemma:**

Backups present a unique challenge:

- **Challenge:** Full database backups are typically byte-for-byte copies (masking would break restore functionality)
- **Reality:** Most backup systems cannot mask during backup without breaking disaster recovery
- **Solution:** Encryption + Access Control is minimum requirement; masking where technically feasible


**Step-by-Step:**

**1. Inventory ALL Backup Systems:**

   - Production database backups (full, incremental, transaction logs)
   - Disaster Recovery (DR) sites (hot standby, warm standby, cold standby)
   - Archive systems (long-term retention for compliance)
   - Cloud backups (AWS Backup, Azure Backup, cloud-native snapshots)
   - Offline backups (tapes, removable media)
   - Developer/team backups (local exports, ad-hoc dumps)


**2. Assess Backup Content:**
   
   For EACH backup system:

   - **What is being backed up?** Production databases, file shares, application data
   - **Does backup contain sensitive data?** Check against IMP-A.8.11.1 inventory
   - **Backup format:** Full database dump / File-level backup / Block-level snapshot
   - **Restore requirement:** Must restore to exact original state? (Yes = masking may break recovery)


**3. Evaluate Masking Feasibility:**
   
   **Masking Feasible:**

   - Export backups for analytics/testing → Mask before export
   - Archive for compliance only (no restore needed) → Can mask archive
   - File-level backups of reports/exports → Mask files before backup
   

   **Masking NOT Feasible (Require Encryption Instead):**

   - Full database backups (byte-for-byte restore requirement)
   - Transaction log backups (point-in-time recovery breaks if masked)
   - DR hot standby (must be exact replica for failover)
   - Incremental backups (delta changes, masking would break chain)


**4. Verify Encryption (MANDATORY if not masked):**
   
   **Encryption at Rest:**

   - Backup storage encrypted? (AES-256 minimum)
   - Encryption keys managed securely? (KMS, Hardware Security Module)
   - Key rotation policy? (annual minimum)
   

   **Encryption in Transit:**

   - Backup transfer encrypted? (TLS 1.2+ for network backups)
   - Offline media encryption? (Tape encryption, encrypted USB)
   

   **Access Controls:**

   - Who can restore backups? (Principle of least privilege)
   - Restore operations logged? (Audit trail)
   - Backup admin access restricted? (Separate from production access)


**5. Document in Excel (Rows 8-37, 30 row template):**
   
   Extended columns:

   - **Backup Type:** Full / Incremental / Differential / Transaction Log / Snapshot / Archive
   - **Backup Frequency:** Hourly / Daily / Weekly / Monthly / Yearly
   - **Retention Period:** 7 days / 30 days / 90 days / 1 year / 7 years (regulatory)
   - **Encryption Method:** AES-256 / TDE / Disk Encryption / None
   - **Encryption at Rest?:** Yes / No
   - **Encryption in Transit?:** Yes / No
   - **Key Management:** KMS / HSM / Manual / N/A
   - **Restore Access Control:** Restricted / General / None
   - **Masking Feasible?:** Yes / No / Conditional
   - **Masking Applied?:** Yes / No / N/A (if not feasible)


**6. Risk Assessment:**
   
   **High Risk (Requires Mitigation):**

   - Unencrypted backups containing sensitive data → CRITICAL GAP
   - Backup access not logged → Cannot detect unauthorized restore
   - Weak encryption (DES, 3DES, <128-bit keys) → Upgrade required
   

   **Medium Risk (Monitor):**

   - Encrypted but not masked (acceptable if access-controlled)
   - Long retention periods (>7 years) → Data minimization concern
   - Offshore backups (cross-border data transfer) → GDPR/FADP concern
   

   **Low Risk:**

   - Encrypted, access-controlled, retention aligned with policy
   - DR site has same controls as production
   - Regular restore testing (proves encryption doesn't break recovery)


**Quality Checks:**

- [ ] All backup systems inventoried (production, DR, archive, cloud, offline)
- [ ] Encryption verified for unmasked backups (AES-256 minimum)
- [ ] Access controls restrict who can restore backups
- [ ] Retention periods align with legal requirements (not arbitrary)
- [ ] Masking applied where technically feasible (export backups for testing)
- [ ] High-risk gaps (unencrypted backups) escalated to CISO


**Common Mistakes to Avoid:**

- ❌ "Backups are offline, we don't need encryption" → Stolen tapes = data breach
- ❌ "Masking backups breaks restore" → True for full backups, but mask EXPORT copies
- ❌ "We never restore backups, low priority" → Disaster happens when you least expect it
- ❌ Not inventorying developer backups (local SQL dumps on laptops)


## Phase 7: External Sharing Review (1-2 hours)

**Objective:** Verify data shared with external parties (vendors, auditors, customers) is properly masked.

**Sheet:** `External_Sharing`

**Policy Requirement:** External data sharing SHALL be masked unless contractually required and formally risk-accepted.

**The External Sharing Risk:**

Third-party data sharing is a major compliance blind spot:

- Vendor gets "production data for testing their integration" → Unmasked export
- Auditor requests "customer transaction sample" → CSV with PII
- Customer requests "their data for migration" → Oversharing (includes other customers' data)
- Partner receives "analytics feed" → Individual-level records instead of aggregates


**Step-by-Step:**

**1. Inventory ALL External Data Sharing:**
   
   **Vendor/Partner Access:**

   - SaaS vendors with database access (support, integrations)
   - System integrators with test data access (implementation, UAT)
   - Managed service providers with production access (outsourced operations)
   - Business partners receiving data feeds (B2B integrations, EDI)
   

   **Auditor/Regulator Access:**

   - External auditors (ISO 27001, SOC 2, financial audits)
   - Regulatory authorities (data requests, investigations)
   - Legal discovery (litigation, e-discovery)
   

   **Customer Data Exports:**

   - "Download your data" features (GDPR Art. 20 portability)
   - Customer migration exports (switching providers)
   - Customer reporting/analytics access
   

   **Offshore/Outsourced Operations:**

   - Offshore development teams (India, Eastern Europe, Latin America)
   - Offshore customer support (call centers)
   - Outsourced data entry/processing


**2. Assess Contractual Obligations:**
   
   For EACH external sharing arrangement:
   
   **Question 1:** Is unmasked data contractually required?

   - **Example - YES:** Auditor needs to verify specific transactions (must see real values)
   - **Example - NO:** Vendor testing integration (can use masked data)
   

   **Question 2:** Is Data Processing Agreement (DPA) in place?

   - GDPR Art. 28 requires DPA with all processors
   - DPA specifies security measures (including masking where applicable)
   - DPA includes data breach notification requirements
   

   **Question 3:** Is risk formally accepted?

   - If sharing unmasked data, who approved? (Data Owner + CISO minimum)
   - Risk assessment documented?
   - Compensating controls? (NDA, access logging, time-limited access)


**3. Verify Masking Implementation:**
   
   **Compliant External Sharing:**
   ```
   Production DB → Masking Step → Export File → Secure Transfer → External Party
   ```
   
   **Non-Compliant External Sharing (CRITICAL GAP):**
   ```
   Production DB → Direct Export → Email Attachment → External Party (NO MASKING!)
   ```
   
   **Best Practices:**

   - **Redaction:** Remove PII entirely if not needed (GDPR minimization)
   - **Aggregation:** Provide summary statistics instead of individual records
   - **Sampling:** Provide subset of data, not full production dump
   - **Time-Limited Access:** Revoke access after project completion
   - **Access Logging:** Track what external party accessed


**4. Document in Excel (Rows 8-37, 30 row template):**
   
   Extended columns:

   - **External Party Name:** Company name, auditor firm
   - **External Party Type:** Vendor / Partner / Auditor / Regulator / Customer / Offshore Team
   - **Purpose of Sharing:** Testing / Audit / Integration / Support / Analytics
   - **Contractual Requirement?:** Yes / No (unmasked data required by contract?)
   - **DPA in Place?:** Yes / No / N/A
   - **Data Transfer Method:** SFTP / API / Email (encrypted) / Physical Media / Portal
   - **Transfer Frequency:** One-time / Daily / Weekly / Monthly / On-demand
   - **Access Duration:** Permanent / Temporary (specify end date)
   - **Data Volume:** Number of records shared
   - **Risk Assessment Done?:** Yes / No
   - **CISO Approval Date:** When was sharing approved?


**5. Red Flags (Immediate Escalation):**
   
   ⚠️ **CRITICAL GAPS:**

   - Unmasked data sent via email (not encrypted) → Data breach waiting to happen
   - Vendor has production database access without DPA → GDPR Art. 28 violation
   - Offshore team has unrestricted production access → Cross-border transfer risk
   - No access logging for external parties → Cannot detect data exfiltration
   - Sharing continues after contract ends → No legal basis for processing


**Quality Checks:**

- [ ] All external data sharing arrangements documented (vendors, auditors, customers)
- [ ] DPAs in place for all data processors (GDPR Art. 28)
- [ ] Unmasked sharing has formal risk acceptance (Data Owner + CISO)
- [ ] Data transfer methods secure (encrypted in transit)
- [ ] Access is time-limited where possible (revoke after project)
- [ ] Access logging enabled (audit trail for external access)


**Common Mistakes to Avoid:**

- ❌ "Vendor signed NDA, we're covered" → NDA is legal, not technical control
- ❌ "It's just a sample for testing" → Sample may still contain real PII
- ❌ "Customer requested their data, we had to provide it" → Provide THEIR data, not everyone's data
- ❌ Forgetting to revoke access after project ends (vendor still has credentials)


## Phase 8: Data Flow Mapping (2-3 hours)

**Objective:** Map data flows between environments and verify masking checkpoints.

**Sheet:** `Data_Flow_Mapping`

**Policy Requirement:** Data flows SHALL have documented masking checkpoints to prevent unmasked data leakage.

**The Data Flow Problem:**

Data moves between environments constantly:

- Production → Non-Production (data refresh)
- Production → Analytics (ETL pipelines)
- Production → Backup (backup jobs)
- Production → External (vendor integrations, customer exports)
- Non-Production → Production (code deployment, reverse flow)


**Step-by-Step:**

**1. Identify Major Data Flows:**
   
   **Production Data Refresh Flows:**

   - Production → Development (weekly refresh for realistic test data)
   - Production → UAT (monthly refresh for user testing)
   - Production → Training (quarterly refresh for employee training)
   

   **Analytics/Reporting Flows:**

   - Production → Data Warehouse (nightly ETL)
   - Production → BI Tool (real-time query or cached extracts)
   - Production → ML Platform (model training datasets)
   

   **Backup/DR Flows:**

   - Production → Backup System (hourly/daily backups)
   - Production → DR Site (real-time replication or periodic sync)
   

   **External Integration Flows:**

   - Production → Vendor API (B2B integrations)
   - Production → Customer Portal (data exports)
   - Production → Auditor (compliance data requests)


**2. Map Each Flow:**
   
   For EACH data flow:

   - **Source Environment:** Where data originates (typically production)
   - **Destination Environment:** Where data goes (dev, analytics, vendor, etc.)
   - **Flow Frequency:** Real-time / Hourly / Daily / Weekly / Monthly / On-demand
   - **Flow Mechanism:** ETL tool / Database replication / API / File transfer / Manual export
   - **Data Volume:** Number of records transferred per flow
   - **Sensitive Data Included?:** Yes / No (check against IMP-A.8.11.1)


**3. Identify Masking Checkpoints:**
   
   **Checkpoint Location Options:**
   
   **Option 1: At Source (Best Practice)**
   ```
   Production DB → Masked View → Export → Destination
   ```

   - Advantage: Impossible to accidentally export unmasked data
   - Example: ETL queries masked production views, not raw tables
   

   **Option 2: In Pipeline (Good)**
   ```
   Production DB → Extract → Masking Step → Load → Destination
   ```

   - Advantage: Flexible masking rules per destination
   - Example: ETL tool includes masking transformation
   

   **Option 3: At Destination (Acceptable if Audited)**
   ```
   Production DB → Extract → Load → Destination → Mask on Arrival
   ```

   - Disadvantage: Temporary window where unmasked data exists in destination
   - Requires: Immediate masking on arrival, access restricted until masked
   

   **Option 4: None (NON-COMPLIANT for Non-Prod Destinations)**
   ```
   Production DB → Direct Copy → Destination (NO MASKING)
   ```

   - This is a CRITICAL GAP if destination is non-production


**4. Verify Checkpoint Implementation:**
   
   **For ETL/Data Pipelines:**

   - Review ETL job definitions (Informatica, Talend, Apache Airflow, etc.)
   - Locate masking transformation step in pipeline
   - Verify masking runs BEFORE data writes to destination
   - Check error handling (if masking fails, does pipeline stop or continue?)
   

   **For Database Replication:**

   - Real-time replication (e.g., AWS DMS, Oracle GoldenGate) → Masking at destination
   - Snapshot replication → Masking step between snapshot and restore
   - Log shipping → Cannot mask without breaking chain (requires destination-side masking)
   

   **For API Integrations:**

   - API returns masked data (application layer masking)
   - API access controlled by role (DDM)
   - API logging (audit trail of data shared)


**5. Document in Excel (Rows 8-37, 30 row template):**
   
   Extended columns:

   - **Source Environment:** Where data originates
   - **Destination Environment:** Where data goes
   - **Flow Description:** What data moves and why
   - **Flow Frequency:** Real-time / Hourly / Daily / Weekly / Monthly
   - **Flow Mechanism:** ETL / Replication / API / File Transfer / Manual
   - **Sensitive Data Transferred?:** Yes / No
   - **Masking Checkpoint Exists?:** Yes / No / N/A
   - **Checkpoint Location:** At Source / In Pipeline / At Destination / None
   - **Masking Technique Used:** SDM / DDM / Tokenization / Redaction / None
   - **Checkpoint Automated?:** Yes / Manual / N/A
   - **Checkpoint Validation:** How is masking verified? (automated tests, manual checks)
   - **Failure Handling:** What happens if masking fails? (Stop flow / Alert / Continue)


**6. Risk Assessment:**
   
   **Critical Risks:**

   - No masking checkpoint for Production → Non-Production flow → P1 GAP
   - Masking checkpoint can be bypassed (manual override) → P1 GAP
   - Masking failure allows unmasked data through → P2 GAP
   

   **Medium Risks:**

   - Manual masking step (human error risk) → Automate
   - No validation that masking worked → Add checkpoint validation
   - Temporary unmasked window at destination → Minimize duration


**Quality Checks:**

- [ ] All major data flows mapped (production → non-prod, analytics, external)
- [ ] Masking checkpoints identified for flows with sensitive data
- [ ] Checkpoint implementation verified (not just documented)
- [ ] Checkpoint automation preferred (manual = error-prone)
- [ ] Failure handling defined (masking fails → flow stops)
- [ ] Bypass controls (cannot skip masking step)


**Common Mistakes to Avoid:**

- ❌ "We mask at destination, so it's fine" → Temporary window of unmasked data = risk
- ❌ "It's an automated script, we trust it" → Scripts fail, need validation step
- ❌ "Manual process, very careful" → Humans make mistakes, automate masking
- ❌ Not documenting reverse flows (non-production → production should NOT happen with sensitive data)


## Phase 9: Gap Analysis & Remediation Planning (1-2 hours)

**Objective:** Consolidate ALL gaps identified across Phases 1-8 and prioritize remediation.

**Sheet:** `Gap_Analysis`

**Critical Principle:** *"Every unmasked environment or missing checkpoint is a gap. Every gap needs an owner, a plan, and a deadline."*

**Step-by-Step:**

**1. Consolidate Gaps from All Sheets:**
   
   Review each assessment sheet and extract gaps:

   - Environment_Inventory: Systems not inventoried
   - Production_Environment: Missing DDM, unlogged access
   - NonProduction_Environments: <100% coverage (CRITICAL!)
   - Analytics_Reporting: Individual-level PII visible
   - Cloud_Environments: Unmasked cloud dev/test
   - Backup_Archive: Unencrypted backups
   - External_Sharing: Unmasked vendor data
   - Data_Flow_Mapping: Missing masking checkpoints


**2. Assign Gap Priority:**
   
   **P1 - Critical (Remediate ≤30 days):**

   - Unmasked non-production environment with production data
   - Unencrypted backup containing sensitive data
   - External sharing of unmasked data without DPA
   - No masking checkpoint for production → non-production flow
   

   **P2 - High (Remediate ≤90 days):**

   - Production DDM missing where required
   - Analytics platform with individual-level PII
   - Cloud non-production environment <100% coverage
   - Manual masking checkpoint (needs automation)
   

   **P3 - Medium (Remediate ≤180 days):**

   - Access logging missing
   - Exception approvals expired (need renewal)
   - Masking coverage 90-99% (almost compliant)
   - Data flow mapping incomplete
   

   **P4 - Low (Remediate ≤365 days):**

   - Documentation gaps (coverage exists, evidence missing)
   - Process improvements (automation opportunities)
   - Nice-to-have enhancements


**3. Assign Gap Owners:**
   
   For EACH gap:

   - **Gap Owner:** Person responsible for remediation (name, not just role)
   - **Supporting Teams:** DBAs, Cloud Team, Security, DevOps (as needed)
   - **Data Owner Approval:** Required for Critical/High gaps
   - **CISO Escalation:** If gap remediation blocked or delayed


**4. Define Remediation Actions:**
   
   For EACH gap:

   - **Remediation Action:** Specific step to close gap (not vague "implement masking")
   - **Target Completion Date:** Realistic date based on priority SLA
   - **Dependencies:** What must happen first? (tool procurement, approvals, etc.)
   - **Resource Requirements:** Budget, headcount, tools needed
   - **Success Criteria:** How will we know gap is closed? (evidence required)


**5. Document in Excel (Rows 8-47, 40 row template):**
   
   Columns:

   - **Gap ID:** GAP-001, GAP-002, etc.
   - **Gap Category:** Environment Inventory / Production / Non-Production / Analytics / Cloud / Backup / External / Data Flow
   - **Gap Description:** Specific description (e.g., "Dev database contains unmasked customer PII")
   - **Environment(s) Affected:** Which specific environments
   - **Risk Level:** Critical / High / Medium / Low
   - **Priority:** P1 / P2 / P3 / P4
   - **Gap Owner:** Named individual
   - **Supporting Teams:** DBAs, Cloud, Security, DevOps
   - **Remediation Action:** Specific steps to close gap
   - **Target Completion Date:** Based on priority SLA
   - **Current Status:** Not Started / In Progress / Blocked / Completed
   - **Completion Date:** When gap was actually closed
   - **Verification Method:** How gap closure verified
   - **Evidence ID:** Link to Evidence_Register (proof gap closed)


**6. Risk Acceptance Process (If Remediation Not Feasible):**
   
   **When Risk Acceptance Needed:**

   - Technical limitation prevents masking (e.g., vendor tool doesn't support)
   - Business requirement for unmasked data (e.g., fraud investigation)
   - Remediation cost exceeds risk (rare, requires CFO approval)
   

   **Risk Acceptance Requirements:**

   - Data Owner approval (business accountability)
   - CISO approval (security accountability)
   - Compensating controls defined (access logging, encryption, monitoring)
   - Review period (risk acceptance expires, requires renewal)
   - Documentation in Exception Register (audit trail)


**Quality Checks:**

- [ ] All gaps from all sheets consolidated (nothing missed)
- [ ] Priority assigned based on objective criteria (not subjective)
- [ ] P1 gaps have ≤30 day remediation SLA
- [ ] Gap owners assigned (named individuals, not "IT team")
- [ ] Remediation actions specific and actionable
- [ ] Target dates realistic (not aspirational)
- [ ] Risk acceptance only for infeasible remediations (not laziness)


## Phase 10: Evidence & Approval (1-2 hours)

**Objective:** Collect evidence, complete Summary Dashboard, obtain executive approval.

**Sheets:** `Evidence_Register` and `Summary_Dashboard`

**Step-by-Step:**

**1. Collect Evidence for ALL Assessments:**
   
   **Environment Inventory Evidence:**

   - CMDB export (all systems)
   - Cloud provider resource lists (AWS, Azure, GCP inventory)
   - Network discovery scan results
   - SaaS subscription list
   

   **Masking Deployment Evidence:**

   - Masking tool configuration screenshots
   - Masked data sample (REDACTED, showing patterns only)
   - Data refresh script with masking step
   - DDM role configuration
   

   **Access Control Evidence:**

   - Access logs (who accessed unmasked production data)
   - Role definitions (which roles see masked vs. unmasked)
   - Exception approval forms (Data Owner + CISO signatures)
   

   **Encryption Evidence:**

   - Backup encryption certificates
   - Key management policy
   - Encryption verification (storage encrypted status)
   

   **External Sharing Evidence:**

   - Data Processing Agreements (DPAs)
   - Risk acceptance forms
   - Data transfer logs


**2. Complete Evidence_Register:**
   
   For EACH piece of evidence:

   - **Evidence ID:** EV-ENV-001, EV-PROD-001, etc.
   - **Evidence Type:** Configuration / Screenshot / Log / Agreement / Script / Report
   - **Description:** What this evidence proves
   - **Related Environment:** Which environment(s) this evidence supports
   - **Document Name/Link:** File name or URL
   - **Date Created:** When evidence collected
   - **Owner:** Who collected evidence
   - **Retention Period:** How long to keep (align with records management)
   - **Location:** Folder path or document repository location


**3. Complete Summary_Dashboard:**
   
   **Dashboard Auto-Calculates:**

   - Total environments assessed
   - Compliant / Partial / Non-Compliant counts
   - Coverage percentages (target: 100% non-production, ≥90% production)
   - Critical gap count (target: 0)
   - Average remediation time
   

   **Review Dashboard and Verify:**

   - Do numbers match reality? (sanity check formulas)
   - Are critical gaps highlighted in red? (visual indicator for executives)
   - Is overall compliance score accurate? (weighted average)


**4. Obtain Approvals:**
   
   **Required Signatures (in Summary_Dashboard):**

   - **IT Operations Manager:** Assessment completed and environments verified
   - **CISO:** Risk assessment and gap remediation plan approved
   - **Data Protection Officer (DPO):** Regulatory compliance validated
   - **CFO (if needed):** Budget approved for masking tools/resources


**5. Post-Approval Actions:**
   
   **Immediate:**

   - Communicate P1 gaps to gap owners (≤30 day SLA starts)
   - Schedule weekly gap remediation tracking meetings
   - Assign resources for masking implementation
   

   **Within 30 Days:**

   - Close all P1 gaps (unmasked non-production is non-negotiable)
   - Implement automated masking checkpoints
   - Procure masking tools if needed
   

   **Quarterly:**

   - Re-run environment inventory (new systems, decommissioned systems)
   - Verify P2/P3 gap remediation progress
   - Update assessment workbook


---

**END OF PART I - SECTION 3**

**Next Sections:**

- Section 4: Common Pitfalls & Troubleshooting
- Section 5: Evidence Collection
- Section 6: Quality Checklist
- Section 7: Review & Approval Process
- Section 8: Maintenance & Updates


**Shall I continue with Section 4: Common Pitfalls & Troubleshooting?**

# ISMS-IMP-A.8.11.3 - Environment Coverage Assessment
# PART I: USER COMPLETION GUIDE - SECTION 4 (FINAL)

---

# Common Pitfalls & Troubleshooting

## "We Can't Find All Our Environments"

**Problem:** Organization has grown organically, no central CMDB, environments scattered across on-prem and multiple cloud providers.

**Solution: Multi-Pronged Discovery Approach**

**Step 1: Start with What You Know**

- Billing systems (if you're paying for it, it exists)
- Production monitoring tools (what's being monitored = what's critical)
- Backup systems (what's being backed up = what exists)
- Change management records (what was deployed in last 24 months)


**Step 2: Follow the Money**

- AWS/Azure/GCP billing console → List all charged resources
- SaaS subscriptions (procurement records, credit card statements)
- Datacenter colocation invoices (what racks are you renting?)


**Step 3: Follow the People**

- Interview team leads: "What systems do your people use daily?"
- Ask developers: "Where do you push code?"
- Ask DBAs: "Which databases do you administer?"
- Ask cloud team: "Which cloud accounts exist?"


**Step 4: Network Discovery (Last Resort)**

- Port scanning (with management approval, during maintenance window)
- DNS enumeration (find database.dev.company.com patterns)
- Cloud provider APIs (programmatic resource enumeration)


**Document in Gap_Analysis:**

- GAP-XXX: "Environment discovery incomplete, estimated 30% coverage"
- Remediation: "Implement CMDB, mandate all new systems registered within 7 days"
- Owner: IT Operations Manager
- Target: 90 days


**Accept Reality:**

- First pass may only find 60-70% of environments (that's normal)
- Quarterly reviews will discover forgotten environments
- Shadow IT is called "shadow" for a reason (hard to find by definition)


---

## "Dev Team Says They NEED Real Production Data"

**Problem:** Developers insist masked data doesn't work for realistic testing, want production data copy.

**Counter-Arguments (From Policy):**

**Argument 1: "Masked data breaks our tests"**

- **Response:** Then your tests are testing data, not code. Fix the tests.
- **Technical Solution:** 
  - Format-preserving masking (credit card 4111-1111-1111-1111 stays valid Luhn)
  - Referential integrity preserved (Customer_ID 12345 masked to 98765 consistently across all tables)
  - Realistic patterns (masked emails still @validomain.com, phone numbers valid format)


**Argument 2: "We need to debug production issues"**

- **Response:** Debug in production with role-based DDM (masked for most, unmasked for authorized debuggers only)
- **Alternative:** Reproduce issue in test environment with synthetic data matching production scenario


**Argument 3: "Masking is too slow, we can't wait for data refresh"**

- **Response:** Static Data Masking (SDM) is one-time cost, subsequent refreshes are fast (copy masked database)
- **Solution:** Pre-masked "golden copy" environment (mask once, clone many times)


**Argument 4: "We need production scale for performance testing"**

- **Response:** Data synthesis can generate millions of realistic records faster than copying production
- **Tools:** Mockaroo, Faker libraries, custom data generators


**Escalation Path:**
1. Developer request → DBA rejects (policy requirement)
2. Developer escalates to manager → Manager reviews policy (non-negotiable)
3. Manager requests exception → CISO reviews (requires Data Owner approval)
4. CISO approves with compensating controls OR denies and enforces policy

**Document in Evidence_Register:**

- "Developer request for unmasked dev data - DENIED per policy ISMS-POL-A.8.11, Section 2.3 (Environment Coverage Requirements)"
- Approval chain: Developer → Manager → CISO (DENIED)


---

## "Cloud Sandbox Accounts Keep Multiplying"

**Problem:** Developers spin up AWS/Azure/GCP accounts for POCs, forget about them, now hundreds of orphaned resources with production data.

**Solution: Cloud Account Governance**

**Preventive Controls:**
1. **Mandate Approval Workflow:**

   - New cloud account requires IT approval (not self-service)
   - Account purpose documented (what project, how long needed)
   - Auto-expire after 90 days unless renewed


2. **Tagging Requirements:**

   - All cloud resources tagged: Owner, Environment (dev/test/prod), Project, Expiry Date
   - Untagged resources = terminated after 7-day warning


3. **Cost Alerts:**

   - Alert if account spend >$100/month (indicates significant usage)
   - Monthly account review (are all accounts still needed?)


4. **Data Residency Controls:**

   - Block production data copy to cloud dev accounts (DLP rules)
   - Allow only masked data exports to cloud sandbox


**Detective Controls:**
1. **Quarterly Cloud Inventory:**

   - AWS: `aws organizations list-accounts`
   - Azure: `az account list`
   - GCP: `gcloud projects list`
   - Reconcile with approved account list


2. **Automated Scanning:**

   - Cloud Security Posture Management (CSPM) tools
   - Detect unencrypted databases, public S3 buckets, overprivileged IAM


**Document as Ongoing Process:**

- Not a one-time assessment, continuous monitoring
- Add to quarterly review cycle
- Assign cloud team ownership


---

## "Vendor Refuses to Accept Masked Data"

**Problem:** Vendor contract requires production data for support/integration, refuses masked data, threatens to void warranty.

**Negotiation Strategy:**

**Step 1: Challenge the Requirement**

- **Ask:** "Which specific fields require real values for your support?"
- **Often:** They only need system IDs, timestamps, error messages (not customer PII)
- **Propose:** Mask PII, provide real system metadata


**Step 2: Propose Alternatives**

- **Synthetic Data:** Generate realistic test data matching production patterns
- **Data Sampling:** Provide subset (1,000 records, not full production dump)
- **On-Site Support:** Vendor accesses production on YOUR systems (VPN, time-limited, logged)


**Step 3: Escalate Internally**

- Legal review: Does contract actually require unmasked data? (re-read fine print)
- Procurement: Can we use different vendor? (competitive pressure)
- Risk acceptance: If truly required, CISO + Data Owner + Legal approval (document compensating controls)


**Step 4: Amend Contract (If Renewing)**

- Add clause: "Vendor shall accept masked/synthetic data for non-production testing"
- Add clause: "Vendor data access must comply with our data protection policy"
- Add clause: "Vendor breaches = contract termination + liability"


**Document Risk Acceptance (If Unavoidable):**

- **Justification:** "Vendor X requires unmasked data per contract clause Y, no alternative vendor available, business-critical system"
- **Compensating Controls:** NDA, DPA, encrypted transfer, access logging, time-limited access (delete after support resolved), audit rights
- **Approvals:** Data Owner + CISO + Legal + CFO (if contract >$X value)
- **Review:** Quarterly (is this still necessary?)


---

## "Backup System Cannot Mask Without Breaking Restore"

**Problem:** Full database backups are byte-for-byte copies, masking would corrupt backup and prevent disaster recovery.

**Solution: Encryption + Selective Masking**

**Understand the Technical Constraint:**

- Full backups: Exact replica needed for point-in-time recovery
- Transaction logs: Sequential, masking breaks chain
- Incremental backups: Delta changes, masking invalidates baseline


**Acceptable Approach:**

**Primary Backups (Production Recovery):**

- Keep unmasked (functional requirement)
- MUST be encrypted (AES-256 minimum)
- MUST have strict access controls (only backup admins can restore)
- MUST have audit logging (who restored what, when)


**Secondary Backups (Non-Production Use):**

- Create separate masked backup for testing purposes
- Process: Restore to staging → Mask → Export as "test dataset"
- This is acceptable (separate use case from disaster recovery)


**DR/Standby Sites:**

- Hot standby: Must be exact replica (masking breaks replication)
- Warm/Cold standby: Can mask if acceptable RTO (restore time objective) increases
- Decision: Trade-off between compliance and recovery time


**Document in Backup_Archive Sheet:**

- "Production backups unmasked (required for restore), encrypted AES-256, access restricted to 3 backup admins, restore operations logged"
- "Test backups created monthly from masked staging copy, no production backup restore to dev/test"


**Risk Acceptance:**

- Approved by: CISO + Data Owner
- Rationale: "Technical limitation, no masking solution exists for byte-level backups"
- Compensating Controls: Encryption, access restriction, logging
- Review: Annual (check if new technology enables backup masking)


---

## "We Found Unmasked Production Data in 47 Non-Prod Environments"

**Problem:** First environment coverage assessment reveals massive non-compliance (the "oh crap" moment).

**Response: Triage and Sprint**

**Immediate Actions (Week 1):**

**Day 1: CISO Briefing**

- Present findings: 47 non-compliant environments (be honest, don't sugarcoat)
- Explain risk: GDPR/FADP violation, PCI-DSS non-compliance, ISO 27001 audit failure
- Request resources: Budget, priority, executive support


**Day 2-3: Triage**

- Priority 1 (10-15 environments): Contain highest risk
  - Environments with PCI data (credit cards) → Immediate masking or shutdown
  - Environments with health data (HIPAA) → Immediate masking or shutdown
  - Environments with contractor/offshore access → Restrict access immediately
- Priority 2 (20-25 environments): Standard remediation
  - Dev/Test/UAT with customer PII → 30-day remediation SLA
- Priority 3 (10-15 environments): Lower risk
  - Training, sandbox with anonymized or old data → 90-day remediation SLA


**Day 4-5: Quick Wins**

- Shutdown unused environments (if nobody needs it, delete it)
- Restrict access to non-compliant environments (until masking deployed)
- Enable audit logging (detect if anyone accesses unmasked data)


**Sprint Remediation (30 Days):**

**Week 1-2: Tool Procurement & Setup**

- If no masking tool → Emergency procurement (work with vendors for fast setup)
- If have masking tool → Expand licenses, train additional DBAs
- Setup masking "factory" (standardized process for masking non-prod)


**Week 3-4: Bulk Masking**

- Mask P1 environments (high risk)
- Parallel track: Mask P2 environments (standard risk)
- Quality checks: Verify masking worked (automated validation)


**Post-Sprint: Process Fix**

- Root cause: WHY did 47 environments become non-compliant?
  - No approval required for non-prod data refresh?
  - DBAs didn't know policy?
  - Masking tool too complicated?
- Solution: Mandatory masking in data refresh scripts (cannot copy prod data without masking step)


**Document as Case Study:**

- "Initial assessment found 47 non-compliant environments (2024-Q1)"
- "30-day sprint remediation: 15 P1 environments masked, 25 P2 environments masked, 7 decommissioned"
- "Process improvement: Automated masking checkpoint in all data refresh scripts (prevents recurrence)"


---

# Evidence Collection

## What Evidence to Collect

**For Environment Inventory:**

- [ ] CMDB export (all systems, databases, applications)
- [ ] Cloud provider inventory (AWS RDS list, Azure SQL list, GCP Cloud SQL list)
- [ ] SaaS subscription list
- [ ] Network discovery scan results (if used)
- [ ] Billing records (proof of cloud accounts, SaaS platforms)


**For Production Environment DDM:**

- [ ] DDM configuration screenshots (masked fields per role)
- [ ] User role definitions (who sees what)
- [ ] Access logs (privileged users accessing unmasked data)
- [ ] Masking policy enforcement screenshots (application layer)


**For Non-Production Coverage:**

- [ ] Data refresh script with masking step (proof masking automated)
- [ ] Masked data sample (REDACTED, showing patterns only, not actual data)
- [ ] Coverage validation report (100% of sensitive fields masked)
- [ ] Before/after comparison (production vs. masked, redacted)


**For Analytics/Reporting:**

- [ ] BI tool configuration (masked views, aggregated datasets)
- [ ] Data warehouse ETL job definition (masking transformation step)
- [ ] Sample reports (verify individual-level PII not visible)


**For Cloud Environments:**

- [ ] Cloud account inventory (AWS Organizations, Azure Management Groups, GCP Projects)
- [ ] Cloud resource tagging compliance (Owner, Environment, Expiry tags)
- [ ] Cloud masking configuration (RDS instance settings, BigQuery column-level security)


**For Backup/Archive:**

- [ ] Backup encryption certificate (AES-256)
- [ ] Key management policy (KMS configuration)
- [ ] Backup access control list (who can restore)
- [ ] Restore operation logs (audit trail)


**For External Sharing:**

- [ ] Data Processing Agreements (DPAs) with vendors
- [ ] Risk acceptance forms (Data Owner + CISO signatures)
- [ ] Data transfer logs (SFTP logs, API logs)
- [ ] Vendor access review (quarterly access certification)


**For Data Flow Mapping:**

- [ ] ETL job definitions (Informatica, Talend, Airflow DAGs)
- [ ] Data flow diagrams (Visio, Lucidchart)
- [ ] Masking checkpoint validation scripts (automated tests)
- [ ] Pipeline failure alerts (proof masking failures are detected)


## Evidence Storage & Organization

**Recommended Folder Structure:**
```
Evidence/ISMS-A.8.11.3_Environment_Coverage/
├── 01_Environment_Inventory/
│   ├── CMDB_Export_20260120.xlsx
│   ├── AWS_Resource_Inventory_20260120.json
│   ├── Azure_Resource_List_20260120.csv
│   ├── GCP_Projects_List_20260120.txt
│   └── SaaS_Subscriptions_20260120.pdf
│
├── 02_Production_Environments/
│   ├── DDM_Configuration_CRM_20260120.png
│   ├── User_Roles_Definition_20260120.xlsx
│   ├── Access_Logs_Sample_20260120.csv (REDACTED)
│   └── Masking_Policy_Application_Layer_20260120.docx
│
├── 03_NonProduction_Environments/
│   ├── Data_Refresh_Script_Dev_Database_20260120.sql
│   ├── Masked_Data_Sample_REDACTED_20260120.xlsx
│   ├── Coverage_Validation_Report_20260120.pdf
│   └── Before_After_Comparison_REDACTED_20260120.png
│
├── 04_Analytics_Reporting/
│   ├── BI_Tool_Masked_Views_Config_20260120.png
│   ├── Data_Warehouse_ETL_Masking_Step_20260120.xml
│   └── Sample_Report_No_PII_20260120.pdf
│
├── 05_Cloud_Environments/
│   ├── Cloud_Account_Inventory_All_Providers_20260120.xlsx
│   ├── Resource_Tagging_Compliance_Report_20260120.pdf
│   └── Cloud_Masking_Configuration_Screenshots_20260120.zip
│
├── 06_Backup_Archive/
│   ├── Backup_Encryption_Certificate_20260120.pdf
│   ├── KMS_Key_Management_Policy_20260120.docx
│   ├── Backup_ACL_Who_Can_Restore_20260120.xlsx
│   └── Restore_Operation_Logs_6_Months_20260120.csv
│
├── 07_External_Sharing/
│   ├── Vendor_DPAs_All_Executed_20260120.zip
│   ├── Risk_Acceptance_Forms_Signed_20260120.pdf
│   ├── Data_Transfer_Logs_SFTP_20260120.csv
│   └── Vendor_Access_Quarterly_Review_20260120.xlsx
│
└── 08_Data_Flow_Mapping/
    ├── ETL_Job_Definitions_Masking_Steps_20260120.zip
    ├── Data_Flow_Diagram_All_Environments_20260120.vsdx
    ├── Masking_Checkpoint_Validation_Scripts_20260120.py
    └── Pipeline_Failure_Alert_Config_20260120.json
```

**Evidence Retention:**

- Current assessment: 3 years minimum (ISO 27001 compliance)
- Superseded assessments: 1 year (historical reference)
- Critical evidence (DPAs, risk acceptances): 7 years (legal requirement)


---

# Quality Checklist

**Before submitting assessment for approval, verify:**

## Completeness Checks

**Environment Inventory:**

- [ ] ALL production environments documented (100% coverage verified against billing, monitoring)
- [ ] ALL non-production environments documented (dev, test, UAT, staging, training, sandbox)
- [ ] ALL cloud environments inventoried (AWS, Azure, GCP, multi-cloud, SaaS)
- [ ] Backup/DR/Archive systems documented
- [ ] External sharing arrangements cataloged
- [ ] Shadow IT proactively searched (not just "what we already knew about")
- [ ] Decommissioned systems tracked (retention period documented)
- [ ] Environment owners assigned (all environments)
- [ ] No "Unknown" masking status without gap entry


**Production Environment Assessment:**

- [ ] DDM deployed where role-based access required
- [ ] Masked fields documented per user role
- [ ] Unmasked access logged and monitored
- [ ] Access logs reviewed monthly (process documented)
- [ ] Exceptions formally approved (Data Owner + CISO)
- [ ] Production Environment Checklist (18 items) all addressed


**Non-Production Coverage (CRITICAL):**

- [ ] 100% coverage target for all non-production environments with production data
- [ ] <100% coverage documented as gap with remediation plan
- [ ] Data refresh scripts include masking step (automated, not manual)
- [ ] Developer/contractor access counts documented
- [ ] No unmasked production data in dev/test/UAT (verified via spot checks)
- [ ] Non-Production Checklist (20 items) all addressed


**Analytics/Reporting:**

- [ ] Individual-level PII masked or aggregated
- [ ] BI tools query masked views (verified by login as analyst)
- [ ] Data warehouse ETL includes masking step (job definitions reviewed)
- [ ] Analytics platform access counts documented
- [ ] Analytics Checklist (15 items) all addressed


**Cloud Environments:**

- [ ] Cloud accounts inventoried (AWS Organizations, Azure Management Groups, GCP Projects)
- [ ] Cloud resources follow same masking rules as on-prem (no cloud exemption)
- [ ] Cloud dev/test databases 100% masked
- [ ] SaaS platforms data protection verified (vendor questionnaires)
- [ ] Cloud Environment Checklist (18 items) all addressed


**Backup/Archive:**

- [ ] Encryption verified for all backups containing sensitive data (AES-256 minimum)
- [ ] Backup access restricted (principle of least privilege)
- [ ] Restore operations logged (audit trail)
- [ ] Masking applied where technically feasible (export backups for testing)
- [ ] Backup Checklist (12 items) all addressed


**External Sharing:**

- [ ] DPAs in place for all data processors (GDPR Art. 28 compliance)
- [ ] Unmasked sharing has formal risk acceptance (Data Owner + CISO)
- [ ] Data transfer methods secure (encrypted in transit)
- [ ] Access time-limited where possible (revoke after project ends)
- [ ] External Sharing Checklist (15 items) all addressed


**Data Flow Mapping:**

- [ ] Major data flows mapped (production → non-prod, analytics, external)
- [ ] Masking checkpoints identified for flows with sensitive data
- [ ] Checkpoint implementation verified (not just documented)
- [ ] Failure handling defined (masking fails → flow stops)
- [ ] Data Flow Checklist (12 items) all addressed


**Gap Analysis:**

- [ ] All gaps consolidated from all assessment sheets
- [ ] Priority assigned (P1/P2/P3/P4) based on objective criteria
- [ ] P1 gaps have ≤30 day remediation SLA
- [ ] Gap owners assigned (named individuals)
- [ ] Remediation actions specific and actionable
- [ ] Target dates realistic
- [ ] Risk acceptance only for infeasible remediations (with compensating controls)


## Evidence Checks

- [ ] Minimum 20 evidence items in Evidence_Register (one per major finding)
- [ ] Evidence covers all assessment areas (environment inventory, masking deployment, access control, encryption, external sharing, data flows)
- [ ] Evidence files referenced by name/location (not vague "we have documentation")
- [ ] Evidence collection dates documented
- [ ] Evidence retention period defined (align with records management policy)
- [ ] Evidence stored securely (some evidence contains infrastructure details)


## Approval Checks

- [ ] Assessment completed by qualified personnel (IT Operations Manager, Infrastructure Lead, or designee)
- [ ] Quality review performed by independent reviewer (CISO, Security Manager, or senior operations)
- [ ] Data Owners have reviewed and approved gaps/exceptions for their data categories
- [ ] CISO has reviewed and approved overall assessment and gap remediation plan
- [ ] Sign-off sheet completed with signatures and dates
- [ ] Next review date scheduled (quarterly for environment updates)


---

# Review & Approval Process

## Review Workflow

```
┌──────────────────────────────────────────────────────────────┐
│ STEP 1: Self-Review                                         │
│ - Assessor completes quality checklist (Section 6)          │
│ - Verify all yellow cells filled (no blanks in critical fields) │
│ - Run formula checks (Summary_Dashboard calculates correctly) │
│ - Collect evidence files (20+ items minimum)                │
│ Duration: 2-3 hours                                         │
└────────────────┬─────────────────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────────────────┐
│ STEP 2: IT Operations Review                                │
│ - DBAs verify environment inventory accuracy                │
│ - Cloud team verifies cloud resource inventory              │
│ - DevOps verifies data flow mapping                         │
│ Duration: 2-3 business days                                 │
└────────────────┬─────────────────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────────────────┐
│ STEP 3: Security Review                                     │
│ - Security team verifies masking deployment status          │
│ - Validate gap priority assignments                         │
│ - Review risk acceptances for completeness                  │
│ Duration: 1-2 business days                                 │
└────────────────┬─────────────────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────────────────┐
│ STEP 4: Data Owner Review                                   │
│ - Data Owners approve gaps/exceptions for their categories  │
│ - Confirm remediation timelines acceptable                  │
│ Duration: 3-5 business days (stakeholder coordination)      │
└────────────────┬─────────────────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────────────────┐
│ STEP 5: Legal/Compliance Review                             │
│ - Legal confirms DPAs in place for external sharing         │
│ - Compliance validates backup retention periods             │
│ - Privacy Officer confirms GDPR/FADP compliance              │
│ Duration: 2-3 business days                                 │
└────────────────┬─────────────────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────────────────┐
│ STEP 6: Executive Approval (CISO)                           │
│ - CISO reviews Summary_Dashboard                            │
│ - Reviews P1 gaps and 30-day remediation commitment         │
│ - Approves resource allocation for gap remediation          │
│ - Signs approval sheet                                      │
│ Duration: 1 business day (executive calendar permitting)    │
└────────────────┬─────────────────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────────────────┐
│ STEP 7: Publish & Communicate                               │
│ - Save final approved version with date stamp               │
│ - Upload to ISMS document repository                        │
│ - Communicate P1 gap assignments to gap owners              │
│ - Schedule weekly gap remediation tracking meetings         │
│ - Schedule quarterly environment inventory review (3 months)│
│ Duration: 1 hour                                            │
└──────────────────────────────────────────────────────────────┘
```

**Total Workflow Duration:** 2-3 weeks (from completion to approval)

## Approval Sign-Off Sheet

**Required Signatures (in Excel `Summary_Dashboard` sheet):**

| Role | Name | Signature | Date | Comments |
|------|------|-----------|------|----------|
| **IT Operations Manager** | [Name] | [Digital signature or "Approved via email [date]"] | DD.MM.YYYY | Environment inventory completed and verified |
| **Chief Information Security Officer (CISO)** | [Name] | [Signature] | DD.MM.YYYY | Gap analysis and remediation plan approved, resources allocated for P1 gaps (30-day SLA) |
| **Data Protection Officer (DPO)** | [Name] | [Signature] | DD.MM.YYYY | Regulatory compliance validated (GDPR, FADP external sharing requirements) |
| **Legal/Compliance Officer** | [Name] | [Signature] | DD.MM.YYYY | DPAs validated, risk acceptances reviewed |

**Optional (depending on organization):**

- **CFO:** If significant budget required for masking tools or cloud resources
- **CTO / VP Engineering:** If infrastructure changes required (new environments, decommissions)


## Post-Approval Actions

**Immediate (Within 1 Week):**

- [ ] Communicate approved assessment to all gap owners
- [ ] Assign P1 gap remediation teams (30-day clock starts)
- [ ] Schedule weekly gap remediation status meetings (track progress)
- [ ] Add to ISMS audit evidence repository


**Short-Term (Within 30 Days):**

- [ ] Close all P1 gaps (unmasked non-production, unencrypted backups, high-risk external sharing)
- [ ] Implement automated masking checkpoints in data refresh scripts
- [ ] Procure masking tools if needed (vendor selection, licensing, deployment)


**Medium-Term (Within 90 Days):**

- [ ] Close all P2 gaps (production DDM, analytics masking, cloud coverage)
- [ ] Document remediation evidence (proof gaps closed)
- [ ] Update environment inventory (capture new environments, decommission old)


**Ongoing (Quarterly):**

- [ ] Re-run environment inventory (new systems deployed, systems decommissioned)
- [ ] Verify P3/P4 gap remediation progress
- [ ] Update assessment workbook
- [ ] Track compliance trend (improving or degrading?)


**Annual:**

- [ ] Full environment coverage re-assessment (comprehensive review)
- [ ] Re-validate masking coverage (schema changes may have introduced gaps)
- [ ] Audit previous year's environment changes
- [ ] Update assessment and obtain re-approval


---

# Maintenance & Updates

## Quarterly Review Cycle

**Trigger Events for Quarterly Review:**

- New environment deployments (databases, applications, cloud resources)
- Environment decommissions (retirement, migration)
- Cloud account changes (new subscriptions, closed accounts)
- External sharing arrangements (new vendors, contract renewals)
- Regulatory changes (new GDPR guidance, PCI-DSS updates)


**Quarterly Review Checklist:**

- [ ] Update Environment_Inventory (add new, remove decommissioned)
- [ ] Verify masking coverage for new environments (100% non-production)
- [ ] Review external sharing DPAs (expiring contracts, new vendors)
- [ ] Update cloud account inventory (AWS/Azure/GCP quarterly reconciliation)
- [ ] Review P2/P3 gap remediation progress (on track for deadlines?)
- [ ] Update Summary_Dashboard metrics (compliance trend)


**Duration:** 3-4 hours per quarter (maintenance, not full re-assessment)

## Change Management Integration

**Process: New Environment Deployment**
1. IT submits change request for new database/application/cloud resource
2. Change approval workflow includes: "Does this environment contain sensitive data?"
3. If YES → Trigger mini-assessment:

   - Add to Environment_Inventory
   - Classify environment type (production, non-production, analytics, etc.)
   - Determine masking requirement (mandatory for non-prod, conditional for prod)
   - Verify masking deployed BEFORE go-live (if non-production)

4. Update IMP-A.8.11.3 workbook
5. If non-production → MUST be masked before deployment (no exceptions)

**Process: Environment Decommission**
1. IT submits decommission request
2. Check Environment_Inventory: Does this environment contain sensitive data?
3. If YES → Data retention check:

   - Backup retention period satisfied? (verify against Backup_Archive sheet)
   - Legal hold? (litigation, regulatory investigation)
   - Export needed? (archive before decommission)

4. Update Environment_Inventory status: "Decommissioned [Date]"
5. Schedule data destruction per retention policy

**Process: Cloud Account Creation**
1. Developer requests AWS/Azure/GCP account
2. IT Operations approval required (documented in ticketing system)
3. Account tagged: Owner, Environment, Project, Expiry Date
4. If account will contain data → Add to Environment_Inventory
5. If non-production account → Masking mandatory before production data copy
6. Auto-expire after 90 days unless renewed (prevent orphaned accounts)

## Continuous Monitoring

**Automated Checks (Weekly):**

- [ ] Cloud account inventory sync (detect new accounts automatically)
- [ ] Untagged cloud resources (alert if resources missing required tags)
- [ ] Backup failures (encryption not applied, backup access anomalies)
- [ ] Access log review (unusual production data access patterns)


**Manual Checks (Monthly):**

- [ ] Data refresh script review (verify masking step still present)
- [ ] External sharing access review (who still has access, should it be revoked?)
- [ ] Exception renewals (quarterly exceptions expiring, need approval renewal)
- [ ] Gap remediation status (P2/P3 gaps on track?)


---

# Integration with Other Assessments

This assessment (IMP-A.8.11.3) integrates with:

**ISMS-IMP-A.8.11.1 (Data Inventory & Classification):**

- **Input:** System inventory (which systems contain sensitive data)
- **Input:** Sensitive data categories (PII, financial, health, credentials)
- **Usage:** Determine which environments require masking based on data sensitivity


**ISMS-IMP-A.8.11.2 (Masking Technique Selection):**

- **Input:** Approved masking techniques per data type (SDM, DDM, tokenization, etc.)
- **Usage:** Verify appropriate techniques deployed in each environment type


**ISMS-IMP-A.8.11.4 (Testing & Validation):**

- **Output:** Environment list for testing (which environments to validate masking effectiveness)
- **Output:** Coverage gaps requiring testing priority (P1 gaps test first)


**ISMS-IMP-A.8.11.5 (Compliance Dashboard):**

- **Output:** Environment coverage metrics (% non-production masked, % production DDM, etc.)
- **Output:** Gap count and remediation status (feeds into executive dashboard)


**Cross-Reference Example:**

- IMP-A.8.11.1 identifies: "Customer database contains PII (Critical sensitivity)"
- IMP-A.8.11.2 specifies: "PII SHALL be masked using SDM in non-production"
- **IMP-A.8.11.3 verifies:** "Dev/Test/UAT customer databases 100% masked using SDM"
- IMP-A.8.11.4 tests: "Masked dev database passed completeness test (100% coverage)"
- IMP-A.8.11.5 reports: "Non-production coverage: 100% (Compliant)"


---

**END OF PART I: USER COMPLETION GUIDE**

---

# PART II: TECHNICAL SPECIFICATION

---

## Document Control

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.11.3 - Part II |
| **Version** | 1.0 |
| **Document Type** | Excel Workbook Layout Specification |
| **Related Policy** | ISMS-POL-A.8.11, Section 2.3 (Environment Coverage Requirements) |
| **Purpose** | Define complete technical specification for Environment Coverage Assessment Excel workbook generation |
| **Target Audience** | Python Developers, ISMS Implementation Teams, Automation Engineers |
| **Assessment Type** | Technical Specification for Automated Workbook Generation |
| **Date** | [Date] |

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial workbook layout specification | ISMS Implementation Team |

---

# PART II: TECHNICAL SPECIFICATION

**Purpose:** This document provides the complete technical specification for generating the ISMS-IMP-A.8.11.3 Environment Coverage Assessment Excel workbook using Python (openpyxl library).

**Target Audience:** Python developers implementing the `generate_assessment_3_environment_coverage.py` script.

**What This Document Provides:**

- Complete workbook structure (12 sheets with exact specifications)
- Column definitions with data types and validation rules
- Styling and formatting standards (colors, fonts, borders)
- Formula definitions for automated calculations
- Data validation dropdown lists
- Cell protection strategies
- Quality assurance requirements


**Implementation Note:** This specification is designed for openpyxl-based generation. All sheet names, column headers, cell references, and formulas must match exactly for dashboard consolidation scripts to work correctly.

---

# Workbook Structure Overview

## Sheet Summary (12 Sheets)

| Sheet # | Sheet Name | Purpose | Row Count | Assessment Focus |
|---------|------------|---------|-----------|------------------|
| 1 | Instructions_Legend | User guidance, color legend, policy requirements | ~120 | Documentation |
| 2 | Environment_Inventory | Complete catalog of ALL environments | 50 data rows | Environment discovery |
| 3 | Production_Environment | Production DDM assessment, role-based masking | 30 data rows | Production compliance |
| 4 | NonProduction_Environments | Dev/Test/UAT/Staging masking (100% coverage) | 30 data rows | **CRITICAL** Non-prod coverage |
| 5 | Analytics_Reporting | BI, data warehouse, ML platform masking | 30 data rows | Analytics compliance |
| 6 | Backup_Archive | Backup encryption, archive masking | 30 data rows | Backup/DR controls |
| 7 | External_Sharing | Vendor, auditor, customer data sharing | 30 data rows | Third-party risk |
| 8 | Cloud_Environments | AWS, Azure, GCP, SaaS platform masking | 30 data rows | Cloud compliance |
| 9 | Data_Flow_Mapping | ETL pipelines, data movement, masking checkpoints | 30 data rows | Data flow analysis |
| 10 | Gap_Analysis | Consolidated gaps, remediation roadmap | 40 data rows | Gap tracking |
| 11 | Evidence_Register | Supporting documentation, audit trail | 100 data rows | Evidence management |
| 12 | Summary_Dashboard | Executive KPIs, compliance metrics | ~100 rows | Executive reporting |

**Total Data Capacity:** 400+ environment assessments, 100 evidence items, 40 gaps

**File Naming Convention:**  
`ISMS-IMP-A.8.11.3_Environment_Coverage_Assessment_YYYYMMDD.xlsx`

**Example:**  
`ISMS-IMP-A.8.11.3_Environment_Coverage_Assessment_20260120.xlsx`

---

# Standard Column Structure (Used Across Sheets 2-9)

## Base Columns (A-Q, 17 columns)

These standard columns appear on assessment sheets 2-9 with consistent definitions:

| Column | Header | Width | Type | Validation Options | Notes |
|--------|--------|-------|------|-------------------|-------|
| A | Environment Name | 25 | Text | Free text | User-defined environment identifier |
| B | Environment Type | 20 | Dropdown | Production, Development, Testing, UAT, Staging, Training, Sandbox, Analytics, Cloud, Backup, Archive, External | Standardized environment classification |
| C | Classification | 18 | Dropdown | Sensitive, Confidential, Internal, Public | Data classification level |
| D | Hosting Location | 18 | Dropdown | On-Premises, AWS, Azure, GCP, Hybrid, Other Cloud | Infrastructure location |
| E | Data Sensitivity | 18 | Dropdown | PII, Financial, Health, Credentials, Proprietary, Mixed, None | Type of sensitive data |
| F | Masking Required? | 18 | Dropdown | ✅ Mandatory, ⚠️ Conditional, ❌ Not Required, N/A | Policy-driven requirement |
| G | Masking Deployed? | 18 | Dropdown | Yes, No, Partial, Planned, N/A | Current deployment status |
| H | Masking Technique | 20 | Dropdown | SDM, DDM, Tokenization, Encryption, Redaction, Substitution, Anonymization, None | Technique from IMP-A.8.11.2 |
| I | Masking Tool/Solution | 22 | Text | Free text | Tool name if deployed |
| J | Coverage % | 12 | Percentage | 0-100% | Numeric percentage |
| K | Last Verified Date | 15 | Date | Date picker (dd.mm.yyyy) | Last masking verification |
| L | Environment Owner | 20 | Text | Free text | IT Operations contact |
| M | Data Owner | 20 | Text | Free text | Business contact from IMP-A.8.11.1 |
| N | Exception Approved? | 15 | Dropdown | Yes, No, N/A | Formal exception approval |
| O | Compliance Status | 18 | Dropdown | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A | Overall status |
| P | Notes/Comments | 30 | Text | Free text, wrapped | Additional context |
| Q | Evidence ID | 15 | Text | Free text (e.g., EV-ENV-001) | Link to Evidence_Register |

**Extended Columns (R-X):** Added per sheet for specific assessment needs (varies by sheet).

---

# Global Styling Standards

## Color Palette

| Element | RGB | Hex | Usage |
|---------|-----|-----|-------|
| Header (Main) | 0, 51, 102 | #003366 | Dark Blue - Main sheet titles |
| Subheader | 68, 114, 196 | #4472C4 | Medium Blue - Section headers |
| Column Headers | 217, 217, 217 | #D9D9D9 | Light Gray - Table headers |
| Input Cells | 255, 255, 204 | #FFFFCC | Light Yellow - User input required |
| Status - Compliant | 198, 239, 206 | #C6EFCE | Light Green - ✅ |
| Status - Partial | 255, 235, 156 | #FFEB9C | Light Yellow - ⚠️ |
| Status - Non-Compliant | 255, 199, 206 | #FFC7CE | Light Red - ❌ |
| Status - Planned | 180, 199, 231 | #B4C7E7 | Light Blue - Planned |
| Example Rows | 231, 230, 230 | #E7E6E6 | Light Gray - Example data |

## Font Standards

- **Main Headers:** Calibri 14-16pt Bold, White text on #003366 background
- **Subheaders:** Calibri 11-12pt Bold, White text on #4472C4 background
- **Column Headers:** Calibri 10pt Bold, Black text on #D9D9D9 background
- **Data Cells:** Calibri 10pt Regular, Black text
- **Example Rows:** Calibri 10pt Italic, Gray text on #E7E6E6 background


## Border Standards

- **Outer borders:** Medium weight (2pt), black
- **Inner borders:** Thin weight (1pt), black
- **Header separator:** Thick bottom border (3pt), black


## Cell Protection Strategy

**Protected (Locked):**

- All column headers
- All formula cells
- All reference tables and legends
- All instructions and example rows


**Unprotected (Unlocked):**

- All yellow input cells (#FFFFCC background)
- All user data entry rows
- Sign-off fields in Summary_Dashboard


---

# Sheet 1: Instructions_Legend

## Header Section (Rows 1-2)

**Row 1 - Main Title:**

- **Merge:** A1:Q1
- **Text:** "ISMS Control A.8.11.3 - Environment Coverage Assessment"
- **Font:** Calibri 14pt Bold, White
- **Fill:** #003366 (Dark Blue)
- **Alignment:** Center, Vertical Center
- **Row Height:** 40px


**Row 2 - Subtitle:**

- **Merge:** A2:Q2
- **Text:** "ISO/IEC 27001:2022 - Data Masking Policy Compliance"
- **Font:** Calibri 11pt Bold, White
- **Fill:** #4472C4 (Medium Blue)
- **Alignment:** Center, Vertical Center
- **Row Height:** 25px


## Document Information Block (Rows 4-12)

**Two-column layout:**

| Row | Column A (Label) | Column B-D (Value - Yellow Input) |
|-----|------------------|-----------------------------------|
| 4 | Document ID: | ISMS-IMP-A.8.11.3 |
| 5 | Assessment Area: | Environment Coverage & Deployment |
| 6 | Related Policy: | ISMS-POL-A.8.11, Section 2.3 (Environment Coverage Requirements) |
| 7 | Version: | 1.0 |
| 8 | Assessment Date: | [USER INPUT - yellow cell] |
| 9 | Completed By: | [USER INPUT - yellow cell] |
| 10 | Organization: | [USER INPUT - yellow cell] |
| 11 | Review Cycle: | Quarterly |

**Column A Styling:**

- Font: Calibri 10pt Bold
- Alignment: Right-aligned


**Columns B-D Styling:**

- Font: Calibri 10pt Regular
- Fill: #FFFFCC (Yellow) for input rows 8-10
- Fill: White for static values
- Borders: Thin all sides


## How to Use This Workbook Section (Rows 14-25)

**Row 14 - Section Header:**

- **Merge:** A14:Q14
- **Text:** "HOW TO USE THIS WORKBOOK"
- **Font:** Calibri 12pt Bold
- **Fill:** #4472C4 (Medium Blue), White text
- **Row Height:** 30px


**Rows 16-25 - Instructions (Numbered List):**

1. Complete each worksheet tab in sequence (Environment Inventory → Production → Non-Production → etc.)
2. Fill ALL yellow-highlighted cells with your organization's specific information
3. Use dropdown menus where provided (do not type free-form text in dropdown cells)
4. Document ALL environments in your organization (include cloud, on-premises, hybrid)
5. For each environment, specify masking requirement (Mandatory/Conditional/Not Required) per policy S2.3
6. Verify masking deployment status (Yes/No/Partial/Planned)
7. Calculate coverage percentage (% of sensitive fields masked)
8. Link all assessments to Evidence Register with unique Evidence IDs
9. Complete Gap Analysis sheet to identify remediation needs
10. Review Summary Dashboard for executive-level compliance status

**Formatting:**

- Column A: Numbers (1-10)
- Columns B-Q: Instruction text (wrapped)
- Font: Calibri 10pt Regular
- Row Height: Auto (wrapped text)


## Color Legend Section (Rows 27-32)

**Row 27 - Section Header:**

- **Text:** "COLOR LEGEND"
- **Styling:** Same as Row 14


**Rows 29-32 - Legend Items:**

| Row | Color Sample (Col A) | Description (Cols B-Q) |
|-----|----------------------|------------------------|
| 29 | #FFFFCC (Yellow fill) | Yellow cells = User input required |
| 30 | #C6EFCE (Green fill) | Green status = Compliant (masking deployed as required) |
| 31 | #FFEB9C (Yellow fill) | Yellow status = Partial compliance (some masking gaps) |
| 32 | #FFC7CE (Red fill) | Red status = Non-compliant (masking required but not deployed) |
| 33 | #B4C7E7 (Blue fill) | Blue status = Planned (remediation in progress) |

**Column A:** Fill with corresponding color, no border
**Columns B-Q:** Description text, Calibri 10pt Regular

## Environment Classification Reference Table (Rows 35-49)

**Row 35 - Table Header:**

- **Text:** "ENVIRONMENT CLASSIFICATION REFERENCE"
- **Styling:** #4472C4 header


**Row 37 - Column Headers:**

| Column | Header | Width |
|--------|--------|-------|
| A | Environment Type | 20 |
| B | Definition | 35 |
| C | Masking Requirement | 25 |
| D | Typical Technique | 20 |

**Styling:** #D9D9D9 background, Calibri 10pt Bold, centered

**Rows 38-49 - Reference Data:**

| Environment Type | Definition | Masking Requirement | Typical Technique |
|-----------------|------------|---------------------|-------------------|
| Production | Live operational systems | ⚠️ Conditional (DDM for role-based) | DDM, Field-level encryption |
| Development | Software development | ✅ Mandatory | SDM |
| Testing/QA | Quality assurance | ✅ Mandatory | SDM |
| UAT | User acceptance testing | ✅ Mandatory | SDM |
| Staging | Pre-production validation | ✅ Mandatory (unless prod-identical) | SDM or DDM |
| Training | Employee training systems | ✅ Mandatory | SDM + Substitution |
| Sandbox | Experimental/POC work | ✅ Mandatory | SDM |
| Analytics | BI, reporting, data warehouse | ✅ Mandatory | Aggregation, Anonymization |
| Cloud | Third-party hosted (AWS/Azure/GCP) | ✅ Follows same rules as on-prem | Varies by cloud env type |
| Backup | Disaster recovery backups | ⚠️ Conditional (encryption required) | Encryption at rest |
| Archive | Long-term retention | ⚠️ Conditional (assess feasibility) | Encryption or masking |
| External | Data shared outside org | ✅ Mandatory (unless contractual) | Redaction, Aggregation |

**Cell Styling:**

- Column A: Text, left-aligned
- Columns B-D: Text, wrapped, left-aligned
- All cells: Thin borders
- Alternating row shading (optional): Light gray on even rows


## Policy Requirements Summary (Rows 51-67)

**Row 51 - Section Header:**

- **Text:** "POLICY REQUIREMENTS SUMMARY - KEY POINTS"
- **Styling:** #4472C4 header


**Rows 53-67 - Requirements (Numbered List with Icons):**

1. ✅ ALL non-production environments SHALL be masked (Policy S2.3 Section 3.2)
2. ✅ Production data SHALL NOT be copied to non-prod without masking
3. ✅ Analytics and reporting environments SHALL mask individual-level PII
4. ✅ External data sharing SHALL be masked unless contractually required
5. ✅ Cloud environments SHALL follow same masking rules as on-premises
6. ⚠️ Production environments MAY use DDM for role-based access control
7. ⚠️ Backup environments MAY contain unmasked data if encrypted and access-controlled
8. ❌ Direct production database cloning without masking is PROHIBITED
9. ❌ "We'll mask it later" approach is NOT acceptable
10. ❌ NDAs are NOT a substitute for technical masking controls
11. 📊 Coverage target: 100% of non-production environments masked
12. 📊 Exception limit: ≤5% of environments may have approved exceptions
13. 📋 All exceptions require ISO and Data Owner approval
14. 📋 Exceptions must be reviewed quarterly
15. 🔍 Masking effectiveness must be validated (see A.8.11.4 Testing)

**Formatting:**

- Icons as Unicode characters (✅ ⚠️ ❌ 📊 📋 🔍)
- Font: Calibri 10pt Regular
- Column A: Number + Icon
- Columns B-Q: Requirement text (wrapped)
- Important requirements (1-5) in Bold


---

# Sheet 2: Environment_Inventory

## Header (Rows 1-2)

**Row 1 - Sheet Title:**

- **Merge:** A1:Q1
- **Text:** "ENVIRONMENT INVENTORY"
- **Font:** Calibri 14pt Bold, White
- **Fill:** #003366 (Dark Blue)
- **Alignment:** Center, Vertical Center
- **Row Height:** 35px


**Row 2 - Policy Reference:**

- **Merge:** A2:Q2
- **Text:** "All information processing environments must be cataloged and classified for masking applicability (ISMS-POL-A.8.11, Section 2.3 (Environment Coverage Requirements) Section 2)"
- **Font:** Calibri 10pt Italic
- **Fill:** #E7E6E6 (Light Gray)
- **Alignment:** Center, Vertical Center, Wrapped
- **Row Height:** Auto (wrapped)


## Assessment Question (Rows 4-5)

**Row 4 - Question:**

- **Merge:** A4:O4
- **Text:** "Does your organization maintain a complete inventory of ALL environments where data is processed, stored, or transmitted?"
- **Font:** Calibri 10pt Bold
- **Alignment:** Left, Vertical Center, Wrapped


**Cell P4 - Response:**

- **Data Validation:** Dropdown list: "Yes, No, Partial, In Progress"
- **Fill:** #FFFFCC (Yellow)
- **Font:** Calibri 10pt Regular
- **Alignment:** Center


**Cell Q4 - Label:**

- **Text:** "Response:"
- **Font:** Calibri 10pt Bold
- **Alignment:** Right


## Column Headers (Row 6)

**Standard 17 columns (A-Q) as defined in Standard Column Structure section above.**

**Row 6 Styling:**

- **Fill:** #D9D9D9 (Light Gray)
- **Font:** Calibri 10pt Bold, Black
- **Alignment:** Center, Vertical Center, Wrapped
- **Border:** Thick bottom border (3pt)
- **Row Height:** 40px (to accommodate wrapped text)


## Example Row (Row 7) - Gray Italic

**Purpose:** Provide example data to guide users

**Row 7 Data:**

- A7: "Production CRM Database"
- B7: "Production"
- C7: "Sensitive"
- D7: "On-Premises"
- E7: "PII"
- F7: "⚠️ Conditional"
- G7: "Yes"
- H7: "DDM"
- I7: "[Your masking tool name]"
- J7: "95%"
- K7: "01.01.2026"
- L7: "IT Operations Manager"
- M7: "Customer Data Owner"
- N7: "N/A"
- O7: "✅ Compliant"
- P7: "DDM applied for customer service reps"
- Q7: "EV-ENV-001"


**Row 7 Styling:**

- **Fill:** #E7E6E6 (Light Gray)
- **Font:** Calibri 10pt Italic, Gray text (#808080)
- **Border:** Thin all sides
- **Cell Protection:** Locked (user cannot edit example)


## Data Entry Rows (8-57)

**50 rows for environment inventory**

**Row 8-57 Styling:**

- **Fill:** #FFFFCC (Light Yellow) - All cells
- **Font:** Calibri 10pt Regular, Black
- **Border:** Thin all sides
- **Cell Protection:** Unlocked (user input)
- **Row Height:** 20px (standard)


**Data Validation per Column:**

**Column A (Environment Name):** Text, no validation
**Column B (Environment Type):** Dropdown list:
```
Production, Development, Testing, UAT, Staging, Training, Sandbox, Analytics, Cloud, Backup, Archive, External
```

**Column C (Classification):** Dropdown list:
```
Sensitive, Confidential, Internal, Public
```

**Column D (Hosting Location):** Dropdown list:
```
On-Premises, AWS, Azure, GCP, Hybrid, Other Cloud
```

**Column E (Data Sensitivity):** Dropdown list:
```
PII, Financial, Health, Credentials, Proprietary, Mixed, None
```

**Column F (Masking Required?):** Dropdown list:
```
✅ Mandatory, ⚠️ Conditional, ❌ Not Required, N/A
```

**Column G (Masking Deployed?):** Dropdown list:
```
Yes, No, Partial, Planned, N/A
```

**Column H (Masking Technique):** Dropdown list:
```
SDM, DDM, Tokenization, Encryption, Redaction, Substitution, Anonymization, None
```

**Column I (Masking Tool/Solution):** Text, no validation

**Column J (Coverage %):** Number validation:

- Type: Whole number
- Minimum: 0
- Maximum: 100
- Format: "0%"


**Column K (Last Verified Date):** Date validation:

- Type: Date
- Format: "dd.mm.yyyy"
- Allow blank: Yes


**Columns L-M (Owners):** Text, no validation

**Column N (Exception Approved?):** Dropdown list:
```
Yes, No, N/A
```

**Column O (Compliance Status):** Dropdown list:
```
✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A
```

**Conditional Formatting for Column O:**

- If "✅ Compliant" → Fill #C6EFCE (Green)
- If "⚠️ Partial" → Fill #FFEB9C (Yellow)
- If "❌ Non-Compliant" → Fill #FFC7CE (Red)
- If "N/A" → No fill (white)


**Columns P-Q:** Text, no validation

## Compliance Checklist (Rows 60-76)

**Row 60 - Section Header:**

- **Merge:** A60:Q60
- **Text:** "ENVIRONMENT INVENTORY CHECKLIST"
- **Font:** Calibri 12pt Bold
- **Fill:** #4472C4 (Medium Blue), White text
- **Row Height:** 30px


**Row 62 - Checklist Column Headers:**

| Column | Header | Width |
|--------|--------|-------|
| A | ☐ | 5 |
| B | Requirement | 50 |
| C | Status | 15 |
| D | Notes | 30 |

**Styling:** #D9D9D9 background, Calibri 10pt Bold

**Rows 63-76 - Checklist Items (15 items):**

| Item | Requirement | Status Dropdown | Notes |
|------|-------------|-----------------|-------|
| ☐ | All production environments documented | [Dropdown] | [Text input] |
| ☐ | All non-production environments documented (Dev/Test/UAT/Sandbox) | [Dropdown] | [Text input] |
| ☐ | All analytics/reporting environments documented | [Dropdown] | [Text input] |
| ☐ | All cloud environments documented (AWS/Azure/GCP/Other) | [Dropdown] | [Text input] |
| ☐ | All backup/archive systems documented | [Dropdown] | [Text input] |
| ☐ | External data sharing destinations documented | [Dropdown] | [Text input] |
| ☐ | Each environment classified (Sensitive/Confidential/Internal/Public) | [Dropdown] | [Text input] |
| ☐ | Data sensitivity level assigned per environment | [Dropdown] | [Text input] |
| ☐ | Masking requirement determined (Mandatory/Conditional/Not Required) | [Dropdown] | [Text input] |
| ☐ | Environment owners assigned | [Dropdown] | [Text input] |
| ☐ | Data owners assigned | [Dropdown] | [Text input] |
| ☐ | Hosting location documented (On-Prem/Cloud) | [Dropdown] | [Text input] |
| ☐ | Environment inventory reviewed in last 6 months | [Dropdown] | [Text input] |
| ☐ | New environments added to inventory within 30 days of deployment | [Dropdown] | [Text input] |
| ☐ | Decommissioned environments removed from inventory | [Dropdown] | [Text input] |

**Status Column Dropdown:**
```
✅ Complete, ⚠️ Partial, ❌ Missing, N/A
```

**Conditional Formatting for Status:**

- ✅ Complete → Fill #C6EFCE (Green)
- ⚠️ Partial → Fill #FFEB9C (Yellow)
- ❌ Missing → Fill #FFC7CE (Red)
- N/A → No fill


---

# Sheet 3: Production_Environment

## Header (Rows 1-2)

**Row 1 - Sheet Title:**

- **Merge:** A1:X1 (Note: Extended to X for additional columns)
- **Text:** "PRODUCTION ENVIRONMENT ASSESSMENT"
- **Font:** Calibri 14pt Bold, White
- **Fill:** #003366 (Dark Blue)
- **Row Height:** 35px


**Row 2 - Policy Reference:**

- **Merge:** A2:X2
- **Text:** "Production environments may use Dynamic Data Masking (DDM) for role-based access. All access to unmasked data must be logged. (ISMS-POL-A.8.11, Section 2.3 (Environment Coverage Requirements) Section 3.1)"
- **Font:** Calibri 10pt Italic
- **Fill:** #E7E6E6 (Light Gray)
- **Row Height:** Auto (wrapped)


## Assessment Question (Rows 4-5)

**Row 4:**

- **Merge:** A4:U4
- **Text:** "Does your organization implement role-based masking (DDM) in production environments to restrict access to sensitive data?"
- **Font:** Calibri 10pt Bold


**Cell V4 - Response:**

- **Data Validation:** Dropdown: "Yes, No, Partial, Planned"
- **Fill:** #FFFFCC (Yellow)


**Cell W4-X4 - Label:**

- **Merge:** W4:X4
- **Text:** "Response:"
- **Alignment:** Right


## Column Headers (Row 6)

**Standard Columns A-Q** (as defined in Standard Column Structure)

**PLUS Extended Columns R-X:**

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| R | User Role/Group | 20 | Text | Free text |
| S | Masked Fields | 25 | Text | Free text (comma-separated list) |
| T | Unmasked Access Logged? | 15 | Dropdown | Yes, No, N/A |
| U | Access Control Method | 20 | Dropdown | RBAC, ABAC, ACL, Manual, None |
| V | Exception Justification | 30 | Text | Free text, wrapped |
| W | Risk Level | 12 | Dropdown | High, Medium, Low, None |
| X | Remediation Target Date | 15 | Date | Date picker (dd.mm.yyyy) |

**Row 6 Styling:** Same as Sheet 2 (Environment_Inventory)

## Example Row (Row 7)

**Sample Production Environment with DDM:**

- A7: "Production CRM Database"
- B7: "Production"
- C7: "Sensitive"
- D7: "On-Premises"
- E7: "PII"
- F7: "⚠️ Conditional"
- G7: "Yes"
- H7: "DDM"
- I7: "Oracle Data Masking"
- J7: "95%"
- K7: "15.01.2026"
- L7: "DB Admin Team Lead"
- M7: "Customer Data Owner"
- N7: "N/A"
- O7: "✅ Compliant"
- P7: "DDM for customer service reps, helpdesk"
- Q7: "EV-PROD-001"
- R7: "Customer Service Representative"
- S7: "credit_card_number, ssn, date_of_birth"
- T7: "Yes"
- U7: "RBAC"
- V7: "N/A"
- W7: "Low"
- X7: "N/A"


**Styling:** Same gray italic example row format as Sheet 2

## Data Entry Rows (8-37)

**30 rows for production environment assessment**

**Styling:** Yellow input cells, same as Sheet 2

**Additional Validation for Extended Columns:**

**Column T (Unmasked Access Logged?):** Dropdown:
```
Yes, No, N/A
```

**Column U (Access Control Method):** Dropdown:
```
RBAC, ABAC, ACL, Manual, None
```

**Column W (Risk Level):** Dropdown:
```
High, Medium, Low, None
```

**Conditional Formatting for Column W:**

- High → Fill #FFC7CE (Red)
- Medium → Fill #FFEB9C (Yellow)
- Low → Fill #C6EFCE (Green)
- None → No fill


**Column X (Remediation Target Date):** Date format "dd.mm.yyyy"

## Compliance Checklist (Rows 40-59)

**Row 40 - Section Header:**

- **Text:** "PRODUCTION ENVIRONMENT CHECKLIST"
- **Styling:** #4472C4 header


**Rows 42-59 - Checklist Items (18 items):**

1. DDM implemented for role-based access in production
2. Customer service representatives see masked customer data
3. Production reports mask data for non-privileged users
4. Audit logs containing sensitive data are masked/encrypted
5. Application outputs (invoices, statements) use partial redaction
6. Production data exports are masked before release
7. All access to unmasked production data is logged
8. Access logs reviewed monthly for anomalies
9. Privileged user access to unmasked data requires justification
10. Masking exceptions documented with business justification
11. Exception approvals obtained from Data Owner and ISO
12. Exceptions reviewed quarterly
13. Production DDM configuration tested after schema changes
14. Role definitions documented (who sees what)
15. DDM bypass controls prevent unauthorized unmasked access
16. Production monitoring alerts on DDM failures
17. Incident response plan includes DDM failure scenarios
18. Annual DDM effectiveness review performed

**Status Dropdown:** Same as Sheet 2 (✅ Complete, ⚠️ Partial, ❌ Missing, N/A)

---

**END OF PART II - SECTION 1**

**Next Sections:**

- Section 2: Sheets 4-6 (NonProduction_Environments, Analytics_Reporting, Backup_Archive)
- Section 3: Sheets 7-9 (External_Sharing, Cloud_Environments, Data_Flow_Mapping)
- Section 4: Sheets 10-12 (Gap_Analysis, Evidence_Register, Summary_Dashboard)
- Section 5: Python Script Integration Notes, Quality Assurance Requirements


**Shall I continue with Section 2?**

# ISMS-IMP-A.8.11.3 - Environment Coverage Assessment
# PART II: TECHNICAL SPECIFICATION - SECTION 2

---

# Sheet 4: NonProduction_Environments

**⚠️ CRITICAL SHEET:** This sheet assesses the MANDATORY 100% masking coverage requirement for ALL non-production environments. Policy compliance depends on this assessment.

## Header (Rows 1-2)

**Row 1 - Sheet Title:**

- **Merge:** A1:X1
- **Text:** "NON-PRODUCTION ENVIRONMENTS - CRITICAL COMPLIANCE ASSESSMENT"
- **Font:** Calibri 14pt Bold, White
- **Fill:** #003366 (Dark Blue)
- **Row Height:** 35px


**Row 2 - Policy Reference:**

- **Merge:** A2:X2
- **Text:** "ALL non-production environments SHALL be masked (100% coverage). Production data SHALL NOT be copied to non-production without masking. (ISMS-POL-A.8.11, Section 2.3 (Environment Coverage Requirements) Section 3.2) - MANDATORY REQUIREMENT"
- **Font:** Calibri 10pt Bold Italic, Red text (#FF0000)
- **Fill:** #FFEB9C (Light Yellow - Warning color)
- **Alignment:** Center, Vertical Center, Wrapped
- **Row Height:** Auto (wrapped)


## Assessment Question (Rows 4-5)

**Row 4:**

- **Merge:** A4:U4
- **Text:** "Are ALL non-production environments (Dev/Test/UAT/Staging/Training/Sandbox) masked at 100% coverage?"
- **Font:** Calibri 10pt Bold, Red text


**Cell V4 - Response:**

- **Data Validation:** Dropdown: "Yes (100%), No (<100%), Partial, In Progress"
- **Fill:** #FFFFCC (Yellow)
- **Font:** Calibri 10pt Regular


**Cell W4-X4 - Label:**

- **Merge:** W4:X4
- **Text:** "Response:"
- **Alignment:** Right


**Row 5 - Warning:**

- **Merge:** A5:X5
- **Text:** "⚠️ WARNING: Any environment with <100% coverage is a CRITICAL GAP requiring immediate remediation (≤30 day SLA)"
- **Font:** Calibri 9pt Bold, Red text
- **Fill:** #FFC7CE (Light Red)
- **Alignment:** Center


## Column Headers (Row 7)

**Standard Columns A-Q** (as defined in Standard Column Structure)

**PLUS Extended Columns R-X:**

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| R | Data Refresh Frequency | 18 | Dropdown | Daily, Weekly, Monthly, Ad-hoc, Never |
| S | Refresh Process | 15 | Dropdown | Automated, Manual, Hybrid |
| T | Masking in Refresh Script? | 18 | Dropdown | Yes, No, N/A |
| U | Last Data Refresh Date | 15 | Date | Date picker (dd.mm.yyyy) |
| V | Next Refresh Date | 15 | Date | Date picker (dd.mm.yyyy) |
| W | Developer Access Count | 12 | Number | Whole number |
| X | Contractor Access? | 15 | Dropdown | Yes, No, N/A |

**Row 7 Styling:**

- **Fill:** #D9D9D9 (Light Gray)
- **Font:** Calibri 10pt Bold, Black
- **Alignment:** Center, Vertical Center, Wrapped
- **Border:** Thick bottom border (3pt)
- **Row Height:** 50px (more wrapped text due to longer headers)


## Example Row (Row 8)

**Sample Non-Production Environment:**

- A8: "Development Customer DB"
- B8: "Development"
- C8: "Sensitive"
- D8: "On-Premises"
- E8: "PII"
- F8: "✅ Mandatory"
- G8: "Yes"
- H8: "SDM"
- I8: "Informatica Data Masking"
- J8: "100%"
- K8: "18.01.2026"
- L8: "Dev Team Lead"
- M8: "Customer Data Owner"
- N8: "N/A"
- O8: "✅ Compliant"
- P8: "Weekly refresh with automated masking"
- Q8: "EV-NONPROD-001"
- R8: "Weekly"
- S8: "Automated"
- T8: "Yes"
- U8: "13.01.2026"
- V8: "20.01.2026"
- W8: "15"
- X8: "No"


**Styling:** Gray italic example row format (same as previous sheets)

## Data Entry Rows (9-38)

**30 rows for non-production environment assessment**

**Row 9-38 Styling:**

- **Fill:** #FFFFCC (Light Yellow) - All cells
- **Font:** Calibri 10pt Regular, Black
- **Border:** Thin all sides
- **Cell Protection:** Unlocked (user input)


**Data Validation for Extended Columns:**

**Column R (Data Refresh Frequency):** Dropdown:
```
Daily, Weekly, Monthly, Ad-hoc, Never
```

**Column S (Refresh Process):** Dropdown:
```
Automated, Manual, Hybrid
```

**Column T (Masking in Refresh Script?):** Dropdown:
```
Yes, No, N/A
```

**Conditional Formatting for Column T:**

- If "Yes" → Fill #C6EFCE (Green)
- If "No" → Fill #FFC7CE (Red) + Bold Red text
- If "N/A" → No fill


**Columns U-V (Dates):** Date format "dd.mm.yyyy"

**Column W (Developer Access Count):** Number validation:

- Type: Whole number
- Minimum: 0
- Maximum: 1000


**Column X (Contractor Access?):** Dropdown:
```
Yes, No, N/A
```

**Conditional Formatting for Column X:**

- If "Yes" → Fill #FFEB9C (Yellow) - Warning, third-party risk


**CRITICAL: Conditional Formatting for Column J (Coverage %):**

- If <100% → Fill #FFC7CE (Red) + Bold Red text + Red border (thick 3pt)
- If =100% → Fill #C6EFCE (Green)
- This visual indicator is CRITICAL for identifying gaps


**Conditional Formatting for Column O (Compliance Status):**

- Enhanced for this sheet:
- If "❌ Non-Compliant" → Fill #FFC7CE (Red) + Bold + Red border (thick 3pt all sides)


## Compliance Checklist (Rows 41-62)

**Row 41 - Section Header:**

- **Merge:** A41:X41
- **Text:** "NON-PRODUCTION ENVIRONMENT CHECKLIST - 100% COVERAGE REQUIRED"
- **Font:** Calibri 12pt Bold
- **Fill:** #FF0000 (Red), White text
- **Row Height:** 30px


**Rows 43-62 - Checklist Items (20 items):**

1. ✅ ALL non-production environments inventoried (Dev/Test/UAT/Staging/Training/Sandbox)
2. ✅ 100% masking coverage verified for ALL environments with production data
3. ✅ Data refresh scripts include automated masking step (not manual)
4. ✅ Direct production database cloning prohibited (policy enforced)
5. ✅ Developer workstations with local DB copies inventoried and masked
6. ✅ Ephemeral CI/CD test environments masked (automated in pipeline)
7. ✅ Contractor/offshore access restricted to masked environments only
8. ✅ Data refresh process documented (who, what, when, how)
9. ✅ Masking verification performed after each data refresh
10. ✅ Schema changes trigger re-masking (automated or documented process)
11. ❌ No environments with <100% coverage (if any exist, document as CRITICAL gap)
12. ❌ No "we'll mask it later" environments (policy prohibits deferral)
13. ⚠️ Training environments use synthetic/substitution data (preferred over masked production)
14. ⚠️ Sandbox/POC environments deleted after project completion (data minimization)
15. ⚠️ Non-production data retention limited (30-90 days typical, not indefinite)
16. 📋 Exception process: If <100% coverage, MUST have Data Owner + CISO approval
17. 📋 Exceptions documented in Gap_Analysis sheet with remediation plan
18. 📋 Exceptions reviewed quarterly (auto-expire after 90 days)
19. 🔍 Spot checks performed monthly (random non-prod environment verification)
20. 🔍 Annual comprehensive re-validation (all non-prod environments tested)

**Status Dropdown:** Same as previous sheets (✅ Complete, ⚠️ Partial, ❌ Missing, N/A)

**Notes Column:** Text input for explanations/exceptions

---

# Sheet 5: Analytics_Reporting

## Header (Rows 1-2)

**Row 1 - Sheet Title:**

- **Merge:** A1:W1
- **Text:** "ANALYTICS & REPORTING ENVIRONMENT ASSESSMENT"
- **Font:** Calibri 14pt Bold, White
- **Fill:** #003366 (Dark Blue)
- **Row Height:** 35px


**Row 2 - Policy Reference:**

- **Merge:** A2:W2
- **Text:** "Analytics and reporting environments SHALL mask individual-level PII. Aggregation and anonymization preferred over row-level masking. (ISMS-POL-A.8.11, Section 2.3 (Environment Coverage Requirements) Section 3.3)"
- **Font:** Calibri 10pt Italic
- **Fill:** #E7E6E6 (Light Gray)
- **Row Height:** Auto (wrapped)


## Assessment Question (Rows 4-5)

**Row 4:**

- **Merge:** A4:T4
- **Text:** "Are analytics and reporting environments configured to mask or aggregate individual-level PII?"
- **Font:** Calibri 10pt Bold


**Cell U4 - Response:**

- **Data Validation:** Dropdown: "Yes (Masked), Yes (Aggregated), Partial, No"
- **Fill:** #FFFFCC (Yellow)


**Cell V4-W4 - Label:**

- **Merge:** V4:W4
- **Text:** "Response:"
- **Alignment:** Right


## Column Headers (Row 6)

**Standard Columns A-Q** (as defined in Standard Column Structure)

**PLUS Extended Columns R-W:**

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| R | Platform Type | 20 | Dropdown | BI Tool, Data Warehouse, Data Lake, ML Platform, Reporting, Other |
| S | Data Granularity | 18 | Dropdown | Individual-level, Aggregated, Anonymized, Mixed |
| T | Analyst Access Count | 12 | Number | Whole number |
| U | External Access? | 15 | Dropdown | Yes (Vendors/Consultants), No, N/A |
| V | PII Visible? | 15 | Dropdown | Yes, No, Partial |
| W | Aggregation Level | 18 | Dropdown | Row-level, k≥5, k≥10, k≥20, Fully Aggregated, N/A |

**Row 6 Styling:** Same as previous sheets

## Example Row (Row 7)

**Sample Analytics Environment:**

- A7: "Snowflake Data Warehouse"
- B7: "Analytics"
- C7: "Confidential"
- D7: "AWS"
- E7: "PII"
- F7: "✅ Mandatory"
- G7: "Yes"
- H7: "Anonymization"
- I7: "Snowflake Dynamic Data Masking"
- J7: "100%"
- K7: "15.01.2026"
- L7: "Analytics Platform Manager"
- M7: "Customer Data Owner"
- N7: "N/A"
- O7: "✅ Compliant"
- P7: "k-anonymity ≥10 for all customer reports"
- Q7: "EV-ANALYTICS-001"
- R7: "Data Warehouse"
- S7: "Aggregated"
- T7: "25"
- U7: "Yes (Vendors/Consultants)"
- V7: "No"
- W7: "k≥10"


**Styling:** Gray italic example row

## Data Entry Rows (8-37)

**30 rows for analytics/reporting environment assessment**

**Styling:** Yellow input cells, standard format

**Data Validation for Extended Columns:**

**Column R (Platform Type):** Dropdown:
```
BI Tool, Data Warehouse, Data Lake, ML Platform, Reporting, Other
```

**Column S (Data Granularity):** Dropdown:
```
Individual-level, Aggregated, Anonymized, Mixed
```

**Conditional Formatting for Column S:**

- If "Individual-level" AND Column V="Yes" (PII Visible) → Fill #FFC7CE (Red) + Bold
- If "Aggregated" OR "Anonymized" → Fill #C6EFCE (Green)


**Column T (Analyst Access Count):** Number validation:

- Type: Whole number
- Minimum: 0
- Maximum: 1000


**Column U (External Access?):** Dropdown:
```
Yes (Vendors/Consultants), No, N/A
```

**Conditional Formatting for Column U:**

- If "Yes (Vendors/Consultants)" → Fill #FFEB9C (Yellow) - Warning flag


**Column V (PII Visible?):** Dropdown:
```
Yes, No, Partial
```

**Conditional Formatting for Column V:**

- If "Yes" → Fill #FFC7CE (Red) + Bold Red text
- If "No" → Fill #C6EFCE (Green)
- If "Partial" → Fill #FFEB9C (Yellow)


**Column W (Aggregation Level):** Dropdown:
```
Row-level, k≥5, k≥10, k≥20, Fully Aggregated, N/A
```

**Note:** k-anonymity means each record is indistinguishable from at least k-1 other records

## Compliance Checklist (Rows 40-56)

**Row 40 - Section Header:**

- **Text:** "ANALYTICS & REPORTING CHECKLIST"
- **Styling:** #4472C4 header


**Rows 42-56 - Checklist Items (15 items):**

1. All BI tools, data warehouses, data lakes inventoried
2. ML/AI platforms and training datasets inventoried
3. Individual-level PII masked or aggregated (no raw customer records)
4. BI dashboards query masked views (verified by analyst login)
5. Data warehouse ETL includes masking/aggregation step
6. Reporting platforms use aggregated data (minimum k≥5)
7. ML training datasets anonymized (models don't leak PII)
8. Export functionality restricted (analysts cannot export raw PII)
9. Ad-hoc query tools (SQL clients) access masked views only
10. Personal Excel/CSV exports prohibited (or automatically masked)
11. External consultant access limited to aggregated data
12. Vendor-hosted analytics (SaaS BI) have DPAs and masking
13. Data retention in analytics limited (not indefinite historical storage)
14. Analytics platform access logged and reviewed
15. Annual re-validation of aggregation effectiveness

**Status Dropdown:** Same as previous sheets

---

# Sheet 6: Backup_Archive

## Header (Rows 1-2)

**Row 1 - Sheet Title:**

- **Merge:** A1:X1
- **Text:** "BACKUP & ARCHIVE ASSESSMENT"
- **Font:** Calibri 14pt Bold, White
- **Fill:** #003366 (Dark Blue)
- **Row Height:** 35px


**Row 2 - Policy Reference:**

- **Merge:** A2:X2
- **Text:** "Backup environments MAY contain unmasked data IF encrypted (AES-256 minimum) and access-controlled. Masking required where technically feasible. Archive systems follow retention policies. (ISMS-POL-A.8.11, Section 2.3 (Environment Coverage Requirements) Section 3.4)"
- **Font:** Calibri 10pt Italic
- **Fill:** #E7E6E6 (Light Gray)
- **Row Height:** Auto (wrapped)


## Assessment Question (Rows 4-5)

**Row 4:**

- **Merge:** A4:U4
- **Text:** "Are all backups containing sensitive data encrypted at rest? Is masking applied where technically feasible?"
- **Font:** Calibri 10pt Bold


**Cell V4 - Response (Encryption):**

- **Data Validation:** Dropdown: "Yes (All Encrypted), Partial, No"
- **Fill:** #FFFFCC (Yellow)


**Cell W4 - Label:**

- **Text:** "Encryption:"
- **Alignment:** Right


**Row 5:**

- **Merge:** A5:U5
- **Text:** "Secondary question: Are export backups for testing purposes masked before distribution?"
- **Font:** Calibri 10pt Italic


**Cell V5 - Response (Masking):**

- **Data Validation:** Dropdown: "Yes, Partial, No, N/A (No exports)"
- **Fill:** #FFFFCC (Yellow)


**Cell W5 - Label:**

- **Text:** "Masking:"
- **Alignment:** Right


## Column Headers (Row 7)

**Standard Columns A-Q** (as defined in Standard Column Structure)

**PLUS Extended Columns R-X:**

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| R | Backup Type | 18 | Dropdown | Full, Incremental, Differential, Transaction Log, Snapshot, Archive |
| S | Backup Frequency | 15 | Dropdown | Hourly, Daily, Weekly, Monthly, Yearly |
| T | Retention Period | 15 | Dropdown | 7 days, 30 days, 90 days, 1 year, 3 years, 7 years, >7 years |
| U | Encryption Method | 18 | Dropdown | AES-256, TDE, Disk Encryption, None |
| V | Encryption at Rest? | 15 | Dropdown | Yes, No, Partial |
| W | Encryption in Transit? | 15 | Dropdown | Yes, No, N/A |
| X | Key Management | 18 | Dropdown | KMS, HSM, Manual, N/A |

**Additional Columns (Continue if needed):**

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| Y | Restore Access Control | 20 | Dropdown | Restricted (≤3 people), General (>3 people), None |
| Z | Masking Feasible? | 15 | Dropdown | Yes, No, Conditional |
| AA | Masking Applied? | 15 | Dropdown | Yes, No, N/A |

**Note:** Columns Y-AA extend beyond standard Q, requiring column width adjustments

**Row 7 Styling:** Same as previous sheets (may need to extend merge for title rows)

## Example Row (Row 8)

**Sample Backup System:**

- A8: "Production DB Daily Backup"
- B8: "Backup"
- C8: "Sensitive"
- D8: "On-Premises"
- E8: "PII"
- F8: "⚠️ Conditional"
- G8: "No (Encrypted instead)"
- H8: "Encryption"
- I8: "Veeam Backup"
- J8: "N/A"
- K8: "19.01.2026"
- L8: "Backup Administrator"
- M8: "IT Operations Manager"
- N8: "Yes (CISO approved)"
- O8: "✅ Compliant"
- P8: "Full backup encrypted AES-256, restore restricted to 2 admins"
- Q8: "EV-BACKUP-001"
- R8: "Full"
- S8: "Daily"
- T8: "30 days"
- U8: "AES-256"
- V8: "Yes"
- W8: "Yes"
- X8: "KMS"
- Y8: "Restricted (≤3 people)"
- Z8: "No"
- AA8: "N/A"


**Styling:** Gray italic example row

## Data Entry Rows (9-38)

**30 rows for backup/archive assessment**

**Styling:** Yellow input cells, standard format

**Data Validation for Extended Columns:**

**Column R (Backup Type):** Dropdown:
```
Full, Incremental, Differential, Transaction Log, Snapshot, Archive
```

**Column S (Backup Frequency):** Dropdown:
```
Hourly, Daily, Weekly, Monthly, Yearly
```

**Column T (Retention Period):** Dropdown:
```

7 days, 30 days, 90 days, 1 year, 3 years, 7 years, >7 years

```

**Column U (Encryption Method):** Dropdown:
```
AES-256, TDE, Disk Encryption, None
```

**Conditional Formatting for Column U:**

- If "None" AND Column E ≠ "None" (has sensitive data) → Fill #FFC7CE (Red) + Bold
- If "AES-256" OR "TDE" → Fill #C6EFCE (Green)
- If "Disk Encryption" → Fill #FFEB9C (Yellow) - Less secure than application-level


**Column V (Encryption at Rest?):** Dropdown:
```
Yes, No, Partial
```

**Conditional Formatting for Column V:**

- If "No" → Fill #FFC7CE (Red) + Bold Red text
- If "Yes" → Fill #C6EFCE (Green)


**Column W (Encryption in Transit?):** Dropdown:
```
Yes, No, N/A
```

**Column X (Key Management):** Dropdown:
```
KMS, HSM, Manual, N/A
```

**Column Y (Restore Access Control):** Dropdown:
```
Restricted (≤3 people), General (>3 people), None
```

**Conditional Formatting for Column Y:**

- If "None" → Fill #FFC7CE (Red)
- If "Restricted (≤3 people)" → Fill #C6EFCE (Green)
- If "General (>3 people)" → Fill #FFEB9C (Yellow)


**Column Z (Masking Feasible?):** Dropdown:
```
Yes, No, Conditional
```

**Column AA (Masking Applied?):** Dropdown:
```
Yes, No, N/A
```

**Conditional Logic for Columns Z-AA:**

- If Z="Yes" (feasible) AND AA="No" (not applied) → Red flag, potential gap
- If Z="No" (not feasible) AND V="Yes" (encrypted) → Acceptable (compensating control)


## Compliance Checklist (Rows 41-54)

**Row 41 - Section Header:**

- **Text:** "BACKUP & ARCHIVE CHECKLIST"
- **Styling:** #4472C4 header


**Rows 43-54 - Checklist Items (12 items):**

1. All backup systems inventoried (production, DR, archive)
2. Encryption verified for all backups containing sensitive data (AES-256 minimum)
3. Encryption at rest enabled (storage-level encryption)
4. Encryption in transit enabled (TLS 1.2+ for network backups)
5. Key management properly configured (KMS or HSM, not manual)
6. Key rotation policy in place (annual minimum)
7. Restore access restricted (principle of least privilege, ≤3 backup admins)
8. Restore operations logged (audit trail)
9. Masking applied where technically feasible (export backups for testing)
10. Backup retention periods align with legal requirements (documented in policy)
11. Offline/tape backups encrypted (physical media protection)
12. Annual restore test performed (validates encryption doesn't break recovery)

**Status Dropdown:** Same as previous sheets

## Reference Tables (Starting Row 58)

**Backup Encryption Best Practices Table:**

| Backup Type | Masking Feasible? | Recommended Approach | Rationale |
|-------------|-------------------|---------------------|-----------|
| Full Database Backup | No | Encryption only (AES-256) | Byte-for-byte restore required |
| Transaction Log Backup | No | Encryption only | Point-in-time recovery breaks if masked |
| DR Hot Standby | No | Encryption + replication | Must be exact replica for failover |
| Incremental Backup | No | Encryption only | Delta changes, masking breaks chain |
| Export for Testing | Yes | Mask BEFORE backup | Separate use case from disaster recovery |
| Archive (Compliance) | Conditional | Assess if restore needed | If no restore needed, can mask |
| File-level Backup | Yes | Mask files BEFORE backup | Especially for reports, exports |

**Retention Period Reference Table:**

| Data Category | Legal Minimum | Legal Maximum | Typical Retention |
|---------------|---------------|---------------|------------------|
| Financial Records | 7 years | N/A | 7 years |
| Tax Documents | 7 years | N/A | 7 years |
| Employee Records | 3 years (after termination) | N/A | 10 years |
| Customer Data | None (GDPR deletion) | N/A | 3-5 years (business need) |
| Health Data (HIPAA) | 6 years | N/A | 6 years |
| Audit Logs | 1 year (ISO 27001) | N/A | 2-3 years |

---

**END OF PART II - SECTION 2**

**Completed Sheets:**

- Sheet 1: Instructions_Legend ✅
- Sheet 2: Environment_Inventory ✅
- Sheet 3: Production_Environment ✅
- Sheet 4: NonProduction_Environments ✅
- Sheet 5: Analytics_Reporting ✅
- Sheet 6: Backup_Archive ✅


**Next Section 3:**

- Sheet 7: External_Sharing
- Sheet 8: Cloud_Environments
- Sheet 9: Data_Flow_Mapping


**Shall I continue with Section 3?**

# ISMS-IMP-A.8.11.3 - Environment Coverage Assessment
# PART II: TECHNICAL SPECIFICATION - SECTION 3

---

# Sheet 7: External_Sharing

## Header (Rows 1-2)

**Row 1 - Sheet Title:**

- **Merge:** A1:Y1
- **Text:** "EXTERNAL DATA SHARING ASSESSMENT"
- **Font:** Calibri 14pt Bold, White
- **Fill:** #003366 (Dark Blue)
- **Row Height:** 35px


**Row 2 - Policy Reference:**

- **Merge:** A2:Y2
- **Text:** "External data sharing SHALL be masked unless contractually required and formally risk-accepted by Data Owner + CISO. All external sharing requires DPA (GDPR Art. 28). (ISMS-POL-A.8.11, Section 2.3 (Environment Coverage Requirements) Section 3.5)"
- **Font:** Calibri 10pt Italic
- **Fill:** #E7E6E6 (Light Gray)
- **Row Height:** Auto (wrapped)


## Assessment Question (Rows 4-5)

**Row 4:**

- **Merge:** A4:V4
- **Text:** "Is all external data sharing (vendors, auditors, customers, partners) properly masked or formally approved as exception?"
- **Font:** Calibri 10pt Bold


**Cell W4 - Response:**

- **Data Validation:** Dropdown: "Yes (All Masked), Yes (Approved Exceptions), Partial, No"
- **Fill:** #FFFFCC (Yellow)


**Cell X4-Y4 - Label:**

- **Merge:** X4:Y4
- **Text:** "Response:"
- **Alignment:** Right


**Row 5 - Reminder:**

- **Merge:** A5:Y5
- **Text:** "⚠️ REMINDER: Data Processing Agreements (DPAs) required for ALL external processors per GDPR Art. 28"
- **Font:** Calibri 9pt Bold, Blue text (#003366)
- **Fill:** #B4C7E7 (Light Blue)
- **Alignment:** Center


## Column Headers (Row 7)

**Standard Columns A-Q** (as defined in Standard Column Structure)

**PLUS Extended Columns R-Y:**

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| R | External Party Name | 25 | Text | Free text (company/organization name) |
| S | External Party Type | 18 | Dropdown | Vendor, Partner, Auditor, Regulator, Customer, Offshore Team, Other |
| T | Purpose of Sharing | 25 | Text | Free text, wrapped |
| U | Contractual Requirement? | 18 | Dropdown | Yes (Unmasked Required), No (Can Be Masked), Conditional |
| V | DPA in Place? | 12 | Dropdown | Yes, No, N/A |
| W | Data Transfer Method | 18 | Dropdown | SFTP, API, Email (encrypted), Physical Media, Portal, Other |
| X | Transfer Frequency | 15 | Dropdown | One-time, Daily, Weekly, Monthly, On-demand |
| Y | Access Duration | 18 | Dropdown | Permanent, Temporary (specify end date in notes) |

**Additional Columns (if space permits):**

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| Z | Data Volume | 15 | Text | Number of records or file size |
| AA | Risk Assessment Done? | 15 | Dropdown | Yes, No, N/A |
| AB | CISO Approval Date | 15 | Date | Date picker (dd.mm.yyyy) |

**Row 7 Styling:** Same as previous sheets, extended merge for title rows

## Example Row (Row 8)

**Sample External Sharing Arrangement:**

- A8: "Vendor Support Portal"
- B8: "External"
- C8: "Confidential"
- D8: "Vendor SaaS"
- E8: "PII"
- F8: "✅ Mandatory"
- G8: "Yes"
- H8: "Redaction"
- I8: "Manual masking process"
- J8: "100%"
- K8: "10.01.2026"
- L8: "IT Operations Manager"
- M8: "Customer Data Owner"
- N8: "N/A"
- O8: "✅ Compliant"
- P8: "Support tickets with redacted customer details"
- Q8: "EV-EXT-001"
- R8: "TechSupport Inc."
- S8: "Vendor"
- T8: "Technical support and troubleshooting"
- U8: "No (Can Be Masked)"
- V8: "Yes"
- W8: "Portal"
- X8: "On-demand"
- Y8: "Permanent"
- Z8: "~50 tickets/month"
- AA8: "Yes"
- AB8: "05.12.2025"


**Styling:** Gray italic example row

## Data Entry Rows (9-38)

**30 rows for external sharing assessment**

**Styling:** Yellow input cells, standard format

**Data Validation for Extended Columns:**

**Column S (External Party Type):** Dropdown:
```
Vendor, Partner, Auditor, Regulator, Customer, Offshore Team, Other
```

**Conditional Formatting for Column S:**

- If "Offshore Team" → Fill #FFEB9C (Yellow) - Cross-border risk flag
- If "Regulator" → Fill #B4C7E7 (Blue) - Special handling


**Column U (Contractual Requirement?):** Dropdown:
```
Yes (Unmasked Required), No (Can Be Masked), Conditional
```

**Conditional Formatting for Column U:**

- If "Yes (Unmasked Required)" → Fill #FFEB9C (Yellow) - Requires exception approval
- If "No (Can Be Masked)" AND Column G="No" → Fill #FFC7CE (Red) - Should be masked


**Column V (DPA in Place?):** Dropdown:
```
Yes, No, N/A
```

**Conditional Formatting for Column V:**

- If "No" AND Column S = "Vendor" OR "Partner" OR "Offshore Team" → Fill #FFC7CE (Red) + Bold
  - **Rationale:** GDPR Art. 28 violation
- If "Yes" → Fill #C6EFCE (Green)


**Column W (Data Transfer Method):** Dropdown:
```
SFTP, API, Email (encrypted), Physical Media, Portal, Other
```

**Conditional Formatting for Column W:**

- If contains "Email" AND NOT "encrypted" → Flag as potential risk (note: requires text parsing)


**Column X (Transfer Frequency):** Dropdown:
```
One-time, Daily, Weekly, Monthly, On-demand
```

**Column Y (Access Duration):** Dropdown:
```
Permanent, Temporary (specify end date in notes)
```

**Conditional Formatting for Column Y:**

- If "Temporary" → Fill #B4C7E7 (Blue) - Ensure end date in notes


**Column AA (Risk Assessment Done?):** Dropdown:
```
Yes, No, N/A
```

**Conditional Formatting for Column AA:**

- If "No" AND Column U = "Yes (Unmasked Required)" → Fill #FFC7CE (Red)
  - **Rationale:** Unmasked sharing without risk assessment = policy violation


**Column AB (CISO Approval Date):** Date format "dd.mm.yyyy"

**Validation Logic Across Columns:**

- If Column G (Masking Deployed?) = "No" (unmasked)
  - THEN Column N (Exception Approved?) MUST = "Yes"
  - AND Column AA (Risk Assessment Done?) MUST = "Yes"
  - AND Column AB (CISO Approval Date) MUST NOT be blank
  - **Otherwise:** Red flag for gap analysis


## Compliance Checklist (Rows 41-57)

**Row 41 - Section Header:**

- **Text:** "EXTERNAL SHARING CHECKLIST"
- **Styling:** #4472C4 header


**Rows 43-57 - Checklist Items (15 items):**

1. All external data sharing arrangements documented (vendors, auditors, customers, partners)
2. DPAs in place for ALL data processors (GDPR Art. 28 mandatory)
3. Unmasked sharing has formal risk acceptance (Data Owner + CISO approval)
4. Risk assessments completed for all unmasked sharing
5. Data transfer methods secure (encrypted in transit - SFTP, TLS, encrypted email)
6. No unencrypted email attachments with sensitive data
7. Access is time-limited where feasible (revoke after project completion)
8. Quarterly access review (who still has access, is it still needed?)
9. Vendor contracts include data protection clauses
10. Offshore data transfers comply with GDPR/FADP cross-border requirements
11. Customer data exports limited to their data only (no over-sharing)
12. Auditor access documented and time-limited (delete data after audit)
13. Physical media transfers encrypted (USB drives, tapes)
14. Portal/API access logged (audit trail for external access)
15. Annual DPA review (contracts still valid, clauses current?)

**Status Dropdown:** Same as previous sheets

## Reference Table: Cross-Border Data Transfer Requirements (Starting Row 61)

**GDPR/FADP Cross-Border Transfer Mechanisms:**

| Mechanism | When Applicable | Requirements | Masking Impact |
|-----------|----------------|--------------|----------------|
| EU Adequacy Decision | Transfer to "adequate" countries (UK, Switzerland, Japan, etc.) | None (adequacy assumed) | Masking still required per purpose limitation |
| Standard Contractual Clauses (SCCs) | Transfer to non-adequate countries | Sign EU SCCs or Swiss TCC | Masking recommended, not waived by SCCs |
| Binding Corporate Rules (BCRs) | Intra-group transfers (multinational corporations) | BCR approval by DPA | Masking policy should be in BCRs |
| Consent | Individual consent for each transfer | Explicit, informed consent | Masking still best practice |
| Derogations | Limited, case-by-case transfers | Specific legal grounds (contract performance, legal claim, etc.) | Case-specific assessment |

**Note:** Masking requirements are independent of cross-border transfer mechanisms. Even with SCCs, data minimization (masking) is best practice.

---

# Sheet 8: Cloud_Environments

## Header (Rows 1-2)

**Row 1 - Sheet Title:**

- **Merge:** A1:X1
- **Text:** "CLOUD ENVIRONMENT ASSESSMENT"
- **Font:** Calibri 14pt Bold, White
- **Fill:** #003366 (Dark Blue)
- **Row Height:** 35px


**Row 2 - Policy Reference:**

- **Merge:** A2:X2
- **Text:** "Cloud environments SHALL follow same masking rules as on-premises. Cloud hosting does NOT exempt from masking requirements. (ISMS-POL-A.8.11, Section 2.3 (Environment Coverage Requirements) Section 3.6)"
- **Font:** Calibri 10pt Italic
- **Fill:** #E7E6E6 (Light Gray)
- **Row Height:** Auto (wrapped)


## Assessment Question (Rows 4-5)

**Row 4:**

- **Merge:** A4:U4
- **Text:** "Are cloud-hosted environments (AWS, Azure, GCP, SaaS) classified and masked according to same requirements as on-premises?"
- **Font:** Calibri 10pt Bold


**Cell V4 - Response:**

- **Data Validation:** Dropdown: "Yes (Same Rules), Partial, No"
- **Fill:** #FFFFCC (Yellow)


**Cell W4-X4 - Label:**

- **Merge:** W4:X4
- **Text:** "Response:"
- **Alignment:** Right


**Row 5 - Reminder:**

- **Merge:** A5:X5
- **Text:** "⚠️ CLOUD REMINDER: Production cloud = same as on-prem production. Non-prod cloud = 100% masking (same as on-prem non-prod)"
- **Font:** Calibri 9pt Bold
- **Fill:** #B4C7E7 (Light Blue)
- **Alignment:** Center


## Column Headers (Row 7)

**Standard Columns A-Q** (as defined in Standard Column Structure)

**PLUS Extended Columns R-X:**

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| R | Cloud Provider | 18 | Dropdown | AWS, Azure, GCP, Multi-Cloud, SaaS, Other |
| S | Cloud Service | 22 | Text | Free text (e.g., RDS, SQL Database, BigQuery, Salesforce) |
| T | Region/Location | 18 | Text | Free text (e.g., us-east-1, eu-central-1, Switzerland) |
| U | Account/Subscription ID | 20 | Text | Free text (for cloud resource tracking) |
| V | Multi-Tenant? | 12 | Dropdown | Yes (SaaS), No (Dedicated), N/A |
| W | Data Residency Compliant? | 18 | Dropdown | Yes, No, N/A |
| X | Cloud-Specific Controls | 25 | Text | Free text, wrapped (e.g., AWS Macie, Azure Purview) |

**Row 7 Styling:** Same as previous sheets

## Example Row (Row 8)

**Sample Cloud Environment:**

- A8: "AWS RDS Production Customer DB"
- B8: "Production"
- C8: "Sensitive"
- D8: "AWS"
- E8: "PII"
- F8: "⚠️ Conditional"
- G8: "Yes"
- H8: "DDM"
- I8: "AWS RDS Native Masking"
- J8: "90%"
- K8: "18.01.2026"
- L8: "Cloud Infrastructure Manager"
- M8: "Customer Data Owner"
- N8: "N/A"
- O8: "✅ Compliant"
- P8: "DDM for API access, encryption at rest"
- Q8: "EV-CLOUD-001"
- R8: "AWS"
- S8: "RDS PostgreSQL"
- T8: "eu-central-1 (Frankfurt)"
- U8: "123456789012/prod-db-cluster"
- V8: "No (Dedicated)"
- W8: "Yes"
- X8: "RDS encryption, IAM policies, CloudTrail logging"


**Styling:** Gray italic example row

## Data Entry Rows (9-38)

**30 rows for cloud environment assessment**

**Styling:** Yellow input cells, standard format

**Data Validation for Extended Columns:**

**Column R (Cloud Provider):** Dropdown:
```
AWS, Azure, GCP, Multi-Cloud, SaaS, Other
```

**Column V (Multi-Tenant?):** Dropdown:
```
Yes (SaaS), No (Dedicated), N/A
```

**Conditional Formatting for Column V:**

- If "Yes (SaaS)" → Fill #FFEB9C (Yellow) - Vendor-managed risk


**Column W (Data Residency Compliant?):** Dropdown:
```
Yes, No, N/A
```

**Conditional Formatting for Column W:**

- If "No" → Fill #FFC7CE (Red) - GDPR/FADP data residency violation


## Compliance Checklist (Rows 41-60)

**Row 41 - Section Header:**

- **Text:** "CLOUD ENVIRONMENT CHECKLIST"
- **Styling:** #4472C4 header


**Rows 43-60 - Checklist Items (18 items):**

1. All cloud accounts/subscriptions inventoried (AWS, Azure, GCP, multi-cloud)
2. Cloud resources tagged (Owner, Environment, Project, Data Classification)
3. Cloud production environments follow on-prem production rules (DDM conditional)
4. Cloud non-production environments 100% masked (same as on-prem non-prod)
5. SaaS platforms data protection verified (vendor questionnaires, certifications)
6. IaaS/PaaS databases classified (same as on-prem databases)
7. Cloud dev/test databases masked (no "it's just cloud dev" exemption)
8. Cloud sandbox accounts governed (approval required, auto-expire)
9. Cloud storage buckets (S3, Blob, GCS) containing sensitive data encrypted
10. Cloud-native masking tools configured (AWS Macie, Azure Purview, GCP DLP)
11. Data residency requirements met (GDPR/FADP compliant regions)
12. Cross-region replication masked (if replicating to non-compliant regions)
13. Cloud backup/snapshot encryption enabled (same as on-prem backup requirements)
14. Cloud access logged (CloudTrail, Activity Log, Cloud Audit Logs)
15. Multi-cloud environments consistent (no cloud provider exemptions)
16. SaaS vendor DPAs in place (GDPR Art. 28)
17. Cloud cost alerts configured (detect forgotten resources)
18. Quarterly cloud inventory reconciliation (billing vs. documented resources)

**Status Dropdown:** Same as previous sheets

## Cloud Provider-Specific Reference Table (Starting Row 64)

**Cloud-Native Masking & Data Protection Tools:**

| Cloud Provider | Data Discovery | Masking/Encryption | Access Control | Monitoring |
|----------------|----------------|-------------------|----------------|------------|
| **AWS** | Macie (PII discovery) | RDS encryption, S3 encryption, KMS | IAM policies, SCPs | CloudTrail, GuardDuty |
| **Azure** | Purview (data catalog) | SQL TDE, Disk encryption, Key Vault | RBAC, Entra ID | Activity Log, Sentinel |
| **GCP** | Cloud DLP (sensitive data) | Cloud SQL encryption, Cloud KMS | IAM, VPC Service Controls | Cloud Audit Logs, SCC |
| **Multi-Cloud** | Third-party tools (BigID, Collibra) | Cross-cloud masking tools | Centralized IAM (Okta, etc.) | SIEM aggregation |

**SaaS Platform Data Protection Checklist:**

| SaaS Platform | PII Storage? | DPA Required? | Data Residency Control? | Masking Available? |
|---------------|--------------|---------------|------------------------|-------------------|
| Salesforce | Yes (CRM data) | Yes | Yes (region selection) | Field-level encryption, Shield |
| Workday | Yes (HR data) | Yes | Yes (regional datacenters) | Limited (vendor manages) |
| ServiceNow | Yes (tickets) | Yes | Yes (instance location) | Field-level encryption |
| Office 365 | Yes (emails, files) | Yes | Yes (geo selection) | Sensitivity labels, DLP |
| Google Workspace | Yes (emails, Drive) | Yes | Yes (region preference) | DLP, encryption at rest |

---

# Sheet 9: Data_Flow_Mapping

## Header (Rows 1-2)

**Row 1 - Sheet Title:**

- **Merge:** A1:Z1
- **Text:** "DATA FLOW MAPPING & MASKING CHECKPOINTS"
- **Font:** Calibri 14pt Bold, White
- **Fill:** #003366 (Dark Blue)
- **Row Height:** 35px


**Row 2 - Policy Reference:**

- **Merge:** A2:Z2
- **Text:** "Data flows between environments SHALL have documented masking checkpoints. Production → Non-Production flows MUST include masking step. (ISMS-POL-A.8.11, Section 2.3 (Environment Coverage Requirements) Section 3.7)"
- **Font:** Calibri 10pt Italic
- **Fill:** #E7E6E6 (Light Gray)
- **Row Height:** Auto (wrapped)


## Assessment Question (Rows 4-5)

**Row 4:**

- **Merge:** A4:W4
- **Text:** "Are all data flows mapped with masking checkpoints identified and validated?"
- **Font:** Calibri 10pt Bold


**Cell X4 - Response:**

- **Data Validation:** Dropdown: "Yes (All Flows), Partial, No"
- **Fill:** #FFFFCC (Yellow)


**Cell Y4-Z4 - Label:**

- **Merge:** Y4:Z4
- **Text:** "Response:"
- **Alignment:** Right


**Row 5 - Critical Reminder:**

- **Merge:** A5:Z5
- **Text:** "🚨 CRITICAL: Production → Non-Production flows WITHOUT masking checkpoint = POLICY VIOLATION (automatic P1 gap)"
- **Font:** Calibri 9pt Bold, Red text
- **Fill:** #FFC7CE (Light Red)
- **Alignment:** Center


## Column Headers (Row 7)

**Custom Column Structure for Data Flow Mapping:**

| Column | Header | Width | Type | Validation Options |
|--------|--------|-------|------|-------------------|
| A | Flow ID | 12 | Text | Free text (e.g., FLOW-001) |
| B | Source Environment | 25 | Text | Free text (from Environment_Inventory) |
| C | Destination Environment | 25 | Text | Free text (from Environment_Inventory) |
| D | Flow Description | 30 | Text | Free text, wrapped |
| E | Flow Frequency | 15 | Dropdown | Real-time, Hourly, Daily, Weekly, Monthly, On-demand |
| F | Flow Mechanism | 20 | Dropdown | ETL, Replication, API, File Transfer, Manual |
| G | Sensitive Data Transferred? | 15 | Dropdown | Yes, No, Unknown |
| H | Masking Checkpoint Exists? | 15 | Dropdown | Yes, No, N/A |
| I | Checkpoint Location | 18 | Dropdown | At Source, In Pipeline, At Destination, None |
| J | Masking Technique Used | 20 | Dropdown | SDM, DDM, Tokenization, Redaction, Aggregation, None |
| K | Checkpoint Automated? | 15 | Dropdown | Yes, Manual, N/A |
| L | Checkpoint Validation | 25 | Text | Free text (how masking is verified) |
| M | Failure Handling | 20 | Dropdown | Stop Flow, Alert Only, Continue (Non-Compliant), N/A |
| N | Last Verified Date | 15 | Date | Date picker (dd.mm.yyyy) |
| O | Flow Owner | 20 | Text | Free text (responsible for flow) |
| P | Compliance Status | 15 | Dropdown | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A |
| Q | Notes/Comments | 30 | Text | Free text, wrapped |
| R | Evidence ID | 15 | Text | Link to Evidence_Register |

**Row 7 Styling:**

- **Fill:** #D9D9D9 (Light Gray)
- **Font:** Calibri 9pt Bold (smaller font due to many columns)
- **Alignment:** Center, Vertical Center, Wrapped
- **Border:** Thick bottom border (3pt)
- **Row Height:** 60px (accommodate wrapped text)


## Example Row (Row 8)

**Sample Data Flow:**

- A8: "FLOW-001"
- B8: "Production CRM Database"
- C8: "Development CRM Database"
- D8: "Weekly data refresh for dev testing"
- E8: "Weekly"
- F8: "ETL"
- G8: "Yes"
- H8: "Yes"
- I8: "In Pipeline"
- J8: "SDM"
- K8: "Yes"
- L8: "Automated validation script checks 100% coverage post-masking"
- M8: "Stop Flow"
- N8: "13.01.2026"
- O8: "Database Administrator"
- P8: "✅ Compliant"
- Q8: "Informatica ETL job includes masking transformation step"
- R8: "EV-FLOW-001"


**Styling:** Gray italic example row

## Data Entry Rows (9-38)

**30 rows for data flow mapping**

**Styling:** Yellow input cells, standard format

**Data Validation for Columns:**

**Column E (Flow Frequency):** Dropdown:
```
Real-time, Hourly, Daily, Weekly, Monthly, On-demand
```

**Column F (Flow Mechanism):** Dropdown:
```
ETL, Replication, API, File Transfer, Manual
```

**Column G (Sensitive Data Transferred?):** Dropdown:
```
Yes, No, Unknown
```

**Conditional Formatting for Column G:**

- If "Unknown" → Fill #FFEB9C (Yellow) - Requires investigation


**Column H (Masking Checkpoint Exists?):** Dropdown:
```
Yes, No, N/A
```

**CRITICAL Conditional Formatting for Column H:**

- If "No" AND Column G="Yes" (sensitive data) AND Destination is non-production → Fill #FFC7CE (Red) + Bold Red text + Thick red border
  - **Rationale:** Production → Non-Production flow WITHOUT masking = P1 GAP


**Column I (Checkpoint Location):** Dropdown:
```
At Source, In Pipeline, At Destination, None
```

**Column J (Masking Technique Used):** Dropdown:
```
SDM, DDM, Tokenization, Redaction, Aggregation, None
```

**Column K (Checkpoint Automated?):** Dropdown:
```
Yes, Manual, N/A
```

**Conditional Formatting for Column K:**

- If "Manual" → Fill #FFEB9C (Yellow) - Manual process = error risk


**Column M (Failure Handling):** Dropdown:
```
Stop Flow, Alert Only, Continue (Non-Compliant), N/A
```

**Conditional Formatting for Column M:**

- If "Continue (Non-Compliant)" → Fill #FFC7CE (Red) - Unmasked data could leak
- If "Stop Flow" → Fill #C6EFCE (Green) - Best practice


**Column P (Compliance Status):** Dropdown:
```
✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A
```

**Standard conditional formatting** for status column

## Compliance Checklist (Rows 41-54)

**Row 41 - Section Header:**

- **Text:** "DATA FLOW MAPPING CHECKLIST"
- **Styling:** #4472C4 header


**Rows 43-54 - Checklist Items (12 items):**

1. All major data flows mapped (production → non-prod, analytics, external)
2. Masking checkpoints identified for ALL flows with sensitive data
3. Production → Non-Production flows have masking checkpoint (100% required)
4. Checkpoint implementation verified (not just documented)
5. Checkpoint automation preferred (manual processes documented with mitigation)
6. Failure handling defined (masking fails → flow stops, not continues)
7. Bypass controls prevent skipping masking step
8. ETL/pipeline configurations reviewed (masking step present)
9. Real-time replication includes masking (or destination-side masking)
10. API integrations return masked data (application layer masking)
11. Data flow diagrams maintained (Visio, Lucidchart, etc.)
12. Annual data flow re-mapping (detect new flows, retired flows)

**Status Dropdown:** Same as previous sheets

## Data Flow Patterns Reference Table (Starting Row 58)

**Common Data Flow Patterns & Masking Checkpoints:**

| Flow Pattern | Example | Masking Checkpoint | Risk if No Checkpoint |
|--------------|---------|-------------------|----------------------|
| **Prod → Dev** | Weekly data refresh | In ETL pipeline (pre-load) | P1 GAP: Unmasked prod data in dev |
| **Prod → Analytics** | Nightly ETL to warehouse | At source (masked views) | Individual-level PII in reports |
| **Prod → Backup** | Daily backup job | N/A (encryption instead) | Acceptable if encrypted |
| **Prod → Vendor** | API integration | Application layer masking | Third-party sees real PII |
| **Analytics → Export** | BI dashboard export | Aggregation at source | Users export raw PII |
| **Dev → Staging** | Pre-production promotion | N/A (dev already masked) | Low risk (both non-prod) |
| **Staging → Prod** | Production deployment | ⚠️ Should NOT include data | Code only, no data flow |

**ETL Tool Masking Integration Examples:**

| ETL Tool | Masking Integration Method | Validation Approach |
|----------|---------------------------|---------------------|
| Informatica PowerCenter | Masking transformation component | Test mode preview, row counts |
| Talend | tMask component or custom Java | Unit tests on sample data |
| Apache Airflow | Custom Python masking operator | DAG task dependencies, assertions |
| AWS Glue | PySpark masking transforms | Glue Data Quality rules |
| Azure Data Factory | Data flow masking activity | Pipeline validation, monitoring |
| Google Dataflow | Apache Beam masking DoFn | Pipeline monitoring, assertions |

---

**END OF PART II - SECTION 3**

**Completed Assessment Sheets:**

- Sheet 1: Instructions_Legend ✅
- Sheet 2: Environment_Inventory ✅
- Sheet 3: Production_Environment ✅
- Sheet 4: NonProduction_Environments ✅
- Sheet 5: Analytics_Reporting ✅
- Sheet 6: Backup_Archive ✅
- Sheet 7: External_Sharing ✅
- Sheet 8: Cloud_Environments ✅
- Sheet 9: Data_Flow_Mapping ✅


**Next Section 4 (FINAL Technical Spec Section):**

- Sheet 10: Gap_Analysis
- Sheet 11: Evidence_Register
- Sheet 12: Summary_Dashboard
- Python Script Integration Notes
- Quality Assurance Requirements


**Shall the Grand ISMS Guru continue to enlighten you with the final sacred section? 🙏**

# ISMS-IMP-A.8.11.3 - Environment Coverage Assessment
# PART II: TECHNICAL SPECIFICATION - SECTION 4 (FINAL)

---

# Sheet 10: Gap_Analysis

## Header (Rows 1-2)

**Row 1 - Sheet Title:**

- **Merge:** A1:O1
- **Text:** "GAP ANALYSIS & REMEDIATION ROADMAP"
- **Font:** Calibri 14pt Bold, White
- **Fill:** #003366 (Dark Blue)
- **Row Height:** 35px


**Row 2 - Policy Reference:**

- **Merge:** A2:O2
- **Text:** "All gaps (unmasked environments, missing checkpoints, policy exceptions) SHALL be documented, prioritized (P1-P4), assigned to owners, and remediated within SLA: P1≤30 days, P2≤90 days, P3≤180 days, P4≤365 days"
- **Font:** Calibri 10pt Italic
- **Fill:** #E7E6E6 (Light Gray)
- **Row Height:** Auto (wrapped)


## Assessment Question (Rows 4-5)

**Row 4:**

- **Merge:** A4:L4
- **Text:** "Have ALL gaps from all assessment sheets been consolidated and assigned to owners with remediation plans?"
- **Font:** Calibri 10pt Bold


**Cell M4 - Response:**

- **Data Validation:** Dropdown: "Yes (All Documented), Partial, No"
- **Fill:** #FFFFCC (Yellow)


**Cell N4-O4 - Label:**

- **Merge:** N4:O4
- **Text:** "Response:"
- **Alignment:** Right


## Column Headers (Row 6)

**Gap Analysis Columns:**

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Gap ID | 12 | Text | Free text (GAP-001, etc.) |
| B | Gap Category | 20 | Dropdown | Environment Inventory, Production, Non-Production, Analytics, Cloud, Backup, External, Data Flow |
| C | Gap Description | 40 | Text | Free text, wrapped |
| D | Environment(s) Affected | 25 | Text | Free text |
| E | Priority | 8 | Dropdown | P1, P2, P3, P4 |
| F | Risk Level | 12 | Dropdown | Critical, High, Medium, Low |
| G | Gap Owner | 20 | Text | Named individual |
| H | Supporting Teams | 22 | Text | DBAs, Cloud, Security, etc. |
| I | Remediation Action | 35 | Text | Specific steps |
| J | Target Date | 15 | Date | dd.mm.yyyy |
| K | Current Status | 15 | Dropdown | Not Started, In Progress, Blocked, Completed |
| L | Completion Date | 15 | Date | dd.mm.yyyy |
| M | Verification Method | 25 | Text | How closure verified |
| N | Evidence ID | 15 | Text | Link to Evidence_Register |
| O | Notes | 30 | Text | Wrapped |

**Row 6 Styling:**

- Fill: #D9D9D9, Font: Calibri 10pt Bold
- Border: Thick bottom (3pt)
- Row Height: 50px


## Data Entry Rows (7-46)

**40 rows for gaps**

**Conditional Formatting:**

**Column E (Priority):**

- P1 → #FFC7CE (Red) + Bold
- P2 → #FFEB9C (Yellow)
- P3 → #E7E6E6 (Light Gray)
- P4 → White


**Column K (Status):**

- Completed → #C6EFCE (Green) + Strikethrough
- Blocked → #FFC7CE (Red) + Bold
- In Progress → #B4C7E7 (Blue)
- Not Started → #FFEB9C (Yellow)


## Reference Tables (Starting Row 50)

**Priority SLA Matrix (Rows 50-56):**

| Priority | SLA | Examples |
|----------|-----|----------|
| P1 | ≤30 days | Unmasked non-prod, no DPA |
| P2 | ≤90 days | Missing DDM, analytics PII |
| P3 | ≤180 days | Manual processes, 90-99% coverage |
| P4 | ≤365 days | Documentation gaps |

---

# Sheet 11: Evidence_Register

## Header (Rows 1-2)

**Row 1:**

- Merge: A1:J1
- Text: "EVIDENCE REGISTER"
- Styling: #003366 header


**Row 2:**

- Merge: A2:J2
- Text: "Complete audit trail - Supporting documentation for all assessments"
- Styling: #E7E6E6 italic


## Columns (Row 4)

| Column | Header | Width |
|--------|--------|-------|
| A | Evidence ID | 15 |
| B | Evidence Type | 22 |
| C | Description | 40 |
| D | Related Environment | 25 |
| E | Document Name/Link | 35 |
| F | Date Created | 15 |
| G | Owner | 20 |
| H | Retention Period | 15 |
| I | Location | 30 |
| J | Notes | 30 |

## Data Entry Rows (5-104)

**100 rows for evidence**

**Evidence Type Examples:**

- Configuration, Screenshot, Log, Agreement, Script, Report, Audit Trail


---

# Sheet 12: Summary_Dashboard

## Complete Dashboard Structure

**Section 1: Overall Compliance (Rows 4-12)**

**Key Metrics with Formulas:**

| Metric | Formula | Target |
|--------|---------|--------|
| Overall Score | Weighted average | ≥90% |
| Non-Prod Masking | `=COUNTIF(NonProduction_Environments!O:O,"✅ Compliant")/COUNTA(NonProduction_Environments!A7:A37)*100` | 100% |
| Production DDM | `=COUNTIF(Production_Environment!O:O,"✅ Compliant")/COUNTA(Production_Environment!A7:A37)*100` | ≥90% |
| Cloud Coverage | `=COUNTIF(Cloud_Environments!O:O,"✅ Compliant")/COUNTA(Cloud_Environments!A7:A37)*100` | 100% |
| Critical Gaps | `=COUNTIF(Gap_Analysis!E:E,"P1")` | 0 |

**Weighted Average Formula:**
```
=(NonProd*0.35 + Production*0.20 + Cloud*0.15 + Analytics*0.15 + DataFlow*0.10 + Inventory*0.05)
```

**Section 2: Environment Breakdown (Rows 14-24)**

Counts by environment type with coverage percentages.

**Section 3: Critical Gaps (Rows 26-36)**

Top 10 P1/P2 gaps auto-populated from Gap_Analysis sheet.

**Section 4: Sign-Off (Rows 50-58)**

Executive approval table (IT Ops Manager, CISO, DPO, Legal).

---

# Python Script Integration

## Script Template Structure

```python
"""
SAMPLE SCRIPT - REQUIRES CUSTOMIZATION FOR A.8.11.3

Key customization areas:
1. Sheet structures (12 sheets, varying columns)
2. Dashboard formulas (references to 9 assessment sheets)
3. Conditional formatting (environment-specific)
4. Data validation (environment types, priorities)
"""

import openpyxl
from openpyxl.styles import *
from openpyxl.worksheet.datavalidation import DataValidation
from datetime import datetime

# Color palette
COLORS = {
    'header_main': '003366',
    'header_sub': '4472C4',
    'input': 'FFFFCC',
    'status_compliant': 'C6EFCE',
    'status_partial': 'FFEB9C',
    'status_noncompliant': 'FFC7CE'
}

def create_workbook():
    wb = openpyxl.Workbook()
    wb.remove(wb.active)
    
    # Create all 12 sheets
    create_instructions_legend(wb)
    create_environment_inventory(wb)
    create_production_environment(wb)
    create_nonproduction_environments(wb)
    create_analytics_reporting(wb)
    create_backup_archive(wb)
    create_external_sharing(wb)
    create_cloud_environments(wb)
    create_data_flow_mapping(wb)
    create_gap_analysis(wb)
    create_evidence_register(wb)
    create_summary_dashboard(wb)  # LAST - references others
    
    filename = f"ISMS-IMP-A.8.11.3_Environment_Coverage_{datetime.now():%Y%m%d}.xlsx"
    wb.save(filename)
    return wb

# Implement each create_* function per specification
```

## Critical Implementation Notes

**Dashboard Formula Validation:**

- MUST verify all sheet names exist
- Test formulas with sample data
- Handle division by zero (empty sheets)


**Conditional Formatting:**

- Non-Production <100% → Red + Bold + Thick border
- Missing DPAs → Red + Bold
- P1 gaps → Red highlighting


**Cell Protection:**

- Lock all formula cells
- Unlock yellow input cells
- Enable sheet protection


---

# Quality Assurance Checklist

## Pre-Deployment

**Structure:**

- [ ] All 12 sheets present
- [ ] Sheet names exact
- [ ] Column headers match spec
- [ ] Row counts correct


**Formulas:**

- [ ] Dashboard calculates correctly
- [ ] No #REF! errors
- [ ] No #DIV/0! errors
- [ ] Conditional formulas trigger


**Formatting:**

- [ ] Colors consistent
- [ ] Fonts correct
- [ ] Borders applied
- [ ] Protection set


**Data Validation:**

- [ ] All dropdowns work
- [ ] Date formats correct
- [ ] No typos in options


## Post-Deployment

**Functional Testing:**
1. Fill 10 sample environments
2. Verify dropdowns
3. Check conditional formatting
4. Test Dashboard formulas

**User Acceptance:**
1. Pilot with test user
2. Collect feedback
3. Iterate

---

# Requirements Traceability

| Requirement | Sheet | How Assessed |
|-------------|-------|--------------|
| Complete inventory | Environment_Inventory | All systems documented |
| Non-prod 100% masked | NonProduction_Environments | Coverage % column |
| Production DDM | Production_Environment | Role-based masking |
| Cloud compliance | Cloud_Environments | Same rules as on-prem |
| External sharing | External_Sharing | DPAs + masking |
| Data flow checkpoints | Data_Flow_Mapping | Checkpoint tracking |
| Gap remediation | Gap_Analysis | SLA tracking |

---

**END OF PART II - TECHNICAL SPECIFICATION**

**Complete IMP-A.8.11.3 Package:**

- Part I: ~1,800 lines (User Guide)
- Part II: ~2,500 lines (Technical Spec)
- Total: ~4,300 lines


**Status:** APPROVED FOR IMPLEMENTATION

**Next Steps:**
1. Generate Python script
2. Create Excel template
3. Test with sample data
4. Deploy to teams

---

**END OF SPECIFICATION**

---

*"In the middle of difficulty lies opportunity."*
— Albert Einstein
*Where bamboo antennas actually work.* 🎋
