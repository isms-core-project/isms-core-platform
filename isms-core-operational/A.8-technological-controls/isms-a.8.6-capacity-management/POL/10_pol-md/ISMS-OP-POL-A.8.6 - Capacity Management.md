**ISMS-OP-POL-A.8.6 — Capacity Management**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Capacity Management |
| **Document Type** | Operational Policy |
| **Document ID** | ISMS-OP-POL-A.8.6 |
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
| 1.0 | [Date] | CISO | Initial operational policy for ISO 27001:2022 |

**Review Cycle**: Annual (aligned with capacity planning cycle)
**Next Review Date**: [Effective Date + 12 months]

**Approved By**: [Information Security Manager / Management]

**Related Documents**:

- ISO/IEC 27001:2022 Control A.8.6 — Capacity management
- ISO/IEC 27002:2022 Section 8.6 — Implementation guidance for capacity management
- NIST SP 800-53 Rev 5 — AU-4 (Audit Log Storage Capacity), CP-2(2) (Capacity Planning), SC-5 (Denial-of-Service Protection)
- ITIL 4 — Capacity and Performance Management Practice

**Related Annex A Controls**:

| Control | Relationship to Capacity Management |
|---------|-------------------------------------|
| A.5.30–8.13–14 Business continuity and DR | Recovery site capacity planning; backup storage capacity |
| A.7.11 Supporting utilities | Physical infrastructure capacity (power, cooling, rack space) |
| A.8.1–7–18–19 Endpoint security | Endpoint resource monitoring and fleet capacity |
| A.8.8 Vulnerability management | Scanning tool capacity; patch deployment resource requirements |
| A.8.9 Configuration management | Baseline configurations include capacity thresholds |
| A.8.15 Logging | Log storage capacity planning and retention management |
| A.8.16 Monitoring activities | Capacity metrics as a subset of overall monitoring |
| A.8.20–22 Network security | Network bandwidth and throughput capacity |

**Related Internal Policies**:

- Monitoring Activities Policy (A.8.16)
- Business Continuity and Disaster Recovery Policy (A.5.30–8.13–14)
- Logging Policy (A.8.15)
- Network Security Policy (A.8.20–22)
- Change Management Policy (A.8.32)

---

# Capacity Management Policy

## Purpose

The purpose of this policy is to ensure that the use of information processing resources is monitored and adjusted in line with current and expected capacity requirements, preventing service disruptions caused by resource exhaustion and supporting informed investment decisions.

Capacity management is both an operational necessity and a security control. Insufficient capacity can cause service outages, degrade security monitoring, prevent audit log collection, and create conditions exploitable by denial-of-service attacks. Proactive capacity planning ensures that infrastructure, applications, and supporting services remain available, performant, and secure.

This policy supports Swiss nFADP (revDSG) Art. 8 by implementing technical and organisational measures appropriate to risk to protect the availability and integrity of systems that process personal data. Where the organisation processes data of individuals in the EU/EEA, GDPR Art. 32 requirements for ensuring the ongoing availability and resilience of processing systems also apply.

## Scope

This policy applies to all infrastructure, application, and service resources within the ISMS scope that require capacity monitoring and planning. This includes:

- **Compute resources**: Servers, virtual machines, containers, cloud instances (CPU and memory utilisation).
- **Storage resources**: Disk storage, database storage, backup storage, archive storage, log storage.
- **Network resources**: Bandwidth, throughput, connections, load balancer capacity, DNS query capacity.
- **Application resources**: Concurrent users, transaction rates, API rate limits, message queue depth.
- **Cloud service resources**: Service quotas, instance limits, API call limits, reserved capacity.
- **Licence capacity**: Software licences, subscription seats, concurrent licence usage.
- **Physical infrastructure**: Power capacity, cooling capacity, rack space (per A.7.11).

All employees, contractors, and third-party service providers with responsibility for infrastructure, application, or service management.

**Out of scope**: Application performance tuning and code optimisation (covered under secure development); detailed software asset management and licence procurement (covered under asset management A.5.9); physical building capacity unrelated to information processing.

## Principle

The organisation shall proactively monitor, forecast, and plan for capacity requirements across all critical resources. Capacity management follows the principle of prevention over reaction — it is significantly less costly and less disruptive to plan for capacity growth than to respond to capacity exhaustion incidents.

Capacity decisions shall be data-driven, based on measured utilisation trends and documented business growth projections, not on assumption or anecdote. Resources shall maintain sufficient headroom to absorb unexpected demand spikes without service degradation.

---

## Resource Monitoring

### Monitoring Coverage

All production systems and services shall have capacity monitoring enabled. Monitoring shall cover, at minimum, the resource categories listed in the Scope section above.

**Coverage Requirements**:

| Environment | Coverage Target | Monitoring Frequency |
|-------------|-----------------|----------------------|
| Production systems | 100% | Every 5 minutes or less |
| Disaster recovery / standby | 100% | Every 15 minutes or less |
| Non-production (staging, test) | 90% | Every 15 minutes or less |

Monitoring shall be implemented using [Monitoring Platform] (e.g., Prometheus, Zabbix, Datadog, Azure Monitor, CloudWatch, or equivalent). The platform shall be documented in the asset inventory with its hosting model, data residency, and administrative access controls.

### Monitored Metrics

The following metrics shall be collected for each applicable resource type:

| Resource Type | Metrics | Units |
|---------------|---------|-------|
| **CPU** | Utilisation (average, peak), load average, ready time | Percentage, count |
| **Memory** | Utilisation, swap usage, available memory | Percentage, GB |
| **Storage** | Used capacity, available capacity, growth rate, IOPS | GB/TB, percentage, ops/sec |
| **Network** | Bandwidth utilisation, packet loss, latency, connection count | Mbps/Gbps, percentage, ms, count |
| **Application** | Concurrent users, active sessions, transaction rate, queue depth | Count, transactions/sec |
| **Cloud quotas** | Service limit utilisation per region and account | Percentage of quota |
| **Licences** | Active allocations vs. total entitlements | Count, percentage |

### Metric Retention

- **Raw metrics**: Minimum 30 days at full resolution (for incident investigation).
- **Aggregated metrics**: Minimum 12 months at hourly or daily granularity (for trend analysis).
- **Historical summaries**: Minimum 36 months at monthly granularity (for strategic planning).

Metric data shall be protected from unauthorised modification or deletion. Where metrics feed security monitoring (A.8.16), log integrity requirements from the Logging Policy (A.8.15) also apply.

---

## Threshold Framework and Alerting

### Threshold Levels

All monitored resources shall have defined capacity thresholds at three levels:

| Level | Purpose | Typical Range | Action |
|-------|---------|---------------|--------|
| **Warning** | Early indication of capacity pressure | 70–80% utilisation | Capacity planning review; investigate growth trend |
| **Critical** | Capacity approaching exhaustion | 85–90% utilisation | Immediate investigation; initiate capacity expansion or load mitigation |
| **Maximum** | Resource exhaustion imminent or occurring | 95%+ utilisation | Emergency response; invoke incident management if service impact |

Exact threshold values shall be defined per resource type and system classification, documented in the monitoring platform, and reviewed quarterly. Thresholds shall be tuned based on false positive rates, workload patterns, and near-miss incidents.

**Storage-specific thresholds** shall also account for growth rate: if storage is projected to reach 95% within 30 days at the current consumption rate, a warning alert shall be generated regardless of current percentage.

### Alert Configuration

Capacity threshold alerts shall be configured with:

- **Routing**: Alerts delivered to the responsible operations team via [Alerting Tool] (e.g., PagerDuty, Opsgenie, ServiceNow, or equivalent).
- **Delivery time**: Alerts delivered within 5 minutes of threshold breach detection.
- **Escalation**: Unacknowledged warning alerts escalated after 4 hours; unacknowledged critical alerts escalated after 30 minutes.
- **Deduplication**: Repeated alerts for the same resource and threshold suppressed to prevent alert fatigue; re-alert if condition persists beyond the suppression window.
- **Integration**: Critical and maximum alerts shall create incidents automatically in [ITSM Tool] (e.g., ServiceNow, Jira Service Management, or equivalent).

### Alert Response

| Alert Level | Response SLA | Response Action |
|-------------|--------------|-----------------|
| **Warning** | Acknowledged within 4 hours (business hours) | Review trend data; update capacity forecast; plan expansion if needed |
| **Critical** | Acknowledged within 30 minutes | Investigate root cause; implement immediate mitigation (load shedding, temporary scaling); initiate capacity expansion |
| **Maximum** | Acknowledged within 15 minutes | Execute emergency response; invoke incident management per A.5.24–28 if service impact; implement emergency capacity expansion |

---

## Capacity Forecasting

### Forecasting Horizons

The organisation shall develop and maintain capacity forecasts at three horizons:

| Horizon | Timeframe | Purpose | Update Frequency |
|---------|-----------|---------|------------------|
| **Short-term** | 3–6 months | Tactical planning; immediate procurement | Monthly |
| **Medium-term** | 6–12 months | Budget planning; contract renewals | Quarterly |
| **Long-term** | 12–24 months | Strategic planning; data centre or cloud migration decisions | Annually |

### Forecasting Methodology

Forecasts shall be based on:

- **Historical trend analysis**: Extrapolation from measured utilisation data (minimum 6 months of data required for reliable trends).
- **Business growth projections**: Input from application owners and business units on planned projects, user growth, data volume increases, and new service launches.
- **Seasonal patterns**: Identification and modelling of periodic demand variations (end-of-month processing, annual reporting cycles, marketing campaigns).
- **Planned changes**: Scheduled deployments, migrations, decommissions, and infrastructure changes.

Where historical data is insufficient (new systems or services), conservative estimates shall be used with more frequent review during the first 6 months of operation.

### Forecast Accuracy

- **Target accuracy**: Forecasts shall be within +/-15% of actual utilisation (measured quarterly).
- **New systems (first 6 months)**: +/-30% accuracy acceptable while baselines are established.
- **High-variability workloads**: +/-25% accuracy with documented justification.
- **Deviations exceeding 15%**: Root cause analysis required within 10 business days; findings documented and incorporated into the next forecast cycle.

---

## Auto-Scaling Policies

Where the organisation operates cloud infrastructure, auto-scaling shall be configured for workloads with variable demand patterns.

### Auto-Scaling Requirements

| Requirement | Standard |
|-------------|----------|
| **Scaling trigger** | CPU utilisation, memory utilisation, request rate, queue depth, or custom application metrics |
| **Scale-out threshold** | Defined per workload; typically 70–80% of target metric for 3–5 minutes sustained |
| **Scale-in threshold** | Defined per workload; typically 30–40% of target metric for 10–15 minutes sustained |
| **Minimum instances** | At least 2 for production workloads (availability); at least 1 for non-production |
| **Maximum instances** | Defined per workload to prevent cost overruns; aligned with budget constraints |
| **Cooldown period** | Minimum 5 minutes between scaling actions to prevent oscillation |

### Auto-Scaling Governance

- Auto-scaling configurations shall be documented and version-controlled.
- Changes to auto-scaling policies for production workloads shall follow the change management process (A.8.32).
- Maximum instance limits shall be reviewed quarterly and aligned with approved budgets.
- Auto-scaling events shall be logged and reviewed monthly for optimisation opportunities.
- **Cost guardrails**: Maximum monthly spend limits shall be configured at the cloud account or subscription level. Auto-scaling that would breach the spend limit shall trigger an alert to the Infrastructure Manager and CFO delegate.

Where auto-scaling is not available or not appropriate (on-premises infrastructure, fixed-capacity services), manual capacity expansion procedures shall be documented with defined procurement and deployment lead times.

---

## Capacity and Cost Optimisation

Capacity management shall balance availability, performance, and cost. Over-provisioning wastes budget; under-provisioning creates risk. The organisation shall actively optimise resource allocation based on measured utilisation data.

### Optimisation Strategies

| Strategy | Description | Applicability |
|----------|-------------|---------------|
| **Right-sizing** | Eliminate over-provisioned resources where sustained utilisation is below 40% | All environments |
| **Reserved capacity** | Purchase reserved instances or committed use discounts for steady-state workloads (e.g., AWS RIs, Azure RIs, GCP CUDs) | Cloud environments with predictable baseline |
| **Spot/preemptible instances** | Use for non-critical, interruptible workloads (batch processing, testing, development) | Cloud environments with fault-tolerant workloads |
| **Auto-scaling** | Align capacity with demand in real-time to avoid paying for idle resources | Cloud environments with variable demand |
| **Storage lifecycle** | Tier infrequently accessed data to lower-cost storage classes (e.g., S3 Glacier, Azure Cool/Archive, GCS Nearline/Coldline) | All storage with defined access patterns |

### Quarterly Cost Review

The Infrastructure Manager shall conduct a quarterly cost review that includes:

- Identification of over-provisioned resources (sustained utilisation consistently below 40%).
- Evaluation of reserved capacity versus on-demand spending ratios.
- Assessment of storage tiering opportunities.
- Reporting of cost optimisation actions taken and savings achieved.

Cost optimisation findings shall be included in the quarterly capacity review report presented to the CIO, CISO, and CFO delegate.

---

## Capacity and Service Level Objectives

Capacity thresholds shall be aligned with service level objectives (SLOs) to ensure that capacity constraints do not degrade service quality below agreed levels. The connection between resource utilisation and service performance shall be documented for each critical service.

### SLO Alignment

| Service Type | Typical SLO | Capacity Threshold Alignment |
|--------------|-------------|------------------------------|
| Web application | 99.9% availability, <500ms p95 latency | CPU shall remain below 75% average (latency degrades above 75%) |
| API service | 99.95% availability, <200ms p95 latency | CPU below 70% average; memory below 80% |
| Database | 99.99% availability, <50ms query response | IOPS below 80% maximum; connections below 90% maximum |
| Message queue | 99.9% availability, <5s processing delay | Queue depth below 80% maximum; consumer capacity maintained |

Where measured resource utilisation approaches levels that would degrade SLO performance, capacity thresholds shall be adjusted downward to trigger earlier intervention. SLO alignment shall be reviewed quarterly as part of the capacity review process.

---

## Capacity Reporting

### Reporting Cadence

| Report | Audience | Frequency | Content |
|--------|----------|-----------|---------|
| **Operational dashboard** | IT Operations | Continuous (real-time) | Current utilisation, active alerts, trend indicators |
| **Monthly capacity report** | IT Leadership, Infrastructure Manager | Monthly | Utilisation summary, alert history, forecast highlights, capacity actions taken |
| **Quarterly capacity review** | CIO, CISO, CFO delegate | Quarterly | Forecasts, expansion plans, budget impact, health scorecard, compliance metrics |
| **Annual capacity plan** | Executive Management | Annually | Strategic plan with multi-year projections, investment requirements, risk assessment |

### Report Content Requirements

Monthly and quarterly reports shall include:

- Current utilisation by resource type (average, peak, trend direction).
- Threshold breach count and response times.
- Capacity-related incidents (count, severity, root cause summary).
- Forecast accuracy measurement (actual vs. predicted).
- Planned capacity changes (expansions, decommissions, migrations).
- Budget utilisation for capacity expenditure.

Reports shall be generated from [Monitoring Platform] data. The annual capacity plan shall be approved by the CIO and included in the management review per ISO 27001 Clause 9.3.

---

## Storage Capacity Management

Storage capacity requires specific attention due to its continuous growth characteristics and the direct security impact of storage exhaustion (loss of audit logs, inability to write security events, application failures).

### Log Storage

- Log storage capacity shall be planned in coordination with the Logging Policy (A.8.15) to ensure retention requirements can be met without storage exhaustion.
- Log storage shall have a dedicated warning threshold at 70% and critical threshold at 85%.
- If log storage reaches critical threshold, automated log rotation or archival shall be triggered before data loss occurs.
- Log storage growth rate shall be tracked and projected monthly.

### Database Storage

- Database storage growth shall be monitored and forecast separately from file storage.
- Database maintenance activities (vacuuming, index rebuilds, archival) shall be factored into capacity planning.
- Database storage thresholds shall account for operational overhead (temporary tables, transaction logs, replication lag).

### Backup Storage

- Backup storage capacity shall be planned to accommodate full backup sets for the required retention period per the backup policy (A.5.30–8.13–14).
- Growth in backup storage shall be forecast based on production data growth and retention policy changes.

---

## Licence Capacity Management

Software licence capacity shall be monitored to prevent compliance violations and service interruptions caused by licence exhaustion.

### Licence Monitoring Requirements

| Requirement | Standard |
|-------------|----------|
| **Licence inventory** | Maintained in asset inventory (A.5.9) with entitlement counts, expiry dates, and licence type (concurrent, named, device) |
| **Usage monitoring** | Active usage tracked against entitlement for all critical software |
| **Warning threshold** | Alert when usage reaches 80% of entitlement |
| **Critical threshold** | Alert when usage reaches 90% of entitlement |
| **Review frequency** | Quarterly usage review; annual renewal planning |

### Licence Renewal Planning

Licence renewals shall be tracked with a minimum 90-day lead time before expiry. Licence capacity requirements shall be included in the medium-term (6–12 month) capacity forecast and aligned with budget planning cycles.

---

## Capacity Incident Response

When capacity exhaustion causes or threatens to cause service impact, the organisation's incident management process (A.5.24–28) shall be invoked.

### Capacity-Specific Incident Procedures

| Scenario | Classification | Immediate Response |
|----------|---------------|-------------------|
| **Warning threshold sustained >24 hours** | Capacity event (non-incident) | Review and plan; no emergency action required |
| **Critical threshold sustained >1 hour** | Priority 3 incident | Implement load mitigation; initiate emergency capacity expansion |
| **Service degradation from capacity** | Priority 2 incident | Emergency scaling or load shedding; customer notification if external impact |
| **Service outage from capacity exhaustion** | Priority 1 incident | Full incident response; emergency procurement; post-incident review mandatory |

### Post-Incident Review

All capacity-related incidents classified Priority 1 or Priority 2 shall undergo post-incident review within 5 business days. The review shall determine:

- Why monitoring and forecasting did not prevent the incident.
- Whether thresholds require adjustment.
- Whether forecasting methodology requires improvement.
- What capacity expansion is needed to prevent recurrence.
- Whether the incident exposed a gap in monitoring coverage.

Findings shall be tracked in the capacity improvement register until remediation is complete.

---

## Denial-of-Service Resilience

Capacity planning shall incorporate resilience against denial-of-service (DoS/DDoS) conditions. Capacity should not be planned solely for average or expected peak loads — headroom shall be maintained to absorb unexpected demand spikes, including those caused by malicious activity.

### Headroom Requirements

| Resource | Minimum Headroom at Peak | Rationale |
|----------|--------------------------|-----------|
| **CPU** | 20% | Absorb traffic spikes without degradation |
| **Memory** | 20% | Prevent out-of-memory failures under load |
| **Storage** | 3 months at current growth rate | Lead time for procurement and provisioning |
| **Network bandwidth** | 30% during business hours | Absorb traffic spikes; accommodate DDoS mitigation overhead |

Where external-facing services are exposed to DDoS risk, additional mitigation measures (CDN, DDoS protection services, rate limiting) shall be implemented in coordination with the Network Security Policy (A.8.20–22).

---

## Capacity Planning Committee

Organisations with complex or large-scale infrastructure (50+ servers or equivalent cloud workloads) should establish a Capacity Planning Committee to coordinate capacity management across teams and ensure alignment between technical capacity decisions and business strategy.

### Committee Structure

| Role | Function |
|------|----------|
| **Infrastructure Manager** (chair) | Sets agenda; presents capacity data and forecasts |
| **Cloud Architect / Platform Engineer** | Cloud capacity trends, auto-scaling effectiveness, cost optimisation |
| **Database Administrator** | Database storage growth, performance capacity, replication capacity |
| **Application Owners** (rotating) | Business growth projections, planned launches, demand changes |
| **CFO delegate** | Budget review, investment approval, cost-benefit analysis |

### Meeting Cadence

The Capacity Planning Committee shall meet quarterly. The agenda shall include:

- Review of capacity forecasts and forecast accuracy.
- Approval of planned capacity expansions and associated budgets.
- Review of capacity-related incidents and near-miss events.
- Budget impact discussion and cost optimisation opportunities.
- Identification of emerging capacity risks from business growth or technology changes.

Meeting minutes shall be retained as evidence of governance (Evidence #10).

Where the organisation is too small to justify a formal committee, the quarterly capacity review meeting between the Infrastructure Manager and CIO shall fulfil this governance function.

---

## Definitions

| Term | Definition |
|------|------------|
| **Auto-scaling** | Automated adjustment of compute resources (instances, containers) in response to measured demand, typically in cloud environments |
| **Capacity forecast** | Projection of future resource requirements based on historical trends, business growth plans, and seasonal patterns |
| **Capacity headroom** | Remaining unused capacity available for growth or unexpected demand above current peak utilisation |
| **Capacity threshold** | A defined utilisation level that triggers alerts or actions when exceeded (warning, critical, or maximum) |
| **Cooldown period** | Minimum interval between auto-scaling actions to prevent rapid oscillation between scaling in and scaling out |
| **DDoS** | Distributed denial-of-service — an attack that attempts to overwhelm a service by flooding it with traffic from multiple sources |
| **Growth rate** | The rate at which resource consumption increases over time, typically measured as a percentage per month or absolute units per month |
| **IOPS** | Input/output operations per second — a storage performance metric measuring the rate of read and write operations |
| **Load shedding** | Deliberately reducing system load during capacity pressure by deprioritising non-essential workloads or rate-limiting requests |
| **Right-sizing** | Adjusting resource allocation to match actual utilisation, eliminating over-provisioned or under-provisioned resources |
| **Scale-in** | Reducing the number of allocated resources (instances, containers) when demand decreases |
| **Scale-out** | Increasing the number of allocated resources (instances, containers) when demand increases |
| **SLO** | Service level objective — a measurable target for service performance (e.g., availability, latency) that capacity must support |
| **Utilisation** | The proportion of a resource's total capacity currently in use, typically expressed as a percentage |

---

## Roles and Responsibilities

| Role | Responsibilities |
|------|-----------------|
| **CISO** | Policy ownership; ensuring capacity for security systems (SIEM, logging, EDR); compliance verification for A.8.6; escalation of capacity risks affecting security posture; annual policy review |
| **CIO / IT Director** | Overall accountability for capacity management programme effectiveness; approval of capacity expansion plans; strategic capacity planning; budget oversight |
| **CFO / Finance** | Approval of capacity management budgets (CapEx and OpEx); financial review of capacity investments; cost optimisation oversight |
| **Infrastructure Manager / IT Operations Manager** | Day-to-day capacity monitoring and alert response; threshold configuration and tuning; capacity forecasting; reporting; emergency capacity mitigation |
| **Cloud Architect / Platform Engineer** | Auto-scaling policy design and implementation; cloud quota management; cost optimisation for cloud resources; reserved instance planning |
| **Application Owners / System Owners** | Business growth projections for capacity planning; participation in capacity review meetings; budget for application-specific capacity |
| **Information Security Manager** | Policy maintenance; exception review; compliance reporting; audit coordination; non-conformance tracking |
| **All Staff** | Reporting of observed performance issues; adherence to approved resource usage policies |

---

## Evidence

The following evidence demonstrates compliance with this policy:

| # | Evidence | Owner | Frequency | Retention |
|---|----------|-------|-----------|-----------|
| 1 | **Monitoring coverage report** showing percentage of production and non-production systems monitored | Infrastructure Manager | Monthly | 3 years |
| 2 | **Threshold configuration documentation** for all monitored resources | Infrastructure Manager | Reviewed quarterly; updated as needed | Current + 2 years |
| 3 | **Alert history and response records** (alerts raised, acknowledged, resolved, response times) | IT Operations | Continuous | 3 years |
| 4 | **Monthly capacity reports** with utilisation summaries and trend data | Infrastructure Manager | Monthly | 3 years |
| 5 | **Quarterly capacity forecasts** with accuracy measurements (actual vs. predicted) | Infrastructure Manager | Quarterly | 3 years |
| 6 | **Annual capacity plan** with strategic projections and investment requirements | CIO / Infrastructure Manager | Annually | 5 years |
| 7 | **Auto-scaling configuration records** and change history | Cloud Architect / Platform Engineer | Maintained continuously; reviewed quarterly | Life of configuration + 1 year |
| 8 | **Capacity-related incident records** and post-incident review reports | IT Operations / Infrastructure Manager | Per incident | 3 years |
| 9 | **Licence inventory and usage reports** showing entitlements vs. active allocations | IT Operations / Procurement | Quarterly | 3 years |
| 10 | **Capacity Planning Committee meeting minutes** or capacity review meeting notes | Infrastructure Manager | Per meeting | 3 years |
| 11 | **Exception register** for capacity policy exceptions with approvals and compensating controls | Information Security Manager | Maintained continuously; reviewed quarterly | Exception duration + 3 years |
| 12 | **Storage growth trend reports** (including log, database, and backup storage) | Infrastructure Manager | Monthly | 3 years |
| 13 | **Cost optimisation reports** documenting right-sizing actions, reserved capacity decisions, and savings achieved | Infrastructure Manager / Cloud Architect | Quarterly | 3 years |

---

# Policy Compliance

## Compliance Measurement

The information security management team will verify compliance with this policy through monitoring coverage audits, threshold configuration reviews, forecast accuracy assessments, capacity reporting timeliness, internal and external audits, and feedback to the policy owner.

**Compliance Metrics**:

| Metric | Target | Measurement Frequency |
|--------|--------|-----------------------|
| Production systems with capacity monitoring enabled | 100% | Monthly |
| Non-production systems with capacity monitoring enabled | >= 90% | Quarterly |
| Resources with defined and documented thresholds | >= 95% | Quarterly |
| Warning alerts acknowledged within 4 hours (business hours) | >= 90% | Monthly |
| Critical alerts acknowledged within 30 minutes | >= 95% | Monthly |
| Capacity forecast accuracy (within +/-15%) | >= 80% of forecasts | Quarterly |
| Monthly capacity reports delivered on schedule | 100% | Monthly |
| Capacity-related service outages per quarter | < 2 | Quarterly |

**Compliance Scoring**:

| Component | Weight | Calculation |
|-----------|--------|-------------|
| Monitoring Coverage | 30% | (Monitored production systems / Total production systems) x 100 |
| Threshold and Alerting | 25% | (Resources with compliant thresholds + alerts responded within SLA) / Total x 100 |
| Forecasting and Planning | 25% | (Accurate forecasts + forecasts delivered on schedule) / Total forecasts x 100 |
| Reporting and Governance | 20% | (Reports delivered on schedule + reviews completed) / Total required x 100 |

**Non-Compliance Handling**: Below 70% requires immediate CIO and CISO escalation with remediation plan within 10 business days. 70-89% requires Infrastructure Manager oversight with monthly improvement reviews. 90% and above follows standard quarterly monitoring.

**Remediation Ownership by Score Component**:

| Component | Below Target | Remediation Owner | Escalation |
|-----------|-------------|-------------------|------------|
| Monitoring Coverage | <100% production | Infrastructure Manager | CIO at 30 days overdue |
| Threshold and Alerting | <95% | IT Operations / Infrastructure Manager | CISO at 15 days overdue |
| Forecasting and Planning | <80% accuracy | Infrastructure Manager | CIO at quarterly review |
| Reporting and Governance | <100% on-time | Infrastructure Manager | CIO at 15 days overdue |

## Exceptions

Any exception to this policy shall be approved and recorded by the Information Security Manager in advance, with documented risk acceptance, compensating controls, and a defined review date (maximum 12 months). Exceptions for critical production systems require joint CIO and CISO approval. All active exceptions shall be reviewed quarterly and reported to the Management Review Team.

## Non-Compliance

An employee found to have violated this policy may be subject to disciplinary action, up to and including termination of employment. Policy violations shall be documented, investigated by the Information Security Manager, and reported to the CISO. Capacity-related incidents caused by policy non-compliance (e.g., failure to monitor, failure to act on alerts) shall be treated as contributing factors in incident post-mortem reviews.

## Continual Improvement

This policy is reviewed and updated as part of the continual improvement process. Reviews shall consider changes to infrastructure platforms and cloud services, capacity-related incident trends and near-miss analysis, improvements to monitoring and forecasting tools, regulatory changes affecting availability requirements, cost optimisation opportunities, and lessons learned from capacity exhaustion events.

---

# Areas of the ISO 27001 Standard Addressed

Capacity Management Policy — ISO 27001 Controls Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership and commitment | 5.1 Policies for information security |
| Clause 5.2 Policy | 5.4 Management responsibilities |
| Clause 6.2 Information security objectives | 5.36 Compliance with policies, rules, and standards |
| Clause 9.1 Monitoring, measurement, analysis, and evaluation | 5.37 Documented operating procedures |
| Clause 9.3 Management review | 6.3 Information security awareness, education, and training |
| | **8.6 Capacity management** |
| | 8.13 Information backup |
| | 8.14 Redundancy of information processing facilities |
| | 8.16 Monitoring activities |

**Regulatory and Legal Framework**:

| Framework | Relevance |
|-----------|-----------|
| Swiss nFADP (revDSG) | Art. 8 — Technical and organisational measures; capacity management ensures availability of systems processing personal data |
| Swiss DSV (Data Protection Ordinance) | Art. 1–3 — Minimum requirements for data security include system availability |
| EU GDPR (where applicable) | Art. 32(1)(b) — Ability to ensure ongoing availability and resilience of processing systems and services |
| ISO/IEC 27001:2022 | Annex A Control 8.6 — Capacity management |
| ISO/IEC 27002:2022 | Section 8.6 — Implementation guidance for capacity management |
| NIST SP 800-53 Rev 5 | AU-4 (Audit Log Storage Capacity), CP-2(2) (Capacity Planning), SC-5 (Denial-of-Service Protection) |
| NIST CSF 2.0 | PR.IR-01 (Networks and environments are protected from unauthorized logical access), DE.CM (Continuous Monitoring) |
| CIS Controls v8 | Control 8 (Audit Log Management — log storage capacity), Control 13 (Network Monitoring and Defence) |
| ITIL 4 | Capacity and Performance Management Practice |
| FINMA (if applicable) | Circular 2023/1 — ICT operational resilience includes capacity management |
| DORA (if applicable) | Art. 11 — ICT capacity planning for digital operational resilience |
| NIS2 (if applicable) | Art. 21(2) — Business continuity includes capacity management |

---

<!-- QA_VERIFIED: 2026-02-08 -->
