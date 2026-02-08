**ISMS-IMP-A.5.24-28.S5-UG - Learning & Continuous Improvement Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.27

---

## Document Control

| Field | Value |
|-------|-------|
| **Document Title** | Learning & Continuous Improvement Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.5.24-28.S5-UG |
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

**Audience:** Incident Managers, CSIRT/SOC Leads, Security Operations Teams, Compliance Officers

---

## Assessment Overview

### Purpose

This assessment evaluates [Organization]'s **post-incident learning and continuous improvement capabilities**, focusing on the **learning** phase of the incident management lifecycle (A.5.27). It determines whether knowledge gained from information security incidents is systematically captured, analysed, and fed back into controls, playbooks, training, and risk assessments.

### What This Assessment Measures

**Scope - 5 learning and improvement domains:**

1. **Post-Incident Review (PIR) Process** - Timeliness, completeness, and quality of post-incident reviews
2. **Root Cause Analysis (RCA)** - Depth, methodology, and accuracy of root cause identification
3. **Lessons Learned & Knowledge Management** - Documentation, dissemination, and knowledge base maintenance
4. **Control Improvement Tracking** - Remediation actions derived from incidents, ownership, and closure
5. **Trend Analysis & Metrics Reporting** - Incident KPIs, trend identification, and executive/board reporting

**Assessment Output:** Excel workbook documenting PIR effectiveness, RCA quality, lessons learned coverage, improvement tracking status, trend metrics, compliance gaps, and remediation plans.

### Why This Matters

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

### Who Should Complete This Assessment

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

### Time Estimate

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

### Connection to Policy

This assessment implements **ISMS-POL-A.5.24-28, Section on A.5.27 (Learning)** which defines mandatory requirements for:
- Post-Incident Review completion within defined timeframes per severity
- Root cause analysis for all incidents rated High or above
- Lessons learned documentation and distribution
- Control improvement actions with ownership and deadlines
- Incident trend reporting to management and board
- Feedback loop into playbooks, training, and risk assessment

**Policy Authority:** Chief Information Security Officer (CISO)
**Compliance Status:** Mandatory for all information security incidents

### Critical Policy Requirements Summary

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

## Prerequisites

### Information Required

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

### Access Required

- [ ] Incident ticketing system (read access to all incidents, last 12 months)
- [ ] PIR/RCA document repository
- [ ] Knowledge base or playbook repository
- [ ] Remediation action tracking system
- [ ] Trend reporting dashboards or report storage

### Knowledge Required

**Essential Understanding:**
- [Organization]'s incident management lifecycle and ticketing workflow
- PIR process and RCA methodology in use
- Knowledge base structure and maintenance practices
- Remediation action lifecycle (creation -> assignment -> tracking -> closure -> verification)
- Incident reporting cadence and distribution

### Estimated Time Commitment

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

## Assessment Workflow

### Recommended Completion Sequence

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

### Quality Checkpoints

After completing each domain sheet, pause and verify:

| Checkpoint | Verify |
|------------|--------|
| After PIR Process | Every incident in scope has a PIR status; all completed PIRs have timeliness scored |
| After RCA | All Critical/High incidents have RCA status; depth scoring completed |
| After Lessons Learned | Every completed PIR maps to >=1 lessons learned entry; distribution verified |
| After Control Improvements | All actions have owner + target date; overdue items flagged |
| After Trend Analysis | All three reporting cadences (monthly/quarterly/annual) verified; KPIs cross-checked |

---

## Question-by-Question Guidance

### Sheet: PIR Process

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

### Sheet: Root Cause Analysis

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

### Sheet: Lessons Learned & Knowledge Management

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

### Sheet: Control Improvement Tracking

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

### Sheet: Trend Analysis & Metrics

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

## Evidence Collection Guide

### Evidence Types for This Assessment

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

### Evidence Naming Convention

All evidence files should follow this naming convention:

`EV-S5-[Domain]-[IncidentID or Sequence]-[Date]-[Type].[ext]`

Examples:
- `EV-S5-PIR-INC20250042-20260115-Report.pdf`
- `EV-S5-RCA-INC20250042-20260115-Analysis.pdf`
- `EV-S5-LL-20260115-Log-Export.xlsx`
- `EV-S5-RA-20260131-Register.xlsx`
- `EV-S5-TREND-Q4-2025-Report.pdf`

### Evidence Storage

- **Location:** [Organization's evidence repository path]
- **Retention:** Audit cycle + 1 year minimum
- **Access Control:** Restricted to Security Team, Incident Managers, and Auditors
- **Sensitivity Note:** Evidence may contain details of security vulnerabilities - ensure distribution is limited to need-to-know

---

## Common Mistakes to Avoid

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

## Quality Checklist

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

## Approval and Sign-Off

### Assessment Summary

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

### Assessment Completed By

**Name:** _______________________
**Role:** _______________________
**Department:** _______________________
**Email:** _______________________
**Date:** _______________________
**Signature:** _______________________

**Certification:**
I certify that this assessment was completed with due diligence, all incident learning data is accurate to the best of my knowledge, PIR and RCA records have been verified against source documentation, and all evidence has been collected and properly referenced.

---

### Reviewed By (Information Security Officer)

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

### Approved By (CISO)

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

### Next Review Date

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

### Distribution List

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

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
