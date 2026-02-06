**ISMS-IMP-A.8.16.4-TG - Alert Management & Response Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.16: Monitoring Activities

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.16.4-TG |
| **Version** | 1.0 |
| **Assessment Area** | Alert Management, Response Procedures, Investigation Workflows |
| **Related Policy** | ISMS-POL-A.8.16, Section 2.3 (Alert Management & Response Requirements) |
| **Purpose** | Assess effectiveness of alert handling, response procedures, investigation workflows, and closure processes |
| **Target Audience** | SOC Analysts, Incident Responders, Security Operations Management, Compliance Officers |
| **Assessment Type** | Operational Effectiveness & Process Assessment |
| **Review Cycle** | Quarterly or After Major Process Changes |
| **Date** | 22.01.2026 |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Original] | Initial technical specification | ISMS Implementation Team |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.8.16.4-UG.

---

# Technical Specification

# ISMS-IMP-A.8.16.4 - Alert Management & Response Assessment
# Excel Workbook Layout Specification
## ISO/IEC 27001:2022 Control A.8.16: Monitoring Activities

---

# Document Overview

**Document ID:** ISMS-IMP-A.8.16.4-TG  
**Assessment Area:** Alert Management, Triage, Investigation, Response  
**Related Policy:** ISMS-POL-A.8.16-S2.3  
**Purpose:** Assess alert management processes, response procedures, and SOC operational effectiveness  
**Generator Script:** `generate_a816_4_alert_management.py`  
**Output Filename:** `ISMS-IMP-A.8.16.4_Alert_Management_YYYYMMDD.xlsx`

---

# Workbook Structure

**Total Sheets:** 9
1. Instructions & Legend
2. 1. Alert Generation & Classification
3. 2. Triage & Investigation Processes
4. 3. Escalation & Response Procedures
5. 4. Alert Performance Metrics
6. 5. SOC Operational Readiness
7. Summary Dashboard
8. Evidence Register
9. Approval Sign-Off

---

# Sheet 2: 1. Alert Generation & Classification

## Header
**Title:** "1. ALERT GENERATION & CLASSIFICATION ASSESSMENT"  
**Policy Reference:** "Assess alert generation per ISMS-POL-A.8.16-S2.3.3"

## Column Headers - 22 Columns (A-V)

| Col | Header | Width | Type | Validation |
|-----|--------|-------|------|------------|
| A | Alert Type/Name | 30 | Text | Free text |
| B | Alert Source | 22 | Dropdown | SIEM, IDS/IPS, EDR, NDR, Firewall, WAF, AV, DLP, Cloud Security, Other |
| C | Detection Rule ID | 20 | Text | Free text |
| D | Alert Severity | 15 | Dropdown | Critical (P1), High (P2), Medium (P3), Low (P4) |
| E | MITRE ATT&CK Technique | 22 | Text | Free text |
| F | Alert Description | 35 | Text | Free text |
| G | Trigger Criteria | 30 | Text | Free text |
| H | Enrichment Data | 30 | Text | Free text (threat intel, asset, user) |
| I | Expected FP Rate | 15 | Text | % |
| J | Actual FP Rate (30d) | 15 | Text | % |
| K | Alert Volume (30d) | 15 | Text | Count |
| L | True Positives (30d) | 15 | Text | Count |
| M | Response Playbook | 22 | Text | Free text (playbook reference) |
| N | SLA Timeframe | 18 | Dropdown | <15 min, <1 hr, <4 hrs, <1 day, <3 days |
| O | Auto-Enrichment | 16 | Dropdown | Yes, Partial, No |
| P | Auto-Containment | 16 | Dropdown | Yes, No, N/A |
| Q | Deduplication Enabled | 18 | Dropdown | Yes, No |
| R | Alert Status | 16 | Dropdown | Active, Testing, Tuning Needed, Retired |
| S | Last Tuned | 14 | Text | DD.MM.YYYY |
| T | Compliance Status | 18 | Dropdown | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A |
| U | Issues/Gaps | 30 | Text | Free text |
| V | Tuning Priority | 16 | Dropdown | Critical, High, Medium, Low, None |

## Compliance Checklist
1. All alert types documented in inventory
2. Alert severity classification defined and consistent
3. MITRE ATT&CK mapping documented
4. Trigger criteria clearly documented
5. Alert enrichment configured (asset, user, threat intel)
6. Response playbook exists for each alert type
7. SLA timeframes defined per severity
8. False positive rates tracked (<25% overall, <10% critical)
9. High FP alerts tuned within 30 days
10. Alert deduplication configured
11. Auto-containment configured for high-confidence alerts
12. Alert generation tested before production
13. Alert volume monitored for spikes
14. Noisy alerts identified and tuned
15. Retired alerts properly archived

---

# Sheet 3: 2. Triage & Investigation Processes

## Header
**Title:** "2. TRIAGE & INVESTIGATION PROCESS ASSESSMENT"  
**Policy Reference:** "Assess triage per ISMS-POL-A.8.16-S2.3.5"

## Column Headers - 21 Columns (A-U)

| Col | Header | Width | Type |
|-----|--------|-------|------|
| A | Process Step | 28 | Dropdown | Alert Acknowledgment, Initial Assessment, Context Gathering, Disposition Decision, Investigation, Documentation, Escalation, Closure |
| B | Process Owner | 20 | Text |
| C | Procedure Documented | 18 | Dropdown | Yes, No, Partial |
| D | Documentation Location | 25 | Text |
| E | Training Provided | 16 | Dropdown | Yes, No, Planned |
| F | Tools/Systems Used | 25 | Text |
| G | Automation Level | 18 | Dropdown | Fully Automated, Partially Automated, Manual |
| H | Average Time (Minutes) | 18 | Text |
| I | SLA Target (Minutes) | 18 | Text |
| J | SLA Compliance % | 16 | Text |
| K | Bottlenecks Identified | 30 | Text |
| L | Quality Metrics | 25 | Text |
| M | Error Rate % | 12 | Text |
| N | Analyst Workload | 18 | Text | (alerts/shift) |
| O | Shift Coverage | 18 | Dropdown | 24/7, Business Hours, On-Call |
| P | Escalation Criteria | 30 | Text |
| Q | Escalation Rate % | 15 | Text |
| R | Process Status | 16 | Dropdown | ✅ Defined, ⚠️ Partial, ❌ Undefined |
| S | Last Process Review | 14 | Text | DD.MM.YYYY |
| T | Improvement Opportunities | 30 | Text |
| U | Priority | 16 | Dropdown | Critical, High, Medium, Low |

## Compliance Checklist
1. Triage procedure documented
2. Triage steps clearly defined
3. Disposition criteria documented (TP/FP/Benign/Investigation)
4. Triage timeframes defined per severity
5. SOC analysts trained on triage procedures
6. Triage tools accessible to all analysts
7. Context enrichment automated where possible
8. Common false positive scenarios documented
9. Investigation playbooks exist
10. Evidence collection guidance provided
11. Documentation requirements defined
12. Escalation criteria clearly defined
13. Escalation paths documented
14. Process reviewed quarterly
15. Continuous improvement implemented

---

# Sheet 4: 3. Escalation & Response Procedures

## Header
**Title:** "3. ESCALATION & RESPONSE PROCEDURES"  
**Policy Reference:** "Assess escalation per ISMS-POL-A.8.16-S2.3.7"

## Column Headers - 19 Columns (A-S)

| Col | Header | Width | Type |
|-----|--------|-------|------|
| A | Escalation Scenario | 30 | Text |
| B | Trigger Criteria | 30 | Text |
| C | Escalation Level | 20 | Dropdown | Tier 1→Tier 2, Tier 2→Tier 3, SOC→IR, IR→CISO, CISO→Exec, Exec→Board, External |
| D | Target Person/Team | 22 | Text |
| E | Primary Contact | 22 | Text |
| F | Backup Contact | 22 | Text |
| G | Contact Method | 18 | Dropdown | Phone, Email, Ticketing System, Secure Chat, Multiple |
| H | Escalation Timeframe | 16 | Text | e.g., "Within 15 min" |
| I | Information to Provide | 35 | Text |
| J | Expected Response Time | 18 | Text |
| K | Procedure Documented | 18 | Dropdown | Yes, No, Partial |
| L | Tested Frequency | 18 | Dropdown | Quarterly, Semi-Annually, Annually, Never |
| M | Last Tested | 14 | Text | DD.MM.YYYY |
| N | Test Result | 16 | Dropdown | Successful, Issues Found, Not Tested |
| O | After-Hours Procedure | 20 | Dropdown | On-Call, 24/7 SOC, Automated, None |
| P | Escalation Rate (30d) | 16 | Text | % or count |
| Q | Compliance Status | 18 | Dropdown | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A |
| R | Gaps/Issues | 30 | Text |
| S | Priority | 16 | Dropdown | Critical, High, Medium, Low |

## Compliance Checklist
1. Escalation paths documented for all severity levels
2. Escalation criteria clearly defined
3. Contact information current (verified quarterly)
4. Backup contacts identified
5. After-hours escalation procedures defined
6. On-call rotation established
7. Escalation timeframes defined
8. Information requirements documented (what to escalate)
9. Communication templates available
10. Escalation tracking in place
11. Escalation procedures tested (tabletop exercises)
12. External escalation procedures defined (law enforcement, regulators)
13. Executive escalation criteria defined
14. Escalation metrics tracked
15. False escalations analyzed and reduced

---

# Sheet 5: 4. Alert Performance Metrics

## Header
**Title:** "4. ALERT PERFORMANCE METRICS"  
**Policy Reference:** "Assess metrics per ISMS-POL-A.8.16-S2.3.9"

## Column Headers - 18 Columns (A-R)

| Col | Header | Width | Type |
|-----|--------|-------|------|
| A | Metric Name | 30 | Text |
| B | Metric Category | 22 | Dropdown | Volume, Response Time, Quality, Effectiveness, Workload |
| C | Measurement Method | 25 | Text |
| D | Data Source | 22 | Text |
| E | Current Value | 15 | Text |
| F | Target/SLA | 15 | Text |
| G | Status | 16 | Dropdown | ✅ Meeting Target, ⚠️ Below Target, ❌ Critical |
| H | Trend (30d) | 16 | Dropdown | Improving, Stable, Declining |
| I | Measurement Frequency | 18 | Dropdown | Real-Time, Daily, Weekly, Monthly |
| J | Reporting Frequency | 18 | Dropdown | Daily, Weekly, Monthly, Quarterly |
| K | Reported To | 20 | Text |
| L | Automated Tracking | 18 | Dropdown | Yes, Partial, No |
| M | Dashboard Available | 18 | Dropdown | Yes, No |
| N | Alert on Threshold | 18 | Dropdown | Yes, No |
| O | Last Review | 14 | Text | DD.MM.YYYY |
| P | Action Items | 30 | Text |
| Q | Compliance Status | 18 | Dropdown | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant |
| R | Notes | 25 | Text |

**Key Metrics to Track:**

- Total alerts per day/week/month
- Alerts by severity (Critical/High/Medium/Low)
- True Positive rate (%)
- False Positive rate (%)
- Mean Time To Acknowledge (MTTA)
- Mean Time To Triage (MTTT)
- Mean Time To Investigate (MTTI)
- Mean Time To Resolve (MTTR)
- SLA compliance rate (%)
- Escalation rate (%)
- Alert-to-Incident ratio
- SOC analyst workload (alerts/shift)
- Detection rate (from testing)

## Compliance Checklist
1. Alert volume metrics tracked
2. Response time metrics tracked (MTTA, MTTT, MTTI, MTTR)
3. Quality metrics tracked (TP rate, FP rate)
4. Effectiveness metrics tracked (detection rate)
5. Metrics targets defined
6. Metrics measured consistently
7. Metrics reported to SOC Lead (weekly)
8. Metrics reported to CISO (monthly)
9. Metrics dashboard available
10. Trends analyzed
11. Performance issues identified
12. Improvement actions taken
13. SLA compliance tracked
14. Metrics drive tuning decisions
15. Metrics included in management reporting

---

# Sheet 6: 5. SOC Operational Readiness

## Header
**Title:** "5. SOC OPERATIONAL READINESS ASSESSMENT"  
**Policy Reference:** "Assess SOC operations per ISMS-POL-A.8.16-S3"

## Column Headers - 17 Columns (A-Q)

| Col | Header | Width | Type |
|-----|--------|-------|------|
| A | Readiness Area | 28 | Dropdown | Staffing, Training, Tools, Procedures, Communication, Facilities, Testing, Documentation |
| B | Requirement | 35 | Text |
| C | Current State | 35 | Text |
| D | Status | 18 | Dropdown | ✅ Adequate, ⚠️ Needs Improvement, ❌ Inadequate |
| E | Evidence | 30 | Text |
| F | Gap Description | 30 | Text |
| G | Business Impact | 25 | Text |
| H | Risk Level | 15 | Dropdown | Critical, High, Medium, Low |
| I | Remediation Plan | 30 | Text |
| J | Target Date | 14 | Text | DD.MM.YYYY |
| K | Owner | 20 | Text |
| L | Budget Required | 15 | Dropdown | Yes, No, Unknown |
| M | Dependencies | 25 | Text |
| N | Status | 16 | Dropdown | Complete, In Progress, Planned, Not Started |
| O | Last Updated | 14 | Text | DD.MM.YYYY |
| P | Compliance Status | 18 | Dropdown | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant |
| Q | Notes | 25 | Text |

## Compliance Checklist
**Staffing:**
1. SOC staffing adequate for 24/7 coverage (if required)
2. SOC analyst to alert ratio acceptable (<50 alerts/shift)
3. SOC tiers defined (Tier 1, 2, 3)
4. On-call rotation established
5. Shift handover procedures defined

**Training:**
6. SOC analysts trained on triage procedures
7. SOC analysts trained on investigation playbooks
8. SOC analysts trained on tools (SIEM, EDR, etc.)
9. Training records maintained
10. Quarterly training refreshers conducted

**Tools & Systems:**
11. All required tools accessible to SOC
12. Tool access tested and functional
13. Tool documentation available
14. Tool integrations working
15. Communication systems functional (ticketing, chat, email)

**Procedures:**
16. SOC procedures documented
17. Playbooks available for common alert types
18. Escalation procedures documented
19. Shift handover checklists available
20. Standard operating procedures (SOPs) updated

**Testing:**
21. Tabletop exercises conducted quarterly
22. Alert response tested (red team, purple team)
23. Escalation procedures tested
24. Communication systems tested
25. Disaster recovery procedures tested

---

# Sheet 7: Summary Dashboard

## Section 1: Alert Management Summary (Rows 3-18)

- Total alerts (last 30 days)
- Alerts by severity breakdown
- True Positive rate % (target >20%)
- False Positive rate % (target <25%)
- Alert-to-Incident ratio
- Noisy alerts requiring tuning (count)

## Section 2: Response Time Performance (Rows 21-35)

- MTTA (Mean Time To Acknowledge)
  - Critical: Current vs. Target (<15 min)
  - High: Current vs. Target (<1 hr)
- MTTT (Mean Time To Triage)
  - Critical: Current vs. Target (<1 hr)
  - High: Current vs. Target (<4 hrs)
- MTTI (Mean Time To Investigate)
- MTTR (Mean Time To Resolve)
- SLA compliance rate % (target >95%)

## Section 3: Escalation Metrics (Rows 38-48)

- Escalations to Tier 2 (count, %)
- Escalations to IR (count, %)
- Escalations to CISO (count)
- Escalation rate by severity
- False escalation rate %

## Section 4: SOC Operational Health (Rows 51-63)

- SOC analyst count (current/required)
- Coverage model (24/7, business hours, hybrid)
- Average alerts per shift
- Analyst workload status
- Training completion %
- Tool availability %
- Procedure documentation complete %

## Section 5: Compliance Summary (Rows 66-76)
| Assessment Area | Total | Compliant | Partial | Non-Compliant | % |
|-----------------|-------|-----------|---------|---------------|---|
| 1. Alert Generation | Formula | Formula | Formula | Formula | Formula |
| 2. Triage & Investigation | Formula | Formula | Formula | Formula | Formula |
| 3. Escalation & Response | Formula | Formula | Formula | Formula | Formula |
| 4. Performance Metrics | Formula | Formula | Formula | Formula | Formula |
| 5. SOC Readiness | Formula | Formula | Formula | Formula | Formula |
| **OVERALL** | Formula | Formula | Formula | Formula | Formula |

## Section 6: Critical Issues (Rows 79-87)

- Priority | Issue | Impact | Target Date | Owner | Status

---

**END OF SPECIFICATION**

---

# Integration Points with Other Assessments

## Cross-References to A.8.16.1 (Monitoring Infrastructure)

**Alert Generation Platforms:**

- Sheet 2, Column A (Alert Source) references monitoring platforms from A.8.16.1, Sheet 2
- Validation: Every alert-generating platform in A.8.16.4 should be documented in A.8.16.1

## Cross-References to A.8.16.2 (Baselines & Detection)

**Detection Rules:**

- Sheet 2 (Alert Sources) maps to A.8.16.2, Sheet 5 (Detection Rule Coverage)
- Alert TP/FP rates inform detection rule tuning
- Sheet 4 (Investigation Procedures) references baselines from A.8.16.2, Sheets 2/3/4

## Cross-References to A.8.16.3 (Coverage)

**Alert Scope:**

- Assets generating alerts should be in A.8.16.3, Sheet 2 (Asset Inventory)
- Coverage gaps identified in A.8.16.3 may explain missing alerts
- Network segments (A.8.16.3, Sheet 3) determine alert scope

---

# Automated Alert Management Tracking

**Recommended Automation:**

**1. Real-Time SLA Monitoring:**
```
# SIEM query for SLA compliance dashboard
index=notable status=Open OR status="In Progress"
| eval age_minutes = (now() - _time) / 60
| eval sla_target = case(
    severity="Critical", 120,
    severity="High", 480,
    severity="Medium", 2880,
    severity="Low", 43200)
| eval sla_status = case(
    age_minutes > sla_target, "Violated",
    age_minutes > (sla_target * 0.8), "Warning",
    1=1, "OK")
| stats count by severity, sla_status
| sort -severity
```

**2. Daily Alert Quality Report:**
```
# Calculate daily TP/FP rates per detection rule
index=notable earliest=-24h latest=now
| stats count, 
        sum(eval(disposition="True Positive")) as tp,
        sum(eval(disposition="False Positive")) as fp
        by rule_id, rule_name
| eval tp_rate = round(tp / count * 100, 1)
| eval fp_rate = round(fp / count * 100, 1)
| eval quality = case(
    fp_rate > 50, "Needs Tuning",
    fp_rate > 30, "Monitor",
    1=1, "Good")
| sort -count
| outputlookup daily_alert_quality.csv
```

**3. Alert Backlog Warning:**
```
# Alert SOC manager if aged alerts exceed threshold
index=notable status=Open
| eval age_hours = (now() - _time) / 3600
| stats count as aged_count by severity
        where age_hours > case(
            severity="Critical", 2,
            severity="High", 8,
            severity="Medium", 48,
            severity="Low", 720)
| where aged_count > 0
| sendemail to="soc-manager@company.com" 
            subject="Alert Backlog Warning"
```

---

# Alert Management Maturity Assessment

**Use this framework to assess your organization's alert management maturity:**

## Level 1: Reactive (Ad-Hoc)

**Characteristics:**

- No formal alert triage process
- Investigation procedures undefined or tribal knowledge
- No SLA tracking
- FP rate unknown or >60%
- No escalation procedures
- Backlog unmanaged (alerts age indefinitely)

**Gaps:**

- Define triage procedures
- Establish SLAs
- Track alert metrics
- Create investigation playbooks
- Define escalation paths

**Timeline to Next Level:** 6-12 months

---

## Level 2: Managed (Process Defined)

**Characteristics:**

- Triage process defined
- Investigation playbooks exist (top 5 alert types)
- SLA tracking manual (spreadsheets)
- FP rate 40-60% (known but not improving)
- Escalation procedures documented
- Backlog managed weekly (some aged alerts)

**Gaps:**

- Automate SLA tracking
- Expand playbook coverage
- Systematic tuning process
- SOAR/automation for routine alerts
- Real-time backlog visibility

**Timeline to Next Level:** 3-6 months

---

## Level 3: Optimized (Automated & Measured)

**Characteristics:**

- Automated triage for routine alerts
- Investigation playbooks for top 20 alert types (80%+ coverage)
- SLA tracking automated with dashboards
- FP rate 20-40% (continuous improvement)
- Escalation tested regularly
- Backlog monitored daily (alerts rarely age beyond SLA)

**Gaps:**

- Advanced SOAR orchestration
- Machine learning-assisted triage
- Proactive FP reduction (predictive tuning)
- Sub-5-minute MTTR for automated response

**Timeline to Next Level:** 6-12 months

---

## Level 4: Continuous Improvement (Data-Driven Excellence)

**Characteristics:**

- AI/ML-assisted triage and enrichment
- Playbook-driven response automation
- Real-time SLA dashboards with executive visibility
- FP rate <20% (industry-leading)
- Automated escalation with context
- Zero backlog (all alerts handled within SLA)
- Metrics-driven continuous improvement

**Sustaining Excellence:**

- Benchmark against industry peers
- Continuously reduce MTTR
- Expand automation coverage
- Share playbooks across security community

---

# Document Change Log

**Version 2.0 (22.01.2026):**

- Added comprehensive Part I: User Completion Guide (1,789 lines)
- Enhanced with detailed sheet-by-sheet guidance for all 6 assessment sheets
- Added 10 common pitfalls with detailed solutions
- Enhanced quality checklist with cross-assessment validation
- Added alert management maturity model
- Added automated tracking queries (SIEM)

**Version 1.0 (Original):**

- Technical specification only (365 lines)
- Sheet structures and column definitions
- Basic compliance checklists

---

# Appendix: Alert Management Quick Reference

## Alert Severity Definitions

| Severity | Definition | Examples | Response SLA |
|----------|------------|----------|--------------|
| **Critical** | Immediate threat, widespread impact, or active compromise | Ransomware detected, data breach in progress, critical infrastructure compromised | Triage: <15 min<br>Response: <2 hours |
| **High** | Significant threat or potential compromise requiring urgent attention | Malware on endpoint, privilege escalation detected, suspicious authentication from foreign IP | Triage: <1 hour<br>Response: <8 hours |
| **Medium** | Policy violation or suspicious activity requiring investigation | Failed login threshold, unusual network traffic, configuration change | Triage: <4 hours<br>Response: <48 hours |
| **Low** | Informational or minor policy deviation | Informational security events, low-priority policy violations | Triage: <24 hours<br>Response: <30 days |

## Alert Disposition Definitions

| Disposition | Definition | Actions Required |
|-------------|------------|------------------|
| **True Positive (TP)** | Confirmed security event requiring response | Containment, eradication, recovery, documentation, escalation if needed |
| **False Positive (FP)** | Benign activity misclassified as threat | Document FP pattern, tune detection rule to prevent recurrence |
| **Benign Positive** | Actual policy violation but not security threat | Policy enforcement action, user notification, documentation |
| **Indeterminate** | Insufficient data to determine | Queue for re-investigation after 7/30 days, consider enhanced monitoring |

## Response Time SLA Targets

| Severity | Triage SLA | Investigation SLA | Total Response SLA | Escalation Required |
|----------|------------|-------------------|-------------------|---------------------|
| Critical | <15 min | <1 hour | <2 hours | Yes (SOC Manager to IR to CISO) |
| High | <1 hour | <4 hours | <8 hours | If impact >10 systems OR unclear |
| Medium | <4 hours | <24 hours | <48 hours | If repeated pattern |
| Low | <24 hours | <7 days | <30 days | No (unless business impact) |

## Alert Quality Thresholds

| Metric | Excellent | Acceptable | Needs Improvement | Critical |
|--------|-----------|------------|-------------------|----------|
| **FP Rate** | <20% | 20-30% | 30-50% | >50% (tune or disable) |
| **TP Rate** | >30% | 20-30% | 10-20% | <10% (low value) |
| **SLA Compliance** | >95% | 90-95% | 80-90% | <80% (capacity issue) |
| **MTTR (Critical)** | <60 min | 60-120 min | 120-240 min | >240 min (SLA violation) |

## Escalation Triggers

**Immediate Escalation (Critical):**

- Ransomware or destructive malware detected
- Active data breach (exfiltration in progress)
- Critical infrastructure compromised (domain controllers, core network)
- Widespread compromise (>50 systems)
- Regulatory notification trigger (GDPR, PCI, HIPAA breach)

**Urgent Escalation (<1 hour, High):**

- Confirmed malware on multiple systems
- Privilege escalation to Domain Admin
- Suspicious authentication from threat actor infrastructure
- Repeated attack attempts on critical systems
- Unable to determine disposition (analyst needs expert help)

**Standard Escalation (<4 hours, Medium):**

- Policy violations requiring management decision
- Repeated low-severity incidents from same source
- Alert pattern suggesting reconnaissance
- Resource capacity concerns (backlog exceeding SLA)

---

**END OF SPECIFICATION**

---

*"Machines take me by surprise with great frequency."*
— Alan Turing

<!-- QA_VERIFIED: 2026-02-06 -->
