# ISMS-IMP-A.8.12.4 - Monitoring & Response Assessment
# PART 1: USER COMPLETION GUIDE

---

## Document Control

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.12.4 |
| **Version** | 1.0 |
| **Assessment Area** | DLP Monitoring, Alert Management, and Incident Response |
| **Related Policy** | ISMS-POL-A.8.12 (Data Leakage Prevention Policy) - Section 2.3 |
| **Purpose** | Assess DLP monitoring effectiveness, SOC integration, alert response times, false positive management, and incident response capabilities to ensure DLP events are detected, analyzed, and remediated promptly |
| **Target Audience** | SOC Analysts, DLP Administrators, Incident Response Team, SIEM Engineers, Security Operations Manager, CISO |
| **Assessment Type** | Operational Effectiveness & Response Capability |
| **Review Cycle** | Quarterly or After Major DLP Tuning / Incident |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for Monitoring & Response assessment | ISMS Implementation Team |

---

# PART I: USER COMPLETION GUIDE
**Audience:** SOC Analysts, DLP Administrators, Incident Response Team, SIEM Engineers

---

## 1. Assessment Overview

### 1.1 What This Assessment Measures

This assessment evaluates [Organization]'s **DLP monitoring and incident response effectiveness** to ensure compliance with ISO/IEC 27001:2022 Control A.8.12 and operational security objectives.

**Scope:** 5 assessment domains covering DLP operational effectiveness:
1. **Alert Management** - Alert volume, triage process, backlog, escalation procedures
2. **SIEM Integration** - Log forwarding, correlation rules, dashboard visibility, retention
3. **SOC Playbooks** - Documented procedures, analyst training, escalation paths
4. **False Positive Tuning** - FP rate, tuning process, pattern accuracy, user feedback
5. **Incident Response Metrics** - MTTR (Mean Time to Respond), containment speed, evidence preservation

**Assessment Output:** Excel workbook with ~55 monitoring effectiveness checkpoints documenting alert handling, SOC integration status, response times, and tuning effectiveness.

### 1.2 Why This Matters

**ISO 27001:2022 Control A.8.12 Requirement:**
> *"Data leakage prevention measures should be applied to systems, networks and any other devices that process, store or transmit sensitive information."*

**Critical Principle:** DLP without effective monitoring = **security theater**. If alerts are not reviewed, analyzed, and acted upon, data leakage occurs undetected.

**Regulatory Context:**
- **Swiss nDSG (Art. 8):** Requires appropriate technical measures against data loss (includes detection and response)
- **EU GDPR (Art. 32, 33):** Requires ability to detect, investigate, and report personal data breaches within 72 hours
- **Industry Standards:** PCI DSS (Req. 10, 12.10), HIPAA (§164.308), SOC 2 all require security monitoring and incident response

**Business Impact:**
- **Unmonitored DLP = Undetected Breaches:** Alerts generated but not reviewed = data leakage happens, organization doesn't know
- **Slow Response = Larger Breach:** MTTR of 24 hours vs. 1 hour = 24× more data exfiltrated
- **Alert Fatigue = Missed Critical Alerts:** 1000 alerts/day, 95% false positives = SOC ignores all alerts, including real breaches
- **Compliance Violations:** GDPR requires breach notification within 72 hours - need monitoring to detect breaches within that window

**Why Monitoring & Response Assessment Matters:**
- **Operational Reality Check:** Is DLP actually monitored or just deployed and forgotten?
- **Response Time Validation:** How long from alert to containment? (MTTR measurement)
- **Tuning Effectiveness:** Is false positive rate acceptable? (<10% target)
- **SOC Integration:** Are DLP alerts in SIEM? Do SOC analysts understand DLP alerts?
- **Incident Preparedness:** Can organization respond to data leakage incident?

### 1.3 Who Should Complete This Assessment

**Primary Responsibility:** SOC Manager, DLP Administrator, SIEM Engineer (collaborative assessment)

**Required Knowledge:**
- DLP alert types and severity levels (critical, high, medium, low)
- SOC alert triage process (how alerts are reviewed and escalated)
- SIEM architecture and DLP log integration
- Incident response procedures for data leakage events
- False positive tuning methodology

**Support Roles:**
- **SOC Analysts:** Day-to-day alert handling, triage, escalation experience
- **Incident Response Team:** Data breach response procedures, containment actions
- **SIEM Engineers:** Log forwarding, correlation rules, dashboard configuration
- **DLP Administrators:** Alert policy configuration, tuning, pattern updates
- **CISO:** Oversight, resource allocation, escalation path approval

### 1.4 Time Estimate

**Total Assessment Time:** 4-6 hours (depending on DLP alert volume and SOC maturity)

**Breakdown:**
- **Alert Volume Analysis:** 1-2 hours (review last 30 days DLP alerts, calculate metrics)
- **SOC Integration Verification:** 1 hour (verify SIEM forwarding, correlation rules, dashboards)
- **Playbook Review:** 1 hour (review incident response procedures, interview SOC analysts)
- **Tuning Assessment:** 1-2 hours (calculate FP rate, review tuning history, test pattern accuracy)
- **Incident Response Testing:** 30-60 minutes (tabletop exercise or review recent incidents)
- **Evidence Collection:** 30 minutes (screenshots, logs, procedure documents)
- **Quality Review:** 30 minutes (self-check using Section 7 quality checklist)

**Pro Tip:** Schedule assessment during low-alert period (not during major incident). Involve SOC analysts who actually handle DLP alerts daily for realistic feedback.

### 1.5 Connection to Policy

This assessment implements **ISMS-POL-A.8.12 (Data Leakage Prevention Policy)** Section 2.3 (Monitoring & Detection Requirements) which mandates:

**Policy Requirements Verified:**
- **Section 2.3 - Continuous Monitoring:** 24/7 DLP alert monitoring (for Critical/High alerts)
- **Section 2.3 - SIEM Integration:** All DLP alerts forwarded to SIEM, correlation rules enabled
- **Section 2.3 - Alert Response Times:** MTTR targets (Critical <1 hour, High <4 hours, Medium <24 hours)
- **Section 2.3 - False Positive Management:** FP rate <10%, quarterly tuning review
- **Section 3.2 - Assessment & Verification:** Quarterly monitoring effectiveness review
- **Section 4.2 - Implementation Resources:** Structured assessment workbooks

**Policy Authority:** Chief Information Security Officer (CISO)  
**Compliance Status:** Mandatory for all DLP deployments

**Relationship to Other Assessments:**
- **A.8.12.1 (DLP Infrastructure):** Verifies DLP technology exists → THIS assessment verifies DLP ALERTS are monitored
- **A.8.12.2 (Data Classification):** Defines sensitive data → THIS assessment verifies ALERTS for that data are handled
- **A.8.12.3 (Channel Coverage):** Verifies DLP deployed → THIS assessment verifies ALERTS from those channels reach SOC
- **A.8.12.5 (Compliance Dashboard):** Consolidates all assessments → THIS provides alert/response metrics

### 1.6 Critical: DLP Value = Monitoring Effectiveness

**⚠️ IMPORTANT - Deployed DLP Without Monitoring = Wasted Investment:**

Organizations commonly deploy DLP technology but fail to establish effective monitoring, resulting in undetected data leakage despite DLP deployment.

**DLP Monitoring Maturity Levels:**

| Level | Characteristics | Impact | Action Required |
|-------|----------------|--------|-----------------|
| **Level 0: No Monitoring** | DLP deployed, alerts generated, nobody reviews | DLP completely ineffective, data leaks undetected | Establish basic alert triage |
| **Level 1: Reactive** | Alerts reviewed occasionally (weekly), large backlog | Breaches detected days/weeks late | Daily alert review, reduce backlog |
| **Level 2: Managed** | Daily alert review, documented procedures, SIEM integrated | Effective for most incidents, some delays | Implement 24/7 coverage, automate triage |
| **Level 3: Optimized** | 24/7 SOC coverage, automated triage, SOAR integration, <10% FP rate | Highly effective, rapid response | Focus on advanced threats, continuous improvement |

**Common Monitoring Failures:**

| Failure Mode | Symptom | Consequence |
|--------------|---------|-------------|
| **Alert Overload** | 500+ alerts/day, SOC ignores all | Critical alerts buried in noise, breaches missed |
| **No SOC Integration** | DLP alerts in separate console, not SIEM | SOC doesn't see DLP alerts, no investigation |
| **No Documented Procedures** | Each analyst handles differently | Inconsistent response, missed escalations |
| **Slow Response** | MTTR >24 hours | Data fully exfiltrated before containment |
| **No Tuning** | FP rate >50% | SOC stops trusting DLP, ignores alerts |
| **No Incident Response Plan** | No procedures for data breach | Chaotic response, evidence lost, notification delays |

**What This Means for Assessment:**
1. **Honest assessment critical:** Don't claim "24/7 monitoring" if alerts sit unreviewed for days
2. **Measure actual MTTR:** Not policy (should be <1 hour) but reality (what is it actually?)
3. **Test SOC knowledge:** Do analysts know what DLP alerts mean? Can they respond?
4. **Verify SIEM integration:** Are DLP alerts actually in SIEM or just promised?
5. **Calculate FP rate:** Measure, don't guess (sample 100 alerts, how many are real?)

---

## 2. Prerequisites

### 2.1 Access Required

**DLP System Access:**
- [ ] DLP management console (alert queue, alert history, blocked events)
- [ ] DLP alert configuration (severity levels, notification rules, escalation)
- [ ] DLP tuning history (pattern changes, exception approvals, FP tracking)

**SIEM/SOC Access:**
- [ ] SIEM console (Splunk, QRadar, Sentinel, LogRhythm, etc.)
- [ ] DLP log source configuration (is DLP forwarding logs?)
- [ ] Correlation rules involving DLP events
- [ ] SOC dashboards showing DLP alerts
- [ ] Alert queue/ticketing system (ServiceNow, Jira, etc.)

**Documentation:**
- [ ] SOC playbooks for DLP incidents (step-by-step procedures)
- [ ] Incident response plan for data leakage
- [ ] Escalation procedures (when to involve CISO, Legal, DPO)
- [ ] Alert severity definitions (what makes alert Critical vs. High vs. Medium)

**Metrics & Logs:**
- [ ] DLP alert logs (last 30-90 days)
- [ ] SOC ticket history for DLP incidents
- [ ] MTTR metrics (if already calculated)
- [ ] False positive tracking (if maintained)
- [ ] Incident reports from recent DLP events

### 2.2 Knowledge Required

**Essential Understanding:**
- How DLP alerts are generated (what triggers alert)
- SOC alert triage process (how alerts are reviewed and prioritized)
- SIEM log ingestion and correlation
- Incident response lifecycle (detection → analysis → containment → eradication → recovery → lessons learned)
- Difference between false positive (non-sensitive data flagged) and true positive (actual sensitive data leak)

**Technical Skills:**
- Query SIEM for DLP events (SPL for Splunk, KQL for Sentinel, etc.)
- Read DLP logs and understand event details
- Calculate metrics (FP rate, MTTR, alert volume trends)
- Review SOC procedures and identify gaps

**NOT Required:**
- Deep SIEM architecture expertise
- Advanced correlation rule development
- Digital forensics expertise

### 2.3 Tools Needed

**Analysis Tools:**
- **SIEM query interface:** To extract DLP alert data
- **Spreadsheet tool:** To calculate metrics (FP rate, MTTR, volume trends)
- **Ticketing system access:** To review incident handling

**Testing Tools:**
- **DLP test alerts:** Ability to generate test alert (send test email with fake SSN)
- **SIEM search:** Verify test alert appears in SIEM

**Documentation Tools:**
- **Screenshot capability:** SOC dashboards, alert queues, SIEM queries
- **Procedure documentation:** Export SOC playbooks, incident response plans

### 2.4 Estimated Time Commitment

**Phase 1: Alert Volume Analysis (1-2 hours)**
- Extract last 30 days DLP alerts from SIEM/DLP console
- Calculate: Total alerts, alerts/day average, by severity (Critical, High, Medium, Low)
- Calculate: Blocked vs. Allowed (monitoring-only alerts)
- Calculate: By channel (Email, Web, USB, etc.)
- Identify trends: Increasing/decreasing alert volume, spikes, patterns

**Phase 2: SOC Integration Verification (1 hour)**
- Verify DLP logs forwarding to SIEM (check SIEM data source config)
- Test: Generate DLP alert, verify it appears in SIEM (end-to-end test)
- Review correlation rules using DLP events
- Check SOC dashboards: Are DLP alerts visible to SOC analysts?
- Verify alerting: Do Critical/High DLP alerts generate SOC tickets automatically?

**Phase 3: Playbook & Procedure Review (1 hour)**
- Review SOC playbook for DLP incidents (does it exist? is it documented?)
- Interview SOC analysts: Do they know how to handle DLP alerts?
- Review escalation procedures: When to escalate to CISO, Legal, DPO?
- Check incident response plan: Specific procedures for data breach?
- Verify training: Have SOC analysts been trained on DLP alert handling?

**Phase 4: False Positive Tuning Assessment (1-2 hours)**
- Sample 100 recent alerts (random sample across 30 days)
- For each alert: Review, classify as True Positive or False Positive
- Calculate FP rate: (False Positives / Total Alerts) × 100
- Review tuning history: How often are patterns updated? Who approves?
- Check user feedback mechanism: Can users report false positives?

**Phase 5: Incident Response Metrics (1 hour)**
- Calculate MTTR: For last 10 DLP incidents, time from alert to containment
- Review containment actions: What was done to stop data leakage?
- Check evidence preservation: Are DLP logs retained? Are alerts archived?
- Assess notification compliance: Were breaches reported within regulatory timelines (72 hours GDPR)?

**Phase 6: Assessment Completion (30 minutes)**
- Complete all assessment sheets
- Document gaps, create remediation plans
- Collect evidence, populate Evidence Register

**Total:** 4-6 hours

---

## 3. Assessment Workflow

### 3.1 Recommended Completion Sequence

**STEP 1: Initial Setup (10 minutes)**
1. Open workbook: `ISMS-IMP-A.8.12.4_Monitoring_Response_YYYYMMDD.xlsx`
2. Review Instructions_Legend sheet
3. Complete Organization Metadata

**STEP 2: Alert Volume Analysis (1-2 hours)**
1. Navigate to Alert_Management sheet
2. Extract DLP alerts from last 30 days (SIEM or DLP console)
3. Calculate metrics:
   - Total alerts: _______
   - Average alerts/day: _______
   - By severity: Critical _____, High _____, Medium _____, Low _____
   - By action: Blocked _____, Allowed (monitoring) _____
   - By channel: Email _____, Web _____, USB _____, etc.
4. Calculate alert backlog: Unreviewed alerts count
5. Identify trends: Plot alerts/day over 30 days, spot anomalies
6. Status determination (see Section 4.2)
7. Collect evidence: SIEM query screenshot, alert volume chart

**STEP 3: SIEM Integration Verification (1 hour)**
1. Navigate to SIEM_Integration sheet
2. Verify DLP log forwarding:
   - Check SIEM data source config (is DLP configured as log source?)
   - Check log volume: Are logs actually flowing? (check SIEM index stats)
   - Check log freshness: Most recent DLP event timestamp in SIEM
3. Test end-to-end:
   - Generate test DLP alert (send email with fake credit card number)
   - Search SIEM for test alert (should appear within minutes)
   - Verify alert details: All fields present? (user, channel, data type, action)
4. Review correlation rules:
   - How many SIEM rules reference DLP events?
   - Do rules work? (test or review recent triggers)
5. Check SOC dashboards:
   - Is there DLP-specific dashboard? (DLP alerts, trends, top users)
   - Are DLP alerts visible in main SOC dashboard?
6. Status determination (see Section 4.3)
7. Collect evidence: SIEM config screenshot, test alert search result

**STEP 4: SOC Playbook Review (1 hour)**
1. Navigate to SOC_Playbooks sheet
2. Review DLP incident playbook:
   - Does playbook exist? (documented procedure)
   - Is it accessible to SOC analysts? (wiki, SharePoint, ticketing system)
   - Is it up to date? (last reviewed date)
3. For each playbook step:
   - Alert triage (how to determine if alert is real)
   - Investigation (what to investigate, where to look)
   - Containment (how to stop ongoing data leak)
   - Escalation (when to escalate, to whom)
   - Evidence preservation (what logs to save)
   - User notification (inform user their action was blocked?)
4. Interview SOC analyst:
   - Have you handled DLP alert? Describe process.
   - What's hardest part of DLP alert triage?
   - What info do you need but don't have?
5. Check training:
   - Have SOC analysts been trained on DLP alerts?
   - Training date, materials, completion rate
6. Status determination (see Section 4.4)
7. Collect evidence: Playbook document, training records

**STEP 5: False Positive Tuning (1-2 hours)**
1. Navigate to False_Positive_Tuning sheet
2. Calculate FP rate:
   - Sample 100 recent alerts (random selection across channels and severities)
   - For each alert: Review details, classify as TP (true positive) or FP (false positive)
   - FP Rate = (FP count / 100) × 100
3. Analyze FP patterns:
   - Which DLP patterns cause most FPs? (credit card regex too broad?)
   - Which channels have highest FP rate? (email vs. web vs. USB)
   - Which users trigger most FPs? (developers testing, legitimate data use)
4. Review tuning process:
   - How are FPs reported? (user feedback, SOC escalation, DLP admin review)
   - How often are patterns updated? (weekly, monthly, quarterly, never)
   - Who approves pattern changes? (DLP admin, security team, change control)
   - Testing before deployment? (test new patterns on sample data before production)
5. Check user feedback:
   - Can users report FPs? (email, portal, ticketing)
   - How many FP reports last quarter?
   - How many acted upon?
6. Status determination (see Section 4.5)
7. Collect evidence: FP rate calculation spreadsheet, tuning history

**STEP 6: Incident Response Metrics (1 hour)**
1. Navigate to Incident_Response sheet
2. Calculate MTTR (Mean Time to Respond):
   - Identify last 10 DLP incidents (true positives requiring response)
   - For each: Alert timestamp, Containment timestamp, Duration
   - MTTR = Average duration
3. Review containment actions:
   - What was done to stop data leakage? (disable account, block USB, quarantine email)
   - Was containment effective? (did data leakage stop?)
   - How long did containment take?
4. Check evidence preservation:
   - Are DLP alerts archived? (retention period)
   - Are affected files quarantined? (email attachments, USB files)
   - Are logs preserved? (SIEM retention, DLP logs)
5. Assess notification compliance:
   - For personal data breaches: Was DPO notified?
   - Was breach reported to regulator within 72 hours? (GDPR requirement)
   - Were affected data subjects notified? (if required)
6. Status determination (see Section 4.6)
7. Collect evidence: MTTR calculation, incident reports

**STEP 7: Gap Analysis & Remediation (30 minutes)**
1. Navigate to Gap_Analysis sheet
2. Document gaps:
   - Example: "FP rate 45%, target <10%" → Risk: High → Action: "Implement quarterly pattern tuning, user feedback mechanism"
   - Example: "No SOC playbook for DLP" → Risk: Critical → Action: "Develop playbook, train SOC analysts"
3. Prioritize:
   - Critical: No monitoring, MTTR >24 hours, FP rate >50%
   - High: No SIEM integration, no playbook, FP rate 30-50%
   - Medium: Playbook outdated, FP rate 10-30%, MTTR 4-24 hours

**STEP 8: Evidence Register & Final Review (15 minutes)**
1. Document all evidence (minimum 2 per domain = 10 items)
2. Review Summary_Dashboard
3. Quality check (Section 7)

**STEP 9: Approval & Sign-Off (15 minutes)**
1. Complete Approval_Sign-Off sheet
2. Save with date

---

## 4. Sheet-by-Sheet Guidance

### 4.2 Sheet: Alert_Management

**Assessment Question:** *"Are DLP alerts actively monitored, triaged, and responded to in a timely manner?"*

**Understanding the Requirement:**

Alert management effectiveness determines whether DLP provides value or is just deployed security theater.

**Policy (ISMS-POL-A.8.12 Section 2.3):**
- 24/7 monitoring for Critical/High alerts
- Alert triage daily (review all alerts within 24 hours)
- MTTR targets: Critical <1 hour, High <4 hours, Medium <24 hours
- Alert backlog <100 unreviewed alerts

**Field Guidance:**

| Field | How to Complete | Examples | Where to Find |
|-------|-----------------|----------|---------------|
| **Total Alerts (30 days)** | Count | 1,500 alerts | SIEM or DLP console query |
| **Average Alerts/Day** | Total / 30 | 50 alerts/day | Calculated |
| **Critical Alerts** | Count by severity | 15 Critical | SIEM query filtered by severity |
| **High Alerts** | Count | 150 High | SIEM query |
| **Medium/Low Alerts** | Count | 1,335 Medium/Low | SIEM query |
| **Blocked Events** | Action = Block | 300 blocked | DLP logs |
| **Allowed (Monitoring)** | Action = Log Only | 1,200 monitored | DLP logs |
| **Alert Backlog** | Unreviewed count | 45 unreviewed | SOC ticket queue |
| **Oldest Unreviewed Alert** | Age in days | 7 days old | Ticket queue |
| **24/7 SOC Coverage** | Yes/No/Partial | Yes (Critical/High only) | SOC staffing |
| **Status** | ✅/⚠️/❌/N/A | Based on checklist | Determined |
| **Evidence ID** | Reference | A812-4-ALT-001 | Evidence register |

**Status Determination:**

**✅ Compliant:**
- All alerts reviewed within 24 hours (backlog <100, oldest <24 hours)
- 24/7 SOC coverage for Critical/High alerts
- Alert volume manageable (<100/day per analyst)
- Triage process documented and followed
- Escalation procedures defined and working
- MTTR meets targets (Critical <1 hour, High <4 hours)

**⚠️ Partial:**
- Alert backlog 100-500 (manageable but needs improvement)
- Business hours monitoring only (no 24/7 for Critical/High)
- Alert volume high but being handled (100-200/day per analyst)
- Triage process exists but not consistently followed
- MTTR exceeds targets (Critical 1-4 hours, High 4-12 hours)

**❌ Non-Compliant:**
- Alert backlog >500 or oldest alert >7 days (alerts not being reviewed)
- No active monitoring (alerts generated but ignored)
- Alert volume overwhelming (>200/day per analyst, alert fatigue)
- No triage process or escalation procedures
- MTTR >24 hours (slow response, data fully exfiltrated)

**Compliance Checklist:**

- [ ] **All DLP alerts reviewed within 24 hours** (backlog <100, oldest <24 hours)
- [ ] **24/7 SOC coverage for Critical/High severity alerts** (business hours insufficient)
- [ ] **Alert volume per analyst <100/day** (>100/day = alert fatigue risk)
- [ ] **Documented triage process** (how to review alert, classify, escalate)
- [ ] **Escalation procedures defined** (when to involve CISO, Legal, DPO, HR)
- [ ] **MTTR tracked and meets targets** (Critical <1 hour, High <4 hours, Medium <24 hours)

**Common Pitfalls:**

**Pitfall 1:** "Alerts generated but nobody reviews them"  
**Problem:** DLP deployed but no SOC integration or monitoring process  
**Solution:** Integrate with SOC, assign DLP alert review responsibility, implement daily triage

**Pitfall 2:** "Alert overload - 1000+ alerts/day, SOC overwhelmed"  
**Problem:** High false positive rate, overly broad DLP patterns  
**Solution:** Aggressive FP tuning, implement alert suppression for known FPs, increase SOC staffing

**Evidence Examples:**
- SIEM query showing alert volume: `EV-2-Alert-20260121-30-Day-Alert-Volume.png`
- Alert backlog screenshot: `EV-2-Alert-20260121-Backlog-Dashboard.png`
- SOC shift schedule showing 24/7 coverage: `EV-2-Alert-20260121-SOC-Schedule.pdf`

---

## 5. Evidence Collection

### 5.1 General Evidence Guidelines

**Evidence Naming Convention:**
```
EV-[Domain]-[Category]-[Date]-[Description].[ext]
```

**Domain Codes:**
- 2 = Alert Management
- 3 = SIEM Integration
- 4 = SOC Playbooks
- 5 = False Positive Tuning
- 6 = Incident Response

**Examples:**
- `EV-2-Alert-20260121-Alert-Volume-Trend.png`
- `EV-3-SIEM-20260121-DLP-Log-Source-Config.png`
- `EV-4-Playbook-20260121-DLP-Incident-Response-Procedure.pdf`
- `EV-5-Tuning-20260121-FP-Rate-Calculation.xlsx`
- `EV-6-IR-20260121-MTTR-Last-10-Incidents.xlsx`

**Storage:** `ISMS/Controls/A.8.12_DLP/Assessments/Monitoring_Response/Evidence/`  
**Retention:** 2-3 years  
**Sensitivity:** Confidential (may contain incident details)

### 5.2 Evidence Types by Domain

**2. Alert Management:**
- Alert volume chart (30-day trend)
- Alert backlog screenshot
- SOC staffing schedule (24/7 coverage verification)

**3. SIEM Integration:**
- SIEM data source configuration (DLP as log source)
- Test alert search result (end-to-end verification)
- Correlation rule list (rules using DLP events)

**4. SOC Playbooks:**
- DLP incident response playbook document
- SOC analyst training records
- Escalation procedure flowchart

**5. False Positive Tuning:**
- FP rate calculation spreadsheet (sample of 100 alerts)
- Pattern tuning history log
- User feedback mechanism documentation

**6. Incident Response:**
- MTTR calculation (last 10 incidents)
- Sample incident report (with PII redacted)
- Evidence preservation checklist

**Minimum Evidence:** 2 per domain × 5 domains = **10 items minimum**

---

## 6. Common Pitfalls and How to Avoid Them

### 6.1 "DLP alerts generated but SOC doesn't monitor them"

**Problem:** DLP deployed, alerts sent to separate console, SOC uses SIEM, alerts never seen

**Solution:**
1. Integrate DLP with SIEM (forward all DLP logs to SIEM)
2. Create SOC dashboard showing DLP alerts
3. Include DLP alerts in SOC daily triage process
4. Train SOC analysts on DLP alert handling

### 6.2 "Alert fatigue - too many alerts, SOC ignores all"

**Problem:** 1000+ alerts/day, 95% false positives, SOC stops reviewing

**Measurement:**
```
Alert Fatigue Risk = Alerts per Analyst per Day
Safe: <50/day
Warning: 50-100/day
Critical: >100/day (alert fatigue guaranteed)
```

**Solution:**
1. **Immediate:** Suppress known FPs (create exception rules)
2. **Short-term:** Aggressive pattern tuning (reduce FP rate to <10%)
3. **Medium-term:** Implement automated triage (SOAR playbooks)
4. **Long-term:** Increase SOC staffing or reduce DLP scope

### 6.3 "MTTR unknown - no metrics tracked"

**Problem:** Don't know how long response takes, can't improve

**Solution:**
1. Implement ticketing for all DLP incidents (use ServiceNow, Jira, etc.)
2. Track timestamps: Alert created, Analyst assigned, Investigation complete, Containment action taken
3. Calculate MTTR monthly: Average(Containment - Alert Created)
4. Set targets: Critical <1 hour, High <4 hours, Medium <24 hours
5. Review trends: Is MTTR improving or degrading?

### 6.4 "No SOC playbook - every analyst handles differently"

**Problem:** Inconsistent response, missed escalations, evidence not preserved

**Solution:**
1. Develop DLP incident playbook:
   - Triage: How to determine if alert is real
   - Investigation: What to check (user history, destination, data type)
   - Containment: How to stop leak (disable account, block destination)
   - Escalation: When to escalate (always for Restricted data)
   - Evidence: What logs to preserve
   - Notification: Who to inform (user, manager, CISO, DPO, Legal)
2. Train all SOC analysts on playbook
3. Review quarterly and update based on lessons learned

### 6.5 "False positive rate >50%, SOC doesn't trust DLP"

**Problem:** Most alerts are FPs, SOC assumes all alerts are FPs, misses real breaches

**Measurement:**
```
FP Rate = (False Positives / Total Alerts) × 100
Excellent: <5%
Good: 5-10%
Acceptable: 10-20%
Poor: 20-50%
Unacceptable: >50% (DLP ineffective)
```

**Solution:**
1. Calculate baseline FP rate (sample 100 alerts, classify each)
2. Identify top FP patterns (which patterns cause most FPs?)
3. Tune or disable worst patterns (disable patterns with >50% FP rate)
4. Implement user feedback (let users report FPs easily)
5. Quarterly tuning review (dedicated session to improve patterns)
6. Target: <10% FP rate within 6 months

### 6.6 "No incident response plan for data breach"

**Problem:** When real breach happens, chaotic response, evidence lost, notification missed

**Solution:**
1. Develop data breach incident response plan:
   - Detection & triage
   - Containment (stop ongoing leak)
   - Investigation (what data, who, where, how much)
   - Eradication (fix root cause, block vulnerability)
   - Evidence preservation (logs, files, screenshots)
   - Notification (GDPR 72 hours, affected individuals, regulators)
   - Recovery (restore normal operations)
   - Lessons learned (post-mortem, improve DLP)
2. Conduct tabletop exercise (simulate data breach, practice response)
3. Test notification process (can we notify within 72 hours?)
4. Review and update annually

---

## 7. Quality Checklist (Self-Review Before Submission)

**Completeness:**
- [ ] All 5 domains assessed (Alert Management, SIEM Integration, Playbooks, Tuning, Incident Response)
- [ ] Alert volume metrics calculated (30-day totals, averages, by severity)
- [ ] SIEM integration verified through testing (not assumptions)
- [ ] SOC playbooks reviewed (exist and are accessible)
- [ ] FP rate calculated from actual sample (not estimated)
- [ ] MTTR calculated from actual incidents (last 10)
- [ ] Gap Analysis complete for all ❌ and ⚠️ items
- [ ] Remediation plans created with owners and dates

**Accuracy:**
- [ ] Alert metrics from actual SIEM/DLP logs (not guessed)
- [ ] SIEM test performed (generated test alert, verified in SIEM)
- [ ] FP rate from manual review (100 alert sample classified)
- [ ] MTTR from ticket timestamps (not policy targets)
- [ ] SOC analyst interviewed (not just documentation review)

**Evidence Quality:**
- [ ] Minimum 2 evidence items per domain (10+ total)
- [ ] SIEM queries documented (reproducible)
- [ ] Screenshots include timestamps
- [ ] Incident details sanitized (PII removed)

**Policy Alignment:**
- [ ] 24/7 monitoring verified (or gap documented)
- [ ] MTTR targets compared to policy requirements
- [ ] FP rate target (<10%) assessed
- [ ] Alert backlog target (<100) checked

**Operational Verification:**
- [ ] SOC actually monitors DLP (not just configured)
- [ ] Playbooks actually used (not just documented)
- [ ] Tuning actually happens (not just process exists)
- [ ] Incidents actually responded to (not just escalated and forgotten)

**Final Checks:**
- [ ] Filename: `ISMS-IMP-A.8.12.4_Monitoring_Response_20260121.xlsx`
- [ ] All formulas calculate correctly
- [ ] Conditional formatting working

---

## 8. Review & Approval Process

### 8.1 Assessment Metadata

**Assessment Period:** _______  
**Assessment Date:** _______  
**Assessment Type:**
- [ ] Initial Assessment
- [ ] Quarterly Review
- [ ] Post-Incident Review
- [ ] Post-Tuning Review

### 8.2 Completed By

**Name:** _______________________  
**Role:** _______________________ (SOC Manager, DLP Administrator)  
**Email:** _______________________  
**Date:** _______________________  
**Signature:** _______________________

**Declaration:**
I confirm:
- Alert metrics from actual data (not estimated)
- SIEM integration tested (not assumed)
- FP rate from manual sample review
- MTTR from actual incident timestamps
- SOC analysts interviewed for realistic assessment

### 8.3 Reviewed By (Security Operations Manager)

**Name:** _______________________  
**Date:** _______________________  
**Outcome:**
- [ ] Approved
- [ ] Approved with corrections
- [ ] Requires revision

### 8.4 Approved By (CISO)

**Name:** _______________________  
**Date:** _______________________  

**Decision:**
- [ ] Approved - Monitoring adequate
- [ ] Approved with conditions - Remediate by: _______
- [ ] Rejected - Critical gaps require immediate action

**Risk Acceptance:**
- [ ] Residual risk accepted
- [ ] Remediation required
- [ ] Escalate to Executive Management

### 8.5 Next Review Date

**Next Assessment:** _______________________

**Review Cycle:** Quarterly or upon:
- Major DLP tuning changes
- SOC process changes
- Data breach incidents
- MTTR target misses
- Alert volume anomalies

---

**END OF PART I: USER COMPLETION GUIDE**

---

# PART II: TECHNICAL SPECIFICATION
**Audience:** Python Developers, Excel Workbook Developers, Quality Assurance, ISMS Implementation Team

---

## 1. Workbook Structure Overview

### 1.1 Sheet List

**Total Sheets:** 9

| # | Sheet Name | Rows (approx) | Purpose | User Input |
|---|------------|---------------|---------|------------|
| 1 | Instructions_Legend | 45 | User guidance, metadata | Metadata only |
| 2 | Alert_Management | 30 | Alert volume, triage, backlog | Yes (metrics) |
| 3 | SIEM_Integration | 20 | Log forwarding, correlation | Yes (integration status) |
| 4 | SOC_Playbooks | 25 | Procedures, training, escalation | Yes (playbook review) |
| 5 | False_Positive_Tuning | 30 | FP rate, tuning process | Yes (FP analysis) |
| 6 | Incident_Response | 25 | MTTR, containment, notification | Yes (IR metrics) |
| 7 | Gap_Analysis | 40 | Gaps and remediation | Yes (gap details) |
| 8 | Evidence_Register | 100 | Evidence tracking | Yes (evidence) |
| 9 | Summary_Dashboard | 40 | KPIs, MTTR trends, alert charts | No (formulas) |

**Total Assessment Items:** ~55 monitoring effectiveness checkpoints

---

## 2. Detailed Sheet Specifications

### 2.1 Sheet: Instructions_Legend

**Purpose:** User guidance, assessment metadata

**Layout:**
- Rows 1-5: Header
- Rows 7-12: Organization metadata (yellow cells)
- Rows 14-30: Instructions
- Rows 32-40: Response value legend
- Rows 42-45: Color coding

---

### 2.2 Sheet: Alert_Management

**Purpose:** Assess alert volume, triage effectiveness, backlog management

**Column Structure:**

| Col | Header | Type | Width | Validation | Notes |
|-----|--------|------|-------|------------|-------|
| A | Metric | Text | 30 | None | Pre-populated metric names |
| B | Value | Number/Text | 20 | Various | User input |
| C | Target | Text | 20 | None | Policy target |
| D | Status | Dropdown | 12 | ✅/⚠️/❌ | Auto or manual |
| E | Notes | Text (wrap) | 40 | None | Additional context |
| F | Evidence ID | Text | 15 | None | A812-4-ALT-001 |

**Pre-Populated Metrics (Rows 6-30):**

| Metric | Target | Description |
|--------|--------|-------------|
| Assessment Period (Days) | 30 | Period analyzed |
| Total DLP Alerts | - | Count all alerts |
| Average Alerts/Day | <100 per analyst | Total / Days |
| Critical Alerts | - | Severity = Critical |
| High Alerts | - | Severity = High |
| Medium Alerts | - | Severity = Medium |
| Low Alerts | - | Severity = Low |
| Blocked Events | - | Action = Block |
| Allowed (Monitoring Only) | - | Action = Log Only |
| Alert Backlog (Unreviewed) | <100 | Current count |
| Oldest Unreviewed Alert (Days) | <1 day | Age of oldest |
| 24/7 SOC Coverage | Yes | For Critical/High |
| Alert Review SLA Met (%) | ≥95% | Within 24 hours |
| Escalation Rate (%) | 5-10% | Alerts escalated |
| MTTR - Critical (Hours) | <1 | Critical alerts |
| MTTR - High (Hours) | <4 | High alerts |
| MTTR - Medium (Hours) | <24 | Medium alerts |
| False Positive Rate (%) | <10% | See Tuning sheet |
| SOC Analysts (FTE) | - | Staffing count |
| Alerts per Analyst per Day | <100 | Workload metric |
| Triage Process Documented | Yes | Playbook exists |
| Escalation Procedures Defined | Yes | Who, when, how |
| Alert Fatigue Risk | Low/Medium/High | Based on volume |
| Overall Status | ✅/⚠️/❌ | Compliance status |

**Data Validation:**

```python
# Column B: Various types based on metric
# Numbers for counts, percentages
# Yes/No for binary metrics
# Risk levels for assessment metrics

# Column D: Status
validation_status = {
    'type': 'list',
    'formula1': '"✅ Compliant,⚠️ Partial,❌ Non-Compliant,N/A"',
    'allow_blank': False
}
```

**Conditional Formatting:**

```python
# Alerts per Analyst per Day (Row 25)
# <50 = Green, 50-100 = Yellow, >100 = Red
alerts_per_analyst_format = {
    'green': ('<=', 50),
    'yellow': ('and', [('>', 50), ('<=', 100)]),
    'red': ('>', 100)
}

# Alert Backlog (Row 15)
# <100 = Green, 100-500 = Yellow, >500 = Red
backlog_format = {
    'green': ('<', 100),
    'yellow': ('and', [('>=', 100), ('<=', 500)]),
    'red': ('>', 500)
}

# MTTR - Critical (Row 20)
# <1 = Green, 1-4 = Yellow, >4 = Red
mttr_critical_format = {
    'green': ('<', 1),
    'yellow': ('and', [('>=', 1), ('<=', 4)]),
    'red': ('>', 4)
}
```

---

### 2.3 Sheet: SIEM_Integration

**Purpose:** Verify DLP log forwarding and SIEM correlation

**Column Structure:**

| Col | Header | Type | Width | Validation | Notes |
|-----|--------|------|-------|------------|-------|
| A | Integration Component | Text | 30 | None | Pre-populated |
| B | Implementation Status | Dropdown | 22 | Deployed/Partial/None | Current state |
| C | Details | Text (wrap) | 35 | None | Configuration details |
| D | Tested | Dropdown | 12 | Yes/No | Verification done? |
| E | Test Result | Dropdown | 15 | Pass/Fail/Partial | Test outcome |
| F | Status | Dropdown | 12 | ✅/⚠️/❌/N/A | Compliance |
| G | Evidence ID | Text | 15 | None | A812-4-SIE-001 |

**Pre-Populated Components (Rows 6-20):**

| Component | Description | Test Method |
|-----------|-------------|-------------|
| DLP Log Source Configured | DLP added as SIEM data source | Check SIEM config |
| Log Forwarding Active | Logs actually flowing to SIEM | Check SIEM index stats |
| Log Volume Adequate | All DLP events forwarded (not sampling) | Compare DLP console vs. SIEM counts |
| Log Freshness | Most recent event <5 minutes old | Check SIEM latest timestamp |
| All Event Types Forwarded | Block, Allow, Encrypt events all present | Search for each event type |
| Event Fields Complete | User, channel, data type, action all populated | Review sample events |
| Correlation Rules Deployed | SIEM rules using DLP events | List correlation rules |
| Correlation Rules Tested | Rules actually trigger on DLP events | Test or review recent triggers |
| DLP Dashboard Created | SOC dashboard showing DLP metrics | Screenshot dashboard |
| Dashboard Accessible to SOC | Analysts can view dashboard | Verify permissions |
| Alerts Auto-Generated | Critical/High DLP events create SIEM alerts | Test alert generation |
| Alerts Routed to SOC Queue | DLP alerts appear in SOC ticketing system | Verify ticket creation |
| Search Performance Adequate | DLP event queries <10 seconds | Test common searches |
| Log Retention Meets Policy | DLP logs retained per policy (e.g., 1 year) | Check retention settings |
| End-to-End Test Passed | Generate test DLP alert, verify in SIEM + ticket | Full integration test |

**Data Rows:** 20 total (15 pre-populated + 5 blank)

**Data Validation:**

```python
# Column B: Implementation Status
validation_status = {
    'type': 'list',
    'formula1': '"Fully Deployed,Partially Deployed,Not Deployed,Planned"',
    'allow_blank': False
}

# Column D: Tested
validation_tested = {
    'type': 'list',
    'formula1': '"Yes,No,In Progress"',
    'allow_blank': False
}

# Column E: Test Result
validation_result = {
    'type': 'list',
    'formula1': '"Pass,Fail,Partial,Not Tested"',
    'allow_blank': False
}

# Column F: Status
validation_compliance = {
    'type': 'list',
    'formula1': '"✅ Compliant,⚠️ Partial,❌ Non-Compliant,N/A"',
    'allow_blank': False
}
```

**Conditional Formatting:**
- Column E (Test Result):
  - "Pass" = Green
  - "Partial" = Yellow
  - "Fail" = Red

---

### 2.4 Sheet: SOC_Playbooks

**Purpose:** Assess incident response procedures and SOC training

**Column Structure:**

| Col | Header | Type | Width | Validation | Notes |
|-----|--------|------|-------|------------|-------|
| A | Playbook Element | Text | 35 | None | Pre-populated |
| B | Documented | Dropdown | 15 | Yes/No/Partial | Procedure exists? |
| C | Location | Text | 30 | None | Where documented |
| D | Last Updated | Date | 15 | None | DD.MM.YYYY |
| E | SOC Trained | Dropdown | 15 | Yes/No/Partial | Training completed? |
| F | Training Date | Date | 15 | None | DD.MM.YYYY |
| G | Accessible | Dropdown | 15 | Yes/No | SOC can access? |
| H | Status | Dropdown | 12 | ✅/⚠️/❌/N/A | Compliance |
| I | Evidence ID | Text | 15 | None | A812-4-PLY-001 |

**Pre-Populated Playbook Elements (Rows 6-25):**

| Element | Description | Importance |
|---------|-------------|------------|
| DLP Incident Response Playbook | Overall procedure for handling DLP incidents | Critical |
| Alert Triage Procedure | How to determine if alert is real (TP vs FP) | Critical |
| Investigation Steps | What to investigate (user history, data accessed, destination) | High |
| Containment Actions | How to stop ongoing data leak (disable account, block destination) | Critical |
| Escalation Criteria | When to escalate (always for Restricted data) | Critical |
| Escalation Contacts | Who to contact (CISO, Legal, DPO, HR) | High |
| Evidence Preservation | What logs/files to preserve | High |
| User Notification | When/how to inform user | Medium |
| Manager Notification | When to inform user's manager | Medium |
| Legal Notification | When to involve Legal team | High |
| DPO Notification | Personal data breach → notify DPO immediately | Critical |
| Regulatory Notification | GDPR 72-hour breach notification process | Critical |
| Data Subject Notification | When to notify affected individuals | High |
| Post-Incident Review | Lessons learned after incident | Medium |
| Playbook Review Schedule | How often playbook updated (quarterly) | Medium |
| SOC Training Plan | DLP alert handling training program | High |
| Training Completion Rate | % of SOC analysts trained | High |
| Tabletop Exercise | Incident simulation for practice | Medium |
| Escalation Path Flowchart | Visual diagram of escalation | Medium |
| Contact List Current | Escalation contacts verified current | Medium |

**Data Rows:** 25 total (20 pre-populated + 5 blank)

**Data Validation:**

```python
# Column B, E, G: Yes/No/Partial
validation_ynp = {
    'type': 'list',
    'formula1': '"Yes,No,Partial,N/A"',
    'allow_blank': False
}

# Column D, F: Date validation
validation_date = {
    'type': 'date',
    'formula1': '01.01.2020',
    'formula2': '31.12.2030',
    'allow_blank': True
}

# Column H: Status
validation_status = {
    'type': 'list',
    'formula1': '"✅ Compliant,⚠️ Partial,❌ Non-Compliant,N/A"',
    'allow_blank': False
}
```

**Conditional Formatting:**
- Column D (Last Updated):
  - <90 days old = Green
  - 90-365 days = Yellow
  - >365 days = Red (playbook outdated)

---

### 2.5 Sheet: False_Positive_Tuning

**Purpose:** Assess FP rate and tuning effectiveness

**Column Structure:**

| Col | Header | Type | Width | Validation | Notes |
|-----|--------|------|-------|------------|-------|
| A | Tuning Metric | Text | 30 | None | Pre-populated |
| B | Value | Number/Text | 20 | Various | User input |
| C | Target | Text | 20 | None | Policy target |
| D | Status | Dropdown | 12 | ✅/⚠️/❌ | Compliance |
| E | Notes | Text (wrap) | 40 | None | Additional context |
| F | Evidence ID | Text | 15 | None | A812-4-TUN-001 |

**Pre-Populated Metrics (Rows 6-30):**

| Metric | Target | Description |
|--------|--------|-------------|
| FP Rate Calculation Method | Manual Sample | How FP rate measured |
| Sample Size | 100 alerts | Alerts reviewed |
| Sample Period | Last 30 days | When sampled |
| True Positives | - | Real sensitive data leaks |
| False Positives | - | Non-sensitive flagged as sensitive |
| False Positive Rate (%) | <10% | (FP / Total) × 100 |
| FP Rate by Channel - Email (%) | <10% | Email-specific FP rate |
| FP Rate by Channel - Web (%) | <10% | Web-specific FP rate |
| FP Rate by Channel - Endpoint (%) | <10% | USB/endpoint FP rate |
| Top FP Pattern #1 | - | Pattern causing most FPs |
| Top FP Pattern #2 | - | Second highest FP pattern |
| Top FP Pattern #3 | - | Third highest FP pattern |
| Tuning Frequency | Quarterly | How often patterns updated |
| Last Tuning Date | - | Most recent tuning |
| Patterns Updated (Last Quarter) | >5 | Number of patterns modified |
| User Feedback Mechanism | Yes | Users can report FPs |
| FP Reports Received (Last Quarter) | - | User reports count |
| FP Reports Acted Upon (%) | >80% | % of reports resulting in tuning |
| Pattern Testing Before Deployment | Yes | Test on sample data before production |
| Tuning Approval Process | Yes | Change control for patterns |
| Tuning Owner | - | Who responsible for tuning |
| False Negative Rate (%) | <5% | Real leaks DLP missed (if measurable) |
| Pattern Accuracy Target | >90% | Overall detection accuracy |
| Alert Suppression Rules | - | Count of FP suppression rules |
| Overall Tuning Status | ✅/⚠️/❌ | Compliance status |

**Data Validation:**

```python
# Column B: Various (numbers, percentages, text)
# Percentages use standard 0-100 validation

validation_percentage = {
    'type': 'whole',
    'formula1': '0',
    'formula2': '100',
    'allow_blank': True,
    'operator': 'between'
}

# Column D: Status
validation_status = {
    'type': 'list',
    'formula1': '"✅ Compliant,⚠️ Partial,❌ Non-Compliant,N/A"',
    'allow_blank': False
}
```

**Conditional Formatting:**

```python
# FP Rate (Row 11)
fp_rate_format = {
    'green': ('<', 10),    # Excellent
    'yellow': ('and', [('>=', 10), ('<', 20)]),  # Acceptable
    'red': ('>=', 20)      # Poor
}

# FP Reports Acted Upon % (Row 23)
action_rate_format = {
    'green': ('>=', 80),   # Good responsiveness
    'yellow': ('and', [('>=', 60), ('<', 80)]),
    'red': ('<', 60)       # Poor responsiveness
}
```

---

### 2.6 Sheet: Incident_Response

**Purpose:** Assess incident response metrics and breach notification compliance

**Column Structure:**

| Col | Header | Type | Width | Validation | Notes |
|-----|--------|------|-------|------------|-------|
| A | IR Metric | Text | 30 | None | Pre-populated |
| B | Value | Number/Text | 20 | Various | User input |
| C | Target | Text | 20 | None | Policy target |
| D | Status | Dropdown | 12 | ✅/⚠️/❌ | Compliance |
| E | Notes | Text (wrap) | 40 | None | Additional context |
| F | Evidence ID | Text | 15 | None | A812-4-INC-001 |

**Pre-Populated Metrics (Rows 6-25):**

| Metric | Target | Description |
|--------|--------|-------------|
| Incidents Analyzed (Period) | Last 90 days | Period for MTTR calculation |
| Total DLP Incidents (True Positives) | - | Count of real data leakage events |
| Critical Incidents | - | Restricted data leakage |
| High Incidents | - | Confidential data leakage |
| Medium Incidents | - | Internal data leakage |
| MTTR - Critical (Hours) | <1 | Alert → Containment time |
| MTTR - High (Hours) | <4 | Alert → Containment time |
| MTTR - Medium (Hours) | <24 | Alert → Containment time |
| MTTR - Overall Average (Hours) | - | Weighted average |
| Fastest Response (Hours) | - | Best case |
| Slowest Response (Hours) | - | Worst case |
| Containment Actions Documented | Yes | Actions logged in tickets |
| Containment Effectiveness (%) | 100% | Did containment stop leak? |
| Evidence Preserved (%) | 100% | Logs/files saved |
| DPO Notified (Personal Data Breaches) | 100% | For GDPR compliance |
| Breach Reported Within 72 Hours (%) | 100% | GDPR requirement |
| Data Subjects Notified (When Required) | 100% | GDPR Article 34 |
| Post-Incident Reviews Conducted | 100% | Lessons learned |
| Repeat Incidents (Same User/Pattern) | <5% | Learning from incidents |
| DLP Log Retention (Days) | 365+ | For investigation |
| Incident Report Template | Yes | Standardized reporting |
| Overall IR Status | ✅/⚠️/❌ | Compliance status |

**Data Validation:**

```python
# Column B: Various (numbers, hours, percentages)

validation_hours = {
    'type': 'decimal',
    'formula1': '0',
    'formula2': '72',
    'allow_blank': True,
    'operator': 'between'
}

validation_percentage = {
    'type': 'whole',
    'formula1': '0',
    'formula2': '100',
    'allow_blank': True,
    'operator': 'between'
}

# Column D: Status
validation_status = {
    'type': 'list',
    'formula1': '"✅ Compliant,⚠️ Partial,❌ Non-Compliant,N/A"',
    'allow_blank': False
}
```

**Conditional Formatting:**

```python
# MTTR - Critical (Row 11)
mttr_critical_format = {
    'green': ('<=', 1),    # Meets target
    'yellow': ('and', [('>', 1), ('<=', 4)]),
    'red': ('>', 4)        # Unacceptable delay
}

# Breach Reported Within 72 Hours % (Row 21)
notification_format = {
    'green': ('=', 100),   # Perfect compliance
    'yellow': ('and', [('>=', 80), ('<', 100)]),
    'red': ('<', 80)       # Regulatory violation risk
}
```

---

### 2.7 Sheet: Gap_Analysis

**Purpose:** Document monitoring/response gaps and remediation plans

*(Same structure as previous IMP documents)*

**Column Structure:**

| Col | Header | Type | Width | Notes |
|-----|--------|------|-------|-------|
| A | Gap ID | Text | 12 | Auto: GAP-001 |
| B | Domain | Dropdown | 22 | Which assessment area |
| C | Gap Description | Text (wrap) | 40 | What's missing |
| D | Current State | Text (wrap) | 25 | Now |
| E | Required State | Text (wrap) | 25 | Target |
| F | Risk Level | Dropdown | 15 | Critical/High/Medium/Low |
| G | Regulatory Impact | Text | 25 | GDPR 72-hour, etc. |
| H | Remediation Action | Text (wrap) | 35 | What to do |
| I | Owner | Text | 20 | Who |
| J | Target Date | Date | 15 | When |
| K | Status | Dropdown | 15 | Open/In Progress/Resolved |
| L | Evidence ID | Text | 15 | A812-4-GAP-001 |

**Data Rows:** 40 total

**Domain Validation:**

```python
validation_domain = {
    'type': 'list',
    'formula1': '"Alert Management,SIEM Integration,SOC Playbooks,False Positive Tuning,Incident Response,General"',
    'allow_blank': False
}
```

---

### 2.8 Sheet: Evidence_Register

*(Same structure as previous IMP documents)*

**Data Rows:** 100 total

---

### 2.9 Sheet: Summary_Dashboard

**Purpose:** Executive summary with MTTR trends and alert volume charts

**Layout:**

**Rows 1-5:** Header

**Rows 7-18: Key Metrics**

| Metric | Formula | Target |
|--------|---------|--------|
| Overall Monitoring Effectiveness (%) | Weighted average across domains | ≥85% |
| Alert Backlog | From Alert_Management sheet | <100 |
| Average Alerts/Day | From Alert_Management | <100 per analyst |
| False Positive Rate (%) | From Tuning sheet | <10% |
| MTTR - Critical (Hours) | From IR sheet | <1 |
| MTTR - High (Hours) | From IR sheet | <4 |
| SOC Coverage | 24/7 for Critical/High | Yes |
| SIEM Integration Status | From SIEM sheet | Fully Deployed |
| Playbooks Documented | From Playbooks sheet | Yes |
| GDPR 72-Hour Compliance (%) | From IR sheet | 100% |
| Critical Gaps | From Gap_Analysis | 0 |

**Rows 20-30: Domain Compliance**

| Domain | Compliance % | Status | Target |
|--------|--------------|--------|--------|
| Alert Management | Formula | ✅/⚠️/❌ | ≥85% |
| SIEM Integration | Formula | ✅/⚠️/❌ | 100% |
| SOC Playbooks | Formula | ✅/⚠️/❌ | 100% |
| False Positive Tuning | Formula | ✅/⚠️/❌ | ≥90% |
| Incident Response | Formula | ✅/⚠️/❌ | ≥90% |

**Rows 32-40: Trend Charts (Descriptions)**
- Alert volume trend (last 30 days)
- MTTR trend (last 90 days)
- FP rate trend (last 6 months)

**Key Formulas:**

```python
# Overall Monitoring Effectiveness %
=ROUND(
  (COUNTIF(Alert_Management!D:D,"✅ Compliant") / COUNTA(Alert_Management!D6:D30) * 20) +
  (COUNTIF(SIEM_Integration!F:F,"✅ Compliant") / COUNTA(SIEM_Integration!F6:F20) * 20) +
  (COUNTIF(SOC_Playbooks!H:H,"✅ Compliant") / COUNTA(SOC_Playbooks!H6:H25) * 25) +
  (COUNTIF(False_Positive_Tuning!D:D,"✅ Compliant") / COUNTA(False_Positive_Tuning!D6:D30) * 20) +
  (COUNTIF(Incident_Response!D:D,"✅ Compliant") / COUNTA(Incident_Response!D6:D25) * 15),
  0
)

# Alert Backlog (reference from Alert_Management)
=Alert_Management!B15  # Row 15 = Alert Backlog metric

# MTTR - Critical (reference from Incident_Response)
=Incident_Response!B11  # Row 11 = MTTR Critical metric

# False Positive Rate (reference from Tuning)
=False_Positive_Tuning!B11  # Row 11 = FP Rate %

# GDPR 72-Hour Compliance %
=Incident_Response!B21  # Row 21 = Breach notification compliance

# Critical Gaps
=COUNTIF(Gap_Analysis!F6:F45,"Critical")
```

**Conditional Formatting:**
- Overall Effectiveness:
  - ≥90% = Dark green
  - 85-89% = Light green
  - 75-84% = Yellow
  - <75% = Red
- MTTR:
  - Critical <1 hour = Green
  - Critical 1-4 hours = Yellow
  - Critical >4 hours = Red
- FP Rate:
  - <10% = Green
  - 10-20% = Yellow
  - >20% = Red

---

## 3-7. [Same as Previous IMP Documents]

*Data Validation Rules, Conditional Formatting, Cell Protection, Summary Formulas, Evidence Auto-Numbering sections follow same patterns as previous IMP documents.*

---

## APPENDIX: Technical Notes

### A.1 Python Script Integration

**Script:** `generate_a812_4_monitoring_response_assessment.py`

**Key Customization Points:**
- Pre-populated metric rows with targets
- MTTR calculation logic
- FP rate calculation methodology
- Dashboard formulas referencing specific rows

### A.2 Quality Assurance

**Validation Script:** `excel_sanity_check_a812_4.py`

**Critical Checks:**
- All metric targets present
- MTTR formulas reference correct rows
- FP rate calculation methodology documented
- Dashboard formulas calculate correctly
- No missing domain coverage

### A.3 Deployment

```bash
python3 generate_a812_4_monitoring_response_assessment.py
# Output: ISMS-IMP-A.8.12.4_Monitoring_Response_YYYYMMDD.xlsx

python3 excel_sanity_check_a812_4.py ISMS-IMP-A.8.12.4_Monitoring_Response_20260121.xlsx
```

---

**END OF PART II: TECHNICAL SPECIFICATION**

**Status:** Complete  
**Next Action:** Implement Python generator per specification

