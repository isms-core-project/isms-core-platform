**ISMS-POL-A.5.19-23-S4 — Supplier Monitoring & Change Management**
**Control A.5.22: Monitoring, Review and Change Management of Supplier Services**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Supplier Monitoring & Change Management |
| **Document Type** | Policy Section |
| **Document ID** | ISMS-POL-A.5.19-23-S4 |
| **Document Creator** | Information Security Officer (ISO) |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Approved By** | Executive Management |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | ISO | Initial section for ISO 27001:2022 Control A.5.22 |

**Review Cycle**: Annual  
**Next Review Date**: [Effective Date + 12 months]  

**Approval Chain**:

- Primary: Chief Information Security Officer (CISO)
- Secondary: Information Security Officer (ISO)
- Compliance: Legal/Compliance Officer
- Operations: Chief Information Officer (CIO)
- Final Authority: Executive Management (GL)

**Related Documents**: 

- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-POL-A.5.19-23 (Parent Policy - Supplier & Cloud Services Security)
- ISMS-POL-A.5.19-23-S1 (Supplier Relationship Fundamentals)
- ISMS-IMP-A.5.23-4-UG/TG (Ongoing Governance & Risk Management)
- ISMS-REF-A.5.23 (Cloud Service Provider Registry)
- ISO/IEC 27001:2022 Control A.5.22
- ISO/IEC 27036-4 (Cloud services)

---

# Purpose

This section defines requirements for ongoing monitoring, periodic review, and change management of supplier services. It ensures that supplier security posture is continuously validated and that changes do not introduce unacceptable risks.

**Critical Principle - "Trust Degrades Over Time"**: A supplier that passed initial due diligence is not guaranteed to remain secure. Certifications expire, security practices drift, ownership changes, and incidents occur. Continuous monitoring and periodic reassessment are not optional oversight - they are essential controls that detect degradation before it becomes breach. This policy requires systematic, evidence-based validation throughout the supplier relationship lifecycle.

**ISO/IEC 27001:2022 Control A.5.22 - Monitoring, Review and Change Management of Supplier Services**

> *The organization should regularly monitor, review, evaluate and manage change in supplier information security practices and service delivery.*

**Control Objective**: Ensure ongoing validation of supplier security posture and controlled management of changes to supplier services.

**ISO/IEC 27002:2022 Guidance Summary**:

- Supplier performance shall be monitored continuously against contractual commitments and SLAs
- Periodic reviews of supplier security practices shall be conducted based on supplier risk classification
- Changes to supplier services shall be managed through formal change control procedures with security review
- Supplier compliance with agreements shall be verified through audits, attestations, or third-party certifications
- Supplier incidents and security events shall be tracked, analyzed, and responded to appropriately
- Supplier audits or third-party attestations (SOC 2, ISO 27001) shall be obtained and reviewed for findings
- Relationship with suppliers shall be maintained through regular communication, reviews, and governance meetings
- Supplier service degradation or non-compliance shall trigger escalation and remediation procedures including potential termination

---

# Scope

## Monitoring Activities

| Activity Type | Description |
|---------------|-------------|
| **Performance monitoring** | SLA compliance, service quality metrics, availability tracking |
| **Security monitoring** | Security posture assessment, incident tracking, vulnerability status, certification validity |
| **Compliance monitoring** | Certification validity, regulatory compliance verification, audit report review |
| **Relationship monitoring** | Communication effectiveness, issue resolution, stakeholder satisfaction |
| **Change monitoring** | Service changes, personnel changes, ownership changes, infrastructure modifications |

## Applicability by Supplier Level

| Activity | Level 1 (Critical) | Level 2 (High) | Level 3 (Medium) | Level 4 (Low) |
|----------|-------------------|----------------|------------------|---------------|
| Performance monitoring | Continuous (automated) | Monthly reporting | Quarterly | Annual |
| Security assessment | Annual comprehensive | Annual standard | Biennial | Initial only |
| Compliance verification | Quarterly cert check | Semi-annual | Annual | At renewal |
| Relationship review | Quarterly governance | Semi-annual | Annual | As needed |
| Change review | All changes pre-approved | Material changes reviewed | Significant only | Standard terms |

---

# Review Cycles

## Review Schedule by Supplier Level

| Supplier Level | Security Review | Performance Review | Relationship Review |
|----------------|-----------------|--------------------|--------------------|
| **Level 1 (Critical)** | Annual comprehensive + continuous monitoring | Monthly SLA reports | Quarterly governance meetings |
| **Level 2 (High)** | Annual standard assessment | Quarterly performance review | Semi-annual relationship check |
| **Level 3 (Medium)** | Biennial security questionnaire | Semi-annual | Annual review |
| **Level 4 (Low)** | At renewal only | Annual summary | At renewal only |

## Unscheduled Review Triggers

Beyond scheduled reviews, conduct immediate review upon:

| Trigger | Review Scope | Timeline |
|---------|--------------|----------|
| Security incident involving supplier (confirmed) | Full security review, contract compliance | Within 48 hours |
| Significant service change (architecture, platform, location) | Impact assessment, risk reassessment | Before implementation |
| Supplier ownership change (M&A, acquisition) | Due diligence refresh, contract review | Within 30 days |
| Certification expiry or loss | Compliance review, risk assessment | Immediate |
| Material contract change or amendment | Security clause verification, impact analysis | Before execution |
| Regulatory change affecting supplier obligations | Compliance assessment, gap analysis | Within 60 days |
| Negative news or reputation event (public incident) | Risk reassessment, communication with supplier | Within 7 days |
| Significant organizational change ([Organization] or supplier) | Relationship review, access validation | Within 30 days |
| Repeated SLA failures (3 consecutive or 6 in 12 months) | Performance review, remediation plan | Immediate |
| Audit finding related to supplier | Compliance review, remediation tracking | Within 14 days |

## Annual Review Calendar

```
┌─────────────────────────────────────────────────────────────┐
│ SUPPLIER REVIEW CALENDAR (Example)                          │
├─────────────────────────────────────────────────────────────┤
│ Q1 (Jan-Mar):                                               │
│     • Level 1 suppliers - Annual security assessment        │
│     • All suppliers - Certification validity verification   │
│     • Contract renewals (Q1 expirations)                    │
│                                                             │
│ Q2 (Apr-Jun):                                               │
│     • Level 2 suppliers - Annual security assessment        │
│     • Level 1 suppliers - Quarterly governance meeting      │
│     • Mid-year compliance check                             │
│                                                             │
│ Q3 (Jul-Sep):                                               │
│     • Level 1 suppliers - Quarterly governance meeting      │
│     • Level 3 suppliers - Annual review (if due this year)  │
│     • Preparation for year-end reporting                    │
│                                                             │
│ Q4 (Oct-Dec):                                               │
│     • Level 1 suppliers - Quarterly governance meeting      │
│     • All suppliers - Annual register validation            │
│     • Planning for next year's review cycle                 │
│     • Year-end compliance reporting                         │
└─────────────────────────────────────────────────────────────┘
```

---

# Performance Monitoring

## Service Level Monitoring

| Metric Category | Examples | Monitoring Frequency | Alert Threshold |
|-----------------|----------|---------------------|-----------------|
| Availability | Uptime percentage, unplanned downtime incidents | Continuous/Real-time | Below SLA target |
| Performance | Response time, throughput, latency | Continuous/Real-time | >10% degradation |
| Support | Ticket response time, resolution time, escalations | Weekly aggregation | SLA breach |
| Capacity | Resource utilization, scalability headroom | Monthly trend analysis | >80% utilization |
| Quality | Error rates, transaction success rate, customer satisfaction | Monthly review | Above baseline |

## SLA Compliance Tracking

| Element | Requirement |
|---------|-------------|
| Baseline establishment | Document agreed SLA targets in contract and monitoring system |
| Measurement methodology | Track actual performance against targets using objective metrics |
| Reporting cadence | Monthly SLA compliance reports from supplier with supporting data |
| Breach tracking | Log all SLA breaches with root cause, impact assessment, remediation |
| Service credits | Track and claim service credits per contract terms for SLA failures |
| Trend analysis | Monitor for degradation patterns indicating systematic issues |
| Escalation triggers | Define thresholds for escalation (e.g., 3 breaches in quarter) |

## Performance Review Process

**For Level 1 & 2 Suppliers:**

1. **Data Collection**: Gather supplier-provided reports + internal monitoring data
2. **SLA Comparison**: Compare actual performance against contractual SLA targets
3. **Trend Analysis**: Identify patterns, degradation trends, anomalies
4. **Issue Documentation**: Document SLA breaches, performance issues, remediation requests
5. **Review Meeting**: Discuss findings in quarterly/semi-annual supplier review
6. **Remediation Tracking**: Track supplier commitments and verify completion
7. **Risk Update**: Update supplier risk assessment if performance indicates increased risk
8. **Contract Review**: Assess whether performance justifies contract renewal or renegotiation

---

# Security Assessment

## Assessment Methods

| Method | Description | Applicability |
|--------|-------------|---------------|
| **Security questionnaire** | Standardized assessment (200-300 questions for L1) | All suppliers with data/system access |
| **Evidence review** | Review of policies, procedures, configurations, logs | Level 1 & 2 |
| **Certification review** | Verify valid ISO 27001, SOC 2, etc. | Level 1, 2, 3 (if applicable) |
| **Audit report review** | Detailed review of SOC 2 Type II, ISO surveillance audit results | Level 1 & 2 (required) |
| **Penetration test review** | Review supplier's external pen test results | Level 1 (required annually) |
| **Vulnerability assessment review** | Review supplier's vulnerability scan results | Level 1 (required quarterly) |
| **On-site assessment** | Physical visit and inspection of facilities/controls | Level 1 (risk-based, every 2-3 years) |
| **Technical security testing** | Independent vulnerability scans of supplier-exposed interfaces | Level 1 (risk-based) |

## Assessment Content Domains

| Domain | Assessment Areas |
|--------|------------------|
| **Governance & Organization** | Security policies, organizational structure, roles and responsibilities, security awareness training |
| **Access Control** | Authentication mechanisms, authorization models, privileged access management, access review processes |
| **Data Protection** | Data classification, encryption (transit & rest), data handling procedures, data loss prevention |
| **Operations Security** | Change management, patch management, configuration management, backup and recovery, capacity management |
| **Incident Management** | Detection capabilities, response procedures, notification processes, post-incident reviews |
| **Business Continuity** | BC/DR plans, testing evidence, RTO/RPO capabilities, geographic redundancy |
| **Compliance** | Current certifications, regulatory compliance evidence, audit findings remediation, contractual compliance |
| **Supply Chain** | Sub-supplier management, software dependencies (SBOM), vulnerability management |

## Assessment Findings Management

| Finding Severity | Description | Response Timeline | Escalation Path |
|------------------|-------------|-------------------|-----------------|
| **Critical** | Data breach risk, missing critical controls, expired encryption | Immediate mitigation plan, 7 days remediation | CISO + Business Owner + Executive Management |
| **High** | Material control gaps, SLA violations, partial compliance | 30 days remediation with weekly progress updates | ISO + Business Owner + CISO notification |
| **Medium** | Control improvements needed, documentation gaps, minor non-compliance | 90 days remediation with monthly updates | ISO + Business Owner |
| **Low** | Best practice recommendations, documentation enhancements | Next review cycle or 6 months | Tracked in assessment record |

**Finding Tracking**: All findings shall be logged in supplier management system with:

- Finding description and evidence
- Severity classification
- Supplier remediation plan and timeline
- Verification method and criteria
- Status tracking (Open → In Progress → Verified → Closed)
- Closure evidence

## Assessment Documentation

Each assessment shall produce comprehensive documentation:

| Document | Content | Retention |
|----------|---------|-----------|
| **Assessment report** | Scope, methodology, findings with evidence, supplier responses | 5 years |
| **Risk rating update** | Updated supplier risk score based on assessment findings | Current + 3 years |
| **Remediation plan** | Actions required, assigned owners, timelines, verification method | Until closure + 2 years |
| **Management summary** | Executive overview for governance review meetings | 3 years |
| **Compliance evidence** | Certifications, audit reports, test results reviewed | Current + 3 years |

---

# Compliance Monitoring

## Certification Tracking

| Activity | Frequency | Action on Expiry/Failure |
|----------|-----------|--------------------------|
| ISO 27001 validity check | Quarterly | Request renewal evidence within 30 days, escalate to CISO if lapsed >60 days |
| SOC 2 Type II currency | Annual request (30 days before anniversary) | Request new report, conduct gap risk assessment if delayed |
| Cloud certifications (ISO 27017/27018, CSA STAR) | Annual | Verify renewal, assess impact if discontinued |
| Regulatory compliance attestations | Annual | Request confirmation letter from supplier management |
| Penetration testing | Annual | Request current report (<12 months), verify critical findings resolved |

## Compliance Evidence Requirements

| Supplier Level | Evidence Required | Verification Method |
|----------------|-------------------|---------------------|
| **Level 1** | Valid certification + full audit report + remediation evidence for all findings | Detailed review, verify finding closure |
| **Level 2** | Valid certification + audit report summary or executive summary | Review for material findings, verify critical items closed |
| **Level 3** | Valid certification (if claimed in due diligence) | Certificate verification only |
| **Level 4** | None required | N/A |

**Certificate Verification**: All certifications shall be verified with issuing body:

- ISO 27001: Check IAF/accreditation body database
- SOC 2: Verify CPA firm license, request AICPA confirmation if needed
- Industry certifications: Verify with certification authority

## Compliance Failure Response

| Scenario | Immediate Action | Timeline | Escalation |
|----------|-----------------|----------|------------|
| Certification lapsed (recently expired) | 30-day cure period, risk assessment, compensating controls | Supplier must renew within 30 days | Business Owner + ISO |
| Certification withdrawn or revoked | Immediate risk assessment, consider service suspension pending renewal | 14 days to resolve or initiate replacement | CISO + Business Owner |
| Failed audit (material findings unresolved) | Review findings, require remediation plan with timeline | 30 days remediation plan, 90 days execution | ISO + Business Owner |
| Regulatory violation or sanction | Legal review, assess [Organization] exposure, document risk acceptance or exit strategy | Immediate legal consult | Legal + CISO + Executive Management |
| Repeated non-compliance (3+ incidents) | Formal performance improvement plan or contract termination initiation | 60 days improvement or transition planning | CISO + Executive Management |

---

# Change Management

## Change Categories

| Change Type | Description | Notification Required | Approval Required |
|-------------|-------------|----------------------|-------------------|
| **Service changes** | Features, functionality, APIs, interfaces | Prior notification (30 days L1, 14 days L2) | Material changes (L1) |
| **Infrastructure changes** | Platform migration, data center relocation, architecture redesign | Prior approval (L1), prior notification (L2) | L1: Yes, L2: If data location change |
| **Security changes** | Security controls, encryption methods, access mechanisms, authentication | Prior notification (L1-L2) | Material security changes (L1) |
| **Personnel changes** | Key contacts, account managers, security personnel | Timely notification (within 14 days) | No |
| **Ownership changes** | Acquisition, merger, divestiture, change of control | Immediate notification (within 48 hours) | L1: Yes, L2: Notification + risk review |
| **Sub-supplier changes** | New or changed sub-suppliers with data access | Prior approval (L1), prior notification (L2) | L1: Yes, L2: If data access |
| **Contractual changes** | Terms, pricing, SLAs, data processing terms | Per contract amendment process | Per contract (typically yes) |
| **Regulatory/compliance changes** | Loss of certification, regulatory sanctions, compliance failures | Immediate notification | Risk assessment required |

## Change Notification Requirements

| Supplier Level | Standard Notification | Material Change Approval |
|----------------|----------------------|--------------------------|
| **Level 1** | 30 days advance notice for all changes | Written approval required for material changes before implementation |
| **Level 2** | 14 days advance notice for material changes | Notification sufficient, [Organization] may object within 7 days |
| **Level 3** | Timely notification of significant changes (7 days) | Standard contract terms apply |
| **Level 4** | Standard contract terms apply | No specific requirement |

## Change Review Process

```
┌─────────────────────────────────────────────────────────────┐
│ SUPPLIER CHANGE REVIEW PROCESS                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. Supplier notifies [Organization] of planned change      │
│     • Change description and business justification         │
│     • Implementation timeline                               │
│     • Impact assessment (supplier's view)                   │
│                         ↓                                   │
│  2. Log change in supplier change register                  │
│     • Assign change request ID                              │
│     • Route to appropriate reviewer (Security/IT/Business)  │
│                         ↓                                   │
│  3. [Organization] assesses change impact                   │
│     • Security impact (controls, risks, vulnerabilities)    │
│     • Operational impact (service delivery, integration)    │
│     • Compliance impact (regulatory, contractual)           │
│     • Business impact (cost, schedule, functionality)       │
│                         ↓                                   │
│  4. Determine response decision                             │
│     • APPROVE: No concerns, proceed as planned              │
│     • APPROVE WITH CONDITIONS: Additional controls/testing  │
│     • REQUEST MODIFICATION: Changes needed before approval  │
│     • REJECT: Unacceptable risk (negotiate alternative)     │
│                         ↓                                   │
│  5. Communicate decision to supplier (within SLA)           │
│     • Decision with rationale                               │
│     • Conditions or requirements if applicable              │
│     • Updated timeline if modified                          │
│                         ↓                                   │
│  6. Update documentation                                    │
│     • Risk assessment (if risk profile changes)             │
│     • Supplier register (record change)                     │
│     • Contract amendments (if applicable)                   │
│                         ↓                                   │
│  7. Verify implementation (post-change)                     │
│     • Confirm change completed as approved                  │
│     • Validate no unexpected impacts                        │
│     • Close change request                                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

## Material Change Definition

A change is considered **material** if it meets any of the following criteria:

**Security-Related**:

- Affects security controls protecting [Organization]'s data
- Changes encryption methods, key management, or authentication mechanisms
- Modifies access control architecture or privileged access procedures
- Introduces new attack surface or expands existing attack vectors

**Data-Related**:

- Changes data processing location or jurisdiction (especially EU/CH to non-adequate country)
- Modifies data retention, backup, or disaster recovery procedures
- Changes data handling processes or introduces new data flows
- Affects data subject rights exercise or GDPR/nDSG compliance

**Compliance-Related**:

- Impacts compliance with regulatory requirements (DORA, NIS2, GDPR)
- Introduces new sub-suppliers with access to [Organization] data
- Changes certification scope or causes certification lapse
- Affects contractual security obligations

**Service-Related**:

- Significantly alters service architecture or technology stack
- Changes service availability, performance, or capacity
- Modifies SLA commitments or introduces new dependencies
- Affects business continuity or disaster recovery capabilities

**Corporate-Related**:

- Changes ownership or control of supplier entity
- Triggers change-of-control provisions in contract
- Affects supplier's ability to perform contractual obligations

---

# Relationship Governance

## Governance Structure by Supplier Level

| Supplier Level | Governance Model | Meeting Frequency | Participants |
|----------------|------------------|-------------------|--------------|
| **Level 1 (Critical)** | Formal governance committee with documented charter | Quarterly | [Organization]: Business Owner, ISO, IT; Supplier: Account Manager, Technical Lead, Security |
| **Level 2 (High)** | Regular business reviews with security component | Semi-annual | [Organization]: Business Owner, ISO; Supplier: Account Manager |
| **Level 3 (Medium)** | Periodic check-ins as needed | Annual | [Organization]: Business Owner; Supplier: Account Manager |
| **Level 4 (Low)** | Transactional relationship | As needed | Per transaction |

## Level 1 Quarterly Governance Meeting Agenda

| Agenda Item | Led By | Time Allocation |
|-------------|--------|-----------------|
| **Performance review** | Business Owner | 15 minutes |
| **SLA compliance & service quality** | IT Operations | 15 minutes |
| **Security posture update** | ISO | 20 minutes |
| **Incident review** (if any) | ISO / Business Owner | 10 minutes |
| **Change requests & roadmap** | Supplier | 15 minutes |
| **Compliance status** (certifications, audits) | ISO | 10 minutes |
| **Issues, risks, and escalations** | Business Owner | 15 minutes |
| **Action item review** | All | 10 minutes |

**Meeting Documentation**: Minutes shall be documented including decisions, action items with owners and due dates, and escalations.

## Escalation Procedures

| Issue Type | Level 1 Escalation | Level 2 Escalation | Level 3 Escalation |
|------------|-------------------|-------------------|-------------------|
| **Service degradation** | Business Owner | IT Management | CIO |
| **Security concern** | ISO | CISO | Executive Management |
| **Compliance violation** | ISO | CISO + Legal | Executive Management |
| **Contract dispute** | Procurement | Legal | Executive Management |
| **Relationship breakdown** | Business Owner | CIO/CISO | Executive Management |
| **Financial issue** (billing disputes) | Business Owner | Finance | CFO |

**Escalation Documentation**: All escalations shall be documented with issue description, escalation path taken, resolution, and timeline.

---

# Incident Review

## Supplier Incident Categories

| Category | Examples | Severity Indicators |
|----------|----------|---------------------|
| **Security incidents** | Data breach, unauthorized access, malware infection, credential compromise | Data exposure, system compromise, regulatory notification requirement |
| **Service incidents** | Unplanned outage, significant degradation, data loss, corruption | Duration, user impact, SLA breach severity |
| **Compliance incidents** | Certification loss, regulatory violation, audit failure | Regulatory impact, contractual breach, reputational risk |
| **Supply chain incidents** | Sub-supplier breach, software vulnerability (Log4Shell-style), dependency compromise | Cascading impact, widespread exposure, remediation complexity |
| **Near misses** | Potential incidents prevented, close calls | Learning opportunity, control validation |

## Incident Review Process

| Step | Activity | Timeline | Responsible |
|------|----------|----------|-------------|
| **1. Notification** | Receive incident notification from supplier per contract terms | Per SLA (4-48 hours) | Supplier → ISO |
| **2. Logging** | Log incident in supplier incident register with initial assessment | Within 4 hours | ISO |
| **3. Impact Assessment** | Assess impact on [Organization] (data, systems, compliance, business) | Within 24 hours | ISO + Business Owner |
| **4. Containment Verification** | Verify supplier has contained incident, assess residual risk | Within 48 hours | ISO |
| **5. Root Cause Analysis** | Request and review supplier's RCA | Within 30 days | Supplier provides, ISO reviews |
| **6. Remediation Review** | Review supplier's remediation actions and preventive measures | Within 60 days | ISO |
| **7. Risk Reassessment** | Update supplier risk assessment if incident indicates control weakness | Within 30 days post-closure | ISO |
| **8. Lessons Learned** | Document lessons learned, update policies/procedures if needed | Within 90 days | ISO + IT |
| **9. Contract Review** | Assess contractual compliance (notification timeliness, cooperation) | Post-incident | Legal + ISO |

## Post-Incident Requirements by Supplier Level

| Supplier Level | Post-Incident Documentation Required |
|----------------|-------------------------------------|
| **Level 1** | Full root cause analysis, detailed timeline, complete remediation plan, verification evidence, lessons learned document, 3rd party forensics (if breach) |
| **Level 2** | Root cause analysis summary, remediation confirmation, high-level timeline, key findings and corrective actions |
| **Level 3** | Incident summary, confirmation of resolution, basic corrective actions |
| **Level 4** | Incident notification and closure confirmation |

**Incident-Triggered Reviews**: Security incidents shall trigger:

- Immediate security reassessment if Critical or High severity
- Contract compliance review (notification timelines, cooperation obligations)
- Potential re-classification of supplier risk level
- Consideration of termination rights if material breach

---

# Documentation & Reporting

## Required Documentation

| Document Type | Update Trigger | Retention Period | Storage Location |
|---------------|----------------|------------------|------------------|
| **Supplier register** | Upon any change | Current + 3 years | Supplier management system |
| **Assessment reports** | Per scheduled/triggered assessment | 5 years | Document management system |
| **Review meeting minutes** | Per governance meeting | 3 years | Supplier folder |
| **Incident records** | Upon incident occurrence | 5 years | Incident management system |
| **Change records** | Upon change request | 3 years | Change management system |
| **SLA reports** | Per reporting period (monthly/quarterly) | 3 years | Performance monitoring system |
| **Compliance certificates** | Upon receipt/renewal | Current + 2 years | Compliance repository |
| **Audit findings** | Upon assessment | Until closure + 3 years | Supplier management system |

## Management Reporting

| Report | Frequency | Audience | Content |
|--------|-----------|----------|---------|
| **Supplier risk summary** | Quarterly | CISO, CIO, Management | Overall supplier risk landscape, high-risk suppliers, trends |
| **Critical supplier status** | Monthly | ISO, Business Owners | Level 1 supplier performance, issues, changes |
| **Incident summary** | Quarterly | CISO, Compliance | Supplier security incidents, impact, remediation status |
| **Compliance status** | Quarterly | ISO, Compliance | Certification validity, compliance findings, gaps |
| **Performance dashboard** | Continuous | Business Owners, IT | SLA compliance, service quality, availability |
| **Annual supplier review** | Annually | Executive Management | Comprehensive supplier portfolio review, strategic recommendations |

## Regulatory Reporting (Where Applicable)

**DORA-Covered Services**:

- Maintain ICT third-party risk register with quarterly updates
- Report material changes to ICT third-party arrangements to competent authority
- Document concentration risk assessments annually

**NIS2-Covered Services**:

- Include supplier incidents in regulatory incident reporting (24-hour early warning)
- Document supply chain security measures in annual cybersecurity report
- Maintain evidence of supplier security requirements and verification

---

# References

| Document | Relationship |
|----------|--------------|
| **ISMS-POL-A.5.19-23** | Parent policy framework |
| **ISMS-POL-A.5.19-23-S1** | Supplier classification determines monitoring frequency |
| **ISMS-POL-A.5.19-23-S2** | Contract terms being monitored for compliance |
| **ISMS-POL-A.5.19-23-S3** | Sub-supplier monitoring requirements |
| **ISMS-IMP-A.5.23-4-UG/TG** | Operational governance assessment workbook |
| **ISO/IEC 27036-4:2016** | Information security for supplier relationships - Cloud services |

---

**Next Document:** ISMS-POL-A.5.19-23-S5 — Cloud Services Security (Control A.5.23)

---

*"Monitoring without action is just expensive watching. Action without monitoring is blind faith."*
<!-- QA_VERIFIED: 2026-02-01 -->
