**ISMS-POL-A.7.4-5-11 — Physical Infrastructure Security**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Physical Infrastructure Security Policy |
| **Document Type** | Policy |
| **Document ID** | ISMS-POL-A.7.4-5-11 |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date to be set] |
| **Version** | 1.0 |
| **Version Date** | [Date to be set] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date to be set] | CISO | Initial consolidated policy for ISO 27001:2022 certification |

**Review Cycle**: Annual (or upon significant facility changes, security incidents, or regulatory updates)
**Next Review Date**: [Effective Date + 12 months]

**Approval Chain**:

- Primary: Chief Information Security Officer (CISO)
- Secondary: Facilities Manager
- Final Authority: Executive Management (GL)

**Related Documents**:

- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-POL-A.7.1-2-3 (Physical Access Control)
- ISMS-POL-A.5.19-23 (Cloud Services)
- ISMS-POL-A.5.24-28 (Incident Management)
- ISMS-POL-A.5.30-8.13-14 (Business Continuity)
- ISMS-IMP-A.7.4-5-11 (Implementation Guidance)
- ISO/IEC 27001:2022 Controls A.7.4, A.7.5, A.7.11

---

# Executive Summary

This policy establishes [Organisation]'s requirements for physical infrastructure security controls to protect information assets through comprehensive monitoring, environmental protection, and utility resilience in accordance with ISO/IEC 27001:2022 Controls A.7.4, A.7.5, and A.7.11.

**Purpose**: Define organisational requirements for physical infrastructure security governance. This policy establishes WHAT physical security protection is required and WHO is accountable. Implementation procedures (HOW) are documented in ISMS-IMP-A.7.4-5-11.

**Combined Control Approach**: These three controls are implemented as a unified Physical Infrastructure Security Framework because they operate on the same physical infrastructure, create interdependencies, and share common assessment processes. Each control maintains distinct requirements for Statement of Applicability (SoA) purposes.

---

# Scope

## In Scope

**Facilities**:

- On-premises datacenters and disaster recovery sites
- Server rooms and telecommunications closets
- Corporate offices (headquarters, regional, branch)
- Colocation facilities (with shared responsibility model)
- Remote and temporary facilities where organization-owned equipment is located

**Personnel**:

- Facilities Management, Security Operations, IT Operations
- All employees accessing physical facilities
- Contractors, vendors, and visitors

## Cloud-Only Organisations

Organisations operating 100% in cloud environments with no on-premises information processing facilities may mark Controls A.7.4, A.7.5, and A.7.11 as "Not Applicable" in the Statement of Applicability.

**Applicability Decision Requirements**: The "Not Applicable" determination SHALL be documented in the Statement of Applicability with justification including:
- Asset inventory reference confirming no on-premises facilities (ISMS-IMP-A.5.9)
- Cloud provider physical security verification through SOC 2 Type II review (ISMS-IMP-A.5.19-23)
- Annual review confirmation that cloud-only status remains accurate

Cloud provider physical security SHALL be assessed through supplier management (Control A.5.19-23).

## Colocation Facilities

When utilising colocation datacenter space, physical infrastructure responsibilities are shared between the colocation provider and [Organisation]. A formal responsibility matrix SHALL be documented in the colocation contract and maintained in the Supplier Management Register (ISMS-POL-A.5.19-23) for centralised tracking. Provider controls SHALL be verified annually through audit reports (SOC 2 Type II or ISO 27001 certification), with review documented in supplier assessment records.

## Out of Scope

- Physical security of portable devices (covered under A.7.7, A.8.1)
- Equipment transport security (covered under A.7.13)
- Offsite backup media storage (covered under A.8.13)
- Personnel security and background checks (covered under A.6.1-6.4)

---

# Policy Statements

## Physical Security Monitoring (A.7.4)

> *Premises should be continuously monitored for unauthorised physical access.*

**Control Objective**: Detect and respond to unauthorised physical access attempts through comprehensive monitoring.

[Organisation] SHALL:

1. **Access Control**: Implement electronic access control at all facility entry/exit points with authentication, logging, and integration with identity management
2. **Intrusion Detection**: Deploy intrusion detection systems appropriate to facility criticality and risk assessment
3. **Video Surveillance**: Provide CCTV coverage for facility entrances, restricted areas, and critical infrastructure
4. **Visitor Management**: Require all visitors to register, receive temporary identification, and be escorted in restricted areas
5. **Access Review**: Conduct periodic access reviews to identify and revoke stale or unauthorised access rights
6. **Security Integration**: Integrate physical security events with SIEM (ISMS-POL-A.8.16) for correlation with logical security events and incident response

**Evidence of Compliance**: Physical security monitoring compliance is demonstrated through ISMS-IMP-A.7.4-5-11-S1 (Physical Monitoring Assessment), which generates monthly workbooks containing:
- Electronic access control logs with authentication success/failure rates
- CCTV system uptime and coverage verification
- Intrusion detection system alerts and response times
- Visitor management records with escort compliance
- Access review results with revocation actions

## Environmental Protection (A.7.5)

> *Protection against physical and environmental threats should be designed and implemented.*

**Control Objective**: Protect information processing facilities from physical and environmental threats including fire, flood, and climate conditions.

[Organisation] SHALL:

1. **Threat Assessment**: Conduct environmental threat risk assessment considering geographic location and facility characteristics
2. **Fire Protection**: Implement fire detection and suppression systems appropriate to facility type and regulatory requirements
3. **Water Protection**: Install water detection systems and implement flood mitigation measures based on risk assessment
4. **Climate Control**: Maintain temperature and humidity within acceptable ranges for information processing equipment
5. **Structural Protection**: Ensure building integrity and implement physical barriers appropriate to identified threats
6. **Emergency Response**: Document and test emergency response procedures for environmental incidents

**Evidence of Compliance**: Environmental protection compliance is demonstrated through ISMS-IMP-A.7.4-5-11-S2 (Environmental Protection Assessment), which generates quarterly workbooks containing:
- Fire system test results and inspection certificates
- Water detection system logs and maintenance records
- Temperature/humidity monitoring data with threshold compliance
- Environmental threat assessment reviews (annual)
- Emergency response drill records and findings

## Utility Resilience (A.7.11)

> *Information processing facilities should be protected from power failures and other disruptions caused by failures in supporting utilities.*

**Control Objective**: Ensure continuity of information processing through resilient utility infrastructure including power, cooling, and telecommunications.

[Organisation] SHALL:

1. **Power Protection**: Implement uninterruptible power supply (UPS) systems with capacity appropriate to facility criticality
2. **Backup Power**: Provide backup generation capability for critical facilities to ensure continued operation during extended outages
3. **Cooling Resilience**: Implement cooling systems with redundancy appropriate to facility criticality
4. **Telecommunications**: Ensure telecommunications connectivity with redundancy appropriate to facility criticality
5. **Utility Monitoring**: Monitor utility systems in real-time with alerting for failures or threshold excursions
6. **Failure Testing**: Conduct regular testing of utility resilience systems per schedule:
   - UPS failover testing: Quarterly
   - Backup generator load test: Semi-annually
   - Cooling redundancy verification: Quarterly
   - Telecommunications failover: Annually

**Evidence of Compliance**: Utility resilience compliance is demonstrated through ISMS-IMP-A.7.4-5-11-S3 (Utility Resilience Assessment), which generates quarterly workbooks containing:
- UPS test logs with failover success/failure results
- Generator load test reports with fuel consumption verification
- Cooling system redundancy verification records
- Telecommunications failover test results
- Utility monitoring alert history and response times

## Facility Criticality Tiers

Facilities SHALL be classified into criticality tiers based on Business Impact Analysis:

| Tier | Definition | Monitoring | Environmental | Utility | Review Frequency |
|------|------------|------------|---------------|---------|------------------|
| **Tier 1 - Critical** | Datacenters, primary server rooms, DR sites | 24/7 SOC monitoring, <15min response SLA, intrusion detection required | Fire suppression + detection, water detection all zones, temperature 18-27°C ±2°C | N+1 UPS (dual units, 30min runtime each), backup generator (48hr fuel), dual cooling paths | Monthly manual verification |
| **Tier 2 - Standard** | Corporate offices, branch offices, non-critical server rooms | 8/5 monitoring, next-business-day response, intrusion detection optional | Fire detection (suppression if equipment value >CHF 500k), water detection high-risk areas only, temperature 18-27°C ±5°C | Single UPS (15min runtime minimum), no generator required, single cooling | Quarterly manual verification |

**Tier Classification Criteria**: Facilities SHALL be classified based on Business Impact Analysis (ISMS-POL-A.5.30-8.13-14) considering:
- System criticality: Tier 1/2 applications hosted
- Data classification: CONFIDENTIAL data processing = Tier 1
- Recovery time objectives: RTO <4hrs = Tier 1, RTO >4hrs = Tier 2

---

# Roles and Responsibilities

| Role | Responsibilities |
|------|------------------|
| **Chief Information Security Officer (CISO)** | Overall accountability for physical infrastructure security framework; policy approval; budget allocation; executive reporting |
| **Facilities Manager** | Day-to-day physical infrastructure operations; environmental and utility system maintenance; vendor management |
| **Security Operations Manager** | Physical security monitoring implementation; access control management; CCTV operations; incident response coordination |
| **System Owners** | Physical security requirements for owned systems; equipment placement coordination; incident participation |
| **IT Operations** | Physical-logical security integration (SIEM); network infrastructure for security systems; monitoring dashboards |
| **Internal Audit** | Annual physical security compliance audit; control testing; evidence review |
| **Risk Management** | Physical security risk assessment; environmental threat assessment; risk register maintenance |
| **Compliance Officer** | Regulatory compliance tracking; evidence collection; regulatory liaison |

---

# Governance and Compliance

## Assessment Framework

[Organisation] SHALL conduct regular assessments per ISMS-IMP-A.7.4-5-11 methodology:

- **Continuous**: Real-time monitoring and alerting
- **Monthly**: Automated data collection from physical security systems
- **Quarterly**: Manual verification and testing compliance review
- **Annual**: Comprehensive audit with external verification

## Compliance Scoring

| Score Range | Rating | Action Required |
|-------------|--------|-----------------|
| >90% | Excellent | Maintain current controls |
| 75-89% | Good | Address gaps in next review cycle |
| 60-74% | Acceptable | Develop remediation plan within 30 days |
| <60% | Non-Compliant | Immediate remediation required, CISO escalation |

**Scoring Methodology**: Compliance score is calculated by ISMS-IMP-A.7.4-5-11-S4 (Facilities Compliance Dashboard) using weighted metrics:

| Metric | Weight | Measurement Source |
|--------|--------|-------------------|
| Access control system availability | 20% | Access control system logs |
| Environmental parameter compliance (temp/humidity within thresholds) | 20% | Environmental monitoring system |
| Utility resilience test success rate | 15% | Test records (S3 workbook) |
| Fire/water detection system operational status | 15% | Inspection records |
| Security incident response time adherence | 15% | Incident management system |
| Visitor management compliance | 10% | Visitor logs |
| Physical security training completion | 5% | LMS records |

Detailed calculation methodology and metric definitions are documented in ISMS-IMP-A.7.4-5-11-S4.

## Exception Management

Physical infrastructure security requirements may be waived through formal exception process:

- **Valid Scenarios**: Technical infeasibility, disproportionate cost, temporary variance during transitions
- **Approval Authority**: Security Operations Manager (low risk), CISO (medium risk), Executive Management (high risk)
- **Requirements**: Documented justification, risk assessment, compensating controls, defined duration (maximum 6 months)
- **Review**: Re-evaluate upon expiration, facility changes, or incident occurrence

## Gap Remediation

Physical infrastructure control deficiencies identified through assessments (Assessment Framework) SHALL be managed as follows:

**1. Documentation**: Deficiencies SHALL be recorded in the Physical Security Gap Register (maintained by Security Operations Manager in ISMS-IMP-A.7.4-5-11-S4 Compliance Dashboard) with:
- Gap description and affected control(s) (A.7.4, A.7.5, A.7.11)
- Risk severity (Critical/High/Medium/Low per Incident Classification)
- Assigned owner and target closure date
- Compensating controls (if applicable)
- Status (Open/In Progress/Closed)

**2. Tracking**: Gap Register SHALL be reviewed:
- Monthly: Security Operations Manager review with owner follow-up
- Quarterly: CISO review with executive escalation for overdue Critical/High gaps
- Annually: Internal Audit verification of closure evidence

**3. Closure**: Gaps may be closed only after:
- Remediation implemented and verified
- Evidence documented (e.g., system installation receipt, test results)
- Sign-off by Security Operations Manager (Low/Medium) or CISO (High/Critical)

**4. Escalation**: Gaps open beyond target date SHALL be escalated per ISMS-POL-A.5.24-28 (Incident Management).

## Incident Classification

| Severity | Examples | Response |
|----------|----------|----------|
| **Critical** | Unauthorised access to restricted areas; physical breach; theft; major environmental event | Immediate response per ISMS-POL-A.5.24-28 |
| **High** | Repeated failed access attempts; tailgating; lost badges; environmental alerts | Same-day investigation and response |
| **Medium** | Door held open; frequent false alarms; minor environmental excursions | Documented and investigated |
| **Low** | Single failed access; minor policy violations | Logged for trend analysis |

## Policy Review

- **Frequency**: Annual or upon significant trigger event
- **Trigger Events**: Facility changes, security incidents, regulatory updates, technology changes
- **Participants**: CISO, Facilities Manager, Security Operations Manager, Compliance Officer
- **Approval**: CISO (minor changes), Executive Management (material changes)

---

# Regulatory Applicability

## Mandatory Compliance (Tier 1)

| Regulation | Key Requirements |
|------------|------------------|
| **Swiss nDSG** | Art. 8 - Technical and organisational measures for physical security |
| **EU GDPR** | Art. 32 - Security of processing including physical measures |
| **ISO/IEC 27001:2022** | Controls A.7.4, A.7.5, A.7.11 - Documented policy and implementation |

## Conditional Compliance (Tier 2)

| Regulation | Trigger Condition |
|------------|-------------------|
| **FINMA Circular 2023/1** | Swiss regulated financial institution |
| **DORA (EU) 2022/2554** | EU financial services entity |
| **NIS2 Directive (EU) 2022/2555** | Essential/important entity in EU |

Refer to ISMS-POL-00 (Regulatory Applicability Framework) for complete regulatory categorization.

---

# Related Documents

## Internal ISMS References

| Document | Relationship |
|----------|--------------|
| ISMS-POL-00 | Regulatory Applicability Framework |
| ISMS-POL-A.7.1-3 | Physical Access Control (prerequisite) |
| ISMS-POL-A.5.19-23 | Cloud Services (cloud provider assessment) |
| ISMS-POL-A.5.24-28 | Incident Management (incident response) |
| ISMS-POL-A.5.30-8.13-14 | Business Continuity (BC/DR integration) |

## Implementation Guidance

| Document | Purpose |
|----------|---------|
| ISMS-IMP-A.7.4-5-11-S1 | Physical Monitoring Assessment |
| ISMS-IMP-A.7.4-5-11-S2 | Environmental Protection Assessment |
| ISMS-IMP-A.7.4-5-11-S3 | Utility Resilience Assessment |
| ISMS-IMP-A.7.4-5-11-S4 | Facilities Compliance Dashboard |

## External Standards

- ISO/IEC 27001:2022 - Information Security Management Systems
- ISO/IEC 27002:2022 - Information Security Controls
- NIST SP 800-53 Rev 5 - Physical and Environmental Protection (PE)
- Uptime Institute Tier Standards - Datacenter Classification
- TIA-942 - Telecommunications Infrastructure Standard for Data Centers

---

# ISMS Integration

## Statement of Applicability

| Control | Status | Implementation Reference |
|---------|--------|-------------------------|
| **A.7.4 - Physical Security Monitoring** | Applicable | This policy, ISMS-IMP-A.7.4-5-11-S1 |
| **A.7.5 - Protecting Against Physical and Environmental Threats** | Applicable | This policy, ISMS-IMP-A.7.4-5-11-S2 |
| **A.7.11 - Supporting Utilities** | Applicable | This policy, ISMS-IMP-A.7.4-5-11-S3 |

## Related Controls

| Control | Relationship |
|---------|--------------|
| **A.7.1-2-3** | Physical access control (prerequisite for monitoring) |
| **A.7.8-9** | Equipment siting and off-premises security |
| **A.5.19-23** | Cloud provider physical security assessment |
| **A.5.24-28** | Incident management for physical security events |
| **A.5.30-8.13-14** | Business continuity integration |
| **A.8.16** | SIEM integration for physical-logical correlation |

---

# Definitions

| Term | Definition |
|------|------------|
| **Physical Security Monitoring** | Continuous surveillance and detection of physical access attempts and environmental conditions |
| **Environmental Threat** | Natural or man-made hazards that can damage facilities (fire, flood, temperature extremes, seismic events) |
| **Supporting Utilities** | Infrastructure services required for facility operation (power, cooling, telecommunications) |
| **Facility Criticality Tier** | Classification of facilities based on business impact and required protection level |
| **N+1 Redundancy** | Configuration where one additional unit is available beyond minimum requirements |
| **Gap Register** | Documented list of control deficiencies with remediation tracking |
| **SOC 2 Type II** | Service Organisation Control audit report demonstrating control effectiveness over time |

---

# Evidence for This Policy

**Stage 1 (Documentation Review) Evidence:**

- ✅ This policy document (ISMS-POL-A.7.4-5-11 v1.0)
- ✅ Approval signatures from CISO, Facilities Manager, Executive Management
- ✅ Physical security monitoring requirements documented (Section: Policy Statements)
- ✅ Environmental protection requirements documented (Section: Policy Statements)
- ✅ Utility resilience requirements documented (Section: Policy Statements)
- ✅ Facility criticality tiers defined (Section: Facility Criticality Tiers)
- ✅ Roles and responsibilities assigned (Section: Roles and Responsibilities)
- ✅ Compliance scoring methodology documented (Section: Governance and Compliance)
- ✅ Gap remediation process documented (Section: Gap Remediation)

**Stage 2 (Operational Effectiveness) Evidence:**

**Evidence Repository and Generation**:

| Evidence Type | Repository Location | Generation Method | Owner | Retention |
|---------------|-------------------|-------------------|-------|-----------|
| Physical Monitoring Workbook | [GRC Platform] - Physical Security Module | Monthly automated collection via ISMS-IMP-A.7.4-5-11-S1 | Security Operations Manager | 3 years |
| Environmental Protection Assessment | [GRC Platform] - Physical Security Module | Quarterly assessment via ISMS-IMP-A.7.4-5-11-S2 | Facilities Manager | 3 years |
| Utility Resilience Assessment | [GRC Platform] - Physical Security Module | Quarterly testing via ISMS-IMP-A.7.4-5-11-S3 | Facilities Manager | 3 years |
| Facilities Compliance Dashboard | [GRC Platform] - Compliance Module | Monthly automated calculation via ISMS-IMP-A.7.4-5-11-S4 | Security Operations Manager | 3 years |
| Physical Security Gap Register | [GRC Platform] - Risk Register | Continuous tracking, monthly review | Security Operations Manager | Active + 2 years |
| Access Control Logs | [Physical Access System] | Automated logging | Security Operations | 12 months |
| CCTV Recordings | [Video Management System] | Continuous recording | Security Operations | 30-90 days per policy |
| Environmental Monitoring Data | [BMS/Environmental Monitoring System] | Continuous sensor data | Facilities Manager | 12 months |
| Utility Test Records | [CMMS/Maintenance System] | Per testing schedule | Facilities Manager | 5 years |
| Exception Records | [GRC Platform] - Exception Register | Per exception request | CISO | Active + 2 years |

**Evidence Accessibility**: All evidence SHALL be accessible to auditors upon request within 2 business days.

---

# Approval Record

| Role | Name | Date |
|------|------|------|
| **Chief Information Security Officer (CISO)** | [Name] | [Date to be set] |
| **Facilities Manager** | [Name] | [Date to be set] |
| **Executive Management (GL)** | [Name] | [Date to be set] |

---

**END OF POLICY DOCUMENT**

---

*This policy establishes [Organisation]'s requirements for physical infrastructure security. Implementation procedures are documented in ISMS-IMP-A.7.4-5-11.*

<!-- QA_VERIFIED: [Date] -->
