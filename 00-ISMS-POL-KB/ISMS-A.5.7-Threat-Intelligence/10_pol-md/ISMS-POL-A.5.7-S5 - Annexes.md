# ISMS-POL-A.5.7-S5
## Threat Intelligence - Annexes

**Document ID**: ISMS-POL-A.5.7-S5  
**Title**: Threat Intelligence - Annexes  
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

## Overview

This document provides supporting annexes for the Threat Intelligence policy framework, including:

- **Annex A**: Threat Intelligence Source Standards
- **Annex B**: Intelligence Report Templates
- **Annex C**: Threat Intelligence Procedure Summary
- **Annex D**: Quick Reference Guide
- **Annex E**: Glossary and Acronyms (EXPANDED CVSS entry in v2.0)
- **Annex F**: Document Relationships and Cross-References

These annexes are maintained as part of the policy framework but may be updated more frequently than core policy sections to reflect operational needs.

---

## Annex A: Threat Intelligence Source Standards

### A.1 Source Categorization

Threat intelligence sources SHALL be categorized to facilitate evaluation and management:

**Category 1: Government and Public Sector**
- National CERTs and cybersecurity agencies (NCSC-CH, CISA, ENISA, etc.)
- Law enforcement cybercrime units
- Government threat reports and advisories
- Critical infrastructure protection programs

**Characteristics**:
- High reliability, typically free of charge
- Broad coverage but may lack timeliness for tactical/operational intelligence
- Focus on strategic and high-impact threats
- May have geographic or sector-specific focus
- **CVSS scores provided by authoritative sources (e.g., CISA KEV includes CVSS 3.1, transitioning to 4.0)** - **NEW in v2.0**

**Category 2: Commercial Threat Intelligence Providers**
- Subscription-based threat intelligence platforms
- Managed threat intelligence services
- Specialized intelligence (malware analysis, dark web monitoring, adversary tracking)

**Characteristics**:
- Variable quality across providers
- Typically high cost
- Broad or niche coverage depending on provider
- Integration capabilities vary
- SLAs and support available
- **CVSS 4.0 support becoming standard among leading providers** - **NEW in v2.0**

**Category 3: Open Source Intelligence (OSINT)**
- Security researcher blogs and publications
- Vulnerability databases (NVD, CVE)
- Security community forums and mailing lists
- Academic research
- Malware analysis repositories (VirusTotal, Hybrid Analysis, etc.)

**Characteristics**:
- Free or low cost
- Variable quality and reliability
- Requires significant analyst effort to filter and validate
- Often leading-edge for new threats
- No SLAs or formal support
- **NVD provides authoritative CVSS scores (3.1 currently, 4.0 adoption in progress)** - **NEW in v2.0**

**Category 4: Industry Collaboration**
- ISACs/ISAOs for relevant sectors
- Peer security organizations
- Industry working groups
- Vendor security bulletins

**Characteristics**:
- High relevance to specific industries/technologies
- Reciprocal sharing expected
- Trusted community with established protocols (TLP)
- Quality varies by community maturity
- **Vendor advisories include CVSS scores for their products** - **NEW in v2.0**

**Category 5: Internal Sources**
- SIEM, IDS/IPS, EDR, firewall logs
- Incident response data
- Vulnerability scan results (when Control A.8.8 implemented) with **CVSS scoring**
- User reports (phishing, suspicious activity)

**Characteristics**:
- Highest relevance to organizational environment
- Requires processing and analysis
- Valuable for contextualization of external intelligence
- May reveal organization-specific targeting
- **Vulnerability scanners provide CVSS scores (verify 4.0/3.1 support)** - **NEW in v2.0**

### A.2 Source Evaluation Criteria - **UPDATED in v2.0**

New threat intelligence sources SHALL be evaluated using the following criteria:

**Relevance (Weight: 30%)**
- Coverage of threats applicable to organizational industry, geography, and technology stack
- Alignment with intelligence requirements (strategic/tactical/operational)
- Specificity vs. generic threat information

**Scoring**:
- 5: Highly targeted to organizational profile
- 4: Strong alignment with most intelligence requirements
- 3: Moderate relevance, some coverage gaps
- 2: Limited relevance, significant gaps
- 1: Minimal relevance to organization

**Quality (Weight: 25%)**
- Accuracy of past intelligence (validated post-incident)
- False positive rate for IOCs
- Depth of analysis and context provided
- Confidence level transparency
- **CVSS accuracy for vulnerability intelligence (compare to NVD/vendor advisories)** - **NEW in v2.0**

**Scoring**:
- 5: Consistently accurate, <2% false positive rate, excellent analysis, **≥95% CVSS accuracy**
- 4: Generally accurate, <5% false positive rate, good analysis, **≥90% CVSS accuracy**
- 3: Acceptable accuracy, <10% false positive rate, adequate analysis, **≥85% CVSS accuracy**
- 2: Frequent inaccuracies, >10% false positive rate, shallow analysis, **<85% CVSS accuracy**
- 1: Poor accuracy, high false positives, minimal analysis, **poor or no CVSS support**

**Timeliness (Weight: 20%)**
- Update frequency
- Time from threat emergence to intelligence delivery
- Availability of real-time or near-real-time feeds

**Scoring**:
- 5: Real-time or hourly updates, <6 hours from emergence
- 4: Daily updates, <24 hours from emergence
- 3: Weekly updates, <72 hours from emergence
- 2: Monthly updates, >72 hours from emergence
- 1: Irregular or infrequent updates

**Integration (Weight: 15%)** - **UPDATED in v2.0**
- Machine-readable format support (STIX, JSON, CSV, etc.)
- API availability
- Compatibility with existing security tools (SIEM, TIP, EDR, etc.)
- Ease of operationalization
- **CVSS data included in machine-readable feeds (version, score, vector)**

**Scoring**:
- 5: Full API, multiple formats, seamless integration, **CVSS 4.0 in STIX/JSON**
- 4: API available, standard formats, good integration, **CVSS 3.1 in feeds**
- 3: Limited API or formats, manual integration possible, **CVSS in human-readable only**
- 2: Manual download only, difficult integration, **inconsistent CVSS**
- 1: No practical integration capability, **no CVSS support**

**Cost Effectiveness (Weight: 10%)**
- Total cost of ownership (subscription, personnel, infrastructure)
- Value delivered relative to cost
- Return on investment

**Scoring**:
- 5: Free or exceptional value for cost
- 4: Good value for cost
- 3: Acceptable value for cost
- 2: High cost for value delivered
- 1: Excessive cost, minimal value

**Overall Source Score**:
- **Weighted Score Formula**: (Relevance × 0.30) + (Quality × 0.25) + (Timeliness × 0.20) + (Integration × 0.15) + (Cost × 0.10)
- **Minimum Acceptable Score**: 3.0/5.0
- **Recommended Score for Adoption**: 3.5/5.0 or higher

**CVSS Support Evaluation - NEW in v2.0**:

Sources providing vulnerability intelligence SHALL be evaluated for CVSS support:

| CVSS Support Level | Description | Quality Score Impact |
|-------------------|-------------|---------------------|
| **CVSS 4.0 Full** | Complete CVSS 4.0 vectors, base scores, temporal metrics | +0.5 to Quality score |
| **CVSS 4.0 Basic** | CVSS 4.0 base scores only, no vectors | +0.3 to Quality score |
| **CVSS 3.1 Full** | Complete CVSS 3.1 vectors, base scores, temporal metrics | No adjustment (baseline) |
| **CVSS 3.1 Basic** | CVSS 3.1 base scores only, no vectors | -0.2 from Quality score |
| **CVSS 2.0 Only** | Legacy CVSS 2.0 scoring | -0.5 from Quality score |
| **Proprietary Scoring** | Vendor-specific severity without CVSS | -0.8 from Quality score |
| **No Scoring** | No vulnerability severity assessment | -1.0 from Quality score |

**Example Source Evaluation**:

*Commercial Threat Intelligence Provider "ThreatWatch Pro"*:
- Relevance: 5/5 (hosting sector focus)
- Quality: 4/5 (90% accurate, <3% FP, **92% CVSS accuracy, CVSS 4.0 supported → +0.5 bonus → 4.5/5**)
- Timeliness: 5/5 (hourly updates)
- Integration: 5/5 (full API, STIX 2.1, **CVSS 4.0 in JSON feeds**)
- Cost: 3/5 (€45K/year)
- **Weighted Score**: (5 × 0.30) + (4.5 × 0.25) + (5 × 0.20) + (5 × 0.15) + (3 × 0.10) = **4.53/5.0** → **STRONGLY RECOMMENDED**

### A.3 Source Reliability Ratings (Admiralty Code)

The Admiralty Code provides standardized ratings for source reliability and information credibility:

**Source Reliability**:
- **A - Completely Reliable**: No history of false reporting, established track record (e.g., CISA, NVD)
- **B - Usually Reliable**: Minor inaccuracies in past, generally trustworthy (e.g., reputable commercial vendors)
- **C - Fairly Reliable**: Some inaccuracies but provides useful information (e.g., community OSINT)
- **D - Not Usually Reliable**: Significant inaccuracies, use with caution (e.g., unvetted security researchers)
- **E - Unreliable**: Known false reporting, not recommended (e.g., sensationalist blogs)
- **F - Cannot Be Judged**: New source with insufficient track record

**Information Credibility**:
- **1 - Confirmed**: Independently corroborated, directly observed, or validated (e.g., **CVSS from NVD**)
- **2 - Probably True**: Logical, consistent with known facts (e.g., vendor advisory with **CVSS**)
- **3 - Possibly True**: Not confirmed but plausible
- **4 - Doubtful**: Questionable validity, requires verification
- **5 - Improbable**: Unlikely based on analysis
- **6 - Cannot Be Judged**: Insufficient information to assess

**Combined Ratings** (e.g., A1, B2, C3):
- **A1**: Completely reliable source, confirmed information → Highest confidence
- **B2**: Usually reliable source, probably true → High confidence
- **C3**: Fairly reliable source, possibly true → Medium confidence
- **D4**: Not usually reliable, doubtful → Low confidence

**Usage in Threat Intelligence**:
- All threat intelligence sources SHALL have Admiralty Code ratings documented
- Ratings SHALL be reviewed quarterly during source performance validation
- Intelligence reports SHALL include source ratings (e.g., "This report is based on A1 and B2 sources")
- **CVSS scores from NVD are considered A1 (completely reliable, confirmed)** - **NEW in v2.0**
- **CVSS scores from vendor advisories are typically B1 (usually reliable, confirmed)** - **NEW in v2.0**

---

## Annex B: Intelligence Report Templates

### B.1 Strategic Intelligence Report Template

**Header**:
- Report ID: TI-STRAT-YYYY-NNN
- Classification: [Internal/Confidential/Restricted]
- TLP: [CLEAR/GREEN/AMBER/AMBER+STRICT/RED]
- Date: DD.MM.YYYY
- Author: [Name], Threat Intelligence Team
- Confidence Level: [High/Medium/Low]

**Executive Summary** (2-3 paragraphs):
- Key findings and recommendations
- Impact to organizational risk profile
- Recommended executive actions

**Threat Landscape Analysis**:
- Threat actor trends and capabilities
- Attack vector evolution
- Industry-specific threats
- **Critical vulnerability trends (CVSS 9.0+) in organizational technology stack** - **NEW in v2.0**
- Geopolitical factors

**Risk Assessment Integration** (Clause 6.1 - MANDATORY):
- Specific risks identified or updated
- Risk register cross-references
- **CVSS-based vulnerability risk quantification** - **NEW in v2.0**
- Likelihood and impact assessments
- Recommended risk treatments

**Security Investment Recommendations**:
- Control gaps and defensive priorities
- Tool and technology recommendations
- Training and staffing needs
- **Emergency patching budget for actively exploited CVSS 9.0+ vulnerabilities** - **NEW in v2.0**

**Appendices**:
- Supporting data and statistics
- Source citations with Admiralty Code ratings
- Related tactical and operational intelligence references

### B.2 Tactical Intelligence Report Template

**Header**:
- Report ID: TI-TACT-YYYY-NNN
- Classification: [Internal/Confidential]
- TLP: [CLEAR/GREEN/AMBER]
- Date: DD.MM.YYYY
- Author: [Name], Threat Intelligence Team
- Confidence Level: [High/Medium/Low]

**Executive Summary** (1 paragraph):
- Campaign or TTP being analyzed
- Relevance to organization
- Recommended defensive actions

**Adversary TTP Analysis**:
- MITRE ATT&CK mapping (tactics, techniques, sub-techniques)
- Technique descriptions and examples
- **Exploitation techniques for CVEs with CVSS scores** - **NEW in v2.0**
- Typical attack sequences (kill chain mapping)

**Campaign Details** (if applicable):
- Campaign timeline and phases
- Targeting criteria and victim profile
- Indicators of compromise (IOCs)
- Threat actor attribution

**Defensive Recommendations**:
- Detection strategies (SIEM rules, EDR signatures, threat hunting queries)
- Prevention controls (configuration hardening, access controls)
- Mitigation techniques (for vulnerabilities, **reference CVSS scores and VTL records**)
- Response playbooks

**Related Intelligence**:
- Links to strategic intelligence reports
- Cross-references to operational IOC feeds
- **VulnerabilityThreatLink (VTL) records created** - **NEW in v2.0**

### B.3 Operational Intelligence Report Template

**Header**:
- Report ID: TI-OPS-YYYY-NNN
- Classification: [Internal/Confidential]
- TLP: [AMBER/RED typically]
- Date: DD.MM.YYYY HH:MM (timestamp for time-sensitive intelligence)
- Author: [Name], Threat Intelligence Team
- Urgency: [Critical/High/Medium/Low]
- Confidence Level: [High/Medium/Low]

**Immediate Threat Summary** (1-2 sentences):
- What is the threat?
- Why does it matter to us?
- What action is required?

**Indicators of Compromise (IOCs)**:
- File hashes (MD5, SHA-1, SHA-256)
- IP addresses
- Domain names and URLs
- Email addresses
- Registry keys
- **CVE identifiers with CVSS 4.0 or 3.1 scores** - **NEW in v2.0**
- Other artifacts

**Threat Context**:
- Threat actor (if known)
- Campaign association (if applicable)
- Malware family or tool
- Attack vector and technique
- **For vulnerabilities: CVSS score, exploitation status, affected assets** - **NEW in v2.0**

**Recommended Actions**:
- Immediate: Block IOCs, hunt for presence, **emergency patch CVSS 9.0+ exploited CVEs**
- Short-term: Enhanced monitoring, threat hunting campaigns
- Long-term: Control improvements, vulnerability remediation

**Tool Integration**:
- SIEM correlation rules to deploy
- EDR signatures to enable
- Firewall/IPS rules to implement
- **VTL record created** (if vulnerability-related) - **NEW in v2.0**

**Validation and Feedback**:
- How to confirm compromise or absence of threat
- Reporting mechanism for positive detections
- Analyst contact for questions

### B.4 VulnerabilityThreatLink (VTL) Report Template - **NEW in v2.0**

**Header**:
- Report ID: TI-VTL-YYYY-NNN
- VTL Record ID: VTL-YYYYMMDD-HHMMSS
- Classification: [Confidential/Restricted]
- TLP: [AMBER typically]
- Date: DD.MM.YYYY HH:MM
- Author: [Name], Threat Intelligence Team
- Urgency: [CRITICAL if Emergency_Patch_Required = Yes]

**Vulnerability Summary**:
- **CVE ID**: CVE-YYYY-NNNNN
- **CVSS Version**: 4.0 or 3.1
- **CVSS Base Score**: X.X (None/Low/Medium/High/Critical)
- **CVSS Vector String**: Full vector for reproduction
- **Exploitation Status**: PoC Available / Active Exploitation / Mass Exploitation
- **Threat Actor**: Nation-State / Organized Crime / Hacktivist / Opportunistic / Unknown

**Organizational Impact**:
- **Affected Assets**: List of systems with vulnerability (from asset inventory)
- **Critical Assets Affected**: Yes/No
- **Business Impact**: Description of potential consequences
- **VTL Criticality Score**: 1-10 (auto-calculated from CVSS + exploitation + assets)

**Exploitation Intelligence**:
- First detection date of exploitation
- Threat intelligence sources (with Admiralty Code ratings)
- Exploitation campaigns observed
- Threat actor TTPs using this vulnerability
- IOCs associated with exploitation attempts

**Remediation Guidance**:
- **Patch Available**: Yes/No/Workaround
- **Vendor Advisory**: Link to official vendor advisory with CVSS
- **Patch Priority**: Emergency / High / Medium / Low
- **Recommended Timeline**: Hours/days based on CVSS + exploitation
- **Compensating Controls**: If patching delayed
- **Detection**: SIEM rules, EDR signatures to identify exploitation attempts

**Integration Tracking**:
- **Control A.8.8 Status**: Implemented / Not Implemented
- If implemented: Emergency patching workflow triggered
- **Expected Patch Date**: From Vulnerability Management Team
- **Remediation Status**: Open / In Progress / Patched / Mitigated
- **Post-Patch Validation**: Required scan/test before closing VTL

**Follow-Up Actions**:
- SOC: Deploy detection signatures
- Vulnerability Management: Execute emergency patching (if A.8.8 implemented)
- Incident Response: Hunt for exploitation indicators
- Risk Management: Update risk assessment if exploitation successful

---

## Annex C: Threat Intelligence Procedure Summary

### C.1 Intelligence Cycle Overview

The threat intelligence production process follows the intelligence cycle:

**1. Planning and Direction**:
- Define intelligence requirements based on organizational risk profile
- Prioritize collection efforts
- Allocate resources (analysts, tools, budget)
- Establish collection plan and source strategy

**2. Collection**:
- Gather data from internal sources (SIEM, EDR, IDS/IPS, vulnerability scans with **CVSS scores**)
- Subscribe to and consume external sources (commercial feeds, OSINT, government, ISACs)
- Participate in information sharing communities
- Monitor vulnerability disclosures (NVD, vendor advisories with **CVSS 4.0/3.1 scores**)

**3. Processing**:
- Normalize and standardize data formats
- Deduplicate indicators and reports
- Correlate information across sources
- **Validate CVSS scores** against authoritative sources (NVD, vendors) - **NEW in v2.0**
- Filter noise and false positives
- Enrich with context (geolocation, threat actor attribution, **CVSS severity**)

**4. Analysis**:
- Identify patterns, trends, and anomalies
- Apply structured analysis frameworks (MITRE ATT&CK, Diamond Model, Kill Chain)
- **Assess vulnerability severity using CVSS 4.0/3.1** - **NEW in v2.0**
- Determine threat actor capabilities and intentions
- Produce finished intelligence (strategic, tactical, operational)
- **Create VulnerabilityThreatLink (VTL) records** for active exploitation - **NEW in v2.0**
- Assign confidence levels (high, medium, low) with Admiralty Code ratings

**5. Dissemination**:
- Distribute intelligence to appropriate stakeholders
- Integrate IOCs into security tools (SIEM, EDR, firewalls)
- **Distribute VTL records** to Vulnerability Management (when A.8.8 implemented) - **NEW in v2.0**
- Brief executives, SOC, incident response teams
- Share externally with ISACs/ISAOs (respecting TLP)
- Update risk assessments (Clause 6.1)

**6. Feedback**:
- Collect stakeholder feedback on intelligence utility
- Refine intelligence requirements
- Adjust collection priorities
- Improve analysis methodologies (including **CVSS accuracy validation**)
- Optimize dissemination channels

### C.2 VTL Workflow - **NEW in v2.0**

**Step 1: Exploitation Detection**
- Source: Commercial TI feed, CISA KEV, security vendor, ISAC, internal SOC detection
- Trigger: Active exploitation detected for CVE affecting organizational technology

**Step 2: Validation**
- Verify CVE ID in NVD or vendor advisory
- Obtain **CVSS 4.0 score** (preferred) or **CVSS 3.1 score** (acceptable)
- Confirm exploitation status (PoC / Active / Mass)
- Identify threat actor if possible (attribution confidence)
- Check if organizational assets affected (query asset inventory or vulnerability scan results)

**Step 3: VTL Record Creation**
- Generate unique VTL Link_ID: VTL-YYYYMMDD-HHMMSS
- Populate mandatory fields:
  - Vulnerability_ID (CVE-YYYY-NNNNN)
  - **CVSS_Version** (4.0 or 3.1)
  - **CVSS_Base_Score** (0.0-10.0)
  - **CVSS_Vector** (complete string)
  - Exploitation_Status
  - Threat_Actor_Type
  - Detection_Date
  - TI_Source (with Admiralty Code rating)
  - Critical_Assets_Affected (Yes/No)
- Calculate Criticality score (1-10)
- Set Emergency_Patch_Required flag
- Document in ISMS-IMP-A.5.7.2 Sheet 8

**Step 4: Distribution**
- **If Emergency_Patch_Required = Yes**:
  - Immediate notification to Vulnerability Management Team
  - Escalation to CISO if Critical Assets affected
  - Email/Slack alert to Security Leadership
- **If Control A.8.8 implemented**:
  - Automated import to vulnerability prioritization workbook
  - Emergency patching workflow triggered
  - SLA timer starts (24-72 hours depending on severity)
- **Always**:
  - VTL record visible in threat intelligence portal/TIP
  - SOC deploys detection signatures for exploitation attempts
  - Incident Response prepares for potential compromise

**Step 5: Remediation Tracking**
- Vulnerability Management updates Remediation_Status field
- Patch deployment tracked (planned date, actual date)
- Post-patch validation (vulnerability scan confirms remediation)
- If patch delayed: Document compensating controls and risk acceptance
- **Bidirectional data flow**: A.5.7 (threat intel) ↔ A.8.8 (vuln mgmt)

**Step 6: Closure and Evidence**
- Remediation_Status = "Patched" or "Mitigated"
- Validation evidence attached (scan results, change tickets)
- VTL record contributes to "Prevented Incidents" KPI
- **CVSS severity** documents risk avoided
- Lessons learned: Time-to-remediation, process improvements

**Escalation Criteria**:
- **Priority 10 (CRITICAL)**: CVSS 9.0-10.0 + Mass Exploitation + Critical Assets → CISO, CIO, CEO notification
- **Priority 9 (HIGH)**: CVSS 7.0-8.9 + Mass Exploitation → CISO, Vulnerability Management Lead
- **Priority 8**: CVSS 9.0+ + Active Exploitation (not mass yet) → Vulnerability Management Lead
- **Priority 7**: CVSS 7.0+ + Active Exploitation → Standard emergency patching process

### C.3 Quarterly Assessment Workflow

**T-14 days before quarter end**:
- Generate all assessment workbooks (ISMS-IMP-A.5.7.1 through A.5.7.4)
- Populate yellow cells with current quarter data
- Update VTL records with remediation status
- **Validate CVSS accuracy** for all VTL records - **NEW in v2.0**

**T-7 days**:
- Run sanity check scripts (excel_sanity_check_a57_1 through a57_4.py)
- Fix any validation errors
- **Verify CVSS field completeness** in Sheet 8 - **NEW in v2.0**
- Peer review by Threat Intelligence Team Lead

**T-3 days**:
- Calculate KPIs and compare to targets
- Identify gaps (e.g., only 2 prevented incidents, target is 3)
- Prepare executive summary and recommendations
- **CVSS adoption metrics** (% of VTL records with CVSS 4.0 vs 3.1) - **NEW in v2.0**

**Quarter End**:
- CISO review and approval
- Distribute quarterly report to stakeholders
- Archive workbooks in central repository
- Update dashboard (ISMS-IMP-A.5.7.4)

---

## Annex D: Quick Reference Guide

### D.1 Threat Intelligence for Executives

**What is Threat Intelligence?**
Information about cyber threats that helps us make better security decisions.

**Why It Matters**:
- Prevents security incidents before they occur
- Informs risk assessments with current threat data (including **CVSS-scored vulnerabilities**)
- Justifies security investments with evidence
- Reduces incident response time and damage

**What You Receive**:
- Quarterly strategic intelligence reports (threat landscape, risk updates)
- Ad-hoc critical threat briefings (active campaigns, **CVSS 9.0+ mass exploitation**)
- Risk assessment updates based on threat intelligence
- Security investment recommendations

**What You Need to Do**:
- Review quarterly strategic reports
- Approve risk assessment updates based on threat intelligence
- Authorize emergency security investments when critical threats emerge
- Support threat intelligence team resource requests

### D.2 Threat Intelligence for SOC Analysts

**What is Threat Intelligence?**
Actionable information about threats targeting our organization.

**What You Receive**:
- Daily operational intelligence feeds (IOCs, malware signatures)
- Real-time alerts for critical threats (**CVSS 9.0+ exploited vulnerabilities**, active campaigns)
- SIEM correlation rules and EDR detection signatures
- Tactical intelligence on adversary TTPs (monthly reports)

**How to Use It**:
- Enrich security alerts with threat context (threat actor, campaign, **CVSS severity**)
- Hunt for IOCs proactively
- Prioritize incident investigation based on threat intelligence severity
- Provide feedback on intelligence utility and false positives

**Where to Find It**:
- Threat Intelligence Platform (TIP) - self-service queries
- SIEM dashboard - TI-enriched alerts
- Email/Slack - critical threat notifications
- Monthly SOC briefings - TTP training

### D.3 Threat Intelligence for Vulnerability Management

**What is Threat Intelligence?**
Information about actively exploited vulnerabilities requiring priority remediation.

**What You Receive**:
- **VulnerabilityThreatLink (VTL) records** with **CVSS 4.0/3.1 scores** + exploitation status - **NEW in v2.0**
- Emergency patching alerts (CVSS 9.0+ mass exploitation)
- Exploitation trend reports (which CVEs are being targeted)
- Threat actor targeting of specific vulnerabilities

**How to Use It**:
- Prioritize patching: **CVSS score + exploitation status** = true risk - **NEW in v2.0**
- Emergency patch CVSS 9.0+ with mass exploitation within 24-72 hours
- Standard patch High/Critical with no exploitation within SLA
- Update remediation status in VTL records (bidirectional data flow)

**Integration** (when Control A.8.8 implemented):
- VTL records automatically imported to vulnerability prioritization workbook
- Emergency patching workflow triggered for Priority 9-10 VTL records
- Remediation status syncs back to threat intelligence

### D.4 Threat Intelligence for Incident Responders

**What is Threat Intelligence?**
Context and guidance for investigating and responding to security incidents.

**What You Receive**:
- Real-time IOCs for active threats (file hashes, IPs, domains)
- Adversary TTP playbooks (how attacks are conducted)
- **VTL records** for vulnerability-related incidents (with **CVSS context**) - **NEW in v2.0**
- Attribution and campaign information (who is behind the attack)
- Response recommendations and containment strategies

**How to Use It**:
- Enrich incidents with threat context (identify threat actor, campaign, severity)
- Search for additional IOCs from same threat actor or campaign
- Apply appropriate response playbook based on adversary TTPs
- **For vulnerability exploitation incidents**: Reference VTL record for CVSS severity and remediation guidance
- Provide feedback: New IOCs discovered, attack variations observed

**Feedback Loop**:
- Report new IOCs discovered during incident investigation
- Share lessons learned to improve future intelligence
- Contribute to prevented incidents tracking (when threat intelligence enabled early detection)

---

## Annex E: Glossary and Acronyms

### E.1 Acronyms

**APT** - Advanced Persistent Threat  
**ATT&CK** - Adversarial Tactics, Techniques, and Common Knowledge (MITRE framework)  
**BEC** - Business Email Compromise  
**C2** - Command and Control  
**CERT** - Computer Emergency Response Team  
**CISA** - Cybersecurity and Infrastructure Security Agency (USA)  
**CVE** - Common Vulnerabilities and Exposures  
**CVSS** - Common Vulnerability Scoring System (**See comprehensive entry in E.2**)  
**DDoS** - Distributed Denial of Service  
**DLP** - Data Loss Prevention  
**EDR** - Endpoint Detection and Response  
**ENISA** - European Union Agency for Cybersecurity  
**FADP** - Swiss Federal Act on Data Protection  
**FIRST** - Forum of Incident Response and Security Teams  
**GDPR** - General Data Protection Regulation (EU)  
**IDS/IPS** - Intrusion Detection System / Intrusion Prevention System  
**IOC** - Indicator of Compromise  
**ISAC** - Information Sharing and Analysis Center  
**ISAO** - Information Sharing and Analysis Organization  
**KEV** - Known Exploited Vulnerabilities (CISA catalog)  
**MISP** - Malware Information Sharing Platform  
**MSSP** - Managed Security Service Provider  
**NCSC-CH** - National Cyber Security Centre (Switzerland)  
**NIS2** - Network and Information Security Directive 2 (EU)  
**NVD** - National Vulnerability Database  
**OSINT** - Open Source Intelligence  
**PoC** - Proof of Concept  
**SIEM** - Security Information and Event Management  
**SOAR** - Security Orchestration, Automation, and Response  
**SOC** - Security Operations Center  
**STIX** - Structured Threat Information Expression  
**TAXII** - Trusted Automated Exchange of Indicator Information  
**TI** - Threat Intelligence  
**TIP** - Threat Intelligence Platform  
**TLP** - Traffic Light Protocol  
**TTP** - Tactics, Techniques, and Procedures  
**VTL** - VulnerabilityThreatLink (schema linking TI to specific CVEs with **CVSS scores**)

### E.2 Key Definitions

**Admiralty Code**  
A standardized method for evaluating intelligence source reliability using ratings A (Completely Reliable) through F (Cannot Be Judged). Used for quarterly source performance validation per ISMS-POL-A.5.7 Section 4.4.3.

**Attribution**  
The process of identifying the threat actor or group responsible for a cyber attack. Attribution ranges from general categorization to specific identification and requires high confidence.

**Common Vulnerabilities and Exposures (CVE)**  
A standardized identifier for publicly disclosed vulnerabilities. CVE IDs follow the format CVE-YYYY-NNNNN (year plus unique number). **All CVEs in NVD include CVSS scores.**

**Common Vulnerability Scoring System (CVSS)** - **MASSIVELY EXPANDED in v2.0**

**Definition**:  
A standardized, vendor-neutral framework for assessing the severity and exploitability of security vulnerabilities. CVSS provides a consistent methodology to communicate vulnerability characteristics and prioritize remediation efforts. Developed and maintained by the Forum of Incident Response and Security Teams (FIRST).

**CVSS Versions**:

**CVSS 4.0** (Current Standard - Released November 2023):
- **Status**: Preferred standard for [Organization]'s threat intelligence program
- **Advantages**:
  - Enhanced base metrics providing more accurate severity assessment
  - Improved temporal metrics reflecting exploit maturity and remediation status
  - Better alignment with real-world exploitation patterns and organizational context
  - Supplemental metrics for specialized environments (e.g., safety systems, operational technology)
  - More granular severity classification
- **Adoption Timeline**: 12-month transition from policy approval (Q4 2025 → Q4 2026)
- **Target**: ≥75% of vulnerability intelligence from CVSS 4.0-capable sources by Q4 2026
- **Source Support**: NVD transitioning to CVSS 4.0, major vendors adopting progressively

**CVSS 3.1** (Legacy Standard - Released June 2019):
- **Status**: Acceptable during transition period, maintained for backward compatibility
- **Use Cases**:
  - Historical vulnerability data (CVEs disclosed before CVSS 4.0 adoption)
  - Sources that have not yet upgraded to CVSS 4.0
  - Integration with legacy tools requiring CVSS 3.1
- **Compatibility**: VulnerabilityThreatLink (VTL) schema supports both 4.0 and 3.1 with explicit version tagging
- **Sunset**: No planned deprecation; CVSS 3.1 remains valid indefinitely for legacy data

**CVSS 2.0 and Earlier**:
- **Status**: **NOT ACCEPTABLE** for new threat intelligence sources
- **Rationale**: Outdated methodology, poor correlation with real-world exploitation
- **Exception Process**: Sources providing only CVSS 2.0 require CISO approval with documented justification (e.g., unique intelligence not available elsewhere)

**CVSS Score Ranges** (Applies to both 4.0 and 3.1):

| Score Range | Severity Rating | Color Code | Threat Intelligence Action |
|-------------|----------------|------------|----------------------------|
| **9.0 - 10.0** | **Critical** | Red | **Immediate action**: Emergency patching if actively exploited, executive notification |
| **7.0 - 8.9** | **High** | Orange | **High priority**: Accelerated patching if exploited, standard emergency process |
| **4.0 - 6.9** | **Medium** | Yellow | **Standard priority**: Normal patching cycle unless mass exploitation detected |
| **0.1 - 3.9** | **Low** | Green | **Low priority**: Routine patching schedule, monitor for exploitation changes |
| **0.0** | **None** | Blue | **Informational**: No direct security impact, document only |

**CVSS Metric Groups**:

**1. Base Metrics** (Intrinsic vulnerability characteristics, constant over time):
- **Attack Vector (AV)**: Network (N), Adjacent (A), Local (L), Physical (P)
  - *Example*: Network = Remotely exploitable (higher severity)
- **Attack Complexity (AC)**: Low (L), High (H)
  - *Example*: Low = Easy to exploit (higher severity)
- **Privileges Required (PR)**: None (N), Low (L), High (H)
  - *Example*: None = No authentication needed (higher severity)
- **User Interaction (UI)**: None (N), Required (R)
  - *Example*: None = No victim action required (higher severity)
- **Scope (S)**: Unchanged (U), Changed (C)
  - *Example*: Changed = Impact extends beyond vulnerable component (higher severity)
- **Confidentiality Impact (C)**: None (N), Low (L), High (H)
- **Integrity Impact (I)**: None (N), Low (L), High (H)
- **Availability Impact (A)**: None (N), Low (L), High (H)

**2. Temporal Metrics** (Time-dependent factors, **CRITICAL for threat intelligence**):
- **Exploit Code Maturity (E)**:
  - Unproven (U): No exploit code available
  - Proof-of-Concept (P): PoC exploit exists
  - Functional (F): Working exploit available
  - High (H): Weaponized exploit widely available or in exploit kits
  - *Threat Intelligence Usage*: Track temporal metrics in VTL records; Functional/High significantly increases priority
- **Remediation Level (RL)**:
  - Official Fix (O): Vendor patch available
  - Temporary Fix (T): Workaround or unofficial patch
  - Workaround (W): Mitigations possible without patch
  - Unavailable (U): No remediation available (zero-day scenario)
  - *Threat Intelligence Usage*: Remediation Level = Unavailable → Maximum urgency
- **Report Confidence (RC)**:
  - Unknown (U): Unconfirmed or unreliable reports
  - Reasonable (R): Credible reports from known sources
  - Confirmed (C): Validated by authoritative sources (e.g., NVD, vendor)
  - *Threat Intelligence Usage*: Confirmed reports from A-rated sources (Admiralty Code) receive priority

**3. Environmental Metrics** (Organizational context, optional):
- Adjust base score based on specific deployment environment
- Factors: Modified Attack Vector, Modified Privileges Required, Modified Confidentiality/Integrity/Availability Requirements
- *Threat Intelligence Usage*: Environmental scores calculated internally based on asset criticality and deployment context; not typically provided by external sources

**CVSS Vector String**:

Compact textual representation of all metrics, enabling score reproduction and validation.

*Example CVSS 4.0 Vector*:
```
CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N
```
Interpretation: Network attack vector, low complexity, no privileges required, no user interaction, high impact to confidentiality/integrity/availability → **Critical severity**

*Example CVSS 3.1 Vector*:
```
CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H
```
Interpretation: Network accessible, low complexity, no privileges, no user interaction, scope changed, high impact → **Critical severity**

**CVSS in Threat Intelligence Context**:

**Primary Use Cases**:
1. **Vulnerability Prioritization**: **CVSS Score + Exploitation Status = True Risk**
   - CVSS provides severity baseline (theoretical risk)
   - Threat intelligence provides exploitation status (actual threat)
   - Combined: Evidence-based prioritization for remediation
   
   *Example Decision Matrix*:
   | Scenario | CVSS | Exploitation | Priority | Action |
   |----------|------|--------------|----------|---------|
   | **Scenario A** | 9.5 (Critical) | No Known Exploit | Priority 7 | Standard patching (30 days) |
   | **Scenario B** | 6.5 (Medium) | Mass Exploitation | Priority 8 | Emergency patching (72 hours) |
   | **Scenario C** | 9.5 (Critical) | Mass Exploitation | Priority 10 | **CRITICAL** Emergency patching (24 hours) |
   
   **Key Insight**: Scenario B (lower CVSS but active exploitation) gets higher priority than Scenario A (higher CVSS but theoretical). This is evidence-based security, not cargo cult.

2. **Risk Assessment (Clause 6.1 - MANDATORY)**:
   - CVSS enables quantitative risk scoring for vulnerability-related threats
   - Risk = Likelihood (informed by exploitation status) × Impact (informed by CVSS score)
   - Supports objective risk register updates with auditable evidence
   
   *Example Risk Calculation*:
```
   Threat: CVE-2024-56789 (Apache Struts RCE)
   CVSS 4.0 Base Score: 9.3 (Critical)
   Exploitation Status: Mass Exploitation (CISA KEV listed)
   Affected Assets: 12 public-facing web servers
   
   Risk Assessment:
   Likelihood: High (mass exploitation confirmed by multiple sources)
   Impact: Critical (CVSS 9.3, RCE on public-facing systems, confidentiality/integrity/availability compromise)
   Overall Risk: CRITICAL → Emergency risk treatment (emergency patching authorized)
   Risk Register Entry: REG-047 updated, approved by CRO
```

3. **VulnerabilityThreatLink (VTL) Schema**:
   - VTL records document CVSS version, base score, and vector for each exploited CVE
   - Enables automated priority escalation in vulnerability management (Control A.8.8)
   - **Critical VTL Fields**:
     - CVSS_Version: 4.0 or 3.1
     - CVSS_Base_Score: 0.0-10.0
     - CVSS_Vector: Complete string
     - Exploitation_Status: PoC / Active / Mass
     - Emergency_Patch_Required: Auto-calculated from CVSS + exploitation + critical assets
   
4. **Prevented Incidents Evidence**:
   - CVSS scores document severity of avoided vulnerability exploits
   - Quantifies risk reduction: "Prevented CVSS 9.3 Critical vulnerability exploitation through proactive patching"
   - Supports cost avoidance calculations and ROI for threat intelligence program

5. **Source Evaluation**:
   - Threat intelligence sources evaluated for CVSS support (4.0 preferred, 3.1 acceptable)
   - CVSS accuracy validated quarterly: Source-reported score vs. NVD/vendor advisory
   - Target: ≥90% CVSS accuracy (±1.0 point tolerance) for all sources
   - Poor CVSS accuracy contributes to source deprecation decisions

**CVSS Accuracy Validation Process**:

Quarterly validation ensures threat intelligence sources provide accurate CVSS scores:

1. **Sample Selection**: Randomly sample 20 CVEs from each source's quarterly output
2. **Authoritative Comparison**: Compare source CVSS scores to NVD and vendor advisories
3. **Tolerance Calculation**: Calculate deviation (source score - NVD score)
   - Within ±1.0 points: Accurate
   - Deviation >1.0 points: Inaccurate
   - Example: Source reports 8.5, NVD reports 7.8 → Deviation 0.7 → Accurate
   - Example: Source reports 9.5, NVD reports 6.2 → Deviation 3.3 → **Inaccurate**
4. **Accuracy Rate**: (Accurate CVEs / Total Sample) × 100%
   - Target: ≥90% accuracy
   - Threshold: <85% triggers source review, potential deprecation
5. **Remediation**: If accuracy <90%, contact source vendor for clarification or correction

**Common CVSS Mistakes to Avoid**:

❌ **Mistake 1: Using CVSS Alone for Prioritization**
- *Problem*: Ignores real-world exploitation status
- *Impact*: Resources wasted on theoretical high-CVSS vulnerabilities while exploited medium-CVSS vulnerabilities are ignored
- ✅ *Solution*: Always combine CVSS with threat intelligence on exploitation status

❌ **Mistake 2: Treating All Critical (9.0+) Vulnerabilities Equally**
- *Problem*: Not all CVSS 9.0+ vulnerabilities are equally urgent
- *Impact*: Alert fatigue, inability to prioritize within "Critical" category
- ✅ *Solution*: Sub-prioritize Critical vulnerabilities based on exploitation status, affected assets, attack vector

❌ **Mistake 3: Ignoring Temporal Metrics**
- *Problem*: Base score alone doesn't reflect exploit availability or patch status
- *Impact*: Miss opportunities to deprioritize patched or unexploitable vulnerabilities
- ✅ *Solution*: Track temporal metrics (Exploit Code Maturity, Remediation Level) in VTL records

❌ **Mistake 4: Assuming CVSS Accuracy Without Validation**
- *Problem*: Sources may provide incorrect or outdated CVSS scores
- *Impact*: Misprioritization, wasted remediation effort
- ✅ *Solution*: Quarterly CVSS accuracy validation against NVD/vendor advisories

❌ **Mistake 5: Mixing CVSS Versions Without Tagging**
- *Problem*: CVSS 4.0 and 3.1 scores calculated differently; direct comparison misleading
- *Impact*: Incorrect prioritization decisions
- ✅ *Solution*: Always tag CVSS version explicitly in VTL records and reports

**CVSS Resources**:
- **Official Specification**: https://www.first.org/cvss/
- **CVSS 4.0 Calculator**: https://www.first.org/cvss/calculator/4.0
- **CVSS 3.1 Calculator**: https://www.first.org/cvss/calculator/3.1
- **NVD CVSS Scores**: https://nvd.nist.gov/
- **FIRST Training**: CVSS Special Interest Group (SIG) materials

**Migration Strategy (Q4 2025 → Q4 2026)**:
- **Q1 2026**: Analyst training on CVSS 4.0 methodology, tool upgrades to support 4.0
- **Q2 2026**: Prioritize CVSS 4.0-capable sources in new subscriptions, deprecate CVSS 2.0 sources
- **Q3 2026**: Target ≥50% of VTL records using CVSS 4.0
- **Q4 2026**: Target ≥75% of VTL records using CVSS 4.0, full framework adoption complete
- **Ongoing**: CVSS 3.1 remains supported indefinitely for legacy data

**Confidence Level**  
An assessment of the reliability and accuracy of threat intelligence (high, medium, low), helping consumers understand certainty and inform decision-making. Based on source Admiralty Code ratings and corroboration. **CVSS scores from NVD are High confidence by default.**

**Cyber Kill Chain**  
A model describing the stages of a cyber attack from reconnaissance to actions on objectives, used to identify defensive opportunities at each stage.

**Diamond Model**  
A framework for analyzing cyber intrusions based on four core features: adversary, capability, infrastructure, and victim. Supports structured threat analysis.

**Finished Intelligence**  
Threat intelligence that has been fully analyzed, validated, and formatted for dissemination, including context, confidence assessments, and recommended actions.

**Indicator of Compromise (IOC)**  
Observable artifacts or evidence indicating a potential or confirmed security incident (file hashes, IP addresses, domains, URLs, email addresses, **CVE identifiers with CVSS scores**, etc.).

**Intelligence Cycle**  
The iterative process of threat intelligence production: Planning, Collection, Processing, Analysis (including **CVSS scoring**), Dissemination, Feedback.

**Known Exploited Vulnerabilities (KEV)**  
CISA's authoritative catalog of vulnerabilities actively exploited in the wild. **KEV entries include CVSS scores** and are mandatory remediation targets for U.S. federal agencies; highly recommended for all organizations as authoritative exploitation intelligence.

**MITRE ATT&CK**  
A globally accessible knowledge base of adversary tactics and techniques based on real-world observations, used to structure threat intelligence and map defenses.

**National Vulnerability Database (NVD)**  
The U.S. government repository of CVE data with **authoritative CVSS scores**. NVD is transitioning from CVSS 3.1 to CVSS 4.0 progressively. Primary reference for CVSS validation.

**Operational Intelligence**  
Actionable intelligence about specific, imminent threats including IOCs, active campaigns, and adversary infrastructure, enabling immediate defensive actions. **Includes actively exploited CVEs with CVSS 4.0/3.1 scores.**

**Prevented Incident (Validated)** - **UPDATED in v2.0**  
Security incident that was avoided due to threat intelligence, with objective evidence: before-state (vulnerability existed), TI alert (warned of exploitation with **CVSS score**), action (remediation deployed), after-state (vulnerability eliminated), validation (technical evidence such as SIEM logs, scan results). Target: ≥3 validated prevented incidents per quarter. Evidence tracked in ISMS-IMP-A.5.7.3 Sheet 7.

**Raw Intelligence**  
Unprocessed threat information that has not been analyzed or validated, may contain noise and requires further processing.

**Strategic Intelligence**  
High-level intelligence about the threat landscape, threat actor capabilities, geopolitical factors, and long-term trends, informing executive decision-making. MUST include Clause 6.1 risk assessment updates with **CVSS-based vulnerability risk quantification where applicable**.

**Tactical Intelligence**  
Intelligence focused on adversary TTPs, tools, and infrastructure, enabling understanding of *how* attacks are conducted and development of appropriate defenses. **Includes vulnerability exploitation techniques with CVSS severity context.**

**Threat Actor**  
An individual, group, or organization conducting or intending to conduct malicious cyber activities, categorized by motivation and sophistication.

**Threat Feed**  
An automated delivery mechanism for threat intelligence, typically providing regularly updated IOCs, malware signatures, or threat actor infrastructure data.

**Threat Intelligence**  
Information that has been collected, analyzed, and contextualized to understand capabilities, intentions, and activities of threat actors, enabling informed decisions.

**Threat Intelligence Platform (TIP)**  
A technology solution that aggregates, correlates, and manages threat intelligence from multiple sources, providing capabilities for indicator management, enrichment, analysis, and integration. **Modern TIPs support CVSS 4.0/3.1 and VTL schema integration.**

**Traffic Light Protocol (TLP)**  
A set of designations to ensure proper handling and sharing of sensitive information:
- **TLP:CLEAR** (formerly TLP:WHITE): No restrictions on sharing
- **TLP:GREEN**: Community-wide sharing
- **TLP:AMBER**: Limited sharing within organization
- **TLP:AMBER+STRICT**: Limited sharing, no propagation
- **TLP:RED**: Personal use only, no sharing

**VulnerabilityThreatLink (VTL)** - **UPDATED in v2.0**  
A data schema linking threat intelligence to specific vulnerabilities (CVEs) when active exploitation is detected. Enables automated priority escalation in vulnerability management (Control A.8.8 when implemented). **VTL records include CVSS 4.0 or 3.1 version, base score, vector string, exploitation status, threat actor attribution, and criticality assessment.** Schema documented in: shared_schemas/vulnerability_threat_link.py. VTL records tracked in ISMS-IMP-A.5.7.2 Sheet 8.

**VTL Record Structure (Key Fields)**:
- Link_ID, Vulnerability_ID (CVE)
- **CVSS_Version** (4.0 or 3.1), **CVSS_Base_Score** (0.0-10.0), **CVSS_Vector** (complete string)
- Exploitation_Status (PoC / Active / Mass)
- Threat_Actor_Type, Detection_Date, TI_Source
- Criticality (1-10 priority score: CVSS + exploitation weight)
- Critical_Assets_Affected, Emergency_Patch_Required
- Remediation_Status (Open / In Progress / Patched / Mitigated)

**Zero-Day**  
Exploitation of a previously unknown vulnerability (zero-day vulnerability) for which no patch or mitigation exists, representing high-impact risk. **Zero-day exploits initially lack CVSS scores; scores assigned post-disclosure to NVD.**

---

## Annex F: Document Relationships and Cross-References

### F.1 Policy Framework Structure

This annex (S5) is part of the complete Threat Intelligence policy framework:
```
ISMS-POL-A.5.7 - Threat Intelligence Policy Framework (Master)
│
├── ISMS-POL-A.5.7-S1 - Purpose, Scope, Definitions (includes CVSS 4.0/3.1 definitions)
├── ISMS-POL-A.5.7-S2 - Threat Intelligence Requirements (includes CVSS scoring requirements)
├── ISMS-POL-A.5.7-S3 - Roles and Responsibilities
├── ISMS-POL-A.5.7-S4 - Policy Governance
└── ISMS-POL-A.5.7-S5 - Annexes (this document - expanded CVSS glossary)
```

### F.2 Related Implementation Documents

The policy framework is supported by implementation specifications:
```
Implementation Layer (ISMS-IMP-A.5.7.x)
│
├── ISMS-IMP-A.5.7.1 - Threat Intelligence Sources Assessment (15 sheets)
│   ├── Sheet 1: Source Inventory (includes CVSS_Support column)
│   ├── Sheet 14: Source Performance Validation (Admiralty Code, accuracy ≥85%, CVSS accuracy ≥90%)
│   └── Sheet 15: Business Continuity Plan
│
├── ISMS-IMP-A.5.7.2 - Intelligence Collection & Analysis Assessment (13 sheets)
│   └── Sheet 8: VulnerabilityThreatLink (VTL) Records (WITH CVSS 4.0/3.1 FIELDS)
│       ├── CVSS_Version column (4.0 or 3.1)
│       ├── CVSS_Base_Score column (0.0-10.0 with validation)
│       ├── CVSS_Vector column (complete vector string)
│       └── Criticality auto-calculated from CVSS + exploitation
│
├── ISMS-IMP-A.5.7.3 - Intelligence Integration & Distribution Assessment (15 sheets)
│   ├── Sheet 7: Prevention Tracking (prevented incidents with CVSS severity documentation)
│   ├── Sheet 13: Risk Assessment Updates (Clause 6.1, CVSS-based risk quantification, ≥3/quarter)
│   ├── Sheet 14: Incident-TI Integration (CVSS context for vulnerability-related incidents, ≥70% P1/P2)
│   └── Sheet 15: Intelligence-Driven Decisions (CVSS-based prioritization decisions, ≥5/quarter)
│
└── ISMS-IMP-A.5.7.4 - Effectiveness Dashboard (consolidated KPIs)
    └── CVSS adoption metrics (% VTL records with CVSS 4.0 vs 3.1, transition progress)
```

### F.3 Related Policies and Controls

**MANDATORY Integrations** (standalone A.5.7 implementation):

- **ISO 27001:2022 Clause 6.1** - Actions to Address Risks and Opportunities
  - Threat intelligence MUST inform risk assessments
  - **CVSS-based vulnerability risk quantification** required for vulnerability-related threats
  - Target: ≥3 risk assessment updates per quarter
  - Evidence: ISMS-IMP-A.5.7.3 Sheet 13
  - CRO approval required for TI-driven risk updates

- **ISMS-POL-A.5.24-5.28** - Incident Management
  - Threat intelligence MUST support incident investigation
  - **CVSS context** for vulnerability-related incidents
  - Target: ≥70% of P1/P2 incidents use threat intelligence
  - Evidence: ISMS-IMP-A.5.7.3 Sheet 14

- **ISMS-POL-A.8.16** - Monitoring Activities
  - Threat intelligence provides detection signatures
  - IOCs deployed to SIEM, EDR, IDS/IPS
  - Monitoring telemetry feeds threat intelligence

**OPTIONAL Integrations** (when other controls implemented):

- **ISMS-POL-A.8.8** - Management of Technical Vulnerabilities (**OPTIONAL**)
  - **Note**: This integration is OPTIONAL and only applies when organization implements Control A.8.8
  - Threat intelligence prioritizes vulnerability remediation
  - **VulnerabilityThreatLink (VTL) schema with CVSS 4.0/3.1 scoring** enables automated integration
  - **CVSS Score + Exploitation Status = Intelligent Prioritization**
  - Active exploitation triggers emergency patching
  - Without A.8.8: Basic threat intelligence consumption (CISA KEV, vendor advisories with CVSS)
  - With A.8.8: Full VTL integration with **CVSS-based automated priority escalation**

- **ISMS-POL-A.5.19-5.22** - Supplier Management
  - Threat intelligence includes supply chain threats
  - Supplier vulnerabilities tracked with **CVSS severity** through intelligence

- **ISMS-POL-A.5.23** - Cloud Security
  - Cloud-specific threat intelligence collected
  - Cloud provider intelligence integrated (CSP-provided **CVSS scores** authoritative)

### F.4 Audit Evidence Cross-Reference - **UPDATED in v2.0**

Per ISMS-POL-A.5.7 Section 4.4, threat intelligence generates the following audit evidence:

| Evidence Category | Policy Section | Implementation Sheet | Target | CVSS Integration |
|-------------------|----------------|---------------------|--------|------------------|
| Clause 6.1 Integration | 4.4.1 | ISMS-IMP-A.5.7.3 Sheet 13 | ≥3 risk updates/quarter | **CVSS-based vulnerability risk quantification** |
| Prevented Incidents | 4.4.2 | ISMS-IMP-A.5.7.3 Sheet 7 | ≥3 validated/quarter | **CVSS severity documentation** |
| Source Accuracy | 4.4.3 | ISMS-IMP-A.5.7.1 Sheet 14 | ≥85% accuracy | **CVSS accuracy ≥90%** |
| Incident-TI Integration | 4.4.4 | ISMS-IMP-A.5.7.3 Sheet 14 | ≥70% P1/P2 incidents | **CVSS context for vuln incidents** |
| Intelligence-Driven Decisions | 4.4.5 | ISMS-IMP-A.5.7.3 Sheet 15 | ≥5 decisions/quarter | **CVSS-based prioritization** |
| Business Continuity | 4.4.6 | ISMS-IMP-A.5.7.1 Sheet 15 | 100% roles with backup | N/A |

**CVSS-Specific Audit Evidence**:
- **VTL Records** (ISMS-IMP-A.5.7.2 Sheet 8): Complete with CVSS 4.0/3.1 version, score, vector
- **CVSS Accuracy Validation**: Quarterly comparison reports (source vs. NVD/vendor)
- **CVSS Migration Progress**: Dashboard tracking % CVSS 4.0 adoption (target ≥75% by Q4 2026)
- **Source Evaluation**: CVSS support documented in source inventory (Sheet 1)

**Audit Preparation Timeline**: See ISMS-POL-A.5.7-S4 Section 4.5 for T-30 to T-0 preparation checklist, including **CVSS data quality validation**.

---

**END OF DOCUMENT**