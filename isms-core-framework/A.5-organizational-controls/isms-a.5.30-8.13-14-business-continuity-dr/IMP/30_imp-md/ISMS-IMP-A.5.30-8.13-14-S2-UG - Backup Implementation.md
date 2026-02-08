**ISMS-IMP-A.5.30-8.13-14-S2-UG - Backup Implementation**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.13: Information Backup

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.30-8.13-14-S2-UG |
| **Version** | 1.0 |
| **Assessment Area** | Backup Implementation & Recovery Capability |
| **Related Policy** | ISMS-POL-A.5.30-8.13-14, Section 2.1 (Information Backup Requirements) |
| **Related Assessment** | ISMS-IMP-A.5.30-8.13-14-S1 (BIA - provides RPO requirements) |
| **Purpose** | Implement backup solutions aligned with BIA-determined RPO requirements, establish backup schedules, configure retention policies, implement backup monitoring, document recovery procedures |
| **Target Audience** | Backup Administrator, Storage Team, Database Administrators, System Administrators, IT Operations, BC/DR Coordinator |
| **Assessment Type** | Technical Implementation |
| **Review Cycle** | Quarterly (backup configuration) + After Major System Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial backup implementation methodology | ISMS Implementation Team |

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.5.30-8.13-14-S2-TG.

---

# Assessment Overview

## What This Assessment Achieves

**Assessment Name:** ISMS-IMP-A.5.30-8.13-14-S2 - Backup Implementation

### The Backup Challenge

**The Hard Truth About Backups:**

You don't have a backup until you've successfully restored from it.

- "We backup everything nightly" ≠ We can recover everything
- "Backups are running green" ≠ Recovery will work
- "We keep 30 days of backups" ≠ We can actually restore 30-day-old data

**Without Tested Backups:** False confidence. You discover backups are corrupt, incomplete, or misconfigured only when disaster strikes and recovery fails.

**With Tested Backups:** Proven recovery capability. You know exactly what can be recovered, how long it takes, and what the process is.

### Backup Implementation Outputs

Upon completion, [Organization] will have:

1. **Backup Inventory** - All systems with backup status (backed up or not)
2. **Backup Architecture** - Documented backup infrastructure and data flows
3. **Backup Schedules** - Configured backup frequencies aligned with RPO requirements
4. **Retention Policies** - Defined retention periods per system criticality tier
5. **Offsite/Cloud Backup** - Geographic separation for disaster recovery
6. **Backup Monitoring** - Automated monitoring and alerting for backup failures
7. **Recovery Procedures** - Documented step-by-step recovery runbooks
8. **Testing Results** - Proven recovery capability through restore tests
9. **Gap Remediation** - Action plan for systems not meeting backup requirements

## Why This Matters - A.8.13 Information Backup

**ISO 27001:2022 Control A.8.13 (exact text):**

> "Backup copies of information, software and systems shall be maintained and regularly tested in accordance with the agreed topic-specific policy."

**Key Requirements from Control:**

- Backup copies SHALL be maintained (mandatory)
- Regular testing (prove recovery works)
- In accordance with agreed policy (follow ISMS-POL-A.5.30-8.13-14 requirements)

**Policy Requirements (from ISMS-POL-A.5.30-8.13-14, Section 2.1):**

Per system criticality tier:

**Tier 1 (Critical) Backup Requirements:**

- Backup frequency: Aligned with RPO (hourly minimum if RPO ≤4h)
- Retention: 30 days minimum (online), 1 year archival
- Offsite backup: MANDATORY (geographic separation)
- Backup encryption: MANDATORY (AES-256 minimum)
- Testing frequency: Quarterly restore testing
- Monitoring: 24/7 automated monitoring with alerts

**Tier 2 (Important) Backup Requirements:**

- Backup frequency: Aligned with RPO (daily minimum if RPO ≤24h)
- Retention: 14 days minimum (online)
- Offsite backup: MANDATORY
- Backup encryption: Required for Confidential/Restricted data
- Testing frequency: Semi-annual restore testing
- Monitoring: Daily monitoring with alerts

**Tier 3 (Standard) Backup Requirements:**

- Backup frequency: Aligned with RPO (weekly minimum if RPO ≤7 days)
- Retention: 7 days minimum
- Offsite backup: Recommended
- Backup encryption: Recommended
- Testing frequency: Annual restore testing
- Monitoring: Best-effort monitoring

**Tier 4 (Low) Backup Requirements:**

- Backup frequency: Optional (on-demand acceptable)
- Retention: Risk-based decision
- Offsite backup: Not required
- Testing: No testing requirement

**Regulatory Context:**

Per ISMS-POL-00 (Regulatory Applicability Framework):

**Tier 1 - Mandatory:**

- **ISO 27001:2022 A.8.13** - Backup copies maintained and tested
- **Swiss nDSG Art. 8** - Appropriate technical measures (backup = data protection measure)
- **EU GDPR Art. 32(1)(c)** - "Ability to restore availability and access to personal data in a timely manner" (backup required)

**Tier 2 - Conditional:**

- **DORA (EU) Art. 12** - "Backup policies and procedures...ensuring restoration of ICT systems"
- **NIS2 (EU) Art. 21** - "Backup management and disaster recovery" for essential entities
- **PCI DSS v4.0.1 Req. 3.4** - "Data at rest shall be rendered unreadable" (encrypted backups for cardholder data)
- **FINMA (Swiss Financial)** - Backup and recovery capability required

## Connection to BIA (IMP-S1)

**CRITICAL:** Backup implementation MUST align with BIA findings. You cannot implement backups correctly without knowing RPO requirements from BIA.

**BIA Provides → Backup Implements:**

| BIA Output (IMP-S1) | Backup Implementation (IMP-S2) |
|---------------------|-------------------------------|
| **RPO Requirement** | **Backup Frequency** |
| RPO 1 hour | Hourly incremental backup + transaction log backups every 15min |
| RPO 4 hours | 4-hourly incremental backup |
| RPO 24 hours | Daily full backup + incremental |
| RPO 7 days | Weekly full backup |
| **System Criticality Tier** | **Retention & Testing** |
| Tier 1 | 30-day retention, quarterly testing, offsite mandatory |
| Tier 2 | 14-day retention, semi-annual testing, offsite mandatory |
| Tier 3 | 7-day retention, annual testing, offsite recommended |
| Tier 4 | Risk-based retention, no testing requirement |
| **Data Classification** | **Backup Encryption** |
| Restricted | AES-256 encryption mandatory, key management |
| Confidential | Encryption required |
| Internal | Encryption recommended |
| Public | No encryption requirement |

**Example Integration:**

```
From BIA (IMP-S1):
  System: Payment Database (SYS-015)
  Tier: Tier 1 (Critical)
  RPO: 1 hour
  Data Classification: Restricted
  Annual Revenue Impact: CHF 50K/hour

Backup Implementation (IMP-S2):
  Backup Solution: Azure SQL Database Backup + Veeam
  Backup Schedule:

    - Full backup: Daily at 02:00 UTC
    - Incremental backup: Every 1 hour
    - Transaction log backup: Every 15 minutes

  Retention: 30 days online, 1 year archival to Azure Blob (Cool tier)
  Offsite: Geo-redundant storage (Azure West Europe primary, Azure North Europe replica)
  Encryption: TDE (Transparent Data Encryption) + AES-256 for backup files
  Monitoring: Azure Monitor + Veeam ONE alerts
  Testing: Quarterly restore to isolated test environment (Q1, Q2, Q3, Q4)
```

## Who Participates in Backup Implementation

| Role | Responsibility | Time Commitment |
|------|---------------|----------------|
| **Backup Administrator** | Primary implementation owner, configure backup solutions, schedule management | 40-80 hours (initial), 5-10 hours/month (ongoing) |
| **Storage Team** | Backup storage provisioning, capacity planning | 10-20 hours |
| **Database Administrators (DBAs)** | Database-specific backup configuration (Azure SQL, PostgreSQL, Oracle, etc.) | 20-40 hours |
| **System Administrators** | Server/VM backup configuration, agent installation | 20-40 hours |
| **Cloud Administrators** | Cloud backup configuration (Azure Backup, AWS Backup, GCP) | 15-30 hours |
| **Network Team** | Backup network traffic management (bandwidth, VPN for offsite) | 5-10 hours |
| **Security Team** | Backup encryption configuration, key management | 10-15 hours |
| **BC/DR Coordinator** | Verify alignment with BIA requirements, testing coordination | 10-20 hours |

**Total Organizational Effort:** 130-255 person-hours (initial implementation for 50-100 systems)

## Time Estimate

**Backup Implementation Timeline:**

| Phase | Duration | Activities |
|-------|----------|-----------|
| **Week 1: Planning** | 5 days | Review BIA, backup solution selection, architecture design |
| **Week 2-3: Infrastructure Setup** | 10 days | Deploy backup servers/appliances, configure cloud backup, storage provisioning |
| **Week 4-6: System Configuration** | 15 days | Configure backup schedules per system, agent installation, initial full backups |
| **Week 7: Testing** | 5 days | Restore testing, validation, issue remediation |
| **Week 8: Monitoring Setup** | 3 days | Configure monitoring, alerts, reporting |
| **Week 9: Documentation** | 2 days | Recovery procedures, backup runbooks |

**Total Duration:** 8-9 weeks (first-time implementation)

**Ongoing:** Daily monitoring, quarterly testing, monthly capacity review

## Integration with Other BC/DR Components

**Backup Alone Is Not Sufficient for BC/DR:**

```
Full BC/DR Capability:
  ├── A.8.13 (Backup) ← THIS GUIDE (IMP-S2)
  │     Purpose: Data recovery (RPO)
  │     Protects against: Data loss, corruption, accidental deletion
  │
  ├── A.8.14 (Redundancy) ← IMP-S3
  │     Purpose: System availability (RTO)
  │     Protects against: System failures, component failures
  │
  └── A.5.30 (ICT BC Readiness) ← IMP-S4, S5
        Purpose: Comprehensive recovery capability
        Protects against: Site-wide disasters, major incidents
```

**Backup Provides:** Data recovery capability (if system fails, restore data)
**Backup Does NOT Provide:** Instant failover (that requires redundancy per A.8.14)

**Example - Why Both Are Needed:**

```
Scenario: E-commerce database failure

With Backup Only:

  - Database fails at 10:00
  - Restore from backup starts at 10:30 (30min to identify and initiate)
  - Restore completes at 14:30 (4 hours to restore)
  - E-commerce down for 4.5 hours
  - Data loss: Last backup was at 09:00 (1 hour of orders lost)
  - Revenue loss: CHF 1,712/hour × 4.5h = CHF 7,704
  - Missed orders: 1 hour of orders = ~CHF 1,712

With Backup + Redundancy:

  - Database fails at 10:00
  - Automatic failover to hot standby at 10:01 (1 minute)
  - E-commerce down for 1 minute
  - Data loss: 0 (synchronous replication)
  - Revenue loss: Negligible
  - Customer impact: Minimal (brief interruption)

```

**Backup Integration Points:**

**To IMP-S3 (Redundancy Implementation):**

- Redundant systems still need backup (redundancy ≠ backup)
- Example: Hot standby database with synchronous replication still backed up daily (protects against data corruption affecting both copies)

**To IMP-S4 (Recovery Testing):**

- Backup restore testing is subset of overall recovery testing
- Full DR scenario testing includes: Restore from backup → Validate data → Start application → Test end-to-end

**To IMP-S5 (BC/DR Assessment):**

- Backup coverage assessment (% systems backed up)
- Backup success rate (% successful backups)
- RPO compliance (backup frequency meets RPO requirement)
- Restore testing compliance (testing per policy requirements)

---

# Prerequisites

## Information Required

**Before Starting Backup Implementation, Gather:**

**From BIA (IMP-S1):**

- [ ] BIA Assessment Workbook with completed:
  - Sheet 2: System-Process Mapping (system inventory)
  - Sheet 4: RPO Requirements (backup frequency drivers)
  - Sheet 5: System Criticality (Tier 1-4 classifications)
  - Sheet 3: Data Classification (encryption requirements)
- [ ] Gap Analysis results (systems not currently backed up)

**Technical Information:**

- [ ] Complete system inventory with:
  - System type (physical server, VM, container, cloud service, SaaS)
  - Operating system (Windows Server, Linux, etc.)
  - Database platform (Azure SQL, PostgreSQL, Oracle, MongoDB, etc.)
  - Application type (file server, web server, application server, etc.)
  - Storage location (on-premises, Azure, AWS, GCP, hybrid)
  - Current backup status (backed up or not)
- [ ] Storage capacity inventory:
  - Current data volume per system
  - Data growth rate (monthly increase)
  - Available backup storage capacity
- [ ] Network bandwidth:
  - WAN bandwidth (for offsite backup)
  - Backup window availability (maintenance windows)
- [ ] Existing backup infrastructure:
  - Backup servers/appliances (Veeam, Commvault, Veritas, etc.)
  - Cloud backup subscriptions (Azure Backup, AWS Backup, Veeam Cloud Connect)
  - Tape libraries (if applicable)

**Cloud Provider Information (from ISMS-REF-A.5.23):**

If using cloud backup:

- [ ] Azure subscription details (if using Azure Backup)
- [ ] AWS account details (if using AWS Backup)
- [ ] GCP project details (if using GCP Backup)
- [ ] SaaS backup services (Veeam Backup for Microsoft 365, Spanning, etc.)

**Regulatory Requirements:**

- [ ] Data residency requirements (Swiss nDSG, GDPR, FINMA)
- [ ] Retention requirements (industry-specific, legal hold)
- [ ] Encryption requirements (data classification → encryption needs)

## Stakeholder Availability

**Coordinate with:**

**Technical Teams:**

- Backup Administrator (primary contact) - Available throughout implementation
- Database Administrators - 2-4 hours per database platform
- System Administrators - 2-3 hours per system type (Windows, Linux, etc.)
- Cloud Administrators - 5-10 hours for cloud backup setup

**Business/Management:**

- BC/DR Coordinator - Verify alignment with BIA
- IT Management - Budget approval for backup storage/licenses
- Security Team - Encryption key management setup

## Tools Needed

**Backup Solutions:**

Select based on environment and requirements (see Section 4: Backup Solution Selection):

**On-Premises/Hybrid Backup:**

- Veeam Backup & Replication (VMware, Hyper-V, physical servers)
- Commvault Complete Backup & Recovery
- Veritas NetBackup
- Windows Server Backup (for small environments)

**Cloud-Native Backup:**

- Azure Backup (Azure VMs, Azure SQL, Azure Files)
- AWS Backup (EC2, RDS, S3, etc.)
- Google Cloud Backup and DR

**SaaS Backup:**

- Veeam Backup for Microsoft 365 (Exchange Online, SharePoint, OneDrive, Teams)
- Spanning Backup (Microsoft 365, Google Workspace, Salesforce)
- Dropsuite (cloud-to-cloud backup)

**Database Backup:**

- Native database backup tools (SQL Server, PostgreSQL, MySQL, MongoDB)
- Azure SQL Database automated backup
- AWS RDS automated backup

**Monitoring Tools:**

- Veeam ONE (if using Veeam)
- Azure Monitor (if using Azure Backup)
- CloudWatch (if using AWS Backup)
- PRTG Network Monitor
- Zabbix

**Assessment Workbook:**

- Provided in PART II of this document
- 5 worksheets for backup inventory, schedule tracking, testing results

---

# Backup Implementation Methodology

## High-Level Backup Implementation Process

```
┌──────────────────────────────────────────────────────────┐
│         BACKUP IMPLEMENTATION WORKFLOW                   │
│                                                          │
│  STEP 1: INVENTORY Systems & Current Backup Status      │
│     ↓                                                    │
│  STEP 2: DESIGN Backup Architecture                     │
│     ↓                                                    │
│  STEP 3: SELECT Backup Solutions                        │
│     ↓                                                    │
│  STEP 4: CALCULATE Backup Storage Requirements          │
│     ↓                                                    │
│  STEP 5: CONFIGURE Backup Schedules (RPO-aligned)       │
│     ↓                                                    │
│  STEP 6: IMPLEMENT Offsite/Cloud Backup                 │
│     ↓                                                    │
│  STEP 7: CONFIGURE Backup Encryption                    │
│     ↓                                                    │
│  STEP 8: SETUP Backup Monitoring & Alerting             │
│     ↓                                                    │
│  STEP 9: DOCUMENT Recovery Procedures                   │
│     ↓                                                    │
│  STEP 10: TEST Restore Capability                       │
└──────────────────────────────────────────────────────────┘
```

## STEP 1: INVENTORY Systems & Current Backup Status

**Objective:** Document all ICT systems and their current backup status.

**Duration:** Week 1

**Activities:**

**1. Extract System Inventory from BIA**

From ISMS-IMP-A.5.30-8.13-14-S1 (BIA), Sheet 2: System-Process Mapping:

- System ID
- System Name
- System Type
- Deployment Model
- Data Classification
- System Owner

**2. For Each System, Document Current Backup Status:**

| Information to Gather | Source | Example |
|----------------------|--------|---------|
| **Is system currently backed up?** | Backup administrator, backup server | Yes/No |
| **Backup solution in use** | Backup configuration | Veeam Backup & Replication, Azure Backup, None |
| **Backup schedule** | Backup job configuration | Daily full at 02:00, Hourly incremental |
| **Retention period** | Backup retention policy | 14 days, 30 days |
| **Last successful backup** | Backup monitoring | 2026-01-22 02:15 |
| **Backup size** | Backup statistics | 250 GB (full), 15 GB (incremental avg) |
| **Backup location** | Backup repository | On-prem NAS, Azure Blob Storage |
| **Offsite/cloud backup** | Backup copy job | Yes (Azure), No |
| **Last restore test** | Testing records | 2025-12-15 (Q4 test), Never tested |

**3. Calculate Backup Coverage:**

```
Backup Coverage = (Systems Backed Up / Total Systems) × 100%

Example:
  Total Systems: 85
  Systems Backed Up: 62
  Systems Not Backed Up: 23
  Backup Coverage: 62 / 85 = 72.9%
```

**4. Identify Backup Gaps:**

Systems NOT currently backed up:

- New systems (deployed after backup configuration)
- Shadow IT (systems deployed without IT involvement)
- Cloud services (assumed "cloud = backed up" - often wrong)
- Development/test environments (assumed "not important" but BIA says otherwise)

**Priority Gap Categories:**

| Gap Category | Priority | Action |
|--------------|----------|--------|
| **Tier 1 system not backed up** | **P1 - CRITICAL** | Implement backup immediately (within 1 week) |
| **Tier 2 system not backed up** | **P2 - HIGH** | Implement backup within 2 weeks |
| **Tier 1/2 backup not meeting RPO** | **P2 - HIGH** | Adjust backup frequency within 2 weeks |
| **Tier 1/2 no offsite backup** | **P2 - HIGH** | Implement offsite backup within 4 weeks |
| **Tier 3 system not backed up** | **P3 - MEDIUM** | Implement backup within 30 days |

**5. Document in Backup Assessment Workbook - Sheet 1: Backup Inventory**

Columns:

- System ID (from BIA)
- System Name
- System Type
- Tier (from BIA)
- RPO Requirement (from BIA)
- Data Classification (from BIA)
- Current Backup Status (Yes/No)
- Backup Solution (name)
- Backup Frequency (current)
- Retention Period (current)
- Last Successful Backup (date/time)
- Offsite Backup (Yes/No)
- Last Restore Test (date)
- Gap Priority (calculated)
- Notes

**Quality Check:**

- ✓ All systems from BIA included in inventory
- ✓ Current backup status verified (not assumed)
- ✓ Gaps prioritized by criticality tier
- ✓ P1 gaps escalated immediately

## STEP 2: DESIGN Backup Architecture

**Objective:** Design backup infrastructure topology and data flows.

**Duration:** Week 1

**Backup Architecture Components:**

### Backup Server/Appliance (Control Plane)

**Purpose:** Manages backup jobs, schedules, retention, orchestration

**Options:**

- **Veeam Backup Server** (Windows VM or physical server)
- **Commvault CommServe**
- **Azure Backup Vault** (cloud-native, no server required)
- **AWS Backup Service** (cloud-native)

**Sizing Considerations:**

- Number of protected systems (VMs, databases, servers)
- Concurrent backup jobs
- Management overhead (CPU, RAM)

**Example Sizing (Veeam):**

- Small (up to 50 VMs): 4 vCPU, 8 GB RAM
- Medium (50-200 VMs): 8 vCPU, 16 GB RAM
- Large (200+ VMs): 16 vCPU, 32 GB RAM

### Backup Repository (Storage)

**Purpose:** Store backup files

**Options:**

**On-Premises:**

- **NAS/SAN** (Synology, QNAP, NetApp, Dell EMC)
- **Direct-Attached Storage (DAS)** (local disks on backup server)
- **Deduplication Appliance** (Dell EMC Data Domain, HPE StoreOnce)

**Cloud:**

- **Azure Blob Storage** (Hot, Cool, Archive tiers)
- **AWS S3** (Standard, IA, Glacier)
- **Google Cloud Storage**

**Hybrid:**

- **On-Premises Primary + Cloud Secondary** (most common)
- **Cloud Primary + On-Premises Secondary** (cloud-first organizations)

**Capacity Planning:**

```
Backup Storage Required = (Total Data Volume) × (Retention Days) × (Change Rate) × (Compression Ratio)

Example:
  Total Data: 10 TB
  Retention: 30 days
  Daily Change Rate: 5% (500 GB/day changes)
  Full backup: 10 TB (weekly)
  Incremental: 500 GB/day × 6 days = 3 TB
  Weekly storage: 10 TB (full) + 3 TB (incrementals) = 13 TB
  Monthly storage: 13 TB × 4 weeks = 52 TB
  With compression (2:1): 52 TB / 2 = 26 TB
  With deduplication (additional 50% reduction): 26 TB / 2 = 13 TB
  Recommended provisioning (with 20% buffer): 13 TB × 1.2 = 15.6 TB
```

### Backup Proxy/Agent (Data Plane)

**Purpose:** Move backup data from source to repository

**Options:**

- **Agentless** (VMware, Hyper-V - backup via hypervisor API)
- **Agent-based** (physical servers, cloud VMs - agent installed on each system)
- **Cloud-native** (Azure Backup Agent, AWS Backup - built into cloud platform)

**Proxy Sizing (for VMware/Hyper-V):**

- 1 proxy core per 3-5 concurrent backup streams
- Example: 20 concurrent VMs backing up → 4-7 vCPU proxy

### Network Paths (Backup Traffic)

**Considerations:**

- **LAN Backup** (source → backup server/repository on same network)
  - Fast (1 Gbps, 10 Gbps typical)
  - Used for: On-premises servers, local VMs
  
- **WAN Backup** (source → offsite backup repository via internet/VPN)
  - Slower (100 Mbps typical for SME)
  - Used for: Cloud backup, remote offices, DR site
  
- **Direct-to-Cloud** (source → Azure/AWS/GCP directly, no backup server)
  - Speed depends on internet connection
  - Used for: Cloud-native workloads (Azure VMs → Azure Backup)

**Backup Window Calculation:**

```
Backup Time = Data Volume / Network Speed

Example (Daily Incremental):
  Data Volume: 500 GB
  Network Speed: 1 Gbps = 125 MB/s
  Backup Time: 500 GB / 125 MB/s = 4,000 seconds = 67 minutes
  
Example (Offsite Copy):
  Data Volume: 500 GB
  WAN Speed: 100 Mbps = 12.5 MB/s
  Backup Time: 500 GB / 12.5 MB/s = 40,000 seconds = 667 minutes = 11 hours
  
→ Offsite backup must run overnight in extended window
```

### Backup Architecture Patterns

**Pattern A: Traditional 3-Tier (On-Premises)**

```
[Production Systems]
         ↓ LAN (1 Gbps)
   [Backup Server]
         ↓ LAN (10 Gbps)
 [Primary Backup Repository] (NAS/SAN)
         ↓ WAN (100 Mbps) - nightly copy
 [Secondary Backup Repository] (Cloud - Azure Blob)
```

**Use Case:** Traditional on-premises infrastructure with cloud DR

**Pattern B: Cloud-First (Azure Example)**

```
[Azure VMs]
         ↓ Azure Backbone
   [Azure Backup Service]
         ↓
 [Recovery Services Vault] (Azure Backup storage)
         ↓ Optional
 [On-Premises Copy] (Veeam Cloud Connect)
```

**Use Case:** Azure-native workloads, minimal on-premises

**Pattern C: Hybrid (Cloud + On-Premises)**

```
[On-Premises Servers] ─────┐
         ↓                  │
   [Veeam Backup Server]    │
         ↓                  │
 [On-Prem Repository]       │
         ↓                  │
 [Azure Blob Storage] ◄─────┘
         ↑                   
[Azure VMs] ────────────────┘
         ↓
   [Azure Backup]
```

**Use Case:** Hybrid environment, centralized backup management

**6. Document Backup Architecture**

Create architecture diagram showing:

- All production systems (grouped by location/type)
- Backup servers/services
- Backup repositories (primary, secondary/offsite)
- Network paths (LAN, WAN speeds)
- Data flow arrows
- Retention tiers

**Quality Check:**

- ✓ Architecture supports all system types (physical, VM, cloud, SaaS)
- ✓ Offsite backup included (geographic separation)
- ✓ Network bandwidth adequate for backup windows
- ✓ Storage capacity sufficient for retention requirements
- ✓ Architecture aligns with BIA requirements

## STEP 3: SELECT Backup Solutions

**Objective:** Choose appropriate backup solutions for each system type.

**Duration:** Week 1

**Backup Solution Selection Matrix:**

### On-Premises/Hybrid Environments

**For VMware vSphere, Microsoft Hyper-V, Nutanix AHV:**

| Solution | Pros | Cons | Best For |
|----------|------|------|----------|
| **Veeam Backup & Replication** | Industry leader, excellent VMware/Hyper-V support, instant VM recovery, cloud integration | Windows-based (not Linux backup server), licensing costs | VMware/Hyper-V environments, 50-500 VMs |
| **Commvault Complete Backup** | Enterprise-grade, supports everything, single pane of glass | Complex, expensive, steep learning curve | Large enterprises (500+ systems), heterogeneous environments |
| **Veritas NetBackup** | Mature product, excellent for physical servers, tape support | Dated interface, expensive | Physical servers, tape backup, legacy environments |
| **Vembu BDR Suite** | Cost-effective, good feature set | Less mature than Veeam, smaller vendor | SME (10-100 VMs), budget-constrained |

**Recommendation for Swiss SME (50-100 VMs):** Veeam Backup & Replication

### Azure Cloud Environments

| Solution | Pros | Cons | Best For |
|----------|------|------|----------|
| **Azure Backup** | Native integration, no infrastructure required, pay-per-use | Azure only, limited retention (5 years max) | Azure VMs, Azure SQL, Azure Files |
| **Veeam Backup for Azure** | Agentless VM backup, Veeam familiar interface | Requires Veeam licensing | Organizations already using Veeam on-premises |
| **Azure Site Recovery** | DR + backup combined | Complex setup, primarily DR-focused | Azure VMs with DR requirement |

**Recommendation:** Azure Backup for Azure-native workloads

### AWS Cloud Environments

| Solution | Pros | Cons | Best For |
|----------|------|------|----------|
| **AWS Backup** | Native integration, centralized backup across AWS services | AWS only | EC2, RDS, EFS, DynamoDB, Aurora |
| **Veeam Backup for AWS** | Agentless EC2 backup | Requires Veeam licensing | Organizations using Veeam |

**Recommendation:** AWS Backup for AWS-native workloads

### Microsoft 365 / SaaS

| Solution | Pros | Cons | Best For |
|----------|------|------|----------|
| **Veeam Backup for Microsoft 365** | Market leader, excellent Exchange/SharePoint/OneDrive/Teams support | Requires infrastructure (Veeam server + storage) | Organizations with Veeam already, >100 M365 users |
| **Spanning Backup** | Cloud-to-cloud, no infrastructure, supports M365/Google/Salesforce | Subscription cost per user | SME, no infrastructure preference |
| **Dropsuite** | Cost-effective, cloud-to-cloud | Smaller vendor | SME, budget-conscious |

**CRITICAL:** Microsoft 365 native retention ≠ backup. Native retention protects against accidental deletion for 30-93 days only, NOT against:

- Ransomware (encrypted data stays encrypted)
- Malicious data deletion
- Compliance violations
- Long-term retention (>90 days)

**Recommendation:** Veeam Backup for Microsoft 365 OR Spanning Backup (cloud-to-cloud)

### Database-Specific Backup

| Database Platform | Recommended Backup Approach |
|-------------------|---------------------------|
| **Azure SQL Database** | Azure SQL automated backup (native) + export to Blob for long-term |
| **AWS RDS** | RDS automated backup + manual snapshots for long-term |
| **SQL Server (on-prem)** | Veeam Backup + native SQL Server transaction log backups |
| **PostgreSQL / MySQL** | pg_dump / mysqldump + Veeam for VM-level backup |
| **Oracle Database** | RMAN (Recovery Manager) + Veeam for VM-level |
| **MongoDB** | mongodump + Veeam Cloud Data Management (paid) |

**Recommendation:** Hybrid approach (native database backup + VM-level backup)

### Physical Servers

**Windows Servers:**

- Veeam Agent for Microsoft Windows (centrally managed via Veeam Backup & Replication)
- Windows Server Backup (built-in, basic features only)

**Linux Servers:**

- Veeam Agent for Linux
- Bacula (open-source, complex)
- rsync + scripting (manual, not recommended for production)

**Recommendation:** Veeam Agent (Windows/Linux)

## STEP 4: CALCULATE Backup Storage Requirements

**Objective:** Determine backup storage capacity needed.

**Duration:** Week 1

**Storage Calculation Methodology:**

**Formula:**
```
Total Backup Storage = Σ (System_Data_Size × Retention_Days × Change_Rate × Compression_Factor)
```

**Step-by-Step Calculation:**

**1. For Each System, Identify:**

- Data size (GB)
- Retention requirement (days) - from BIA tier
- Change rate (% daily changes) - estimate or measure
- Compression ratio - typical values:
  - Databases: 1.5:1 to 2:1
  - File servers: 2:1 to 3:1
  - VMs: 2:1
  - Media files (photos, videos): 1:1 (already compressed)

**2. Calculate Storage Per System:**

```
Example (Tier 1 Database):
  Data Size: 500 GB
  Retention: 30 days
  Change Rate: 10% daily (50 GB changes/day)
  
  Full Backup: 500 GB (weekly)
  Incremental: 50 GB/day × 6 days = 300 GB
  Weekly total: 500 GB + 300 GB = 800 GB
  Monthly storage (4 weeks): 800 GB × 4 = 3,200 GB = 3.2 TB
  With compression (2:1): 3.2 TB / 2 = 1.6 TB
```

**3. Sum Across All Systems:**

| Tier | Systems | Avg Size | Retention | Total Storage (uncompressed) | Compressed (2:1) |
|------|---------|----------|-----------|------------------------------|------------------|
| Tier 1 | 15 | 200 GB | 30 days | 90 TB | 45 TB |
| Tier 2 | 25 | 150 GB | 14 days | 52.5 TB | 26.25 TB |
| Tier 3 | 30 | 100 GB | 7 days | 21 TB | 10.5 TB |
| Tier 4 | 10 | 50 GB | 7 days | 3.5 TB | 1.75 TB |
| **TOTAL** | **80** | - | - | **167 TB** | **83.5 TB** |

**4. Add Overhead (20% buffer for growth):**
```
Total Required: 83.5 TB × 1.2 = 100.2 TB ≈ 100 TB
```

**5. Split Primary vs. Offsite:**

- Primary (on-premises): 30-day retention → 60 TB
- Offsite (cloud): 30-day retention → 60 TB (replica of primary)
- **Total: 120 TB** (100 TB × 1.2 safety margin)

**6. Cloud Storage Cost Estimation (Azure Example):**

```
Azure Blob Storage (Cool Tier - for backup):
  Cost: $0.01 per GB/month (approximately)
  Storage: 60 TB = 60,000 GB
  Monthly Cost: 60,000 GB × $0.01 = $600/month = CHF 540/month (approx)
  Annual Cost: CHF 6,480/year
```

**Quality Check:**

- ✓ Compression ratio realistic (2:1 typical)
- ✓ Change rate estimated or measured (not guessed as 100%)
- ✓ Buffer included (20% recommended for growth)
- ✓ Primary + offsite storage both sized
- ✓ Cost estimate approved by management

## STEP 5: CONFIGURE Backup Schedules (RPO-Aligned)

**Objective:** Configure backup job schedules to meet RPO requirements from BIA.

**Duration:** Week 4-6

**Backup Schedule Framework:**

**From BIA → To Backup Schedule:**

| RPO Requirement | Backup Frequency | Backup Type | Example Schedule |
|-----------------|-----------------|-------------|------------------|
| **Near-zero (continuous)** | Continuous replication + 15min log backups | Transaction logs | SQL: Log backup every 15 min |
| **≤ 1 hour** | Hourly incremental + 15min logs | Incremental | 00:00, 01:00, 02:00... (24×/day) + logs |
| **≤ 4 hours** | 4-hourly incremental | Incremental | 00:00, 04:00, 08:00, 12:00, 16:00, 20:00 |
| **≤ 24 hours** | Daily full or incremental | Full (weekly) + Incremental (daily) | Full: Sunday 02:00, Incremental: Mon-Sat 02:00 |
| **≤ 7 days** | Weekly full | Full | Sunday 02:00 |

**Backup Job Types:**

**1. Full Backup:**

- Backs up ALL data
- Slowest, largest backup
- Required: At least weekly for Tier 1/2 systems
- Example: Sunday 02:00 (overnight, low usage period)

**2. Incremental Backup:**

- Backs up only CHANGES since last backup (any type)
- Fastest, smallest backup
- Most common for frequent backups
- Example: Monday-Saturday 02:00 (after Sunday full)

**3. Differential Backup:**

- Backs up all changes since last FULL backup
- Faster restore than incremental (only need full + last differential)
- Larger than incremental, slower than full
- Less common (incrementals preferred in modern backup solutions)

**4. Transaction Log Backup (Databases):**

- Backs up database transaction logs
- Enables point-in-time recovery
- Required for near-zero RPO databases
- Example: Every 15 minutes for Tier 1 databases

**Backup Schedule Examples (Swiss Business Context):**

**Example 1: Payment Database (Tier 1, RPO 1h)**
```
Backup Schedule:

  - Full Backup: Sunday 02:00 (weekly)
  - Incremental Backup: Every 1 hour (24×/day)
  - Transaction Log Backup: Every 15 minutes

Implementation (Azure SQL):

  - Azure SQL automated backup (full: weekly, differential: 12h, log: 5-10min)
  - Retention: 30 days (policy setting)
  - Geo-redundant: Enabled (replicated to paired region)

```

**Example 2: E-commerce Website (Tier 1, RPO 4h)**
```
Backup Schedule:

  - Full Backup: Sunday 02:00
  - Incremental Backup: Every 4 hours (00:00, 04:00, 08:00, 12:00, 16:00, 20:00)

Implementation (Veeam):

  - Backup Job: "Ecommerce-Tier1"
  - Schedule: Daily at 02:00 (full on Sunday, incremental Mon-Sat)
  - Additional: Backup copy job to Azure Blob (4-hourly)
  - Retention: 30 days local, 30 days cloud

```

**Example 3: CRM System (Tier 2, RPO 24h)**
```
Backup Schedule:

  - Full Backup: Sunday 02:00
  - Incremental Backup: Daily at 02:00 (Monday-Saturday)

Implementation (Salesforce):

  - Veeam Backup for Salesforce OR Spanning Backup
  - Schedule: Daily at 02:00 UTC
  - Retention: 14 days
  - Cloud storage: AWS S3

```

**Backup Window Management:**

**Challenge:** All backups want to run during low-usage period (e.g., 02:00-06:00), but:

- Limited network bandwidth
- Limited storage I/O
- Limited backup server capacity

**Solution: Stagger Backup Jobs**

```
Backup Window: 02:00 - 06:00 (4 hours)

Tier 1 (High Priority):

  - 02:00-03:00: Payment DB, E-commerce DB (critical databases - fast)
  - 03:00-04:00: E-commerce App Servers, CRM

Tier 2 (Medium Priority):

  - 04:00-05:00: Email servers, File servers
  - 05:00-06:00: ERP, HR systems

Tier 3 (Low Priority):

  - 06:00+: Intranet, Dev/Test (can run during business hours, less critical)

```

**Document in Backup Assessment Workbook - Sheet 2: Backup Schedules**

- System Name
- Tier
- RPO Requirement (from BIA)
- Backup Frequency (configured)
- Backup Type (Full/Incremental/Differential/Log)
- Backup Time (schedule)
- Backup Window (duration)
- Retention Period (days)
- Status (Configured/Pending)

**Quality Check:**

- ✓ Backup frequency meets RPO requirement
- ✓ Backup windows don't overlap (staggered)
- ✓ Critical systems (Tier 1) backed up first
- ✓ Retention period matches tier requirement (Tier 1 = 30 days, etc.)

---

# STEP 6: IMPLEMENT Offsite/Cloud Backup

**Objective:** Establish geographic separation of backups for disaster recovery.

**Duration:** Week 3-4

**Critical Principle:** On-site backup alone is NOT sufficient. Site-wide disasters (fire, flood, ransomware) can destroy both production and backup data if co-located.

**3-2-1 Backup Rule (Industry Best Practice):**

- **3 copies** of data (1 production + 2 backups)
- **2 different media types** (e.g., disk + cloud, disk + tape)
- **1 copy offsite** (geographic separation)

## Offsite Backup Options

### Option 1: Cloud Backup (Recommended for Most Organizations)

**Azure Blob Storage (Example):**

**Configuration:**
```
Primary Backup: On-premises Veeam repository (30-day retention)
Offsite Backup: Azure Blob Storage Cool tier (30-day retention)

Veeam Backup Copy Job:
  Source: Primary backup repository
  Target: Azure Blob Storage
  Schedule: Nightly at 22:00 (after primary backup completes)
  Bandwidth: Throttled to 80 Mbps (leave 20% WAN for business use)
  Encryption: AES-256 (before upload)
  Storage tier: Cool (cost-optimized for backup)
```

**Azure Storage Account Setup:**
```
Storage Account: [orgname]backup[region]
Region: West Europe (if production in Switzerland/EU)
Redundancy: GRS (Geo-Redundant Storage) - replicated to paired region
Access tier: Cool (backup storage, infrequent access)
Network: Private endpoint (secure connection via VPN/ExpressRoute)
Retention: Lifecycle management (move to Archive tier after 90 days)
```

**Cost Example (60 TB offsite backup):**
```
Azure Blob Storage Cool Tier:
  Storage: 60 TB × CHF 0.009/GB/month = CHF 540/month
  Write operations (backup copy): ~CHF 50/month
  Data egress (restore - if needed): CHF 0 (within Azure), CHF 0.08/GB (to internet)
  Total: ~CHF 590/month = CHF 7,080/year

Compare to:
  Tape backup: Initial CHF 15K (tape library) + CHF 2K/year (tapes)
  Secondary datacenter: CHF 30K+ setup + CHF 10K+/year
  
→ Cloud backup most cost-effective for SME
```

**AWS S3 (Alternative):**
```
Storage Class: S3 Glacier Instant Retrieval (for backup)
Cost: Similar to Azure Cool tier (~CHF 0.004/GB/month)
Setup: Similar to Azure (S3 bucket, lifecycle policies, encryption)
```

### Option 2: Tape Backup (Legacy, Decreasing Usage)

**When Tape Still Makes Sense:**

- Very large datasets (PB-scale) where cloud egress cost prohibitive
- Air-gapped requirement (tape physically disconnected = ransomware-proof)
- Regulatory compliance requiring physical media

**Tape Backup Setup:**
```
Tape Library: Dell EMC PowerVault TL4000 (example)
Capacity: 1.5 PB (compressed)
Cost: CHF 20K initial + CHF 3K/year (tapes)

Backup Schedule:

  - Weekly full backup to tape
  - Tapes rotated offsite (secure storage facility)
  - Retention: 1 year on tape

```

**Challenges:**

- Slow restore (tape retrieval + read time)
- Management overhead (tape rotation, tracking)
- Technology obsolescence (tape drives/formats change)

**Recommendation:** Cloud backup preferred unless specific tape requirement

### Option 3: DR Site/Colo (Enterprise)

**When DR Site Appropriate:**

- Large enterprise (500+ systems)
- RTO <1 hour requirement (DR site allows instant failover)
- Compliance requirement for owned infrastructure

**Setup:**
```
Primary Site: Zurich datacenter
DR Site: Basel datacenter (>100 km separation)

Replication:
  Tier 1 systems: Synchronous replication to DR site (near-zero RPO)
  Tier 2 systems: Asynchronous replication (hourly)
  Tier 3/4: Backup copy to DR site (daily)
```

**Cost:** CHF 50K-200K/year (rental + infrastructure + connectivity)

## Offsite Backup Implementation Steps

**Step 1: Select Offsite Target**

For Swiss SME, recommend: **Azure Blob Storage** (Cool tier)

**Step 2: Configure Backup Copy Job (Veeam Example)**

```
Veeam Backup Copy Job Configuration:

Job Name: "Offsite-Tier1-Azure"
Source: Backup jobs for Tier 1 systems
Target: Azure Blob Storage (Cool tier)
Schedule: 

  - After primary backup completes (automatic)
  - Sync interval: Daily

Retention: 30 days (Tier 1 requirement)
Bandwidth: 

  - Throttle to 80 Mbps (weekdays 08:00-18:00)
  - Unlimited (nights/weekends)

Encryption: Enabled (AES-256, password-protected)
```

**Step 3: Test Offsite Backup**

```
Validation Steps:
1. Verify backup copy completes successfully
2. Browse Azure Blob Storage → Confirm backup files present
3. Restore test file from Azure → Validate recovery works
4. Measure restore time from cloud (typically slower than on-premises)
5. Document restore procedure from cloud
```

**Step 4: Monitor Offsite Backup**

```
Monitoring Checks:

- Backup copy job completion (daily)
- Azure storage capacity (monthly)
- Cost monitoring (monthly - avoid surprise bills)
- Network bandwidth usage (ensure not saturating WAN)

```

## Geographic Separation Guidelines

**Minimum Distance:** 100 km (protects against regional disasters)

**Example (Swiss Context):**

- Production: Zurich
- Offsite backup: Azure West Europe (Amsterdam) - 800 km
- Alternative: Azure Switzerland North (Zurich region) + Azure Switzerland West (Geneva region) - 250 km

**Regulatory Considerations:**

**Swiss nDSG / GDPR Data Residency:**

- Personal data of Swiss/EU residents should stay in Switzerland/EU
- Azure regions: Switzerland North, Switzerland West, West Europe (all compliant)
- Avoid: Azure US regions (data residency issue for personal data)

**FINMA (Swiss Financial):**

- Financial institutions: Data must remain in Switzerland or contractually approved countries
- Recommendation: Azure Switzerland North + Switzerland West

**Quality Check:**

- ✓ Offsite backup configured for all Tier 1 and Tier 2 systems
- ✓ Geographic separation >100 km
- ✓ Data residency requirements met (nDSG, GDPR, FINMA)
- ✓ Offsite restore tested and documented
- ✓ Cost monitoring in place

---

# STEP 7: CONFIGURE Backup Encryption

**Objective:** Protect backup data confidentiality per data classification requirements.

**Duration:** Week 4

**Encryption Requirements (from Policy):**

| Data Classification | Backup Encryption Requirement | Key Management |
|---------------------|-------------------------------|----------------|
| **Restricted** | AES-256 mandatory, encrypted at rest + in transit | Hardware Security Module (HSM) or Azure Key Vault |
| **Confidential** | AES-256 required | Centralized key management |
| **Internal** | Encryption recommended | Standard key storage |
| **Public** | No encryption required | N/A |

## Encryption Points

**1. Encryption in Transit (Network)**

Protects backup data while transferring from source to backup repository.

**Methods:**

- **TLS/SSL** (HTTPS, default for cloud backup)
- **VPN** (site-to-site VPN for WAN backup)
- **Private connectivity** (Azure ExpressRoute, AWS Direct Connect)

**Example (Veeam to Azure):**
```
Backup traffic to Azure Blob Storage:

  - Protocol: HTTPS (TLS 1.2+)
  - Encryption: Built-in (Azure enforces encryption in transit)
  - Additional: VPN optional (for extra security)

```

**2. Encryption at Rest (Storage)**

Protects backup data while stored in backup repository.

**Cloud Storage - Automatic:**

- **Azure Blob Storage:** Encrypted by default (AES-256)
- **AWS S3:** Encrypted by default (AES-256)
- **Google Cloud Storage:** Encrypted by default (AES-256)

**On-Premises Storage - Manual Configuration:**

**Veeam Backup Encryption:**
```
Veeam Backup Job Configuration:

Encryption: Enabled
Algorithm: AES-256
Encryption key: 

  - Password-based (for small environments)
  - Enterprise Key Management (for large environments - integrates with Azure Key Vault)
  
Storage: 

  - Backup files encrypted before writing to disk
  - Each backup job can have different encryption key

```

**Example Configuration (Tier 1 Payment Database):**
```
Backup Job: "Payment-DB-Tier1"
Encryption: Enabled
Algorithm: AES-256
Key: Stored in Azure Key Vault "BackupKeys-Prod"
Key rotation: Annual (January)
Recovery: Requires Azure Key Vault access (role-based)
```

## Key Management

**Critical Principle:** Lose the encryption key = Lose the backup. Key management is as critical as backup itself.

**Key Management Options:**

**Option 1: Password-Based (Simple, Small Environments)**

```
Veeam Encryption Password:
  Password: [Strong password, 20+ characters]
  Storage: Password manager (1Password, LastPass, Bitwarden)
  Access: Backup admin + 2 backup users (redundancy)
  
Recovery Procedure:
  1. Retrieve password from password manager
  2. Enter password in Veeam restore wizard
  3. Restore proceeds
```

**Risks:**

- Password forgotten = backups unrecoverable
- Password on paper/email = security risk

**Mitigation:**

- Store password in enterprise password manager
- Document in secure location (physical safe)
- Test password retrieval quarterly

**Option 2: Enterprise Key Management (Recommended for Tier 1 Data)**

```
Azure Key Vault Integration:

Key Vault: "BackupKeys-Production"
Region: Switzerland North (data residency)
Access: 

  - Veeam Backup Server: Managed Identity
  - Backup Admins: RBAC role "Key Vault Secrets User"

Keys:

  - "Payment-DB-Key" (AES-256)
  - "Ecommerce-DB-Key" (AES-256)
  - Rotation: Automated (annual)
  
Audit:

  - All key access logged (Azure Monitor)
  - Alerting on unusual access patterns

```

**Benefits:**

- Centralized key management
- Automated key rotation
- Audit trail of key access
- RBAC-based access control
- HSM-backed keys (optional, for FINMA compliance)

**Cost:** Azure Key Vault: CHF 0.03 per 10,000 operations (minimal cost)

## Encryption Configuration Steps

**Step 1: Define Encryption Policy**

Per data classification:

- Restricted → AES-256, Azure Key Vault
- Confidential → AES-256, password-based acceptable
- Internal → AES-256 recommended
- Public → No encryption

**Step 2: Configure Encryption per Backup Job**

**Veeam Example:**
```
For each Tier 1 backup job:
  1. Edit backup job
  2. Storage → Advanced → Enable encryption
  3. Select: AES-256
  4. Key source: Enterprise Key Management (Azure Key Vault)
  5. Select key from vault
  6. Save
```

**Step 3: Test Encrypted Restore**

```
Test Procedure:
  1. Initiate restore from encrypted backup
  2. Veeam requests encryption key
  3. Authenticate to Azure Key Vault (Managed Identity)
  4. Key retrieved automatically
  5. Restore proceeds
  6. Validate data integrity
```

**Step 4: Document Key Management**

```
Key Management Documentation:

Key Inventory:

  - System: Payment Database
  - Key Name: "Payment-DB-Key"
  - Key Vault: "BackupKeys-Production"
  - Algorithm: AES-256
  - Created: 2025-01-15
  - Next Rotation: 2026-01-15
  - Access: Veeam-Prod (Managed Identity), backup-admins@org.ch (RBAC)

Recovery Procedure:
  1. Authenticate to Azure (backup admin account)
  2. Access Key Vault "BackupKeys-Production"
  3. Retrieve key "Payment-DB-Key"
  4. Provide to Veeam restore wizard
  5. Restore proceeds
```

**Quality Check:**

- ✓ All Restricted/Confidential data backups encrypted (AES-256)
- ✓ Encryption keys stored securely (password manager or Key Vault)
- ✓ Key access documented and restricted
- ✓ Encrypted restore tested successfully
- ✓ Key recovery procedure documented

---

# STEP 8: SETUP Backup Monitoring & Alerting

**Objective:** Automated monitoring to detect backup failures immediately.

**Duration:** Week 8

**Critical Principle:** "Backups running green" in the backup console is NOT sufficient monitoring. You need:

- Automated alerts on failure
- Centralized monitoring (not just backup console)
- Escalation to on-call (24/7 for Tier 1)
- Trend analysis (detecting degradation before failure)

## Monitoring Requirements by Tier

| Tier | Monitoring Frequency | Alerting | Escalation | Dashboard |
|------|---------------------|----------|------------|-----------|
| **Tier 1** | Real-time (24/7) | Immediate alert on failure | On-call escalation | Executive dashboard (weekly) |
| **Tier 2** | Daily | Alert within 4 hours | Email to backup team | Operations dashboard |
| **Tier 3** | Daily | Alert within 24 hours | Email | Self-service |
| **Tier 4** | Weekly | Best-effort | None | None |

## Monitoring Metrics

**1. Backup Job Status (Primary Metric)**

Monitors: Did backup complete successfully?

**States:**

- **Success** (green) - Backup completed, all data protected
- **Warning** (yellow) - Backup completed with warnings (e.g., some files skipped)
- **Failed** (red) - Backup failed, data NOT protected

**Alert Triggers:**

- Tier 1: Failed OR Warning → Immediate alert (SMS/call)
- Tier 2: Failed → Alert within 4 hours (email + ticket)
- Tier 3: Failed for 2 consecutive days → Alert (email)

**2. Backup Duration (Trend Metric)**

Monitors: How long did backup take?

**Purpose:** Detect degradation (backup taking longer = potential issue)

**Example Trend:**
```
Payment DB Backup Duration:
  Week 1: 45 minutes (baseline)
  Week 2: 47 minutes (+4%)
  Week 3: 52 minutes (+16%)
  Week 4: 68 minutes (+51%) ← ALERT: Investigate why
  
Cause: Database growth (normal) OR backup infrastructure issue (abnormal)
Action: Review and increase backup resources if needed
```

**Alert Trigger:**

- Duration >150% of baseline for 3 consecutive days → Investigate

**3. Backup Size (Trend Metric)**

Monitors: How much data was backed up?

**Purpose:** Detect unexpected changes

**Example Scenarios:**
```
Normal Growth:
  Day 1: 500 GB
  Day 2: 502 GB (+0.4%)
  Day 3: 504 GB (+0.4%)
  → Healthy growth trend

Unexpected Change:
  Day 1: 500 GB
  Day 2: 750 GB (+50%) ← ALERT: Investigate
  
Causes:

  - Legitimate: Large data import (e.g., end-of-month reporting)
  - Issue: Backup capturing unnecessary data (misconfiguration)
  - Attack: Ransomware encrypting files (creates many new files)

```

**Alert Trigger:**

- Backup size change >20% from previous day → Investigate

**4. Storage Capacity (Capacity Metric)**

Monitors: Backup repository capacity utilization

**Alert Thresholds:**

- 70% full → Warning (plan capacity expansion)
- 85% full → Critical (expand capacity immediately)
- 95% full → Emergency (backups will fail soon)

**Example:**
```
Backup Repository: Primary-Backup-NAS
Capacity: 100 TB
Used: 82 TB (82%)
Free: 18 TB

Status: WARNING (>80%)
Action: Provision additional storage within 30 days
Estimate: Current growth 2 TB/month → Capacity in 9 months
Plan: Expand to 150 TB or implement lifecycle management (move old backups to archive)
```

**5. Restore Test Status (Compliance Metric)**

Monitors: Are restore tests being performed per policy?

**Requirements:**

- Tier 1: Quarterly restore testing
- Tier 2: Semi-annual restore testing
- Tier 3: Annual restore testing

**Alert Trigger:**

- Restore test overdue >30 days → Alert to BC/DR Coordinator

## Monitoring Implementation

### Option 1: Veeam ONE (If Using Veeam)

**Setup:**
```
Veeam ONE Installation:
  Server: Monitoring-VM (Windows Server)
  Database: SQL Server (Veeam ONE database)
  License: Included with Veeam Backup & Replication license

Configuration:
  1. Add Veeam Backup Servers to Veeam ONE
  2. Configure alerts:

     - Backup job failed (Tier 1) → Email + SMS
     - Backup job failed (Tier 2) → Email
     - Backup repository >80% full → Email
     - Long-running backup (>2× baseline) → Email

  3. Configure dashboards:

     - Executive Dashboard (backup status summary)
     - Operations Dashboard (detailed backup job status)

  4. Schedule reports:

     - Weekly backup report (email to IT management)
     - Monthly capacity report (email to storage team)

```

**Cost:** Included with Veeam license (no additional cost)

### Option 2: Azure Monitor (If Using Azure Backup)

**Setup:**
```
Azure Monitor Configuration:

Metrics:

  - Backup job status (Azure Backup built-in metric)
  - Backup vault capacity
  - Restore test success rate (custom metric)

Alerts:

  - Backup failure → Action Group: Email to backup-team@org.ch + SMS to on-call
  - Vault capacity >80% → Email to storage-team@org.ch

Log Analytics:

  - Backup logs ingested to Log Analytics workspace
  - Custom queries for trend analysis
  - Dashboards in Azure Workbook

Reports:

  - Azure Backup Reports (built-in)
  - Custom Power BI reports (using Log Analytics data)

```

**Cost:** 

- Log Analytics: ~CHF 2/GB ingested (typical: CHF 50-100/month)
- Alerts: CHF 0.10 per alert (minimal)

### Option 3: Generic Monitoring (Zabbix, PRTG, etc.)

**Setup:**
```
Zabbix Monitoring:

Template: Veeam Backup Monitoring
Metrics:

  - Backup job status (via Veeam API or PowerShell script)
  - Backup repository capacity (SNMP or WMI)
  - Backup job duration

Triggers:

  - Backup failed (Tier 1) → Severity: High → Escalation: On-call
  - Backup failed (Tier 2) → Severity: Medium → Email
  - Repository >85% → Severity: High → Email

Dashboards:

  - Backup Status Dashboard (all jobs, color-coded)
  - Capacity Dashboard (repository utilization)

```

**Cost:** Open-source (free) or PRTG (paid, ~CHF 1,500/year for 500 sensors)

## Alert Configuration

**Tiered Alerting Structure:**

```
Tier 1 Backup Failure Alert:

Recipients:

  - Primary: backup-admin@org.ch (email + SMS)
  - Escalation (15 min): backup-oncall@org.ch (phone call)
  - Escalation (30 min): it-management@org.ch

Message:
  Subject: [CRITICAL] Tier 1 Backup Failed - Payment Database
  Body:
    System: Payment Database (SYS-015)
    Tier: Tier 1 (Critical)
    Backup Job: Payment-DB-Backup
    Status: FAILED
    Error: Network connection timeout
    Impact: RPO at risk (last successful backup: 24h ago)
    Action Required: Investigate and remediate immediately
    
Tier 2 Backup Failure Alert:

Recipients:

  - Primary: backup-team@org.ch (email only)
  - No escalation (handled during business hours)

Message:
  Subject: [WARNING] Tier 2 Backup Failed - CRM System
  Body:
    System: CRM System
    Tier: Tier 2
    Status: FAILED
    Error: Insufficient storage space
    Action Required: Investigate within 4 hours
```

**Quality Check:**

- ✓ Monitoring configured for all Tier 1 and Tier 2 systems
- ✓ Alerts escalate appropriately (Tier 1 = immediate, Tier 2 = 4h)
- ✓ Trend analysis in place (backup duration, size, capacity)
- ✓ Dashboards accessible to management
- ✓ Alert fatigue avoided (only meaningful alerts)

---

# STEP 9: DOCUMENT Recovery Procedures

**Objective:** Step-by-step recovery runbooks for each critical system.

**Duration:** Week 9

**Critical Principle:** Recovery procedures must be documented BEFORE disaster, not discovered DURING disaster.

## Recovery Procedure Template

**For Each Tier 1 and Tier 2 System:**

```
SYSTEM RECOVERY PROCEDURE
System: [System Name]
Tier: [Tier 1/2/3]
RPO: [X hours]
RTO: [X hours]
Last Updated: [Date]
Owner: [Name]

─────────────────────────────────────────────────
PREREQUISITES

Required Access:

  - Veeam Backup Console: [Role]
  - Azure Portal: [Subscription]
  - System credentials: [Where stored]

Required Tools:

  - Veeam Backup & Replication Console
  - Azure Portal access
  - RDP/SSH client

Estimated Duration: [X hours]

─────────────────────────────────────────────────
RECOVERY PROCEDURE

STEP 1: Assess Situation
  □ Confirm system is down/data is lost
  □ Identify last known good state
  □ Check backup availability:

    - Last successful backup: [How to check]
    - Backup location: [Path]
    - Backup encryption: [Yes/No, key location]

STEP 2: Prepare Recovery Environment
  □ Verify target infrastructure available:

    - VM host: [Details]
    - Network: [VLAN, IP]
    - Storage: [Datastore]

  □ Notify stakeholders:

    - BC/DR Coordinator: [Contact]
    - System Owner: [Contact]
    - Users: [Communication plan]

STEP 3: Initiate Restore
  □ Open Veeam Backup & Replication Console
  □ Navigate to: Home → Backups → [Backup Job Name]
  □ Right-click → Restore → [Restore Type]
  □ Select restore point: [Criteria]
  □ Configure restore options:

    - Target location: [Details]
    - Network settings: [IP address, VLAN]
    - Power on after restore: [Yes/No]

  □ Start restore

STEP 4: Monitor Restore Progress
  □ Watch restore progress in Veeam console
  □ Estimated restore time: [Duration based on data size]
  □ Document any warnings/errors
  □ Contact: backup-team@org.ch if issues

STEP 5: Validate Restored System
  □ System powers on successfully
  □ Network connectivity verified
  □ Services/applications start correctly
  □ Data integrity spot-check:

    - [Specific checks for this system]

  □ Application functionality test:

    - [Specific tests for this system]

STEP 6: Cut Over to Production
  □ Update DNS (if needed)
  □ Redirect traffic to restored system
  □ Monitor system performance
  □ Notify stakeholders of recovery completion

STEP 7: Post-Recovery
  □ Document recovery time (actual vs. RTO)
  □ Document data loss (actual vs. RPO)
  □ Update incident report
  □ Schedule lessons learned review

─────────────────────────────────────────────────
ROLLBACK PROCEDURE

If restore fails or validation fails:
  □ Stop restored system
  □ Investigate issue
  □ Attempt alternative restore point
  □ Escalate to: [Vendor support / senior admin]

─────────────────────────────────────────────────
CONTACTS

Primary: [Backup Admin] - [Phone] - [Email]
Escalation: [IT Manager] - [Phone] - [Email]
Vendor Support: [Veeam Support] - [Contract #] - [Phone]

─────────────────────────────────────────────────
CHANGE LOG

| Date | Change | Author |
|------|--------|--------|
| 2026-01-22 | Initial version | Backup Admin |
```

## System-Specific Recovery Examples

**Example 1: Payment Database (Azure SQL)**

```
SYSTEM: Payment Database (SYS-015)
TYPE: Azure SQL Database
TIER: Tier 1
RPO: 1 hour
RTO: 1 hour

RECOVERY PROCEDURE:

STEP 1: Assess
  □ Confirm database unavailable in Azure Portal
  □ Identify required restore point:

    - Check transaction timestamp of last known good state
    - Azure SQL backup: Point-in-time restore available (5-10min granularity)

STEP 2: Initiate Restore (Azure Portal)
  □ Navigate to: Azure Portal → SQL databases → [DB Name]
  □ Click: Restore
  □ Select: Point-in-time restore
  □ Restore point: [Date/Time - within last 30 days]
  □ Target:

    - Option A: Restore to new database (test first, then cut over)
    - Option B: Overwrite existing database (faster but riskier)

  □ Start restore

STEP 3: Monitor
  □ Restore duration: Typically 15-30 min for 500GB database
  □ Azure Portal shows progress

STEP 4: Validate
  □ Connect to restored database:

    - Server: [servername].database.windows.net
    - Database: [dbname]-restored
    - Credentials: SQL Admin (from Key Vault)

  □ Run validation queries:

    - SELECT COUNT(*) FROM Orders WHERE OrderDate = '[Yesterday]'
    - SELECT MAX(OrderID) FROM Orders
    - Compare with expected values

  □ Application connection test:

    - Update application config to point to restored DB
    - Test order processing
    - Test payment processing

STEP 5: Cut Over
  □ If Option A (new database):

    - Update DNS alias to point to restored database
    - Estimated cutover: 2 minutes

  □ If Option B (overwrite):

    - Already in production

  □ Monitor application logs for errors

STEP 6: Post-Recovery
  □ Document actual recovery time
  □ Document data loss (should be near-zero due to 1h RPO)
  □ Investigate root cause of original failure
  □ Update runbook if lessons learned
```

**Example 2: E-commerce Website (Veeam VM Restore)**

```
SYSTEM: E-commerce Website (SYS-010)
TYPE: Virtual Machine (VMware)
TIER: Tier 1
RPO: 4 hours
RTO: 4 hours

RECOVERY PROCEDURE:

STEP 1: Assess
  □ Confirm VM down or data corrupted
  □ Identify restore point:

    - Veeam Backup Console → Backups → Ecommerce-Tier1
    - Select restore point within RPO (≤4 hours old)

STEP 2: Initiate Restore
  □ Veeam Console → Right-click backup → Restore → Entire VM
  □ Restore mode: 

    - Restore to original location (overwrite existing VM)
    - OR Restore to new location (test first, then cut over)

  □ Options:

    - Power on VM after restore: Yes
    - Network: Reconnect network adapter
    - Quick rollback: Disabled (full restore)

  □ Start restore

STEP 3: Monitor
  □ Restore duration: Estimate 60-90 min (200 GB VM)
  □ Watch progress in Veeam console
  □ Do NOT interrupt restore

STEP 4: Validate
  □ VM powered on successfully
  □ RDP/SSH login: Verify OS accessible
  □ Check services:

    - Web server (IIS / Nginx): Running
    - Application server: Running
    - Check application logs: No errors

  □ Functionality test:

    - Browse to: https://shop.org.ch
    - Test: Add item to cart, proceed to checkout
    - Verify: Database connection working

  □ Data validation:

    - Check product catalog: Recent products visible
    - Check orders: Orders from last 4 hours present (within RPO)

STEP 5: Cut Over
  □ If restored to new VM:

    - Update load balancer to include restored VM
    - Disable old VM

  □ If restored to original location:

    - Already in production

  □ Monitor web traffic and error logs

STEP 6: Post-Recovery
  □ Document recovery time (actual)
  □ Document data loss (orders in last 4h may be lost - within RPO)
  □ Customer notification (if needed)
  □ Root cause analysis
```

## Recovery Procedure Storage

**Location:** Centralized documentation repository

**Options:**

- SharePoint (ISMS Documentation library)
- Confluence / Wiki
- Azure DevOps Wiki
- GitHub (private repo)

**Accessibility:**

- Must be accessible during disaster (cloud-hosted preferred)
- Must be accessible to backup team (permissions)
- Version-controlled (track changes)

**Quality Check:**

- ✓ Recovery procedures documented for all Tier 1 and Tier 2 systems
- ✓ Procedures tested (validated during restore tests)
- ✓ Procedures accessible to backup team
- ✓ Contact information current
- ✓ Procedures reviewed annually

---

# STEP 10: TEST Restore Capability

**Objective:** Prove backups can be successfully restored.

**Duration:** Ongoing (per testing schedule)

**Critical Principle:** Untested backups = no backups. You don't have a backup until you've successfully restored from it.

## Testing Requirements by Tier

| Tier | Testing Frequency | Test Type | Success Criteria |
|------|------------------|-----------|------------------|
| **Tier 1** | **Quarterly** (Q1, Q2, Q3, Q4) | Full restore to isolated test environment | Complete system recovery, functionality validated, RTO met |
| **Tier 2** | **Semi-annual** (Q2, Q4) | Full restore to test environment | System recoverable, basic functionality validated |
| **Tier 3** | **Annual** (Q4) | Sample file/database restore | Data recoverable |
| **Tier 4** | No requirement | Optional | N/A |

## Restore Test Types

**1. File-Level Restore (Basic Test)**

**Scope:** Restore individual file(s)

**Use Case:** Accidental deletion, file corruption

**Procedure:**
```
1. Select file to restore (e.g., document from file server)
2. Identify backup containing file (date/time)
3. Initiate restore to alternative location (not overwrite)
4. Validate file integrity:

   - File size correct
   - File opens successfully
   - Content as expected

5. Document: Date, system, file name, result (success/failure)
```

**Duration:** 10-15 minutes

**2. Database Restore (Medium Test)**

**Scope:** Restore entire database

**Use Case:** Database corruption, data loss

**Procedure:**
```
1. Select database backup (e.g., CRM database from last night)
2. Restore to test database server (isolated from production)
3. Validate database:

   - Database accessible (SQL login works)
   - Row counts correct (compare with production)
   - Sample queries return expected results
   - Application can connect to test database

4. Document: Date, database, restore time, result
```

**Duration:** 30-60 minutes

**3. Full VM Restore (Comprehensive Test)**

**Scope:** Restore entire virtual machine

**Use Case:** Complete system failure

**Procedure:**
```
1. Select VM backup (e.g., e-commerce server from last week)
2. Restore to isolated test network (VLAN)
3. Power on restored VM
4. Validate system:

   - OS boots successfully
   - Services start automatically
   - Network connectivity (within test VLAN)
   - Application functionality (web server responds)
   - User login works

5. Performance test:

   - Load test (if applicable)
   - Response time acceptable

6. Document: Date, VM, restore time, RTO achieved, result
```

**Duration:** 1-3 hours

**4. Disaster Recovery Scenario Test (Full Test)**

**Scope:** Restore multiple interdependent systems

**Use Case:** Site-wide disaster, complete recovery

**Procedure:**
```
1. Simulate disaster scenario (e.g., "Primary datacenter unavailable")
2. Restore critical systems in dependency order:

   - Active Directory (authentication)
   - Network infrastructure (connectivity)
   - Database servers (data tier)
   - Application servers (app tier)
   - Web servers (presentation tier)

3. Validate end-to-end functionality:

   - User can login (AD works)
   - User can access application (network works)
   - User can perform business transaction (database works)
   - Transaction completes successfully (application works)

4. Measure RTO: Time from disaster declaration to system functional
5. Document: Full scenario report, lessons learned, gaps identified
```

**Duration:** 4-8 hours (coordinated exercise)

## Restore Testing Schedule

**Quarterly Testing (Tier 1 Systems):**

```
Q1 (January-March):
  Week 1: Payment Database (restore + validation)
  Week 2: E-commerce Platform (full VM restore)
  Week 3: Manufacturing Control System (restore + functionality test)

Q2 (April-June):
  Week 1: Payment Database
  Week 2: E-commerce Platform
  Week 3: [Next Tier 1 system]

Q3 (July-September):
  [Same pattern]

Q4 (October-December):
  [Same pattern]

  + DR Scenario Test (full recovery exercise)

```

**Semi-Annual Testing (Tier 2 Systems):**

```
Q2 (June):
  CRM System, Email (Microsoft 365), ERP System

Q4 (December):
  [Same systems]
```

## Restore Test Documentation

**For Each Test, Document:**

```
BACKUP RESTORE TEST REPORT

Test Date: [Date]
Tester: [Name]
System: [System Name]
Tier: [Tier 1/2/3]
Backup Date: [Date of backup being tested]

─────────────────────────────────────────────────
TEST DETAILS

Test Type: [File / Database / VM / DR Scenario]
Restore Source: [Backup location]
Restore Target: [Test environment]
Restore Initiated: [Time]
Restore Completed: [Time]
Restore Duration: [Calculated]

─────────────────────────────────────────────────
VALIDATION RESULTS

□ System Accessible: [Yes/No]
□ Data Integrity: [Pass/Fail]

  - [Specific validation checks performed]

□ Functionality: [Pass/Fail]

  - [Specific functionality tests]

□ Performance: [Acceptable/Degraded]

─────────────────────────────────────────────────
RTO/RPO COMPLIANCE

RTO Requirement: [X hours]
Actual Recovery Time: [Y hours]
RTO Met: [Yes/No]

RPO Requirement: [X hours]
Data Age: [Y hours old]
RPO Met: [Yes/No]

─────────────────────────────────────────────────
ISSUES ENCOUNTERED

[Description of any issues, errors, warnings]

─────────────────────────────────────────────────
REMEDIATION ACTIONS

Issue #1: [Description]
Action: [Remediation plan]
Owner: [Name]
Due Date: [Date]

─────────────────────────────────────────────────
CONCLUSION

Test Result: [SUCCESS / PARTIAL SUCCESS / FAILURE]
Recovery Capability: [PROVEN / PROVEN WITH CAVEATS / NOT PROVEN]

Next Test Scheduled: [Date]

─────────────────────────────────────────────────
APPROVALS

Tested By: [Signature] [Date]
Reviewed By: [BC/DR Coordinator] [Date]
Approved By: [IT Manager] [Date]
```

## Common Restore Test Failures & Solutions

**Issue 1: Restore Takes Longer Than RTO**

```
Symptom: Payment DB restore took 6 hours, RTO requirement is 1 hour

Root Cause: Network bandwidth limitation (offsite restore slow)

Solution:

  - Option A: Increase network bandwidth (cost)
  - Option B: Keep more recent backups on-site (faster restore from local)
  - Option C: Implement hot standby (redundancy per A.8.14)

Action: Update backup architecture to meet RTO
```

**Issue 2: Restored System Doesn't Boot**

```
Symptom: VM restored but won't power on, boot errors

Root Cause: Hardware/hypervisor incompatibility (backup from VMware 7, restore to VMware 8)

Solution:

  - Update Veeam to latest version (better compatibility)
  - Test restore to same hypervisor version as production
  - Document hypervisor requirements in recovery procedure

Action: Update recovery procedure, schedule Veeam upgrade
```

**Issue 3: Data Integrity Issues**

```
Symptom: Database restored but queries return incorrect data

Root Cause: Backup captured database mid-transaction (inconsistent state)

Solution:

  - For databases: Use application-consistent backup (VSS / app-aware processing)
  - Enable Veeam application-aware processing for SQL/Oracle
  - For critical databases: Use native database backup tools + Veeam

Action: Reconfigure backup job, re-test
```

**Issue 4: Missing Encryption Key**

```
Symptom: Cannot restore, "encryption key not found"

Root Cause: Encryption key not accessible (Azure Key Vault permission issue)

Solution:

  - Grant restore server Managed Identity permission to Key Vault
  - Test key retrieval as part of DR preparedness
  - Document key recovery procedure

Action: Update Key Vault RBAC, update recovery procedure
```

**Quality Check:**

- ✓ All Tier 1 systems tested quarterly
- ✓ All Tier 2 systems tested semi-annually
- ✓ Test results documented with evidence
- ✓ RTO/RPO compliance measured
- ✓ Issues remediated or risk accepted
- ✓ Recovery procedures updated based on test results

---

[Sections 4-12 follow with Testing, Monitoring, Documentation details]

# Backup Testing Procedures

[Complete section with detailed testing methodologies, scripts, validation criteria]

# Backup Monitoring & Alerting

[Complete section with monitoring setup, alert rules, dashboards]

# Recovery Procedure Documentation

[Complete section with templates and examples]

# Common Backup Issues & Solutions

## Issue: Backup Window Exceeded

**Symptom:** Backup job doesn't complete within maintenance window

**Causes:**

- Data growth (more data to backup)
- Network congestion
- Backup infrastructure under-resourced
- Backup method inefficient (full backup when incremental appropriate)

**Solutions:**
1. Switch to incremental backup (reduce data volume)
2. Increase backup window (extend maintenance window)
3. Increase network bandwidth (dedicated backup network)
4. Implement backup acceleration (WAN accelerators, deduplication)
5. Add backup proxy resources (more concurrent streams)

## Issue: Backup Repository Full

**Symptom:** Backups fail with "insufficient storage space"

**Immediate Action:**
1. Free space immediately:

   - Delete oldest backup chains (if retention policy allows)
   - Move backups to alternative storage
   - Temporarily reduce retention

2. Expand storage capacity:

   - Provision additional disk (NAS/SAN)
   - Extend cloud storage subscription

**Prevention:**

- Monitor capacity trend (Section 3.9)
- Set alerts at 70% / 85% / 95% thresholds
- Plan capacity 6-12 months ahead

## Issue: Cloud Backup Slow

**Symptom:** Cloud backup copy takes >12 hours, exceeds backup window

**Causes:**

- Insufficient internet bandwidth
- ISP throttling during business hours
- Large data change rate

**Solutions:**
1. Schedule cloud backup during off-hours (20:00-06:00)
2. Enable WAN acceleration (Veeam Cloud Connect)
3. Implement backup compression (reduce data volume)
4. Implement deduplication (Veeam uses this by default)
5. Increase internet bandwidth (upgrade ISP plan)
6. Direct cloud connection (Azure ExpressRoute, AWS Direct Connect - expensive)

## Issue: Ransomware Encrypted Backups

**Symptom:** Ransomware infected production system, backups also encrypted

**Root Cause:** Backups on writable shares (attacker encrypted backup repository)

**Prevention:**
1. **Immutable backups** (cannot be deleted/encrypted):

   - Veeam: Enable "Immutability" on backup repositories
   - Azure Blob: Enable "Immutable Blob Storage"
   - AWS S3: Enable "Object Lock"

2. **Air-gapped backups** (offline/disconnected):

   - Tape backups (physical disconnection)
   - Cloud backups (separate credentials, MFA)

3. **Backup isolation:**

   - Backup repository on separate network segment
   - No domain join (prevents domain admin compromise → backup compromise)

**Recovery:**

- Restore from immutable backup (unaffected by ransomware)
- Rebuild systems from clean backups
- Do NOT pay ransom

## Issue: SaaS Data Loss (Microsoft 365)

**Symptom:** User accidentally deleted emails/files, need to recover >30 days old

**Root Cause:** Microsoft 365 native retention only 30-93 days

**Solution:**

- Implement third-party SaaS backup:
  - Veeam Backup for Microsoft 365
  - Spanning Backup
- Configure long-term retention (1+ years)
- Regular restore testing

---

# Backup Assessment Workbook Guide (5 Sheets)

## Sheet 1: Backup_Inventory

**Purpose:** Track all systems and their backup status

**Columns:**
1. System_ID (from BIA) - Text
2. System_Name - Text
3. System_Type (Server/Database/SaaS/VM) - Dropdown
4. Tier (Tier 1/2/3/4) - Dropdown (from BIA)
5. RPO_Requirement (from BIA) - Dropdown (1h/4h/24h/7d)
6. Data_Classification (Public/Internal/Confidential/Restricted) - Dropdown
7. Backup_Status (Backed Up / Not Backed Up) - Dropdown
8. Backup_Solution (Veeam/Azure Backup/AWS Backup/None) - Dropdown
9. Backup_Frequency (Hourly/4h/Daily/Weekly/None) - Dropdown
10. Retention_Days - Number
11. Last_Successful_Backup - Date/Time
12. Offsite_Backup (Yes/No) - Dropdown
13. Last_Restore_Test - Date
14. Gap_Priority (P1/P2/P3/P4) - Formula
15. Notes - Text

**Formula (Gap_Priority):**
```excel
=IF(AND(Tier="Tier 1", Backup_Status="Not Backed Up"), "P1 - Critical",
  IF(AND(Tier="Tier 2", Backup_Status="Not Backed Up"), "P2 - High",
    IF(AND(OR(Tier="Tier 1", Tier="Tier 2"), Offsite_Backup="No"), "P2 - High",
      IF(Backup_Status="Not Backed Up", "P3 - Medium", "No Gap"))))
```

**Conditional Formatting:**

- Gap_Priority = "P1 - Critical": Red fill
- Gap_Priority = "P2 - High": Orange fill
- Backup_Status = "Not Backed Up": Red text
- Last_Restore_Test > 120 days (Tier 1): Yellow fill

**Data Validation:**

- Tier: List = Tier 1, Tier 2, Tier 3, Tier 4
- Backup_Status: List = Backed Up, Not Backed Up
- Backup_Frequency: List = Hourly, 4-hourly, Daily, Weekly, None

## Sheet 2: Backup_Schedules

**Purpose:** Track backup job schedules and compliance with RPO

**Columns:**
1. System_Name (from Sheet 1) - Dropdown
2. Tier (from Sheet 1) - Lookup
3. RPO_Requirement (from Sheet 1) - Lookup
4. Backup_Job_Name - Text
5. Backup_Type (Full/Incremental/Differential/Log) - Dropdown
6. Scheduled_Time - Time
7. Scheduled_Days (Daily/Weekdays/Weekly) - Dropdown
8. Actual_Frequency (calculated from schedule) - Formula
9. RPO_Compliance (Pass/Fail) - Formula
10. Backup_Window_Minutes - Number
11. Status (Configured/Pending) - Dropdown

**Formula (Actual_Frequency in hours):**
```excel
=IF(Scheduled_Days="Daily", 24,
  IF(Scheduled_Days="Weekdays", 24,
    IF(Scheduled_Days="Weekly", 168, 0)))

[Adjust based on backup type]
```

**Formula (RPO_Compliance):**
```excel
=IF(Actual_Frequency_Hours <= RPO_Requirement_Hours, "PASS", "FAIL")
```

**Conditional Formatting:**

- RPO_Compliance = "FAIL": Red fill
- Status = "Pending": Yellow fill

## Sheet 3: Backup_Testing

**Purpose:** Track restore test results

**Columns:**
1. Test_Date - Date
2. System_Name - Dropdown (from Sheet 1)
3. Tier - Lookup
4. Test_Type (File/Database/VM/DR Scenario) - Dropdown
5. Backup_Date (date of backup being tested) - Date
6. Restore_Duration_Minutes - Number
7. RTO_Requirement_Minutes (from BIA) - Lookup
8. RTO_Met (Pass/Fail) - Formula
9. Data_Integrity (Pass/Fail) - Dropdown
10. Functionality (Pass/Fail) - Dropdown
11. Overall_Result (Success/Partial/Failure) - Formula
12. Issues_Encountered - Text
13. Remediation_Required (Yes/No) - Dropdown
14. Tester_Name - Text
15. Next_Test_Due - Date (calculated)

**Formula (RTO_Met):**
```excel
=IF(Restore_Duration_Minutes <= RTO_Requirement_Minutes, "PASS", "FAIL")
```

**Formula (Overall_Result):**
```excel
=IF(AND(RTO_Met="PASS", Data_Integrity="Pass", Functionality="Pass"), "Success",
  IF(OR(Data_Integrity="Fail", Functionality="Fail"), "Failure", "Partial Success"))
```

**Formula (Next_Test_Due):**
```excel
=IF(Tier="Tier 1", Test_Date+90,
  IF(Tier="Tier 2", Test_Date+180,
    IF(Tier="Tier 3", Test_Date+365, "")))
```

**Conditional Formatting:**

- Overall_Result = "Failure": Red fill
- Overall_Result = "Partial Success": Yellow fill
- Next_Test_Due < TODAY(): Red text (overdue)

## Sheet 4: Storage_Capacity

**Purpose:** Track backup storage capacity and growth

**Columns:**
1. Repository_Name - Text
2. Location (On-Premises/Azure/AWS) - Dropdown
3. Total_Capacity_TB - Number
4. Used_Capacity_TB - Number
5. Free_Capacity_TB - Formula
6. Utilization_Percent - Formula
7. Monthly_Growth_TB - Number (manual entry or calculated from trend)
8. Months_Until_Full - Formula
9. Status (OK/Warning/Critical) - Formula
10. Action_Required - Text
11. Last_Updated - Date

**Formula (Free_Capacity_TB):**
```excel
=Total_Capacity_TB - Used_Capacity_TB
```

**Formula (Utilization_Percent):**
```excel
=(Used_Capacity_TB / Total_Capacity_TB) * 100
```

**Formula (Months_Until_Full):**
```excel
=IF(Monthly_Growth_TB>0, Free_Capacity_TB / Monthly_Growth_TB, "N/A")
```

**Formula (Status):**
```excel
=IF(Utilization_Percent>=95, "CRITICAL",
  IF(Utilization_Percent>=85, "WARNING",
    IF(Utilization_Percent>=70, "MONITOR", "OK")))
```

**Conditional Formatting:**

- Status = "CRITICAL": Red fill
- Status = "WARNING": Orange fill
- Status = "MONITOR": Yellow fill
- Months_Until_Full < 3: Red text

## Sheet 5: Dashboard

**Purpose:** Executive summary of backup status

**Metrics (calculated from other sheets):**

1. **Backup Coverage:**

   - Total Systems: COUNT(Sheet1)
   - Systems Backed Up: COUNTIF(Sheet1, Backup_Status="Backed Up")
   - Coverage %: (Backed Up / Total) × 100

2. **Gap Summary:**

   - P1 Critical Gaps: COUNTIF(Sheet1, Gap_Priority="P1 - Critical")
   - P2 High Gaps: COUNTIF(Sheet1, Gap_Priority="P2 - High")
   - P3 Medium Gaps: COUNTIF(Sheet1, Gap_Priority="P3 - Medium")

3. **Testing Compliance:**

   - Tier 1 Tests Overdue: COUNT(Sheet3, Tier="Tier 1", Next_Test_Due<TODAY())
   - Tier 2 Tests Overdue: COUNT(Sheet3, Tier="Tier 2", Next_Test_Due<TODAY())
   - Last Test Failure: Most recent "Failure" from Sheet 3

4. **Storage Status:**

   - Total Storage Capacity: SUM(Sheet4, Total_Capacity_TB)
   - Used Storage: SUM(Sheet4, Used_Capacity_TB)
   - Overall Utilization %: Used / Total
   - Critical Repositories: COUNTIF(Sheet4, Status="CRITICAL")

5. **Compliance Summary:**

   - RPO Compliance Rate: COUNTIF(Sheet2, RPO_Compliance="PASS") / COUNT(Sheet2)
   - RTO Compliance Rate: COUNTIF(Sheet3, RTO_Met="PASS") / COUNT(Sheet3)

**Visualizations (Excel Charts):**

- Pie chart: Backup Coverage (Backed Up vs. Not Backed Up)
- Bar chart: Gap Priority Distribution (P1, P2, P3)
- Line chart: Storage Utilization Trend (over time)
- Gauge chart: Overall Backup Health Score (0-100%)

**Health Score Calculation:**
```
Backup Health Score = 
  (Backup Coverage % × 0.30) +
  ((100 - Gap_Priority_Weighted) × 0.25) +
  (Testing Compliance % × 0.25) +
  ((100 - Storage_Critical_Percent) × 0.20)

Where:
  Gap_Priority_Weighted = (P1×3 + P2×2 + P3×1) / Total_Systems
  Testing Compliance % = Tests_Passed / Total_Tests
  Storage_Critical_Percent = Critical_Repos / Total_Repos
```

---

# Evidence Collection

**Evidence Required for Audit:**

1. **Backup Configuration Evidence:**

   - Backup job configurations (export from Veeam/Azure)
   - Backup schedules (screenshots)
   - Retention policies (documented)
   - Encryption settings (screenshots/config export)

2. **Backup Success Evidence:**

   - Backup job history (last 90 days minimum)
   - Success/failure statistics
   - Storage capacity reports
   - Monitoring dashboards (screenshots)

3. **Testing Evidence:**

   - Restore test reports (Sheet 3 from workbook)
   - Test validation results
   - Screenshots of successful restores
   - Signed approval of test results

4. **Compliance Evidence:**

   - BIA Assessment → Backup Implementation mapping
   - RPO/RTO compliance report
   - Gap remediation tracking
   - Management approval of backup architecture

**Evidence Storage:**

- Location: SharePoint ISMS Evidence Library
- Folder: A.8.13-Backup-Implementation
- Retention: 3 years minimum
- Access: CISO, BC/DR Coordinator, Auditors

---

# Quality Checklist

**Before Marking IMP-S2 Complete:**

**Planning & Architecture:**

- [ ] BIA requirements reviewed (RPO/RTO per system)
- [ ] Backup architecture designed and documented
- [ ] Backup solution selected and licensed
- [ ] Storage capacity calculated and provisioned
- [ ] Network bandwidth validated for backup windows

**Implementation:**

- [ ] All Tier 1 systems backed up (100% coverage)
- [ ] All Tier 2 systems backed up (100% coverage)
- [ ] Backup schedules configured per RPO requirements
- [ ] Retention policies configured per tier requirements
- [ ] Offsite/cloud backup configured for Tier 1 & 2
- [ ] Backup encryption configured for Confidential/Restricted data

**Monitoring:**

- [ ] Backup monitoring configured (Veeam ONE / Azure Monitor / other)
- [ ] Alerts configured for backup failures
- [ ] Escalation procedures documented
- [ ] Dashboards accessible to management
- [ ] Storage capacity monitoring in place

**Testing:**

- [ ] Restore testing schedule defined
- [ ] Tier 1 systems tested (quarterly schedule established)
- [ ] Tier 2 systems tested (semi-annual schedule established)
- [ ] Recovery procedures documented for all Tier 1 & 2 systems
- [ ] Test results documented in workbook

**Documentation:**

- [ ] Backup architecture diagram created
- [ ] Recovery procedures documented
- [ ] Backup Assessment Workbook completed
- [ ] Evidence collected and stored
- [ ] Integration with IMP-S1 (BIA) validated

**Compliance:**

- [ ] RPO requirements met (verified in workbook)
- [ ] RTO capability estimated (will be proven in testing)
- [ ] Data residency requirements met (nDSG, GDPR)
- [ ] Encryption requirements met (Restricted/Confidential data)
- [ ] Management approval obtained

---

# Integration with BC/DR Components

## To IMP-S1 (BIA and RPO/RTO)

**Inputs from IMP-S1:**

- System inventory
- RPO requirements → Backup frequency
- RTO requirements → Restore time target
- System criticality tier → Retention, testing frequency
- Data classification → Encryption requirements

**Feedback to IMP-S1:**

- Actual backup frequency achieved
- Estimated restore time (from testing)
- Gaps identified (RPO not met)

## To IMP-S3 (Redundancy Implementation)

**Backup Complements Redundancy:**

- Redundancy provides availability (RTO)
- Backup provides data recovery (RPO)
- Both are required for complete BC/DR

**Example:**
```
E-commerce Platform:
  IMP-S2 (Backup): 4-hourly backup → RPO 4h
  IMP-S3 (Redundancy): Hot standby → RTO 15min
  Result: Fast recovery (RTO 15min) with minimal data loss (RPO 4h)
```

**Even Redundant Systems Need Backup:**

- Redundancy protects against hardware failure
- Backup protects against data corruption, ransomware, accidental deletion
- Example: Hot standby database (IMP-S3) still backed up daily (IMP-S2)

## To IMP-S4 (Recovery Testing)

**Backup Testing is Subset of Recovery Testing:**

- IMP-S2: Backup restore testing (prove data recoverable)
- IMP-S4: Full recovery testing (prove complete system recoverable)

**Integration:**

- Backup restore is Step 1 of recovery testing
- Recovery testing validates end-to-end (backup → restore → application start → validation)

## To IMP-S5 (BC/DR Assessment)

**Backup Metrics Feed BC/DR Assessment:**

- Backup coverage % (from IMP-S2 Sheet 5)
- RPO compliance % (from IMP-S2 Sheet 2)
- Testing compliance (from IMP-S2 Sheet 3)
- Storage capacity status (from IMP-S2 Sheet 4)

**IMP-S5 Dashboard Includes:**

- Backup health score
- Gap summary (P1/P2/P3)
- Testing overdue count
- Storage at-risk repositories

---

# Regulatory Compliance Mapping

## ISO 27001:2022 A.8.13 - Information Backup

**Control Statement:** "Backup copies of information, software and systems shall be maintained and regularly tested in accordance with the agreed topic-specific policy."

**Evidence from IMP-S2:**

- Backup inventory (Sheet 1) - proves backup copies maintained
- Backup schedules (Sheet 2) - proves backup frequency per policy
- Testing results (Sheet 3) - proves regular testing
- Recovery procedures (Section 3.10) - proves backup capability documented

**SoA Justification:**
```
Control A.8.13: APPLICABLE

Justification: [Organization] maintains backup copies of all Tier 1, Tier 2, and Tier 3 systems. Backup frequency is aligned with RPO requirements from Business Impact Analysis. Tier 1 systems backed up hourly/4-hourly with 30-day retention and offsite replication to Azure Blob Storage. Quarterly restore testing validates recovery capability.

Implementation Status: IMPLEMENTED

Evidence:

- Backup inventory (85 systems, 100% Tier 1/2 coverage)
- Backup Assessment Workbook (current version dated [Date])
- Restore test results (Q4 2025 testing completed)
- Recovery procedures (documented for all Tier 1 systems)

```

## Swiss nDSG Art. 8 - Data Security

**Requirement:** "Appropriate technical and organizational measures"

**Backup as Security Measure:**

- Backup protects against data loss (availability)
- Encryption protects confidentiality
- Testing ensures effectiveness

**Evidence:** IMP-S2 workbook, testing results, encryption configuration

## EU GDPR Art. 32(1)(c) - Security of Processing

**Requirement:** "Ability to restore availability and access to personal data in a timely manner in the event of physical or technical incident"

**Evidence from IMP-S2:**

- Systems processing personal data identified (BIA data classification)
- Backup configured for all such systems
- Restore testing proves "ability to restore"
- RTO/RPO targets define "timely manner"

## DORA Art. 12 - Backup Policies

**Requirement (if applicable):** "Financial entities shall have backup policies and procedures...ensuring restoration of ICT systems"

**Evidence from IMP-S2:**

- Backup policy (ISMS-POL-A.5.30-8.13-14)
- Backup procedures (this implementation guide)
- Restoration procedures (Section 3.10)
- Testing results (proves restoration capability)

## PCI DSS v4.0.1 Requirement 3.4 - Backup Protection

**Requirement (if processing payment cards):** "Data at rest shall be rendered unreadable"

**Evidence from IMP-S2:**

- Payment database identified (Tier 1, Restricted data)
- Backup encryption configured (AES-256)
- Key management documented (Azure Key Vault)
- Encryption validated during restore testing

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
