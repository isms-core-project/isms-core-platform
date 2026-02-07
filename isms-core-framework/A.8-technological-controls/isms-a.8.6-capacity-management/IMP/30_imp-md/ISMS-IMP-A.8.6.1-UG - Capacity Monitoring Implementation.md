**ISMS-IMP-A.8.6.1-UG - Capacity Utilization Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.6: Capacity Management

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.6.1-UG |
| **Version** | 1.0 |
| **Assessment Area** | Infrastructure Capacity Utilization & Resource Monitoring |
| **Related Policy** | ISMS-POL-A.8.6 (Capacity Management Policy) |
| **Purpose** | Document current capacity utilization across all infrastructure resources, assess against policy thresholds, and identify capacity risks in a vendor-agnostic manner |
| **Target Audience** | Infrastructure Engineers, IT Operations, Capacity Planning Team, System Administrators, Compliance Officers, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Monthly (with quarterly deep reviews) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Capacity Utilization assessment workbook | ISMS Implementation Team |

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.8.6.1-TG.

---

## Assessment Overview

### Purpose & Scope

**Assessment Name:** ISMS-IMP-A.8.6.1 - Capacity Utilization Assessment

#### What This Assessment Covers

This assessment documents CURRENT capacity utilization across all infrastructure and application resources. This is the foundational "WHERE are we now?" assessment that answers:

- What resources exist in the infrastructure? (compute, storage, network, application)
- What is the current utilization of each resource? (percentage used)
- What is the peak utilization over recent history? (maximum observed)
- How does current utilization compare to policy thresholds? (warning, critical)
- What capacity headroom exists? (remaining capacity before exhaustion)
- Which resources are at risk of capacity exhaustion?

#### Key Principle

This assessment is **completely vendor-agnostic and platform-independent**. You document YOUR specific infrastructure (whether physical servers, VMware, Hyper-V, AWS, Azure, GCP, Kubernetes, hybrid, whatever), and measure utilization against generic policy thresholds.

#### What You'll Document

- Complete resource inventory (all compute, storage, network, application resources)
- Current utilization metrics for each resource
- Peak utilization (30-day and 90-day maximum)
- Average utilization (30-day and 90-day average)
- Threshold status (below warning, warning, critical, exceeded)
- Capacity headroom (percentage remaining before thresholds)
- Monitoring coverage (which resources are monitored, which are not)
- Resources at risk (threshold breaches, trending toward exhaustion)
- Supporting evidence (monitoring dashboards, metric exports)

#### How This Relates to Other A.8.6 Assessments

| Assessment            | Focus                  | Relationship to A.8.6.1           |
|-----------------------|------------------------|------------------------------------|
| **ISMS-IMP-A.8.6.1** | **Current Utilization** | **WHERE are we now - current capacity status** |
| ISMS-IMP-A.8.6.2     | Forecasting & Planning | WHERE will we be - future capacity needs |
| ISMS-IMP-A.8.6.3     | Compliance Dashboard   | Consolidated view across current + future |

This assessment (A.8.6.1) MUST be completed first - you can't forecast future capacity until you know current utilization!

### Who Should Complete This Assessment

#### Primary Stakeholders

1. **Infrastructure Engineering** - Architecture, resource inventory, virtualization platforms
2. **IT Operations** - Day-to-day monitoring, resource management
3. **Capacity Planning Team** - Utilization analysis, threshold management
4. **System Administrators** - Server, storage, network administration
5. **Cloud Operations** - Cloud resource management (if applicable)

#### Required Skills

- Understanding of infrastructure architecture (compute, storage, network)
- Familiarity with monitoring tools (Prometheus, Datadog, CloudWatch, etc.)
- Access to monitoring dashboards and metric sources
- Understanding of resource types and utilization metrics
- Knowledge of organizational threshold policies

#### Time Commitment

- **Initial assessment:** 8-12 hours (for comprehensive resource inventory and data collection)
- **Monthly updates:** 2-3 hours (update metrics, review thresholds)
- **Quarterly deep reviews:** 4-6 hours (validate inventory, review monitoring coverage)

### Expected Outputs

Upon completion, you will have:

1. ✅ **Complete resource inventory** - Every infrastructure resource documented
2. ✅ **Current utilization data** - Real-time and historical utilization metrics
3. ✅ **Peak utilization tracking** - Maximum observed utilization (30/90 days)
4. ✅ **Threshold assessment** - Comparison vs. warning and critical thresholds
5. ✅ **Capacity headroom analysis** - Remaining capacity before exhaustion
6. ✅ **At-risk resource identification** - Resources approaching or exceeding thresholds
7. ✅ **Monitoring coverage assessment** - Gaps in monitoring infrastructure
8. ✅ **Evidence register** - Supporting documentation for audit
9. ✅ **Approved assessment** - Three-level approval workflow completed

---

## Prerequisites

### Information You'll Need

Before starting this assessment, gather:

#### 1. Infrastructure Access

- Administrator access to monitoring systems (Prometheus, Datadog, CloudWatch, etc.)
- Access to infrastructure management consoles:
  - **Hypervisor management** (vCenter, Hyper-V Manager, Proxmox, etc.)
  - **Cloud consoles** (AWS Console, Azure Portal, GCP Console)
  - **Container orchestration** (Kubernetes Dashboard, OpenShift, Rancher)
  - **Storage management** (SAN/NAS management, cloud storage dashboards)
  - **Network management** (switch/router management, network monitoring)
- Access to asset inventory or CMDB systems
- Access to application monitoring dashboards

#### 2. Documentation

- Current infrastructure architecture diagrams
- Network topology diagrams
- Resource allocation documentation
- Capacity threshold policies (from ISMS-POL-A.8.6)
- Previous capacity assessments (if available)

#### 3. Historical Data

- Monitoring data covering last 90 days minimum (180 days preferred)
- Incident reports related to capacity issues
- Previous capacity expansion records
- Performance reports

#### 4. Policy Requirements

- ISMS-POL-A.8.6, Section 2 (Resource Types to Monitor)
- ISMS-POL-A.8.6, Section 3 (Capacity Monitoring Requirements)
- ISMS-POL-A.8.6, Section 4 (Capacity Thresholds and Alerting)
- Organizational threshold definitions (warning, critical)

### Required Tools

- **Microsoft Excel** (2016 or later) for workbook completion
- **Monitoring system access** (dashboards, APIs, metric export)
- **Infrastructure management tools** (hypervisor consoles, cloud dashboards)
- **Screen capture tools** (for evidence screenshots)
- **Metric export tools** (CSV export, API clients, monitoring tool native export)

### Dependencies

This assessment has NO dependencies - it's the first assessment in the A.8.6 series.

However, outputs from this assessment are INPUT to:

- A.8.6.2 (Forecasting & Planning) - Needs utilization data from this assessment
- A.8.6.3 (Compliance Dashboard) - Consolidates data from all A.8.6 assessments

---

## Workflow

### High-Level Process

```
1. PREPARE
   ↓
2. INVENTORY RESOURCES (Sheet 1)
   ↓
3. COLLECT UTILIZATION DATA (Sheets 2-5)
   ↓
4. ASSESS THRESHOLDS (Sheet 6)
   ↓
5. ANALYZE MONITORING COVERAGE (Sheet 7)
   ↓
6. IDENTIFY AT-RISK RESOURCES (Sheet 8)
   ↓
7. REGISTER EVIDENCE (Sheet 9)
   ↓
8. REVIEW & APPROVE
```

### Detailed Workflow

#### Phase 1: Preparation (1-2 hours)

**Objective:** Gather information and understand requirements

**Steps:**
1. Read this entire User Guide
2. Gather all prerequisites (see above)
3. Review policy requirements (ISMS-POL-A.8.6, Sections 2, 3, 4)
4. Identify all infrastructure resources in your environment
5. Verify monitoring system access and data availability
6. Schedule time with SMEs (infrastructure, operations, monitoring teams)
7. Create working folder for evidence collection

**Deliverable:** List of all resources and SME availability

#### Phase 2: Resource Inventory (3-4 hours)

**Objective:** Complete Sheet 1 - Resource Inventory

**Steps:**
1. List EVERY infrastructure resource in scope:

   - Physical servers
   - Virtual machines (VMware, Hyper-V, KVM, etc.)
   - Cloud instances (AWS EC2, Azure VMs, GCP Compute Engine)
   - Containers and Kubernetes pods/nodes
   - Storage volumes (SAN, NAS, cloud storage)
   - Network devices (switches, routers, firewalls, load balancers)
   - Application resources (concurrent users, transaction capacity)

2. For each resource:

   - Document resource ID, name, type
   - Identify infrastructure platform
   - Classify environment (Production, UAT, Dev, DR)
   - Assign criticality (Critical, High, Medium, Low)
   - Determine monitoring status

3. Verify completeness with infrastructure team
4. Cross-check with asset inventory/CMDB

**Deliverable:** Complete Sheet 1 with all resources

**Quality Check:**

- ✓ All production resources identified
- ✓ Non-production resources identified
- ✓ Cloud resources included
- ✓ Virtual and container resources included
- ✓ No "unknown" or "TBD" values
- ✓ Status accurately reflects current state

#### Phase 3: Compute Capacity Data Collection (2-3 hours)

**Objective:** Complete Sheet 2 - Compute Capacity

**Steps:**
1. For each compute resource (servers, VMs, containers):

   - Collect current CPU utilization (%)
   - Collect current memory utilization (%)
   - Collect 30-day peak CPU utilization
   - Collect 30-day peak memory utilization
   - Collect 30-day average CPU utilization
   - Collect 30-day average memory utilization
   - Collect 90-day peak and average (if available)

2. Document total capacity (CPU cores, memory GB)
3. Calculate utilization vs. capacity
4. Compare against policy thresholds
5. Capture evidence (monitoring dashboard screenshots)

**Deliverable:** Complete Sheet 2 with compute utilization data

**Quality Check:**

- ✓ Current utilization is recent (< 24 hours old)
- ✓ Peak utilization reflects true maximums
- ✓ Average utilization calculated correctly
- ✓ Threshold comparisons accurate
- ✓ Evidence collected for critical resources

#### Phase 4: Storage Capacity Data Collection (2-3 hours)

**Objective:** Complete Sheet 3 - Storage Capacity

**Steps:**
1. For each storage resource (volumes, file systems, databases):

   - Collect current disk space utilization (GB used, % used)
   - Collect 30-day peak utilization
   - Collect 30-day average utilization
   - Document total capacity (GB)
   - Document IOPS utilization (if applicable)
   - Document throughput utilization (if applicable)

2. For database storage:

   - Document table/database sizes
   - Document transaction log sizes
   - Document backup storage utilization

3. For cloud storage:

   - Document object storage utilization
   - Document block storage utilization

4. Compare against policy thresholds
5. Capture evidence

**Deliverable:** Complete Sheet 3 with storage utilization data

**Quality Check:**

- ✓ All storage types included (disk, database, backup, cloud)
- ✓ Utilization data is current
- ✓ Growth trends considered
- ✓ Evidence collected

#### Phase 5: Network Capacity Data Collection (1-2 hours)

**Objective:** Complete Sheet 4 - Network Capacity

**Steps:**
1. For each network resource:

   - Collect interface utilization (% bandwidth)
   - Collect throughput (Mbps/Gbps actual vs. capacity)
   - Collect packet rate (packets per second)
   - Collect error rates and dropped packets
   - Document 30-day peak utilization
   - Document 30-day average utilization

2. For network services:

   - Load balancer connection counts
   - Firewall connection table utilization
   - VPN tunnel utilization

3. Compare against policy thresholds
4. Capture evidence

**Deliverable:** Complete Sheet 4 with network utilization data

**Quality Check:**

- ✓ All network segments covered
- ✓ Peak utilization captured
- ✓ Service-level metrics included
- ✓ Evidence collected

#### Phase 6: Application Capacity Data Collection (2-3 hours)

**Objective:** Complete Sheet 5 - Application Capacity

**Steps:**
1. For each application or service:

   - Collect concurrent user/session counts
   - Collect transaction rates (requests per second, TPS)
   - Collect queue depths (message queues, job queues)
   - Collect connection pool utilization
   - Collect thread pool utilization
   - Document licensed capacity limits
   - Document architectural capacity limits

2. For web services:

   - HTTP request rates
   - API rate limits and utilization
   - Response time metrics

3. Compare against capacity limits and thresholds
4. Capture evidence

**Deliverable:** Complete Sheet 5 with application capacity data

**Quality Check:**

- ✓ All critical applications covered
- ✓ Capacity limits documented
- ✓ Current utilization vs. limits assessed
- ✓ Evidence collected

#### Phase 7: Threshold Assessment (1-2 hours)

**Objective:** Complete Sheet 6 - Threshold Status

**Steps:**
1. For each resource, compare utilization vs. thresholds:

   - Identify resources below warning threshold (healthy)
   - Identify resources at/above warning threshold (plan capacity)
   - Identify resources at/above critical threshold (immediate action)
   - Identify resources exceeding maximum capacity (capacity exhausted)

2. Calculate capacity headroom (% remaining before warning/critical)
3. Calculate time-to-threshold (if trending data available)
4. Prioritize at-risk resources by criticality
5. Document threshold breach incidents (if any)

**Deliverable:** Complete Sheet 6 with threshold assessment

**Quality Check:**

- ✓ All resources assessed against thresholds
- ✓ Threshold status is accurate
- ✓ At-risk resources identified
- ✓ Prioritization reflects business criticality

#### Phase 8: Monitoring Coverage Assessment (1 hour)

**Objective:** Complete Sheet 7 - Monitoring Coverage

**Steps:**
1. For each resource:

   - Document monitoring status (monitored, partially monitored, not monitored)
   - Identify monitoring tool(s) used
   - Document metric coverage (which metrics collected)
   - Identify monitoring gaps

2. For monitored resources:

   - Verify data retention meets policy (12+ months historical data)
   - Verify alerting configured for thresholds
   - Verify data quality and accuracy

3. For unmonitored resources:

   - Document reason (technical limitation, cost, deprioritized)
   - Assess risk of not monitoring
   - Create remediation plan

**Deliverable:** Complete Sheet 7 with monitoring coverage assessment

**Quality Check:**

- ✓ Monitoring status accurate
- ✓ Gaps identified
- ✓ Remediation plans for gaps

#### Phase 9: At-Risk Resource Analysis (1-2 hours)

**Objective:** Complete Sheet 8 - At-Risk Resources

**Steps:**
1. Consolidate all resources at/above warning threshold
2. Consolidate all resources at/above critical threshold
3. For each at-risk resource:

   - Assess business impact if capacity exhausted
   - Determine root cause (workload growth, inefficiency, etc.)
   - Identify potential solutions (capacity expansion, optimization, workload migration)
   - Create remediation plan
   - Assign owner
   - Set target date

4. Prioritize remediation by risk and business impact

**Deliverable:** Complete Sheet 8 with at-risk analysis and remediation plans

**Quality Check:**

- ✓ All at-risk resources identified
- ✓ Business impact assessed
- ✓ Remediation plans are actionable
- ✓ Owners assigned
- ✓ Target dates are realistic

#### Phase 10: Evidence Registry (30-60 minutes)

**Objective:** Complete Sheet 9 - Evidence Registry

**Steps:**
1. List all evidence collected during assessment
2. Organize by category (monitoring dashboards, metric exports, infrastructure screenshots, documentation)
3. Document storage locations
4. Verify accessibility
5. Tag for audit readiness
6. Ensure evidence is recent (< 30 days old for current assessments)

**Deliverable:** Complete Sheet 9 with evidence register

**Quality Check:**

- ✓ All evidence listed
- ✓ Storage locations accessible
- ✓ Evidence is recent
- ✓ Audit-ready format

#### Phase 11: Review & Approval (1-2 hours)

**Objective:** Three-level approval process

**Steps:**
1. **Self-review** (completer)

   - Check completeness of all sheets
   - Verify accuracy of data
   - Validate evidence quality
   - Run quality checklist (see Quality Checklist section)
   
2. **Technical review** (infrastructure/operations manager)

   - Review technical accuracy
   - Validate utilization data
   - Check threshold assessments
   - Verify monitoring coverage
   - Approve or request changes
   
3. **Management review** (CIO/IT Director or delegate)

   - Review at-risk resources and business impact
   - Approve remediation plans
   - Allocate resources for capacity expansion
   - Final approval

**Deliverable:** Approved assessment ready for forecasting and dashboard consolidation

**Quality Check:**

- ✓ All sections complete
- ✓ All reviewers have approved
- ✓ Evidence is audit-ready
- ✓ At-risk resources have remediation plans

---

## Completing Each Sheet

This section provides detailed guidance for completing each sheet in the workbook.

### Sheet 1: Resource Inventory

#### Purpose

Create a master list of ALL infrastructure resources in scope for capacity management. This is your "single source of truth" for what exists and must be monitored.

#### What to Document

For EACH resource:

- **Resource ID**: Unique identifier (hostname, instance ID, asset tag)
- **Resource Name**: Human-readable name
- **Resource Type**: Compute, Storage, Network, Application
- **Sub-Type**: Server, VM, Container, Disk, Network Interface, Load Balancer, etc.
- **Infrastructure Platform**: Physical, VMware, Hyper-V, AWS, Azure, GCP, Kubernetes, etc.
- **Environment**: Production, UAT, Development, Disaster Recovery
- **Criticality**: Critical, High, Medium, Low
- **Business Owner**: Department/team that owns the resource
- **Technical Owner**: Person/team responsible for operations
- **Monitoring Status**: Monitored, Partially Monitored, Not Monitored
- **Notes**: Any relevant context

#### Common Mistakes to Avoid

❌ **Incomplete inventory** - Forgetting dev/test environments, cloud resources, containers  
❌ **Duplicate entries** - Same resource listed multiple times  
❌ **Vague names** - "Server1" instead of "web-prod-01.example.com"  
❌ **Missing cloud resources** - Forgetting cloud VMs, storage, serverless  
❌ **Not documenting virtual resources** - Missing VMs, containers, cloud instances  
❌ **Ignoring application-level capacity** - Forgetting concurrent users, connection pools  

#### How to Complete

**Step 1: Identify All Resources**

Ask these questions:
1. What compute resources exist?

   - Physical servers (on-premises datacenter)
   - Virtual machines (VMware, Hyper-V, KVM)
   - Cloud instances (AWS EC2, Azure VMs, GCP Compute Engine)
   - Containers (Docker, Kubernetes pods)
   - Serverless functions (AWS Lambda, Azure Functions)

2. What storage resources exist?

   - SAN/NAS volumes
   - Local disk storage
   - Cloud block storage (AWS EBS, Azure Disks)
   - Cloud object storage (AWS S3, Azure Blob)
   - Database storage
   - Backup storage

3. What network resources exist?

   - Network switches
   - Routers
   - Firewalls
   - Load balancers
   - VPN concentrators
   - WAN links

4. What application resources exist?

   - Web servers and application servers
   - Databases
   - Message queues
   - Cache servers
   - Application-specific capacity limits

**Step 2: For Each Resource, Gather Details**

- **Access infrastructure management consoles**:
  - VMware vCenter (for VMware VMs)
  - Hyper-V Manager (for Hyper-V VMs)
  - AWS Console → EC2, EBS, S3 (for AWS resources)
  - Azure Portal → Virtual Machines, Disks, Storage Accounts
  - GCP Console → Compute Engine, Persistent Disks, Cloud Storage
  - Kubernetes Dashboard → Nodes, Pods
- **Check asset inventory or CMDB** (if available)
- **Query monitoring systems** for discovered resources
- **Consult with infrastructure teams** to ensure completeness

**Step 3: Classify Environment**

| Environment | Definition | Examples |
|-------------|------------|----------|
| **Production** | Live systems serving customers or critical business functions | Customer-facing web servers, production databases, critical SaaS applications |
| **UAT** | User acceptance testing, pre-production | Staging environment, QA testing systems |
| **Development** | Development and testing | Developer workstations, development servers, test databases |
| **Disaster Recovery** | Backup/failover systems | DR datacenter resources, backup infrastructure |

**Step 4: Assign Criticality**

| Criticality | Definition | Business Impact if Unavailable |
|-------------|------------|--------------------------------|
| **Critical** | Essential for business operations, revenue-generating | Immediate business impact, revenue loss, customer impact |
| **High** | Important for business operations | Significant impact within hours, productivity loss |
| **Medium** | Supports business operations | Moderate impact within days |
| **Low** | Non-essential, development/test | Minimal business impact |

**Critical resources should be prioritized for capacity management.**

**Step 5: Determine Monitoring Status**

| Status | Definition | Action Required |
|--------|------------|-----------------|
| **Monitored** | Resource is fully monitored (all relevant metrics collected) | Continue monitoring |
| **Partially Monitored** | Some metrics monitored but gaps exist | Complete monitoring coverage |
| **Not Monitored** | Resource not monitored at all | Implement monitoring |

**Step 6: Document Business and Technical Owners**

- **Business Owner**: Department/team that owns the resource from a business perspective (e.g., "Sales", "Finance", "HR")
- **Technical Owner**: Person/team responsible for day-to-day operations (e.g., "Infrastructure Team", "Database Team", "Cloud Operations")

**Step 7: Add Relevant Notes**

Examples:

- "Scheduled for decommission Q3 2026"
- "Pending migration to cloud"
- "Shared resource across multiple applications"
- "License limit: 1000 concurrent users"

#### Real-World Examples

**Example 1: Physical Server**
| Attribute | Value |
|-------|-------|
| Resource ID | srv-dc01-rack12-u15 |
| Resource Name | Database Server - Production Primary |
| Resource Type | Compute |
| Sub-Type | Physical Server |
| Infrastructure Platform | Physical (Dell PowerEdge R750) |
| Environment | Production |
| Criticality | Critical |
| Business Owner | Finance Department |
| Technical Owner | Database Team |
| Monitoring Status | Monitored |
| Notes | Primary database for financial reporting system, 2x redundancy with srv-dc02-rack12-u16 |

**Example 2: VMware Virtual Machine**
| Attribute | Value |
|-------|-------|
| Resource ID | web-prod-01 |
| Resource Name | Production Web Server 01 |
| Resource Type | Compute |
| Sub-Type | Virtual Machine |
| Infrastructure Platform | VMware (ESXi 7.0, Cluster: PROD-WEB) |
| Environment | Production |
| Criticality | High |
| Business Owner | Marketing |
| Technical Owner | Infrastructure Team |
| Monitoring Status | Monitored |
| Notes | Part of 3-node web cluster, load balanced |

**Example 3: AWS EC2 Instance**
| Attribute | Value |
|-------|-------|
| Resource ID | i-0abcd1234efgh5678 |
| Resource Name | app-prod-api-01 |
| Resource Type | Compute |
| Sub-Type | Cloud Instance |
| Infrastructure Platform | AWS (EC2 m5.xlarge, us-east-1a) |
| Environment | Production |
| Criticality | Critical |
| Business Owner | Product Team |
| Technical Owner | Cloud Operations |
| Monitoring Status | Monitored |
| Notes | API gateway for mobile app, auto-scaling group: 2-10 instances |

**Example 4: Kubernetes Pod (Abstract)**
| Attribute | Value |
|-------|-------|
| Resource ID | k8s-node-prod-worker-03 |
| Resource Name | Kubernetes Worker Node 03 |
| Resource Type | Compute |
| Sub-Type | Container Host (Kubernetes Node) |
| Infrastructure Platform | Kubernetes (v1.28, Cluster: prod-k8s) |
| Environment | Production |
| Criticality | High |
| Business Owner | Engineering |
| Technical Owner | Platform Team |
| Monitoring Status | Monitored |
| Notes | Runs 20-30 pods, node capacity: 64 CPU, 256GB RAM |

**Example 5: Storage Volume**
| Attribute | Value |
|-------|-------|
| Resource ID | vol-data-prod-db-01 |
| Resource Name | Database Data Volume |
| Resource Type | Storage |
| Sub-Type | SAN Volume (LUN) |
| Infrastructure Platform | NetApp FAS8200 |
| Environment | Production |
| Criticality | Critical |
| Business Owner | Finance |
| Technical Owner | Storage Team |
| Monitoring Status | Monitored |
| Notes | 2TB allocated, RAID 10, mounted on srv-dc01-rack12-u15 as /data |

**Example 6: AWS S3 Bucket**
| Attribute | Value |
|-------|-------|
| Resource ID | s3-prod-customer-uploads |
| Resource Name | Customer Uploads Bucket |
| Resource Type | Storage |
| Sub-Type | Object Storage |
| Infrastructure Platform | AWS (S3, us-east-1) |
| Environment | Production |
| Criticality | High |
| Business Owner | Customer Success |
| Technical Owner | Cloud Operations |
| Monitoring Status | Monitored |
| Notes | Public-facing uploads, lifecycle policy: 90 days to Glacier |

**Example 7: Network Switch**
| Attribute | Value |
|-------|-------|
| Resource ID | sw-core-dc01-01 |
| Resource Name | Datacenter Core Switch 01 |
| Resource Type | Network |
| Sub-Type | Switch (Core) |
| Infrastructure Platform | Cisco Nexus 9000 |
| Environment | Production |
| Criticality | Critical |
| Technical Owner | Network Team |
| Monitoring Status | Monitored |
| Notes | 40Gbps uplinks, serves all production racks 1-20 |

**Example 8: Application - Concurrent Users**
| Attribute | Value |
|-------|-------|
| Resource ID | app-crm-prod |
| Resource Name | CRM System |
| Resource Type | Application |
| Sub-Type | Web Application |
| Infrastructure Platform | Salesforce (SaaS) |
| Environment | Production |
| Criticality | Critical |
| Business Owner | Sales |
| Technical Owner | IT Operations |
| Monitoring Status | Partially Monitored |
| Notes | License: 500 concurrent users, 1000 named users |

#### Evidence to Collect

- Asset inventory export (from CMDB or asset management system)
- Infrastructure management console screenshots:
  - VMware vCenter: VM inventory screenshot
  - AWS Console: EC2 instance list, EBS volume list, S3 bucket list
  - Azure Portal: VM list, disk list, storage account list
  - GCP Console: Compute Engine instance list, persistent disk list
- Network diagrams (current architecture)
- Monitoring system inventory (discovered resources screenshot/export)

**Evidence Naming Convention:**
```
Sheet1-Evidence-[Type]-[Date].extension

Examples:
Sheet1-Evidence-vCenter-Inventory-2026-01-15.png
Sheet1-Evidence-AWS-EC2-List-2026-01-15.csv
Sheet1-Evidence-Network-Diagram-2026-01-15.pdf
```

#### Quality Checklist

- [ ] All production resources documented
- [ ] Non-production resources documented (dev, test, DR)
- [ ] Cloud resources included (if applicable)
- [ ] Virtual and container resources included
- [ ] Resource types correctly categorized
- [ ] Environment classification accurate
- [ ] Criticality assigned based on business impact
- [ ] Monitoring status verified (not assumed)
- [ ] Business and technical owners identified
- [ ] No "TBD" or "Unknown" values without justification
- [ ] Evidence collected and registered in Sheet 9
- [ ] Cross-referenced with asset inventory/CMDB
- [ ] Reviewed with infrastructure teams for completeness

---

### Sheet 2: Compute Capacity

#### Purpose

Document current CPU and memory utilization for all compute resources. This provides visibility into compute capacity consumption and identifies resources approaching capacity limits.

#### What to Document

For EACH compute resource:

- **Resource ID** (from Sheet 1)
- **Total Capacity**:
  - CPU cores (total)
  - Memory GB (total)
- **Current Utilization**:
  - CPU utilization (% used)
  - Memory utilization (% used)
- **Peak Utilization** (30 days):
  - CPU peak (% max observed)
  - Memory peak (% max observed)
- **Peak Utilization** (90 days):
  - CPU peak (% max observed)
  - Memory peak (% max observed)
- **Average Utilization** (30 days):
  - CPU average (% mean)
  - Memory average (% mean)
- **Average Utilization** (90 days):
  - CPU average (% mean)
  - Memory average (% mean)
- **Threshold Status**:
  - Below Warning / Warning / Critical / Exceeded
- **Capacity Headroom**:
  - CPU headroom (% remaining before warning threshold)
  - Memory headroom (% remaining before warning threshold)

#### Common Mistakes to Avoid

❌ **Using stale data** - Utilization data from weeks/months ago  
❌ **Ignoring peak utilization** - Only looking at current or average  
❌ **Not accounting for burst capacity** - Assuming average = sufficient  
❌ **Mixing CPU allocation with utilization** - Allocated vCPUs ≠ actual CPU usage  
❌ **Ignoring memory pressure** - Memory utilization may not show swapping/paging  
❌ **Not considering workload patterns** - Missing daily/weekly peaks  

#### How to Complete

**Step 1: Access Monitoring Data**

Depending on your infrastructure, access:

- **Physical Servers**:
  - Operating system monitoring (top, htop, Task Manager, Performance Monitor)
  - Hardware management (iLO, iDRAC, BMC)
  - Monitoring tools (Nagios, Zabbix, Prometheus)
- **Virtual Machines**:
  - Hypervisor monitoring (vCenter Performance, Hyper-V Performance Monitor)
  - Guest OS monitoring
  - Monitoring tools
- **Cloud Instances**:
  - AWS CloudWatch (EC2 metrics)
  - Azure Monitor (VM metrics)
  - GCP Cloud Monitoring (Compute Engine metrics)
- **Containers**:
  - Kubernetes metrics (kubectl top, metrics-server)
  - Container monitoring (cAdvisor, Prometheus)
  - Orchestration platform dashboards

**Step 2: Collect Total Capacity**

- **CPU Cores**: Total number of physical or virtual CPU cores
  - Physical server: Physical core count (e.g., 2 sockets × 16 cores = 32 cores)
  - VM: Allocated vCPUs (e.g., 4 vCPUs)
  - Cloud instance: Instance type vCPU count (e.g., m5.xlarge = 4 vCPUs)
  - Container: CPU limit (e.g., 2000m = 2 cores)
- **Memory GB**: Total memory capacity
  - Physical server: Installed RAM (e.g., 128 GB)
  - VM: Allocated memory (e.g., 16 GB)
  - Cloud instance: Instance type memory (e.g., m5.xlarge = 16 GB)
  - Container: Memory limit (e.g., 8 GB)

**Step 3: Collect Current Utilization**

- **CPU Utilization (%)**: Current CPU usage as percentage of total capacity
  - Linux: `top` or `htop` (look at CPU% column)
  - Windows: Task Manager → Performance → CPU
  - Monitoring dashboards: Current CPU% metric
- **Memory Utilization (%)**: Current memory usage as percentage of total capacity
  - Linux: `free -h` (Used / Total × 100)
  - Windows: Task Manager → Performance → Memory
  - Monitoring dashboards: Current Memory% metric

**IMPORTANT: Current utilization should be recent (< 24 hours old) to reflect actual state.**

**Step 4: Collect Peak Utilization (30 days and 90 days)**

- **CPU Peak**: Maximum CPU utilization observed over period
  - Query monitoring system: `max(cpu_utilization) over last 30 days`
  - Example tools:
    - Prometheus: `max_over_time(cpu_percent[30d])`
    - CloudWatch: EC2 CPUUtilization metric, statistic=Maximum, period=30 days
    - Datadog: `max:system.cpu.user{*} over 30d`
- **Memory Peak**: Maximum memory utilization observed over period
  - Query monitoring system: `max(memory_utilization) over last 30 days`

**WHY PEAK MATTERS**: Peak utilization reveals capacity risks that averages hide. A resource averaging 40% CPU but peaking at 95% is at risk during peak load.

**Step 5: Collect Average Utilization (30 days and 90 days)**

- **CPU Average**: Mean CPU utilization over period
  - Query monitoring system: `avg(cpu_utilization) over last 30 days`
- **Memory Average**: Mean memory utilization over period
  - Query monitoring system: `avg(memory_utilization) over last 30 days`

**WHY AVERAGE MATTERS**: Average utilization reveals baseline load and identifies over-provisioned resources (consistently low average = waste).

**Step 6: Assess Threshold Status**

Compare current/peak utilization against policy thresholds (from ISMS-POL-A.8.6, Section 4.1):

**Standard Thresholds** (adjust based on your policy):

- **CPU**: Warning 70%, Critical 85%
- **Memory**: Warning 75%, Critical 90%

| Threshold Status | Definition | Action Required |
|------------------|------------|-----------------|
| **Below Warning** | Utilization < warning threshold (healthy) | Continue monitoring |
| **Warning** | Utilization ≥ warning threshold but < critical | Begin capacity planning, prepare expansion |
| **Critical** | Utilization ≥ critical threshold but < 100% | Immediate action required |
| **Exceeded** | Utilization = 100% (capacity exhausted) | Emergency response |

**Important**: Assess threshold status based on PEAK utilization (30-day or 90-day), not just current or average. A resource peaking at 88% CPU is at Critical status even if average is 40%.

**Step 7: Calculate Capacity Headroom**

**Headroom = Warning Threshold - Current Peak Utilization**

Examples:

- CPU: Warning threshold 70%, current peak 55% → Headroom = 15%
- Memory: Warning threshold 75%, current peak 82% → Headroom = -7% (NEGATIVE = already exceeded warning)

**Negative headroom means resource is already at/above warning threshold and requires immediate planning.**

**Step 8: Document Data Sources**

For audit purposes, note where data came from:

- Monitoring system name (e.g., "Prometheus", "CloudWatch", "Datadog")
- Query or dashboard used
- Date/time of data collection

#### Real-World Examples

**Example 1: Physical Server - Healthy**
| Attribute | Value | Notes |
|-------|-------|-------|
| Resource ID | srv-dc01-rack12-u15 |
| Total CPU Cores | 32 | 2 sockets × 16 cores |
| Total Memory GB | 128 |
| Current CPU % | 42% | Collected 2026-01-15 08:00 |
| Current Memory % | 58% |
| Peak CPU % (30d) | 68% | During nightly backup |
| Peak Memory % (30d) | 72% |
| Peak CPU % (90d) | 71% |
| Peak Memory % (90d) | 75% | Month-end processing |
| Avg CPU % (30d) | 38% |
| Avg Memory % (30d) | 55% |
| Threshold Status (CPU) | Below Warning | 68% < 70% warning |
| Threshold Status (Memory) | Below Warning | 72% < 75% warning |
| CPU Headroom % | +2% | 70% - 68% = 2% |
| Memory Headroom % | +3% | 75% - 72% = 3% |
| Data Source | Prometheus |
| Collection Date | 2026-01-15 |

**Analysis**: Healthy resource. CPU peak (68%) is just below warning (70%), but headroom is minimal (2%). Monitor closely for growth. Memory is healthy with 3% headroom.

**Example 2: VMware VM - Warning Status**
| Attribute | Value | Notes |
|-------|-------|-------|
| Resource ID | web-prod-01 |
| Total CPU Cores | 8 | 8 vCPUs |
| Total Memory GB | 32 |
| Current CPU % | 65% |
| Current Memory % | 78% |
| Peak CPU % (30d) | 88% | **WARNING EXCEEDED** |
| Peak Memory % (30d) | 92% | **CRITICAL EXCEEDED** |
| Peak CPU % (90d) | 91% |
| Peak Memory % (90d) | 94% |
| Avg CPU % (30d) | 52% |
| Avg Memory % (30d) | 68% |
| Threshold Status (CPU) | **Critical** | 88% > 85% critical |
| Threshold Status (Memory) | **Critical** | 92% > 90% critical |
| CPU Headroom % | **-18%** | 70% - 88% = -18% |
| Memory Headroom % | **-17%** | 75% - 92% = -17% |
| Data Source | VMware vCenter |
| Collection Date | 2026-01-15 |

**Analysis**: CRITICAL - Immediate action required. Both CPU and memory exceed critical thresholds during peak load. Averages look acceptable (52%/68%), but peaks reveal severe capacity constraint. Risk of performance degradation or outages during peak times.

**Recommended Actions**:
1. **Immediate**: Review application for optimization opportunities (memory leaks, inefficient queries)
2. **Short-term** (1-2 weeks): Increase VM allocation (12 vCPUs, 48 GB RAM)
3. **Long-term**: Consider application refactoring or horizontal scaling

**Example 3: AWS EC2 - Over-Provisioned**
| Attribute | Value | Notes |
|-------|-------|-------|
| Resource ID | i-0abcd1234efgh5678 |
| Total CPU Cores | 16 | c5.4xlarge |
| Total Memory GB | 32 |
| Current CPU % | 12% |
| Current Memory % | 18% |
| Peak CPU % (30d) | 22% |
| Peak Memory % (30d) | 28% |
| Peak CPU % (90d) | 25% |
| Peak Memory % (90d) | 30% |
| Avg CPU % (30d) | 15% |
| Avg Memory % (30d) | 20% |
| Threshold Status (CPU) | Below Warning |
| Threshold Status (Memory) | Below Warning |
| CPU Headroom % | +48% | Large headroom |
| Memory Headroom % | +47% |
| Data Source | AWS CloudWatch |
| Collection Date | 2026-01-15 |

**Analysis**: OVER-PROVISIONED - Resource is significantly oversized. Peak utilization (22% CPU, 28% memory) is well below warning thresholds. Consider right-sizing to reduce costs.

**Recommended Actions**:
1. **Cost Optimization**: Downsize to c5.xlarge (4 vCPUs, 8 GB RAM) - would still have 50%+ headroom
2. **Estimated Savings**: $200/month (approximate, verify with AWS pricing)
3. **Implementation**: Test in dev/staging first, then production during maintenance window

**Example 4: Kubernetes Node - Trending Toward Critical**
| Attribute | Value | Notes |
|-------|-------|-------|
| Resource ID | k8s-node-prod-worker-03 |
| Total CPU Cores | 64 |
| Total Memory GB | 256 |
| Current CPU % | 72% |
| Current Memory % | 80% |
| Peak CPU % (30d) | 82% | **Trending up** |
| Peak Memory % (30d) | 88% |
| Peak CPU % (90d) | 75% |
| Peak Memory % (90d) | 82% |
| Avg CPU % (30d) | 68% |
| Avg Memory % (30d) | 74% |
| Threshold Status (CPU) | Warning | 82% > 70% but < 85% |
| Threshold Status (Memory) | Warning | 88% > 75% but < 90% |
| CPU Headroom % | -12% |
| Memory Headroom % | -13% |
| Data Source | Prometheus (kube-state-metrics) |
| Collection Date | 2026-01-15 |

**Analysis**: WARNING - Capacity planning required. Resource is trending upward (90-day peak: 75% CPU → 30-day peak: 82% CPU). At current growth rate, will hit critical within 1-2 months.

**Recommended Actions**:
1. **Immediate**: Review pod resource requests/limits (are they accurate?)
2. **Short-term** (2-4 weeks): Add capacity (add node to cluster OR increase node size)
3. **Monitor**: Weekly capacity reviews until remediation complete

#### Evidence to Collect

- **Monitoring dashboard screenshots** showing:
  - Current CPU and memory utilization
  - 30-day CPU and memory trends
  - Peak utilization markers
- **Metric export files** (CSV or JSON):
  - CPU utilization time series (30-90 days)
  - Memory utilization time series (30-90 days)
- **Hypervisor performance data**:
  - VMware: vCenter performance charts
  - Hyper-V: Hyper-V Manager performance screenshots
- **Cloud monitoring data**:
  - AWS CloudWatch: EC2 metrics export
  - Azure Monitor: VM metrics export
  - GCP Cloud Monitoring: Compute Engine metrics export

**Evidence Naming Convention:**
```
Sheet2-Evidence-[ResourceID]-[Metric]-[Date].extension

Examples:
Sheet2-Evidence-web-prod-01-CPU-Utilization-2026-01-15.png
Sheet2-Evidence-web-prod-01-Memory-Utilization-2026-01-15.csv
Sheet2-Evidence-srv-dc01-Performance-Dashboard-2026-01-15.png
```

#### Quality Checklist

- [ ] All compute resources from Sheet 1 included
- [ ] Total capacity documented (CPU cores, memory GB)
- [ ] Current utilization is recent (< 24 hours old)
- [ ] Peak utilization calculated correctly (max over period, not average of peaks)
- [ ] Average utilization calculated correctly (mean over period)
- [ ] Both 30-day and 90-day data collected (if available)
- [ ] Threshold status assessed based on PEAK (not current or average)
- [ ] Capacity headroom calculated (warning threshold minus peak utilization)
- [ ] Negative headroom flagged for immediate action
- [ ] Evidence collected for all critical resources
- [ ] Evidence collected for all at-risk resources (warning/critical status)
- [ ] Data sources documented (monitoring system name)
- [ ] Collection date/time documented
- [ ] Formulas verified (% calculations, threshold logic)

---

### Sheet 3: Storage Capacity

#### Purpose

Document current disk space and storage utilization for all storage resources. Storage capacity exhaustion can cause application failures, data loss, and service outages.

#### What to Document

For EACH storage resource:

- **Resource ID** (from Sheet 1)
- **Storage Type**: Disk, Volume, File System, Database, Object Storage, Backup Storage
- **Total Capacity**: Total storage space (GB or TB)
- **Used Space**: Currently used space (GB or TB)
- **Free Space**: Available space (GB or TB)
- **Utilization**: Percentage used (%)
- **Peak Utilization** (30 days): Maximum % used over period
- **Peak Utilization** (90 days): Maximum % used over period
- **Average Utilization** (30 days): Mean % used over period
- **Average Utilization** (90 days): Mean % used over period
- **Growth Rate**: GB or TB per month (if calculable)
- **IOPS Utilization**: If applicable (% of maximum IOPS)
- **Throughput Utilization**: If applicable (% of maximum throughput)
- **Threshold Status**: Below Warning / Warning / Critical / Exceeded
- **Capacity Headroom**: % remaining before warning threshold
- **Estimated Exhaustion Date**: When storage will hit 100% (if trending)

#### Common Mistakes to Avoid

❌ **Only checking OS disk** - Forgetting data volumes, databases, backups  
❌ **Ignoring database storage growth** - Transaction logs growing unchecked  
❌ **Not monitoring backup storage** - Backups filling up, failing  
❌ **Missing cloud storage** - S3 buckets, Azure Blob storage  
❌ **Not calculating growth rate** - Missing predictable exhaustion  
❌ **Ignoring IOPS/throughput limits** - Space available but IOPS exhausted  
❌ **Assuming "unlimited" cloud storage** - Cost controls, quotas still apply  

#### How to Complete

**Step 1: Identify All Storage Resources**

- **Local Disks/Volumes**:
  - Operating system volumes (C:, /, /boot, etc.)
  - Data volumes (/data, D:, /var, /opt, etc.)
  - Swap/page files
- **SAN/NAS Storage**:
  - LUNs (Logical Unit Numbers)
  - NFS shares
  - CIFS/SMB shares
- **Cloud Block Storage**:
  - AWS EBS volumes
  - Azure Managed Disks
  - GCP Persistent Disks
- **Cloud Object Storage**:
  - AWS S3 buckets
  - Azure Blob Storage containers
  - GCP Cloud Storage buckets
- **Database Storage**:
  - Database data files
  - Transaction logs
  - Temp databases
- **Backup Storage**:
  - Backup repositories
  - Archive storage
  - Snapshot storage

**Step 2: Collect Storage Capacity Data**

**For Local Disks/Volumes**:

- Linux: `df -h` (shows used, available, %)
- Windows: `Get-PSDrive` or Disk Management
- Monitoring tools: Disk space metrics

**For SAN/NAS Storage**:

- Storage management console (NetApp OnCommand, Dell EMC Unisphere, etc.)
- Monitoring integration with SAN/NAS

**For Cloud Block Storage**:

- AWS CloudWatch: EBS volume metrics
- Azure Monitor: Disk metrics
- GCP Cloud Monitoring: Persistent Disk metrics

**For Cloud Object Storage**:

- AWS S3: Bucket metrics (S3 Storage Lens, CloudWatch)
- Azure: Storage Account metrics
- GCP: Cloud Storage metrics

**For Database Storage**:

- Database-specific commands:
  - MySQL: `SELECT table_schema, SUM(data_length + index_length) / 1024 / 1024 AS size_mb FROM information_schema.tables GROUP BY table_schema;`
  - PostgreSQL: `SELECT pg_size_pretty(pg_database_size('database_name'));`
  - SQL Server: `sp_spaceused`
  - Oracle: `SELECT tablespace_name, SUM(bytes)/1024/1024/1024 AS size_gb FROM dba_data_files GROUP BY tablespace_name;`

**For Backup Storage**:

- Backup software console (Veeam, Commvault, AWS Backup, Azure Backup, etc.)
- Check backup repository utilization

**Step 3: Calculate Utilization**

**Utilization (%) = (Used Space / Total Capacity) × 100**

Example:

- Total Capacity: 1000 GB
- Used Space: 750 GB
- Free Space: 250 GB
- Utilization: 75%

**Step 4: Collect Peak Utilization (30 days and 90 days)**

Storage typically grows over time, so peak utilization = most recent maximum.

Query monitoring system for maximum storage utilization over period:

- Prometheus: `max_over_time(disk_used_percent[30d])`
- CloudWatch: EBS VolumeUtilization, statistic=Maximum, period=30 days

**Step 5: Calculate Growth Rate**

If historical data is available, calculate monthly growth:

**Growth Rate (GB/month) = (Current Used - Used 30 Days Ago) / 1 month**

Example:

- Current: 750 GB
- 30 days ago: 700 GB
- Growth Rate: (750 - 700) / 1 = 50 GB/month

**This is critical for forecasting storage exhaustion.**

**Step 6: Estimate Exhaustion Date (If Trending)**

If growth rate is predictable:

**Months Until Exhaustion = (Total Capacity - Current Used) / Growth Rate**

Example:

- Total Capacity: 1000 GB
- Current Used: 750 GB
- Growth Rate: 50 GB/month
- Free Space: 250 GB
- Months Until Exhaustion: 250 / 50 = 5 months
- Estimated Exhaustion: Current Date + 5 months = June 2026

**This helps prioritize storage expansion planning.**

**Step 7: Check IOPS and Throughput Limits (If Applicable)**

Storage capacity (GB) is not the only constraint. IOPS (Input/Output Operations Per Second) and throughput (MB/s) can also be limiting factors.

**For Cloud Block Storage** (AWS EBS, Azure Disks):

- Check IOPS limits (e.g., AWS gp3: 3000 baseline IOPS)
- Check throughput limits (e.g., AWS gp3: 125 MB/s baseline)
- Monitor current IOPS and throughput utilization vs. limits

**For SAN/NAS**:

- Check storage array IOPS limits
- Monitor current IOPS utilization

**Step 8: Assess Threshold Status**

Compare utilization against policy thresholds (from ISMS-POL-A.8.6, Section 4.1):

**Standard Thresholds** (adjust based on your policy):

- **Disk Space**: Warning 75%, Critical 85%

**IMPORTANT**: Some applications require lower thresholds:

- **Databases**: Warning 70%, Critical 80% (to prevent transaction log issues)
- **Log volumes**: Warning 70%, Critical 80% (logs grow quickly)
- **Backup storage**: Warning 75%, Critical 85%

| Threshold Status | Definition | Action Required |
|------------------|------------|-----------------|
| **Below Warning** | Utilization < warning threshold | Continue monitoring |
| **Warning** | Utilization ≥ warning threshold but < critical | Plan storage expansion |
| **Critical** | Utilization ≥ critical threshold but < 100% | Immediate expansion or cleanup |
| **Exceeded** | Utilization = 100% (storage full) | Emergency response, application failure imminent |

**Step 9: Calculate Capacity Headroom**

**Headroom = Warning Threshold - Current Utilization**

Example:

- Warning threshold: 75%
- Current utilization: 68%
- Headroom: 7% (= 7% of total capacity remaining before warning)

**Negative headroom means already at/above warning.**

#### Real-World Examples

**Example 1: SAN Volume - Healthy with Growth Trending**
| Attribute | Value | Notes |
|-------|-------|-------|
| Resource ID | vol-data-prod-db-01 |
| Storage Type | SAN Volume (LUN) |
| Total Capacity GB | 2000 |
| Used Space GB | 1350 |
| Free Space GB | 650 |
| Utilization % | 68% | Calculated: 1350/2000 |
| Peak Util % (30d) | 70% |
| Peak Util % (90d) | 65% | Growing trend |
| Avg Util % (30d) | 67% |
| Growth Rate GB/mo | 50 | Measured from historical data |
| IOPS Utilization % | 45% | Well below limit |
| Throughput Util % | 38% |
| Threshold Status | Below Warning | 70% < 75% warning |
| Headroom % | +5% | 75% - 70% = 5% |
| Months to Exhaustion | 13 | (650 GB free / 50 GB/mo) |
| Data Source | NetApp OnCommand |
| Collection Date | 2026-01-15 |

**Analysis**: Currently healthy (below warning), but limited headroom (5%). Growing at 50 GB/month means will reach warning threshold (75% = 1500 GB) in ~3 months (150 GB growth needed / 50 GB/mo). Plan storage expansion now to avoid reactive scramble.

**Recommended Actions**:
1. **Planning** (now): Procurement approval for +1TB expansion
2. **Implementation** (Q2 2026): Expand volume to 3TB (provides 18 months headroom at current growth rate)
3. **Monitor**: Monthly growth rate validation

**Example 2: Database Transaction Log - CRITICAL**
| Attribute | Value | Notes |
|-------|-------|-------|
| Resource ID | db-prod-01-tlog |
| Storage Type | Database Transaction Log |
| Total Capacity GB | 500 |
| Used Space GB | 465 |
| Free Space GB | 35 |
| Utilization % | 93% | **CRITICAL** |
| Peak Util % (30d) | 95% | **EXCEEDED CRITICAL** |
| Peak Util % (90d) | 92% |
| Avg Util % (30d) | 89% |
| Growth Rate GB/mo | 75 | **RAPID GROWTH** |
| Threshold Status | **Exceeded** | 95% > 85% critical |
| Headroom % | **-20%** | 75% - 95% = -20% |
| Months to Exhaustion | **0.5** | 35 GB / 75 GB/mo = 0.5 months |
| Data Source | SQL Server Management Studio |
| Collection Date | 2026-01-15 |

**Analysis**: EMERGENCY - Transaction log will fill within 2 weeks at current growth rate. When transaction log fills, database stops accepting writes = application outage.

**Immediate Actions Required**:
1. **IMMEDIATE** (today): Increase transaction log size to 1TB
2. **URGENT** (this week): Investigate why transaction log is growing so fast:

   - Long-running transactions not committing?
   - Log backup frequency insufficient?
   - Massive data loads?

3. **SHORT-TERM** (2 weeks): Implement transaction log monitoring alert (>80% = page on-call)
4. **LONG-TERM**: Review database maintenance practices

**Example 3: AWS S3 Bucket - Cost Concern**
| Attribute | Value | Notes |
|-------|-------|-------|
| Resource ID | s3-prod-customer-uploads |
| Storage Type | Object Storage (S3) |
| Total Capacity GB | Unlimited (S3) | No hard limit, but cost concern |
| Used Space GB | 85000 | 85 TB |
| Free Space GB | N/A |
| Utilization % | N/A | No fixed capacity |
| Peak Util % (30d) | N/A |
| Growth Rate GB/mo | 2500 | 2.5 TB/month |
| Threshold Status | N/A | Cost-based threshold instead |
| Monthly Cost | $1,955 | 85TB × $0.023/GB (S3 Standard) |
| Projected Cost (12mo) | $3,545 | (85TB + 30TB growth) × $0.023 |
| Data Source | AWS S3 Storage Lens |
| Collection Date | 2026-01-15 |

**Analysis**: No capacity constraint (S3 is "unlimited"), but COST concern. Growing 2.5TB/month = +$57.50/month cost increase. In 12 months, will add ~$690/month to cloud bill.

**Recommended Actions**:
1. **Lifecycle Policy**: Move files >90 days old to S3 Glacier (saves 80% on storage costs)
2. **Compression**: Compress uploads before storage (if not already compressed)
3. **Retention Policy**: Define and enforce data retention (delete old uploads if business allows)
4. **Estimated Savings**: $1,200-1,500/month with lifecycle policy

**Example 4: Backup Storage - Approaching Limit**
| Attribute | Value | Notes |
|-------|-------|-------|
| Resource ID | backup-repo-prod |
| Storage Type | Backup Repository |
| Total Capacity GB | 50000 | 50 TB |
| Used Space GB | 42500 | 42.5 TB |
| Free Space GB | 7500 | 7.5 TB |
| Utilization % | 85% | **AT CRITICAL THRESHOLD** |
| Peak Util % (30d) | 86% |
| Peak Util % (90d) | 82% |
| Avg Util % (30d) | 84% |
| Growth Rate GB/mo | 1250 | 1.25 TB/month |
| Threshold Status | **Critical** | 86% > 85% critical |
| Headroom % | **-11%** | 75% - 86% = -11% |
| Months to Exhaustion | **6** | 7500 GB / 1250 GB/mo |
| Data Source | Veeam Backup & Replication |
| Collection Date | 2026-01-15 |

**Analysis**: CRITICAL - Backup storage at critical threshold. 6 months until exhaustion, but backup failures will start before then (backups need working space). Must act now.

**Recommended Actions**:
1. **IMMEDIATE** (2 weeks): Review backup retention policy

   - Current: 90-day retention
   - Reduce to 60 days? (saves ~10TB)

2. **SHORT-TERM** (4-6 weeks): Add +20TB storage capacity
3. **MEDIUM-TERM**: Implement backup compression (if not already enabled)
4. **LONG-TERM**: Migrate old backups to cheaper tier storage (tape, cloud glacier)

#### Evidence to Collect

- **Storage dashboard screenshots** showing current utilization
- **Metric export files** with historical storage data (30-90 days)
- **Growth trend graphs** showing storage consumption over time
- **Database storage reports** (if applicable):
  - Database size query results
  - Transaction log size
  - Table/index sizes
- **Cloud storage billing reports** (for cloud storage):
  - S3 Storage Lens reports
  - Azure Storage Analytics
  - GCP Cloud Storage usage reports
- **Storage array management console** screenshots (for SAN/NAS):
  - Volume utilization
  - IOPS graphs
  - Throughput graphs

**Evidence Naming Convention:**
```
Sheet3-Evidence-[ResourceID]-[Metric]-[Date].extension

Examples:
Sheet3-Evidence-vol-data-prod-db-01-Utilization-2026-01-15.png
Sheet3-Evidence-vol-data-prod-db-01-Growth-Trend-2026-01-15.png
Sheet3-Evidence-s3-prod-uploads-Storage-Report-2026-01-15.pdf
```

#### Quality Checklist

- [ ] All storage resources from Sheet 1 included
- [ ] Total capacity documented accurately
- [ ] Current utilization is recent (< 24 hours for on-prem, < 1 week for cloud)
- [ ] Peak utilization over 30/90 days calculated
- [ ] Growth rate calculated (GB/month or TB/month) from historical data
- [ ] Estimated exhaustion date calculated for resources with positive growth
- [ ] IOPS/throughput limits checked (if applicable)
- [ ] Database storage included (data files, transaction logs, tempdb)
- [ ] Backup storage included
- [ ] Cloud storage included (if applicable) with cost analysis
- [ ] Threshold status assessed based on peak utilization
- [ ] Capacity headroom calculated
- [ ] Evidence collected for all critical resources
- [ ] Evidence collected for all at-risk resources (warning/critical status)
- [ ] Data sources documented
- [ ] Collection dates documented

 capacity is healthy

- Reality: CPU peaks at 95% daily during backups → Critical capacity risk
- Memory averages 60% → assume safe
- Reality: Memory peaks at 98% during month-end processing → Risk of crashes

**Why It Happens:**

- Average metrics are easier to understand
- Dashboards often show averages by default
- Not aware of daily/weekly/monthly usage patterns
- Monitoring tools default to showing current, not peak

**How to Avoid:**

- ALWAYS collect peak utilization (30-day and 90-day maximum)
- Review utilization graphs to see patterns
- Identify peak times (daily backups, month-end processing, business hours)
- Assess threshold status based on PEAK, not average
- Configure monitoring dashboards to show max/peak prominently

**Impact of Not Fixing:**

- Capacity exhaustion during peak times
- Service degradation or outages during critical business periods
- Inaccurate capacity planning (planning for average, not peak)

### Pitfall 5: Missing Cloud Resources

**Mistake:** Forgetting cloud infrastructure in capacity assessment

**Examples:**

- EC2 instances, Azure VMs, GCP Compute Engine instances not inventoried
- Cloud storage (S3, Azure Blob, GCP Cloud Storage) not monitored
- Serverless functions (Lambda, Azure Functions, Cloud Functions) not assessed
- Cloud database instances (RDS, Azure SQL, Cloud SQL) not tracked

**Why It Happens:**

- Different teams manage cloud vs. on-premises
- Cloud resources not in traditional asset inventory
- Assumption that "cloud is infinite capacity"
- Cloud accounts not centrally managed

**How to Avoid:**

- Review cloud console for ALL resources (compute, storage, network, database, serverless)
- Include cloud operations team in assessment
- Check cloud billing reports (resources using cost = resources to monitor)
- Recognize that cloud has limits too (service quotas, cost controls)

**Impact of Not Fixing:**

- Cloud cost surprises (unexpected scaling)
- Hitting cloud service quotas
- Incomplete capacity visibility

### Pitfall 6: Not Documenting Monitoring Gaps

**Mistake:** Knowing resources are unmonitored but not documenting gaps or remediation plans

**Examples:**

- "We know server XYZ isn't monitored, we'll get to it someday"
- No documentation of WHY unmonitored
- No plan to close monitoring gap
- No prioritization of gaps

**Why It Happens:**

- Embarrassment about gaps
- Assuming documenting gap makes it worse
- No budget/resources to close gap
- Lack of accountability

**How to Avoid:**

- Document ALL gaps honestly (Sheet 7)
- For each gap, document reason (technical limitation, cost, deprioritized)
- Create remediation plan even if "accept risk" (document acceptance)
- Prioritize gaps by risk and business impact
- Assign owners and target dates

**Impact of Not Fixing:**

- Gaps never get closed
- Audit finding (monitoring not comprehensive)
- Capacity risks on unmonitored resources

### Pitfall 7: Treating Warnings as Acceptable

**Mistake:** Resources at Warning threshold treated as "good enough"

**Examples:**

- Resource at 72% utilization (warning threshold 70%) → "Close enough, no action needed"
- Resource at 78% → "It's not Critical yet, we'll wait"

**Why It Happens:**

- Misunderstanding purpose of warning threshold
- "If it's not Critical, it's okay"
- Reactionary mindset (act only when critical)

**How to Avoid:**

- Understand warning threshold purpose: PLAN CAPACITY EXPANSION NOW
- Warning means "start planning", not "wait and see"
- Create capacity expansion plan for ALL resources at Warning
- Target: <5% of resources at Warning (per policy objective)

**Impact of Not Fixing:**

- Warning becomes Critical before action taken
- Critical becomes Exceeded (capacity exhaustion)
- Reactive capacity management (always firefighting)

### Pitfall 8: No Remediation Follow-Through

**Mistake:** Identifying capacity gaps but never fixing them

**Examples:**

- Assessment Q1 2026: "Gap: Database storage at 82%"
- Assessment Q2 2026: Same gap, still 82%
- Assessment Q3 2026: Now at 89% (getting worse)
- Assessment Q4 2026: Capacity exhausted, outage

**Why It Happens:**

- No ownership assigned ("someone should fix this")
- No budget allocated
- Competing priorities (capacity planning is not urgent until it is)
- Assessment fatigue (endless gap lists, no action)

**How to Avoid:**

- Assign owner to EVERY gap
- Set target date for EVERY remediation
- Get management commitment and budget
- Track progress in monthly capacity reviews
- Escalate stalled remediations to management

**Impact of Not Fixing:**

- Capacity-related outages
- Business impact
- Audit finding (identified gaps not remediated)

### Pitfall 9: Not Calculating Growth Rates

**Mistake:** Not tracking how fast capacity is being consumed

**Examples:**

- Storage at 70% today → "Safe, below critical"
- Growing 5% per month → Will hit critical in 3 months
- No awareness of growth rate

**Why It Happens:**

- Focusing on current state, not trend
- Not collecting historical data
- Manual assessment (hard to calculate trends)

**How to Avoid:**

- Collect 30-day and 90-day historical data
- Calculate growth rates (GB/month, %/month)
- Estimate capacity exhaustion date: Months Until Exhaustion = (Free Space / Growth Rate)
- Prioritize remediations by how soon capacity will exhaust

**Impact of Not Fixing:**

- Surprise capacity exhaustion
- Insufficient lead time for procurement/provisioning
- Emergency capacity additions (expensive)

### Pitfall 10: Siloed Assessment

**Mistake:** Completing assessment in isolation without input from other teams

**Examples:**

- Infrastructure team completes assessment alone
- Cloud operations team not consulted (they manage cloud resources)
- Application teams not involved (they know application capacity limits)
- Network team not involved (they manage network capacity)

**Why It Happens:**

- Assuming one team knows everything
- Not knowing who else manages capacity
- Time pressure

**How to Avoid:**

- Identify ALL stakeholders upfront (infrastructure, cloud, network, application, database, monitoring)
- Schedule collaboration sessions
- Review drafts with all teams
- Three-level approval ensures cross-team review

**Impact of Not Fixing:**

- Incomplete assessment (missing resources, missing data)
- Inaccurate capacity understanding
- Gaps discovered during audit

---

## Quality Checklist

Use this checklist to verify assessment completeness and quality before submitting for review.

### Overall Completeness

- [ ] All 9 sheets completed (no empty sheets)
- [ ] All required fields filled (no "TBD" or "Unknown" without justification)
- [ ] Assessment date is current (within last 30 days)
- [ ] Assessment covers all environments (Production, UAT, Development, DR)
- [ ] Assessment covers all resource types (Compute, Storage, Network, Application)

### Sheet 1: Resource Inventory

- [ ] All production resources documented
- [ ] Non-production resources documented
- [ ] Cloud resources included (if applicable)
- [ ] Virtual and container resources included
- [ ] Resource types correctly categorized
- [ ] Environment classification accurate
- [ ] Criticality assigned based on business impact
- [ ] Monitoring status verified (not assumed)
- [ ] Business and technical owners identified
- [ ] No "TBD" or "Unknown" values without justification
- [ ] Evidence collected and registered

### Sheet 2: Compute Capacity

- [ ] All compute resources from Sheet 1 included
- [ ] Total capacity documented (CPU cores, memory GB)
- [ ] Current utilization is recent (< 24 hours old)
- [ ] Peak utilization calculated correctly (max over 30/90 days)
- [ ] Average utilization calculated correctly (mean over 30/90 days)
- [ ] Both 30-day and 90-day data collected (if available)
- [ ] Threshold status assessed based on peak (not average)
- [ ] Capacity headroom calculated
- [ ] Negative headroom flagged for action
- [ ] Evidence collected for critical resources
- [ ] Data sources documented

### Sheet 3: Storage Capacity

- [ ] All storage resources from Sheet 1 included
- [ ] Total capacity documented accurately
- [ ] Current utilization is recent (< 24 hours)
- [ ] Peak utilization over 30/90 days calculated
- [ ] Growth rate calculated (GB/month or TB/month)
- [ ] Estimated exhaustion date calculated (if trending)
- [ ] IOPS/throughput limits checked (if applicable)
- [ ] Database storage included
- [ ] Backup storage included
- [ ] Cloud storage included (if applicable)
- [ ] Threshold status assessed
- [ ] Capacity headroom calculated
- [ ] Evidence collected

### Sheet 4: Network Capacity

- [ ] All network resources from Sheet 1 included
- [ ] Interface speeds documented accurately
- [ ] Current utilization is recent
- [ ] Peak utilization over 30/90 days calculated
- [ ] Both inbound and outbound utilization checked
- [ ] Packet rate limits checked (if applicable)
- [ ] Error rates and dropped packets reviewed
- [ ] Threshold status assessed
- [ ] Capacity headroom calculated
- [ ] Evidence collected

### Sheet 5: Application Capacity

- [ ] All critical applications from Sheet 1 included
- [ ] Capacity limits documented (licensed, architectural, configured)
- [ ] Current utilization is recent
- [ ] Peak utilization over 30/90 days calculated
- [ ] License compliance verified (if applicable)
- [ ] Threshold status assessed
- [ ] Capacity headroom calculated
- [ ] Evidence collected

### Sheet 6: Threshold Status Summary

- [ ] All resources from Sheets 2-5 summarized
- [ ] Threshold status counts accurate
- [ ] Percentages calculated correctly
- [ ] Breakdown by resource type included
- [ ] Breakdown by environment included
- [ ] Breakdown by criticality included
- [ ] Top at-risk resources identified
- [ ] Overall capacity health score calculated
- [ ] Comparison to policy objective (95%) included

### Sheet 7: Monitoring Coverage Assessment

- [ ] All resources from Sheet 1 assessed
- [ ] Monitoring status verified (not assumed)
- [ ] Monitoring tools documented
- [ ] Metrics collected listed
- [ ] Metrics missing identified
- [ ] Data retention verified against policy requirements
- [ ] Alerting configuration verified
- [ ] Data quality assessed
- [ ] Gap reasons documented
- [ ] Remediation plans created for all gaps
- [ ] Remediation owners assigned
- [ ] Target dates set
- [ ] Gaps prioritized by risk

### Sheet 8: At-Risk Resources & Remediation

- [ ] All at-risk resources from Sheets 2-5 included
- [ ] Resources prioritized by risk
- [ ] Business impact assessed for each resource
- [ ] Root cause identified
- [ ] Multiple solution options evaluated
- [ ] Recommended solution selected with justification
- [ ] Cost estimates documented
- [ ] Lead time estimates realistic
- [ ] Owners assigned
- [ ] Target dates set and reasonable
- [ ] Status tracking implemented

### Sheet 9: Evidence Registry

- [ ] All evidence collected during assessment listed
- [ ] Evidence organized by category (folder structure)
- [ ] Evidence IDs assigned systematically
- [ ] Metadata documented (description, source, date, location)
- [ ] Sensitive data sanitized
- [ ] Audit tags applied
- [ ] Evidence accessibility verified
- [ ] Retention periods documented
- [ ] No orphaned evidence (evidence not linked to assessment)
- [ ] Evidence is recent (< 30 days for current assessments)

### Data Quality

- [ ] All utilization data is current (< 24-48 hours old for "current" metrics)
- [ ] Historical data covers adequate period (30 days minimum, 90 days preferred)
- [ ] Peak utilization represents true maximums (not averages)
- [ ] Threshold comparisons are accurate
- [ ] Calculations verified (utilization %, headroom %, growth rates)
- [ ] No obvious data errors (e.g., >100% utilization, negative headroom without explanation)

### Evidence Quality

- [ ] Evidence is recent (< 30 days old)
- [ ] Screenshots are clear and readable
- [ ] Metric exports are complete (no truncated data)
- [ ] Sensitive data sanitized
- [ ] Evidence properly stored and accessible
- [ ] Evidence metadata documented

### Policy Compliance

- [ ] Assessment scope aligns with policy (ISMS-POL-A.8.6, Section 1.3)
- [ ] Resource types monitored per policy (ISMS-POL-A.8.6, Section 2)
- [ ] Thresholds applied per policy (ISMS-POL-A.8.6, Section 4.1)
- [ ] Monitoring coverage meets policy requirements (ISMS-POL-A.8.6, Section 3.1)
- [ ] Capacity health score calculated and compared to policy objective (95%)

### Review & Approval Readiness

- [ ] Self-review completed (this checklist)
- [ ] All known gaps documented honestly
- [ ] Remediation plans created for all gaps
- [ ] Assessment ready for technical review
- [ ] Evidence ready for audit

---

## Review & Approval

### Three-Level Approval Process

This assessment requires three levels of review and approval to ensure quality, accuracy, and management buy-in.

#### Level 1: Self-Review (Completer)

**Objective:** Ensure assessment is complete and accurate before submitting for technical review

**Reviewer:** Person(s) who completed the assessment

**Steps:**
1. Run through Quality Checklist (above) - check every box
2. Verify all sheets are complete (no empty sections)
3. Verify data accuracy:

   - Spot-check utilization metrics against monitoring dashboards
   - Verify calculations (percentages, headroom, growth rates)
   - Cross-reference resource inventory with asset inventory/CMDB

4. Validate evidence:

   - Verify all evidence is collected
   - Check evidence is recent (< 30 days)
   - Verify evidence is stored in accessible location

5. Review at-risk resources and remediation plans:

   - Are all at-risk resources identified?
   - Are remediation plans actionable and realistic?
   - Are owners assigned and target dates set?

6. Check for consistency:

   - Resource IDs consistent across sheets
   - No contradictions between sheets
   - Terminology consistent with policy

**Approval Criteria:**

- ✅ Quality checklist 100% complete
- ✅ No obvious errors or gaps
- ✅ Evidence collected and accessible
- ✅ Ready for technical review

**Output:** Self-review sign-off, forward to Level 2 reviewer

#### Level 2: Technical Review (Infrastructure/Operations Manager)

**Objective:** Verify technical accuracy and completeness

**Reviewer:** Infrastructure Manager, IT Operations Manager, or Capacity Planning Manager

**Steps:**
1. Review resource inventory (Sheet 1):

   - Is inventory complete? Any missing resources?
   - Are resource types correctly categorized?
   - Is criticality assignment reasonable?

2. Review utilization data (Sheets 2-5):

   - Spot-check utilization metrics against monitoring systems
   - Verify peak utilization calculations
   - Check threshold assessments are accurate

3. Review monitoring coverage (Sheet 7):

   - Are monitoring gaps accurately identified?
   - Are gap reasons valid?
   - Are remediation plans feasible?

4. Review at-risk resources (Sheet 8):

   - Are business impacts accurately assessed?
   - Are root causes correct?
   - Are recommended solutions appropriate?
   - Are cost estimates and lead times realistic?

5. Review evidence (Sheet 9):

   - Spot-check evidence quality
   - Verify evidence supports claims in assessment

6. Provide feedback:

   - Request corrections if needed
   - Request additional evidence if needed
   - Request clarification if needed

**Approval Criteria:**

- ✅ Technical accuracy verified
- ✅ Resource inventory complete
- ✅ Utilization data accurate
- ✅ Monitoring gaps correctly identified
- ✅ Remediation plans are feasible
- ✅ Evidence quality acceptable

**Output:** Technical review sign-off (with any required corrections), forward to Level 3 reviewer

#### Level 3: Management Review (CIO/IT Director or Delegate)

**Objective:** Review capacity risks, approve remediation plans, allocate resources

**Reviewer:** CIO, IT Director, or delegated senior manager

**Steps:**
1. Review executive summary:

   - Overall capacity health score
   - Number of resources at Warning/Critical
   - Top at-risk resources
   - Key capacity risks

2. Review at-risk resources and remediation plans (Sheet 8):

   - Understand business impact of capacity risks
   - Review recommended solutions and cost estimates
   - Assess budget implications
   - Prioritize remediations by risk and cost

3. Approve remediation plans:

   - Approve budget for capacity expansions
   - Assign accountability for remediation execution
   - Set expectations for remediation timelines

4. Address policy compliance:

   - If capacity health score < 95%, understand gap and approve remediation plan to meet target
   - If monitoring coverage < 100% production resources, approve monitoring expansion plan

5. Provide strategic input:

   - Align capacity planning with business growth plans
   - Approve capacity planning budget for next fiscal year

**Approval Criteria:**

- ✅ Capacity risks understood
- ✅ Remediation plans approved
- ✅ Budget allocated for critical remediations
- ✅ Accountability assigned
- ✅ Policy compliance gaps addressed

**Output:** Final approval, assessment is complete and approved

### Approval Workflow

```
Assessment Completed
        ↓
[Level 1: Self-Review]
        ↓
   Corrections Needed? → Yes → Return to Completer
        ↓ No
[Level 2: Technical Review]
        ↓
   Corrections Needed? → Yes → Return to Completer
        ↓ No
[Level 3: Management Review]
        ↓
   Additional Budget/Resources Needed? → Discuss with Finance/CIO
        ↓
[Final Approval]
        ↓
Assessment Archived & Used for Forecasting (A.8.6.2) and Dashboard (A.8.6.3)
```

### Approval Documentation

Document approvals in the workbook:

- **Self-Review**: Name, Date, Signature
- **Technical Review**: Name, Title, Date, Signature, Comments
- **Management Review**: Name, Title, Date, Signature, Approved Budget (if applicable), Comments

### Post-Approval Actions

Once assessment is approved:
1. **Archive assessment** in ISMS documentation repository
2. **Share with stakeholders** (capacity planning team, infrastructure teams, management)
3. **Use as input for forecasting** (ISMS-IMP-A.8.6.2 - Capacity Forecasting & Planning)
4. **Track remediation progress** (monthly capacity reviews)
5. **Schedule next assessment** (monthly update cycle)

---


**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
