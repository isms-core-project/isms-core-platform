<!-- ISMS-CORE:IMP:ISMS-IMP-A.5.7.2-UG:framework:UG:a.5.7.2 -->
**ISMS-IMP-A.5.7.2-UG - Intelligence Collection & Analysis Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.7: Threat Intelligence

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.7.2-UG |
| **Version** | 1.0 |
| **Assessment Area** | Intelligence Collection, Analysis & Production Capabilities |
| **Related Policy** | ISMS-POL-A.5.7, Section 2.1 (Intelligence Collection Requirements), Section 2.2 (Intelligence Analysis and Production Requirements) |
| **Purpose** | Assess organizational capability to collect, analyze, and produce actionable threat intelligence including CVSS-integrated vulnerability-threat linkage |
| **Target Audience** | Threat Intelligence Analysts, SOC Team, Security Engineers, CISO, Compliance Officers, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Quarterly |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial consolidated specification (14 sheets) | ISMS Implementation Team |

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.5.7.2-TG.

---

## Assessment Overview

### Purpose & Scope

**Assessment Name:** ISMS-IMP-A.5.7.2 - Intelligence Collection & Analysis Assessment

#### What This Assessment Covers

This assessment evaluates [Organization]'s CAPABILITY to collect, analyze, and produce actionable threat intelligence. This is the operational "HOW do we process intelligence?" assessment that answers:

- How do we collect threat intelligence from multiple sources?
- What analysis methodologies do we use? (MITRE ATT&CK, Diamond Model, Kill Chain)
- What intelligence products do we produce? (strategic, tactical, operational)
- How skilled are our analysts?
- How effective is our VulnerabilityThreatLink (VTL) integration with Control A.8.8?
- How do we track threat actors and campaigns?
- What tools do we use for analysis?
- How mature are our intelligence processes?

#### Key Principle

This assessment is **operational and process-focused**. You document YOUR actual workflows, methodologies, and capabilities - not what sources you have (that's A.5.7.1) or where you distribute intelligence (that's A.5.7.3).

#### What You'll Document

- Intelligence collection workflows (automated and manual)
- Analysis methodologies (MITRE ATT&CK, Diamond Model, Kill Chain, CVSS)
- Intelligence production (reports, briefings, alerts, IOC feeds)
- Analyst skills matrix and training completion
- Quality metrics and KPIs
- **CRITICAL**: VulnerabilityThreatLink (VTL) records with CVSS 4.0/3.1 integration
- Threat actor profiles (maintained knowledge base)
- Campaign tracking (active threat campaigns)
- Analysis tools inventory
- Process maturity assessment
- Action items for capability improvements

#### How This Relates to Other A.5.7 Assessments

| Assessment | Focus | Relationship to A.5.7.2 |
|------------|-------|-------------------------|
| ISMS-IMP-A.5.7.1 | Source Portfolio | WHERE intelligence comes from (input to A.5.7.2) |
| **ISMS-IMP-A.5.7.2** | **Collection & Analysis** | **HOW intelligence is processed (this assessment)** |
| ISMS-IMP-A.5.7.3 | Integration & Distribution | WHERE intelligence is deployed (uses VTL from A.5.7.2) |
| ISMS-IMP-A.5.7.4 | Effectiveness Dashboard | OVERALL program metrics (consolidates A.5.7.2 data) |
| ISMS-IMP-A.5.7.5 | Standalone Dashboard | EXECUTIVE summary (uses A.5.7.2 production metrics) |

This assessment (A.5.7.2) is the CORE operational intelligence capability assessment - it depends on sources from A.5.7.1 and feeds into distribution (A.5.7.3).

### Who Should Complete This Assessment

#### Primary Stakeholders

1. **Threat Intelligence Team Lead** - Overall assessment ownership, process maturity
2. **Threat Intelligence Analysts** - Collection workflows, analysis methodologies, production tracking
3. **SOC Team** - Integration with security operations, VTL operational usage
4. **Security Engineers** - Technical integration points, tool architecture
5. **CISO** - Strategic intelligence requirements, program oversight

#### Required Skills

- Understanding of threat intelligence lifecycle (collection, processing, analysis, dissemination)
- Familiarity with MITRE ATT&CK framework
- Knowledge of CVSS 4.0/3.1 for vulnerability severity assessment
- Experience with threat actor profiling and campaign tracking
- Understanding of intelligence production methodologies

#### Time Commitment

- **Initial assessment:** 10-15 hours (comprehensive capability review across 14 sheets)
- **Quarterly updates:** 3-5 hours (update metrics, VTL records, campaigns, production tracking)
- **VTL maintenance:** Ongoing (create records as threats emerge - 15-30 min per record)

### Expected Outputs

Upon completion, you will have:

1. ✅ **Intelligence requirements documented** - Know what intelligence is needed and why (Sheet 2)
2. ✅ **Collection workflows mapped** - Understand how intelligence flows into analysis (Sheet 3)
3. ✅ **Analysis capabilities assessed** - Evaluate analytical methodologies and tools (Sheets 4, 11)
4. ✅ **Production tracking** - All intelligence products documented with quality metrics (Sheet 5)
5. ✅ **MITRE ATT&CK coverage** - Know which tactics/techniques are covered (Sheet 6)
6. ✅ **Quality metrics** - Track KPIs against targets (Sheet 7)
7. ✅ **VTL records created** - CVSS-integrated vulnerability-threat linkage operational (Sheet 8)
8. ✅ **Process maturity baseline** - Understand program maturity level (Sheet 9)
9. ✅ **Threat actor profiles** - Maintained knowledge base of adversaries (Sheet 12)
10. ✅ **Campaign tracking** - Active threat campaigns monitored (Sheet 13)
11. ✅ **Analysis tools inventory** - Complete tool landscape documented (Sheet 11)
12. ✅ **Action items** - Capability gaps identified with remediation plans (Sheet 10)
13. ✅ **Approved assessment** - Three-level approval workflow completed

---

## Prerequisites

### Information You'll Need

Before starting this assessment, gather:

#### 1. Access Required

- Threat Intelligence Platform (TIP) admin access or analyst accounts
- SIEM access for intelligence correlation
- EDR/XDR platforms (for VTL validation)
- Vulnerability management system (for VTL integration with A.8.8)
- MITRE ATT&CK Navigator or equivalent
- Analysis tools (OSINT collection, malware sandboxes, etc.)

#### 2. Documentation

- Intelligence requirements from stakeholders (if documented)
- Analysis playbooks or standard operating procedures
- Training records for analysts
- Historical intelligence production reports
- Threat actor profiles (if maintained)
- Campaign tracking notes or documents
- Tool architecture diagrams

#### 3. Historical Data

- Intelligence products produced (last 90 days minimum)
- Quality feedback from stakeholders
- Analyst performance reviews
- False positive/negative tracking
- VTL records created (if any exist)
- Campaign tracking data

#### 4. Policy Requirements

- **ISMS-POL-A.5.7, Section 2.1** (Intelligence Collection Requirements)
- **ISMS-POL-A.5.7, Section 2.2** (Intelligence Analysis and Production Requirements)
- **ISMS-POL-A.5.7, Section 2.6** (Vulnerability Management Integration Requirements - VTL schema)

### Required Tools

- Microsoft Excel (2016 or later) for workbook completion
- CVSS calculator (https://www.first.org/cvss/calculator/4.0 or 3.1)
- MITRE ATT&CK framework reference (https://attack.mitre.org)
- Access to NVD (National Vulnerability Database) for CVSS validation
- Screen capture tools (for evidence screenshots)

### Dependencies

This assessment depends on:

- **A.5.7.1 (Sources Assessment)** - Source IDs and capabilities must be documented first
- VTL records reference sources from A.5.7.1

However, outputs from this assessment are INPUT to:

- **A.5.7.3 (Integration & Distribution)** - VTL records (Sheet 8) feed into IOC deployment
- **A.5.7.4 (Effectiveness Dashboard)** - Quality metrics (Sheet 7) consolidated
- **A.8.8 (Vulnerability Management)** - VTL records trigger emergency patching workflows

---

## Workflow

### High-Level Process

```
1. PREPARE (Gather information)
   ↓
2. DEFINE REQUIREMENTS (Sheet 2: What intelligence do we need?)
   ↓
3. DOCUMENT COLLECTION (Sheet 3: How do we collect?)
   ↓
4. LOG RAW INTELLIGENCE (Sheet 4: Track ingest)
   ↓
5. TRACK PRODUCTION (Sheet 5: What products do we create?)
   ↓
6. MAP MITRE COVERAGE (Sheet 6: What techniques are covered?)
   ↓
7. MEASURE QUALITY (Sheet 7: Are we meeting targets?)
   ↓
8. CREATE VTL RECORDS (Sheet 8: Link vulnerabilities to threats with CVSS)
   ↓
9. ASSESS MATURITY (Sheet 9: How mature are our processes?)
   ↓
10. INVENTORY TOOLS (Sheet 11: What tools do we use?)
   ↓
11. PROFILE ACTORS (Sheet 12: Who are the adversaries?)
   ↓
12. TRACK CAMPAIGNS (Sheet 13: What campaigns are active?)
   ↓
13. IDENTIFY GAPS (Sheet 10: What needs improvement?)
   ↓
14. REVIEW & APPROVE
```

### Detailed Workflow

#### Phase 1: Preparation (2-3 hours)

**Objective:** Gather information and understand requirements

**Steps:**
1. Read this entire User Guide (Parts I and II)
2. Review **ISMS-POL-A.5.7, Section 2.1** (Collection Requirements)
3. Review **ISMS-POL-A.5.7, Section 2.2** (Analysis and Production Requirements)
4. Review **ISMS-POL-A.5.7, Section 2.6** (Vulnerability Management Integration - VTL)
5. Gather all prerequisites (see above)
6. Identify intelligence stakeholders (who needs intelligence?)
7. Schedule time with SMEs (analysts, SOC, security engineers)
8. Create working folder for evidence collection

**Deliverable:** Complete understanding of requirements and available data

---

#### Phase 2: Intelligence Requirements Definition (2-3 hours)

**Objective:** Complete Sheet 2 - Intelligence_Requirements

**Steps:**
1. List EVERY intelligence requirement your organization has
2. For each requirement:

   - Classify type (Strategic, Tactical, Operational, Technical)
   - Define what information is needed
   - Identify priority (Critical, High, Medium, Low)
   - Map to target sectors and regions
   - Identify threat categories
   - List which sources (from A.5.7.1) provide coverage
   - Assess coverage status (Adequate, Minimal, Gap)

3. Identify collection gaps where requirements are not met
4. Create remediation plans for critical gaps

**Deliverable:** Complete Sheet 2 with all intelligence requirements documented

**Quality Check:**

- ✓ All organizational intelligence needs documented
- ✓ Critical requirements have ≥2 sources (redundancy)
- ✓ Gaps identified with remediation plans
- ✓ Stakeholder needs represented

---

#### Phase 3: Collection Workflows Documentation (2-3 hours)

**Objective:** Complete Sheet 3 - Collection_Sources

**Steps:**
1. For each intelligence source (from A.5.7.1):

   - Document data format (STIX, JSON, CSV, etc.)
   - Document update frequency
   - Document coverage (geographic, sector, threat types)
   - Document integration status (automated vs. manual)
   - Document quality rating

2. Map sources to collection methods
3. Document integration platforms (TIP, SIEM, etc.)
4. Identify collection bottlenecks or issues

**Deliverable:** Complete Sheet 3 with collection workflows mapped

**Quality Check:**

- ✓ All sources from A.5.7.1 documented
- ✓ Automation status clear (automated vs. manual)
- ✓ Integration points documented
- ✓ Quality issues flagged

---

#### Phase 4: Raw Intelligence Logging (Ongoing)

**Objective:** Complete Sheet 4 - Raw_Intelligence_Log

**Steps:**
1. Log RAW intelligence as it arrives (daily activity)
2. For each intelligence item:

   - Assign unique Log_ID
   - Document source and timestamp
   - Classify intelligence type (IOC, Vulnerability, Campaign, etc.)
   - Assess priority and confidence level
   - Assign to analyst for processing
   - Set analysis deadline

3. Track processing status (Pending, In_Analysis, Completed, Discarded)

**Deliverable:** Running log of all raw intelligence ingested

**Quality Check:**

- ✓ All high-priority intelligence logged within 1 hour of receipt
- ✓ Critical intelligence assigned immediately
- ✓ Analysis deadlines set appropriately (Critical: same day, High: 2 days, etc.)
- ✓ No intelligence "lost" without logging

---

#### Phase 5: Production Tracking (Ongoing)

**Objective:** Complete Sheet 5 - Intelligence_Production

**Steps:**
1. Document EVERY intelligence product created:

   - Strategic reports (quarterly threat landscape, adversary trends)
   - Tactical briefs (campaign analysis, threat actor profiles)
   - Technical alerts (IOC feeds, vulnerability advisories)
   - Operational intelligence (hunting hypotheses, detection rules)

2. For each product:

   - Document production date and author
   - Identify target audience
   - Track distribution method
   - List sources used
   - Measure timeliness (expected vs. actual delivery)
   - Collect stakeholder feedback (quality ratings)
   - Document actions implemented (was it used?)

3. Calculate production metrics monthly

**Deliverable:** Complete record of all intelligence products

**Quality Check:**

- ✓ All products documented (no shadow intelligence)
- ✓ Timeliness tracked (≥80% delivered on time per policy)
- ✓ Stakeholder feedback collected
- ✓ Actionability demonstrated (intelligence used in decisions)

---

#### Phase 6: MITRE ATT&CK Coverage Mapping (Quarterly)

**Objective:** Complete Sheet 6 - MITRE_Mapping

**Steps:**
1. Map intelligence sources to MITRE ATT&CK techniques
2. For each technique (200+ techniques in Enterprise matrix):

   - Identify if intelligence coverage exists
   - List which sources provide coverage
   - Assess detection capability (High, Medium, Low, None)
   - Document if technique seen in wild recently
   - Prioritize gaps based on threat model

3. Generate gap remediation plans for critical techniques

**Deliverable:** Complete MITRE ATT&CK coverage assessment

**Quality Check:**

- ✓ All 14 tactics assessed
- ✓ Priority techniques have ≥2 sources
- ✓ Recently-used techniques (last 90 days) have detection capability
- ✓ Critical gaps have action items

---

#### Phase 7: Quality Metrics Tracking (Monthly)

**Objective:** Complete Sheet 7 - Quality_Metrics

**Steps:**
1. Calculate monthly KPIs:

   - Active collection sources (count from Sheet 3)
   - Average intelligence timeliness (from Sheet 5)
   - Requirements coverage percentage (from Sheet 2)
   - VTL records created (from Sheet 8)
   - Critical VTL response time (hours)
   - Products published (from Sheet 5)
   - Analyst training completion (from Sheet 4)
   - MITRE technique coverage (from Sheet 6)
   - Threat actor profiles maintained (from Sheet 12)
   - Campaigns tracked (from Sheet 13)

2. Compare actual vs. target for each KPI
3. Identify below-target metrics requiring attention
4. Update trends (month-over-month)

**Deliverable:** Complete quality dashboard with all KPIs

**Quality Check:**

- ✓ All KPIs calculated accurately
- ✓ Targets from policy documented
- ✓ Below-target metrics have action items
- ✓ Trends tracked for executive visibility

---

#### Phase 8: VulnerabilityThreatLink (VTL) Creation (Ongoing) - CRITICAL

**Objective:** Complete Sheet 8 - Vulnerability_Linked_Threats

**VTL Purpose:** Link vulnerabilities (CVEs) to active threat intelligence, enabling CVSS-based risk prioritization and emergency patching triggers.

**Steps:**

**WHEN to create VTL record:**
1. **Active Exploitation Detected**: Threat intelligence source reports a CVE is being actively exploited in the wild
2. **Mass Exploitation**: Widespread exploitation across multiple organizations or sectors
3. **Targeted Exploitation**: APT or nation-state actor targeting vulnerabilities relevant to [Organization]
4. **Zero-Day Discovery**: New vulnerability with no patch but active exploitation
5. **CISA KEV Addition**: CVE added to CISA Known Exploited Vulnerabilities catalog

**HOW to create VTL record:**

1. **Identify the Vulnerability:**

   - CVE identifier (CVE-YYYY-NNNNN)
   - If no CVE, use internal ID (INT-YYYY-NNNNN)

2. **Obtain CVSS Score:**

   - **Preferred**: CVSS 4.0 from NVD (https://nvd.nist.gov)
   - **Acceptable**: CVSS 3.1 from NVD or vendor advisory
   - **Required Fields**:
     * CVSS_Version (4.0 or 3.1)
     * CVSS_Base_Score (0.0-10.0, one decimal)
     * CVSS_Vector (full vector string)

3. **Document Threat Intelligence:**

   - Threat actor (if known): e.g., "APT28 (Fancy Bear)"
   - Threat actor type: Nation-State, Organized_Crime, Hacktivist, etc.
   - Exploitation status: No_Known_Exploit, PoC_Available, Active_Exploitation, Mass_Exploitation
   - Intelligence source: Reference source ID from A.5.7.1
   - Confidence level: High, Medium, Low, Unconfirmed
   - IOCs: IP addresses, domains, file hashes
   - TTPs: MITRE ATT&CK technique IDs (e.g., T1190, T1059)

4. **Assess Risk Impact:**

   - Critical assets affected: Yes/No
   - Affected systems count: Number of vulnerable systems in [Organization]
   - Business impact: What would happen if exploited?
   - Related incidents: Any incidents already occurred?

5. **AUTO-CALCULATED Priority Score:**

   - Formula: CVSS_Base_Score + Exploitation_Bonus + Critical_Assets_Bonus + Actor_Bonus (capped at 10.0)
   - DO NOT enter manually - this calculates automatically

6. **Determine Remediation Urgency:**

   - **Critical**: CVSS ≥8.0 AND Mass_Exploitation AND Critical_Assets_Affected
   - **High**: CVSS ≥7.0 AND Active_Exploitation
   - **Medium**: CVSS ≥4.0 OR PoC_Available
   - **Low**: CVSS <4.0 AND No_Known_Exploit

7. **Track Remediation:**

   - Remediation status: Open, In_Progress, Patched, Mitigated, Risk_Accepted, Verified
   - Assigned to: Team or person responsible
   - Link to vulnerability management system (A.8.8)

**VTL Integration with Control A.8.8:**

- VTL records automatically flag in vulnerability management dashboard
- High CVSS + active exploitation triggers emergency patching workflow
- Remediation status syncs bidirectionally between A.5.7.2 (Sheet 8) and A.8.8

**Example VTL Record:**

```
CVE-2024-12345
CVSS 4.0: 9.3 (CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N)
Threat Actor: APT28 (Fancy Bear)
Exploitation: Mass_Exploitation
Critical Assets: Yes (customer database servers)
Priority Score: 10.0 (auto-calculated: 9.3 + 2 + 2 + 1 = 14.3 capped at 10.0)
Remediation Urgency: Critical
Status: In_Progress
Assigned To: Infrastructure Team
```

**Deliverable:** VTL records for all actively exploited vulnerabilities

**Quality Check:**

- ✓ All CVSS scores from authoritative source (NVD preferred)
- ✓ CVSS vectors complete (not just base scores)
- ✓ Exploitation status verified (not assumed)
- ✓ Critical/High urgency records have assignments
- ✓ Priority Score auto-calculated (not manual entry)
- ✓ Integration with A.8.8 validated

---

#### Phase 9: Process Maturity Assessment (Quarterly)

**Objective:** Complete Sheet 9 - Process_Maturity

**Steps:**
1. Assess maturity across capability areas:

   - Intelligence requirements management
   - Collection automation
   - Analysis methodologies
   - Production workflows
   - Quality assurance
   - Integration with security operations
   - Analyst training and development
   - Tool maturity and integration

2. Use maturity levels (1-5):

   - **Level 1 - Initial**: Ad hoc, reactive, undocumented
   - **Level 2 - Repeatable**: Some processes defined but inconsistent
   - **Level 3 - Defined**: Documented processes, generally followed
   - **Level 4 - Managed**: Measured, monitored, controlled
   - **Level 5 - Optimizing**: Continuous improvement, industry-leading

3. Provide evidence for each maturity rating
4. Identify gaps between current and target maturity
5. Create improvement roadmap

**Deliverable:** Complete process maturity assessment with improvement plan

**Quality Check:**

- ✓ Honest assessment (not aspirational)
- ✓ Evidence provided for each rating
- ✓ Improvement targets realistic (typically +1 level per year)
- ✓ Executive buy-in for maturity improvements

---

#### Phase 10: Analysis Tools Inventory (Quarterly)

**Objective:** Complete Sheet 11 - Analysis_Tools

**Steps:**
1. Document EVERY tool used for threat intelligence analysis:

   - **TI Platforms**: MISP, ThreatConnect, Anomali, etc.
   - **OSINT Collection**: Maltego, Spiderfoot, Shodan, etc.
   - **Malware Analysis**: Sandboxes, disassemblers, debuggers
   - **Visualization**: MITRE ATT&CK Navigator, link analysis tools
   - **Data Processing**: Python scripts, SIEM queries, SQL databases
   - **Collaboration**: Wikis, Slack, ticketing systems

2. For each tool:

   - Document purpose and use cases
   - Assess utilization (high, medium, low)
   - Document licensing and costs
   - Assess analyst skill level with tool
   - Identify integration points
   - Note any limitations or issues

3. Identify tool gaps or redundancies
4. Plan tool consolidation or acquisitions

**Deliverable:** Complete analysis tools inventory

**Quality Check:**

- ✓ All tools documented (including scripts and manual processes)
- ✓ Costs tracked for budget planning
- ✓ Utilization assessed honestly
- ✓ Integration architecture clear

---

#### Phase 11: Threat Actor Profiling (Ongoing)

**Objective:** Complete Sheet 12 - Threat_Actor_Profiles

**Steps:**
1. For each threat actor relevant to [Organization]:

   - **Identification**: Name, aliases, attribution (nation-state, group)
   - **Motivation**: Financial gain, espionage, disruption, etc.
   - **Target Profile**: Which sectors, regions, organizations
   - **Capabilities**: Sophistication level, resources, tradecraft
   - **TTPs**: MITRE ATT&CK techniques commonly used
   - **Infrastructure**: Known C2 servers, malware families, tools
   - **Campaigns**: Historical campaigns attributed to actor
   - **Indicators**: IOCs associated with actor
   - **Intelligence Sources**: Which sources track this actor

2. Update profiles when new intelligence emerges
3. Link actors to active campaigns (Sheet 13)
4. Link actors to VTL records (Sheet 8) when exploitation attributed

**Deliverable:** Maintained threat actor knowledge base

**Quality Check:**

- ✓ Actors relevant to [Organization]'s threat model
- ✓ Profiles updated when new intelligence available
- ✓ Attribution confidence documented (Confirmed, Likely, Suspected)
- ✓ Cross-references to campaigns and VTL records

---

#### Phase 12: Campaign Tracking (Ongoing)

**Objective:** Complete Sheet 13 - Campaign_Tracking

**Steps:**
1. For each active threat campaign:

   - **Campaign Name**: Descriptive name or codename
   - **Threat Actor**: Attribution to known actor (if possible)
   - **Discovery Date**: When campaign first detected
   - **Status**: Active, Monitoring, Contained, Concluded
   - **Target Profile**: Which organizations/sectors targeted
   - **Attack Vectors**: How intrusions occur (phishing, exploits, etc.)
   - **Objectives**: What attackers are after (data theft, ransomware, etc.)
   - **TTPs**: MITRE ATT&CK techniques used
   - **IOCs**: Associated indicators (IPs, domains, hashes)
   - **CVEs Exploited**: Link to VTL records (Sheet 8)
   - **Affected Organizations**: Known victims
   - **Intelligence Sources**: Which sources reporting on campaign
   - **[Organization] Risk**: Assessment of risk to [Organization] (High, Medium, Low)

2. Update campaigns as intelligence evolves
3. Mark campaigns "Concluded" when no longer active
4. Link campaigns to VTL records when vulnerabilities exploited

**Deliverable:** Active campaign tracking dashboard

**Quality Check:**

- ✓ All active campaigns documented
- ✓ [Organization] risk assessed for each campaign
- ✓ IOCs extracted and ready for deployment (feeds into A.5.7.3)
- ✓ VTL linkage maintained (campaign exploiting CVE-XXXX)
- ✓ Status updated regularly (weekly for active campaigns)

---

#### Phase 13: Analyst Capabilities Assessment (Annual)

**Objective:** Complete Sheet 4 - Analyst_Capabilities

**Steps:**
1. For each analyst on TI team:

   - Document role and hire date
   - List certifications (GCTI, GIAC, CISSP, etc.)
   - Track training completed and hours (YTD and annual target)
   - Assess skills across competencies:
     * MITRE ATT&CK proficiency
     * Malware analysis
     * OSINT collection
     * Scripting/automation
     * Report writing
   - Document current workload
   - Track production metrics (reports authored, VTL records created)
   - Assess quality rating

2. Identify skill gaps across team
3. Create training plans to close gaps
4. Monitor training completion vs. targets

**Deliverable:** Complete analyst skills matrix

**Quality Check:**

- ✓ All analysts documented
- ✓ Training on track (actual ≥ target)
- ✓ Skill gaps identified with training plans
- ✓ Workload balanced (no "Overloaded" analysts)

---

#### Phase 14: Gap Identification & Action Items (Ongoing)

**Objective:** Complete Sheet 10 - Action_Items

**Steps:**
1. Review all assessment sheets (2-9, 11-13) for identified gaps
2. For each gap, create action item with:

   - Description of gap
   - Impact assessment (High, Medium, Low)
   - Source sheet reference
   - Assigned owner
   - Target completion date
   - Status (Not Started, In Progress, Completed, Blocked)
   - Notes and progress updates

3. Prioritize action items:

   - **Critical**: Prevents meeting policy requirements, high risk
   - **High**: Significant capability gap, impacts effectiveness
   - **Medium**: Improvement opportunity, non-critical
   - **Low**: Nice-to-have enhancement

4. Track progress weekly
5. Update status regularly

**Deliverable:** Complete action items register with progress tracking

**Quality Check:**

- ✓ All gaps from Sheets 2-9, 11-13 captured
- ✓ High/Critical items have owners and target dates
- ✓ Status current (updated weekly)
- ✓ Completed items have verification notes

---

#### Phase 15: Review & Approval (1-2 hours)

**Objective:** Obtain three-level approval for assessment

**Approval Workflow:**

**Level 1: Threat Intelligence Team Lead**

- Reviews assessment for completeness and accuracy
- Verifies all sheets populated correctly
- Confirms VTL records (Sheet 8) operational and accurate
- Confirms campaign tracking (Sheet 13) current
- Signs off on operational accuracy

**Level 2: CISO**

- Reviews assessment for policy compliance
- Verifies quality metrics (Sheet 7) meet targets
- Reviews VTL integration with Control A.8.8
- Reviews high-impact action items (Sheet 10)
- Signs off on strategic approval

**Level 3: Executive Management (if required)**

- Required if major capability gaps identified
- Required if significant budget needed for improvements
- Reviews analyst capability gaps and training needs
- Approves resources for capability improvements
- Signs off on executive approval

**Deliverable:** Fully approved assessment workbook

---

## Completing Each Sheet

### Sheet 1: Instructions

**User Action:** READ ONLY - No data entry required

**What's Provided:**

- Workbook overview (14 sheets)
- Data entry instructions
- CVSS integration guidance for VTL records (Sheet 8)
- Integration points with Control A.8.8
- Data validation rules explanation
- Color coding legend
- Contact information for Threat Intelligence Team
- Link to policy framework (ISMS-POL-A.5.7)

**Key Concepts:**

**VulnerabilityThreatLink (VTL) Schema:**

- **Purpose**: Link CVE vulnerabilities to active threat intelligence
- **CVSS Integration**: Uses CVSS 4.0 (preferred) or 3.1 for severity scoring
- **Priority Scoring**: Auto-calculated from CVSS + threat factors
- **Integration**: Bidirectional sync with Control A.8.8 vulnerability management
- **Emergency Triggers**: CVSS ≥8.0 + Mass Exploitation + Critical Assets = Emergency patching

**Intelligence Types:**

- **Strategic**: Long-term trends, adversary capabilities, geopolitical context
- **Operational**: Campaign analysis, TTP documentation, hunt hypotheses
- **Tactical**: IOCs, detection rules, immediate defensive actions
- **Technical**: Malware analysis, exploit details, vulnerability advisories

---

### Sheet 2: Intelligence_Requirements

**User Action:** DATA ENTRY - Document all intelligence requirements

**Columns to Complete:**

| Column | Instructions | Example |
|--------|--------------|---------|
| **Requirement_ID** | Auto-generated or manual | REQ-001 |
| **Intelligence_Type** | Dropdown: Strategic, Tactical, Operational, Technical | Tactical |
| **Requirement_Description** | What intelligence is needed? (max 300 chars) | APT campaign targeting financial sector with ransomware |
| **Priority** | Dropdown: Critical, High, Medium, Low | High |
| **Target_Sector** | Dropdown or multiple selection | Financial |
| **Target_Region** | Dropdown or multiple selection | Europe |
| **Threat_Category** | Dropdown: APT_Campaign, Ransomware, Data_Breach, etc. | Ransomware |
| **Collection_Source_1** | Reference to source from A.5.7.1 | SRC-001 |
| **Collection_Source_2** | Reference to source from A.5.7.1 | SRC-005 |
| **Collection_Source_3** | Reference to source from A.5.7.1 | N/A |
| **Collection_Method** | Dropdown: Automated_Feed, Manual_Research, etc. | Automated_Feed |
| **Coverage_Status** | Auto-calculated: Adequate (≥2 sources), Minimal (1), Gap (0) | Adequate |
| **Collection_Frequency** | Dropdown: Real-time, Hourly, Daily, Weekly, On_Demand | Real-time |
| **Last_Collected** | Date DD.MM.YYYY | [Date] |
| **Gap_Identified** | Auto-calculated: Yes if Coverage_Status=Gap | No |
| **Gap_Remediation** | If Gap: What's the plan? | N/A |
| **Responsible_Analyst** | Email or name | ti.analyst@example.com |
| **Notes** | Free text | Primary coverage from commercial TI platform |

**Tips:**

- Start with Critical and High priority requirements
- Requirements should reflect stakeholder needs (SOC, IR, executives, risk management)
- Ensure Critical requirements have ≥2 sources (redundancy)
- Be specific in descriptions (not just "ransomware intelligence" but "ransomware campaigns targeting financial sector in DACH region")

**Conditional Formatting:**

- Coverage_Status "Gap" → Red (critical issue)
- Coverage_Status "Minimal" → Yellow (single point of failure)
- Priority "Critical" + Coverage_Status "Gap" → Bold red (immediate attention)

---

### Sheet 3: Collection_Sources

**User Action:** DATA ENTRY - Document collection workflows for each source

**Purpose:** Map sources from A.5.7.1 to actual collection processes

**Columns to Complete:**

| Column | Instructions | Example |
|--------|--------------|---------|
| **Source_ID** | From A.5.7.1 | SRC-001 |
| **Source_Name** | From A.5.7.1 | CrowdStrike Falcon Intelligence |
| **Source_Type** | Dropdown: Commercial_Feed, Open_Source, Government, etc. | Commercial_Feed |
| **Data_Format** | Dropdown: STIX, JSON, CSV, RSS, API, Email, Portal | STIX |
| **Update_Frequency** | Dropdown: Real-time, Hourly, Daily, Weekly, On_Demand | Real-time |
| **Coverage_Geographic** | Comma-separated regions | Global |
| **Coverage_Sector** | Comma-separated sectors | All |
| **Coverage_Threat_Types** | Free text | APT, Ransomware, Malware, Vulnerabilities |
| **Integration_Status** | Dropdown: Integrated, Manual, Planned, Deprecated | Integrated |
| **Integration_Platform** | TIP name if integrated | MISP |
| **Cost_Annual** | Optional currency value | 75000.00 |
| **Contract_Expiry** | Date DD.MM.YYYY | 31.12.2025 |
| **Primary_Contact** | Vendor contact | support@crowdstrike.com |
| **Data_Quality_Rating** | Dropdown: Excellent, Good, Fair, Poor | Excellent |
| **Last_Review_Date** | Date DD.MM.YYYY | 15.12.2025 |
| **Notes** | Free text | Critical source for APT intelligence |

**Tips:**

- Pull source list from A.5.7.1 (don't retype)
- Focus on HOW intelligence is collected (automated vs. manual)
- Document actual integration status (not aspirational)
- Update quality ratings based on recent performance

---

### Sheet 4: Raw_Intelligence_Log

**User Action:** DATA ENTRY (ONGOING) - Log intelligence as it arrives

**Purpose:** Audit trail of raw intelligence ingestion

**Columns to Complete:**

| Column | Instructions | Example |
|--------|--------------|---------|
| **Log_ID** | Auto-generated (LOG-YYYYMMDD-NNNN) | LOG-20260121-0001 |
| **Timestamp** | DateTime DD.MM.YYYY HH:MM | 21.01.2026 14:30 |
| **Source_ID** | Dropdown from Sheet 3 | SRC-001 |
| **Intelligence_Type** | Dropdown: IOC, Vulnerability, Campaign, Threat_Actor, etc. | Vulnerability |
| **Raw_Data_Summary** | Free text (max 500 chars) | CVE-2025-12345 active exploitation by APT28 |
| **Confidence_Level** | Dropdown: High, Medium, Low, Unconfirmed | High |
| **Classification** | Dropdown: TLP_RED, TLP_AMBER, TLP_GREEN, TLP_WHITE | TLP_AMBER |
| **Priority** | Dropdown: Critical, High, Medium, Low, Info | Critical |
| **Processed_Status** | Dropdown: Pending, In_Analysis, Completed, Discarded | Pending |
| **Assigned_Analyst** | Email | analyst@example.com |
| **Analysis_Deadline** | Date DD.MM.YYYY | 21.01.2026 |
| **Related_Requirements** | Comma-separated REQ IDs | REQ-001, REQ-005 |
| **Notes** | Free text | Requires urgent analysis, emergency patching likely |

**Tips:**

- Log Critical intelligence within 15 minutes of receipt
- Set realistic analysis deadlines (Critical: same day, High: 2 days, Medium: 1 week)
- Track everything (don't lose intelligence in email or Slack)
- Update Processed_Status as analysis progresses

**Conditional Formatting:**

- Priority "Critical" + Status "Pending" → Red (urgent action needed)
- Analysis_Deadline overdue → Bold red

---

### Sheet 5: Intelligence_Production

**User Action:** DATA ENTRY (ONGOING) - Document every intelligence product

**Purpose:** Track what intelligence products are created and their quality

**Columns to Complete:**

| Column | Instructions | Example |
|--------|--------------|---------|
| **Product_ID** | Auto-generated (PROD-YYYYMMDD-NN) | PROD-20260121-01 |
| **Product_Type** | Dropdown: Strategic_Report, Tactical_Brief, Technical_Alert, etc. | Tactical_Brief |
| **Product_Title** | Free text | APT28 Credential Harvesting Campaign Q1 2026 |
| **Intelligence_Level** | Dropdown: Strategic, Operational, Tactical | Tactical |
| **Production_Date** | Date DD.MM.YYYY | 21.01.2026 |
| **Author** | Analyst name | Senior TI Analyst |
| **Reviewer** | Reviewer name | TI Team Lead |
| **Target_Audience** | Dropdown: Executive, Technical, SOC, IT_Ops, All_Staff | Technical |
| **Distribution_Method** | Dropdown: Email, Portal, API, Briefing, Report | Email |
| **Sources_Used** | Comma-separated Source IDs | SRC-001, SRC-003, SRC-007 |
| **Timeliness_Target** | Days expected | 3 |
| **Timeliness_Actual** | Days taken | 2 |
| **Timeliness_Met** | Auto-calculated: Yes if Actual ≤ Target | Yes |
| **Quality_Score** | Dropdown: Excellent, Good, Acceptable, Poor, N/A | Good |
| **Quality_Feedback** | Free text stakeholder feedback | "Actionable IOCs, deployed to SIEM" |
| **Actions_Implemented** | Number of actions taken based on product | 5 |
| **Impact_Rating** | Dropdown: High, Medium, Low, None | High |
| **Notes** | Free text | Led to emergency patching of 15 servers |

**Tips:**

- Document EVERY product (even internal notes if distributed)
- Collect stakeholder feedback actively (don't assume)
- Track actionability (was intelligence actually used?)
- Celebrate successes (High impact products with actions implemented)

**Conditional Formatting:**

- Timeliness_Met "No" → Yellow (missed deadline)
- Quality_Score "Poor" → Red (quality issue)
- Impact_Rating "High" + Actions_Implemented > 0 → Green (success!)

---

### Sheet 6: MITRE_Mapping

**User Action:** DATA ENTRY (QUARTERLY) - Map ATT&CK technique coverage

**Purpose:** Understand which MITRE ATT&CK techniques have intelligence coverage

**Structure:** Matrix with tactics and techniques

**Columns:**

- **MITRE_Tactic**: Dropdown (14 tactics)
- **MITRE_Technique_ID**: Technique ID (e.g., T1190)
- **Technique_Name**: Technique name
- **Coverage_Status**: Dropdown (Covered, Partial, Gap)
- **Sources_Covering**: Comma-separated source IDs
- **Detection_Capability**: Dropdown (High, Medium, Low, None)
- **Last_Seen_In_Wild**: Date if technique observed in campaigns
- **Priority_For_Coverage**: Dropdown (Critical, High, Medium, Low)
- **Gap_Remediation_Plan**: If Gap: what's the plan?

**Tips:**

- Use MITRE ATT&CK Navigator for visualization
- Focus on techniques seen in wild (last 90 days) first
- Prioritize based on [Organization]'s threat model
- Critical gaps = technique seen recently + no coverage + high impact

**Conditional Formatting:**

- Coverage_Status "Gap" + Priority "Critical" → Red
- Detection_Capability "None" + Last_Seen < 90 days → Orange

---

### Sheet 7: Quality_Metrics

**User Action:** DATA ENTRY (MONTHLY) - Calculate and track KPIs

**Purpose:** Track performance against policy targets

**Metrics to Track:**

| Metric | Source | Target | How to Calculate |
|--------|--------|--------|------------------|
| **Collection_Sources_Active** | Sheet 3 | N/A | Count where Status="Active" |
| **Average_Intelligence_Timeliness** | Sheet 5 | ≤3 days | AVG(Timeliness_Actual) |
| **Requirements_Coverage_Percent** | Sheet 2 | ≥90% | (Adequate + Minimal) / Total × 100% |
| **VTL_Records_Created_MTD** | Sheet 8 | ≥5/month | Count new VTL records this month |
| **Critical_VTL_Response_Time_Hours** | Sheet 8 | <4 hours | Time from discovery to VTL creation for Critical |
| **Products_Published_MTD** | Sheet 5 | ≥10/month | Count products this month |
| **Analyst_Training_Completion_Percent** | Sheet 4 | ≥80% | AVG(Training_Hours / Target_Hours) × 100% |
| **MITRE_Technique_Coverage_Percent** | Sheet 6 | ≥70% | (Covered + Partial) / Total × 100% |
| **Threat_Actor_Profiles_Active** | Sheet 12 | ≥10 | Count active profiles |
| **Campaigns_Tracked_Active** | Sheet 13 | ≥3 | Count active campaigns |

**Tips:**

- Calculate monthly, track trends
- Compare actual vs. target for each metric
- Below-target metrics require action items
- Present to CISO monthly

**Conditional Formatting:**

- Status "Below Target" → Red
- Status "At Target" → Green
- Status "Above Target" → Dark Green

---

### Sheet 8: Vulnerability_Linked_Threats (VTL) - CRITICAL

**User Action:** DATA ENTRY (ONGOING) - Create VTL records for exploited vulnerabilities

**Purpose:** **CRITICAL INTEGRATION WITH CONTROL A.8.8** - Link CVE vulnerabilities to active threat intelligence with CVSS scoring

**When to Create VTL Record:**
1. Intelligence reports CVE being actively exploited
2. Mass exploitation detected in wild
3. Targeted exploitation by APT/nation-state
4. Zero-day with active exploitation
5. CVE added to CISA KEV catalog

**Columns to Complete:**

| Column | Instructions | Example |
|--------|--------------|---------|
| **Link_ID** | Auto-generated (VTL-YYYYMMDD-NNNN) | VTL-20260121-0001 |
| **Vulnerability_ID** | CVE-YYYY-NNNNN or internal ID | CVE-2025-12345 |
| **CVSS_Version** | Dropdown: 4.0, 3.1 | 4.0 |
| **CVSS_Base_Score** | Number 0.0-10.0, 1 decimal | 9.3 |
| **CVSS_Vector** | Full CVSS vector string (max 200 chars) | CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N |
| **Threat_Actor** | Free text if known | APT28 (Fancy Bear) |
| **Threat_Actor_Type** | Dropdown: Nation-State, Organized_Crime, etc. | Nation-State |
| **Exploitation_Status** | Dropdown: No_Known_Exploit, PoC_Available, Active_Exploitation, Mass_Exploitation | Mass_Exploitation |
| **Intelligence_Source** | Source_ID from A.5.7.1 | SRC-001 |
| **Confidence_Level** | Dropdown: High, Medium, Low, Unconfirmed | High |
| **Discovery_Date** | Date DD.MM.YYYY | 21.01.2026 |
| **Last_Updated** | Auto TODAY() | 21.01.2026 |
| **IOCs** | Comma-separated indicators | 192.0.2.100, malicious.example.com |
| **TTPs** | Comma-separated MITRE IDs | T1190, T1059 |
| **Attack_Vector** | Free text | Network - Remote unauthenticated |
| **Priority_Score** | AUTO-CALCULATED (do not enter manually) | 10.0 |
| **Remediation_Urgency** | Dropdown: Critical, High, Medium, Low, Info | Critical |
| **Business_Impact** | Free text | Would expose customer PII database |
| **Affected_Systems_Count** | Number ≥0 | 47 |
| **Critical_Assets_Affected** | Dropdown: Yes, No | Yes |
| **Remediation_Status** | Dropdown: Open, In_Progress, Patched, Mitigated, Risk_Accepted, Verified | Open |
| **Assigned_To** | Team or person | Infrastructure Team |
| **Related_Incidents** | Comma-separated incident IDs if applicable | INC-2026-001 |
| **Notes** | Free text (max 500 chars) | CISA KEV listing, emergency patching required |

**Priority_Score Formula (AUTO-CALCULATED):**

```
Priority_Score = MIN(10, 
  CVSS_Base_Score 

  + IF(Exploitation_Status="Mass_Exploitation", 2, IF("Active_Exploitation", 1, 0))
  + IF(Critical_Assets_Affected="Yes", 2, 0)
  + IF(Threat_Actor_Type="Nation-State", 1, 0)

)
```

**CVSS Vector Examples:**

- **CVSS 4.0**: `CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N`
- **CVSS 3.1**: `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H`

**CVSS Sources:**

- **NVD** (National Vulnerability Database): https://nvd.nist.gov
- **Vendor Advisories**: Vendor-published CVSS scores
- **CISA KEV**: https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- **Threat Intelligence Platforms**: Commercial TI feeds with CVSS

**Conditional Formatting:**

- **CVSS ≥9.0** → Red (#DC143C) - Critical
- **CVSS 7.0-8.9** → Orange (#FF8C00) - High
- **CVSS 4.0-6.9** → Yellow (#FFD700) - Medium
- **CVSS <4.0** → Green (#90EE90) - Low
- **CVSS ≥9.0 + Mass_Exploitation** → BRIGHT RED + BOLD (Emergency!)
- **CVSS ≥7.0 + Active_Exploitation** → RED + BOLD

**Integration Workflow with Control A.8.8:**
1. TI analyst discovers active exploitation → Creates VTL record with CVSS
2. Priority_Score auto-calculated
3. VTL record automatically flags in A.8.8 vulnerability dashboard
4. High CVSS + active exploitation triggers emergency patching workflow
5. Vulnerability manager updates Remediation_Status
6. Status syncs back to Sheet 8
7. TI analyst verifies remediation

**Tips:**

- Use CVSS 4.0 when available (preferred)
- Copy full CVSS vector (not just base score)
- Verify exploitation status (don't assume)
- Update as threat evolves (exploitation status may change)
- Link to related incidents (demonstrates value)

---

### Sheet 9: Process_Maturity

**User Action:** DATA ENTRY (QUARTERLY) - Assess process maturity

**Purpose:** Benchmark TI program maturity, identify improvement areas

**Capability Areas:**
1. Intelligence Requirements Management
2. Collection Automation
3. Analysis Methodologies
4. Production Workflows
5. Quality Assurance
6. Integration with Security Operations
7. Analyst Training and Development
8. Tool Maturity and Integration

**Maturity Levels:**

| Level | Name | Description |
|-------|------|-------------|
| 1 | Initial | Ad hoc, reactive, undocumented processes |
| 2 | Repeatable | Some processes defined but inconsistently followed |
| 3 | Defined | Documented processes, generally followed |
| 4 | Managed | Measured, monitored, controlled processes |
| 5 | Optimizing | Continuous improvement, industry-leading |

**Columns:**

- **Capability_Area**
- **Current_Maturity_Level** (1-5)
- **Evidence** (what demonstrates this level?)
- **Target_Maturity_Level** (1-5)
- **Gap** (Target - Current)
- **Improvement_Actions** (what's needed to reach target?)
- **Target_Date** (when will target be reached?)

**Tips:**

- Be honest (not aspirational) - auditors will verify
- Provide specific evidence for each rating
- Target improvements realistically (typically +1 level per year)
- Focus on high-impact capability areas first

---

### Sheet 10: Action_Items

**User Action:** DATA ENTRY (ONGOING) - Track all capability gaps and improvements

**Purpose:** Central register of all improvement actions

**Columns:**

| Column | Instructions | Example |
|--------|--------------|---------|
| **Action_ID** | Auto-generated | ACT-2026-001 |
| **Source_Sheet** | Which sheet identified this gap? | Sheet 6: MITRE_Mapping |
| **Issue_Description** | What's the problem? (max 500 chars) | T1190 (Exploit Public-Facing Application) has no intelligence coverage but seen in 3 recent campaigns |
| **Impact** | Dropdown: Critical, High, Medium, Low | High |
| **Priority** | Dropdown: P1-Critical, P2-High, P3-Medium, P4-Low | P2-High |
| **Assigned_To** | Email | ti.team.lead@example.com |
| **Target_Date** | Date DD.MM.YYYY | 28.02.2026 |
| **Status** | Dropdown: Not Started, In Progress, Completed, Blocked, Cancelled | In Progress |
| **Status_Notes** | Free text | Evaluating additional sources with T1190 coverage |
| **Completion_Date** | Date when completed | [blank] |
| **Verification** | How will completion be verified? | Re-assess Sheet 6, verify T1190 has ≥2 sources |

**Action Item Sources:**

- **Sheet 2**: Coverage gaps (requirements with no sources)
- **Sheet 3**: Collection issues (manual processes that should be automated)
- **Sheet 4**: Analyst skill gaps, training deficits
- **Sheet 5**: Production quality issues, timeliness failures
- **Sheet 6**: MITRE ATT&CK coverage gaps
- **Sheet 7**: KPIs below target
- **Sheet 8**: High-impact VTL records requiring urgent remediation
- **Sheet 9**: Process maturity gaps
- **Sheet 11**: Tool gaps or limitations
- **Sheet 12**: Threat actor intelligence gaps
- **Sheet 13**: Campaign monitoring gaps

**Priority Definitions:**

- **P1-Critical**: Policy violation, complete capability gap, active risk
- **P2-High**: Significant gap impacting effectiveness
- **P3-Medium**: Improvement opportunity, non-critical
- **P4-Low**: Nice-to-have enhancement

**Tips:**

- Create action items immediately when gaps identified
- Assign to person with authority to resolve
- Update status weekly (minimum for P1/P2)
- Verify completion before marking "Completed"

**Conditional Formatting:**

- Priority "P1-Critical" → Red background
- Target_Date overdue + Status ≠ "Completed" → Bold red
- Status "Blocked" → Yellow background

---

### Sheet 11: Analysis_Tools

**User Action:** DATA ENTRY (QUARTERLY) - Document all analysis tools

**Purpose:** Complete inventory of tools used for TI analysis

**Columns:**

| Column | Instructions | Example |
|--------|--------------|---------|
| **Tool_ID** | Auto-generated | TOOL-001 |
| **Tool_Name** | Product name | MISP |
| **Tool_Category** | Dropdown: TI_Platform, OSINT, Malware_Analysis, Visualization, etc. | TI_Platform |
| **Vendor** | Provider name | CIRCL |
| **Purpose** | Free text | Central threat intelligence platform for collection, analysis, sharing |
| **Utilization** | Dropdown: High, Medium, Low | High |
| **License_Type** | Dropdown: Commercial, Open_Source, Subscription, Internal | Open_Source |
| **Annual_Cost** | Currency (if commercial) | 0 |
| **Analyst_Skill_Level** | Dropdown: Expert, Advanced, Intermediate, Novice | Advanced |
| **Integration_Points** | Comma-separated systems | SIEM, EDR, Firewall |
| **Limitations** | Free text | Limited built-in visualization |
| **Notes** | Free text | Core platform, all analysts trained |

**Tips:**

- Include scripts and manual processes (not just commercial tools)
- Be honest about utilization (low-use tools may be candidates for retirement)
- Document skill levels honestly (identifies training needs)
- Identify integration gaps

---

### Sheet 12: Threat_Actor_Profiles

**User Action:** DATA ENTRY (ONGOING) - Maintain threat actor knowledge base

**Purpose:** Centralized repository of adversary intelligence

**Columns:**

| Column | Instructions | Example |
|--------|--------------|---------|
| **Actor_ID** | Auto-generated | ACTOR-001 |
| **Actor_Name** | Primary name | APT28 |
| **Actor_Aliases** | Comma-separated | Fancy Bear, Sofacy, Sednit |
| **Attribution** | Nation-State or Group | Russian Federation (GRU) |
| **Attribution_Confidence** | Dropdown: Confirmed, Likely, Suspected, Unknown | Confirmed |
| **First_Observed** | Date | 01.01.2007 |
| **Status** | Dropdown: Active, Dormant, Disbanded | Active |
| **Motivation** | Dropdown: Espionage, Financial, Disruption, etc. | Espionage |
| **Target_Sectors** | Comma-separated | Government, Military, Defense, Media |
| **Target_Regions** | Comma-separated | Europe, North America |
| **Sophistication** | Dropdown: Advanced, Intermediate, Basic | Advanced |
| **Capabilities** | Free text | Custom malware development, exploit creation, supply chain compromise |
| **Primary_TTPs** | Comma-separated MITRE IDs | T1566.001, T1078, T1053.005 |
| **Infrastructure** | Known C2, malware families | Zebrocy, X-Agent, Sofacy |
| **Associated_Campaigns** | Link to Sheet 13 campaign IDs | CAMP-001, CAMP-015 |
| **Intelligence_Sources** | Which sources track this actor? | SRC-001, SRC-003 |
| **Threat_To_Org** | Dropdown: High, Medium, Low | Medium |
| **Notes** | Free text | Active targeting of government entities in Europe |

**Tips:**

- Focus on actors relevant to [Organization]'s threat model
- Update when new intelligence emerges
- Link to campaigns (Sheet 13) and VTL records (Sheet 8)
- Document threat level to [Organization] realistically

---

### Sheet 13: Campaign_Tracking

**User Action:** DATA ENTRY (ONGOING) - Track active threat campaigns

**Purpose:** Monitor active campaigns that may affect [Organization]

**Columns:**

| Column | Instructions | Example |
|--------|--------------|---------|
| **Campaign_ID** | Auto-generated | CAMP-001 |
| **Campaign_Name** | Descriptive name | Winter Vivern Credential Harvesting |
| **Threat_Actor_ID** | Link to Sheet 12 | ACTOR-005 |
| **Threat_Actor_Name** | Auto-populated from Sheet 12 | Winter Vivern |
| **Discovery_Date** | Date | 15.12.2025 |
| **Status** | Dropdown: Active, Monitoring, Contained, Concluded | Active |
| **Target_Profile** | Who's being targeted? | Government agencies in Eastern Europe |
| **Attack_Vectors** | Comma-separated | Phishing emails, watering hole attacks |
| **Campaign_Objectives** | What do attackers want? | Credential theft for espionage |
| **TTPs_Used** | Comma-separated MITRE IDs | T1566.001, T1189, T1078 |
| **IOCs** | Comma-separated | 192.0.2.50, evil.example.com, hash:abc123... |
| **CVEs_Exploited** | Comma-separated CVE IDs, link to VTL (Sheet 8) | CVE-2025-11111 |
| **CVEs_CVSS_Max** | Highest CVSS score of exploited CVEs | 8.1 |
| **Affected_Organizations** | Known victims | Ministry of Defense (Country X) |
| **Intelligence_Sources** | Which sources reporting? | SRC-001, SRC-007 |
| **Org_Risk_Assessment** | Dropdown: High, Medium, Low | Low |
| **Org_Risk_Justification** | Why this risk level? | [Organization] not in target profile, no similar infrastructure |
| **Monitoring_Actions** | What are we doing? | IOCs deployed to SIEM, hunting for similar TTPs |
| **Last_Updated** | Date | 21.01.2026 |
| **Notes** | Free text | Campaign primarily targeting government, low direct risk |

**Tips:**

- Update Active campaigns weekly (at minimum)
- Mark "Concluded" when campaign no longer active
- Link CVEs to VTL records (Sheet 8)
- Assess risk to [Organization] honestly
- Extract IOCs for deployment (feeds into A.5.7.3)

---

### Sheet 14: Metadata

**User Action:** AUTO-POPULATED - Review only

**Purpose:** Document provenance and version control

**What's Included:**

- Workbook generation date/time
- Generator script version
- Assessment version number
- Policy framework reference (ISMS-POL-A.5.7)
- IMP specification reference (ISMS-IMP-A.5.7.2 v2.0)
- Total sheets in workbook
- Named ranges defined
- Change log

---

## Evidence Collection

### What Evidence to Collect

**Per Assessment Phase:**

**Phase 2 (Intelligence Requirements):**

- Stakeholder interviews documenting intelligence needs
- Risk assessment showing threat-based requirements
- Executive directives or board mandates

**Phase 3 (Collection Workflows):**

- TIP integration architecture diagrams
- API configuration screenshots
- STIX feed examples
- Collection automation scripts

**Phase 5 (Production Tracking):**

- Sample intelligence products (redact sensitive)
- Stakeholder feedback emails or surveys
- Metrics showing production volume and timeliness

**Phase 6 (MITRE Mapping):**

- ATT&CK Navigator exports showing coverage
- Gap analysis spreadsheets
- Prioritization matrices

**Phase 7 (Quality Metrics):**

- Monthly KPI dashboards
- Trend charts (month-over-month)
- Executive reports showing metrics

**Phase 8 (VTL Records):**

- NVD CVSS score screenshots
- Threat intelligence reports documenting exploitation
- Vulnerability scan results showing affected systems
- Emergency patching approvals/communications
- Remediation verification (patch deployment confirmations)

**Phase 9 (Process Maturity):**

- Process documentation showing maturity level
- Training completion records
- Tool integration architecture
- Quality assurance reports

**Phase 11 (Analysis Tools):**

- Tool architecture diagrams
- License agreements
- Integration configurations
- Training materials

**Phase 12 (Threat Actor Profiles):**

- Intelligence reports on actors
- Attribution analysis
- TTP mapping documentation

**Phase 13 (Campaign Tracking):**

- Campaign intelligence reports
- IOC extraction worksheets
- Risk assessments
- Monitoring dashboards

### Evidence Storage

**Organization:**
```
Evidence/
├── 2026-Q1/
│   ├── Requirements/
│   ├── Collection/
│   ├── Production/
│   ├── MITRE-Mapping/
│   ├── VTL-Records/  (CRITICAL)
│   │   ├── CVE-2026-12345-NVD-screenshot.png
│   │   ├── CVE-2026-12345-exploitation-report.pdf
│   │   ├── CVE-2026-12345-remediation-approval.pdf
│   │   └── ...
│   ├── Process-Maturity/
│   ├── Threat-Actors/
│   ├── Campaigns/
│   └── Tools/
└── 2026-Q2/
    └── ...
```

**Retention:** 3 years (ISO 27001 audit requirement)

---

## Common Pitfalls

### Pitfall 1: Incomplete VTL Records

**Problem:** VTL records created without proper CVSS validation or threat intelligence verification

**Symptoms:**

- CVSS scores don't match NVD
- Exploitation status unverified (assumed)
- Missing CVSS vectors (only base scores)
- No threat actor attribution
- No IOCs documented

**Solution:**

- ALWAYS verify CVSS from NVD (https://nvd.nist.gov)
- Copy full CVSS vector (not just score)
- Verify exploitation status from multiple sources
- Document threat actor if known (even if low confidence)
- Extract all available IOCs
- Link to source intelligence reports (Evidence_Link)

---

### Pitfall 2: No Integration with A.8.8

**Problem:** VTL records created but not integrated with vulnerability management

**Symptoms:**

- Vulnerability team unaware of active exploitation
- Emergency patching not triggered
- Remediation_Status never updated
- No bidirectional sync between A.5.7.2 and A.8.8

**Solution:**

- Establish integration workflow with vulnerability management team
- Share VTL Critical/High records immediately (within 4 hours)
- Track remediation status updates from A.8.8
- Hold weekly syncs between TI and vulnerability teams
- Demonstrate integration in audits (key compliance requirement)

---

### Pitfall 3: Stale Campaign Tracking

**Problem:** Sheet 13 filled in once but never updated

**Symptoms:**

- Campaigns marked "Active" but concluded months ago
- No updates in Last_Updated field
- Risk assessments outdated
- IOCs not extracted for deployment

**Solution:**

- Update Active campaigns WEEKLY (minimum)
- Mark campaigns "Concluded" when no longer active (don't leave orphaned)
- Refresh risk assessments as campaigns evolve
- Extract IOCs for deployment to A.5.7.3
- Hold regular campaign review meetings

---

### Pitfall 4: Missing Process Maturity Evidence

**Problem:** Sheet 9 maturity levels not supported by evidence

**Symptoms:**

- Claims Level 4 "Managed" but no metrics exist
- Claims Level 5 "Optimizing" but no continuous improvement
- Auditor challenges maturity ratings
- Cannot provide documentation

**Solution:**

- Be honest (not aspirational) in maturity ratings
- Collect evidence BEFORE claiming maturity level
- Document processes before claiming Level 3+
- Track metrics before claiming Level 4+
- Implement continuous improvement before claiming Level 5

---

### Pitfall 5: Analyst Skill Gaps Not Addressed

**Problem:** Sheet 4 shows skill gaps but no training plans

**Symptoms:**

- Training_Hours below target for multiple analysts
- Critical skills (MITRE ATT&CK, CVSS) at Novice/Intermediate
- No training budget allocated
- Skills gaps same year-over-year

**Solution:**

- Create individual training plans for each analyst
- Budget for training (conferences, certifications, courses)
- Track training completion monthly
- Measure skill improvement (re-assess annually)
- Tie training to career development

---

## Quality Checklist

**Before submitting assessment for approval, verify:**

### Completeness

- [ ] **Sheet 2:** All intelligence requirements documented with sources
- [ ] **Sheet 3:** All sources from A.5.7.1 documented with collection workflows
- [ ] **Sheet 4:** Raw intelligence logging operational (if performing daily TI operations)
- [ ] **Sheet 5:** Intelligence production tracking current (last 90 days minimum)
- [ ] **Sheet 6:** MITRE ATT&CK coverage assessed, gaps identified
- [ ] **Sheet 7:** Quality metrics calculated, compared to targets
- [ ] **Sheet 8:** VTL records created for all actively exploited CVEs
- [ ] **Sheet 9:** Process maturity assessed with evidence
- [ ] **Sheet 10:** Action items documented for all gaps
- [ ] **Sheet 11:** Analysis tools inventory complete
- [ ] **Sheet 12:** Threat actor profiles for relevant adversaries
- [ ] **Sheet 13:** Active campaigns tracked and current

### Data Quality

- [ ] No "TBD", "Unknown", or blank required fields
- [ ] All dates in DD.MM.YYYY format
- [ ] All CVSS scores validated against NVD
- [ ] All CVSS vectors complete (not just base scores)
- [ ] VTL Priority_Score auto-calculated (not manual)
- [ ] Campaign Last_Updated within 7 days for Active campaigns
- [ ] Analyst training hours current (YTD)
- [ ] All formulas calculate correctly

### Evidence

- [ ] VTL records have NVD screenshots for CVSS validation
- [ ] VTL records have threat intelligence reports documenting exploitation
- [ ] Production tracking has stakeholder feedback
- [ ] MITRE coverage has ATT&CK Navigator exports
- [ ] Process maturity has supporting documentation
- [ ] Tools inventory has architecture diagrams

### Policy Compliance

- [ ] Intelligence requirements coverage ≥90% (Adequate + Minimal)
- [ ] Average production timeliness ≤3 days
- [ ] VTL Critical records response time <4 hours
- [ ] Products published ≥10 per month
- [ ] Analyst training ≥80% completion
- [ ] MITRE technique coverage ≥70%
- [ ] VTL records integrate with A.8.8 (bidirectional)

### Integration

- [ ] Sources reference A.5.7.1 source IDs correctly
- [ ] VTL records ready for use by A.5.7.3 (IOC deployment)
- [ ] Quality metrics ready for A.5.7.4 dashboard consolidation
- [ ] Integration with A.8.8 operational and verified

### Approvals

- [ ] Threat Intelligence Team Lead reviewed and approved
- [ ] CISO reviewed and approved
- [ ] Executive Management approved (if required)
- [ ] Approval dates documented
- [ ] Approval signatures obtained

---

## Review & Approval

### Three-Level Approval Process

**Level 1: Threat Intelligence Team Lead**

**Responsibilities:**

- Review assessment for completeness and operational accuracy
- Verify all sheets populated correctly
- Confirm VTL records operational and CVSS-validated
- Confirm campaign tracking current
- Verify analyst capabilities accurately reflected
- Review process maturity assessment
- Sign off on operational accuracy

**Approval Criteria:**

- All required sheets complete
- Quality checklist passed
- Evidence collected
- Integration with A.5.7.1 and A.8.8 verified

**Timeline:** 3-5 business days after submission

---

**Level 2: CISO**

**Responsibilities:**

- Review assessment for policy compliance
- Verify quality metrics meet targets (Sheet 7)
- Review VTL integration with Control A.8.8
- Review high-impact action items (Sheet 10)
- Assess process maturity and improvement plans (Sheet 9)
- Review analyst capability gaps and training plans (Sheet 4)
- Provide strategic guidance on capability development
- Sign off on strategic approval

**Approval Criteria:**

- Policy compliance verified
- Quality metrics meet or exceed targets
- VTL integration operational
- Critical action items have owners and realistic timelines
- Process improvement roadmap approved

**Timeline:** 5 business days after Team Lead approval

---

**Level 3: Executive Management (if required)**

**Trigger Conditions:**

- Major capability gaps requiring significant investment
- Analyst skill gaps requiring hiring or major training budget
- Process maturity improvements requiring organizational change
- Integration with A.8.8 requiring cross-team coordination and resources

**Responsibilities:**

- Review business justification for capability investments
- Approve budget for tools, training, or personnel
- Provide strategic direction on program development
- Approve cross-organizational integration initiatives

**Approval Criteria:**

- Business case justified
- Budget approved
- Strategic alignment confirmed
- Resources allocated

**Timeline:** 10 business days after CISO approval

---

### Documentation of Approvals

**Approval Sign-Off Section** (in workbook):

| Approval Level | Name | Role | Signature | Date |
|----------------|------|------|-----------|------|
| Level 1: Team Lead | [Name] | Threat Intelligence Team Lead | [Signature] | [DD.MM.YYYY] |
| Level 2: CISO | [Name] | Chief Information Security Officer | [Signature] | [DD.MM.YYYY] |
| Level 3: Executive | [Name] | [Title] | [Signature] | [DD.MM.YYYY] |

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
