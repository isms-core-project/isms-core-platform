# ISMS-POL-A.8.16 – Monitoring
## Comprehensive Policy & Implementation Framework

---

**Document ID**: ISMS-POL-A.8.16  
**Title**: Monitoring Policy  
**Version**: 1.0  
**Date**: [Date]   
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date]  | CISO / Information Security Manager | Initial policy framework |

**Review Cycle**: Annual (or upon significant organizational/regulatory/threat landscape changes)  
**Next Review Date**: [Approval Date + 12 months]  
**Approvers**: 
- Chief Information Security Officer (CISO)
- Chief Information Officer (CIO) or IT Director
- Security Operations Center (SOC) Lead
- Legal/Compliance Officer (for regulatory alignment)
- Executive Management / Board (for strategic approval)

**Distribution**: Security team, SOC analysts, system owners, IT operations, network team  
**Related Standards**: ISO/IEC 27001:2022 Control A.8.16, ISO/IEC 27002:2022 Control 8.16, NIST SP 800-92, CIS Controls v8

---

## Executive Summary

This document serves as the **master index** for the organization's monitoring activities control framework, implementing ISO/IEC 27001:2022 Control A.8.16. The framework consists of:

- **Policy Layer:** Governance documents defining requirements (~13 documents)
- **Assessment Layer:** Technical evaluation specifications (5 markdown specs)
- **Implementation Layer:** Automated Excel workbook generators (5 Python scripts)
- **Validation Layer:** Quality assurance and checking tools (1 sanity check script)
- **Integration Layer:** Executive dashboard with consolidated oversight

**Approach:** This framework uses a **system engineering methodology** rather than traditional paperwork-based compliance. All assessments are generated via Python scripts to ensure consistency, repeatability, and maintainability.

**Control Objective (ISO/IEC 27002:2022 Control 8.16):**
> *Networks, systems and applications should be monitored for anomalous behavior and appropriate actions taken to evaluate potential information security incidents.*

**Purpose:** Detect abnormal behavior and potential information security incidents through systematic monitoring; establish baselines for normal behavior; respond appropriately to deviations; and integrate monitoring outputs with incident management processes.

**Philosophy:** As Feynman wisely noted: *"The first principle is that you must not fool yourself—and you are the easiest person to fool."* This framework prevents **cargo cult monitoring**—having SIEM dashboards that no one reads, alerts that everyone ignores, and "baselines" that are just guesses. True monitoring requires documented baselines, measurable thresholds, and evidenced response procedures.

---

## Control Alignment

**ISO/IEC 27001:2022 Annex A.8.16 - Monitoring Activities**

**Control Type**: #Detective #Corrective  
**Information Security Properties**: #Confidentiality #Integrity #Availability  
**Cybersecurity Concepts**: #Detect #Respond  
**Operational Capabilities**: #Information_Security_Incident_Handling  
**Security Domains**: #Defense

This policy framework provides the organizational governance, requirements, roles, and procedures necessary to fulfill Control 8.16 objectives and integrate monitoring activities across the Information Security Management System (ISMS).

**Key ISO 27002:2022 Guidance Elements Addressed:**
- Monitoring scope and level determination (business requirements, legal compliance)
- Items to be monitored (network traffic, system access, configuration files, security tool logs, event logs, resource usage)
- Baseline establishment for normal behavior (system utilization, access patterns)
- Anomaly detection capabilities (malware activity, attack signatures, unusual behavior, unauthorized access)
- Continuous monitoring with automated tools (real-time or regular intervals)
- Alert generation and notification (predefined thresholds, minimized false positives)
- Personnel training for alert response

**Regulatory Alignment**: This framework complies with ISO/IEC 27001:2022 requirements and aligns with Swiss Federal Data Protection Act (FADP), EU GDPR where applicable, and industry-specific regulations (financial services, healthcare, etc.) as relevant to the organization.

---

## 1. Framework Structure

### 1.1 Purpose

Define mandatory requirements for monitoring activities to:
- Detect anomalous behavior in networks, systems, and applications
- Identify potential information security incidents at the earliest possible stage
- Establish measurable baselines for normal behavior
- Configure effective alerting with minimal false positives
- Enable rapid response to security events
- Support forensic investigation and compliance auditing
- Integrate monitoring outputs with incident response processes

### 1.2 Scope

This framework applies to:

- **Network segments**: All networks where monitoring is technically feasible (on-premises LANs, WANs, wireless, remote access, cloud)
- **Systems**: All servers, workstations, network devices, security appliances (critical systems mandatorily monitored, non-critical systems risk-assessed)
- **Applications**: Business-critical applications, security-sensitive applications, externally-facing applications
- **Users**: All users accessing organizational resources (employees, contractors, service accounts, automated systems)
- **Monitoring technologies**: All monitoring solutions regardless of vendor or implementation method (SIEM, IDS/IPS, NDR, EDR, UEBA, log management, APM)

### 1.3 Users

This framework is binding for:

- **Security Operations Center (SOC)** – Responsible for 24/7 monitoring and initial alert triage
- **Security Team** – Responsible for baseline definition, threshold tuning, monitoring tool management
- **System Owners** – Accountable for ensuring their systems are monitored per policy requirements
- **Network Team** – Responsible for network monitoring infrastructure and traffic analysis
- **Incident Response Team** – Responsible for escalated alert investigation and incident handling
- **IT Operations** – Responsible for system performance monitoring and operational alerting
- **Management** – Accountable for monitoring control effectiveness and resourcing
- **Auditors and regulators** – May review for compliance verification

### 1.4 Applicability of Regulatory Frameworks

References to standards, frameworks, and regulations throughout this monitoring activities framework are categorized per **ISMS-POL-00 (Regulatory Applicability Framework)**:

**Mandatory Compliance:**
* Swiss Federal Data Protection Act (FADP)
* EU GDPR (where processing EU personal data)
* ISO/IEC 27001:2022 (Control A.8.16)
* [Additional mandatory regulations per ISMS-POL-00]

**Informational Reference / Best Practice Alignment:**
* NIST SP 800-92 (Guide to Computer Security Log Management)
* NIST SP 800-137 (Information Security Continuous Monitoring)
* CIS Controls v8 (Control 8, 13)
* MITRE ATT&CK Framework
* [Other frameworks per ISMS-POL-00]

**United States Federal Requirements:**
References to US federal frameworks (FISMA, FIPS, FedRAMP, NIST cybersecurity requirements) apply only where the organization has explicit US federal contractual obligations, as defined in **ISMS-POL-00**.

For complete regulatory categorization, refer to **ISMS-POL-00 - Regulatory Applicability Framework**.

---

## 2. Policy Documents

### 2.1 Policy Structure

The monitoring activities policy framework consists of the following modular documents:

| Document ID | Title | Purpose | Lines |
|-------------|-------|---------|-------|
| **ISMS-POL-A.8.16** | Master Framework | This document - index and overview | ~400 |
| **ISMS-POL-A.8.16-S1** | Purpose, Scope, Definitions | Foundation and terminology | ~300 |
| **ISMS-POL-A.8.16-S2** | Monitoring Requirements | Requirements overview | ~200 |
| **ISMS-POL-A.8.16-S2.1** | Monitoring Infrastructure Requirements | Tool capabilities, coverage, integration | ~350 |
| **ISMS-POL-A.8.16-S2.2** | Baseline & Anomaly Detection Requirements | Baseline establishment, anomaly types, detection methods | ~350 |
| **ISMS-POL-A.8.16-S2.3** | Alert Management & Response Requirements | Alert classification, SLAs, escalation, tuning | ~350 |
| **ISMS-POL-A.8.16-S2.4** | Retention & Archival Requirements | Data retention, archival, evidence preservation | ~250 |
| **ISMS-POL-A.8.16-S3** | Roles & Responsibilities | RACI and accountability | ~300 |
| **ISMS-POL-A.8.16-S4** | Policy Governance | Review, exceptions, compliance | ~300 |
| **ISMS-POL-A.8.16-S5** | Annexes | Supporting materials | Variable |
| **ISMS-POL-A.8.16-S5.A** | Monitoring Capability Standards | Technical reference (vendor-agnostic) | ~300 |
| **ISMS-POL-A.8.16-S5.B** | Baseline Definition Template | Template for documenting baselines | ~150 |
| **ISMS-POL-A.8.16-S5.C** | Alert Response Procedures | Incident handling procedures | ~250 |
| **ISMS-POL-A.8.16-S5.D** | Quick Reference Guide | Operational summary | ~150 |

**Total Policy Layer:** ~13 documents, approximately 3,200 lines

**Design Philosophy**: Each document is independently versionable (maximum 300-400 lines) to enable granular change management, targeted stakeholder reviews, and clear audit trails.

### 2.2 Document Hierarchy
```
ISMS-POL-A.8.16 (Master) ← You are here
├── ISMS-POL-A.8.16-S1 (Purpose, Scope, Definitions)
├── ISMS-POL-A.8.16-S2 (Requirements Overview)
│   ├── ISMS-POL-A.8.16-S2.1 (Monitoring Infrastructure Requirements)
│   ├── ISMS-POL-A.8.16-S2.2 (Baseline & Anomaly Detection Requirements)
│   ├── ISMS-POL-A.8.16-S2.3 (Alert Management & Response Requirements)
│   └── ISMS-POL-A.8.16-S2.4 (Retention & Archival Requirements)
├── ISMS-POL-A.8.16-S3 (Roles & Responsibilities)
├── ISMS-POL-A.8.16-S4 (Policy Governance)
└── ISMS-POL-A.8.16-S5 (Annexes)
    ├── ISMS-POL-A.8.16-S5.A (Monitoring Capability Standards)
    ├── ISMS-POL-A.8.16-S5.B (Baseline Definition Template)
    ├── ISMS-POL-A.8.16-S5.C (Alert Response Procedures)
    └── ISMS-POL-A.8.16-S5.D (Quick Reference Guide)
```

---

## 3. Assessment & Implementation Framework

### 3.1 Assessment Domains

The implementation assessment framework consists of five domains, each with a dedicated Excel workbook for stakeholder completion:

| Domain | Assessment Area | File Name | Purpose |
|--------|-----------------|-----------|---------|
| **Domain 1** | Monitoring Infrastructure | ISMS-IMP-A.8.16.1 | Assess monitoring tools (SIEM, IDS/IPS, NDR, EDR, UEBA), tool capabilities, integration, and redundancy |
| **Domain 2** | Baseline & Anomaly Detection | ISMS-IMP-A.8.16.2 | Assess baseline coverage, documented baselines, anomaly detection rules, threshold configuration |
| **Domain 3** | Log Sources & Coverage | ISMS-IMP-A.8.16.3 | Assess log source inventory, coverage mapping, integration status, gap analysis |
| **Domain 4** | Alert Management & Response | ISMS-IMP-A.8.16.4 | Assess alert rules, performance metrics, response time SLAs, personnel training |
| **Domain 5** | Compliance Dashboard | ISMS-IMP-A.8.16.5 | Executive consolidation of Domains 1-4, KPI tracking, critical gaps summary |

### 3.2 Assessment Specifications (Markdown)

Each domain has a detailed markdown specification document that defines:
- Excel workbook structure (sheets, columns, validation rules)
- Assessment questions and checklists
- Data entry requirements
- Evidence collection requirements
- Compliance scoring methodology

**Files:**
- `ISMS-IMP-A.8.16.1 - Monitoring Infrastructure Assessment.md`
- `ISMS-IMP-A.8.16.2 - Baseline & Anomaly Detection Assessment.md`
- `ISMS-IMP-A.8.16.3 - Log Sources & Coverage Assessment.md`
- `ISMS-IMP-A.8.16.4 - Alert Management & Response Assessment.md`
- `ISMS-IMP-A.8.16.5 - Compliance Dashboard Specification.md`

### 3.3 Excel Workbook Generators (Python Scripts)

Each assessment specification has a corresponding Python script that generates the Excel workbook:

**Scripts:**
- `generate_a816_1_monitoring_infrastructure.py`
- `generate_a816_2_baseline_anomaly_detection.py`
- `generate_a816_3_log_sources_coverage.py`
- `generate_a816_4_alert_management_response.py`
- `generate_a816_5_compliance_dashboard.py`

**Requirements:**
- Python 3.x with openpyxl library (`sudo apt install python3-openpyxl`)
- Execution generates date-stamped Excel workbook
- All styling, validation, and formulas automatically applied

**Validation Script:**
- `excel_sanity_check_a816.py` - Validates generated workbooks for correctness

### 3.4 Workbook Structure (Standard across all domains)

Each Excel workbook contains:
- **Sheet 1**: Instructions & Legend (how to use, color coding, definitions)
- **Sheets 2-6**: Assessment sheets (domain-specific content with standardized 17 base columns A-Q)
- **Sheet 7**: Summary Dashboard (compliance scoring, KPIs, gap summary)
- **Sheet 8**: Evidence Register (100 rows for evidence tracking)
- **Sheet 9**: Approval Sign-Off (3-level approval workflow)

**Standard Column Structure (A-Q, 17 columns):**
- A: System/Asset/Tool Name (30 chars)
- B: Type/Category (22 chars, dropdown)
- C-O: Domain-specific assessment fields
- P: Status (12 chars, dropdown: ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A)
- Q: Notes (25 chars, free text)

**Extended Columns (R-X):** Domain-specific additional fields as needed

---

## 4. Key Requirements Summary

### 4.1 Monitoring Scope (per ISO 27002:2022)

Organizations **SHALL** include the following in the monitoring system:

**a) Network & System Traffic:**
- Inbound and outbound network traffic (firewall, IDS/IPS, NDR)
- System and application traffic (server logs, application logs)

**b) Access to Critical Resources:**
- Access to systems, servers, network equipment, monitoring systems, critical applications
- Authentication events (successful/failed logins, privilege escalations)

**c) Configuration Changes:**
- System and network configuration files at critical or administrative level
- Changes to security controls, policies, firewall rules

**d) Security Tool Logs:**
- Antivirus, IDS/IPS, web filtering, firewalls, data loss prevention
- Security appliance alerts and actions

**e) Event Logs:**
- System and network activity event logs (Windows Event Logs, syslog, etc.)
- Application event logs

**f) Code Integrity:**
- Verification that code execution is authorized and not tampered with (e.g., recompilation to add malicious code)

**g) Resource Usage:**
- Processor, disk, memory, bandwidth utilization and performance metrics

### 4.2 Baseline Establishment (per ISO 27002:2022)

Organizations **SHALL** establish a baseline for normal behavior considering:

**a) System Utilization:**
- Review system utilization during normal and peak times
- Identify typical resource consumption patterns

**b) Access Patterns:**
- Usual time of access, location of access, frequency of access for each user or group of users
- Establish user behavior baselines

### 4.3 Anomaly Detection (per ISO 27002:2022)

Monitoring systems **SHALL** be configured to detect anomalous behavior including:

**a) Unplanned Termination:** Unexpected shutdown of processes or applications  
**b) Malware Activity:** Activities typically associated with malware or traffic from known malicious IPs/domains (e.g., botnet C2)  
**c) Attack Signatures:** Known attack characteristics (e.g., denial-of-service, buffer overflows)  
**d) Unusual System Behavior:** Unusual behavior such as keystroke logging, process injection, deviations in standard protocol usage  
**e) Bottlenecks & Overloads:** Network queue delays, latency, jitter  
**f) Unauthorized Access:** Unauthorized (actual or attempted) access to systems or information  
**g) Unauthorized Scanning:** Unauthorized scanning of business applications, systems, and networks  
**h) Access Attempts:** Successful and unsuccessful access attempts to protected resources (DNS servers, web portals, file systems)  
**i) Unusual User/System Behavior:** Behavior that deviates from expected patterns

### 4.4 Continuous Monitoring & Alerting (per ISO 27002:2022)

Organizations **SHALL:**
- Conduct continuous monitoring using monitoring tools
- Monitor in real-time or at regular intervals depending on organizational needs and capabilities
- Use tools capable of processing large volumes of data, adapting to changing threat landscape, enabling real-time notification
- Configure automated monitoring software to generate alerts based on predefined thresholds
- Tune alert systems to organizational baseline to minimize false positives
- Train personnel to respond to alerts and properly interpret potential incidents

---

## 5. Integration with ISMS

### 5.1 Related Controls

Monitoring activities integrate with and support multiple ISO 27001 controls:

| Control | Integration Point |
|---------|-------------------|
| **A.5.1** | Policies - Monitoring policy is part of ISMS policy suite |
| **A.5.7** | Threat Intelligence - Monitoring generates intelligence from observed attacks |
| **A.5.16** | Identity Management - User/entity behavior monitoring uses identity data |
| **A.5.24-5.28** | Incident Management - Monitoring alerts trigger incident response process |
| **A.8.7** | Malware Protection - Malware detection alerts feed into monitoring |
| **A.8.8** | Vulnerability Management - Monitoring identifies exploitation attempts, prioritizes patching |
| **A.8.12** | Data Leakage Prevention - Monitoring detects data exfiltration patterns |
| **A.8.15** | Logging - Monitoring analyzes log data generated by logging controls |
| **A.8.16** | **Monitoring Activities** - **This control** |
| **A.8.17** | Clock Synchronization - Accurate timestamps essential for monitoring correlation |
| **A.8.20** | Network Security - Network security controls generate monitored events |
| **A.8.23** | Web Filtering - Web filtering logs feed into monitoring as a log source |

### 5.2 Bidirectional Data Flows

**Monitoring Activities → Other Controls:**
- Security alerts to incident response (A.5.24-5.28) - detected incidents escalated
- Threat intelligence to vulnerability management (A.8.8) - observed exploitation prioritizes patching
- Attack patterns to threat intelligence (A.5.7) - monitoring generates intelligence feeds
- Performance data to capacity management (A.8.6) - resource utilization trends
- Policy violations to compliance (A.5.36) - monitoring provides compliance evidence

**Other Controls → Monitoring Activities:**
- Log data from logging (A.8.15) - primary data source for analysis
- Malware alerts from endpoint protection (A.8.7) - security events to correlate
- Network traffic from network security (A.8.20) - traffic patterns to analyze
- Web filtering logs from web filtering (A.8.23) - user behavior data
- Identity data from identity management (A.5.16) - user/entity context for baselines

### 5.3 Risk Management Integration

**Risk Treatment:**
- Monitoring controls as detective measure in defense-in-depth strategy
- Residual risks from monitoring gaps tracked in risk register
- Risk assessment feeds monitoring scope and prioritization

**Risk Register:**
- Monitoring risks (blind spots, alert fatigue, insufficient coverage) documented in Compliance Dashboard (Domain 5)
- Risk scores drive remediation urgency (critical gaps addressed first)
- Quarterly risk reassessment based on monitoring effectiveness metrics

---

## 6. Assessment Methodology

### 6.1 Assessment Approach

**System Engineering Principle**: Assessments are not "fill in the blank" compliance exercises. They are evidence-based technical evaluations that force specificity:

- **NOT**: "We have monitoring" (cargo cult compliance)
- **YES**: "We monitor 127 servers using SIEM X, with 89% coverage documented in Domain 1 Sheet 3, with 23 documented baselines in Domain 2 Sheet 2, and 156 alert rules with 18% false positive rate documented in Domain 4 Sheet 3"

### 6.2 Quarterly Assessment Cycle

**Frequency:** Quarterly (or upon significant change to IT infrastructure, threat landscape, or regulatory requirements)

**Cycle:**
1. **Week 1:** Generate assessment workbooks (Domains 1-4), distribute to responsible teams
2. **Weeks 2-3:** Teams complete assessments, attach evidence, document gaps
3. **Week 4:** Security team reviews, validates, identifies critical gaps
4. **Week 5:** Consolidate into Domain 5 dashboard, executive review, remediation planning
5. **Week 6:** Remediation initiation, tracking, sign-off

### 6.3 Scoring Methodology

**Compliance Status per Item:**
- **✅ Compliant**: Requirement fully met, evidence provided
- **⚠️ Partial**: Requirement partially met, remediation plan in progress
- **❌ Non-Compliant**: Requirement not met, significant gap exists
- **N/A**: Requirement not applicable to this organization/environment

**Domain-Level Compliance Percentage:**
- Formula: (Compliant Items / Total Applicable Items) × 100%
- Target: >90% compliant for all domains
- Partial compliance counts as 50% toward total

**Overall Control Compliance:**
- Weighted average of Domain 1-4 scores
- Domain weights: Domain 1 (25%), Domain 2 (30%), Domain 3 (25%), Domain 4 (20%)
- Target: >90% overall compliance

### 6.4 Evidence Requirements

All "Compliant" status claims **SHALL** be supported by evidence:

**Acceptable Evidence Types:**
- Configuration screenshots (monitoring tool configs, alert rules, baselines)
- Log exports (sample monitoring data, alert logs)
- Documentation (baseline definitions, response procedures, training records)
- Reports (SIEM reports, alert performance metrics, SLA compliance reports)
- Meeting minutes (baseline review meetings, alert tuning sessions)

**Evidence Storage:**
- Evidence files referenced in "Evidence Register" sheet (Sheet 8)
- Evidence files stored in centralized ISMS repository (e.g., SharePoint, document management system)
- Evidence retention: Minimum 12 months, or per regulatory requirements

---

## 7. Key Performance Indicators (KPIs)

### 7.1 Monitoring Effectiveness Metrics

**Detection Metrics:**
- **Mean Time to Detect (MTTD)**: Average time from incident occurrence to detection
  - Target: <15 minutes for critical incidents
- **Detection Rate**: Percentage of actual incidents detected by monitoring
  - Target: >95%

**Response Metrics:**
- **Mean Time to Respond (MTTR)**: Average time from detection to initial response
  - Target: <15 minutes for critical alerts, <60 minutes for high alerts
- **Alert Response SLA Compliance**: Percentage of alerts responded to within SLA
  - Target: >90%

**Quality Metrics:**
- **False Positive Rate**: Percentage of alerts that are false positives
  - Target: <20%
- **Alert Tuning Effectiveness**: Reduction in false positives over time
  - Target: 10% reduction quarter-over-quarter

**Coverage Metrics:**
- **Monitored Asset Coverage**: Percentage of critical assets with active monitoring
  - Target: >95% for critical assets, >80% for all assets
- **Baseline Coverage**: Percentage of monitored assets with documented baselines
  - Target: >90%

### 7.2 Dashboard KPIs (Domain 5)

The Compliance Dashboard (Domain 5) tracks:
- Overall compliance percentage (Domains 1-4 weighted average)
- Compliance percentage per domain
- Number of critical gaps (severity: critical/high)
- MTTD / MTTR trend (quarterly comparison)
- False positive rate trend
- Coverage percentage trend
- Baseline coverage percentage

---

## 8. Roles & Responsibilities (High-Level)

Detailed RACI matrix in **ISMS-POL-A.8.16-S3**.

| Role | Responsibility |
|------|----------------|
| **CISO** | Accountable for overall monitoring control effectiveness, policy approval, strategic direction |
| **SOC Lead** | Responsible for 24/7 monitoring operations, alert triage, initial incident response |
| **Security Team** | Responsible for baseline definition, threshold tuning, monitoring tool management, policy maintenance |
| **System Owners** | Accountable for ensuring their systems are monitored, providing system-specific baselines |
| **Network Team** | Responsible for network monitoring infrastructure, traffic analysis, network baselines |
| **Incident Response Team** | Responsible for escalated alert investigation, incident handling, post-incident review |
| **IT Operations** | Informed of monitoring activities, provides operational context, assists with performance baselines |

---

## 9. Compliance & Audit

### 9.1 Internal Audits

**Annual Internal Audit** (per ISO 27001 Clause 9.2):
- Review monitoring policy documents for accuracy and completeness
- Assess implementation effectiveness (review assessment workbooks from last quarter)
- Verify evidence exists for compliance claims
- Interview SOC personnel on alert response procedures
- Test alert response (simulate alerts, measure response times)
- Verify baselines are documented and current
- Check monitoring coverage against asset inventory

**Audit Evidence:**
- Completed assessment workbooks (Domains 1-5)
- Evidence register with attached evidence files
- Alert logs demonstrating response times
- Baseline documentation
- Training records (personnel certifications, training attendance)

### 9.2 External Audits

**ISO 27001 Certification Audit:**
- Auditor reviews monitoring policy framework (this document + S1-S5.D)
- Auditor samples assessment workbooks for evidence quality
- Auditor interviews SOC personnel
- Auditor reviews incident reports to verify monitoring detected incidents
- Auditor verifies compliance with Control A.8.16 requirements

**Regulatory Audits** (if applicable):
- Financial services regulators may review monitoring for transaction monitoring, fraud detection
- Healthcare regulators may review monitoring for HIPAA compliance (access monitoring)
- Data protection authorities may review monitoring for GDPR compliance (privacy considerations)

---

## 10. Continuous Improvement

### 10.1 Feedback Loops

**Incident Review → Monitoring Improvement:**
- Post-incident review asks: "Did monitoring detect this incident? If not, why not?"
- Gaps identified → New monitoring rules, baselines, or log sources added
- Detection successes celebrated → Best practices documented

**Alert Tuning → False Positive Reduction:**
- Quarterly review of false positive rates per alert rule (Domain 4)
- High false positive alerts → Threshold adjustment or rule refinement
- Alert tuning documented in change log

**Coverage Expansion:**
- Quarterly review of asset inventory vs. monitored assets (Domain 3)
- New critical assets added → Monitoring deployed, baselines established
- Technology changes (new cloud services, applications) → Monitoring extended

### 10.2 Metrics-Driven Improvement

**Quarterly Metrics Review:**
- CISO reviews KPIs from Domain 5 dashboard
- Trends identified (improving/degrading metrics)
- Root cause analysis for degrading metrics
- Action plans for improvement

**Benchmarking:**
- Compare organizational metrics to industry benchmarks (MTTD, MTTR, false positive rate)
- Identify opportunities for improvement
- Set realistic targets based on benchmarks

---

## 11. Training & Awareness

### 11.1 Role-Specific Training

**SOC Analysts:**
- Alert triage and prioritization (40 hours initial, 8 hours annual refresher)
- Alert investigation techniques
- Escalation procedures
- Tool-specific training (SIEM, IDS/IPS, NDR, EDR)

**Security Team:**
- Baseline definition methodologies (16 hours initial, 4 hours annual refresher)
- Threshold tuning techniques
- Monitoring tool administration

**System Owners:**
- Monitoring policy overview (2 hours initial, 1 hour annual refresher)
- Responsibilities for ensuring system monitoring
- How to define system-specific baselines

### 11.2 General Awareness

**All Personnel:**
- Annual security awareness training includes: "Why monitoring matters" (monitoring protects the organization from threats)
- Monitoring is not surveillance—it's security (privacy considerations addressed)
- Reporting suspicious activity (complements monitoring)

---

## 12. Reference Documents

### 12.1 Internal Documents

**Policy Layer:**
- ISMS-POL-A.8.16 (this document) + Sections S1 through S5.D (13 documents total)

**Assessment Layer:**
- ISMS-IMP-A.8.16.1 – Monitoring Infrastructure Assessment (Markdown + Excel)
- ISMS-IMP-A.8.16.2 – Baseline & Anomaly Detection Assessment (Markdown + Excel)
- ISMS-IMP-A.8.16.3 – Log Sources & Coverage Assessment (Markdown + Excel)
- ISMS-IMP-A.8.16.4 – Alert Management & Response Assessment (Markdown + Excel)
- ISMS-IMP-A.8.16.5 – Compliance Dashboard (Markdown + Excel)

**Automation Layer:**
- Generator Scripts (5 Python files)
- Validation Script (1 Python file)

**Related ISMS Policies:**
- ISMS-POL-A.8.15 - Logging (provides data for monitoring)
- ISMS-POL-A.5.24-5.28 - Incident Management (consumes monitoring alerts)
- ISMS-POL-A.8.8 - Vulnerability Management (informed by monitoring)
- ISMS-POL-A.8.20 - Network Security (generates monitored events)
- ISMS-POL-A.8.23 - Web Filtering (log source for monitoring)

### 12.2 External Standards & Regulations

**International Standards:**
- ISO/IEC 27001:2022 – Information Security Management Systems
- ISO/IEC 27002:2022 – Information Security Controls (Control 8.16 guidance)
- ISO/IEC 27035 – Incident Management (integration)

**Technical Standards:**
- NIST SP 800-92 – Guide to Computer Security Log Management
- NIST SP 800-137 – Information Security Continuous Monitoring (ISCM)
- CIS Controls v8 – Control 8 (Audit Log Management), Control 13 (Network Monitoring)

**Regulatory:**
- Swiss Federal Act on Data Protection (FADP/nDSG)
- EU General Data Protection Regulation (GDPR) – where applicable
- Industry-specific regulations (as applicable to organization)

**Framework Alignment:**
- NIST Cybersecurity Framework (CSF) – Detect function
- MITRE ATT&CK Framework – Detection tactics
- SANS Internet Storm Center – Threat intelligence

---

## Appendix A: Philosophy & Methodology

### A.1 Evidence Over Theater

> "It doesn't matter how beautiful your theory is, it doesn't matter how smart you are. If it doesn't agree with experiment, it's wrong."  
*— Richard Feynman*

Applied to monitoring: It doesn't matter how expensive your SIEM is, how impressive your dashboard looks, or how many alerts you generate. If you can't demonstrate that you:
1. Have documented baselines for normal behavior
2. Can detect deviations from those baselines
3. Respond to alerts within defined SLAs
4. Have evidence of all the above

...then you have **cargo cult monitoring**.

### A.2 The Cargo Cult Monitoring Trap

During World War II, Pacific islanders saw planes land with cargo. After the war, they built fake runways and bamboo control towers, hoping planes would return with cargo. The form was there, but not the substance.

**Cargo Cult Monitoring** is:
- ✅ "We have a SIEM!" (but logs aren't reviewed)
- ✅ "We get alerts!" (but they're all ignored)
- ✅ "We have baselines!" (but they're guesses, not measurements)
- ✅ "We're compliant!" (but have no evidence)

**Actual Evidence-Based Monitoring** is:
- ✅ Documented baselines in Domain 2 workbook with justification and update frequency
- ✅ Alert rules in Domain 4 workbook with measured false positive rates
- ✅ Response time SLAs with actual performance tracking
- ✅ Coverage maps showing what is monitored (and what isn't)
- ✅ Quarterly assessments with filled Excel workbooks, not empty templates

### A.3 The Assessment Workbooks Force Honesty

The assessment workbooks are designed to prevent self-deception:
- **Forcing function**: If you claim compliance, you must provide evidence
- **Gap identification**: If you skip rows, the gaps are visible and countable
- **Trending**: Quarterly assessments show improvement (or lack thereof) over time
- **Accountability**: Sign-off sheet (Sheet 9) requires named individuals to attest to accuracy

---

## Appendix B: Frequently Asked Questions

**Q1: What if we don't have a SIEM yet?**  
A: Document the gap in Domain 1 assessment. Use alternative monitoring tools (IDS/IPS, log aggregation, performance monitoring) in the interim. Develop a remediation plan with timeline and budget.

**Q2: How do we establish baselines for a new system?**  
A: Monitor the system for 30-90 days (normal operations, include peak times). Document observed patterns using template in ISMS-POL-A.8.16-S5.B. Refine baseline as more data is collected.

**Q3: Our false positive rate is 40%. Is that acceptable?**  
A: No. Target is <20%. High false positive rate leads to alert fatigue and missed real incidents. Prioritize alert tuning (Domain 4 assessment). Consider better baselining (Domain 2) to improve detection accuracy.

**Q4: Can we monitor some systems but not others?**  
A: Yes, but it must be risk-based and documented. Critical assets MUST be monitored. Non-critical assets MAY be excluded if justified by risk assessment. Document exclusions in Domain 3 assessment with risk acceptance.

**Q5: How is this different from logging (A.8.15)?**  
A: Logging (A.8.15) is *recording* events. Monitoring (A.8.16) is *analyzing* those events to detect anomalies. Logging provides the data, monitoring provides the intelligence.

**Q6: Who is responsible if monitoring fails to detect an incident?**  
A: Depends on root cause. If monitoring was properly configured and maintained per policy but incident was novel/sophisticated, no one is at fault (continuous improvement opportunity). If monitoring gap was known and not addressed, accountability per RACI matrix (ISMS-POL-A.8.16-S3).

---

**END OF MASTER POLICY DOCUMENT**

*"The purpose of monitoring is not to generate alerts—it is to detect threats before they become breaches. Evidence, not dashboards."*