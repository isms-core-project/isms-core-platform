<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.7.3-UG:framework:UG:a.5.7.3 -->
**ISMS-IMP-A.5.7.3-UG - Intelligence Integration & Distribution Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.7: Threat Intelligence

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Intelligence Integration & Distribution Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.7.3-UG |
| **Related Policy** | ISMS-POL-A.5.7 (Threat Intelligence) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.5.7 (Threat Intelligence) |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | CISO |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO | Initial implementation specification |

**Review Cycle**: Quarterly  
**Next Review Date**: [Effective Date + 90 days]

**Related Documents**:

- ISMS-POL-A.5.7 (Threat Intelligence)
- ISMS-IMP-A.5.7.1 (Threat Intelligence Sources Assessment)
- ISMS-IMP-A.5.7.2 (Intelligence Collection & Analysis Assessment)

---

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.5.7.3-TG.

### Workbook at a Glance

This workbook contains the following 12 sheets:

| Sheet | Purpose |
|-------|---------|
| **Instructions & Legend** | Assessment guidance, control requirements, and field descriptions |
| **Tool Integration Matrix** | Mapping of intelligence integration with security tools (SIEM, EDR, SOAR) |
| **IOC Deployment** | Tracking of IOC deployment across security controls |
| **Dissemination Channels** | Documentation of intelligence distribution channels by stakeholder |
| **Stakeholder Registry** | Intelligence consumer registry with distribution preferences |
| **Distribution Tracking** | Record of intelligence distributed and stakeholder acknowledgement |
| **Feedback Collection** | Structured feedback from intelligence consumers |
| **Integration Metrics** | Measurement of integration effectiveness and operational impact |
| **Action Items** | Gap identification and remediation tracking |
| **Evidence Register** | Tracking of supporting evidence for audit purposes |
| **Summary Dashboard** | Compliance overview auto-populated from your input data |
| **Approval Sign-Off** | Stakeholder sign-off and approval workflow |

---

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

This assessment is **integration and distribution-focused**. You document HOW intelligence flows INTO security tools and OUT to stakeholders - not how intelligence is collected (A.5.7.1) or analysed (A.5.7.2), but where it goes and what happens with it.

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
1. List EVERY security tool in [Organisation]'s environment:

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
- ✓ Automation maximised (reduce manual distribution)
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
   - Who authorised/executed the action?
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
- ✓ Business impact justified (not exaggerated, not minimised)
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
- ✓ Negative feedback analysed and addressed
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
Organisations must regularly review and update their risk assessment based on changes in:

- Threat landscape
- Vulnerabilities discovered
- Business context changes
- Control effectiveness

**Threat intelligence is a PRIMARY INPUT to this process.**

**WHEN TO UPDATE RISK ASSESSMENT BASED ON TI:**

✅ **Trigger 1: New Threat Actor Targeting Organisation's Sector**

- Intelligence: Threat actor profile (from A.5.7.2 Sheet 12) shows targeting of [Organisation]'s sector
- Action: Update risk assessment to reflect new threat actor capability/motivation
- Example: APT group now targeting financial sector → increase likelihood ratings

✅ **Trigger 2: High-CVSS Vulnerability with Active Exploitation**

- Intelligence: VTL record (from A.5.7.2 Sheet 8) shows CVSS ≥8.0 with active exploitation
- Action: Update risk assessment for affected systems/data
- Example: CVE-2025-12345 (CVSS 9.3) actively exploited → increase risk rating for web servers

✅ **Trigger 3: Campaign Targeting Similar Organisations**

- Intelligence: Campaign tracking (from A.5.7.2 Sheet 13) shows attacks on similar organisations
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
| **Intelligence_Summary** | Brief summary (max 500 chars) | Ransomware group RansomX targeting financial sector, 15 organisations compromised Q4-2025. Backups primary target. No working decryptors ever provided despite ransom payment. |
| **Intelligence_Significance** | Why was this intelligence important? | Direct threat to [Organisation] as financial services provider, backup strategy at risk |
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

**END OF USER GUIDE**

---

*"An intelligence failure is not just a failure of information; it is a failure of sharing."*
— Anon

<!-- QA_VERIFIED: 2026-03-01 -->
