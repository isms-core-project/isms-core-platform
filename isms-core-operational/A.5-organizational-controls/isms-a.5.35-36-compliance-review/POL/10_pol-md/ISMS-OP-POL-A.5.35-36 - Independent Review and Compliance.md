**ISMS-OP-POL-A.5.35-36 — Independent Review and Compliance**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Independent Review and Compliance |
| **Document Type** | Operational Policy |
| **Document ID** | ISMS-OP-POL-A.5.35-36 |
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

**Review Cycle**: Annual
**Next Review Date**: [Effective Date + 12 months]

**Approved By**: [Information Security Manager / Management]

**Related Documents**:

- ISO/IEC 27001:2022 Control A.5.35 — Independent review of information security
- ISO/IEC 27001:2022 Control A.5.36 — Compliance with policies, rules and standards for information security
- ISO/IEC 27007:2020 — Guidelines for information security management systems auditing
- ISO/IEC TS 27008 — Guidelines for the assessment of information security controls

**Related Annex A Controls**:

| Control | Relationship to Independent Review and Compliance |
|---------|---------------------------------------------------|
| A.5.1 Policies for information security | Policies are the baseline against which compliance is measured |
| A.5.2 Information security roles and responsibilities | Roles determine accountability for compliance and review |
| A.5.24–28 Incident management lifecycle | Incidents may trigger non-conformity and corrective action |
| A.5.31 Legal, statutory, regulatory, and contractual requirements | Legal compliance obligations feed into compliance verification |
| A.5.36/A.5.35 (reciprocal) | Independent review validates compliance; compliance results feed reviews |
| A.8.34 Protection of information systems during audit testing | Audit tools and testing must not compromise system integrity |

**Related Internal Policies**:

- Information Security Policy
- Risk Management Policy
- Incident Management Policy
- Documented Operating Procedures Policy
- Change Management Policy

---

# Independent Review and Compliance Policy

## Purpose

This policy establishes requirements for the independent review of information security and the verification of compliance with information security policies, rules, and standards.

Independent review ensures the organisation's approach to managing information security — including people, processes, and technologies — is assessed objectively and remains effective. Compliance verification ensures that established policies are consistently followed and enforced across the organisation.

This policy supports Swiss nFADP (revDSG) Art. 8 by implementing organisational measures for the verification and continuous improvement of data security. Where the organisation processes data of individuals in the EU/EEA, GDPR requirements also apply.

## Scope

All employees and third-party users.

All information security management activities, controls, policies, and standards within the ISMS scope, including all personnel, systems, processes, and third parties subject to the organisation's information security requirements.

## Principle

The organisation's approach to managing information security and its implementation shall be reviewed independently at planned intervals, or when significant changes occur. Compliance with information security policies, topic-specific policies, rules, and standards shall be regularly reviewed. Non-conformities shall be identified, root causes determined, corrective actions implemented, and improvements managed and recorded.

---

## Audit Programme

### Internal Audits

Internal audits shall be conducted to assess the effectiveness of the information security management system and the controls documented in the Statement of Applicability.

- Internal audits shall be planned annually, based on risk and business need, ensuring all ISMS areas are covered over the **[specify: 1-year / 3-year]** audit cycle.
- **Annual audit programme shall prioritise**:
  - **Mandatory annual**: Critical controls (incident response, access control, backup/DR, change management).
  - **Risk-based rotation**: Other controls based on risk assessment, prior findings, and significant changes.
  - **100% coverage**: All controls in Statement of Applicability audited within the cycle period.
- The annual audit plan shall be approved by the Management Review Team by **[month, e.g., December]** for the following year.
- Internal audits shall be conducted by individuals independent of the area being audited (i.e., auditors shall not audit their own work).
- Internal audit results shall be reported to and overseen by the Management Review Team.
- Internal audits may result in a non-conformity requiring corrective action or identifying an opportunity for improvement.

### External Certification Audits

External certification audits shall be conducted to assess the effectiveness of the information security management system and the controls documented in the Statement of Applicability.

- External certification audits shall be conducted per the certification body's requirements and schedule.
- External audit results shall be reported to and overseen by the Management Review Team.
- External audits may result in a non-conformity requiring corrective action or an opportunity for improvement.

### Client and Third-Party Audits

Client and third-party audits may be conducted to assess the effectiveness of the information security management system and relevant controls.

- Client and third-party audits shall be conducted subject to a contract and/or non-disclosure agreement being in place.
- Results shall be reported to and overseen by the Management Review Team.
- Client and third-party audits may result in a non-conformity requiring corrective action or an opportunity for improvement.

---

## Independent Review of Information Security

### Review Frequency

Independent reviews of the organisation's approach to managing information security shall be conducted:

- **At planned intervals**: At least annually, covering the full ISMS scope over the review cycle.
- **Upon significant changes**, including:
  - Major organisational restructuring.
  - Significant changes to IT infrastructure or architecture.
  - Introduction of new products or services with security implications.
  - Changes to laws, regulations, or standards affecting information security.
  - Following significant security incidents or breaches.
  - Major changes to the business model or operations.

### Reviewer Independence

Reviews shall be conducted by persons independent of the area being reviewed to prevent "marking your own homework." Independence may be achieved through:

- Internal auditors not responsible for the area under review.
- External third-party auditors or consultants.
- Qualified personnel from separate departments with no operational responsibility for areas reviewed.

### Reviewer Competence

Reviewers shall possess appropriate competence to conduct information security reviews, demonstrated through:

- Relevant qualifications (e.g., CISA, ISO 27001 Lead Auditor, CISSP, or equivalent).
- Demonstrated experience in information security auditing.
- Knowledge of ISO 27001:2022 and relevant regulatory requirements (including Swiss nFADP).

Reviewer qualifications shall be verified and documented before assignment to review activities.

### Review Scope

Independent reviews shall assess whether the organisation's information security approach:

- Meets the requirements set by the organisation for information security.
- Achieves the stated information security objectives.
- Performs effectively as designed.
- Remains adequate for the organisation's risk environment.

Each review's scope shall be documented in advance, including: controls and areas to be reviewed, time period covered, review methodology, documentation and evidence requirements, and planned interviews and assessments.

### Review Execution and Reporting

Independent reviews shall follow a documented plan covering objectives, criteria, sampling methodology, timeline, resource requirements, and reporting requirements.

Reviews shall be evidence-based. Evidence collected during reviews shall be retained in the **ISMS Evidence Library**: [Specify: SharePoint site URL, Confluence space, GRC platform, or equivalent].

**Evidence Library structure**:
- `/Internal Audits/[Year]/` — Internal audit reports, working papers, evidence.
- `/External Audits/[Year]/` — External certification audit reports, findings, corrective actions.
- `/Compliance Assessments/[Year]/` — Self-assessments, management reviews, comprehensive assessments.
- `/Corrective Actions/` — Finding register, action plans, closure evidence.
- `/Risk Acceptances/` — Risk acceptance requests, approvals, review records.

**Access control**: Evidence Library classified as **Internal**; access restricted to CISO, information security team, internal audit, and management.

Evidence retained shall include: documentation reviewed, interview notes, observation records, technical assessment results, and sampling records.

Review findings shall be documented in a formal review report and communicated to appropriate management levels.

### Protection of Systems During Audit Testing

Audit and review activities shall not compromise the security, availability, or integrity of production systems or data (ISO 27001:2022 Control A.8.34).

**Audit tool controls**:
- **Approved tools only**: Auditors shall use pre-approved security assessment tools and scanning software. Approval list maintained by CISO.
- **Change management**: Intrusive testing (penetration testing, vulnerability scanning with exploits) shall follow the change management process with risk assessment and rollback plan.
- **Non-production first**: Testing shall be performed in non-production environments where feasible; production testing requires CISO approval and business owner acceptance.
- **Time windows**: Testing shall be scheduled during approved maintenance windows or low-impact periods.
- **Backups verified**: Current backups shall be verified before intrusive testing.
- **Monitoring**: Audit testing shall be logged; security monitoring teams notified to reduce false positive alerts.

**Data protection during audits**:
- Live production data shall not be exported for audit analysis without Data Protection Officer approval and encryption.
- Audit working papers containing personal or confidential data shall be protected per the Information Classification and Handling Policy.
- Audit evidence shall be securely disposed of after the retention period per this policy.

---

## Finding Severity Classification

All findings from independent reviews, compliance assessments, and audits shall be classified by severity:

| Severity | Definition | Examples | Management Notification |
|----------|------------|----------|------------------------|
| **Critical** | Fundamental control failure with immediate risk to the organisation | Missing access control entirely; no backup system for critical data; active data breach undetected | Immediate notification to CISO and Executive Management |
| **High** | Significant gap requiring prompt attention | Incomplete access reviews; encryption not applied to sensitive data at rest; privileged accounts without MFA | Reported within 5 business days |
| **Medium** | Partial implementation requiring improvement | Inconsistent documentation; infrequent log reviews; outdated risk assessments | Reported with review completion |
| **Low** | Minor gap with limited risk | Procedure clarification needed; minor policy wording ambiguity; training record gaps for non-critical roles | Reported with review completion |
| **Observation** | Improvement opportunity, not a compliance gap | Process efficiency enhancement; automation opportunity; best practice adoption | Included in review report for consideration |

---

## Corrective Action and Remediation

### Action Plan Timeliness

When findings are identified, corrective actions shall be planned and implemented within the following timeframes:

| Finding Severity | Action Plan Required | Target Resolution |
|------------------|---------------------|-------------------|
| **Critical** | Within 24 hours | 30 days maximum |
| **High** | Within 5 business days | 60 days maximum |
| **Medium** | Within 10 business days | 90 days maximum |
| **Low** | Within 30 business days | Next review cycle |

### Tracking

All corrective actions shall be tracked in the corrective action register (incident and corrective action log) with:

- Finding reference and description.
- Owner accountable for completion.
- Target completion date.
- Resources required and dependencies.
- Current status and progress notes.

Progress shall be tracked and reported:

- **Weekly** for Critical findings.
- **Bi-weekly** for High findings.
- **Monthly** for Medium and Low findings.

### Closure Verification

Corrective actions shall not be marked as complete until:

- The action has been implemented.
- Evidence of implementation exists.
- Verification confirms effectiveness.
- For Critical and High findings: independent verification by a person other than the action owner.

**Effectiveness verification timing**:
- **Critical findings**: Effectiveness verified **30 days** after implementation (verify issue has not recurred).
- **High findings**: Effectiveness verified **60 days** after implementation.
- **Medium/Low findings**: Effectiveness verified at next scheduled compliance assessment or internal audit.

Verification confirms the finding has been fully resolved and will not recur. If the finding recurs or the corrective action is ineffective, the action is re-opened for root cause analysis and alternative remediation.

---

## Compliance Verification

### Three-Tier Review Structure

Compliance with the organisation's information security policy, topic-specific policies, rules, and standards shall be reviewed through a three-tier approach:

| Review Type | Frequency | Responsible | Scope |
|-------------|-----------|-------------|-------|
| **Self-assessment** | Quarterly | System/Asset Owners | Own systems and areas of responsibility |
| **Management compliance review** | Semi-annually | Department Managers | Department-wide compliance with policies and standards |
| **Comprehensive compliance assessment** | Annually | CISO / Information Security Team | Organisation-wide compliance across all policies and controls |

### Verification Methods

Compliance shall be verified through appropriate methods, including:

- **Document review** — Policies signed, procedures followed, records maintained.
- **Technical assessment** — Configuration review, vulnerability scanning, automated compliance checks.
- **Interview and observation** — Staff interviews, process observation, walk-throughs.
- **Sampling and testing** — Random or risk-based sampling of transactions, records, or configurations.
- **Automated monitoring** — Continuous compliance monitoring tools where available.

### Evidence Requirements

Compliance claims shall be supported by evidence, including:

- Screenshots or system reports for technical compliance.
- Signed acknowledgments for policy acceptance.
- Training records for awareness requirements.
- Logs and records for procedural compliance.

Compliance evidence shall be stored in the ISMS Evidence Library (SharePoint, Confluence, or equivalent) and retained in accordance with the organisation's records retention schedule.

### Assessment Completion Tracking

- **Self-assessments (quarterly)**: System/asset owners submit completed assessment checklist to CISO by **[day, e.g., last business day of the quarter]**. Completion tracked in compliance dashboard.
- **Management reviews (semi-annual)**: Department managers conduct reviews in **[months, e.g., June and December]**; submit summary report to CISO. Completion target: 100% of departments.
- **Comprehensive assessment (annual)**: CISO or information security team conducts full assessment; report presented to Management Review Team by **[month/date, e.g., end of Q1]**.

Non-completion of scheduled assessments shall be escalated: 30 days overdue to Department Head, 60 days overdue to CISO, reported at next Management Review.

---

## Non-Conformity Management

### Definition

A non-conformity is a deviation from the norm — defined as a deviation from policy, procedure, standard, or regulatory requirement. Non-conformities may be identified through audits, compliance reviews, incident management, or change management.

### Severity Classification

| Severity | Definition | Action Required |
|----------|------------|-----------------|
| **Critical** | Complete disregard for, or absence of, a security requirement | Immediate containment; 30-day resolution |
| **High** | Significant deviation from a requirement | 60-day resolution |
| **Medium** | Partial compliance; gaps exist | 90-day resolution |
| **Low** | Minor deviation with limited risk | Next review cycle |

### Escalation

Non-conformities not resolved within target timeframes shall be escalated:

- **30 days overdue**: Escalate to Department Head.
- **60 days overdue**: Escalate to CISO.
- **90 days overdue**: Escalate to Executive Management.

### Root Cause Analysis

Root cause analysis (RCA) shall be conducted for:

- All Critical severity findings.
- All High severity findings.
- Recurring findings (same or similar finding in two consecutive reviews).
- Findings with systemic implications.

**RCA methodology**: The organisation shall use a structured RCA approach such as:
- **5 Whys**: Iterative questioning to drill down to root cause (suitable for most findings).
- **Fishbone Diagram (Ishikawa)**: Categorise causes by People, Process, Technology, Environment.
- **Fault Tree Analysis**: For complex, multi-factor findings.

**RCA documentation** shall include: finding description, analysis method used, identified root cause(s), contributing factors, corrective actions, and preventive actions.

When a non-conformity occurs, the organisation shall:

1. Take action to correct it and deal with the consequences.
2. Review the non-conformity.
3. Determine the root cause of the non-conformity.
4. Determine if similar non-conformities exist or could potentially occur.
5. Implement corrective actions to eliminate the root cause.
6. Implement preventive actions to address similar or potential non-conformities elsewhere.

### Corrective and Preventive Actions

- **Corrective actions** address the specific non-conformity and its root cause to prevent recurrence.
- **Preventive actions** address similar or potential non-conformities in other areas of the ISMS.

Non-conformities shall be recorded, documented, and tracked in the incident and corrective action log. The effectiveness of corrective and preventive actions shall be reviewed.

Non-conformities are reported through the Management Review Team.

---

## Risk Acceptance

### Authority by Severity

Findings that cannot be remediated within acceptable timeframes, or where remediation cost exceeds the associated risk, may be submitted for formal risk acceptance:

| Finding Severity | Risk Acceptance Authority |
|------------------|---------------------------|
| **Critical** | CEO / Executive Management |
| **High** | CISO with CIO endorsement |
| **Medium** | CISO |
| **Low** | Department Head with CISO notification |

### Documentation Requirements

Risk acceptance requests shall include:

- Finding description and severity.
- Business justification for acceptance.
- Compensating controls in place.
- Duration of acceptance (maximum 12 months).
- Review trigger conditions.
- Risk owner acknowledgment.

### Renewal

Risk acceptances shall be reviewed:
- **Scheduled**: At each compliance review cycle (minimum annually).
- **Triggered**: When circumstances change:
  - New technology or compensating control becomes available.
  - Risk level increases (e.g., threat landscape change, new regulatory requirement).
  - Security incident occurs related to the accepted risk.
  - Business context changes (e.g., new data processed, new jurisdiction).

When a trigger condition occurs, the risk owner shall notify the CISO within **14 days** for reassessment.

Renewals require the same approval authority level as the initial acceptance and must demonstrate re-assessment of risk and continued justification.

---

## Compliance Metrics and Reporting

### Key Performance Indicators

The following KPIs shall be tracked to measure the effectiveness of the compliance and review programme:

| KPI | Target | Measurement |
|-----|--------|-------------|
| Independent review completion rate | 100% | Scheduled reviews completed vs. planned |
| Finding closure rate within SLA | 90% | Findings closed on time vs. total findings |
| Critical finding MTTR | < 30 days | Mean time to remediate Critical findings |
| High finding MTTR | < 60 days | Mean time to remediate High findings |
| Compliance assessment completion | 100% | Assessments completed vs. scheduled |
| Policy compliance rate | > 90% | Compliant items vs. total assessed items |

### Reporting Cadence

- **Monthly**: CISO receives compliance dashboard with:
  - KPI status (target vs. actual).
  - **Finding aging** (findings by severity and days open):
    - **Green**: Within target resolution timeframe.
    - **Yellow**: 50–100% of target timeframe elapsed (e.g., Critical at 15–30 days, High at 30–60 days).
    - **Red**: Past target resolution timeframe.
  - Top 5 overdue findings with owners and escalation status.
  - Newly opened and closed findings since last report.
- **Quarterly**: Executive Management receives compliance summary, KPI scorecard, trend analysis, and escalated items.
- **Annually**: Management Review receives comprehensive compliance report, annual trend analysis, and programme effectiveness assessment.

### Trend Analysis

Compliance and review metrics shall be tracked over time to identify improvement or degradation trends (quarter-over-quarter, year-over-year), recurring finding patterns, areas requiring focused attention, and the effectiveness of remediation efforts.

**Key trends to monitor**:
- Finding volume by severity (increasing/decreasing).
- Mean time to remediate (MTTR) by severity (improving/degrading).
- Finding recurrence rate (% of findings that recur within 12 months).
- Department/system compliance scores (consistently high/low performers).

Trend data shall be retained for a minimum of **3 years** to support long-term analysis and certification audit preparation.

**Annual trend report**: Presented to Management Review Team showing 3-year trend analysis and improvement/degradation areas.

---

## Improvement Inputs

The following sources shall be considered as inputs for continual improvement of the ISMS:

- **Audit findings** — Internal, external, and client/third-party audits.
- **Incident management** — Security incidents may identify non-conformities or improvement opportunities.
- **Change management** — Changes to systems, processes, or the organisation may identify improvement needs.
- **Review of objectives** — Review of information security objectives may identify improvement opportunities.
- **Legal, regulatory, and standards changes** — Changes to applicable laws, regulations, or information security standards.
- **Management Review Team** — The Management Review Team shall consider opportunities for improvement as a standing agenda item.

Changes to the information security management system resulting from improvement activities shall be planned, managed, and recorded in the incident and corrective action log or change log, as appropriate.

### Improvement Action Process

When improvement opportunities are identified from reviews, audits, or compliance assessments:

1. **Capture**: Document in the incident and corrective action log or dedicated improvement register with description, source (audit, review, incident), proposed action, and expected benefit.
2. **Evaluate**: Information security team evaluates feasibility, cost, benefit, and priority within **30 days**.
3. **Approve**: Improvements requiring investment or significant effort require Management Review Team approval.
4. **Implement**: Approved improvements follow change management process; owner assigned, tracked to completion.
5. **Measure**: Effectiveness of improvement measured through subsequent reviews or KPI changes.

**Improvement metrics**: Number of improvement opportunities identified, percentage implemented, average time from identification to implementation.

---

## Roles and Responsibilities

| Role | Responsibilities |
|------|-----------------|
| **Executive Management** | Approve compliance policy; receive and act on review findings; approve risk acceptances for Critical findings; ensure resources for audit and review programme |
| **CISO** | Own compliance and review programme; ensure reviews are conducted; oversee remediation; report to Executive Management; approve risk acceptances for Medium findings |
| **Internal Audit / Compliance Manager** | Coordinate audit programme and compliance activities; maintain findings register; track remediation; produce reports; verify reviewer independence |
| **Department Managers** | Ensure team compliance; conduct semi-annual management reviews; own remediation actions in their areas; report compliance status |
| **System / Asset Owners** | Conduct quarterly self-assessments; maintain compliance evidence; implement remediations for owned systems |
| **Information Security Team** | Support compliance verification; provide technical assessment capability; verify finding closures |
| **All Personnel** | Comply with policies, rules, and standards; cooperate with audits and reviews; report suspected non-compliance |

---

## Evidence

The following evidence demonstrates compliance with this policy:

| # | Evidence | Owner | Frequency |
|---|----------|-------|-----------|
| 1 | **Internal audit reports** and annual audit plan | CISO / Internal Audit | *Annual programme; per audit; retained 7 years* |
| 2 | **External audit reports** (certification body) | CISO | *Per certification cycle; retained 7 years* |
| 3 | **Independent review reports** with scope, findings, and recommendations | CISO / Reviewer | *Annual + upon significant changes; retained 7 years* |
| 4 | **Corrective action register** (findings, owners, status, closure evidence) | CISO / Compliance Manager | *Maintained continuously; reviewed monthly; retained 7 years* |
| 5 | **Compliance assessment records** (self-assessments, management reviews, comprehensive assessments) | Department Managers / CISO | *Per schedule (quarterly/semi-annual/annual); retained 5 years* |
| 6 | **Risk acceptance records** with business justification and compensating controls | CISO / Executive Management | *Per event; reviewed annually; retained 7 years* |
| 7 | **Root cause analysis records** for Critical, High, and recurring findings | CISO / Compliance Manager | *Per finding; retained 5 years* |
| 8 | **Reviewer qualification records** (certifications, experience, independence declarations) | CISO / HR | *Per engagement; retained for duration + 3 years* |
| 9 | **Compliance dashboard and KPI reports** with trend analysis | CISO / Compliance Manager | *Monthly dashboard; quarterly management report; retained 3 years* |
| 10 | **Management Review minutes** documenting review of compliance and audit findings | CISO / Executive Management | *Per Management Review; retained 7 years* |

---

# Policy Compliance

## Compliance Measurement

The information security management team will verify compliance with this policy through various methods, including but not limited to, audit completion tracking, compliance assessment records, finding closure metrics, KPI monitoring, internal and external audits, and feedback to the policy owner.

## Exceptions

Any exception to this policy shall be approved and recorded by the Information Security Manager in advance, with documented risk acceptance, compensating controls, and a defined review date (maximum 12 months, renewable). Exceptions shall be reported to the Management Review Team.

## Non-Compliance

An employee found to have violated this policy may be subject to disciplinary action, up to and including termination of employment.

## Continual Improvement

This policy is reviewed and updated as part of the continual improvement process. Reviews shall consider changes to auditing standards, regulatory compliance requirements, emerging risks, audit findings, lessons learned from non-conformities, and feedback from internal and external stakeholders.

---

# Areas of the ISO 27001 Standard Addressed

Independent Review and Compliance Policy — ISO 27001 Controls Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership and commitment | 5.1 Policies for information security |
| Clause 5.2 Policy | 5.4 Management responsibilities |
| Clause 6.2 Information security objectives | **5.35 Independent review of information security** |
| Clause 9.1 Monitoring, measurement, analysis, and evaluation | **5.36 Compliance with policies, rules, and standards for information security** |
| Clause 9.2 Internal audit | 6.3 Information security awareness, education, and training |
| Clause 9.3 Management review | 6.4 Disciplinary process |
| Clause 10.1 Continual improvement | 8.34 Protection of information systems during audit testing |
| Clause 10.2 Nonconformity and corrective action | |

**Regulatory and Legal Framework**:

| Framework | Relevance |
|-----------|-----------|
| Swiss nFADP (revDSG) | Art. 8 — Technical and organisational measures, including verification of effectiveness of security controls |
| Swiss DSV (Data Protection Ordinance) | Art. 1–3 — Minimum requirements for data security; requirement for periodic review of measures |
| EU GDPR (where applicable) | Art. 5(2) — Accountability principle; Art. 32 — Verification of security measures effectiveness |
| ISO/IEC 27001:2022 | Annex A Controls 5.35 (Independent Review), 5.36 (Compliance Verification) |
| ISO/IEC 27002:2022 | Sections 5.35–5.36 — Implementation guidance for review and compliance |
| ISO/IEC 27007:2020 | Guidelines for information security management systems auditing |
| NIST SP 800-53 Rev 5 | CA-2 (Control Assessments), CA-5 (Plan of Action and Milestones), CA-7 (Continuous Monitoring) |
| CIS Controls v8 | Control 18 (Penetration Testing — independent security assessment) |

---

<!-- QA_VERIFIED: 2026-02-07 -->
