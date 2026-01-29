# ISMS-POL-A.5.19-23-S4 — Supplier Monitoring & Change Management
## Control A.5.22: Monitoring, Review and Change Management of Supplier Services

---

## Document Control

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
- ISMS-IMP-A.5.23-4 (Ongoing Governance & Risk Management)
- ISO/IEC 27001:2022 Control A.5.22
- ISO/IEC 27036-4 (Cloud services)

---

## 1. Purpose

This section defines requirements for ongoing monitoring, periodic review, and change management of supplier services. It ensures that supplier security posture is continuously validated and that changes do not introduce unacceptable risks.

**Control Objective (ISO 27002:2022):**
> "The organization shall regularly monitor, review, evaluate and manage change in supplier information security practices and service delivery."

---

## 2. Scope

### 2.1 Monitoring Activities

| Activity Type | Description |
|---------------|-------------|
| **Performance monitoring** | SLA compliance, service quality metrics |
| **Security monitoring** | Security posture, incident tracking, vulnerability status |
| **Compliance monitoring** | Certification validity, regulatory compliance |
| **Relationship monitoring** | Communication effectiveness, issue resolution |
| **Change monitoring** | Service changes, personnel changes, ownership changes |

### 2.2 Applicability by Supplier Level

| Activity | Level 1 | Level 2 | Level 3 | Level 4 |
|----------|---------|---------|---------|---------|
| Performance monitoring | Continuous | Monthly | Quarterly | Annual |
| Security assessment | Annual | Annual | Biennial | Initial only |
| Compliance verification | Quarterly | Semi-annual | Annual | — |
| Relationship review | Quarterly | Semi-annual | Annual | As needed |
| Change review | All changes | Material changes | Significant only | — |

---

## 3. Review Cycles

### 3.1 Review Schedule by Supplier Level

| Supplier Level | Security Review | Performance Review | Relationship Review |
|----------------|-----------------|--------------------|--------------------|
| **Level 1 (Critical)** | Annual comprehensive | Monthly | Quarterly |
| **Level 2 (High)** | Annual standard | Quarterly | Semi-annual |
| **Level 3 (Medium)** | Biennial | Semi-annual | Annual |
| **Level 4 (Low)** | At renewal only | Annual | At renewal |

### 3.2 Review Triggers (Unscheduled)

Beyond scheduled reviews, conduct review upon:

| Trigger | Review Scope |
|---------|--------------|
| Security incident involving supplier | Full security review |
| Significant service change | Impact and risk assessment |
| Supplier ownership change | Due diligence refresh |
| Certification expiry or loss | Compliance and risk review |
| Material contract change | Security clause verification |
| Regulatory change affecting supplier | Compliance assessment |
| Negative news or reputation event | Risk reassessment |
| Significant organizational change | Relationship and risk review |

### 3.3 Annual Review Calendar

```
┌─────────────────────────────────────────────────────────────────┐
│ SUPPLIER REVIEW CALENDAR (Example)                              │
├─────────────────────────────────────────────────────────────────┤
│ Q1: Level 1 suppliers - Full security assessment                │
│     All suppliers - Certification validity check                │
│                                                                 │
│ Q2: Level 2 suppliers - Security assessment                     │
│     Level 1 suppliers - Quarterly relationship review           │
│                                                                 │
│ Q3: Level 1 suppliers - Quarterly relationship review           │
│     Level 3 suppliers - Annual review (if due)                  │
│                                                                 │
│ Q4: Level 1 suppliers - Quarterly relationship review           │
│     All suppliers - Annual register validation                  │
│     Planning for next year's review cycle                       │
└─────────────────────────────────────────────────────────────────┘
```

---

## 4. Performance Monitoring

### 4.1 Service Level Monitoring

| Metric Category | Examples | Monitoring Frequency |
|-----------------|----------|---------------------|
| Availability | Uptime percentage, planned downtime | Continuous/Daily |
| Performance | Response time, throughput | Continuous/Daily |
| Support | Ticket response time, resolution time | Weekly |
| Capacity | Resource utilization, scalability | Monthly |
| Quality | Error rates, customer satisfaction | Monthly |

### 4.2 SLA Compliance Tracking

| Element | Requirement |
|---------|-------------|
| Baseline | Document agreed SLA targets |
| Measurement | Track actual performance against targets |
| Reporting | Regular SLA compliance reports from supplier |
| Breach tracking | Log and escalate SLA breaches |
| Credits | Track and claim service credits if applicable |
| Trending | Monitor for degradation patterns |

### 4.3 Performance Review Process

**Level 1 & 2 Suppliers:**

1. Collect performance data (supplier reports + internal metrics)
2. Compare against SLA targets
3. Identify trends and anomalies
4. Document issues and remediation requests
5. Discuss in supplier review meeting
6. Track remediation to completion
7. Update risk assessment if warranted

---

## 5. Security Assessment

### 5.1 Assessment Methods

| Method | Description | Applicability |
|--------|-------------|---------------|
| **Security questionnaire** | Standardized assessment questions | All suppliers with data access |
| **Evidence review** | Review of policies, configs, logs | Level 1 & 2 |
| **Certification review** | Verify valid certifications | Level 1, 2, 3 |
| **Audit report review** | Review SOC 2, ISO 27001 reports | Level 1 & 2 |
| **Penetration test review** | Review supplier's pen test results | Level 1 |
| **On-site assessment** | Physical visit and inspection | Level 1 (risk-based) |
| **Technical testing** | Vulnerability scans of interfaces | Level 1 (risk-based) |

### 5.2 Assessment Content

| Domain | Assessment Areas |
|--------|------------------|
| **Governance** | Policies, roles, training, awareness |
| **Access control** | Authentication, authorization, access review |
| **Data protection** | Classification, encryption, handling |
| **Operations** | Change management, patching, backup |
| **Incident management** | Detection, response, notification |
| **Business continuity** | BC/DR plans, testing, recovery capabilities |
| **Compliance** | Certifications, regulatory, contractual |

### 5.3 Assessment Findings Management

| Finding Severity | Response Timeline | Escalation |
|------------------|-------------------|------------|
| Critical | Immediate mitigation, 7 days resolution | CISO + Business Owner |
| High | 30 days resolution | ISO + Business Owner |
| Medium | 90 days resolution | ISO |
| Low | Next review cycle | Tracked only |

### 5.4 Assessment Documentation

Each assessment shall produce:

| Document | Content |
|----------|---------|
| Assessment report | Scope, methodology, findings, evidence |
| Risk rating | Updated supplier risk score |
| Remediation plan | Actions, owners, timelines |
| Management summary | Executive overview for relationship review |

---

## 6. Compliance Monitoring

### 6.1 Certification Tracking

| Activity | Frequency | Action on Expiry |
|----------|-----------|------------------|
| ISO 27001 validity | Quarterly check | Request renewal evidence, escalate if lapsed |
| SOC 2 report currency | Annual request | Request new report, review findings |
| Other certifications | Per validity period | Verify renewal |
| Regulatory compliance | Annual attestation | Request confirmation |

### 6.2 Compliance Evidence Requirements

| Supplier Level | Evidence Requirements |
|----------------|----------------------|
| Level 1 | Valid certification + audit report + remediation status |
| Level 2 | Valid certification + audit report summary |
| Level 3 | Valid certification (if claimed) |
| Level 4 | None required |

### 6.3 Compliance Failure Response

| Scenario | Response |
|----------|----------|
| Certification lapsed | 30-day cure period, escalate to Business Owner |
| Certification withdrawn | Immediate risk assessment, consider termination |
| Failed audit | Review findings, require remediation plan |
| Regulatory violation | Legal review, assess organizational exposure |

---

## 7. Change Management

### 7.1 Change Categories

| Change Type | Description | Notification Required |
|-------------|-------------|----------------------|
| **Service changes** | Features, functionality, interfaces | Prior notification (Level 1-2) |
| **Infrastructure changes** | Platform, location, architecture | Prior approval (Level 1) |
| **Security changes** | Controls, encryption, access | Prior notification (Level 1-2) |
| **Personnel changes** | Key contacts, account managers | Timely notification |
| **Ownership changes** | Acquisition, merger, divestiture | Immediate notification |
| **Sub-supplier changes** | New or changed sub-suppliers | Prior approval (Level 1) |
| **Contractual changes** | Terms, pricing, SLAs | As per contract |

### 7.2 Change Notification Requirements

| Supplier Level | Notification Requirement |
|----------------|--------------------------|
| Level 1 | 30 days advance notice for material changes |
| Level 2 | 14 days advance notice for material changes |
| Level 3 | Timely notification of significant changes |
| Level 4 | Standard terms apply |

### 7.3 Change Review Process

```
┌─────────────────────────────────────────────────────────────────┐
│ SUPPLIER CHANGE REVIEW PROCESS                                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  1. Supplier notifies of planned change                         │
│                         ↓                                       │
│  2. Log change in supplier register                             │
│                         ↓                                       │
│  3. Assess change impact                                        │
│     • Security impact                                           │
│     • Operational impact                                        │
│     • Compliance impact                                         │
│                         ↓                                       │
│  4. Determine response                                          │
│     • Accept: No concerns                                       │
│     • Accept with conditions: Additional controls needed        │
│     • Reject: Unacceptable risk (negotiate or escalate)         │
│                         ↓                                       │
│  5. Communicate decision to supplier                            │
│                         ↓                                       │
│  6. Update documentation (risk assessment, register)            │
│                         ↓                                       │
│  7. Verify implementation (if applicable)                       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### 7.4 Material Change Definition

A change is considered material if it:

- Affects security controls protecting organization data
- Changes data processing location or jurisdiction
- Modifies access control mechanisms
- Introduces new sub-suppliers with data access
- Significantly alters service architecture
- Impacts compliance with regulatory requirements
- Changes ownership or control of supplier

---

## 8. Relationship Governance

### 8.1 Governance Structure

| Supplier Level | Governance Model |
|----------------|------------------|
| Level 1 | Formal governance with scheduled meetings |
| Level 2 | Regular touchpoints with documented outcomes |
| Level 3 | Periodic check-ins as needed |
| Level 4 | Transactional relationship |

### 8.2 Relationship Review Meetings

**Level 1 Suppliers (Quarterly):**

| Agenda Item | Owner |
|-------------|-------|
| Performance review | Business Owner |
| Security status | Security Team |
| Incident review | Security Team |
| Change review | IT Operations |
| Issues and escalations | Business Owner |
| Upcoming changes | Supplier |
| Action item review | All |

### 8.3 Escalation Procedures

| Issue Type | Level 1 Escalation | Level 2 Escalation | Level 3 Escalation |
|------------|-------------------|-------------------|-------------------|
| Service degradation | Business Owner | IT Management | CIO |
| Security concern | ISO | CISO | Executive |
| Contract dispute | Procurement | Legal | Executive |
| Relationship breakdown | Business Owner | Management | Executive |

---

## 9. Incident Review

### 9.1 Supplier Incident Categories

| Category | Examples |
|----------|----------|
| Security incidents | Data breach, unauthorized access, malware |
| Service incidents | Outage, degradation, data loss |
| Compliance incidents | Certification loss, regulatory violation |
| Near misses | Potential incidents prevented |

### 9.2 Incident Review Process

| Step | Activity |
|------|----------|
| 1 | Receive incident notification from supplier |
| 2 | Log incident in supplier incident register |
| 3 | Assess impact on organization |
| 4 | Request root cause analysis from supplier |
| 5 | Review remediation actions |
| 6 | Update risk assessment if warranted |
| 7 | Document lessons learned |
| 8 | Consider contract/relationship implications |

### 9.3 Post-Incident Requirements

| Supplier Level | Post-Incident Requirements |
|----------------|---------------------------|
| Level 1 | Full RCA, remediation plan, verification, lessons learned |
| Level 2 | RCA summary, remediation confirmation |
| Level 3 | Incident summary, closure confirmation |
| Level 4 | Notification only |

---

## 10. Documentation & Reporting

### 10.1 Required Documentation

| Document | Update Frequency | Retention |
|----------|------------------|-----------|
| Supplier register | Upon change | Current + 3 years |
| Assessment reports | Per assessment | 5 years |
| Review meeting minutes | Per meeting | 3 years |
| Incident records | Upon occurrence | 5 years |
| Change records | Upon change | 3 years |
| SLA reports | Per reporting period | 3 years |

### 10.2 Management Reporting

| Report | Frequency | Audience |
|--------|-----------|----------|
| Supplier risk summary | Quarterly | CISO, Management |
| Critical supplier status | Monthly | ISO, Business Owners |
| Incident summary | Quarterly | CISO |
| Compliance status | Quarterly | ISO, Compliance |

---

## 11. References

| Document | Relationship |
|----------|--------------|
| ISMS-POL-A.5.19-23 | Parent policy framework |
| ISMS-POL-A.5.19-23-S1 | Classification determines monitoring frequency |
| ISMS-POL-A.5.19-23-S2 | Contract terms being monitored |
| ISMS-POL-A.5.19-23-S3 | Sub-supplier monitoring included |
| ISMS-IMP-A.5.19-23.4 | Operational governance assessment workbook |

---

**Next Document:** ISMS-POL-A.5.19-23-S5 — Cloud Services Security (Control A.5.23)

---

*"Monitoring without action is just expensive watching.