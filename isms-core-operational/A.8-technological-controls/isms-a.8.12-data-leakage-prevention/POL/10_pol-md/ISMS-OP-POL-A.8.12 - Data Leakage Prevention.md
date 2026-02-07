**ISMS-OP-POL-A.8.12 — Data Leakage Prevention**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Data Leakage Prevention |
| **Document Type** | Operational Policy |
| **Document ID** | ISMS-OP-POL-A.8.12 |
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

- ISO/IEC 27001:2022 Control A.8.12 — Data leakage prevention
- ISO/IEC 27002:2022 Section 8.12 — Implementation guidance for data leakage prevention
- NIST SP 800-53 Rev 5 — AC-4 (Information Flow Enforcement), SC-7 (Boundary Protection), SI-4 (System Monitoring)
- CIS Controls v8 — Safeguard 3.13 (Deploy a Data Loss Prevention Solution), 3.1–3.14 (Data Protection)

**Related Annex A Controls**:

| Control | Relationship to Data Leakage Prevention |
|---------|-----------------------------------------|
| A.5.10 Acceptable use of information and other associated assets | Defines acceptable data handling and transfer practices enforced by DLP |
| A.5.12 Classification of information | Data classification drives DLP rule severity and enforcement mode |
| A.5.13 Labelling of information | Document labels enable DLP content detection and policy matching |
| A.5.14 Information transfer | Transfer policies enforced through DLP channel monitoring |
| A.5.15–16–18 Identity and access management | User identity context used in DLP rule evaluation and exception management |
| A.5.24–28 Incident management lifecycle | DLP alerts feed into incident management workflow and breach notification |
| A.5.34 Privacy and PII protection | DLP prevents unauthorised PII disclosure; privacy law constrains monitoring scope |
| A.8.10 Information deletion | DLP complements deletion controls by preventing retention on removable media |
| A.8.11 Data masking | Masking applied before sharing reduces DLP alert volume and residual risk |
| A.8.15 Logging | DLP events logged for investigation, correlation, and compliance evidence |
| A.8.16 Monitoring activities | DLP generates security events for SIEM integration and behavioural analytics |
| A.8.20–22 Network security | Network segmentation defines DLP sensor placement and inspection points |
| A.8.23 Web filtering | Web filtering and DLP jointly control web-based data exfiltration channels |
| A.8.24 Use of cryptography | Encrypted channels may require TLS inspection for DLP content analysis |

**Related Internal Policies**:

- Information Classification and Handling Policy
- Acceptable Use Policy
- Incident Management Policy
- Logging and Monitoring Policy
- Network Security Policy
- Privacy and PII Protection Policy
- Web Filtering Policy

---

# Data Leakage Prevention Policy

## Purpose

The purpose of this policy is to establish requirements for data leakage prevention (DLP) controls that detect, prevent, and respond to unauthorised disclosure, transfer, or exfiltration of sensitive information from organisational systems, networks, and endpoints. DLP controls address both malicious exfiltration (insider threats, compromised accounts, advanced persistent threats) and accidental disclosure (user error, misconfiguration, misdirected communications).

This policy supports Swiss nFADP (revDSG) Art. 8 by implementing technical and organisational measures appropriate to risk to protect personal data processed by the organisation. DLP monitoring is implemented in compliance with Swiss employment law, specifically Art. 26 ArGV 3 (prohibition of behaviour surveillance systems) and Art. 328b CO (proportionate processing of employee data). Where the organisation processes data of individuals in the EU/EEA, GDPR Art. 32 (security of processing) and Art. 88 (processing in employment context) requirements also apply.

## Scope

This policy applies to all information assets classified as Internal, Confidential, or Restricted per the organisation's data classification scheme. This includes:

- All systems, applications, networks, endpoints, and services that process, store, or transmit organisational information.
- All data egress channels: email (SMTP, webmail), web (HTTP/HTTPS uploads), endpoints (USB, local storage, printing), network (file transfer protocols), cloud services (SaaS, cloud storage), mobile devices (corporate and BYOD), and application APIs.
- All organisational personnel (employees, contractors, temporary staff) with access to organisational information.
- All third-party service providers and cloud services handling organisational data.
- All deployment models (on-premises, hybrid, cloud-native).

**Out of scope**: Public information requiring no DLP protection. Physical security of paper documents (covered by A.7.x Physical Security). Backup and archival processes (covered by A.8.13 Information Backup). Data retention and deletion (covered by A.8.10 Information Deletion). Data masking and anonymisation (covered by A.8.11 Data Masking). Information security controls unrelated to data exfiltration (access control, authentication, and patching are addressed by their respective controls).

## Principle

Data leakage prevention measures should be applied to systems, networks, and any other devices that process, store, or transmit sensitive information (ISO 27001:2022 Control A.8.12).

The organisation shall implement DLP controls proportionate to the sensitivity of the information being protected and the risk of unauthorised disclosure. DLP controls shall be classification-driven — protection requirements escalate with data sensitivity. The organisation shall balance security monitoring with employee privacy rights, ensuring that DLP monitoring is transparent, proportionate, and focused on data protection rather than employee behaviour surveillance.

DLP controls shall not be used for employee performance monitoring, time tracking, or any purpose other than information security and data protection.

---

## Data Classification Integration

DLP controls shall be applied based on the organisation's data classification scheme. Classification determines the enforcement mode, channel coverage, and response priority for each data category.

**Classification-Based DLP Protection**:

| Classification Level | DLP Requirement | Enforcement Mode |
|---------------------|-----------------|------------------|
| **Restricted** | Full DLP monitoring and blocking across all egress channels | Block and alert |
| **Confidential** | DLP monitoring and blocking on high-risk channels (email, web, endpoint, cloud) | Block or prompt user with justification |
| **Internal** | DLP monitoring on primary egress channels (email, web) | Monitor and alert (detection without automatic blocking) |
| **Public** | No DLP controls required | Not applicable |

**Sensitive Data Categories Requiring DLP Protection**:

| Data Category | Examples | Regulatory Driver |
|--------------|----------|-------------------|
| **Personal Data (PII)** | Names, addresses, national IDs, AHV numbers, phone numbers | Swiss nFADP, GDPR (where applicable) |
| **Employee Data** | HR records, payroll, performance reviews, health information | Swiss nFADP Art. 328b CO |
| **Authentication Credentials** | Passwords, API keys, tokens, certificates, SSH keys | ISO 27001 A.5.17 |
| **Intellectual Property** | Source code, designs, patents, trade secrets, strategic plans | Business risk |
| **Customer Data** | Customer lists, contracts, pricing, communications | Contractual obligations |
| **Financial Data** | Bank account numbers, payment data, financial statements | Business risk, contractual |

**Data Identification Methods**:

The organisation shall implement multiple identification methods to detect sensitive information in transit:

- **Content inspection**: Pattern matching, regular expressions, and keyword detection for structured data (e.g., credit card numbers, national IDs, AHV numbers).
- **Document labelling**: Classification metadata embedded in files (headers, footers, properties) enabling DLP to identify sensitive documents regardless of content.
- **Contextual analysis**: Evaluation of source system, user role, destination, transfer volume, and time of day to assess risk level.
- **Fingerprinting** (recommended): Hash-based tracking for high-value documents such as source code, design specifications, and strategic plans.

The organisation shall maintain an inventory of sensitive data requiring DLP protection, reconciled quarterly against the asset inventory (A.5.9). Specific detection patterns, regex rules, and classification labels shall be documented and maintained by the Security Team.

---

## Channel Protection

The organisation shall implement DLP controls across all data egress channels to prevent unauthorised information disclosure. Channel coverage shall be verified through technical testing at least quarterly.

### Email Protection

All outbound email (SMTP and webmail) shall be subject to DLP content inspection:

- Scan message bodies and attachments for sensitive content matching DLP detection rules.
- Validate recipient domains: distinguish internal, trusted external, and untrusted external recipients.
- Block or quarantine messages containing Restricted data to external recipients.
- Alert on Confidential data to external recipients (block or prompt user depending on classification and destination).
- Support encryption (S/MIME, TLS) for approved sensitive email where business need exists.
- Monitor browser-based webmail services (e.g., Gmail, Outlook.com, Yahoo Mail) to prevent bypass of SMTP-based DLP controls.

### Web and Cloud Channel Protection

Web-based data egress channels shall be monitored and controlled:

- **Web uploads**: Monitor and control file uploads to cloud storage services (e.g., Dropbox, Google Drive, personal OneDrive accounts). Approved corporate cloud storage [Cloud Storage Platform] shall be distinguished from personal or unapproved services.
- **Cloud applications**: Integrate [CASB] (Cloud Access Security Broker) or equivalent for SaaS application monitoring (e.g., Microsoft 365, Google Workspace). Monitor data sharing, external collaboration, and cloud-to-cloud transfers.
- **Web forms**: Monitor paste and form-fill activity on external web forms where risk-appropriate.
- **TLS inspection**: Where legally permissible and technically feasible, inspect encrypted web traffic at the internet gateway to detect sensitive content in HTTPS uploads. TLS inspection shall comply with privacy requirements and be documented in the organisation's privacy notice.

### Endpoint Protection

Endpoint DLP controls shall be deployed on all managed devices:

- **Removable media**: Monitor and control file transfers to USB drives, external hard drives, SD cards, and other removable storage. Block unauthorised removable media usage for Restricted and Confidential data. Approved removable media (e.g., encrypted corporate USB devices) shall be documented.
- **Local storage**: Monitor file write operations to local disk, network shares, and offline storage for sensitive data.
- **Printing**: Monitor print jobs for Restricted data. Print-to-PDF and virtual printer activity shall be included in monitoring scope.
- **Screenshots and clipboard** (risk-based): Where the risk assessment justifies it, monitor screen capture tools and clipboard operations for Restricted data. This control shall be applied only to specific high-risk roles or data sets, not organisation-wide.
- **Offline enforcement**: Endpoint DLP agents shall enforce policies when the device is disconnected from the corporate network.
- **Shadow IT detection**: Detect unapproved cloud storage, messaging, and file-sharing applications installed on managed endpoints.

### Network Protection

Network-level DLP controls shall monitor data flows at egress points:

- Monitor network traffic at internet gateways and cloud connection points.
- Monitor file transfer protocols (FTP, SFTP, SCP, rsync) for sensitive data transfers.
- Detect data exfiltration via covert channels (DNS tunneling, ICMP exfiltration, steganography) where the threat assessment identifies this risk.
- Integrate DLP alerts with firewall, proxy, and [SIEM] for correlation and investigation.

### Mobile Device Protection

Corporate data on mobile devices shall be protected:

- Integrate DLP with [MDM] (Mobile Device Management) to enforce data protection policies on corporate mobile devices.
- Containerise corporate applications and data on BYOD devices to prevent data leakage to personal applications.
- Monitor email and document sharing from mobile devices.
- Apply conditional access policies that restrict sensitive data access to compliant devices.

### Coverage Verification

The organisation shall verify DLP channel coverage through technical testing at least quarterly. Coverage gaps shall be documented with:

- Gap description and affected systems or users.
- Risk assessment of the gap.
- CISO approval for risk acceptance (if applicable).
- Remediation plan with timeline (if not accepted).

Acceptable coverage exceptions (documented and CISO-approved): guest networks with no access to sensitive data; dedicated B2B partner connections with alternative controls; air-gapped networks with no internet connectivity; specific user groups with documented and approved exceptions (e.g., legal counsel handling privileged communications).

---

## Monitoring and Detection

The organisation shall implement continuous monitoring to detect data leakage attempts and policy violations.

**Detection Modes**:

| Mode | Description | Use Case |
|------|-------------|----------|
| **Monitor only** | Log and alert without blocking | Initial deployment phase, low-risk channels, tuning period |
| **Prompt user** | Require user justification before allowing transfer | Confidential data transfers to external recipients |
| **Block** | Prevent data transfer and alert security team | Restricted data to untrusted destinations, credential leakage |
| **Quarantine** | Hold transfer for security team review | Suspected malicious exfiltration, ambiguous cases |

**Alert Priority and Response Times**:

| Priority | Trigger Examples | Response Time |
|----------|-----------------|---------------|
| **Critical** | Restricted data exfiltrated externally; credential leakage; high-volume bulk transfer | Immediate (< 15 minutes) |
| **High** | Confidential data to untrusted domain; privileged user policy violation; repeated violations | < 1 hour |
| **Medium** | Confidential data to approved external party; bulk file transfer within normal business context | < 4 hours |
| **Low** | Internal data to external; informational alerts; false positive candidates | < 24 hours |

**DLP Event Logging**:

All DLP events shall be logged with the following information:

- Timestamp (UTC, ISO 8601 format).
- User identity (username, employee ID).
- Source system (hostname, IP address, device identifier).
- Destination (recipient email, URL, external service, removable media identifier).
- Data classification triggered (Restricted, Confidential, Internal).
- Detection method (content inspection, labelling, contextual analysis).
- Action taken (blocked, allowed, quarantined, user-justified).
- Data sample (first 100 characters or sanitised excerpt — limited to what is necessary for investigation, in compliance with privacy requirements).

**Log Retention**:

- DLP security events (blocked transfers, policy violations, critical alerts): 12 months minimum.
- DLP operational logs (allowed transfers, informational events): 90 days minimum.
- Extended retention where regulatory requirements mandate longer periods.
- Logs protected with integrity and confidentiality controls per A.8.15.

**Behavioural Analytics** (recommended): Where the organisation deploys user and entity behaviour analytics (UEBA), DLP data shall be correlated with baseline user activity to detect anomalous transfer patterns (e.g., unusual volume, unusual destination, unusual time). Behavioural analytics shall comply with the employee monitoring legal requirements defined in this policy.

**Threat Intelligence Integration** (recommended): DLP systems should integrate with threat intelligence feeds to identify known exfiltration indicators (command-and-control domains, malware signatures, APT techniques documented in MITRE ATT&CK).

---

## DLP Incident Response

DLP security incidents shall follow the organisation's incident management process (A.5.24-28) with the following DLP-specific requirements.

**DLP Incident Classification**:

| Severity | Indicators | Initial Actions |
|----------|-----------|-----------------|
| **Critical** | Restricted data confirmed exfiltrated; credentials leaked externally; insider threat indicators; APT exfiltration patterns | Block user; isolate endpoint; notify CISO and DPO; initiate incident response |
| **High** | Confidential data to untrusted recipient; bulk sensitive data transfer; repeated policy violations by same user | Block transfer; investigate user activity; escalate to Security Team lead |
| **Medium** | Confidential data to approved external party via unapproved channel; user error with limited exposure | Contain transfer; interview user; assess scope; remediate |
| **Low** | False positive; policy tuning required; user clarification needed | Log; tune DLP rule; communicate with user if needed |

**Response Workflow**:

1. **Detection**: DLP system generates alert based on policy violation.
2. **Triage**: Security Team classifies incident severity, determines scope, and initiates containment.
3. **Containment**: Block user account, isolate endpoint, revoke credentials, or quarantine transfer as appropriate.
4. **Investigation**: Root cause analysis (malicious vs. accidental), scope determination (data volume, sensitivity, recipients, exposure duration), forensic evidence collection.
5. **Eradication**: Credential rotation (if credentials leaked), malware remediation (if exfiltration via malware), access revocation.
6. **Recovery**: Restore normal operations, adjust DLP policy, re-enable user with appropriate controls.
7. **Post-incident review**: Lessons learned (within 30 days), DLP policy tuning, control improvement recommendations.

**Regulatory Breach Notification**:

Where DLP incidents constitute personal data breaches, the organisation shall follow notification requirements:

| Regulation | Requirement | Timeline |
|-----------|-------------|----------|
| **Swiss nFADP** | Art. 24 — Notify FDPIC if breach poses high risk to data subjects | Without undue delay |
| **EU GDPR** (where applicable) | Art. 33 — Notify supervisory authority | 72 hours |
| **GDPR Data Subjects** | Art. 34 — Notify individuals if high risk | Without undue delay |

The Data Protection Officer (DPO) or designated privacy lead shall be consulted for all DLP incidents involving personal data to determine breach notification obligations.

**DLP-to-Incident-Management Integration**: Critical and High severity DLP events shall automatically create incident tickets in [ITSM Platform] (e.g., ServiceNow, Jira Service Management, or equivalent). Tickets not acknowledged within the response SLA shall auto-escalate per incident management procedures.

---

## Employee Monitoring Legal Requirements

DLP monitoring constitutes a form of employee monitoring under Swiss law. The organisation shall comply with the following legal requirements before deploying and operating DLP controls.

### Swiss Legal Framework

**Art. 26 ArGV 3 (Ordinance 3 to the Employment Act)**: Monitoring and surveillance systems shall not be used if their sole or primary purpose is to monitor employee behaviour. DLP systems are permissible because their primary purpose is protecting organisational data from unauthorised disclosure — not monitoring individual employee conduct. However, DLP implementation must demonstrably serve a data protection objective, and any incidental monitoring of employee behaviour must be proportionate.

**Art. 328b CO (Swiss Code of Obligations)**: The employer may process data concerning employees only insofar as it relates to the employee's suitability for the employment relationship or is necessary for the performance of the employment contract. DLP monitoring data shall be processed only for information security purposes. DLP data shall not be used for:

- Employee performance evaluation or ranking.
- Time and attendance tracking.
- Personal browsing or communication surveillance.
- Any purpose unrelated to data security and leakage prevention.

**Swiss nFADP (FADP) Principles**:

- **Lawfulness**: DLP monitoring must have a legitimate basis (protecting organisational data is a legitimate interest).
- **Proportionality**: Monitoring scope shall be limited to what is necessary for data protection. The organisation shall not monitor more broadly than required.
- **Purpose limitation**: Data collected through DLP shall be used only for security purposes, not repurposed for other objectives.
- **Transparency**: Employees shall be informed about DLP monitoring before it is activated.

### EU GDPR Requirements (Where Applicable)

Where the organisation processes data of individuals in the EU/EEA:

- **Art. 6(1)(f) Legitimate Interest**: DLP monitoring relies on the legitimate interest of protecting organisational data, balanced against employee privacy rights.
- **Art. 32 Security of Processing**: DLP is an appropriate technical measure for protecting personal data.
- **Art. 88 Processing in Employment Context**: DLP monitoring must comply with national employment law in each EU jurisdiction where the organisation operates.

### Proportionality Assessment

The organisation shall conduct a proportionality assessment before deploying DLP controls. The assessment shall verify that:

**Proportionate (permissible)**:
- Monitoring egress channels for sensitive data patterns (email attachments, web uploads, USB transfers).
- Logging DLP alerts with limited retention (90 days routine, 12 months security events).
- Restricting access to DLP logs to Security Team, CISO, and DPO on a need-to-know basis.
- Deploying in monitor-only mode initially before enabling blocking.
- Limiting data samples in logs to the minimum necessary for investigation.

**Disproportionate (not permissible)**:
- Recording all email content indefinitely regardless of sensitivity.
- Monitoring all web browsing activity without risk-based scope limitation.
- Keystroke logging or continuous screen recording without specific documented justification.
- Allowing HR or line managers to browse DLP alerts for performance management.
- Monitoring personal devices for non-work activity.
- Using DLP data for employee evaluation or disciplinary actions unrelated to data security.

### Transparency Requirements

The organisation shall inform all employees about DLP monitoring through:

1. **Employment contracts or addenda**: Clear statement that DLP monitoring is in place, its scope, purpose, and data retention periods.
2. **Privacy notice / employee handbook**: Detailed explanation of what is monitored, what is not monitored, how data is used, and who has access.
3. **Acceptable use policy**: Explicit prohibition against data exfiltration, examples of prohibited activities, consequences of violations, and the exception process.
4. **Security awareness training**: Annual training module covering DLP purpose, user responsibilities, exception requests, and reporting.
5. **Works council consultation** (where applicable): In jurisdictions requiring co-determination, the works council shall be consulted before deploying DLP monitoring.

**Critical**: Failure to provide transparency may render DLP monitoring unlawful. DLP monitoring shall not be activated until employee notification has been completed and documented. The organisation shall retain evidence of employee notification (signed acknowledgments, training completion records, privacy notice distribution records).

### Enforcement Risk

Non-compliance with employee monitoring requirements exposes the organisation to:

- **Swiss nFADP**: Fines up to CHF 250,000 for individual violations; FDPIC enforcement actions.
- **EU GDPR**: Fines up to EUR 20,000,000 or 4% of annual global turnover.
- **Employment law**: Unlawful monitoring may be grounds for employee claims under personality rights (Art. 28 ZGB); DLP evidence obtained unlawfully may be inadmissible in disciplinary proceedings.

---

## User Awareness and Acceptable Use

All personnel shall be informed of DLP controls and their responsibilities.

**User Responsibilities**:

- Handle sensitive data according to its classification and the acceptable use policy.
- Use approved channels for data transfers (corporate email, approved cloud storage, encrypted transfer tools).
- Request exceptions through the formal exception process for legitimate business needs that require DLP policy deviation.
- Report false positives and usability issues to the Security Team or Help Desk.
- Complete annual DLP awareness training.

**Prohibited Activities**:

- Attempting to bypass DLP controls through proxies, encryption of data to avoid inspection, use of unapproved cloud services, or any other circumvention method.
- Transferring Restricted or Confidential data to personal email accounts, personal cloud storage, or unapproved external services.
- Disabling or tampering with endpoint DLP agents.
- Sharing DLP exception credentials or approved transfer methods with unauthorised individuals.

Violations of DLP policy shall be subject to disciplinary action in accordance with HR policy. Deliberate or repeated attempts to circumvent DLP controls may result in termination of employment.

**If DLP Blocks a Transfer**:

1. Verify the data classification — is this actually sensitive data?
2. Use an approved transfer method (corporate email with encryption, approved cloud sharing, secure file transfer).
3. If the transfer is a legitimate business need, submit an exception request to the Security Team.
4. Contact the Help Desk for urgent assistance or to report a false positive.

---

## DLP Performance and Tuning

The organisation shall track DLP effectiveness through key performance indicators and continuously tune DLP rules to reduce false positives while maintaining detection coverage.

**Performance Metrics**:

| Metric | Target | Acceptable Range | Review Frequency |
|--------|--------|------------------|------------------|
| False positive rate | < 5% of total alerts | < 10% maximum | Monthly |
| Alert response SLA compliance | > 95% within target times | > 90% minimum | Weekly |
| Channel coverage (critical egress paths) | 100% | > 95% minimum | Quarterly |
| Incident detection rate (Restricted data) | 100% of exfiltration attempts | > 98% minimum | Per incident review |
| Policy tuning effectiveness | > 20% FP reduction per tuning cycle | Positive trend required | Quarterly |
| User-reported issues | < 10 per month | < 20 maximum | Monthly |

**Tuning Process**:

- **Monthly**: Security Team reviews false positive trends and adjusts detection rules.
- **Quarterly**: Comprehensive review of DLP rule effectiveness, coverage gaps, and emerging data types.
- **Per incident**: Post-incident review identifies detection rule improvements and coverage enhancements.
- **Annually**: Full DLP programme review as part of management review (ISO 27001 Clause 9.3), including technology assessment and vendor evaluation.

**Below-Target Response**: If metrics fall below the acceptable range for two consecutive measurement periods, the CISO shall conduct a root cause analysis within 30 days, implement a corrective action plan, and report remediation status to Executive Management.

---

## Exception Management

Exceptions to DLP policy requirements shall be requested in writing and shall include:

- Specific requirement(s) requiring exception.
- Business justification and use case description.
- Risk assessment (likelihood of data leakage, impact if leaked).
- Compensating controls (encryption, enhanced monitoring, limited scope, time-bound access).
- Requested exception duration (maximum 12 months; one-time transfers may be approved without ongoing exception).

**Approval Authority**:

| Exception Type | Approval Required |
|---------------|-------------------|
| Single one-time transfer | Security Team Lead |
| Individual user exception | Security Team Lead + Line Manager |
| Department or group exception | CISO + Department Head |
| Channel exception (disable monitoring for a channel) | CISO + CIO |
| Data classification exception (reduce protection for a data category) | CISO + Executive Management |

**Restrictions**: The following exceptions are not permitted under any circumstances:

- Disabling DLP protection for Restricted data without compensating controls.
- Bypassing DLP for credential transfers (passwords, API keys, certificates).
- Permanent exceptions without documented compensating controls and regular review.

All active exceptions shall be recorded in the DLP Exception Register (format: DLP-EX-YYYY-NNN), reviewed at least quarterly, and revoked when the business justification no longer applies or the risk profile changes.

---

## Definitions

| Term | Definition |
|------|------------|
| **CASB** | Cloud Access Security Broker — a security policy enforcement point between cloud service consumers and cloud service providers |
| **Content inspection** | Analysis of data content to detect sensitive information using pattern matching, keyword detection, and regular expressions |
| **Contextual analysis** | Evaluation of data transfer context (source, destination, user role, volume, timing) to assess risk |
| **Data leakage** | Unintentional or unauthorised disclosure of sensitive information to external or unauthorised internal parties |
| **Data leakage prevention (DLP)** | Technologies, processes, and policies designed to detect, prevent, and respond to unauthorised data disclosure |
| **Detection mode** | Operational mode determining DLP response: monitor only, prompt user, block, or quarantine |
| **Egress channel** | Any communication path through which data can leave the organisation's control (email, web, endpoint, network, cloud, mobile, API) |
| **Exfiltration** | Unauthorised transfer of data from organisational systems to external locations or actors |
| **False negative** | Data leakage that occurs despite DLP controls (bypassed or undetected) |
| **False positive** | Legitimate business activity incorrectly identified as a DLP policy violation |
| **Fingerprinting** | Hash-based document tracking that enables DLP to identify specific documents regardless of filename or format changes |
| **Insider threat** | Security risk posed by individuals with authorised access who intentionally or unintentionally cause data disclosure |
| **MDM** | Mobile Device Management — technology for managing and securing mobile devices accessing corporate data |
| **Proportionality** | Legal requirement that security monitoring must be proportionate to the legitimate security objective and not excessively intrude on employee privacy |
| **Quarantine** | Temporary holding of data transfers pending security team review before release or permanent blocking |
| **SIEM** | Security Information and Event Management — platform for centralised log collection, correlation, and security alerting |
| **TLS inspection** | Decryption and re-encryption of TLS-encrypted traffic at a network gateway for DLP content analysis |
| **Transparency** | Legal obligation to inform employees about monitoring activities before activation |

---

## Roles and Responsibilities

| Role | Responsibilities |
|------|-----------------|
| **CISO** | Policy ownership; DLP programme oversight; approval of high-risk exceptions and channel exceptions; escalation of critical DLP incidents to Executive Management; annual policy review; budget ownership for DLP technology |
| **Information Security Manager** | Day-to-day policy maintenance; exception review; security monitoring and incident investigation; audit coordination; quarterly compliance reporting to CISO |
| **Data Protection Officer (DPO)** | Review DLP monitoring for proportionality and transparency compliance; advise on breach notification obligations (nFADP Art. 24, GDPR Art. 33/34); approve DLP deployment from privacy perspective; conduct or review legitimate interest assessments |
| **Security Team** | Deploy and maintain DLP solutions across all channels; configure detection rules and policies; monitor alerts and respond to incidents; process exception requests; tune policies to reduce false positives; conduct coverage assessments |
| **IT Operations / Network Team** | Deploy and maintain DLP infrastructure; ensure network topology supports DLP coverage (traffic routing, TLS inspection points); maintain DLP system availability and performance; coordinate with Security Team on network changes |
| **Data Owners / System Owners** | Classify data within their domain; define protection requirements; review DLP incidents involving their data; approve exceptions for business-justified transfers |
| **HR** | Ensure employment contracts include DLP monitoring acknowledgment; coordinate on disciplinary actions for policy violations; support transparency requirements (privacy notices, employee handbook updates) |
| **Legal / Compliance** | Review DLP policies for legal compliance (employment law, data protection law); advise on regulatory interpretation; support incident investigations requiring legal expertise |
| **All Personnel** | Comply with DLP policies and acceptable use requirements; report false positives and usability issues; use exception process for legitimate business needs; complete annual DLP awareness training; do not attempt to bypass DLP controls |

---

## Evidence

The following evidence demonstrates compliance with this policy:

| # | Evidence | Owner | Frequency | Retention |
|---|----------|-------|-----------|-----------|
| 1 | **DLP solution inventory** with deployment scope, channel coverage, and version information | Security Team | Maintained continuously; reviewed quarterly | Life of deployment + 3 years |
| 2 | **Data classification inventory** with sensitive data categories, detection rules, and DLP rule mappings | Security Team / Data Owners | Maintained continuously; reconciled quarterly against asset inventory | 3 years |
| 3 | **Channel coverage assessment** with test results per channel (email, web, endpoint, network, cloud, mobile) | Security Team | Quarterly | 3 years |
| 4 | **DLP alert and incident log** (blocked transfers, policy violations, critical alerts, incident reports) | Security Team | Continuous | Security events: 12 months; operational logs: 90 days |
| 5 | **DLP performance metrics** (false positive rate, SLA compliance, coverage, detection rate, tuning effectiveness) | Security Team / CISO | Monthly metrics; quarterly review | 3 years |
| 6 | **DLP exception register** (requests, approvals, compensating controls, expiry dates, review records) | Security Team Lead | Maintained continuously; reviewed quarterly | Exception duration + 3 years |
| 7 | **Proportionality assessment** documenting that DLP monitoring is proportionate to security objective | DPO / CISO | Before deployment; reviewed annually | Life of deployment + 3 years |
| 8 | **Employee notification records** (signed contracts/addenda, privacy notice distribution, acceptable use acknowledgments) | HR / Legal | Per onboarding; annually for awareness training | Employment duration + 3 years |
| 9 | **DLP awareness training completion records** | CISO / HR | Annually | Employment duration + 3 years |
| 10 | **DLP incident response records** (timeline, containment, investigation, remediation, lessons learned) | Security Team | Per incident | 3 years |
| 11 | **Breach notification records** (regulatory notifications filed, data subject notifications sent) | DPO / Legal | Per incident | 7 years |
| 12 | **DLP rule tuning log** (rules changed, false positive reduction, justification, approval) | Security Team | Per change | 3 years |
| 13 | **Works council consultation records** (where applicable) | HR | Before deployment; per scope change | Life of deployment + 3 years |
| 14 | **DLP log access control records** (who has access, justification, review records) | IT Operations / Security Team | Maintained continuously; reviewed quarterly | 3 years |

---

# Policy Compliance

## Compliance Measurement

The information security management team will verify compliance with this policy through various methods, including but not limited to, DLP system reports, channel coverage assessments, incident response records, exception register reviews, employee notification audits, internal and external audits, and feedback to the policy owner.

**Compliance Metrics**:

| Metric | Target | Measurement Frequency |
|--------|--------|-----------------------|
| DLP channel coverage (critical egress paths) | >= 95% | Quarterly |
| DLP alert response within SLA | >= 95% | Weekly |
| False positive rate | < 10% | Monthly |
| Active exceptions reviewed within schedule | 100% | Quarterly |
| Employee DLP awareness training completion | >= 95% | Annually |
| Employee monitoring transparency documentation complete | 100% | Annually |
| Proportionality assessment current and approved | 100% | Annually |

**Compliance Scoring**:

| Component | Weight | Calculation |
|-----------|--------|-------------|
| Channel Coverage | 30% | (Channels with verified DLP coverage) / (Total critical egress channels) x 100 |
| Incident Response Effectiveness | 25% | (Incidents responded within SLA) / (Total incidents) x 100 |
| Policy Tuning & False Positive Management | 20% | Inverse of false positive rate + tuning improvement trend |
| Legal Compliance (transparency, proportionality) | 15% | (Completed legal requirements) / (Total legal requirements) x 100 |
| Exception Management | 10% | (Exceptions reviewed on schedule) / (Total active exceptions) x 100 |

**Non-Compliance Handling**: Below 70% requires immediate CISO escalation and remediation plan within 30 days. 70-89% requires Information Security Manager oversight with monthly reviews. 90% and above follows standard quarterly monitoring.

## Exceptions

Any exception to this policy shall be approved and recorded by the Information Security Manager in advance, with documented risk acceptance, compensating controls, and a defined review date (maximum 12 months). Exceptions shall be reported to the Management Review Team. Permanent exceptions are not permitted without documented compensating controls and quarterly review.

## Non-Compliance

An employee found to have violated this policy may be subject to disciplinary action, up to and including termination of employment. Deliberate attempts to circumvent DLP controls shall be treated as serious misconduct. Policy violations shall be documented, investigated by the Information Security Manager, and reported to the CISO. Where violations involve personal data breaches, the DPO shall be consulted.

## Continual Improvement

This policy is reviewed and updated as part of the continual improvement process. Reviews shall consider changes in DLP technology capabilities, evolving data exfiltration techniques (insider threats, advanced persistent threats, supply chain attacks), regulatory changes affecting employee monitoring or data protection requirements, audit findings, DLP performance metrics and trends, false positive feedback from users, and lessons learned from DLP incidents.

---

# Areas of the ISO 27001 Standard Addressed

Data Leakage Prevention Policy — ISO 27001 Controls Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership and commitment | 5.1 Policies for information security |
| Clause 5.2 Policy | 5.10 Acceptable use of information and other associated assets |
| Clause 6.1 Actions to address risks and opportunities | 5.12 Classification of information |
| Clause 6.2 Information security objectives | 5.13 Labelling of information |
| Clause 7.3 Awareness | 5.14 Information transfer |
| Clause 9.1 Monitoring, measurement, analysis, and evaluation | **8.12 Data leakage prevention** |
| Clause 9.3 Management review | 8.15 Logging |
| Clause 10.1 Continual improvement | 8.16 Monitoring activities |

**Regulatory and Legal Framework**:

| Framework | Relevance |
|-----------|-----------|
| Swiss nFADP (revDSG) | Art. 8 — Technical and organisational measures for data protection; DLP as a technical measure. Art. 6 — Principles of proportionality, purpose limitation, and transparency |
| Swiss CO Art. 328b | Employee data processing limited to employment suitability and contract performance; DLP monitoring must comply |
| Swiss ArGV 3 Art. 26 | Prohibition of behaviour surveillance systems; DLP permissible where primary purpose is data protection |
| Swiss DSV (Data Protection Ordinance) | Art. 1-3 — Minimum requirements for data security |
| EU GDPR (where applicable) | Art. 5 (Processing principles), Art. 6 (Lawful basis), Art. 32 (Security measures), Art. 33/34 (Breach notification), Art. 88 (Employment processing) |
| ISO/IEC 27001:2022 | Annex A Control 8.12 — Data leakage prevention |
| ISO/IEC 27002:2022 | Section 8.12 — Implementation guidance for data leakage prevention measures |
| NIST SP 800-53 Rev 5 | AC-4 (Information Flow Enforcement), SC-7 (Boundary Protection), SI-4 (System Monitoring) |
| CIS Controls v8 | 3.1-3.14 (Data Protection), 3.13 (Deploy a Data Loss Prevention Solution) |

---

<!-- QA_VERIFIED: 2026-02-07 -->
