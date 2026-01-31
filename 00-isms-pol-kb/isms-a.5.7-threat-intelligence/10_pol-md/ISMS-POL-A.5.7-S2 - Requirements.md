# ISMS-POL-A.5.7-S2
## Threat Intelligence - Requirements

**Document ID**: ISMS-POL-A.5.7-S2  
**Title**: Threat Intelligence - Requirements  
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

## 2.1 Intelligence Collection Requirements

### 2.1.1 Collection Objectives

The organization SHALL establish and maintain threat intelligence collection capabilities to:

- Identify threats relevant to the organization's industry, geographic presence, technology stack, and risk profile
- Maintain awareness of threat actor groups targeting organizations with similar characteristics
- Monitor emerging attack techniques and vulnerabilities affecting organizational assets
- Track active exploitation campaigns and malware families
- **Monitor CVE disclosures with CVSS 4.0/3.1 severity scores for organizational technology stack**
- Understand geopolitical and industry trends that may impact the threat landscape
- Support proactive defense and informed risk management decisions
- **Enable risk assessment updates (Clause 6.1 - MANDATORY)** with current threat landscape data and **CVSS-based vulnerability risk quantification**
- **Generate objective audit evidence** per ISMS-POL-A.5.7 Section 4.4

Collection activities SHALL be conducted in compliance with all applicable laws, regulations, and ethical standards.

### 2.1.2 Internal Intelligence Sources

The organization SHALL collect threat information from internal sources including:

**Security Infrastructure Telemetry**:
- Security Information and Event Management (SIEM) systems
- Intrusion Detection/Prevention Systems (IDS/IPS)
- Endpoint Detection and Response (EDR) platforms
- Firewall and network security appliance logs
- Web proxy and content filtering logs
- Email security gateway alerts
- Data Loss Prevention (DLP) systems
- Authentication and access control logs

**Incident Response Data (Control A.5.24-5.28 - MANDATORY integration)**:
- Historical incident data and post-incident reviews
- Indicators of compromise (IOCs) from past incidents
- Attack patterns and adversary TTPs observed during investigations
- Lessons learned and defensive gaps identified
- **Evidence tracked in**: ISMS-IMP-A.5.7.3 Sheet 14 (Incident-TI Integration)

**Vulnerability Management Data (Control A.8.8 - OPTIONAL integration when implemented)**:
- Vulnerability scan results and trends
- Asset inventory and software bill of materials (SBOM)
- Patch deployment status and exceptions
- Penetration test findings
- **CVSS-scored vulnerabilities from scanning tools**
- **VulnerabilityThreatLink (VTL) data** when Control A.8.8 is operational

**User and Help Desk Reporting**:
- Phishing reports from employees
- Suspicious activity reports
- Security awareness training metrics
- Social engineering test results

Internal threat information SHALL be sanitized and anonymized as appropriate before sharing externally or with third parties.

### 2.1.3 External Intelligence Sources

The organization SHALL establish and maintain access to external threat intelligence sources appropriate to its risk profile and resources. External sources may include:

**Commercial Threat Intelligence Providers**:
- Subscription-based threat intelligence feeds
- Malware analysis and reverse engineering services
- Adversary infrastructure tracking
- Industry-specific threat intelligence
- Managed threat intelligence services

Selection criteria for commercial providers SHALL include:
- Coverage of threats relevant to the organization
- Timeliness and accuracy of intelligence
- **CVSS 4.0 support for vulnerability intelligence (preferred) or CVSS 3.1 (acceptable)** - **NEW in v2.0**
- Integration capabilities with existing security tools (STIX/TAXII, API, TIP compatibility)
- Total cost of ownership
- Vendor reputation and track record
- Support and service level agreements

**Open-Source Intelligence (OSINT)**:
- Security researcher blogs and publications
- Vulnerability databases (NVD, CVE, vendor advisories) with **CVSS 4.0/3.1 scores**
- Malware analysis repositories
- Security community forums and mailing lists
- Academic research on emerging threats
- Dark web monitoring (where legally permissible and ethically conducted)

**Government and Public Sector Sources**:
- National Computer Emergency Response Teams (CERTs)
- Cybersecurity agencies (e.g., NCSC-CH, CISA, ENISA)
- Law enforcement cybercrime units
- Government threat reports and advisories
- Critical infrastructure protection programs
- **CISA Known Exploited Vulnerabilities (KEV) catalog with CVSS scores**

**Industry Collaboration and Information Sharing**:
- Information Sharing and Analysis Centers (ISACs) for relevant sectors
- Information Sharing and Analysis Organizations (ISAOs)
- Industry peer groups and security consortia
- Vendor security bulletins and advisories with **CVSS scoring**
- Professional security associations

**Cloud and Service Provider Intelligence**:
- Threat intelligence from cloud service providers (AWS, Azure, GCP, etc.)
- Content Delivery Network (CDN) provider threat data
- Managed Security Service Provider (MSSP) intelligence
- Security-as-a-Service vendor feeds

### 2.1.3A Vulnerability Scoring Requirements - **NEW in v2.0**

**MANDATORY CVSS Support for Threat Intelligence Sources**:

All threat intelligence sources providing vulnerability-related intelligence SHALL support **Common Vulnerability Scoring System (CVSS)** scoring:

**Primary Standard - CVSS 4.0** (Preferred):
- All new threat intelligence source subscriptions SHALL prioritize CVSS 4.0 support
- Sources providing CVSS 4.0 receive higher evaluation scores in source selection
- **Target**: ≥75% of vulnerability intelligence from CVSS 4.0-capable sources by Q4 2026

**Legacy Standard - CVSS 3.1** (Acceptable):
- CVSS 3.1 remains acceptable during 12-month transition period
- Existing sources providing CVSS 3.1 are not required to upgrade immediately
- **Minimum requirement**: All sources MUST provide CVSS 3.1 or higher

**Unacceptable Scoring**:
- Sources providing only CVSS 2.0 or proprietary scoring SHALL be evaluated for deprecation
- Exceptions may be granted for sources providing unique threat intelligence not available elsewhere
- Exception approval required from CISO with documented justification

**Required CVSS Data Elements**:

Threat intelligence sources SHALL provide the following for each CVE:
- **CVE Identifier**: Standard CVE-YYYY-NNNNN format
- **CVSS Version**: Explicitly stated (4.0 or 3.1)
- **CVSS Base Score**: Numerical score (0.0-10.0)
- **CVSS Vector String**: Complete vector for score reproduction
- **CVSS Severity Rating**: None/Low/Medium/High/Critical
- **Exploitation Status**: PoC Available, Active Exploitation, Mass Exploitation, or No Known Exploit
- **Publication Date**: When CVE was disclosed
- **Last Updated**: Most recent intelligence update

**Optional but Recommended CVSS Data**:
- CVSS Temporal Score (accounting for exploit maturity)
- CVSS Environmental Score (organizational context - may be calculated internally)
- Attack Vector details (Network, Adjacent, Local, Physical)
- Attack Complexity assessment
- Privileges Required and User Interaction factors

**CVSS Accuracy Validation**:
- Threat intelligence CVSS scores SHALL be validated quarterly against authoritative sources (NVD, vendor advisories)
- Discrepancies >1.0 points SHALL be investigated and documented
- Persistent CVSS accuracy issues contribute to source reliability assessment (Admiralty Code)
- **Target**: ≥90% CVSS accuracy (±1.0 point tolerance) for all sources

**Integration with VulnerabilityThreatLink (VTL)**:
- Active exploitation intelligence SHALL include CVSS scores for VTL record creation
- VTL schema (ISMS-IMP-A.5.7.2 Sheet 8) captures CVSS version, score, and vector
- When Control A.8.8 implemented, CVSS scores enable automated priority escalation

**Source Evaluation Impact**:
- CVSS support is weighted at 15% in overall source evaluation (see Annex A.2)
- Sources without CVSS support score 1/5 in "Quality" criterion
- CVSS 4.0 support: 5/5, CVSS 3.1 support: 4/5, CVSS 2.0 only: 2/5, No CVSS: 1/5

### 2.1.4 Source Vetting and Reliability Assessment

The organization SHALL implement a process for vetting and assessing the reliability of threat intelligence sources.

**Initial Source Evaluation** SHALL consider:
- Source credibility and track record
- Transparency of collection and analysis methodology
- Relevance to organizational threat profile
- Data quality and false positive rates
- **CVSS support and vulnerability scoring accuracy** - **NEW in v2.0**
- Update frequency and timeliness
- Legal and ethical compliance of collection methods
- Cost versus value delivered

**Ongoing Source Assessment** SHALL include:
- **Quarterly validation** of intelligence accuracy and actionability
- False positive and false negative analysis
- **CVSS score accuracy validation** (comparison to NVD/vendor advisories) - **NEW in v2.0**
- Comparison against other sources for validation
- Feedback from intelligence consumers on utility
- **Documentation of source reliability scoring** using Admiralty Code or equivalent
- **Documented in**: ISMS-IMP-A.5.7.1 Sheet 14 (Source Performance Validation)

**Quality Targets**:
- Overall source accuracy rate: **≥85%** (per ISMS-POL-A.5.7 Section 4.4.3)
- Individual source accuracy: **≥80%** to maintain subscription/access
- **CVSS accuracy rate: ≥90%** (±1.0 point tolerance) - **NEW in v2.0**
- False positive rate: **≤15%** across all sources

**Source Management**:
- Sources consistently below 80% accuracy SHALL be deprecated or removed
- **Sources with CVSS accuracy <85%** SHALL be flagged for review - **NEW in v2.0**
- Deprecation decisions SHALL be documented with justification
- Alternative sources SHALL be identified to maintain coverage

### 2.1.5 Collection Coverage Requirements

Threat intelligence collection SHALL provide coverage across:

**Threat Actor Categories**:
- Nation-state and state-sponsored actors
- Organized cybercrime groups
- Hacktivists and ideologically motivated actors
- Insider threats
- Opportunistic and commodity threats

**Attack Vectors**:
- Email-based attacks (phishing, BEC, malicious attachments)
- Web-based attacks (drive-by downloads, watering holes, exploitation frameworks)
- Network-based attacks (exploitation, lateral movement, command and control)
- Supply chain compromises
- Social engineering and physical security bypasses
- Cloud and SaaS-specific attack techniques

**Asset Classes**:
- On-premises infrastructure
- Cloud environments and services
- Applications and databases
- Network infrastructure
- Endpoints (workstations, mobile devices)
- Operational technology (where applicable)

**Intelligence Types**:
- Strategic intelligence (executive decision-making, risk assessment)
- Tactical intelligence (adversary TTPs, campaign analysis)
- Operational intelligence (IOCs, active campaigns, **actively exploited CVEs with CVSS scores**)

**Geographic Coverage**:
- Primary operating regions (Switzerland, EU)
- Cloud provider regions hosting customer workloads
- Threat actor countries of origin (nation-state attribution)
- Global threat trends affecting critical infrastructure

**Technology Coverage**:
- Operating systems deployed (Linux, Windows, VMware ESXi, etc.)
- Key applications (web servers, databases, control panels, email)
- Network infrastructure (firewalls, routers, switches, load balancers)
- Virtualization and container platforms
- Cloud control planes and SaaS platforms
- **CVE coverage for entire organizational technology stack**

---

## 2.2 Intelligence Analysis Requirements

### 2.2.1 Analysis Objectives

The organization SHALL analyze collected threat information to produce actionable intelligence that:

- Identifies patterns, trends, and emerging threats
- Provides context on threat actor capabilities, intentions, and TTPs
- **Assesses vulnerability severity using CVSS 4.0/3.1 combined with exploitation status** - **NEW in v2.0**
- Assesses likelihood and potential impact of threats to organizational assets
- Supports strategic, tactical, and operational decision-making
- Enables proactive defense and threat mitigation
- Informs risk management (Clause 6.1 - MANDATORY) with **CVSS-based vulnerability risk quantification**
- Generates audit evidence demonstrating threat intelligence effectiveness

Analysis SHALL be conducted using structured methodologies (MITRE ATT&CK, Diamond Model, Cyber Kill Chain) and supported by appropriate tools (Threat Intelligence Platform, SIEM, malware analysis sandboxes).

### 2.2.2 Strategic Intelligence Analysis

The organization SHALL produce strategic threat intelligence to inform executive decision-making, risk management, and security strategy.

**Strategic Intelligence Requirements**:

- **Threat Landscape Assessment**: Analysis of threats relevant to organizational industry, geography, and risk profile:
  - Nation-state and APT targeting of hosting/infrastructure sectors
  - Ransomware and extortion trends affecting similar organizations
  - Supply chain compromise risks
  - Geopolitical factors affecting cyber threat landscape
  - Long-term adversary capability evolution
  - **Critical vulnerability trends (CVSS 9.0+ CVEs) in organizational technology stack** - **NEW in v2.0**

- **Risk Assessment Integration (Clause 6.1 - MANDATORY)**:
  - Threat intelligence findings SHALL inform risk assessment updates
  - Emerging threats SHALL trigger risk reassessment when likelihood or impact changes
  - **CVSS-based vulnerability risk quantification** for vulnerability-related threats - **NEW in v2.0**
  - Risk register SHALL reference threat intelligence reports supporting likelihood estimates
  - Quarterly: Submit risk assessment update report to Risk Management
  - **Target**: ≥3 risk assessment updates per quarter
  - **Evidence**: ISMS-IMP-A.5.7.3 Sheet 13

- **Security Investment Prioritization**: Data-driven recommendations for security spending:
  - Control gaps based on threat landscape analysis
  - Tool and technology investments to address priority threats
  - Training and staffing needs based on adversary evolution
  - **Emergency patching budget for CVSS 9.0+ actively exploited vulnerabilities** - **NEW in v2.0**

- **Threat Actor Profiling**: In-depth analysis of adversaries targeting similar organizations:
  - Capabilities and resource levels
  - Motivations and targeting criteria
  - Historical campaigns and TTPs
  - Attribution confidence and evidence

**Audience**: C-suite, Board of Directors, Chief Risk Officer, business unit leaders

**Frequency**: Quarterly strategic intelligence reports with ad-hoc updates for significant threats or **critical CVSS 9.0+ mass exploitation events**

### 2.2.3 Tactical Intelligence Analysis

The organization SHALL produce tactical threat intelligence to inform security operations, threat hunting, and defensive architecture.

**Tactical Intelligence Requirements**:

- **Adversary TTP Analysis**: Detailed examination of threat actor tactics, techniques, and procedures:
  - Mapping to MITRE ATT&CK framework
  - Technique prevalence and success rates
  - Detection and mitigation strategies for each TTP
  - Evolution of TTPs over time
  - **Exploitation techniques for CVEs with CVSS context** - **NEW in v2.0**

- **Campaign Analysis**: Tracking and analyzing coordinated threat campaigns:
  - Campaign objectives and targeting criteria
  - Phasing and evolution of campaigns over time
  - Similarities and differences from previous campaigns
  - Attribution and threat actor association

- **Vulnerability and Exploit Analysis**: Context on vulnerabilities being actively exploited - **EXPANDED in v2.0**:
  - **CVE identification with CVSS 4.0 or 3.1 scoring**
  - **CVSS Base Score, Vector, and Temporal Metrics (exploit maturity)**
  - Exploitation techniques and proof-of-concept availability
  - Targeting of specific software versions or configurations
  - Typical post-exploitation activities
  - Defensive mitigations and detection opportunities
  - **Prioritization recommendation: CVSS Score + Exploitation Status**
  - **Integration with Control A.8.8 (OPTIONAL)**: When implemented, active exploitation intelligence triggers VulnerabilityThreatLink (VTL) records for priority escalation

**Example Vulnerability Analysis**:
```
CVE-2024-56789: Apache Struts Remote Code Execution
├─ CVSS 4.0 Base Score: 9.3 (Critical)
├─ CVSS Vector: CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N
├─ Exploitation Status: Mass Exploitation (detected in 15+ campaigns)
├─ Threat Actors: Multiple ransomware groups, nation-state actors
├─ Exploitation Technique: Unauthenticated RCE via OGNL injection
├─ Detection: SIEM rules available, EDR behavioral signatures
├─ Mitigation: Patch to version 2.5.33 or implement WAF rules
├─ Priority: CRITICAL - Emergency patching required
└─ VTL Record: VTL-20250109-143000 created, linked to A.8.8 emergency workflow
```

- **Defensive Gap Assessment**: Analysis of organizational defensive capabilities against known TTPs:
  - Coverage gaps in detection and prevention controls
  - High-priority capability development areas
  - Threat hunting hypotheses and investigation priorities

**Audience**: Security architects, threat hunters, incident responders, SOC managers, penetration testers

**Frequency**: Monthly, with ad-hoc updates for significant campaigns, technique evolution, or **critical vulnerability exploitation (CVSS 9.0+)**

### 2.2.4 Operational Intelligence Analysis

The organization SHALL produce operational threat intelligence to enable immediate defensive actions and threat detection.

**Operational Intelligence Requirements**:

- **Indicator Management**: Processing and enrichment of indicators of compromise (IOCs):
  - Deduplication and normalization of indicators
  - Context enrichment (threat actor association, campaign linkage, severity, **CVSS scores for CVE indicators**)
  - False positive filtering and validation
  - Aging and expiration of stale indicators
  - Prioritization based on organizational relevance and **CVSS severity**

- **Active Campaign Monitoring**: Tracking of ongoing threat campaigns:
  - Real-time updates on active exploitation
  - Targeting of specific industries, technologies, or regions
  - Immediate defensive actions required
  - Compromise assessment recommendations
  - **Prevention tracking**: Document blocked attacks and prevented incidents with **CVSS severity documentation**
  - **Evidence tracked in**: ISMS-IMP-A.5.7.3 Sheet 7 (Prevention Tracking)

- **Vulnerability Exploitation Tracking (Control A.8.8 Integration - OPTIONAL)** - **EXPANDED in v2.0**:
  - Zero-day exploitation in the wild (assign temporary severity until CVSS available)
  - Widespread exploitation of recently disclosed vulnerabilities
  - **CVSS 7.0+ (High/Critical) vulnerabilities with active exploitation → Priority escalation**
  - **CVSS 9.0+ (Critical) vulnerabilities with mass exploitation → Emergency patching**
  - Exploitation of vulnerabilities in organizational technology stack
  - Patch priority escalation based on **CVSS score + active exploitation status**
  - **When Control A.8.8 implemented**: Automated VTL record creation for emergency patching

**VTL Record Creation Criteria** - **NEW in v2.0**:
- **Automatic VTL Creation**:
  - CVSS 9.0-10.0 (Critical) + Active Exploitation → Immediate VTL record
  - CVSS 7.0-8.9 (High) + Mass Exploitation → VTL record within 4 hours
  - Any CVSS + Exploitation of Critical Assets → VTL record within 8 hours

- **Manual VTL Assessment**:
  - CVSS 4.0-6.9 (Medium) + Active Exploitation → Analyst review, potential VTL
  - CVSS 7.0+ (High/Critical) + PoC Available → Monitor for exploitation, prepare VTL

- **No VTL Required**:
  - Any CVSS + No Known Exploit → Standard vulnerability management (A.8.8)
  - CVSS 0.1-3.9 (Low) even with exploitation → Standard patching cycle

- **Malware Analysis Summary**: Behavioral analysis of relevant malware families:
  - Infection vectors and delivery mechanisms
  - Capabilities and objectives
  - Network indicators and communication protocols
  - Detection signatures and mitigation techniques
  - **Exploited CVEs used in malware delivery with CVSS scores**

**Audience**: SOC analysts, incident responders, network defenders, vulnerability management team (when Control A.8.8 implemented)

**Frequency**: Real-time or daily operational intelligence feeds with immediate alerting for **critical threats (CVSS 9.0+ active exploitation, zero-days, targeted campaigns)**

### 2.2.5 Analysis Methodology Standards

All threat intelligence analysis SHALL adhere to the following standards:

**Structured Analysis Frameworks**:
- **MITRE ATT&CK**: Map adversary TTPs to ATT&CK techniques and sub-techniques
- **Diamond Model**: Analyze intrusions using Adversary-Capability-Infrastructure-Victim framework
- **Cyber Kill Chain**: Identify defensive opportunities at each attack stage
- **CVSS Scoring**: Apply CVSS 4.0 (preferred) or 3.1 (acceptable) for vulnerability severity assessment - **NEW in v2.0**

**Confidence Assessment**:
- All intelligence SHALL include confidence level (High, Medium, Low)
- Confidence based on source reliability (Admiralty Code), corroboration, and analyst assessment
- **CVSS scores from authoritative sources (NVD, vendors) have High confidence by default**
- High confidence: Multiple corroborating sources or direct observation
- Medium confidence: Single reliable source or logical inference
- Low confidence: Unverified source or insufficient evidence

**Bias Mitigation**:
- Analysts SHALL be trained in cognitive biases affecting intelligence analysis
- Peer review required for strategic and high-impact tactical intelligence
- Alternative hypotheses SHALL be considered and documented
- Challenge assumptions and avoid confirmation bias

**Documentation Standards**:
- All finished intelligence SHALL follow templates (ISMS-POL-A.5.7-S5 Annex B)
- Intelligence SHALL include: executive summary, detailed analysis, confidence assessment, recommended actions, supporting evidence, **CVSS scores for vulnerability intelligence**
- Intelligence reports SHALL be stored in central repository with unique IDs for cross-referencing

**Quality Assurance**:
- Peer review for all strategic intelligence and high-impact tactical intelligence
- CISO or Threat Intelligence Team Lead approval for executive distribution
- Post-publication feedback loop to refine future analysis
- **CVSS accuracy validation** against NVD/vendor advisories - **NEW in v2.0**

---

## 2.3 Intelligence Dissemination and Integration Requirements

### 2.3.1 Distribution Requirements

The organization SHALL distribute threat intelligence to appropriate stakeholders based on intelligence type, sensitivity, and consumer needs.

**Distribution Channels**:
- Formal intelligence reports (strategic, tactical, operational)
- Real-time alerting (critical threats, active campaigns, **CVSS 9.0+ mass exploitation**)
- Intelligence portal / TIP (on-demand access, self-service queries)
- Integration with security tools (SIEM, EDR, firewalls, email gateway)
- Stakeholder briefings (executive, SOC, incident response, vulnerability management)
- Information sharing communities (ISACs, ISAOs, peer groups)

**Distribution Frequency**:
- **Strategic Intelligence**: Quarterly reports, ad-hoc for significant threats
- **Tactical Intelligence**: Monthly reports, ad-hoc for emerging campaigns or **critical CVEs**
- **Operational Intelligence**: Real-time/daily feeds, immediate alerts for **CVSS 9.0+ active exploitation**
- **VulnerabilityThreatLink (VTL) Records**: Real-time creation and distribution to vulnerability management (when A.8.8 implemented)

**Classification and Handling**:
- All intelligence SHALL be classified (Public, Internal, Confidential, Restricted)
- External intelligence SHALL respect source TLP markings (CLEAR, GREEN, AMBER, AMBER+STRICT, RED)
- Distribution SHALL be limited to authorized recipients based on classification
- Recipients SHALL be trained on proper handling of classified intelligence

**Stakeholder Registry**:
- Maintain registry of threat intelligence consumers (name, role, intelligence types, delivery method)
- **Documented in**: ISMS-IMP-A.5.7.3 Sheet 1 (Stakeholder Register)
- Quarterly review and update of stakeholder requirements
- Feedback mechanism for consumers to request adjustments

### 2.3.2 Security Tool Integration Requirements

Threat intelligence SHALL be integrated with organizational security tools to enable automated detection and response.

**SIEM Integration** (Control A.8.16 - MANDATORY):
- IOC ingestion (IP addresses, domains, file hashes, URLs)
- Correlation rules based on threat actor TTPs
- Automated alerting for IOC matches
- **CVSS-scored vulnerability context** in security events
- Threat intelligence enrichment of security alerts
- Evidence: Documented in ISMS-IMP-A.5.7.3 Sheet 3 (SIEM Integration)

**EDR Integration** (Control A.8.16 - MANDATORY):
- Malware signatures and behavioral indicators
- Threat hunting queries based on adversary TTPs
- Automated response actions (quarantine, isolate, block)
- Endpoint telemetry feeding threat intelligence (internal sources)

**Firewall / IPS Integration**:
- Malicious IP address and domain blocking
- Network-based IOC blocking
- Geolocation-based filtering (threat actor countries)
- Regular update frequency (daily minimum for dynamic threats)

**Email Gateway Integration**:
- Phishing indicator blocking (domains, sender addresses, subject patterns)
- Malicious attachment signatures
- URL rewriting and sandboxing for suspicious links
- Feedback loop: Blocked emails inform threat intelligence

**Web Proxy Integration** (Control A.8.23 - OPTIONAL):
- Malicious URL/domain blocklists
- C2 infrastructure blocking
- Threat category filtering
- Web access telemetry feeding threat intelligence

**Vulnerability Management Integration** (Control A.8.8 - OPTIONAL) - **EXPANDED in v2.0**:
- **VulnerabilityThreatLink (VTL) records** created for active exploitation
- **CVSS 4.0/3.1 scores** enable automated priority escalation
- Active exploitation intel → Emergency patching workflows
- Remediation status feedback → Threat intelligence tracking
- **Documented in**: ISMS-IMP-A.5.7.2 Sheet 8 (VTL Records)

**Integration Validation**:
- Quarterly testing of all integrations (IOC blocking, alerting, VTL workflows)
- Measure detection rates and false positive rates
- Validate that **CVSS-based prioritization** is functioning correctly (when A.8.8 implemented)
- Document integration effectiveness in ISMS-IMP-A.5.7.3 Sheet 4 (Tool Integration Status)

### 2.3.3 Vulnerability Management Integration (Control A.8.8 - OPTIONAL) - **EXPANDED in v2.0**

When [Organization] implements Control A.8.8 (Management of Technical Vulnerabilities), threat intelligence SHALL integrate with vulnerability management through the **VulnerabilityThreatLink (VTL) schema**.

**VTL Schema Purpose**:
- Link threat intelligence (active exploitation) to specific CVEs
- Combine **CVSS severity scores** with exploitation status for intelligent prioritization
- Enable automated emergency patching workflows
- Track remediation status and validate prevented incidents
- Provide bidirectional data flow: A.5.7 → A.8.8 (exploitation intel), A.8.8 → A.5.7 (remediation status)

**VTL Record Requirements** - **UPDATED in v2.0**:

**Mandatory Fields**:
- **Link_ID**: Unique identifier (VTL-YYYYMMDD-HHMMSS format)
- **Vulnerability_ID**: CVE identifier (CVE-YYYY-NNNNN format)
- **CVSS_Version**: Scoring version (4.0 or 3.1) - **NEW in v2.0**
- **CVSS_Base_Score**: Numerical severity (0.0-10.0) - **NEW in v2.0**
- **CVSS_Vector**: Complete vector string for score reproduction - **NEW in v2.0**
- **Exploitation_Status**: PoC Available, Active Exploitation, Mass Exploitation
- **Threat_Actor_Type**: Nation-State, Organized Crime, Hacktivist, Opportunistic, Unknown
- **Criticality**: Priority rating 1-10 (formula: CVSS score + exploitation weight)
- **Detection_Date**: When exploitation first detected (ISO format)
- **TI_Source**: Threat intelligence source reporting exploitation (with Admiralty Code)
- **Critical_Assets_Affected**: Yes/No (based on asset inventory analysis)
- **Emergency_Patch_Required**: Yes/No (auto-calculated from CVSS + exploitation + critical assets)

**Optional but Recommended Fields**:
- **CVSS_Temporal_Score**: Accounting for exploit maturity (when available)
- **CVSS_Environmental_Score**: Organizational context adjustment (calculated internally)
- **Attack_Vector_Detail**: Network accessible, requires local access, etc.
- **Privileges_Required**: None, Low, High
- **Affected_Assets**: Specific systems with vulnerability
- **Patch_Available**: Yes/No/Workaround
- **Expected_Patch_Date**: When patch deployment planned
- **Threat_Campaign_Link**: Associated campaign ID if part of larger operation
- **IOCs**: File hashes, IPs, domains associated with exploitation

**VTL Record Creation Workflow**:

1. **Threat Intelligence Analyst** detects active exploitation via:
   - Commercial threat intelligence feed alert
   - CISA KEV listing
   - Security vendor advisory
   - Internal SOC detection
   - ISAC/ISAO notification

2. **Validate Exploitation**:
   - Confirm CVE ID and **CVSS score** (from NVD or vendor advisory)
   - Assess exploitation status (PoC, Active, Mass)
   - Identify threat actor if possible
   - Check if organizational assets affected (query asset inventory)

3. **Create VTL Record** (ISMS-IMP-A.5.7.2 Sheet 8):
   - Generate Link_ID
   - Populate all mandatory fields including **CVSS 4.0 or 3.1 data**
   - Calculate Criticality: Base = CVSS score, +2 if Mass Exploitation, +2 if Critical Assets, +1 if Nation-State
   - Set Emergency_Patch_Required flag if: (CVSS ≥7.0 AND Active Exploitation) OR (CVSS ≥9.0) OR (Critical Assets = Yes AND Exploitation ≠ No Known Exploit)

4. **Distribute VTL Record**:
   - **Immediate notification** to Vulnerability Management Team (when A.8.8 implemented)
   - Email/Slack alert for Emergency_Patch_Required = Yes
   - Automated import to A.8.8 vulnerability prioritization workbook
   - Escalation to CISO if Critical Assets affected + Nation-State actor

5. **Track Remediation** (A.8.8 → A.5.7 feedback):
   - Vulnerability Management updates Remediation_Status field
   - Threat Intelligence tracks time-to-remediation metrics
   - Closed VTL records contribute to "Prevented Incidents" KPI
   - Post-remediation validation (re-scan evidence)

**CVSS-Based Prioritization Matrix** - **NEW in v2.0**:

| CVSS Score | No Exploit | PoC Available | Active Exploitation | Mass Exploitation |
|------------|-----------|---------------|---------------------|-------------------|
| **9.0-10.0 (Critical)** | Priority 7 | Priority 8 | Priority 10 (Emergency) | Priority 10 (Emergency) |
| **7.0-8.9 (High)** | Priority 5 | Priority 6 | Priority 9 (Emergency) | Priority 10 (Emergency) |
| **4.0-6.9 (Medium)** | Priority 3 | Priority 4 | Priority 7 | Priority 8 |
| **0.1-3.9 (Low)** | Priority 1 | Priority 2 | Priority 4 | Priority 5 |

**Emergency Patching Criteria**:
- Priority 9-10 vulnerabilities trigger emergency patching workflow (A.8.8)
- Emergency patching SLA: 24-72 hours depending on exploitability and asset criticality
- CISO approval authority for emergency changes to production systems
- Post-patch validation required before closing VTL record

**Without Control A.8.8**:
- Basic threat intelligence consumption (CISA KEV, vendor advisories, **CVSS scores**)
- Manual vulnerability prioritization by IT/Security teams
- No automated VTL workflow
- Threat intelligence provides recommendations, but no formal integration

**With Control A.8.8**:
- Full VTL schema integration with **CVSS-based automated priority escalation**
- Bidirectional data flow and remediation tracking
- Automated emergency patching workflows
- Objective evidence of prevented incidents with **CVSS severity documentation**

### 2.3.4 Incident Response Integration (Controls A.5.24-5.28 - MANDATORY)

Threat intelligence SHALL support incident investigation and response capabilities.

**Incident Enrichment**:
- Automatically enrich security incidents with threat intelligence context
- Provide IOCs, TTPs, and threat actor attribution for incidents
- **Document CVSS scores** for vulnerability-related incidents
- Estimate incident severity based on threat actor sophistication
- **Evidence tracked in**: ISMS-IMP-A.5.7.3 Sheet 14 (Incident-TI Integration)

**Integration Requirements**:
- Incident ticketing system integration for automatic TI enrichment
- Threat intelligence analysts participate in P1/P2 incident response
- Post-incident: Extract IOCs and lessons learned to inform future intelligence
- **Target**: ≥70% of P1/P2 incidents use threat intelligence

**Incident-to-Intelligence Feedback Loop**:
- Incident findings inform threat intelligence collection requirements
- New IOCs discovered during incident response → Added to indicator feeds
- Attack TTPs observed → Mapped to MITRE ATT&CK and shared with community
- **Exploited CVEs** → Create VTL records to prevent future exploitation

---

## 2.4 Program Effectiveness and Measurement Requirements

### 2.4.1 Key Performance Indicators (KPIs)

The threat intelligence program SHALL be measured against the following quantitative KPIs:

**Intelligence Production Metrics**:
- Number of finished intelligence reports produced (strategic, tactical, operational)
- Intelligence report quality ratings from stakeholders (1-5 scale, target ≥4.0)
- Time from threat detection to intelligence dissemination (target: <24 hours for critical threats)
- **VulnerabilityThreatLink (VTL) records created** (when A.8.8 implemented) - **NEW in v2.0**
- **CVSS-scored vulnerabilities tracked** per quarter - **NEW in v2.0**

**Source Performance Metrics**:
- Number of active threat intelligence sources
- Source accuracy rate (target: ≥85% overall, ≥80% per source)
- **CVSS accuracy rate** (target: ≥90% ±1.0 point tolerance) - **NEW in v2.0**
- Source coverage across threat categories, attack vectors, and technologies
- Cost per source and value delivered
- Admiralty Code ratings distribution

**Integration and Operationalization Metrics**:
- Percentage of IOCs successfully integrated into security tools (target: ≥95%)
- SIEM correlation rules based on threat intelligence (target: ≥50 active rules)
- EDR detection signatures from threat intelligence (target: ≥100 active signatures)
- **VTL records successfully triggering emergency patching** (when A.8.8 implemented) - **NEW in v2.0**
- Security tool integration uptime (target: ≥99%)

**Threat Detection and Prevention Metrics**:
- Threats detected via threat intelligence IOCs (count per quarter)
- **Number of attacks prevented through proactive intelligence** (validated with evidence, including **CVSS severity documentation**)
- Reduction in dwell time (time from compromise to detection)
- Reduction in mean time to detect (MTTD) and respond (MTTR)
- **Target**: ≥3 documented prevented incidents per quarter (per ISMS-POL-A.5.7 Section 4.4.2)
- **Evidence tracked in**: ISMS-IMP-A.5.7.3 Sheet 7 (Prevention Tracking)

**Risk Management Impact (Clause 6.1 - MANDATORY)**:
- **Updates to risk assessments based on threat intelligence**
- Risk treatment decisions informed by intelligence
- **CVSS-based vulnerability risk quantification** for vulnerability-related risks - **NEW in v2.0**
- Vulnerability prioritization improvements (when Control A.8.8 implemented)
- Reduction in exploitable vulnerabilities
- **Target**: ≥3 risk assessment updates per quarter (per ISMS-POL-A.5.7 Section 4.4.1)
- **Evidence tracked in**: ISMS-IMP-A.5.7.3 Sheet 13 (Risk Assessment Updates)

**Incident Response Impact (Controls A.5.24-5.28 - MANDATORY)**:
- Faster incident triage and categorization
- Improved attribution and campaign association
- More effective containment and eradication
- Reduced incident investigation time
- **Target**: ≥70% of P1/P2 incidents use threat intelligence (per ISMS-POL-A.5.7 Section 4.4.4)
- **Evidence tracked in**: ISMS-IMP-A.5.7.3 Sheet 14 (Incident-TI Integration)

**Intelligence-Driven Decisions**:
- Policy changes informed by threat intelligence
- Technical control implementations based on threat landscape
- Security investment decisions justified by intelligence (including **CVSS-based vulnerability prioritization**)
- Training and awareness content updated with current threats
- **Target**: ≥5 intelligence-driven decisions per quarter (per ISMS-POL-A.5.7 Section 4.4.5)
- **Evidence tracked in**: ISMS-IMP-A.5.7.3 Sheet 15 (Intelligence-Driven Decisions)

**Cost Avoidance**:
- Prevented incidents and estimated cost savings (with **CVSS severity as impact multiplier**)
- Optimized security investments based on threat intelligence
- Reduced false positives and alert fatigue

### 2.4.2 Qualitative Effectiveness Measures

**Stakeholder Satisfaction**:
- Quarterly surveys of threat intelligence consumers
- Usefulness, timeliness, accuracy, and actionability ratings
- Open feedback on improvement opportunities
- **Target**: ≥4.0/5.0 average satisfaction score (per ISMS-POL-A.5.7)

**Program Maturity Assessment**:
- Annual self-assessment against industry frameworks (SANS Threat Intelligence Survey, etc.)
- Identification of capability gaps and improvement priorities
- **CVSS 4.0 adoption progress** tracking - **NEW in v2.0**
- Benchmarking against peer organizations

**Audit and Compliance**:
- ISO 27001:2022 Control A.5.7 compliance evidence
- Clause 6.1 integration demonstration (risk assessment updates with **CVSS-based quantification**)
- External audit findings and recommendations
- Regulatory compliance (FADP, GDPR, NIS2 where applicable)

### 2.4.3 Continuous Improvement

The threat intelligence program SHALL include a continuous improvement process:

**Regular Program Reviews**: Quarterly assessment of program effectiveness including:
- Metrics review and trend analysis against targets (Section 2.4.1)
- Consumer feedback and satisfaction surveys (target: ≥4.0/5.0)
- Gap analysis against threat landscape evolution
- **CVSS version migration progress** (Q1-Q4 2026 transition tracking) - **NEW in v2.0**
- Benchmarking against industry peers
- **KPI dashboard review** (ISMS-IMP-A.5.7.4)

**Intelligence Requirements Refinement**: Ongoing review and update of intelligence requirements based on:
- Changes to organizational risk profile
- Feedback from intelligence consumers
- Gaps identified during incident response
- Evolution of threat landscape (new adversaries, TTPs, **critical CVEs**)

**Source and Process Optimization**:
- Addition of new sources to address coverage gaps (prioritize **CVSS 4.0 support**)
- **Deprecation of low-value sources** (accuracy <80%, **CVSS accuracy <85%**)
- Automation of repetitive analysis tasks
- Integration improvements with security tools
- **VTL workflow optimization** when A.8.8 implemented

**Training and Development**:
- Analyst skill development in threat intelligence tradecraft
- **CVSS 4.0 scoring methodology training** for all analysts - **NEW in v2.0**
- Cross-training with incident response and threat hunting teams
- Participation in industry training and conferences
- Knowledge sharing and lessons learned sessions

**Audit Preparation**:
- Quarterly evidence package generation (per ISMS-POL-A.5.7 Section 4.5)
- Validation of all metrics against targets
- **CVSS data quality validation** in VTL records and prevented incidents
- Documentation of non-conformances and corrective actions
- Audit readiness review 30 days before certification audit

---

## 2.5 Special Considerations

### 2.5.1 Privacy and Legal Compliance

Threat intelligence collection and analysis SHALL comply with all applicable privacy and data protection regulations:

**Personal Data in Threat Intelligence**: Where threat intelligence contains personal data (e.g., email addresses, usernames, IP addresses):
- Lawful basis for processing SHALL be established (legitimate interest, legal obligation, etc.)
- Data minimization principles SHALL be applied
- Retention periods SHALL be defined and enforced
- Access SHALL be restricted to authorized personnel
- Sharing SHALL comply with data transfer requirements

**Monitoring and Surveillance**: Threat intelligence collection from internal systems SHALL comply with:
- Employee privacy laws and works council agreements (where applicable)
- Transparency requirements (privacy notices, acceptable use policies)
- Proportionality and necessity principles
- Legal restrictions on content inspection

### 2.5.2 Classification and Handling

Threat intelligence SHALL be classified and handled according to its sensitivity:

**Public**: Intelligence from open sources with no organizational context (e.g., generic CVE information, **public CVSS scores from NVD**)

**Internal**: Intelligence for organizational use containing general threat information but no sensitive details (e.g., **VTL records without specific asset identifiers**)

**Confidential**: Intelligence containing organizational context, incident details, or vulnerability information (e.g., **VTL records with Critical_Assets_Affected = Yes**)

**Restricted**: Highly sensitive intelligence containing classified information, customer data, or advanced adversary TTPs

Classification SHALL dictate storage, transmission, sharing, and retention requirements.

**Traffic Light Protocol (TLP)**: When sharing externally, use TLP markings:
- **TLP:CLEAR**: Unlimited disclosure
- **TLP:GREEN**: Community-wide disclosure
- **TLP:AMBER**: Limited disclosure
- **TLP:AMBER+STRICT**: Limited disclosure, no further sharing
- **TLP:RED**: Recipients only, no further disclosure

### 2.5.3 Third-Party and Supplier Considerations

When threat intelligence involves third-party systems or suppliers:

**Supplier Notification**: Where threat intelligence identifies supplier vulnerabilities or compromises, suppliers SHALL be notified in accordance with contractual obligations and responsible disclosure practices (see Control 5.20). **CVSS scores SHALL be communicated** to help suppliers prioritize remediation.

**Cloud Service Provider Intelligence**: Threat intelligence SHALL incorporate data from cloud service providers where the organization uses cloud services (see Control 5.23). **CSP-provided CVSS scores** are considered authoritative for CSP-specific vulnerabilities.

**Supply Chain Threat Intelligence**: Intelligence collection SHALL include supply chain threats affecting vendors, suppliers, and service providers (see Controls 5.19-5.22). **Monitor CVEs affecting supply chain components** with CVSS severity assessment.

---

## 2.6 Evidence and Audit Requirements

### 2.6.1 Mandatory Evidence Generation

All threat intelligence activities SHALL generate evidence as defined in ISMS-POL-A.5.7 Section 4.4:

**Clause 6.1 Integration Evidence (Section 4.4.1)**:
- Quarterly report: "Threat Intelligence Impact on Risk Assessment"
- Cross-reference: TI Report ID → Risk Register Entry ID → Likelihood/Impact Changes
- **CVSS-based vulnerability risk quantification** documentation - **NEW in v2.0**
- Risk owner approval documentation
- **Target**: ≥3 risk assessment updates per quarter

**Prevented Incident Evidence (Section 4.4.2)** - **UPDATED in v2.0**:
- Prevented incident register with before/after states
- **CVSS scores** documenting severity of prevented vulnerability exploits
- Technical validation evidence (scan results, SIEM logs, EDR telemetry)
- SIEM query IDs for reproducibility
- **Target**: ≥3 documented prevented incidents per quarter

**Intelligence Accuracy Validation (Section 4.4.3)** - **UPDATED in v2.0**:
- Quarterly source performance analysis
- Per-source accuracy metrics
- **CVSS accuracy validation** (source-reported vs. NVD/vendor advisory)
- Source continuation/discontinuation decisions
- **Target**: ≥85% overall accuracy, **≥90% CVSS accuracy**

**Incident-TI Integration Evidence (Section 4.4.4)** - **UPDATED in v2.0**:
- Incident register cross-reference: Incident ID → TI Reports Used
- **CVSS context** for vulnerability-related incidents
- Incident handler effectiveness ratings
- Investigation time reduction metrics
- **Target**: ≥70% of P1/P2 incidents use TI

**Intelligence-Driven Decisions (Section 4.4.5)** - **UPDATED in v2.0**:
- Decision register: TI Report → Decision → Implementation → Outcome
- **CVSS-based vulnerability prioritization** decisions documented
- Measurable outcomes (incidents prevented, costs avoided, time saved)
- **Target**: ≥5 intelligence-driven decisions per quarter

**Business Continuity Evidence (Section 4.4.6)**:
- Backup personnel assignments
- Critical source access documentation
- Annual continuity test results

### 2.6.2 Assessment Workbooks

Evidence SHALL be documented in the following workbooks:
- **ISMS-IMP-A.5.7.1**: Threat Intelligence Sources Assessment (source vetting, reliability tracking, **CVSS support validation**)
- **ISMS-IMP-A.5.7.2**: Intelligence Collection & Analysis Assessment (analysis quality, **VTL records with CVSS 4.0/3.1 fields**)
- **ISMS-IMP-A.5.7.3**: Intelligence Integration & Distribution Assessment (risk updates with **CVSS quantification**, prevention with **CVSS severity**, incidents, decisions)
- **ISMS-IMP-A.5.7.4**: Effectiveness Dashboard (consolidated KPIs, executive summary, **CVSS adoption metrics**)

### 2.6.3 Audit Preparation

Thirty days before ISO 27001 certification audit:
- Generate all quarterly workbooks
- Validate against sanity check scripts (including **CVSS field validation**)
- Prepare audit evidence package per ISMS-POL-A.5.7 Section 4.5
- **Prepare CVSS scoring methodology documentation** for auditor questions
- CISO review of audit readiness
- Auditor briefing document finalized

---

**END OF DOCUMENT**