**ISMS-OP-POL-A.5.7 — Threat Intelligence**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Threat Intelligence |
| **Document Type** | Operational Policy |
| **Document ID** | ISMS-OP-POL-A.5.7 |
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

- ISO/IEC 27001:2022 Control A.5.7 — Threat intelligence
- ISO/IEC 27002:2022 Section 5.7 — Implementation guidance
- NIST SP 800-150 — Guide to Cyber Threat Information Sharing
- NIST SP 800-53 Rev 5 PM-16 — Threat Awareness Program
- NIST SP 800-53 Rev 5 RA-3 — Risk Assessment
- NIST SP 800-53 Rev 5 SI-5 — Security Alerts, Advisories and Directives
- FIRST TLP v2.0 — Traffic Light Protocol for information sharing
- OASIS STIX v2.1 / TAXII v2.1 — Threat intelligence exchange standards

**Related Annex A Controls**:

| Control | Relationship to Threat Intelligence |
|---------|-------------------------------------|
| A.5.1 Policies for information security | Overarching policy framework governing threat intelligence requirements |
| A.5.24-28 Incident management | Threat intelligence enhances detection, investigation, and response |
| A.5.30 ICT readiness for business continuity | Threat intelligence informs continuity planning and threat preparedness |
| A.8.7 Protection against malware | Threat intelligence provides IOCs for malware detection |
| A.8.8 Management of technical vulnerabilities | Exploitation intelligence prioritises vulnerability remediation |
| A.8.15 Logging | Logs provide internal telemetry for threat intelligence analysis |
| A.8.16 Monitoring activities | Threat intelligence provides detection context and correlation rules |
| A.8.23 Web filtering | Threat intelligence provides malicious domain and URL feeds |

**Related Internal Policies**:

- Incident Management Policy
- Risk Management Policy
- Vulnerability Management Policy
- Logging Policy
- Monitoring Activities Policy (A.8.16)
- Malware Protection Policy
- Information Classification and Handling Policy

---

# Threat Intelligence Policy

## Purpose

The purpose of this policy is to establish requirements for collecting, analysing, and using information about current and emerging information security threats to enable proactive defence, inform risk management decisions, and enhance the organisation's ability to detect, prevent, and respond to security incidents.

Threat intelligence transforms raw threat data into actionable knowledge. Without structured threat intelligence, the organisation operates reactively — responding to incidents after damage has occurred rather than anticipating and preventing them. This policy ensures the organisation maintains appropriate situational awareness of the threat landscape relevant to its operations, assets, and sector.

This policy supports Swiss nFADP (revDSG) by implementing technical and organisational measures appropriate to risk to protect personal data processing integrity. Threat intelligence contributes to the data security measures required under Art. 8 nFADP by enabling proactive identification of threats to systems processing personal data. Where the organisation processes data of individuals in the EU/EEA, GDPR Art. 32 requirements for security measures including threat monitoring also apply.

## Scope

All activities related to threat intelligence collection, analysis, production, dissemination, and consumption across the organisation.

This includes:

- Collection of threat information from external and internal sources.
- Analysis and production of intelligence at strategic, tactical, and operational levels.
- Dissemination of intelligence to appropriate stakeholders.
- Integration of threat intelligence with risk assessment processes.
- Integration of threat intelligence with incident management and security monitoring.
- External sharing of threat intelligence with trusted partners and communities.

**Out of scope**: Offensive cyber operations or retaliatory actions (prohibited); law enforcement investigations (cooperation supported, not conducted); vulnerability scanning and penetration testing operations (covered under A.8.8); threat hunting procedures (covered under A.8.16); intelligence operations unrelated to information security.

## Principle

Information relating to information security threats should be collected and analysed to produce threat intelligence. Threat intelligence shall be relevant to the organisation's specific threat landscape, technically accurate, contextualised to organisational assets and risk profile, and actionable — providing clear guidance that enables the organisation to detect, prevent, or respond to identified threats.

The organisation shall maintain threat intelligence capabilities proportionate to its size, risk exposure, and sector. Not every organisation requires a dedicated Security Operations Centre (SOC) or full-time threat intelligence analysts. What every organisation requires is a structured, documented process for staying informed about threats relevant to its operations and acting on that information.

---

## Definitions

| Term | Definition |
|------|------------|
| **Threat Intelligence** | Information about current or emerging threats that has been collected, processed, and analysed to enable informed security decisions and proactive defence |
| **Strategic Intelligence** | High-level intelligence addressing broad threat trends, threat actor motivations, and sector-specific risks, supporting executive decisions and long-term security strategy |
| **Tactical Intelligence** | Intelligence describing adversary tactics, techniques, and procedures (TTPs), supporting security operations planning and defence configuration |
| **Operational Intelligence** | Actionable technical intelligence including indicators of compromise (IOCs) and detection signatures, supporting immediate detection and response operations |
| **Indicator of Compromise (IOC)** | An observable artefact — such as an IP address, domain name, file hash, or email address — indicating that a security breach has occurred or is occurring |
| **Tactics, Techniques, and Procedures (TTPs)** | Patterns of behaviour and methods used by threat actors to conduct attacks, documented in frameworks such as MITRE ATT&CK |
| **Traffic Light Protocol (TLP)** | An information sharing classification system using colour codes (TLP:RED, TLP:AMBER+STRICT, TLP:AMBER, TLP:GREEN, TLP:CLEAR) to indicate permitted sharing boundaries |
| **STIX (Structured Threat Information eXpression)** | An OASIS standard language and serialisation format for exchanging cyber threat intelligence in a structured, machine-readable manner |
| **TAXII (Trusted Automated eXchange of Intelligence Information)** | An OASIS standard application protocol for the automated exchange of cyber threat intelligence over HTTPS |
| **MITRE ATT&CK** | A globally accessible knowledge base of adversary tactics and techniques based on real-world observations, maintained by the MITRE Corporation |
| **Threat Actor** | An individual, group, or organisation conducting malicious cyber activities with identifiable intent and capability |
| **OSINT (Open-Source Intelligence)** | Threat intelligence derived from publicly available sources including security blogs, vulnerability databases, social media, and public advisories |

---

## Intelligence Types and Layers

The organisation shall produce or consume threat intelligence at three layers, each serving a distinct audience and purpose. Not all organisations will produce intelligence at every layer internally; consumption from external sources is acceptable where internal production capacity is limited.

### Strategic Intelligence

**Audience**: Executive Management, CISO, Risk Management.
**Purpose**: Inform business decisions, security investment, and long-term strategy.

Strategic intelligence shall address:

- The overall threat landscape relevant to the organisation's sector and geography.
- Threat actor motivations and capabilities targeting the organisation's industry.
- Emerging threat trends and their potential business impact.
- Regulatory and geopolitical developments affecting the threat environment.
- Peer organisation incidents and sector-wide attack campaigns.

**Production frequency**: Quarterly at minimum, or triggered by significant threat landscape changes. Where the organisation does not produce strategic intelligence internally, it shall subscribe to or access at least one source of sector-relevant strategic threat reporting (e.g., Swiss NCSC semi-annual reports, CERT advisories, or commercial strategic intelligence services).

### Tactical Intelligence

**Audience**: Security operations staff, IT administrators, incident responders.
**Purpose**: Inform defensive configurations, detection rules, and security architecture.

Tactical intelligence shall address:

- Threat actor profiles and TTPs relevant to the organisation's technology stack.
- Attack patterns and campaign analysis targeting the organisation's sector.
- Malware families and their behavioural characteristics.
- Social engineering techniques and phishing campaign patterns.
- Recommended defensive measures and detection strategies.

**Production frequency**: Monthly at minimum, or triggered by emerging threats. Where internal analysis capacity is limited, the organisation shall consume tactical intelligence from at least one structured source (e.g., MITRE ATT&CK, Swiss NCSC advisories, CERT feeds, or commercial threat reports).

### Operational Intelligence

**Audience**: Technical security staff, system administrators, SOC analysts.
**Purpose**: Enable immediate detection and blocking of known threats.

Operational intelligence shall include:

- Indicators of compromise (IOCs): malicious IP addresses, domains, URLs, file hashes, email addresses.
- Malware signatures and behavioural indicators.
- Detection rules and YARA rules.
- Blocklists for firewalls, email gateways, and web filters.

**Production frequency**: Continuously via automated feeds, with periodic analyst review (daily where a SOC is operational; weekly at minimum for organisations without a dedicated SOC).

---

## Source Categories

The organisation shall maintain threat intelligence sources across multiple categories to avoid single-source dependency and ensure comprehensive coverage. The number and depth of sources shall be proportionate to organisational size and risk exposure.

### Required Source Categories

| Category | Description | Examples | Minimum Requirement |
|----------|-------------|----------|---------------------|
| **Government / CERT** | National and sector-specific CERT advisories and alerts | Swiss NCSC (ncsc.admin.ch), GovCERT.ch, CERT-EU, US-CERT/CISA | At least one national CERT subscription |
| **Open-Source Intelligence (OSINT)** | Publicly available threat data, vulnerability databases, security research | CVE/NVD, AlienVault OTX, Abuse.ch, VirusTotal, security researcher blogs | At least two OSINT feeds |
| **Internal Telemetry** | Security events and findings from the organisation's own systems | [SIEM] alerts, firewall logs, email gateway reports, endpoint detection alerts, incident post-mortems | All available internal security tool outputs |

### Recommended Source Categories

| Category | Description | Examples | When to Implement |
|----------|-------------|----------|-------------------|
| **Commercial Platforms** | Curated, validated threat intelligence with SLA-backed quality | [Threat Intelligence Platform], Recorded Future, Mandiant, CrowdStrike | When budget allows and threat exposure justifies investment |
| **Industry Sharing (ISAC/ISAO)** | Sector-specific threat intelligence shared among peers | Financial ISAC (FS-ISAC), Health ISAC, sector-specific sharing groups | When a relevant ISAC/ISAO exists for the organisation's sector |
| **Vendor Security Advisories** | Threat and vulnerability information from technology vendors | Microsoft Security Response Centre, AWS Security Bulletins, vendor-specific feeds | For all critical technology vendors in use |

### Source Evaluation

All threat intelligence sources shall be evaluated before operationalisation and periodically thereafter. Evaluation shall consider:

- **Reliability**: The source's track record for providing accurate information.
- **Timeliness**: How quickly information is available after a threat emerges.
- **Relevance**: Whether the source covers threats applicable to the organisation's sector, geography, and technology stack.
- **Actionability**: Whether the information enables concrete defensive actions.
- **False positive rate**: The proportion of indicators that prove to be benign upon investigation.

Sources that consistently provide inaccurate, irrelevant, or excessively noisy information shall be replaced or deprioritised. Source performance shall be reviewed at least annually.

---

## Vendor-Provided Intelligence Management

Where the organisation subscribes to commercial threat intelligence services or platforms, vendor management requirements apply.

### Vendor Selection Criteria

Commercial threat intelligence vendors shall be evaluated against:

| Criterion | Evaluation Method | Acceptance Threshold |
|-----------|------------------|---------------------|
| **Intelligence quality** | Trial period review of 30-day sample data; false positive rate analysis | <10% false positive rate; >90% relevance to organisation's sector |
| **Timeliness** | Time from threat emergence to feed availability | <24 hours for critical IOCs; <72 hours for tactical intelligence |
| **Source transparency** | Vendor discloses intelligence collection methods and sourcing | Methodology documented; primary sources identified |
| **Data protection compliance** | Vendor processing of personal data in IOCs complies with nFADP/GDPR | Data processing agreement in place; documented lawful basis |
| **Platform integration** | Compatibility with organisation's security tools (SIEM, EDR, firewall) | Standard integration protocols supported (STIX/TAXII, API, syslog) |
| **Vendor stability** | Financial viability, customer base, industry reputation | Established vendor with >2 years operation; references available |

### Ongoing Vendor Performance Monitoring

| Metric | Target | Review Frequency | Owner |
|--------|--------|-----------------|-------|
| **Feed uptime** | >99% | Monthly | IT Operations |
| **False positive rate** | <10% | Quarterly | CISO |
| **True positive contribution** | >5 validated detections per quarter | Quarterly | CISO |
| **Timeliness vs. OSINT sources** | Commercial feed provides intelligence ≥24 hours earlier than free sources | Quarterly | CISO |
| **Support responsiveness** | Support inquiries resolved within vendor SLA | Per incident | IT Operations |
| **Data protection compliance** | No unauthorised personal data processing incidents | Continuous | Data Protection Advisor |

### Vendor Contract Requirements

Contracts with commercial threat intelligence vendors shall include:

- **Service level agreement (SLA)** specifying uptime, feed freshness, and support response times
- **Data processing agreement (DPA)** addressing personal data in IOCs (processor obligations under nFADP Art. 9 or GDPR Art. 28)
- **Intellectual property terms** clarifying permitted use of intelligence (internal security only; no redistribution without approval)
- **Termination and data portability** — ability to export intelligence data in standard format upon contract termination
- **Incident notification** — vendor obligation to notify organisation of any security incident affecting the intelligence service within 24 hours

### Annual Vendor Review

Commercial intelligence vendors shall be reviewed annually covering:
- Performance against SLAs and quality metrics
- Cost-benefit analysis (value delivered vs. subscription cost)
- Comparison against alternative vendors or OSINT sources
- Contract renewal recommendation with documented justification

**Review documentation retained 3 years; renewal decisions documented in vendor risk register.**

---

## Collection and Analysis

### Collection Process

The organisation shall implement a documented process for collecting threat intelligence that includes:

1. **Automated collection**: Threat feeds shall be ingested automatically where feasible, using standard protocols (STIX/TAXII where supported) or vendor-specific APIs. Automated feeds shall be directed to [SIEM] or [Threat Intelligence Platform] for centralised processing.

2. **Manual collection**: Security personnel shall review advisory sources, security news, and community forums on a defined schedule. Manual collection findings shall be documented and entered into the threat intelligence register.

3. **Internal collection**: Security events, incident findings, and forensic analysis results shall be captured as internal threat intelligence. Post-incident reviews shall explicitly identify and record IOCs and TTPs encountered.

4. **Data protection**: All collected intelligence shall comply with applicable data protection requirements. Personal data included in threat intelligence (e.g., email addresses in phishing indicators) shall be processed only for the legitimate interest of information security and retained only as long as the indicator remains operationally relevant.

### Analysis Process

Raw threat data shall be analysed before dissemination to ensure quality and relevance. Analysis shall:

- **Validate** information through multiple sources where possible.
- **Contextualise** threats against the organisation's specific assets, technology stack, and risk profile.
- **Assess** the likelihood and potential impact of identified threats to the organisation.
- **Prioritise** threats based on relevance, severity, and the organisation's exposure.
- **Produce** actionable recommendations or detection guidance.

Where the organisation does not have dedicated threat intelligence analysts, analysis responsibilities shall be assigned to the CISO or designated security personnel. Analysis need not be a full-time function for smaller organisations, but it shall be a documented, recurring activity with clear ownership.

### Quality Requirements

All threat intelligence — whether produced internally or consumed from external sources — shall meet the following quality criteria before being acted upon:

- **Relevant**: Applicable to the organisation's threat landscape, sector, and technology environment.
- **Accurate**: Validated through corroboration or source reliability assessment.
- **Timely**: Current and delivered within a timeframe that permits effective action.
- **Actionable**: Accompanied by clear guidance on detection, prevention, or response actions.

Intelligence that does not meet these criteria shall be flagged, investigated, or discarded. Source evaluation records shall document quality issues.

---

## Intelligence Data Lifecycle Management

### Retention Requirements

Threat intelligence data shall be retained according to operational and regulatory requirements:

| Intelligence Type | Retention Period | Rationale |
|-------------------|-----------------|-----------|
| **Operational IOCs** (in active detection) | As long as threat remains relevant; minimum 90 days | Active detection requires current indicators |
| **Historical IOCs** (no longer active) | 12 months after deactivation | Historical context for incident investigation; trend analysis |
| **Strategic and tactical intelligence reports** | 3 years | Risk assessment audit trail; programme maturity assessment; historical context |
| **Internal intelligence from incidents** | Per incident retention schedule (typically 5 years) | Regulatory compliance; potential legal proceedings |
| **Source evaluation records** | 3 years | Audit trail for source selection decisions |
| **Intelligence sharing agreements** | 7 years after termination | Legal record retention requirements |

### IOC Lifecycle Management

Indicators of compromise deployed to detection systems shall be managed through a lifecycle process:

1. **Ingestion** — IOC received from source, validated, and classified (TLP, threat type, severity)
2. **Deployment** — IOC deployed to relevant detection systems (SIEM, EDR, firewall, web filter)
3. **Active monitoring** — IOC generates alerts when matched; alerts triaged and investigated
4. **Review** — IOCs reviewed quarterly for continued relevance:
   - Has indicator been observed in alerts? (Active vs. dormant)
   - Is threat still current? (Intelligence source updated or deprecated?)
   - False positive rate acceptable? (If >20% false positives, consider removal)
5. **Deactivation** — IOC removed from detection systems when no longer relevant
6. **Archival** — IOC moved to historical database for trend analysis and incident investigation reference
7. **Purging** — IOC permanently deleted after retention period expires

**Automation**: Where technically feasible, IOC lifecycle management should be automated through threat intelligence platform (TIP) or SIEM functionality. Manual IOC management acceptable for organisations without TIP capability.

### Data Protection Considerations

Where threat intelligence contains personal data (e.g., email addresses in phishing indicators, IP addresses of compromised systems):

- **Lawful basis**: Processing justified under legitimate interest for information security (nFADP Art. 6 para. 2; GDPR Art. 6(1)(f) where applicable)
- **Purpose limitation**: Personal data in IOCs processed only for threat detection and incident response; not used for other purposes
- **Retention minimisation**: Personal data retained only as long as operationally necessary; IOCs containing personal data prioritised for lifecycle review
- **Access restriction**: Intelligence databases containing personal data restricted to authorised security personnel only

**DPIA**: If threat intelligence processing involves large-scale systematic monitoring or special categories of personal data, a Data Protection Impact Assessment may be required under nFADP Art. 22.

---

## Dissemination and Sharing

### Internal Dissemination

Threat intelligence shall be distributed to the appropriate audience based on intelligence type:

| Intelligence Type | Recipients | Format | Frequency |
|-------------------|------------|--------|-----------|
| **Strategic** | Executive Management, CISO, Risk Management | Briefing documents, quarterly reports | Quarterly or on significant change |
| **Tactical** | IT Operations, Security team, System administrators | Advisories, TTP summaries, defence recommendations | Monthly or on emerging threat |
| **Operational** | [SIEM] / security tools, SOC analysts, IT administrators | IOC feeds, detection rules, blocklists | Continuously (automated) or weekly (manual) |

### Escalation for Critical Threats

When threat intelligence identifies an imminent or active threat targeting the organisation or its sector:

1. **Immediate notification** to the CISO (within 1 hour of identification).
2. **Rapid assessment** of organisational exposure (within 4 hours).
3. **Emergency briefing** to affected stakeholders with recommended actions.
4. **Incident response activation** if the threat assessment warrants it (per Incident Management Policy).

### External Sharing

The organisation may share threat intelligence with trusted external parties subject to the following controls:

- **TLP classification**: All shared intelligence shall be classified using Traffic Light Protocol v2.0 (TLP:RED, TLP:AMBER+STRICT, TLP:AMBER, TLP:GREEN, TLP:CLEAR). Sharing shall not exceed the TLP designation assigned by the originator.
- **Sharing agreements**: Formal agreements (NDA, information sharing agreement, or membership terms) shall be in place before sharing with external parties.
- **Data protection**: Shared intelligence shall not include personal data beyond what is necessary for threat detection (e.g., IOCs). Where personal data is shared, a lawful basis under nFADP shall be established.
- **Regulatory reporting**: Where Swiss NCSC mandatory reporting obligations apply (critical infrastructure operators — ISG Art. 74b), the organisation shall report relevant cyber incidents to the NCSC within 24 hours per applicable requirements.

### Receiving External Intelligence

When receiving threat intelligence from external sources:

- **Respect TLP markings**: Intelligence received with TLP designations shall not be shared beyond the permitted boundaries.
- **Validate before acting**: Externally received IOCs shall be validated against the organisation's environment before deployment to blocking or detection systems to minimise false positives.
- **Acknowledge receipt**: Where sharing is bidirectional, the organisation shall acknowledge receipt and provide feedback on intelligence utility when requested.

---

## Risk Assessment Integration

Threat intelligence shall inform the organisation's risk assessment process per ISO 27001:2022 Clause 6.1. This integration is mandatory — threat intelligence that does not influence risk decisions provides limited value.

### Required Integration Points

- **Likelihood assessment**: Threat intelligence on active campaigns, exploitation activity, and threat actor targeting shall inform the likelihood estimates assigned to identified risks.
- **Impact assessment**: Intelligence on attack techniques and observed consequences in peer organisations shall inform impact assessments.
- **Risk register updates**: When threat intelligence identifies new threats or changes to existing threats, the risk register shall be updated accordingly. Each update shall reference the supporting threat intelligence source.
- **Control effectiveness**: Threat intelligence on bypassed or ineffective controls observed in the wild shall trigger re-evaluation of the organisation's control effectiveness.

### Process

1. The CISO or designated security personnel shall review strategic and tactical threat intelligence outputs at least quarterly against the current risk register.
2. New threats identified through intelligence analysis shall be submitted to Risk Management for formal risk assessment.
3. Changes to threat likelihood or impact based on intelligence shall be documented with traceable references to supporting intelligence reports.
4. Risk treatment decisions influenced by threat intelligence shall be recorded in the risk register.

### Privacy and Confidentiality Threat Assessment

Where the organisation processes personal data subject to nFADP or GDPR, threat intelligence shall specifically address threats to data confidentiality and privacy:

| Threat Category | Privacy Impact | Intelligence Requirements |
|-----------------|---------------|---------------------------|
| **Data exfiltration** | Unauthorised disclosure of personal data | IOCs for data theft malware, exfiltration techniques (DNS tunnelling, steganography), attacker infrastructure used for data staging |
| **Credential theft** | Unauthorised access to systems processing personal data | Phishing campaign indicators, credential-stealing malware signatures, compromised credential databases |
| **Insider threats** | Intentional or accidental data misuse | Behavioural indicators, privileged access abuse patterns, data access anomaly detection |
| **Third-party breaches** | Personal data compromise via processors/vendors | Intelligence on breached service providers, compromised SaaS platforms, supply chain data leakage |

**Risk register impact:**
- Risks related to personal data processing (e.g., “R-DATA-01: Unauthorised access to customer personal data”) shall be reviewed quarterly against threat intelligence findings
- Threat intelligence indicating increased targeting of data controllers in the organisation’s sector shall trigger re-assessment of data protection control adequacy
- Detection rules for data exfiltration attempts shall be updated based on observed attacker techniques

---

## Incident Management Integration

Threat intelligence shall enhance incident detection, investigation, and response per Controls A.5.24-28.

### Detection Enhancement

- IOCs from threat intelligence sources shall be deployed to detection systems ([SIEM], [EDR], email gateway, web filter) to enable automated alerting.
- Threat actor TTPs from tactical intelligence shall be translated into detection rules or monitoring use cases where feasible.
- Detection rule effectiveness shall be reviewed periodically and rules updated based on evolving intelligence.

### Investigation Support

- When a security incident occurs, available threat intelligence shall be queried for related indicators, known threat actor profiles, and attack pattern context.
- Threat intelligence context shall be included in incident investigation records to support root cause analysis and attribution assessment.

### Post-Incident Feedback

- Incident findings — including newly discovered IOCs, observed TTPs, and attack infrastructure — shall be captured as internal threat intelligence.
- Post-incident reviews shall assess whether existing threat intelligence sources provided adequate warning and whether detection rules performed as expected.
- Lessons learned shall feed back into source evaluation, detection rule tuning, and risk assessment updates.

---

## Security Monitoring Integration

Threat intelligence shall be integrated with security monitoring capabilities to enhance detection effectiveness.

### Integration Requirements

- **[SIEM] integration**: Operational IOCs shall be ingested into the [SIEM] for correlation with internal security events. Where automated ingestion is not feasible, manual IOC entry shall be performed on a defined schedule.
- **Endpoint detection**: Where [EDR] or endpoint protection platforms support threat intelligence feed integration, relevant IOCs shall be deployed to endpoint detection systems.
- **Email security**: Known phishing domains, malicious sender addresses, and attachment hashes shall be deployed to email gateway filtering rules.
- **Web filtering**: Malicious domains and URLs from threat intelligence shall be deployed to web filtering or DNS security systems.
- **Firewall rules**: Known malicious IP addresses and network indicators shall be deployed to perimeter and internal firewall blocklists, subject to false positive validation.

### Monitoring Effectiveness

The organisation shall track the following to assess integration effectiveness:

- Number of alerts generated from threat intelligence-sourced indicators.
- Confirmed true positive rate for threat intelligence-sourced alerts.
- Time from intelligence receipt to detection rule deployment.
- Coverage gaps between threat intelligence and monitoring capabilities.

---

## Availability and Business Continuity Integration

Threat intelligence shall inform business continuity planning and service availability protection per Controls A.5.29-30.

### Availability Threat Monitoring

The following threat categories shall be prioritised for detection and response due to their potential impact on service availability:

| Threat Type | Availability Impact | Detection Priority | Response Action |
|-------------|-------------------|-------------------|-----------------|
| **Distributed Denial of Service (DDoS)** | Direct service disruption | High | Activate DDoS mitigation service; traffic filtering; upstream ISP coordination |
| **Ransomware** | Data and system unavailability | Critical | Immediate containment; backup restoration; no ransom payment |
| **Wiper malware** | Permanent data destruction | Critical | Immediate isolation; forensic preservation; disaster recovery activation |
| **Supply chain attacks** | Third-party dependency disruption | High | Alternative provider evaluation; service degradation procedures |
| **Resource exhaustion attacks** | Capacity degradation | Medium | Capacity scaling; rate limiting; malicious actor blocking |

### Continuity Planning Inputs

Threat intelligence shall provide the following inputs to business continuity and disaster recovery planning:

1. **Threat scenarios** — Annual review of plausible threat scenarios (ransomware, DDoS, data destruction) based on observed industry incidents shall inform business impact analysis (BIA) and recovery strategies.

2. **Recovery time objectives (RTO) validation** — Observed attack speeds in the wild (e.g., ransomware encryption time, DDoS attack duration) shall be compared against RTO assumptions to validate recovery feasibility.

3. **Third-party dependency risks** — Intelligence on supply chain attacks or cloud service provider incidents shall trigger reviews of vendor contingency plans and alternative provider readiness.

4. **Tabletop exercise scenarios** — Annual business continuity exercises shall incorporate realistic threat scenarios derived from current threat intelligence.

**Integration process:**
- Quarterly review of availability-impacting threats by CISO and Business Continuity Manager
- Annual update of BIA threat assumptions based on intelligence findings
- Business continuity plan updates documented with reference to supporting threat intelligence

---

## Effectiveness Measurement

The organisation shall measure threat intelligence programme effectiveness to justify investment, identify improvement opportunities, and demonstrate value to stakeholders.

### Metrics

The following metrics shall be tracked and reported to the CISO quarterly:

| Metric | Target | Red Threshold |
|--------|--------|---------------|
| Active threat intelligence sources | Per minimum requirements above | Below minimum in any required category |
| Source evaluation reviews completed | 100% annually | <80% of sources reviewed |
| Risk register updates informed by threat intelligence | At minimum 1 per quarter | 0 updates in any quarter |
| IOC deployment to detection systems | Within 24 hours of validated receipt | >72 hours average deployment time |
| Threat intelligence-sourced alerts (true positive rate) | >70% | <50% |
| Strategic intelligence briefings delivered to Executive Management | Quarterly at minimum | Missed >1 quarter |
| Post-incident threat intelligence feedback completed | 100% of P1/P2 incidents | <80% of P1/P2 incidents |

### Annual Programme Review

The CISO shall conduct an annual review of the threat intelligence programme covering:

- Source portfolio adequacy and performance.
- Intelligence production quality and timeliness.
- Integration effectiveness with risk assessment, incident management, and monitoring.
- Resource adequacy (personnel, tools, budget).
- Maturity assessment against the organisation's target maturity level.
- Recommendations for programme improvement.

---

## Testing and Validation

The organisation shall test threat intelligence effectiveness to validate that intelligence sources and detection integrations perform as intended.

### Intelligence Detection Testing

| Test Type | Frequency | Method | Success Criteria | Owner |
|-----------|-----------|--------|------------------|-------|
| **IOC detection validation** | Quarterly | Deploy test IOCs (non-malicious simulation) to security tools; verify alerts generated | >90% of deployed IOCs trigger expected alerts | IT Security |
| **Threat intelligence feed integrity** | Monthly | Verify automated feeds are ingesting successfully; check for stale data | All feeds updated within 24 hours; no ingestion failures >48 hours old | IT Operations |
| **TTP detection coverage** | Semi-annually | Map organisation’s detection rules to MITRE ATT&CK; identify coverage gaps | >70% of MITRE ATT&CK techniques relevant to organisation’s threat profile covered by detection rules | CISO |
| **False positive analysis** | Quarterly | Sample 20 threat intelligence-sourced alerts; investigate true positive rate | >70% true positive rate | IT Security |
| **Escalation path test** | Annually | Simulate critical threat scenario; test escalation to CISO and Executive Management | Escalation completed within 1 hour; all stakeholders engaged | CISO |
| **Source utility assessment** | Annually | For each intelligence source, identify actionable intelligence produced in past 12 months | Each source produced ≥1 actionable intelligence item or documented reason for retention | CISO |

### Purple Team Exercises

Where resources permit, the organisation should conduct annual purple team exercises:
- **Red team** simulates attack based on current threat intelligence (realistic adversary TTPs)
- **Blue team** (detection and response) attempts to detect and respond using threat intelligence-informed detections
- **Debrief** identifies gaps in intelligence coverage, detection rules, or response procedures
- **Improvement actions** documented and tracked through corrective action process

**For organisations without purple team capability:** Tabletop exercises simulating threat intelligence-driven incident scenarios serve as an acceptable alternative.

### Testing Documentation

All testing activities shall be documented with:
- Test date, scope, and participants
- Test results (pass/fail, metrics achieved, gaps identified)
- Corrective actions assigned (where gaps identified)
- Follow-up validation of corrective actions

Testing documentation retained 3 years; reported in annual programme review.

---

## Customer Threat Intelligence Sharing (If Applicable)

*Note: This section applies only if the organisation provides managed security services or has contractual commitments to share threat intelligence with customers.*

### Customer Intelligence Deliverables

Where the organisation has contractually committed to provide threat intelligence to customers:

| Deliverable | Frequency | Content | Audience |
|-------------|-----------|---------|----------|
| **Threat briefing** | Quarterly | Strategic intelligence summary relevant to customer’s sector; emerging threats; recommended actions | Customer security leadership |
| **IOC feed** | Continuous or daily | Operational IOCs relevant to customer environment | Customer SOC or IT security |
| **Incident notifications** | Immediate | Notification of threats actively targeting customer’s sector or technology stack | Customer security contact |
| **Annual threat report** | Annually | Comprehensive threat landscape analysis; attack trend data; sector-specific threat actor profiles | Customer executive management |

### Customer-Specific Intelligence

For customers with dedicated service agreements, the organisation shall:
- Tailor intelligence to customer’s specific technology stack, geography, and threat profile
- Provide actionable recommendations specific to customer environment
- Coordinate with customer’s security team on intelligence application
- Maintain confidentiality of customer-specific intelligence (not shared with other customers unless anonymised)

### Customer Intelligence Feedback Loop

- Customers shall be invited to provide feedback on intelligence utility and relevance
- Customer feedback incorporated into quarterly intelligence programme review
- Adjustments to deliverables made based on customer needs and feedback

**Evidence**: Customer intelligence deliverables documented with delivery confirmation; customer feedback recorded; service level compliance tracked.

---

## SME Scaling Guidance

Not all organisations have dedicated threat intelligence teams or SOC capabilities. The following guidance helps smaller organisations implement threat intelligence proportionate to their resources:

### Minimum Viable Programme (Organisations Without Dedicated Security Staff)

- Subscribe to Swiss NCSC alerts and at least one relevant CERT feed.
- Subscribe to at least two free OSINT threat feeds (e.g., Abuse.ch, AlienVault OTX).
- Assign one individual (CISO, IT Manager, or designated security contact) responsibility for reviewing advisories weekly.
- Review strategic threat landscape reports from Swiss NCSC semi-annually.
- Ensure critical vendor security advisories are monitored and acted upon.
- Document threat intelligence findings in a simple register (spreadsheet is acceptable).
- Review the register quarterly against the risk register.

### Growth Path (Organisations With Emerging Security Function)

- Add commercial threat intelligence feeds relevant to sector and technology stack.
- Implement automated IOC ingestion into [SIEM] or firewall systems.
- Begin producing internal tactical intelligence from incident post-mortems.
- Join relevant information sharing communities (ISAC/ISAO) where available.
- Establish formal dissemination schedule and stakeholder briefings.
- Map observed threats to MITRE ATT&CK framework for structured analysis.

### Mature Programme (Organisations With Dedicated Security Operations)

- Deploy dedicated [Threat Intelligence Platform] for collection, analysis, and dissemination.
- Employ or contract dedicated threat intelligence analysts.
- Produce intelligence at all three layers (strategic, tactical, operational).
- Integrate threat intelligence with all security tools via automated feeds.
- Participate actively in external sharing communities.
- Conduct threat modelling exercises informed by intelligence.

---

## Roles and Responsibilities

| Role | Threat Intelligence Responsibilities |
|------|--------------------------------------|
| **Executive Management** | Approve threat intelligence policy; allocate resources; receive strategic intelligence briefings; approve sharing agreements |
| **CISO** | Programme ownership; source portfolio management; intelligence quality oversight; escalation for critical threats; annual programme review; exception approval |
| **IT Manager / Security Lead** | Day-to-day intelligence collection and review; IOC deployment to security tools; tactical and operational intelligence consumption; internal telemetry analysis |
| **Risk Management** | Integrate threat intelligence into risk assessments; update risk register based on intelligence findings; assess threat-driven risk changes |
| **Incident Response** | Apply threat intelligence during investigations; extract IOCs from incidents; provide post-incident feedback to intelligence function |
| **IT Operations** | Deploy IOCs to detection and blocking systems; maintain feed integrations; report technical anomalies identified through monitoring |
| **All Personnel** | Report suspicious activities and potential security events; complete threat awareness training; follow disseminated advisories |

### Escalation Path

- **Routine intelligence**: IT Manager / Security Lead reviews and acts. CISO informed at regular reporting intervals.
- **Elevated threat**: IT Manager / Security Lead escalates to CISO within 4 hours. CISO assesses organisational exposure and determines response.
- **Critical / imminent threat**: Immediate escalation to CISO. CISO briefs Executive Management and activates incident response if warranted.
- **Regulatory reporting**: CISO coordinates mandatory reporting to Swiss NCSC where applicable (critical infrastructure operators — within 24 hours per ISG Art. 74b).

---

## Evidence (Enhanced for Audit)

The following evidence demonstrates compliance with this policy. **For SOC 2 Type II audits**, auditors will test operating effectiveness by sampling evidence from the audit period (typically 12 months).

| # | Evidence | Owner | Frequency | Audit Trail Details |
|---|----------|-------|-----------|---------------------|
| 1 | **Threat intelligence source inventory** | CISO | *Annual review; updated upon change* | Inventory document with version history; change log showing source additions/removals with dates and approvals |
| 2 | **Source evaluation records** | CISO | *Annual per source* | Evaluation template completed for each source; scoring documented; decision to retain/replace source with justification |
| 3 | **Strategic intelligence reports** | CISO | *Quarterly minimum* | Report documents with distribution list and delivery confirmation; executive management meeting minutes showing receipt and discussion |
| 4 | **Tactical intelligence advisories** | IT Manager / Security Lead | *Monthly minimum; ad hoc* | Advisory documents with distribution timestamp; acknowledgment of receipt by key stakeholders |
| 5 | **IOC deployment records** | IT Operations | *Per deployment* | Deployment tickets or TIP logs showing: IOC identifier, source, deployment date/time, target systems, deployment method, validation test results |
| 6 | **Risk register updates** | Risk Management | *Per update* | Risk register entries with “last updated” timestamp; “intelligence source” field documenting threat intelligence report that triggered update |
| 7 | **Incident investigation records** | Incident Response | *Per P1/P2 incident* | Incident tickets with “threat intelligence context” section populated; IOC correlation results; threat actor attribution assessment (where feasible) |
| 8 | **Post-incident intelligence feedback** | Incident Response | *Per P1/P2 incident* | Incident post-mortem section documenting: new IOCs discovered, TTPs observed, intelligence gaps identified, recommendations for detection improvement |
| 9 | **External sharing agreements** | CISO | *Per agreement; annual review* | Signed NDAs, ISAC membership agreements, information sharing MoUs; annual review notes confirming agreements current |
| 10 | **TLP compliance records** | CISO | *Per sharing event* | Sharing log documenting: date, recipient, TLP classification assigned, approval (if TLP:AMBER or above), confirmation of recipient TLP acknowledgment |
| 11 | **Vendor performance reviews** | CISO | *Annual per vendor* | Vendor review template with SLA compliance data, false positive rates, cost-benefit analysis, renewal recommendation with approval signature |
| 12 | **Intelligence testing results** | IT Security | *Per test (quarterly/semi-annual)* | Test reports documenting: test date, test scope, test results (pass/fail metrics), gaps identified, corrective actions assigned with due dates |
| 13 | **Metrics dashboard** | CISO | *Quarterly* | Dashboard screenshot or report showing all KPIs; trend charts for year-over-year comparison; red threshold breaches highlighted with corrective action status |
| 14 | **Annual programme review** | CISO | *Annual* | Comprehensive review document covering source performance, integration effectiveness, maturity assessment, resource adequacy, executive presentation slides with approval signatures |

### Audit Trail Requirements

For SOC 2 Type II operating effectiveness testing, ensure:

- **Completeness**: All required evidence exists for the entire audit period (typically 12 months)
- **Accuracy**: Evidence reflects actual activities (not templated placeholders)
- **Timestamps**: All evidence clearly dated; electronic evidence includes metadata showing creation/modification dates
- **Approvals**: Where policy requires approval (e.g., exceptions, vendor selections, sharing agreements), approval documented with approver name and date
- **Population vs. Sample**: Auditors will typically test:
  - **All** strategic reports (should be 4 per year minimum)
  - **Sample** of IOC deployments (20-25 samples)
  - **All** incidents rated P1/P2 (should have threat intelligence context)
  - **All** sources (should have annual evaluation)
  - **All** vendor contracts (should have annual performance review)

---

# Policy Compliance

## Compliance Measurement

The information security management team will verify compliance with this policy through various methods, including but not limited to, threat intelligence source audits, integration effectiveness reviews, dissemination tracking, risk register cross-referencing, internal and external audits, and feedback to the policy owner.

The following metrics shall be tracked and reported to the CISO quarterly:

| Metric | Target | Red Threshold |
|--------|--------|---------------|
| Threat intelligence sources active across required categories | 100% of required categories covered | Any required category with 0 active sources |
| Source evaluation reviews completed on schedule | 100% annually | <80% of sources reviewed |
| Strategic intelligence briefings delivered | Quarterly at minimum | Missed >1 consecutive quarter |
| IOC deployment timeliness | Within 24 hours of validated receipt | >72 hours average |
| Risk register updates informed by threat intelligence | At minimum 1 per quarter | 0 updates in any quarter |
| Post-incident intelligence feedback completion (P1/P2) | 100% | <80% |

**Reporting requirements**:
- **Monthly CISO dashboard**: Active sources, recent intelligence highlights, IOC deployment status, open actions.
- **Quarterly Executive Management report**: Strategic threat landscape summary, metrics status, programme improvement recommendations.
- **Annual Management Review**: Full programme effectiveness assessment including maturity assessment, resource adequacy, and strategic recommendations.

Metrics breaching red thresholds shall be escalated to the CISO for immediate attention and reported at the next Management Review.

## Exceptions

Any exception to this policy shall be approved and recorded by the CISO in advance, with documented risk acceptance, compensating controls, and a defined review date. Common exceptions include budget constraints limiting commercial source access, technical limitations preventing automated feed integration, and newly implemented programmes that have not yet achieved target metrics. Exceptions requiring resource allocation beyond the CISO's authority shall require joint CISO and Executive Management approval. Exceptions shall be time-limited (maximum 12 months), reviewed quarterly, and reported to the Management Review Team.

## Non-Compliance

An employee found to have violated this policy may be subject to disciplinary action, up to and including termination of employment. Specific non-compliance concerns include: sharing intelligence in violation of TLP designations; failing to act on critical threat advisories within required timeframes; failing to report known threats through established channels; and unauthorised disclosure of intelligence sources or methods.

## Continual Improvement

This policy is reviewed and updated as part of the continual improvement process. Reviews shall consider changes to the threat landscape, new intelligence sources and capabilities, audit findings, regulatory changes (including Swiss NCSC reporting requirements), integration effectiveness with risk assessment and incident management, programme maturity progression, and lessons learned from threat intelligence-related incidents. Nonconformities related to this policy shall be recorded and managed through the ISMS corrective action process (Clause 10.2) with root cause analysis and tracked remediation.

---

# Areas of the ISO 27001 Standard Addressed

Threat Intelligence Policy — ISO 27001 Controls Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership and commitment | 5.1 Policies for information security |
| Clause 5.3 Organisational roles, responsibilities and authorities | **5.7 Threat intelligence** |
| Clause 6.1 Actions to address risks and opportunities | 5.24 Information security incident management planning and preparation |
| Clause 7.3 Awareness | 5.25 Assessment and decision on information security events |
| Clause 8.1 Operational planning and control | 8.7 Protection against malware |
| Clause 9.1 Monitoring, measurement, analysis and evaluation | 8.8 Management of technical vulnerabilities |
| Clause 10.2 Nonconformity and corrective action | 8.15 Logging |
| | 8.16 Monitoring activities |

**Regulatory and Legal Framework**:

| Framework | Relevance |
|-----------|-----------|
| Swiss nFADP (revDSG) | Art. 8 — Technical and organisational measures (threat intelligence as a proactive security measure protecting data processing integrity) |
| Swiss DSV (Data Protection Ordinance) | Art. 1-3 — Minimum requirements for data security |
| Swiss ISG Art. 74b | Mandatory cyber incident reporting for critical infrastructure operators (24-hour reporting to NCSC, effective April 2025) |
| EU GDPR (where applicable) | Art. 32 — Security of processing (appropriate technical and organisational measures including threat detection) |
| ISO/IEC 27001:2022 | Annex A Control 5.7 — Threat intelligence |
| ISO/IEC 27002:2022 | Section 5.7 — Implementation guidance for threat intelligence |
| NIST SP 800-53 Rev 5 | PM-16 (Threat Awareness Program), RA-3 (Risk Assessment), SI-5 (Security Alerts, Advisories and Directives) |
| NIST SP 800-150 | Guide to Cyber Threat Information Sharing |
| NIST CSF 2.0 | ID.RA (Risk Assessment), DE.AE (Adverse Events), DE.CM (Continuous Monitoring) |
| CIS Controls v8 | Control 13 (Network Monitoring and Defense) — Threat intelligence supports situational awareness and detection |
| MITRE ATT&CK | Adversary tactics and techniques knowledge base — Structured taxonomy for threat intelligence analysis |
| FIRST TLP v2.0 | Traffic Light Protocol — Standard for classifying and controlling threat intelligence sharing |
| OASIS STIX v2.1 / TAXII v2.1 | Structured threat information exchange and automated sharing protocol standards |

---

## Appendix A: Threat Intelligence Metrics Dashboard Template

**Report Period:** Q[X] [YEAR]
**Report Date:** [Date]
**Prepared by:** [CISO/Security Lead]

### Executive Summary
[2-3 paragraph summary of threat landscape, key threats identified, actions taken]

### Source Portfolio Status

| Source Category | Required | Active | Status | Action Required |
|-----------------|----------|--------|--------|-----------------|
| Government/CERT | ≥1 | [X] | Green | None |
| OSINT | ≥2 | [X] | Green | None |
| Internal Telemetry | All | [X] | Green | None |
| Commercial | [As budgeted] | [X] | Green | None |
| Vendor Advisories | All critical vendors | [X] | Amber | [Vendor X] advisory feed not monitored; action: subscribe by [date] |

### Key Performance Indicators

| Metric | Target | Q[X] Actual | Trend | Status |
|--------|--------|-------------|-------|--------|
| Active sources (all required categories) | 100% | 100% | Stable | Pass |
| Source evaluations completed | 100% annually | 25% YTD (on track) | Up | Pass |
| Strategic briefings delivered | ≥1 per quarter | 1 | Stable | Pass |
| IOC deployment timeliness | <24h average | 18h average | Improved | Pass |
| Risk register updates from intelligence | ≥1 per quarter | 3 | Up | Pass |
| True positive rate (intelligence-sourced alerts) | >70% | 78% | Up | Pass |
| Post-incident feedback completion (P1/P2) | 100% | 100% (2/2 incidents) | Stable | Pass |

### Threat Intelligence Activity Summary

- **IOCs deployed this quarter:** [X] indicators (breakdown: [Y] IP addresses, [Z] domains, [N] file hashes)
- **Alerts generated from intelligence:** [X] alerts; [Y] true positives, [Z] false positives
- **Incidents leveraging intelligence:** [X] investigations used threat intelligence context
- **Intelligence-driven risk updates:** [X] risk register entries updated based on intelligence
- **External intelligence shared:** [X] sharing events (all TLP-compliant)

### Top Threats Identified This Quarter

1. **[Threat Name]** — [Brief description, relevance to organisation, action taken]
2. **[Threat Name]** — [Brief description, relevance to organisation, action taken]
3. **[Threat Name]** — [Brief description, relevance to organisation, action taken]

### Intelligence Programme Improvements This Quarter

- [Improvement action 1 with completion status]
- [Improvement action 2 with completion status]

### Next Quarter Priorities

- [Priority action 1]
- [Priority action 2]

**Prepared by:** [Name, Role]
**Reviewed by:** [CISO]
**Distribution:** Executive Management, Risk Management, IT Operations Manager

---

<!-- QA_VERIFIED: 2026-02-08 -->
