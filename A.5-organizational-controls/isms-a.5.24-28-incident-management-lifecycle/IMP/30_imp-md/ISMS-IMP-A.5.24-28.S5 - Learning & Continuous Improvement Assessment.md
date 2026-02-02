# ISMS-IMP-A.5.24-28.S5 - Learning & Continuous Improvement Assessment

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | Learning & Continuous Improvement Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.24-28.S5 |
| **Assessment Domain** | Domain 5 - Learning & Improvement (A.5.27 Focus) |
| **Related Policy** | ISMS-POL-A.5.24-28 (Incident Management Lifecycle) |
| **Related Reference** | ISMS-REF-A.5.24-28 (Incident Response Reference Guide) |
| **Document Owner** | Chief Information Security Officer (CISO) |
| **Technical Authority** | Incident Response Team Lead / CSIRT Manager |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Version Date** | [To Be Determined] |
| **Classification** | Internal |
| **Status** | Draft |

**Version History:**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CSIRT Manager | Initial learning & improvement assessment specification |

**Review Cycle:** Annual (or after major incident management process changes)
**Next Review Date:** [Effective Date + 12 months]

**Related Documents:**
- ISMS-POL-A.5.24-28 (Incident Management Lifecycle Policy)
- ISMS-REF-A.5.24-28 (Incident Response Reference Guide)
- ISMS-IMP-A.5.24-28.S1 (Framework & Governance Assessment)
- ISMS-IMP-A.5.24-28.S2 (Detection & Classification Assessment)
- ISMS-IMP-A.5.24-28.S3 (Response Capabilities Assessment)
- ISMS-IMP-A.5.24-28.S4 (Forensic Evidence Assessment)
- ISO/IEC 27002:2022 Control A.5.27
- NIST SP 800-61 Rev. 2 Section 3.4 (Post-Incident Activity)

---

# PART I: USER COMPLETION GUIDE
**Audience:** Incident Managers, CSIRT/SOC Leads, Security Operations Teams, Compliance Officers

---

## 1. Assessment Overview

### 1.1 Purpose

This assessment evaluates [Organization]'s **post-incident learning and continuous improvement capabilities**, focusing on the **learning** phase of the incident management lifecycle (A.5.27). It determines whether knowledge gained from information security incidents is systematically captured, analysed, and fed back into controls, playbooks, training, and risk assessments.

### 1.2 What This Assessment Measures

**Scope - 5 learning and improvement domains:**

1. **Post-Incident Review (PIR) Process** - Timeliness, completeness, and quality of post-incident reviews
2. **Root Cause Analysis (RCA)** - Depth, methodology, and accuracy of root cause identification
3. **Lessons Learned & Knowledge Management** - Documentation, dissemination, and knowledge base maintenance
4. **Control Improvement Tracking** - Remediation actions derived from incidents, ownership, and closure
5. **Trend Analysis & Metrics Reporting** - Incident KPIs, trend identification, and executive/board reporting

**Assessment Output:** Excel workbook documenting PIR effectiveness, RCA quality, lessons learned coverage, improvement tracking status, trend metrics, compliance gaps, and remediation plans.

### 1.3 Why This Matters

**ISO 27001:2022 Control A.5.27 Requirement:**
> *"Knowledge gained from information security incidents should be used to strengthen and improve the information security controls."*

**A.5.27 is the closing loop of the entire incident lifecycle:**

- **S1 (Framework)** defines HOW incidents will be managed
- **S2 (Detection)** identifies WHEN something has happened
- **S3 (Response)** contains and eradicates the threat
- **S4 (Evidence)** preserves forensic proof
- **S5 (Learning - THIS ASSESSMENT)** ensures the organisation IMPROVES after every incident

Without a functioning learning loop, the same incidents recur, playbooks stagnate, and the organisation never advances its security posture. Auditors treat S5 as the strongest signal of incident management maturity.

**Regulatory Context:**
- **Swiss nDSG (Art. 8):** Requires continuous improvement of security measures; incident learning feeds this obligation
- **EU GDPR (Art. 32):** Mandates appropriate technical and organisational measures - learning from breaches is a documented expectation
- **DORA (Art. 11):** Explicitly requires lessons learned from ICT incidents to be integrated into ICT risk management
- **NIS2 (Art. 21):** Requires incident response procedures that include post-incident analysis

**Business Impact:**
- **Recurring incidents** without learning signals indicate systemic process failure
- **Stale playbooks** directly increase response time and damage scope
- **Untracked remediation** from incidents leaves known vulnerabilities open
- **No trend visibility** prevents proactive risk treatment and budget justification
- **Audit failure** - A.5.27 is commonly cited in ISO 27001 non-conformities when PIR/RCA evidence is missing

### 1.4 Who Should Complete This Assessment

**Primary Responsibility:** Incident Response Team Lead / CSIRT Manager

**Required Knowledge:**
- [Organization]'s incident ticketing system and PIR workflow
- Historical incident records (minimum 12-month lookback recommended)
- Root cause analysis methodology in use
- Lessons learned repository or knowledge base location
- Control improvement / remediation tracking process
- Incident trend reporting dashboards or reports

**Support Roles:**
- **SOC Analysts:** For operational PIR participation records
- **Security Engineering:** For control improvement implementation status
- **Compliance Team:** For regulatory notification and reporting linkages
- **IT Management:** For remediation budget and resource allocation status
- **Risk Management:** For risk register update verification

### 1.5 Time Estimate

**Total Assessment Time:** 6-10 hours (depending on incident volume and documentation maturity)

**Breakdown:**
- Information Gathering: 2-3 hours (PIR records, RCA reports, lessons learned logs, remediation tracker, trend reports)
- Historical Review: 2-3 hours (sampling and scoring PIRs and RCAs from last 12 months)
- Assessment Completion: 2-3 hours (5 domain sheets)
- Evidence Collection: 1-1.5 hours (screenshots, exports, reports)
- Quality Review: 30-60 minutes

**Complexity Factors:**
- **Simple:** Low incident volume (<20/year), basic PIR process, single ticketing system - 6 hours
- **Moderate:** Moderate volume (20-100/year), multiple incident types, some trend reporting - 8 hours
- **Complex:** High volume (100+/year), multi-team CSIRT, mature trend analytics, regulatory reporting - 10+ hours

### 1.6 Connection to Policy

This assessment implements **ISMS-POL-A.5.24-28, Section on A.5.27 (Learning)** which defines mandatory requirements for:
- Post-Incident Review completion within defined timeframes per severity
- Root cause analysis for all incidents rated High or above
- Lessons learned documentation and distribution
- Control improvement actions with ownership and deadlines
- Incident trend reporting to management and board
- Feedback loop into playbooks, training, and risk assessment

**Policy Authority:** Chief Information Security Officer (CISO)
**Compliance Status:** Mandatory for all information security incidents

### 1.7 Critical Policy Requirements Summary

**PIR Process:**
- **Critical/High incidents:** PIR within 5 business days of resolution
- **Medium incidents:** PIR within 15 business days of resolution
- **Low incidents:** PIR within 30 business days or during quarterly batch review
- **PIR participation:** Incident owner + at least one additional stakeholder (SOC lead, system owner, or security engineering)

**Root Cause Analysis:**
- **Mandatory for:** All Critical and High incidents
- **Recommended for:** All Medium incidents
- **Methodology:** Documented methodology required (e.g., 5 Whys, fishbone, fault tree)
- **Depth:** Root cause must trace beyond immediate technical failure to process, governance, or systemic factors where applicable

**Lessons Learned & Knowledge Management:**
- **Documentation:** Every PIR produces at least one documented lesson learned entry
- **Distribution:** Lessons learned communicated to relevant teams within 10 business days of PIR completion
- **Knowledge Base:** Maintained and searchable; reviewed and curated quarterly
- **Playbook Updates:** Affected playbooks updated within 20 business days of PIR completion

**Control Improvements:**
- **Action Tracking:** All remediation actions from incidents logged with owner, priority, target date
- **Closure Verification:** Completed actions verified by an independent party (not the implementer)
- **Escalation:** Overdue Critical/High remediation actions escalated to CISO within 5 business days of missed deadline

**Trend Analysis & Reporting:**
- **Frequency:** Monthly trend summary for SOC/CSIRT; Quarterly report to CISO; Annual summary to Board/Executive
- **KPIs tracked:** MTTD, MTTR, recurrence rate, PIR completion rate, remediation closure rate
- **Comparison:** Current period vs. prior period; year-over-year trending

---

## 2. Prerequisites

### 2.1 Information Required

Before starting this assessment, gather the following:

**Incident Records:**
- [ ] Complete incident log for last 12 months (all severities)
- [ ] Classification and severity per incident
- [ ] Resolution timestamps (for PIR timeliness verification)

**PIR Documentation:**
- [ ] All completed PIR reports from last 12 months
- [ ] PIR participants list (who attended each review)
- [ ] PIR completion dates vs. policy SLA deadlines

**RCA Documentation:**
- [ ] All completed RCA reports from last 12 months
- [ ] RCA methodology documentation
- [ ] Root cause statements and corrective action mapping

**Lessons Learned / Knowledge Base:**
- [ ] Lessons learned repository or log (all entries, last 12 months)
- [ ] Knowledge base / playbook inventory
- [ ] Playbook revision history (last 12 months)
- [ ] Distribution/communication records for lessons learned

**Remediation Tracking:**
- [ ] Remediation action register (all open and closed actions, last 12 months)
- [ ] Ownership records per action
- [ ] Closure verification records
- [ ] Any escalations triggered by overdue actions

**Trend Reporting:**
- [ ] Monthly/Quarterly/Annual incident trend reports (last 12 months)
- [ ] KPI dashboards or reports (MTTD, MTTR, recurrence, etc.)
- [ ] Executive/Board incident reporting records

### 2.2 Access Required

- [ ] Incident ticketing system (read access to all incidents, last 12 months)
- [ ] PIR/RCA document repository
- [ ] Knowledge base or playbook repository
- [ ] Remediation action tracking system
- [ ] Trend reporting dashboards or report storage

### 2.3 Knowledge Required

**Essential Understanding:**
- [Organization]'s incident management lifecycle and ticketing workflow
- PIR process and RCA methodology in use
- Knowledge base structure and maintenance practices
- Remediation action lifecycle (creation -> assignment -> tracking -> closure -> verification)
- Incident reporting cadence and distribution

### 2.4 Estimated Time Commitment

**Phase 1: Information Gathering (2-3 hours)**
- Export incident log (12-month window)
- Collect all PIR and RCA reports
- Download lessons learned log and playbook revision history
- Export remediation action register
- Gather trend reports

**Phase 2: Historical Sampling & Scoring (2-3 hours)**
- Sample PIRs for timeliness and quality (minimum 10, or all if fewer)
- Sample RCAs for depth and methodology adherence
- Verify lessons learned linkage to PIRs
- Check remediation action closure and verification status
- Review trend reports for completeness and accuracy

**Phase 3: Assessment Completion (2-3 hours)**
- Complete 5 domain assessment sheets
- Identify gaps and populate remediation plans
- Collect and link evidence

**Phase 4: Quality Review (30-60 minutes)**
- Self-check using Quality Checklist (Section 7)
- Verify evidence completeness
- Review Summary Dashboard
- Ensure all gaps have owners and target dates

**Total:** 6-10 hours for comprehensive assessment

---

## 3. Assessment Workflow

### 3.1 Recommended Completion Sequence

**STEP 1: Initial Setup (10 minutes)**
1. Download assessment Excel workbook (`ISMS-IMP-A.5.24-28.S5_Learning_Improvement_[DATE].xlsx`)
2. Open "Instructions & Legend" sheet
3. Complete document information fields
4. Review Status Legend and Evidence Types
5. Skim all 5 assessment sheets to understand scope

**STEP 2: PIR Process Assessment (60-90 minutes - START HERE)**
1. **Sheet: PIR Process** <- START HERE (foundational - if PIRs don't happen, nothing downstream works)
   - Map every incident (last 12 months) to its PIR status: Completed / Overdue / Not Required / Pending
   - For each completed PIR: verify timeliness against policy SLA (Critical <=5 days, High <=5 days, Medium <=15 days, Low <=30 days)
   - Score PIR quality (completeness of incident description, timeline, impact assessment, action items)
   - Verify participant coverage (incident owner + at least one additional stakeholder)
   - **CRITICAL:** PIR completion rate and timeliness are the single most auditor-visible metric in A.5.27
   - **Evidence:** PIR completion log, PIR reports, incident timeline records

**STEP 3: Root Cause Analysis (45-75 minutes)**
2. **Sheet: Root Cause Analysis**
   - Identify all Critical and High incidents; verify RCA was performed for each
   - For each RCA: verify documented methodology (5 Whys, fishbone, fault tree, or equivalent)
   - Assess RCA depth - does the root cause go beyond the immediate technical trigger to address process/governance/systemic factors?
   - Verify corrective actions are mapped to each identified root cause
   - Check for recurring root causes (same root cause appearing in multiple incidents = systemic gap)
   - **CRITICAL:** Shallow RCAs ("server crashed") without process-level analysis are a common audit finding
   - **Evidence:** RCA reports, methodology documentation, corrective action mapping

**STEP 4: Lessons Learned & Knowledge Management (45-75 minutes)**
3. **Sheet: Lessons Learned & Knowledge Management**
   - Verify every completed PIR produced at least one lessons learned entry
   - Check distribution records: were lessons communicated to relevant teams within 10 business days?
   - Review knowledge base: is it searchable? Current? Curated quarterly?
   - Verify playbook updates: were affected playbooks updated within 20 business days of PIR completion?
   - Check for knowledge gaps: are there incident categories with no corresponding playbook or knowledge base entry?
   - **CRITICAL:** Knowledge management is where learning becomes organisational capability - not just individual memory
   - **Evidence:** Lessons learned log, distribution records, knowledge base inventory, playbook revision history

**STEP 5: Control Improvement Tracking (45-60 minutes)**
4. **Sheet: Control Improvement Tracking**
   - Export all remediation actions derived from incidents (last 12 months)
   - Verify each action has: owner, priority, target date, current status
   - For closed actions: verify independent closure verification was performed (not self-certified)
   - Identify overdue Critical/High actions and verify escalation to CISO was triggered within 5 business days of missed deadline
   - Calculate closure rate by priority (Critical, High, Medium, Low)
   - Identify actions blocked or stalled - these often reveal resource or governance gaps
   - **CRITICAL:** Unverified closures and overdue Critical actions are immediate audit findings
   - **Evidence:** Remediation action register, closure verification records, escalation logs

**STEP 6: Trend Analysis & Metrics Reporting (45-60 minutes)**
5. **Sheet: Trend Analysis & Metrics**
   - Verify monthly trend summaries exist and are distributed to SOC/CSIRT
   - Verify quarterly reports are produced and distributed to CISO
   - Verify annual summary is produced for Board/Executive
   - Check KPI completeness: MTTD, MTTR, recurrence rate, PIR completion rate, remediation closure rate - all tracked?
   - Review trend accuracy: do reported numbers match source incident data?
   - Verify period-over-period comparison is included (current vs. prior; year-over-year)
   - Identify reporting gaps: missing periods, incomplete KPIs, no distribution records
   - **CRITICAL:** Auditors check not only that reports exist but that they are accurate, timely, and distributed
   - **Evidence:** Trend reports (monthly/quarterly/annual), KPI dashboards, distribution records

**STEP 7: Gap Analysis & Evidence (30-45 minutes)**
6. **Sheet: Gap Analysis** - auto-populated from sheets above; review, prioritise, assign owners
7. **Sheet: Evidence Register** - link all collected evidence to specific assessment items

**STEP 8: Review & Approval (30 minutes)**
8. **Sheet: Summary Dashboard** - review overall compliance rates and critical gap flags
9. **Sheet: Approval Sign-Off** - route for three-level approval

### 3.2 Quality Checkpoints

After completing each domain sheet, pause and verify:

| Checkpoint | Verify |
|------------|--------|
| After PIR Process | Every incident in scope has a PIR status; all completed PIRs have timeliness scored |
| After RCA | All Critical/High incidents have RCA status; depth scoring completed |
| After Lessons Learned | Every completed PIR maps to >=1 lessons learned entry; distribution verified |
| After Control Improvements | All actions have owner + target date; overdue items flagged |
| After Trend Analysis | All three reporting cadences (monthly/quarterly/annual) verified; KPIs cross-checked |

---

## 4. Question-by-Question Guidance

### 4.1 Sheet: PIR Process

This sheet assesses whether Post-Incident Reviews are conducted systematically, on time, and with sufficient participation.

**Section A - PIR Inventory (Per Incident, Last 12 Months)**

For each incident in scope, complete one row:

- **Incident_ID:** Reference from your ticketing system (e.g., INC-2025-0042)
- **Incident_Date:** Date the incident was first reported/detected (DD.MM.YYYY)
- **Severity:** As classified at time of incident (Critical / High / Medium / Low)
- **Resolution_Date:** Date the incident was formally closed/resolved
- **PIR_Status:** One of - Completed / Overdue / Pending / Not_Required
  - *Not_Required:* Only if your policy explicitly exempts this severity from PIR. If in doubt, mark Pending.
- **PIR_Completion_Date:** Date the PIR was finalised (blank if not yet completed)
- **Policy_SLA_Days:** The number of business days allowed by policy for this severity (auto-populated based on severity: Critical=5, High=5, Medium=15, Low=30)
- **Actual_Days_To_PIR:** Calculated field - business days between Resolution_Date and PIR_Completion_Date
- **SLA_Met:** Yes / No / N/A (auto-calculated)
- **Participants_Count:** Number of people who participated in the PIR
- **Participant_Requirement_Met:** Yes / No - Did the review include the incident owner AND at least one additional stakeholder?
- **PIR_Quality_Score:** 1-5 rating based on the quality criteria in Section B below
- **Evidence_Ref:** Link to the PIR report document

**Section B - PIR Quality Scoring Criteria**

Score each completed PIR on a 1-5 scale:

| Score | Criteria |
|-------|----------|
| **5 - Excellent** | Complete incident timeline documented; full impact assessment; all action items defined with owners and dates; root cause referenced; distributed to stakeholders |
| **4 - Good** | Timeline and impact documented; most action items defined; minor gaps in distribution or owner assignment |
| **3 - Adequate** | Basic incident summary present; some action items defined; distribution incomplete or delayed |
| **2 - Poor** | Minimal documentation; few or no action items; no distribution; does not meet policy requirements |
| **1 - Non-existent** | PIR marked as completed but no substantive report exists, or report contains only incident ID and date |

**Section C - PIR Process Summary**

- **Total incidents in scope:** [count]
- **PIRs completed:** [count]
- **PIRs overdue:** [count]
- **PIRs pending:** [count]
- **PIR completion rate (%):** [formula]
- **SLA compliance rate (%):** [formula - PIRs meeting SLA / PIRs completed]
- **Average PIR quality score:** [formula]
- **Average days to PIR (all completed):** [formula]

### 4.2 Sheet: Root Cause Analysis

This sheet assesses whether root causes are systematically identified and whether findings are deep enough to prevent recurrence.

**Section A - RCA Inventory (Critical and High Incidents)**

For each Critical or High incident in the assessment period:

- **Incident_ID:** Cross-reference to PIR Process sheet
- **Severity:** Critical / High
- **RCA_Status:** Completed / Overdue / Not_Performed / In_Progress
- **RCA_Completion_Date:** Date the RCA was finalised
- **RCA_Methodology:** Documented methodology used (5_Whys / Fishbone / Fault_Tree / Timeline_Analysis / Other / None)
- **Immediate_Cause:** The direct technical or operational trigger (e.g., "Unpatched vulnerability exploited")
- **Root_Cause:** The underlying systemic cause identified by the RCA (e.g., "Patch management process does not cover legacy systems in DMZ")
- **Root_Cause_Depth:** Score 1-3:
  - **3 - Systemic:** Root cause addresses process, governance, or organisational gap
  - **2 - Procedural:** Root cause addresses a gap in documented procedures or training
  - **1 - Technical:** Root cause is limited to a technical failure with no process-level analysis
- **Recurring_Root_Cause:** Yes / No - Has this same root cause appeared in a previous incident?
- **Corrective_Actions_Count:** Number of corrective actions mapped to this RCA
- **Evidence_Ref:** Link to the RCA report

**Section B - RCA Quality Assessment**

For each completed RCA, answer:

1. Is the root cause clearly distinguishable from the immediate cause? (Yes / No)
2. Does the root cause statement explain WHY the immediate cause was possible? (Yes / No)
3. Are corrective actions directly linked to the root cause (not just the symptoms)? (Yes / No)
4. Has the RCA been reviewed by someone other than the incident owner? (Yes / No)

**Section C - Recurring Root Cause Analysis**

Identify all root causes that appear in more than one incident during the assessment period. For each recurring root cause:

- **Root_Cause_Statement:** Description of the recurring root cause
- **Occurrences:** Number of incidents sharing this root cause
- **First_Occurrence:** Date of first incident with this root cause
- **Latest_Occurrence:** Date of most recent incident
- **Corrective_Action_Status:** Is a systemic corrective action in progress or completed?
- **Risk_Register_Update:** Has this recurring pattern been documented in the organisational risk register?

### 4.3 Sheet: Lessons Learned & Knowledge Management

This sheet assesses whether learning is captured, distributed, and institutionalised.

**Section A - Lessons Learned Log (Per PIR)**

For each completed PIR in the assessment period:

- **PIR_Reference:** Cross-reference to PIR Process sheet
- **Lesson_ID:** Auto-generated (e.g., LL-2025-001)
- **Lesson_Category:** Classification of the lesson (Detection / Response / Communication / Governance / Technology / Training / Process / Other)
- **Lesson_Summary:** Brief description of the lesson learned (what was learned and why it matters)
- **Applicable_Teams:** Which teams or functions this lesson is relevant to (e.g., SOC, IT Ops, Security Engineering, Management)
- **Distribution_Date:** Date lessons were communicated to applicable teams
- **Distribution_Method:** How lessons were communicated (Email / Team_Meeting / Knowledge_Base_Update / Training / All_of_the_Above)
- **SLA_Met:** Yes / No - Was distribution completed within 10 business days of PIR completion?
- **Playbook_Update_Required:** Yes / No - Does this lesson necessitate a playbook update?
- **Playbook_Updated:** Yes / No / N/A
- **Playbook_Update_Date:** Date the relevant playbook was updated
- **Playbook_SLA_Met:** Yes / No / N/A - Was the playbook updated within 20 business days of PIR completion?
- **Evidence_Ref:** Link to lessons learned entry and any playbook revision

**Section B - Knowledge Base Inventory**

Assess the current state of the knowledge base:

| Item | Status | Last_Updated | Next_Review_Due | Gap_Identified |
|------|--------|--------------|-----------------|----------------|
| Incident classification playbook | Exists / Outdated / Missing | [Date] | [Date] | Yes / No |
| Per-category response playbooks (list each category) | Exists / Outdated / Missing | [Date] | [Date] | Yes / No |
| Escalation procedures | Exists / Outdated / Missing | [Date] | [Date] | Yes / No |
| Communication templates (internal/external/regulatory) | Exists / Outdated / Missing | [Date] | [Date] | Yes / No |
| Forensic procedures quick reference | Exists / Outdated / Missing | [Date] | [Date] | Yes / No |
| Post-incident review template | Exists / Outdated / Missing | [Date] | [Date] | Yes / No |
| Lessons learned index | Exists / Outdated / Missing | [Date] | [Date] | Yes / No |
| Training materials (incident awareness) | Exists / Outdated / Missing | [Date] | [Date] | Yes / No |

**Section C - Knowledge Base Governance**

- Is the knowledge base searchable? (Yes / No)
- Is there a designated owner responsible for knowledge base maintenance? (Yes / No / Name: ___)
- Is the knowledge base reviewed and curated on a quarterly basis? (Yes / No - Evidence: ___)
- Are incident teams informed when relevant knowledge base entries are updated? (Yes / No)

### 4.4 Sheet: Control Improvement Tracking

This sheet assesses whether remediation actions from incidents are tracked, owned, and closed with verification.

**Section A - Remediation Action Register**

For each remediation action derived from an incident in the assessment period:

- **Action_ID:** Auto-generated (e.g., RA-2025-001)
- **Source_Incident_ID:** The incident that generated this action
- **Source_PIR_ID:** The PIR that identified this action
- **Action_Description:** What needs to be done
- **Priority:** Critical / High / Medium / Low (must align with incident severity and risk assessment)
- **Owner:** Name and role of the person responsible for implementation
- **Department:** Owning department or team
- **Target_Date:** Planned completion date (DD.MM.YYYY)
- **Status:** Not_Started / In_Progress / Completed / Blocked / Cancelled
- **Completion_Date:** Date the action was completed (blank if not yet completed)
- **Overdue:** Yes / No (auto-calculated: Completion_Date > Target_Date AND Status != Completed)
- **Escalation_Triggered:** Yes / No - For overdue Critical/High actions, was escalation to CISO triggered within 5 business days of missed deadline?
- **Closure_Verified_By:** Name of person who independently verified closure (must NOT be the owner)
- **Closure_Verification_Date:** Date verification was performed
- **Closure_Verified:** Yes / No / N/A (N/A if action not yet completed)
- **Evidence_Ref:** Link to implementation evidence and closure verification

**Section B - Action Summary Metrics**

- **Total actions in scope:** [count]
- **Actions by status:** Not_Started / In_Progress / Completed / Blocked / Cancelled [counts]
- **Actions by priority:** Critical / High / Medium / Low [counts]
- **Closure rate (all):** Completed / Total x 100
- **Closure rate (Critical):** Completed Critical / Total Critical x 100
- **Closure rate (High):** Completed High / Total High x 100
- **Overdue actions (Critical):** [count] - each must have escalation evidence
- **Overdue actions (High):** [count] - each must have escalation evidence
- **Self-verified closures (non-compliant):** [count] - where Closure_Verified_By = Owner
- **Actions without owner:** [count]
- **Actions without target date:** [count]

**Section C - Blocked Actions Analysis**

For each action with Status = Blocked:

- **Action_ID:** Reference
- **Block_Reason:** Why is this action blocked? (Budget / Resource / Technical_Dependency / Governance / Other)
- **Block_Since_Date:** When did the action become blocked?
- **Escalation_Path:** Who has been notified?
- **Expected_Unblock_Date:** When is resolution expected?

### 4.5 Sheet: Trend Analysis & Metrics

This sheet assesses whether incident trends are tracked, reported, and used for decision-making.

**Section A - KPI Definitions and Current Values**

For each required KPI, document the current value and compare to targets:

| KPI_ID | KPI_Name | Measurement_Unit | Target_Value | Current_Value | Met_Target | Trend | Reporting_Period | Evidence_Ref |
|--------|----------|------------------|--------------|---------------|------------|-------|------------------|--------------|
| KPI-01 | Mean Time to Detect (MTTD) | Minutes | [Org target] | [Current] | Yes/No/At_Risk | Improving/Stable/Degrading | [Period] | [Ref] |
| KPI-02 | Mean Time to Respond (MTTR) | Minutes | [Org target] | [Current] | Yes/No/At_Risk | Improving/Stable/Degrading | [Period] | [Ref] |
| KPI-03 | Mean Time to Resolve | Hours | [Org target] | [Current] | Yes/No/At_Risk | Improving/Stable/Degrading | [Period] | [Ref] |
| KPI-04 | Incident Recurrence Rate | Percentage | <=15% | [Current] | Yes/No/At_Risk | Improving/Stable/Degrading | [Period] | [Ref] |
| KPI-05 | PIR Completion Rate | Percentage | 100% | [Current] | Yes/No/At_Risk | Improving/Stable/Degrading | [Period] | [Ref] |
| KPI-06 | PIR SLA Compliance Rate | Percentage | >=95% | [Current] | Yes/No/At_Risk | Improving/Stable/Degrading | [Period] | [Ref] |
| KPI-07 | RCA Completion Rate (Crit/High) | Percentage | 100% | [Current] | Yes/No/At_Risk | Improving/Stable/Degrading | [Period] | [Ref] |
| KPI-08 | Lessons Learned Distribution SLA | Percentage | >=90% | [Current] | Yes/No/At_Risk | Improving/Stable/Degrading | [Period] | [Ref] |
| KPI-09 | Remediation Closure Rate | Percentage | >=85% | [Current] | Yes/No/At_Risk | Improving/Stable/Degrading | [Period] | [Ref] |
| KPI-10 | Critical Remediation Closure Rate | Percentage | 100% | [Current] | Yes/No/At_Risk | Improving/Stable/Degrading | [Period] | [Ref] |

**Section B - Reporting Cadence Verification**

For each reporting cadence, verify existence and compliance:

| Report_Type | Audience | Frequency | Last_Report_Date | On_Schedule | Distributed | Distribution_List_Complete | Content_Accuracy_Verified | Evidence_Ref |
|-------------|----------|-----------|------------------|-------------|-------------|----------------------------|---------------------------|--------------|
| Monthly Incident Trend Summary | SOC / CSIRT | Monthly | [Date] | Yes/No | Yes/No | Yes/No | Yes/No | [Ref] |
| Quarterly Incident Report | CISO | Quarterly | [Date] | Yes/No | Yes/No | Yes/No | Yes/No | [Ref] |
| Annual Incident Summary | Board / Executive | Annual | [Date] | Yes/No | Yes/No | Yes/No | Yes/No | [Ref] |

**Section C - Trend Accuracy Spot-Check**

Select 3 reported KPI values from the most recent quarterly report and verify against source data:

| KPI_Name | Reported_Value | Source_Verified_Value | Match | Discrepancy_Notes |
|----------|----------------|----------------------|-------|-------------------|
| [KPI 1] | [Value] | [Verified] | Yes/No | [Notes if mismatch] |
| KPI 2] | [Value] | [Verified] | Yes/No | [Notes if mismatch] |
| [KPI 3] | [Value] | [Verified] | Yes/No | [Notes if mismatch] |

**Section D - Period-over-Period Comparison**

Verify that trend reports include comparison to prior periods:

- Does the monthly report compare to the prior month? (Yes / No)
- Does the quarterly report compare to the prior quarter? (Yes / No)
- Does the quarterly report compare to the same quarter last year (year-over-year)? (Yes / No)
- Does the annual report include multi-year trending? (Yes / No)

---

## 5. Evidence Collection Guide

### 5.1 Evidence Types for This Assessment

| Evidence Type | Description | Where to Find |
|---------------|-------------|---------------|
| PIR Reports | Completed Post-Incident Review documents | PIR repository / ticketing system |
| RCA Reports | Root Cause Analysis documents | RCA repository / incident records |
| Lessons Learned Log | Registry of all lessons learned entries | Knowledge management system |
| Playbook Revision History | Change log for all incident playbooks | Version control / document management |
| Distribution Records | Emails or confirmations showing lessons were communicated | Email archives / communication logs |
| Remediation Action Register | Tracking system for all incident-derived actions | Project/action tracking tool |
| Closure Verification Records | Evidence of independent closure verification | Ticketing system / sign-off records |
| Escalation Records | Evidence of escalation for overdue Critical/High actions | Email / ticketing system |
| Trend Reports | Monthly, quarterly, and annual incident reports | Reporting repository |
| KPI Dashboards | Real-time or periodic incident metrics dashboards | SIEM / BI tool screenshots |

### 5.2 Evidence Naming Convention

All evidence files should follow this naming convention:

`EV-S5-[Domain]-[IncidentID or Sequence]-[Date]-[Type].[ext]`

Examples:
- `EV-S5-PIR-INC20250042-20260115-Report.pdf`
- `EV-S5-RCA-INC20250042-20260115-Analysis.pdf`
- `EV-S5-LL-20260115-Log-Export.xlsx`
- `EV-S5-RA-20260131-Register.xlsx`
- `EV-S5-TREND-Q4-2025-Report.pdf`

### 5.3 Evidence Storage

- **Location:** [Organization's evidence repository path]
- **Retention:** Audit cycle + 1 year minimum
- **Access Control:** Restricted to Security Team, Incident Managers, and Auditors
- **Sensitivity Note:** Evidence may contain details of security vulnerabilities - ensure distribution is limited to need-to-know

---

## 6. Common Mistakes to Avoid

| Mistake | Why It Matters | How to Avoid |
|---------|----------------|--------------|
| Counting PIRs as "done" when only the incident is closed | PIR is a separate activity from incident closure - auditors check both | Verify a substantive PIR report exists, not just a closed ticket |
| Accepting "server crashed" as a root cause | This is the immediate cause, not the root cause | Push analysis to WHY the server crashed, and WHY the conditions existed |
| Marking lessons as "distributed" without evidence | Verbal briefings don't count unless documented | Require email confirmation or meeting attendance records |
| Self-verifying remediation action closures | Defeats the purpose of independent verification | Assign verification to someone outside the implementation team |
| Reporting KPIs without verifying accuracy | Inaccurate reports undermine trust and decision-making | Spot-check reported numbers against source incident data |
| Skipping Low-severity incidents entirely | Low-severity patterns can mask systemic risks | At minimum, include Low incidents in quarterly batch PIR review |
| Not updating playbooks after lessons are identified | Playbooks become stale; next incident repeats the same mistakes | Set explicit playbook update deadlines tied to PIR completion |

---

## 7. Quality Checklist

Before submitting for approval, verify:

- [ ] All incidents in scope (last 12 months) have PIR status documented
- [ ] All Critical and High incidents have RCA status documented
- [ ] PIR quality scores are based on the defined 1-5 criteria (Section 4.1)
- [ ] RCA depth scores reflect actual analysis depth (not aspirational)
- [ ] Every completed PIR maps to at least one lessons learned entry
- [ ] Remediation actions have owners, priorities, and target dates
- [ ] Overdue Critical/High actions have escalation evidence
- [ ] Closure verifications are performed by independent parties
- [ ] KPI values in Trend Analysis are cross-checked against source data
- [ ] All three reporting cadences (monthly/quarterly/annual) are verified
- [ ] Evidence Register is complete and all references are valid
- [ ] Gap Analysis sheet accurately reflects findings from all 5 domains
- [ ] No placeholder text or template instructions remain in the workbook

---

## 8. Approval and Sign-Off

### 8.1 Assessment Summary

**Assessment Document:** ISMS-IMP-A.5.24-28.S5 - Learning & Continuous Improvement Assessment
**Assessment Period:** From __________ To __________
**Overall Compliance Rate:** _______ % (from Summary Dashboard)
**Assessment Status:** [ ] Draft [ ] Final [ ] Requires remediation [ ] Re-assessment required

**Key Findings:**
- Total incidents assessed: _______
- PIR completion rate: _______ %
- PIR SLA compliance rate: _______ %
- RCA completion rate (Critical/High): _______ %
- Lessons learned entries documented: _______
- Playbooks requiring update: _______ (updated: _______ )
- Remediation actions tracked: _______ (closed: _______ )
- Critical gaps identified: _______
- High-priority remediation items: _______

---

### 8.2 Assessment Completed By

**Name:** _______________________
**Role:** _______________________
**Department:** _______________________
**Email:** _______________________
**Date:** _______________________
**Signature:** _______________________

**Certification:**
I certify that this assessment was completed with due diligence, all incident learning data is accurate to the best of my knowledge, PIR and RCA records have been verified against source documentation, and all evidence has been collected and properly referenced.

---

### 8.3 Reviewed By (Information Security Officer)

**Name:** _______________________
**Date:** _______________________
**Signature:** _______________________

**Review Comments:**
_________________________________________________________________

**Review Outcome:**
- [ ] Approved - Assessment complete and accurate
- [ ] Approved with minor corrections - Specific items to address: _______
- [ ] Requires revision - Significant issues identified, re-submit required

---

### 8.4 Approved By (CISO)

**Name:** _______________________
**Date:** _______________________
**Signature:** _______________________

**Approval Decision:**
- [ ] Approved - Learning and improvement posture acceptable, remediation plans approved
- [ ] Approved with conditions - Remediation must be completed by: _______
- [ ] Rejected - Re-assessment required due to: _______

**Risk Acceptance:**
For any documented exceptions or gaps where immediate remediation is not feasible, I accept the residual risk based on documented risk assessment, approved compensating controls, and business justification.

---

### 8.5 Next Review Date

**Next Scheduled Assessment:** _______________________

**Review Cycle:** Annual, or upon:
- Discovery of systemic recurring root cause
- Major incident with PIR/RCA process failure
- Significant change to incident management tooling or process
- Audit finding related to A.5.27
- Organisational restructuring affecting incident response teams

**Interim Monitoring:**
- PIR completion and SLA: Monthly
- Remediation action progress: Monthly
- KPI trending: Monthly
- Knowledge base review: Quarterly
- RCA recurring pattern check: Quarterly

---

### 8.6 Distribution List

This assessment shall be distributed to:
- [ ] Chief Information Security Officer (CISO)
- [ ] Information Security Officer (ISO)
- [ ] Incident Response Team Lead / CSIRT Manager
- [ ] SOC Manager
- [ ] Security Engineering Lead
- [ ] IT Management
- [ ] Compliance Team
- [ ] Internal Audit
- [ ] Risk Management
- [ ] Other: _______________________

**Storage Location:**
- **ISMS Repository:** `ISMS/Controls/A.5.24-28_Incident_Management/Assessments/`
- **Filename:** `ISMS-IMP-A.5.24-28.S5_Learning_Improvement_[DATE]_APPROVED.xlsx`

---

# PART II: TECHNICAL SPECIFICATION
**Audience:** Workbook developers, Python script maintainers, Technical reviewers

**Note:** This section provides the technical specification for the Excel assessment workbook generation. Users completing the assessment should refer to Part I above.

---

## Instructions for Completing This Assessment

### How to Use This Document

This technical specification defines the structure, validation rules, and formulas for the Learning & Improvement Assessment Excel workbook (`ISMS-IMP-A.5.24-28.S5_Learning_Improvement_[DATE].xlsx`).

**Workbook Generation:** Python script `generate_a524_28_s5_learning_improvement.py` creates the workbook based on this specification.

**Assessment Completion Process:**

1. **Read each section** and determine if the learning/improvement practice applies to your organisation
2. **Complete the assessment** using the dropdown options and free-text fields as specified
3. **Mark Status:** [X] Compliant / [!] Partial / [N] Non-Compliant / N/A
4. **If [!] or [N]:** Complete the Gap Analysis entry with remediation plan
5. **Provide Evidence:** Document where compliance evidence can be found in the Evidence Register
6. **Review the Summary Dashboard** before submitting for approval

### Status Legend

| Symbol | Meaning | Description |
|--------|---------|-------------|
| **[X]** | **Compliant** | Fully meets policy requirements, no gaps identified |
| **[!]** | **Partial** | Some requirements met, minor gaps exist, remediation planned |
| **[N]** | **Non-Compliant** | Does not meet policy requirements, significant gaps |
| **N/A** | **Not Applicable** | This requirement does not apply (rare in this assessment) |

### Evidence Types

Acceptable evidence includes:
- PIR report documents (PDF or Word)
- RCA report documents
- Lessons learned log exports
- Playbook revision history
- Distribution confirmation records (email screenshots)
- Remediation action tracker exports
- Closure verification sign-off records
- Incident trend reports (monthly/quarterly/annual)
- KPI dashboard screenshots
- Escalation notification records

---

## Workbook Structure

### Sheet Overview (10 Sheets)

| Sheet # | Sheet Name | Purpose |
|---------|------------|---------|
| 1 | Instructions & Legend | Overview, status legend, evidence types, navigation guide |
| 2 | PIR Process | Post-Incident Review inventory, timeliness, quality scoring |
| 3 | Root Cause Analysis | RCA inventory, methodology, depth scoring, recurring causes |
| 4 | Lessons Learned | Lessons log, distribution verification, knowledge base inventory |
| 5 | Control Improvements | Remediation action register, closure verification, blocked actions |
| 6 | Trend Analysis | KPI tracking, reporting cadence verification, trend accuracy |
| 7 | Gap Analysis | Consolidated gap register auto-populated from domain sheets |
| 8 | Evidence Register | Central evidence log with auto-numbering |
| 9 | Summary Dashboard | Compliance overview, KPI summary, critical flags |
| 10 | Approval Sign-Off | Three-level approval workflow |

---

## Sheet 1: Instructions & Legend

### Layout

| Row | Content |
|-----|---------|
| 1-3 | Title block: "ISMS-IMP-A.5.24-28.S5 - Learning & Continuous Improvement Assessment" |
| 5-8 | Document info fields: Organisation, Assessment Date, Assessor Name, Assessment Period |
| 10 | Section header: "Status Legend" |
| 11-15 | Status legend table ([X] / [!] / [N] / N/A with descriptions) |
| 17 | Section header: "Evidence Types" |
| 18-28 | Evidence types list |
| 30 | Section header: "Navigation Guide" |
| 31-40 | Sheet-by-sheet completion instructions and time estimates |
| 42 | Section header: "Quality Checklist" |
| 43-57 | Pre-submission quality checklist items |

---

## Sheet 2: PIR Process

### Section A - PIR Inventory

**Header Row:** Row 5

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Incident_ID | 18 | Text | Free text |
| B | Incident_Date | 14 | Date | DD.MM.YYYY |
| C | Severity | 12 | Dropdown | Critical, High, Medium, Low |
| D | Resolution_Date | 16 | Date | DD.MM.YYYY |
| E | PIR_Status | 14 | Dropdown | Completed, Overdue, Pending, Not_Required |
| F | PIR_Completion_Date | 20 | Date | DD.MM.YYYY |
| G | Policy_SLA_Days | 16 | Number | Auto: 5 (Critical/High), 15 (Medium), 30 (Low) |
| H | Actual_Days_To_PIR | 18 | Number | Formula: business days between D and F |
| I | SLA_Met | 10 | Dropdown | Yes, No, N/A |
| J | Participants_Count | 18 | Number | Integer |
| K | Participant_Req_Met | 20 | Dropdown | Yes, No |
| L | PIR_Quality_Score | 18 | Dropdown | 1, 2, 3, 4, 5 |
| M | Evidence_Ref | 22 | Text | Free text |

**Data Rows:** 6-55 (50 rows - supports up to 50 incidents)

**Conditional Formatting:**
- Column E (PIR_Status): Green = Completed; Yellow = Pending; Red = Overdue
- Column I (SLA_Met): Green = Yes; Red = No
- Column L (PIR_Quality_Score): Green = 4-5; Yellow = 3; Red = 1-2

**Section Header Row:** Row 3 - "Section A: PIR Inventory"

### Section B - PIR Quality Scoring Criteria (Reference)

**Rows 58-68:** Static reference table showing the 1-5 quality scoring criteria. Read-only, informational.

### Section C - PIR Process Summary

**Rows 72-82:** Summary metrics with formulas

| Row | Label | Formula |
|-----|-------|---------|
| 72 | Total incidents in scope | `=COUNTA(A6:A55)` |
| 73 | PIRs completed | `=COUNTIF(E6:E55,"Completed")` |
| 74 | PIRs overdue | `=COUNTIF(E6:E55,"Overdue")` |
| 75 | PIRs pending | `=COUNTIF(E6:E55,"Pending")` |
| 76 | PIR completion rate (%) | `=COUNTIF(E6:E55,"Completed")/COUNTA(E6:E55)*100` |
| 77 | SLA compliance rate (%) | `=COUNTIF(I6:I55,"Yes")/(COUNTIF(I6:I55,"Yes")+COUNTIF(I6:I55,"No"))*100` |
| 78 | Average PIR quality score | `=AVERAGEIF(E6:E55,"Completed",L6:L55)` |
| 79 | Average days to PIR | `=AVERAGEIF(E6:E55,"Completed",H6:H55)` |

---

## Sheet 3: Root Cause Analysis

### Section A - RCA Inventory

**Header Row:** Row 5

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Incident_ID | 18 | Text | Free text (cross-ref to Sheet 2) |
| B | Severity | 12 | Dropdown | Critical, High |
| C | RCA_Status | 16 | Dropdown | Completed, Overdue, Not_Performed, In_Progress |
| D | RCA_Completion_Date | 20 | Date | DD.MM.YYYY |
| E | RCA_Methodology | 20 | Dropdown | 5_Whys, Fishbone, Fault_Tree, Timeline_Analysis, Other, None |
| F | Immediate_Cause | 40 | Text | Free text |
| G | Root_Cause | 45 | Text | Free text |
| H | Root_Cause_Depth | 18 | Dropdown | 3-Systemic, 2-Procedural, 1-Technical |
| I | Recurring_Root_Cause | 20 | Dropdown | Yes, No |
| J | Corrective_Actions_Count | 22 | Number | Integer |
| K | Evidence_Ref | 22 | Text | Free text |

**Data Rows:** 6-35 (30 rows - Critical and High incidents only)

**Conditional Formatting:**
- Column C (RCA_Status): Green = Completed; Yellow = In_Progress; Red = Not_Performed / Overdue
- Column H (Root_Cause_Depth): Green = 3-Systemic; Yellow = 2-Procedural; Red = 1-Technical
- Column I (Recurring_Root_Cause): Red = Yes (flags systemic risk)

### Section B - RCA Quality Assessment

**Rows 40-75:** One block per RCA (up to 30 entries), each containing 4 Yes/No questions.

| Row Offset | Question | Validation |
|------------|----------|------------|
| +0 | RCA Reference (auto from Section A) | Auto |
| +1 | Root cause clearly distinguishable from immediate cause? | Yes, No |
| +2 | Root cause explains WHY immediate cause was possible? | Yes, No |
| +3 | Corrective actions linked to root cause (not symptoms)? | Yes, No |
| +4 | RCA reviewed by someone other than incident owner? | Yes, No |

### Section C - Recurring Root Cause Analysis

**Header Row:** Row 80 (after Section B ends)

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Root_Cause_Statement | 45 | Text | Free text |
| B | Occurrences | 14 | Number | Integer |
| C | First_Occurrence | 18 | Date | DD.MM.YYYY |
| D | Latest_Occurrence | 18 | Date | DD.MM.YYYY |
| E | Corrective_Action_Status | 24 | Dropdown | In_Progress, Completed, Not_Started |
| F | Risk_Register_Updated | 22 | Dropdown | Yes, No |
| G | Evidence_Ref | 22 | Text | Free text |

**Data Rows:** 10 rows for recurring root causes

---

## Sheet 4: Lessons Learned

### Section A - Lessons Learned Log

**Header Row:** Row 5

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | PIR_Reference | 18 | Text | Free text |
| B | Lesson_ID | 16 | Text | Auto: ="LL-"&TEXT(ROW()-5,"000") |
| C | Lesson_Category | 20 | Dropdown | Detection, Response, Communication, Governance, Technology, Training, Process, Other |
| D | Lesson_Summary | 50 | Text | Free text |
| E | Applicable_Teams | 30 | Text | Free text (comma-separated) |
| F | Distribution_Date | 18 | Date | DD.MM.YYYY |
| G | Distribution_Method | 24 | Dropdown | Email, Team_Meeting, KB_Update, Training, Multiple, None |
| H | Distribution_SLA_Met | 18 | Dropdown | Yes, No |
| I | Playbook_Update_Required | 22 | Dropdown | Yes, No |
| J | Playbook_Updated | 18 | Dropdown | Yes, No, N/A |
| K | Playbook_Update_Date | 20 | Date | DD.MM.YYYY |
| L | Playbook_SLA_Met | 18 | Dropdown | Yes, No, N/A |
| M | Evidence_Ref | 22 | Text | Free text |

**Data Rows:** 6-55 (50 rows)

**Conditional Formatting:**
- Column H (Distribution_SLA_Met): Green = Yes; Red = No
- Column J (Playbook_Updated): Green = Yes; Yellow = N/A; Red = No (when I = Yes)
- Column L (Playbook_SLA_Met): Green = Yes; Yellow = N/A; Red = No

### Section B - Knowledge Base Inventory

**Header Row:** Row 60

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | KB_Item | 38 | Text | Pre-filled item list (see Section 4.3) |
| B | Status | 16 | Dropdown | Exists, Outdated, Missing |
| C | Last_Updated | 16 | Date | DD.MM.YYYY |
| D | Next_Review_Due | 18 | Date | DD.MM.YYYY |
| E | Gap_Identified | 16 | Dropdown | Yes, No |
| F | Gap_Description | 40 | Text | Free text (required if E = Yes) |
| G | Evidence_Ref | 22 | Text | Free text |

**Data Rows:** 8 pre-filled items (as listed in Section 4.3 of Part I)

**Conditional Formatting:**
- Column B (Status): Green = Exists; Yellow = Outdated; Red = Missing
- Column E (Gap_Identified): Red = Yes

### Section C - Knowledge Base Governance

**Rows 75-82:** 4 Yes/No questions with notes fields. Static layout.

---

## Sheet 5: Control Improvements

### Section A - Remediation Action Register

**Header Row:** Row 5

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Action_ID | 16 | Text | Auto: ="RA-"&TEXT(ROW()-5,"000") |
| B | Source_Incident_ID | 20 | Text | Free text |
| C | Source_PIR_ID | 16 | Text | Free text |
| D | Action_Description | 45 | Text | Free text |
| E | Priority | 12 | Dropdown | Critical, High, Medium, Low |
| F | Owner | 26 | Text | Free text |
| G | Department | 22 | Text | Free text |
| H | Target_Date | 14 | Date | DD.MM.YYYY |
| I | Status | 16 | Dropdown | Not_Started, In_Progress, Completed, Blocked, Cancelled |
| J | Completion_Date | 18 | Date | DD.MM.YYYY |
| K | Overdue | 10 | Text | Formula: =IF(AND(I5<>"Completed",J5<>"",H5<TODAY()),"Yes","No") |
| L | Escalation_Triggered | 20 | Dropdown | Yes, No, N/A |
| M | Closure_Verified_By | 24 | Text | Free text |
| N | Closure_Verification_Date | 24 | Date | DD.MM.YYYY |
| O | Closure_Verified | 16 | Dropdown | Yes, No, N/A |
| P | Evidence_Ref | 22 | Text | Free text |

**Data Rows:** 6-75 (70 rows)

**Conditional Formatting:**
- Column E (Priority): Red = Critical; Orange = High; Yellow = Medium; Green = Low
- Column I (Status): Green = Completed; Blue = In_Progress; Grey = Not_Started; Red = Blocked
- Column K (Overdue): Red = Yes
- Column O (Closure_Verified): Green = Yes; Red = No (when status = Completed)

### Section B - Action Summary Metrics

**Rows 80-96:** Summary formulas

| Row | Label | Formula |
|-----|-------|---------|
| 80 | Total actions | `=COUNTA(A6:A75)` |
| 81 | Not Started | `=COUNTIF(I6:I75,"Not_Started")` |
| 82 | In Progress | `=COUNTIF(I6:I75,"In_Progress")` |
| 83 | Completed | `=COUNTIF(I6:I75,"Completed")` |
| 84 | Blocked | `=COUNTIF(I6:I75,"Blocked")` |
| 85 | Cancelled | `=COUNTIF(I6:I75,"Cancelled")` |
| 86 | Closure rate (all) | `=COUNTIF(I6:I75,"Completed")/COUNTA(I6:I75)*100` |
| 87 | Closure rate (Critical) | `=COUNTIFS(E6:E75,"Critical",I6:I75,"Completed")/COUNTIF(E6:E75,"Critical")*100` |
| 88 | Closure rate (High) | `=COUNTIFS(E6:E75,"High",I6:I75,"Completed")/COUNTIF(E6:E75,"High")*100` |
| 89 | Overdue Critical | `=COUNTIFS(E6:E75,"Critical",K6:K75,"Yes")` |
| 90 | Overdue High | `=COUNTIFS(E6:E75,"High",K6:K75,"Yes")` |
| 91 | Self-verified (non-compliant) | `=COUNTIF(O6:O75,"Yes")` where M = F (owner = verifier) - flag for manual review |
| 92 | Actions without owner | `=COUNTBLANK(F6:F75)` (where A is not blank) |
| 93 | Actions without target date | `=COUNTBLANK(H6:H75)` (where A is not blank) |

### Section C - Blocked Actions Analysis

**Header Row:** Row 100

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Action_ID | 16 | Text | Cross-ref to Section A |
| B | Block_Reason | 28 | Dropdown | Budget, Resource, Technical_Dependency, Governance, Other |
| C | Block_Since_Date | 18 | Date | DD.MM.YYYY |
| D | Escalation_Path | 34 | Text | Free text |
| E | Expected_Unblock_Date | 22 | Date | DD.MM.YYYY |
| F | Evidence_Ref | 22 | Text | Free text |

**Data Rows:** 10 rows

---

## Sheet 6: Trend Analysis

### Section A - KPI Definitions and Current Values

**Header Row:** Row 5

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | KPI_ID | 10 | Text | Auto: KPI-01 through KPI-10 |
| B | KPI_Name | 38 | Text | Pre-filled (see Section 4.5) |
| C | Measurement_Unit | 18 | Dropdown | Minutes, Hours, Percentage, Count |
| D | Target_Value | 16 | Text | Free text (org-specific target) |
| E | Current_Value | 16 | Text | Free text |
| F | Met_Target | 12 | Dropdown | Yes, No, At_Risk |
| G | Trend | 14 | Dropdown | Improving, Stable, Degrading |
| H | Reporting_Period | 20 | Text | Free text (e.g., "Q4 2025") |
| I | Evidence_Ref | 22 | Text | Free text |

**Data Rows:** 6-15 (10 pre-filled KPIs as defined in Section 4.5)

**Conditional Formatting:**
- Column F (Met_Target): Green = Yes; Yellow = At_Risk; Red = No
- Column G (Trend): Green = Improving; Yellow = Stable; Red = Degrading

### Section B - Reporting Cadence Verification

**Header Row:** Row 20

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Report_Type | 32 | Text | Pre-filled: Monthly / Quarterly / Annual |
| B | Audience | 24 | Text | Pre-filled per report type |
| C | Frequency | 14 | Text | Pre-filled |
| D | Last_Report_Date | 18 | Date | DD.MM.YYYY |
| E | On_Schedule | 14 | Dropdown | Yes, No |
| F | Distributed | 14 | Dropdown | Yes, No |
| G | Distribution_List_Complete | 26 | Dropdown | Yes, No |
| H | Content_Accuracy_Verified | 26 | Dropdown | Yes, No |
| I | Evidence_Ref | 22 | Text | Free text |

**Data Rows:** 3 rows (Monthly / Quarterly / Annual)

**Conditional Formatting:**
- Columns E-H: Green = Yes; Red = No

### Section C - Trend Accuracy Spot-Check

**Header Row:** Row 28

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | KPI_Name | 38 | Text | Free text |
| B | Reported_Value | 18 | Text | Free text |
| C | Source_Verified_Value | 24 | Text | Free text |
| D | Match | 10 | Dropdown | Yes, No |
| E | Discrepancy_Notes | 40 | Text | Free text (required if D = No) |

**Data Rows:** 3 rows

**Conditional Formatting:**
- Column D (Match): Green = Yes; Red = No

### Section D - Period-over-Period Comparison

**Rows 36-42:** 4 Yes/No questions with notes fields. Static layout.

---

## Sheet 7: Gap Analysis

### Structure

**Header Row:** Row 5

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Gap_ID | 12 | Text | Auto: ="GAP-"&TEXT(ROW()-5,"000") |
| B | Source_Sheet | 22 | Dropdown | PIR_Process, Root_Cause_Analysis, Lessons_Learned, Control_Improvements, Trend_Analysis |
| C | Gap_Category | 26 | Dropdown | PIR_Timeliness, PIR_Quality, RCA_Completeness, RCA_Depth, Knowledge_Gap, Distribution_Failure, Remediation_Overdue, Reporting_Gap, Other |
| D | Gap_Description | 48 | Text | Free text |
| E | Priority | 12 | Dropdown | Critical, High, Medium, Low |
| F | Current_Status | 18 | Dropdown | Open, In_Progress, Resolved, Accepted |
| G | Remediation_Action | 45 | Text | Free text |
| H | Owner | 24 | Text | Free text |
| I | Target_Date | 14 | Date | DD.MM.YYYY |
| J | Evidence_Ref | 22 | Text | Free text |

**Data Rows:** 6-35 (30 rows)

**Summary Row (Row 40):**
- Total gaps: `=COUNTA(A6:A35)`
- Critical: `=COUNTIF(E6:E35,"Critical")`
- High: `=COUNTIF(E6:E35,"High")`
- Medium: `=COUNTIF(E6:E35,"Medium")`
- Low: `=COUNTIF(E6:E35,"Low")`
- Open: `=COUNTIF(F6:F35,"Open")`
- Resolved: `=COUNTIF(F6:F35,"Resolved")`

**Conditional Formatting:**
- Column E (Priority): Red = Critical; Orange = High; Yellow = Medium; Green = Low
- Column F (Current_Status): Green = Resolved; Blue = In_Progress; Grey = Open; Yellow = Accepted

---

## Sheet 8: Evidence Register

### Structure

**Header Row:** Row 5

| Column | Header | Width | Type | Validation |
|--------|--------|-------|------|------------|
| A | Evidence_ID | 16 | Text | Auto: ="EV-S5-"&TEXT(ROW()-5,"000") |
| B | Domain | 24 | Dropdown | PIR_Process, Root_Cause_Analysis, Lessons_Learned, Control_Improvements, Trend_Analysis |
| C | Evidence_Type | 28 | Dropdown | PIR_Report, RCA_Report, LL_Log, KB_Entry, Playbook_Revision, Distribution_Record, Action_Register, Closure_Verification, Trend_Report, Dashboard_Screenshot, Other |
| D | Description | 44 | Text | Free text |
| E | File_Name | 34 | Text | Free text |
| F | Storage_Location | 38 | Text | Free text |
| G | Date_Collected | 16 | Date | DD.MM.YYYY |
| H | Collected_By | 24 | Text | Free text |
| I | Related_Incident_ID | 20 | Text | Free text (if applicable) |
| J | Verified | 12 | Dropdown | Yes, No |

**Data Rows:** 6-55 (50 rows)

---

## Sheet 9: Summary Dashboard

### Layout

**Panel 1: Overall Compliance (Rows 3-12)**

| Row | Label | Formula |
|-----|-------|---------|
| 3 | Title | "ISMS-IMP-A.5.24-28.S5 - Summary Dashboard" |
| 5 | Assessment Period | [From PIR Process sheet - auto or manual] |
| 6 | Overall Compliance Rate | Weighted average across all 5 domains |
| 7 | Total Gaps Identified | `='Gap Analysis'!A40 total` |
| 8 | Critical Gaps | `='Gap Analysis'!E40 Critical count` |
| 9 | High Gaps | `='Gap Analysis'!E40 High count` |
| 10 | Gaps Resolved | `='Gap Analysis'!F40 Resolved count` |

**Panel 2: Domain Compliance Scores (Rows 15-24)**

| Row | Domain | Compliance Score (%) | Status |
|-----|--------|----------------------|--------|
| 16 | PIR Process | Formula based on SLA compliance + quality | [X]/[!]/[N] |
| 17 | Root Cause Analysis | Formula based on RCA completion + depth | [X]/[!]/[N] |
| 18 | Lessons Learned | Formula based on LL documentation + distribution | [X]/[!]/[N] |
| 19 | Control Improvements | Formula based on closure rate + verification | [X]/[!]/[N] |
| 20 | Trend Analysis | Formula based on reporting cadence + accuracy | [X]/[!]/[N] |

**Domain Scoring Logic:**
- **PIR Process:** (SLA compliance rate x 0.4) + (Average quality score / 5 x 0.4) + (Participant requirement met rate x 0.2)
- **Root Cause Analysis:** (RCA completion rate x 0.5) + (Average depth score / 3 x 0.3) + (Quality check pass rate x 0.2)
- **Lessons Learned:** (LL entry rate per PIR x 0.3) + (Distribution SLA rate x 0.3) + (Playbook update SLA rate x 0.2) + (KB completeness x 0.2)
- **Control Improvements:** (Closure rate x 0.4) + (Critical closure rate x 0.3) + (Verification compliance x 0.2) + (No-owner/no-date rate inverted x 0.1)
- **Trend Analysis:** (Reporting cadence compliance x 0.4) + (Accuracy spot-check pass rate x 0.3) + (Period comparison completeness x 0.3)

**Panel 3: Key Metrics (Rows 27-38)**

| Metric | Value | Source |
|--------|-------|--------|
| PIR Completion Rate | [%] | Sheet 2 Summary |
| PIR SLA Compliance Rate | [%] | Sheet 2 Summary |
| Avg PIR Quality Score | [1-5] | Sheet 2 Summary |
| RCA Completion Rate (Crit/High) | [%] | Sheet 3 |
| Recurring Root Causes | [count] | Sheet 3 Section C |
| Lessons Learned Entries | [count] | Sheet 4 |
| Playbooks Requiring Update | [count] | Sheet 4 |
| Remediation Actions - Open | [count] | Sheet 5 Summary |
| Remediation Actions - Overdue Critical | [count] | Sheet 5 Summary |
| Reporting Cadence Compliance | [count of 3 met] | Sheet 6 |

**Panel 4: Critical Flags (Rows 41-50)**

Auto-generated flags for immediate attention:

| Flag | Condition | Status |
|------|-----------|--------|
| Overdue Critical Remediation Actions | Count of overdue Critical actions > 0 | [R] / [G] |
| Missing Escalation for Overdue Crit/High | Overdue Crit/High action with Escalation_Triggered = No | [R] / [G] |
| Self-Verified Closures Detected | Any action where owner = closure verifier | [R] / [G] |
| RCA Not Performed for Critical Incident | Any Critical incident with RCA_Status = Not_Performed | [R] / [G] |
| PIR Overdue > 2x SLA | Any PIR where Actual_Days > 2 x Policy_SLA_Days | [R] / [G] |
| Lessons Learned Distribution Failure | Any LL entry where Distribution_SLA_Met = No | [R] / [G] |
| Reporting Gap (Missing Report) | Any reporting cadence with On_Schedule = No | [R] / [G] |
| Knowledge Base Items Missing | Any KB item with Status = Missing | [R] / [G] |

---

## Sheet 10: Approval Sign-Off

### Structure

Static layout mirroring Section 8 of Part I:

| Row | Content |
|-----|---------|
| 3-8 | Assessment Summary block (Period, Compliance Rate, Status checkbox, Key Findings) |
| 12-18 | Completed By block (Name, Role, Department, Email, Date, Signature, Certification text) |
| 22-28 | Reviewed By block (Name, Date, Signature, Review Comments, Outcome checkboxes) |
| 32-40 | Approved By block (Name, Date, Signature, Decision checkboxes, Risk Acceptance statement) |
| 44-50 | Next Review Date block (Date, Review Cycle triggers, Interim Monitoring schedule) |
| 54-65 | Distribution List (checkboxes for each role, Storage Location) |

---

## Validation Dropdowns Summary

| Dropdown Name | Values |
|---------------|--------|
| Severity | Critical, High, Medium, Low |
| PIR_Status | Completed, Overdue, Pending, Not_Required |
| SLA_Met | Yes, No, N/A |
| RCA_Status | Completed, Overdue, Not_Performed, In_Progress |
| RCA_Methodology | 5_Whys, Fishbone, Fault_Tree, Timeline_Analysis, Other, None |
| Root_Cause_Depth | 3-Systemic, 2-Procedural, 1-Technical |
| Recurring | Yes, No |
| Lesson_Category | Detection, Response, Communication, Governance, Technology, Training, Process, Other |
| Distribution_Method | Email, Team_Meeting, KB_Update, Training, Multiple, None |
| KB_Status | Exists, Outdated, Missing |
| Action_Status | Not_Started, In_Progress, Completed, Blocked, Cancelled |
| Block_Reason | Budget, Resource, Technical_Dependency, Governance, Other |
| Met_Target | Yes, No, At_Risk |
| Trend | Improving, Stable, Degrading |
| Gap_Category | PIR_Timeliness, PIR_Quality, RCA_Completeness, RCA_Depth, Knowledge_Gap, Distribution_Failure, Remediation_Overdue, Reporting_Gap, Other |
| Gap_Status | Open, In_Progress, Resolved, Accepted |
| Priority | Critical, High, Medium, Low |
| Status | [X] Compliant, [!] Partial, [N] Non-Compliant, N/A |
| Evidence_Type | PIR_Report, RCA_Report, LL_Log, KB_Entry, Playbook_Revision, Distribution_Record, Action_Register, Closure_Verification, Trend_Report, Dashboard_Screenshot, Other |

---

## Appendix: Technical Notes for Workbook Developers

### A.1 Excel Workbook Structure

**Sheet Names (10 sheets total):**
1. Instructions & Legend
2. PIR Process
3. Root Cause Analysis
4. Lessons Learned
5. Control Improvements
6. Trend Analysis
7. Gap Analysis
8. Evidence Register
9. Summary Dashboard
10. Approval Sign-Off

### A.2 Conditional Formatting Summary

| Sheet | Column | Rule | Format |
|-------|--------|------|--------|
| PIR Process | E | Completed | Green fill |
| PIR Process | E | Overdue | Red fill |
| PIR Process | E | Pending | Yellow fill |
| PIR Process | I | Yes | Green fill |
| PIR Process | I | No | Red fill |
| PIR Process | L | 4-5 | Green fill |
| PIR Process | L | 3 | Yellow fill |
| PIR Process | L | 1-2 | Red fill |
| RCA | C | Completed | Green fill |
| RCA | C | Not_Performed / Overdue | Red fill |
| RCA | H | 3-Systemic | Green fill |
| RCA | H | 2-Procedural | Yellow fill |
| RCA | H | 1-Technical | Red fill |
| RCA | I | Yes (recurring) | Red fill |
| Lessons Learned | H | Yes | Green fill |
| Lessons Learned | H | No | Red fill |
| Control Improvements | E | Critical | Red fill |
| Control Improvements | E | High | Orange fill |
| Control Improvements | K | Yes (overdue) | Red fill |
| Control Improvements | O | No (when Completed) | Red fill |
| Trend Analysis | F | Yes | Green fill |
| Trend Analysis | F | No | Red fill |
| Trend Analysis | G | Improving | Green fill |
| Trend Analysis | G | Degrading | Red fill |
| Gap Analysis | E | Critical | Red fill |
| Gap Analysis | F | Resolved | Green fill |
| Gap Analysis | F | Open | Grey fill |

### A.3 Cell Protection

**Protected:** All formula cells, headers, static reference tables, pre-filled labels
**Unprotected (input cells):** All data entry fields (yellow fill recommended), date fields, dropdown selections, free-text fields

### A.4 Python Script Integration Points

**Script:** `generate_a524_28_s5_learning_improvement.py`

**Key Functions:**
- `create_workbook()` - Master workbook creation and sheet ordering
- `setup_styles()` - Style definitions (header, input, formula, flag)
- `create_instructions_sheet()` - Sheet 1 layout
- `create_pir_process_sheet()` - Sheet 2: inventory table + quality criteria + summary formulas
- `create_rca_sheet()` - Sheet 3: inventory + quality questions + recurring causes table
- `create_lessons_learned_sheet()` - Sheet 4: LL log + KB inventory + governance questions
- `create_control_improvements_sheet()` - Sheet 5: action register + summary metrics + blocked analysis
- `create_trend_analysis_sheet()` - Sheet 6: KPI table + reporting cadence + spot-check + comparison
- `create_gap_analysis_sheet()` - Sheet 7: consolidated gap register with summary row
- `create_evidence_register_sheet()` - Sheet 8: evidence log with auto-numbering
- `create_summary_dashboard_sheet()` - Sheet 9: 4-panel dashboard with scoring formulas and critical flags
- `create_approval_sheet()` - Sheet 10: static approval layout

**QA Script:** `excel_sanity_check_a524_28_s5.py`

### A.5 Version Control

- Filename: `ISMS-IMP-A.5.24-28.S5_Learning_Improvement_YYYYMMDD.xlsx`
- v1.0: Initial release - full 10-sheet assessment workbook

---

**END OF PART II: TECHNICAL SPECIFICATION**

---

**Quality Checks Before Finalising:**
- [ ] All cross-references to S1-S4 documents are accurate
- [ ] Document Control version shows 1.0
- [ ] Dates in DD.MM.YYYY format throughout
- [ ] Policy SLA values match ISMS-POL-A.5.24-28 (Critical/High: 5 days, Medium: 15 days, Low: 30 days)
- [ ] All 10 KPIs in Trend Analysis are defined and targets populated
- [ ] Dashboard scoring formulas verified against domain sheet structures
- [ ] Critical Flags logic verified (conditions and cell references)
- [ ] Evidence naming convention documented and consistent
- [ ] No placeholder or template-only content remains

---

**END OF SPECIFICATION**

---

*"The idea is to try to give all the information to help others to judge the value of your contribution."*
— Richard Feynman

<!-- QA_VERIFIED: 2026-02-02 -->
