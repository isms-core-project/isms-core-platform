**ISMS-IMP-A.8.6.1 - Capacity Utilization Assessment**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.6: Capacity Management

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.6.1 |
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

This document consists of two parts:

- **PART I: USER COMPLETION GUIDE**
  - Assessment Overview
  - Prerequisites
  - Workflow
  - Completing Each Sheet
  - Evidence Collection
  - Common Pitfalls
  - Quality Checklist
  - Review & Approval

- **PART II: TECHNICAL SPECIFICATION**
  - Excel Workbook Structure
  - Sheet-by-Sheet Specifications
  - Cell Styling Reference
  - Integration Points

---

# PART I: USER COMPLETION GUIDE

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

# PART II: TECHNICAL SPECIFICATION

This part provides detailed technical specifications for the Excel workbook structure, formulas, and styling.

## Excel Workbook Structure

### Workbook Overview

**Filename:** `ISMS-A.8.6.1-Capacity-Utilization-Assessment-YYYY-MM.xlsx`

**Number of Sheets:** 10 sheets

**Sheet List:**
1. Instructions & Legend
2. Compute_Resources
3. Storage_Resources
4. Network_Resources
5. Application_Resources
6. Cloud_Resources
7. Threshold_Summary
8. Coverage_Analysis
9. Evidence_Register
10. Approval_Sign_Off

### Sheet Dependencies

```
Sheet 1 (Resource Inventory)
    ↓ (provides resource list)
├── Sheet 2 (Compute Capacity)
├── Sheet 3 (Storage Capacity)
├── Sheet 4 (Network Capacity)
└── Sheet 5 (Application Capacity)
    ↓ (all feed into)
Sheet 6 (Threshold Status Summary)
    ↓
Sheet 7 (Monitoring Coverage Assessment)
    ↓
Sheet 8 (At-Risk Resources & Remediation)
    ↓
Sheet 9 (Evidence Registry)
    ↓ (all feed into)
Summary Dashboard
```

---

## Sheet-by-Sheet Specifications

### Summary Dashboard

**Purpose:** Executive-level overview of capacity status

**Layout:**

| Section | Contents |
|---------|----------|
| **Header** | Assessment metadata (date, period covered, reviewer) |
| **KPIs** | Key metrics (capacity health score, resources at warning/critical, etc.) |
| **Charts** | Visual charts (capacity status distribution, breakdown by type/environment) |
| **Top Risks** | List of top 10 at-risk resources |
| **Actions** | Summary of remediation actions required |

**Columns:**

| Column | Header | Data Type | Formula/Source |
|--------|--------|-----------|----------------|
| A | Metric Name | Text | Manual |
| B | Value | Number/Text | Formula (references other sheets) |
| C | Target | Number/Text | Policy targets |
| D | Status | Text | Conditional (Green/Yellow/Red based on B vs C) |

**Key Formulas:**

```excel
# Capacity Health Score
=COUNTIF(Sheet6!D:D,"Below Warning")/COUNTA(Sheet6!D:D)*100

# Resources at Warning
=COUNTIF(Sheet6!D:D,"Warning")

# Resources at Critical
=COUNTIF(Sheet6!D:D,"Critical")

# Resources Exceeded
=COUNTIF(Sheet6!D:D,"Exceeded")
```

**Charts:**
1. Pie chart: Capacity status distribution (Below Warning, Warning, Critical, Exceeded)
2. Bar chart: Resources by threshold status, broken down by type (Compute, Storage, Network, Application)
3. Bar chart: Top 10 at-risk resources by utilization %

**Conditional Formatting:**

- Status column: Green if ≥95%, Yellow if 90-95%, Red if <90%

---

### Sheet 1: Resource Inventory

**Purpose:** Master list of all infrastructure resources

**Columns:**

| Col | Header | Data Type | Width | Description | Validation |
|-----|--------|-----------|-------|-------------|------------|
| A | Resource ID | Text | 20 | Unique identifier (hostname, instance ID, asset tag) | Required, unique |
| B | Resource Name | Text | 30 | Human-readable name | Required |
| C | Resource Type | Dropdown | 15 | Compute, Storage, Network, Application | Dropdown list |
| D | Sub-Type | Text | 20 | Server, VM, Disk, Switch, Database, etc. | Required |
| E | Infrastructure Platform | Dropdown | 20 | Physical, VMware, Hyper-V, AWS, Azure, GCP, Kubernetes, etc. | Dropdown list |
| F | Environment | Dropdown | 15 | Production, UAT, Development, DR | Dropdown list |
| G | Criticality | Dropdown | 12 | Critical, High, Medium, Low | Dropdown list |
| H | Business Owner | Text | 20 | Department or team | Optional |
| I | Technical Owner | Text | 20 | Person or team | Required |
| J | Monitoring Status | Dropdown | 18 | Monitored, Partially Monitored, Not Monitored | Dropdown list |
| K | Notes | Text | 40 | Any relevant context | Optional |

**Data Validation:**

```excel
# Resource Type dropdown
={"Compute","Storage","Network","Application"}

# Infrastructure Platform dropdown
={"Physical","VMware","Hyper-V","Proxmox","KVM","AWS","Azure","GCP","Kubernetes","Docker","Other"}

# Environment dropdown
={"Production","UAT","Development","Disaster Recovery"}

# Criticality dropdown
={"Critical","High","Medium","Low"}

# Monitoring Status dropdown
={"Monitored","Partially Monitored","Not Monitored"}
```

**Conditional Formatting:**

- Criticality column:
  - Critical: Red background, white text
  - High: Orange background
  - Medium: Yellow background
  - Low: Green background
- Monitoring Status column:
  - Monitored: Green background
  - Partially Monitored: Yellow background
  - Not Monitored: Red background, white text

**Sample Row:**
| A | B | C | D | E | F | G | H | I | J | K |
|---|---|---|---|---|---|---|---|---|---|---|
| web-prod-01 | Production Web Server 01 | Compute | VM | VMware | Production | Critical | Sales | Infrastructure Team | Monitored | Primary web server |

---

### Sheet 2: Compute Capacity

**Purpose:** Document CPU and memory utilization

**Columns:**

| Col | Header | Data Type | Width | Description | Formula/Source |
|-----|--------|-----------|-------|-------------|----------------|
| A | Resource ID | Text | 20 | From Sheet 1 | =Sheet1!A2 |
| B | Resource Name | Text | 30 | From Sheet 1 | =Sheet1!B2 |
| C | Total CPU Cores | Number | 12 | Total CPU capacity | Manual |
| D | Total Memory GB | Number | 12 | Total memory capacity | Manual |
| E | Current CPU % | Percentage | 12 | Current CPU utilization | Manual |
| F | Current Memory % | Percentage | 12 | Current memory utilization | Manual |
| G | Peak CPU % (30d) | Percentage | 15 | Max CPU over 30 days | Manual |
| H | Peak Memory % (30d) | Percentage | 18 | Max memory over 30 days | Manual |
| I | Peak CPU % (90d) | Percentage | 15 | Max CPU over 90 days | Manual |
| J | Peak Memory % (90d) | Percentage | 18 | Max memory over 90 days | Manual |
| K | Avg CPU % (30d) | Percentage | 15 | Mean CPU over 30 days | Manual |
| L | Avg Memory % (30d) | Percentage | 18 | Mean memory over 30 days | Manual |
| M | Threshold Status (CPU) | Text | 18 | Below Warning/Warning/Critical/Exceeded | Formula |
| N | Threshold Status (Memory) | Text | 20 | Below Warning/Warning/Critical/Exceeded | Formula |
| O | CPU Headroom % | Percentage | 15 | % remaining before warning | Formula |
| P | Memory Headroom % | Percentage | 18 | % remaining before warning | Formula |
| Q | Data Source | Text | 25 | Monitoring system name | Manual |
| R | Collection Date | Date | 15 | When data collected | Manual |

**Threshold Definitions (from policy):**

- CPU Warning: 70%
- CPU Critical: 85%
- Memory Warning: 75%
- Memory Critical: 90%

**Key Formulas:**

```excel
# Threshold Status (CPU) - Column M
=IF(G2>=100,"Exceeded",IF(G2>=85,"Critical",IF(G2>=70,"Warning","Below Warning")))

# Threshold Status (Memory) - Column N
=IF(H2>=100,"Exceeded",IF(H2>=90,"Critical",IF(H2>=75,"Warning","Below Warning")))

# CPU Headroom % - Column O
=70-G2

# Memory Headroom % - Column P
=75-H2
```

**Conditional Formatting:**

- Threshold Status columns (M, N):
  - "Below Warning": Green background
  - "Warning": Yellow background
  - "Critical": Orange background
  - "Exceeded": Red background, white text
- Headroom columns (O, P):
  - Positive (>0): Green
  - Negative (<0): Red
- Peak utilization columns (G, H, I, J):
  - <70%: No formatting
  - 70-84%: Yellow background
  - 85-99%: Orange background
  - ≥100%: Red background

**Sample Row:**
| A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| web-prod-01 | Production Web Server 01 | 8 | 32 | 45% | 62% | 68% | 72% | 71% | 75% | 42% | 58% | Below Warning | Warning | 2% | 3% | Prometheus | 2026-01-15 |

---

### Sheet 3: Storage Capacity

**Purpose:** Document disk space and storage utilization

**Columns:**

| Col | Header | Data Type | Width | Description | Formula/Source |
|-----|--------|-----------|-------|-------------|----------------|
| A | Resource ID | Text | 20 | From Sheet 1 | =Sheet1!A2 |
| B | Resource Name | Text | 30 | From Sheet 1 | =Sheet1!B2 |
| C | Storage Type | Dropdown | 15 | Disk/Volume/Database/Object/Backup | Dropdown |
| D | Total Capacity GB | Number | 18 | Total storage space | Manual |
| E | Used Space GB | Number | 15 | Currently used space | Manual |
| F | Free Space GB | Number | 15 | Available space | Formula =D2-E2 |
| G | Utilization % | Percentage | 12 | % used | Formula =E2/D2 |
| H | Peak Util % (30d) | Percentage | 15 | Max % used over 30 days | Manual |
| I | Peak Util % (90d) | Percentage | 15 | Max % used over 90 days | Manual |
| J | Avg Util % (30d) | Percentage | 15 | Mean % used over 30 days | Manual |
| K | Growth Rate GB/mo | Number | 18 | Monthly growth rate | Manual |
| L | IOPS Utilization % | Percentage | 18 | IOPS utilization (if applicable) | Manual |
| M | Throughput Util % | Percentage | 18 | Throughput utilization (if applicable) | Manual |
| N | Threshold Status | Text | 18 | Below Warning/Warning/Critical/Exceeded | Formula |
| O | Headroom % | Percentage | 12 | % remaining before warning | Formula |
| P | Months to Exhaustion | Number | 20 | Months until full (if trending) | Formula |
| Q | Data Source | Text | 25 | Monitoring system | Manual |
| R | Collection Date | Date | 15 | When collected | Manual |

**Threshold Definitions (from policy):**

- Storage Warning: 75%
- Storage Critical: 85%

**Key Formulas:**

```excel
# Free Space GB - Column F
=D2-E2

# Utilization % - Column G
=E2/D2

# Threshold Status - Column N
=IF(H2>=100,"Exceeded",IF(H2>=85,"Critical",IF(H2>=75,"Warning","Below Warning")))

# Headroom % - Column O
=75-H2

# Months to Exhaustion - Column P
=IF(K2>0,(D2-E2)/K2,"N/A")
```

**Conditional Formatting:**

- Threshold Status column (N): Same as Sheet 2
- Headroom column (O): Same as Sheet 2
- Months to Exhaustion (P):
  - <3 months: Red
  - 3-6 months: Orange
  - 6-12 months: Yellow
  - >12 months: Green

**Sample Row:**
| A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| db-prod-01-data | Database Data Volume | Database | 1000 | 750 | 250 | 75% | 78% | 80% | 72% | 25 | 60% | 45% | Warning | -3% | 10 | AWS CloudWatch | 2026-01-15 |

---

### Sheet 4: Network Capacity

**Purpose:** Document network bandwidth and throughput utilization

**Columns:**

| Col | Header | Data Type | Width | Description | Formula/Source |
|-----|--------|-----------|-------|-------------|----------------|
| A | Resource ID | Text | 20 | From Sheet 1 | =Sheet1!A2 |
| B | Resource Name | Text | 30 | From Sheet 1 | =Sheet1!B2 |
| C | Network Resource Type | Dropdown | 20 | Switch Port/Router/Firewall/WAN Link/VPN/LB | Dropdown |
| D | Interface Speed Mbps | Number | 18 | Link capacity | Manual |
| E | Current Inbound Mbps | Number | 18 | Current inbound throughput | Manual |
| F | Current Outbound Mbps | Number | 20 | Current outbound throughput | Manual |
| G | Inbound Util % | Percentage | 15 | Inbound utilization % | Formula =E2/D2 |
| H | Outbound Util % | Percentage | 15 | Outbound utilization % | Formula =F2/D2 |
| I | Peak Inbound % (30d) | Percentage | 18 | Max inbound over 30 days | Manual |
| J | Peak Outbound % (30d) | Percentage | 20 | Max outbound over 30 days | Manual |
| K | Avg Inbound % (30d) | Percentage | 18 | Mean inbound over 30 days | Manual |
| L | Avg Outbound % (30d) | Percentage | 20 | Mean outbound over 30 days | Manual |
| M | Packet Rate PPS | Number | 15 | Packets per second | Manual |
| N | Error Rate % | Percentage | 12 | Packet error rate | Manual |
| O | Dropped Packets % | Percentage | 18 | Packet drops | Manual |
| P | Threshold Status | Text | 18 | Below Warning/Warning/Critical/Exceeded | Formula |
| Q | Headroom % | Percentage | 12 | % remaining before warning | Formula |
| R | Data Source | Text | 25 | Monitoring system | Manual |
| S | Collection Date | Date | 15 | When collected | Manual |

**Threshold Definitions (from policy):**

- Network Warning: 70%
- Network Critical: 85%

**Key Formulas:**

```excel
# Inbound Util % - Column G
=E2/D2

# Outbound Util % - Column H
=F2/D2

# Threshold Status - Column P (based on MAX of inbound/outbound peak)
=IF(MAX(I2,J2)>=100,"Exceeded",IF(MAX(I2,J2)>=85,"Critical",IF(MAX(I2,J2)>=70,"Warning","Below Warning")))

# Headroom % - Column Q
=70-MAX(I2,J2)
```

**Conditional Formatting:**

- Threshold Status (P): Same as Sheet 2
- Error Rate % (N), Dropped Packets % (O):
  - <0.01%: Green
  - 0.01-0.1%: Yellow
  - >0.1%: Red

---

### Sheet 5: Application Capacity

**Purpose:** Document application-level capacity utilization

**Columns:**

| Col | Header | Data Type | Width | Description | Formula/Source |
|-----|--------|-----------|-------|-------------|----------------|
| A | Application Name | Text | 25 | From Sheet 1 | =Sheet1!B2 |
| B | Capacity Type | Dropdown | 20 | Concurrent Users/TPS/Connection Pool/Queue/API | Dropdown |
| C | Capacity Limit | Number | 15 | Maximum capacity | Manual |
| D | Current Usage | Number | 15 | Current usage | Manual |
| E | Utilization % | Percentage | 12 | % of limit | Formula =D2/C2 |
| F | Peak Usage (30d) | Number | 18 | Max usage over 30 days | Manual |
| G | Peak Util % (30d) | Percentage | 18 | Max % over 30 days | Formula =F2/C2 |
| H | Avg Usage (30d) | Number | 15 | Mean usage over 30 days | Manual |
| I | Avg Util % (30d) | Percentage | 15 | Mean % over 30 days | Formula =H2/C2 |
| J | License Limit | Number | 15 | Licensed capacity (if applicable) | Manual |
| K | License Compliance | Text | 18 | Compliant/Over-Licensed/Under-Licensed | Formula |
| L | Threshold Status | Text | 18 | Below Warning/Warning/Critical/Exceeded | Formula |
| M | Headroom % | Percentage | 12 | % remaining before warning | Formula |
| N | Data Source | Text | 25 | Monitoring system | Manual |
| O | Collection Date | Date | 15 | When collected | Manual |

**Threshold Definitions (from policy):**

- Application Warning: 75%
- Application Critical: 90%

**Key Formulas:**

```excel
# Utilization % - Column E
=D2/C2

# Peak Util % (30d) - Column G
=F2/C2

# Avg Util % (30d) - Column I
=H2/C2

# License Compliance - Column K
=IF(J2="","N/A",IF(F2>J2,"Under-Licensed",IF(F2<J2*0.7,"Over-Licensed","Compliant")))

# Threshold Status - Column L
=IF(G2>=100,"Exceeded",IF(G2>=90,"Critical",IF(G2>=75,"Warning","Below Warning")))

# Headroom % - Column M
=75-G2
```

**Conditional Formatting:**

- Threshold Status (L): Same as Sheet 2
- License Compliance (K):
  - "Compliant": Green
  - "Over-Licensed": Yellow
  - "Under-Licensed": Red

---

### Sheet 6: Threshold Status Summary

**Purpose:** Consolidated threshold status summary

**Sections:**

**Section 1: Overall Summary**

| Metric | Count | Percentage |
|--------|-------|------------|
| Total Resources | COUNTA(Sheet1!A:A)-1 | 100% |
| Resources Monitored | COUNTIF(Sheet1!J:J,"Monitored") | % |
| Resources Below Warning | COUNTIF formulas across Sheets 2-5 | % |
| Resources at Warning | COUNTIF | % |
| Resources at Critical | COUNTIF | % |
| Resources Exceeded | COUNTIF | % |

**Section 2: Breakdown by Resource Type**

| Resource Type | Total | Below Warning | Warning | Critical | Exceeded |
|---------------|-------|---------------|---------|----------|----------|
| Compute | | | | | |
| Storage | | | | | |
| Network | | | | | |
| Application | | | | | |

**Section 3: Breakdown by Environment**

| Environment | Total | Below Warning | Warning | Critical | Exceeded |
|-------------|-------|---------------|---------|----------|----------|
| Production | | | | | |
| UAT | | | | | |
| Development | | | | | |
| DR | | | | | |

**Section 4: Breakdown by Criticality**

| Criticality | Total | Below Warning | Warning | Critical | Exceeded |
|-------------|-------|---------------|---------|----------|----------|
| Critical | | | | | |
| High | | | | | |
| Medium | | | | | |
| Low | | | | | |

**Section 5: Top 10 At-Risk Resources**

| Resource ID | Resource Name | Type | Utilization % | Threshold Status |
|-------------|---------------|------|---------------|------------------|
| (Auto-populated from Sheets 2-5, sorted by utilization descending) | | | | |

**Key Formulas:**

```excel
# Total Resources
=COUNTA(Sheet1!A:A)-1

# Resources Monitored
=COUNTIF(Sheet1!J:J,"Monitored")

# Resources Below Warning (compute + storage + network + application)
=COUNTIF(Sheet2!M:M,"Below Warning")+COUNTIF(Sheet2!N:N,"Below Warning")+COUNTIF(Sheet3!N:N,"Below Warning")+COUNTIF(Sheet4!P:P,"Below Warning")+COUNTIF(Sheet5!L:L,"Below Warning")

# Capacity Health Score
=(Resources Below Warning / Total Monitored) * 100
```

---

### Sheet 7: Monitoring Coverage Assessment

**Purpose:** Document monitoring coverage and gaps

**Columns:**

| Col | Header | Data Type | Width | Description | Formula/Source |
|-----|--------|-----------|-------|-------------|----------------|
| A | Resource ID | Text | 20 | From Sheet 1 | =Sheet1!A2 |
| B | Resource Name | Text | 30 | From Sheet 1 | =Sheet1!B2 |
| C | Monitoring Status | Dropdown | 18 | Monitored/Partially Monitored/Not Monitored | =Sheet1!J2 |
| D | Monitoring Tool(s) | Text | 25 | Tool names | Manual |
| E | Metrics Collected | Text | 35 | List of metrics monitored | Manual |
| F | Metrics Missing | Text | 35 | List of metrics NOT monitored | Manual |
| G | Data Retention Days | Number | 20 | Historical retention period | Manual |
| H | Retention Meets Policy | Dropdown | 20 | Yes/No (>365 days required) | Formula |
| I | Alerting Configured | Dropdown | 18 | Yes/No | Manual |
| J | Data Quality | Dropdown | 15 | Good/Acceptable/Poor | Manual |
| K | Gap Reason | Text | 30 | Why not fully monitored | Manual |
| L | Remediation Plan | Text | 40 | Action to close gap | Manual |
| M | Remediation Owner | Text | 20 | Who will close gap | Manual |
| N | Target Date | Date | 15 | When gap will be closed | Manual |

**Key Formulas:**

```excel
# Retention Meets Policy - Column H
=IF(G2>=365,"Yes","No")
```

**Conditional Formatting:**

- Monitoring Status (C): Same as Sheet 1
- Retention Meets Policy (H):
  - "Yes": Green
  - "No": Red
- Alerting Configured (I):
  - "Yes": Green
  - "No": Red
- Data Quality (J):
  - "Good": Green
  - "Acceptable": Yellow
  - "Poor": Red

---

### Sheet 8: At-Risk Resources & Remediation

**Purpose:** At-risk resource remediation tracking

**Columns:**

| Col | Header | Data Type | Width | Description | Formula/Source |
|-----|--------|-----------|-------|-------------|----------------|
| A | Resource ID | Text | 20 | From Sheets 2-5 (where Warning/Critical/Exceeded) | Manual |
| B | Resource Name | Text | 30 | From Sheets 2-5 | Manual |
| C | Resource Type | Text | 15 | Compute/Storage/Network/Application | Manual |
| D | Threshold Status | Text | 18 | Warning/Critical/Exceeded | Manual |
| E | Current/Peak Util % | Percentage | 18 | Current or peak % utilization | Manual |
| F | Criticality | Text | 12 | From Sheet 1 | Manual |
| G | Environment | Text | 15 | From Sheet 1 | Manual |
| H | Business Impact | Text | 40 | Impact if capacity exhausted | Manual |
| I | Root Cause | Text | 35 | Why capacity is constrained | Manual |
| J | Potential Solutions | Text | 40 | Options to address | Manual |
| K | Recommended Solution | Text | 40 | Preferred approach | Manual |
| L | Cost Estimate | Currency | 15 | Estimated cost | Manual |
| M | Lead Time | Text | 15 | Time to implement | Manual |
| N | Remediation Owner | Text | 20 | Who will implement | Manual |
| O | Target Date | Date | 15 | When completed | Manual |
| P | Status | Dropdown | 15 | Not Started/In Progress/Completed | Manual |

**Conditional Formatting:**

- Threshold Status (D): Same as Sheet 2
- Criticality (F): Same as Sheet 1
- Status (P):
  - "Not Started": Red
  - "In Progress": Yellow
  - "Completed": Green

---

### Sheet 9: Evidence Registry

**Purpose:** Evidence registry for audit

**Columns:**

| Col | Header | Data Type | Width | Description |
|-----|--------|-----------|-------|-------------|
| A | Evidence ID | Text | 15 | Unique ID |
| B | Evidence Type | Dropdown | 18 | Screenshot/Metric Export/Config File/Documentation/Report |
| C | Description | Text | 45 | What evidence shows |
| D | Related Sheet | Text | 15 | Which sheet supported |
| E | Related Resource | Text | 25 | Which resource(s) documented |
| F | Source System | Text | 25 | Where evidence came from |
| G | Collection Date | Date | 15 | When collected |
| H | File Name | Text | 35 | Name of file |
| I | File Location | Text | 45 | Where stored |
| J | File Size KB | Number | 12 | Size |
| K | File Format | Text | 12 | PDF/PNG/CSV/JSON/XLSX |
| L | Retention Years | Number | 15 | How long retained |
| M | Access Restrictions | Text | 20 | Access controls |
| N | Audit Tag | Dropdown | 15 | Audit Ready/Confidential/Public/Internal Only |

**Conditional Formatting:**

- Audit Tag (N):
  - "Audit Ready": Green
  - "Confidential": Orange
  - "Public": Blue
  - "Internal Only": Yellow

---

## Cell Styling Reference

### Header Row Styling

**All sheet headers (Row 1):**

- Font: Bold, 11pt, Calibri
- Background: Dark blue (#1F4E78)
- Text color: White
- Border: All borders, medium weight
- Alignment: Center, Vertical Center
- Text wrap: Enabled
- Row height: 30

### Data Cell Styling

**Text cells:**

- Font: Regular, 10pt, Calibri
- Background: White
- Text color: Black (#000000)
- Border: All borders, thin
- Alignment: Left, Vertical Center

**Number cells:**

- Font: Regular, 10pt, Calibri
- Background: White
- Number format: Number with 1 decimal place
- Alignment: Right, Vertical Center

**Percentage cells:**

- Font: Regular, 10pt, Calibri
- Background: White
- Number format: Percentage with 0 decimal places
- Alignment: Right, Vertical Center

**Currency cells:**

- Font: Regular, 10pt, Calibri
- Background: White
- Number format: Currency (local currency, 2 decimal places)
- Alignment: Right, Vertical Center

**Date cells:**

- Font: Regular, 10pt, Calibri
- Background: White
- Number format: Date (YYYY-MM-DD)
- Alignment: Right, Vertical Center

### Conditional Formatting Color Codes

**Threshold Status:**

- Below Warning: #C6EFCE (Light green)
- Warning: #FFEB9C (Light yellow)
- Critical: #FFC7CE (Light orange)
- Exceeded: #FF0000 (Red), text: #FFFFFF (White)

**Monitoring Status:**

- Monitored: #C6EFCE (Light green)
- Partially Monitored: #FFEB9C (Light yellow)
- Not Monitored: #FFC7CE (Light red)

**Criticality:**

- Critical: #FF0000 (Red), text: #FFFFFF (White)
- High: #FFC000 (Orange)
- Medium: #FFFF00 (Yellow)
- Low: #92D050 (Light green)

**Headroom (positive/negative):**

- Positive (>0): #C6EFCE (Light green)
- Negative (<0): #FFC7CE (Light red)

### Dropdown Lists

**All dropdowns:**

- Input validation type: List
- Show dropdown arrow: Yes
- Ignore blank: Yes
- Show error alert: No (allow free text if needed)

---

## Integration Points

### Integration with Monitoring Tools

**Data Collection:**

- Manual data entry from monitoring dashboards
- Automated data import via monitoring tool APIs (optional)
- Scheduled data refresh (monthly)

**Supported Monitoring Tools:**

- Prometheus: API query for metrics export
- Datadog: API export or dashboard screenshot
- AWS CloudWatch: CLI export or console screenshot
- Azure Monitor: CLI export or portal screenshot
- GCP Cloud Monitoring: CLI export or console screenshot
- Nagios/Zabbix/Icinga: Reporting API or screenshot

**Example API Integration (Prometheus):**
```python
import requests
import pandas as pd

# Query Prometheus for CPU utilization (last 30 days)
query = 'cpu_percent{instance="web-prod-01"}'
response = requests.get(
    'http://prometheus:9090/api/v1/query_range',
    params={
        'query': query,
        'start': '2025-12-15T00:00:00Z',
        'end': '2026-01-15T00:00:00Z',
        'step': '1h'
    }
)

# Parse response and calculate peak/average
data = response.json()['data']['result'][0]['values']
values = [float(v[1]) for v in data]
peak = max(values)
avg = sum(values) / len(values)

# Populate Excel cells
# (Use openpyxl or xlsxwriter to write to workbook)
```

### Integration with CMDB/Asset Inventory

**Resource Inventory Sync:**

- Export asset inventory from CMDB
- Import into Sheet 1 (Resource Inventory)
- Cross-reference to ensure completeness

### Integration with ITSM Tools

**Remediation Tracking:**

- Export at-risk resources from Sheet 8
- Create ITSM tickets (ServiceNow, Jira) for remediation
- Track remediation progress in ITSM
- Update Sheet 8 status as tickets progress

### Integration with Capacity Forecasting (A.8.6.2)

**Data Flow:**

- Sheet 2 (Compute), Sheet 3 (Storage) → Feed into A.8.6.2 for trend analysis
- Historical utilization + growth rates → Used for forecasting

### Integration with Compliance Dashboard (A.8.6.3)

**Data Flow:**

- All sheets → Consolidated into A.8.6.3 dashboard
- Threshold status summary → Dashboard KPIs
- At-risk resources → Dashboard prioritization

---

## Appendix: Example Queries and Scripts

### Prometheus Queries

```promql
# CPU utilization (30-day peak)
max_over_time(cpu_percent{instance="web-prod-01"}[30d])

# Memory utilization (30-day average)
avg_over_time(memory_percent{instance="web-prod-01"}[30d])

# Disk space utilization (current)
(disk_used_bytes{mountpoint="/"} / disk_total_bytes{mountpoint="/"}) * 100

# Network interface utilization (30-day peak)
max_over_time(rate(node_network_transmit_bytes_total{device="eth0"}[5m])[30d:])
```

### AWS CLI Queries

```bash
# Get EC2 CPU utilization (last 30 days, maximum)
aws cloudwatch get-metric-statistics \
  --namespace AWS/EC2 \
  --metric-name CPUUtilization \
  --dimensions Name=InstanceId,Value=i-1234567890abcdef0 \
  --start-time 2025-12-15T00:00:00Z \
  --end-time 2026-01-15T00:00:00Z \
  --period 86400 \
  --statistics Maximum \
  --output json

# Get EBS volume utilization
aws cloudwatch get-metric-statistics \
  --namespace AWS/EBS \
  --metric-name VolumeReadBytes \
  --dimensions Name=VolumeId,Value=vol-1234567890abcdef0 \
  --start-time 2025-12-15T00:00:00Z \
  --end-time 2026-01-15T00:00:00Z \
  --period 86400 \
  --statistics Sum \
  --output json
```

### Azure CLI Queries

```bash
# Get VM CPU utilization (last 30 days)
az monitor metrics list \
  --resource /subscriptions/{subscription-id}/resourceGroups/{resource-group}/providers/Microsoft.Compute/virtualMachines/{vm-name} \
  --metric "Percentage CPU" \
  --start-time 2025-12-15T00:00:00Z \
  --end-time 2026-01-15T00:00:00Z \
  --interval PT1H \
  --aggregation Maximum

# Get disk utilization
az monitor metrics list \
  --resource /subscriptions/{subscription-id}/resourceGroups/{resource-group}/providers/Microsoft.Compute/disks/{disk-name} \
  --metric "Used Bytes" \
  --start-time 2025-12-15T00:00:00Z \
  --end-time 2026-01-15T00:00:00Z \
  --interval PT1H \
  --aggregation Average
```

### Python Script for Excel Population

```python
import openpyxl
from datetime import datetime

# Load workbook
wb = openpyxl.load_workbook('ISMS-A.8.6.1-Capacity-Utilization-Assessment.xlsx')
ws = wb['Sheet 2: Compute Capacity']

# Example: Populate compute capacity data
row = 2  # Start from row 2 (after header)
ws[f'A{row}'] = 'web-prod-01'
ws[f'B{row}'] = 'Production Web Server 01'
ws[f'C{row}'] = 8  # CPU cores
ws[f'D{row}'] = 32  # Memory GB
ws[f'E{row}'] = 0.45  # Current CPU % (as decimal)
ws[f'F{row}'] = 0.62  # Current Memory % (as decimal)
ws[f'G{row}'] = 0.68  # Peak CPU % 30d
ws[f'H{row}'] = 0.72  # Peak Memory % 30d
ws[f'Q{row}'] = 'Prometheus'
ws[f'R{row}'] = datetime.now()

# Formulas are preserved (Threshold Status, Headroom)
# Excel will recalculate on open

# Save workbook
wb.save('ISMS-A.8.6.1-Capacity-Utilization-Assessment.xlsx')
```

---

**END OF DOCUMENT**

**Total Lines:** 3,100+

This comprehensive assessment specification provides everything needed to complete a professional, audit-ready capacity utilization assessment aligned with ISO/IEC 27001:2022 Control A.8.6 and organizational capacity management policies.
---

## Appendix A: Quick Reference Guide

### Critical Thresholds Summary

| Resource Type | Warning Threshold | Critical Threshold | Notes |
|---------------|-------------------|-------------------|-------|
| **Compute - CPU** | 70% | 85% | Based on peak utilization |
| **Compute - Memory** | 75% | 90% | Risk of swapping/paging |
| **Storage - Disk** | 75% | 85% | General purpose |
| **Storage - Database** | 70% | 80% | Lower threshold for safety |
| **Storage - Logs** | 70% | 80% | Fast growth patterns |
| **Network - Bandwidth** | 70% | 85% | Sustained utilization |
| **Application - Users** | 75% | 90% | Concurrent sessions |
| **Application - Connections** | 75% | 90% | Connection pools |
| **Application - Queues** | 70% | 85% | Message/job queues |

### Capacity Headroom Interpretation

| Headroom | Status | Action Required |
|----------|--------|-----------------|
| **> 20%** | Healthy | Continue monitoring |
| **10-20%** | Adequate | Monthly review |
| **5-10%** | Marginal | Weekly review, plan expansion |
| **0-5%** | At Risk | Daily monitoring, immediate planning |
| **< 0% (Negative)** | **EXCEEDED** | **Immediate action required** |

### Estimated Exhaustion Timeline Actions

| Months Until Exhaustion | Priority | Action Timeline |
|-------------------------|----------|-----------------|
| **< 1 month** | **CRITICAL** | Immediate emergency expansion |
| **1-3 months** | **HIGH** | Initiate procurement/expansion now |
| **3-6 months** | **MEDIUM** | Begin planning and budgeting |
| **6-12 months** | **LOW** | Include in annual capacity plan |
| **> 12 months** | **Monitor** | Continue quarterly reviews |

### Data Collection Frequencies

| Data Type | Collection Frequency | Retention Period | Purpose |
|-----------|---------------------|------------------|---------|
| **Current utilization** | Real-time (< 5 min) | 30-90 days | Instant visibility |
| **Peak utilization** | Daily aggregates | 12-24 months | Trend analysis |
| **Average utilization** | Daily aggregates | 12-24 months | Baseline understanding |
| **Growth rates** | Monthly calculation | 36 months | Forecasting |
| **Capacity changes** | As they occur | Permanent | Change history |

---

## Appendix B: Monitoring Tool Quick Reference

### Prometheus Example Queries

```promql
# Current CPU utilization
100 - (avg by (instance) (irate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)

# Peak CPU over 30 days
max_over_time((100 - (avg by (instance) (irate(node_cpu_seconds_total{mode="idle"}[5m])) * 100))[30d:])

# Average CPU over 30 days
avg_over_time((100 - (avg by (instance) (irate(node_cpu_seconds_total{mode="idle"}[5m])) * 100))[30d:])

# Memory utilization percentage
(1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)) * 100

# Disk space utilization
(1 - (node_filesystem_avail_bytes{mountpoint="/"} / node_filesystem_size_bytes{mountpoint="/"})) * 100

# Network interface utilization (percentage of link speed)
rate(node_network_transmit_bytes_total{device="eth0"}[5m]) * 8 / 1000000000 * 100
```

### AWS CloudWatch CLI Examples

```bash
# Get EC2 CPU utilization (30-day maximum)
aws cloudwatch get-metric-statistics \
  --namespace AWS/EC2 \
  --metric-name CPUUtilization \
  --dimensions Name=InstanceId,Value=i-1234567890abcdef0 \
  --start-time $(date -u -d '30 days ago' +%Y-%m-%dT%H:%M:%S) \
  --end-time $(date -u +%Y-%m-%dT%H:%M:%S) \
  --period 3600 \
  --statistics Maximum \
  --output json

# Get EBS volume utilization
aws cloudwatch get-metric-statistics \
  --namespace AWS/EBS \
  --metric-name VolumeReadBytes \
  --dimensions Name=VolumeId,Value=vol-1234567890abcdef0 \
  --start-time $(date -u -d '30 days ago' +%Y-%m-%dT%H:%M:%S) \
  --end-time $(date -u +%Y-%m-%dT%H:%M:%S) \
  --period 86400 \
  --statistics Sum \
  --output json
```

### Azure CLI Examples

```bash
# Get VM CPU percentage (30-day max)
az monitor metrics list \
  --resource /subscriptions/{sub-id}/resourceGroups/{rg}/providers/Microsoft.Compute/virtualMachines/{vm-name} \
  --metric "Percentage CPU" \
  --start-time $(date -u -d '30 days ago' +%Y-%m-%dT%H:%M:%S) \
  --end-time $(date -u +%Y-%m-%dT%H:%M:%S) \
  --interval PT1H \
  --aggregation Maximum

# Get disk utilization
az monitor metrics list \
  --resource /subscriptions/{sub-id}/resourceGroups/{rg}/providers/Microsoft.Compute/disks/{disk-name} \
  --metric "Used Bytes" \
  --start-time $(date -u -d '30 days ago' +%Y-%m-%dT%H:%M:%S) \
  --end-time $(date -u +%Y-%m-%dT%H:%M:%S) \
  --interval PT1H \
  --aggregation Average
```

---

## Appendix C: Common Capacity Expansion Scenarios

### Scenario 1: Virtual Machine Vertical Scaling

**Situation:** VM at 88% CPU peak, 92% memory peak (both critical)

**Options:**
1. **Increase VM allocation**

   - Pros: Simple, quick
   - Cons: Requires downtime (typically)
   - Timeline: 1-2 hours (with change control approval)
   - Example: 8 vCPU → 12 vCPU, 32 GB → 48 GB RAM

2. **Hot-add CPU/memory** (if supported)

   - Pros: No downtime
   - Cons: Requires hot-add support (VMware, Hyper-V Enterprise)
   - Timeline: Minutes
   
**Implementation Steps:**
1. Schedule maintenance window (if downtime required)
2. Take VM snapshot/backup
3. Increase vCPU/memory allocation
4. Power on VM
5. Verify utilization improvement
6. Update Sheet 2 with new capacity

### Scenario 2: Storage Volume Expansion

**Situation:** Storage volume at 86% utilization, growing 50 GB/month

**Options:**
1. **Expand existing volume**

   - Pros: Preserves data, simple
   - Cons: May require OS-level filesystem resize
   - Timeline: 1-2 hours
   - Example: 1 TB → 2 TB

2. **Add additional volume**

   - Pros: No impact to existing volume
   - Cons: Requires application reconfiguration
   - Timeline: 2-4 hours
   
**Implementation Steps:**
1. Verify storage array has capacity
2. Expand LUN/volume at storage layer
3. Rescan storage on host
4. Extend partition/filesystem (Linux: `resize2fs`, Windows: Disk Management)
5. Verify new capacity visible
6. Update Sheet 3 with new capacity

### Scenario 3: Cloud Instance Right-Sizing

**Situation:** AWS EC2 instance at 22% CPU peak, 28% memory peak (over-provisioned)

**Options:**
1. **Downsize instance type**

   - Pros: Cost savings, still adequate headroom
   - Cons: Requires stop/start (downtime)
   - Timeline: 30-60 minutes
   - Example: c5.4xlarge (16 vCPU, 32 GB) → c5.xlarge (4 vCPU, 8 GB)
   - Savings: ~$200/month

2. **Use AWS Compute Optimizer recommendations**

   - Pros: AWS suggests optimal size
   - Cons: Still requires testing
   
**Implementation Steps:**
1. Review AWS Compute Optimizer recommendations
2. Test in dev/staging environment first
3. Schedule maintenance window for production
4. Stop instance
5. Change instance type
6. Start instance
7. Verify performance acceptable
8. Monitor for 1-2 weeks
9. Update Sheet 2 with new capacity

### Scenario 4: Database Transaction Log Growth

**Situation:** Transaction log at 95% utilization, growing 75 GB/month

**Immediate Actions:**
1. **Increase transaction log size** (emergency)
   ```sql
   ALTER DATABASE [DatabaseName]
   MODIFY FILE (NAME = LogFileName, SIZE = 1024000MB);  -- 1TB
   ```

2. **Investigate root cause:**

   - Long-running transactions?
   - Insufficient log backup frequency?
   - Massive data loads without proper batching?

3. **Long-term fixes:**

   - Increase log backup frequency (every 15-30 minutes instead of hourly)
   - Implement transaction log monitoring alerts
   - Review application transaction patterns
   
**Implementation Timeline:**

- Emergency expansion: 5-10 minutes
- Root cause investigation: 1-2 days
- Long-term fixes: 1-2 weeks

### Scenario 5: Network Link Upgrade

**Situation:** WAN link at 82% peak utilization

**Options:**
1. **Upgrade link speed**

   - Example: 1 Gbps → 10 Gbps
   - Pros: More capacity
   - Cons: Cost, may require new hardware
   - Timeline: Weeks to months (ISP provisioning)

2. **Add additional link (ECMP/bonding)**

   - Pros: Redundancy + capacity
   - Cons: Requires compatible routing
   - Timeline: Weeks
   
3. **Traffic optimization**

   - Implement QoS to prioritize critical traffic
   - Enable compression
   - Offload non-critical traffic (e.g., backups to off-hours)
   
**Implementation Steps:**
1. Contact ISP for link upgrade quote and timeline
2. Budget approval
3. ISP provisions new link
4. Update router configuration
5. Verify traffic load-balanced
6. Update Sheet 4 with new capacity

---

## Appendix D: Troubleshooting Common Issues

### Issue: Monitoring Data Not Available

**Symptoms:**

- Can't collect peak/average utilization
- Missing historical data
- Gaps in monitoring

**Causes:**
1. Monitoring agent not installed
2. Monitoring data retention too short
3. Monitoring system performance issues
4. Network connectivity issues

**Resolution:**
1. Verify monitoring agent status
2. Check monitoring data retention settings (should be 12+ months)
3. Review monitoring system capacity
4. Verify network connectivity between monitored resources and monitoring system

**Workaround:**

- If historical data unavailable, document gap in Sheet 7 (Monitoring Coverage)
- Use current utilization as best estimate
- Flag for follow-up in next assessment cycle

### Issue: Threshold Status Calculation Errors

**Symptoms:**

- Excel formulas showing errors
- Threshold status incorrect
- Headroom calculations wrong

**Causes:**
1. Peak utilization cell empty or non-numeric
2. Threshold values not defined
3. Formula references incorrect cells

**Resolution:**
1. Verify all required cells populated with numeric values
2. Check threshold definitions match policy
3. Verify Excel formula syntax:
   ```excel
   =IF(G2>=100,"Exceeded",IF(G2>=85,"Critical",IF(G2>=70,"Warning","Below Warning")))
   ```
4. Ensure percentage values formatted correctly (0.88 = 88%, not 88 = 88%)

### Issue: Growth Rate Calculation Impossible

**Symptoms:**

- Can't calculate GB/month growth
- Historical data insufficient

**Causes:**
1. Less than 30 days of historical data
2. Storage capacity changed recently (expansion)
3. Data inconsistencies

**Resolution:**
1. If <30 days data: Estimate based on available data, document assumption
2. If recent expansion: Calculate growth rate from pre-expansion data
3. If inconsistent data: Review monitoring data quality, flag for investigation

**Workaround:**

- Use business knowledge to estimate growth (e.g., "we add 100 new customers/month, each customer = 500 MB data")
- Document estimation methodology
- Plan to measure actual growth over next 30-90 days

### Issue: Cloud Resources Missing from Inventory

**Symptoms:**

- Cloud instances not in Sheet 1
- Cloud storage not documented
- Incomplete assessment

**Causes:**
1. Different teams manage cloud vs. on-premises
2. Cloud resources not in CMDB
3. Shadow IT (cloud resources provisioned without central IT knowledge)

**Resolution:**
1. Review cloud consoles directly (AWS, Azure, GCP)
2. Check cloud billing reports (resources incurring cost = resources to document)
3. Interview cloud operations team
4. Use cloud discovery tools (AWS Config, Azure Resource Graph, GCP Asset Inventory)

### Issue: IOPS/Throughput Limits Unknown

**Symptoms:**

- Can't document IOPS or throughput utilization
- Don't know limits

**Causes:**
1. Storage system documentation not available
2. Cloud instance limits not documented
3. Monitoring doesn't track IOPS/throughput

**Resolution:**
1. **For cloud:** Lookup instance type limits:

   - AWS: Check instance type specifications
   - Azure: Check VM size specifications
   - GCP: Check machine type specifications

2. **For SAN/NAS:** Review storage array specifications or contact vendor
3. **For monitoring:** Implement IOPS/throughput monitoring if critical

**Workaround:**

- If limits unknown, document as "Unknown - to be determined"
- Flag for follow-up investigation
- Continue with disk space utilization assessment

---

**END OF APPENDICES**

---

**Document Completion Statistics:**

- **Total Sheets:** 9 + 1 summary dashboard = 10 sheets
- **Total Workflows:** 11 phases (Preparation through Review & Approval)
- **Assessment Types Covered:** Compute, Storage, Network, Application
- **Monitoring Tools Supported:** Prometheus, Datadog, AWS CloudWatch, Azure Monitor, GCP Cloud Monitoring, Nagios, Zabbix, VMware vCenter, and others
- **Evidence Types:** Screenshots, metric exports, configuration files, reports, documentation
- **Quality Checkpoints:** 14 quality checklists throughout document
- **Real-World Examples:** 25+ detailed scenario examples
- **Formulas Provided:** 15+ Excel formulas for calculations
- **Total Sections:** 9 major sections in Part I, 6 major sections in Part II

---

**END OF SPECIFICATION**

---

*"Differential cryptanalysis taught us that even small biases can lead to complete breaks of cryptographic systems."*
— Adi Shamir

<!-- QA_VERIFIED: 2026-01-31 -->
