**ISMS-IMP-A.5.7.2 - Intelligence Collection & Analysis Assessment**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.7: Threat Intelligence

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.7.2 |
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

This document consists of two parts:

- **PART I: USER COMPLETION GUIDE**
  - Assessment Overview
  - Prerequisites
  - Workflow
  - Completing Each Sheet
  - Evidence Collection
  - Common Pitfalls
  - Quality Checklist
  - Review & Approval

- **PART II: TECHNICAL SPECIFICATION**
  - Excel Workbook Structure
  - Sheet-by-Sheet Specifications
  - Formula Specifications
  - Integration Points
  - CVSS Integration Details


---

# PART I: USER COMPLETION GUIDE

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

**END OF PART I: USER COMPLETION GUIDE**

---

# PART II: TECHNICAL SPECIFICATION

## Excel Workbook Structure

### Workbook Properties

**File Name:** `ISMS_A_5_7_2_Collection_Analysis_Assessment_YYYYMMDD.xlsx`

**Example:** `ISMS_A_5_7_2_Collection_Analysis_Assessment_20260121.xlsx`

**Workbook Settings:**

- Format: Excel 2016+ (.xlsx)
- Calculation: Automatic
- Protection: Sheets protected (only yellow cells editable)
- Macros: None (VBA-free for security)
- External Links: References to ISMS-IMP-A.5.7.1 source IDs


**Total Sheets:** 14

**Tab Colors:**

- Instructions: Blue (#4472C4)
- Requirements & Collection (Sheets 2-4): Yellow (#FFD966)
- Production & Analysis (Sheets 5-6): Orange (#FFA500)
- Quality & Metrics (Sheet 7): Green (#70AD47)
- VTL & Critical (Sheet 8): Red (#C00000) - AUDIT CRITICAL
- Maturity & Actions (Sheets 9-10): Purple (#7030A0)
- Tools & Intelligence (Sheets 11-13): Teal (#00B0F0)
- Metadata: Gray (#D9D9D9)


---

## Sheet-by-Sheet Technical Specifications

# Sheet Specifications

## Sheet 1: Instructions

**Purpose**: Guide users through the workbook structure and data entry requirements

**Content**:

- Workbook overview (14 sheets)
- Data entry instructions
- CVSS integration in Sheet 8
- Integration points with Control 8.8
- Data validation rules
- Color coding legend
- Contact information for Threat Intelligence Team


---

## Sheet 2: Intelligence_Requirements

**Purpose**: Map collection capabilities to intelligence requirements

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Requirement_ID | Text | Auto-generated (REQ-NNN) | Yes | REQ-001 |
| Intelligence_Type | Dropdown | Strategic, Tactical, Operational, Technical | Yes | Tactical |
| Requirement_Description | Text | Free text (max 300 chars) | Yes | APT campaign targeting financial sector |
| Priority | Dropdown | Critical, High, Medium, Low | Yes | High |
| Target_Sector | Dropdown | Financial, Healthcare, Energy, Government, Technology, Other | No | Financial |
| Target_Region | Dropdown | Global, Europe, Americas, Asia_Pacific, Middle_East, Africa | No | Europe |
| Threat_Category | Dropdown | APT_Campaign, Ransomware, Data_Breach, DDoS, Supply_Chain, Insider, Other | Yes | APT_Campaign |
| Collection_Source_1 | Text | Reference to 5.7.1 | No | SRC-001 |
| Collection_Source_2 | Text | Reference to 5.7.1 | No | SRC-005 |
| Collection_Source_3 | Text | Reference to 5.7.1 | No | N/A |
| Collection_Method | Dropdown | Automated_Feed, Manual_Research, OSINT, Partnership, Internal_Telemetry | Yes | Automated_Feed |
| Coverage_Status | Formula | IF >= 2 sources: Adequate, =1: Minimal, =0: Gap | Auto | Adequate |
| Collection_Frequency | Dropdown | Real-time, Hourly, Daily, Weekly, On_Demand | Yes | Real-time |
| Last_Collected | Date | DD.MM.YYYY | No | 02.01.2025 |
| Gap_Identified | Formula | IF Coverage_Status=Gap: Yes | Auto | No |
| Gap_Remediation | Text | If Gap_Identified=Yes | Conditional | N/A |
| Responsible_Analyst | Text | Email or name | Yes | ti.analyst@example.com |
| Notes | Text | Free text | No | Primary coverage from commercial TI platform |

**Conditional Formatting**:

- Coverage_Status "Gap" → Red background
- Coverage_Status "Minimal" → Yellow background
- Priority "Critical" + Coverage_Status "Gap" → Bold red background


---

## Sheet 3: Collection_Sources

**Purpose**: Document intelligence collection sources and their characteristics

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Source_ID | Text | Auto-generated (SRC-NNN) | Yes | SRC-001 |
| Source_Name | Text | Free text | Yes | CrowdStrike Falcon Intelligence |
| Source_Type | Dropdown | Commercial_Feed, Open_Source, Government, Industry_Partnership, Internal | Yes | Commercial_Feed |
| Data_Format | Dropdown | STIX, JSON, CSV, RSS, API, Email, Portal | Yes | STIX |
| Update_Frequency | Dropdown | Real-time, Hourly, Daily, Weekly, On_Demand | Yes | Real-time |
| Coverage_Geographic | Text | Comma-separated regions | No | Global |
| Coverage_Sector | Text | Comma-separated sectors | No | All |
| Coverage_Threat_Types | Text | Free text | Yes | APT, Ransomware, Malware, Vulnerabilities |
| Integration_Status | Dropdown | Integrated, Manual, Planned, Deprecated | Yes | Integrated |
| Integration_Platform | Text | TIP name if integrated | No | MISP |
| Cost_Annual | Currency | >= 0, 2 decimals | No | 75000.00 |
| Contract_Expiry | Date | DD.MM.YYYY | No | 31.12.2025 |
| Primary_Contact | Text | Vendor contact | No | support@crowdstrike.com |
| Data_Quality_Rating | Dropdown | Excellent, Good, Fair, Poor | No | Excellent |
| Last_Review_Date | Date | DD.MM.YYYY | Yes | 15.12.2024 |
| Notes | Text | Free text | No | Critical source for APT intelligence |

**Conditional Formatting**:

- Integration_Status "Deprecated" → Gray background
- Contract_Expiry within 60 days → Yellow background
- Data_Quality_Rating "Poor" → Red background


---

## Sheet 4: Raw_Intelligence_Log

**Purpose**: Track raw intelligence ingestion for audit trail

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Log_ID | Text | Auto-generated (LOG-YYYYMMDD-NNNN) | Yes | LOG-20250109-0001 |
| Timestamp | DateTime | DD.MM.YYYY HH:MM | Yes | 09.01.2025 14:30 |
| Source_ID | Dropdown | From Sheet 3 | Yes | SRC-001 |
| Intelligence_Type | Dropdown | IOC, Vulnerability, Campaign, Threat_Actor, TTP, Malware, Other | Yes | Vulnerability |
| Raw_Data_Summary | Text | Free text (max 500 chars) | Yes | CVE-2024-12345 active exploitation by APT28 |
| Confidence_Level | Dropdown | High, Medium, Low, Unconfirmed | Yes | High |
| Classification | Dropdown | TLP_RED, TLP_AMBER, TLP_GREEN, TLP_WHITE | Yes | TLP_AMBER |
| Priority | Dropdown | Critical, High, Medium, Low, Info | Yes | Critical |
| Processed_Status | Dropdown | Pending, In_Analysis, Completed, Discarded | Yes | Pending |
| Assigned_Analyst | Text | Email | Yes | analyst@example.com |
| Analysis_Deadline | Date | DD.MM.YYYY | No | 10.01.2025 |
| Related_Requirements | Text | Comma-separated REQ IDs | No | REQ-001, REQ-005 |
| Notes | Text | Free text | No | Requires urgent analysis |

**Conditional Formatting**:

- Priority "Critical" + Processed_Status "Pending" → Red background
- Analysis_Deadline overdue → Bold red


---

## Sheet 5: Intelligence_Production

**Purpose**: Track intelligence products and quality metrics

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Product_ID | Text | Auto-generated (PROD-YYYYMMDD-NN) | Yes | PROD-20250109-01 |
| Product_Type | Dropdown | Strategic_Report, Tactical_Brief, Technical_Alert, IOC_Feed, Campaign_Analysis, Threat_Profile | Yes | Tactical_Brief |
| Product_Title | Text | Free text | Yes | APT28 Credential Harvesting Campaign Q1 2025 |
| Intelligence_Level | Dropdown | Strategic, Operational, Tactical | Yes | Tactical |
| Production_Date | Date | DD.MM.YYYY | Yes | 09.01.2025 |
| Author | Text | Analyst name | Yes | Senior TI Analyst |
| Reviewer | Text | Reviewer name | No | TI Team Lead |
| Target_Audience | Dropdown | Executive, Technical, SOC, IT_Ops, All_Staff | Yes | Technical |
| Distribution_Method | Dropdown | Email, Portal, API, Briefing, Report | Yes | Email |
| Sources_Used | Text | Comma-separated Source IDs | Yes | SRC-001, SRC-003, SRC-007 |
| Requirements_Addressed | Text | Comma-separated REQ IDs | Yes | REQ-001, REQ-004 |
| Timeliness_Target_Hours | Number | Integer >= 0 | Yes | 24 |
| Actual_Production_Hours | Number | Integer >= 0 | Yes | 18 |
| Timeliness_Met | Formula | IF Actual <= Target: Yes | Auto | Yes |
| Quality_Score | Dropdown | Excellent, Good, Acceptable, Poor | No | Excellent |
| Feedback_Received | Dropdown | Positive, Neutral, Negative, None | No | Positive |
| Actionable_Items | Number | Integer >= 0 | Yes | 5 |
| Actions_Implemented | Number | Integer >= 0 | Yes | 4 |
| Impact_Rating | Dropdown | High, Medium, Low, Unknown | No | High |
| Notes | Text | Free text | No | Led to emergency patching of 15 servers |

**Conditional Formatting**:

- Timeliness_Met "No" → Yellow background
- Quality_Score "Poor" → Red background
- Impact_Rating "High" + Actions_Implemented > 0 → Green background


---

## Sheet 6: Coverage_Matrix

**Purpose**: Map MITRE ATT&CK technique coverage

**Structure**: Matrix format with tactics and techniques

**Columns**:

- MITRE_Tactic (Column A)
- MITRE_Technique_ID (Column B)
- Technique_Name (Column C)
- Coverage_Status (Dropdown: Covered, Partial, Gap)
- Sources_Covering (Text: Comma-separated)
- Detection_Capability (Dropdown: High, Medium, Low, None)
- Last_Seen_In_Wild (Date)
- Priority_For_Coverage (Dropdown: Critical, High, Medium, Low)
- Gap_Remediation_Plan (Text)


**Conditional Formatting**:

- Coverage_Status "Gap" + Priority "Critical" → Red background
- Detection_Capability "None" + Last_Seen_In_Wild < 90 days → Orange background


---

## Sheet 7: Quality_Metrics

**Purpose**: Track key performance indicators

**Metrics**:

| Metric | Target | Actual | Status | Notes |
|--------|--------|--------|--------|-------|
| Collection_Sources_Active | Number | Number | Formula | Count from Sheet 3 |
| Average_Intelligence_Timeliness | Hours | Formula | Auto | From Sheet 5 |
| Requirements_Coverage_Percent | % | Formula | Auto | From Sheet 2 |
| VTL_Records_Created_MTD | Number | Formula | Auto | From Sheet 8 |
| Critical_VTL_Response_Time_Hours | Number | Number | Manual | Target < 4 hours |
| Products_Published_MTD | Number | Formula | Auto | From Sheet 5 |
| Analyst_Training_Completion_Percent | % | Formula | Auto | From Sheet 9 |
| MITRE_Technique_Coverage_Percent | % | Formula | Auto | From Sheet 6 |
| Threat_Actor_Profiles_Active | Number | Formula | Auto | From Sheet 12 |
| Campaigns_Tracked_Active | Number | Formula | Auto | From Sheet 13 |

**Conditional Formatting**:

- Status "Below Target" → Red background
- Status "At Target" → Green background


---

## Sheet 8: Vulnerability_Linked_Threats (CVSS INTEGRATED)

**PURPOSE**: **CRITICAL INTEGRATION WITH CONTROL 8.8 + CVSS SCORING**

This sheet implements the VulnerabilityThreatLink schema with CVSS integration for quantified risk-based prioritization.

**CVSS Integration**: 

- ✅ Added CVSS_Version column (3)
- ✅ Added CVSS_Base_Score column (4)
- ✅ Added CVSS_Vector column (5)
- ✅ Priority_Score now AUTO-CALCULATED from CVSS + threat factors


**Column Specifications** (24 columns, expanded from 21):

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Link_ID | Text | Auto-generated (VTL-YYYYMMDD-NNNN) | Yes | VTL-20250109-0001 |
| Vulnerability_ID | Text | CVE-YYYY-NNNNN or internal | Yes | CVE-2024-12345 |
| **CVSS_Version** | **Dropdown** | **4.0, 3.1** | **Yes** | **4.0** |
| **CVSS_Base_Score** | **Number** | **0.0-10.0, 1 decimal** | **Yes** | **9.3** |
| **CVSS_Vector** | **Text** | **Max 200 chars** | **Yes** | **CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N** |
| Threat_Actor | Text | Free text | No | APT28 (Fancy Bear) |
| Threat_Actor_Type | Dropdown | Nation-State, Organized_Crime, Hacktivist, Insider, Opportunistic, Unknown | No | Nation-State |
| Exploitation_Status | Dropdown | No_Known_Exploit, PoC_Available, Active_Exploitation, Mass_Exploitation | Yes | Active_Exploitation |
| Intelligence_Source | Text | Source_ID from 5.7.1 | Yes | SRC-001 |
| Confidence_Level | Dropdown | High, Medium, Low, Unconfirmed | Yes | High |
| Discovery_Date | Date | DD.MM.YYYY | Yes | 01.01.2025 |
| Last_Updated | Date | Auto TODAY() | Yes | 09.01.2025 |
| IOCs | Text | Comma-separated | No | 192.0.2.100, malicious.example.com |
| TTPs | Text | Comma-separated MITRE IDs | No | T1190, T1059 |
| Attack_Vector | Text | Free text | No | Network - Remote unauthenticated |
| **Priority_Score** | **Formula** | **AUTO-CALC** | **Auto** | **14.3 → 10.0** |
| Remediation_Urgency | Dropdown | Critical, High, Medium, Low, Info | Yes | Critical |
| Business_Impact | Text | Free text | No | Would expose customer PII database |
| Affected_Systems_Count | Number | Integer >= 0 | No | 47 |
| Critical_Assets_Affected | Dropdown | Yes, No | Yes | Yes |
| Remediation_Status | Dropdown | Open, In_Progress, Patched, Mitigated, Risk_Accepted, Verified | Yes | Open |
| Assigned_To | Text | Email or team | No | Infrastructure Team |
| Related_Incidents | Text | Comma-separated IDs | No | INC-2025-001 |
| Notes | Text | Max 500 chars | No | CISA KEV listing, emergency patching required |

**Priority_Score Formula** (Column 16):

=MIN(10, 
    [CVSS_Base_Score] 

    + IF([Exploitation_Status]="Mass_Exploitation", 2, 

         IF([Exploitation_Status]="Active_Exploitation", 1, 0))

    + IF([Critical_Assets_Affected]="Yes", 2, 0)
    + IF([Threat_Actor_Type]="Nation-State", 1, 0)

)


**Example Calculations**:

- CVSS 9.3 + Mass Exploitation (2) + Critical Assets (2) + Nation-State (1) = 14.3 → **Capped at 10.0**
- CVSS 6.5 + Active Exploitation (1) + No Critical Assets (0) + Organized Crime (0) = **7.5**
- CVSS 4.2 + PoC Available (0) + Critical Assets (2) + Opportunistic (0) = **6.2**


**Conditional Formatting (CVSS-based)**:

- **CVSS_Base_Score >= 9.0** → Red background (Critical severity)
- **CVSS_Base_Score >= 7.0 AND < 9.0** → Orange background (High severity)
- **CVSS_Base_Score >= 4.0 AND < 7.0** → Yellow background (Medium severity)
- **CVSS_Base_Score < 4.0** → Green background (Low severity)
- **CVSS >= 9.0 AND Exploitation_Status = "Mass_Exploitation"** → **BRIGHT RED + BOLD** (Emergency)
- **CVSS >= 7.0 AND Exploitation_Status = "Active_Exploitation"** → **RED + BOLD** (Emergency)
- Exploitation_Status "Active" + Critical_Assets "Yes" → Bright red background
- Remediation_Status "Verified" → Green background
- Remediation_Status "Open" + Priority >= 8 → Bold red


**Integration Workflow**:
1. TI analyst discovers active exploitation → Creates VTL record with CVSS score
2. Priority_Score auto-calculated from CVSS + threat intelligence factors
3. VTL record automatically flags in Control 8.8 vulnerability workbook
4. High CVSS + active exploitation triggers emergency patching workflow
5. Vulnerability manager updates remediation_status
6. Status syncs back to this sheet for TI tracking
7. Closed-loop validation with quantified risk metrics

---

## Sheet 9: Analyst_Capabilities

**Purpose**: Track analyst skills and training

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Analyst_ID | Text | Auto-generated (ANL-NNN) | Yes | ANL-001 |
| Analyst_Name | Text | Free text | Yes | Jane Smith |
| Role | Dropdown | Senior_Analyst, Mid_Analyst, Junior_Analyst, Team_Lead, Manager | Yes | Mid_Analyst |
| Primary_Focus | Dropdown | Tactical_Analysis, Strategic_Analysis, Technical_Analysis, Dissemination | Yes | Tactical_Analysis |
| Hire_Date | Date | DD.MM.YYYY | Yes | 15.03.2022 |
| Certifications | Text | Comma-separated | No | GCTI, GIAC, CISSP |
| Training_Completed | Text | Comma-separated courses | No | MITRE ATT&CK, Threat Hunting |
| Training_Hours_YTD | Number | Integer >= 0 | Yes | 40 |
| Training_Target_Hours_Annual | Number | Integer >= 0 | Yes | 80 |
| Training_On_Track | Formula | IF Actual >= Target: Yes | Auto | Yes |
| Skills_MITRE_ATT&CK | Dropdown | Expert, Advanced, Intermediate, Novice, None | Yes | Advanced |
| Skills_Malware_Analysis | Dropdown | Expert, Advanced, Intermediate, Novice, None | Yes | Intermediate |
| Skills_OSINT | Dropdown | Expert, Advanced, Intermediate, Novice, None | Yes | Advanced |
| Skills_Scripting | Dropdown | Expert, Advanced, Intermediate, Novice, None | Yes | Intermediate |
| Skills_Reporting | Dropdown | Expert, Advanced, Intermediate, Novice, None | Yes | Advanced |
| Workload_Current | Dropdown | Overloaded, High, Normal, Low | Yes | Normal |
| Reports_Authored_MTD | Number | Integer >= 0 | Yes | 5 |
| VTL_Records_Created_MTD | Number | Integer >= 0 | Yes | 12 |
| Quality_Rating_Avg | Dropdown | Excellent, Good, Acceptable, Needs_Improvement | No | Good |
| Notes | Text | Free text | No | Strong OSINT and reporting skills |

**Conditional Formatting**:

- Workload_Current "Overloaded" → Red background
- Training_On_Track "No" → Yellow background
- Quality_Rating "Needs_Improvement" → Orange background


---

## Sheet 10: Action_Items

**Purpose**: Track improvement actions from assessments

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Action_ID | Text | Auto-generated (ACT-YYYYMMDD-NN) | Yes | ACT-20250109-01 |
| Action_Type | Dropdown | Process_Improvement, Tool_Integration, Training, Coverage_Gap, Integration, CVSS_Quality, Other | Yes | Coverage_Gap |
| Priority | Dropdown | Critical, High, Medium, Low | Yes | High |
| Description | Text | Free text (max 500 chars) | Yes | Add threat intelligence source for Asia-Pacific region |
| Source_Sheet | Dropdown | Sheet 2-13 | Yes | Sheet 2 |
| Responsible_Party | Text | Email or role | Yes | TI Team Lead |
| Due_Date | Date | DD.MM.YYYY | Yes | 31.01.2025 |
| Status | Dropdown | Open, In_Progress, Blocked, Completed, Cancelled | Yes | In_Progress |
| Progress_Percent | Number | 0-100% | No | 60% |
| Budget_Required | Currency | >= 0, 2 decimals | No | 5000.00 |
| Budget_Approved | Dropdown | Yes, No, Pending, N/A | No | Yes |
| Completion_Date | Date | DD.MM.YYYY | No | N/A |
| Impact_Expected | Dropdown | High, Medium, Low | Yes | High |
| Notes | Text | Free text | No | Evaluating 3 potential vendors |

**Conditional Formatting**:

- Priority "Critical" + Status "Open" → Red background
- Due_Date overdue + Status != "Completed" → Bold red
- Status "Completed" → Green background


---### 5.11 Sheet 11: Analysis_Tools

**Purpose**: Document threat intelligence analysis tools and platforms

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Tool_ID | Text | Auto-generated (TOOL-NNN) | Yes | TOOL-001 |
| Tool_Name | Text | Free text | Yes | MITRE ATT&CK Navigator |
| Tool_Category | Dropdown | TIP, SIEM, Malware_Analysis, OSINT, Collaboration, Visualization, Scripting, Other | Yes | Visualization |
| Vendor | Text | Free text | No | MITRE Corporation |
| License_Type | Dropdown | Commercial, Open_Source, Freeware, Internal_Developed | Yes | Open_Source |
| Primary_Users | Text | Free text | No | All TI analysts |
| Use_Cases | Text | Max 300 chars | Yes | Mapping adversary TTPs to ATT&CK framework |
| Integration_Status | Dropdown | Integrated, Standalone, Planned, Deprecated | Yes | Integrated |
| Data_Sources | Text | Free text | No | MITRE ATT&CK knowledge base |
| CVSS_Support | Dropdown | Yes, No, N/A | Yes | N/A |
| Last_Updated | Date | DD.MM.YYYY | Yes | 15.12.2024 |
| Version | Text | Free text | No | v11.1 |
| Training_Required | Dropdown | Yes, No | Yes | Yes |
| Training_Status | Text | Free text | No | 5/8 analysts trained |
| Cost_Annual | Currency | >= 0, 2 decimals | No | 0.00 |
| Notes | Text | Max 500 chars | No | Free tool from MITRE, essential for TTP mapping |

**Conditional Formatting**:

- Integration_Status "Deprecated" → Gray background
- Training_Required "Yes" + Training_Status shows incomplete (e.g., "3/8") → Yellow background
- CVSS_Support "Yes" → Green background


**Tool Categories Explained**:

- **TIP**: Threat Intelligence Platform (e.g., MISP, OpenCTI, ThreatConnect)
- **SIEM**: Security Information and Event Management (e.g., Splunk, QRadar)
- **Malware_Analysis**: Malware sandboxes and analysis tools (e.g., Cuckoo, ANY.RUN)
- **OSINT**: Open Source Intelligence tools (e.g., Shodan, Maltego, theHarvester)
- **Collaboration**: Team collaboration platforms (e.g., Slack, Microsoft Teams)
- **Visualization**: Data visualization tools (e.g., ATT&CK Navigator, D3.js)
- **Scripting**: Automation and scripting environments (e.g., Python, PowerShell)


---

## Sheet 12: Threat_Actor_Profiles

**Purpose**: Maintain profiles of known threat actors targeting organization or sector

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Actor_ID | Text | Auto-generated (ACTOR-NNN) | Yes | ACTOR-001 |
| Actor_Name | Text | Free text | Yes | APT28 (Fancy Bear) |
| Actor_Aliases | Text | Free text | No | Sofacy, Sednit, STRONTIUM |
| Actor_Type | Dropdown | Nation-State, Organized_Crime, Hacktivist, Insider, Opportunistic, Unknown | Yes | Nation-State |
| Attribution_Confidence | Dropdown | High, Medium, Low, Unconfirmed | Yes | High |
| Country_of_Origin | Text | Free text | No | Russia |
| First_Observed | Date | DD.MM.YYYY | No | 01.01.2007 |
| Last_Activity | Date | DD.MM.YYYY | Yes | 15.12.2024 |
| Targeting_Our_Sector | Dropdown | Yes, No, Unknown | Yes | Yes |
| Targeting_Our_Org | Dropdown | Confirmed, Suspected, No, Unknown | Yes | Suspected |
| Primary_Motivation | Dropdown | Espionage, Financial, Disruption, Ideology, Unknown | Yes | Espionage |
| Sophistication_Level | Dropdown | Advanced, Moderate, Low | Yes | Advanced |
| Primary_TTPs | Text | Comma-separated MITRE IDs | No | T1566.001, T1059.001, T1053.005 |
| Common_Malware | Text | Free text | No | Sofacy, X-Agent, Zebrocy |
| Infrastructure_Notes | Text | Max 500 chars | No | Uses bulletproof hosting, frequently changes C2 |
| CVEs_Exploited | Text | Comma-separated CVE IDs | No | CVE-2023-23397, CVE-2022-30190 |
| VTL_Records_Count | Number | Integer >= 0 | Yes | 5 |
| Related_Campaigns | Text | Comma-separated CAMP IDs | No | CAMP-2024-015, CAMP-2024-022 |
| Last_Update_Date | Date | DD.MM.YYYY | Yes | 09.01.2025 |
| Notes | Text | Max 1000 chars | No | GRU Unit 26165, targets government and defense sectors |

**Conditional Formatting**:

- Targeting_Our_Org "Confirmed" → Red background
- Targeting_Our_Org "Suspected" + Targeting_Our_Sector "Yes" → Orange background
- Sophistication_Level "Advanced" + Targeting_Our_Sector "Yes" → Yellow background
- Last_Activity within 90 days + Targeting_Our_Sector "Yes" → Bold


**Integration with Other Sheets**:

- **Sheet 8 (VTL)**: Threat_Actor field can reference Actor_Name from this sheet
- **Sheet 13 (Campaign_Tracking)**: Actor_ID used for VLOOKUP


---

## Sheet 13: Campaign_Tracking

**Purpose**: Track and analyze threat campaigns over time

**Column Specifications**:

| Column | Data Type | Validation | Required | Example |
|--------|-----------|------------|----------|---------|
| Campaign_ID | Text | Auto-generated (CAMP-YYYY-NNN) | Yes | CAMP-2024-015 |
| Campaign_Name | Text | Free text | Yes | Winter Vivern Credential Harvesting |
| Actor_ID | Dropdown | From Sheet 12 | No | ACTOR-001 |
| Actor_Name | Formula | =IFERROR(VLOOKUP(Actor_ID, Sheet12, 2, FALSE), "Unknown") | Auto | APT28 (Fancy Bear) |
| Campaign_Start_Date | Date | DD.MM.YYYY | Yes | 15.10.2024 |
| Campaign_End_Date | Date | DD.MM.YYYY or "Ongoing" | No | Ongoing |
| Campaign_Status | Dropdown | Active, Concluded, Dormant, Unknown | Yes | Active |
| Target_Sectors | Text | Free text | Yes | Government, Defense, Think Tanks |
| Target_Geographies | Text | Free text | Yes | Europe, North America |
| Our_Sector_Targeted | Dropdown | Yes, No, Unknown | Yes | No |
| Our_Org_Targeted | Dropdown | Confirmed, Suspected, No, Unknown | Yes | No |
| Primary_Objective | Dropdown | Espionage, Data_Theft, Disruption, Ransomware, Credential_Harvesting, Other | Yes | Credential_Harvesting |
| Attack_Vectors | Text | Free text | Yes | Spearphishing with malicious links |
| TTPs_Used | Text | Comma-separated MITRE IDs | No | T1566.002, T1204.001, T1056.001 |
| CVEs_Exploited | Text | Comma-separated CVE IDs | No | CVE-2023-38831 |
| CVEs_CVSS_Max | Formula | Max CVSS from VTL records | Auto | 7.8 |
| IOCs_Count | Number | Integer >= 0 | Yes | 47 |
| VTL_Records_Created | Number | Integer >= 0 | Yes | 2 |
| Incidents_Our_Org | Number | Integer >= 0 | Yes | 0 |
| Intelligence_Sources | Text | Comma-separated Source IDs | No | SRC-001, SRC-005 |
| Threat_Level | Dropdown | Critical, High, Medium, Low | Yes | Medium |
| Monitoring_Status | Dropdown | Active_Monitoring, Passive_Monitoring, Concluded | Yes | Active_Monitoring |
| Last_Update_Date | Date | DD.MM.YYYY | Yes | 09.01.2025 |
| Notes | Text | Max 1000 chars | No | Targeting webmail, using Mockbin for exfiltration |

**CVEs_CVSS_Max Formula** (Column 16):

=IFERROR(
    MAXIFS(
        'Vulnerability_Linked_Threats'!D:D,  # CVSS_Base_Score column
        'Vulnerability_Linked_Threats'!B:B,  # Vulnerability_ID column
        CVEs_Exploited                        # Match any CVE in this campaign
    ), 
    0.0
)

*Note: This is a simplified representation; actual implementation may require array formulas or helper columns*

**Conditional Formatting**:

- Campaign_Status "Active" + Our_Org_Targeted "Confirmed" → Red background
- Campaign_Status "Active" + Our_Org_Targeted "Suspected" → Orange background
- Threat_Level "Critical" → Red text, bold
- Incidents_Our_Org > 0 → Orange background
- CVEs_CVSS_Max >= 9.0 → Red background (Critical vulnerabilities)


**Integration with Other Sheets**:

- **Sheet 8 (VTL)**: CVE data flows to calculate CVEs_CVSS_Max
- **Sheet 12 (Threat_Actor_Profiles)**: Actor_ID VLOOKUP for Actor_Name
- **Sheet 3 (Collection_Sources)**: Intelligence_Sources reference


---

## Sheet 14: Metadata

**Purpose**: Workbook generation and versioning information

**Content**:

- Workbook version: 2.0
- Generation date
- Generator script version
- Total sheets: 14
- CVSS integration: Enabled
- Control references: A.5.7, A.8.8
- Review schedule
- Contact information


---

# Data Validation Rules

## Standard Dropdowns

**Priority Levels**:

- Critical
- High
- Medium
- Low
- Info (where applicable)


**Status Values**:

- Open
- In_Progress
- Completed
- Blocked
- Cancelled
- Verified


**Confidence Levels**:

- High
- Medium
- Low
- Unconfirmed


**Yes/No/Unknown**:

- Yes
- No
- Unknown
- N/A (where applicable)


**CVSS Versions**:

- 4.0
- 3.1


**Exploitation Status**:

- No_Known_Exploit
- PoC_Available
- Active_Exploitation
- Mass_Exploitation


**Threat Actor Types**:

- Nation-State
- Organized_Crime
- Hacktivist
- Insider
- Opportunistic
- Unknown


---

# Integration Points

## Control 5.7 Internal Links

- Sheet 2 (Intelligence_Requirements) ↔ Sheet 3 (Collection_Sources)
- Sheet 3 (Collection_Sources) ↔ Sheet 5 (Intelligence_Production)
- Sheet 4 (Raw_Intelligence_Log) → Sheet 5 (Intelligence_Production)
- Sheet 5 (Intelligence_Production) → Sheet 7 (Quality_Metrics)
- **Sheet 8 (VTL) ↔ Sheet 12 (Threat_Actor_Profiles)**
- **Sheet 8 (VTL) ↔ Sheet 13 (Campaign_Tracking)**
- Sheet 9 (Analyst_Capabilities) → Sheet 7 (Quality_Metrics)
- **Sheet 11 (Analysis_Tools) → Sheet 9 (Analyst_Capabilities)**
- All sheets → Sheet 10 (Action_Items)
- All sheets → Sheet 14 (Metadata)


## External Integration: Control 8.8 (Vulnerability Management)

**Bidirectional Data Flow via Sheet 8 (VTL)**:

**5.7 → 8.8 (Threat Context)**:

- Vulnerability_ID (with CVSS)
- CVSS_Version, CVSS_Base_Score, CVSS_Vector
- Threat_Actor
- Exploitation_Status
- Intelligence_Source
- Confidence_Level
- IOCs
- TTPs
- Priority_Score (auto-calculated from CVSS)
- Business_Impact


**8.8 → 5.7 (Remediation Status)**:

- Remediation_Status
- Remediation_Urgency
- Assigned_To
- Affected_Systems_Count
- Related_Incidents


**Emergency Patching Trigger**:

- IF CVSS_Base_Score >= 9.0 AND Exploitation_Status = "Mass_Exploitation"
- IF CVSS_Base_Score >= 7.0 AND Exploitation_Status = "Active_Exploitation" AND Critical_Assets_Affected = "Yes"
- Auto-escalates to Control 8.8 emergency patching workflow


## External Integration: Control 5.7.1 (Source Assessment)

- Sheet 3 (Collection_Sources) references Source_IDs from 5.7.1
- Sheet 8 (VTL) Intelligence_Source field references 5.7.1 sources
- Sheet 13 (Campaign_Tracking) Intelligence_Sources references 5.7.1


---

# Formulas Reference

## Priority_Score Auto-Calculation (Sheet 8, Column 16)

**Excel Formula**:
excel
=MIN(10, 
    D5 +                                    # CVSS_Base_Score
    IF(H5="Mass_Exploitation", 2, 
       IF(H5="Active_Exploitation", 1, 0)) +  # Exploitation bonus
    IF(T5="Yes", 2, 0) +                    # Critical assets bonus
    IF(G5="Nation-State", 1, 0)             # Nation-state bonus
)


**Components**:
1. **Base**: CVSS_Base_Score (0.0-10.0)
2. **+2**: Mass Exploitation detected
3. **+1**: Active Exploitation detected
4. **+2**: Critical Assets Affected = Yes
5. **+1**: Threat Actor Type = Nation-State
6. **Cap**: MIN(result, 10.0)

**Rationale**:

- Quantifies risk using industry-standard CVSS
- Adds context-specific threat intelligence factors
- Caps at 10.0 to maintain consistency
- Auto-updates when any input changes


## Coverage_Status (Sheet 2, Column 12)

excel
=IF(COUNTA(H5:J5)>=2, "Adequate", 
    IF(COUNTA(H5:J5)=1, "Minimal", "Gap"))


## Timeliness_Met (Sheet 5, Column 14)

excel
=IF(M5<=L5, "Yes", "No")


## Actor_Name VLOOKUP (Sheet 13, Column 4)

excel
=IFERROR(VLOOKUP(C5, 'Threat_Actor_Profiles'!A:B, 2, FALSE), "Unknown")


## CVEs_CVSS_Max (Sheet 13, Column 16)

excel
# Simplified - actual implementation may vary
=IFERROR(MAX(
    IF(ISNUMBER(SEARCH(O5, 'Vulnerability_Linked_Threats'!B:B)), 
       'Vulnerability_Linked_Threats'!D:D, 0)
), 0.0)


---

# Conditional Formatting Rules

## CVSS-Based Severity (Sheet 8)

| CVSS Range | Color | Severity |
|------------|-------|----------|
| >= 9.0 | Red (#DC143C) | Critical |
| 7.0 - 8.9 | Orange (#FF8C00) | High |
| 4.0 - 6.9 | Yellow (#FFD700) | Medium |
| 0.0 - 3.9 | Green (#90EE90) | Low |

**Emergency Highlight**:

- CVSS >= 9.0 + Exploitation = "Mass_Exploitation" → **BRIGHT RED + BOLD**
- CVSS >= 7.0 + Exploitation = "Active_Exploitation" → **RED + BOLD**


## Status-Based Formatting

| Condition | Format | Applies To |
|-----------|--------|------------|
| Status = "Completed" | Green background | All action/task sheets |
| Status = "Overdue" | Bold red | All sheets with dates |
| Priority = "Critical" + Status = "Open" | Red background | All sheets |
| Coverage_Status = "Gap" | Red background | Sheet 2 |
| Threat_Level = "Critical" | Red text, bold | Sheets 8, 13 |

---

# Quality Assurance

## Validation Checks

**Pre-Deployment**:
1. ✅ All 14 sheets present
2. ✅ Sheet 8 has 24 columns (including 3 CVSS columns)
3. ✅ Priority_Score formula correct (column 16, Sheet 8)
4. ✅ CVSS conditional formatting applied (Sheet 8)
5. ✅ All dropdowns functional
6. ✅ VLOOKUP formulas have IFERROR wrappers
7. ✅ Sheets 11-13 present with correct structures
8. ✅ Integration references correct (Sheet 13 → Sheet 12)
9. ✅ Python generator script produces error-free workbook
10. ✅ Sanity check script passes

**Post-Generation**:
1. Open workbook in Excel
2. Verify no formula errors (#REF!, #VALUE!, #N/A)
3. Test all dropdowns
4. Verify conditional formatting displays correctly
5. Test CVSS score calculation (enter test data in Sheet 8)
6. Verify VLOOKUP (Sheet 13 Actor_Name from Sheet 12)
7. Check merge cells display properly
8. Verify protected cells cannot be edited
9. Test workbook saves without corruption warnings

---

# Change History

## v1.0 ([Date])

**Initial Release**:
1. 14-sheet workbook covering intelligence collection and analysis
2. CVSS-integrated vulnerability-threat linkage (Sheet 8)
3. Threat actor profiling (Sheet 12)
4. Campaign tracking (Sheet 13)
5. Analysis tools inventory (Sheet 11)
6. Automated priority scoring using CVSS + threat context
7. Bidirectional integration with Control 8.8 (Management of Technical Vulnerabilities)

---

# Usage Guidelines

## Data Entry Workflow

1. **Initial Setup**:

   - Sheet 2: Define intelligence requirements
   - Sheet 3: Document collection sources
   - Sheet 11: Document analysis tools
   - Sheet 12: Build threat actor profiles


2. **Daily Operations**:

   - Sheet 4: Log raw intelligence
   - Sheet 8: Create VTL records (with CVSS)
   - Sheet 13: Track campaigns


3. **Regular Production**:

   - Sheet 5: Document intelligence products
   - Sheet 9: Update analyst capabilities
   - Sheet 10: Track action items


4. **Periodic Review**:

   - Sheet 6: MITRE coverage assessment
   - Sheet 7: Quality metrics review
   - Sheet 9: Process maturity assessment


## CVSS Data Entry (Sheet 8)

**Required Fields**:
1. Vulnerability_ID (CVE or internal)
2. **CVSS_Version** (4.0 or 3.1)
3. **CVSS_Base_Score** (0.0-10.0, one decimal)
4. **CVSS_Vector** (full vector string)
5. Exploitation_Status
6. Critical_Assets_Affected
7. Threat_Actor_Type (if known)

**Priority_Score Auto-Calculates** - do NOT enter manually!

**CVSS Vector Examples**:

- **CVSS 4.0**: `CVSS:4.0/AV:N/AC:L/AT:N/PR:N/UI:N/VC:H/VI:H/VA:H/SC:N/SI:N/SA:N`
- **CVSS 3.1**: `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H`


**Source for CVSS Scores**:

- NVD (National Vulnerability Database): https://nvd.nist.gov
- Vendor security advisories
- Commercial threat intelligence feeds
- CISA KEV (Known Exploited Vulnerabilities): https://www.cisa.gov/known-exploited-vulnerabilities-catalog


## Maintenance Schedule

**Daily**:

- Update Sheet 4 (Raw Intelligence Log)
- Update Sheet 8 (VTL) for new exploitations
- Monitor Sheet 13 (Campaign Tracking) for active campaigns


**Weekly**:

- Review Sheet 7 (Quality Metrics)
- Update Sheet 10 (Action Items) progress
- Review Sheet 8 for remediation status updates


**Monthly**:

- Review Sheet 2 (Intelligence Requirements) coverage
- Assess Sheet 9 (Process Maturity)
- Update Sheet 12 (Threat Actor Profiles)


**Quarterly**:

- Complete Sheet 6 (MITRE Mapping) assessment
- Review Sheet 3 (Collection Sources) contracts
- Update Sheet 11 (Analysis Tools) inventory


---

# Audit Evidence

This workbook provides audit evidence for:

**ISO 27001:2022 Control A.5.7**:

- Intelligence requirements documentation (Sheet 2)
- Collection capabilities (Sheet 3)
- Analysis methodologies (Sheet 6)
- Quality metrics (Sheet 7)
- Process maturity (Sheet 9)


**Control A.5.7 ↔ A.8.8 Integration**:

- Vulnerability-threat linkage (Sheet 8 with CVSS)
- Quantified risk scoring (Priority_Score formula)
- Emergency patching triggers (CVSS + exploitation)
- Remediation tracking (bidirectional data flow)


**Key Features**:

- CVSS-based prioritization evidence
- Threat actor intelligence maintenance
- Campaign tracking and analysis
- Tool inventory and training records


---

# Support & Contact

**Workbook Issues**:

- Threat Intelligence Team Lead
- Email: ti-team@[organization].com


**Technical Issues**:

- ISMS Implementation Team
- Email: isms@[organization].com


**Policy Questions**:

- Information Security Manager
- Refer to: ISMS-POL-A.5.7 (Threat Intelligence Policy)


---

**Document Status**: Production  
**Last Updated**: [Date] 

---

# Related Documents

**Policy Framework:**

- **ISMS-POL-A.5.7** (Threat Intelligence Policy) - Consolidated single policy document
- **ISMS-POL-A.5.7, Section 2.1** (Intelligence Collection Requirements)
- **ISMS-POL-A.5.7, Section 2.2** (Intelligence Analysis and Production Requirements)
- **ISMS-POL-A.5.7, Section 2.6** (Vulnerability Management Integration Requirements) - VTL schema
- **ISMS-POL-A.5.7, Section 2.7** (Effectiveness Measurement Requirements)


**Implementation Specifications:**

- **ISMS-IMP-A.5.7.1** (Threat Intelligence Sources Assessment) - Source IDs referenced
- **ISMS-IMP-A.5.7.3** (Integration & Distribution Assessment) - VTL records feed IOC deployment
- **ISMS-IMP-A.5.7.4** (Effectiveness Dashboard) - Quality metrics consolidated
- **ISMS-IMP-A.5.7.5** (Standalone Dashboard) - Production metrics used


**Cross-Control Integration:**

- **ISMS-IMP-A.8.8** (Vulnerability Management) - VTL bidirectional integration (CRITICAL)
- **ISMS-POL-A.8.8** (Vulnerability Management Policy) - VulnerabilityThreatLink schema


**Standards References:**

- ISO/IEC 27001:2022 Annex A Control A.5.7
- ISO/IEC 27002:2022 Control 5.7 Implementation Guidance
- MITRE ATT&CK Framework v18.1 (Enterprise)
- CVSS 4.0 Specification (FIRST)
- CVSS 3.1 Specification (FIRST)


---

**END OF SPECIFICATION**

---

*"How wonderful that we have met with a paradox. Now we have some hope of making progress."*
— Niels Bohr

<!-- QA_VERIFIED: 2026-01-31 -->
