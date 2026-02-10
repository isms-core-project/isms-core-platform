<!-- ISMS-CORE:POLICY:ISMS-POL-A.8.6:framework:GOV-POL:a.8.6 -->
**ISMS-POL-A.8.6 – Capacity Management**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Capacity Management Policy |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.8.6 |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | Chief Executive Officer (CEO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | CISO / Information Security Manager | Initial policy for ISO 27001:2022 certification |

**Review Cycle**: Annual (aligned with capacity planning cycle)
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:

- Primary: Chief Information Security Officer (CISO)
- Technical Review: IT Operations Manager / Infrastructure Manager
- Financial Review: Chief Financial Officer (CFO)
- Final Authority: Chief Information Officer (CIO)

**Related Documents**:

- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-IMP-A.8.6.1-UG/TG (Capacity Monitoring Implementation)
- ISMS-IMP-A.8.6.2-UG/TG (Capacity Forecasting and Planning)
- ISMS-IMP-A.8.6.3-UG/TG (Capacity Management Assessment)
- ISO/IEC 27001:2022 Control A.8.6

---

# Executive Summary

This policy establishes [Organization]'s requirements for capacity management to ensure sufficient infrastructure and application capacity in accordance with ISO/IEC 27001:2022 Control A.8.6.

**Purpose**: Define organizational requirements for capacity management governance. This policy establishes WHAT capacity management controls are required, WHEN capacity planning must occur, and WHO is accountable. Implementation procedures (HOW monitoring, forecasting, and planning are performed) are documented in ISMS-IMP-A.8.6 series.

**Regulatory Alignment**: This policy addresses mandatory compliance requirements per ISMS-POL-00 (Regulatory Applicability Framework), including ISO/IEC 27001:2022 Control A.8.6. Conditional sector-specific requirements (FINMA Circular 2023/1, DORA Article 11, NIS2 Article 21) apply where [Organization]'s business activities trigger applicability.

---

# Scope

## Applicability

**This policy applies to**:

**Infrastructure Resources**:

- Compute capacity (servers, virtual machines, containers, cloud instances)
- Storage capacity (disk space, database storage, backup storage, archive storage)
- Network capacity (bandwidth, throughput, connections, load balancer capacity)
- Application capacity (concurrent users, transaction rates, API rate limits)
- Cloud capacity (cloud service quotas, limits, instance counts)
- Physical infrastructure (power capacity, cooling capacity, rack space per A.7.11)

**Coverage**:

- All infrastructure supporting production business operations (mandatory)
- Development, test, and quality assurance environments (recommended)
- Business continuity and disaster recovery sites (per A.5.30)
- Third-party hosted infrastructure (where [Organization] has capacity management responsibility)

**Personnel**:

- Executive management (capacity planning budget approval)
- Capacity planning team (monitoring, forecasting, planning, reporting)
- IT operations team (day-to-day monitoring, alert response)
- Application owners / system owners (business growth projections)
- Financial controller / CFO (capacity budget approval)

**Out of Scope**:

- Application performance tuning (covered under application optimization)
- Software licensing management (covered under asset management)

## ISO/IEC 27001:2022 Control Alignment

**ISO/IEC 27001:2022 Annex A.8.6 - Capacity Management**

> *The use of resources should be monitored and tuned, and projections of future capacity requirements should be made to ensure the required system performance and to inform investment decisions.*

**Control Objective**: Ensure adequate resources are available to meet current and future performance and availability requirements through monitoring, tuning, and projection.

## Policy Integration

This control integrates with:

- **A.8.16 - Monitoring Activities**: Capacity metrics as subset of overall monitoring
- **A.8.14 - Redundancy**: Capacity planning for failover scenarios
- **A.8.13 - Information Backup**: Backup storage capacity planning
- **A.7.11 - Supporting Utilities**: Physical infrastructure capacity (power, cooling)
- **A.5.30 - ICT Readiness for Business Continuity**: Recovery site capacity

---

# Policy Statements

## Capacity Monitoring Requirements

[Organization] SHALL implement capacity monitoring for all infrastructure and application resources supporting business operations with the following characteristics:

- **Metric collection frequency**: Minimum every 5 minutes for production systems, every 15 minutes for non-production systems
- **Data completeness**: 99.5% metric availability (excluding planned maintenance windows)
- **Alert delivery**: Threshold breach alerts delivered within 5 minutes of detection
- **Coverage verification**: Monthly assessment per ISMS-IMP-A.8.6.3

**Monitoring Coverage Requirements**:

- Production systems: 100% monitoring coverage required
- Non-production systems: 90% monitoring coverage recommended
- Cloud infrastructure: All cloud services and resources monitored
- Network infrastructure: Bandwidth, throughput, and connections monitored
- Physical infrastructure: Power and cooling capacity monitored per A.7.11

**Data Retention Requirements**:

- Raw metrics: Minimum 30 days for incident investigation
- Aggregated metrics: Minimum 12 months for trend analysis
- Historical data: Minimum 36 months for strategic planning

## Capacity Threshold Requirements

[Organization] SHALL define and implement capacity thresholds for all monitored resources.

**Threshold Framework**:

- **Warning threshold**: Triggers capacity planning activities before exhaustion
- **Critical threshold**: Triggers immediate action to prevent exhaustion
- **Maximum capacity**: Absolute limit requiring immediate response

Thresholds SHALL be reviewed quarterly and tuned based on false positive rates, near-miss incidents, and workload pattern changes.

## Capacity Alerting Requirements

[Organization] SHALL implement alerting for capacity threshold breaches with:

- Routing to appropriate teams based on severity
- Escalation procedures for unacknowledged alerts
- Integration with incident management processes

## Capacity Forecasting Requirements

[Organization] SHALL develop capacity forecasts for all critical infrastructure and application resources.

**Forecasting Requirements**:

- Short-term forecasts: 3-6 months (tactical planning)
- Medium-term forecasts: 6-12 months (budget planning)
- Long-term forecasts: 12-24 months (strategic planning)

**Update Frequency**:

- Monthly: Short-term forecast updates
- Quarterly: Comprehensive forecast review
- Annually: Strategic forecast aligned with budget cycle

**Accuracy Target**: Forecasts within ±15% of actual utilization (measured quarterly).

**Accuracy Target Exceptions**:
- New systems (first 6 months post-deployment): ±30% accuracy acceptable while baseline established
- High-variability workloads (systems with >50% utilization variance): ±25% accuracy with CIO approval
- Program maturity (first 12 months of program): ±20% accuracy target, tightening to ±15% thereafter

**Accuracy Measurement**:
- Calculate quarterly: (Actual Utilization - Forecasted Utilization) / Forecasted Utilization
- Document in ISMS-IMP-A.8.6.2 workbook with trend analysis
- Root cause analysis required for deviations >15% (completed within 10 business days)

## Capacity Planning Requirements

[Organization] SHALL implement a structured capacity planning process.

**Planning Cycle Requirements**:

- Monthly review: Capacity alerts, near-miss events, short-term forecasts
- Quarterly planning: Comprehensive planning with 12-month horizon
- Annual budget: Long-term planning aligned with budget cycle

**Approval Requirements**:

- Routine capacity: IT Director/CIO within approved budget
- Major capacity: CFO approval for budget impact
- Emergency capacity: CIO fast-track approval with executive notification

## Capacity Reporting Requirements

[Organization] SHALL produce regular capacity reports:

- **Monthly**: Utilization summary, incidents, forecast highlights, actions
- **Quarterly**: Comprehensive forecasts, expansion plans, health scorecard
- **Annually**: Strategic capacity plan with multi-year projections

**Report Evidence Requirements**:
- Reports SHALL be generated from monitoring platform via ISMS-IMP-A.8.6 Python scripts
- Monthly reports: Delivered to IT Leadership Team, stored in GRC Platform/SharePoint
- Quarterly reports: Presented to Capacity Planning Committee with meeting minutes
- Annual reports: Approved by CIO, included in management review (ISO 27001 Clause 9.3)

## Capacity Management Evidence Requirements

[Organization] SHALL maintain verifiable evidence of capacity management activities to demonstrate control effectiveness per ISO/IEC 27001:2022 requirements.

**Monitoring Evidence**:
- Metric data: 30 days raw, 12 months aggregated, 36 months historical
- Coverage assessments: Monthly per ISMS-IMP-A.8.6.3, retained 12 months
- Threshold configurations: Current configuration with quarterly review documentation, retained 24 months

**Forecasting Evidence**:
- Capacity forecasts: All forecasts retained 36 months (short-term, medium-term, long-term)
- Accuracy assessments: Quarterly calculations per ISMS-IMP-A.8.6.2, retained 36 months
- Root cause analyses: Deviations >15% documented and retained 24 months

**Planning Evidence**:
- Capacity Planning Committee meeting minutes: Retained 36 months
- Expansion plans: Approved plans retained 36 months
- Exception requests: All requests with approvals retained until remediation + 12 months

**Evidence Storage**:
- Automated evidence (Python workbooks, monitoring data): GRC Platform/Monitoring Platform
- Manual evidence (meeting minutes, approvals): Document Management System/SharePoint
- Audit trail: All evidence timestamped and version-controlled

## Capacity Management Failure Modes and Response

**Forecast Accuracy Failures**:
- IF forecast accuracy >15% deviation: Infrastructure Manager SHALL conduct root cause analysis within 10 business days
- Analysis SHALL document: forecast assumptions, actual vs. projected comparison, deviation causes, methodology improvements
- Findings SHALL be presented to Capacity Planning Committee and incorporated into next forecast cycle
- IF deviation >30%: CIO notification required with process improvement plan

**Capacity Exhaustion Events**:
- IF critical capacity threshold breached: IT Operations SHALL immediately implement mitigation per runbook
- IF capacity exhaustion occurs (service impact): Classify as Priority 1 incident per ISMS-POL-A.5.24-28 (Incident Management)
- Post-incident review SHALL include: why monitoring/forecasting didn't prevent exhaustion, threshold tuning, process improvements
- Findings SHALL be tracked in Gap Register until remediation complete

**Monitoring Coverage Gaps**:
- IF production coverage falls below 100%: Infrastructure Manager SHALL create remediation plan within 5 business days
- Completion required within 30 days for production systems, 60 days for non-production systems
- IF critical system monitoring fails: Immediate escalation to CIO + CISO within 4 hours
- Emergency remediation (manual monitoring) required within 24 hours

**Gap Register Integration**:
All capacity management non-conformances SHALL be logged in Gap Register with:
- Gap ID, control reference (A.8.6), description, risk rating
- Corrective action plan (who, what, when), verification method
- Gap Register reviewed monthly by IT Leadership Team

---

# Roles and Responsibilities

## Executive Management (CEO, Board)

**Accountabilities**:

- Ultimate accountability for adequate capacity to support business operations
- Approve major capacity investments and strategic capacity plans
- Ensure adequate budget allocation for capacity management program

## Chief Information Officer (CIO)

**Accountabilities**:

- Overall accountability for capacity management program effectiveness
- Ensure capacity headroom meets organizational targets:
  - Production systems: Minimum 20% headroom at peak utilization
  - Storage systems: Minimum 3 months headroom at current growth rate
  - Network bandwidth: Minimum 30% headroom during business hours
- Balance capacity requirements with budget constraints

**Authorities**:

- Approve capacity expansion plans within budget
- Authorize emergency capacity procurement
- Allocate IT resources for capacity planning

## Chief Information Security Officer (CISO)

**Accountabilities**:

- Ensure capacity for security systems (SIEM, logging, monitoring, EDR)
- Risk assessment for capacity-related security issues
- Compliance verification for capacity management controls (ISO 27001 A.8.6)

**Authorities**:

- Require capacity planning for security systems
- Approve capacity management policy
- Escalate capacity risks that impact security posture

## Capacity Planning Team / Infrastructure Manager

**Accountabilities**:

- Day-to-day execution of capacity management program
- Capacity monitoring, forecasting, and trend analysis
- Capacity expansion planning and coordination
- Capacity reporting to management

**Authorities**:

- Implement capacity monitoring for all resources
- Define capacity thresholds and alerting rules
- Recommend capacity expansion plans

## IT Operations Team

**Accountabilities**:

- Day-to-day capacity monitoring and alert response
- Immediate response to capacity incidents
- Deployment of approved capacity expansions

**Authorities**:

- Execute emergency capacity mitigation actions
- Implement approved capacity tuning and optimization
- Escalate capacity issues per procedures

## Application Owners / System Owners

**Accountabilities**:

- Provide business growth projections for capacity planning
- Participate in capacity planning for their applications
- Budget for application capacity requirements

## Chief Financial Officer (CFO)

**Accountabilities**:

- Approve capacity management budgets (CapEx and OpEx)
- Financial reporting on capacity investments
- Cost optimization oversight

---

# Governance and Compliance

## Policy Governance Framework

**Policy Owner**: Chief Information Security Officer (CISO)
**Policy Approver**: Chief Information Officer (CIO)
**Policy Review**: Annual review aligned with capacity planning cycle

**Governance Bodies**:

**Capacity Planning Committee** (Operational):

- Chair: Infrastructure Manager or Capacity Planning Manager
- Core Members: IT Operations Manager, Application Owners, Network Manager, Cloud Architect
- Business Representatives: Business Unit Leader or Product Manager (for growth projections)
- Financial Representative: Finance Manager or Budget Analyst (for budget planning)
- Frequency: Monthly
- Purpose: Review capacity status, forecasts, plan expansions, align with business roadmap

**IT Leadership Team** (Strategic):

- Members: CIO, CISO, CFO, IT Director
- Frequency: Quarterly
- Purpose: Review capacity reports, approve budgets, strategic decisions

## Regulatory Compliance

This policy satisfies requirements per **ISMS-POL-00 (Regulatory Applicability Framework)**:

**Tier 1 - Mandatory Compliance**:

- **ISO/IEC 27001:2022**: Control A.8.6 (Capacity Management)

**Tier 2 - Conditional Applicability** (where business activities trigger):

- **FINMA Circular 2023/1** (Swiss financial institutions): ICT operational resilience
- **DORA Article 11** (EU financial entities): ICT capacity planning
- **NIS2 Article 21(2)** (Essential/important entities): Business continuity capacity

**Tier 3 - Informational Reference**:

- ITIL 4 Capacity Management
- NIST SP 800-53 AU-6

## Policy Exceptions

**Temporary Exceptions - Critical Systems** (supporting essential business operations per BIA):
- Maximum duration: 3 months
- Approved by: CIO + CISO (joint approval required)
- Conditions: Compensating controls required, risk acceptance documented, weekly status review
- Documentation: Exception request with risk assessment, mitigation plan, remediation timeline

**Temporary Exceptions - Non-Critical Systems**:
- Maximum duration: 6 months
- Approved by: IT Director or CIO
- Conditions: Risk acceptance documented, monthly status review
- Documentation: Exception request with mitigation plan, remediation timeline

**Permanent Exceptions**:

- Approved by: CIO + CISO + Executive Management
- Documentation: Formal risk acceptance, compensating controls
- Review: Annual re-approval required

## Compliance Verification

**Monthly Self-Assessment** (per ISMS-IMP-A.8.6.3):
- **Performed by**: Infrastructure Manager or designated Capacity Planning Team member
- **Scope**: Monitoring coverage %, threshold configuration, forecasting completeness, reporting timeliness
- **Output**: ISMS-IMP-A.8.6.3 Python-generated workbook with pass/fail results
- **Review**: Presented to IT Operations Manager within 10 business days of month end
- **Tracking**: Non-conformances logged in Gap Register

**Quarterly Internal Audit**:
- **Performed by**: Internal Audit function or CISO-designated auditor (independent of capacity planning team)
- **Scope**: Sample 3 critical systems, verify monitoring configuration, review last 3 months of forecasts, interview capacity planning team
- **Output**: Audit report with findings, evidence samples, recommendations
- **Review**: Presented to IT Leadership Team within 15 business days of quarter end
- **Tracking**: Non-conformances tracked in Gap Register with corrective action plans

**Annual External Audit**:
- **Performed by**: ISO 27001 certification auditor
- **Scope**: Full control assessment per ISO 27001:2022 A.8.6
- **Response**: CISO SHALL coordinate response, corrective action plans within 30 days

**Non-Conformance Handling**:
- Minor non-conformances: Infrastructure Manager creates corrective action plan, approved by CISO, completed within 90 days
- Major non-conformances: CIO and CISO create corrective action plan, approved by Executive Management, completed within 30 days

**Compliance Metrics** (reported monthly):
- Monitoring coverage percentage (target: 100% production, 90% non-production)
- Threshold configuration completeness
- Forecasting coverage for critical resources
- Reporting timeliness
- Non-conformance count and closure rate

**Capacity Management Program KPIs** (reported quarterly):

| KPI Category | Metric | Target |
|-------------|--------|--------|
| **Availability** | Capacity-related incidents per quarter | <2 |
| **Availability** | Mean time to capacity expansion | <30 days from approval |
| **Availability** | Emergency capacity procurements per year | <3 |
| **Accuracy** | Forecast accuracy | ±15% |
| **Accuracy** | False positive alert rate | <10% |
| **Accuracy** | Monitoring data completeness | >99% |
| **Efficiency** | Average headroom across systems | 15-30% |
| **Efficiency** | Average utilization at peak | 70-85% |
| **Efficiency** | Budget variance (actual vs. planned) | ±10% |

KPIs SHALL be reported quarterly to IT Leadership Team and annually to Executive Management

## Non-Compliance Consequences

**Operational**: Service outages, performance degradation, emergency procurement
**Financial**: Unbudgeted spending, lost revenue, contract penalties
**Compliance**: ISO 27001 non-conformance, regulatory violations, audit findings
**Organizational**: Performance management actions, executive escalation

## Policy Review and Updates

**Review Triggers**:

- Annual scheduled review
- Major infrastructure changes or cloud migrations
- Regulatory changes affecting capacity requirements
- Major capacity-related incidents

**Update Approval**:

- Minor updates (clarifications): Information Security Manager
- Major updates (requirement changes): CISO and IT Director
- Strategic changes: Executive Management

---

# Related Documents

## ISMS Documents

**Implementation Guidance**:

- ISMS-IMP-A.8.6.1: Capacity Monitoring Implementation
- ISMS-IMP-A.8.6.2: Capacity Forecasting and Planning
- ISMS-IMP-A.8.6.3: Capacity Management Assessment

**Related Policies**:

- ISMS-POL-00: Regulatory Applicability Framework
- ISMS-POL-A.8.16: Monitoring Activities
- ISMS-POL-A.8.14: Redundancy of Information Processing Facilities
- ISMS-POL-A.8.13: Information Backup
- ISMS-POL-A.7.11: Supporting Utilities
- ISMS-POL-A.5.30: ICT Readiness for Business Continuity

## External Standards

**Regulatory References** (per ISMS-POL-00):

- ISO/IEC 27001:2022 - Control A.8.6
- ISO/IEC 27002:2022 - Control 8.6 guidance
- FINMA Circular 2023/1 (if applicable)
- DORA - Regulation (EU) 2022/2554 (if applicable)
- NIS2 - Directive (EU) 2022/2555 (if applicable)

---

# Definitions

| Term | Definition |
|------|------------|
| **Capacity Management** | Process of ensuring adequate resources to meet current and future performance and availability requirements |
| **Capacity Monitoring** | Continuous measurement of resource utilization to understand consumption and track trends |
| **Capacity Planning** | Proactive process of determining future capacity requirements and developing expansion plans |
| **Capacity Threshold** | Defined utilization level that triggers alerts or actions when exceeded |
| **Capacity Forecast** | Projection of future capacity requirements based on trends and business plans |
| **Headroom** | Remaining unused capacity available for growth or unexpected demand |

---

# Approval Record

| Role | Name | Date |
|------|------|------|
| **Chief Information Security Officer (CISO)** | [Name] | [Date to be set] |
| **Chief Information Officer (CIO)** | [Name] | [Date to be set] |
| **Chief Financial Officer (CFO)** | [Name] | [Date to be set] |
| **IT Operations Manager** | [Name] | [Date to be set] |

---

**END OF POLICY DOCUMENT**

---

*This policy establishes capacity management requirements. Implementation procedures are documented in ISMS-IMP-A.8.6 (UG/TG).1 (Capacity Monitoring Implementation), ISMS-IMP-A.8.6.2 (Capacity Forecasting and Planning), and ISMS-IMP-A.8.6.3 (Capacity Management Assessment).*

<!-- QA_VERIFIED: 2026-02-02 -->
