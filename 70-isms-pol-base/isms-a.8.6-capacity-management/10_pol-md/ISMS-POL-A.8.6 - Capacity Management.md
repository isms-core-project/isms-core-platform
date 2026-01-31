# ISMS-POL-A.8.6 – Capacity Management

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | Capacity Management |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.8.6 |
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
| 1.0 | [Date] | CISO / Information Security Manager | Initial consolidated policy for ISO 27001:2022 first certification |

**Review Cycle**: Annual (aligned with capacity planning cycle)  
**Next Review Date**: [Effective Date + 12 months]  

**Approval Chain**:
- Primary: Chief Information Security Officer (CISO)
- Technical Review: IT Operations Manager / Infrastructure Manager
- Financial Review: Chief Financial Officer (CFO)
- Compliance Review: Legal/Compliance Officer
- Final Authority: Chief Information Officer (CIO)

**Related Documents**: 
- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-IMP-A.8.6.1 (Capacity Monitoring Implementation)
- ISMS-IMP-A.8.6.2 (Capacity Forecasting and Planning)
- ISMS-IMP-A.8.6.3 (Capacity Management Assessment)
- ISO/IEC 27001:2022 Control A.8.6

---

## Executive Summary

This policy establishes [Organization]'s requirements for capacity management to ensure sufficient infrastructure and application capacity in accordance with ISO/IEC 27001:2022 Control A.8.6.

**Scope**: This policy applies to all infrastructure resources (compute, storage, network, application capacity) supporting business operations, all personnel involved in capacity planning and infrastructure management, and all monitoring and capacity management technologies regardless of deployment model (on-premises, cloud, hybrid).

**Purpose**: Define organizational requirements for capacity management implementation and governance. This policy establishes WHAT capacity management protection is required, WHEN capacity planning must occur, and WHO is accountable. Implementation procedures (HOW monitoring, forecasting, and planning are performed) are documented separately in ISMS-IMP-A.8.6 series.

**Regulatory Alignment**: This policy addresses mandatory compliance requirements per ISMS-POL-00 (Regulatory Applicability Framework), including ISO/IEC 27001:2022 Control A.8.6. Conditional sector-specific requirements (FINMA Circular 2023/1, DORA Article 11, NIS2 Article 21) apply where [Organization]'s business activities trigger applicability. Informational references include ITIL 4 Capacity Management and NIST SP 800-53 AU-6.

**Why Capacity Management Matters**: Organizations face critical operational and business risks when capacity is not properly managed: service outages due to resource exhaustion, performance degradation from contention, reactive emergency procurement at premium pricing, security risks from insufficient logging capacity, compliance violations from SLA breaches, and strategic inability to support business growth. This framework uses systems engineering methodology through systematic monitoring, data-driven forecasting, proactive planning, and continuous optimization.

---

## 1. Control Alignment & Scope

### 1.1 ISO/IEC 27001:2022 Control A.8.6

**ISO/IEC 27001:2022 Annex A.8.6 - Capacity Management**

> *The use of resources should be monitored and tuned, and projections of future capacity requirements should be made to ensure the required system performance and to inform investment decisions.*

**Control Objective**: Ensure adequate resources (compute, storage, network, application) are available to meet current and future performance and availability requirements through monitoring, tuning, projection, performance assurance, and investment planning.

**This Policy Addresses**:
- Capacity monitoring requirements across all infrastructure and application resources
- Capacity thresholds and alerting to enable proactive capacity planning
- Capacity forecasting methodology based on trend analysis and business growth
- Capacity planning process aligned with budget and procurement cycles
- Roles and responsibilities for capacity management governance
- Integration with [Organization]'s risk assessment and monitoring processes

### 1.2 What This Policy Does

This policy:
- **Defines** capacity management control requirements aligned with organizational risk assessment
- **Establishes** governance framework for capacity planning decision-making
- **Specifies** mandatory capacity monitoring, forecasting, and planning requirements
- **References** applicable regulatory requirements per ISMS-POL-00
- **Identifies** organizational roles and responsibilities for capacity management
- **Provides** assessment methodology framework for measuring compliance effectiveness

### 1.3 What This Policy Does NOT Do

This policy does NOT:
- **Specify technical implementation procedures** (see ISMS-IMP-A.8.6.1, ISMS-IMP-A.8.6.2, ISMS-IMP-A.8.6.3)
- **Define specific monitoring tool configurations** (monitoring tool selection based on [Organization]'s infrastructure and risk assessment)
- **List approved monitoring tools or vendors** (technology selection based on [Organization]'s technical environment)
- **Provide step-by-step forecasting procedures** (see ISMS-IMP-A.8.6.2 - Capacity Forecasting and Planning)
- **Replace infrastructure planning processes** (capacity management complements, not replaces, architecture planning)

**Rationale**: Separating policy requirements from implementation guidance enables policy stability despite evolving monitoring technologies and forecasting methods, technical agility for new tools without policy revision, clear distinction between governance (policy) and execution (implementation), focused audit scope (auditors verify policy compliance, not tool configurations), and adaptability for different organizational contexts and infrastructure types.

### 1.4 Scope

**This policy applies to**:

**Infrastructure Resources**:
- Compute capacity (servers, virtual machines, containers, cloud instances - CPU, memory)
- Storage capacity (disk space, database storage, backup storage, archive storage)
- Network capacity (bandwidth, throughput, connections, load balancer capacity)
- Application capacity (concurrent users, transaction rates, API rate limits, queue depths)
- Cloud capacity (cloud service quotas, limits, instance counts, cost thresholds)
- Physical infrastructure (power capacity, cooling capacity, rack space per A.7.11)

**Coverage**:
- All infrastructure supporting production business operations (mandatory monitoring)
- Development, test, and quality assurance environments (recommended monitoring)
- Business continuity and disaster recovery sites (capacity for failover scenarios per A.5.30)
- Third-party hosted infrastructure (where [Organization] has capacity management responsibility)

**Personnel**:
- Executive management (capacity planning budget approval, strategic decision-making)
- Capacity planning team (monitoring, forecasting, planning, reporting)
- IT operations team (day-to-day monitoring, alert response, capacity tuning)
- Application owners / system owners (capacity planning for their systems, business growth projections)
- Financial controller / CFO (capacity budget approval, financial reporting)
- Chief Information Officer (overall accountability, capacity expansion approval)
- Chief Information Security Officer (security system capacity, compliance verification)

**Out of Scope**:
- Application performance tuning (covered under application optimization, not capacity management)
- Software licensing management (covered under asset management, though capacity planning informs licensing decisions)
- Network security capacity planning (covered under A.8.20 - Networks Security, though integrated with capacity management)

### 1.5 Regulatory Applicability

Regulatory requirements are categorized per **ISMS-POL-00 (Regulatory Applicability Framework)**:

**Mandatory Compliance (Tier 1)**:
- **ISO/IEC 27001:2022**: Control A.8.6 (Capacity Management)
- This control is mandatory for all organizations implementing ISO/IEC 27001

**Conditional Applicability (Tier 2)**:
- **FINMA Circular 2023/1** (if Swiss financial institution):
  - Margin 50-62: ICT operational resilience includes capacity management to ensure availability
- **DORA - Digital Operational Resilience Act** (if EU financial entity):
  - Article 11: ICT capacity planning required to ensure availability and performance
- **NIS2 - Network and Information Security Directive** (if essential or important entity):
  - Article 21(2): Business continuity measures include capacity planning for critical systems

**Informational Reference (Tier 3)**:
- **ITIL 4**: IT Service Management (Capacity Management process best practices)
- **ISO/IEC 20000**: IT Service Management (capacity management requirements)
- **NIST SP 800-53**: AU-6 (Audit Record Review, Analysis, and Reporting - includes capacity monitoring)

For complete regulatory categorization, refer to ISMS-POL-00.

### 1.6 Policy Integration

Capacity management does not operate in isolation. This control integrates with:

**A.8.16 - Monitoring Activities**  
Capacity management depends on monitoring infrastructure (metrics collection, alerting, dashboards). Monitoring provides the data foundation for capacity analysis. Capacity metrics are a subset of overall monitoring scope.

**A.8.14 - Redundancy of Information Processing Facilities**  
Redundant systems require capacity planning to ensure failover capacity is sufficient. Capacity management must account for both normal operations and failure scenarios. Redundancy design decisions (active/active, active/passive) have capacity implications.

**A.8.13 - Information Backup**  
Backup storage capacity must be planned based on data growth rates. Backup window capacity (network bandwidth, deduplication performance) must be sufficient for backup completion. Capacity management tracks backup storage utilization and forecasts growth.

**A.7.11 - Supporting Utilities**  
Physical infrastructure capacity (power, cooling, HVAC, rack space) supports IT capacity. Power capacity planning ensures electrical supply for compute infrastructure. Cooling capacity must scale with compute density.

**A.5.30 - ICT Readiness for Business Continuity**  
Business continuity requires capacity planning for alternate sites and disaster recovery infrastructure. Capacity must support business continuity scenarios (failover, workload migration). Recovery time objectives (RTO) depend on available capacity at recovery sites.

**A.8.7 - Protection Against Malware**  
Malware outbreaks can cause abnormal capacity consumption (cryptominers, botnets). Capacity monitoring may detect malware through unusual resource utilization patterns.

**A.8.20 - Networks Security**  
Network capacity (bandwidth, throughput, connections) is part of overall capacity management. Network security controls (firewalls, IDS/IPS) have capacity limitations that must be managed.

### 1.7 Definitions and Terminology

**Capacity Management**  
The process of ensuring that adequate infrastructure and application resources are available to meet current and future performance and availability requirements through monitoring, forecasting, and planning.

**Capacity Monitoring**  
The continuous or periodic measurement of resource utilization (CPU, memory, disk, network, application metrics) to understand current capacity consumption and track trends over time.

**Capacity Planning**  
The proactive process of determining future capacity requirements based on forecasts, business plans, and growth projections, and developing plans for capacity expansion, optimization, or acquisition.

**Capacity Threshold**  
A defined utilization level that triggers alerts or actions when exceeded:
- **Warning Threshold**: Utilization level indicating capacity planning should begin (commonly 70-80%)
- **Critical Threshold**: Utilization level requiring immediate action to add capacity or reduce load (commonly 85-95%)
- **Maximum Capacity**: Theoretical or practical limit of a resource (100% or defined maximum)

**Utilization**  
The percentage or proportion of available capacity currently in use. Calculated as: (Used Capacity / Total Available Capacity) × 100%

**Headroom**  
The remaining unused capacity available for growth, peaks, or unexpected demand. Calculated as: Total Available Capacity - Current Utilization

**Peak Utilization**  
The maximum observed utilization over a defined time period (daily peak, monthly peak, annual peak). Peak utilization is critical for capacity planning as sustained operation at peak levels indicates insufficient capacity.

**Average Utilization**  
The mean utilization over a defined time period. Average utilization provides baseline understanding but may mask peak utilization issues. Capacity planning should consider both average and peak utilization.

**Trend Analysis**  
The statistical examination of historical capacity utilization data to identify patterns, growth rates, and seasonal variations. Trend analysis forms the foundation for capacity forecasting.

**Capacity Forecast**  
A projection of future capacity requirements based on historical trends, business plans, and growth assumptions. Forecasts typically project 6-12 months forward and are updated regularly as new data becomes available.

**Growth Rate**  
The rate at which capacity utilization is increasing over time, typically expressed as a percentage per month, quarter, or year. Growth rate is calculated from historical trend analysis and used in forecasting.

**Capacity Exhaustion**  
The point at which a resource reaches its maximum capacity and can no longer support additional load. Capacity exhaustion leads to service degradation or outages. Forecasting aims to predict capacity exhaustion dates to enable proactive expansion.

**Right-Sizing**  
The process of matching resource allocation to actual utilization requirements to eliminate over-provisioning (wasted capacity) or under-provisioning (insufficient capacity). Right-sizing optimizes cost and performance.

**Resource Consolidation**  
The process of combining workloads onto fewer resources to improve utilization efficiency and reduce infrastructure sprawl. Examples: virtual machine consolidation, database consolidation, server consolidation.

**Scalability**  
The ability of a system to handle increased load by adding resources:
- **Vertical Scaling (Scale-Up)**: Adding more capacity to existing resources (more CPU, memory, disk)
- **Horizontal Scaling (Scale-Out)**: Adding more resources to distribute load (more servers, instances, nodes)

---

## 2. Capacity Management Requirements

### 2.1 Capacity Monitoring Requirements

[Organization] SHALL implement systematic capacity monitoring for all infrastructure and application resources supporting business operations.

**Monitoring Coverage**:
- **Production Systems**: 100% of production infrastructure and business-critical applications SHALL be monitored
- **Non-Production Systems**: 90% of development, test, and quality assurance environments SHOULD be monitored
- **Cloud Infrastructure**: All cloud services, instances, and resources SHALL be monitored
- **Network Infrastructure**: Network bandwidth, throughput, and connection capacity SHALL be monitored
- **Physical Infrastructure**: Power, cooling, and rack space capacity SHALL be monitored per A.7.11

**Monitoring Frequency**:
- **Real-time Metrics**: 1-5 minute intervals for operational monitoring and alerting
- **Historical Aggregates**: Hourly, daily, weekly, and monthly aggregates for trend analysis
- **Baseline Collection**: Minimum 2-4 weeks of data collection before threshold configuration

**Data Retention**:
- **Raw Metrics** (1-5 min granularity): 30-90 days minimum for incident investigation
- **Hourly Aggregates**: 12-24 months minimum for medium-term trend analysis and forecasting
- **Daily Aggregates**: 36-60 months recommended for long-term strategic planning

[Organization] MAY use any monitoring tool or platform (open-source or commercial, on-premises or cloud-based) provided it meets the monitoring requirements defined in this policy. Tool selection is based on [Organization]'s technical environment, budget, and risk assessment.

### 2.2 Resource Types to Monitor

[Organization] SHALL monitor capacity for the following resource categories:

**2.2.1 Compute Capacity**

**Physical Servers** (if applicable):
- CPU utilization (percentage, per-core metrics where available)
- Memory (RAM) utilization (percentage, available memory)
- System load averages (1-min, 5-min, 15-min load)

**Virtual Machines** (if applicable):
- VM CPU utilization and CPU ready time (hypervisor contention)
- VM memory utilization and memory ballooning (hypervisor memory pressure)
- Hypervisor-level capacity (ESXi cluster CPU/memory, Azure subscription limits)

**Containers and Kubernetes** (if applicable):
- Container CPU and memory limits vs. usage
- Kubernetes node capacity (allocatable resources vs. requested resources)
- Pod counts per node and cluster-wide capacity

**Cloud Instances** (if applicable):
- EC2/VM instance CPU and memory utilization
- Auto-scaling metrics (scale-in/scale-out triggers)
- Cloud service quotas and limits (instances per region, vCPU limits)

**2.2.2 Storage Capacity**

**Local and Shared Storage**:
- Disk space utilization per volume/filesystem (percentage used, bytes available)
- Inodes utilization (for Linux/Unix filesystems - running out of inodes before disk space)
- Storage performance metrics (IOPS, latency - performance degradation indicates capacity constraints)

**Database Storage**:
- Database file sizes and growth rates
- Transaction log sizes and growth rates
- Table and index space utilization
- Tempdb usage (SQL Server) or temp tablespace usage (Oracle)

**Backup Storage**:
- Backup repository capacity (target storage, deduplication appliances)
- Backup retention capacity (capacity required to meet retention policies)
- Backup growth rates (incremental and full backup sizes)

**Archive Storage**:
- Archive tier capacity (cold storage, tape, cloud archive)
- Archive growth rates and retention compliance

**2.2.3 Network Capacity**

**Network Bandwidth**:
- Interface bandwidth utilization (percentage of link capacity)
- Sustained throughput vs. burst capacity
- Network latency (latency increase may indicate congestion before bandwidth saturation)

**Network Connections**:
- Firewall connection table utilization
- Load balancer connection limits
- NAT translation table capacity

**Network Services**:
- DNS query capacity (queries per second vs. server capacity)
- DHCP scope utilization (available IP addresses vs. allocated)
- VPN concentrator capacity (concurrent tunnels, throughput)

**2.2.4 Application Capacity**

**User Sessions and Connections**:
- Concurrent user sessions (application-level, web server sessions)
- Database connection pool utilization
- Application server thread pool utilization
- WebSocket or persistent connection counts

**Transaction Rates**:
- Requests per second (web server, API gateway)
- Transactions per second (database, message queue)
- Batch job processing capacity (jobs per hour, queue depth)

**Queue Depth**:
- Message queue depth (RabbitMQ, Kafka, SQS queues)
- Job queue backlog (background job processors)
- Request queues (web server request queues, load balancer queues)

**API Rate Limits**:
- API calls per second vs. rate limits
- Third-party API quota consumption (external SaaS APIs)
- Webhook delivery capacity

**2.2.5 Cloud Capacity** (if applicable)

**Cloud Service Quotas**:
- AWS service limits (EC2 instances, VPCs, EBS volumes, etc.)
- Azure subscription limits (VMs, storage accounts, network interfaces)
- GCP project quotas (compute instances, persistent disks, networks)

**Cloud Cost Thresholds**:
- Monthly cloud spend vs. budget
- Cost anomaly detection (sudden cost spikes indicating capacity issues or misconfigurations)
- Reserved capacity utilization (reserved instances, savings plans)

**Cloud-Specific Metrics**:
- Lambda/Functions invocation counts vs. concurrency limits
- Container registry storage
- Serverless database capacity units

### 2.3 Capacity Thresholds and Alerting

[Organization] SHALL define and implement capacity thresholds for all monitored resources.

**2.3.1 Threshold Definitions**

**Warning Threshold**:
- **Purpose**: Trigger capacity planning activities before capacity exhaustion
- **Typical Range**: 70-80% utilization
- **Action**: Begin capacity planning, forecast review, prepare expansion plan
- **Timing**: Must provide sufficient lead time for planned capacity additions (considering procurement/provisioning lead times)

**Critical Threshold**:
- **Purpose**: Trigger immediate action to prevent capacity exhaustion
- **Typical Range**: 85-95% utilization
- **Action**: Immediate capacity addition, workload reduction, or resource reallocation
- **Timing**: Requires emergency response within business hours or escalation after hours

**Maximum Capacity**:
- **Purpose**: Absolute limit of resource capacity
- **Value**: 100% or vendor-defined maximum
- **Impact**: Capacity exhaustion leads to service degradation or outages

**2.3.2 Threshold Configuration**

Thresholds SHALL be configured based on:

**Resource Type Considerations**:
- **Compute (CPU)**: Warning 70%, Critical 85% (allows for burst capacity)
- **Memory (RAM)**: Warning 75%, Critical 90% (memory exhaustion causes crashes)
- **Disk Space**: Warning 75%, Critical 85% (application-specific - databases may need lower thresholds)
- **Network Bandwidth**: Warning 70%, Critical 85% (sustained high utilization impacts latency)
- **Application Sessions**: Warning 75%, Critical 90% (based on licensed/architectural limits)

**Workload Characteristics**:
- **Steady-State Workloads**: Lower thresholds (more predictable)
- **Bursty Workloads**: Higher thresholds with burst headroom
- **Business-Critical Systems**: Lower thresholds (more conservative)
- **Development/Test Systems**: Higher thresholds (acceptable risk)

**Lead Time Requirements**:
- **Cloud Resources** (instant provisioning): Higher thresholds acceptable (80-85% warning)
- **Physical Infrastructure** (weeks-months procurement): Lower thresholds required (65-70% warning)

**Threshold Tuning**: Thresholds SHALL be reviewed quarterly and tuned based on false positive alert rates, near-miss incidents, workload pattern changes, and business criticality changes.

**2.3.3 Alerting Requirements**

[Organization] SHALL implement alerting for capacity threshold breaches:

**Alert Routing**:
- **Warning Alerts**: Route to capacity planning team during business hours
- **Critical Alerts**: Route to IT operations 24x7 with escalation procedures
- **Maximum Capacity Alerts**: Route to on-call engineer immediately with executive escalation

**Alert Content**:
- Resource identification (server name, storage volume, application)
- Current utilization and threshold exceeded
- Trend information (rate of growth)
- Projected time to capacity exhaustion
- Recommended actions

**Alert Channels**:
- Email for warning-level alerts
- SMS/push notifications for critical alerts
- Integration with incident management system (ServiceNow, Jira, PagerDuty)
- Dashboard notifications (visual indicators)

**Alert Deduplication**: Alerting system SHALL deduplicate alerts to prevent alert fatigue (single alert per incident, not continuous alerting).

**Alert Acknowledgment**: Critical alerts SHALL require acknowledgment within 30 minutes, with escalation if not acknowledged.

**2.3.4 Escalation Procedures**

Capacity alerts SHALL escalate as follows:

**Level 1 - Warning Threshold**:
- Notify: Capacity planning team
- Timeframe: Review within 2 business days
- Action: Update forecast, develop capacity expansion plan

**Level 2 - Critical Threshold**:
- Notify: IT operations team + infrastructure manager
- Timeframe: Immediate response required (within 1 hour)
- Action: Implement immediate mitigation (cleanup, optimization, emergency capacity)

**Level 3 - Repeated Critical Alerts or Capacity Exhaustion**:
- Notify: IT Director/CIO + CISO
- Timeframe: Immediate (executive briefing within 4 hours)
- Action: Emergency capacity procurement, service degradation communication, root cause analysis

### 2.4 Capacity Forecasting Requirements

[Organization] SHALL develop capacity forecasts for all critical infrastructure and application resources.

**Forecasting Methodology**:
- **Trend Analysis**: Statistical analysis of historical utilization data to identify growth patterns
- **Growth Rate Calculation**: Determine percentage growth per month, quarter, year
- **Linear Regression**: Project future utilization based on historical linear trends
- **Seasonal Adjustment**: Account for known seasonal patterns (year-end processing, tax season, holiday peaks)
- **Business Growth Integration**: Incorporate business plans, new product launches, marketing campaigns

**Forecasting Horizon**:
- **Short-term**: 3-6 months (tactical planning)
- **Medium-term**: 6-12 months (budget planning)
- **Long-term**: 12-24 months (strategic planning)

**Forecasting Frequency**:
- **Monthly**: Update short-term forecasts with latest utilization data
- **Quarterly**: Comprehensive forecast review including business plan changes
- **Annually**: Long-term strategic forecast aligned with annual budget cycle

**Forecast Accuracy**:
- **Target Accuracy**: Within ±15% of actual utilization at forecast date
- **Accuracy Validation**: Compare previous forecasts to actual utilization quarterly
- **Continuous Improvement**: Refine forecasting methodology based on accuracy validation

**Forecast Documentation**:
- Forecast assumptions (growth rate, business plans, seasonal factors)
- Forecast methodology (trend analysis, regression model)
- Confidence intervals (optimistic, realistic, pessimistic scenarios)
- Capacity exhaustion dates (if no expansion occurs)

### 2.5 Capacity Planning Requirements

[Organization] SHALL implement a structured capacity planning process.

**Planning Cycle**:
- **Monthly Review**: Review capacity alerts, near-miss events, short-term forecasts
- **Quarterly Planning**: Comprehensive capacity planning with 12-month horizon
- **Annual Budget**: Long-term capacity planning aligned with annual budget cycle

**Capacity Expansion Planning**:
- **Trigger Points**: When forecasts predict capacity exhaustion within planning horizon
- **Lead Time Consideration**: Account for procurement lead time, deployment time, testing time
- **Sizing Decisions**: Determine how much capacity to add (incremental vs. large step increases)
- **Technology Refresh**: Integrate capacity expansion with hardware refresh cycles

**Budget Planning**:
- **Capital Expenditure (CapEx)**: Hardware procurement, infrastructure builds
- **Operating Expenditure (OpEx)**: Cloud services, managed services, maintenance
- **Cost-Benefit Analysis**: Compare cost of proactive capacity vs. cost of outages/emergency procurement

**Approval Process**:
- **Routine Capacity**: Approved by IT Director/CIO within approved budget
- **Major Capacity**: Requires CFO approval for budget impact
- **Emergency Capacity**: Fast-track approval by CIO with subsequent executive notification

### 2.6 Capacity Testing Requirements

[Organization] SHALL conduct capacity testing to validate capacity planning assumptions.

**Load Testing**:
- **Purpose**: Verify system capacity under expected production load
- **Frequency**: Before major releases, annually for existing systems
- **Scope**: Application capacity, database capacity, network capacity

**Stress Testing**:
- **Purpose**: Determine system breaking point and maximum capacity
- **Frequency**: Before production deployment, after major infrastructure changes
- **Scope**: Peak load scenarios, sustained high utilization

**Scalability Testing**:
- **Purpose**: Verify horizontal and vertical scaling capabilities
- **Frequency**: Before implementing auto-scaling, after architecture changes
- **Scope**: Application scalability, database scalability, cloud auto-scaling

### 2.7 Capacity Optimization Requirements

[Organization] SHALL continuously optimize capacity utilization.

**Right-Sizing**:
- **Over-Provisioned Resources**: Identify resources consistently below 30% utilization for downsizing
- **Under-Provisioned Resources**: Identify resources frequently exceeding thresholds for upsizing
- **Cloud Instance Optimization**: Right-size cloud instances based on utilization patterns

**Resource Consolidation**:
- **Virtual Machine Consolidation**: Consolidate low-utilization VMs onto fewer hosts
- **Database Consolidation**: Consolidate databases onto shared instances where appropriate
- **Application Consolidation**: Consolidate microservices or applications with complementary load patterns

**Capacity Reclamation**:
- **Decommissioning**: Remove unused or retired systems
- **Cleanup**: Delete obsolete data, old logs, unused files
- **Archiving**: Move infrequently accessed data to archive tier

### 2.8 Capacity Reporting Requirements

[Organization] SHALL produce regular capacity reports to management.

**2.8.1 Monthly Capacity Report**

The capacity planning team SHALL produce a monthly capacity report containing:

**Utilization Summary**:
- Current utilization for all monitored resource categories
- Resources exceeding warning thresholds (count, percentage)
- Resources exceeding critical thresholds (count, percentage)
- Month-over-month utilization trend

**Capacity Incidents**:
- Capacity-related incidents or outages during the month
- Near-miss events (resources that approached exhaustion)
- Alert summary (warning, critical alerts generated)

**Forecast Status**:
- Short-term forecast (3-6 months) highlights
- Resources projected to exceed thresholds within 3 months
- Changes to forecasts from previous month

**Capacity Actions**:
- Capacity expansions completed during the month
- Capacity expansions in progress
- Capacity optimization activities

**Distribution**: IT management, infrastructure teams, capacity planning team

**Format**: Executive summary (1-2 pages) + detailed appendix with metrics

**2.8.2 Quarterly Capacity Planning Report**

The capacity planning team SHALL produce a quarterly capacity planning report containing:

**Comprehensive Forecast Update**:
- 12-month capacity forecasts for all resource categories
- Forecast accuracy validation (previous quarter's forecast vs. actual)
- Seasonal pattern analysis
- Business growth impact on capacity

**Capacity Expansion Plan**:
- Planned capacity expansions for next 12 months
- Budget impact (CapEx and OpEx)
- Risk assessment (resources at risk of exhaustion)
- Dependency and sequencing of expansions

**Capacity Health Scorecard**:
- Percentage of resources below warning threshold (target: >95%)
- Proactive vs. reactive expansion ratio (target: >90% proactive)
- Forecast accuracy (target: within ±15%)
- Capacity-related incidents (target: zero)

**Optimization Summary**:
- Resources identified for right-sizing
- Potential cost savings from optimization
- Over-provisioning analysis

**Distribution**: IT leadership (CIO, CISO, IT Director), finance (CFO, financial controller), executive management

**Presentation**: Formal presentation to IT leadership and executive sponsors

**2.8.3 Annual Capacity Strategic Plan**

The capacity planning team SHALL produce an annual strategic capacity plan containing:

**Long-Term Capacity Forecast** (24-36 months):
- Multi-year capacity growth projections
- Alignment with business strategic plans
- Major technology initiatives impact on capacity
- Infrastructure lifecycle and refresh planning

**Strategic Capacity Investments**:
- Major infrastructure investments (datacenter expansion, cloud migration, technology refresh)
- Multi-year budget projections
- Total cost of ownership (TCO) analysis

**Capacity Architecture Review**:
- Infrastructure scalability assessment
- Architectural bottlenecks and constraints
- Cloud vs. on-premises capacity strategy
- Technology trends and capacity implications

**Distribution**: Executive management (CEO, CIO, CFO, CISO), board of directors (if applicable)

**Presentation**: Annual executive presentation

---

## 3. Roles and Responsibilities

### 3.1 Executive Management (CEO, Board of Directors)

**Accountabilities**:
- Ultimate accountability for adequate capacity to support business operations
- Approve major capacity investments and strategic capacity plans
- Ensure adequate budget allocation for capacity management program
- Receive capacity management reports and understand capacity risks

**Authorities**:
- Approve annual capacity budgets (CapEx and OpEx)
- Approve major capacity expansion projects (datacenter builds, cloud migrations)
- Set strategic direction for infrastructure investments

**Responsibilities**:
- Review annual capacity strategic plan
- Understand capacity risks and business impact
- Allocate resources for capacity management program

### 3.2 Chief Information Officer (CIO) / IT Director

**Accountabilities**:
- Overall accountability for capacity management program implementation and effectiveness
- Ensure adequate capacity for business operations
- Balance capacity requirements with budget constraints
- Escalation point for capacity-related risks

**Authorities**:
- Approve capacity expansion plans within approved budget
- Approve capacity management policies and procedures
- Allocate IT resources for capacity planning activities
- Authorize emergency capacity procurement

**Responsibilities**:
- Review quarterly capacity planning reports
- Approve capacity expansion plans
- Resolve capacity planning conflicts and priorities
- Communicate capacity risks to executive management

### 3.3 Chief Information Security Officer (CISO)

**Accountabilities**:
- Ensure capacity for security systems (SIEM, logging, monitoring, EDR)
- Risk assessment for capacity-related security issues
- Compliance verification for capacity management controls (ISO 27001 A.8.6)
- Integration of capacity management with overall ISMS

**Authorities**:
- Require capacity planning for security systems
- Escalate capacity risks that impact security posture
- Approve capacity management policy

**Responsibilities**:
- Monitor capacity for security systems
- Review capacity management compliance
- Ensure capacity considerations in security architecture
- Audit capacity management implementation

### 3.4 Capacity Planning Team / Infrastructure Manager

**Accountabilities**:
- Day-to-day execution of capacity management program
- Capacity monitoring infrastructure implementation and operation
- Capacity forecasting and trend analysis
- Capacity expansion planning and coordination
- Capacity reporting to management

**Authorities**:
- Implement capacity monitoring for all infrastructure resources
- Define capacity thresholds and alerting rules
- Recommend capacity expansion plans
- Coordinate capacity planning across teams

**Responsibilities**:
- Implement and maintain capacity monitoring infrastructure (per ISMS-IMP-A.8.6.1)
- Collect and analyze capacity utilization data
- Develop capacity forecasts (per ISMS-IMP-A.8.6.2)
- Produce monthly, quarterly, and annual capacity reports
- Coordinate with infrastructure teams for capacity expansion implementation
- Conduct capacity management assessments (per ISMS-IMP-A.8.6.3)
- Maintain capacity planning documentation and evidence

### 3.5 IT Operations Team

**Accountabilities**:
- Day-to-day capacity monitoring and alert response
- Immediate response to capacity alerts and incidents
- Capacity tuning and optimization activities
- Deployment of approved capacity expansions

**Authorities**:
- Implement approved capacity tuning and optimization
- Execute emergency capacity mitigation actions
- Escalate capacity issues per escalation procedures

**Responsibilities**:
- Monitor capacity dashboards and respond to alerts
- Investigate capacity incidents and near-miss events
- Implement capacity cleanup and optimization
- Deploy approved capacity expansions
- Document capacity incidents and actions taken
- Provide feedback to capacity planning team on capacity issues

### 3.6 Application Owners / System Owners

**Accountabilities**:
- Provide business growth projections for capacity planning
- Participate in capacity planning for their applications/systems
- Monitor application-specific capacity metrics
- Budget for application capacity requirements

**Authorities**:
- Define application capacity requirements
- Request capacity expansion for their systems
- Participate in capacity planning meetings

**Responsibilities**:
- Provide business projections (user growth, transaction volume, data growth)
- Review capacity forecasts for their applications
- Participate in quarterly capacity planning sessions
- Test application capacity requirements
- Document application capacity requirements

### 3.7 Financial Controller / Chief Financial Officer (CFO)

**Accountabilities**:
- Approve capacity management budgets (CapEx and OpEx)
- Financial reporting on capacity investments
- Cost optimization oversight
- Budget planning for capacity expansion

**Authorities**:
- Approve capacity budgets
- Approve major capacity expenditures
- Request cost optimization initiatives

**Responsibilities**:
- Review quarterly capacity planning reports (budget impact)
- Approve capacity expansion budgets
- Track capacity expenditures vs. budget
- Support capacity planning with financial analysis (TCO, ROI)

---

## 4. Governance and Compliance

### 4.1 Policy Governance Framework

**Policy Owner**: Chief Information Security Officer (CISO)  
**Policy Approver**: Chief Information Officer (CIO) with concurrence from CFO and CISO  
**Policy Review**: Annual review aligned with capacity planning cycle

**Governance Bodies**:

**Capacity Planning Committee** (operational governance):
- **Chair**: Infrastructure Manager or Capacity Planning Manager
- **Members**: IT Operations Manager, Application Owners, Network Manager, Cloud Architect
- **Meeting Frequency**: Monthly
- **Purpose**: Review capacity status, discuss forecasts, plan capacity expansions, resolve issues

**IT Leadership Team** (strategic governance):
- **Members**: CIO, CISO, CFO (or Financial Controller), IT Director
- **Meeting Frequency**: Quarterly
- **Purpose**: Review capacity planning reports, approve capacity budgets, strategic capacity decisions

### 4.2 Regulatory Compliance

This policy satisfies the following regulatory and framework requirements per **ISMS-POL-00 (Regulatory Applicability Framework)**:

**Tier 1 - Mandatory Compliance**:
- **ISO/IEC 27001:2022**: Control A.8.6 (Capacity Management) - Mandatory for ISO 27001 certification

**Tier 2 - Conditional Applicability**:
- **FINMA Circular 2023/1** (Swiss financial institutions): Margin 50-62 ICT operational resilience
- **DORA Article 11** (EU financial entities): ICT capacity planning requirements
- **NIS2 Article 21(2)** (Essential/important entities): Business continuity capacity planning

**Tier 3 - Informational Reference**:
- **ITIL 4 Capacity Management**: Best practices for IT service management
- **NIST SP 800-53 AU-6**: Audit record review and capacity monitoring

### 4.3 Document Hierarchy

This policy is supported by:

**Implementation Guidance**:
- **ISMS-IMP-A.8.6.1**: Capacity Monitoring Implementation
- **ISMS-IMP-A.8.6.2**: Capacity Forecasting and Planning
- **ISMS-IMP-A.8.6.3**: Capacity Management Assessment

**Assessment Tools** (Excel workbooks generated by Python scripts):
- Assessment 1: Capacity Utilization Analysis
- Assessment 2: Capacity Forecasts and Planning
- Dashboard: Capacity Management Overview

**Related Policies**:
- ISMS-POL-00: Regulatory Applicability Framework
- ISMS-POL-A.8.16: Monitoring Activities
- ISMS-POL-A.8.14: Redundancy of Information Processing Facilities
- ISMS-POL-A.8.13: Information Backup
- ISMS-POL-A.7.11: Supporting Utilities
- ISMS-POL-A.5.30: ICT Readiness for Business Continuity

### 4.4 Policy Exceptions and Risk Acceptance

**Exception Process**:

**Temporary Exceptions** (up to 6 months):
- **Approved by**: IT Director/CIO
- **Documentation**: Risk acceptance, mitigation plan, remediation timeline
- **Examples**: New systems in pilot phase, transitional states during migrations, vendor constraints
- **Review**: Monthly review of exception status

**Permanent Exceptions**:
- **Approved by**: CIO + CISO + Executive Management
- **Documentation**: Formal risk acceptance, compensating controls, business justification
- **Review**: Annual re-approval required
- **Conditions**: Must demonstrate compensating controls or business necessity

**Exception Request Process**:
1. Submit exception request to Capacity Planning Team
2. Risk assessment by CISO
3. Approval per authority levels above
4. Document in exception register
5. Regular review of active exceptions

### 4.5 Compliance Verification and Enforcement

**Compliance Verification**:
- **Internal Audits**: Quarterly internal audits of capacity management implementation
- **External Audits**: Annual ISO 27001 certification audit includes A.8.6 verification
- **Self-Assessment**: Monthly capacity management self-assessment via ISMS-IMP-A.8.6.3

**Compliance Metrics**:
- Monitoring coverage (% of systems monitored)
- Threshold configuration (% of resources with thresholds)
- Forecasting completeness (% of critical resources forecasted)
- Reporting timeliness (monthly/quarterly reports on schedule)
- Proactive vs. reactive capacity additions

**Non-Compliance Consequences**:

**Operational Consequences**:
- Service outages or degradation due to capacity exhaustion
- Emergency capacity procurement at premium pricing
- Missed SLAs and potential contract penalties

**Financial Consequences**:
- Unbudgeted emergency spending
- Over-provisioning waste
- Lost revenue due to service unavailability

**Compliance Consequences**:
- ISO 27001 certification non-conformance
- Regulatory violations (for regulated industries)
- Audit findings and corrective action requirements

**Organizational Consequences**:
- Performance management actions for responsible individuals
- Escalation to executive management
- Reputational damage

### 4.6 Policy Review and Updates

**Review Schedule**:

This policy SHALL be reviewed:
- **Annually**: Scheduled review aligned with capacity planning cycle
- **On Significant Change**: Major infrastructure changes, cloud migrations, business acquisitions
- **Regulatory Changes**: Updates to ISO 27001 or applicable regulations
- **Incident-Driven**: Following major capacity-related incidents

**Update Process**:

Policy updates require:
1. Stakeholder consultation (IT, security, finance, business)
2. Impact analysis (technical, financial, organizational)
3. Approval per governance framework
4. Communication to all affected parties
5. Training updates (if procedures change)
6. Version control and archival

**Approval Authority**:
- **Minor Updates** (clarifications, non-substantive changes): Information Security Manager
- **Major Updates** (requirement changes, scope changes): CISO and IT Director
- **Strategic Changes** (regulatory changes, organizational changes): Executive Management

---

## 5. Assessment and Evidence Framework

### 5.1 Assessment Methodology Overview

[Organization] implements a structured assessment methodology to verify capacity management effectiveness and compliance. The assessment framework consists of three components:

**Assessment 1: Capacity Utilization Analysis**
- **Purpose**: Document current capacity inventory, utilization status, and monitoring coverage
- **Frequency**: Monthly
- **Owner**: Capacity Planning Team
- **Outputs**: Capacity utilization workbook, resource inventory, threshold status, coverage metrics

**Assessment 2: Capacity Forecasts and Planning**
- **Purpose**: Validate capacity forecasting methodology, review capacity plans, assess planning effectiveness
- **Frequency**: Quarterly
- **Owner**: Capacity Planning Team with IT management review
- **Outputs**: Capacity forecast workbook, planning status, forecast accuracy validation, expansion plans

**Dashboard: Capacity Management Overview**
- **Purpose**: Executive summary of capacity health, compliance status, trends
- **Frequency**: Monthly
- **Audience**: Executive management, CIO, CISO, CFO
- **Outputs**: Executive dashboard, KPI tracking, gap analysis, compliance certification

### 5.2 Assessment 1: Capacity Utilization Analysis

**What This Assessment Evaluates**:
- Current utilization for all monitored resources (compute, storage, network, application, cloud)
- Threshold status (OK, Warning, Critical)
- Monitoring coverage (% of resources monitored)
- Capacity headroom (remaining capacity)
- Resources requiring immediate action

**Assessment Methodology**:
1. **Resource Inventory**: Document all infrastructure resources in scope
2. **Utilization Data Collection**: Export current and peak utilization from monitoring tools
3. **Threshold Classification**: Classify each resource by threshold status
4. **Coverage Analysis**: Calculate monitoring coverage percentages
5. **Gap Identification**: Identify resources at/above critical thresholds or not monitored
6. **Action Planning**: Prioritize resources requiring capacity expansion or monitoring implementation

**Evidence Requirements**:
- Monitoring tool exports (Prometheus, Datadog, CloudWatch, etc.)
- Infrastructure inventory from CMDB
- Threshold configuration documentation
- Coverage metrics and gap analysis

**Compliance Criteria**:
- ≥95% of production systems monitored (compliant)
- ≥90% of non-production systems monitored (target)
- ≥95% of monitored resources below warning threshold (healthy)
- Zero resources at maximum capacity (critical finding if violated)

### 5.3 Assessment 2: Capacity Forecasts and Planning

**What This Assessment Evaluates**:
- Forecasting methodology and assumptions
- Forecast accuracy (previous forecasts vs. actual)
- Capacity planning process effectiveness
- Planned capacity expansions and status
- Proactive vs. reactive capacity additions

**Assessment Methodology**:
1. **Forecast Documentation Review**: Verify forecasts exist for all critical resources
2. **Accuracy Validation**: Compare previous period forecasts to actual utilization
3. **Planning Process Review**: Verify planning cycles executed (monthly, quarterly, annual)
4. **Expansion Tracking**: Track planned vs. emergency capacity additions
5. **Effectiveness Metrics**: Calculate proactive ratio, forecast accuracy, planning lead time

**Evidence Requirements**:
- Capacity forecast documents and workbooks
- Historical forecast accuracy data
- Capacity planning meeting minutes
- Capacity expansion approvals and tracking
- Budget documents for capacity expenditures

**Compliance Criteria**:
- Forecasts exist for 100% of critical resources (mandatory)
- Forecast accuracy within ±15% (target)
- ≥90% of capacity expansions are proactive (target)
- Quarterly planning cycles executed on schedule (compliant)

### 5.4 Dashboard: Capacity Management Overview

**What This Dashboard Provides**:
- Overall capacity health score
- Compliance status (monitoring coverage, forecasting completeness, reporting timeliness)
- Resources at risk (warning/critical thresholds)
- Capacity trends (utilization growth, forecast accuracy trends)
- Executive certification (CISO sign-off on capacity management status)

**Dashboard Sections**:
1. **Executive Summary**: One-page capacity health overview
2. **Key Performance Indicators**: Monitoring coverage, threshold compliance, forecast accuracy, proactive ratio
3. **Resources at Risk**: Count and list of resources at/above critical thresholds
4. **Capacity Trends**: Utilization trends over time, growth rates, seasonal patterns
5. **Compliance Status**: Certification of compliance with policy requirements
6. **Gap Analysis**: Identified gaps and remediation plans
7. **CISO Certification**: Executive sign-off on capacity management posture

### 5.5 Evidence Collection Requirements

[Organization] SHALL collect and retain the following evidence types:

**Monitoring Evidence**:
- Monitoring tool configuration exports
- Threshold definitions and alert rules
- Monitoring coverage reports
- Historical utilization data (12-24 months minimum)
- Alert logs (warning and critical capacity alerts)
- **Retention**: 24 months minimum

**Forecasting Evidence**:
- Capacity forecast documents
- Trend analysis outputs
- Forecast accuracy validation reports
- Forecasting methodology documentation
- **Retention**: 24 months (to enable multi-year validation)

**Planning Evidence**:
- Capacity planning meeting minutes
- Quarterly and annual capacity plans
- Capacity expansion approvals
- Budget documents (CapEx/OpEx for capacity)
- Expansion tracking (planned vs. actual)
- **Retention**: 36 months (multi-year planning cycle)

**Reporting Evidence**:
- Monthly capacity reports
- Quarterly capacity planning reports
- Annual strategic capacity plans
- Executive presentations
- Distribution records
- **Retention**: 24 months

**Incident Evidence**:
- Capacity-related incident reports
- Root cause analysis for capacity exhaustion
- Near-miss reports
- Corrective and preventive actions
- Lessons learned
- **Retention**: 36 months

**Assessment Evidence**:
- Completed assessment workbooks (Assessment 1, Assessment 2, Dashboard)
- Assessment approval signatures
- Gap analysis and remediation tracking
- Audit findings and responses
- **Retention**: Permanent (part of ISMS audit trail)

### 5.6 Evidence Storage and Retention

**Evidence Repository**:
- Centralized storage location (SharePoint, network share, document management system)
- Organized by assessment type and time period
- Version-controlled for policy/procedure documents
- Access-controlled (appropriate permissions for auditors, compliance, management)

**Naming Convention**:
```
ISMS-A.8.6-[Evidence Type]-[YYYY-MM]-[Description].[Extension]

Examples:
ISMS-A.8.6-Monitoring-2026-01-Utilization-Data.xlsx
ISMS-A.8.6-Forecasting-2026-Q1-Forecast-Report.pdf
ISMS-A.8.6-Planning-2026-01-Meeting-Minutes.docx
ISMS-A.8.6-Assessment-2026-01-Utilization-Assessment.xlsx
```

**Backup and Protection**:
- Evidence SHALL be backed up per [Organization]'s backup policy (A.8.13)
- Evidence SHALL be protected from unauthorized modification
- Version control for all documents
- Audit log for evidence access and modifications

### 5.7 Compliance Scoring Methodology

[Organization] uses a weighted scoring system to measure capacity management compliance:

**Scoring Categories**:

| Category | Weight | Measurement | Target Score |
|----------|--------|-------------|--------------|
| **Monitoring Coverage** | 30% | % of resources monitored | ≥95% |
| **Threshold Compliance** | 25% | % of resources below warning threshold | ≥95% |
| **Forecasting Completeness** | 20% | % of critical resources with forecasts | 100% |
| **Planning Effectiveness** | 15% | % proactive capacity additions | ≥90% |
| **Reporting Timeliness** | 10% | Reports delivered on schedule | 100% |

**Overall Compliance Score**:
```
Overall Score = (Monitoring Coverage × 0.30) + 
                (Threshold Compliance × 0.25) + 
                (Forecasting Completeness × 0.20) + 
                (Planning Effectiveness × 0.15) + 
                (Reporting Timeliness × 0.10)
```

**Compliance Ratings**:
- **90-100%**: Compliant (Green) - Capacity management fully effective
- **75-89%**: Partial Compliance (Yellow) - Gaps identified, remediation required
- **<75%**: Non-Compliant (Red) - Significant gaps, immediate action required

**Quarterly Trend Analysis**:
- Track compliance score over time
- Identify improving or declining trends
- Root cause analysis for score decreases
- Continuous improvement initiatives

### 5.8 Audit Preparation Framework

**Audit Types**:
- **Internal Audit**: Quarterly capacity management self-assessment
- **ISO 27001 External Audit**: Annual certification audit includes A.8.6
- **Regulatory Audit** (if applicable): FINMA, DORA, NIS2 compliance verification

**Audit Preparation Checklist**:

**Documentation Readiness**:
- [ ] Policy documents current and approved
- [ ] Implementation procedures documented (ISMS-IMP-A.8.6.1, .2, .3)
- [ ] Assessment workbooks completed for audit period
- [ ] Evidence repository organized and accessible
- [ ] Gap analysis and remediation plans documented

**Process Demonstration**:
- [ ] Monitoring infrastructure operational and demonstrable
- [ ] Capacity forecasts current (within last quarter)
- [ ] Capacity reports generated and distributed on schedule
- [ ] Capacity planning meeting minutes available
- [ ] Capacity expansion approvals and tracking available

**Compliance Verification**:
- [ ] Compliance score calculated (≥90% target)
- [ ] Gap analysis completed
- [ ] Remediation plans for any gaps
- [ ] Executive certification obtained (CISO sign-off)

**Auditor Interviews**:
- Capacity Planning Team prepared to demonstrate processes
- IT Operations Team prepared to demonstrate monitoring
- Management prepared to discuss capacity governance

**Audit Evidence Package**:
- Policy documents (this policy and implementation guides)
- Assessment workbooks (last 4 quarters)
- Capacity reports (monthly and quarterly for audit period)
- Evidence samples (monitoring data, forecasts, planning documents)
- Compliance dashboard and certification
- Gap analysis and remediation tracking

---

## 6. Related Documents and References

### 6.1 Internal ISMS Documents

**Policy Framework**:
- ISMS-POL-00: Regulatory Applicability Framework
- ISO/IEC 27001:2022 Clause 6: Risk Management
- [Organization] Data Classification Policy (if applicable)

**Implementation Guidance**:
- ISMS-IMP-A.8.6.1: Capacity Monitoring Implementation
- ISMS-IMP-A.8.6.2: Capacity Forecasting and Planning
- ISMS-IMP-A.8.6.3: Capacity Management Assessment

**Related Policies**:
- ISMS-POL-A.8.16: Monitoring Activities
- ISMS-POL-A.8.14: Redundancy of Information Processing Facilities
- ISMS-POL-A.8.13: Information Backup
- ISMS-POL-A.7.11: Supporting Utilities
- ISMS-POL-A.5.30: ICT Readiness for Business Continuity

### 6.2 External Standards and Frameworks

**Regulatory References** (per ISMS-POL-00):
- ISO/IEC 27001:2022 - Control A.8.6
- ISO/IEC 27002:2022 - Control 8.6 guidance
- FINMA Circular 2023/1 (if applicable)
- DORA - Regulation (EU) 2022/2554 (if applicable)
- NIS2 - Directive (EU) 2022/2555 (if applicable)

**Technical Standards** (Informational Reference):
- ITIL 4: IT Service Management (Capacity Management process)
- ISO/IEC 20000: IT Service Management
- NIST SP 800-53: AU-6 (Audit Record Review, Analysis, and Reporting)

---


---

## Approval Record

| Role | Name | Date |
|------|------|------|
| **Chief Information Security Officer (CISO)** | [Name] | [Date] |
| **Chief Information Officer (CIO)** | [Name] | [Date] |
| **Chief Financial Officer (CFO)** | [Name] | [Date] |
| **IT Operations Manager** | [Name] | [Date] |
| **Legal/Compliance Officer** | [Name] | [Date] |

---

**END OF POLICY DOCUMENT**

---

*This policy establishes capacity management requirements. Implementation procedures are documented in ISMS-IMP-A.8.6.1, ISMS-IMP-A.8.6.2, and ISMS-IMP-A.8.6.3.*