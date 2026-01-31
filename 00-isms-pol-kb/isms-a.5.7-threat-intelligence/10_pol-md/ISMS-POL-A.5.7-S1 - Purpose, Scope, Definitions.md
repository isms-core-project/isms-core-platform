# ISMS-POL-A.5.7-S1
## Threat Intelligence - Purpose, Scope, Definitions

**Document ID**: ISMS-POL-A.5.7-S1  
**Title**: Threat Intelligence - Purpose, Scope, Definitions  
**Version**: 1.0
**Date**: [Date]
**Classification**: Internal  
**Owner**: Chief Information Security Officer (CISO)  
**Status**: Draft

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | [Author Name] | Initial draft |

**Review Cycle**: Annual (mandatory in Q4), quarterly light review (metrics only), or upon significant changes  
**Review Month**: Q4 (October-November) to align with budget planning and annual ISMS reviews  
**Next Review Date**: [Date + 1 year]  
**Approvers**: 
- Chief Information Security Officer (CISO)
- Chief Information Officer (CIO)
- Chief Risk Officer (CRO)
- Legal/Compliance Officer
- Chief Executive Officer (CEO)

---

## 1.1 Purpose

### 1.1.1 Policy Objectives

This document establishes the foundation for [Organization]'s threat intelligence program by defining:

- **Purpose and Scope**: What threat intelligence activities are covered and why they matter
- **Key Terminology**: Common definitions to ensure consistent understanding across stakeholders
- **Threat Landscape Context**: The types of threats relevant to organizations operating in the hosting and infrastructure services sector
- **Integration Framework**: How threat intelligence connects to other security and risk management processes

### 1.1.2 Strategic Goals

The threat intelligence program enables [Organization] to:

- **Shift from Reactive to Proactive Security**: Anticipate threats before they impact operations, rather than only responding after incidents occur
- **Inform Risk-Based Decision Making**: Provide executives and security teams with current, relevant threat information to prioritize security investments and risk treatments
- **Enhance Operational Effectiveness**: Improve detection, response, and prevention capabilities across the Security Operations Center (SOC), incident response, and vulnerability management teams
- **Meet Compliance Obligations**: Fulfill ISO/IEC 27001:2022 Control A.5.7 requirements and support Clause 6.1 risk assessment with objective threat intelligence
- **Protect Organizational Assets**: Defend critical infrastructure, customer data, and business operations against relevant threat actors and attack campaigns
- **Enable Intelligence-Driven Vulnerability Management**: Use **CVSS-based severity scoring combined with active exploitation intelligence** to prioritize remediation efforts (when Control A.8.8 implemented)

### 1.1.3 Value Proposition

Effective threat intelligence provides:

- **Early Warning**: Detection of threats targeting the organization's industry, technology stack, or geographic region before they materialize as incidents
- **Contextual Awareness**: Understanding of *who* is targeting the organization, *why* they are targeted, *how* attacks are conducted, and *what* assets are at risk
- **Prioritized Response**: Focus limited security resources on the threats most likely to impact the organization, informed by **CVSS severity scores and active exploitation status**
- **Faster Incident Resolution**: Enrichment of security alerts and incidents with threat context, attribution, and known TTPs reduces investigation time and improves containment
- **Quantifiable Risk Reduction**: Measurable outcomes including prevented incidents, reduced dwell time, and **CVSS-based vulnerability risk quantification**
- **Regulatory Compliance**: Objective evidence of threat intelligence capabilities for ISO 27001 certification and other security frameworks

---

## 1.2 Scope

### 1.2.1 In-Scope Activities

This threat intelligence framework covers all activities related to:

**Intelligence Collection**:
- Subscribing to and consuming commercial threat intelligence platforms
- Gathering open-source intelligence (OSINT) from security researchers, vulnerability databases, and public sources
- Receiving threat intelligence from government agencies, CERTs, and law enforcement
- Participating in industry information sharing (ISACs, ISAOs, peer groups)
- Collecting internal threat data from security tools (SIEM, EDR, IDS/IPS, firewalls, proxies)
- Monitoring vulnerability advisories and **CVSS-scored CVE disclosures**

**Intelligence Analysis and Production**:
- Processing raw threat data into finished intelligence reports
- Analyzing threat actor capabilities, intentions, and tactics, techniques, and procedures (TTPs)
- Assessing campaign activity and threat trends
- Evaluating vulnerabilities for active exploitation and **CVSS-based severity assessment**
- Producing strategic, tactical, and operational intelligence products
- Creating **VulnerabilityThreatLink (VTL) records** linking CVEs to exploitation intelligence with CVSS scores
- Validating intelligence accuracy and reliability (Admiralty Code methodology)

**Intelligence Dissemination and Operationalization**:
- Distributing intelligence to appropriate stakeholders (executives, SOC, incident response, vulnerability management, risk management)
- Integrating indicators of compromise (IOCs) into security tools (SIEM, EDR, firewalls, email gateways, web proxies)
- Providing intelligence support during incident investigations
- Updating risk assessments based on threat intelligence (Clause 6.1 - MANDATORY)
- **Informing CVSS-based vulnerability prioritization** decisions (when Control A.8.8 implemented)
- Tracking prevented incidents and security effectiveness

**Program Management**:
- Defining and refining intelligence requirements based on organizational needs
- Managing relationships with threat intelligence sources and vendors
- Measuring program effectiveness through KPIs and metrics
- Conducting source performance validation and accuracy assessments
- Maintaining business continuity for critical threat intelligence capabilities

### 1.2.2 Out-of-Scope Activities

The following activities are **NOT** covered by this threat intelligence framework:

- **Offensive Cyber Operations**: Active penetration of adversary infrastructure, retaliatory attacks, or hack-back activities (prohibited under Swiss and EU law)
- **Counterintelligence Operations**: Identification and neutralization of insider threats or espionage activities (covered under separate HR security and insider threat programs if applicable)
- **Law Enforcement Investigations**: Criminal investigations and evidence collection for prosecution (cooperate with law enforcement but do not conduct investigations)
- **Vulnerability Scanning and Penetration Testing**: Technical assessment of organizational vulnerabilities (covered under Control A.8.8 when implemented and separate penetration testing policies)
- **Threat Hunting as Primary Activity**: While threat intelligence informs threat hunting, the hunting activities themselves are covered under Control A.8.16 (Monitoring Activities)
- **Malware Reverse Engineering at Scale**: In-depth reverse engineering of malware samples (may be performed on limited basis or outsourced to specialized vendors)

### 1.2.3 Organizational Applicability

This framework applies to **all organizational entities** including:

- Corporate headquarters and administrative offices
- Data center and hosting infrastructure operations
- Cloud environments and multi-tenant platforms
- Network operations centers (NOC) and security operations centers (SOC)
- Remote and distributed teams accessing organizational systems
- Third-party service providers with access to organizational networks or data (contractual requirements)

**Geographic Scope**: All locations where [Organization] operates, including:
- Primary operations in Switzerland
- International data center facilities
- Cloud provider regions utilized for customer hosting
- Remote employee locations accessing organizational systems

### 1.2.4 Threat Actor Scope

The threat intelligence program monitors and analyzes threats from the following adversary categories:

**Nation-State and Advanced Persistent Threats (APTs)**:
- State-sponsored cyber espionage campaigns targeting critical infrastructure
- Advanced adversaries with significant resources and persistence
- Strategic intelligence to inform executive risk assessments
- Zero-day exploits and emerging vulnerability exploitation
- Focus: Geopolitical tensions affecting hosting/infrastructure sectors

**Organized Cybercrime Groups**:
- Ransomware-as-a-Service (RaaS) operators targeting hosting providers
- Business Email Compromise (BEC) campaigns
- Cryptocurrency mining malware (cryptojacking) on shared infrastructure
- Credential theft and account takeover campaigns
- Data theft and extortion groups
- Focus: Financially motivated threats to hosting infrastructure and customer data

**Hacktivists and Ideologically Motivated Actors**:
- Distributed Denial of Service (DDoS) campaigns
- Website defacement and disruption operations
- Data leaks and exposure campaigns
- Focus: Reputational damage and service disruption threats

**Insider Threats**:
- Malicious insiders with legitimate access (employees, contractors, third parties)
- Negligent insiders creating unintentional security risks
- Compromised insider accounts controlled by external adversaries
- Focus: Abuse of privileged access and data exfiltration

**Opportunistic and Commodity Threats**:
- Automated scanning and exploitation of known vulnerabilities
- Phishing and social engineering campaigns targeting generic victims
- Mass malware distribution and botnet recruitment
- Exploitation of misconfigured cloud services and exposed APIs
- Focus: Volume-based threats requiring detection and blocking at scale

### 1.2.5 Asset and Technology Scope

Threat intelligence SHALL cover threats affecting:

**Infrastructure Assets**:
- Physical and virtual servers (bare metal, VMs, containers)
- Network infrastructure (routers, switches, firewalls, load balancers)
- Storage systems (SAN, NAS, object storage)
- Hypervisors and virtualization platforms (VMware, KVM, Hyper-V, etc.)
- Cloud control planes (AWS, Azure, GCP, etc.)

**Application and Platform Assets**:
- Web hosting platforms and control panels
- Database systems (MySQL, PostgreSQL, MongoDB, etc.)
- Email and collaboration platforms
- Customer-facing portals and APIs
- Internal business applications

**Operational Technology (where applicable)**:
- Data center environmental controls (HVAC, power management)
- Physical security systems (access control, surveillance)
- Building management systems

**Data Assets**:
- Customer data hosted on infrastructure
- Organizational confidential information
- Intellectual property and trade secrets
- Authentication credentials and cryptographic keys
- Backup and disaster recovery data

**Supply Chain Dependencies**:
- Software vendors and open-source components
- Hardware suppliers and firmware
- Cloud service providers and SaaS platforms
- Managed service providers (MSSPs, NOC/SOC outsourcing)

### 1.2.6 Integration with Related Controls

Threat intelligence integrates with the following ISO 27001:2022 controls and ISMS processes:

**MANDATORY Integrations** (standalone A.5.7 implementation):

- **Clause 6.1 - Actions to Address Risks and Opportunities**:
  - Threat intelligence MUST inform risk assessment
  - Emerging threats trigger risk reassessment
  - **CVSS-based vulnerability risk quantification** required
  - Tracked in: ISMS-IMP-A.5.7.3 Sheet 13
  - Target: ≥3 risk assessment updates per quarter

- **Controls A.5.24-5.28 - Incident Management**:
  - Threat intelligence MUST support incident investigation
  - IOCs and TTPs used for alert enrichment and attribution
  - **CVSS context** for vulnerability-related incidents
  - Tracked in: ISMS-IMP-A.5.7.3 Sheet 14
  - Target: ≥70% of P1/P2 incidents use threat intelligence

- **Control A.8.16 - Monitoring Activities**:
  - Threat intelligence provides detection signatures and IOCs
  - IOCs deployed to SIEM, EDR, IDS/IPS, email gateway, web proxy
  - Monitoring telemetry feeds internal threat intelligence

**OPTIONAL Integrations** (when other controls implemented):

- **Control A.8.8 - Management of Technical Vulnerabilities** (**OPTIONAL**):
  - **Note**: This integration is OPTIONAL and only applies when organization implements Control A.8.8
  - **Prioritizing vulnerability remediation** based on active exploitation rather than theoretical risk (Control A.8.8 - **OPTIONAL** when implemented)
  - **CVSS 4.0/3.1 severity scoring** combined with exploitation intelligence
  - **VulnerabilityThreatLink (VTL) schema** enables automated data flow
  - Active exploitation triggers emergency patching workflows
  - Without A.8.8: Basic threat intelligence consumption (CISA KEV, vendor advisories)
  - With A.8.8: Full VTL integration with **CVSS-based automated priority escalation**

- **Controls A.5.19-5.22 - Supplier Management**:
  - Supply chain threat intelligence
  - Supplier vulnerability and compromise tracking
  - Responsible disclosure coordination

- **Control A.5.23 - Cloud Security**:
  - Cloud-specific threat intelligence
  - Cloud provider intelligence feeds
  - Multi-cloud threat visibility

- **Control A.8.23 - Web Filtering**:
  - Malicious URL/domain blocklists from threat intelligence
  - Web filtering telemetry informing threat intelligence

---

## 1.3 Definitions and Terminology

### 1.3.1 Core Threat Intelligence Terms

**Threat Intelligence (TI)**  
Information that has been collected, processed, and analyzed to understand the capabilities, intentions, and activities of threat actors. Threat intelligence enables informed decisions about defensive strategies, risk assessments, and security investments. Effective threat intelligence is *actionable* (supports specific decisions), *timely* (current and relevant), *accurate* (validated and reliable), and *contextualized* (tailored to organizational needs).

**Raw Intelligence**  
Unprocessed threat information collected from sources but not yet analyzed, validated, or formatted for dissemination. Raw intelligence may contain noise, false positives, and conflicting data requiring further processing. Examples: vulnerability scanner outputs, firewall logs, unvalidated IOC feeds.

**Finished Intelligence**  
Threat intelligence that has been fully analyzed, validated, and formatted for dissemination to stakeholders. Finished intelligence includes context, confidence assessments, recommended actions, and supporting evidence. Examples: threat intelligence reports, executive briefings, tactical IOC packages with TTPs.

**Strategic Intelligence**  
High-level intelligence about the threat landscape, threat actor capabilities and intentions, geopolitical factors, and long-term trends. Strategic intelligence informs executive decision-making, risk management, and security strategy. **MUST include Clause 6.1 risk assessment updates with CVSS-based vulnerability risk quantification where applicable.**

*Audience*: C-suite, Board of Directors, Chief Risk Officer, business unit leaders  
*Frequency*: Quarterly reports with ad-hoc updates for significant threats  
*Examples*: Annual threat landscape assessment, geopolitical risk analysis, adversary capability trends, **CVSS-scored critical vulnerability trends**

**Tactical Intelligence**  
Intelligence focused on adversary tactics, techniques, and procedures (TTPs), tools, and infrastructure. Tactical intelligence helps security teams understand *how* attacks are conducted and develop appropriate defenses. Typically mapped to MITRE ATT&CK framework. **Includes vulnerability exploitation techniques with CVSS severity context.**

*Audience*: Security architects, SOC managers, threat hunters, incident responders, penetration testers  
*Frequency*: Monthly reports with ad-hoc updates for emerging TTPs or campaigns  
*Examples*: Adversary TTP analysis, campaign breakdowns, **CVE exploitation techniques with CVSS scores**, detection strategies

**Operational Intelligence**  
Actionable intelligence about specific, imminent threats requiring immediate defensive actions. Includes indicators of compromise (IOCs), active campaigns, and adversary infrastructure. **Includes actively exploited vulnerabilities with CVSS-based prioritization.**

*Audience*: SOC analysts, incident responders, network defenders, vulnerability management team (when Control A.8.8 implemented)  
*Frequency*: Real-time or daily feeds with immediate alerting for critical threats  
*Examples*: Malicious IP addresses, file hashes, phishing campaigns, **actively exploited CVEs with CVSS 4.0/3.1 scores**, zero-day exploitation

**Intelligence Cycle**  
The iterative process of threat intelligence production: **Planning** (define requirements) → **Collection** (gather raw data) → **Processing** (normalize and deduplicate) → **Analysis** (identify patterns, assess threats, **apply CVSS scoring**) → **Dissemination** (distribute to stakeholders) → **Feedback** (refine requirements based on consumer needs).

**Intelligence Requirement**  
A specific intelligence need defined by stakeholders to support decision-making. Requirements are prioritized based on organizational risk profile, threat landscape, and consumer needs. Examples: "What ransomware groups are actively targeting hosting providers?", **"Which CVSS 9.0+ vulnerabilities in our tech stack have active exploitation?"**, "What are the TTPs of APT groups targeting our industry?"

**Indicator of Compromise (IOC)**  
Observable artifacts or evidence of a potential or confirmed security incident. IOCs enable detection and investigation of threats. Common IOC types: file hashes (MD5, SHA-1, SHA-256), IP addresses, domain names, URLs, email addresses, registry keys, mutex names, **CVE identifiers with CVSS scores**, YARA rules.

**Confidence Level**  
An assessment of the reliability and accuracy of threat intelligence, typically expressed as high, medium, or low. Confidence levels help intelligence consumers understand certainty and inform decision-making. Based on source reliability (Admiralty Code), corroboration from multiple sources, and analyst assessment. **CVSS scores have inherent confidence when provided by authoritative sources (NVD, vendors).**

**Attribution**  
The process of identifying the threat actor or group responsible for a cyber attack. Attribution ranges from general categorization (e.g., "likely nation-state actor") to specific identification (e.g., "APT28"). High-confidence attribution requires significant evidence and analysis. Attribution informs defensive prioritization and geopolitical risk assessment.

**Indicator Management**  
The process of collecting, validating, prioritizing, and operationalizing indicators of compromise (IOCs) for detection and response. Effective indicator management includes deduplication, false positive reduction, aging out stale indicators, and enrichment with context.

**VulnerabilityThreatLink (VTL)**  
A data schema linking threat intelligence to specific vulnerabilities (CVEs) when active exploitation is detected. VTL enables automated priority escalation in vulnerability management (Control A.8.8 when implemented). **VTL records include CVSS 4.0 or 3.1 scores, exploitation status, threat actor attribution, and criticality assessment.** Schema documented in: shared_schemas/vulnerability_threat_link.py

**VTL Record Structure (Schema Fields)**:
- **Link_ID**: Unique identifier (VTL-YYYYMMDD-HHMMSS)
- **Vulnerability_ID**: CVE identifier (CVE-YYYY-NNNNN)
- **CVSS_Version**: Scoring version (4.0 or 3.1) - **NEW in v2.0**
- **CVSS_Base_Score**: Severity score (0.0-10.0) - **NEW in v2.0**
- **CVSS_Vector**: Complete vector string - **NEW in v2.0**
- **Exploitation_Status**: PoC Available, Active Exploitation, Mass Exploitation
- **Threat_Actor_Type**: Nation-State, Organized Crime, Hacktivist, etc.
- **Criticality**: Priority rating (1-10)
- **Detection_Date**: When exploitation first detected
- **TI_Source**: Threat intelligence source reporting exploitation
- **Remediation_Status**: Patched, Mitigated, In Progress, Open
- **Critical_Assets_Affected**: Yes/No
- **Emergency_Patch_Required**: Yes/No

### 1.3.2 Intelligence Classification Terms

**Finished Intelligence**  
Threat intelligence that has been fully analyzed, validated, and formatted for dissemination to stakeholders. Finished intelligence includes context, confidence assessments, and recommended actions.

**Validated Intelligence**  
Intelligence that has been confirmed through multiple independent sources, technical analysis, or real-world observation. Validation increases confidence level and actionability.

**Single-Source Intelligence**  
Intelligence derived from a single source without independent corroboration. Lower confidence level; requires cautious interpretation and potential follow-up validation.

**All-Source Intelligence**  
Intelligence synthesized from multiple collection disciplines and sources (commercial feeds, OSINT, internal telemetry, government sources). Higher confidence through corroboration. **CVSS scores are considered all-source when validated by both NVD and vendor advisories.**

### 1.3.3 Threat Actor Terms

**Advanced Persistent Threat (APT)**  
A sophisticated, well-resourced adversary (typically nation-state or state-sponsored) with the capability and intent to maintain long-term access to target networks. APTs use advanced TTPs, custom malware, zero-day exploits, and are characterized by persistence and stealth.

**Threat Actor Group**  
An organized collection of individuals conducting coordinated cyber operations. Groups may be tracked by vendor names (e.g., APT28, FIN7, Lazarus Group) or descriptive characteristics when formal attribution is unavailable.

**Nation-State Actor**  
Cyber threat actors operating on behalf of or sponsored by nation-states. Motivations include espionage, intellectual property theft, critical infrastructure disruption, and geopolitical influence. Typically exhibit advanced capabilities, significant resources, and strategic targeting.

**Cybercrime Group**  
Financially motivated threat actors conducting criminal operations such as ransomware, banking fraud, credential theft, and data extortion. May operate as organized groups or Ransomware-as-a-Service (RaaS) business models.

**Hacktivist**  
Ideologically or politically motivated threat actors conducting cyber operations to promote causes, protest policies, or disrupt organizations. Tactics include DDoS attacks, website defacement, data leaks, and doxing. Capabilities range from novice to advanced.

**Insider Threat**  
Individuals with legitimate access to organizational systems who intentionally misuse access (malicious insiders) or unintentionally create security risks (negligent insiders). Insider threats are difficult to detect and can cause significant damage.

**Script Kiddie / Opportunistic Attacker**  
Low-skill adversaries using pre-built tools and exploit kits to conduct attacks. Typically rely on automation, target low-hanging fruit (unpatched systems, default credentials), and lack sophistication. High volume but generally low impact per attack.

### 1.3.4 Attack and Campaign Terms

**Tactics, Techniques, and Procedures (TTPs)**  
The patterns of adversary behavior and methods used to conduct cyber attacks. **Tactics** are high-level objectives (e.g., initial access, privilege escalation). **Techniques** are specific methods to achieve tactics (e.g., spearphishing, credential dumping). **Procedures** are detailed implementation steps. TTPs are typically mapped to MITRE ATT&CK framework. **May include vulnerability exploitation techniques with associated CVSS scores.**

**Cyber Kill Chain**  
A model describing the stages of a cyber attack from reconnaissance to actions on objectives: Reconnaissance → Weaponization → Delivery → Exploitation → Installation → Command & Control → Actions on Objectives. Used to identify defensive opportunities at each stage.

**Diamond Model**  
A framework for analyzing cyber intrusions based on four core features: **Adversary** (who), **Capability** (tools/TTPs), **Infrastructure** (adversary systems), **Victim** (target). The diamond model supports structured threat analysis and pattern recognition.

**Campaign**  
A series of related cyber attacks conducted by the same threat actor or group targeting similar victims, using consistent TTPs, or pursuing common objectives. Campaign analysis reveals adversary patterns and enables proactive defense. **May include vulnerability exploitation campaigns targeting specific CVEs with CVSS severity context.**

**Zero-Day**  
Exploitation of previously unknown vulnerabilities (zero-day vulnerabilities) for which no patch or mitigation exists. Zero-day threats represent high-impact, low-probability risks. **Zero-day exploits do not have CVSS scores initially; scores are assigned post-disclosure.** Intelligence on zero-day exploitation is critical for emergency response.

**Exploit**  
Code or techniques that take advantage of a vulnerability to compromise a system, escalate privileges, or execute unauthorized actions. Exploits may be proof-of-concept (PoC) demonstrations, weaponized malware, or exploit kit components. **Exploits targeting CVEs are tracked with CVSS severity ratings in VTL records.**

**Malware Family**  
A category of malicious software sharing code, behavior, or infrastructure characteristics. Malware families are often associated with specific threat actors or campaigns. Examples: Emotet (botnet), Ryuk (ransomware), Cobalt Strike (post-exploitation framework).

**Command and Control (C2)**  
Infrastructure used by adversaries to maintain communication with compromised systems, issue commands, and exfiltrate data. C2 may use various protocols (HTTP, DNS, custom protocols) and techniques (domain generation algorithms, fast flux DNS, encrypted channels).

### 1.3.5 Vulnerability and Exploitation Terms

**Common Vulnerability Scoring System (CVSS)** - **EXPANDED in v2.0**  
A standardized framework for assessing vulnerability severity developed by the Forum of Incident Response and Security Teams (FIRST). CVSS provides a consistent, objective methodology to score vulnerabilities based on exploitability, impact, and other factors.

**CVSS Version Strategy**:
- **CVSS 4.0** (preferred) - Current standard released November 2023
  - Enhanced base metrics for improved severity assessment
  - Refined temporal metrics for exploitation maturity
  - Better alignment with real-world exploitation patterns
  - Supplemental metrics for specific deployment contexts
  - **Primary version for new VTL records and vulnerability assessments**

- **CVSS 3.1** (legacy) - Previous standard maintained for compatibility
  - Widely deployed in existing vulnerability databases
  - Supported for historical data and legacy source compatibility
  - **Acceptable for VTL records during transition period**

- **Migration Timeline**: 12 months from policy approval (Q4 2025 → Q4 2026)
  - All new vulnerability assessments SHALL use CVSS 4.0 when available
  - Legacy CVSS 3.1 scores remain valid for historical vulnerabilities
  - VulnerabilityThreatLink (VTL) schema supports both versions with explicit version tagging
  - Threat intelligence sources SHALL be evaluated for CVSS 4.0 support

**CVSS Score Ranges** (both v4.0 and v3.1):
- **Critical**: 9.0 - 10.0 (immediate action required, especially if actively exploited)
- **High**: 7.0 - 8.9 (high priority, accelerated patching if exploited)
- **Medium**: 4.0 - 6.9 (standard priority, monitor for exploitation)
- **Low**: 0.1 - 3.9 (low priority unless specific organizational context)
- **None**: 0.0 (informational, no direct security impact)

**CVSS Base Score**  
The intrinsic characteristics of a vulnerability that remain constant over time and across user environments. Base metrics include: Attack Vector (network, adjacent, local, physical), Attack Complexity, Privileges Required, User Interaction, Scope, Confidentiality Impact, Integrity Impact, Availability Impact.

**CVSS Vector String**  
A compact textual representation of CVSS metrics enabling score reproduction and communication. Example CVSS 4.0 vector: `CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N`

**CVSS Temporal Metrics** (Optional)  
Time-dependent factors affecting vulnerability severity: Exploit Code Maturity (unproven, proof-of-concept, functional, high), Remediation Level (official fix, temporary fix, workaround, unavailable), Report Confidence (unknown, reasonable, confirmed). **Temporal metrics are critical for threat intelligence - a CVSS 6.0 vulnerability with functional public exploit may be higher priority than a CVSS 9.0 with no known exploit.**

**CVSS in Threat Intelligence Context**  
Threat intelligence uses CVSS scores to:
- **Prioritize vulnerability remediation** when combined with exploitation status
- **Quantify risk** for vulnerability-related threats in Clause 6.1 risk assessments
- **Communicate severity** consistently across stakeholders
- **Trigger emergency patching** (e.g., CVSS 9.0+ with active exploitation → emergency response)
- **Track prevented incidents** (document severity of avoided vulnerability exploits)

**Critical Principle**: **CVSS Score + Exploitation Status = Effective Prioritization**
- ❌ CVSS alone: Prioritizes theoretical severity (may not reflect real-world threat)
- ❌ Exploitation alone: Ignores severity (low-severity exploited CVE may not justify emergency patching)
- ✅ CVSS + Exploitation: Evidence-based prioritization balancing severity and threat intelligence

**Common Vulnerabilities and Exposures (CVE)**  
A standardized identifier for publicly disclosed vulnerabilities. CVE IDs follow the format CVE-YYYY-NNNNN (year plus unique number). CVE IDs enable consistent vulnerability tracking across organizations, tools, and databases. **All CVEs published by NVD include CVSS scores (transitioning from 3.1 to 4.0).**

**National Vulnerability Database (NVD)**  
The U.S. government repository of standards-based vulnerability management data. NVD provides CVE descriptions, CVSS scores, affected software versions, and reference links. **Primary authoritative source for CVSS scores; transitioning to CVSS 4.0.**

**Common Weakness Enumeration (CWE)**  
A community-developed list of software and hardware weakness types. CWE provides a taxonomy for vulnerability root causes (e.g., CWE-79 Cross-Site Scripting, CWE-89 SQL Injection). Helps identify systemic security issues beyond individual CVEs.

**Proof of Concept (PoC)**  
Demonstration code or techniques showing that a vulnerability can be exploited. PoC availability increases exploitation likelihood and urgency for remediation. **VTL records track exploitation status including PoC availability.**

**Exploit Availability**  
The maturity and accessibility of exploit code for a vulnerability:
- **No Exploit**: No public exploit code available
- **PoC Available**: Demonstration code exists but may not be weaponized
- **Functional Exploit**: Working exploit code available to adversaries
- **Exploited in the Wild**: Confirmed active exploitation by threat actors
- **Mass Exploitation**: Widespread, automated exploitation at scale

**Active Exploitation**  
Confirmed use of a vulnerability by threat actors in real-world attacks. Active exploitation is detected through honeypots, incident response investigations, SOC telemetry, threat intelligence sources, or security vendor reports. **VTL records document active exploitation with supporting TI source citations.**

**Known Exploited Vulnerabilities (KEV)**  
CISA's authoritative catalog of vulnerabilities actively exploited in the wild. KEV listing indicates high priority for remediation based on confirmed exploitation. **KEV entries include CVSS scores and are mandatory for federal agencies; highly recommended for all organizations.**

**Emergency Patching**  
Accelerated vulnerability remediation process triggered by active exploitation of critical vulnerabilities. **Typical threshold: CVSS 7.0+ (High/Critical) + Active Exploitation = Emergency Patching.** When Control A.8.8 implemented, VTL records automatically trigger emergency patching workflows.

### 1.3.6 Source and Reliability Terms

**Admiralty Code**  
A standardized method for evaluating intelligence source reliability and information credibility. Used for quarterly source performance validation per ISMS-POL-A.5.7 Section 4.4.3.

**Source Reliability Ratings**:
- **A** - Completely Reliable: Established track record, no history of false reporting
- **B** - Usually Reliable: Minor inaccuracies in the past, generally trustworthy
- **C** - Fairly Reliable: Some inaccuracies but useful information
- **D** - Not Usually Reliable: Significant inaccuracies, use with caution
- **E** - Unreliable: Known false reporting, not recommended for use
- **F** - Cannot Be Judged: New source with insufficient track record

**Information Credibility Ratings**:
- **1** - Confirmed: Independently corroborated or directly observed
- **2** - Probably True: Consistent with known facts, logical
- **3** - Possibly True: Not confirmed but plausible
- **4** - Doubtful: Questionable validity, requires verification
- **5** - Improbable: Unlikely to be true based on analysis
- **6** - Cannot Be Judged: Insufficient information to assess

**Admiralty Code Notation**: Combined rating (e.g., A1 = Completely Reliable Source, Confirmed Information; C3 = Fairly Reliable Source, Possibly True Information)

**False Positive**  
An IOC or intelligence assessment incorrectly identifying benign activity as malicious. High false positive rates reduce intelligence utility and create alert fatigue. **Target**: ≤15% false positive rate across all sources (ISMS-POL-A.5.7 Section 4.4.3).

**True Positive**  
An IOC or intelligence assessment correctly identifying malicious activity. True positive rate is a key metric for source accuracy validation.

**False Negative**  
Failure to identify a genuine threat. More difficult to measure than false positives but critical for assessing intelligence coverage gaps. Typically identified post-incident during root cause analysis.

### 1.3.7 Information Sharing Terms

**Traffic Light Protocol (TLP)**  
A set of designations to ensure proper handling and sharing of sensitive information:
- **TLP:CLEAR** (formerly TLP:WHITE): No restrictions on sharing, may be distributed publicly
- **TLP:GREEN**: Community-wide sharing within sector or peer group
- **TLP:AMBER**: Limited sharing within organization and clients, no further propagation
- **TLP:AMBER+STRICT**: Very limited sharing, recipients only, absolutely no onward sharing
- **TLP:RED**: Personal use only, no sharing beyond named recipients

TLP markings SHALL be respected on all received threat intelligence and applied to all disseminated intelligence.

**Information Sharing and Analysis Center (ISAC)**  
Industry-specific organizations facilitating threat intelligence sharing among member companies. Examples: FS-ISAC (financial services), MS-ISAC (multi-state), IT-ISAC (information technology). ISACs provide trusted communities, vetted intelligence, and sector-specific threat analysis.

**Information Sharing and Analysis Organization (ISAO)**  
Broader threat intelligence sharing organizations not limited to specific sectors. ISAOs may focus on geographic regions, shared technologies, or cross-industry collaboration.

**Structured Threat Information Expression (STIX)**  
A standardized language for representing cyber threat information in a machine-readable format. STIX 2.1 supports indicators, threat actors, TTPs, campaigns, malware, and relationships. Enables automated intelligence sharing and tool integration.

**Trusted Automated Exchange of Indicator Information (TAXII)**  
A transport protocol for sharing STIX-formatted threat intelligence. TAXII 2.1 enables automated, bidirectional intelligence exchange with ISACs, threat intelligence platforms, and peer organizations.

### 1.3.8 Organizational Risk Terms

**Threat Landscape**  
The totality of threats relevant to an organization based on industry, geography, technology stack, adversary targeting, and geopolitical factors. Threat landscape analysis informs strategic risk assessments and security strategy.

**Threat Actor Targeting**  
Assessment of whether an organization is actively targeted by specific threat actors or likely to be targeted based on characteristics (industry, size, data holdings, geopolitical factors). Targeting analysis informs threat prioritization and defensive investment.

**Attack Surface**  
The sum of all potential entry points for adversaries, including externally facing systems (websites, email, remote access), supply chain dependencies, cloud environments, and insider access. Attack surface reduction is a key defensive strategy informed by threat intelligence.

**Risk Appetite**  
The amount of risk an organization is willing to accept in pursuit of business objectives. Threat intelligence informs risk appetite by providing realistic threat assessments. Executive leadership defines risk appetite; threat intelligence quantifies threats against that appetite.

**Prevented Incident (Validated)** - **UPDATED in v2.0**  
Security incident that was avoided due to threat intelligence, with objective evidence:
- **Before-state**: Vulnerability existed (scan evidence, asset confirmation)
- **TI alert**: Threat intelligence warned of exploitation (report ID, timestamp, **CVSS score**)
- **Action**: Remediation deployed (patch, mitigation, compensating control)
- **After-state**: Vulnerability eliminated (re-scan evidence)
- **Validation**: Technical evidence (SIEM logs, scan results, EDR telemetry)

**Target**: ≥3 validated prevented incidents per quarter. Evidence tracked in ISMS-IMP-A.5.7.3 Sheet 7.

**Example**: "Threat intelligence report TI-2025-001 (CVSS 4.0 Base Score 9.3) warned of active exploitation of CVE-2024-56789 in Apache Struts. Vulnerability scan confirmed presence on web server WEB-PROD-05. Emergency patching deployed within 4 hours. Post-patch scan confirmed remediation. SIEM logs show 23 exploitation attempts blocked during patching window. Prevented incident documented with full evidence package."

### 1.3.9 Technical Integration Terms

**Security Information and Event Management (SIEM)**  
Centralized platform for collecting, correlating, and analyzing security events from across the organization. Threat intelligence provides IOCs, correlation rules, and threat context to improve SIEM detection effectiveness.

**Endpoint Detection and Response (EDR)**  
Security tools providing continuous monitoring, detection, and response capabilities on endpoints (workstations, servers). Threat intelligence provides malware signatures, behavioral indicators, and threat actor TTPs to enhance EDR effectiveness.

**Threat Intelligence Platform (TIP)**  
A technology solution that aggregates, correlates, and manages threat intelligence from multiple sources. TIPs provide capabilities for indicator management, enrichment, analysis, scoring, and integration with security tools. **Modern TIPs support CVSS 4.0/3.1 and VTL schema integration.**

**Security Orchestration, Automation, and Response (SOAR)**  
Platforms that integrate security tools, automate repetitive tasks, and orchestrate response workflows. Threat intelligence enables automated response playbooks (e.g., block malicious IPs, quarantine malware, trigger VTL emergency patching).

**Indicator Feed**  
An automated delivery mechanism for threat intelligence, typically providing regularly updated IOCs in machine-readable formats (STIX, JSON, CSV). Indicator feeds enable continuous, scalable operationalization of threat intelligence.

---

## 1.4 Policy Structure and Navigation

This document (ISMS-POL-A.5.7-S1) is part of the complete threat intelligence policy framework:
```
ISMS-POL-A.5.7 - Threat Intelligence Policy Framework (Master)
│
├── ISMS-POL-A.5.7-S1 - Purpose, Scope, Definitions (this document)
├── ISMS-POL-A.5.7-S2 - Threat Intelligence Requirements
├── ISMS-POL-A.5.7-S3 - Roles and Responsibilities
├── ISMS-POL-A.5.7-S4 - Policy Governance
└── ISMS-POL-A.5.7-S5 - Annexes
    ├── Annex A: Threat Intelligence Source Standards
    ├── Annex B: Intelligence Report Templates
    ├── Annex C: Threat Intelligence Procedure Summary
    ├── Annex D: Quick Reference Guide
    ├── Annex E: Glossary and Acronyms
    └── Annex F: Document Relationships and Cross-References
```

**For detailed requirements**, refer to **ISMS-POL-A.5.7-S2** (Requirements)  
**For role assignments and RACI**, refer to **ISMS-POL-A.5.7-S3** (Roles and Responsibilities)  
**For integration with other controls**, refer to **ISMS-POL-A.5.7-S4** (Policy Governance)  
**For supporting materials and references**, refer to **ISMS-POL-A.5.7-S5** (Annexes)

---

**END OF DOCUMENT**