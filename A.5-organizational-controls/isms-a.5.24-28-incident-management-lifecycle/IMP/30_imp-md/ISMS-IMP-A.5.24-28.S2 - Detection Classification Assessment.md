**ISMS-IMP-A.5.24-28.S2 — Incident Detection & Classification Assessment**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.24: Information Security Incident Management

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Incident Detection & Classification Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.24-28.S2 |
| **Assessment Domain** | Domain 2 - Detection & Classification (A.5.25 Focus) |
| **Related Policy** | ISMS-POL-A.5.24-28 (Incident Management Lifecycle) |
| **Related Reference** | ISMS-REF-A.5.24-28 (Incident Response Reference Guide) |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Technical Authority** | SOC Manager / Detection Engineering Lead |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | SOC Manager | Initial detection & classification assessment specification |

**Review Cycle**: Annual (or after major detection capability changes)  
**Next Review Date**: [Effective Date + 12 months]  

**Related Documents**: 

- ISMS-POL-A.5.24-28 (Incident Management Lifecycle Policy)
- ISMS-REF-A.5.24-28 (Incident Response Reference Guide, Section 1: Incident Classification Taxonomy)
- ISMS-IMP-A.5.24-28.S1 (Framework & Governance Assessment)
- ISMS-IMP-A.5.24-28.S3 (Response Capabilities Assessment)
- ISMS-IMP-A.5.24-28.S4 (Forensic Evidence Assessment)
- ISMS-IMP-A.5.24-28.S5 (Learning & Improvement Assessment)
- ISMS-IMP-A.8.16 (Security Monitoring Assessment)
- ISO/IEC 27002:2022 Control A.5.25
- NIST SP 800-61 Rev. 2 Section 3.2 (Detection and Analysis)

---

# PART I: USER COMPLETION GUIDE

# Assessment Overview

## Purpose

This assessment evaluates [Organization]'s **incident detection and classification capabilities**, focusing on the **assessment and decision** phase of incident management (A.5.25).

**What This Assessment Covers:**

- Detection mechanisms (SIEM rules, EDR alerts, IDS/IPS, user reporting)
- Alert triage and investigation procedures
- Incident classification and categorization
- Severity assignment criteria and processes
- False positive handling and tuning
- Detection coverage gaps
- Mean Time to Detect (MTTD) and Mean Time to Triage (MTTT) metrics

**What This Assessment Does NOT Cover:**

- Incident management governance (see S1 - Framework Assessment)
- Response execution and containment (see S3 - Response Assessment)
- Forensic evidence collection (see S4 - Forensic Assessment)
- Post-incident learning (see S5 - Learning Assessment)

**Assessment Output:**

- Excel workbook documenting detection and classification maturity
- Detection coverage assessment across threat categories
- Alert quality and false positive analysis
- Classification consistency evaluation
- Detection effectiveness metrics
- Gap analysis and tuning recommendations

## Why This Matters

**ISO/IEC 27001:2022 Control A.5.25 Requirement:**
> *"Information security events should be assessed and it should be decided if they are to be classified as information security incidents."*

**NIST SP 800-61 Guidance:**
> *"Detection and Analysis: The primary goal of this phase is to detect information security incidents and determine their scope. Analysis should be performed to determine the nature of the incident, its impact, and the appropriate response."*

**Business Impact of Poor Detection/Classification:**

- **Missed Incidents:** Undetected breaches lead to extended dwell time (average 200+ days)
- **Alert Fatigue:** High false positive rates cause analysts to miss real threats
- **Inconsistent Response:** Poor classification leads to inappropriate response (over/under-reaction)
- **Delayed Response:** Slow triage delays containment, increasing damage
- **Regulatory Non-Compliance:** Failure to detect data breaches within notification windows
- **Resource Waste:** Investigating false positives wastes expensive analyst time

**This Assessment Addresses:**

- Do we detect security incidents across all threat categories?
- Are our detection mechanisms effective (low false positives, high true positives)?
- Can we classify incidents consistently and accurately?
- Do we triage alerts quickly enough to enable timely response?
- Are severity assignments appropriate and actionable?

## Who Should Complete This Assessment

**Primary Responsibility:** SOC Manager, Detection Engineering Lead, or Security Analyst Lead

**Required Knowledge:**

- [Organization]'s detection technologies (SIEM, EDR, IDS/IPS, NDR)
- Alert triage procedures and investigation workflows
- Incident classification criteria and severity definitions
- Detection rule development and tuning processes
- Integration with monitoring infrastructure (A.8.16)

**Support Roles:**

- **Detection Engineers:** Rule development, tuning, threat hunting
- **SOC Analysts:** Alert handling, triage, investigation
- **Threat Intelligence:** Threat landscape, IOC management
- **IT Operations:** Log sources, network visibility, endpoint coverage
- **CSIRT Manager:** Incident escalation criteria, severity thresholds

**Collaboration Required:**

- This is NOT a solo assessment
- Requires input from SOC analysts (frontline perspective)
- Requires metrics data (SIEM, ticketing system)
- Review sessions with detection team and CSIRT

## Time Estimate

**Total Assessment Time:** 6-10 hours (depending on SOC maturity)

**Breakdown:**

- **Information Gathering:** 2-3 hours
  - Review detection rules and alert configurations
  - Extract detection metrics (MTTD, MTTT, false positive rate)
  - Collect classification procedures and severity matrices
  - Review recent incident tickets for classification consistency
  
- **Assessment Completion:** 2-3 hours
  - Complete detection mechanism assessment
  - Document alert handling procedures
  - Assess classification and severity processes
  - Evaluate detection coverage by threat category
  
- **Metrics Analysis:** 1-2 hours
  - Calculate detection effectiveness metrics
  - Analyze false positive trends
  - Review MTTD/MTTT performance
  
- **Gap Analysis:** 1-2 hours
  - Identify detection blind spots
  - Prioritize tuning requirements
  - Develop improvement recommendations

**Complexity Factors:**

- **Simple (6 hours):** Mature SOC, comprehensive SIEM, documented procedures
- **Moderate (8 hours):** Growing SOC, some detection gaps, basic metrics
- **Complex (10+ hours):** Immature SOC, limited detection, inconsistent classification

## Connection to Policy

This assessment implements **ISMS-POL-A.5.24-28, Section 2.2 (Incident Assessment & Decision)** which defines mandatory requirements for:

**Detection Requirements:**

- Multi-layered detection (network, endpoint, application, user reporting)
- 24/7 alert monitoring for Critical/High severity systems
- Detection rule coverage for all 11 primary threat categories
- Automated alerting with defined thresholds
- Integration with threat intelligence feeds

**Classification Requirements:**

- Consistent use of 11 primary incident categories (per ISMS-REF-A.5.24-28 Section 1)
- Severity assignment criteria (Critical, High, Medium, Low)
- Documented classification procedures
- Classification accuracy tracking
- Reclassification process for evolving incidents

**Triage Requirements:**

- Defined triage procedures for each severity level
- Maximum triage time thresholds (15 min Critical, 1 hour High, 4 hours Medium, 24 hours Low)
- Escalation triggers documented
- False positive handling procedures
- Analyst training on triage methodology

**Metrics Requirements:**

- Mean Time to Detect (MTTD) tracked monthly
- Mean Time to Triage (MTTT) tracked per severity
- False positive rate monitored and trended
- Detection coverage assessed quarterly
- Alert volume and handling capacity tracked

**Policy Authority:** Chief Information Security Officer (CISO)  
**Compliance Status:** Mandatory for all [Organization] security incidents

## Assessment Scope

**Included in This Assessment:**

✅ **Detection Mechanisms:**

- SIEM rule coverage and effectiveness
- EDR/XDR alert configuration
- IDS/IPS signature coverage
- Network Detection and Response (NDR)
- User reporting mechanisms (A.6.8 integration)
- Threat intelligence integration

✅ **Alert Handling:**

- Triage procedures and workflows
- Investigation playbooks
- Escalation criteria
- Queue management
- Analyst training

✅ **Classification & Severity:**

- Category assignment consistency
- Severity criteria application
- Reclassification procedures
- Correlation of related events

✅ **Detection Effectiveness:**

- False positive/negative rates
- MTTD and MTTT metrics
- Detection coverage by threat type
- Alert quality assessment

**Excluded from This Assessment:**

❌ Incident response execution (see S3)
❌ Forensic evidence collection (see S4)
❌ Post-incident review (see S5)
❌ CSIRT organizational structure (see S1)
❌ Detailed SIEM configuration (see A.8.16 Monitoring Assessment)

## Prerequisites

**Before Starting This Assessment:**

1. ✅ **Read Related Documents:**

   - ISMS-POL-A.5.24-28 Section 2.2 (Assessment & Decision Requirements)
   - ISMS-REF-A.5.24-28 Section 1 (Incident Classification Taxonomy)
   - ISMS-IMP-A.8.16 (Security Monitoring Assessment - if available)

2. ✅ **Gather Documentation:**

   - SIEM rule catalog and alert configurations
   - Alert triage procedures/runbooks
   - Incident classification matrix
   - Severity assignment criteria
   - SOC playbooks for common incident types
   - Detection coverage matrix (threat categories mapped to detection tools)

3. ✅ **Extract Metrics (Last 90 Days):**

   - Total alerts generated (by source, by severity)
   - Alerts triaged and investigated
   - False positive count and rate
   - True positive count (actual incidents)
   - MTTD (time from event to alert)
   - MTTT (time from alert to triage/classification)
   - Incidents by category and severity

4. ✅ **Identify Stakeholders:**

   - SOC Manager (primary assessor)
   - Detection Engineers (rule development, tuning)
   - SOC Analysts (frontline triage experience)
   - Threat Intelligence Analyst (IOC integration)
   - CSIRT Manager (escalation, severity validation)

5. ✅ **Prepare Evidence Folder:**

   - Create folder: `/Evidence/A.5.24-28/S2_Detection/`
   - Collect: SIEM rule exports, alert reports, classification examples, metrics dashboards

---

# Assessment Workflow

## High-Level Process

**Step-by-Step Assessment Flow:**

```
1. Detection Mechanism Inventory (1-2 hours)
   ├── List all detection technologies (SIEM, EDR, IDS/IPS, NDR, etc.)
   ├── Document alert sources and rule counts
   ├── Map detection coverage to threat categories
   └── Identify detection blind spots

2. Alert Handling Assessment (1-2 hours)
   ├── Review triage procedures
   ├── Assess queue management processes
   ├── Evaluate playbook completeness
   └── Review analyst training adequacy

3. Classification & Severity Assessment (1-2 hours)
   ├── Review classification consistency (sample 20-30 incidents)
   ├── Validate severity assignment criteria
   ├── Assess reclassification procedures
   └── Evaluate category/severity correlation

4. Metrics Analysis (1-2 hours)
   ├── Calculate MTTD and MTTT
   ├── Analyze false positive rate and trends
   ├── Review alert volume vs. capacity
   └── Assess detection effectiveness by category

5. Gap Analysis (1 hour)
   ├── Identify detection coverage gaps
   ├── Prioritize tuning requirements
   └── Develop improvement recommendations

6. Quality Review (1 hour)
   ├── Validate metrics calculations
   ├── Peer review with SOC team
   └── Management review
```

## Assessment Sections Overview

**The workbook contains the following sections:**

**Sheet 1: Instructions & Legend**

- Assessment overview and methodology
- Detection effectiveness metrics definitions
- Color coding and validation rules

**Sheet 2: Detection Mechanisms**

- SIEM rule inventory and coverage
- EDR/XDR alert configurations
- IDS/IPS signature coverage
- Network detection capabilities
- User reporting integration
- Threat intelligence integration

**Sheet 3: Alert Handling**

- Triage procedures completeness
- Investigation playbooks by incident category
- Queue management processes
- Escalation triggers and workflows
- Analyst training assessment

**Sheet 4: Classification & Severity**

- Category assignment consistency
- Severity criteria validation
- Reclassification procedures
- Category/severity correlation matrix
- Classification training adequacy

**Sheet 5: Detection Effectiveness**

- MTTD metrics (overall and by severity)
- MTTT metrics (overall and by severity)
- False positive/negative analysis
- Alert volume and handling capacity
- Detection coverage by threat category

**Sheet 6: Gap Analysis**

- Detection blind spots identification
- Alert tuning requirements
- Procedure gaps and improvements
- Prioritization and remediation

**Sheet 7: Evidence Register**

- SIEM rule exports
- Alert handling metrics reports
- Classification examples
- Playbook documentation

**Sheet 8: Dashboard**

- Detection effectiveness summary
- Alert handling performance
- Classification accuracy
- Top detection gaps

**Sheet 9: Approval Sign-Off**

- SOC Manager approval
- CISO review and approval

---

# Section-by-Section Guidance

## Sheet 2: Detection Mechanisms

**Purpose:** Document all detection technologies and assess coverage

**Assessment Questions (30 questions):**

---

### **Section A: SIEM Detection (Q1-Q8)**

**Q1: SIEM_Platform**

- **Question:** What SIEM platform(s) does [Organization] use?
- **Format:** Free text (e.g., "Splunk Enterprise", "Microsoft Sentinel", "QRadar")
- **Evidence:** SIEM platform documentation, license information

**Q2: SIEM_Rule_Count**

- **Question:** How many active detection rules/alerts are configured in the SIEM?
- **Format:** Number
- **Best Practice:** 
  - Small org: 50-200 rules
  - Mid-size: 200-500 rules
  - Large/complex: 500-2000+ rules
- **Evidence:** SIEM rule catalog export

**Q3: SIEM_Rule_Categories**

- **Question:** Which threat categories have SIEM detection rules? (Select all: Malware/Unauthorized Access/Data Breach/DoS/Social Engineering/Web Attack/Network Attack/Endpoint/Physical/Config-Patch/Other)
- **Format:** Checkbox (multiple selections)
- **Target:** Coverage across all 11 primary categories (ISMS-REF-A.5.24-28 Section 1)

**Q4: SIEM_Tuning_Frequency**

- **Question:** How often are SIEM rules tuned to reduce false positives?
- **Dropdown:** Weekly / Monthly / Quarterly / Annually / Ad-Hoc Only / Never
- **Best Practice:** Monthly minimum, weekly for high-noise rules
- **Gap if "Annually" or "Never":** HIGH - Stale rules increase false positive rate

**Q5: SIEM_Custom_Rules**

- **Question:** What percentage of SIEM rules are custom-developed (vs. vendor-provided)?
- **Format:** Percentage (0-100%)
- **Interpretation:**
  - <20%: Heavy reliance on vendor content (may miss organization-specific threats)
  - 20-50%: Balanced approach
  - >50%: Strong custom detection capability
- **Note:** No right answer, depends on threat landscape and resources

**Q6: SIEM_Threat_Intel_Integration**

- **Question:** Is threat intelligence integrated into SIEM for automated alerting?
- **Dropdown:** Yes - Fully Automated / Yes - Manual Lookups / No
- **Integration Examples:**
  - IOC feeds (malicious IPs, domains, file hashes) auto-enriched
  - SIEM alerts when log event matches IOC
- **Evidence:** Threat intel feed configuration, example enriched alerts

**Q7: SIEM_Alert_Volume**

- **Question:** What is the average daily SIEM alert volume?
- **Format:** Number (alerts per day)
- **Benchmarking:**
  - <100/day: Likely under-detection or very mature tuning
  - 100-1000/day: Typical for mid-size org
  - >1000/day: High volume, assess if manageable or needs tuning
- **Cross-Check:** Compare to analyst capacity (Q20)

**Q8: SIEM_Log_Sources**

- **Question:** How many log sources feed the SIEM?
- **Format:** Number
- **Cross-Reference:** Should align with ISMS-IMP-A.8.16 (Monitoring Assessment)
- **Evidence:** SIEM log source inventory

---

### **Section B: Endpoint Detection (Q9-Q13)**

**Q9: EDR_XDR_Deployed**

- **Question:** Is Endpoint Detection and Response (EDR) or Extended Detection and Response (XDR) deployed?
- **Dropdown:** Yes - EDR / Yes - XDR / No
- **Definitions:**
  - EDR: Endpoint-focused (endpoints only)
  - XDR: Extended (endpoints + network + cloud + email)
- **Evidence:** EDR/XDR platform documentation, deployment scope

**Q10: EDR_Coverage**

- **Question:** What percentage of endpoints have EDR/XDR agent deployed?
- **Format:** Percentage (0-100%)
- **Target:** >95% for Critical/High systems, >90% overall
- **Gap if <90%:** HIGH - Incomplete endpoint visibility

**Q11: EDR_Alert_Types**

- **Question:** What types of EDR alerts are enabled? (Select all: Malware Detection/Suspicious Behavior/Lateral Movement/Privilege Escalation/Data Exfiltration/Persistence/Other)
- **Format:** Checkbox (multiple selections)
- **Best Practice:** Enable all applicable alert types, tune to reduce noise

**Q12: EDR_Automated_Response**

- **Question:** Does EDR support automated response actions (e.g., isolate endpoint, kill process)?
- **Dropdown:** Yes - Fully Automated / Yes - Semi-Automated (Analyst Approval) / Manual Only
- **Trade-off:** Automation speeds response but risks false positive impact

**Q13: EDR_Forensic_Data_Retention**

- **Question:** How long does EDR retain forensic data (process execution, network connections, file activity)?
- **Dropdown:** 30 days / 60 days / 90 days / 180 days / 1 year+ / Not Defined
- **Best Practice:** 90 days minimum (supports investigation of delayed detection)
- **Evidence:** EDR retention policy configuration

---

### **Section C: Network Detection (Q14-Q17)**

**Q14: IDS_IPS_Deployed**

- **Question:** Is Intrusion Detection/Prevention System (IDS/IPS) deployed?
- **Dropdown:** Yes - IPS (Blocking) / Yes - IDS (Alerting Only) / No
- **Note:** IPS blocks threats, IDS only alerts (analyst investigates)

**Q15: IDS_IPS_Coverage**

- **Question:** Where is IDS/IPS deployed? (Select all: Network Perimeter/Internal Network Segments/Data Center/Cloud Environments/Not Applicable)
- **Format:** Checkbox
- **Best Practice:** Perimeter + critical internal segments

**Q16: IDS_IPS_Signature_Updates**

- **Question:** How frequently are IDS/IPS signatures updated?
- **Dropdown:** Daily / Weekly / Monthly / Manual Only / Not Updated
- **Best Practice:** Daily automated updates
- **Gap if "Monthly" or less:** MEDIUM - Delayed protection against new threats

**Q17: Network_Detection_Response_NDR**

- **Question:** Is Network Detection and Response (NDR) or Network Traffic Analysis (NTA) deployed?
- **Dropdown:** Yes / No
- **NDR/NTA:** ML-based network threat detection (east-west traffic, anomaly detection)
- **Evidence:** NDR platform documentation, deployment scope

---

### **Section D: Other Detection Mechanisms (Q18-Q22)**

**Q18: User_Reporting_Mechanism**

- **Question:** Is there a user reporting mechanism for security events (A.6.8 integration)?
- **Dropdown:** Yes - Dedicated / Yes - General IT Helpdesk / No
- **Cross-Reference:** ISMS-IMP-A.5.24-28.S1 (Framework Assessment) Q106-Q108
- **Evidence:** User reporting process documentation

**Q19: User_Reports_Volume**

- **Question:** What is the average monthly volume of user-reported security events?
- **Format:** Number (reports per month)
- **Interpretation:**
  - Very low (<5/month for large org): Users may not know how to report
  - Moderate (10-50/month): Healthy user awareness
  - Very high (>100/month): May need better user training (reduce noise)

**Q20: DLP_Alerts**

- **Question:** Does Data Loss Prevention (DLP) generate security alerts?
- **Dropdown:** Yes - Integrated with Incident Management / Yes - Separate Process / No DLP
- **Integration:** DLP alerts should feed incident management for data exfiltration incidents

**Q21: CASB_Alerts**

- **Question:** Does Cloud Access Security Broker (CASB) generate security alerts?
- **Dropdown:** Yes - Integrated / Yes - Separate Process / No CASB / N/A (No Cloud)
- **Use Case:** Detect cloud app misuse, shadow IT, data exfiltration via cloud

**Q22: Honeypots_Deception**

- **Question:** Are honeypots or deception technology deployed for threat detection?
- **Dropdown:** Yes / No
- **Purpose:** High-fidelity detection (any activity = malicious)
- **Evidence:** Honeypot deployment documentation

---

### **Section E: Detection Coverage Assessment (Q23-Q30)**

**Q23-Q33:** **Threat Category Coverage (11 categories from ISMS-REF-A.5.24-28 Section 1)**

For each of the 11 primary threat categories, assess:

- **Detection Exists:** Yes / Partial / No
- **Primary Detection Method:** SIEM / EDR / IDS/IPS / NDR / User Reporting / Multiple / None
- **Coverage Quality:** Good / Fair / Poor

**Q23: Category_1_Malware_Detection**

- **Category:** Malware (Ransomware, Trojan, Worm, Spyware, Cryptojacking, Adware)
- **Detection Exists:** Yes / Partial / No
- **Primary Detection Method:** Dropdown
- **Coverage Quality:** Dropdown (Good = multiple layers, Fair = single layer, Poor = gaps)

**Q24: Category_2_Unauthorized_Access_Detection**

- **Category:** Unauthorized Access (Compromised Credentials, Brute Force, Privilege Escalation, Insider Threat, Supply Chain)

**Q25: Category_3_Data_Breach_Detection**

- **Category:** Data Breach/Exfiltration (Unauthorized Access, Exfiltration, Accidental Loss, Privacy Breach)

**Q26: Category_4_DoS_Detection**

- **Category:** Denial of Service (Volumetric, Application-Layer, Resource Exhaustion)

**Q27: Category_5_Social_Engineering_Detection**

- **Category:** Social Engineering (Phishing, Vishing, Smishing, BEC, Physical)

**Q28: Category_6_Web_Attack_Detection**

- **Category:** Web Application Attack (SQLi, XSS, Auth Bypass, API Abuse, File Upload)

**Q29: Category_7_Network_Attack_Detection**

- **Category:** Network-Based Attack (MITM, Scanning, Protocol Exploitation, Rogue Device)

**Q30: Category_8_Endpoint_Compromise_Detection**

- **Category:** Endpoint Compromise (Laptop/Workstation, Mobile, Server, IoT/OT)

**Q31: Category_9_Physical_Security_Detection**

- **Category:** Physical Security (Theft/Loss, Unauthorized Access, Hardware Tampering)

**Q32: Category_10_Config_Patch_Detection**

- **Category:** Configuration/Patch (Misconfiguration, Unpatched Vulnerability, Shadow IT)

**Q33: Category_11_Other_Detection**

- **Category:** Other (Policy Violation, False Positive, Non-Incident Event)

---

## Sheet 3: Alert Handling

**Purpose:** Assess alert triage, investigation, and escalation processes

**Assessment Questions (25 questions):**

---

### **Section A: Triage Procedures (Q34-Q40)**

**Q34: Triage_Procedure_Documented**

- **Question:** Are alert triage procedures documented?
- **Dropdown:** Yes - Comprehensive / Yes - Basic / No
- **Comprehensive:** Procedures for each severity, decision trees, escalation triggers
- **Evidence:** Triage procedure document, SOC runbook

**Q35: Triage_SLA_Defined**

- **Question:** Are triage time SLAs defined for each severity level?
- **Dropdown:** Yes / No
- **Example SLAs (from ISMS-POL-A.5.24-28):**
  - Critical: 15 minutes
  - High: 1 hour
  - Medium: 4 hours
  - Low: 24 hours
- **Evidence:** SLA documentation

**Q36: Triage_SLA_Compliance**

- **Question:** What percentage of alerts are triaged within SLA? (Last 90 days)
- **Format:** Percentage (0-100%)
- **Target:** >90% compliance
- **Gap if <80%:** HIGH - Slow triage delays response
- **Evidence:** Ticketing system SLA compliance report

**Q37: Triage_Queue_Management**

- **Question:** How are alerts prioritized in the triage queue?
- **Dropdown:** Automated (Severity-Based) / Manual (Analyst Discretion) / FIFO (First In First Out) / No Defined Process
- **Best Practice:** Automated severity-based prioritization with analyst override

**Q38: Triage_Shift_Handoff**

- **Question:** Is there a documented shift handoff process for open/in-progress alerts?
- **Dropdown:** Yes - Formal Process / Informal / No
- **Risk if "Informal" or "No":** Alerts dropped during handoff, continuity lost

**Q39: Triage_Training**

- **Question:** Do all SOC analysts receive triage procedure training?
- **Dropdown:** Yes - Regular / Yes - Onboarding Only / No
- **Best Practice:** Onboarding + annual refresher + on-the-job mentoring

**Q40: Triage_Tools**

- **Question:** What tools do analysts use for alert triage? (Select all: SIEM/Ticketing System/EDR Console/Threat Intel Platform/SOAR/Other)
- **Format:** Checkbox
- **Best Practice:** Integrated workflow (SIEM alert → auto-create ticket → enrich with threat intel)

---

### **Section B: Investigation Playbooks (Q41-Q48)**

**Q41: Playbook_Existence**

- **Question:** Are investigation playbooks documented for common incident types?
- **Dropdown:** Yes - Comprehensive / Yes - Limited / No
- **Evidence:** Playbook library (SOAR platform or document repository)

**Q42: Playbook_Coverage**

- **Question:** Which incident categories have documented playbooks? (Select all: Malware/Unauthorized Access/Data Breach/DoS/Social Engineering/Web Attack/Network Attack/Endpoint/Physical/Config-Patch/Other)
- **Format:** Checkbox
- **Target:** Playbooks for top 5-7 incident categories (based on historical volume)

**Q43: Playbook_Format**

- **Question:** In what format are playbooks maintained?
- **Dropdown:** SOAR Automated / Written Documents / Flowcharts / Checklist / Not Documented
- **Best Practice:** SOAR automated (fastest, most consistent) > Written/Flowcharts

**Q44: Playbook_Update_Frequency**

- **Question:** How often are playbooks reviewed and updated?
- **Dropdown:** Quarterly / Semi-Annually / Annually / After Major Incidents / Never
- **Best Practice:** Annually + after major incidents (lessons learned)

**Q45-Q48:** **Example Playbook Assessment (4 most common incident types)**

For each common incident type:

- **Playbook Exists:** Yes / No
- **Playbook Completeness:** Comprehensive / Basic / Missing Steps
- **Analyst Feedback:** Effective / Needs Improvement / Not Used

**Q45: Playbook_Malware**

- **Incident Type:** Malware/Ransomware

**Q46: Playbook_Phishing**

- **Incident Type:** Phishing/BEC

**Q47: Playbook_Unauthorized_Access**

- **Incident Type:** Unauthorized Access/Compromised Credentials

**Q48: Playbook_Data_Exfiltration**

- **Incident Type:** Data Exfiltration/Breach

---

### **Section C: Escalation & Handoff (Q49-Q53)**

**Q49: Escalation_Criteria_Defined**

- **Question:** Are escalation criteria clearly defined (when to escalate from SOC to CSIRT)?
- **Dropdown:** Yes - Well Defined / Partially Defined / No
- **Common Escalation Triggers:**
  - Severity = Critical or High
  - Data breach confirmed (personal/confidential data)
  - Widespread impact (multiple systems/users)
  - Requires forensic investigation
  - Regulatory notification may be required

**Q50: Escalation_Process**

- **Question:** How are incidents escalated from SOC to CSIRT?
- **Dropdown:** Automated (Ticketing System) / Manual (Email/Phone) / Informal / No Process
- **Best Practice:** Automated escalation via ticketing system with notifications

**Q51: CSIRT_Handoff_Documentation**

- **Question:** Is there a documented handoff checklist for escalation to CSIRT?
- **Dropdown:** Yes / No
- **Handoff Should Include:**
  - Initial triage findings
  - Affected systems/users
  - Timeline of events
  - Evidence collected so far
  - Recommended next steps

**Q52: False_Positive_Handling**

- **Question:** Is there a documented process for handling false positives?
- **Dropdown:** Yes - Documented / Informal / No
- **Process Should Include:**
  - Analyst marks alert as false positive with justification
  - Detection engineer reviews for tuning
  - Rule tuned or suppression created
  - Feedback loop tracked

**Q53: False_Positive_Tuning_Loop**

- **Question:** Is there a feedback loop from false positive identification to rule tuning?
- **Dropdown:** Yes - Systematic / Informal / No
- **Best Practice:** Monthly false positive review → rule tuning → measure improvement

---

### **Section D: Analyst Capacity & Training (Q54-Q58)**

**Q54: Analyst_FTE**

- **Question:** How many FTE SOC analysts handle alert triage?
- **Format:** Number
- **Benchmarking:** 
  - Alert volume / Analyst capacity
  - Target: <50 alerts per analyst per shift (allows proper investigation time)

**Q55: Analyst_Tier_Structure**

- **Question:** Is there a tiered analyst structure (Tier 1, Tier 2, Tier 3)?
- **Dropdown:** Yes - Multi-Tier / No - Single Tier
- **Multi-Tier Benefits:**
  - Tier 1: Triage and initial investigation
  - Tier 2: Deep investigation, escalated incidents
  - Tier 3: Threat hunting, complex investigations

**Q56: Analyst_Training_Frequency**

- **Question:** How often do SOC analysts receive training on triage and investigation?
- **Dropdown:** Quarterly / Semi-Annually / Annually / Onboarding Only / Never
- **Best Practice:** Quarterly (threat landscape evolves rapidly)

**Q57: Analyst_Burnout_Assessment**

- **Question:** Are there indicators of analyst burnout (high turnover, low morale)?
- **Dropdown:** No Indicators / Some Indicators / Significant Indicators
- **Indicators:**
  - Turnover >20% annually
  - Increased triage times
  - Decreased alert handling quality
  - Staff feedback negative

**Q58: Analyst_Tool_Training**

- **Question:** Do analysts receive training on all detection and investigation tools?
- **Dropdown:** Yes - Comprehensive / Partial / No
- **Tools:** SIEM, EDR, Ticketing, Threat Intel Platform, SOAR, Forensic Tools

---

## Sheet 4: Classification & Severity

**Purpose:** Assess incident classification consistency and severity assignment

**Assessment Questions (25 questions):**

---

### **Section A: Classification Framework (Q59-Q65)**

**Q59: Classification_Taxonomy_Adopted**

- **Question:** Has [Organization] adopted the ISMS-REF-A.5.24-28 incident classification taxonomy (11 primary categories)?
- **Dropdown:** Yes - Fully Adopted / Partially Adopted / No - Different Taxonomy
- **Note:** Consistency with reference guide enables better tracking and comparison

**Q60: Classification_Procedure_Documented**

- **Question:** Is the incident classification procedure documented?
- **Dropdown:** Yes / No
- **Procedure Should Define:**
  - How to assign primary category
  - How to assign subcategory
  - When to use multiple categories
  - Reclassification triggers

**Q61: Classification_Training**

- **Question:** Do analysts receive training on incident classification?
- **Dropdown:** Yes - Regular / Yes - Onboarding Only / No
- **Best Practice:** Onboarding + annual refresher + classification examples

**Q62: Classification_Consistency_Check**

- **Question:** Is classification consistency periodically reviewed (e.g., QA sampling)?
- **Dropdown:** Yes - Monthly / Yes - Quarterly / Yes - Annually / No
- **QA Process:** Sample 20-30 incidents, verify classification accuracy, provide feedback

**Q63: Classification_Accuracy**

- **Question:** Based on recent QA review, what is the classification accuracy rate?
- **Format:** Percentage (0-100%)
- **Target:** >90% accuracy
- **Gap if <80%:** MEDIUM - Inconsistent classification affects metrics and response

**Q64: Reclassification_Process**

- **Question:** Is there a documented process for reclassifying incidents as more information becomes available?
- **Dropdown:** Yes / No
- **Example:** Initial classification "Malware" reclassified to "Data Breach" upon discovering exfiltration

**Q65: Multi_Category_Incidents**

- **Question:** How are incidents with multiple categories handled (e.g., Phishing + Malware)?
- **Dropdown:** Primary + Secondary Categories / Multiple Incident Tickets / Single Best-Fit Category / No Process
- **Best Practice:** Primary + Secondary categories in single ticket

---

### **Section B: Severity Assignment (Q66-Q75)**

**Q66: Severity_Levels_Defined**

- **Question:** How many severity levels does [Organization] use?
- **Dropdown:** 4 (Critical/High/Medium/Low) / 3 (High/Medium/Low) / 5 (Critical/High/Medium/Low/Info) / Other
- **Recommendation:** 4 levels (aligns with ISMS-POL-A.5.24-28)

**Q67: Severity_Criteria_Documented**

- **Question:** Are severity assignment criteria documented?
- **Dropdown:** Yes - Comprehensive / Yes - Basic / No
- **Criteria Should Include:**
  - Impact (data confidentiality, system availability, financial loss)
  - Scope (number of systems/users affected)
  - Regulatory implications (breach notification required?)
  - Recoverability (ease of containment and recovery)

**Q68: Critical_Severity_Criteria**

- **Question:** What defines a "Critical" severity incident? (Select all: Data Breach (Restricted/Confidential)/Ransomware/Widespread System Outage/Regulatory Notification Required/Executive/C-Suite Compromise/Other)
- **Format:** Checkbox

**Q69: Severity_Assignment_Training**

- **Question:** Do analysts receive training on severity assignment?
- **Dropdown:** Yes - Regular / Yes - Onboarding Only / No

**Q70: Severity_Consistency_QA**

- **Question:** Is severity assignment consistency periodically reviewed?
- **Dropdown:** Yes - Monthly / Yes - Quarterly / Yes - Annually / No

**Q71: Severity_Upgrade_Process**

- **Question:** Is there a process for upgrading severity as incidents evolve?
- **Dropdown:** Yes - Documented / Informal / No
- **Example:** Initial "Medium" upgraded to "High" when scope expands

**Q72: Severity_Downgrade_Process**

- **Question:** Is there a process for downgrading severity (e.g., false alarm, contained quickly)?
- **Dropdown:** Yes - Documented / Informal / No

**Q73-Q75:** **Severity Distribution Analysis (Last 90 Days)**

**Q73: Severity_Distribution_Critical**

- **Question:** What percentage of incidents were classified as Critical? (Last 90 days)
- **Format:** Percentage
- **Typical Distribution:** 1-5% Critical, 10-20% High, 40-50% Medium, 30-40% Low

**Q74: Severity_Distribution_High**

- **Question:** What percentage of incidents were classified as High?
- **Format:** Percentage

**Q75: Severity_Distribution_Medium**

- **Question:** What percentage of incidents were classified as Medium?
- **Format:** Percentage

**Note:** Low severity calculated as 100% - (Critical + High + Medium)

---

### **Section C: Category/Severity Correlation (Q76-Q83)**

**Q76-Q83:** **Most Common Category/Severity Combinations (Last 90 Days)**

Assess the top incident categories by volume and their typical severity:

**Q76: Top_Category_1**

- **Category:** [Auto-populate from incident data or manual entry]
- **Incident Count:** Number
- **Typical Severity:** Critical / High / Medium / Low
- **Example:** "Malware - 45 incidents - Typical Severity: High"

**Q77-Q83:** Repeat for Top Categories 2-8

**Purpose:** Identify patterns (e.g., "All Ransomware incidents are Critical" → validate severity criteria)

---

## Sheet 5: Detection Effectiveness

**Purpose:** Analyze detection metrics and performance

**Assessment Questions (25 questions) + Metrics Calculations:**

---

### **Section A: Mean Time to Detect (MTTD) (Q84-Q88)**

**Q84: MTTD_Tracked**

- **Question:** Is Mean Time to Detect (MTTD) tracked?
- **Dropdown:** Yes / No
- **MTTD Definition:** Time from actual event occurrence to alert generation
- **Note:** Requires correlation between event timestamp and alert timestamp

**Q85: MTTD_Overall**

- **Question:** What is the overall MTTD (all incidents, last 90 days)?
- **Format:** Duration (e.g., "2 hours", "30 minutes", "5 days")
- **Benchmark:**
  - <1 hour: Excellent
  - 1-4 hours: Good
  - 4-24 hours: Fair
  - >24 hours: Poor (long dwell time before detection)

**Q86: MTTD_Critical**

- **Question:** What is the MTTD for Critical severity incidents?
- **Format:** Duration
- **Target:** <15 minutes (near real-time detection)

**Q87: MTTD_High**

- **Question:** What is the MTTD for High severity incidents?
- **Format:** Duration
- **Target:** <1 hour

**Q88: MTTD_Improvement_Trend**

- **Question:** Is MTTD improving, stable, or worsening over time?
- **Dropdown:** Improving / Stable / Worsening / Not Tracked
- **Evidence:** MTTD trend chart (last 6-12 months)

---

### **Section B: Mean Time to Triage (MTTT) (Q89-Q93)**

**Q89: MTTT_Tracked**

- **Question:** Is Mean Time to Triage (MTTT) tracked?
- **Dropdown:** Yes / No
- **MTTT Definition:** Time from alert generation to triage completion (classification + severity assignment)

**Q90: MTTT_Overall**

- **Question:** What is the overall MTTT (all alerts, last 90 days)?
- **Format:** Duration
- **Benchmark:**
  - <30 minutes: Excellent
  - 30 min - 2 hours: Good
  - 2-8 hours: Fair
  - >8 hours: Poor

**Q91: MTTT_Critical**

- **Question:** What is the MTTT for Critical alerts?
- **Format:** Duration
- **Target:** <15 minutes (per ISMS-POL-A.5.24-28 SLA)

**Q92: MTTT_High**

- **Question:** What is the MTTT for High alerts?
- **Format:** Duration
- **Target:** <1 hour

**Q93: MTTT_SLA_Compliance**

- **Question:** What percentage of alerts meet MTTT SLA (per severity)?
- **Format:** Percentage
- **Target:** >90%
- **Evidence:** Ticketing system SLA compliance report

---

### **Section C: False Positive Analysis (Q94-Q100)**

**Q94: False_Positive_Tracking**

- **Question:** Are false positives systematically tracked?
- **Dropdown:** Yes / No
- **Importance:** High false positive rate = analyst burnout + missed real threats

**Q95: Total_Alerts_90_Days**

- **Question:** How many total alerts were generated in the last 90 days?
- **Format:** Number
- **Use:** Denominator for false positive rate calculation

**Q96: False_Positives_90_Days**

- **Question:** How many alerts were determined to be false positives (last 90 days)?
- **Format:** Number

**Q97: False_Positive_Rate**

- **Question:** What is the false positive rate? (Auto-calculate: Q96 / Q95 × 100)
- **Format:** Percentage (calculated)
- **Benchmark:**
  - <5%: Excellent (well-tuned)
  - 5-15%: Good
  - 15-30%: Fair (tuning needed)
  - >30%: Poor (high noise, analyst fatigue risk)

**Q98: False_Positive_Trend**

- **Question:** Is the false positive rate improving, stable, or worsening?
- **Dropdown:** Improving / Stable / Worsening / Not Tracked
- **Goal:** Continuous improvement through tuning

**Q99: Top_False_Positive_Source**

- **Question:** What detection mechanism generates the most false positives?
- **Dropdown:** SIEM / EDR / IDS/IPS / NDR / User Reports / Other
- **Action:** Prioritize tuning for top source

**Q100: False_Positive_Tuning_Backlog**

- **Question:** Is there a backlog of false positive alerts needing tuning?
- **Dropdown:** Yes - Large Backlog / Yes - Small Backlog / No Backlog / Not Tracked
- **Risk if "Large Backlog":** Noise continues, analyst fatigue increases

---

### **Section D: True Positive & Incident Volume (Q101-Q105)**

**Q101: True_Positives_90_Days**

- **Question:** How many alerts were confirmed as true positives (actual incidents) in last 90 days?
- **Format:** Number

**Q102: True_Positive_Rate**

- **Question:** What is the true positive rate? (Auto-calculate: Q101 / Q95 × 100)
- **Format:** Percentage (calculated)
- **Interpretation:** Inverse of false positive rate (approximately)

**Q103: Incident_Volume_Trend**

- **Question:** Is incident volume increasing, stable, or decreasing over time?
- **Dropdown:** Increasing / Stable / Decreasing / Not Tracked
- **Interpretation:**
  - Increasing: Growing threat activity OR improved detection
  - Decreasing: Better security posture OR under-detection

**Q104: Alert_to_Incident_Ratio**

- **Question:** What is the alert-to-incident ratio? (Total Alerts / True Positives)
- **Format:** Ratio (e.g., "10:1" means 10 alerts per actual incident)
- **Benchmark:** Lower is better (less noise per real incident)

**Q105: Handling_Capacity_Assessment**

- **Question:** Can the SOC handle the current alert/incident volume?
- **Dropdown:** Yes - Comfortably / Yes - At Capacity / No - Overwhelmed
- **Cross-Check:** Alert volume vs. Analyst FTE (Q54)

---

### **Section E: Detection Coverage Gaps (Q106-Q108)**

**Q106: Detection_Blind_Spots_Identified**

- **Question:** Have detection blind spots been identified (threats not currently detected)?
- **Dropdown:** Yes - Documented / Informally Known / No
- **Examples:**
  - No detection for encrypted exfiltration
  - No cloud app monitoring (shadow IT)
  - No detection for insider threat (behavioral analytics)

**Q107: Coverage_Gap_Priority**

- **Question:** Are coverage gaps prioritized for remediation?
- **Dropdown:** Yes / No
- **Prioritization Criteria:** Threat likelihood × Impact

**Q108: Coverage_Improvement_Plan**

- **Question:** Is there a plan to address detection coverage gaps?
- **Dropdown:** Yes - Funded / Planned - Not Funded / No Plan
- **Plan May Include:** New detection tools, additional rules, threat hunting capability

---

## Sheet 6: Gap Analysis

**Purpose:** Consolidate gaps and prioritize remediation

**Gap Register Format:**

| Gap_ID | Assessment_Section | Gap_Description | Risk_Level | Current_State | Target_State | Remediation_Action | Owner | Target_Date | Status |
|--------|-------------------|-----------------|-----------|---------------|--------------|-------------------|-------|-------------|--------|
| GAP-001 | Detection | No NDR/NTA deployed | High | No east-west traffic visibility | NDR deployed for data center | Evaluate and deploy NDR solution | SOC Manager | Q3 2026 | Open |
| GAP-002 | Alert Handling | False positive rate 28% | High | High noise, analyst fatigue | FP rate <10% | Monthly tuning sprints for top 10 noisy rules | Detection Engineer | Q2 2026 | In Progress |
| GAP-003 | Classification | Category QA only annually | Medium | Low classification accuracy (78%) | Accuracy >90% | Implement quarterly QA sampling | SOC Manager | Q1 2026 | Open |
| GAP-004 | Metrics | MTTD not tracked | Medium | No visibility into detection lag | MTTD tracked and trended monthly | Configure MTTD reporting in SIEM | SOC Analyst Lead | Q1 2026 | Open |
| GAP-005 | Coverage | No detection for Category 9 (Physical) | Low | Physical security incidents not detected | Integration with physical access logs | Integrate badge reader logs into SIEM | IT Manager | Q4 2026 | Planned |

**Risk Levels:**

- **Critical:** Severe detection blind spot, high false positive rate preventing detection
- **High:** Significant gap, should remediate within 3 months
- **Medium:** Moderate gap, remediate within 6-12 months
- **Low:** Minor gap, address when feasible

---

## Sheet 7: Evidence Register

**Evidence Types for Detection Assessment:**

- SIEM rule catalog export
- Alert handling metrics dashboard (screenshot)
- False positive analysis report
- MTTD/MTTT trend charts
- Classification QA review results
- Triage procedure documentation
- Investigation playbook examples
- Detection coverage matrix
- EDR deployment report
- IDS/IPS signature version report

---

## Sheet 8: Dashboard

**Dashboard Sections:**

**A. Detection Effectiveness Summary**

- Overall MTTD: [Metric]
- Overall MTTT: [Metric]
- False Positive Rate: [%]
- True Positive Rate: [%]
- Detection Coverage: [X out of 11 categories]

**B. Alert Handling Performance**

- Total Alerts (90 days): [#]
- Alerts Triaged: [#]
- Triage SLA Compliance: [%]
- Analyst FTE: [#]
- Alerts per Analyst per Day: [#]

**C. Classification Accuracy**

- Classification Accuracy Rate: [%]
- Severity Assignment Consistency: [%]
- Reclassifications (90 days): [#]

**D. Top Detection Gaps**
1. [Gap description]
2. [Gap description]
3. [Gap description]

---

## Sheet 9: Approval Sign-Off

**Assessment Summary:**

- Assessment Period: [Dates]
- Completed By: SOC Manager
- Overall Detection Maturity: [Score/Level]
- Critical Gaps: [Count]

**Approval Workflow:**

- SOC Manager: [Name, Date, Signature]
- CISO: [Name, Date, Approval Decision, Signature]
- Next Review Date: [Date + 12 months]

---

# Metrics Calculation Guide

## Mean Time to Detect (MTTD)

**Formula:**
```
MTTD = Σ(Alert Timestamp - Event Timestamp) / Number of Incidents
```

**Data Required:**

- Event timestamp (actual malicious activity)
- Alert timestamp (when SIEM/EDR generated alert)

**Challenge:** Event timestamp often unknown (requires log analysis or forensics)

**Workaround:** Use first log evidence timestamp as proxy for event timestamp

---

## Mean Time to Triage (MTTT)

**Formula:**
```
MTTT = Σ(Triage Complete Timestamp - Alert Timestamp) / Number of Alerts
```

**Data Required:**

- Alert timestamp
- Triage complete timestamp (when classification + severity assigned)

**Source:** Incident ticketing system (workflow timestamps)

---

## False Positive Rate

**Formula:**
```
False Positive Rate = (False Positives / Total Alerts) × 100
```

**Data Required:**

- Total alerts generated
- Alerts marked as false positive

**Best Practice:** Track by detection source (SIEM, EDR, etc.) to identify tuning priorities

---

## Detection Coverage

**Formula:**
```
Coverage = (Categories with Detection / Total Categories) × 100
```

**Example:** 9 out of 11 categories have detection = 82% coverage

**Weighting:** Consider weighting by threat likelihood (e.g., Malware weighted higher than Physical Security)

---

# Common Mistakes to Avoid

**❌ Mistake:** Focusing on alert volume instead of alert quality
**✅ Solution:** Prioritize reducing false positives over increasing alert count

**❌ Mistake:** Not tracking MTTD/MTTT (no visibility into detection lag)
**✅ Solution:** Implement metrics tracking in SIEM and ticketing system

**❌ Mistake:** Inconsistent classification across analysts
**✅ Solution:** Regular QA sampling + classification training

**❌ Mistake:** No feedback loop from false positives to tuning
**✅ Solution:** Monthly false positive review → rule tuning → measure improvement

**❌ Mistake:** Detection engineers isolated from SOC analysts
**✅ Solution:** Weekly sync between detection engineering and SOC (discuss noisy rules, coverage gaps)

---

# Assessment Timeline

**Week 1:**

- Day 1-2: Extract metrics (MTTD, MTTT, false positive rate, alert volume)
- Day 3-4: Review detection mechanisms and coverage
- Day 5: Review triage procedures and playbooks

**Week 2:**

- Day 6-7: Complete assessment (Detection through Effectiveness sheets)
- Day 8: Gap analysis
- Day 9: Evidence collection
- Day 10: Quality review and approval

**Total:** 2 weeks (part-time) or 1 week (dedicated full-time)

---

**END OF PART I: USER COMPLETION GUIDE**

---

# PART II: TECHNICAL SPECIFICATION

# Workbook Structure

**Sheet 1: Instructions & Legend** - Assessment guidance
**Sheet 2: Detection Mechanisms** - 33 questions (SIEM, EDR, IDS/IPS, NDR, user reporting, coverage by category)
**Sheet 3: Alert Handling** - 25 questions (triage, playbooks, escalation, capacity)
**Sheet 4: Classification & Severity** - 25 questions (category assignment, severity criteria, consistency)
**Sheet 5: Detection Effectiveness** - 25 questions (MTTD, MTTT, false positives, coverage gaps)
**Sheet 6: Gap Analysis** - 40 gap capacity
**Sheet 7: Evidence Register** - 60 evidence capacity
**Sheet 8: Dashboard** - Detection effectiveness summary
**Sheet 9: Approval Sign-Off** - SOC Manager + CISO approval

---

# Python Script Specifications

**Total Questions:** 108 (33+25+25+25)
**Calculated Metrics:** MTTD, MTTT, False Positive Rate, Coverage %, Alert-to-Incident Ratio
**Conditional Formatting:** 

- Red: High false positive rate (>30%), Poor MTTD (>24h), Low coverage (<60%)
- Yellow: Medium thresholds
- Green: Good performance

**Data Validation:**

- Dropdowns for all categorical questions
- Date format validation
- Percentage validation (0-100%)
- Duration format guidance

---

**END OF SPECIFICATION**

---

*"The first principle is that you must not fool yourself — and you are the easiest person to fool."*
— Richard Feynman

<!-- QA_VERIFIED: 2026-02-01 -->
