**ISMS-OP-POL-A.5.5-6 — Contact with Authorities and Special Interest Groups**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Contact with Authorities and Special Interest Groups |
| **Document Type** | Operational Policy |
| **Document ID** | ISMS-OP-POL-A.5.5-6 |
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

- ISO/IEC 27001:2022 Controls A.5.5, A.5.6 — Contact with authorities; Contact with special interest groups
- ISO/IEC 27002:2022 Sections 5.5, 5.6 — Implementation guidance
- Swiss nFADP (revDSG) Art. 24 — Data breach notification
- Swiss Information Security Act (ISG) Art. 73a-79 — Mandatory cyber incident reporting
- NIST SP 800-53 Rev 5 IR-6 — Incident Reporting
- NIST SP 800-53 Rev 5 PM-15 — Security and Privacy Groups and Associations

**Related Annex A Controls**:

| Control | Relationship to Contact with Authorities and Special Interest Groups |
|---------|----------------------------------------------------------------------|
| A.5.1 Policies for information security | Overarching policy framework governing external communications |
| A.5.7 Threat intelligence | Intelligence received from authorities and special interest groups |
| A.5.24-28 Incident management lifecycle | Authority notification triggered during incident response |
| A.5.31 Legal, statutory, regulatory and contractual requirements | Regulatory obligations that mandate authority contacts |
| A.5.34 Privacy and PII protection | Data protection authority communications and breach notification |
| A.8.16 Monitoring activities | Monitoring outputs may trigger mandatory authority reports |

**Related Internal Policies**:

- Incident Management Lifecycle Policy
- Threat Intelligence Policy
- Privacy and PII Protection Policy
- Legal, Statutory, Regulatory and Contractual Requirements Policy
- Information Classification and Handling Policy

---

# Contact with Authorities and Special Interest Groups Policy

## Purpose

The purpose of this policy is to ensure that [Organisation] establishes and maintains appropriate contacts with relevant authorities, regulatory bodies, law enforcement agencies, and special interest groups — and that these contacts are used effectively to support regulatory compliance, incident response, and information security improvement.

Maintaining current authority contacts enables rapid, compliant reporting when security incidents or data breaches occur. Participation in special interest groups ensures [Organisation] receives timely threat intelligence, vulnerability advisories, and access to industry best practices that strengthen the organisation's security posture.

This policy supports Swiss nFADP (revDSG) by implementing organisational measures to ensure timely notification to the Federal Data Protection and Information Commissioner (FDPIC) in the event of data security breaches likely to result in high risk to data subjects (Art. 24 nFADP). It also addresses mandatory cyber incident reporting obligations under the Swiss Information Security Act (ISG) where applicable. Where [Organisation] processes data of individuals in the EU/EEA, GDPR Art. 33 notification requirements also apply.

## Scope

All personnel involved in external communications with authorities, regulatory bodies, law enforcement, and special interest groups regarding information security matters.

This includes:

- Mandatory authority contacts (NCSC, FDPIC, cantonal police, emergency services).
- Notification obligations with regulatory timeframes (data breaches, cyber incidents).
- Authorised spokespersons for authority communications.
- Special interest group and professional association participation.
- Information sharing with external security communities.
- Maintenance and verification of the authority contact register.

**Out of scope**: Routine business communications unrelated to information security; personal professional memberships where the individual is not representing [Organisation]; media relations and public communications (covered by the organisation's communications policy, though security-related media inquiries shall be coordinated with the CISO); internal security communications between departments.

## Principle

Appropriate contacts with relevant authorities should be maintained to ensure timely exchange of information regarding security matters, including regulatory notifications, incident reporting, and receipt of advisories. Appropriate contacts with special interest groups or other specialist security forums and professional associations should be maintained to improve knowledge of best practices, stay current with threats and vulnerabilities, and receive early warnings of attacks.

All external authority communications regarding security matters shall be conducted only by authorised personnel through documented channels. The organisation shall maintain a current, verified contact register accessible to authorised staff at all times, including during incidents when primary communication systems may be unavailable.

---

## Definitions

| Term | Definition |
|------|------------|
| **Relevant Authority** | Any government body, law enforcement agency, or regulatory authority with jurisdiction over [Organisation]'s operations or data processing activities |
| **Special Interest Group (SIG)** | Professional associations, industry forums, information sharing organisations, and security communities focused on cybersecurity topics |
| **Traffic Light Protocol (TLP)** | A standardised system created by FIRST for classifying sensitive information and controlling its distribution, using four labels: TLP:RED, TLP:AMBER, TLP:GREEN, TLP:CLEAR |
| **ISAC / ISAO** | Information Sharing and Analysis Centre / Organisation — sector-specific groups for sharing threat intelligence and security best practices |
| **Mandatory Notification** | A legally required report to authorities triggered by specific events such as a data breach or cyber incident |
| **NCSC** | National Cyber Security Centre (Nationales Zentrum fuer Cybersicherheit) — Switzerland's central competence centre for cybersecurity |
| **FDPIC** | Federal Data Protection and Information Commissioner (Eidgenoessischer Datenschutz- und Oeffentlichkeitsbeauftragter, EDOEB) — Switzerland's data protection supervisory authority |
| **Contact Register** | A maintained record of all authority and special interest group contacts, including names, roles, contact details, and communication protocols |
| **Authorised Spokesperson** | A designated individual approved to communicate with external authorities or groups on behalf of [Organisation] regarding security matters |

---

## Authority Contact Register

### Mandatory Authority Contacts

[Organisation] shall maintain active, verified contacts with the following authorities:

**Swiss Cyber and Law Enforcement Authorities**:

| Authority | Contact Purpose | When to Contact |
|-----------|----------------|-----------------|
| **NCSC** (National Cyber Security Centre) | Cyber threat reporting, vulnerability advisories, threat intelligence | Cyber incidents affecting critical functions; voluntary reporting of threats; receiving advisories |
| **Cantonal Police — Cybercrime Unit** | Criminal incident reporting, digital forensics coordination | Evidence of criminal activity (ransomware, fraud, extortion, unauthorised access) |
| **fedpol** (Federal Police) | Serious cybercrime, terrorism-related threats | Incidents involving national security, organised crime, terrorism |
| **GovCERT.ch** | Government CERT coordination | Critical infrastructure incidents (where applicable) |

**Data Protection and Regulatory Authorities**:

| Authority | Trigger | Contact Purpose |
|-----------|---------|-----------------|
| **FDPIC** (Federal Data Protection and Information Commissioner) | Personal data processing | Data breach notification (Art. 24 nFADP), regulatory inquiries, guidance requests |
| **FINMA** (Swiss Financial Market Supervisory Authority) | Financial services operations (conditional) | Regulatory incident reporting, supervisory inquiries |
| **Relevant EU DPAs** | Processing EU/EEA personal data (conditional) | GDPR Art. 33 breach notification, cross-border cooperation |

**Emergency Services**:

| Service | Contact Trigger |
|---------|-----------------|
| Fire Services | Physical security emergency affecting premises or data centre |
| Medical Services | Personnel safety emergency |
| Utility Providers (electricity, telecommunications) | Infrastructure disruption affecting IT operations |

### Contact Register Maintenance

The authority contact register shall be:

- **Owned** by the CISO, with updates coordinated through Legal Counsel.
- **Verified** quarterly — the CISO or delegate shall confirm that all contact details remain current, contact persons are still in their roles, and communication channels are operational.
- **Stored** in [Contact Management System] or equivalent secure register with version control and access logging.
- **Available offline** — a printed or locally stored copy of critical contacts (NCSC, FDPIC, cantonal police, emergency services) shall be maintained for use during incidents when primary systems may be unavailable.
- **Access-restricted** to authorised personnel only. The register may contain personal contact details of authority liaison officers and shall be classified as Internal.

> **Contact register location**: [Specify: SharePoint controlled library, ServiceNow CMDB, dedicated contacts database, or "Controlled Excel register in shared drive with quarterly integrity verification"]

---

## Mandatory Notifications

### Notification Obligations and Timeframes

Notification obligations are determined by applicable legal, regulatory, and contractual requirements. The following table sets out the primary obligations and internal target timeframes intended to ensure legal compliance.

| Event Type | Authority | Timeframe | Threshold / Trigger |
|------------|-----------|-----------|---------------------|
| **Personal data breach (CH)** | FDPIC via breach notification portal | As soon as possible (no fixed statutory deadline) | Breach likely to result in high risk to personality or fundamental rights of data subjects |
| **Cyber incident — critical infrastructure** | NCSC | 24 hours from discovery; full report within 14 days | Functionality jeopardised; data manipulation or leakage; extended undetected presence; extortion, threats, or coercion |
| **Personal data breach (EU)** | Lead Supervisory Authority | 72 hours from awareness | Unless unlikely to result in risk to rights and freedoms |
| **Criminal activity** | Cantonal Police / fedpol | Immediately upon confirmation | Evidence of crime (ransomware, fraud, extortion, theft, sabotage) |
| **Financial services incident** | FINMA | Per FINMA circular requirements | Material incident affecting regulated operations (conditional) |

**Key regulatory notes**:

- **nFADP Art. 24** does not stipulate a fixed notification deadline but requires reporting "as soon as possible". The FDPIC has published guidelines clarifying that this means without undue delay once the controller becomes aware of the breach. [Organisation] shall target notification within 72 hours as an internal standard to demonstrate diligence, even though Swiss law does not mandate this specific timeframe.
- **Swiss ISG (Information Security Act)**: Since 1 April 2025, operators of critical infrastructure must report cyberattacks to the NCSC within 24 hours of discovery. Failure to report may result in fines up to CHF 100,000 (penalties in force since 1 October 2025). [Organisation] shall assess whether it falls within the ISG's definition of critical infrastructure and comply accordingly.
- **FDPIC breach reporting portal**: Notifications shall be submitted via the FDPIC's dedicated portal at databreach.edoeb.admin.ch/report.
- **Processor obligations**: Where [Organisation] acts as a data processor, it shall notify the data controller as soon as possible of any data security breach, in addition to its own notification obligations.

### Notification Decision Process

When a potential notification trigger is identified:

1. **Initial assessment** — The CISO (or incident manager on duty) assesses whether the event meets a mandatory notification threshold, consulting Legal Counsel where the assessment is uncertain.
2. **Legal review** — Legal Counsel confirms applicable notification obligations, timeframes, and any contractual notification requirements.
3. **Notification preparation** — The authorised spokesperson prepares the notification using the relevant authority's prescribed format or portal, including:
   - Nature and circumstances of the breach or incident.
   - Categories and approximate number of affected data subjects or systems.
   - Likely consequences.
   - Measures taken or proposed to address the breach and mitigate adverse effects.
4. **Approval and submission** — Notification submitted by an authorised spokesperson (see below). Submission timestamp and confirmation recorded.
5. **Follow-up** — Full report completed within the required timeframe (e.g., 14 days for NCSC). Authority responses tracked and actioned.

Where an event triggers multiple notification obligations (e.g., a data breach that also constitutes a cyber incident), each obligation shall be addressed independently but coordinated to ensure consistent messaging.

---

## Authorised Spokespersons

### Designation of Authorised Personnel

Only designated personnel may communicate with external authorities regarding [Organisation]'s security matters. Unauthorised contact with authorities regarding security matters is prohibited.

| Topic | Primary Spokesperson | Backup Spokesperson |
|-------|---------------------|---------------------|
| **Security incidents and cyber events** | CISO | Deputy CISO or IT Manager |
| **Data protection matters and breach notification** | DPO (or CISO where no dedicated DPO) | Legal Counsel |
| **Regulatory and legal inquiries** | Legal Counsel | CFO |
| **Criminal matters and law enforcement** | CISO (with Legal Counsel) | CEO |
| **Media inquiries regarding security** | Communications Director (or CEO) | CISO |
| **Emergency services coordination** | Facilities Manager | CISO |

### Communication Rules

- **No employee shall contact authorities** regarding [Organisation]'s security matters without prior authorisation from the CISO or Legal Counsel, except for immediate life-safety emergencies.
- **All authority communications shall be documented** — a record of date, time, authority contacted, contact person, subject, content summary, and any commitments made shall be maintained in the communication log.
- **Legal Counsel shall review** all communications involving potential legal liability, regulatory filings, or responses to formal authority requests before submission.
- **Classified or confidential information** requires explicit CISO and Legal Counsel approval before disclosure to any authority, even where a notification obligation exists. Disclosure shall be limited to the minimum information necessary to fulfil the obligation.
- **Verbal communications** with authorities shall be followed up with a written summary within 24 hours, stored in the communication log.

### Response to Authority Inquiries

When [Organisation] receives an inquiry from an authority:

1. **Acknowledge receipt** within 24 hours or the next business day, whichever is sooner. Critical or time-sensitive inquiries follow the incident on-call process.
2. **Route to the appropriate spokesperson** — the recipient shall forward the inquiry to the CISO and Legal Counsel without providing any substantive response.
3. **Assess scope and obligations** — Legal Counsel determines the nature of the inquiry (informal request, formal investigation, statutory demand) and the required response.
4. **Prepare and review response** — the designated spokesperson prepares the response; Legal Counsel reviews before submission.
5. **Document and track** — all inquiries, responses, and follow-up actions recorded in the communication log with assigned owners and due dates.

---

## Special Interest Group Participation

### Participation Requirements

[Organisation] shall maintain active participation in relevant security communities to receive threat intelligence, access best practices, and contribute to collective security improvement.

**Recommended Group Categories**:

| Group Type | Swiss / International Examples | Participation Level |
|------------|-------------------------------|---------------------|
| **National CERT / CSIRT** | SWITCH-CERT, GovCERT.ch, NCSC advisory services | Information recipient; incident coordination |
| **Industry ISAC / ISAO** | SIGS ISAC (Security Interest Group Switzerland), FS-ISAC (financial services), sector-specific ISACs | Active membership; intelligence sharing |
| **Professional associations** | ISACA Switzerland, ISC2 Switzerland, Swiss Cyber Institute, OWASP | Professional development; knowledge sharing |
| **Vendor security programmes** | Security advisory lists for deployed technologies, vendor notification programmes | Alert recipient; patch intelligence |
| **International forums** | FIRST (Forum of Incident Response and Security Teams), ENISA communities | Standards development; peer exchange |

The CISO shall determine which groups are relevant based on [Organisation]'s industry sector, technology stack, threat landscape, and regulatory environment. The selection shall be reviewed annually.

### Active Participation Standards

At minimum, "active participation" means:

1. **Membership or subscription is current** — fees paid, accounts active, credentials valid.
2. **A monitored intake channel exists** — advisories and intelligence are received into a monitored mailbox, feed, or platform, not an unmonitored distribution list.
3. **Relevant advisories are reviewed** — at least weekly (or upon receipt for high-severity items) by the CISO or designated security team member.
4. **Actions and decisions are recorded** — in the ticketing system, risk register, or [GRC Tool], including "no action required" decisions with documented rationale.
5. **Intelligence is integrated** — relevant threat intelligence is fed into risk assessments, vulnerability management, and incident response planning.

**Participation activities** may include:

- Receiving and acting on threat intelligence and vulnerability advisories.
- Contributing anonymised incident data where permitted and beneficial.
- Attending conferences, workshops, and meetings.
- Sharing best practices and lessons learned (within approved boundaries).
- Participating in joint exercises, tabletop drills, and coordinated response activities.

### Participation Register

The CISO shall maintain a register of all special interest group memberships and subscriptions, recording:

| Field | Description |
|-------|-------------|
| **Group name** | Full name of the group or forum |
| **Category** | CERT, ISAC, professional association, vendor programme, other |
| **Contact person** | [Organisation]'s designated representative |
| **Membership status** | Active, pending, lapsed |
| **Cost** | Annual membership fee (if any) |
| **Value assessment** | Brief assessment of value received (reviewed annually) |
| **Last activity** | Date of last meaningful engagement |

---

## Information Sharing Protocols

### Traffic Light Protocol (TLP)

All information sharing with external parties — authorities, special interest groups, and peer organisations — shall use the Traffic Light Protocol (TLP) version 2.0, as defined by FIRST, to classify and control distribution.

| TLP Label | Sharing Rule | Use Case |
|-----------|-------------|----------|
| **TLP:RED** | Recipients only; no further sharing | Highly sensitive incident details shared in closed meetings; intelligence that could cause harm if disclosed |
| **TLP:AMBER+STRICT** | Organisation only; not shared with clients | Threat intelligence relevant to [Organisation]'s internal defences only |
| **TLP:AMBER** | Organisation and clients on need-to-know basis | Threat intelligence that may affect [Organisation]'s clients or partners |
| **TLP:GREEN** | Community sharing; not published publicly | Indicators of compromise, best practices, lessons learned shared within trusted communities |
| **TLP:CLEAR** | Unrestricted; may be shared publicly | General advisories, public vulnerability disclosures, non-sensitive best practices |

### Information Sharing Controls

Before sharing any information externally, the following controls apply:

- **Pre-disclosure review** — All information proposed for external sharing shall be reviewed by the CISO (and Legal Counsel where the information involves personal data, contractual obligations, or potential legal liability) to confirm:
  - The appropriate TLP classification has been applied.
  - No customer data, personal data, or proprietary business information is disclosed without consent or legal basis.
  - Contractual non-disclosure obligations are respected.
  - The sharing serves a legitimate security purpose.
- **Anonymisation** — Incident data shared with external groups shall be anonymised to remove identifying details of [Organisation], its clients, and affected individuals, unless disclosure is required by law or authorised by the data subjects.
- **Receiving intelligence** — Information received from external groups shall be handled according to its TLP classification. TLP:RED and TLP:AMBER information shall not be forwarded outside the designated recipients without the originator's explicit consent.
- **Record keeping** — A log of all information shared externally (excluding routine advisory receipt) shall be maintained, recording: date, recipient group, TLP classification, subject, and approving authority.

### Sharing Boundaries

**Permitted without additional approval**:

- Receiving threat intelligence and advisories from subscribed sources.
- Sharing technical indicators of compromise (IoCs) at TLP:GREEN or TLP:CLEAR.
- Participating in anonymised industry benchmarking.
- Contributing to standards development discussions.
- Attending educational events and conferences.

**Requires CISO and Legal Counsel approval**:

- Disclosing any details of [Organisation]'s security incidents (even anonymised).
- Participating in joint operations or coordinated response activities.
- Public speaking or publishing on [Organisation]'s security practices.
- Sharing information classified as TLP:AMBER or above.
- Media interviews or statements regarding security matters.

---

## Roles and Responsibilities

| Role | Contact with Authorities and Special Interest Groups Responsibilities |
|------|-----------------------------------------------------------------------|
| **CEO** | Ultimate authority for external communications; approves public statements; signs regulatory attestations |
| **CISO** | Primary authority contact for security matters; owns contact register and SIG participation register; approves information sharing; coordinates incident notifications |
| **Legal Counsel** | Reviews all authority communications involving legal liability; confirms notification obligations and timeframes; advises on disclosure boundaries |
| **DPO** | Data protection authority communications; prepares and submits FDPIC breach notifications; coordinates with EU DPAs where applicable |
| **IT Manager** | Technical liaison for NCSC and SWITCH-CERT interactions; receives and triages vendor security advisories |
| **Department Heads** | Ensure staff awareness of communication restrictions; route authority inquiries to CISO; support notification preparation within their domain |
| **All Employees** | Do not contact authorities regarding security matters without authorisation; immediately report any authority inquiry received to the CISO |

### Escalation Path

- **Authority inquiry received**: Recipient forwards to CISO and Legal Counsel without substantive response. CISO assesses and assigns spokesperson. Legal Counsel reviews response before submission.
- **Notification required**: Incident Manager notifies CISO. CISO engages Legal Counsel. Authorised spokesperson prepares and submits notification. CEO informed for significant events.
- **Media inquiry regarding security**: Recipient forwards to Communications Director and CISO. No response without CEO or Communications Director approval.
- **Threat intelligence received requiring action**: CISO triages and assigns to relevant team. Actions tracked in ticketing system.

---

## Training and Awareness

**Annual awareness training** shall be provided to all authorised spokespersons and incident response team members, covering:

- Authority contact procedures and escalation paths.
- Notification obligations and timeframes (nFADP, ISG, GDPR where applicable).
- Communication restrictions — what may and may not be disclosed.
- TLP classifications and information sharing rules.
- How to handle unsolicited authority inquiries.
- Use of the contact register and communication log.

**Role-specific training**:

- **CISO and DPO**: Regulatory notification procedures, FDPIC portal operation, NCSC reporting requirements, cross-border coordination.
- **Legal Counsel**: Disclosure boundaries, legal privilege considerations, regulatory inquiry response.
- **All employees**: Awareness that they shall not communicate with authorities on security matters without authorisation, and shall immediately forward any authority inquiry to the CISO.

Training completion tracked; target: **100% of authorised spokespersons trained annually**.

---

## Evidence

The following evidence demonstrates compliance with this policy:

| # | Evidence | Owner | Frequency |
|---|----------|-------|-----------|
| 1 | **Authority contact register** with verified contact details and quarterly update records | CISO | *Verified quarterly; updated upon change* |
| 2 | **Special interest group participation register** with membership status and annual value assessment | CISO | *Reviewed annually; updated upon change* |
| 3 | **Communication log** documenting all authority interactions (inquiries received, notifications submitted, responses) | CISO | *Per interaction; retained for 5 years* |
| 4 | **Notification records** — copies of breach notifications submitted to FDPIC, NCSC, or other authorities with submission timestamps and confirmation | CISO / DPO | *Per event; retained for 5 years* |
| 5 | **Threat intelligence intake records** — advisories received, triage decisions, and actions taken | CISO | *Per advisory; retained for 3 years* |
| 6 | **Information sharing log** — records of information shared externally, TLP classification, and approval | CISO | *Per sharing event; retained for 3 years* |
| 7 | **Offline contact list** — current printed or locally stored copy of critical authority contacts for incident use | CISO | *Updated quarterly; verified during incident exercises* |
| 8 | **Training records** for authorised spokespersons and incident response team | CISO / HR | *Annually; retained for 3 years* |
| 9 | **Quarterly contact register verification** sign-off confirming all contacts current and communication channels operational | CISO | *Quarterly; retained for 3 years* |
| 10 | **Tabletop exercise records** demonstrating notification readiness (where no real notification events occurred in audit period) | CISO | *Annually at minimum; retained for 3 years* |
| 11 | **Exception Register entries** for any deviations from contact or notification requirements | CISO | *Per exception; retained for 3 years* |
| 12 | **Annual SIG value review** documenting assessment of each membership's contribution to security posture | CISO | *Annually; retained for 3 years* |

---

# Policy Compliance

## Compliance Measurement

The information security management team will verify compliance with this policy through various methods, including but not limited to, contact register audits, notification timeliness reviews, SIG participation assessments, communication log inspections, internal and external audits, and feedback to the policy owner.

The following metrics shall be tracked and reported to the CISO quarterly:

| Metric | Target | Red Threshold |
|--------|--------|---------------|
| Authority contact register accuracy (all contacts verified current) | 100% verified quarterly | <90% or any quarter missed |
| Mandatory notification compliance (submitted within required timeframe) | 100% | Any missed or late notification |
| Special interest group participation (active in relevant groups) | All identified groups active | >1 group lapsed or unmonitored |
| Authority inquiry response (acknowledged within 24 hours) | 100% | Any inquiry unacknowledged >48 hours |
| Authorised spokesperson training completion | 100% annually | <80% trained |
| Offline contact list currency | Updated quarterly | >6 months since last update |

**Reporting requirements**:

- **Quarterly CISO dashboard**: Contact register status, notification events, SIG participation activity, inquiry response times.
- **Annual Management Review**: Full programme effectiveness assessment including notification readiness, intelligence value received from SIG participation, and improvement recommendations.

Metrics breaching red thresholds shall be escalated to the CISO for immediate attention and reported at the next Management Review.

## Exceptions

Any exception to this policy shall be approved and recorded by the CISO in advance, with documented justification and compensating controls. Exceptions shall be reported to the Management Review Team.

**Limited exceptions** may be granted for:

- Alternative contact arrangements during personnel unavailability (documented delegation with qualified backup).
- Temporary suspension of a specific SIG membership where value assessment determines low benefit (subject to annual re-evaluation).

**Not permissible** — the following exceptions shall not be granted under any circumstances:

- Failure to maintain mandatory authority contacts (NCSC, FDPIC, cantonal police).
- Non-compliance with legally mandated notification obligations.
- Unauthorised disclosure of security information to authorities or external parties.
- Removal of the offline contact list without equivalent alternative.

All exceptions shall be recorded in the Exception Register (ISMS-REG-EXCEPTIONS).

## Non-Compliance

An employee found to have violated this policy may be subject to disciplinary action, up to and including termination of employment. Unauthorised contact with authorities regarding [Organisation]'s security matters — or failure to report an authority inquiry received — shall be treated as a serious policy violation. Where a violation results in a missed mandatory notification or improper disclosure, the incident shall be escalated to Legal Counsel and Executive Management for assessment of regulatory and legal consequences.

## Continual Improvement

This policy is reviewed and updated as part of the continual improvement process. Reviews shall consider changes to regulatory requirements (including new or amended notification obligations), organisational changes affecting spokesperson designations, lessons learned from notification events and authority interactions, feedback from special interest group participation, audit findings, and developments in the threat landscape that may require new external contacts or group memberships. Nonconformities related to this policy shall be recorded and managed through the ISMS corrective action process (Clause 10.2) with root cause analysis and tracked remediation.

---

# Areas of the ISO 27001 Standard Addressed

Contact with Authorities and Special Interest Groups Policy — ISO 27001 Controls Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership and commitment | 5.1 Policies for information security |
| Clause 5.2 Policy | 5.4 Management responsibilities |
| Clause 5.3 Organisational roles, responsibilities and authorities | **5.5 Contact with authorities** |
| Clause 6.1 Actions to address risks and opportunities | **5.6 Contact with special interest groups** |
| Clause 7.3 Awareness | 5.7 Threat intelligence |
| Clause 7.4 Communication | 5.24 Information security incident management planning and preparation |
| Clause 8.1 Operational planning and control | 5.34 Privacy and protection of PII |
| Clause 9.1 Monitoring, measurement, analysis and evaluation | |
| Clause 10.2 Nonconformity and corrective action | |

**Regulatory and Legal Framework**:

| Framework | Relevance |
|-----------|-----------|
| Swiss nFADP (revDSG) Art. 24 | Data breach notification to FDPIC "as soon as possible" where breach likely to result in high risk to data subjects |
| Swiss nFADP (revDSG) Art. 24 para. 3 | Processor obligation to notify controller of data security breaches as soon as possible |
| Swiss ISG Art. 73a-79 | Mandatory reporting of cyberattacks on critical infrastructure to NCSC within 24 hours (in force since 1 April 2025; penalties since 1 October 2025, up to CHF 100,000) |
| Swiss DSV (Data Protection Ordinance) | Art. 1-3 — Minimum requirements for data security including organisational measures |
| EU GDPR Art. 33 (where applicable) | Supervisory authority notification within 72 hours of becoming aware of personal data breach |
| EU GDPR Art. 34 (where applicable) | Communication to data subjects without undue delay where breach likely to result in high risk |
| ISO/IEC 27001:2022 | Annex A Controls 5.5 and 5.6 — Contact with authorities; Contact with special interest groups |
| ISO/IEC 27002:2022 | Sections 5.5 and 5.6 — Implementation guidance for authority contacts and SIG participation |
| NIST SP 800-53 Rev 5 | IR-6 (Incident Reporting) — Reporting incidents to designated authorities; PM-15 (Security and Privacy Groups and Associations) — Contact with security groups |
| CIS Controls v8 | Control 17 (Incident Response Management) — Safeguard 17.2: Establish and maintain contact information for reporting security incidents; Safeguard 17.3: Establish and maintain an enterprise process for reporting incidents |
| FIRST TLP v2.0 | Traffic Light Protocol for classified information sharing between trusted parties |

---

<!-- QA_VERIFIED: 2026-02-07 -->
