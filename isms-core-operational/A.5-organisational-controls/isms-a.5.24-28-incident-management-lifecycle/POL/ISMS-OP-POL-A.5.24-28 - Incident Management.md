<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.5.24-28:operational:OP-POL:a.5.24-28 -->
**ISMS-OP-POL-A.5.24-28 — Incident Management**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Incident Management |
| **Document Type** | Operational Policy |
| **Document ID** | ISMS-OP-POL-A.5.24-28 |
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

- ISO/IEC 27001:2022 Controls A.5.24, A.5.25, A.5.26, A.5.27, A.5.28 — Incident management planning, assessment, response, learning, evidence collection

**Related Annex A Controls**:

| Control | Relationship to Incident Management |
|---------|-------------------------------------|
| A.5.5–6 Contact with authorities and special interest groups | External reporting obligations (FDPIC, law enforcement, CERT) |
| A.5.7 Threat intelligence | Threat intelligence informs incident detection and response |
| A.5.29 Information security during disruption | Business continuity activation during major incidents |
| A.5.34 Privacy and protection of PII | Personal data breach notification requirements |
| A.6.8 Information security event reporting | User reporting of security events feeds incident triage |
| A.8.15 Logging | Log data supports incident detection and forensic analysis |
| A.8.16 Monitoring activities | Monitoring detects security events for incident triage |

**Related Internal Policies**:

- Access Control Policy
- Logging Policy
- Monitoring Activities Policy (A.8.16)
- Business Continuity Policy
- Privacy and Protection of PII Policy
- Information Classification and Handling Policy

---

# Incident Management Policy

## Purpose

This policy provides guidance on managing information security incidents in a structured manner, including the identification, assessment, response, and resolution of security events and incidents, and the identification, collection, acquisition, and preservation of information which can serve as evidence.

This policy supports Swiss nFADP (revDSG) and the Data Protection Ordinance (DSV) by implementing breach notification procedures and technical and organisational measures appropriate to risk. Where the organisation processes data of individuals in the EU/EEA, GDPR requirements also apply.

## Scope

All employees and third-party users.

All information systems, applications, and services deemed in scope by the ISO 27001 scope statement.

## Principle

All information security events shall be reported and assessed. Confirmed incidents shall be managed through a structured response process with defined roles, escalation paths, and communication procedures. The organisation shall learn from incidents to improve its security posture. Where incidents may lead to external investigation or legal proceedings, specialist external resources shall be engaged.

---

## Definitions

| Term | Definition |
|------|------------|
| **Security event** | An identified occurrence indicating a possible breach of security policy or failure of controls. Not all events are incidents. |
| **Security incident** | A security event that has been assessed and confirmed as having an actual or potential adverse effect on the confidentiality, integrity, or availability of information. |
| **Personal data breach** | A security incident involving accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to personal data. |
| **Significant incident** | An incident that constitutes a legal or regulatory breach, could lead to an external investigation or legal proceedings, or creates high risk to data subjects. |

---

## Incident Reporting

All employees and third-party users shall report security events immediately upon discovery to the information security management team through the designated reporting channels:

- **Primary**: IT service desk (email, phone, or ticketing system).
- **Alternative**: Direct contact with the information security management team (email distribution list or phone).
- **After hours**: On-call security contact (phone or messaging).
- **Anonymous**: Where employees wish to report concerns anonymously, reports may be submitted via the organisation's whistleblowing or ethics reporting mechanism.

Reporting channels shall be communicated during onboarding and annual awareness training, and published on the organisation intranet.

Reports shall include, where known:

- What was observed (description of the event).
- When it occurred or was discovered.
- Which systems, data, or people are affected.
- Any actions already taken.

Security events may also be detected through automated monitoring, log analysis, or third-party notification.

Employees shall not attempt to investigate or resolve suspected incidents themselves. Preservation of evidence takes priority over curiosity.

---

## Event Assessment and Triage

The information security management team shall assess all reported security events to determine whether they constitute a security incident.

Assessment shall consider:

- The nature and scope of the event.
- The classification of information affected.
- The number of data subjects or systems affected.
- Whether personal data is involved (potential data breach).
- The potential business, legal, or regulatory impact.

Events that do not meet the threshold for an incident shall be logged, and trends shall be monitored.

### Incident Register

All reported security events and confirmed incidents shall be recorded in the incident register with the following minimum fields:

| Field | Description |
|-------|-------------|
| Incident ID | Unique identifier (e.g., INC-2026-001) |
| Date/time reported | When the event was reported |
| Date/time detected | When the event occurred or was first detected |
| Reporter | Who reported the event |
| Description | Summary of what happened |
| Systems/data affected | Which systems, applications, or data types are involved |
| Classification level | Classification of information affected |
| Personal data involved | Yes/No; if yes, categories and estimated number of data subjects |
| Severity | Critical / High / Medium / Low |
| Status | Open / Investigating / Contained / Resolved / Closed |
| Assigned to | Incident handler or team |
| Root cause | Determined after investigation |
| Actions taken | Containment, eradication, recovery actions with timestamps |
| Lessons learned | Reference to post-incident review (if conducted) |
| Closure date | When the incident was formally closed |

---

## Incident Classification

Confirmed incidents shall be classified by severity to determine response priority, escalation, and communication requirements:

| Severity | Description | Examples | Initial Response |
|----------|-------------|----------|-----------------|
| **Critical** | Confirmed data breach, complete service outage, active compromise of critical systems | Ransomware, data exfiltration, compromise of authentication systems | Immediate (within 1 hour) |
| **High** | Significant impact to major functions, potential data exposure, targeted attack | Malware on multiple endpoints, unauthorised access to sensitive data, phishing campaign targeting executives | Within 4 hours |
| **Medium** | Limited impact, contained to single system or user, no confirmed data loss | Single malware detection, policy violation, failed intrusion attempt | Within 1 business day |
| **Low** | Minimal impact, no data involved, informational | Spam increase, minor policy deviation, single failed login pattern | Within 3 business days |

Severity may be escalated at any point during the incident lifecycle as new information emerges.

---

## Incident Response

### Response Lifecycle

Incidents shall be managed through the following phases, aligned with NIST SP 800-61:

1. **Containment** — Limit the impact and prevent further damage. Short-term containment actions (e.g., isolating affected systems, disabling compromised accounts) shall be taken immediately. Long-term containment strategies shall be planned where eradication cannot be immediate.

2. **Eradication** — Remove the root cause of the incident. This may include removing malware, closing vulnerabilities, resetting compromised credentials, or rebuilding affected systems.

3. **Recovery** — Restore systems and services to normal operations. Recovery shall be verified through testing before returning systems to production. Monitoring shall be enhanced during the recovery period to detect recurrence.

4. **Post-incident review** — Conduct a structured review after resolution (see Lessons Learned section below).

All incident response actions shall be documented with timestamps, actions taken, and personnel involved.

### Incident Response Team

The following roles shall be assigned within the incident response capability:

| Role | Responsibility | Assigned To |
|------|----------------|-------------|
| **Incident Response Team Leader** | Overall coordination of incident response; escalation decisions; communication with senior management | CISO or IT Security Manager |
| **Technical Lead** | Technical investigation, containment, and eradication; evidence preservation | Senior IT Security Analyst or IT Operations Lead |
| **Communications Lead** | Internal and external communications; media liaison (if required) | CISO or designated spokesperson |
| **Legal Advisor** | Legal guidance on notification obligations, evidence handling, regulatory requirements | Legal counsel (internal or external) |
| **Business Liaison** | Business impact assessment; coordination with affected business units | Department head or business continuity coordinator |

Role assignments shall be documented, communicated to all team members, and reviewed annually. Deputies shall be assigned for each role to ensure availability.

### Escalation

The incident response team leader shall escalate incidents to senior management when:

- The incident is classified as Critical or High.
- The incident involves personal data (potential data breach notification).
- The incident may require external notification (regulatory, law enforcement, customers).
- The incident exceeds the response team's capability or authority.
- The incident has not been contained within the expected timeframe.

### Communication

Incident information shall be shared on a strict need-to-know basis. Communication during an active incident shall be coordinated through the incident response team leader.

Internal status updates shall be provided at regular intervals for Critical and High incidents.

External communication (media, customers, partners) shall be approved by senior management and reviewed by legal counsel before release.

---

## Significant Incidents

Significant incidents are defined as incidents that constitute a legal or regulatory breach, could lead to an external investigation, or could lead to legal proceedings.

### High-Level Guidance

In all instances where a situation may lead to an external investigation or legal proceedings, specialist external resources shall be engaged.

At the earliest opportunity, all work on, access to, modification of, or tampering with affected systems, documents, locations, files, databases, applications, or other in-scope entities shall stop. The only exceptions are the preservation of life, health, and safety, or the bare minimum actions required to triage and make safe.

### Process

1. Appoint a Significant Incident Team Leader from the senior management team as the single point of contact and coordination.
2. Follow the guidance above to stop and make safe.
3. Immediately contact legal counsel.
4. Immediately contact a computer forensic and investigative supplier from a qualified and authorised company.
5. As required, contact the authorities including law enforcement, the Federal Data Protection and Information Commissioner (FDPIC), and any applicable industry regulators.
6. If cyber security insurance cover is held, immediately inform the insurance company.
7. Follow the guidance of legal counsel, law enforcement, forensic investigators, and insurance companies, while following the incident management process for recording, tracking, and managing the incident.

---

## Data Breach Notification

Where an incident involves personal data (a personal data breach), the following notification requirements apply:

### Swiss nFADP Notification

| Notification | Trigger | Timeline |
|--------------|---------|----------|
| **FDPIC** (Federal Data Protection and Information Commissioner) | Data breach likely to result in a **high risk** to the personality or fundamental rights of data subjects | **As soon as possible** after becoming aware of the breach |
| **Data subjects** | Where notification is necessary for the protection of the data subjects, or where the FDPIC requests it | **As soon as possible** (no fixed deadline) |
| **Processor → Controller** | Processor discovers a breach involving the controller's personal data | **As soon as possible** after discovery |

### EU GDPR Notification (where applicable)

| Notification | Trigger | Timeline |
|--------------|---------|----------|
| **Supervisory authority** | Any personal data breach unless unlikely to result in risk to rights and freedoms | **Within 72 hours** of becoming aware |
| **Data subjects** | Breach likely to result in **high risk** to rights and freedoms | **Without undue delay** |

Where both nFADP and GDPR apply, the organisation shall meet the stricter timeline (72 hours).

### Notification Content

Breach notifications to supervisory authorities shall include, at minimum:

| Element | nFADP (Art. 24) | GDPR (Art. 33) |
|---------|-----------------|-----------------|
| Nature of the breach | Required | Required (including categories and approximate number of data subjects and records) |
| Consequences and risks | Required | Required (likely consequences) |
| Measures taken or planned | Required | Required (measures taken or proposed to address and mitigate) |
| Contact point | Required (where FDPIC or data subjects can obtain further information) | Required (name and contact details of DPO or other contact point) |

Where full information is not available at the time of notification, it shall be provided in phases without undue delay.

### Breach Assessment

Not all security incidents involving personal data require notification. The incident response team shall assess:

- The nature and sensitivity of the personal data involved.
- The number of data subjects affected.
- The severity and likelihood of consequences for data subjects.
- Whether the data was encrypted or otherwise rendered unintelligible.
- Whether the breach has been contained and the risk mitigated.

The assessment and decision (including the rationale for not notifying, if applicable) shall be documented.

---

## Collection and Preservation of Evidence

Where an incident may require forensic analysis, legal action, or regulatory investigation, evidence shall be collected and preserved following these principles:

### Evidence Handling

- Evidence shall be collected as soon as possible after the incident is identified.
- Original evidence shall not be accessed, modified, or analysed directly. Forensic copies (bit-for-bit images) shall be created using write-blocking tools.
- All evidence shall be verified using cryptographic hash functions (SHA-256 minimum) to confirm integrity.

### Chain of Custody

A chain of custody record shall be maintained for all evidence, documenting:

- What was collected (description, serial numbers, identifiers).
- When it was collected (date, time).
- Who collected it.
- Where it is stored.
- Who has accessed it and when.
- Any transfers between custodians.

### Evidence Storage

- Evidence shall be stored in a secure location with restricted access.
- Digital evidence shall be stored on encrypted media.
- Physical evidence shall be stored in a locked, tamper-evident container.
- Evidence shall be retained for a minimum of **12 months** from incident closure, or longer where required by legal counsel, regulatory requirements, or ongoing proceedings.

### External Forensic Support

For significant incidents, qualified external forensic investigators shall be engaged. The organisation shall identify and pre-approve at least one external forensic provider and maintain current contact details and engagement terms (retainer or pre-agreed terms of reference). Internal personnel shall not conduct forensic analysis unless trained and qualified to do so.

---

## Lessons Learned

A post-incident review shall be conducted for all Critical and High severity incidents, and optionally for Medium incidents where useful lessons may be derived.

### Review Process

The review shall be held within 5 business days of incident resolution, while details are still fresh. The review shall include all personnel who contributed to the response.

The review shall document:

- **Timeline**: A factual chronology of the incident from detection through resolution.
- **Root cause**: The underlying cause of the incident (not just the trigger).
- **What worked**: Effective response actions, successful containment measures, good team coordination.
- **What could be improved**: Gaps in detection, response delays, communication issues, missing tools or procedures.
- **Action items**: Specific, measurable improvements with an assigned owner and deadline.

### Follow-Up

- Action items shall be tracked to completion.
- Lessons learned shall be communicated to relevant personnel.
- The incident response plan shall be updated where findings indicate gaps.
- Trends across incidents shall be reviewed quarterly to identify systemic issues.

Reviews shall be conducted in a blame-free manner, focusing on system and process improvement rather than individual fault.

---

## Incident Response Testing

The incident response plan shall be tested at least **annually** through tabletop exercises or simulations to verify that:

- Roles and responsibilities are understood.
- Communication channels function correctly.
- Escalation paths are clear and effective.
- Evidence collection procedures are practical.
- Data breach notification timelines can be met.

**Minimum test scenarios** (rotate annually):

| Scenario | Tests | Frequency |
|----------|-------|-----------|
| Ransomware attack with data encryption | Containment, recovery from backup, communication, decision to pay/not pay | At least every 2 years |
| Personal data breach with notification obligation | Breach assessment, FDPIC notification process, data subject notification | At least every 2 years |
| Insider threat / compromised privileged account | Detection, access revocation, evidence preservation, HR coordination | At least every 2 years |
| Business email compromise / social engineering | Detection, financial controls verification, incident reporting | At least every 2 years |

Test results and improvements shall be documented, including participants, scenario details, observed gaps, and corrective actions with owners and deadlines.

---

## Evidence

The following evidence demonstrates compliance with this policy:

- **Incident register** (all reported events and confirmed incidents with severity, status, resolution) — *maintained continuously; reviewed quarterly for trends*
- **Incident response records** (containment, eradication, recovery actions with timestamps) — *retained for minimum 3 years*
- **Data breach assessment and notification records** (including decisions not to notify, with rationale) — *retained for 5 years*
- **Chain of custody records** for forensic evidence — *retained for duration of any legal proceedings plus 2 years*
- **Post-incident review reports** with action items and completion tracking — *completed within 5 business days of resolution; actions tracked to closure*
- **Incident response testing records** (tabletop exercises, simulations) — *annual; retained for 3 years*
- **Contact list for incident response** (internal team, legal counsel, pre-approved forensic provider, FDPIC, cyber insurance provider) — *reviewed quarterly; updated upon any change*
- **Communication templates** (internal notification, external notification, data subject notification, media statement) — *pre-approved by legal counsel; reviewed annually*

### Incident Metrics

The following metrics shall be reported quarterly to the CISO and Management Review Team:

| Metric | Description |
|--------|-------------|
| Total events reported | Volume of security events received |
| Events converted to incidents | Number and percentage of events classified as incidents |
| Incidents by severity | Breakdown of Critical / High / Medium / Low |
| Mean time to detect (MTTD) | Average time from event occurrence to detection |
| Mean time to respond (MTTR) | Average time from detection to containment |
| Mean time to resolve | Average time from detection to closure |
| Overdue incidents | Incidents exceeding target response timelines |
| Data breaches reported | Number requiring notification to FDPIC or supervisory authority |
| Post-incident reviews completed | Percentage of Critical/High incidents with completed reviews |

---

# Policy Compliance

## Compliance Measurement

The information security management team will verify compliance with this policy through various methods, including but not limited to, incident response metrics, post-incident review completion, testing records, internal and external audits, and feedback to the policy owner.

## Exceptions

Any exception to this policy shall be approved and recorded by the Information Security Manager in advance, with documented risk acceptance, compensating controls, and a defined review date. Exceptions shall be reported to the Management Review Team.

## Non-Compliance

An employee found to have violated this policy may be subject to disciplinary action, up to and including termination of employment.

## Continual Improvement

This policy is reviewed and updated as part of the continual improvement process. Reviews shall consider changes to incident management standards, regulatory notification requirements, emerging threats, and lessons learned from incidents and exercises.

---

# Areas of the ISO 27001 Standard Addressed

Incident Management Policy — ISO 27001 Controls Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership and commitment | 5.1 Policies for information security |
| Clause 5.2 Policy | 5.4 Management responsibilities |
| Clause 6.2 Information security objectives | 5.36 Compliance with policies, rules, and standards |
| Clause 7.3 Awareness | **5.24 Information security incident management planning and preparation** |
| Clause 8.1 Operational planning and control | **5.25 Assessment and decision on information security events** |
| | **5.26 Response to information security incidents** |
| | **5.27 Learning from information security incidents** |
| | **5.28 Collection of evidence** |
| | 6.3 Information security awareness, education, and training |
| | 6.4 Disciplinary process |
| | 6.8 Information security event reporting |

**Regulatory and Legal Framework**:

| Framework | Relevance |
|-----------|-----------|
| Swiss nFADP (revDSG) | Art. 24 — Data breach notification to FDPIC ("as soon as possible") |
| Swiss DSV (Data Protection Ordinance) | Art. 1–3 — Minimum requirements for data security |
| EU GDPR (where applicable) | Art. 33–34 — Breach notification (72 hours to authority, without undue delay to data subjects) |
| ISO/IEC 27001:2022 | Annex A Controls 5.24, 5.25, 5.26, 5.27, 5.28 |
| ISO/IEC 27002:2022 | Sections 5.24–5.28 — Implementation guidance |
| ISO/IEC 27037:2012 | Guidelines for identification, collection, acquisition, and preservation of digital evidence |
| NIST SP 800-61 Rev 2 | Computer Security Incident Handling Guide (four-phase lifecycle) |
| CIS Controls v8 | Control 17 (Incident Response Management) |

---

<!-- QA_VERIFIED: 2026-02-07 -->
