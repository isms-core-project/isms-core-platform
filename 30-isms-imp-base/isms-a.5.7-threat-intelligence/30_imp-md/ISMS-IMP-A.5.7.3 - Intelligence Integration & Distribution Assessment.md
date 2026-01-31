**ISMS-IMP-A.5.7.3 - Intelligence Integration & Distribution Assessment**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.7: Threat Intelligence

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.7.3 |
| **Version** | 1.0 |
| **Assessment Area** | Intelligence Integration into Security Operations & Distribution to Stakeholders |
| **Related Policy** | ISMS-POL-A.5.7, Section 2.3 (Intelligence Dissemination Requirements), Section 2.4 (Risk Assessment Integration Requirements), Section 2.5 (Incident Management Integration Requirements), Section 2.7 (Effectiveness Measurement Requirements) |
| **Purpose** | Assess effectiveness of threat intelligence integration with security tools, dissemination to stakeholders, and measurement of operational impact including prevention tracking |
| **Target Audience** | Security Operations Manager, SOC Team, Incident Response, Network Security, Threat Intelligence Team, Risk Management, CISO, Auditors |
| **Assessment Type** | Operational & Compliance |
| **Review Cycle** | Quarterly |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial consolidated specification (17 sheets) | ISMS Implementation Team |

### Document Structure

This document consists of two parts:

- **PART I: USER COMPLETION GUIDE**
  - Assessment Overview
  - Prerequisites
  - Workflow (16 Phases)
  - Completing Each Sheet
  - Evidence Collection
  - **CRITICAL: Audit Evidence Requirements** (Sheets 7, 13, 14, 15)
  - Common Pitfalls
  - Quality Checklist
  - Review & Approval

- **PART II: TECHNICAL SPECIFICATION**
  - Excel Workbook Structure (17 sheets)
  - Sheet-by-Sheet Specifications
  - Integration Architecture
  - IOC Deployment Workflows
  - Prevention Tracking Methodology
  - Risk Assessment Updates (ISO 27001 Clause 6.1)
  - Incident-TI Integration (Controls A.5.24-5.28)


---

# PART I: USER COMPLETION GUIDE

## Assessment Overview

### Purpose & Scope

**Assessment Name:** ISMS-IMP-A.5.7.3 - Intelligence Integration & Distribution Assessment

#### What This Assessment Covers

This assessment evaluates how effectively threat intelligence is INTEGRATED into security operations and DISTRIBUTED to stakeholders. This is the "WHERE does intelligence go?" assessment that answers:

- How is threat intelligence integrated into security tools? (SIEM, EDR, firewalls, proxies, email gateways)
- How effectively are IOCs deployed and tracked?
- Who receives threat intelligence? (stakeholder management)
- How is intelligence distributed? (email, portal, API, briefings)
- **CRITICAL**: How many incidents were prevented? (Sheet 7 - MANDATORY audit evidence)
- **CRITICAL**: How does TI update risk assessments? (Sheet 13 - ISO 27001 Clause 6.1 MANDATORY)
- **CRITICAL**: How is TI used in incident response? (Sheet 14 - Controls A.5.24-5.28 MANDATORY)
- **CRITICAL**: What business decisions were driven by TI? (Sheet 15 - MANDATORY audit evidence)
- How effective is the feedback loop from consumers back to producers?


#### Key Principle

This assessment is **integration and distribution-focused**. You document HOW intelligence flows INTO security tools and OUT to stakeholders - not how intelligence is collected (A.5.7.1) or analyzed (A.5.7.2), but where it goes and what happens with it.

**CRITICAL COMPLIANCE NOTE**: Sheets 7, 13, 14, and 15 provide MANDATORY audit evidence required by:

- ISO 27001:2022 Control A.5.7 (threat intelligence effectiveness)
- ISO 27001:2022 Clause 6.1 (risk assessment updates - Sheet 13)
- ISO 27001:2022 Controls A.5.24-5.28 (incident management integration - Sheet 14)


#### What You'll Document

**Tool Integration:**

- Security tool integration matrix (SIEM, EDR, firewalls, proxies, email gateways)
- IOC deployment tracking and effectiveness
- SIEM integration details (rules, queries, alerts)
- EDR integration details (IOC deployment, detections)


**Dissemination:**

- Stakeholder registry (who needs intelligence?)
- Distribution channels (email, portal, API, briefings)
- Distribution tracking (who received what?)
- Feedback collection (is intelligence useful?)


**MANDATORY Audit Evidence (CRITICAL):**

- **Sheet 7: Prevention_Tracking** - ≥3 validated prevented incidents per quarter
- **Sheet 13: Risk_Assessment_Updates** - ≥3 risk assessment updates per quarter (Clause 6.1)
- **Sheet 14: Incident_TI_Integration** - ≥70% of P1/P2 incidents use TI (Controls A.5.24-5.28)
- **Sheet 15: Intelligence_Driven_Decisions** - ≥5 documented business decisions per quarter


**Operational Tracking:**

- Integration metrics and KPIs
- Threat hunting campaigns driven by TI
- Dissemination effectiveness


#### How This Relates to Other A.5.7 Assessments

| Assessment | Focus | Relationship to A.5.7.3 |
|------------|-------|-------------------------|
| ISMS-IMP-A.5.7.1 | Source Portfolio | Sources identified, feeds into A.5.7.3 |
| ISMS-IMP-A.5.7.2 | Collection & Analysis | VTL records and IOCs produced, consumed by A.5.7.3 |
| **ISMS-IMP-A.5.7.3** | **Integration & Distribution** | **WHERE intelligence is deployed (this assessment)** |
| ISMS-IMP-A.5.7.4 | Effectiveness Dashboard | Consolidates A.5.7.3 metrics |
| ISMS-IMP-A.5.7.5 | Standalone Dashboard | Uses A.5.7.3 prevention/decision metrics |

This assessment (A.5.7.3) is the OPERATIONAL DEPLOYMENT - it consumes intelligence from A.5.7.2 and demonstrates VALUE through prevented incidents, updated risk assessments, and business decisions.

### Who Should Complete This Assessment

#### Primary Stakeholders

1. **Security Operations Manager** - Overall assessment ownership, tool integration
2. **SOC Team** - IOC deployment, SIEM/EDR integration, detection tracking
3. **Threat Intelligence Team** - Dissemination workflows, stakeholder engagement
4. **Network Security Team** - Firewall/proxy integration, blocking effectiveness
5. **Incident Response Team** - Incident-TI integration tracking (Sheet 14)
6. **Risk Management** - Risk assessment updates (Sheet 13 - MANDATORY)
7. **CISO** - Business decisions documentation (Sheet 15 - MANDATORY)

#### Required Skills

- Understanding of security tool architecture (SIEM, EDR, firewalls, proxies)
- Experience with IOC deployment and management
- Familiarity with stakeholder management and communication
- Knowledge of incident response processes
- Understanding of risk assessment methodologies (ISO 27001 Clause 6.1)
- Ability to document business decisions and their intelligence basis


#### Time Commitment

- **Initial assessment:** 12-18 hours (comprehensive integration review across 15 sheets)
- **Quarterly updates:** 4-6 hours (update metrics, prevention tracking, risk assessments)
- **Monthly tracking:** 1-2 hours (IOC deployment, stakeholder distribution, prevention documentation)
- **Prevention tracking (Sheet 7):** Ongoing (document each prevented incident - 30 min per incident)
- **Risk updates (Sheet 13):** As needed when intelligence triggers risk changes
- **Incident tracking (Sheet 14):** Ongoing (document TI usage in each P1/P2 incident)
- **Decision tracking (Sheet 15):** As needed when intelligence drives business decisions


### Expected Outputs

Upon completion, you will have:

1. ✅ **Tool integration documented** - Complete security tool integration matrix (Sheet 2)
2. ✅ **IOC deployment tracked** - All deployed IOCs with hit tracking (Sheet 3)
3. ✅ **Dissemination channels mapped** - How intelligence reaches stakeholders (Sheet 4)
4. ✅ **Stakeholder registry complete** - Who needs what intelligence (Sheet 5)
5. ✅ **Distribution tracking operational** - Who received what intelligence (Sheet 6)
6. ✅ **MANDATORY: Prevention tracking** - ≥3 prevented incidents per quarter (Sheet 7)
7. ✅ **Feedback collection active** - Stakeholder feedback captured (Sheet 8)
8. ✅ **Integration metrics calculated** - KPIs against targets (Sheet 9)
9. ✅ **SIEM integration detailed** - Complete SIEM integration mapping (Sheet 10)
10. ✅ **EDR integration detailed** - Complete EDR integration mapping (Sheet 11)
11. ✅ **Threat hunting tracked** - TI-driven hunting campaigns (Sheet 12)
12. ✅ **MANDATORY: Risk assessments updated** - ≥3 updates per quarter (Sheet 13 - Clause 6.1)
13. ✅ **MANDATORY: Incident-TI integration** - ≥70% P1/P2 use TI (Sheet 14 - A.5.24-5.28)
14. ✅ **MANDATORY: Business decisions documented** - ≥5 per quarter (Sheet 15)
15. ✅ **Approved assessment** - Three-level approval workflow completed

---

## Prerequisites

### Information You'll Need

Before starting this assessment, gather:

#### 1. Access Required

- SIEM admin access (for integration verification)
- EDR/XDR admin console access
- Firewall/proxy management access
- Email gateway configuration access
- Threat Intelligence Platform (TIP) access
- Risk management system access (for Sheet 13)
- Incident management system access (for Sheet 14)
- Executive decision documentation (for Sheet 15)


#### 2. Documentation

- Security tool architecture diagrams
- IOC deployment procedures
- Stakeholder communication plans
- Intelligence distribution lists
- SIEM correlation rules using TI
- EDR detection rules using TI
- Historical prevented incident documentation
- Risk assessment records (past 12 months)
- Incident response records with TI usage
- Executive meeting minutes referencing TI-driven decisions


#### 3. Historical Data

- IOC deployment logs (past 90 days minimum)
- SIEM/EDR detection statistics
- Intelligence distribution records
- Stakeholder feedback surveys or emails
- **CRITICAL**: Prevented incident records (if any exist)
- **CRITICAL**: Risk assessment change logs
- **CRITICAL**: Incident records showing TI usage
- **CRITICAL**: Business decision records mentioning threat intelligence


#### 4. Policy Requirements

- **ISMS-POL-A.5.7, Section 2.3** (Intelligence Dissemination Requirements)
- **ISMS-POL-A.5.7, Section 2.4** (Risk Assessment Integration Requirements) - MANDATORY
- **ISMS-POL-A.5.7, Section 2.5** (Incident Management Integration Requirements) - MANDATORY
- **ISMS-POL-A.5.7, Section 2.7** (Effectiveness Measurement Requirements) - Prevention tracking
- **ISO 27001:2022 Clause 6.1** (Risk Assessment) - Referenced in Sheet 13
- **ISO 27001:2022 Controls A.5.24-5.28** (Incident Management) - Referenced in Sheet 14


### Required Tools

- Microsoft Excel (2016 or later)
- Access to security tool management consoles
- Screen capture tools (for evidence screenshots)
- Risk management system access
- Incident management system access
- Meeting minutes or decision logs access


### Dependencies

This assessment depends on:

- **A.5.7.1 (Sources Assessment)** - Source IDs referenced in IOC deployment
- **A.5.7.2 (Collection & Analysis)** - VTL records and IOCs consumed for deployment


Outputs from this assessment feed into:

- **A.5.7.4 (Effectiveness Dashboard)** - Prevention metrics, integration metrics consolidated
- **A.5.7.5 (Standalone Dashboard)** - Prevention and decision metrics for executives
- **Risk Management Process** - Sheet 13 updates feed into risk register
- **Incident Management Process** - Sheet 14 tracks TI usage effectiveness


---

## Workflow

### High-Level Process

```
1. PREPARE (Gather information)
   ↓
2. MAP TOOL INTEGRATION (Sheet 2: What tools integrate?)
   ↓
3. TRACK IOC DEPLOYMENT (Sheet 3: Deploy and monitor IOCs)
   ↓
4. DEFINE DISSEMINATION (Sheet 4: How is intelligence shared?)
   ↓
5. MANAGE STAKEHOLDERS (Sheet 5: Who receives intelligence?)
   ↓
6. TRACK DISTRIBUTION (Sheet 6: Who got what?)
   ↓
7. DOCUMENT PREVENTION (Sheet 7: What incidents were prevented?) ⚠️ MANDATORY
   ↓
8. COLLECT FEEDBACK (Sheet 8: Is intelligence useful?)
   ↓
9. MEASURE EFFECTIVENESS (Sheet 9: Calculate KPIs)
   ↓
10. DETAIL SIEM INTEGRATION (Sheet 10: SIEM deep dive)
   ↓
11. DETAIL EDR INTEGRATION (Sheet 11: EDR deep dive)
   ↓
12. TRACK HUNTING (Sheet 12: TI-driven hunts)
   ↓
13. UPDATE RISK ASSESSMENTS (Sheet 13: Clause 6.1 integration) ⚠️ MANDATORY
   ↓
14. TRACK INCIDENT-TI USAGE (Sheet 14: IR integration) ⚠️ MANDATORY
   ↓
15. DOCUMENT DECISIONS (Sheet 15: Intelligence-driven decisions) ⚠️ MANDATORY
   ↓
16. REVIEW & APPROVE
```

### Detailed Workflow

#### Phase 1: Preparation (2-3 hours)

**Objective:** Gather information and understand requirements

**Steps:**
1. Read this entire User Guide (Parts I and II)
2. Review **ISMS-POL-A.5.7, Section 2.3** (Dissemination Requirements)
3. Review **ISMS-POL-A.5.7, Section 2.4** (Risk Assessment Integration - MANDATORY)
4. Review **ISMS-POL-A.5.7, Section 2.5** (Incident Management Integration - MANDATORY)
5. Review **ISMS-POL-A.5.7, Section 2.7** (Effectiveness Measurement - Prevention tracking)
6. Understand audit requirements for Sheets 7, 13, 14, 15 (MANDATORY evidence)
7. Gather all prerequisites (see above)
8. Schedule time with SMEs (SOC, network security, IR, risk management, executives)
9. Create working folder for evidence collection
10. **CRITICAL**: Identify past prevented incidents, risk updates, TI-driven decisions for documentation

**Deliverable:** Complete understanding of integration landscape and MANDATORY audit requirements

---

#### Phase 2: Tool Integration Matrix (2-3 hours)

**Objective:** Complete Sheet 2 - Tool_Integration_Matrix

**Steps:**
1. List EVERY security tool in [Organization]'s environment:

   - SIEM (Splunk, QRadar, Sentinel, etc.)
   - EDR/XDR (CrowdStrike, SentinelOne, Carbon Black, etc.)
   - Firewalls (Palo Alto, Fortinet, Cisco, etc.)
   - Web proxies (Zscaler, Squid, Blue Coat, etc.)
   - Email gateways (Proofpoint, Mimecast, Microsoft Defender for Office 365, etc.)
   - DNS security (Cisco Umbrella, Infoblox, etc.)
   - Cloud security (CASB, CSPM)

2. For each tool:

   - Document TI integration status (Integrated, Manual, Planned, None)
   - Document integration method (API, Feed, Manual, Email)
   - Document IOC types supported (IP, Domain, Hash, URL, Email)
   - Assess automation level (Fully_Automated, Semi_Automated, Manual)
   - Document update frequency (Real-time, Hourly, Daily, Weekly)
   - Assess integration maturity (High, Medium, Low)

3. Identify integration gaps (tools not receiving TI)
4. Create action items for critical integration gaps

**Deliverable:** Complete tool integration matrix

**Quality Check:**

- ✓ All production security tools documented
- ✓ Integration status current (not aspirational)
- ✓ Critical tools (SIEM, EDR) have High maturity integration
- ✓ Gaps identified with remediation plans


---

#### Phase 3: IOC Deployment Tracking (Ongoing)

**Objective:** Complete Sheet 3 - IOC_Deployment

**Steps:**
1. For each IOC deployed to security tools:

   - Assign unique IOC_ID
   - Document IOC type (IP, Domain, Hash, URL, Email, etc.)
   - Document IOC value
   - Document source intelligence (from A.5.7.2 or external)
   - Document confidence level (High, Medium, Low)
   - Document deployment date and expiration
   - List tools where deployed (SIEM, EDR, Firewall, etc.)
   - Track deployment status (Active, Expired, False_Positive, Removed)

2. Track hits/detections:

   - Count of detections/blocks
   - First hit date
   - Last hit date
   - Actions taken when hit

3. Calculate effectiveness metrics:

   - Hit rate (% of IOCs with detections)
   - False positive rate
   - Average time to first hit

4. Review and remove expired or false positive IOCs
5. Link to prevented incidents (Sheet 7) when IOCs block attacks

**Deliverable:** Running log of all deployed IOCs with hit tracking

**Quality Check:**

- ✓ All deployed IOCs documented
- ✓ Hit tracking current (updated weekly)
- ✓ Expired IOCs removed promptly
- ✓ False positives documented and addressed
- ✓ Prevention linkage maintained (IOC hit → prevented incident)


---

#### Phase 4: Dissemination Channels Mapping (1-2 hours)

**Objective:** Complete Sheet 4 - Dissemination_Channels

**Steps:**
1. Document EVERY method used to distribute threat intelligence:

   - Email distribution lists
   - Portal/wiki access
   - API feeds
   - Briefings (in-person, virtual)
   - Chat channels (Slack, Teams)
   - Ticketing system integrations
   - SMS/mobile alerts

2. For each channel:

   - Document channel type and description
   - List target audiences
   - Document distribution frequency
   - Assess automation level
   - Document access controls/permissions
   - Assess effectiveness

3. Map channels to intelligence types:

   - Strategic intelligence → Executive briefings
   - Tactical intelligence → SOC email distribution
   - Technical IOCs → API feeds to security tools
   - Urgent alerts → SMS + Slack

4. Identify channel gaps or inefficiencies

**Deliverable:** Complete dissemination channel inventory

**Quality Check:**

- ✓ All distribution methods documented
- ✓ Appropriate channels for each audience
- ✓ Automation maximized (reduce manual distribution)
- ✓ Access controls appropriate (TLP compliance)


---

#### Phase 5: Stakeholder Registry (2-3 hours)

**Objective:** Complete Sheet 5 - Stakeholder_Registry

**Steps:**
1. Identify ALL stakeholders who need threat intelligence:

   - **Technical**: SOC analysts, incident responders, network security, system admins
   - **Management**: CISO, security managers, IT managers
   - **Executive**: C-suite, board members
   - **Risk Management**: Risk officers, compliance team
   - **Business Units**: As appropriate (e.g., fraud team for financial threats)

2. For each stakeholder:

   - Document name and role
   - Document intelligence needs (what topics/types?)
   - Document preferred channels
   - Document distribution frequency preference
   - Document TLP clearance level
   - Assess engagement level (Active, Passive, Unresponsive)

3. Map stakeholders to intelligence requirements (from A.5.7.2)
4. Identify stakeholders not receiving appropriate intelligence

**Deliverable:** Complete stakeholder registry with intelligence needs

**Quality Check:**

- ✓ All relevant stakeholders documented
- ✓ Intelligence needs match stakeholder roles
- ✓ Executive stakeholders included (for Sheet 15)
- ✓ Engagement levels assessed honestly


---

#### Phase 6: Distribution Tracking (Ongoing)

**Objective:** Complete Sheet 6 - Distribution_Tracking

**Steps:**
1. For each intelligence product distributed (from A.5.7.2):

   - Document Product_ID (link to A.5.7.2 Sheet 5)
   - Document distribution date
   - List stakeholders who received it
   - Document distribution channel used
   - Track acknowledgment/read receipts
   - Document actions taken by recipients
   - Collect feedback/comments

2. Track distribution metrics:

   - Distribution timeliness (how quickly distributed after production?)
   - Reach (% of intended audience received it)
   - Acknowledgment rate
   - Action rate (% who acted on intelligence)

3. Identify distribution failures or delays
4. Adjust distribution lists based on engagement

**Deliverable:** Running log of all intelligence distributions

**Quality Check:**

- ✓ All products distributed tracked
- ✓ Distribution timeliness monitored (target: <4 hours after production)
- ✓ Acknowledgment tracked (shows stakeholder engagement)
- ✓ Actions documented (demonstrates value)


---

#### Phase 7: Prevention Tracking (Ongoing) - ⚠️ MANDATORY AUDIT EVIDENCE

**Objective:** Complete Sheet 7 - Prevention_Tracking

**PURPOSE**: Document prevented incidents per **ISMS-POL-A.5.7, Section 2.7 (Effectiveness Measurement Requirements)**

**KPI TARGET**: ≥3 validated prevented incidents per quarter

**WHAT QUALIFIES AS "PREVENTED INCIDENT":**

A prevented incident is a situation where:
1. Threat intelligence identified a specific threat (IOC, TTP, vulnerability)
2. Preventive action was taken based on that intelligence
3. The preventive action demonstrably stopped an attack that would have succeeded otherwise
4. The prevention can be verified with evidence

**EXAMPLES OF PREVENTED INCIDENTS:**

✅ **Example 1: IOC Blocking**

- Intelligence: IOC (malicious IP 192.0.2.100) from commercial TI feed
- Action: IP blocked at firewall
- Evidence: Firewall logs show 47 connection attempts from 192.0.2.100 (all blocked)
- Validation: IP confirmed malicious by 3 other sources, used in active campaign
- **Qualifies**: Yes - demonstrable blocking of malicious activity


✅ **Example 2: Emergency Patching**

- Intelligence: CVE-2025-12345 actively exploited (VTL record from A.5.7.2)
- Action: Emergency patching of 15 servers in 48 hours
- Evidence: Vulnerability scan before/after, patch deployment logs
- Validation: Exploit attempts seen in honeypot after patching
- **Qualifies**: Yes - patched before exploitation


✅ **Example 3: Phishing Campaign Block**

- Intelligence: Phishing campaign targeting financial sector (from ISAC)
- Action: Email gateway rules updated to block specific indicators
- Evidence: 127 phishing emails blocked over 3 days
- Validation: Samples match intelligence, malicious payload confirmed
- **Qualifies**: Yes - mass phishing prevented


❌ **Non-Example 1: Routine IOC Blocking**

- Intelligence: Generic IOC list update (not threat-specific)
- Action: IOC feed refreshed (routine process)
- Evidence: No hits detected
- **Does NOT Qualify**: No specific threat prevented


❌ **Non-Example 2: Assumed Prevention**

- Intelligence: General threat advisory ("ransomware increasing")
- Action: Security awareness training conducted
- Evidence: Training attendance records
- **Does NOT Qualify**: No specific incident prevented (general hygiene)


**STEPS TO DOCUMENT PREVENTED INCIDENT:**

1. **Identify the Intelligence**:

   - What specific threat intelligence was received?
   - Source intelligence ID (from A.5.7.1 or A.5.7.2)
   - Intelligence date
   - Confidence level


2. **Document the Preventive Action**:

   - What specific action was taken?
   - When was action taken?
   - Who authorized/executed the action?
   - Systems/processes affected


3. **Collect Evidence**:

   - **REQUIRED**: Logs showing blocked attempts (firewall, SIEM, EDR, email gateway)
   - **REQUIRED**: "Before" state showing vulnerability/exposure
   - **REQUIRED**: "After" state showing protection
   - **RECOMMENDED**: External validation (other sources confirming threat)
   - **RECOMMENDED**: Stakeholder communications (approvals, notifications)


4. **Validate the Prevention**:

   - How do you know attack would have succeeded?
   - What was the potential business impact?
   - Were there actual attack attempts after prevention?
   - Can prevention be independently verified?


5. **Document in Sheet 7**:

   - Complete all required columns
   - Attach evidence files
   - Calculate prevented incident value (optional but recommended)


**COLUMNS TO COMPLETE:**

| Column | Instructions | Example |
|--------|--------------|---------|
| **Prevention_ID** | Auto-generated | PREV-2026-Q1-001 |
| **Prevention_Date** | Date action taken | 15.01.2026 |
| **Quarter** | Auto-calculated | 2026-Q1 |
| **Intelligence_Source** | Source ID from A.5.7.1 or intelligence product ID | SRC-001 / PROD-20260115-01 |
| **Intelligence_Summary** | What intelligence was received? (max 500 chars) | Commercial TI feed reported APT28 actively exploiting CVE-2025-12345 |
| **Threat_Type** | Dropdown: Phishing, Malware, Exploit, Ransomware, etc. | Exploit |
| **IOCs_Deployed** | Comma-separated IOC IDs from Sheet 3 (if applicable) | IOC-001, IOC-005 |
| **VTL_Record** | VTL ID from A.5.7.2 Sheet 8 (if vulnerability-related) | VTL-20260115-0001 |
| **Preventive_Action** | What action was taken? (max 500 chars) | Emergency patching of 15 customer-facing servers within 48 hours |
| **Action_Date** | Date action completed | 17.01.2026 |
| **Action_Owner** | Who executed? | Infrastructure Team |
| **Approval_Authority** | Who approved emergency action? | CISO |
| **Systems_Protected** | Count or description | 15 servers, 3 web applications |
| **Attack_Attempts_Blocked** | Count if measurable | 7 exploit attempts detected post-patch (all failed) |
| **Potential_Impact_Prevented** | Dropdown: Critical, High, Medium, Low | Critical |
| **Business_Impact_Description** | What would have happened? | Customer PII database breach (500K records) |
| **Estimated_Cost_Avoided** | Optional currency value | CHF 2,000,000 |
| **Evidence_Location** | File path or link to evidence | /Evidence/2026-Q1/Prevention/PREV-001/ |
| **Validation_Method** | How was prevention verified? | Honeypot showed exploit attempts; patched servers resistant |
| **Confidence_Level** | Dropdown: High, Medium, Low | High |
| **Stakeholders_Informed** | Who was informed of prevention? | CISO, Board, Customer Success |
| **Lessons_Learned** | What was learned? | Emergency patch process effective; communication to customers critical |
| **Notes** | Free text | Intelligence from A.5.7.2 VTL triggered emergency response |

**VALIDATION CHECKLIST (before submitting prevented incident):**

- [ ] Intelligence source documented and verifiable
- [ ] Specific threat identified (not general advisory)
- [ ] Preventive action taken within reasonable timeframe
- [ ] Evidence collected showing blocked attempts or vulnerable state before/after
- [ ] Business impact assessed and justified
- [ ] Prevention independently verifiable
- [ ] Stakeholders informed
- [ ] Lessons learned documented


**QUARTERLY TARGET**: ≥3 prevented incidents per quarter

**If Target Not Met**:

- Document why (lack of actionable intelligence? lack of threats? detection gaps?)
- Review intelligence sources for actionability
- Assess security posture (are there other preventions not documented?)
- Create action items to improve prevention documentation


**Deliverable:** ≥3 validated prevented incidents per quarter with complete evidence

**Quality Check:**

- ✓ Each prevention has complete evidence package
- ✓ Business impact justified (not exaggerated, not minimized)
- ✓ Confidence level appropriate to evidence quality
- ✓ Quarterly target met (≥3)
- ✓ Lessons learned actionable


---

#### Phase 8: Feedback Collection (Ongoing)

**Objective:** Complete Sheet 8 - Feedback_Collection

**Steps:**
1. For each intelligence product distributed (from Sheet 6):

   - Solicit feedback from recipients (surveys, emails, conversations)
   - Document feedback received
   - Rate feedback: Positive, Neutral, Negative
   - Categorize feedback: Timeliness, Relevance, Actionability, Quality, Format
   - Document requested improvements
   - Track actions taken based on feedback

2. Calculate feedback metrics:

   - Response rate (% who provide feedback)
   - Satisfaction score
   - Actionability score
   - Timeliness score

3. Identify systemic issues from feedback patterns
4. Implement improvements based on feedback
5. Close the loop (inform stakeholders of improvements)

**Deliverable:** Running feedback log with improvement actions

**Quality Check:**

- ✓ Feedback solicited for all major distributions
- ✓ Response rate ≥30% (target)
- ✓ Negative feedback analyzed and addressed
- ✓ Improvements implemented and communicated


---

#### Phase 9: Integration Metrics (Monthly)

**Objective:** Complete Sheet 9 - Integration_Metrics

**Steps:**
1. Calculate monthly KPIs:

   - Tools integrated (count from Sheet 2)
   - IOCs deployed (count from Sheet 3)
   - IOC hit rate (% with detections)
   - Distribution reach (% stakeholders receiving intelligence)
   - Stakeholder engagement rate
   - **Prevention tracking**: Prevented incidents MTD/QTD (from Sheet 7)
   - Feedback response rate
   - Average distribution timeliness

2. Compare actual vs. target for each metric
3. Identify below-target metrics requiring attention
4. Update trends (month-over-month)

**Deliverable:** Complete integration metrics dashboard

**Quality Check:**

- ✓ All KPIs calculated accurately
- ✓ Targets from policy documented
- ✓ Below-target metrics have action items
- ✓ Prevention tracking current (Sheet 7 drives this metric)


---

#### Phase 10: SIEM Integration Details (Quarterly)

**Objective:** Complete Sheet 10 - SIEM_Integration_Details

**Steps:**
1. Document SIEM threat intelligence integration:

   - Correlation rules using TI
   - IOC lookups/enrichment
   - Threat feed integrations
   - Alert generation based on TI
   - Dashboard visualizations

2. For each TI-enabled SIEM capability:

   - Document rule/query name
   - Document TI source used
   - Track alert volume
   - Track true positive rate
   - Track MTTR (mean time to respond)

3. Assess SIEM integration maturity
4. Identify SIEM integration gaps

**Deliverable:** Complete SIEM integration deep-dive

**Quality Check:**

- ✓ All TI-enabled SIEM rules documented
- ✓ Alert volumes tracked
- ✓ True positive rates acceptable (≥70% target)
- ✓ Integration gaps identified with remediation plans


---

#### Phase 11: EDR Integration Details (Quarterly)

**Objective:** Complete Sheet 11 - EDR_Integration_Details

**Steps:**
1. Document EDR threat intelligence integration:

   - IOC deployment to endpoints
   - Custom detection rules based on TI
   - Behavioral detections using TTP intelligence
   - Threat hunting queries using TI
   - Automated response actions

2. For each TI-enabled EDR capability:

   - Document capability name
   - Document TI source used
   - Track detection volume
   - Track containment actions
   - Track false positive rate

3. Assess EDR integration maturity
4. Identify EDR integration gaps

**Deliverable:** Complete EDR integration deep-dive

**Quality Check:**

- ✓ All TI-enabled EDR capabilities documented
- ✓ Detection volumes tracked
- ✓ False positive rates acceptable (≤10% target)
- ✓ Integration gaps identified with remediation plans


---

#### Phase 12: Threat Hunting Campaigns (Ongoing)

**Objective:** Complete Sheet 12 - Threat_Hunting_Campaigns

**Steps:**
1. For each TI-driven threat hunt:

   - Assign unique Campaign_ID
   - Document hunt hypothesis (based on which intelligence?)
   - Document hunt methodology
   - Document hunt scope (systems searched)
   - Track hunt results (findings)
   - Document actions taken
   - Calculate hunt ROI (time invested vs. value of findings)

2. Link hunts to threat intelligence:

   - Which intelligence triggered hunt?
   - Which TTPs were hunted?
   - Which IOCs were searched?

3. Track hunt effectiveness metrics
4. Share hunt results with stakeholders

**Deliverable:** Complete threat hunting campaign tracker

**Quality Check:**

- ✓ All TI-driven hunts documented
- ✓ Hunt hypotheses clear and intelligence-based
- ✓ Results documented (even if nothing found)
- ✓ Lessons learned captured for future hunts


---

#### Phase 13: Risk Assessment Updates (Ongoing) - ⚠️ MANDATORY AUDIT EVIDENCE

**Objective:** Complete Sheet 13 - Risk_Assessment_Updates

**PURPOSE**: Document Clause 6.1 integration per **ISMS-POL-A.5.7, Section 2.4 (Risk Assessment Integration Requirements)**

**KPI TARGET**: ≥3 risk assessment updates per quarter

**ISO 27001 CLAUSE 6.1 REQUIREMENT**:
Organizations must regularly review and update their risk assessment based on changes in:

- Threat landscape
- Vulnerabilities discovered
- Business context changes
- Control effectiveness


**Threat intelligence is a PRIMARY INPUT to this process.**

**WHEN TO UPDATE RISK ASSESSMENT BASED ON TI:**

✅ **Trigger 1: New Threat Actor Targeting Organization's Sector**

- Intelligence: Threat actor profile (from A.5.7.2 Sheet 12) shows targeting of [Organization]'s sector
- Action: Update risk assessment to reflect new threat actor capability/motivation
- Example: APT group now targeting financial sector → increase likelihood ratings


✅ **Trigger 2: High-CVSS Vulnerability with Active Exploitation**

- Intelligence: VTL record (from A.5.7.2 Sheet 8) shows CVSS ≥8.0 with active exploitation
- Action: Update risk assessment for affected systems/data
- Example: CVE-2025-12345 (CVSS 9.3) actively exploited → increase risk rating for web servers


✅ **Trigger 3: Campaign Targeting Similar Organizations**

- Intelligence: Campaign tracking (from A.5.7.2 Sheet 13) shows attacks on similar organizations
- Action: Update risk assessment based on campaign TTPs and targets
- Example: Ransomware campaign targeting healthcare providers → reassess data backup risks


✅ **Trigger 4: Control Effectiveness Change**

- Intelligence: Prevention tracking (from A.5.7.3 Sheet 7) demonstrates control effectiveness
- Action: Update risk assessment to reflect improved control effectiveness
- Example: 5 incidents prevented by TI → reduce likelihood ratings


✅ **Trigger 5: Intelligence-Driven Decision Implementation**

- Intelligence: Business decision (from Sheet 15) implements new security control
- Action: Update risk assessment to reflect new control
- Example: Cloud security posture management deployed → reduce cloud misconfig risks


**STEPS TO DOCUMENT RISK ASSESSMENT UPDATE:**

1. **Identify the Intelligence Trigger**:

   - What threat intelligence prompted the risk update?
   - Reference source (A.5.7.1 source, A.5.7.2 VTL/actor/campaign, A.5.7.3 prevention)
   - Intelligence date
   - Intelligence summary


2. **Identify the Risk(s) Affected**:

   - Which risk(s) in the risk register are impacted?
   - Risk ID and description
   - Previous risk rating (Likelihood × Impact)


3. **Assess the Change**:

   - What changed? (Likelihood? Impact? Control effectiveness?)
   - Why did it change? (new threat? new vulnerability? new control?)
   - Direction of change (Increased risk? Decreased risk?)


4. **Calculate New Risk Rating**:

   - New likelihood rating (1-5)
   - New impact rating (1-5)
   - New risk score (Likelihood × Impact)
   - Risk level (Critical: 20-25, High: 15-19, Medium: 8-14, Low: 1-7)


5. **Document Treatment Decision**:

   - Treat (implement new controls)
   - Tolerate (accept the risk)
   - Transfer (insurance, outsourcing)
   - Terminate (eliminate the activity)


6. **Obtain Approval**:

   - Risk Owner approval
   - CISO approval
   - Executive approval (if Critical risk)


7. **Update Risk Register**:

   - Update official risk register in risk management system
   - Document intelligence source in risk register notes
   - Link to this assessment (Sheet 13 record)


**COLUMNS TO COMPLETE:**

| Column | Instructions | Example |
|--------|--------------|---------|
| **Update_ID** | Auto-generated | RISK-UPD-2026-001 |
| **Update_Date** | Date assessment updated | 18.01.2026 |
| **Quarter** | Auto-calculated | 2026-Q1 |
| **Intelligence_Source** | What intelligence triggered update? | VTL-20260115-0001 (CVE-2025-12345 active exploitation) |
| **Intelligence_Summary** | Brief description (max 300 chars) | CVSS 9.3 vulnerability in web app framework, mass exploitation by APT28 |
| **Risk_ID** | Risk register ID | RISK-2024-015 |
| **Risk_Description** | What risk was updated? | Web application compromise leading to customer data breach |
| **Previous_Likelihood** | 1-5 scale | 2 (Unlikely) |
| **Previous_Impact** | 1-5 scale | 5 (Critical) |
| **Previous_Risk_Score** | Likelihood × Impact | 10 (Medium) |
| **Change_Type** | Dropdown: Likelihood_Increase, Impact_Increase, Both_Increase, Likelihood_Decrease, Impact_Decrease, Both_Decrease | Likelihood_Increase |
| **Change_Rationale** | Why did risk change? | Active exploitation increases likelihood from "Unlikely" to "Likely" |
| **New_Likelihood** | 1-5 scale | 4 (Likely) |
| **New_Impact** | 1-5 scale | 5 (Critical) |
| **New_Risk_Score** | Likelihood × Impact | 20 (Critical) |
| **New_Risk_Level** | Auto-calculated | Critical |
| **Treatment_Decision** | Dropdown: Treat, Tolerate, Transfer, Terminate | Treat |
| **Treatment_Actions** | What will be done? | Emergency patching within 48 hours |
| **Action_Owner** | Who is responsible? | Infrastructure Team Lead |
| **Target_Completion** | Date | 20.01.2026 |
| **Risk_Owner_Approval** | Name/signature | Jane Smith, IT Manager |
| **CISO_Approval** | Name/signature | John Doe, CISO |
| **Executive_Approval** | Name/signature (if Critical risk) | Sarah Johnson, CTO |
| **Risk_Register_Updated** | Checkbox: Yes/No | Yes |
| **Evidence_Location** | Link to intelligence and risk register entry | /Risk/2026/RISK-UPD-2026-001/ |
| **Notes** | Free text | Updated in risk management system, treatment plan approved by exec |

**QUARTERLY TARGET**: ≥3 risk assessment updates per quarter

**If Target Not Met**:

- Review: Is threat intelligence informing risk management?
- Check: Are intelligence teams and risk management teams communicating?
- Assess: Are intelligence findings being escalated appropriately?
- Action: Establish formal intelligence → risk management workflow


**Deliverable:** ≥3 documented risk assessment updates per quarter with evidence of risk register updates

**Quality Check:**

- ✓ Intelligence trigger clearly documented
- ✓ Risk rating calculations correct
- ✓ Treatment decisions appropriate to risk level
- ✓ Approvals obtained (Risk Owner, CISO, Executive if Critical)
- ✓ Risk register actually updated (not just Sheet 13)
- ✓ Quarterly target met (≥3)
- ✓ Evidence collected (before/after risk ratings, approvals)


---

#### Phase 14: Incident-TI Integration Tracking (Ongoing) - ⚠️ MANDATORY AUDIT EVIDENCE

**Objective:** Complete Sheet 14 - Incident_TI_Integration

**PURPOSE**: Track TI usage in incident response per **ISMS-POL-A.5.7, Section 2.5 (Incident Management Integration Requirements)**

**KPI TARGET**: ≥70% of P1/P2 incidents use threat intelligence

**ISO 27001 CONTROLS A.5.24-5.28 REQUIREMENTS**:

- A.5.24: Incident response planning
- A.5.25: Assessment and decision on information security events
- A.5.26: Response to information security incidents
- A.5.27: Learning from information security incidents
- A.5.28: Collection of evidence


**Threat intelligence must be integrated into incident response process.**

**WHEN TO DOCUMENT INCIDENT-TI INTEGRATION:**

Document for EVERY P1 (Critical) and P2 (High) incident. Optional for P3/P4.

**WHAT QUALIFIES AS "THREAT INTELLIGENCE USE":**

✅ **Example 1: IOC Correlation**

- Incident: Suspicious network connection detected
- TI Usage: IOC matched from threat feed (IOC-2026-001)
- Outcome: Confirmed malicious, isolated system
- **Qualifies**: Yes - TI enabled detection and rapid response


✅ **Example 2: TTP Identification**

- Incident: Ransomware encryption detected
- TI Usage: Attack patterns matched known ransomware group from threat actor profile
- Outcome: Identified RansomX group, knew decryption impossible, paid ransom avoided
- **Qualifies**: Yes - TI informed response strategy


✅ **Example 3: Intelligence-Driven Hunting**

- Incident: Compromised credential discovered
- TI Usage: Threat hunt using campaign intelligence found lateral movement
- Outcome: Contained before data exfiltration
- **Qualifies**: Yes - TI drove proactive discovery


✅ **Example 4: Attribution and Strategy**

- Incident: Targeted phishing campaign
- TI Usage: Attribution to known APT group, understood objectives
- Outcome: Informed communication strategy and law enforcement engagement
- **Qualifies**: Yes - TI shaped response approach


❌ **Non-Example 1: TI Consulted But Not Used**

- Incident: Malware outbreak
- TI Usage: Checked threat feeds, no relevant intelligence
- Outcome: Responded using standard playbook
- **Does NOT Qualify**: TI was available but didn't inform response


❌ **Non-Example 2: Post-Incident Only**

- Incident: Data breach discovered
- TI Usage: Post-mortem analysis using TI
- Outcome: TI used for lessons learned only
- **Does NOT Qualify**: TI not used during active response


**STEPS TO DOCUMENT INCIDENT-TI INTEGRATION:**

1. **Identify the Incident**:

   - Incident ID from incident management system
   - Incident classification (P1, P2, P3, P4)
   - Incident date and detection time
   - Incident summary


2. **Document TI Usage**:

   - HOW was threat intelligence used?
   - WHEN in the incident lifecycle? (Detection, Analysis, Containment, Eradication, Recovery)
   - WHICH intelligence? (IOC ID, VTL ID, threat actor profile, campaign)
   - WHO used the intelligence? (SOC analyst, IR lead, etc.)


3. **Assess TI Effectiveness**:

   - Did TI improve incident response?
   - Time saved by using TI?
   - Better decisions made because of TI?
   - What would have been different without TI?


4. **Document Outcome**:

   - Incident resolution
   - Response time metrics
   - Business impact
   - Lessons learned


5. **Calculate Metrics**:

   - % of P1/P2 incidents using TI (target: ≥70%)
   - Average MTTR (Mean Time To Respond) for TI-informed vs. non-TI incidents
   - TI effectiveness rating


**COLUMNS TO COMPLETE:**

| Column | Instructions | Example |
|--------|--------------|---------|
| **Incident_ID** | From incident management system | INC-2026-001 |
| **Incident_Date** | Date incident detected | 20.01.2026 |
| **Incident_Classification** | Dropdown: P1-Critical, P2-High, P3-Medium, P4-Low | P1-Critical |
| **Incident_Type** | Dropdown: Malware, Phishing, Data_Breach, Ransomware, etc. | Ransomware |
| **Incident_Summary** | Brief description (max 300 chars) | Ransomware encryption detected on file server, 500 files encrypted |
| **Detection_Time** | DateTime | 20.01.2026 03:15 |
| **TI_Used** | Dropdown: Yes, No, Partial | Yes |
| **TI_Usage_Phase** | When was TI used? Dropdown: Detection, Analysis, Containment, Eradication, Recovery, Multiple | Multiple |
| **TI_Source** | Which intelligence? | ACTOR-005 (RansomX threat actor profile), CAMP-003 (RansomX campaign) |
| **TI_Usage_Description** | HOW was TI used? (max 500 chars) | Matched attack patterns to RansomX group from actor profile. Campaign intel showed group never provides working decryptors. Informed decision to restore from backups rather than negotiate. |
| **TI_User** | Who used the intelligence? | Senior IR Analyst |
| **TI_Effectiveness** | Dropdown: High, Medium, Low, None | High |
| **TI_Impact_Description** | What difference did TI make? | Saved estimated CHF 50K ransom payment, reduced recovery time by avoiding negotiation |
| **Time_To_Detection** | Minutes from start of attack | 45 |
| **Time_To_Containment** | Minutes from detection to containment | 30 |
| **Time_To_Resolution** | Hours from detection to full resolution | 8 |
| **MTTR** | Mean Time To Respond (auto-calculated or manual) | 8 hours |
| **Business_Impact** | Dropdown: Critical, High, Medium, Low, None | Medium |
| **Business_Impact_Description** | What was the business impact? | 8 hours of file server downtime, 500 files restored from backup |
| **Estimated_Cost** | Optional currency value | CHF 25,000 (staff time + downtime) |
| **Cost_Avoided_By_TI** | Optional currency value | CHF 50,000 (ransom not paid) |
| **Lessons_Learned** | What was learned? | Campaign intelligence proved valuable for ransom decision-making |
| **TI_Gaps_Identified** | Were there intelligence gaps? | None - good coverage for this threat |
| **Action_Items** | Follow-up actions | Update IR playbook with RansomX-specific guidance |
| **Notes** | Free text | Excellent use of TI by IR team, case study for training |

**QUARTERLY TARGET**: ≥70% of P1/P2 incidents use threat intelligence

**Calculation:**
```
TI Usage Rate = (P1/P2 Incidents with TI_Used="Yes") / (Total P1/P2 Incidents) × 100%
```

**If Target Not Met**:

- Review: Is threat intelligence accessible to incident responders?
- Check: Are IR playbooks integrated with TI workflows?
- Assess: Do IR analysts know how to access/use TI?
- Train: Conduct TI-for-IR training sessions
- Action: Establish formal TI → IR integration workflow


**Deliverable:** Documented TI usage for all P1/P2 incidents, ≥70% showing TI usage

**Quality Check:**

- ✓ All P1/P2 incidents documented
- ✓ TI usage accurately described (not exaggerated)
- ✓ TI effectiveness honestly assessed
- ✓ Quarterly target met (≥70%)
- ✓ Gaps identified when TI not used
- ✓ Evidence collected (incident records, TI references)


---

#### Phase 15: Intelligence-Driven Decisions (Ongoing) - ⚠️ MANDATORY AUDIT EVIDENCE

**Objective:** Complete Sheet 15 - Intelligence_Driven_Decisions

**PURPOSE**: Document business decisions based on TI per **ISMS-POL-A.5.7, Section 2.7 (Effectiveness Measurement Requirements)**

**KPI TARGET**: ≥5 documented intelligence-driven decisions per quarter

**WHAT QUALIFIES AS "INTELLIGENCE-DRIVEN DECISION":**

A decision where:
1. Threat intelligence was a PRIMARY INPUT (not just background context)
2. A business or strategic decision was made
3. The decision had resource or operational implications
4. Executive or senior management was involved

**EXAMPLES OF INTELLIGENCE-DRIVEN DECISIONS:**

✅ **Example 1: Security Tool Acquisition**

- Intelligence: Multiple threat campaigns exploiting lack of EDR visibility
- Decision: Approved CHF 150K budget for EDR deployment
- Approver: CTO
- **Qualifies**: Yes - strategic security investment driven by threat landscape


✅ **Example 2: Cloud Security Posture Change**

- Intelligence: Nation-state actor targeting cloud misconfigurations in sector
- Decision: Accelerated cloud security posture management (CSPM) implementation
- Approver: CISO + VP Engineering
- **Qualifies**: Yes - architectural decision based on specific threat intelligence


✅ **Example 3: Geographic Expansion Pause**

- Intelligence: Active cyber operations in target expansion region
- Decision: Delayed market expansion by 6 months until threat subsides
- Approver: CEO + Board
- **Qualifies**: Yes - business strategy decision based on geopolitical threat intelligence


✅ **Example 4: Vendor Security Requirements**

- Intelligence: Supply chain attacks increasing, targeting specific vendor types
- Decision: New vendor security assessment requirements implemented
- Approver: CISO + Procurement VP
- **Qualifies**: Yes - policy decision based on threat trend


✅ **Example 5: Incident Response Process Change**

- Intelligence: Ransomware group never provides working decryptors (from A.5.7.2)
- Decision: Updated IR playbook - never negotiate, always restore from backup
- Approver: CISO
- **Qualifies**: Yes - operational policy change based on threat actor intelligence


❌ **Non-Example 1: Routine Security Hygiene**

- Intelligence: General phishing threats increasing
- Decision: Conducted security awareness training (already scheduled)
- **Does NOT Qualify**: Routine activity, not a strategic decision


❌ **Non-Example 2: TI-Informed But Not TI-Driven**

- Intelligence: Threat landscape reviewed during annual planning
- Decision: Maintained existing security budget
- **Does NOT Qualify**: TI was context, not primary driver


**STEPS TO DOCUMENT INTELLIGENCE-DRIVEN DECISION:**

1. **Identify the Intelligence**:

   - What specific threat intelligence informed the decision?
   - Source(s) of intelligence
   - Intelligence date and summary
   - Why was this intelligence significant?


2. **Document the Decision**:

   - What decision was made?
   - Who made the decision? (Decision-maker name and role)
   - When was the decision made?
   - What was the decision rationale?


3. **Assess Decision Impact**:

   - What resources were committed? (budget, staff, time)
   - What operational changes resulted?
   - What risk reduction was achieved?
   - What business value was created?


4. **Track Implementation**:

   - Decision implementation status
   - Implementation timeline
   - Responsible party
   - Verification of completion


5. **Measure Outcomes**:

   - Was the decision effective?
   - Lessons learned
   - Would make same decision again?


**COLUMNS TO COMPLETE:**

| Column | Instructions | Example |
|--------|--------------|---------|
| **Decision_ID** | Auto-generated | DEC-2026-001 |
| **Decision_Date** | Date decision made | 25.01.2026 |
| **Quarter** | Auto-calculated | 2026-Q1 |
| **Intelligence_Source** | What intelligence informed decision? | ACTOR-005, CAMP-003, Industry ISAC Report Q4-2025 |
| **Intelligence_Summary** | Brief summary (max 500 chars) | Ransomware group RansomX targeting financial sector, 15 organizations compromised Q4-2025. Backups primary target. No working decryptors ever provided despite ransom payment. |
| **Intelligence_Significance** | Why was this intelligence important? | Direct threat to [Organization] as financial services provider, backup strategy at risk |
| **Decision_Category** | Dropdown: Security_Investment, Policy_Change, Process_Change, Architecture_Change, Business_Strategy, Vendor_Management, Other | Security_Investment |
| **Decision_Description** | What was decided? (max 500 chars) | Approved CHF 100K for immutable backup solution deployment to protect against ransomware targeting backups |
| **Decision_Maker** | Name and role | Sarah Johnson, CTO |
| **Decision_Approvers** | Additional approvers if any | CISO, CFO |
| **Decision_Rationale** | Why was this decision made? (max 500 chars) | Intelligence showed RansomX specifically targeting backups. Current backup solution vulnerable. Immutable backups provide protection against this tactic. ROI justified by CHF 50K average ransom demand. |
| **Resources_Committed** | Budget, staff time, etc. | CHF 100K budget, 2 weeks infrastructure team time |
| **Implementation_Status** | Dropdown: Approved, In_Progress, Completed, Cancelled, Delayed | In_Progress |
| **Implementation_Owner** | Who is implementing? | Infrastructure Team Lead |
| **Implementation_Target** | Target completion date | 28.02.2026 |
| **Implementation_Actual** | Actual completion date | [blank] |
| **Risk_Reduction** | Dropdown: High, Medium, Low | High |
| **Risk_Reduction_Description** | What risk was reduced? | Eliminated backup compromise risk, ensured recovery capability against ransomware |
| **Business_Value** | What business value was created? | Ransomware resilience, regulatory compliance (backup requirements), customer confidence |
| **Estimated_Cost_Benefit** | Optional ROI calculation | Investment: CHF 100K, Potential loss avoided: CHF 500K (ransom + downtime), ROI: 5:1 |
| **Lessons_Learned** | What was learned? | Threat intelligence highly effective for security investment justification |
| **Would_Repeat** | Dropdown: Yes, No, Maybe | Yes |
| **Stakeholders_Informed** | Who was informed of decision? | Board, Executive Team, All Staff (via townhall) |
| **Evidence_Location** | Link to decision documentation | /Decisions/2026-Q1/DEC-2026-001/ |
| **Notes** | Free text | Excellent example of TI driving security strategy, used in board presentation |

**QUARTERLY TARGET**: ≥5 documented intelligence-driven decisions per quarter

**If Target Not Met**:

- Review: Is threat intelligence reaching decision-makers?
- Check: Are executive briefings including actionable intelligence?
- Assess: Are intelligence findings translated to business language?
- Train: Educate executives on interpreting threat intelligence
- Action: Establish formal TI → executive decision-making workflow


**Deliverable:** ≥5 documented intelligence-driven decisions per quarter with evidence of decision records

**Quality Check:**

- ✓ Intelligence clearly identified and significant
- ✓ Decision genuinely intelligence-driven (not routine)
- ✓ Executive/senior management involved
- ✓ Resource implications documented
- ✓ Implementation tracked
- ✓ Quarterly target met (≥5)
- ✓ Evidence collected (meeting minutes, approvals, budget docs)


---

#### Phase 16: Review & Approval (1-2 hours)

**Objective:** Obtain three-level approval for assessment

**Approval Workflow:**

**Level 1: Security Operations Manager**

- Reviews assessment for completeness and accuracy
- Verifies tool integration documentation accurate
- Confirms IOC deployment tracking current
- Confirms stakeholder registry complete
- **CRITICAL**: Verifies Sheets 7, 13, 14, 15 meet quarterly targets
- Signs off on operational accuracy


**Level 2: CISO**

- Reviews assessment for policy compliance
- Verifies integration metrics meet targets
- **CRITICAL**: Reviews prevention tracking (Sheet 7) - ≥3 per quarter
- **CRITICAL**: Reviews risk assessment updates (Sheet 13) - ≥3 per quarter, Clause 6.1
- **CRITICAL**: Reviews incident-TI integration (Sheet 14) - ≥70% P1/P2
- **CRITICAL**: Reviews intelligence-driven decisions (Sheet 15) - ≥5 per quarter
- Reviews high-impact action items
- Signs off on strategic approval


**Level 3: Executive Management (if required)**

- Required if major integration gaps identified requiring investment
- Required if quarterly KPI targets not met
- Reviews intelligence-driven decisions (Sheet 15 should include some executive decisions)
- Approves resources for integration improvements
- Signs off on executive approval


**Deliverable:** Fully approved assessment workbook with all MANDATORY audit evidence

---

**END OF PART I: USER COMPLETION GUIDE**

---

# PART II: TECHNICAL SPECIFICATION

## Excel Workbook Structure

### Workbook Properties

**File Name:** `ISMS_A_5_7_3_Integration_Distribution_Assessment_YYYYMMDD.xlsx`

**Example:** `ISMS_A_5_7_3_Integration_Distribution_Assessment_20260121.xlsx`

**Workbook Settings:**

- Format: Excel 2016+ (.xlsx)
- Calculation: Automatic
- Protection: Sheets protected (only yellow cells editable)
- Macros: None (VBA-free for security)
- External Links: References to A.5.7.1 sources, A.5.7.2 intelligence products


**Total Sheets:** 15

**Tab Colors:**

- Instructions: Blue (#4472C4)
- Integration (Sheets 2-3): Yellow (#FFD966)
- Dissemination (Sheets 4-6): Orange (#FFA500)
- **Prevention Tracking (Sheet 7): Red (#C00000) - AUDIT CRITICAL**
- Feedback & Metrics (Sheets 8-9): Green (#70AD47)
- Tool Details (Sheets 10-11): Teal (#00B0F0)
- Hunting (Sheet 12): Purple (#7030A0)
- **Risk/Incident/Decisions (Sheets 13-15): Red (#C00000) - AUDIT CRITICAL**
- Metadata: Gray (#D9D9D9)


**CRITICAL AUDIT EVIDENCE SHEETS:**

- **Sheet 7: Prevention_Tracking** - ≥3 prevented incidents per quarter
- **Sheet 13: Risk_Assessment_Updates** - ≥3 risk updates per quarter (ISO 27001 Clause 6.1)
- **Sheet 14: Incident_TI_Integration** - ≥70% P1/P2 incidents use TI (Controls A.5.24-5.28)
- **Sheet 15: Intelligence_Driven_Decisions** - ≥5 decisions per quarter


---

## Sheet-by-Sheet Technical Specifications

# Sheet Specifications

## Sheet 2: Tool_Integration_Matrix

**Purpose**: Document TI integration across security stack

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Tool_ID | Text | Auto-generated (TOOL-NNN) | Yes | TOOL-001 |
| Tool_Category | Dropdown | SIEM, EDR, Firewall, Proxy, Email_Gateway, IDS_IPS, TIP, SOAR, Vuln_Scanner, Other | Yes | SIEM |
| Tool_Name | Text | Free text | Yes | Splunk Enterprise Security |
| Vendor | Text | Free text | Yes | Splunk Inc. |
| Version | Text | Free text | No | 7.2.1 |
| Primary_Owner | Text | Email or team | Yes | SOC Team |
| Integration_Status | Dropdown | Fully_Integrated, Partially_Integrated, Planned, Not_Integrated | Yes | Fully_Integrated |
| Integration_Method | Dropdown | API, Feed, Manual_Import, STIX_TAXII, Syslog, Custom_Script | Yes | API |
| Integration_Direction | Dropdown | Inbound, Outbound, Bidirectional | Yes | Inbound |
| Data_Types_Integrated | Text | Comma-separated: IOCs, TTPs, Reports, Alerts, Context | Yes | IOCs, TTPs, Context |
| Automation_Level | Dropdown | Fully_Automated, Semi_Automated, Manual | Yes | Fully_Automated |
| Update_Frequency | Dropdown | Real-time, Hourly, Daily, Weekly, On_Demand | Yes | Real-time |
| IOC_Types_Supported | Text | Comma-separated: IP, Domain, URL, Hash, Email, Registry, Mutex | Yes | IP, Domain, URL, Hash |
| Last_Successful_Sync | DateTime | DD.MM.YYYY HH:MM | No | 02.01.2025 14:30 |
| Sync_Errors_Last_30_Days | Number | Integer >= 0 | No | 2 |
| False_Positive_Rate | Dropdown | High, Medium, Low, Unknown | No | Low |
| Effectiveness_Rating | Dropdown | Excellent, Good, Fair, Poor | No | Excellent |
| Integration_Challenges | Text | Free text | No | Rate limiting on API calls |
| Improvement_Opportunities | Text | Free text | No | Add TTP mapping to correlation rules |
| Integration_Date | Date | DD.MM.YYYY | No | 15.06.2024 |
| Documentation_Link | Text | Hyperlink | No | https://docs.example.com/siem-ti |
| Notes | Text | Free text | No | Primary IOC ingestion point |

**Integration Maturity Levels**:

Fully_Integrated:

- Automated data flow
- No manual intervention
- Error handling in place
- Documented and monitored


Partially_Integrated:

- Some automation
- Requires manual steps
- Limited error handling
- Basic documentation


Planned:

- Requirements defined
- Resources allocated
- Timeline established


Not_Integrated:

- No integration
- May be future consideration



**Conditional Formatting**:

- Integration_Status "Fully_Integrated" → Green
- Integration_Status "Not_Integrated" → Red
- Sync_Errors > 5 → Yellow background
- Effectiveness_Rating "Poor" → Red text


---

## Sheet 3: IOC_Deployment

**Purpose**: Track IOC deployment and detection effectiveness

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| IOC_ID | Text | Auto-generated (IOC-YYYY-NNN) | Yes | IOC-2025-001 |
| IOC_Type | Dropdown | From common_enums.IOCType | Yes | IP Address |
| IOC_Value | Text | Format validation by type | Yes | 192.0.2.100 |
| Intelligence_Source | Dropdown | From 5.7.1.Source_Inventory | Yes | SRC-2025-001 |
| Related_Product_ID | Dropdown | From 5.7.2.Intelligence_Production | No | PROD-2025-015 |
| Threat_Actor | Text | Free text | No | APT28 |
| Associated_Malware | Text | Free text | No | Cobalt Strike |
| MITRE_Technique | Dropdown | From common_enums | No | T1071 - Application Layer Protocol |
| Confidence_Level | Dropdown | High, Medium, Low | Yes | High |
| Severity | Dropdown | Critical, High, Medium, Low, Info | Yes | High |
| TLP_Classification | Dropdown | TLP:CLEAR, GREEN, AMBER, AMBER+STRICT, RED | Yes | TLP:AMBER |
| Deployment_Date | Date | DD.MM.YYYY | Yes | 02.01.2025 |
| Deployed_To_Tools | Text | Comma-separated Tool_IDs | Yes | TOOL-001, TOOL-003 |
| Deployment_Method | Dropdown | Automated, Manual, Hybrid | Yes | Automated |
| Expiration_Date | Date | DD.MM.YYYY | No | 02.04.2025 |
| Status | Dropdown | Active, Expired, Withdrawn, Under_Review | Yes | Active |
| Hits_Last_7_Days | Number | Integer >= 0 | No | 0 |
| Hits_Last_30_Days | Number | Integer >= 0 | No | 3 |
| Hits_Total | Number | Integer >= 0 | No | 12 |
| Last_Hit_Date | Date | DD.MM.YYYY | No | 28.12.2024 |
| False_Positive | Dropdown | Yes, No, Under_Investigation | No | No |
| FP_Investigation_Notes | Text | If FP=Yes or Under_Investigation | Conditional | N/A |
| Action_Taken_On_Hit | Dropdown | Alert, Block, Log_Only, Escalate | No | Block |
| Related_Incidents | Text | Comma-separated incident IDs | No | INC-2024-089 |
| Effectiveness_Rating | Formula | Based on hits, FP rate, incidents | Auto | Effective |
| Notes | Text | Free text | No | Associated with known C2 infrastructure |

**Effectiveness Calculation**:

IF Hits_Total > 0 AND False_Positive = No: "Effective"
ELSE IF Hits_Total > 0 AND False_Positive = Yes: "Ineffective"
ELSE IF Hits_Total = 0 AND Days_Deployed > 30: "Ineffective"
ELSE: "Monitoring"


**IOC Lifecycle Management** (calculated fields):

- Days since deployment
- Days until expiration
- Hit rate (hits per day)
- FP rate (FP hits / total hits)


**Conditional Formatting**:

- Status "Active" + Expiration within 7 days → Orange
- Status "Expired" → Gray background
- False_Positive "Yes" → Red background
- Hits_Last_7_Days > 0 → Green highlight
- Effectiveness_Rating "Ineffective" → Red text


---

## Sheet 4: Dissemination_Channels

**Purpose**: Document intelligence distribution methods

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Channel_ID | Text | Auto-generated (CHAN-NNN) | Yes | CHAN-001 |
| Channel_Name | Text | Free text | Yes | TI Weekly Email |
| Channel_Type | Dropdown | Email_List, Portal, Dashboard, API, Briefing, Chat, Ticketing_System | Yes | Email_List |
| Target_Audience | Dropdown | Executive, CISO, SOC, IR_Team, IT_Ops, Developers, All_Staff | Yes | SOC |
| Intelligence_Types | Text | Comma-separated: Strategic, Tactical, Operational, Technical | Yes | Tactical, Technical |
| Delivery_Frequency | Dropdown | Real-time, Daily, Weekly, Monthly, Ad_Hoc | Yes | Weekly |
| Automation_Level | Dropdown | Fully_Automated, Semi_Automated, Manual | Yes | Semi_Automated |
| Distribution_Method | Text | Free text | Yes | Email via Marketing Platform |
| TLP_Max_Allowed | Dropdown | TLP:CLEAR, GREEN, AMBER, RED | Yes | TLP:AMBER |
| Active_Status | Dropdown | Active, Suspended, Deprecated | Yes | Active |
| Subscriber_Count | Number | Integer >= 0 | No | 45 |
| Average_Open_Rate | Number | Percentage 0-100 | No | 78 |
| Average_Engagement_Score | Number | 1-5 scale | No | 4.2 |
| Channel_Owner | Text | Email | Yes | ti.team@example.com |
| Technical_Platform | Text | Free text | No | Microsoft Exchange + Power Automate |
| Launch_Date | Date | DD.MM.YYYY | No | 01.01.2024 |
| Last_Distribution | Date | DD.MM.YYYY | No | 02.01.2025 |
| Effectiveness_Rating | Dropdown | Excellent, Good, Fair, Poor | No | Excellent |
| Improvement_Opportunities | Text | Free text | No | Add interactive threat dashboard |
| Notes | Text | Free text | No | Primary dissemination channel for SOC |

**Conditional Formatting**:

- Active_Status "Deprecated" → Gray
- Average_Engagement_Score < 3 → Yellow background
- Effectiveness_Rating "Poor" → Red text
- Average_Open_Rate > 75 → Green highlight


---

## Sheet 5: Stakeholder_Registry

**Purpose**: Manage intelligence consumer database

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Stakeholder_ID | Text | Auto-generated (STK-NNN) | Yes | STK-001 |
| Name | Text | Free text | Yes | John Security |
| Email | Text | Email format | Yes | john.security@example.com |
| Department | Dropdown | Executive, IT, Security, Operations, Legal, Compliance, Other | Yes | Security |
| Role | Text | Free text | Yes | SOC Analyst |
| TLP_Clearance | Dropdown | TLP:CLEAR, GREEN, AMBER, RED | Yes | TLP:AMBER |
| Intelligence_Interests | Text | Comma-separated: Threat_Actors, Vulnerabilities, Malware, Industry_Trends, Tactics | Yes | Threat_Actors, Malware |
| Preferred_Channels | Text | Comma-separated Channel_IDs | Yes | CHAN-001, CHAN-003 |
| Engagement_Level | Dropdown | High, Medium, Low, Inactive | No | High |
| Average_Feedback_Rating | Number | 1-5 scale (auto-calc) | Auto | 4.5 |
| Last_Engagement_Date | Date | DD.MM.YYYY (auto-calc) | Auto | 02.01.2025 |
| Onboarding_Date | Date | DD.MM.YYYY | Yes | 15.03.2024 |
| Status | Dropdown | Active, On_Leave, Departed | Yes | Active |
| Contact_Preference | Dropdown | Email, Slack, Teams, Portal | No | Email |
| Time_Zone | Text | Standard TZ | No | Europe/Zurich |
| Language_Preference | Dropdown | English, German, French | No | English |
| Notes | Text | Free text | No | Key stakeholder for ransomware intelligence |

**Conditional Formatting**:

- Status "Departed" → Gray background
- Engagement_Level "Inactive" → Yellow
- Average_Feedback_Rating >= 4.5 → Green highlight


---

## Sheet 6: Distribution_Tracking

**Purpose**: Track intelligence distribution and engagement

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Distribution_ID | Text | Auto-generated (DIST-YYYY-NNN) | Yes | DIST-2025-001 |
| Product_ID | Dropdown | From 5.7.2.Intelligence_Production | Yes | PROD-2025-015 |
| Product_Title | Formula | =VLOOKUP | Auto | APT28 Campaign Analysis |
| Intelligence_Type | Formula | =VLOOKUP | Auto | Tactical |
| Distribution_Date | DateTime | DD.MM.YYYY HH:MM | Yes | 02.01.2025 14:00 |
| Channel_ID | Dropdown | From Dissemination_Channels | Yes | CHAN-001 |
| Channel_Name | Formula | =VLOOKUP | Auto | TI Weekly Email |
| Stakeholder_ID | Dropdown | From Stakeholder_Registry | Yes | STK-001 |
| Stakeholder_Name | Formula | =VLOOKUP | Auto | John Security |
| TLP_Classification | Dropdown | TLP:CLEAR, GREEN, AMBER, RED | Yes | TLP:AMBER |
| Delivery_Method | Text | Free text | Yes | Email |
| Delivery_Status | Dropdown | Sent, Delivered, Opened, Failed, Bounced | Yes | Opened |
| Open_Date | DateTime | DD.MM.YYYY HH:MM | No | 02.01.2025 14:15 |
| Click_Through | Dropdown | Yes, No | No | Yes |
| Action_Taken | Dropdown | Yes, No, Unknown | No | Yes |
| Action_Description | Text | Free text | Conditional | Deployed IOCs to SIEM |
| Feedback_Received | Dropdown | Yes, No, Pending | No | Yes |
| Feedback_ID | Text | Link to Feedback_Collection | Conditional | FB-2025-001 |
| Engagement_Score | Formula | Based on open, click, action | Auto | High |
| Distribution_Effectiveness | Formula | Auto-calc | Auto | Effective |
| Follow_Up_Required | Dropdown | Yes, No | No | No |
| Follow_Up_Notes | Text | Conditional | Conditional | N/A |
| Notes | Text | Free text | No | Stakeholder requested similar analysis for APT29 |

**Effectiveness Calculation**:

IF Action_Taken = Yes AND Feedback_Received = Yes: "Highly_Effective"
ELSE IF Action_Taken = Yes: "Effective"
ELSE IF Opened = Yes: "Delivered_But_No_Action"
ELSE: "Not_Engaged"


**Conditional Formatting**:

- Delivery_Status "Failed" or "Bounced" → Red
- Action_Taken "Yes" → Green highlight
- Engagement_Score "High" → Green
- Engagement_Score "Low" → Yellow


---
## Sheet 7: Prevention_Tracking ⚠️ **CRITICAL AUDIT EVIDENCE**

**Purpose**: Document prevented incidents per ISMS-POL-A.5.7, Section 2.7 (Effectiveness Measurement Requirements)

**KPI Target**: ≥3 validated prevented incidents per quarter

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Prevention_ID | Text | Auto-generated (PREV-YYYYQQ-NNN) | Yes | PREV-2025Q1-001 |
| Quarter | Text | YYYY-QQ format | Yes | 2025-Q1 |
| Detection_Date | Date | DD.MM.YYYY | Yes | 15.01.2025 |
| CVE_ID | Text | CVE-YYYY-NNNNN format | Yes | CVE-2024-56789 |
| CVSS_Version | Dropdown | 4.0, 3.1 | Yes | 4.0 |
| CVSS_Base_Score | Number | 0.0-10.0, 1 decimal | Yes | 9.3 |
| CVSS_Vector | Text | Max 200 chars | Yes | CVSS:4.0/AV:N/AC:L/PR:N/UI:N/S:C/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H |
| Threat_Source | Text | Source_ID or free text | Yes | CISA KEV, SRC-2025-001 |
| Threat_Report_ID | Text | TI-YYYY-NNN format | Yes | TI-2025-003 |
| Exploitation_Status | Dropdown | PoC Available, Active, Mass Exploitation | Yes | Mass Exploitation |
| Before_State | Text | Max 500 chars | Yes | Vulnerability present on 12 web servers |
| Before_Evidence | Text | File path or reference | Yes | Scan-20250115-WebServers.xlsx |
| TI_Alert_Date | Date | DD.MM.YYYY | Yes | 15.01.2025 |
| TI_Alert_Details | Text | Max 500 chars | Yes | CISA KEV Alert: Mass exploitation detected |
| Action_Taken | Text | Max 500 chars | Yes | Emergency patching deployed within 4 hours |
| Action_Date | Date | DD.MM.YYYY | Yes | 15.01.2025 |
| Action_Owner | Text | Email or name | Yes | infrastructure@example.com |
| After_State | Text | Max 500 chars | Yes | All 12 servers patched, vulnerability eliminated |
| After_Evidence | Text | File path or reference | Yes | Scan-20250116-WebServers-Clean.xlsx |
| Validation_Method | Dropdown | Vulnerability_Scan, SIEM_Logs, EDR_Telemetry, Manual_Verification, Multiple | Yes | Multiple |
| Validation_Evidence | Text | File path or reference | Yes | SIEM logs show 23 blocked exploit attempts during patching |
| SIEM_Query_ID | Text | Free text | No | QUERY-2025-0115-001 |
| Time_to_Remediation | Formula | Hours, 1 decimal | Auto | 4.0 |
| Validated_By | Text | Email or name | Yes | jane.analyst@example.com |
| Validation_Date | Date | DD.MM.YYYY | Yes | 16.01.2025 |
| Cost_Avoidance_Estimate | Currency | >=0, 2 decimals | No | 50000.00 |
| Notes | Text | Max 1000 chars | No | Full evidence package prepared for audit |

**Formulas**:

Time_to_Remediation = (Action_Date + Action_Time) - (TI_Alert_Date + TI_Alert_Time)

Convert to hours with 1 decimal.

**Conditional Formatting**:

- CVSS_Base_Score >= 9.0 → Red background (Critical prevented)
- CVSS_Base_Score >= 7.0 → Orange background (High prevented)
- Validation_Evidence empty → Yellow background (needs validation)
- Time_to_Remediation > 72 hours → Orange background (slow response)


**Validation Rules**:

- After_Date must be >= Action_Date
- Validation_Date must be >= After_Date
- All "Evidence" fields must be non-empty for audit


**Audit Evidence Requirements**:

- **Before_Evidence**: Vulnerability scan showing affected systems
- **TI_Alert_Details**: Documented threat intelligence that triggered action
- **After_Evidence**: Validation that vulnerability was remediated
- **Validation_Evidence**: Proof no exploitation occurred
- **Quarterly Target**: Minimum 3 fully documented preventions


---

## Sheet 8: Feedback_Collection

**Purpose**: Capture and analyze stakeholder feedback

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Feedback_ID | Text | Auto-generated (FB-YYYY-NNN) | Yes | FB-2025-001 |
| Distribution_ID | Dropdown | From Distribution_Tracking | Yes | DIST-2025-001 |
| Product_ID | Formula | =VLOOKUP from Distribution | Auto | PROD-2025-015 |
| Stakeholder_ID | Dropdown | From Stakeholder_Registry | Yes | STK-001 |
| Stakeholder_Name | Formula | =VLOOKUP | Auto | John Security |
| Feedback_Date | DateTime | DD.MM.YYYY HH:MM | Yes | 02.01.2025 15:45 |
| Feedback_Method | Dropdown | Survey, Email_Reply, Meeting, Ticket, Call | Yes | Survey |
| Overall_Rating | Number | 1-5 scale | Yes | 5 |
| Relevance_Rating | Number | 1-5 scale | Yes | 5 |
| Timeliness_Rating | Number | 1-5 scale | Yes | 4 |
| Actionability_Rating | Number | 1-5 scale | Yes | 5 |
| Clarity_Rating | Number | 1-5 scale | No | 4 |
| Intelligence_Used | Dropdown | Yes, Partial, No, Will_Use_Later | Yes | Yes |
| Action_Taken | Text | Free text (max 300 chars) | No | Deployed IOCs to SIEM, created detection rules |
| Action_Result | Text | Free text | No | Detected 3 related events, no true positives yet |
| Improvement_Suggestions | Text | Free text | No | Include more context on threat actor motivations |
| Additional_Requirements | Text | Free text | No | Request similar analysis for APT29 |
| Would_Recommend | Dropdown | Yes, Maybe, No | No | Yes |
| Positive_Comments | Text | Free text | No | Excellent TTPs mapping, very actionable |
| Negative_Comments | Text | Free text | No | Could use more IOCs |
| Follow_Up_Required | Dropdown | Yes, No | No | No |
| Follow_Up_Notes | Text | If Yes | Conditional | N/A |
| Follow_Up_Complete | Dropdown | Yes, No, N/A | Auto | N/A |
| Notes | Text | Free text | No | Stakeholder is highly engaged, key consumer |

**Feedback Analysis** (summary section):

- Average ratings by category
- Sentiment analysis (positive/negative comments)
- Common improvement themes
- Most engaged stakeholders


---

## Sheet 9: Integration_Metrics

**Purpose**: KPIs for integration and dissemination effectiveness

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Metric_ID | Text | Auto-generated (IM-NNN) | Yes | IM-001 |
| Metric_Name | Text | Free text | Yes | IOC Deployment Rate |
| Metric_Category | Dropdown | Tool_Integration, IOC_Effectiveness, Dissemination, Stakeholder_Engagement, Automation, Prevention, Risk_Management | Yes | IOC_Effectiveness |
| Measurement_Period | Dropdown | Daily, Weekly, Monthly, Quarterly | Yes | Monthly |
| Target_Value | Number | Decimal | Yes | 95 |
| Actual_Value | Number | Decimal | Yes | 98 |
| Unit | Text | Free text | Yes | % |
| Performance_vs_Target | Formula | (Actual/Target - 1) * 100 | Auto | +3.2% |
| Status | Formula | Based on performance | Auto | Exceeds_Target |
| Trend | Dropdown | Improving, Stable, Declining | No | Stable |
| Data_Source | Text | Reference to sheet/cell | Yes | =IOC_Deployment!H:H |
| Owner | Text | Email | Yes | soc.manager@example.com |
| Last_Updated | Date | Auto TODAY() | Yes | 02.01.2025 |
| Notes | Text | Free text | No | Consistently meeting target |

**Standard Metrics**:
1. % of security tools with TI integration
2. IOC deployment success rate
3. Average time from IOC publication to deployment
4. IOC hit rate (hits per 100 IOCs)
5. False positive rate for IOCs
6. Intelligence distribution reach (% of target audience)
7. Average stakeholder engagement score
8. Feedback response rate
9. Intelligence consumption rate (% acted upon)
10. Mean time from intelligence to action
11. **Prevented incidents per quarter (Sheet 7)**
12. **Risk assessments updated per quarter (Sheet 13)**
13. **Incident-TI integration rate (Sheet 14)**
14. **Intelligence-driven decisions per quarter (Sheet 15)**

---

## Sheet 10: SIEM_Integration_Details

**Purpose**: Detailed SIEM integration tracking for primary security tool

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Integration_ID | Text | Auto-generated (SIEM-INT-NNN) | Yes | SIEM-INT-001 |
| Tool_ID | Dropdown | From Tool_Integration_Matrix (SIEM category only) | Yes | TOOL-001 |
| Tool_Name | Formula | =VLOOKUP | Auto | Splunk Enterprise Security |
| IOC_Feed_Name | Text | Free text | Yes | STIX Feed - Malware Hashes |
| Feed_Type | Dropdown | STIX_TAXII, CSV_Feed, API, Manual | Yes | STIX_TAXII |
| Feed_URL | Text | URL | No | https://taxii.example.com/collections/malware |
| Authentication_Method | Dropdown | API_Key, OAuth, Certificate, Basic_Auth, None | Yes | API_Key |
| Update_Frequency | Dropdown | Real-time, Hourly, Daily, Weekly | Yes | Hourly |
| Last_Successful_Pull | DateTime | DD.MM.YYYY HH:MM | No | 09.01.2025 14:00 |
| Last_Error_Date | DateTime | DD.MM.YYYY HH:MM | No | 08.01.2025 23:15 |
| Error_Details | Text | Free text | No | SSL certificate validation failed |
| IOCs_Ingested_Last_24h | Number | Integer >= 0 | No | 487 |
| IOCs_Active_Total | Number | Integer >= 0 | No | 12450 |
| Detection_Rules_Created | Number | Integer >= 0 | No | 23 |
| Correlation_Searches_Updated | Number | Integer >= 0 | No | 15 |
| Alerts_Generated_Last_30d | Number | Integer >= 0 | No | 145 |
| True_Positive_Rate | Number | Percentage 0-100 | No | 78 |
| Integration_Health | Dropdown | Healthy, Degraded, Down, Maintenance | Yes | Healthy |
| Monitoring_Dashboard | Text | URL | No | https://siem.example.com/dashboard/ti-health |
| Owner | Text | Email | Yes | soc.team@example.com |
| Notes | Text | Free text | No | Primary threat feed for malware detection |

**Conditional Formatting**:

- Integration_Health "Down" → Red background
- Integration_Health "Degraded" → Yellow background
- True_Positive_Rate < 50% → Yellow background
- Last_Successful_Pull > 24 hours ago → Orange background


---

## Sheet 11: EDR_Integration_Details

**Purpose**: Detailed EDR integration tracking for endpoint security

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Integration_ID | Text | Auto-generated (EDR-INT-NNN) | Yes | EDR-INT-001 |
| Tool_ID | Dropdown | From Tool_Integration_Matrix (EDR category only) | Yes | TOOL-002 |
| Tool_Name | Formula | =VLOOKUP | Auto | CrowdStrike Falcon |
| IOC_Feed_Name | Text | Free text | Yes | Custom Threat Intel Feed |
| Feed_Type | Dropdown | API, Hash_List, Watchlist, Custom_Indicator, Manual | Yes | API |
| Feed_URL | Text | URL | No | https://api.crowdstrike.com/iocs |
| Authentication_Method | Dropdown | API_Key, OAuth, Certificate, Basic_Auth | Yes | OAuth |
| Update_Frequency | Dropdown | Real-time, Hourly, Daily, Weekly | Yes | Real-time |
| Last_Successful_Push | DateTime | DD.MM.YYYY HH:MM | No | 09.01.2025 14:30 |
| Last_Error_Date | DateTime | DD.MM.YYYY HH:MM | No | N/A |
| Error_Details | Text | Free text | No | N/A |
| IOCs_Deployed_Last_24h | Number | Integer >= 0 | No | 156 |
| IOCs_Active_Total | Number | Integer >= 0 | No | 8920 |
| Endpoints_Protected | Number | Integer >= 0 | Yes | 285 |
| Detections_Last_30d | Number | Integer >= 0 | No | 45 |
| False_Positive_Rate | Number | Percentage 0-100 | No | 12 |
| Quarantine_Actions | Number | Integer >= 0 | No | 8 |
| Block_Actions | Number | Integer >= 0 | No | 37 |
| Integration_Health | Dropdown | Healthy, Degraded, Down, Maintenance | Yes | Healthy |
| Policy_Version | Text | Version number | No | 2.4.1 |
| Last_Policy_Update | Date | DD.MM.YYYY | No | 15.12.2024 |
| Owner | Text | Email | Yes | endpoint.team@example.com |
| Notes | Text | Free text | No | Excellent integration, low FP rate |

**Conditional Formatting**:

- Integration_Health "Down" → Red background
- Integration_Health "Degraded" → Yellow background
- False_Positive_Rate > 20% → Yellow background
- Detections_Last_30d > 0 → Green highlight


---
## Sheet 12: Threat_Hunting_Campaigns

**Purpose**: Track TI-driven proactive threat hunting activities

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Campaign_ID | Text | Auto-generated (HUNT-YYYY-NNN) | Yes | HUNT-2025-001 |
| Campaign_Name | Text | Free text | Yes | APT28 Infrastructure Hunt |
| TI_Report_ID | Text | TI-YYYY-NNN format | Yes | TI-2025-008 |
| TI_Report_Title | Formula | =VLOOKUP | Auto | APT28 New C2 Infrastructure |
| Threat_Actor | Text | Free text | No | APT28 (Fancy Bear) |
| Start_Date | Date | DD.MM.YYYY | Yes | 20.01.2025 |
| End_Date | Date | DD.MM.YYYY | No | 22.01.2025 |
| Status | Dropdown | Planned, Active, Completed, Suspended | Yes | Completed |
| Hunt_Hypothesis | Text | Max 500 chars | Yes | APT28 may have established persistence in our environment using newly identified C2 domains |
| MITRE_Techniques | Text | Comma-separated | No | T1071.001, T1090, T1102 |
| Data_Sources_Analyzed | Text | Comma-separated | Yes | SIEM, EDR, Firewall logs, DNS logs, Proxy logs |
| Tools_Used | Text | Free text | Yes | Splunk, EDR console, MITRE ATT&CK Navigator |
| Time_Invested_Hours | Number | Hours, 1 decimal | Yes | 16.5 |
| Hunters | Text | Comma-separated names | Yes | jane.analyst@example.com, john.researcher@example.com |
| Outcome | Dropdown | No_Findings, Findings_Benign, Findings_Malicious, Investigation_Ongoing | Yes | No_Findings |
| Findings_Description | Text | Max 1000 chars | Conditional | No APT28 presence detected |
| IOCs_Discovered | Number | Integer >= 0 | No | 0 |
| New_Detection_Rules | Number | Integer >= 0 | No | 2 |
| Suspicious_Activity_Description | Text | Max 500 chars | No | N/A |
| Incidents_Created | Number | Integer >= 0 | Yes | 0 |
| Lessons_Learned | Text | Max 1000 chars | No | No APT28 presence detected. TI intel was accurate but threat did not reach our environment. |
| Follow_Up_Required | Dropdown | Yes, No | No | No |
| Notes | Text | Max 500 chars | No | Good proactive hunt, validated defensive posture |

**Conditional Formatting**:

- Outcome "Findings_Malicious" → Red background
- Outcome "Findings_Benign" → Yellow background
- Status "Active" → Blue highlight
- Time_Invested_Hours > 40 → Orange (resource intensive)


**Hunt Effectiveness Metrics**:

- Total hunts per quarter
- % hunts with findings
- Average time per hunt
- Detection rules created
- Incidents discovered


---

## Sheet 13: Risk_Assessment_Updates ⚠️ **CRITICAL AUDIT EVIDENCE**

**Purpose**: Document Clause 6.1 integration per ISMS-POL-A.5.7, Section 2.4 (Risk Assessment Integration Requirements)

**KPI Target**: ≥3 risk assessment updates per quarter

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Update_ID | Text | Auto-generated (RISK-YYYYQQ-NNN) | Yes | RISK-2025Q1-001 |
| Quarter | Text | YYYY-QQ format | Yes | 2025-Q1 |
| Update_Date | Date | DD.MM.YYYY | Yes | 20.01.2025 |
| TI_Report_ID | Text | TI-YYYY-NNN format | Yes | TI-2025-005 |
| TI_Report_Title | Text | Free text | Yes | Ransomware Targeting Hosting Sector |
| Risk_Register_ID | Text | REG-NNN format | Yes | REG-047 |
| Risk_Name | Text | Free text | Yes | Data Confidentiality - Ransomware |
| Risk_Type | Dropdown | Vulnerability, Threat_Campaign, Threat_Actor, Emerging_Threat, Supply_Chain | Yes | Vulnerability |
| CVE_ID | Text | CVE-YYYY-NNNNN or N/A | No | CVE-2024-56789 |
| CVSS_Version | Dropdown | 4.0, 3.1, N/A | No | 4.0 |
| CVSS_Base_Score | Number | 0.0-10.0 or blank | No | 9.3 |
| CVSS_Vector | Text | Max 200 chars | No | CVSS:4.0/AV:N/AC:L/PR:N/UI:N/S:C/VC:H/VI:H/VA:H/SC:H/SI:H/SA:H |
| Risk_Before_Likelihood | Dropdown | Very_Low, Low, Medium, High, Very_High | Yes | Medium |
| Risk_Before_Impact | Dropdown | Very_Low, Low, Medium, High, Very_High | Yes | High |
| Risk_Before_Rating | Formula | Auto-calc | Auto | High |
| Risk_After_Likelihood | Dropdown | Very_Low, Low, Medium, High, Very_High | Yes | High |
| Risk_After_Impact | Dropdown | Very_Low, Low, Medium, High, Very_High | Yes | Critical |
| Risk_After_Rating | Formula | Auto-calc | Auto | Critical |
| Likelihood_Change_Rationale | Text | Max 500 chars | Yes | Mass exploitation detected per CISA KEV |
| Impact_Change_Rationale | Text | Max 500 chars | Yes | CVSS 9.3 indicates severe impact to confidentiality/integrity/availability |
| CVSS_Risk_Quantification | Text | Max 500 chars | No | CVSS 9.3 (Critical) + Mass Exploitation = Critical risk requiring emergency treatment |
| Risk_Treatment_Change | Dropdown | No_Change, New_Treatment, Accelerated_Treatment, Emergency_Treatment | Yes | Emergency_Treatment |
| Treatment_Plan_ID | Text | PLAN-YYYY-NNN format | Yes | PLAN-2025-005 |
| Treatment_Description | Text | Max 500 chars | Yes | Emergency patching of all vulnerable systems within 24 hours |
| Treatment_Owner | Text | Email | Yes | infrastructure.manager@example.com |
| Treatment_Deadline | Date | DD.MM.YYYY | Yes | 21.01.2025 |
| CRO_Review_Date | Date | DD.MM.YYYY | Yes | 20.01.2025 |
| CRO_Approval_Date | Date | DD.MM.YYYY | Yes | 20.01.2025 |
| CRO_Signature | Text | Name | Yes | John Doe, CRO |
| Treatment_Completion_Date | Date | DD.MM.YYYY | No | 21.01.2025 |
| Treatment_Status | Dropdown | Planned, In_Progress, Completed, Delayed, Cancelled | Yes | Completed |
| Validation_Evidence | Text | File reference | Yes | Vuln-Scan-20250121-Clean.xlsx |
| Notes | Text | Max 1000 chars | No | Emergency patching completed ahead of deadline, threat mitigated |

**Risk Rating Calculation** (simplified matrix):

Impact vs. Likelihood Matrix:

- Critical = Very_High Impact + (High or Very_High Likelihood)
- High = High Impact + (Medium or High Likelihood) OR Very_High Impact + Low Likelihood
- Medium = Medium Impact + Medium Likelihood
- Low = Low Impact or Very_Low Impact with Low/Very_Low Likelihood



**Conditional Formatting**:

- Risk_After_Rating "Critical" → Red background
- CVSS_Base_Score >= 9.0 → Red text
- Treatment_Status "Delayed" → Yellow background
- CRO_Approval_Date missing → Red background (blocking audit)
- Treatment_Completion_Date > Treatment_Deadline → Orange (missed deadline)


**Validation Rules**:

- CRO_Review_Date required for all updates
- CRO_Approval_Date required within 48 hours of Review_Date
- Treatment_Completion_Date required if Status = Completed
- Validation_Evidence required for all Completed treatments


**Audit Evidence Requirements**:

- **TI_Report linkage**: Threat intelligence that triggered update
- **Risk_Rating changes**: Documented rationale with CVSS context
- **CRO approval**: Chief Risk Officer formal sign-off (Clause 6.1 requirement)
- **Treatment evidence**: Proof of risk treatment completion
- **Quarterly target**: Minimum 3 risk updates with full audit trail


---

## Sheet 14: Incident_TI_Integration ⚠️ **CRITICAL AUDIT EVIDENCE**

**Purpose**: Track TI usage in incident response per ISMS-POL-A.5.7, Section 2.5 (Incident Management Integration Requirements)

**KPI Target**: ≥70% of P1/P2 incidents use threat intelligence

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Integration_ID | Text | Auto-generated (INC-TI-YYYY-NNN) | Yes | INC-TI-2025-001 |
| Incident_ID | Text | INC-YYYY-NNN format | Yes | INC-2025-012 |
| Incident_Priority | Dropdown | P1, P2, P3, P4 | Yes | P1 |
| Incident_Date | DateTime | DD.MM.YYYY HH:MM | Yes | 25.01.2025 14:30 |
| Incident_Title | Text | Free text | Yes | Suspicious network activity detected |
| Incident_Category | Dropdown | Malware, Phishing, Data_Breach, DDoS, Insider_Threat, Vulnerability_Exploit, Other | Yes | Malware |
| TI_Used | Dropdown | Yes, No, Partial | Yes | Yes |
| TI_Usage_Timing | Dropdown | During_Detection, During_Investigation, During_Containment, During_Recovery, Post_Incident | Conditional | During_Investigation |
| TI_Reports_Referenced | Text | Comma-separated TI-YYYY-NNN | Conditional | TI-2025-008, TI-2025-012 |
| IOCs_Matched | Text | Comma-separated IOC-YYYY-NNN | No | IOC-2025-045, IOC-2025-098 |
| CVE_ID | Text | CVE-YYYY-NNNNN or N/A | No | CVE-2024-98765 |
| CVSS_Version | Dropdown | 4.0, 3.1, N/A | No | 4.0 |
| CVSS_Base_Score | Number | 0.0-10.0 or blank | No | 8.7 |
| CVSS_Vector | Text | Max 200 chars | No | CVSS:4.0/AV:N/AC:L/PR:N/UI:R/S:C/VC:H/VI:H/VA:N/SC:L/SI:L/SA:N |
| Threat_Actor_Identified | Text | Free text | No | APT28 |
| MITRE_Techniques_Observed | Text | Comma-separated | No | T1071.001, T1059.001, T1055 |
| TI_Value_Assessment | Dropdown | Critical, High, Medium, Low, None | Conditional | High |
| TI_Impact_Description | Text | Max 500 chars | Conditional | TI provided TTPs that enabled rapid detection of lateral movement attempts |
| Investigation_Duration_Hours | Number | Hours, 1 decimal | Yes | 6.5 |
| Time_Saved_Estimate_Hours | Number | Hours, 1 decimal | No | 18.0 |
| Containment_Actions | Text | Max 500 chars | Yes | Isolated affected host, blocked C2 domains at firewall |
| TI_Driven_Containment | Dropdown | Yes, No, Partial | No | Yes |
| Eradication_Actions | Text | Max 500 chars | Yes | Removed malware, patched vulnerability, reset credentials |
| Recovery_Actions | Text | Max 500 chars | Yes | Restored from clean backup, verified system integrity |
| Lessons_Learned | Text | Max 1000 chars | No | Early TI integration critical for rapid response |
| New_IOCs_Discovered | Number | Integer >= 0 | No | 3 |
| New_Detection_Rules_Created | Number | Integer >= 0 | No | 2 |
| TI_Feedback_Provided_to_Sources | Dropdown | Yes, No | No | Yes |
| Feedback_Details | Text | Max 300 chars | Conditional | Shared newly discovered IOCs with ISAC |
| Incident_Responder | Text | Email | Yes | incident.responder@example.com |
| Incident_Close_Date | Date | DD.MM.YYYY | No | 26.01.2025 |
| Notes | Text | Max 1000 chars | No | Excellent example of TI-driven incident response |

**Formulas**:

Investigation_Duration_Hours = (Incident_Close_Date - Incident_Date) in hours
Time_Saved_Estimate_Hours = Manual estimate by responder


**Conditional Formatting**:

- Incident_Priority "P1" AND TI_Used "No" → Red background (missed opportunity)
- TI_Value_Assessment "Critical" → Green highlight
- CVSS_Base_Score >= 9.0 → Red text
- Time_Saved_Estimate_Hours > 10 → Green highlight (significant value)
- Investigation_Duration_Hours > 48 → Yellow (prolonged investigation)


**Validation Rules**:

- If TI_Used = "Yes" or "Partial": TI_Reports_Referenced required
- If TI_Used = "Yes" or "Partial": TI_Value_Assessment required
- If TI_Used = "Yes" or "Partial": TI_Impact_Description required
- P1/P2 incidents with TI_Used "No" require justification in Notes


**Audit Evidence Requirements**:

- **P1/P2 TI usage tracking**: ≥70% must have TI_Used = "Yes"
- **TI value quantification**: Time saved, faster containment, better eradication
- **IOC matching**: Direct evidence of TI-to-detection pipeline effectiveness
- **Feedback loop**: TI_Feedback_Provided shows bidirectional intelligence flow
- **Quarterly KPI**: Calculate (Count P1/P2 with TI_Used="Yes") / (Total P1/P2) >= 70%


---

## Sheet 15: Intelligence_Driven_Decisions ⚠️ **CRITICAL AUDIT EVIDENCE**

**Purpose**: Document business decisions based on TI per ISMS-POL-A.5.7, Section 2.7 (Effectiveness Measurement Requirements)

**KPI Target**: ≥5 documented intelligence-driven decisions per quarter

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Decision_ID | Text | Auto-generated (DEC-YYYYQQ-NNN) | Yes | DEC-2025Q1-001 |
| Quarter | Text | YYYY-QQ format | Yes | 2025-Q1 |
| Decision_Date | Date | DD.MM.YYYY | Yes | 22.01.2025 |
| TI_Report_ID | Text | TI-YYYY-NNN format | Yes | TI-2025-009 |
| TI_Report_Title | Text | Free text | Yes | Emerging Threat: Supply Chain Attack Vector |
| Decision_Category | Dropdown | Architecture, Tool_Investment, Process_Change, Resource_Allocation, Risk_Treatment, Strategic_Initiative | Yes | Tool_Investment |
| Decision_Title | Text | Free text | Yes | Accelerate EDR deployment to development environment |
| Decision_Description | Text | Max 1000 chars | Yes | Deploy EDR to 45 developer workstations to protect against supply chain attacks targeting dev tools |
| TI_Insight_Summary | Text | Max 500 chars | Yes | TI report shows threat actors targeting developer tools and build pipelines in hosting sector |
| CVE_ID | Text | CVE-YYYY-NNNNN or N/A | No | N/A |
| CVSS_Version | Dropdown | 4.0, 3.1, N/A | No | N/A |
| CVSS_Base_Score | Number | 0.0-10.0 or blank | No | N/A |
| CVSS_Prioritization_Flag | Dropdown | Yes, No | No | No |
| Risk_Addressed | Text | Free text | Yes | Supply chain compromise via developer workstation |
| Business_Impact | Text | Max 500 chars | Yes | Protects critical build infrastructure, reduces risk of malicious code injection |
| Decision_Maker | Text | Name and role | Yes | Jane Smith, CISO |
| Decision_Maker_Level | Dropdown | C-Suite, VP, Director, Manager | Yes | C-Suite |
| Stakeholders_Involved | Text | Comma-separated | Yes | CISO, CTO, Development Manager, Security Operations |
| Investment_Required_CHF | Currency | >=0, 2 decimals | No | 45000.00 |
| Resource_Hours_Required | Number | Hours, 1 decimal | No | 120.0 |
| Implementation_Timeline | Text | Free text | Yes | 4 weeks (01.02.2025 - 28.02.2025) |
| Expected_Benefits | Text | Max 500 chars | Yes | Early detection of dev workstation compromise, protection of build pipeline, reduced supply chain risk |
| ROI_Estimate | Formula | Auto-calc if data present | Auto | 3.5x |
| Implementation_Status | Dropdown | Planned, In_Progress, Completed, On_Hold, Cancelled | Yes | In_Progress |
| Implementation_Start_Date | Date | DD.MM.YYYY | No | 01.02.2025 |
| Implementation_Complete_Date | Date | DD.MM.YYYY | No | N/A |
| Success_Metrics | Text | Max 300 chars | Yes | All 45 dev workstations with EDR, <5% performance impact, zero missed detections |
| Outcome_Assessment | Text | Max 500 chars | No | TBD upon completion |
| Lessons_Learned | Text | Max 500 chars | No | TBD |
| Documentation_Link | Text | URL or file path | No | https://docs.example.com/projects/edr-dev-rollout |
| Board_Presentation | Dropdown | Yes, No, Planned | No | Planned |
| Notes | Text | Max 1000 chars | No | Approved in Q1 CISO review, accelerated based on TI assessment |

**ROI Calculation** (if data present):

ROI_Estimate = (Cost_Avoidance_Estimate) / (Investment_Required_CHF)

Where Cost_Avoidance_Estimate is based on:

- Potential incident costs prevented
- Business disruption avoided
- Reputation protection



**Conditional Formatting**:

- Decision_Maker_Level "C-Suite" → Green highlight (executive buy-in)
- Investment_Required > 100,000 CHF → Yellow (significant investment)
- Implementation_Status "Cancelled" → Gray background
- ROI_Estimate >= 3.0x → Green (strong ROI)
- CVSS_Base_Score >= 9.0 → Red text (critical vulnerability addressed)


**Validation Rules**:

- Decision_Maker_Level "C-Suite" required for Investment > 50,000 CHF
- Implementation_Complete_Date required if Status = "Completed"
- Outcome_Assessment required if Status = "Completed"
- Success_Metrics required for all decisions


**Audit Evidence Requirements**:

- **TI linkage**: Direct connection to threat intelligence report
- **Executive involvement**: Decision_Maker and stakeholder documentation
- **Business justification**: Risk addressed, business impact, expected benefits
- **Outcome tracking**: Implementation status and success metrics
- **Quarterly target**: Minimum 5 documented decisions with full audit trail
- **Strategic value**: Demonstrate TI drives business and security decisions


---

## Sheet 16: Action_Items

**Purpose**: Track identified issues, gaps, and remediation actions from the assessment

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Item_ID | Text | Auto-generated (ACT-NNN) | Yes | ACT-001 |
| Category | Dropdown | Integration_Gap, Process_Improvement, Documentation, Training, Tool_Configuration | Yes | Integration_Gap |
| Description | Text | Free text (max 500 chars) | Yes | EDR integration missing for endpoint group B |
| Priority | Dropdown | Critical, High, Medium, Low | Yes | High |
| Source_Sheet | Text | Sheet name reference | Yes | Tool_Integration_Matrix |
| Assigned_To | Text | Name/email | Yes | soc.lead@example.com |
| Due_Date | Date | DD.MM.YYYY | Yes | 15.03.2025 |
| Status | Dropdown | Open, In_Progress, Completed, Deferred, Cancelled | Yes | Open |
| Completion_Date | Date | DD.MM.YYYY | No | N/A |
| Resolution_Notes | Text | Max 500 chars | No | N/A |
| Evidence_Link | Text | URL or file path | No | N/A |

**Conditional Formatting**:

- Priority "Critical" + Status "Open" -> Red background
- Due_Date < Today AND Status != "Completed" -> Yellow background
- Status "Completed" -> Green highlight


---

## Sheet 17: Metadata

**Purpose**: Document workbook metadata, version history, and assessment summary

**Content Sections**:

1. **Document Information**
   - Document ID: ISMS-IMP-A.5.7.3
   - Version: 1.0
   - Control Reference: ISO/IEC 27001:2022 Control A.5.7
   - Assessment Type: Integration & Distribution Assessment

2. **Generation Information**
   - Generated Date: [Auto-populated]
   - Generator Version: 1.0
   - Framework Version: 1.0

3. **Assessment Summary**
   - Total Sheets: 17
   - Sheets Completed: [Count]
   - Overall Status: [Draft/In_Review/Approved]
   - Last Modified: [Date]
   - Modified By: [Name]

4. **Approval Workflow**
   - Prepared By: [Name/Date]
   - Reviewed By: [Name/Date]
   - Approved By: [Name/Date]

5. **Related Documents**
   - ISMS-POL-A.5.7
   - ISMS-IMP-A.5.7.1 through A.5.7.5
   - Cross-control references


---

# Assessment Methodology

## Tool Integration Assessment

- Inventory all security tools
- Assess current integration status
- Identify integration gaps
- Prioritize based on business value
- Develop integration roadmap
- Track detailed SIEM/EDR integration (Sheets 10-11)


## IOC Effectiveness Assessment

- Track IOC deployment lifecycle
- Monitor hit rates and false positives
- Correlate IOCs to incidents
- Retire ineffective IOCs
- Continuous quality improvement


## Dissemination Effectiveness Assessment

- Analyze engagement metrics
- Collect stakeholder feedback
- Identify channel performance
- Optimize distribution strategy
- Tailor content to audience


## Prevention Tracking (Sheet 7)

- Document prevented incidents with before/after evidence
- Validate prevention through SIEM/EDR/scanning evidence
- Calculate time-to-remediation metrics
- Achieve quarterly KPI: ≥3 validated preventions
- Prepare full audit evidence packages


## Risk Assessment Integration (Sheet 13)

- Track TI-driven risk register updates (Clause 6.1)
- Document risk rating changes with CVSS quantification
- Obtain CRO approval for all risk treatment changes
- Achieve quarterly KPI: ≥3 risk updates with audit trail
- Link threat intelligence to risk management framework


## Incident Response Integration (Sheet 14)

- Track TI usage in all P1/P2 incidents
- Quantify TI value (time saved, faster containment)
- Document IOC matches and TTP correlations
- Achieve quarterly KPI: ≥70% P1/P2 incidents use TI
- Establish bidirectional TI feedback loop


## Intelligence-Driven Decisions (Sheet 15)

- Document C-suite and VP-level decisions based on TI
- Quantify business impact and ROI
- Track implementation status and success metrics
- Achieve quarterly KPI: ≥5 documented decisions
- Demonstrate strategic value of threat intelligence program


## Threat Hunting (Sheet 12)

- Conduct proactive TI-driven threat hunts
- Document hunt hypotheses and methodologies
- Track outcomes and lessons learned
- Create new detection rules from hunt findings
- Build threat hunting capability


---

# Integration Points

## From Control 5.7.2 (Collection & Analysis)

- Intelligence_Production → Distribution_Tracking.Product_ID
- Intelligence_Production → Prevention_Tracking.Threat_Report_ID
- Intelligence_Production → Risk_Assessment_Updates.TI_Report_ID
- Intelligence_Production → Incident_TI_Integration.TI_Reports_Referenced
- Intelligence_Production → Intelligence_Driven_Decisions.TI_Report_ID
- Intelligence_Production → Threat_Hunting_Campaigns.TI_Report_ID
- VulnerabilityThreatLink → IOC_Deployment (vulnerability-related IOCs)
- VulnerabilityThreatLink → Prevention_Tracking.CVE_ID


## To Control 5.7.1 (Sources)

- IOC effectiveness data → Source quality evaluation
- Feedback on source-specific intelligence → Source ratings
- Prevention tracking → Source value quantification
- Incident TI integration → Source actionability assessment


## To Control 5.7.4 (Dashboard)

- All 15 sheets → External references for program-level KPIs
- Critical evidence sheets (7, 13, 14, 15) → Dashboard KPI tracking


## To Control 8.8 (Vulnerability Management)

- IOCs related to vulnerabilities → 8.8 compromise assessment
- Tool integration status → 8.8 detection capabilities
- Prevention_Tracking → 8.8 emergency patching validation
- Risk_Assessment_Updates → 8.8 vulnerability prioritization


## To Controls A.5.24-5.28 (Incident Management)

- Incident_TI_Integration → A.5.24-5.28 incident response evidence
- IOC matches → Incident detection documentation
- Threat hunting findings → Proactive incident prevention


## To Clause 6.1 (Risk Assessment)

- Risk_Assessment_Updates → Clause 6.1 mandatory risk register updates
- CRO approval tracking → Clause 6.1 governance evidence


---

# Evidence Requirements

## Standard Evidence

- Integration documentation and diagrams
- IOC deployment logs
- Stakeholder feedback surveys
- Engagement analytics reports
- Tool configuration evidence
- Incident correlation reports


## Critical Audit Evidence

**Sheet 7 - Prevention_Tracking**:

- Before-state vulnerability scans
- Threat intelligence alerts that triggered action
- After-state clean scans
- SIEM/EDR validation logs
- Time-to-remediation calculations
- Minimum 3 fully documented preventions per quarter


**Sheet 13 - Risk_Assessment_Updates**:

- Threat intelligence reports triggering risk updates
- Risk rating change calculations with CVSS context
- CRO review and approval signatures
- Risk treatment completion evidence
- Minimum 3 risk updates with CRO approval per quarter


**Sheet 14 - Incident_TI_Integration**:

- Incident records with TI usage documentation
- IOC match evidence
- Time-saved quantification
- P1/P2 incident TI usage rate ≥70%
- Bidirectional TI feedback examples


**Sheet 15 - Intelligence_Driven_Decisions**:

- Executive decision documentation
- Business justification and ROI calculations
- Implementation tracking and success metrics
- Minimum 5 C-suite/VP decisions per quarter
- Strategic TI program value demonstration


---

# Completion Instructions

## Initial Assessment

**Phase 1: Core Integration (Sheets 1-6)** - 2 days
1. Document all Tool_Integration entries (Sheet 2)
2. Load IOC_Deployment data (past 90 days) (Sheet 3)
3. Configure Dissemination_Channels (Sheet 4)
4. Populate Stakeholder_Registry (Sheet 5)
5. Review Distribution_Tracking (past 90 days) (Sheet 6)

**Phase 2: Critical Evidence Sheets (Sheets 7, 13-15)** - 3 days
6. Document Prevention_Tracking (Sheet 7) - past quarter
7. Document Risk_Assessment_Updates (Sheet 13) - past quarter
8. Document Incident_TI_Integration (Sheet 14) - past quarter
9. Document Intelligence_Driven_Decisions (Sheet 15) - past quarter

**Phase 3: Supporting Sheets (Sheets 8-12)** - 2 days
10. Collect and enter Feedback (Sheet 8)
11. Establish baseline Integration_Metrics (Sheet 9)
12. Document SIEM_Integration_Details (Sheet 10)
13. Document EDR_Integration_Details (Sheet 11)
14. Document Threat_Hunting_Campaigns (Sheet 12) - past quarter

**Estimated Total Time**: 5-7 days for comprehensive initial assessment

## Ongoing Management

**Daily**:

- IOC deployment tracking (Sheet 3)
- SIEM/EDR integration health monitoring (Sheets 10-11)


**Weekly**:

- Distribution tracking (Sheet 6)
- Feedback collection (Sheet 8)
- Tool integration status updates (Sheet 2)


**Monthly**:

- Metrics review (Sheet 9)
- Dissemination channel performance (Sheet 4)
- Stakeholder engagement analysis (Sheet 5)


**Quarterly** (CRITICAL for audit):

- Prevention tracking documentation (Sheet 7) - Target: ≥3 preventions
- Risk assessment updates (Sheet 13) - Target: ≥3 updates with CRO approval
- Incident-TI integration assessment (Sheet 14) - Target: ≥70% P1/P2 usage
- Intelligence-driven decisions (Sheet 15) - Target: ≥5 documented decisions
- Threat hunting campaigns (Sheet 12) - Minimum 2 campaigns
- Full assessment workbook review and validation
- Dashboard consolidation (Control 5.7.4)


---

# Validation Rules

## Standard Validation

- All Active IOCs must be deployed to >= 1 tool
- Expired IOCs must have Status updated
- Distribution must match Stakeholder TLP clearance
- Tool integration with "Fully_Integrated" must have automation
- Critical IOCs (Severity=Critical) must deploy within 4 hours


## Critical Evidence Validation

**Sheet 7 - Prevention_Tracking**:

- All Evidence fields (Before, TI Alert, After, Validation) must be non-empty
- Validation_Date >= After_Date >= Action_Date
- Time_to_Remediation must be auto-calculated
- Quarterly count >= 3 validated preventions


**Sheet 13 - Risk_Assessment_Updates**:

- CRO_Review_Date required for ALL updates
- CRO_Approval_Date within 48 hours of Review_Date
- Validation_Evidence required for Completed treatments
- Quarterly count >= 3 updates with CRO signatures


**Sheet 14 - Incident_TI_Integration**:

- P1/P2 incidents with TI_Used="No" require justification in Notes
- TI_Used="Yes" requires: TI_Reports_Referenced, TI_Value_Assessment, TI_Impact_Description
- Quarterly P1/P2 TI usage rate >= 70%


**Sheet 15 - Intelligence_Driven_Decisions**:

- Investment > 50,000 CHF requires Decision_Maker_Level="C-Suite"
- Status="Completed" requires Outcome_Assessment
- Success_Metrics required for ALL decisions
- Quarterly count >= 5 documented decisions


---

# Quarterly KPI Summary

| KPI | Target | Sheet | Audit Criticality |
|-----|--------|-------|-------------------|
| Prevented Incidents | ≥3 per quarter | Sheet 7 | CRITICAL |
| Risk Assessment Updates | ≥3 per quarter with CRO approval | Sheet 13 | CRITICAL (Clause 6.1) |
| P1/P2 Incident TI Usage | ≥70% | Sheet 14 | CRITICAL |
| Intelligence-Driven Decisions | ≥5 per quarter | Sheet 15 | CRITICAL |
| Threat Hunting Campaigns | ≥2 per quarter | Sheet 12 | HIGH |
| Tool Integration Rate | ≥80% fully integrated | Sheet 2 | MEDIUM |
| IOC Deployment Rate | ≥95% | Sheet 3 | MEDIUM |
| Stakeholder Engagement | Avg ≥4.0/5.0 | Sheet 8 | MEDIUM |
| Distribution Reach | ≥90% target audience | Sheet 6 | LOW |

**Audit Readiness**: Sheets 7, 13, 14, 15 are MANDATORY for demonstrating threat intelligence program value and Clause 6.1 compliance.

---

# Related Documents

**Policy Framework**:

- **ISMS-POL-A.5.7** (Threat Intelligence Policy) - Consolidated single policy document
- **ISMS-POL-A.5.7, Section 2.3** (Intelligence Dissemination Requirements)
- **ISMS-POL-A.5.7, Section 2.4** (Risk Assessment Integration Requirements) - **References Sheet 13**
- **ISMS-POL-A.5.7, Section 2.5** (Incident Management Integration Requirements) - **References Sheet 14**
- **ISMS-POL-A.5.7, Section 2.7** (Effectiveness Measurement Requirements) - **References Sheets 7, 15**
- **ISMS-POL-A.5.7, Section 3.1** (Roles & Responsibilities)


**Implementation Specifications**:

- ISMS-IMP-A.5.7.1 (Threat Intelligence Sources Assessment)
- ISMS-IMP-A.5.7.2 (Intelligence Collection & Analysis Assessment)
- ISMS-IMP-A.5.7.4 (Threat Intelligence Effectiveness Dashboard)


**Cross-Control Integration**:

- ISMS-IMP-A.8.8 (Vulnerability Management) - **Integration with Prevention_Tracking**
- Tool-specific integration guides
- Incident response procedures (A.5.24-5.28)
- Risk management framework (Clause 6.1)


---


---

# Related Documents

**Policy Framework:**

- **ISMS-POL-A.5.7** (Threat Intelligence Policy) - Consolidated single policy document
- **ISMS-POL-A.5.7, Section 2.3** (Intelligence Dissemination Requirements)
- **ISMS-POL-A.5.7, Section 2.4** (Risk Assessment Integration Requirements) - **References Sheet 13**
- **ISMS-POL-A.5.7, Section 2.5** (Incident Management Integration Requirements) - **References Sheet 14**
- **ISMS-POL-A.5.7, Section 2.7** (Effectiveness Measurement Requirements) - **References Sheets 7, 15**
- **ISMS-POL-A.5.7, Section 3.1** (Roles & Responsibilities)


**Implementation Specifications:**

- **ISMS-IMP-A.5.7.1** (Threat Intelligence Sources Assessment) - Source IDs referenced
- **ISMS-IMP-A.5.7.2** (Intelligence Collection & Analysis Assessment) - VTL records, IOCs, intelligence products consumed
- **ISMS-IMP-A.5.7.4** (Effectiveness Dashboard) - Integration metrics consolidated
- **ISMS-IMP-A.5.7.5** (Standalone Dashboard) - Prevention and decision metrics for executives


**Cross-Control Integration:**

- **ISMS-IMP-A.8.8** (Vulnerability Management) - VTL records feed into prevention tracking
- **ISO 27001:2022 Clause 6.1** (Risk Assessment) - **Sheet 13 MANDATORY integration**
- **ISO 27001:2022 Controls A.5.24-5.28** (Incident Management) - **Sheet 14 MANDATORY integration**


**Standards References:**

- ISO/IEC 27001:2022 Annex A Control A.5.7
- ISO/IEC 27002:2022 Control 5.7 Implementation Guidance
- ISO/IEC 27001:2022 Clause 6.1 (Actions to address risks and opportunities)
- ISO/IEC 27001:2022 Controls A.5.24-5.28 (Incident management)


---

**END OF SPECIFICATION**

---

*"The opposite of a correct statement is a false statement. But the opposite of a profound truth may well be another profound truth."*
— Niels Bohr
*Where bamboo antennas actually work.* 🎋
