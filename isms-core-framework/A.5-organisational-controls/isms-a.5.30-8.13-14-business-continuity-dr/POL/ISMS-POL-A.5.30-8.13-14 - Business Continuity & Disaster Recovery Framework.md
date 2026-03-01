<!-- ISMS-CORE:POLICY:ISMS-POL-A.5.30-8.13-14:framework:POL:a.5.30-8.13-14 -->
**ISMS-POL-A.5.30-8.13-14 – Business Continuity & Disaster Recovery Framework**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Business Continuity & Disaster Recovery Framework |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.5.30-8.13-14 |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | Chief Executive Officer (CEO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO | Initial policy for ISO 27001:2022 first certification |

**Review Cycle**: Annual  
**Next Review Date**: [Effective Date + 12 months]  

**Approval Chain**:

- Primary: Chief Information Security Officer (CISO)
- Secondary: Chief Information Officer (CIO)
- Technical: IT Operations Manager / BC/DR Coordinator
- Compliance: Legal/Compliance Officer
- Final Authority: Executive Management (GL)

**Related Documents**: 

- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-IMP-A.5.30-8.13-14-S1-UG/TG (BIA and RPO:RTO Process)
- ISMS-IMP-A.5.30-8.13-14-S2-UG/TG (Backup Implementation)
- ISMS-IMP-A.5.30-8.13-14-S3-UG/TG (Redundancy Implementation)
- ISMS-IMP-A.5.30-8.13-14-S4-UG/TG (Recovery Testing Process)
- ISO/IEC 27001:2022 Controls A.8.13, A.8.14, A.5.30
- ISMS-POL-A.5.19-23 (Supplier/Cloud Services - supplier BC/DR requirements)
- ISMS-POL-A.5.24 (Incident Management)
- ISMS-POL-A.8.6 (Capacity Management)

---

## Executive Summary

This policy establishes [Organisation]'s requirements for Business Continuity and Disaster Recovery (BC/DR) controls to ensure organisational resilience through systematic backup, redundancy, and ICT continuity capabilities in accordance with ISO/IEC 27001:2022 Controls A.8.13, A.8.14, and A.5.30.

**Scope**: This policy applies to all information assets, ICT systems, and business processes regardless of deployment model (on-premises, cloud, hybrid) or technology platform.

**Purpose**: Define organisational requirements for BC/DR control implementation and governance. This policy establishes WHAT recovery capabilities are required and WHO is accountable. Implementation procedures (HOW) are documented separately in ISMS-IMP-A.5.30-8.13-14 (UG/TG variants). Technical standards and configurations are intentionally defined outside this policy to preserve technological agility.

**Combined Control Approach**: These three controls are implemented as a unified framework because they operate as an integrated BC/DR ecosystem: backup provides data recovery capability (A.8.13), redundancy provides system availability capability (A.8.14), and ICT BC readiness provides overall preparedness and governance (A.5.30). Attempting separate implementation would create disconnected strategies where backup policies ignore redundancy architecture and business continuity plans don't reflect actual technical capabilities. Despite unified implementation, each control maintains distinct requirements for Statement of Applicability (SoA) purposes.

**Critical Principle - "Untested Recovery = No Recovery"**: This framework mandates regular testing of all recovery capabilities. Backup success without restore testing, redundancy without failover testing, and BC plans without scenario testing provide false confidence. Evidence-based verification through systematic testing is non-negotiable.

**Regulatory Alignment**: This policy addresses mandatory compliance requirements per ISMS-POL-00 (Regulatory Applicability Framework), including Swiss nDSG, EU GDPR, ISO/IEC 27001:2022, and conditional requirements for DORA (immutability, offsite backup, geographic redundancy), NIS2 (3-2-1 rule compliance, 24-hour incident notification), and sector-specific regulations where [Organisation]'s business activities trigger applicability.

---

# Control Alignment & Scope

## ISO/IEC 27001:2022 Controls A.8.13, A.8.14, A.5.30

**ISO/IEC 27001:2022 Annex A.8.13 - Information Backup**

> *Backup copies of information, software and systems shall be maintained and regularly tested in accordance with the agreed topic-specific policy.*

**Control Objective**: Ensure that information, software, and systems can be recovered in the event of loss, damage, corruption, or unavailability.

**ISO/IEC 27002:2022 Guidance Summary**:

- Backup copies shall be created according to defined and documented backup policy
- Backups shall include all essential information, software, system images, and configurations
- Backups shall be tested regularly to ensure they can be restored successfully
- Backups shall be protected to the same level as original data
- Multiple generations of backups shall be retained based on business requirements
- Backups shall be stored in secure, separate location (offsite or offline)

**ISO/IEC 27001:2022 Annex A.8.14 - Redundancy of Information Processing Facilities**

> *Information processing facilities shall be implemented with sufficient redundancy to meet availability requirements.*

**Control Objective**: Ensure availability of information processing facilities in accordance with organisational requirements.

**ISO/IEC 27002:2022 Guidance Summary**:

- Redundancy shall be implemented for critical information processing facilities
- Level of redundancy determined by availability requirements
- Redundancy can include hardware, software, network, power, and cooling
- Geographic redundancy should be considered to protect against site-wide disasters
- Failover mechanisms shall be implemented and tested
- Single Points of Failure (SPOF) shall be identified and mitigated

**ISO/IEC 27001:2022 Annex A.5.30 - ICT Readiness for Business Continuity**

> *ICT readiness shall be planned, implemented, maintained and tested based on business continuity objectives and ICT continuity requirements.*

**Control Objective**: Ensure ICT systems are ready to support business continuity in the event of disruptions.

**ISO/IEC 27002:2022 Guidance Summary**:

- ICT continuity plans shall be developed based on Business Impact Analysis (BIA)
- Plans shall define Recovery Point Objectives (RPO) and Recovery Time Objectives (RTO)
- ICT continuity requirements shall be aligned with business continuity objectives
- Plans shall be tested regularly through exercises and simulations
- Dependencies between ICT systems shall be documented
- Backup and redundancy capabilities shall align with recovery requirements

**Statement of Applicability Independence**: Despite unified implementation and documentation, Controls A.8.13, A.8.14, and A.5.30 are assessed independently in the Statement of Applicability. Each control maintains distinct requirements, evidence collection, and compliance scoring for audit purposes.

**This Policy Addresses**:

- Information backup requirements (A.8.13)
- Redundancy and failover requirements (A.8.14)
- ICT business continuity readiness requirements (A.5.30)
- Recovery testing and validation framework
- Organisational roles and responsibilities for BC/DR governance
- Exception and incident management frameworks
- Integration with [Organisation]'s risk assessment and treatment processes

## What This Policy Does

This policy:

- **Defines** backup, redundancy, and ICT continuity requirements aligned with organisational risk assessment
- **Establishes** governance framework for BC/DR decision-making
- **Specifies** accountability for BC/DR capability implementation
- **References** applicable regulatory requirements per ISMS-POL-00
- **Integrates** three related controls into unified BC/DR framework for implementation efficiency
- **Requires** systematic testing of recovery capabilities as proof of readiness

## What This Policy Does NOT Do

This policy does NOT:

- **Specify technical implementation details** (see ISMS-IMP-A.5.30-8.13-14 Implementation Guides)
- **Define backup technologies or solutions** (see ISMS-IMP-A.5.30-8.13-14-S2 Backup Implementation)
- **Provide redundancy architecture designs** (see ISMS-IMP-A.5.30-8.13-14-S3 Redundancy Implementation)
- **Document recovery procedures** (see ISMS-IMP-A.5.30-8.13-14-S4 Recovery Testing Process)
- **Select backup or DR vendors** (technology selection based on [Organisation]'s risk assessment)
- **Define specific RPO/RTO values** (business-driven, documented in BIA per ISMS-IMP-A.5.30-8.13-14-S1)

**Rationale**: Separating policy requirements from implementation guidance enables:

- Policy stability despite evolving BC/DR technologies (cloud DR, immutable backups, continuous replication)
- Technical agility for technology updates without policy revision
- Clear distinction between governance (policy) and execution (implementation)
- Technology-agnostic approach applicable to any infrastructure (on-premises, cloud, hybrid)

## Scope

**This policy applies to**:

**Information Assets** (A.8.13):

- Business-critical data (customer, financial, intellectual property, operational)
- System configurations and infrastructure-as-code
- Application software and dependencies
- Security configurations and access controls
- All data classifications (Restricted, Confidential, Internal, Public)

**Information Processing Facilities** (A.8.14):

- On-premises servers (physical and virtual)
- Cloud infrastructure (IaaS, PaaS, SaaS)
- Hybrid environments (on-premises + cloud integration)
- Network infrastructure (routers, switches, firewalls, load balancers)
- Storage systems (SAN, NAS, object storage, databases)
- Critical end-user systems (where business-critical)

**Business Processes** (A.5.30):

- All ICT-dependent business processes identified through Business Impact Analysis
- Critical business functions and supporting processes
- Third-party services and dependencies

**ICT Systems and Services** (A.5.30):

- All ICT systems supporting business operations
- Critical business applications
- Infrastructure services (directory, email, collaboration)
- Security systems (SIEM, IAM, endpoint protection)
- Network services (DNS, DHCP, VPN)
- Cloud services and SaaS platforms

**Infrastructure Deployment Models**:

- On-premises infrastructure (data centers, offices)
- Cloud infrastructure (IaaS: AWS EC2, Azure VMs, GCP Compute)
- Cloud platforms (PaaS: AWS RDS, Azure SQL, GCP Cloud Functions)
- Cloud applications (SaaS: Office 365, Salesforce, ServiceNow)
- Hybrid architectures (on-premises + cloud integration)
- Multi-cloud environments (multiple cloud providers)

**Recovery Direction Scenarios**:

- On-premises to on-premises (traditional DR)
- On-premises to cloud (cloud as DR target)
- Cloud to on-premises (cloud repatriation, extended outage scenarios)
- Cloud to alternative cloud (multi-cloud portability)
- Geographic failover (region-to-region within same provider)

**Personnel**:

- BC/DR Coordinator, backup administrators, system administrators
- Cloud administrators, application owners, database administrators
- Business continuity team, crisis management team
- All employees (BC awareness and responsibilities)

**This policy does NOT apply to**:

- Physical records and non-digital information (covered under physical security controls)
- Business continuity for non-ICT functions (covered under organisational BCM framework)
- Information security incident response (covered under A.5.24-27, though BC/DR invoked during major incidents)

**Cloud Environment Scope**:

This policy applies to all cloud environments utilized by [Organisation], regardless of provider or service model (IaaS/PaaS/SaaS). The authoritative list of in-scope cloud environments is maintained in:

- **Backup Inventory (Workbook 1)**: All cloud workloads requiring backup protection, including IaaS instances, PaaS databases, and SaaS application data
- **Redundancy Analysis (Workbook 2)**: Cloud infrastructure implementing redundancy requirements (multi-AZ, multi-region, multi-cloud deployments)
- **Asset Inventory (ISMS-POL-A.5.9)**: Complete inventory of information assets including cloud resources, organised by criticality classification

References to specific cloud providers (AWS, Azure, GCP) throughout this policy are illustrative of cloud BC/DR concepts and architectures. The actual cloud providers, services, and deployment models in scope are determined by [Organisation]'s current infrastructure deployment as documented in the inventories listed above.

**Cloud Provider Change Management**: Addition of new cloud providers or services requires BC/DR capability implementation (backup configuration, redundancy architecture, recovery testing) before production deployment per Section 8.1 (Operational Planning and Control). Updates to cloud provider inventory do not require policy revision but SHALL be reflected in BC/DR inventories within 30 days of production deployment.

**Multi-Cloud and Hybrid Considerations**: Where [Organisation] operates multi-cloud (multiple providers) or hybrid (on-premises + cloud) architectures, BC/DR requirements apply consistently across all deployment models. Recovery scenarios SHALL include:
- Cloud-to-cloud failover (primary cloud region to secondary region or alternative provider)
- Cloud-to-on-premises recovery (for extended cloud provider outages)
- On-premises-to-cloud recovery (cloud as disaster recovery target)

Cross-platform recovery capabilities SHALL be documented in recovery procedures (ISMS-IMP-A.5.30-8.13-14-S2, S3) and validated through annual testing per Section 2.3.4.

## Regulatory Applicability

This policy implements BC/DR requirements to comply with regulations per **ISMS-POL-00 (Regulatory Applicability Framework)**:

**Tier 1: Mandatory Compliance**

| Regulation | Requirement | Applicability |
|------------|-------------|---------------|
| **Swiss nDSG (Federal Data Protection Act)** | Appropriate technical and organisational measures including availability protection (Art. 8) | All [Organisation] processing of personal data |
| **EU GDPR** | Ability to restore availability and access to personal data in timely manner (Art. 32(1)(c)) | When processing EU personal data |
| **ISO/IEC 27001:2022** | Controls A.8.13, A.8.14, A.5.30 | Certification scope |

**Tier 2: Conditional Applicability**

| Regulation | Requirement | Trigger Condition |
|------------|-------------|-------------------|
| **DORA (Digital Operational Resilience Act)** | ICT business continuity policy, backup policies, disaster recovery plans, testing (Art. 11-12) | EU financial services operations |
| **NIS2 Directive** | Business continuity and crisis management measures, backup management (Art. 21) | Essential/important entity designation |
| **FINMA** | Business continuity management for financial institutions | Swiss financial services operations |
| **PCI DSS v4.0.1** | Data backup and retention (Req. 12.10), testing of backup/recovery (Req. 12.10.7) | Processing payment card data |

**Tier 3: Informational Guidance**

Best practice frameworks referenced but not mandatory compliance requirements:

- ISO/IEC 22301 (Business Continuity Management)
- NIST SP 800-34 (Contingency Planning)
- ISO/IEC 27031 (ICT Readiness for Business Continuity)
- ITIL Service Continuity Management

**DORA-Specific Requirements**: For EU financial entities subject to DORA, the following additional requirements apply:

- Immutable backup copies where technically feasible (Art. 12(4))
- Offsite backup storage at sufficient geographic distance (Art. 12(4))
- Annual backup recovery testing (Art. 12(6))
- BC/DR testing integrated with threat-led penetration testing (Art. 26)

**NIS2-Specific Requirements**: For essential/important entities subject to NIS2:

- 3-2-1 backup rule implementation (3 copies, 2 media types, 1 offsite)
- Encryption of backups in transit and at rest
- 24-hour incident reporting capability for BC/DR events

**United States Federal Requirements**: References to US federal frameworks (FISMA, FIPS, FedRAMP, NIST cybersecurity requirements) apply only where [Organisation] has explicit US federal contractual obligations, as defined in ISMS-POL-00.

**Compliance Determination**: Legal/Compliance Officer determines applicability of Tier 2 regulations based on [Organisation]'s business activities and regulatory status.

---

# Requirements Framework

## Information Backup Requirements (A.8.13)

[Organisation] implements information backup capabilities to enable recovery from data loss, corruption, or system failure.

### Backup Scope Requirements

**Systems and Data Requiring Backup**:

| Category | Backup Requirement | Rationale |
|----------|-------------------|-----------|
| **Critical business data** | Mandatory backup | Data loss would severely impact operations |
| **Production systems** | Mandatory backup (data + configuration) | Required for business continuity |
| **Critical infrastructure configs** | Mandatory backup | Required for infrastructure recovery |
| **Important business data** | Mandatory backup | Data loss would moderately impact operations |
| **Development/test systems** | Risk-based backup | Backup if recreation cost exceeds backup cost |
| **Ephemeral data** | No backup required | Data deliberately temporary (caches, logs with retention) |
| **Non-critical systems** | Risk-based backup | Backup if restoration time unacceptable |

**Backup Scope Determination**: System owners, in consultation with BC/DR Coordinator, determine backup requirements based on:

- Business Impact Analysis (BIA) results
- Data criticality classification (per ISMS-POL-A.5.12)
- Regulatory retention requirements
- System recovery time objectives (RTO)
- Rebuild complexity vs. backup cost analysis

### Backup Schedule Requirements

**Backup Frequency by System Criticality**:

| System Tier | Backup Frequency | RPO Target | Rationale |
|-------------|-----------------|------------|-----------|
| **Tier 1 (Critical)** | Continuous or hourly | ≤ 1 hour | Minimal data loss acceptable |
| **Tier 2 (High)** | Every 4-6 hours | ≤ 6 hours | Limited data loss acceptable |
| **Tier 3 (Medium)** | Daily | ≤ 24 hours | Daily data loss acceptable |
| **Tier 4 (Low)** | Weekly or on-change | ≤ 7 days | Weekly data loss acceptable |

**Backup Window**: Backups SHALL complete within defined maintenance windows. If backup duration exceeds available window, incremental/differential strategies or continuous data protection SHALL be implemented.

### RPO Requirements by Criticality

**Recovery Point Objective (RPO) Framework**:

RPO defines maximum acceptable age of data that can be recovered. RPO drives backup frequency requirements.

| System Criticality | Maximum RPO | Backup Strategy | Example Technologies |
|--------------------|-------------|-----------------|---------------------|
| **Tier 1 (Critical)** | 1 hour or less | Continuous replication or hourly backups | CDP, real-time replication, hourly snapshots |
| **Tier 2 (High)** | 4-6 hours | Multiple daily backups | 4x daily backups, periodic snapshots |
| **Tier 3 (Medium)** | 24 hours | Daily backups | Nightly full or incremental |
| **Tier 4 (Low)** | 7 days | Weekly backups | Weekly full backups |

**RPO Calculation**: System owners SHALL document RPO requirements based on:

- Maximum acceptable data loss measured in time (hours/days)
- Business impact of losing X hours of transactions
- Regulatory data reconstruction requirements
- Cost of backup infrastructure vs. cost of data loss

**RPO Exceptions**: Systems unable to meet defined RPO SHALL follow exception management process (Section 3.2).

### Backup Technology Requirements

**Backup Types**:

| Backup Type | Description | Use Case | Advantages | Disadvantages |
|-------------|-------------|----------|------------|---------------|
| **Full Backup** | Complete copy of all data | Baseline, weekly/monthly | Simplest recovery | Time/storage intensive |
| **Incremental** | Changed data since last backup (any type) | Daily backups | Fast, efficient storage | Slower recovery (all increments needed) |
| **Differential** | Changed data since last full backup | Daily backups | Faster recovery than incremental | More storage than incremental |
| **Snapshot** | Point-in-time copy (storage-level) | Frequent backups, VMs | Very fast, space-efficient | Storage-dependent, not portable |
| **Continuous Data Protection (CDP)** | Real-time or near-real-time replication | Critical systems (RPO < 1 hour) | Minimal data loss | Complex, expensive |

**Backup Strategy Selection**: System owners SHALL select appropriate backup technology based on:

- RPO and RTO requirements
- System architecture (physical, virtual, cloud, database)
- Data change rate (how much data changes daily)
- Available backup window
- Storage capacity and cost constraints

**Backup Retention Requirements**:

Backups SHALL be retained according to the following minimum retention periods:

| Backup Type | Minimum Retention | Regulatory Considerations |
|-------------|------------------|--------------------------|
| **Daily backups** | 30 days | Most regulations require 30-day recovery capability |
| **Weekly backups** | 90 days | Quarterly compliance and audit needs |
| **Monthly backups** | 12 months | Annual compliance verification and historical analysis |
| **Yearly backups** | 7 years (or per regulation) | Financial records, tax compliance, legal holds |

**Extended Retention**: Additional retention requirements may apply based on:

- Regulatory requirements (GDPR, FINMA, PCI DSS v4.0.1, tax law)
- Legal hold requests
- Contractual obligations
- Business needs (historical analytics, compliance audits)

**Retention Policy Exceptions**: Shorter retention periods require CISO approval and documented risk acceptance.

### 3-2-1-1-0 Backup Rule (Industry Best Practice)

**3-2-1-1-0 Rule Definition**:

| Element | Requirement | Rationale |
|---------|------------|-----------|
| **3 copies** | Original + 2 backup copies | Protection against single-point-of-failure |
| **2 media types** | Different storage technologies | Protection against media-specific failures |
| **1 offsite copy** | Geographically separated location | Protection against site disasters |
| **1 immutable/air-gapped** | Write-once-read-many or offline | Protection against ransomware and insider threats |
| **0 errors** | Verified backup integrity | Only verified backups are reliable |

**Implementation for Critical Systems** (Tier 1):

Critical systems (Tier 1) SHALL implement 3-2-1-1-0 rule:

- **3 copies**: Production data + on-premises backup + cloud/offsite backup
- **2 media types**: Disk-based + tape/object storage, or on-premises + cloud
- **1 offsite**: Geographic separation (different datacenter, region, or cloud)
- **1 immutable**: WORM storage, object lock (S3), or air-gapped tape
- **0 errors**: Automated backup verification, periodic restore testing

**Implementation for High/Medium Systems** (Tier 2-3):

High and Medium systems SHOULD implement at minimum 3-2-1:

- **3 copies**: Production + primary backup + secondary backup
- **2 media types**: Different technologies (disk + cloud, disk + tape)
- **1 offsite**: Cloud backup or remote datacenter

**Rationale**: 3-2-1-1-0 provides defense-in-depth against multiple failure scenarios: hardware failure, ransomware, natural disasters, human error, and data corruption.

### Offsite and Immutability Requirements

**Offsite Backup Requirements**:

| System Tier | Offsite Requirement | Geographic Separation | Replication Frequency |
|-------------|-------------------|----------------------|---------------------|
| **Tier 1 (Critical)** | Mandatory | Minimum 100 km or different region | Continuous or hourly |
| **Tier 2 (High)** | Mandatory | Minimum 50 km or different availability zone | Daily |
| **Tier 3 (Medium)** | Recommended | Different physical location | Weekly |
| **Tier 4 (Low)** | Risk-based | Cloud storage acceptable | On-change |

**Geographic Separation Criteria**:

- **Different building**: Protection against building fire, flood, power outage
- **Different datacenter**: Protection against datacenter-wide disasters
- **Different city/region**: Protection against regional disasters (earthquake, hurricane)
- **Different country/jurisdiction**: Protection against geopolitical risks (for multinational operations)

**DORA Compliance**: EU financial entities subject to DORA SHALL implement offsite backup at sufficient geographic distance to protect against regional disasters (Art. 12(4)).

**Immutable Backup Requirements**:

**Critical Systems** (Tier 1):

- SHALL implement immutable backups using WORM (Write-Once-Read-Many) technology
- Immutability period SHALL align with retention policy (minimum 30 days)
- Immutable backups SHALL be separate from standard backup infrastructure
- Technologies: Object storage with object lock (AWS S3 Object Lock, Azure Immutable Blob), tape libraries with WORM media, dedicated immutable backup appliances

**Offline/Air-Gapped Backup**: For Critical systems, at least one backup copy should be:

- Physically disconnected from network (air-gapped tape, removable media)
- Stored in secure offsite location
- Rotated periodically (weekly/monthly)

**Rationale**: Immutable and air-gapped backups provide last line of defense against ransomware attacks that attempt to encrypt or delete backup repositories.

**Cloud-to-On-Premises Backup**: Cloud workloads should have backup copies:

- Exportable to portable format (avoid cloud provider lock-in)
- Restorable to on-premises infrastructure if needed
- Documented recovery process for cloud repatriation scenarios

### Backup Portability Requirements

**Vendor Lock-In Mitigation**:

To ensure recovery flexibility and avoid dependency on specific backup vendors or cloud providers, backup implementations SHALL ensure:

**Backup Format Portability**:

- Backups SHALL be exportable to industry-standard formats where feasible
- Proprietary formats SHALL include documented conversion procedures
- Cloud backups SHALL be exportable without vendor-specific tools

**Recovery Platform Independence**:

- Backups SHALL be restorable to different platforms (physical, virtual, cloud)
- Cloud backups SHALL be restorable to on-premises infrastructure
- On-premises backups SHALL be portable to cloud infrastructure (on-prem-to-cloud recovery)
- Backup solutions SHALL document export/migration procedures
- Recovery procedures SHALL address provider exit scenarios

**Rationale**: Avoid vendor lock-in, enable flexible DR strategies, support cloud repatriation scenarios, maintain recovery options during extended cloud outages.

This requirement is critical for cloud independence and is referenced in supplier agreements (ISMS-POL-A.5.19-23-S2 Section 8: Data Return and Destruction).

### Backup Testing Requirements

**Restore Testing** (all backup tiers):

| System Tier | Restore Test Frequency | Test Scope |
|-------------|----------------------|-----------|
| **Tier 1** | Quarterly minimum | Full system restore to alternate environment |
| **Tier 2** | Semi-annually minimum | Representative data sets, full system annually |
| **Tier 3** | Annually minimum | Sample restore verification |
| **Tier 4** | Upon significant change | Sample restore or risk acceptance |

**Testing Documentation Requirements**:

Each backup restore test SHALL be documented using standardized template including:

1. **Test Metadata**: Test ID, date, type (full/partial), system(s) tested, test environment, participants
2. **Pre-Test State**: Systems in scope, backup source (date/location), expected RTO/RPO
3. **Test Execution**: Step-by-step log of restore actions, timestamps, commands/procedures used
4. **Results Validation**:
   - Data integrity verification (checksums, record counts, sample data inspection)
   - System functionality validation (application startup, user access, business process test)
   - Performance validation (meets production requirements)
5. **Metrics**: Actual restore duration, data recovered (TB/GB), RTO variance (actual vs. target)
6. **Evidence Artifacts**: Screenshots of restored system, validation reports, log excerpts demonstrating success
7. **Issues Log**: Problems encountered, workarounds applied, root cause if identified
8. **Sign-Off**: BC/DR Coordinator approval, System Owner confirmation of functionality

**Testing Documentation Standards**:
- Standardized template maintained in ISMS-IMP-A.5.30-8.13-14-S4 (Recovery Testing Process)
- Testing documentation SHALL be stored in [centralized repository/SharePoint/ISMS tool]
- Minimum retention: 3 years or per regulatory requirement
- Test results referenced in Workbook 4 (BC/DR Testing Results)

**Critical Principle**: Backup success metrics (backup completed successfully) do NOT validate recovery capability. Only restore testing validates recovery capability.

**Failed Test Response**: Backup tests revealing recovery failures shall trigger:

- Immediate investigation of root cause
- Remediation of identified issues
- Retest within 30 days
- Incident reporting if affecting Critical systems

**DORA Compliance**: Financial entities subject to DORA must test backup recovery annually at minimum (Art. 12(6)).

### Backup Monitoring Requirements

Backup operations SHALL be monitored:

| Monitoring Element | Requirement | Alert Threshold |
|-------------------|-------------|-----------------|
| **Backup Success/Failure** | Real-time monitoring | Immediate alert on failure |
| **Backup Duration** | Trend analysis | Alert if duration exceeds window |
| **Backup Size** | Trend analysis | Alert on unexpected growth/shrinkage |
| **Repository Capacity** | Capacity monitoring | Alert at 75% utilization |
| **Retention Compliance** | Automated validation | Alert on retention policy violations |

**Alerting Requirements**:

| Alert Trigger | Severity | Notification To |
|---------------|----------|-----------------|
| Critical system backup failure | High | BC/DR Coordinator + System Owner |
| Multiple consecutive backup failures | High | BC/DR Coordinator + CISO |
| Backup storage capacity threshold (80%) | Medium | Backup Administrator |
| Offsite replication failure | High | BC/DR Coordinator |
| Backup integrity verification failure | High | BC/DR Coordinator + System Owner |

**Reporting**: Monthly backup status reports shall be provided to CISO including:

- Backup coverage percentage (systems backed up vs. total systems)
- Backup success rate by system criticality
- Testing completion status
- Outstanding issues and remediation timeline

Monitoring integration: Backup alerts SHALL integrate with organisational monitoring platform (ISMS-POL-A.8.16 Monitoring Activities).

### Recovery Procedures

Recovery procedures SHALL be documented for each backed-up system including:

- Step-by-step restore process
- Required access credentials and authorisation
- Recovery time estimate (RTO)
- Recovery validation steps
- Known issues and workarounds
- Contact information for escalation

Recovery procedures SHALL be tested during restore testing exercises and updated based on test results.

**Cloud Backup Considerations**:

**Cloud Service Provider Backup**:

- Understand provider's "shared responsibility model"
- Document which backups are provider's responsibility vs. customer's responsibility
- Implement customer-managed backups where provider does not guarantee RPO requirements

**SaaS Application Backup**:

- Evaluate SaaS provider's backup and retention capabilities
- Implement third-party SaaS backup solution if provider capabilities insufficient
- Test SaaS data export and import procedures

**Cloud Backup Portability**:

- Backup formats should enable restoration to alternative cloud provider or on-premises
- Document recovery procedures for cloud-to-cloud and cloud-to-on-premises scenarios
- Avoid backup solutions that create vendor lock-in

**Supplier Requirements**: Cloud backup providers shall meet requirements per ISMS-POL-A.5.19-23 (Supplier/Cloud Services) including:

- Classification as Level 1 (Critical) supplier
- Security assessment and due diligence
- Contractual commitments for availability, data protection, and incident notification
- Audit rights or third-party attestation (SOC 2 Type II, ISO 27001)

## Redundancy of Information Processing Facilities (A.8.14)

[Organisation] implements redundancy for critical information processing facilities to meet availability requirements and minimise single points of failure.

### Redundancy Requirements by System Criticality

**Redundancy Level Determination**:

| System Criticality | Maximum RTO | Minimum Redundancy Requirement |
|--------------------|-------------|-------------------------------|
| **Critical** | ≤ 4 hours | Active-active or active-passive with automated failover |
| **High** | ≤ 24 hours | Warm standby or documented cold standby with tested recovery |
| **Medium** | ≤ 72 hours | Cold standby or documented rebuild procedures |
| **Low** | > 72 hours | Backup-based recovery acceptable |

**Redundancy Architecture Options**:

| Architecture | Description | Typical RTO | Use Case |
|-------------|-------------|-------------|----------|
| **Active-Active** | Multiple systems serving traffic simultaneously | Minutes | Critical systems requiring continuous availability |
| **Active-Passive** | Standby system ready for immediate failover | Minutes to hours | Critical systems with acceptable brief outage |
| **Warm Standby** | Standby environment partially provisioned | Hours | High-priority systems with moderate RTO |
| **Cold Standby** | Infrastructure available but not provisioned | Days | Important systems with longer acceptable RTO |

### Single Point of Failure (SPOF) Analysis

**SPOF Identification Process**:

System owners SHALL conduct SPOF analysis for Critical and High systems to identify components whose failure would cause complete system failure:

**Infrastructure SPOF Examples**:

- Single server (no clustering or failover)
- Single network path (no redundant connectivity)
- Single power supply or UPS
- Single storage controller
- Single availability zone or datacenter
- Single DNS server
- Single authentication server

**SPOF Analysis Documentation**:

- Component inventory (servers, network, storage, power, cooling)
- Dependency mapping (what depends on what)
- SPOF identification (components with no redundancy)
- Impact assessment (what fails if component fails)
- Mitigation plan (how to eliminate SPOF or accept risk)

**SPOF Remediation Priority**:

| SPOF Risk Level | Remediation Requirement | Timeline |
|-----------------|------------------------|----------|
| **Critical system SPOF** | Mandatory remediation | 90 days or risk acceptance |
| **High system SPOF** | Recommended remediation | 180 days or risk acceptance |
| **Medium system SPOF** | Risk-based decision | Risk assessment required |

**SPOF Exceptions**: Accepted SPOFs SHALL be documented in exception register with risk acceptance from CISO.

### Failover and Switchover Requirements

**Failover Mechanisms**:

| System Tier | Failover Type | Recovery Action | RTO Impact |
|-------------|--------------|-----------------|-----------|
| **Tier 1 (Critical)** | Automated failover | System automatically switches to standby | Minutes |
| **Tier 2 (High)** | Manual failover with runbook | Operator executes documented procedure | Hours |
| **Tier 3 (Medium)** | Rebuild or restore | Provision new system or restore from backup | Days |

**Failover Testing Requirements**:

Critical and High systems with redundancy SHALL test failover mechanisms:

| System Tier | Failover Test Frequency | Test Scope |
|-------------|------------------------|-----------|
| **Tier 1 (Critical)** | Quarterly | Full failover in production or production-like environment |
| **Tier 2 (High)** | Semi-annually | Documented failover test or tabletop exercise |
| **Tier 3 (Medium)** | Annually | Tabletop exercise or documented procedure validation |

**Failover Test Documentation**:

- Test date and scope
- Systems tested
- Failover trigger mechanism (manual or automated)
- Actual failover time vs. RTO target
- Issues identified and remediation
- Evidence of successful failover

**Failed Failover Response**: Failover tests revealing inability to meet RTO shall trigger immediate remediation and risk assessment.

### Geographic Redundancy

**Critical Systems**: Critical systems should implement redundancy at sufficient distance to protect against:

- Site-wide disasters (fire, flood, power outage)
- Regional disasters (earthquake, hurricane)
- Extended cloud provider outages (multi-region deployment)

**Geographic Redundancy Options**:

| Redundancy Level | Geographic Separation | Protection Against | Example |
|------------------|----------------------|-------------------|---------|
| **Multi-Server** | Same datacenter/rack | Server hardware failure | Clustered servers |
| **Multi-Rack** | Same datacenter | Power/cooling failure in rack | Servers in different racks |
| **Multi-Zone** | Same region, different availability zones | Datacenter-level outage | AWS Multi-AZ, Azure Availability Zones |
| **Multi-Region** | Different geographic regions | Regional disaster | AWS us-east-1 + us-west-2 |
| **Multi-Cloud** | Different cloud providers | Cloud provider outage | AWS + Azure redundancy |

**DORA/NIS2 Compliance**: Financial entities and essential entities should implement geographic redundancy for critical systems to meet operational resilience requirements.

**Cost-Benefit Analysis**: Geographic redundancy decisions shall balance:

- Cost of redundant infrastructure
- Complexity of multi-region/multi-cloud management
- Risk of regional outages
- Regulatory requirements (DORA, NIS2, FINMA)
- Business impact of extended outages

### Network Redundancy

**Network Redundancy Requirements**:

Critical systems SHALL implement network redundancy at multiple layers:

| Network Layer | Redundancy Requirement | Implementation Example |
|--------------|----------------------|----------------------|
| **Internet Connectivity** | Dual ISPs or providers | Multiple internet connections |
| **WAN Connectivity** | Redundant circuits | MPLS + Internet, dual circuits |
| **Internal Network** | Redundant switches/routers | Switch stacking, HSRP/VRRP |
| **Load Balancing** | Multiple load balancers | Active-active LB cluster |
| **Firewalls** | HA firewall pairs | Active-passive firewall cluster |

**Network Failover Testing**: Network failover mechanisms SHALL be tested quarterly for Critical systems.

### Cloud-to-On-Premises Redundancy

**Hybrid Redundancy Strategies**:

For organisations with hybrid cloud deployments, redundancy strategies should consider:

**Cloud-First with On-Premises Failback**:

- Primary: Cloud infrastructure (AWS, Azure, GCP)
- Secondary: On-premises infrastructure for extended cloud outages
- Use case: Cloud repatriation during multi-day cloud provider incidents

**On-Premises-First with Cloud Failover**:

- Primary: On-premises infrastructure
- Secondary: Cloud infrastructure for DR
- Use case: Traditional on-premises with cloud as disaster recovery target

**Active-Active Hybrid**:

- Traffic split between cloud and on-premises
- Both environments active simultaneously
- Use case: Geographic distribution, performance optimization

**Implementation Considerations**:

- Data synchronization between cloud and on-premises
- Network connectivity requirements (VPN, Direct Connect, ExpressRoute)
- License portability (bring-your-own-license to cloud)
- Recovery procedures for bidirectional failover

### Power and Environmental Redundancy

**Critical Infrastructure Redundancy**:

Datacenters and critical infrastructure facilities SHALL implement redundancy for:

**Power Systems**:

- Dual power feeds from utility (where available)
- Uninterruptible Power Supply (UPS) systems
- Backup generator with fuel supply
- Automatic transfer switches

**Cooling Systems**:

- Redundant HVAC units
- Environmental monitoring (temperature, humidity)
- Alerts for environmental threshold violations

**Physical Security**:

- Redundant access control systems
- Backup physical security monitoring

**Cloud Environments**: Cloud providers typically implement N+1 or 2N power/cooling redundancy. Verify provider's redundancy claims through:

- SOC 2 Type II reports
- Site visits (where permitted)
- Third-party datacenter certifications (Tier III/IV)

## ICT Readiness for Business Continuity (A.5.30)

[Organisation] implements ICT continuity planning to ensure readiness for business disruptions.

### Business Impact Analysis (BIA)

**BIA Process**:

Business Impact Analysis SHALL be conducted to:

- Identify critical business processes
- Determine ICT dependencies for each business process
- Quantify impact of ICT disruptions (financial, operational, reputational, regulatory)
- Establish Maximum Tolerable Downtime (MTD), Recovery Time Objective (RTO), and Recovery Point Objective (RPO)

**BIA Frequency**: BIA SHALL be conducted:

- Initially during ISMS implementation
- Annually at minimum
- Upon significant business changes (new services, acquisitions, major system changes)
- After major incidents (lessons learned integration)

**BIA Output**:

- Business process inventory with criticality ratings
- ICT system inventory with criticality classifications (Tier 1-4)
- MTD, RTO, and RPO for each critical system
- Dependency mapping (system interdependencies)
- Impact quantification (financial loss per hour of downtime)

**BIA Documentation**: BIA results SHALL be documented in:

- **System Criticality Register**: Master inventory of all systems with Tier 1-4 classification, documented MTD/RTO/RPO, business justification, and owner sign-off. Maintained by BC/DR Coordinator in [ISMS tool/SharePoint/database]. Updated within 30 days of any system classification change.
- **Business Process Dependency Maps**: Visual or tabular documentation of ICT dependencies for each critical business process, showing upstream/downstream system relationships.
- **BIA Assessment Reports**: Formal BIA report with impact quantification, stakeholder interviews, analysis methodology, and approval signatures from business process owners and CISO.

BIA documentation SHALL be:
- Version-controlled with change tracking
- Reviewed and approved annually
- Referenced in Workbook 3 (RPO/RTO Compliance Matrix)
- Maintained for audit inspection (minimum 3-year retention)

**BIA Responsibility**: BC/DR Coordinator leads BIA process with input from business process owners and system owners.

### ICT Continuity Strategy

Based on BIA results, [Organisation] SHALL define ICT continuity strategy including:

**Recovery Strategies by System Tier**:

| System Tier | Recovery Strategy | Infrastructure Approach |
|-------------|------------------|----------------------|
| **Tier 1 (Critical)** | Active-active or hot standby | Redundant infrastructure, automated failover |
| **Tier 2 (High)** | Warm standby or rapid rebuild | Pre-provisioned resources, documented procedures |
| **Tier 3 (Medium)** | Cold standby or restore from backup | Available infrastructure, backup restore |
| **Tier 4 (Low)** | Rebuild or deferred recovery | Standard rebuild procedures |

**Recovery Site Strategy**:

[Organisation]'s recovery site strategy:

- **Hot Site**: Fully operational site for Tier 1 systems (cloud multi-region, alternate datacenter)
- **Warm Site**: Partially provisioned site for Tier 2 systems (cloud reserved capacity, DR datacenter)
- **Cold Site**: Infrastructure-ready site for Tier 3 systems (contract with datacenter provider)

**Alternative Strategies**:

- Cloud as recovery site (on-premises primary, cloud DR)
- Multi-cloud redundancy (AWS + Azure, regional diversity)
- Reciprocal agreements (mutual DR agreements with partners - rarely used)

### ICT Recovery Plans

**ICT Continuity Plan Documentation**:

ICT continuity plans SHALL document:

**Plan Structure**:
1. **Activation Criteria**: When to activate plan (disaster declaration process)
2. **Roles and Responsibilities**: Recovery team structure, escalation procedures
3. **Emergency Contacts**: Contact lists for recovery team, vendors, stakeholders
4. **Recovery Procedures**: Step-by-step system recovery procedures
5. **Communication Procedures**: Internal and external communication templates
6. **Recovery Priorities**: System recovery sequence based on dependencies
7. **Validation Procedures**: How to verify systems are operational

**System-Specific Recovery Procedures**:

For each Critical and High system:

- Prerequisites (infrastructure, network, dependencies)
- Step-by-step recovery instructions
- Recovery time estimates
- Validation steps to confirm successful recovery
- Rollback procedures if recovery fails
- Known issues and workarounds

**Plan Maintenance**: ICT continuity plans SHALL be:

- Reviewed annually
- Updated after testing exercises
- Updated after major incidents
- Updated when systems or infrastructure changes significantly
- Version controlled with change tracking

### BC/DR Testing Program

**Testing Types**:

| Test Type | Description | Frequency | Scope |
|-----------|-------------|-----------|-------|
| **Tabletop Exercise** | Discussion-based walkthrough | Annually | All critical processes |
| **Component Test** | Test individual system recovery | Quarterly | Critical systems |
| **Full DR Test** | Complete failover to DR site | Annually | Critical processes end-to-end |
| **Surprise Test** | Unannounced test (optional) | As needed | Selected systems |

**Testing Schedule by Criticality**:

| Criticality | Annual Testing Requirement |
|-------------|---------------------------|
| **Critical** | Full DR test + 2 component tests |
| **High** | Full DR test or 2 component tests |
| **Medium** | Component test or tabletop exercise |
| **Low** | Tabletop exercise |

**DORA Compliance**: Financial entities subject to DORA shall:

- Test BC arrangements at least annually (Art. 11(9))
- Test ICT backup and restoration at least annually (Art. 12(6))
- Integrate BC/DR testing with threat-led penetration testing (Art. 26)

**Testing Documentation**: Each BC/DR test shall document:

- Test date, scope, objectives, and participants
- Test scenario and conditions
- Test results (success/failure/partial)
- Actual vs. target RTO/RPO
- Issues identified during test
- Lessons learned and action items
- Plan updates required based on test results
- Sign-off by BC/DR Coordinator and CISO

**Failed Test Response**: Tests revealing inability to meet RTO/RPO shall trigger:

- Immediate investigation and root cause analysis
- Gap remediation plan with timeline
- Risk assessment of current capability
- Interim compensating controls if needed
- Executive notification for Critical systems
- Retest after remediation

### RPO/RTO Compliance Monitoring

**RPO/RTO Alignment**: Technical capabilities (backup frequency, redundancy architecture) shall align with business-defined RPO/RTO requirements.

**Compliance Assessment**:

- Backup frequency vs. RPO: Does backup schedule support RPO?
- Redundancy capability vs. RTO: Can failover meet RTO?
- Testing results vs. targets: Do actual recovery times meet RTO?

**Gap Management**: Identified gaps between requirements and capabilities shall:

- Be documented with risk assessment
- Have remediation plan with timeline
- Require risk acceptance if not immediately remediable
- Be escalated to CISO and executive management for Critical systems

**Continuous Monitoring**: Automated monitoring shall track:

- Backup job completion within RPO window
- Redundancy health checks
- Failover capability verification
- Testing schedule compliance

**RPO/RTO Reporting**: Quarterly reports to CISO shall include:

- Systems meeting vs. not meeting RPO/RTO targets
- Gap analysis with criticality-prioritized remediation
- Testing compliance status
- Trend analysis (improving vs. degrading)

### Supplier and Third-Party Coordination

**Supplier BC/DR Requirements**: Suppliers providing Critical or High services shall meet requirements per ISMS-POL-A.5.19-23 (Supplier/Cloud Services) including:

- Documented BC/DR plans
- Defined SLA including RTO/RPO commitments
- Annual BC/DR testing with results sharing
- Incident notification procedures
- Supplier BC/DR plan reviews during due diligence

**Cloud Provider Coordination**: For cloud-hosted systems:

- Understand provider's BC/DR capabilities and responsibilities
- Validate provider SLA aligns with organisational RTO/RPO
- Implement customer-managed DR where provider capability insufficient
- Document provider incident notification procedures
- Test recovery procedures including cloud provider engagement

**Managed Service Provider Coordination**: For outsourced ICT operations:

- Ensure MSP recovery plans integrate with organisational BC plans
- Define MSP roles and responsibilities during disasters
- Include MSP in BC/DR testing exercises
- Verify MSP staffing and resource availability during disasters

### Crisis Communication

**Communication Plan Requirements**: BC/DR plans shall include communication procedures for:

**Internal Communication**:

- Activation notification (who, when, how)
- Status updates during recovery
- All-clear notification when recovery complete
- Post-incident review scheduling

**External Communication**:

- Customer notification (proactive for known outages)
- Supplier/partner coordination (if needed for recovery)
- Regulatory notification (if required by regulation)
- Public/media communication (if applicable)

**Communication Channels**:

- Primary: [Organisation]'s communication platform (email, Teams/Slack)
- Backup: SMS, phone calls (if primary unavailable)
- Emergency: Pre-established external communication service

## Cross-Control Requirements

### Integrated Testing Approach

**Cross-Control Testing**:

BC/DR testing SHALL integrate all three controls:

**Integrated Test Scenario**:
1. **Backup Recovery** (A.8.13): Restore system from backup
2. **Redundancy Failover** (A.8.14): Failover to redundant infrastructure
3. **Business Continuity** (A.5.30): Execute full business process recovery

**Annual Integrated Test**: At least one annual BC/DR test SHALL exercise:

- Backup restoration (data recovery from offsite backup)
- Redundancy activation (failover to DR site/cloud region)
- Business process validation (confirm business operations can continue)
- Communication procedures (internal and external notifications)

**Test Success Criteria**:

- All systems restored within RTO targets
- Data restored meets RPO targets (acceptable data loss)
- Business processes operational on recovered systems
- Communication procedures executed correctly

### Evidence Collection Requirements

**Audit Evidence Documentation**:

For each BC/DR activity, maintain evidence:

**Backup Evidence**:

- Backup job completion logs
- Backup storage inventory (what is backed up, where)
- Backup test results (restore tests with screenshots)
- Backup monitoring alerts and response

**Redundancy Evidence**:

- Redundancy architecture diagrams
- SPOF analysis results
- Failover test results
- Redundancy health monitoring data

**ICT Continuity Evidence**:

- BIA results and approval
- ICT continuity plans (current versions)
- Testing exercise results
- Plan update history

**Evidence Repository tracked in Summary Dashboards**: BC/DR Coordinator SHALL maintain centralised evidence repository including:

- Test results database
- Plan versions and change history
- Exception register
- Incident post-mortems involving BC/DR activation

### Gap Management and Remediation

**Gap Identification**:

Gaps in BC/DR capability SHALL be identified through:

- Testing failures (systems not meeting RTO/RPO)
- BIA updates (new critical systems identified)
- Audit findings (internal or external audits)
- Incident lessons learned (actual disaster response)
- Technology changes (new systems without backup/redundancy)

**Gap Prioritization**:

| Gap Type | Priority | Remediation Timeline |
|----------|----------|---------------------|
| **Critical system not meeting RTO/RPO** | P1 - Critical | 30 days or risk acceptance |
| **High system gap** | P2 - High | 90 days |
| **Medium system gap** | P3 - Medium | 180 days |
| **Testing non-compliance** | P2 - High | Next test cycle |

**Gap Remediation Process**:
1. Gap identified and documented
2. Root cause analysis
3. Remediation plan developed (technical solution, timeline, resources)
4. CISO approval of plan
5. Implementation and validation
6. Retest to confirm gap closure
7. Documentation update

**Gap Register**: BC/DR Coordinator SHALL maintain gap register including:

- Gap description
- System/process affected
- Risk assessment
- Remediation plan and timeline
- Remediation status
- Target closure date

---

# Governance & Compliance

## Roles & Responsibilities

| Role | BC/DR Responsibilities |
|------|----------------------|
| **Chief Executive Officer (CEO)** | Ultimate accountability for business continuity; Approve BC/DR strategy and budget; Declare disasters requiring plan activation |
| **Chief Information Security Officer (CISO)** | BC/DR policy owner; Approve BC/DR requirements and risk acceptance; Ensure adequate resources for BC/DR implementation; Report BC/DR status to executive management |
| **Chief Information Officer (CIO)** | Operational accountability for ICT continuity; Allocate resources for backup/redundancy implementation; Approve technology investments for BC/DR; Ensure ICT recovery plans align with business requirements |
| **BC/DR Coordinator** | Day-to-day BC/DR program management; Coordinate BIA process; Maintain recovery plans; Schedule and facilitate BC/DR testing; Track compliance with backup/redundancy requirements; Report BC/DR metrics and gaps |
| **Backup Administrator** | Implement and manage backup solutions; Configure backup schedules and retention; Monitor backup jobs and troubleshoot failures; Coordinate backup testing; Maintain backup infrastructure |
| **System Administrators / Cloud Administrators** | Implement redundancy for assigned systems; Configure failover mechanisms; Participate in BC/DR testing; Maintain system recovery documentation; Respond to system failures and recovery events |
| **System Owners / Application Owners** | Define RTO/RPO requirements for their systems; Provide input to BIA process; Approve system recovery priorities; Participate in BC/DR testing; Validate recovered systems functionality |
| **Business Process Owners** | Define business continuity requirements; Identify critical processes and dependencies; Approve RTO/RPO for business processes; Participate in BC/DR exercises; Validate business process recovery |
| **Security Team** | Monitor backup and DR infrastructure security; Verify encryption implementation; Review security of DR sites and cloud DR; Participate in BC/DR testing; Incident response coordination |
| **Legal/Compliance Officer** | Determine regulatory BC/DR requirements; Ensure compliance with DORA, NIS2, etc.; Review supplier BC/DR commitments; Advise on data residency implications |

**Responsibility Matrix**:

| Activity | Lead | Support | Approve | Inform |
|----------|------|---------|---------|--------|
| BIA Process | BC/DR Coordinator | Business Owners, System Owners | CISO | CIO |
| Backup Policy | CISO | BC/DR Coordinator | Executive Management | All Staff |
| Backup Implementation | Backup Administrator | System Administrators | CIO | BC/DR Coordinator |
| Redundancy Design | System Owners | Infrastructure Team | CIO | BC/DR Coordinator |
| Recovery Plan Development | BC/DR Coordinator | System Owners | CISO | Business Owners |
| BC/DR Testing | BC/DR Coordinator | All Recovery Team | CISO | Executive Management |
| Gap Remediation | System Owners | Infrastructure Team | CISO (risk acceptance) | BC/DR Coordinator |

## Exception Management

**Exception Request Process**:

Exceptions to BC/DR requirements (e.g., system excluded from backup, redundancy not implemented) shall follow formal approval process:

**Step 1: Exception Request Submission**

- Requestor: System owner or business owner
- Required information: System/scope, requirement being excepted, business justification, risk assessment, proposed compensating controls, exception duration

**Step 2: Risk Assessment**

- Performed by: BC/DR Coordinator + Security Team
- Assessment: Impact if disaster occurs, likelihood of disaster, regulatory implications, risk rating

**Step 3: Approval Decision**

| Exception Risk Level | Approval Authority |
|---------------------|-------------------|
| Low risk (non-critical system, short duration) | BC/DR Coordinator |
| Medium risk | CISO |
| High risk (critical system, regulatory impact) | CISO + CIO |
| Critical risk (severe business impact) | Executive Management (CEO/CIO/CISO) |

**Step 4: Exception Tracking**

- All exceptions documented in exception register
- Periodic review (quarterly for temporary exceptions)
- Re-approval required upon expiration
- Remediation tracking if exception temporary

**Permanent Exceptions**: Systems permanently excluded from backup/redundancy requirements shall:

- Have documented risk acceptance
- Be reviewed annually
- Require CISO approval for Critical/High systems
- Document why standard BC/DR approach is not feasible

## Monitoring & Reporting

**Continuous Monitoring**:

- Backup job success/failure rates
- Backup storage capacity utilization
- Redundancy health checks (clustering, replication status)
- RPO/RTO compliance metrics
- Testing schedule adherence

**Reporting Requirements**:

**Monthly Reports** (BC/DR Coordinator → CISO):

- Backup success rate by criticality
- Failed backups requiring investigation
- Redundancy availability status
- Upcoming testing schedule
- Open issues and remediation status

**Quarterly Reports** (BC/DR Coordinator → CISO + CIO):

- BC/DR program KPIs
- RPO/RTO compliance summary
- Testing results and lessons learned
- Gap analysis with prioritization
- Exception register review
- Trend analysis

**Annual Reports** (CISO → Executive Management):

- BC/DR maturity assessment
- Major incidents and recovery effectiveness
- Compliance with regulatory requirements
- Investment needs and strategic recommendations

**Key Performance Indicators (KPIs)**:

| KPI | Target | Measurement |
|-----|--------|-------------|
| Backup coverage (% of critical systems backed up) | 100% | Monthly |
| Backup success rate | ≥ 99% | Monthly |
| Backup testing compliance | ≥ 95% | Quarterly |
| RPO compliance (% systems meeting RPO) | 100% critical, ≥ 95% high | Quarterly |
| RTO compliance (% systems meeting RTO in tests) | 100% critical, ≥ 95% high | Quarterly |
| DR test success rate | ≥ 90% | Annually |
| SPOF remediation (% critical SPOFs mitigated) | ≥ 90% | Quarterly |

## Incident Management

**BC/DR Incident Types**:

| Incident Type | Description | Response |
|---------------|-------------|----------|
| **Backup failure** | Critical system backup fails multiple times | Investigate immediately, restore from previous backup if needed |
| **Storage capacity** | Backup storage exceeds threshold | Expand capacity or adjust retention policy |
| **Redundancy failure** | Failover capability unavailable | Immediate remediation, risk assessment |
| **Testing failure** | Recovery test does not meet RTO/RPO | Root cause analysis, remediation plan |
| **Disaster event** | Actual disaster requiring recovery | Activate BC/DR plan, execute recovery procedures |

**Incident Notification**:

- Backup failures (Critical systems): Notify BC/DR Coordinator + System Owner immediately
- Redundancy failures: Notify BC/DR Coordinator + CISO immediately
- Disaster declaration: Activate crisis communication plan

**Integration with Incident Management**: BC/DR incidents integrate with organisational incident management process (A.5.24-27) for:

- Incident logging and tracking
- Root cause analysis
- Lessons learned
- Continuous improvement

## Policy Governance

**Policy Review**:

- **Frequency**: Annual minimum
- **Triggers**: Regulatory changes, major incidents, significant business changes, audit findings, technology changes
- **Reviewers**: CISO, BC/DR Coordinator, CIO, Legal/Compliance
- **Approval**: CISO (technical), Executive Management (strategic)

**Implementation Standards Review**:

- **Frequency**: Based on technology evolution (at least semi-annual)
- **Authority**: BC/DR Coordinator proposes updates, CISO approves
- **Note**: Implementation standard updates (ISMS-IMP-A.5.30-8.13-14) do not require policy revision

**Policy Updates**:

- **Minor** (clarifications, references): CISO approval, communication within 30 days
- **Major** (scope changes, new requirements): Full approval chain, implementation timeline per change management
- **Emergency** (critical regulatory change, major incident lessons learned): CISO approval, immediate communication and implementation

**Communication**: Policy published in ISMS document repository. Changes communicated organisation-wide. Training provided for significant changes affecting responsibilities or procedures.

---

# Implementation & References

## Integration with ISMS

This policy integrates with [Organisation]'s Information Security Management System:

**Risk Assessment** (ISO 27001 Clause 6.1):

- BC/DR controls selected based on [Organisation]'s risk assessment
- BIA results feed risk assessment process
- Risk treatment plans document BC/DR control implementation
- Residual risks from BC/DR exceptions documented

**Asset Inventory** (A.5.9):

- Systems requiring backup/redundancy identified through asset inventory
- Asset criticality classification drives BC/DR requirements
- Changes to asset inventory trigger BC/DR review

**Configuration Management** (A.8.9):

- System configurations backed up per backup policy
- Configuration baselines documented for recovery
- Infrastructure-as-Code enables rapid rebuild
- Integration: Configuration backups managed per A.8.9 requirements

**Logging** (A.8.15):

- Backup operations logged (success, failure, duration)
- Failover events logged
- Recovery operations logged for audit trail
- Integration: BC/DR logs centralized per A.8.15 requirements

**Monitoring Activities** (A.8.16):

- Backup monitoring integrated with organisational monitoring platform
- Redundant system health monitored continuously
- RTO/RPO compliance monitored
- Integration: BC/DR monitoring per A.8.16 requirements

## Implementation Resources

**Implementation Guidance** (ISMS-IMP-A.5.30-8.13-14 Suite):

| Document | Purpose | Scope |
|----------|---------|-------|
| **ISMS-IMP-A.5.30-8.13-14-S1** | BIA and RPO/RTO Process | Business Impact Analysis methodology, system criticality classification, RPO/RTO determination |
| **ISMS-IMP-A.5.30-8.13-14-S2** | Backup Implementation | Backup solution selection, architecture design, scheduling, retention, monitoring, recovery procedures |
| **ISMS-IMP-A.5.30-8.13-14-S3** | Redundancy Implementation | SPOF identification, redundancy architecture design, failover mechanisms, geographic redundancy |
| **ISMS-IMP-A.5.30-8.13-14-S4** | Recovery Testing Process | Backup restore testing, failover testing, BC/DR scenario testing, evidence collection |

**Assessment Tools** (Excel workbooks):

- **Workbook 1**: Backup Inventory & Coverage Assessment (systems backed up, RPO compliance, 3-2-1-1-0 compliance)
- **Workbook 2**: Redundancy Analysis (redundancy architecture, SPOF analysis, RTO compliance)
- **Workbook 3**: RPO/RTO Compliance Matrix (business requirements vs. technical capabilities, gap analysis)
- **Workbook 4**: BC/DR Testing Results (test inventory, results tracking, remediation status)

**Supporting Materials**:

- Recovery procedure templates
- BIA questionnaire templates
- Testing checklists and scenarios
- Exception request forms
- Gap remediation tracking templates

## Regulatory Mapping

This policy addresses BC/DR requirements from applicable regulations:

| Requirement Category | Swiss nDSG | EU GDPR | ISO 27001 | DORA* | NIS2* | PCI DSS v4.0.1* | FINMA* |
|---------------------|-----------|---------|-----------|-------|-------|---------|--------|
| Backup requirements | Art. 8 | Art. 32 | A.8.13 | Art. 12 | Art. 21 | Req. 12.10 | Risk-Based |
| Offsite backup | Art. 8 | Art. 32 | A.8.13 | Art. 12 (Required) | Art. 21 (Required) | Req. 12.10 | Risk-Based |
| Immutability | – | – | A.8.13 | Art. 12 (Required) | Art. 21 (Recommended) | – | Risk-Based |
| Redundancy | Art. 8 | Art. 32 | A.8.14 | Art. 12 | Art. 21 | – | Risk-Based |
| ICT continuity planning | Art. 8 | Art. 32 | A.5.30 | Art. 12, 14 | Art. 21 | Req. 12.10 | Risk-Based |
| Testing requirements | Art. 8 | Art. 32 | A.8.13, A.5.30 | Art. 12 | Art. 21 | Req. 12.10 | Risk-Based |
| Incident notification | Art. 24 | Art. 33 | A.5.24 | Art. 19 (24h) | Art. 23 (24h) | Req. 12.10 | Incident Mgmt |
| Supplier BC/DR | Art. 9 | Art. 28 | A.5.19-23 | Art. 28 | Art. 22 | Req. 12.8 | Outsourcing |

*Conditional applicability per ISMS-POL-00

**DORA-Specific Mapping** (Art. 11-12):

- ICT business continuity policy → Section 2.3
- Backup policies and procedures → Section 2.1
- Disaster recovery plans → Section 2.3.3
- Immutable backups → Section 2.1.6
- Offsite backup storage → Section 2.1.6
- Annual backup testing → Section 2.1.8
- Annual BC plan testing → Section 2.3.4

**NIS2-Specific Mapping** (Art. 21):

- Business continuity and crisis management → Section 2.3
- Backup management and restoration → Section 2.1
- 3-2-1 backup rule → Section 2.1.5
- 24-hour incident reporting → ISMS-POL-A.5.24 (Incident Management)

## Training & Awareness

**Security Awareness** (All Personnel):

- Annual training module on BC/DR awareness
- User responsibilities during disasters
- Data backup best practices (for personal responsibility areas)
- Business continuity mindset and culture

**BC/DR Team Training** (BC/DR Coordinator, Backup Administrators, System Administrators):

- BC/DR policy and procedures
- Backup technology configuration and management
- Recovery procedure execution
- Testing methodology and documentation
- Incident response during disasters

**Recovery Team Training**:

- Annual review of recovery plans
- Participation in BC/DR exercises
- Role-specific recovery procedures
- Crisis communication procedures

**Executive Training**:

- BC/DR strategy and governance
- Disaster declaration criteria and procedures
- Crisis leadership responsibilities
- Regulatory compliance requirements

---

# Definitions

**Backup**: Copy of data, software, or system configuration created for recovery purposes in the event of loss, corruption, or unavailability. Backups are typically stored separately from production systems.

**Redundancy**: Implementation of duplicate or alternative information processing facilities to ensure availability in the event of failure. Redundancy can be hardware-based (multiple servers), software-based (clustering), or geographic (multiple data centers).

**Business Continuity (BC)**: Organisational capability to continue business operations during and after disruptive events. BC encompasses both ICT systems and non-ICT business processes.

**Disaster Recovery (DR)**: Process of restoring ICT systems and data after disruption. DR is a subset of business continuity focused specifically on ICT recovery.

**Recovery Point Objective (RPO)**: Maximum acceptable amount of data loss measured in time. RPO defines how frequently backups must occur. Example: RPO of 4 hours means backups must occur at least every 4 hours, and up to 4 hours of data loss is acceptable.

**Recovery Time Objective (RTO)**: Maximum acceptable time to restore a system after disruption. RTO defines how quickly recovery must occur. Example: RTO of 24 hours means system must be restored within 24 hours of failure.

**Maximum Tolerable Downtime (MTD)**: Absolute maximum time a business process can be unavailable before causing unacceptable consequences. MTD is typically longer than RTO as it includes time for workarounds and manual processes.

**Business Impact Analysis (BIA)**: Systematic process to identify and evaluate potential effects of disruption to critical business operations. BIA determines MTD, RTO, and RPO for business processes and supporting ICT systems.

**Single Point of Failure (SPOF)**: Component whose failure would cause entire system or process to fail. SPOF analysis identifies components lacking redundancy.

**Failover**: Process of automatically or manually switching to redundant or standby system when primary system fails.

**Hot Site**: Fully operational backup facility with equipment, connectivity, and data replication enabling immediate failover.

**Warm Site**: Backup facility with equipment and connectivity but requiring data restoration before becoming operational.

**Cold Site**: Backup facility with basic infrastructure (power, cooling, space) but requiring equipment installation and data restoration before becoming operational.

**Active-Active**: Redundancy architecture where multiple systems actively serve traffic simultaneously. Failure of one system is handled by remaining active systems.

**Active-Passive**: Redundancy architecture where primary system actively serves traffic while standby system remains idle but ready for immediate activation upon primary failure.

**Immutable Backup**: Backup that cannot be modified or deleted after creation (WORM - Write Once Read Many). Provides protection against ransomware and accidental deletion.

**Air-Gapped Backup**: Backup physically disconnected from network, providing isolation from cyberattacks.

**Offsite Backup**: Backup stored at geographic location separate from primary data location, providing protection against site-specific disasters.

**3-2-1 Backup Rule**: Industry best practice recommending 3 copies of data (original + 2 backups), on 2 different media types, with 1 copy offsite.

**3-2-1-1-0 Backup Rule**: Enhanced backup rule adding 1 immutable/air-gapped copy and 0 errors in backup verification testing.

**Incremental Backup**: Backup of only data that changed since last backup (full or incremental), reducing backup time and storage.

**Differential Backup**: Backup of data that changed since last full backup, providing faster recovery than incremental but using more storage.

**Full Backup**: Complete backup of all data, providing simplest recovery but requiring most time and storage.

**Cloud Repatriation**: Process of moving workloads and data from cloud back to on-premises infrastructure, relevant for extended cloud outages or strategic changes.

**Multi-Cloud**: Architecture utilizing multiple cloud providers for redundancy, avoiding vendor lock-in, or service optimization.

**Hybrid Cloud**: Architecture combining on-premises infrastructure with cloud services, supporting flexible recovery scenarios.

---

# Approval Record

| Role | Name | Date |
|------|------|------|
| **Chief Information Security Officer (CISO)** | [Name] | [Date] |
| **Chief Information Officer (CIO)** | [Name] | [Date] |
| **BC/DR Coordinator** | [Name] | [Date] |
| **Legal/Compliance Officer** | [Name] | [Date] |
| **Executive Management (GL)** | [Name] | [Date] |

---

**END OF POLICY DOCUMENT**

---

*This policy establishes BC/DR requirements. Implementation procedures are documented in ISMS-IMP-A.5.30-8.13-14-S1 through S4 (UG/TG). Each assessment workbook includes its own Summary Dashboard for compliance verification.*

<!-- QA_VERIFIED: 2026-03-01 -->