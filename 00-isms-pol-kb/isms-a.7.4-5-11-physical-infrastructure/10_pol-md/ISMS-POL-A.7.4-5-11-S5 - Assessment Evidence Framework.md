# ISMS-POL-A.7.4-5-11-S5: Assessment Methodology and Evidence Framework

**Document Classification:** Internal - ISMS Policy  
**Version:** 1.0  
**Effective Date:** [To be defined]  
**Review Cycle:** Annual  
**Policy Owner:** CISO / Internal Audit  
**Approved By:** [Approval Authority]

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO / Internal Audit / Facilities Manager | Initial policy for physical infrastructure assessment and evidence collection |

**Review Schedule:** Annual review or upon significant changes to assessment methodology or evidence requirements  
**Next Review Date:** [Approval Date + 12 months]  
**Distribution:** CISO, Internal Audit, Facilities Management, Security Operations, Compliance Officer, Auditors

---

## Table of Contents

1. [Assessment Framework Overview](#1-assessment-framework-overview)
2. [Physical Access Monitoring Assessment (A.7.4)](#2-physical-access-monitoring-assessment-a74)
3. [Environmental Protection Assessment (A.7.5)](#3-environmental-protection-assessment-a75)
4. [Utility Resilience Assessment (A.7.11)](#4-utility-resilience-assessment-a711)
5. [Unified Physical Infrastructure Dashboard](#5-unified-physical-infrastructure-dashboard)
6. [Evidence Collection Framework](#6-evidence-collection-framework)
7. [Compliance Scoring Methodology](#7-compliance-scoring-methodology)
8. [Related Documents](#8-related-documents)

---

## 1. Assessment Framework Overview

### 1.1 Purpose and Scope

This assessment framework provides systematic methodology for evaluating [Organization's] compliance with ISO 27001:2022 physical infrastructure security controls (A.7.4, A.7.5, A.7.11).

**Assessment Objectives:**
- Measure compliance with policy requirements (POL-S2, POL-S3, POL-S4)
- Identify gaps and non-compliance (risk assessment)
- Generate audit-ready evidence (internal and external audits)
- Track compliance trends (month-over-month improvement)
- Prioritize remediation efforts (risk-based prioritization)

**Assessment Scope:**
- All facilities where [Organization] operates (datacenters, offices, colocation, as applicable)
- All three controls assessed in unified framework (A.7.4, A.7.5, A.7.11)
- Both technical controls (UPS, HVAC, sensors) and procedural controls (testing, maintenance, incident response)

### 1.2 Assessment Frequency

**Automated Assessments:**
- **Frequency:** Monthly (first week of each month)
- **Scope:** Access log analysis, temperature excursion count, UPS battery health, utility uptime
- **Method:** Automated data collection from monitoring systems (access control, environmental monitoring, UPS/generator monitoring, network monitoring)
- **Output:** Monthly compliance metrics dashboard

**Manual Assessments:**
- **Frequency:** Quarterly (end of quarter: March 31, June 30, September 30, December 31)
- **Scope:** Comprehensive assessment of all requirements (coverage, testing compliance, operational metrics)
- **Method:** Manual data collection (physical inspection, test record review, interview personnel)
- **Output:** Quarterly comprehensive assessment report

**Triggered Assessments:**
- **Trigger Conditions:**
  - Major incident (power outage >1 hour, HVAC failure causing shutdown, physical security breach)
  - Facility changes (new datacenter, major equipment addition, facility relocation)
  - Audit preparation (internal audit, external audit, regulatory audit)
- **Scope:** Focused assessment of affected area or control
- **Output:** Incident-specific or change-specific assessment report

**Annual Comprehensive Assessment:**
- **Frequency:** Annual (Q4 - October/November, before year-end)
- **Scope:** All facilities, all controls, all requirements (comprehensive audit-readiness assessment)
- **Method:** Combination of automated data collection and manual assessment
- **Output:** Annual compliance report (executive summary, detailed findings, remediation plan)

### 1.3 Assessment Tools

**Assessment Workbooks (Excel):**
- **ISMS_Assessment_Access_Monitoring.xlsx:** Physical access monitoring assessment (A.7.4)
- **ISMS_Assessment_Environmental_Protection.xlsx:** Environmental protection assessment (A.7.5)
- **ISMS_Assessment_Utility_Resilience.xlsx:** Utility resilience assessment (A.7.11)
- **ISMS_Dashboard_Physical_Infrastructure.xlsx:** Unified compliance dashboard (all three controls)

**Supporting Tools:**
- Access control system (export access logs)
- CCTV system (verify coverage, retention)
- Environmental monitoring system (export temperature/humidity data)
- UPS monitoring system (battery health, runtime data)
- Generator test logs (monthly/quarterly/annual tests)
- Network monitoring system (ISP uptime, failover tests)

**Assessment Tool Features:**
- **Data Entry:** 100 rows per worksheet (scalable for large deployments)
- **Example Data:** 10 example rows (guidance for assessors)
- **Formulas:** Automated compliance score calculation
- **Conditional Formatting:** Visual indicators (✅ compliant, ❌ non-compliant, ⚠️ warning)
- **Evidence Register:** Document evidence sources (who, what, where, when)
- **Approval Workflow:** Assessor → ISO → CISO sign-off

---

## 2. Physical Access Monitoring Assessment (A.7.4)

### 2.1 Assessment Scope

**Requirements Assessed (per POL-S2):**
- Access control system coverage (badge readers at all entry/exit points)
- Access log retention (365 days critical, 90 days standard)
- CCTV coverage (all entrances, server rooms, parking)
- CCTV retention (90 days critical, 30 days standard)
- Intrusion detection coverage (100% sensitive areas critical, entry points + sensitive standard)
- Visitor management compliance (sign-in, escort, badge return)
- Physical security incident count (target <2 per year excluding false alarms)
- Testing compliance (access control quarterly, CCTV monthly, intrusion detection monthly)

### 2.2 Data Sources

**Access Control System:**
- Access logs (export 30-day sample from past 12 months)
- User count (total authorized users, active users)
- Failed access attempts (count per month)
- Access control system configuration (door list, user groups, access levels)

**CCTV System:**
- Camera inventory (camera count, locations, coverage map)
- Recording retention verification (oldest footage date)
- Camera health status (online/offline cameras)
- CCTV test logs (monthly recording verification tests)

**Intrusion Detection System:**
- Sensor inventory (sensor count by type: motion, door/window, glass break)
- Sensor coverage map (floor plans with sensor placement)
- Alarm event logs (past 12 months)
- False alarm count (per month)
- Intrusion detection test logs (monthly sensor tests)

**Visitor Management:**
- Visitor logs (sample 30 days)
- Visitor badge inventory (total issued, total returned, missing badges)

**Physical Security Incidents:**
- Incident reports (past 12 months)
- Incident type distribution (unauthorized access, tailgating, lost badge, other)
- Response time data (alarm to resolution)

### 2.3 Assessment Workbook

**Tool:** ISMS_Assessment_Access_Monitoring.xlsx (generated by Script 1)

**Worksheets:**
1. **Cover Sheet:** Facility information, assessment date, assessor
2. **Access Log Analysis:** Access entries per day, failed attempts, after-hours access
3. **CCTV Coverage:** Camera inventory, coverage percentage, retention compliance
4. **Intrusion Detection:** Sensor inventory, coverage percentage, alarm events, false alarms
5. **Visitor Management:** Visitor count, badge return rate, policy compliance
6. **Physical Security Incidents:** Incident count, severity, response time
7. **Evidence Register:** Documentation of evidence sources
8. **Approval Sign-Off:** Assessor → ISO → CISO

**Compliance Metrics Calculated:**
- Access control coverage: % of entry points with badge readers (target 100%)
- CCTV coverage: % of required areas with cameras (target 100%)
- Intrusion detection coverage: % of sensitive areas with sensors (target 100%)
- Access log retention: Days retained (target 365 critical, 90 standard)
- Failed access attempts: Count per month (target <5 legitimate failures)
- Incident count: Count per year (target <2 excluding false alarms)
- Testing compliance: % of required tests completed (target 100%)

**Overall A.7.4 Score:** Weighted average of compliance metrics (0-100%)

### 2.4 Assessment Frequency

- **Automated (Monthly):** Access log analysis (failed attempts, after-hours access)
- **Manual (Quarterly):** Comprehensive assessment (coverage, CCTV retention, testing compliance)
- **Triggered:** After physical security incidents

---

## 3. Environmental Protection Assessment (A.7.5)

### 3.1 Assessment Scope

**Requirements Assessed (per POL-S3):**
- Environmental threat risk assessment (completed annually)
- Fire detection coverage (100% of facility area)
- Fire suppression coverage (100% of facility area)
- Water detection coverage (100% of at-risk areas)
- Temperature monitoring coverage (100% of server rooms)
- Temperature excursions (target <5 per month)
- Environmental incidents (target 0 major incidents per year)
- Testing compliance (fire alarm semi-annual, smoke detectors semi-annual, water sensors monthly, temperature sensors monthly)
- Fire drill compliance (annual critical, biennial standard)

### 3.2 Data Sources

**Environmental Risk Assessment:**
- Risk assessment report (annual, current year)
- Risk register (all identified risks, mitigation strategies)

**Fire Detection System:**
- Smoke detector inventory (count, locations, coverage map)
- Fire alarm panel configuration
- Fire alarm test logs (semi-annual detector tests, annual system tests, past 12 months)

**Fire Suppression System:**
- Sprinkler system documentation (type, coverage map)
- Gas suppression system documentation (if applicable - type, agent, nozzle placement)
- Sprinkler inspection reports (annual professional inspection)
- Fire extinguisher inventory and inspection logs (monthly visual, annual professional)

**Water Detection System:**
- Water sensor inventory (count, locations, coverage map)
- Water sensor test logs (monthly tests, past 12 months)
- Water detection alerts (past 12 months)

**Temperature/Humidity Monitoring:**
- Sensor inventory (count, locations)
- Historical monitoring data (12 months of temperature/humidity readings)
- Temperature excursion count (monthly, past 12 months)
- Alert logs (threshold breaches)

**Environmental Incidents:**
- Incident reports (fire, flood, temperature, past 12 months)
- Incident severity (minor, moderate, major)
- Response time and resolution

**Fire Drills:**
- Fire drill reports (past 24 months for standard facilities, past 12 months for critical)
- Drill attendance, duration, issues identified

### 3.3 Assessment Workbook

**Tool:** ISMS_Assessment_Environmental_Protection.xlsx (generated by Script 2)

**Worksheets:**
1. **Cover Sheet:** Facility information, assessment date, assessor
2. **Fire Detection Status:** Detector inventory, coverage percentage, test compliance
3. **Fire Suppression Status:** Suppression system inventory, coverage percentage, inspection compliance
4. **Water Detection Coverage:** Sensor inventory, at-risk area coverage percentage, test compliance
5. **Temperature/Humidity Monitoring:** Sensor inventory, coverage percentage, excursion count
6. **Environmental Threat Incidents:** Incident count by type, severity, resolution
7. **Evidence Register:** Documentation of evidence sources
8. **Approval Sign-Off:** Assessor → ISO → CISO

**Compliance Metrics Calculated:**
- Fire detection coverage: % of facility area (target 100%)
- Fire suppression coverage: % of facility area (target 100%)
- Water detection coverage: % of at-risk areas (target 100%)
- Temperature monitoring coverage: % of server rooms (target 100%)
- Temperature excursions: Count per month (target <5)
- Environmental incidents: Count per year (target 0 major incidents)
- Testing compliance: % of required tests completed (target 100%)
- Fire drill compliance: Drills completed per year (target 1 annual or 0.5 biennial)

**Overall A.7.5 Score:** Weighted average of compliance metrics (0-100%)

### 3.4 Assessment Frequency

- **Automated (Monthly):** Temperature excursion count, water detection alerts
- **Manual (Quarterly):** Comprehensive assessment (coverage, testing compliance, incident review)
- **Triggered:** After environmental incidents (fire, flood, temperature excursion causing damage)

---

## 4. Utility Resilience Assessment (A.7.11)

### 4.1 Assessment Scope

**Requirements Assessed (per POL-S4):**
- Power uptime (99.99% critical, 99.9% standard)
- UPS runtime (15 min critical, 5 min standard)
- UPS battery health (target >80%)
- Generator availability (99% critical facilities with generators)
- HVAC uptime (99.9% critical, 99% standard)
- Temperature excursions (target <5 per month - duplicate with A.7.5 assessment)
- ISP uptime (meets SLA, typically 99.9%)
- Failover success rate (100% for dual ISP)
- Testing compliance (UPS monthly/quarterly, generator monthly/quarterly/annual, ISP failover quarterly)

### 4.2 Data Sources

**Power Infrastructure:**
- UPS specifications (capacity kVA/kW, runtime, battery type, redundancy)
- UPS monitoring data (battery health, uptime, past 12 months)
- UPS test logs (monthly self-tests, quarterly load tests, past 12 months)
- Generator specifications (capacity kW, fuel type, runtime)
- Generator test logs (monthly no-load, quarterly 50% load, annual 100% load, past 12 months)
- Generator fuel logs (fuel deliveries, fuel level monitoring)
- Power outage incident reports (past 12 months)

**HVAC Infrastructure:**
- HVAC specifications (capacity tons/BTU, redundancy)
- HVAC monitoring data (temperature, humidity, unit status, past 12 months)
- HVAC maintenance logs (filter replacement, coil cleaning, inspections)
- HVAC failure incidents (past 12 months)

**Telecommunications Infrastructure:**
- ISP contracts (bandwidth, SLA, MTTR)
- ISP SLA reports (monthly uptime reports, past 12 months)
- Network monitoring data (uptime, latency, packet loss, past 12 months)
- ISP failover test reports (quarterly, past 12 months)
- ISP outage incidents (past 12 months)

**Utility Failure Events:**
- Power failure events (count, duration, cause, past 12 months)
- HVAC failure events (count, duration, cause, past 12 months)
- ISP outage events (count, duration, cause, past 12 months)

### 4.3 Assessment Workbook

**Tool:** ISMS_Assessment_Utility_Resilience.xlsx (generated by Script 3)

**Worksheets:**
1. **Cover Sheet:** Facility information, assessment date, assessor
2. **Power Infrastructure:** UPS inventory, capacity, runtime, battery health, generator status
3. **HVAC Infrastructure:** HVAC inventory, capacity, redundancy, uptime
4. **Telecommunications Infrastructure:** ISP inventory, bandwidth, SLA compliance, failover testing
5. **Utility Failure Events:** Failure count by type (power, HVAC, ISP), duration, impact
6. **Utility Monitoring Coverage:** Monitoring system coverage percentage
7. **Evidence Register:** Documentation of evidence sources
8. **Approval Sign-Off:** Assessor → ISO → CISO

**Compliance Metrics Calculated:**
- Power uptime: % (target 99.99% critical, 99.9% standard)
- UPS runtime: Minutes at full load (target 15 critical, 5 standard)
- UPS battery health: % of original capacity (target >80%)
- Generator test compliance: % of required tests completed (target 100%)
- HVAC uptime: % (target 99.9% critical, 99% standard)
- ISP uptime: % vs. SLA (target meets SLA)
- ISP failover success rate: % (target 100%)
- Testing compliance: % of required tests completed (target 100%)

**Overall A.7.11 Score:** Weighted average of compliance metrics (0-100%)

### 4.4 Assessment Frequency

- **Automated (Monthly):** Power uptime, HVAC uptime, ISP uptime, UPS battery health
- **Manual (Quarterly):** Comprehensive assessment (capacity, testing compliance, incident review)
- **Triggered:** After utility failure events (power outage, HVAC failure, ISP outage)

---

## 5. Unified Physical Infrastructure Dashboard

### 5.1 Dashboard Purpose

The Unified Physical Infrastructure Dashboard provides executive-level visibility into overall physical infrastructure security compliance across all three controls (A.7.4, A.7.5, A.7.11).

**Target Audience:**
- Executive Management (CISO, CFO, COO)
- Internal Audit (annual audit planning, ongoing compliance monitoring)
- External Auditors (ISO 27001 certification audits)
- Facilities Management (operational performance tracking)

### 5.2 Dashboard Tool

**Tool:** ISMS_Dashboard_Physical_Infrastructure.xlsx (generated by Script 4)

**Worksheets:**

**1. Executive Dashboard:**
- Overall physical infrastructure security score (weighted average A.7.4 + A.7.5 + A.7.11)
- Compliance score per control:
  - A.7.4 - Physical Security Monitoring: XX%
  - A.7.5 - Environmental Protection: XX%
  - A.7.11 - Utility Resilience: XX%
- Compliance trend (past 6-12 months, line chart)
- Top 5 findings (highest-risk non-compliance items)
- Top 5 recommendations (prioritized remediation actions)

**2. Access Monitoring Metrics (A.7.4):**
- Access control coverage: % of entry points
- CCTV coverage: % of required areas
- Intrusion detection coverage: % of sensitive areas
- Failed access attempts: Count per month (trend chart)
- Physical security incidents: Count per month (trend chart)

**3. Environmental Protection Metrics (A.7.5):**
- Fire detection coverage: % of facility area
- Fire suppression coverage: % of facility area
- Water detection coverage: % of at-risk areas
- Temperature excursions: Count per month (trend chart)
- Environmental incidents: Count per month (trend chart)

**4. Utility Uptime Metrics (A.7.11):**
- Power uptime: % (trend chart)
- HVAC uptime: % (trend chart)
- ISP uptime: % (trend chart)
- UPS battery health: % (gauge chart)
- Utility failure events: Count per month (trend chart)

**5. Incident Trends:**
- Physical security incidents by month (stacked bar chart: unauthorized access, tailgating, lost badge, other)
- Environmental incidents by month (stacked bar chart: fire, flood, temperature, other)
- Utility failures by month (stacked bar chart: power, HVAC, ISP)
- Severity distribution (pie chart: low, medium, high)

**6. Recommendations:**
- Prioritized list of remediation actions (based on compliance gaps)
- Estimated effort (hours/days)
- Estimated cost (if applicable)
- Target completion date
- Responsible party (facilities manager, IT operations, security operations)

### 5.3 Dashboard Update Frequency

- **Monthly Update:** After monthly automated assessment (first week of each month)
- **Quarterly Comprehensive Update:** After quarterly manual assessment (Q1, Q2, Q3, Q4)
- **Annual Update:** After annual comprehensive assessment (Q4)
- **On-Demand:** For executive presentations, audit preparation, board reporting

### 5.4 Dashboard Distribution

- **Monthly:** CISO, Facilities Manager, Security Operations Manager
- **Quarterly:** Executive Management, Internal Audit
- **Annual:** Board of Directors (if applicable), External Auditors
- **On-Demand:** As requested by stakeholders

---

## 6. Evidence Collection Framework

### 6.1 Evidence Types

**Configuration Evidence:**
- System documentation (access control, CCTV, intrusion detection, UPS, generator, HVAC, ISP)
- Network diagrams (physical security systems, power distribution, HVAC distribution, telecommunications)
- Floor plans (camera placement, sensor placement, equipment locations)
- System configuration files (access control user groups, CCTV retention settings, environmental monitoring thresholds)

**Operational Evidence:**
- Logs (access logs, CCTV recordings, environmental monitoring data, UPS monitoring data, network monitoring data)
- Test records (access control tests, CCTV tests, intrusion detection tests, UPS tests, generator tests, fire alarm tests, water sensor tests, ISP failover tests)
- Maintenance records (UPS battery replacement, generator oil changes, HVAC filter replacement, fire alarm inspections)
- Incident reports (physical security incidents, environmental incidents, utility failure incidents)

**Compliance Evidence:**
- Assessment reports (monthly, quarterly, annual)
- Compliance dashboard (current month, historical trends)
- Audit reports (internal audits, external audits)
- Certifications (ISO 27001, SOC 2, Uptime Institute Tier, if applicable)

**Third-Party Evidence (Colocation/Cloud):**
- Provider audit reports (SOC 2 Type II, ISO 27001)
- Provider SLA reports (physical security, environmental, utility uptime)
- Provider certifications (Uptime Institute, TIA-942, EN 50600)
- Responsibility matrix (documented in contract)

### 6.2 Evidence Retention

**Logs and Monitoring Data:**
- **Access logs:** 365 days minimum (critical facilities), 90 days minimum (standard facilities)
- **CCTV footage:** 90 days minimum (critical), 30 days minimum (standard), incident footage retained until incident closed + 12 months
- **Environmental monitoring data:** 12 months raw data (5-minute intervals), 3 years aggregated data (hourly averages)
- **UPS/Generator monitoring data:** 12 months raw data, 3 years aggregated data
- **Network monitoring data:** 12 months raw data (1-minute intervals), 3 years aggregated data

**Test Records and Maintenance Records:**
- **Retention:** 3 years minimum (demonstrate ongoing testing and maintenance compliance)
- **Contents:** Test date, equipment ID, test type, results, technician name

**Incident Reports:**
- **Retention:** 5 years minimum (demonstrate incident response capability, trend analysis)
- **Contents:** Incident date/time, location, type, severity, response actions, resolution, root cause analysis

**Configuration Documentation:**
- **Retention:** Current + 2 previous versions (track changes over time)
- **Version control:** Document version, date, author, changes

**Assessment Reports:**
- **Retention:** 3 years minimum (internal audits), 7 years minimum (external audits, regulatory audits)

### 6.3 Evidence Storage

**Secure Storage:**
- Evidence stored on access-controlled file servers (read-only for auditors, full access for facilities/security operations)
- Encryption for sensitive evidence (if contains PII, confidential business information)

**Backup:**
- All evidence backed up per [Organization] backup policy (see POL-A.8.13)
- Off-site backup for critical evidence (access logs, incident reports, test records)

**Retrieval:**
- Evidence retrievable within 24 hours for internal audits
- Evidence retrievable within 4 hours for external audits (if advance notice provided)

### 6.4 Evidence Register

Each assessment workbook includes **Evidence Register** worksheet:

**Evidence Register Contents:**
- **Evidence ID:** Unique identifier (e.g., A74-001, A75-002, A711-003)
- **Evidence Type:** Configuration, Operational, Compliance, Third-Party
- **Description:** Brief description of evidence (e.g., "Access control system configuration document")
- **Location:** File path or physical location (e.g., \\fileserver\isms\physical-security\access-control-config.pdf)
- **Date:** Evidence creation date or collection date
- **Custodian:** Person responsible for evidence (e.g., Facilities Manager, Security Operations Manager)
- **Linked Requirement:** Which policy requirement this evidence supports (e.g., POL-S2 Section 2.1.1)

**Evidence Traceability:**
- Each policy requirement → Linked to evidence in Evidence Register
- Each evidence item → Linked to specific policy requirement
- Auditors can trace requirement → evidence → verification

---

## 7. Compliance Scoring Methodology

### 7.1 Scoring Formula

**Overall Physical Infrastructure Security Score:**
```
Overall Score = (A.7.4 Score × 35%) + (A.7.5 Score × 35%) + (A.7.11 Score × 30%)
```

**Weighting Rationale:**
- A.7.4 (Physical Security Monitoring): 35% - Foundation for detection and response
- A.7.5 (Environmental Protection): 35% - Critical for facility protection
- A.7.11 (Utility Resilience): 30% - Essential for availability

**Per-Control Score Calculation:**
Each control score is weighted average of compliance metrics (see Sections 2.3, 3.3, 4.3)

**Example Calculation:**
```
A.7.4 Score:
- Access control coverage: 100% → 100 points (weight 20%)
- CCTV coverage: 95% → 95 points (weight 20%)
- Intrusion detection coverage: 100% → 100 points (weight 20%)
- Testing compliance: 100% → 100 points (weight 20%)
- Failed access attempts: 3/month (target <5) → 100 points (weight 10%)
- Incident count: 1/year (target <2) → 100 points (weight 10%)

A.7.4 Score = (100×0.2) + (95×0.2) + (100×0.2) + (100×0.2) + (100×0.1) + (100×0.1) = 99%

Similarly calculate A.7.5 Score and A.7.11 Score.

Overall Score = (99% × 0.35) + (88% × 0.35) + (95% × 0.30) = 94%
```

### 7.2 Compliance Thresholds

**Score Interpretation:**
- **90-100% (Excellent):** Full compliance, minor improvements only
  - **Action:** Maintain current controls, continuous improvement
- **75-89% (Good):** Mostly compliant, some gaps
  - **Action:** Address gaps within 6 months (non-critical) or 3 months (critical gaps)
- **60-74% (Acceptable):** Partial compliance, significant gaps
  - **Action:** Remediation plan required, address gaps within 3 months (all gaps)
- **<60% (Non-Compliant):** Major compliance failures
  - **Action:** Immediate remediation plan, escalate to executive management, address critical gaps within 30 days

**Audit Findings Correlation:**
- 90-100%: 0 major findings expected, <3 minor findings
- 75-89%: <2 major findings expected, <10 minor findings
- 60-74%: 2-5 major findings expected, numerous minor findings
- <60%: >5 major findings expected, remediation required before certification

### 7.3 Trend Analysis

**Month-Over-Month Trend:**
- Track overall score and per-control scores monthly
- Identify improving trends (score increasing) vs. declining trends (score decreasing)
- Investigate declining trends (root cause analysis, corrective actions)

**Target Trajectory:**
- New implementations: 60% → 75% → 85% → 90% over 12 months
- Established implementations: Maintain 85-95% (continuous improvement)

---

## 8. Related Documents

**Framework Sections:**
- **ISMS-POL-A.7.4-5-11-S1:** Executive Summary, Control Alignment, Scope (framework foundation)
- **ISMS-POL-A.7.4-5-11-S2:** Physical Security Monitoring (A.7.4) - requirements to be assessed
- **ISMS-POL-A.7.4-5-11-S3:** Environmental Protection (A.7.5) - requirements to be assessed
- **ISMS-POL-A.7.4-5-11-S4:** Utility Resilience (A.7.11) - requirements to be assessed
- **ISMS-IMP-A.7.4-5-11-S4:** Facilities Assessment (detailed assessment procedures)

**Assessment Tools:**
- **generate_assessment_1_access_monitoring.py:** Script to generate Access Monitoring workbook
- **generate_assessment_2_environmental_protection.py:** Script to generate Environmental Protection workbook
- **generate_assessment_3_utility_resilience.py:** Script to generate Utility Resilience workbook
- **generate_dashboard_physical_infrastructure.py:** Script to generate unified compliance dashboard
- **normalize_physical_infrastructure_assessments.py:** Utility script for data normalization
- **excel_sanity_check_physical_infrastructure.py:** Pre-delivery validation script

**Related ISMS Policies:**
- **ISMS-POL-00:** Regulatory Applicability Framework (compliance context)
- **ISMS-POL-A.8.13:** Information Backup (backup policy referenced for evidence backup)
- **ISMS-POL-A.5.24-27:** Incident Management (incident reporting and tracking)

**External Standards:**
- **ISO/IEC 27001:2022:** Controls A.7.4, A.7.5, A.7.11 (controls being assessed)
- **ISO/IEC 27002:2022:** Detailed guidance for assessment criteria

---

**END OF ISMS-POL-A.7.4-5-11-S5**

---

**Document Approval Signatures:**

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Policy Author | [Name] | | |
| Internal Audit Manager | [Name] | | |
| Facilities Manager | [Name] | | |
| CISO | [Name] | | |

---

*"Assessment is not just filling out spreadsheets. It's systematic measurement of compliance using automated data collection, manual verification, evidence-based scoring, and trend analysis—all designed to demonstrate ISO 27001:2022 compliance and drive continuous improvement in physical infrastructure security."*
