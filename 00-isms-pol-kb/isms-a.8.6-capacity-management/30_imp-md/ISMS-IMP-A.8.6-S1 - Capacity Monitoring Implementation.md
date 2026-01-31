# ISMS-IMP-A.8.6-S1
## Capacity Monitoring Implementation Guide

**Document ID**: ISMS-IMP-A.8.6-S1  
**Title**: Capacity Monitoring Implementation Guide  
**Version**: 1.0  
**Date**: [Date]  
**Classification**: Internal  
**Owner**: Infrastructure Manager / Capacity Planning Team  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | Capacity Planning Team / Infrastructure Team | Initial implementation guidance |

**Review Cycle**: Annual (or upon significant infrastructure/tool changes)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Primary: Infrastructure Manager / IT Operations Manager
- Technical Review: Capacity Planning Manager
- Security Review: Chief Information Security Officer (CISO)

**Distribution**: IT operations, infrastructure teams, capacity planning team, monitoring team  
**Related Documents**: ISMS-POL-A.8.6-S2 (Capacity Management Policy), ISMS-POL-A.8.16 (Monitoring Activities)

---

## 1. Purpose and Scope

### 1.1 Implementation Guide Purpose

This document provides **step-by-step technical guidance** for implementing capacity monitoring infrastructure to satisfy requirements defined in ISMS-POL-A.8.6-S2 (Capacity Management Policy).

**Target Audience**: Infrastructure engineers, IT operations staff, capacity planning team, monitoring administrators

**Prerequisites**: 
- Approved capacity management policy (ISMS-POL-A.8.6-S2)
- Executive support and budget allocation for monitoring tools
- Inventory of resources to be monitored
- Access to infrastructure platforms (hypervisors, cloud consoles, storage management, network management)

### 1.2 Implementation Scope

This guide covers implementation of:

1. **Monitoring Tool Selection** - Criteria and process for selecting capacity monitoring tools
2. **Resource Monitoring Configuration** - Setting up monitoring for compute, storage, network, application, cloud resources
3. **Threshold Configuration** - Defining and implementing warning and critical thresholds
4. **Alerting Integration** - Connecting monitoring to alerting channels (email, SMS, incident management)
5. **Data Retention** - Configuring historical data retention for trend analysis
6. **Dashboard Creation** - Building capacity visibility dashboards
7. **Assessment Tool** - Using the capacity utilization assessment Excel generator

**Out of Scope**: This guide does NOT cover capacity forecasting, planning, or reporting (covered in ISMS-IMP-A.8.6-S2 and ISMS-IMP-A.8.6-S3).

### 1.3 Implementation Approach

**Phased Implementation**:
- **Phase 1** (Months 1-2): Production critical systems monitoring
- **Phase 2** (Months 3-4): Remaining production systems
- **Phase 3** (Months 5-6): Non-production systems
- **Ongoing**: Continuous improvement and optimization

**Success Criteria**:
- 100% of production systems monitored within 6 months
- 90% of non-production systems monitored within 12 months
- All monitoring data feeding capacity utilization assessment
- Alerting operational and tested

---

## 2. Monitoring Tool Selection

### 2.1 Tool Selection Criteria

Capacity monitoring tools SHALL be evaluated against the following criteria:

#### 2.1.1 Functional Requirements

**Metric Collection**:
- Support for compute metrics (CPU, memory, processes)
- Support for storage metrics (disk space, IOPS, throughput)
- Support for network metrics (bandwidth, packets, connections)
- Support for application metrics (custom metrics, API access)
- Support for cloud platform metrics (AWS CloudWatch, Azure Monitor, GCP Cloud Monitoring)

**Data Retention**:
- Minimum 12 months historical data retention
- Configurable data aggregation (minute, hour, day)
- Data export capability (CSV, JSON, API)

**Alerting**:
- Threshold-based alerting (warning, critical)
- Multi-channel alerting (email, SMS, webhook, API)
- Alert deduplication and grouping
- Escalation support

**Visualization**:
- Dashboard creation for capacity visibility
- Chart/graph generation
- Real-time and historical views

**Integration**:
- Integration with infrastructure platforms (VMware, Hyper-V, Kubernetes)
- Integration with cloud platforms (AWS, Azure, GCP)
- Integration with ITSM tools (ServiceNow, Jira)
- API access for automation and custom integrations

#### 2.1.2 Non-Functional Requirements

**Scalability**:
- Support for current resource count plus 50% growth
- Performance impact on monitored systems <1% CPU/memory

**Reliability**:
- High availability deployment option
- Data loss prevention (buffering, queuing)
- Monitoring system self-monitoring

**Usability**:
- Intuitive interface for dashboard creation
- Role-based access control
- Self-service metric exploration

**Cost**:
- Total cost of ownership within budget
- Licensing model (per-host, per-metric, per-user)
- Implementation and maintenance costs

### 2.2 Tool Categories

Organizations may choose from the following tool categories:

#### 2.2.1 Open Source Tools

**Prometheus + Grafana**:
- **Strengths**: Free, widely adopted, extensive integrations, flexible
- **Use Case**: Cloud-native, Kubernetes, microservices
- **Considerations**: Requires operational expertise, self-hosted
- **Cost**: Free software, infrastructure costs only

**Nagios / Icinga / Zabbix**:
- **Strengths**: Mature, stable, comprehensive monitoring
- **Use Case**: Traditional infrastructure, on-premises datacenters
- **Considerations**: Configuration complexity, older UX
- **Cost**: Free software, infrastructure costs only

#### 2.2.2 Commercial SaaS Tools

**Datadog**:
- **Strengths**: Comprehensive, easy to use, excellent integrations, cloud-native
- **Use Case**: Hybrid cloud, comprehensive observability
- **Considerations**: Cost can escalate with scale
- **Cost**: ~$15-31/host/month depending on features

**New Relic**:
- **Strengths**: Application performance + infrastructure monitoring, unified platform
- **Use Case**: Application-centric monitoring
- **Considerations**: Pricing based on data ingestion
- **Cost**: ~$0.30/GB ingested

**Dynatrace**:
- **Strengths**: AI/ML-driven insights, automated baselining, root cause analysis
- **Use Case**: Large enterprises, complex environments
- **Considerations**: Premium pricing
- **Cost**: Custom pricing, typically $70-100/host/month

**Splunk Infrastructure Monitoring (SignalFx)**:
- **Strengths**: Real-time streaming, metric analytics, cloud-native
- **Use Case**: High-volume metric environments
- **Considerations**: Complex pricing model
- **Cost**: ~$18/host/month + data costs

#### 2.2.3 Cloud-Native Tools

**AWS CloudWatch**:
- **Strengths**: Native AWS integration, no additional deployment, pay-per-use
- **Use Case**: AWS-based infrastructure
- **Considerations**: Limited cross-cloud visibility
- **Cost**: ~$0.30/custom metric/month, $0.01/1000 GetMetric requests

**Azure Monitor**:
- **Strengths**: Native Azure integration, comprehensive Azure resource monitoring
- **Use Case**: Azure-based infrastructure
- **Considerations**: Limited non-Azure visibility
- **Cost**: ~$0.25/GB logs, metrics included with resources

**Google Cloud Monitoring (formerly Stackdriver)**:
- **Strengths**: Native GCP integration, comprehensive GCP resource monitoring
- **Use Case**: GCP-based infrastructure
- **Considerations**: Limited non-GCP visibility
- **Cost**: ~$0.258/GB logs, metrics included with resources

#### 2.2.4 Infrastructure Management Tools

**VMware vRealize Operations**:
- **Strengths**: Deep VMware integration, capacity planning features, optimization recommendations
- **Use Case**: VMware-centric environments
- **Considerations**: VMware-specific
- **Cost**: ~$3,000-4,000/CPU (perpetual license) or ~$700/CPU/year (subscription)

**Microsoft System Center Operations Manager (SCOM)**:
- **Strengths**: Deep Microsoft integration, comprehensive Windows/Active Directory monitoring
- **Use Case**: Microsoft-centric environments
- **Considerations**: Complex deployment, Windows-focused
- **Cost**: Included with System Center license

### 2.3 Tool Selection Process

**Step 1: Define Requirements**:
- Document functional requirements per Section 2.1.1
- Document non-functional requirements per Section 2.1.2
- Identify must-have vs. nice-to-have features
- Define budget constraints

**Step 2: Shortlist Candidates**:
- Evaluate 3-5 tools against requirements
- Consider existing tool investments (avoid redundancy)
- Check compatibility with infrastructure platforms
- Review analyst reports (Gartner, Forrester)

**Step 3: Proof of Concept (POC)**:
- Deploy shortlisted tools in test environment
- Monitor representative workloads (compute, storage, network, application)
- Test alerting and integration
- Evaluate usability and performance
- Duration: 2-4 weeks per tool

**Step 4: Total Cost of Ownership Analysis**:
- Calculate 3-year TCO:
  - Licensing costs (subscription or perpetual)
  - Infrastructure costs (self-hosted tools)
  - Implementation costs (deployment, configuration, integration)
  - Operational costs (administration, maintenance, training)
- Compare costs across shortlisted tools

**Step 5: Selection Decision**:
- Score tools against requirements (weighted scoring)
- Consider TCO, usability, vendor support, roadmap
- Document selection rationale
- Obtain approval from IT management and finance

**Step 6: Procurement and Deployment**:
- Procure selected tool (license, subscription)
- Deploy in production (or production-ready staging)
- Begin Phase 1 implementation (critical systems)

---

## 3. Resource Monitoring Configuration

### 3.1 Compute Capacity Monitoring

#### 3.1.1 Physical Server Monitoring

**Metrics to Collect**:

| Metric | Description | Unit | Collection Interval |
|--------|-------------|------|-------------------|
| CPU Utilization | Percentage of CPU cores in use | % | 1-5 minutes |
| CPU Load Average | 1-min, 5-min, 15-min load averages (Linux) | Load | 1-5 minutes |
| Memory Utilization | Percentage of RAM in use | % | 1-5 minutes |
| Memory Available | Free + buffers/cache (Linux) | GB | 1-5 minutes |
| Swap Utilization | Swap space usage (indicates memory pressure) | % | 1-5 minutes |

**Configuration Examples**:

**Prometheus** (Linux node_exporter):
```yaml
# Deployed as systemd service on each server
# Collects system metrics via /proc and /sys filesystems
# Scraped by Prometheus server every 60 seconds

# /etc/prometheus/prometheus.yml
scrape_configs:
  - job_name: 'linux-servers'
    scrape_interval: 60s
    static_configs:
      - targets:
        - 'server1.example.com:9100'
        - 'server2.example.com:9100'
```

**CloudWatch** (AWS EC2):
```bash
# Install CloudWatch agent
sudo wget https://s3.amazonaws.com/amazoncloudwatch-agent/linux/amd64/latest/amazon-cloudwatch-agent.deb
sudo dpkg -i amazon-cloudwatch-agent.deb

# Configure metrics collection
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl \
  -a fetch-config \
  -m ec2 \
  -c file:/opt/aws/amazon-cloudwatch-agent/etc/config.json \
  -s

# config.json includes CPU, memory, disk metrics every 60 seconds
```

**SNMP** (Generic hardware servers):
```bash
# Enable SNMP on server
# Configure monitoring tool to poll SNMP OIDs:
# CPU: .1.3.6.1.2.1.25.3.3.1.2 (hrProcessorLoad)
# Memory: .1.3.6.1.2.1.25.2.3.1.6 (hrStorageUsed)
```

#### 3.1.2 Virtual Machine Monitoring

**Hypervisor-Level Metrics**:

| Metric | Description | Unit | Collection Interval |
|--------|-------------|------|-------------------|
| Host CPU Utilization | Hypervisor host CPU usage | % | 1-5 minutes |
| Host Memory Utilization | Hypervisor host memory usage | % | 1-5 minutes |
| VM Count | Number of VMs per host | Count | 5-15 minutes |
| vCPU Overcommitment | vCPU allocated / physical CPU cores | Ratio | 5-15 minutes |
| Memory Overcommitment | vRAM allocated / physical RAM | Ratio | 5-15 minutes |

**VM-Level Metrics**:
- Same as physical server metrics (CPU, memory)
- Guest OS agent required for detailed metrics

**Configuration Examples**:

**VMware vCenter**:
```python
# Using pyVmomi (Python vSphere SDK)
from pyVim.connect import SmartConnect
from pyVmomi import vim

# Connect to vCenter
si = SmartConnect(host='vcenter.example.com', user='monitor@vsphere.local', pwd='password')

# Query host performance metrics
content = si.content
perfManager = content.perfManager

# CPU usage metric ID: 2 (cpu.usage.average)
# Memory usage metric ID: 24 (mem.usage.average)
# Query every 5 minutes (300 seconds)
```

**Prometheus + VMware Exporter**:
```yaml
# Deploy vmware_exporter
# Collects metrics from vCenter API

# /etc/prometheus/prometheus.yml
scrape_configs:
  - job_name: 'vmware'
    scrape_interval: 300s
    static_configs:
      - targets:
        - 'vmware-exporter.example.com:9272'
    params:
      target: ['vcenter.example.com']
```

#### 3.1.3 Container/Kubernetes Monitoring

**Node-Level Metrics**:

| Metric | Description | Unit | Collection Interval |
|--------|-------------|------|-------------------|
| Node CPU Utilization | Kubernetes node CPU usage | % | 1 minute |
| Node Memory Utilization | Kubernetes node memory usage | % | 1 minute |
| Pod Count | Pods running on node | Count | 1 minute |
| Allocatable CPU/Memory | Resources available for pods | Cores/GB | 5 minutes |

**Pod/Container-Level Metrics**:
- Container CPU usage and limits
- Container memory usage and limits
- Container restart count

**Configuration Examples**:

**Prometheus + kube-state-metrics**:
```yaml
# Deploy kube-state-metrics in kube-system namespace
kubectl apply -f https://github.com/kubernetes/kube-state-metrics/examples/standard/

# Prometheus scrape config
scrape_configs:
  - job_name: 'kubernetes-nodes'
    kubernetes_sd_configs:
      - role: node
    relabel_configs:
      - source_labels: [__address__]
        target_label: __address__
        replacement: kubernetes.default.svc:443

  - job_name: 'kubernetes-pods'
    kubernetes_sd_configs:
      - role: pod
```

**Datadog Kubernetes Integration**:
```yaml
# Deploy Datadog agent as DaemonSet
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: datadog-agent
spec:
  template:
    spec:
      containers:
      - name: datadog-agent
        image: datadog/agent:latest
        env:
        - name: DD_API_KEY
          value: "YOUR_API_KEY"
        - name: DD_SITE
          value: "datadoghq.com"
        - name: DD_KUBELET_TLS_VERIFY
          value: "false"
```

#### 3.1.4 Cloud Compute Monitoring

**AWS EC2**:
- Default CloudWatch metrics: CPU, network, disk I/O
- Enhanced monitoring: Memory, disk space (requires CloudWatch agent)
- Collection interval: 1 or 5 minutes

**Azure Virtual Machines**:
- Default Azure Monitor metrics: CPU, network, disk
- Detailed metrics: Memory, disk space (requires diagnostics extension)
- Collection interval: 1 minute

**Google Compute Engine**:
- Default Cloud Monitoring metrics: CPU, network, disk
- Custom metrics via Monitoring API
- Collection interval: 1 minute

### 3.2 Storage Capacity Monitoring

#### 3.2.1 Filesystem/Volume Monitoring

**Metrics to Collect**:

| Metric | Description | Unit | Collection Interval |
|--------|-------------|------|-------------------|
| Disk Space Used | Space consumed on filesystem/volume | GB | 5-15 minutes |
| Disk Space Available | Free space remaining | GB | 5-15 minutes |
| Disk Space Utilization | Percentage used | % | 5-15 minutes |
| Inode Utilization | Filesystem inode usage (Linux) | % | 15 minutes |

**Configuration Examples**:

**Prometheus** (node_exporter):
```promql
# Query filesystem metrics
node_filesystem_avail_bytes{mountpoint="/"}  # Available bytes
node_filesystem_size_bytes{mountpoint="/"}   # Total size bytes
node_filesystem_files{mountpoint="/"}        # Total inodes
node_filesystem_files_free{mountpoint="/"}   # Free inodes

# Calculate utilization percentage
(1 - (node_filesystem_avail_bytes / node_filesystem_size_bytes)) * 100
```

**Windows Disk Monitoring** (Performance Counters):
```powershell
# LogicalDisk counters
Get-Counter '\LogicalDisk(*)\% Free Space'
Get-Counter '\LogicalDisk(*)\Free Megabytes'
```

**Storage Array Monitoring** (vendor-specific):
- NetApp ONTAP: REST API or SNMP
- Dell EMC: Unisphere API
- HPE 3PAR: REST API or CLI
- Pure Storage: REST API

#### 3.2.2 Database Storage Monitoring

**Database-Specific Metrics**:

**PostgreSQL**:
```sql
-- Database size
SELECT pg_database.datname, 
       pg_size_pretty(pg_database_size(pg_database.datname)) AS size
FROM pg_database;

-- Tablespace utilization
SELECT spcname, 
       pg_size_pretty(pg_tablespace_size(spcname)) AS size
FROM pg_tablespace;
```

**MySQL/MariaDB**:
```sql
-- Database size
SELECT table_schema AS database_name,
       ROUND(SUM(data_length + index_length) / 1024 / 1024, 2) AS size_mb
FROM information_schema.tables
GROUP BY table_schema;
```

**SQL Server**:
```sql
-- Database size and space available
EXEC sp_spaceused;

-- File size and growth
SELECT name, size, growth 
FROM sys.database_files;
```

**Oracle**:
```sql
-- Tablespace utilization
SELECT tablespace_name,
       ROUND(SUM(bytes)/1024/1024/1024, 2) AS size_gb,
       ROUND(SUM(bytes - NVL(free_bytes,0))/1024/1024/1024, 2) AS used_gb
FROM (
  SELECT tablespace_name, SUM(bytes) AS bytes
  FROM dba_data_files
  GROUP BY tablespace_name
) df,
(
  SELECT tablespace_name, SUM(bytes) AS free_bytes
  FROM dba_free_space
  GROUP BY tablespace_name
) fs
WHERE df.tablespace_name = fs.tablespace_name (+)
GROUP BY df.tablespace_name;
```

#### 3.2.3 Backup Storage Monitoring

**Backup Repository Capacity**:
- Monitor backup storage utilization
- Track backup data growth rate
- Monitor deduplication/compression ratios

**Backup Software-Specific**:

**Veeam Backup & Replication**:
```powershell
# PowerShell cmdlets
Get-VBRBackupRepository | Select Name, FriendlyPath, @{N="Capacity";E={$_.GetContainer().CachedTotalSpace}}, @{N="Free";E={$_.GetContainer().CachedFreeSpace}}
```

**Commvault**:
- Monitor via CommServe database queries
- MediaAgent disk space monitoring

**Rubrik**:
- REST API: GET /api/v1/cluster/me/capacity

### 3.3 Network Capacity Monitoring

#### 3.3.1 Network Interface Monitoring

**Metrics to Collect**:

| Metric | Description | Unit | Collection Interval |
|--------|-------------|------|-------------------|
| Interface Bandwidth In | Inbound traffic rate | Mbps | 1-5 minutes |
| Interface Bandwidth Out | Outbound traffic rate | Mbps | 1-5 minutes |
| Interface Utilization | % of interface capacity used | % | 1-5 minutes |
| Interface Errors | Packet errors, drops, collisions | Count | 5 minutes |
| Packets per Second | Packet rate (PPS) | PPS | 1-5 minutes |

**Configuration Examples**:

**SNMP Network Device Monitoring**:
```python
# Common SNMP OIDs for network interfaces
ifInOctets = '.1.3.6.1.2.1.2.2.1.10'      # Bytes received
ifOutOctets = '.1.3.6.1.2.1.2.2.1.16'     # Bytes transmitted
ifSpeed = '.1.3.6.1.2.1.2.2.1.5'          # Interface speed (bps)
ifOperStatus = '.1.3.6.1.2.1.2.2.1.8'     # Operational status

# Calculate utilization
utilization = ((ifInOctets + ifOutOctets) * 8 / interval) / ifSpeed * 100
```

**Prometheus SNMP Exporter**:
```yaml
# SNMP exporter configuration
modules:
  if_mib:
    walk:
      - interfaces
      - ifXTable
    metrics:
      - name: ifHCInOctets
        oid: 1.3.6.1.2.1.31.1.1.1.6
        type: counter
      - name: ifHCOutOctets
        oid: 1.3.6.1.2.1.31.1.1.1.10
        type: counter
```

#### 3.3.2 Network Services Monitoring

**Load Balancer Capacity**:
- Active connections
- Requests/connections per second
- SSL/TLS sessions
- Backend server health

**Firewall Capacity**:
- Concurrent connections
- New connections per second
- Throughput (Mbps/Gbps)
- CPU/memory utilization of firewall appliance

**Configuration varies by vendor**:
- F5 BIG-IP: iControl REST API
- Citrix NetScaler: NITRO API
- HAProxy: Stats socket or HTTP stats page
- Palo Alto Networks: XML API
- Fortinet FortiGate: REST API

### 3.4 Application Capacity Monitoring

#### 3.4.1 Application Performance Metrics

**Metrics to Collect**:

| Metric | Description | Unit | Collection Interval |
|--------|-------------|------|-------------------|
| Active Sessions | Current user sessions | Count | 1-5 minutes |
| Requests per Second | HTTP/API request rate | RPS | 1 minute |
| Response Time | Request latency (p50, p95, p99) | ms | 1 minute |
| Error Rate | Failed requests percentage | % | 1 minute |
| Thread Pool Utilization | Active threads / max threads | % | 1-5 minutes |
| Database Connection Pool | Active connections / max connections | % | 1-5 minutes |

**Configuration Examples**:

**Application Performance Monitoring (APM) Tools**:
- New Relic APM: Agent-based application instrumentation
- Datadog APM: Application tracing and metrics
- Dynatrace: OneAgent for automatic discovery and monitoring

**Custom Application Metrics**:

**Prometheus Client Libraries** (Python example):
```python
from prometheus_client import Gauge, Counter, Histogram, start_http_server

# Define metrics
active_sessions = Gauge('app_active_sessions', 'Number of active user sessions')
requests_total = Counter('app_requests_total', 'Total HTTP requests')
request_duration = Histogram('app_request_duration_seconds', 'Request duration')

# Update metrics in application code
active_sessions.set(get_active_session_count())
requests_total.inc()
with request_duration.time():
    process_request()

# Expose metrics on :8000/metrics
start_http_server(8000)
```

**StatsD** (application metrics collection):
```python
import statsd

# Initialize StatsD client
c = statsd.StatsClient('statsd.example.com', 8125)

# Send metrics
c.incr('api.requests')                      # Increment counter
c.gauge('api.active_users', 1523)           # Set gauge value
c.timing('api.response_time', 245)          # Record timing (ms)
```

#### 3.4.2 Message Queue Monitoring

**Queue Depth Metrics**:

**RabbitMQ**:
```bash
# CLI monitoring
rabbitmqctl list_queues name messages consumers

# HTTP API
curl -u guest:guest http://localhost:15672/api/queues
```

**Apache Kafka**:
```bash
# Consumer lag monitoring (messages behind)
kafka-consumer-groups.sh --bootstrap-server localhost:9092 --describe --group my-group
```

**AWS SQS**:
```python
import boto3

cloudwatch = boto3.client('cloudwatch')
response = cloudwatch.get_metric_statistics(
    Namespace='AWS/SQS',
    MetricName='ApproximateNumberOfMessagesVisible',
    Dimensions=[{'Name': 'QueueName', 'Value': 'my-queue'}],
    Statistics=['Average'],
    Period=300,
    StartTime=...,
    EndTime=...
)
```

### 3.5 Cloud Service Quota Monitoring

#### 3.5.1 AWS Service Quotas

**Monitor Service Limits**:
```python
import boto3

quotas = boto3.client('service-quotas')

# Get EC2 instance quota
response = quotas.get_service_quota(
    ServiceCode='ec2',
    QuotaCode='L-1216C47A'  # Running On-Demand instances
)

# List quotas approaching limits
response = quotas.list_service_quotas(ServiceCode='ec2')
for quota in response['Quotas']:
    if quota['UsageMetric']:
        utilization = get_usage(quota['UsageMetric']) / quota['Value'] * 100
        if utilization > 70:
            print(f"Warning: {quota['QuotaName']} at {utilization}%")
```

#### 3.5.2 Azure Subscription Limits

**Monitor Subscription Usage**:
```powershell
# Azure PowerShell
Get-AzVMUsage -Location "East US"

# Example output:
# Name              CurrentValue Limit Unit
# ----              ------------ ----- ----
# Virtual Machines  45           100   Count
# Total Regional vCPUs 180        200   Count
```

#### 3.5.3 GCP Quotas

**Monitor Project Quotas**:
```bash
# gcloud CLI
gcloud compute project-info describe --project=my-project

# Quotas listed under "quotas" section
# Example: CPUS, DISKS_TOTAL_GB, IN_USE_ADDRESSES
```

**Quota Alerting**:
- Configure Cloud Monitoring alerts when quotas reach 80% utilization
- Request quota increases proactively based on forecasts

---

## 4. Threshold Configuration

### 4.1 Threshold Definition Process

**Step 1: Establish Baseline Utilization**:
- Collect 2-4 weeks of utilization data for each resource
- Calculate average utilization and peak utilization
- Identify utilization patterns (business hours, daily cycles, weekly cycles)

**Step 2: Define Warning Thresholds**:
- **Purpose**: Trigger capacity planning before exhaustion
- **Typical Value**: 70-80% utilization
- **Adjustment Factors**:
  - Lead time to add capacity (lower threshold if long lead time)
  - Workload variability (lower threshold if highly variable)
  - Business criticality (lower threshold for critical systems)

**Example**: 
- Cloud VM (instant scaling): Warning at 80%
- Physical server (4-week procurement): Warning at 65%

**Step 3: Define Critical Thresholds**:
- **Purpose**: Immediate action required
- **Typical Value**: 85-95% utilization
- **Adjustment Factors**:
  - Headroom for bursts (ensure buffer for temporary spikes)
  - Resource type (memory exhaustion is more critical than CPU)

**Example**:
- CPU: Critical at 85% (allows 15% burst headroom)
- Memory: Critical at 90% (memory exhaustion causes crashes)
- Disk: Critical at 85% (applications may fail if disk fills)

**Step 4: Document Thresholds**:
- Create threshold configuration spreadsheet
- Document rationale for each threshold
- Review and approve thresholds with stakeholders

### 4.2 Threshold Configuration in Monitoring Tools

#### 4.2.1 Prometheus Alerting Rules

**Alert Configuration** (alert.rules.yml):
```yaml
groups:
- name: capacity_alerts
  interval: 60s
  rules:
  
  # CPU Warning
  - alert: HighCPUWarning
    expr: 100 - (avg by (instance) (irate(node_cpu_seconds_total{mode="idle"}[5m])) * 100) > 70
    for: 15m
    labels:
      severity: warning
      category: capacity
    annotations:
      summary: "CPU utilization warning on {{ $labels.instance }}"
      description: "CPU utilization is {{ $value }}% (threshold: 70%)"
  
  # CPU Critical
  - alert: HighCPUCritical
    expr: 100 - (avg by (instance) (irate(node_cpu_seconds_total{mode="idle"}[5m])) * 100) > 85
    for: 15m
    labels:
      severity: critical
      category: capacity
    annotations:
      summary: "CRITICAL: CPU utilization on {{ $labels.instance }}"
      description: "CPU utilization is {{ $value }}% (threshold: 85%)"
  
  # Disk Space Warning
  - alert: DiskSpaceWarning
    expr: (node_filesystem_avail_bytes{mountpoint="/"} / node_filesystem_size_bytes{mountpoint="/"}) * 100 < 25
    for: 15m
    labels:
      severity: warning
      category: capacity
    annotations:
      summary: "Disk space warning on {{ $labels.instance }}"
      description: "Disk space is {{ $value }}% free (threshold: 25% free = 75% used)"
  
  # Memory Warning
  - alert: HighMemoryWarning
    expr: (1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes)) * 100 > 75
    for: 15m
    labels:
      severity: warning
      category: capacity
    annotations:
      summary: "Memory utilization warning on {{ $labels.instance }}"
      description: "Memory utilization is {{ $value }}% (threshold: 75%)"
```

#### 4.2.2 Datadog Monitors

**Monitor Configuration** (via UI or API):
```json
{
  "name": "CPU Utilization Warning",
  "type": "metric alert",
  "query": "avg(last_15m):avg:system.cpu.user{*} by {host} > 70",
  "message": "@slack-capacity-team CPU utilization warning on {{host.name}}: {{value}}%",
  "tags": ["capacity", "cpu"],
  "options": {
    "thresholds": {
      "warning": 70,
      "critical": 85
    },
    "notify_no_data": false,
    "notify_audit": false
  }
}
```

#### 4.2.3 CloudWatch Alarms

**Alarm Configuration** (AWS CLI):
```bash
aws cloudwatch put-metric-alarm \
  --alarm-name "EC2-CPU-Warning-i-1234567890abcdef0" \
  --alarm-description "CPU utilization warning" \
  --metric-name CPUUtilization \
  --namespace AWS/EC2 \
  --statistic Average \
  --period 300 \
  --evaluation-periods 3 \
  --threshold 70 \
  --comparison-operator GreaterThanThreshold \
  --dimensions Name=InstanceId,Value=i-1234567890abcdef0 \
  --alarm-actions arn:aws:sns:us-east-1:123456789012:capacity-warnings
```

### 4.3 Dynamic Threshold Tuning

**Continuous Improvement**:
- Review threshold effectiveness monthly
- Identify false positives (alerts triggered but no real issue)
- Identify false negatives (capacity exhaustion without alert)
- Adjust thresholds based on operational experience

**Adaptive Thresholds** (advanced):
- Some tools support ML-based anomaly detection
- Thresholds adapt automatically based on historical patterns
- Examples: Datadog Anomaly Detection, Dynatrace Davis AI

---

## 5. Alerting Integration

### 5.1 Alert Routing Configuration

**Alert Severity Routing**:

| Severity | Recipients | Channels | Response Time |
|----------|-----------|----------|---------------|
| **Warning** | Capacity planning team | Email | Review within 2 business days |
| **Critical** | IT operations (24x7) | Email + SMS + PagerDuty | Immediate (within 1 hour) |
| **Emergency** (capacity exhausted) | On-call engineer + management | Phone + SMS + Incident management | Immediate |

### 5.2 Email Alerting

**SMTP Configuration Example** (Prometheus Alertmanager):
```yaml
# alertmanager.yml
global:
  smtp_smarthost: 'smtp.example.com:587'
  smtp_from: 'alertmanager@example.com'
  smtp_auth_username: 'alertmanager@example.com'
  smtp_auth_password: 'password'

route:
  group_by: ['alertname', 'cluster', 'severity']
  group_wait: 30s
  group_interval: 5m
  repeat_interval: 4h
  receiver: 'capacity-team'
  
  routes:
  - match:
      severity: critical
    receiver: 'on-call'

receivers:
- name: 'capacity-team'
  email_configs:
  - to: 'capacity-team@example.com'
    headers:
      Subject: '[Capacity Warning] {{ .GroupLabels.alertname }}'

- name: 'on-call'
  email_configs:
  - to: 'oncall@example.com'
    headers:
      Subject: '[CRITICAL CAPACITY] {{ .GroupLabels.alertname }}'
```

### 5.3 Incident Management Integration

**PagerDuty Integration**:
```yaml
# Prometheus Alertmanager PagerDuty receiver
receivers:
- name: 'pagerduty-critical'
  pagerduty_configs:
  - service_key: 'YOUR_PAGERDUTY_SERVICE_KEY'
    description: '{{ .GroupLabels.alertname }}: {{ .GroupLabels.instance }}'
    severity: '{{ .CommonLabels.severity }}'
```

**ServiceNow Integration**:
- Configure webhook to create incidents via ServiceNow REST API
- Map alert severity to ServiceNow priority
- Attach alert details to incident description

**Jira Integration**:
- Create Jira issues for capacity planning tasks (warning alerts)
- Auto-assign to capacity planning team
- Track remediation in Jira workflow

### 5.4 Slack/Microsoft Teams Integration

**Slack Webhook**:
```yaml
# Prometheus Alertmanager Slack receiver
receivers:
- name: 'slack-capacity'
  slack_configs:
  - api_url: 'https://hooks.slack.com/services/YOUR/SLACK/WEBHOOK'
    channel: '#capacity-alerts'
    title: '{{ .GroupLabels.alertname }}'
    text: '{{ range .Alerts }}{{ .Annotations.summary }}{{ end }}'
    color: '{{ if eq .Status "firing" }}danger{{ else }}good{{ end }}'
```

---

## 6. Data Retention Configuration

### 6.1 Retention Policy Implementation

**Tiered Retention**:

| Data Granularity | Retention Period | Purpose | Storage Requirement |
|------------------|------------------|---------|---------------------|
| Raw metrics (1-min) | 30-90 days | Incident investigation, short-term trending | High (SSD recommended) |
| Hourly aggregates | 12-24 months | Medium-term trend analysis, forecasting | Medium (HDD acceptable) |
| Daily aggregates | 36-60 months | Long-term strategic planning | Low (HDD/archive) |

### 6.2 Prometheus Retention Configuration

```yaml
# Prometheus command-line flags
prometheus \
  --storage.tsdb.path=/var/lib/prometheus \
  --storage.tsdb.retention.time=90d \
  --storage.tsdb.retention.size=50GB
  
# Downsampling with VictoriaMetrics or Thanos (separate tools)
# Provides long-term storage with automatic downsampling
```

### 6.3 Commercial Tool Retention

**Datadog**:
- Default: Full-resolution metrics for 15 months
- Custom retention configurable via support

**CloudWatch**:
- High-resolution metrics (1-minute): 15 days
- Standard metrics (5-minute): 63 days
- 1-hour metrics: 15 months
- Export to S3 for longer retention

### 6.4 Capacity Planning for Monitoring Data

**Estimate Monitoring Storage Requirements**:

```
Metrics per server: ~500 metrics
Servers to monitor: 100
Data points per minute: 500 metrics × 100 servers = 50,000 data points/min
Data points per day: 50,000 × 60 min × 24 hr = 72,000,000 data points/day
Storage per data point: ~16 bytes (Prometheus TSDB)
Daily storage: 72M × 16 bytes = 1.15 GB/day
90-day retention: 1.15 GB × 90 = 103.5 GB
```

**Plan monitoring infrastructure capacity accordingly**:
- Disk space for metrics database
- CPU/memory for query processing
- Network bandwidth for metric collection

---

## 7. Dashboard Creation

### 7.1 Capacity Dashboard Design

**Dashboard Audience**:
- **Executive Dashboard**: High-level capacity health (for CIO, CFO)
- **Operational Dashboard**: Detailed real-time utilization (for IT operations)
- **Planning Dashboard**: Trends and forecasts (for capacity planning team)

### 7.2 Dashboard Metrics and Visualizations

**Essential Capacity Metrics**:

1. **Capacity Health Score**: Percentage of resources below warning threshold
2. **Resources at Risk**: Count of resources at warning/critical
3. **Capacity Headroom**: Remaining capacity per resource type
4. **Utilization Trends**: 30/60/90-day utilization trends
5. **Top Consumers**: Highest-utilized resources (top 10)

**Visualization Types**:
- **Gauges**: Current utilization percentage
- **Time Series Graphs**: Utilization over time
- **Heatmaps**: Utilization across many resources
- **Bar Charts**: Resource comparison
- **Pie Charts**: Capacity distribution by resource type

### 7.3 Grafana Dashboard Example

```json
{
  "dashboard": {
    "title": "Capacity Management Overview",
    "panels": [
      {
        "title": "Capacity Health Score",
        "type": "gauge",
        "targets": [
          {
            "expr": "(count(node_cpu_seconds_total < 70) / count(node_cpu_seconds_total)) * 100"
          }
        ],
        "thresholds": [
          { "value": 95, "color": "green" },
          { "value": 85, "color": "yellow" },
          { "value": 0, "color": "red" }
        ]
      },
      {
        "title": "CPU Utilization Trend (30 days)",
        "type": "graph",
        "targets": [
          {
            "expr": "100 - (avg(irate(node_cpu_seconds_total{mode=\"idle\"}[5m])) * 100)"
          }
        ]
      }
    ]
  }
}
```

---

## 8. Assessment Tool Usage

### 8.1 Capacity Utilization Assessment Workbook

**Purpose**: Document current capacity status in standardized Excel workbook for compliance and reporting.

**Generation**: Use Python script `generate_assessment_1_capacity_utilization.py`

```bash
# Generate assessment workbook
python3 generate_assessment_1_capacity_utilization.py

# Output: ISMS-IMP-A.8.6.1_Capacity_Utilization_Assessment.xlsx
```

### 8.2 Workbook Completion Process

**Step 1: Generate Workbook**:
- Run Python script to create blank assessment workbook
- Workbook contains 10 sheets with formulas and validations

**Step 2: Populate Resource Inventory**:
- Export monitoring data (CSV, JSON, or manual collection)
- Populate Compute_Resources, Storage_Resources, Network_Resources, Application_Resources, Cloud_Resources sheets
- Use dropdown menus for consistent status values

**Step 3: Review Calculations**:
- Utilization percentages auto-calculate
- Threshold status auto-applies (OK, Warning, Critical)
- Threshold_Summary sheet aggregates data

**Step 4: Document Evidence**:
- Populate Evidence_Register sheet with supporting documentation
- Reference monitoring dashboards, data exports, configuration files

**Step 5: Review and Approval**:
- Capacity planning team reviews for completeness
- Infrastructure manager approves
- Save final version with date stamp

**Step 6: Distribution**:
- Distribute to IT management, capacity planning team
- File in capacity management evidence repository
- Feed into Dashboard (using normalization script)

### 8.3 Assessment Frequency

- **Monthly**: Capacity utilization assessment
- **Quarterly**: Feed into capacity forecasting assessment
- **Annually**: Comprehensive review for audit preparation

---

## 9. Implementation Checklist

### 9.1 Pre-Implementation

- [ ] Capacity management policy approved (ISMS-POL-A.8.6-S2)
- [ ] Budget allocated for monitoring tools
- [ ] Monitoring tool selected and procured
- [ ] Infrastructure inventory completed
- [ ] Capacity planning team identified

### 9.2 Tool Deployment

- [ ] Monitoring tool deployed (production or production-ready)
- [ ] Monitoring agents installed on critical systems
- [ ] Monitoring data collection verified
- [ ] Historical data retention configured
- [ ] Dashboard access provisioned for capacity team

### 9.3 Threshold and Alerting

- [ ] Baseline utilization data collected (2-4 weeks)
- [ ] Thresholds defined and documented
- [ ] Warning thresholds configured in monitoring tool
- [ ] Critical thresholds configured in monitoring tool
- [ ] Email alerting tested
- [ ] Incident management integration tested (if applicable)
- [ ] Escalation procedures documented and trained

### 9.4 Dashboard and Reporting

- [ ] Capacity dashboard created in monitoring tool
- [ ] Dashboard metrics validated
- [ ] Dashboard access granted to stakeholders
- [ ] Assessment workbook generator tested
- [ ] First capacity utilization assessment completed

### 9.5 Documentation and Training

- [ ] Monitoring tool configuration documented
- [ ] Threshold rationale documented
- [ ] Alert response procedures documented
- [ ] Capacity team trained on monitoring tool
- [ ] IT operations trained on alert response
- [ ] Evidence repository established

---

## Appendix A: Monitoring Tool Comparison Matrix

| Feature | Prometheus | Datadog | CloudWatch | Zabbix | Nagios |
|---------|-----------|---------|------------|--------|---------|
| **Deployment** | Self-hosted | SaaS | Cloud-native | Self-hosted | Self-hosted |
| **Cost** | Free | $15-31/host/mo | Pay-per-use | Free | Free |
| **Compute Metrics** | ✅ Excellent | ✅ Excellent | ✅ Good | ✅ Excellent | ✅ Good |
| **Storage Metrics** | ✅ Excellent | ✅ Excellent | ✅ Good | ✅ Excellent | ✅ Good |
| **Network Metrics** | ✅ Good (SNMP) | ✅ Excellent | âš ï¸ Limited | ✅ Excellent | ✅ Good (SNMP) |
| **Cloud Integration** | âš ï¸ Exporters req | ✅ Native | ✅ Native (AWS) | âš ï¸ Manual | âš ï¸ Manual |
| **Alerting** | ✅ Excellent | ✅ Excellent | ✅ Good | ✅ Good | ✅ Good |
| **Dashboards** | ✅ Grafana | ✅ Built-in | ✅ Built-in | ✅ Built-in | âš ï¸ Limited |
| **Data Retention** | Configurable | 15 months | 15 months | Configurable | Limited |
| **Learning Curve** | Medium | Low | Low | High | High |
| **Best For** | Cloud-native, K8s | Hybrid cloud | AWS-only | On-prem, mixed | Traditional infra |

---

**End of Document ISMS-IMP-A.8.6-S1**

---

**Document Status**: DRAFT - Pending Approval  
**Next Steps**: 
1. Review by capacity planning team and infrastructure team
2. Approval by Infrastructure Manager and CISO
3. Tool selection and procurement
4. Phased implementation (critical systems first)
5. Training for capacity and operations teams
6. First capacity utilization assessment
