# ISMS-POL-A.5.19-23-S5 — Cloud Services Security
## Control A.5.23: Information Security for Use of Cloud Services

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | Cloud Services Security |
| **Document Type** | Policy Section |
| **Document ID** | ISMS-POL-A.5.19-23-S5 |
| **Document Creator** | Information Security Officer (ISO) |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | ISO | Initial section for ISO 27001:2022 Control A.5.23 |

**Review Cycle**: Annual  
**Next Review Date**: [Effective Date + 12 months]  

**Approval Chain**:
- Primary: Chief Information Security Officer (CISO)
- Secondary: Information Security Officer (ISO)
- Technical: Cloud Architecture Team Lead
- Compliance: Legal/Compliance Officer
- Final Authority: Executive Management (GL)

**Related Documents**: 
- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-POL-A.5.19-23 (Parent Policy - Supplier & Cloud Services Security)
- ISMS-IMP-A.5.23-1 (Cloud Service Inventory & Classification)
- ISMS-IMP-A.5.23-2 (Vendor Due Diligence & Contracts)
- ISMS-IMP-A.5.23-3 (Secure Configuration & Deployment)
- ISMS-IMP-A.5.23-4 (Ongoing Governance & Risk Management)
- ISMS-IMP-A.5.23-5 (Compliance Monitoring Dashboard)
- ISMS-REF-A.5.23 (Cloud Service Provider Registry)
- ISO/IEC 27001:2022 Control A.5.23
- ISO/IEC 27017:2015 (Cloud security controls)
- ISO/IEC 27018:2019 (Cloud privacy)
---

## 1. Purpose

This section defines requirements for the secure acquisition, use, management, and exit from cloud services. It establishes the cloud service lifecycle framework and cloud-specific security controls.

**Control Objective (ISO 27002:2022):**
> "Processes for acquisition, use, management and exit from cloud services shall be established in accordance with the organization's information security requirements."

**Critical Principle - "The Cloud is Someone Else's Computer"**: Cloud services operate on infrastructure you don't control, in jurisdictions you don't govern, with access by personnel you haven't vetted. The shared responsibility model means security failures can occur in either party's domain - but the compliance and reputational consequences fall on [Organization]. This policy requires systematic cloud lifecycle management from selection through exit, with continuous verification that provider security claims match operational reality.

**ISO/IEC 27002:2022 Guidance Summary**:
- Cloud service acquisition shall follow risk-based selection process with comprehensive security evaluation
- Cloud service agreements shall address information security requirements and clearly define shared responsibility model
- Shared responsibility model shall be explicitly understood, documented, and managed (provider vs customer controls)
- Cloud service configuration shall be secured according to vendor security baselines and organizational requirements
- Cloud data residency and sovereignty requirements shall be enforced per regulatory obligations (GDPR, nDSG)
- Cloud service monitoring and logging shall be implemented with appropriate retention and review
- Cloud service exit strategy shall be planned and tested including data export, portability, and transition procedures
- Cloud-specific risks (multi-tenancy, data commingling, jurisdiction, provider access) shall be assessed and mitigated
- Cloud provider certifications and compliance (SOC 2, ISO 27017, CSA STAR) shall be verified annually

---

## 2. Scope

### 2.1 Cloud Service Models

| Model | Description | Organization Responsibility |
|-------|-------------|----------------------------|
| **IaaS** | Infrastructure as a Service | OS, middleware, applications, data |
| **PaaS** | Platform as a Service | Applications, data |
| **SaaS** | Software as a Service | Data, user configuration |
| **XDR/SECaaS** | Security as a Service | Configuration, policy, response |
| **FaaS** | Function as a Service | Code, data |
| **DaaS** | Desktop as a Service | User data, endpoint policy |

### 2.2 Cloud Deployment Models

| Model | Description | Consideration |
|-------|-------------|---------------|
| **Public** | Shared infrastructure, multi-tenant | Data isolation, compliance |
| **Private** | Dedicated infrastructure | Cost, management overhead |
| **Hybrid** | Mix of public and private | Integration complexity |
| **Multi-cloud** | Multiple cloud providers | Portability, consistency |
| **Community** | Shared by specific community | Governance, shared risk |

### 2.3 Applicability

This section applies to all cloud services that:

- Process, store, or transmit organizational data
- Provide infrastructure for organizational systems
- Are accessed by organizational users
- Integrate with organizational systems

---

## 3. Cloud Service Lifecycle

### 3.1 Lifecycle Overview

```
┌─────────────────────────────────────────────────────────────┐
│                  CLOUD SERVICE LIFECYCLE                        │
├─────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐      │
│  │ SELECT   │ → │IMPLEMENT │ → │ OPERATE  │ → │   EXIT   │      │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘      │
│       │              │              │              │            │
│       ▼              ▼              ▼              ▼            │
│  • Requirements  • Configure    • Monitor     • Plan exit       │
│  • Evaluate      • Integrate    • Review      • Export data     │
│  • Risk assess   • Migrate      • Patch       • Transition      │
│  • Contract      • Test         • Incident    • Terminate       │
│  • Approve       • Go-live      • Change      • Verify delete   │
│                                                                 │
└─────────────────────────────────────────────────────────────┘
```

### 3.2 Phase Requirements Summary

| Phase | Key Activities | Deliverables |
|-------|----------------|--------------|
| **Selection** | Requirements, evaluation, risk assessment | Approved service + contract |
| **Implementation** | Configuration, integration, migration | Production-ready service |
| **Operation** | Monitoring, review, incident response | Ongoing compliance |
| **Exit** | Planning, data export, termination | Clean exit + data destruction |

---

## 4. Selection & Evaluation

### 4.1 Pre-Selection Requirements

Before evaluating cloud services:

| Requirement | Description |
|-------------|-------------|
| Business need | Documented business justification |
| Data classification | Classification of data to be processed |
| Compliance requirements | Regulatory and contractual obligations |
| Integration requirements | Systems and data flows involved |
| Security requirements | Minimum security controls needed |

### 4.2 Cloud Service Evaluation Criteria

| Category | Evaluation Areas |
|----------|------------------|
| **Security** | Certifications, controls, incident history |
| **Compliance** | Regulatory alignment, data residency, audit support |
| **Reliability** | SLA, uptime history, redundancy |
| **Portability** | Data export, API standards, lock-in risk |
| **Support** | Availability, responsiveness, expertise |
| **Viability** | Financial stability, market position, roadmap |

### 4.3 Security Evaluation Checklist

| Requirement | Verification Method |
|-------------|---------------------|
| ISO 27001 or SOC 2 certification | Certificate/report review |
| Encryption at rest and in transit | Technical documentation |
| Multi-factor authentication | Configuration capability |
| Access logging and monitoring | Feature verification |
| Data residency options | Contract and technical review |
| Incident notification process | Contract and documentation |
| Backup and recovery capabilities | Technical documentation |
| Penetration testing program | Report availability |
| Vulnerability management | Process documentation |
| Sub-processor transparency | Sub-processor list review |

### 4.4 Risk Assessment

Prior to approval, conduct risk assessment covering:

| Risk Area | Assessment Focus |
|-----------|------------------|
| Data exposure | What data, what classification, what controls |
| Availability | Business impact of service failure |
| Compliance | Regulatory implications |
| Vendor lock-in | Switching costs and feasibility |
| Concentration | Dependency on single provider |
| Jurisdiction | Legal and regulatory framework |

### 4.5 Approval Requirements

| Data Classification | Approval Required |
|---------------------|-------------------|
| Restricted | CISO + Business Owner + Legal |
| Confidential | ISO + Business Owner |
| Internal | Business Owner + Security review |
| Public | Business Owner |

---

## 5. Implementation & Configuration

### 5.1 Secure Configuration Principles

| Principle | Implementation |
|-----------|----------------|
| **Least privilege** | Minimum permissions for users and services |
| **Defense in depth** | Multiple layers of controls |
| **Secure defaults** | Start secure, deviate only with approval |
| **Separation** | Isolate environments, data, access |
| **Encryption** | Protect data at rest and in transit |
| **Logging** | Comprehensive audit trails |

### 5.2 Configuration Requirements

| Control Area | Requirements |
|--------------|--------------|
| **Identity & Access** | SSO integration, MFA enforced, RBAC implemented |
| **Data Protection** | Encryption enabled, classification applied, DLP configured |
| **Network Security** | Access restrictions, secure connectivity, segmentation |
| **Logging & Monitoring** | Audit logs enabled, SIEM integration, alerting configured |
| **Backup & Recovery** | Automated backups, tested recovery, appropriate retention |
| **Endpoint Integration** | Secure access from managed devices |

### 5.3 Implementation Checklist

| Phase | Activities |
|-------|------------|
| **Pre-deployment** | Security configuration review, integration testing |
| **Deployment** | Staged rollout, validation testing |
| **Post-deployment** | Security verification, monitoring confirmation |
| **Documentation** | Configuration records, runbooks, access inventory |

### 5.4 Data Migration Security

| Requirement | Description |
|-------------|-------------|
| Migration plan | Documented approach with security controls |
| Data inventory | What data, classification, volume |
| Secure transfer | Encrypted transmission |
| Validation | Data integrity verification |
| Legacy cleanup | Secure deletion from source (if applicable) |

---

## 6. Operational Management

### 6.1 Ongoing Security Activities

| Activity | Frequency | Responsibility |
|----------|-----------|----------------|
| Access review | Quarterly | Business Owner + IT |
| Configuration review | Semi-annual | Security + IT |
| Security assessment | Annual | Security |
| Compliance verification | Annual | Compliance |
| Backup testing | Semi-annual | IT Operations |
| Incident response drill | Annual | Security |

### 6.2 Change Management

Cloud service changes shall follow organizational change management:

| Change Type | Process |
|-------------|---------|
| Provider-initiated | Review notification, assess impact, approve/escalate |
| Organization-initiated | Change request, security review, approval, implementation |
| Emergency | Expedited approval, post-implementation review |

### 6.3 Incident Management

| Requirement | Description |
|-------------|-------------|
| Detection | Monitor for security events via logs and alerts |
| Notification | Receive and process provider notifications |
| Response | Execute incident response procedures |
| Coordination | Collaborate with provider on investigation |
| Recovery | Restore services and data as needed |
| Lessons learned | Update controls based on incidents |

### 6.4 Forensic Readiness

| Requirement | Description |
|-------------|-------------|
| Log retention | Sufficient retention for investigation |
| Log access | Ability to retrieve logs for analysis |
| Evidence preservation | Provider cooperation for legal holds |
| Chain of custody | Documentation for legal proceedings |
| Investigation support | Provider assistance with forensics |

---

## 7. Shared Responsibility Model

### 7.1 Understanding Shared Responsibility

```
┌─────────────────────────────────────────────────────────────┐
│              SHARED RESPONSIBILITY BY SERVICE MODEL             │
├─────────────────────────────────────────────────────────────┤
│                                                                 │
│ Responsibility    │  IaaS    │  PaaS    │  SaaS    │            │
│ ──────────────────┼──────────┼──────────┼──────────┤            │
│ Data              │   YOU    │   YOU    │   YOU    │            │
│ Applications      │   YOU    │   YOU    │ PROVIDER │            │
│ Runtime           │   YOU    │ PROVIDER │ PROVIDER │            │
│ Middleware        │   YOU    │ PROVIDER │ PROVIDER │            │
│ Operating System  │   YOU    │ PROVIDER │ PROVIDER │            │
│ Virtualization    │ PROVIDER │ PROVIDER │ PROVIDER │            │
│ Infrastructure    │ PROVIDER │ PROVIDER │ PROVIDER │            │
│ Physical          │ PROVIDER │ PROVIDER │ PROVIDER │            │
│                                                                 │
│ YOU = Organization responsibility                               │
│ PROVIDER = Cloud service provider responsibility                │
└─────────────────────────────────────────────────────────────┘
```

### 7.2 Responsibility Documentation

For each cloud service, document:

| Element | Documentation |
|---------|---------------|
| Provider responsibilities | What provider commits to |
| Organization responsibilities | What we must do |
| Shared responsibilities | Joint activities |
| Gaps | Areas not covered by either party |
| Compensating controls | How gaps are addressed |

---

## 8. Exit Strategy

### 8.1 Exit Planning Requirements

**All cloud services shall have documented exit strategy including:**

| Element | Description |
|---------|-------------|
| Trigger events | Conditions that would initiate exit |
| Data export | How to extract data in usable format |
| Alternative services | Identified alternatives or in-house options |
| Migration approach | High-level transition plan |
| Timeline estimate | Expected duration for exit |
| Resource requirements | Skills and effort needed |
| Cost estimate | Budget for transition |

### 8.1.1 Exit Strategy Options

Exit strategies SHALL evaluate three primary transition paths based on service criticality, cost, timeline, and regulatory requirements. [Organization] shall document which exit strategy is appropriate for each cloud service during initial risk assessment and review annually.

**Exit Strategy Selection Principles:**

1. **Cloud-to-Cloud Migration** - Default exit strategy for most services (90%+)
2. **Hybrid Cloud Transition** - For regulatory/cost drivers requiring partial repatriation (5-10%)
3. **On-Premises Repatriation** - Reserved for regulatory mandates or extreme circumstances (<5%)

---

#### 8.1.1.1 Cloud-to-Cloud Migration (Primary Exit Strategy)

Migration to alternative cloud provider is the **default exit strategy** for most services due to lower capital expenditure, faster timelines, maintained elasticity, and reduced operational overhead.

**Strategic Rationale:**

| Advantage | Benefit |
|-----------|---------|
| No infrastructure purchase | Zero CAPEX, operational expenditure model continues |
| Faster transition | 1-6 months typical vs. 6-18 months for on-premises |
| Maintained elasticity | Burst capacity, auto-scaling, pay-per-use preserved |
| Modern capabilities | Access to cloud-native services (containers, serverless, AI/ML) |
| Reduced operational overhead | Provider-managed infrastructure, patching, updates |
| Geographic flexibility | Multi-region deployment without facility investment |

**Assessment Requirements:**

| Criterion | Evaluation Method | Documentation |
|-----------|-------------------|---------------|
| **Alternative providers** | Identify 2+ viable alternatives (AWS, Azure, GCP, OVHcloud, Alibaba Cloud) | Provider comparison matrix |
| **Service parity** | Verify alternative offers equivalent functionality (compute, storage, database, networking) | Service feature mapping |
| **Data portability** | Confirm export format compatibility with alternative (JSON, CSV, Parquet, database dumps) | Data export test results |
| **Integration compatibility** | Assess API/integration rewrite requirements (REST APIs, SDKs, authentication) | Integration impact analysis |
| **Cost comparison** | 3-year TCO of alternative vs. current provider (compute, storage, network, licenses) | TCO spreadsheet |
| **Certification alignment** | Verify alternative meets compliance requirements (ISO 27001, SOC 2, GDPR, sector-specific) | Certification matrix |
| **Migration timeline** | Estimate transition duration including testing and validation | Project timeline (Gantt) |
| **Proof-of-concept** | Test critical workload on alternative provider (annual requirement per DORA Article 28.6) | PoC test report, screenshots |

**Migration Phases (Cloud-to-Cloud):**

| Phase | Duration | Activities | Deliverables |
|-------|----------|------------|--------------|
| **Assessment** | 2-4 weeks | Alternative provider evaluation, cost analysis, risk assessment | Provider selection, migration plan |
| **Preparation** | 4-8 weeks | Account setup, network connectivity, IAM configuration, data classification | Target environment configured |
| **Migration** | 4-12 weeks | Data migration, application deployment, integration testing | Migrated services in production |
| **Validation** | 2-4 weeks | Performance testing, security validation, user acceptance | Sign-off, decommission source |
| **Cleanup** | 1-2 weeks | Source environment decommission, data deletion verification | Deletion certificates |

**Total Timeline: 3-6 months typical for medium-complexity services**

**Cost Considerations (Cloud-to-Cloud):**

| Cost Category | Estimate Range | Notes |
|---------------|----------------|-------|
| **Professional services** | CHF 20K-100K | Consulting, migration support (if needed) |
| **Data egress fees** | CHF 5K-50K | Outbound data transfer from source provider |
| **Parallel operation** | 1-3 months cloud costs | Running both environments during migration |
| **Testing/validation** | CHF 10K-30K | Load testing, security assessment |
| **Training** | CHF 5K-20K | Staff training on new provider platform |
| **TOTAL (One-Time)** | **CHF 40K-200K** | Varies by service complexity and data volume |

**When Cloud-to-Cloud is Optimal:**

✅ **Service is cloud-native** (containers, microservices, serverless, managed databases)  
✅ **Workload has variable demand** (traffic spikes, seasonal patterns, unpredictable growth)  
✅ **Organization lacks on-premises capacity** (no data center, limited infrastructure staff)  
✅ **No regulatory mandate** for physical on-premises hosting  
✅ **Cloud TCO remains favorable** vs. on-premises over 3-5 year horizon  
✅ **Geographic distribution required** (multi-region, low-latency global access)  
✅ **Modern cloud services utilized** (AI/ML, IoT, analytics, CDN)

**Example Scenario:**

> **SaaS Collaboration Platform (Microsoft 365 → Google Workspace)**  
> - **Service**: Email, calendar, file storage, video conferencing  
> - **Users**: 300 staff  
> - **Migration Timeline**: 3 months (planning 4 weeks, migration 8 weeks, validation 2 weeks)  
> - **Migration Cost**: CHF 45K (consulting CHF 30K, training CHF 10K, parallel licenses CHF 5K)  
> - **Outcome**: Zero CAPEX, maintained cloud elasticity, improved collaboration features

---

#### 8.1.1.2 Hybrid Cloud Transition (Partial Repatriation)

Hybrid approach maintains some workloads in cloud while repatriating selected components to on-premises infrastructure. This strategy balances cloud benefits with specific requirements for on-premises control.

**Typical Hybrid Scenarios:**

| Scenario | Cloud Component | On-Premises Component | Rationale |
|----------|----------------|----------------------|-----------|
| **Data Sovereignty** | Application tier, compute, dev/test | Database with sensitive/regulated data | Regulatory data residency requirements (FADP, sector laws) |
| **Cost Optimization** | Burst capacity, non-production | Baseline production workload | Predictable baseline on-prem, elastic overflow in cloud |
| **Latency-Sensitive** | Backup/DR, analytics, reporting | Real-time transaction processing | Reduce network latency for critical interactive workloads |
| **Staged Migration** | New cloud-native services | Legacy systems being refactored | Gradual transition over 12-24 months, de-risk migration |
| **Regulatory Hybrid** | Non-critical data processing | Confidential/Restricted data | GDPR Article 44-50 transfer limitations, data classification-driven |

**Assessment Requirements:**

| Criterion | Evaluation Method | Documentation |
|-----------|-------------------|---------------|
| **Workload segmentation** | Identify which components remain cloud vs. on-prem (by data classification, latency, compliance) | Workload placement matrix |
| **Data synchronization** | Assess data replication requirements (latency tolerance, consistency model, volume) | Data flow diagram, sync SLA |
| **Network connectivity** | Evaluate hybrid connectivity options (VPN, AWS Direct Connect, Azure ExpressRoute, GCP Interconnect) | Network architecture diagram |
| **Management complexity** | Document additional operational overhead (multiple platforms, tools, skills) | Operational runbook |
| **Skill requirements** | Assess need for hybrid cloud expertise (both cloud and on-prem infrastructure) | Training plan, hiring needs |
| **Cost model** | Hybrid TCO vs. full cloud vs. full on-prem over 3-5 years | TCO comparison spreadsheet |
| **Security boundaries** | Define trust zones, encryption requirements, access controls across environments | Security architecture doc |
| **Compliance impact** | Verify hybrid model meets regulatory requirements (data residency, audit, access controls) | Compliance assessment |

**Hybrid Architecture Patterns:**

| Pattern | Description | Use Case |
|---------|-------------|----------|
| **Cloud-Bursting** | On-prem baseline + cloud overflow | Predictable load with occasional spikes (e-commerce, tax season) |
| **Data Residency Split** | Sensitive data on-prem, processing in cloud | Swiss FADP/GDPR strict data residency, but need cloud compute |
| **Active-Active** | Workloads distributed across cloud + on-prem | High availability, disaster recovery, geographic distribution |
| **Active-Passive** | On-prem primary, cloud DR/backup | Business continuity with cloud as standby |
| **Edge-Core** | Edge processing on-prem, aggregation in cloud | IoT, retail POS, latency-sensitive edge computing |

**Capital & Operational Expenditure (Hybrid Transition):**

| Component | CAPEX (Year 0) | OPEX (Annual) | Notes |
|-----------|---------------|---------------|-------|
| **On-prem infrastructure** | CHF 50K-500K | CHF 30K-100K | Partial infrastructure (compute, storage, network) |
| **Network connectivity** | CHF 10K-30K | CHF 5K-50K/year | VPN or dedicated circuits (1-10 Gbps) |
| **Hybrid management tools** | CHF 0-20K | CHF 10K-50K/year | Orchestration (Terraform, Ansible), monitoring (Datadog, Prometheus) |
| **Skills/training** | CHF 0-30K | CHF 20K-50K | Staff training on hybrid architectures, consulting |
| **Data synchronization** | CHF 5K-20K | CHF 5K-20K | Replication tools, bandwidth costs |
| **Professional services** | CHF 30K-100K | CHF 10K-30K | Architecture design, implementation support |
| **TOTAL** | **CHF 95K-700K** | **CHF 80K-300K/year** | **3-year TCO: CHF 335K-1.6M** |

**Migration Timeline (Hybrid Transition):**

| Phase | Duration | Activities |
|-------|----------|------------|
| **Architecture Design** | 4-8 weeks | Workload placement, network design, data flow mapping |
| **Infrastructure Procurement** | 8-12 weeks | Hardware procurement, facility preparation, network circuits |
| **Hybrid Connectivity Setup** | 4-6 weeks | VPN/Direct Connect configuration, testing |
| **Workload Migration** | 8-16 weeks | Phased migration of selected workloads to on-prem |
| **Integration & Testing** | 4-8 weeks | Data synchronization, failover testing, performance validation |
| **Optimization** | 4-8 weeks | Cost optimization, performance tuning, operational handoff |

**Total Timeline: 6-12 months typical**

**When Hybrid is Optimal:**

✅ **Regulatory requirements** mandate some on-premises data storage (FADP Art. 16, sector-specific)  
✅ **Specific workloads** have extreme latency sensitivity (<10ms requirements)  
✅ **Organization has existing on-premises capacity** with available headroom  
✅ **Workload characteristics support segmentation** (stateless app tier vs. stateful database)  
✅ **Gradual transition strategy** preferred (spread cost/risk over 12-24 months)  
✅ **Cost profile mixed** (some workloads cheaper on-prem, others in cloud)  
✅ **Legacy systems** require refactoring before cloud migration (interim hybrid state)

**Example Scenario:**

> **Healthcare Patient Records System (Hybrid)**  
> - **Cloud**: Application front-end (Azure), analytics/reporting (Power BI), backup (Azure Backup)  
> - **On-Premises**: Patient database with sensitive medical records (HIPAA/FADP compliance)  
> - **Network**: Azure ExpressRoute 1 Gbps  
> - **Migration Timeline**: 8 months (design 2 months, infrastructure 3 months, migration 3 months)  
> - **Migration Cost**: CHF 250K CAPEX + CHF 80K/year OPEX  
> - **Outcome**: Regulatory compliance maintained, cloud benefits for non-sensitive workloads

---

#### 8.1.1.3 On-Premises Repatriation (Full Build-Back)

Complete migration from cloud to [Organization]-owned infrastructure. This is the **highest-risk, highest-cost** exit strategy and should be considered only when justified by regulatory mandates or extraordinary circumstances.

**⚠️ CRITICAL: On-premises repatriation is economically justified in <5% of cloud exit scenarios.**

**Realistic Scenarios for Full Repatriation:**

| Scenario | Justification | Probability | Example |
|----------|---------------|-------------|---------|
| **Regulatory mandate** | Legal requirement for physically controlled on-premises infrastructure | Low-Medium | Classified government systems, some banking core systems |
| **Cost inversion** | Cloud costs exceed on-prem TCO over 3-5 years for stable, high-volume workloads | Low | Massive-scale batch processing (>1PB data, predictable load) |
| **Strategic independence** | Eliminate all external dependencies for critical infrastructure | Very Low | Defense systems, critical infrastructure (energy, water) |
| **Provider failure** | Cloud provider bankruptcy, unrecoverable breach, geopolitical access loss | Very Low | BC/DR emergency scenario (refer to ISMS-POL-A.8.13-14-5.30) |
| **Concentration risk** | DORA Article 28.9 diversification from single critical provider | Low | Financial institutions reducing hyperscaler dependency |

**Assessment Requirements:**

| Criterion | Evaluation Method | Documentation |
|-----------|-------------------|---------------|
| **Infrastructure requirements** | Size compute, storage, network, facilities, power/cooling | Infrastructure capacity plan |
| **Capital expenditure** | Initial investment for hardware, software, facilities | CAPEX budget (CHF 200K-2M+) |
| **Operational expenditure** | Staff, maintenance, utilities, software licenses | OPEX budget (annual) |
| **Total Cost of Ownership** | 3-5 year amortized TCO vs. current cloud costs | TCO comparison model |
| **Timeline** | Realistic build-out including procurement, deployment, testing | Project timeline (6-18 months) |
| **Skills/staffing** | Hiring, training, retention for infrastructure operations | Staffing plan (3-10 FTEs) |
| **Facilities** | Data center space, power/cooling capacity, physical security | Facility assessment |
| **Compliance** | On-prem infrastructure audit requirements (ISO 27001, sector-specific) | Compliance gap analysis |
| **Technology refresh** | Hardware refresh cycles (3-5 years), technology debt risk | Technology roadmap |
| **Elasticity loss** | Impact of losing cloud burst capacity on business | Business impact analysis |

**Capital & Operational Cost Estimates (Mid-Sized Organization, ~300 Staff):**

**CAPEX (Year 0) - Infrastructure Build-Out:**

| Component | Specification | Cost Range (CHF) | Lifecycle |
|-----------|--------------|------------------|-----------|
| **Compute** | 50 VMs @ 4-8 vCPU, 16-32 GB RAM | 150K-300K | 3-5 years |
| **Storage** | 100 TB usable (SAN/NAS, RAID 6, tiered) | 50K-150K | 5 years |
| **Network** | Core switches (10/25 GbE), firewalls, load balancers | 40K-80K | 5 years |
| **Backup** | Backup appliances, deduplication, tape library (optional) | 30K-60K | 5 years |
| **Facilities** | Rack space, power distribution, cooling (if colo) | 0-100K | N/A (or colo contract) |
| **Software licenses** | Virtualization (VMware, Hyper-V), backup (Veeam, Commvault) | 20K-50K | 1-3 years |
| **Professional services** | Migration consulting, implementation support | 50K-100K | One-time |
| **Contingency** | 15-20% buffer for unexpected costs | 50K-150K | One-time |
| **TOTAL CAPEX** | | **CHF 390K-990K** | |

**OPEX (Annual) - Ongoing Operations:**

| Component | Specification | Cost Range (CHF) | Notes |
|-----------|--------------|------------------|-------|
| **Staffing** | 3-5 FTEs (sysadmin, network, security) @ CHF 100K-120K loaded | 300K-600K | Salaries, benefits, training |
| **Maintenance** | Hardware support contracts (15-20% of CAPEX annually) | 30K-80K | Critical for uptime |
| **Software licenses** | Virtualization, backup, monitoring, security tools | 30K-100K | Annual renewals, support |
| **Facilities** | Colo rent, power, cooling (if no owned DC) | 30K-100K | Or CAPEX if owned facility |
| **Network** | WAN connectivity, ISP, bandwidth | 10K-30K | Multi-homed for redundancy |
| **Consulting** | Ongoing architecture, security, performance tuning | 20K-50K | Intermittent support |
| **Technology refresh reserve** | Set aside for 3-5 year hardware replacement | 50K-150K | Amortized CAPEX |
| **TOTAL OPEX** | | **CHF 470K-1.11M/year** | |

**5-Year Total Cost of Ownership:**

| Item | Cost (CHF) |
|------|-----------|
| **CAPEX (Year 0)** | 390K-990K |
| **OPEX (Years 1-5)** | 2.35M-5.55M |
| **Technology Refresh (Year 3-4)** | 200K-500K |
| **TOTAL 5-YEAR TCO** | **CHF 2.94M-7.04M** |

**Compare to Cloud (Example):**

| Scenario | Annual Cloud Cost | 5-Year Cloud Cost | On-Prem TCO | Verdict |
|----------|------------------|-------------------|-------------|---------|
| **Small workload** | CHF 200K | CHF 1M | CHF 2.94M-7.04M | ❌ Cloud cheaper |
| **Medium workload** | CHF 500K | CHF 2.5M | CHF 2.94M-7.04M | 🟡 Break-even |
| **Large, stable workload** | CHF 1M+ | CHF 5M+ | CHF 2.94M-7.04M | ✅ On-prem may be cheaper |

**Decision Framework: When On-Premises Repatriation is Justified**

Full on-premises repatriation is economically justified **ONLY** when one or more of the following apply:

**1. Regulatory Mandate (Compliance-Driven):**
- Legal requirement for physically controlled, air-gapped on-premises infrastructure
- Cloud services cannot meet data sovereignty requirements even with in-country deployments
- Sector-specific regulations prohibit public cloud (classified government, some defense)
- **Example**: Swiss Bundesverwaltung systems requiring air-gapped infrastructure, some cantonal healthcare systems

**2. Cost Inversion (Economics-Driven):**
- Annual cloud costs >CHF 500K **AND** workload characteristics:
  - Stable, predictable baseline (no burst requirements)
  - High-volume data processing (>500TB, low egress needs)
  - CPU-intensive batch workloads (continuous high utilization)
- 3-5 year on-prem TCO < 70% of equivalent cloud costs
- **Example**: Genomics research (petabyte-scale data, continuous compute), large-scale batch processing

**3. Strategic Independence (Risk-Driven):**
- Critical infrastructure requiring zero external dependencies
- National security, defense, or essential infrastructure sectors
- Geopolitical risk mitigation (provider jurisdiction conflicts)
- **Example**: Military command systems, critical infrastructure SCADA, central bank core systems

**4. Concentration Risk Elimination (DORA-Driven):**
- DORA Article 28.9: Critical ICT third-party provider concentration risk
- Financial institutions diversifying from single hyperscaler
- Not full repatriation, but hybrid with substantial on-prem component
- **Example**: Tier 1 bank moving 40% of workloads on-prem to reduce AWS dependency

**For all other scenarios, cloud-to-cloud or hybrid models are preferred due to:**
- Lower TCO for most workloads (70-80% of cases)
- Faster implementation (1/3 the timeline)
- Maintained elasticity and innovation access
- Reduced operational burden (no hardware lifecycle management)

**Migration Timeline (On-Premises Repatriation):**

| Phase | Duration | Activities | Critical Path Items |
|-------|----------|------------|---------------------|
| **Business Case** | 4-6 weeks | TCO analysis, regulatory justification, executive approval | Board approval, budget allocation |
| **Design** | 6-8 weeks | Architecture, capacity planning, facility assessment | Data center selection (if needed) |
| **Procurement** | 8-16 weeks | Hardware RFP, vendor selection, purchase orders | Lead times (network 12+ weeks) |
| **Facility Preparation** | 4-8 weeks | Rack installation, power/cooling, physical security (if new DC) | Facility readiness inspection |
| **Infrastructure Deployment** | 6-10 weeks | Hardware installation, network configuration, virtualization setup | Network connectivity established |
| **Migration & Testing** | 8-16 weeks | Phased workload migration, integration testing, performance validation | Cutover windows, rollback plans |
| **Optimization** | 4-8 weeks | Performance tuning, cost optimization, operational handoff | Operational acceptance |

**Total Timeline: 9-18 months typical (median: 12 months)**

**Staffing Requirements (On-Premises Operations):**

| Role | FTE | Responsibilities | Salary Range (CHF) |
|------|-----|------------------|-------------------|
| **Infrastructure Manager** | 1.0 | Architecture, vendor management, capacity planning | 120K-150K |
| **System Administrators** | 2-4 | Server management, patching, backup, monitoring | 90K-120K each |
| **Network Engineer** | 1.0 | Network design, firewall, routing, connectivity | 100K-130K |
| **Security Engineer** | 0.5-1.0 | Hardening, vulnerability management, incident response | 110K-140K |
| **On-Call Support** | Rotation | 24/7 incident response (if critical services) | +20% on-call premium |
| **TOTAL** | **4.5-7.0 FTEs** | | **CHF 450K-790K/year** |

**Risk Considerations (On-Premises Repatriation):**

| Risk | Impact | Mitigation |
|------|--------|------------|
| **Technology debt** | Hardware becomes obsolete, refresh needed every 3-5 years | Budget for refresh cycles, lifecycle planning |
| **Capacity planning** | Over-provisioning (wasted cost) or under-provisioning (performance issues) | Start with 30% headroom, monitor utilization |
| **Elasticity loss** | Cannot handle unexpected traffic spikes or growth | Hybrid architecture with cloud burst capacity |
| **Skills retention** | Infrastructure staff turnover, knowledge loss | Documentation, cross-training, competitive compensation |
| **Single points of failure** | On-prem infrastructure has failure domains | Redundancy (N+1), BC/DR to cloud or colo |
| **Compliance burden** | On-prem audits more intensive (physical security, environmental) | Annual penetration testing, compliance automation |
| **Exit cost** | Already invested in on-prem, hard to move back to cloud | Avoid proprietary lock-in (VMware NSX, etc.), use portable formats |

**When On-Premises Repatriation is NOT Justified:**

❌ **Cloud costs are high but workload is elastic** → Stay in cloud, optimize costs (reserved instances, autoscaling)  
❌ **Management perception "we want control"** → Hybrid with proper governance achieves control without full repatriation  
❌ **Short-term cloud pricing increase** → Negotiate enterprise agreement, consider alternative cloud provider  
❌ **Security concerns** → Cloud providers have better security than most on-prem (leverage their economies of scale)  
❌ **"We've always been on-prem"** → Cargo cult thinking, not a valid business justification

**Example Scenario:**

> **Large-Scale Batch Processing System (Justified On-Prem Repatriation)**  
> - **Workload**: Nightly ETL processing, 800 TB data warehouse, predictable 90% CPU utilization  
> - **Current Cloud Cost**: CHF 1.2M/year (EC2, S3, RDS)  
> - **On-Prem TCO**: CHF 600K CAPEX + CHF 400K/year OPEX = CHF 2.6M over 5 years  
> - **Cloud 5-Year**: CHF 6M  
> - **Savings**: CHF 3.4M over 5 years (57% reduction)  
> - **Justification**: Stable, predictable workload with no burst requirements  
> - **Migration Timeline**: 10 months  
> - **Outcome**: Cost-justified repatriation for high-volume, low-variability workload

---

#### 8.1.1.4 Decision Matrix

**Quantitative Decision Framework:**

Use this decision tree for exit strategy selection:
```
                    START: Cloud Service Exit Required
                                  │
                                  ▼
                    ┌─────────────────────────────┐
                    │ Is there a REGULATORY       │
                    │ MANDATE for on-prem?        │
                    │ (data sovereignty, air-gap) │
                    └──────┬───────────┬──────────┘
                           │           │
                      YES  │           │  NO
                           ▼           ▼
                    ┌─────────┐   ┌──────────────────────┐
                    │ On-Prem │   │ Annual cloud cost >  │
                    │    or   │   │ CHF 500K AND stable  │
                    │ Hybrid  │   │ workload (no burst)? │
                    └─────────┘   └──────┬────────┬──────┘
                                         │        │
                                    YES  │        │  NO
                                         ▼        ▼
                                  ┌──────────┐  ┌─────────────┐
                                  │ Run TCO  │  │ Cloud-to-   │
                                  │ analysis │  │ Cloud       │
                                  └────┬─────┘  │ (Default)   │
                                       │        └─────────────┘
                            On-prem TCO < 70%
                            of 5-year cloud?
                                       │
                                  YES  │  NO
                                       ▼  ▼
                              ┌──────────────────┐
                              │ On-Prem  │ Cloud-│
                              │    or    │ to-   │
                              │ Hybrid   │ Cloud │
                              └──────────────────┘
```

**Comparison Matrix:**

| Factor | Cloud-to-Cloud | Hybrid | On-Premises |
|--------|---------------|--------|-------------|
| **CAPEX** | ✅ None (zero infrastructure) | 🟡 CHF 95K-700K | ❌ CHF 390K-990K |
| **OPEX (Annual)** | 🟡 CHF 50K-500K+ (cloud fees) | 🟡 CHF 80K-300K (split) | ❌ CHF 470K-1.11M |
| **5-Year TCO** | 🟡 CHF 250K-2.5M+ | 🟡 CHF 335K-1.6M | ❌ CHF 2.94M-7.04M |
| **Timeline** | ✅ 3-6 months | 🟡 6-12 months | ❌ 9-18 months |
| **Risk** | ✅ Low (proven pattern) | 🟡 Medium (complexity) | ❌ High (technology debt) |
| **Elasticity** | ✅ Maintained | 🟡 Partial | ❌ Lost (fixed capacity) |
| **Skills Required** | ✅ Existing cloud skills | 🟡 Cloud + on-prem | ❌ Deep on-prem expertise |
| **Operational Complexity** | ✅ Low (single platform) | 🟡 Medium (multi-platform) | ❌ High (full lifecycle) |
| **Regulatory Flexibility** | 🟡 Provider-dependent | ✅ High (flexible placement) | ✅ Full control |
| **Technology Refresh** | ✅ Provider managed | 🟡 Partial responsibility | ❌ Full responsibility |
| **Business Continuity** | ✅ Provider SLA + geo-redundancy | 🟡 Complex (multi-site) | ❌ Organization responsible |
| **Innovation Access** | ✅ Latest cloud services (AI/ML, IoT) | 🟡 Cloud services only | ❌ Limited (vendor cycles) |

**Recommendation Priority (90-5-5 Rule):**

| Exit Strategy | Expected Usage | Primary Drivers |
|--------------|----------------|-----------------|
| **Cloud-to-Cloud** | 90%+ of services | Cost, speed, elasticity, innovation |
| **Hybrid** | 5-10% of services | Regulatory compliance, latency, cost optimization |
| **On-Premises** | <5% of services | Regulatory mandate, extreme cost inversion, strategic independence |

---

#### 8.1.1.5 Cross-Reference: Business Continuity & Disaster Recovery

Exit strategies address **planned, voluntary transitions** from cloud services. For **emergency scenarios** involving cloud provider failure, refer to Business Continuity and Disaster Recovery planning (ISMS-POL-A.8.13-14-5.30).

**Distinction:**

| Scenario Type | Planning Framework | Timeline | Example |
|---------------|-------------------|----------|---------|
| **Planned Exit** | This policy (A.5.23) | 3-18 months | Contract negotiation failure, cost optimization, strategic change |
| **Emergency Failover** | BC/DR (A.8.13-14-5.30) | Hours-Days | Provider outage, security breach, geopolitical access loss |

**Emergency Scenarios Requiring BC/DR:**

| Scenario | Probability | Response | Recovery Point |
|----------|-------------|----------|----------------|
| **Provider regional outage** | Medium | Failover to alternative region | Hours (RTO 4-8h) |
| **Provider security breach** | Low | Risk assessment, consider immediate exit | Days (RTO 24-72h) |
| **Provider bankruptcy** | Very Low | Execute exit plan immediately | Weeks (RTO 2-4 weeks) |
| **Geopolitical access loss** | Very Low | Emergency on-prem failover or alt provider | Days-Weeks (RTO 3-14 days) |
| **Contract termination for cause** | Low | Planned exit with compressed timeline | Months (RTO 1-3 months) |

**DORA Article 28.6 Requirement:**

> "The contractual arrangements on the use of ICT services supporting critical or important functions shall include [...] exit strategies, particularly for critical or important functions [...] as well as an obligation for the ICT third-party service provider to cooperate with the financial entity and with competent authorities during exit processes."

[Organization] shall document **both**:
1. **Planned exit strategies** (this section) for voluntary transitions
2. **Emergency exit procedures** (BC/DR policy) for provider failure scenarios

**Integration Points:**

- **Data Backup Strategy**: BC/DR backup location serves as exit data source (e.g., on-prem backup appliance or alternative cloud)
- **Alternative Provider Standby**: For Critical services, maintain hot/warm standby in alternative cloud (BC/DR + exit strategy)
- **Annual Failover Testing**: BC/DR testing validates exit data portability and alternative provider readiness
- **Documentation Consolidation**: Exit plans in ISMS-IMP-A.5.23.4 workbook cross-reference BC/DR runbooks

---

#### 8.1.1.6 Annual Review & Testing

Exit strategy viability SHALL be reviewed and tested annually to ensure assumptions remain valid and exit plans are executable.

**Annual Review Requirements:**

| Review Area | Activities | Documentation |
|-------------|------------|---------------|
| **Cost Updates** | Re-calculate cloud vs. alternative TCO using current pricing | Updated TCO spreadsheet |
| **Alternative Provider Evaluation** | Verify alternative providers still meet requirements | Provider comparison matrix |
| **Regulatory Changes** | Assess impact of new regulations on exit strategy | Regulatory impact assessment |
| **Technology Changes** | Evaluate new exit-enabling technologies (data portability tools, multi-cloud platforms) | Technology evaluation |
| **Contract Terms** | Review termination clauses, notice periods, data deletion requirements | Contract review checklist |
| **Organizational Changes** | Assess changes in risk appetite, business strategy, staffing | Strategic alignment doc |

**Annual Testing Requirements (DORA Article 28.6 Compliant):**

| Exit Strategy Type | Testing Requirement | Evidence | Frequency |
|-------------------|---------------------|----------|-----------|
| **Cloud-to-Cloud** | Export subset of data (10-20% sample), deploy on alternative provider | PoC screenshots, export validation report, cost quote | Annual |
| **Hybrid** | Test hybrid connectivity, data synchronization latency, failover procedures | Network performance metrics, sync test results, failover log | Annual |
| **On-Premises** | Update TCO calculation, verify infrastructure availability/capacity | TCO spreadsheet, capacity planning report, vendor quotes | Annual |

**Testing Scope:**

| Service Criticality | Testing Depth | Sample Size |
|--------------------|---------------|-------------|
| **Critical** | Full exit simulation (export all data, deploy in alt environment) | 100% of data, full workload |
| **High** | Significant sample test (export 50% data, deploy representative workload) | 50% sample |
| **Medium** | Representative sample (export 10-20% data, validate format) | 10-20% sample |
| **Low** | Verification only (confirm export capability exists) | Documentation review |

**Documentation & Evidence:**

All testing results SHALL be documented in:
- **ISMS-IMP-A.5.23.4** (Governance & Risk Management workbook) - "Exit Strategy" sheet
- **ISMS-IMP-A.5.23.5** (Compliance Monitoring Dashboard workbook) - "Exit Planning" sheet

**Required Evidence:**

| Evidence Type | Description | Retention |
|---------------|-------------|-----------|
| **Export Test Results** | Screenshots, file listings, data integrity validation | 3 years |
| **Cost Quotes** | Alternative provider pricing (compute, storage, network, licenses) | 1 year (refresh annually) |
| **PoC Reports** | Proof-of-concept deployment results, performance metrics, issues identified | 3 years |
| **Timeline Updates** | Revised migration timeline based on testing experience | 1 year (refresh annually) |
| **Lessons Learned** | Challenges encountered, process improvements | 3 years |

**Escalation & Remediation:**

| Finding | Action | Timeline |
|---------|--------|----------|
| **Exit not feasible** | Initiate alternative provider evaluation or architecture redesign | 3 months |
| **Cost inversion** | Re-evaluate cloud vs. on-prem decision, consider alternative providers | 6 months |
| **Regulatory non-compliance** | Immediate remediation, consider alternative provider or hybrid model | 30 days |
| **Data portability failure** | Engage provider to fix export, evaluate alternative exit method | 60 days |
| **Alternative provider unavailable** | Identify additional alternatives, consider multi-cloud architecture | 3 months |

**Review Cycle:**

- **Quarterly**: Critical services (risk rating = Critical)
- **Semi-Annual**: High-risk services (risk rating = High)
- **Annual**: Medium/Low-risk services

**Audit Trail:**

Exit strategy reviews and testing results shall be retained for audit purposes:
- **Evidence location**: `/evidence/cloud-services/exit-strategy/YYYY/`
- **Naming convention**: `EV-EXIT-[Service-ID]-[YYYYMMDD]-[Test-Type].pdf`
- **Retention period**: 3 years minimum (7 years for DORA-regulated entities)

### 8.2 Exit Triggers

| Trigger | Response |
|---------|----------|
| Contract termination | Execute planned exit |
| Provider failure | Emergency exit procedures |
| Security breach | Risk-based exit decision |
| Compliance failure | Immediate exit or remediation |
| Cost or value | Planned transition |
| Strategic change | Planned transition |

### 8.3 Data Portability Requirements

| Requirement | Description |
|-------------|-------------|
| Export format | Industry-standard, documented formats |
| Export method | Secure, reliable extraction mechanism |
| Completeness | All data, metadata, configurations |
| Validation | Verification of export integrity |
| Timeline | Reasonable window for extraction |
| Assistance | Provider support for migration |

### 8.4 Exit Execution

| Phase | Activities |
|-------|------------|
| **Planning** | Confirm exit strategy, timeline, resources |
| **Preparation** | Configure target, test migration |
| **Execution** | Export data, migrate services, validate |
| **Termination** | Confirm data deletion, close accounts |
| **Verification** | Destruction certificate, access removal |

### 8.5 Vendor Lock-In Mitigation

| Strategy | Implementation |
|----------|----------------|
| Standard formats | Use portable data formats |
| API abstraction | Avoid deep proprietary integration |
| Multi-cloud capability | Design for portability |
| Regular export testing | Verify data can be extracted |
| Alternative evaluation | Maintain awareness of alternatives |

---

## 9. Cloud-Specific Security Requirements

### 9.1 Identity & Access Management

| Requirement | Implementation |
|-------------|----------------|
| Federated identity | SSO via organizational identity provider |
| MFA enforcement | Required for all users, mandatory for admins |
| Privileged access | Just-in-time, time-limited, monitored |
| Service accounts | Inventory, rotate credentials, least privilege |
| Access reviews | Regular certification of access rights |

### 9.2 Data Protection

| Requirement | Implementation |
|-------------|----------------|
| Encryption in transit | TLS 1.2+ for all communications |
| Encryption at rest | Provider or customer-managed keys |
| Key management | Secure key storage, rotation policy |
| Data classification | Labels applied, controls enforced |
| Data residency | Processing location documented and verified |
| Data segregation | Logical or physical isolation as required |

### 9.3 Security Monitoring

| Requirement | Implementation |
|-------------|----------------|
| Audit logging | All security-relevant events logged |
| Log centralization | Logs exported to organizational SIEM |
| Alerting | Security events trigger appropriate alerts |
| Retention | Logs retained per policy (minimum 12 months) |
| Threat detection | Provider and organizational detection |

---

## 10. Multi-Cloud Considerations

### 10.1 Multi-Cloud Challenges

| Challenge | Mitigation |
|-----------|------------|
| Inconsistent controls | Standardized baseline across providers |
| Visibility gaps | Unified monitoring and logging |
| Skill requirements | Training and documentation |
| Complexity | Clear architecture and governance |
| Cost management | Centralized tracking and optimization |

### 10.2 Multi-Cloud Governance

| Element | Requirement |
|---------|-------------|
| Policy consistency | Same security policies across providers |
| Identity federation | Unified identity across clouds |
| Monitoring | Consolidated security monitoring |
| Incident response | Coordinated response procedures |
| Compliance | Consistent compliance posture |

---

## 11. References

| Document | Relationship |
|----------|--------------|
| ISMS-POL-A.5.19-23 | Parent policy framework |
| ISMS-POL-A.5.19-23-S1 | Cloud providers are suppliers |
| ISMS-POL-A.5.19-23-S2 | Cloud contract requirements |
| ISMS-POL-A.5.19-23-S3 | Cloud sub-processor management |
| ISMS-POL-A.5.19-23-S4 | Cloud service monitoring |
| ISO/IEC 27017 | Cloud security controls |
| ISO/IEC 27018 | Cloud privacy |

---

**Next Document:** ISMS-POL-A.5.19-23-S6 — Assessment Methodology & Automation

---

*"The cloud is just someone else's computer — but you're still responsible for your data."*