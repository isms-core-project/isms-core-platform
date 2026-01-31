# ISMS-POL-A.8.16-S2
## Monitoring Activities Requirements - Overview

**Document ID**: ISMS-POL-A.8.16-S2
**Title**: Monitoring Activities Requirements - Overview  
**Version**: 1.0  
**Date**: [Date]   
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date]  | Information Security Manager | Initial requirements framework |

**Review Cycle**: Semi-annual (or upon significant threat landscape changes)  
**Next Review Date**: [Approval Date + 6 months]  
**Approvers**: 
- Primary: Chief Information Security Officer (CISO)
- Technical Review: Security Operations Center (SOC) Lead / Security Architect
- Operational Review: IT Operations Manager

**Distribution**: Security team, SOC analysts, IT operations, system administrators  
**Related Documents**: ISMS-POL-A.8.16-S2.1 through S2.4 (specific requirements)

---

## 2.1 Introduction

This document provides an overview of monitoring requirements established to implement ISO/IEC 27001:2022 Control A.8.16. Detailed requirements are organized into four functional domains, each documented in separate policy sections to support granular change management and stakeholder accountability.

Monitoring requirements balance multiple organizational objectives:

- **Security**: Early detection of security incidents and anomalous behavior
- **Compliance**: Adherence to legal, regulatory, and contractual monitoring obligations
- **Privacy**: Respect for user privacy while maintaining necessary security visibility
- **Operational Efficiency**: Minimized false positives, maintainable baselines, actionable alerts
- **Forensic Readiness**: Adequate evidence collection for incident investigation and legal proceedings
- **Performance**: Monitoring infrastructure that doesn't degrade system performance

### 2.1.1 The Challenge of Effective Monitoring

*"Monitoring without baselines is like astronomy without telescopes—you're just staring into darkness."*

Organizations often face cargo cult monitoring: 
- ✅ SIEM deployed? Check.
- ✅ Logs collected? Check.
- ✅ Alerts configured? Check.
- ❌ Can you detect an actual attack? ... *crickets*

**Effective monitoring requires:**
1. **Documented baselines** - Measurable profiles of normal behavior
2. **Tuned thresholds** - Alert triggers that balance detection vs. noise
3. **Response procedures** - Clear actions when alerts fire
4. **Validation** - Regular testing to verify detection works

This framework prevents cargo cult monitoring by requiring evidence at every stage.

---

## 2.2 Requirements Framework

Monitoring requirements are organized into four domains:

### 2.2.1 Monitoring Infrastructure Requirements (S2.1)

**Objective**: Establish the technical infrastructure necessary to collect, analyze, and store security monitoring data.

**Scope**: Requirements for:
- Log source coverage (systems, networks, applications to be monitored)
- Monitoring tool capabilities (SIEM, IDS/IPS, EDR, NDR, etc.)
- Data collection and aggregation infrastructure
- Parsing and normalization of log formats
- Integration with other security controls (threat intel, incident response, SOAR)
- Redundancy and high availability
- Performance and scalability requirements
- Secure transmission of monitoring data

**Primary Stakeholders**: Security Engineering, SOC, IT Operations  
**Detailed Requirements**: ISMS-POL-A.8.16-S2.1

**Key Questions Answered:**
- What systems MUST be monitored?
- What log sources feed the monitoring infrastructure?
- What capabilities must monitoring tools provide?
- How is monitoring infrastructure deployed and maintained?

### 2.2.2 Baseline & Anomaly Detection Requirements (S2.2)

**Objective**: Establish measurable baselines for normal behavior and define how anomalies are detected.

**Scope**: Requirements for:
- Baseline establishment methodology (observation periods, data collection)
- Baseline documentation standards (metrics, thresholds, context)
- Baseline maintenance and updates (frequency, triggers, approval)
- Anomaly detection approaches (signature-based, behavior-based, statistical)
- Correlation rules and detection logic
- Threat intelligence integration
- False positive/negative management
- Detection effectiveness measurement

**Primary Stakeholders**: SOC, Security Engineering, Threat Intelligence  
**Detailed Requirements**: ISMS-POL-A.8.16-S2.2

**Key Questions Answered:**
- What does "normal" look like for each monitored system?
- How are baselines established and documented?
- How are anomalies detected?
- How is detection effectiveness measured?

**Feynman Test:**
*"If you cannot explain your baseline with measurable metrics, you don't have a baseline—you have a guess."*

### 2.2.3 Alert Management & Response Requirements (S2.3)

**Objective**: Define how security alerts are generated, triaged, investigated, and escalated.

**Scope**: Requirements for:
- Alert generation rules and severity classification
- Alert triage and prioritization procedures
- Response timeframes by severity level
- Escalation paths and handoff procedures
- Alert documentation and tracking
- False positive handling and tuning processes
- Integration with incident response (A.5.24-28)
- Performance metrics (MTTD, MTTR, false positive rate)

**Primary Stakeholders**: SOC, Incident Response Team, Security Engineering  
**Detailed Requirements**: ISMS-POL-A.8.16-S2.3

**Key Questions Answered:**
- How are alerts generated and classified?
- Who responds to alerts and within what timeframe?
- How are alerts escalated to incident response?
- How is alert effectiveness measured?

### 2.2.4 Retention & Archival Requirements (S2.4)

**Objective**: Ensure monitoring data is retained appropriately for security, compliance, and forensic purposes.

**Scope**: Requirements for:
- Retention periods by data type and regulatory requirement
- Storage infrastructure and capacity planning
- Data integrity and tamper-evidence controls
- Access controls for archived monitoring data
- Search and retrieval capabilities
- Long-term archival and deletion procedures
- Backup and disaster recovery for monitoring data
- Privacy considerations (anonymization, pseudonymization)

**Primary Stakeholders**: Security Team, IT Operations, Legal/Compliance  
**Detailed Requirements**: ISMS-POL-A.8.16-S2.4

**Key Questions Answered:**
- How long must monitoring data be retained?
- How is archived data protected from tampering?
- How can archived data be retrieved for investigations?
- How is monitoring data eventually deleted?

---

## 2.3 Risk-Based Approach

Monitoring requirements follow a risk-based methodology:

1. **Identify Assets**: Systems, networks, applications requiring monitoring based on criticality
2. **Assess Threats**: Attack vectors, insider threats, compliance violations relevant to the organization
3. **Define Baselines**: Establish measurable profiles of normal behavior for critical assets
4. **Implement Detection**: Deploy monitoring tools and configure detection logic
5. **Tune Continuously**: Reduce false positives, improve detection rates, update baselines
6. **Measure Effectiveness**: Validate detection capabilities through testing (red team, simulations)
7. **Review Periodically**: Reassess threats, baselines, and detection logic as environment evolves

Requirements are **not one-size-fits-all**. Organizations must:
- Prioritize monitoring based on asset criticality and threat exposure
- Balance detection capabilities with operational overhead (false positives, analyst workload)
- Comply with applicable legal and regulatory monitoring obligations
- Document risk-based decisions and trade-offs
- Accept residual risk where comprehensive monitoring is not feasible

**Example Risk-Based Decisions:**
- **Critical Systems**: Real-time monitoring, 24/7 SOC coverage, immediate alert escalation
- **Standard Systems**: Near-real-time monitoring, business hours SOC coverage, next-business-day triage
- **Low-Risk Systems**: Batch monitoring, periodic log reviews, no active alerting

All risk-based decisions MUST be documented with justification and approved by the CISO.

---

## 2.4 Technology Neutrality

All requirements in this framework are **vendor-agnostic** and **technology-independent**. Requirements specify:

- **Capabilities** that must be achieved (WHAT must be detected)
- **Outcomes** that must be demonstrated (evidence of detection effectiveness)

Requirements do **NOT** specify:
- Specific vendor products or SIEM platforms (HOW to implement)
- Implementation technologies or architectures
- Configuration parameters or detection rule syntax

Organizations may satisfy requirements using any technology solution(s) appropriate to their environment, provided the solution demonstrably meets stated requirements.

**Acceptable Approaches:**
- Commercial SIEM platform (Splunk, QRadar, ArcSight, etc.)
- Cloud-native solutions (AWS GuardDuty + CloudWatch, Azure Sentinel, Google Chronicle)
- Open-source SIEM (Elastic Stack, Wazuh, Graylog)
- Hybrid architectures combining multiple tools
- Managed SOC services with monitoring-as-a-service

The organization's choice depends on:
- Existing infrastructure and skill sets
- Budget and total cost of ownership
- Log volume and retention requirements
- Integration needs with other security controls
- Compliance requirements (data residency, audit trail)

---

## 2.5 Relationship to Implementation

Policy requirements (this document and S2.1-S2.4) define **WHAT** must be achieved. Implementation specifications (ISMS-IMP-A.8.16.x) define **HOW** compliance is assessed and demonstrated.

**Mapping**:

| Policy Section | Implementation Assessment | Purpose |
|----------------|--------------------------|---------|
| S2.1 (Monitoring Infrastructure) | IMP-A.8.16.1 | Document monitoring tools, log sources, and infrastructure capabilities |
| S2.2 (Baseline & Anomaly Detection) | IMP-A.8.16.2 | Document baselines, detection logic, and effectiveness metrics |
| S2.3 (Alert Management & Response) | IMP-A.8.16.4 | Document alert rules, response procedures, and performance metrics |
| S2.4 (Retention & Archival) | IMP-A.8.16.1 | Document retention policies and storage infrastructure |
| All Sections | IMP-A.8.16.3 | Verify monitoring coverage across assets (gap analysis) |
| All Sections | IMP-A.8.16.5 | Consolidated compliance dashboard and metrics |

Implementation assessments provide evidence that policy requirements are met, using quantifiable metrics and documented artifacts.

**Assessment Methodology:**
- Python scripts generate Excel workbooks for each domain
- Stakeholders document implementation status in workbooks
- Master dashboard consolidates all assessments
- Gaps are tracked and prioritized for remediation
- Evidence is maintained for audit purposes

---

## 2.6 Compliance Verification

Compliance with monitoring requirements shall be verified through:

- **Technical Assessments**: Evaluation of monitoring infrastructure, log sources, detection capabilities
- **Baseline Reviews**: Periodic verification that baselines are documented, current, and measurable
- **Detection Testing**: Red team exercises, attack simulations, injected test events to validate detection
- **Alert Analysis**: Review of alert volume, false positive rates, response times, escalation patterns
- **Coverage Analysis**: Verification that all critical assets are monitored per requirements
- **Retention Audits**: Verification that monitoring data is retained and protected per policy
- **Incident Reviews**: Post-incident analysis to identify monitoring gaps or detection failures
- **Third-Party Audits**: External validation during ISO 27001 certification audits

Evidence of compliance shall be documented in implementation assessment workbooks (ISMS-IMP-A.8.16.x) and retained per organizational record retention policies.

**Audit Artifacts:**
- Baseline documentation for critical systems
- Detection rule repository with change history
- Alert metrics (volume, false positive rate, MTTD, MTTR)
- Test results from red team exercises
- Incident reports demonstrating detection effectiveness
- Log retention and archival configurations
- Coverage gap analysis and remediation plans

---

## 2.7 Requirement Prioritization

Where resource constraints prevent simultaneous implementation of all requirements, organizations should prioritize:

### Critical (Must Implement):
- Monitoring of critical systems and high-risk assets (S2.1)
- Basic baseline establishment for critical systems (S2.2)
- Alert generation for high-severity threats (S2.3)
- Minimum retention for regulatory compliance (S2.4)

### Important (Should Implement):
- Comprehensive log source coverage (S2.1)
- Documented baselines with regular updates (S2.2)
- Structured alert triage and response procedures (S2.3)
- Extended retention for forensic analysis (S2.4)

### Beneficial (May Implement):
- Advanced correlation and behavior analytics (S2.2)
- Automated response and orchestration (S2.3)
- Long-term archival for trend analysis (S2.4)
- Integration with threat intelligence platforms (S2.2)

Prioritization decisions must be documented with risk justification and approved by the CISO.

**Minimum Viable Monitoring (MVM):**
For organizations starting from scratch, the absolute minimum is:
1. Log collection from critical systems
2. Real-time alerting on critical threats (malware detection, privilege escalation, data exfiltration attempts)
3. 24/7 alert monitoring (even if outsourced to MSSP)
4. 90-day log retention
5. Documented response procedures for critical alerts

This MVM provides basic detection capability. Organizations MUST have a roadmap to achieve full compliance within 12-24 months.

---

## 2.8 Integration with Related Controls

Monitoring activities (A.8.16) integrate tightly with other ISMS controls:

### Upstream Dependencies (Monitoring Consumes These):
- **A.8.15 (Logging)**: Monitoring analyzes logs generated by logging controls
- **A.5.7 (Threat Intelligence)**: Threat intelligence informs detection rules and IOC feeds
- **A.8.23 (Web Filtering)**: Web filtering logs feed into monitoring infrastructure
- **A.8.8 (Vulnerability Management)**: Monitoring detects exploitation of known vulnerabilities

### Downstream Dependencies (Monitoring Feeds These):
- **A.5.24-28 (Incident Management)**: Monitoring alerts trigger incident response
- **A.8.15 (Logging)**: Monitoring generates its own logs requiring retention
- **A.5.7 (Threat Intelligence)**: Monitoring generates intelligence (observed attack patterns)

### Lateral Integration:
- **A.5.36 (Compliance)**: Monitoring provides evidence for compliance audits
- **A.5.26 (Learning from Incidents)**: Monitoring data enables post-incident analysis

**Critical Note:** Monitoring is NOT a standalone control. It requires effective logging (A.8.15) as input and effective incident response (A.5.24-28) as output. A monitoring system that doesn't feed incident response is just expensive data storage.

---

## 2.9 Document Structure

The complete Monitoring Activities Requirements framework consists of:

- **ISMS-POL-A.8.16-S2.md** - This overview document
- **ISMS-POL-A.8.16-S2.1.md** - Monitoring Infrastructure Requirements
- **ISMS-POL-A.8.16-S2.2.md** - Baseline & Anomaly Detection Requirements
- **ISMS-POL-A.8.16-S2.3.md** - Alert Management & Response Requirements
- **ISMS-POL-A.8.16-S2.4.md** - Retention & Archival Requirements

Each section is independently versionable. Changes to one section do not require re-approval of other sections unless dependencies exist.

---

## 2.10 Key Success Factors

Effective monitoring requires more than deploying tools. Success depends on:

**People:**
- Skilled SOC analysts capable of triaging alerts
- Security engineers who can tune detection logic
- Incident responders who act on monitoring outputs
- Management support and adequate resourcing

**Process:**
- Documented baselines updated regularly
- Clear alert response procedures
- Structured tuning process to reduce false positives
- Regular testing to validate detection effectiveness

**Technology:**
- Monitoring tools with adequate log source coverage
- Scalable infrastructure for log volume
- Integration with incident response workflows
- Automated correlation to reduce analyst burden

**Culture:**
- Recognition that monitoring is continuous, not one-time
- Willingness to invest in tuning and baseline maintenance
- Acceptance that some false positives are inevitable
- Commitment to acting on alerts (not just collecting logs)

**Anti-Patterns to Avoid:**
- ❌ "Set it and forget it" - Monitoring requires continuous tuning
- ❌ "Log everything" - Unfocused log collection overwhelms analysts
- ❌ "Alert on everything" - High false positive rates cause alert fatigue
- ❌ "Someone will look at it eventually" - Alerts require timely response

---

**END OF DOCUMENT**

---

## Related Documents in Framework

- **ISMS-POL-A.8.16-S1** (Purpose, Scope, Definitions) - Foundation and terminology
- **ISMS-POL-A.8.16-S2.1** (Infrastructure) - Detailed monitoring infrastructure requirements
- **ISMS-POL-A.8.16-S2.2** (Baselines & Detection) - Detailed baseline and anomaly detection requirements
- **ISMS-POL-A.8.16-S2.3** (Alert Management) - Detailed alert response requirements
- **ISMS-POL-A.8.16-S2.4** (Retention) - Detailed retention and archival requirements
- **ISMS-POL-A.8.16-S3** (Roles) - RACI matrix and accountability
- **ISMS-POL-A.8.16-S4** (Governance) - Policy lifecycle and updates
- **ISMS-POL-A.8.16-S5** (Annexes) - Templates and procedures

---

*"You can't manage what you don't measure. You can't measure what you don't monitor. You can't monitor what you don't baseline."*  
*—Systems Engineering Wisdom (probably someone famous)*