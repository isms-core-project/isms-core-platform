# PROJECT BRIEF: ISMS Control A.8.6 - Capacity Management

## Standalone Control Approach

You are implementing **ONE ISO 27001:2022 Annex A control**:

- **A.8.6 - Capacity Management**: Monitoring and projecting resource usage to ensure availability

**Why Standalone:**
This control addresses a specific operational concern: **ensuring sufficient capacity to maintain availability and performance**. While it relates to availability (A.8.14 - Redundancy) and monitoring (A.8.16), it focuses specifically on **capacity planning and resource forecasting**.

**Reference Implementation**: 
- **Quality level**: ISMS-A.8.23-Web-Filtering (standalone control)
- **Approach**: Focused policy on capacity monitoring and planning

**Integration Note**: This control integrates with:
- A.8.14 (Redundancy) - Redundant capacity for resilience
- A.8.16 (Monitoring) - Real-time resource monitoring
- A.7.11 (Supporting Utilities) - Physical infrastructure capacity (power, cooling)
- A.5.30 (ICT BC Readiness) - Capacity for business continuity
- A.8.13 (Information Backup) - Backup storage capacity

## Context & Approach

You are implementing **Capacity Management** using Systems Engineering methodology. This framework must be **completely generic** - applicable to any organization's infrastructure, whether on-premises, cloud, or hybrid.

**Implementation Philosophy**: 
- Apply Feynman's "don't fool yourself" principle - no security theater
- System Engineering approach: Monitor → Analyze → Forecast → Plan
- Think with TWO hats simultaneously:
  * **ISMS Implementer**: Build practical capacity management framework
  * **ISMS Auditor**: Verify measurable capacity planning effectiveness
- Focus on genuine availability and performance, not checkbox compliance

**Applicability**:
- All content must be **completely generic and environment-agnostic**
- Use "[Organization]" as placeholder throughout
- No assumptions about infrastructure type (servers, cloud, hybrid)
- No assumptions about monitoring tools (Prometheus, Datadog, CloudWatch, etc.)
- Framework adapts to any capacity management environment

## Core Requirements (Specific to A.8.6)

### 1. The Capacity Management Challenge

**Traditional approach (cargo cult):**
```
"We have monitoring. Servers are... 60% CPU? Seems fine.
We'll add capacity when something breaks."
[No capacity planning, no forecasting, reactive approach only]
```
❌ This is meaningless checkbox compliance.

**What auditors and implementers actually need:**

**For A.8.6 (Capacity Management):**
- Capacity management policy
  - Capacity monitoring scope (compute, storage, network, application)
  - Capacity thresholds (warning, critical)
  - Capacity forecasting methodology (trend analysis, growth projections)
  - Capacity planning cycle (quarterly, annually)
  - Responsibility assignment (who monitors, who plans, who approves capacity additions)
- Resource types to monitor
  - **Compute capacity**:
    - CPU utilization (per server, per cluster)
    - Memory utilization
    - Virtual machine capacity (if virtualized)
    - Container capacity (if containerized - Kubernetes pods, nodes)
  - **Storage capacity**:
    - Disk space utilization (per volume, per system)
    - Database storage growth
    - Backup storage capacity
    - Archive storage capacity
  - **Network capacity**:
    - Network bandwidth utilization
    - Network throughput (packets per second)
    - Load balancer capacity
    - Firewall throughput
  - **Application capacity**:
    - Concurrent users/sessions
    - Transaction rates (requests per second)
    - Queue depths (message queues, job queues)
    - API rate limits
  - **Cloud capacity** (if applicable):
    - Cloud service limits (AWS service quotas, Azure subscription limits)
    - Cloud cost thresholds (budget alerts)
- Capacity monitoring
  - Real-time monitoring (current utilization)
  - Historical data collection (trends over time)
  - Peak usage tracking (maximum observed capacity)
  - Monitoring frequency (every minute, every 5 minutes)
  - Monitoring retention (1-3 years for trend analysis)
- Capacity thresholds and alerting
  - Warning thresholds (e.g., 70% utilization - plan capacity expansion)
  - Critical thresholds (e.g., 85% utilization - immediate action required)
  - Alerting mechanisms (email, SMS, incident management system)
  - Escalation procedures (if capacity not addressed)
- Capacity forecasting
  - Trend analysis (linear growth, seasonal patterns)
  - Growth rate calculation (percent growth per month/quarter/year)
  - Forecasting horizon (6-12 months typical)
  - Forecasting accuracy validation (actual vs. predicted)
- Capacity planning
  - Capacity expansion planning (when to add capacity, how much)
  - Lead time consideration (hardware procurement, cloud provisioning)
  - Budget planning (capital expenditure for capacity)
  - Capacity optimization (right-sizing, resource consolidation)
- Capacity testing
  - Load testing (verify capacity under expected load)
  - Stress testing (verify capacity under peak load)
  - Scalability testing (verify horizontal/vertical scaling)
- Capacity reporting
  - Monthly capacity reports (utilization, trends, forecasts)
  - Capacity planning presentations (to management)
  - Capacity incident reports (capacity exhaustion events)

**Your SE Framework Must Provide:**
- **Capacity Monitoring Framework** - systematic resource utilization tracking
- **Capacity Forecasting Methodology** - trend analysis and growth projections
- **Capacity Planning Process** - proactive capacity expansion
- **Evidence Collection Framework** - monitoring data, forecasts, planning documentation

### 2. Document Length and Quality Guidelines

**Python Scripts:**
- Scripts should be **as long as required** to meet quality standards
- No arbitrary line limits - focus on correctness and robustness
- Capacity forecasting may require statistical analysis (trend lines, growth rates)
- Quality > arbitrary length constraints

**Policy Document (POL):**
- Should be **comprehensive but not over-engineered**
- Include everything necessary for implementation and audit
- This is a single control, focused on capacity planning
- Expected range: 400-600 lines total
- "Just right" - not too short (incomplete), not too long (overkill)

**Implementation Guide (IMP):**
- Should be **practical and focused**
- Step-by-step procedures without unnecessary elaboration
- Include examples for common monitoring tools

**Annexes:**
- Monitoring tool comparison (Prometheus, Datadog, CloudWatch, etc.)
- Capacity forecasting formulas
- Capacity planning templates

### 3. Document Structure (Adapted for A.8.6)

```
ISMS-A.8.6-Capacity-Management/
├── 00_pol-struc/
│   └── [Policy planning notes]
├── 10_pol-md/
│   ├── ISMS-POL-A.8.6-S1-Executive-Summary-Control-Alignment.md
│   ├── ISMS-POL-A.8.6-S2-Capacity-Management-Policy.md
│   ├── ISMS-POL-A.8.6-S3-Assessment-Evidence-Framework.md
│   └── ISMS-POL-A.8.6-Annex-[Topic].md [if needed]
├── 30_imp-md/
│   ├── ISMS-IMP-A.8.6-S1-Capacity-Monitoring-Implementation.md
│   ├── ISMS-IMP-A.8.6-S2-Capacity-Forecasting-Planning.md
│   ├── ISMS-IMP-A.8.6-S3-Capacity-Management-Assessment.md
│   └── ISMS-IMP-A.8.6-Annex-[Topic].md [if needed]
└── 50_scripts-excel/
    ├── generate_assessment_1_capacity_utilization.py
    ├── generate_assessment_2_capacity_forecasts.py
    └── generate_dashboard_capacity_management.py
```

### 4. Policy Content Requirements (Specific to A.8.6)

**Section 1 (S1): Executive Summary, Control Alignment, Scope**
- ISO 27001:2022 control text for A.8.6 (exact quote)
- Executive summary explaining capacity management
- Scope: All infrastructure resources (compute, storage, network, application)
- Integration with other controls (monitoring, redundancy, BC/DR)

**Section 2 (S2): Capacity Management Policy**
Focus on **A.8.6 - Capacity Management** specifically:
- Capacity management policy (scope, thresholds, forecasting, planning)
- Resource types (compute, storage, network, application, cloud)
- Capacity monitoring (real-time, historical, retention)
- Capacity thresholds and alerting (warning, critical)
- Capacity forecasting (trend analysis, growth projections)
- Capacity planning (expansion, lead time, budget)
- Capacity testing (load, stress, scalability)
- Capacity reporting (monthly reports, management presentations)
- Measurable requirements with audit verification criteria

**Section 3 (S3): Assessment Methodology and Evidence Framework**
- Capacity utilization assessment
- Capacity forecast accuracy validation
- Capacity planning effectiveness
- Evidence collection
- Compliance scoring

### 5. Implementation Guidance Requirements

**IMP-S1: Capacity Monitoring Implementation**
- Monitoring tool selection and deployment (Prometheus, Datadog, CloudWatch, Nagios)
- Resource monitoring configuration (compute, storage, network, application)
- Threshold configuration (warning, critical)
- Alerting integration (email, SMS, PagerDuty, Slack)

**IMP-S2: Capacity Forecasting and Planning**
- Trend analysis methodology (linear regression, growth rates)
- Forecasting tool selection (Excel, Python, monitoring tool built-in)
- Capacity planning procedures (quarterly/annual planning cycle)
- Capacity expansion procedures (procurement, provisioning, scaling)

**IMP-S3: Capacity Management Assessment**
- Capacity utilization analysis
- Forecast accuracy validation
- Capacity planning effectiveness
- Continuous monitoring and improvement

### 6. Assessment Tools (Specific to A.8.6)

**Assessment Workbook 1: Capacity Utilization**
- Resource inventory (servers, storage, network, applications)
- Current utilization (CPU, memory, disk, network - % used)
- Peak utilization (maximum observed)
- Threshold status (below warning, warning, critical)
- Capacity headroom (% remaining capacity)

**Assessment Workbook 2: Capacity Forecasts and Planning**
- Resource → forecasted utilization (6 months, 12 months)
- Forecasted capacity exhaustion date (if no expansion)
- Planned capacity expansions (date, amount, status)
- Forecast accuracy (previous forecasts vs. actual)
- Planning effectiveness (proactive vs. reactive expansions)

**Dashboard: Capacity Management Overview**
- Overall capacity health score
- Resources at/above warning threshold (%)
- Resources at/above critical threshold (%)
- Forecasted capacity exhaustion (months until exhaustion)
- Capacity planning status (expansions planned/completed)
- Trend analysis (utilization over time)

### 7. Python Scripts Approach

Scripts should:
- Parse monitoring tool data (APIs or exports)
- Calculate utilization percentages
- Perform trend analysis (linear regression)
- Calculate forecasted capacity exhaustion dates
- Generate capacity reports and dashboards

**No arbitrary line limits** - statistical analysis and forecasting can be complex.

### 8. Key Integration Points

**Integrates with:**
- A.8.14 (Redundancy) - Redundant capacity planning
- A.8.16 (Monitoring) - Real-time resource monitoring
- A.7.11 (Supporting Utilities) - Physical infrastructure capacity (power, cooling, HVAC)
- A.5.30 (ICT BC Readiness) - Capacity for business continuity
- A.8.13 (Information Backup) - Backup storage capacity planning

### 9. Quality Checks

- [ ] Control text quoted correctly (A.8.6)
- [ ] Framework works for on-premises, cloud, hybrid
- [ ] No assumptions about monitoring tools
- [ ] Assessment workbooks comprehensive
- [ ] Forecasting methodology clear
- [ ] Capacity planning process documented

### 10. Regulatory Framework (per ISMS-POL-00)

**Mandatory Compliance (Tier 1):**
- ISO/IEC 27001:2022: Control A.8.6

**Conditional Compliance (Tier 2):**
- **FINMA** (if Swiss financial institution):
  - FINMA Circular 2023/1 Margin 50-62: ICT operational resilience includes capacity management
- **DORA** (if EU financial entity):
  - Article 11: ICT capacity planning to ensure availability
- **NIS2** (if essential/important entity):
  - Article 21(2): Business continuity includes capacity planning

**Informational Reference (Tier 3):**
- ITIL Capacity Management (IT service management best practices)
- NIST SP 800-53: AU-6 (Audit Record Review, Analysis, and Reporting - includes capacity monitoring)

For complete regulatory categorization, refer to ISMS-POL-00.

### 11. Special Considerations

**Cloud vs. On-Premises:**
- **On-premises**: Hardware procurement lead time (weeks to months)
- **Cloud**: Instant provisioning (minutes), but cost implications
- Framework must address both

**Elastic Scaling:**
- Auto-scaling (cloud-native, Kubernetes HPA)
- Manual scaling (traditional infrastructure)
- Framework must address both

**Monitoring Tool Diversity:**
- **Open source**: Prometheus, Grafana, Nagios, Zabbix
- **Commercial SaaS**: Datadog, New Relic, Dynatrace
- **Cloud-native**: AWS CloudWatch, Azure Monitor, GCP Cloud Monitoring
- Framework must be tool-neutral

**Capacity Optimization:**
- Right-sizing (reduce over-provisioned resources)
- Resource consolidation (reduce sprawl)
- Reserved capacity (cloud commitments for cost savings)

**Capacity Testing:**
- Load testing (verify capacity under expected load)
- Stress testing (find breaking point)
- Chaos engineering (verify resilience under failure)

### 12. Autonomous Work Requirements

Follow standard autonomous work requirements:
- READ reference implementations
- UPDATE with capacity management context
- TEST (UTF-8, formulas, scripts - especially forecasting calculations)
- PRESENT complete deliverables

### 13. Deliverable Sequence

1. **Structure Plan** - Confirm approach
2. **Policy Sections** (S1→S2→S3) - Wait for approval
3. **Implementation Sections** (S1→S2→S3) - Wait for approval
4. **Assessment Scripts** - Test thoroughly (especially trend analysis)
5. **Quality Review** - Self-assessment

---

## Your Mission for A.8.6

Create the **Capacity Management Framework** that provides:
- Systematic resource utilization monitoring
- Trend analysis and capacity forecasting
- Proactive capacity planning procedures
- Comprehensive capacity reporting
- Environment and tool-agnostic principles

Use Systems Engineering methodology for **systematic capacity management assessment**.

Make it completely generic - works for any infrastructure, any monitoring tool, any organization.

Think like a systems engineer AND an auditor.

**Ready? Let's start with the structure plan.**
