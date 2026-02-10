<!-- ISMS-CORE:POLICY:ISMS-OP-POL-A.8.23:operational:OP-POL:a.8.23 -->
**ISMS-OP-POL-A.8.23 — Web Filtering**

---

**Document Control**

| Field | Value |
|-------|-------|
| **Document Title** | Web Filtering |
| **Document Type** | Operational Policy |
| **Document ID** | ISMS-OP-POL-A.8.23 |
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

- ISO/IEC 27001:2022 Control A.8.23 — Web filtering

**Related Annex A Controls**:

| Control | Relationship to Web Filtering |
|---------|-------------------------------|
| A.5.7 Threat intelligence | Threat intelligence feeds inform web filtering block lists and URL categorisation |
| A.5.10 Acceptable use of information | Acceptable use policy defines permitted and prohibited web usage |
| A.8.7 Protection against malware | Web filtering prevents malware delivery via drive-by downloads and malicious websites |
| A.8.16 Monitoring activities | Web filtering logs feed security monitoring and anomaly detection |
| A.8.20 Network security | Web filtering is a network-layer security control |
| A.8.21 Security of network services | Secure Web Gateway (SWG) is a managed network security service |
| A.8.22 Segregation of networks | Web filtering enforced at network segment boundaries |
| A.8.24 Use of cryptography | TLS inspection considerations for encrypted web traffic |

**Related Internal Policies**:

- Acceptable Use Policy
- Network Security Policy
- Endpoint Security Policy
- Monitoring Activities Policy (A.8.16)
- Protection Against Malware Policy
- Privacy and Protection of PII Policy

---

# Web Filtering Policy

## Purpose

The purpose of this policy is to manage access to external websites to reduce exposure to malicious content, prevent data leakage via web channels, and enforce acceptable use requirements. Web filtering protects organisational systems from malware delivered via drive-by downloads, phishing sites, and other web-borne threats.

Web filtering is a key control identified through the organisation's information security risk assessment. The filtering scope and category decisions in this policy are directly informed by the risk treatment plan, addressing risks including: malware infection via web-borne threats, credential theft via phishing, data leakage via unauthorised web services, and reputational harm from inappropriate content access.

This policy supports Swiss nFADP (revDSG) Art. 8 by implementing web filtering as a technical measure to protect personal data from compromise through web-based attack vectors. Web filtering that monitors employee browsing activity shall comply with Swiss employment law (CO Art. 328/328b) and the prohibition on behaviour surveillance (ArGV3 Art. 26). Where the organisation processes data of individuals in the EU/EEA, GDPR Art. 32 requirements also apply.

## Scope

This policy applies to:

- All web traffic (HTTP/HTTPS) originating from organisation-managed devices and networks.
- All employees, contractors, and third-party users accessing the internet via organisation infrastructure.
- All environments: corporate network, remote workers (via VPN or cloud proxy), and guest networks (limited scope).
- All web access methods: browsers, applications making HTTP/HTTPS calls, and API connections to external services.

Out of scope:
- Email filtering (covered under endpoint security and malware protection policies).
- Application-layer controls for specific SaaS platforms (covered under cloud services policy, A.5.19-23).

## Principle

Access to external websites shall be managed to reduce exposure to malicious content. Web filtering shall operate on a risk-based approach: block known threats automatically, restrict discretionary categories by policy, and allow legitimate business access without unnecessary friction. Filtering shall apply consistently regardless of user location or device.

---

## Web Filtering Architecture

### Filtering Approach

The organisation shall implement web filtering using one or more of the following technologies:

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **DNS filtering** | DNS-layer filtering service (e.g., Cisco Umbrella, Cloudflare Gateway, DNSFilter, or equivalent) | First line of defence; blocks resolution of malicious and prohibited domains before connection is established |
| **URL filtering** | Secure Web Gateway (SWG) or proxy with URL categorisation database | Inspects full URL path; enforces category-based policies; provides granular control |
| **TLS inspection** | SWG or proxy performing SSL/TLS decryption and inspection | Inspects encrypted web traffic for threats hidden in HTTPS (applies to selected categories — see TLS Inspection section) |
| **Browser isolation** (optional) | Remote browser isolation (RBI) for high-risk or uncategorised sites | Renders web content in a cloud sandbox; only safe visual output streamed to the user |

### Deployment Model

| Environment | Filtering Method |
|-------------|-----------------|
| **Corporate network** | SWG/proxy or DNS filtering enforced at the network perimeter |
| **Remote workers** | Cloud-delivered SWG or DNS filtering agent on managed endpoints; consistent policy regardless of network |
| **BYOD devices** | DNS filtering (lightweight, privacy-respecting); TLS inspection shall **not** be performed on personal devices |
| **Guest network** | DNS filtering for malware/phishing categories only; discretionary category filtering not applied |

DNS filtering shall be enforced on all managed devices as the baseline. Direct DNS queries to external resolvers (including DNS over HTTPS (DoH) and DNS over TLS (DoT) to non-approved resolvers) shall be blocked at the firewall to prevent filter bypass.

### Availability and Performance (SOC 2: A1.1)

The web filtering platform shall meet the following service level objectives:

| SLO | Target | Measurement |
|-----|--------|-------------|
| **Availability** | ≥99.9% uptime (measured monthly) | Platform monitoring dashboard |
| **Latency** | ≤50ms additional latency per web request (p95) | Periodic performance testing |
| **Failover** | Automatic failover to secondary filtering path or fail-open within 5 minutes | Annual failover testing |
| **Capacity** | Platform sized for peak traffic + 30% headroom | Quarterly capacity review |

If the filtering platform experiences sustained degradation exceeding SLO thresholds, IT Operations shall implement the documented incident response procedure. Fail-open (allowing unfiltered traffic) is permitted only as a temporary measure during platform failure and shall be logged, reported to the CISO, and remediated within 4 hours.

### Change Management for Filtering Rules (SOC 2: CC8.1)

Changes to web filtering configuration (category policies, block/allow lists, TLS inspection settings, deployment architecture) shall follow the organisation's change management process:

1. **Request**: Change request submitted with justification, scope, and risk assessment.
2. **Review**: IT Security reviews the change for security implications; Data Protection Advisor reviews privacy impact if employee monitoring is affected.
3. **Test**: Changes tested in a staging environment or limited deployment where feasible.
4. **Approve**: Standard changes approved by IT Security lead; significant changes (new category blocks, TLS inspection scope changes) approved by CISO.
5. **Implement**: Change deployed by IT Operations during approved maintenance window.
6. **Verify**: Post-implementation verification that the change functions as intended.
7. **Document**: Change recorded in the change log with before/after configuration states.

Emergency changes (e.g., blocking an active phishing campaign) may bypass standard approval but shall be retrospectively documented within 24 hours.

### Vendor Management (SOC 2: CC9.2)

Where web filtering is provided by a third-party service (cloud SWG, DNS filtering provider):

- The vendor shall be included in the organisation's vendor risk management programme.
- SOC 2 Type II report or ISO 27001 certification shall be reviewed annually.
- SLA compliance (availability, latency, threat detection rate, support response time) shall be monitored against contractual thresholds.
- Data processing agreements shall address: employee browsing data handling, data residency, retention periods, and incident notification.
- Vendor lock-in risk shall be assessed; the organisation shall maintain the ability to migrate to an alternative provider within a reasonable timeframe.

---

## URL Categorisation and Filtering Rules

### Mandatory Block — Security Threat Categories

The following categories shall be blocked for all users without exception:

| # | Category | Rationale |
|---|----------|-----------|
| 1 | **Malware distribution** | Sites actively hosting or distributing malware, exploit kits, or drive-by downloads |
| 2 | **Phishing and fraud** | Sites designed to harvest credentials, financial information, or personal data |
| 3 | **Command and control (C2)** | Known botnet and advanced persistent threat infrastructure |
| 4 | **Ransomware** | Ransomware distribution, payment, and communication sites |
| 5 | **Spyware and adware** | Sites distributing unwanted software or tracking tools |
| 6 | **Cryptomining** | Sites running unauthorised cryptocurrency mining scripts |
| 7 | **Exploit kits** | Sites hosting browser and plugin exploitation frameworks |
| 8 | **Dynamic DNS (malicious)** | Frequently used for malicious infrastructure; block known-malicious dynamic DNS providers |
| 9 | **Illegal content** | Content prohibited by Swiss or applicable law |
| 10 | **Child abuse material** | Mandatory legal obligation to block |

### Mandatory Block — Policy Categories

The following categories shall be blocked unless an approved exception exists:

| # | Category | Rationale |
|---|----------|-----------|
| 11 | **Proxy avoidance and anonymisers** | Web proxies, VPN services, and Tor nodes used to bypass filtering controls |
| 12 | **Hacking tools and resources** | Exploit databases, hacking tutorials, and attack tool distribution (exception: security team with documented justification) |
| 13 | **Peer-to-peer file sharing** | Data leakage risk and malware vector |
| 14 | **Copyright infringement / piracy** | Intellectual property and legal risk |

### Discretionary Restriction — Monitored Categories

The following categories may be restricted, monitored, or allowed based on organisational policy:

| # | Category | Default Policy | Notes |
|---|----------|---------------|-------|
| 15 | **Personal cloud storage** (Dropbox, Google Drive personal, etc.) | Restrict | Data leakage risk; corporate cloud storage permitted |
| 16 | **Personal webmail** (Gmail, Outlook personal, etc.) | Restrict | Data leakage risk; corporate email permitted |
| 17 | **Social media** | Allow with monitoring | Business use cases exist; restrict uploads where feasible |
| 18 | **Streaming media / video** | Allow with bandwidth limits | Bandwidth management; restrict during peak hours if needed |
| 19 | **Gaming** | Block during business hours | Productivity; allow outside hours if desired |
| 20 | **Adult content** | Block | Workplace appropriateness |
| 21 | **Gambling** | Block | Workplace appropriateness and legal risk |

### Allowed — Business-Critical Categories

The following categories shall not be filtered or restricted:

| Category | Examples |
|----------|---------|
| **Business and finance** | Banking, industry portals, professional services |
| **Government and legal** | Regulatory sites, government portals, legal databases |
| **Technology and IT** | Software vendors, documentation, developer resources |
| **Education and training** | E-learning platforms, professional development, academic resources |
| **News and media** | Major news outlets, industry publications |
| **Search engines** | Google, Bing, DuckDuckGo |
| **Corporate SaaS applications** | Approved cloud applications per the organisation's SaaS register |

### Uncategorised Websites

Websites not categorised by the filtering solution shall be handled as follows:

- **Default**: Allow with logging (for organisations with lower risk appetite: restrict with user override option).
- All access to uncategorised sites shall be logged for security review.
- If browser isolation is deployed, uncategorised sites should be rendered via isolation by default.

---

## TLS Inspection

### Purpose

Approximately 80% of web traffic is encrypted (HTTPS). Without TLS inspection, threats hidden in encrypted traffic cannot be detected by the web filtering solution. TLS inspection decrypts, inspects, and re-encrypts HTTPS traffic at the SWG/proxy.

### Requirements

| Requirement | Specification |
|-------------|---------------|
| **Deployment** | TLS inspection shall be enabled on the SWG/proxy for traffic from organisation-managed devices |
| **Certificate** | A private root CA certificate shall be deployed to all managed endpoints via MDM, Group Policy, or equivalent |
| **Firefox** | Firefox uses its own certificate store; the private root CA shall be deployed separately via Firefox enterprise policy |
| **Performance** | SWG/proxy shall be sized for TLS inspection workload; QUIC protocol (UDP 443) shall be blocked to force TCP-based HTTPS inspection |

### Privacy Exclusions — Categories to Bypass TLS Inspection

The following categories shall be **excluded** from TLS inspection to protect privacy and avoid technical issues:

| # | Category | Reason |
|---|----------|--------|
| 1 | **Financial / banking** | Credential sensitivity; regulatory considerations |
| 2 | **Healthcare** | Health data privacy (nFADP sensitive personal data) |
| 3 | **Government portals** | Regulatory sensitivity |
| 4 | **Certificate-pinned applications** | Technical incompatibility (e.g., certain APIs, financial applications) |
| 5 | **Personal devices (BYOD)** | No legal basis for TLS inspection on personal devices |

### Legal Requirements for TLS Inspection

- Employees shall be informed in advance that encrypted web traffic may be decrypted and inspected for security purposes.
- The acceptable use policy shall document TLS inspection and its purpose.
- TLS inspection data shall be processed only for security purposes (malware detection, data leakage prevention, policy enforcement) — not for behavioural monitoring.
- BYOD and guest network traffic shall **not** be subject to TLS inspection.

---

## Threat Intelligence Integration

### Block List Updates

Web filtering block lists shall be updated using threat intelligence from multiple sources:

| Source Type | Examples | Update Frequency |
|-------------|---------|-----------------|
| **Vendor-provided** | Filtering solution vendor's URL categorisation database | Real-time or daily (automatic) |
| **Threat intelligence feeds** | Industry ISACs, government cyber agencies (NCSC.ch, MELANI), commercial threat feeds | Automatic where supported; manual review weekly |
| **Internal intelligence** | IOCs from incident investigations, phishing reports from employees, security team research | Ad hoc; added within 4 hours of identification |
| **Community feeds** | Open-source threat intelligence (MISP, abuse.ch, PhishTank, URLhaus) | Automatic where supported |

### Phishing and Social Engineering

- Employee-reported phishing URLs shall be assessed and added to the block list within **4 hours** during business hours.
- Phishing simulation URLs shall be excluded from web filtering during testing campaigns (coordinated between Information Security and IT Operations).

### Incident Response Integration

Web filtering events shall be integrated with the organisation's incident management process (A.5.24-28). The following thresholds shall trigger incident creation:

| Trigger | Severity | Action |
|---------|----------|--------|
| User accesses confirmed malware/C2 site (filtering bypassed or failed) | Critical | Immediate incident; isolate endpoint; forensic investigation |
| Multiple users blocked from same phishing URL within 1 hour | High | Investigate potential phishing campaign; assess whether any users accessed the URL before blocking |
| Single user repeatedly attempts to access blocked categories (>20 attempts/day) | Medium | Investigate for policy violation or compromised account |
| Filtering platform bypass detected (DoH/proxy evasion successful) | High | Block evasion vector; investigate scope; assess policy enforcement gaps |
| Sudden spike in blocked requests (>200% of baseline) | Medium | Assess for malware campaign, compromised infrastructure, or misconfiguration |

---

## Exception and Override Process

### Requesting Access to Blocked Sites

When a user encounters a blocked website required for legitimate business purposes:

1. **Block page**: The user sees a block page displaying the reason for blocking and a link to request access.
2. **Request**: User submits an exception request via [ticketing system / self-service portal] with:
   - URL or domain requested.
   - Business justification.
   - Duration needed (temporary or permanent).
   - Department and project context.
3. **Review**: The request is reviewed by:
   - **Line Manager**: Confirms business justification (within 1 business day).
   - **IT Security**: Assesses security risk (within 1 business day).
4. **Decision**:
   - **Approve**: URL/domain added to allow list (time-limited preferred; default: 90 days).
   - **Deny**: User notified with reason; alternative suggested where possible.
   - **Escalate**: High-risk category overrides (proxy avoidance, hacking tools) require CISO approval.
5. **Implementation**: IT Operations adds the approved exception to the filtering solution within 4 hours of approval.
6. **Documentation**: Exception recorded in the exception register with requestor, justification, approver, expiry date, and review date.

### Exception Register

| Field | Description |
|-------|-------------|
| Exception ID | Unique identifier |
| URL/Domain | What is permitted |
| Requestor | Name, department |
| Business justification | Why access is required |
| Risk assessment | Security risk assessment outcome |
| Approver | Name and date |
| Expiry date | Default: 90 days (temporary) or annual review (permanent) |
| Review date | When exception is next reviewed |
| Compensating controls | Any additional controls applied (e.g., monitoring, logging) |

### Exception Governance

- All exceptions shall be reviewed **quarterly** by IT Security.
- Expired exceptions shall be automatically revoked.
- Unused exceptions (no access recorded in 90 days) shall be removed.
- The total number of active exceptions shall be reported to the CISO quarterly.
- Exceptions shall be the minimum scope needed: specific URL preferred over full domain; domain preferred over entire category.

---

## Remote Worker and BYOD Considerations

### Remote Workers (Managed Devices)

- Cloud-delivered SWG or DNS filtering agent shall be installed on all managed endpoints.
- Web filtering policies shall apply consistently whether the user is on the corporate network, home Wi-Fi, mobile hotspot, or public network.
- Split tunnelling (VPN) shall not bypass web filtering; web traffic shall be routed through the filtering solution regardless of VPN configuration.

### BYOD (Personal Devices)

- DNS filtering is the minimum baseline for BYOD devices accessing corporate resources.
- TLS inspection shall **not** be performed on personal devices (privacy and legal constraints).
- A managed browser or secure workspace container (e.g., Microsoft Edge for Business, VMware Workspace ONE) should be considered for BYOD access to corporate web applications.
- Separate, less intrusive filtering policies shall apply to BYOD compared to corporate-managed devices.

---

## Employee Privacy and Web Filtering

### Legal Requirements

Web filtering that processes employee browsing data shall comply with Swiss employment law:

- **ArGV3 Art. 26**: Web filtering systems shall not be used primarily to monitor employee behaviour. Their purpose is security (malware prevention, data leakage prevention, policy enforcement).
- **CO Art. 328b**: Processing of employee web browsing data shall be proportional and limited to security purposes.
- **nFADP**: Lawfulness, proportionality, purpose limitation, and transparency apply to all web browsing data processing.

### Privacy Safeguards

- **Transparency**: Employees shall be informed that web filtering is in place, what categories are filtered, and that access to blocked sites is logged. This information shall be included in the acceptable use policy and employment documentation.
- **Non-personalised monitoring by default**: Web filtering logs shall be reviewed in aggregate for security monitoring (e.g., total blocked requests by category, top blocked domains). Individual user browsing activity shall not be reviewed unless:
  - (a) A security alert indicates a potential incident or policy violation, and
  - (b) The investigation is documented with justification.
- **Purpose limitation**: Web filtering data shall not be used for HR performance evaluation, disciplinary action for non-security matters, or general behavioural profiling.
- **Data minimisation**: Web filtering logs shall be retained only as long as necessary for security purposes (per log retention schedule in the Logging Policy, A.8.15).
- **DPIA**: If web filtering includes TLS inspection or detailed user-level logging at scale, a Data Protection Impact Assessment under nFADP Art. 22 may be required.

---

## Training and Awareness

- All employees shall be trained on:
  - The organisation's web filtering policy and acceptable web use.
  - How to recognise browser security warnings (certificate errors, phishing indicators).
  - How to report suspected malicious websites to Information Security.
  - The exception request process for accessing blocked sites.
- Training shall be included in the annual information security awareness programme.
- System administrators responsible for web filtering maintenance shall receive platform-specific training.

---

## Roles and Responsibilities

| Role | Responsibilities |
|------|-----------------|
| **CISO** | Policy ownership; approval of category filtering decisions; approval of high-risk exceptions; oversight of web filtering effectiveness |
| **IT Operations / Network Team** | Web filtering platform deployment, configuration, and maintenance; exception implementation; capacity management; TLS inspection certificate management |
| **Information Security** | Threat intelligence integration; block list updates; exception risk assessment; quarterly exception review; web filtering log analysis |
| **Line Managers** | Business justification review for exception requests |
| **All Employees** | Comply with web filtering policy; report suspected malicious websites; use the exception request process for legitimate business needs |
| **Data Protection Advisor** | DPIA assessment for TLS inspection; guidance on employee privacy safeguards |

### Administrative Access Review (SOC 2: CC6.1)

Administrative access to the web filtering platform shall be:

- Restricted to IT Operations and Information Security personnel with a documented need.
- Reviewed quarterly to ensure only authorised personnel retain access.
- Protected with MFA and privileged access management controls.
- Logged — all administrative actions (rule changes, configuration modifications, exception additions) shall be auditable.
- Revoked within 24 hours when personnel change roles or leave the organisation.

---

## Evidence

The following evidence demonstrates compliance with this policy:

| # | Evidence | Owner | Frequency |
|---|----------|-------|-----------|
| 1 | **Web filtering platform configuration** (categories blocked/allowed, TLS inspection settings, DNS filtering configuration) | IT Operations | *Documented; reviewed semi-annually and after policy changes* |
| 2 | **Block list update records** (threat intelligence sources, update frequency, manual additions from incident investigations) | Information Security | *Continuous automatic updates; manual additions logged with date and source* |
| 3 | **Exception register** (active exceptions with justification, approver, expiry, and review date) | Information Security | *Maintained continuously; reviewed quarterly; total reported to CISO quarterly* |
| 4 | **Web filtering log summary** (aggregated statistics: total requests, blocked requests by category, top blocked domains) | Information Security | *Monthly summary; retained 12 months* |
| 5 | **TLS inspection privacy exclusion list** (categories bypassing inspection) | IT Operations | *Documented; reviewed annually* |
| 6 | **Employee notification records** (acceptable use policy acknowledgment including web filtering disclosure) | HR / Information Security | *Updated per policy change; acknowledgment tracked annually* |
| 7 | **Remote worker filtering coverage** (percentage of managed remote endpoints with active filtering agent) | IT Operations | *Quarterly; target: 100% of managed remote devices* |
| 8 | **DPIA records** (if TLS inspection or detailed user-level logging is implemented) | Data Protection Advisor | *Completed before deployment; reviewed annually* |
| 9 | **Filtering platform SLO reports** — availability, latency, and incident resolution metrics (SOC 2: A1.1) | IT Operations | *Monthly; retained 12 months* |
| 10 | **Filtering rule change records** — change requests, risk assessments, approvals, implementation dates (SOC 2: CC8.1) | IT Operations / Information Security | *Per change; retained 12 months* |
| 11 | **Vendor risk assessment records** — third-party SWG/DNS provider evaluations, SLA compliance, SOC 2/ISO 27001 reports (SOC 2: CC9.2) | Information Security / Procurement | *Annually; retained active contract + 2 years* |
| 12 | **Administrative access review records** — filtering platform admin access list, review outcomes, access modifications (SOC 2: CC6.1) | IT Operations / Information Security | *Quarterly; retained 12 months* |
| 13 | **Filtering effectiveness test results** — test URLs, bypass attempt results, detection rate measurements (SOC 2: CC4.1) | Information Security | *Semi-annually; retained 12 months* |
| 14 | **Management reporting** — monthly metrics summary, quarterly trend analysis, annual effectiveness review (SOC 2: CC4.2) | CISO / Information Security | *Monthly/quarterly/annually as specified* |

---

# Policy Compliance

## Compliance Measurement

The information security management team will verify compliance with this policy through web filtering configuration reviews, exception register audits, block rate analysis, remote device coverage checks, internal and external audits, and feedback to the policy owner.

## Exceptions

Any exception to this policy shall be approved and recorded per the Exception and Override Process defined above. Exceptions to the overall web filtering policy (e.g., systems that cannot be filtered) shall be approved by the CISO with documented risk acceptance and compensating controls.

## Non-Compliance

An employee found to have violated this policy — including attempting to bypass web filtering controls (e.g., using personal VPN, proxy avoidance tools, or unauthorised DNS resolvers) — may be subject to disciplinary action, up to and including termination of employment.

## Testing and Validation (SOC 2: CC4.1)

The effectiveness of web filtering controls shall be tested on a regular basis:

| Test | Frequency | Method | Owner |
|------|-----------|--------|-------|
| **Block verification** | Monthly | Attempt access to known-blocked URLs from test accounts; verify block page displays correctly | Information Security |
| **Bypass testing** | Semi-annually | Attempt to bypass filtering using common evasion techniques (DoH to non-approved resolvers, VPN, proxy) | Information Security |
| **Malware detection rate** | Quarterly | Submit known malicious URLs (from test feeds) through the filtering solution; measure detection rate | Information Security |
| **TLS inspection verification** | Quarterly | Verify TLS inspection is active on expected traffic; confirm privacy exclusions function correctly | IT Operations |
| **Remote worker coverage** | Quarterly | Verify filtering agent is active on a sample of remote managed endpoints | IT Operations |

Test results shall be documented and remediation actions tracked for any identified weaknesses.

## Metrics and Management Reporting (SOC 2: CC4.2)

The following metrics shall be reported:

| Metric | Target | Reporting |
|--------|--------|-----------|
| Filtering platform availability | ≥99.9% uptime | Monthly to IT Operations |
| Malware/phishing block rate | ≥99% of known threats blocked | Quarterly to CISO |
| Exception request turnaround | ≤2 business days from request to decision | Monthly to CISO |
| Active exceptions count | Trending downward or stable | Quarterly to CISO |
| Remote worker filtering coverage | 100% of managed remote endpoints | Quarterly to CISO |
| Employee-reported phishing URLs processed | Within 4 hours SLA | Monthly to Information Security |

## Continual Improvement

This policy is reviewed and updated as part of the continual improvement process. Reviews shall consider changes to web threat landscape, filtering technology capabilities, regulatory requirements, employee feedback on legitimate access being blocked, and false positive/negative rates.

---

# Areas of the ISO 27001 Standard Addressed

Web Filtering Policy — ISO 27001 Controls Mapping

| ISO 27001:2022 | ISO 27002:2022 |
|----------------|----------------|
| Clause 5.1 Leadership and commitment | 5.1 Policies for information security |
| Clause 5.2 Policy | 5.4 Management responsibilities |
| Clause 6.2 Information security objectives | 5.36 Compliance with policies, rules, and standards |
| | 5.37 Documented operating procedures |
| | 6.3 Information security awareness, education, and training |
| | 6.4 Disciplinary process |
| | **8.23 Web filtering** |

**Regulatory and Legal Framework**:

| Framework | Relevance |
|-----------|-----------|
| Swiss nFADP (revDSG) | Art. 8 — Technical and organisational measures; Art. 6 — Proportionality |
| Swiss CO (Code of Obligations) | Art. 328b — Employee data processing limitations |
| Swiss ArGV3 (Ordinance 3 to Employment Act) | Art. 26 — Prohibition on behaviour surveillance |
| EU GDPR (where applicable) | Art. 32 — Security of processing |
| ISO/IEC 27001:2022 | Annex A Control 8.23 |
| ISO/IEC 27002:2022 | Section 8.23 — Implementation guidance |
| NIST SP 800-53 Rev 5 | AC-4 (Information Flow Enforcement), SC-7 (Boundary Protection), SC-7(8) (Route Traffic to Proxy), SI-3 (Malicious Code Protection) |
| NIST CSF 2.0 | PR.DS (Data Security), PR.IR (Infrastructure Resilience), DE.CM (Continuous Monitoring) |
| CIS Controls v8 | Control 9.2 (DNS Filtering Services), Control 9.3 (Network URL Filters) |

---

<!-- QA_VERIFIED: 2026-02-07 -->
