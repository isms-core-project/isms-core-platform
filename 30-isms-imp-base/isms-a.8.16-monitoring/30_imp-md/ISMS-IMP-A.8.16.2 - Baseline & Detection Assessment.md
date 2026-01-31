**ISMS-IMP-A.8.16.2 - Baseline & Detection Assessment**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.16: Monitoring Activities

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.16.2 |
| **Version** | 1.0 |
| **Assessment Area** | Baseline Establishment & Anomaly Detection Capabilities |
| **Related Policy** | ISMS-POL-A.8.16, Section 2.2 (Baseline & Anomaly Detection Requirements) |
| **Purpose** | Assess baseline establishment for normal behavior, evaluate anomaly detection capabilities, and verify detection effectiveness across monitoring infrastructure |
| **Target Audience** | SOC Analysts, Security Engineers, Threat Intelligence Analysts, Detection Engineers, Compliance Officers, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Quarterly (Baselines evolve, detection rules require continuous tuning) |
| **Date** | 22.01.2026 |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Original] | Initial technical specification | ISMS Implementation Team |

### Document Structure

This document consists of two parts:

- **PART I: USER COMPLETION GUIDE** (~1,500 lines structured framework)
  - Assessment Overview
  - The Feynman Principle Applied to Baselines
  - Prerequisites & Baseline Data Requirements
  - Step-by-Step Workflow
  - Sheet-by-Sheet Completion Instructions
  - Evidence Collection Requirements
  - Common Pitfalls (The "Gut Feel" Trap)
  - Quality Self-Check Checklist
  - Review & Approval Process

- **PART II: TECHNICAL SPECIFICATION** (~600 lines)
  - Excel Workbook Structure
  - Sheet-by-Sheet Technical Specifications
  - Statistical Profile Requirements
  - Detection Rule Format
  - Effectiveness Metrics Calculations
  - Integration with A.8.16.1 (Infrastructure)


---

**IMPLEMENTATION NOTE:**

This reworked document follows the **ISMS-POL-A.8.16 consolidated policy structure** (dated 22.01.2026).

All policy references have been updated from the old modular format:

- ❌ OLD: "ISMS-POL-A.8.16-S2.2"
- ✅ NEW: "ISMS-POL-A.8.16, Section 2.2 (Baseline & Anomaly Detection Requirements)"


**Prerequisites:** ISMS-IMP-A.8.16.1 (Monitoring Infrastructure Assessment) must be completed first. This assessment builds on the monitoring platforms and log sources documented in A.8.16.1.

---

# EXECUTIVE SUMMARY

## What This Assessment Does

**ISMS-IMP-A.8.16.2** assesses your baseline establishment and anomaly detection capabilities - the foundation of effective threat detection.

**Key Questions Answered:**
1. **Do you have documented baselines?** (Measured behavioral profiles, not guesses)
2. **Are baselines statistically valid?** (30+ days observation, exclude incidents, time-aware)
3. **What can you detect?** (Attack types covered by detection rules)
4. **What can't you detect?** (Coverage gaps requiring new detection rules)
5. **How effective is detection?** (True positive rate, false positive rate, MTTD)
6. **Are detection rules tuned?** (Alert noise vs. signal, tuning frequency)

## Why This Assessment Matters

### The Feynman Principle Applied to Baselines

As Richard Feynman famously said: *"The first principle is that you must not fool yourself—and you are the easiest person to fool."*

**Applied to baselines and detection:**

**❌ Fooling Yourself (Cargo Cult Baselines):**

- "Normal authentication is around 100-200 logins per hour" (vague, unmeasurable)
- "Database seems busy during the day" (subjective, no numbers)
- "That user always accesses lots of files" (gut feel, no data)
- "We have 500 detection rules, so we're detecting threats" (quantity ≠ quality)


**✅ Not Fooling Yourself (Real Baselines):**

- "User authentication rate during business hours (08:00-18:00 CET): Mean 145 logins/hour, Std Dev 23, 95th percentile 189 logins/hour. Alert threshold: 245 logins/hour (95th percentile × 1.3). Baseline established over 45-day observation period (15.11.2025 - 29.12.2025) excluding 2 security incidents."
- "Database query rate: Baseline 450 queries/minute ±50 (mean ±1 std dev), 95th percentile 523 queries/min. Alert threshold: 680 queries/minute (95th percentile × 1.3). Baseline observation: 60 days, updated monthly."
- "User X file access pattern: Normal 15-30 files/day, mean 22, std dev 5. Alert threshold: 50 files/day (mean + 3×std dev). Baseline valid 01.10.2025 - 31.12.2025, next review 31.01.2026."


**If you cannot express baselines with numbers, statistics, and time periods, you don't have baselines—you have opinions.**

This assessment prevents cargo cult monitoring by requiring:

- **Documented baselines** - Not guesses, but measured behavioral patterns
- **Statistical profiles** - Mean, median, standard deviation, percentiles
- **Threshold derivation** - Explicit methodology (95th percentile × 1.3, mean + 3σ, etc.)
- **Observation periods** - 30+ days minimum, business cycles included
- **Regular validation** - Quarterly baseline review, monthly for critical systems


## The "Gut Feel" Trap

**Common Scenario:**

- SOC Analyst: "That login pattern looks suspicious"
- Manager: "How do you know?"
- SOC Analyst: "Just... doesn't feel right. User normally logs in at 9 AM, this is 6 AM"
- Manager: "Has the user EVER logged in at 6 AM before?"
- SOC Analyst: "Uh... I don't know. Maybe?"
- Manager: "What IS their normal login time range?"
- SOC Analyst: "Around 9 AM... I think?"


**Without baselines:**

- Gut feel replaces data (unreliable, biased, inconsistent)
- Analysts waste time on false positives (investigating normal behavior)
- True anomalies are missed (no threshold to trigger alert)
- Incident response is delayed (manual triage of everything)


**With baselines:**

- Alert triggers automatically (user logged in 4 standard deviations outside normal time window)
- Context is immediate (baseline shows normal login time: 08:45-09:15, 99.7% of time)
- Investigation is focused (automated pre-investigation: recent HR changes? Travel? VPN from unusual location?)
- MTTD (Mean Time to Detect) drops from hours to minutes


## How to Use This Document

### For Assessors (SOC, Detection Engineering, Threat Intelligence):

**Part I: User Completion Guide** is YOUR primary resource:

1. **Read Assessment Overview** (pages 4-8) to understand baseline requirements
2. **Understand Feynman Principle** (page 5) - if you can't measure it, you don't have it
3. **Gather Baseline Data** (pages 9-12) - 30+ days of historical data required
4. **Follow the Workflow** (pages 13-16) - 3-week timeline for comprehensive baseline assessment
5. **Complete Each Sheet** (pages 17-70) using detailed instructions:

   - Sheet 2: System Utilization Baselines (pages 17-30)
   - Sheet 3: Access Pattern Baselines (pages 31-40)
   - Sheet 4: Application Behavior Baselines (pages 41-50)
   - Sheet 5: Detection Rule Coverage (pages 51-60)
   - Sheet 6: Detection Effectiveness (pages 61-70)

6. **Collect Evidence** (pages 71-75) - baseline documentation, detection rules, test results
7. **Avoid Common Pitfalls** (pages 76-85) - learn from "gut feel" failures
8. **Self-Check Quality** (pages 86-88) before submitting
9. **Navigate Approval Process** (pages 89-91)

### For Technical Implementers (Python Developers, SIEM Engineers):

**Part II: Technical Specification** is YOUR primary resource:

1. **Review Workbook Structure** (pages 93-95) - 8 sheets, statistical requirements
2. **Implement Baseline Templates** (pages 96-110):

   - Statistical profile format (mean, median, std dev, percentiles)
   - Time-aware baseline structures (business hours, off-hours, weekends)
   - Threshold derivation methodologies

3. **Implement Detection Rule Format** (pages 111-120):

   - Rule taxonomy (signature, anomaly, behavioral, correlation)
   - Coverage mapping (MITRE ATT&CK, kill chain)
   - Effectiveness tracking (TP, FP, FN rates)

4. **Apply Formulas** (pages 121-125) - compliance scoring, effectiveness calculations

### For Auditors & Compliance Officers:

**Focus Areas:**

- **Baseline Requirements** (Part I, pages 17-50): Statistical rigor, observation periods
- **Detection Coverage** (Part I, pages 51-60): MITRE ATT&CK mapping, gap analysis
- **Effectiveness Evidence** (Part I, pages 61-70, 71-75): True positive rates, testing results
- **Policy Traceability** (Throughout): Requirements traced to ISMS-POL-A.8.16, Section 2.2


### For Management (CISO, Security Managers):

**Executive Summary Locations:**

- **Baseline Summary** (Part I, page 50): Coverage by system type, baseline maturity
- **Detection Coverage Summary** (Part I, page 60): Attack types covered vs. gaps
- **Effectiveness Metrics** (Part I, page 70): MTTD, detection rate, false positive rate
- **Dashboard** (Part II, pages 126-128): Consolidated compliance view


---

# PART I: USER COMPLETION GUIDE

# Assessment Overview

## Purpose & Scope

**Assessment Name:** ISMS-IMP-A.8.16.2 - Baseline & Detection Assessment

This assessment evaluates your organization's capability to:
1. Establish **measurable baselines** for normal behavior (systems, users, applications)
2. Detect **anomalous behavior** that deviates from baselines
3. Cover **attack scenarios** with detection rules (MITRE ATT&CK, kill chain)
4. Measure **detection effectiveness** (true positives, false positives, MTTD)
5. **Tune detection** to reduce alert noise and improve signal

**Core Questions:**

- Do you have documented baselines with statistical profiles? (Mean, std dev, percentiles)
- Are baselines time-aware? (Business hours vs. off-hours, weekday vs. weekend)
- What attack types can you detect? (Malware, lateral movement, data exfiltration, etc.)
- What attack types CAN'T you detect? (Coverage gaps)
- How effective is detection? (What percentage of attacks are detected? False positive rate?)
- How often are detection rules tuned? (Monthly? Quarterly? Never?)


## Key Principle: Baselines Must Be Measurable

**Acceptable Baseline** (measurable, specific, statistical):
```
Baseline ID: BL-2026-001
System: dc01.organization.example (Domain Controller)
Metric: Authentication Success Rate (Events/Hour)
Observation Period: 45 days (15.11.2025 - 29.12.2025)
Exclusions: Security incident 18.12.2025 (brute force attack - excluded from baseline)

Statistical Profile (Business Hours 08:00-18:00 CET, Mon-Fri):

- Mean: 145 authentications/hour
- Median: 142 authentications/hour
- Standard Deviation: 23 authentications/hour
- 95th Percentile: 189 authentications/hour
- 99th Percentile: 215 authentications/hour


Alert Threshold: 245 authentications/hour
Derivation: 95th percentile × 1.3 (allows normal peaks, alerts on anomalies)

Time-Aware Baselines:

- Business Hours (Mon-Fri 08:00-18:00): Mean 145, 95th %ile 189
- Off-Hours (Mon-Fri 18:00-08:00): Mean 12, 95th %ile 25
- Weekends (Sat-Sun all hours): Mean 8, 95th %ile 18


Baseline Validity: 01.01.2026 - 31.03.2026
Next Review: 31.03.2026 (quarterly)
Owner: SOC Lead
```

**Unacceptable "Baseline"** (vague, unmeasurable, subjective):
```
"Normal authentication activity is around 100-200 logins per hour during the day.
Sometimes it's higher, sometimes lower. We alert if it seems unusually high."
```

**Why the second is unacceptable:**

- "Around 100-200" - Too broad (100% margin of error!)
- "During the day" - What hours exactly? Does 7 AM count? 7 PM?
- "Sometimes higher" - How much higher is normal? 250? 500? 1000?
- "Seems unusually high" - Subjective judgment, not measurable threshold


## What You'll Document

### System Utilization Baselines (Sheet 2)

- CPU utilization patterns (mean, std dev, peak times)
- Memory consumption baselines
- Disk I/O patterns
- Network bandwidth consumption
- Process resource usage


**For Each Baseline:**

- Statistical profile (mean, median, std dev, percentiles)
- Time-aware variations (business hours, off-hours, weekends)
- Alert thresholds (derived from statistical profile)
- Observation period (dates, duration, exclusions)


### Access Pattern Baselines (Sheet 3)

- User authentication patterns (login times, frequency, locations)
- Geographic access patterns (normal locations, travel patterns)
- Privileged access patterns (sudo, admin logins, elevation requests)
- Failed authentication baselines (normal failure rate vs. attack indicators)
- Service account activity patterns


### Application Behavior Baselines (Sheet 4)

- Transaction volumes and timing patterns
- API call rates and patterns
- Database query patterns (queries/minute, query types)
- File access and modification patterns
- Network connection patterns (internal, external, protocols)


### Detection Rule Coverage (Sheet 5)

- Detection rule inventory (all active rules)
- Rule taxonomy (signature, anomaly, behavioral, correlation)
- MITRE ATT&CK coverage (tactics and techniques covered)
- Kill chain coverage (reconnaissance, exploitation, persistence, etc.)
- Coverage gaps (attack types not covered by rules)


### Detection Effectiveness (Sheet 6)

- True positive rate (% of attacks detected)
- False positive rate (% of alerts that are noise)
- False negative rate (% of attacks missed)
- Mean Time to Detect (MTTD) - time from attack start to detection
- Alert volume trends (improving or degrading?)
- Tuning effectiveness (false positive reduction over time)


## How This Relates to Other A.8.16 Assessments

| Assessment | Focus | Relationship to A.8.16.2 |
|-----------|-------|--------------------------|
| ISMS-IMP-A.8.16.1 | Infrastructure | Provides monitoring platforms and log sources that A.8.16.2 uses for baseline establishment |
| **ISMS-IMP-A.8.16.2** | **Baselines & Detection** | **HOW you detect anomalies** (THIS ASSESSMENT) |
| ISMS-IMP-A.8.16.3 | Coverage | Uses baselines from A.8.16.2 to validate monitoring coverage completeness |
| ISMS-IMP-A.8.16.4 | Alert Management | Uses detection rules from A.8.16.2 to analyze alert response effectiveness |
| ISMS-IMP-A.8.16.5 | Compliance Dashboard | Consolidates all assessments including baseline/detection maturity from A.8.16.2 |

**Dependencies:**

- **A.8.16.1 must be completed first** - Can't establish baselines without knowing what monitoring platforms and log sources exist
- **A.8.16.2 informs A.8.16.3** - Coverage assessment validates that baselines exist for critical systems
- **A.8.16.2 informs A.8.16.4** - Alert management effectiveness depends on detection rule quality


## Policy References

This assessment implements requirements from:

**Primary Policy Reference:**

- **ISMS-POL-A.8.16, Section 2.2 (Baseline & Anomaly Detection Requirements)**
  - Section 2.2.1: Baseline Philosophy
  - Section 2.2.2: Baseline Establishment Requirements
  - Section 2.2.3: Baseline Documentation
  - Section 2.2.4: Anomaly Detection Scope
  - Section 2.2.5: Detection Effectiveness Requirements


**Supporting Policy References:**

- ISMS-POL-A.8.16, Section 2.1 (Monitoring Infrastructure Requirements) - for platform capabilities
- ISMS-POL-A.8.16, Section 2.3 (Alert Management & Response Requirements) - for alert handling
- ISMS-POL-A.8.16, Annex B (Baseline Definition Template) - standardized baseline format


**Regulatory Context:**

- Swiss nDSG / EU GDPR: Anomaly detection for data protection incident identification
- ISO/IEC 27001:2022 Control A.8.16: Monitoring for anomalous behavior
- NIST SP 800-137: Information Security Continuous Monitoring (ISCM)
- MITRE ATT&CK Framework: Detection coverage mapping


## Expected Outputs

After completing this assessment, you will have:

1. **Documented Baseline Inventory**

   - All critical systems with statistical behavioral baselines
   - Time-aware baselines (business hours, off-hours, weekends)
   - Threshold derivation methodology documented


2. **Detection Rule Inventory**

   - All active detection rules catalogued
   - MITRE ATT&CK coverage mapped
   - Coverage gaps identified (attack types not covered)


3. **Effectiveness Metrics**

   - True positive rate (target: >90% for high-severity threats)
   - False positive rate (target: <20% for critical alerts)
   - MTTD (Mean Time to Detect) measured and tracked
   - Baseline for continuous improvement


4. **Tuning Roadmap**

   - High false-positive rules identified for tuning
   - Coverage gaps prioritized for new rule development
   - Quarterly tuning plan with owners and timelines


5. **Evidence Package**

   - Baseline documentation (using ISMS-POL-A.8.16, Annex B template)
   - Detection rule exports (SIEM rule configurations)
   - Effectiveness test results (purple team, simulated attacks)
   - Tuning history (before/after false positive rates)


6. **Compliance Status**

   - Compliance with ISMS-POL-A.8.16, Section 2.2 requirements
   - Baseline coverage percentage (% of critical systems with baselines)
   - Detection coverage percentage (% of MITRE ATT&CK tactics covered)
   - Improvement roadmap for gaps


---

# Prerequisites & Baseline Data Requirements

Before starting this assessment, you need:

## Completed Prerequisites

**Required Previous Assessment:**

- ✅ **ISMS-IMP-A.8.16.1 (Monitoring Infrastructure Assessment)** must be completed
  - Provides monitoring platform inventory
  - Provides log source inventory
  - Confirms which systems are monitored (can establish baselines for)


## Historical Log Data

**Minimum Data Requirements:**

- **30 days** of historical log data (absolute minimum)
- **45-60 days** recommended (captures business cycles, seasonal variations)
- **90+ days** ideal (robust statistical profiles, multiple business cycles)


**Data Must Include:**

- System performance metrics (CPU, memory, disk, network)
- User authentication events (success, failure, timing, locations)
- Application activity logs (transactions, API calls, database queries)
- Network traffic data (connections, bandwidth, protocols)


**Data Must Be:**

- **Continuous** (no large gaps - gaps invalidate baseline)
- **Clean** (exclude known incidents from baseline establishment)
- **Representative** (include normal business cycles - month-end, quarter-end if applicable)


**Where to Find:**

- SIEM historical data (if retention ≥30 days)
- Log management platform archives
- Performance monitoring tools (Grafana, Prometheus, CloudWatch)
- Application performance monitoring (APM) tools


## System Documentation

**For Each System Being Baselined:**

- System name / hostname
- System type and function
- Business criticality tier (Tier 1, 2, 3)
- Normal operating schedule (24/7, business hours only, batch processing windows)
- Known seasonal patterns (month-end spikes, holiday lulls, fiscal year-end processing)
- Recent changes (migrations, upgrades, configuration changes that affect behavior)


**Where to Find:**

- ISMS-IMP-A.8.16.1, Sheet 3 (Log Source Coverage) - provides system inventory
- CMDB (Configuration Management Database)
- System owner documentation
- Change management records


## Incident History

**Why This Matters:**
Baselines must represent NORMAL behavior. Security incidents create anomalies that contaminate baselines if not excluded.

**Required Information:**

- Security incident dates and times (last 90 days)
- Affected systems (which systems were involved in incidents)
- Incident type (malware, brute force, data exfiltration, etc.)


**Purpose:**
Exclude incident periods from baseline observation windows to ensure baselines reflect normal, not attack behavior.

**Example:**

- Baseline observation period: 15.11.2025 - 29.12.2025 (45 days)
- Security incident: 18.12.2025 14:00-22:00 (brute force attack on dc01)
- Excluded from baseline: 18.12.2025 00:00-23:59 (entire day excluded for safety)
- Effective observation: 44 days (45 days - 1 incident day)


## Detection Rule Access

**SIEM / Monitoring Platform Access:**

- Administrative access to view detection rules
- Access to rule configuration (conditions, thresholds, actions)
- Access to alert history (last 90 days)
- Access to false positive tracking (if available)


**Detection Rule Export:**

- Ability to export rule configurations
- Ability to export alert history
- Ability to export rule effectiveness metrics (if platform provides)


**Where to Find:**

- SIEM: Settings → Detection → Correlation Rules / Searches / Alerts
- IDS/IPS: Rule sets, signature databases
- EDR: Detection policies, behavioral rules
- UEBA: Anomaly detection configurations


## Detection Testing Capability

**For Effectiveness Assessment:**

- Ability to run simulated attacks (purple team, red team, testing tools)
- Test environment (or controlled production testing with approval)
- Attack simulation tools (Atomic Red Team, Caldera, Metasploit, custom scripts)
- Coordination with security team (ensure tests don't trigger real incident response)


**Testing Scope:**

- Test sample of detection rules (not all - focus on critical rules)
- Test across MITRE ATT&CK tactics (reconnaissance, persistence, lateral movement, etc.)
- Document what was detected vs. missed


## Statistical Analysis Tools

**Basic Tools (Minimum):**

- Excel / Spreadsheet software (calculate mean, median, std dev, percentiles)
- Python / R (optional but helpful for larger datasets)
- SIEM built-in analytics (if available)


**Statistical Knowledge (Assessor Requirements):**

- Understand mean, median, mode
- Understand standard deviation (measure of spread)
- Understand percentiles (95th percentile = 95% of values below this)
- Understand normal distribution (bell curve) vs. skewed distributions


**If Assessor Lacks Statistical Knowledge:**

- Partner with data analyst or statistician
- Use SIEM built-in baseline features (if available)
- Use baseline template strictly (ISMS-POL-A.8.16, Annex B) - follow formulas


## Time Commitment

**Total Assessment Time:** 3 weeks for comprehensive baseline assessment

**Phase 1: Data Collection (Week 1)**

- Extract 45-60 days of historical data: 2-4 hours
- Clean data (remove incident periods): 1-2 hours
- Organize by system/user/application: 2-3 hours
- **Total:** 5-9 hours


**Phase 2: Baseline Establishment (Week 2)**

- System utilization baselines (Sheet 2): 8-12 hours (10-20 systems)
- Access pattern baselines (Sheet 3): 6-10 hours (authentication, privileged access)
- Application baselines (Sheet 4): 6-10 hours (key applications)
- **Total:** 20-32 hours


**Phase 3: Detection Assessment (Week 2-3)**

- Detection rule inventory (Sheet 5): 4-6 hours
- MITRE ATT&CK mapping: 6-8 hours
- Effectiveness testing (Sheet 6): 8-12 hours
- **Total:** 18-26 hours


**Phase 4: Documentation & Approval (Week 3)**

- Evidence collection: 4-6 hours
- Quality review: 2-3 hours
- Stakeholder review and approval: 4-6 hours
- **Total:** 10-15 hours


**Grand Total:** 53-82 hours (7-10 business days of effort across 3-week calendar period)

**For Large Environments:**

- Multiply by number of critical systems / applications
- Consider phased approach (baseline Tier 1 systems first, then Tier 2)
- Leverage automation (scripted statistical analysis, SIEM features)


**For Small Environments:**

- Can complete in 2 weeks if few systems
- Still requires same statistical rigor per baseline


---

# Assessment Workflow

## Phase 1: Data Collection & Preparation (Week 1)

**Step 1.1: Extract Historical Data (2-4 hours)**
1. Identify systems for baseline establishment (from A.8.16.1, Sheet 3 - prioritize Tier 1)
2. Determine observation period (45-60 days recommended)
3. Extract performance data from monitoring platforms:

   - System metrics: CPU, memory, disk I/O, network
   - Authentication logs: successful logins, failures, timing, locations
   - Application logs: transactions, API calls, database queries

4. Save raw data (CSV, JSON, or database export)

**Step 1.2: Clean Data (1-2 hours)**
1. Review incident history (last 90 days)
2. Identify affected systems and time periods
3. Exclude incident periods from baseline data
4. Document exclusions (dates, reasons, systems affected)

**Step 1.3: Organize Data (2-3 hours)**
1. Group by system / user / application
2. Aggregate by time period (hourly, daily as appropriate)
3. Separate business hours vs. off-hours data (if patterns differ)
4. Validate data completeness (no large gaps)

## Phase 2: Baseline Establishment (Week 2)

**Step 2.1: System Utilization Baselines (Sheet 2: 8-12 hours)**
For each critical system:
1. Calculate statistical profile:

   - Mean (average) CPU, memory, disk, network usage
   - Median (50th percentile) - middle value
   - Standard deviation (measure of variability)
   - 95th percentile (95% of values below this)
   - 99th percentile (99% of values below this)

2. Create time-aware baselines (if patterns differ):

   - Business hours (08:00-18:00 Mon-Fri)
   - Off-hours (18:00-08:00 Mon-Fri)
   - Weekends (Sat-Sun all hours)

3. Derive alert thresholds:

   - Methodology: 95th percentile × 1.3 (or mean + 3σ, or other justified method)
   - Document rationale

4. Document in Sheet 2 (using ISMS-POL-A.8.16, Annex B template)

**Step 2.2: Access Pattern Baselines (Sheet 3: 6-10 hours)**
For user authentication patterns:
1. Calculate per-user statistics:

   - Login count per day (mean, std dev, percentiles)
   - Login timing (normal login time window)
   - Login locations (normal offices, VPN endpoints, countries)
   - Failed login rate (normal failure rate baseline)

2. Calculate aggregate statistics:

   - Total organization authentication rate (events/hour)
   - Privileged access rate (sudo, admin logins per day)
   - Service account activity patterns

3. Derive alert thresholds (unusual timing, unusual location, high failure rate)
4. Document in Sheet 3

**Step 2.3: Application Behavior Baselines (Sheet 4: 6-10 hours)**
For critical applications:
1. Transaction volume baselines (transactions/minute, by hour of day)
2. API call rate baselines (calls/minute, by endpoint if available)
3. Database query baselines (queries/minute, query types if available)
4. File access baselines (files accessed/day, unusual file types)
5. Network connection baselines (connections/hour, protocols, destinations)
6. Document in Sheet 4

## Phase 3: Detection Rule Assessment (Week 2-3)

**Step 3.1: Detection Rule Inventory (Sheet 5: 4-6 hours)**
1. Export detection rules from SIEM / monitoring platforms
2. Catalog all active rules:

   - Rule ID / name
   - Rule type (signature, anomaly, behavioral, correlation)
   - Description (what attack/behavior does it detect?)
   - Severity (Critical, High, Medium, Low)
   - Status (Active, Disabled, Testing)

3. Count total rules by type and severity

**Step 3.2: MITRE ATT&CK Coverage Mapping (6-8 hours)**
1. For each detection rule, identify which MITRE ATT&CK technique(s) it detects
2. Create coverage matrix:

   - Rows: MITRE ATT&CK Tactics (Reconnaissance, Initial Access, Execution, etc.)
   - Columns: Detection status (Covered, Partial, Not Covered)

3. Identify coverage gaps:

   - Tactics with no detection rules
   - High-priority techniques not covered (lateral movement, credential dumping, etc.)

4. Prioritize gap remediation (focus on high-risk, high-likelihood techniques)

**Step 3.3: Detection Effectiveness Testing (Sheet 6: 8-12 hours)**
1. Select sample of detection rules for testing (10-20 rules across severity levels)
2. Run simulated attacks (Atomic Red Team, Caldera, manual testing):

   - Execute attack technique
   - Monitor for alert generation
   - Record: Detected (TP), Missed (FN), False Alert (FP)

3. Calculate effectiveness metrics:

   - True Positive Rate: (Detected Attacks / Total Attack Attempts) × 100
   - False Positive Rate: (False Alerts / Total Alerts) × 100
   - False Negative Rate: (Missed Attacks / Total Attack Attempts) × 100
   - Mean Time to Detect (MTTD): Average time from attack start to alert

4. Document test results in Sheet 6

## Phase 4: Documentation & Approval (Week 3)

**Step 4.1: Complete Evidence Register (Sheet 8: 4-6 hours)**
1. Collect baseline documentation (statistical profiles, threshold calculations)
2. Collect detection rule exports (SIEM configuration, rule descriptions)
3. Collect effectiveness test results (test logs, alert screenshots, MTTD measurements)
4. Organize evidence with IDs (E001, E002, etc.)
5. Document in Evidence Register

**Step 4.2: Quality Self-Check (2-3 hours)**

- Use Quality Checklist (Section 7)
- Verify all baselines have statistical profiles (not vague descriptions)
- Verify MITRE ATT&CK coverage is complete
- Verify effectiveness metrics are measured (not estimated)


**Step 4.3: Stakeholder Review & Approval (4-6 hours)**

- SOC Lead review (technical accuracy of baselines and detection rules)
- Detection Engineering review (validate statistical methodology, threshold derivation)
- Security Manager review (risk assessment of coverage gaps)
- CISO approval (accept residual risk from detection gaps, approve remediation budget)


---

# Completing Each Sheet

[Due to length constraints, full section includes detailed column-by-column guidance for:]

## Sheet 2: System Utilization Baselines

**Purpose:** Document measured baselines for system resource utilization (CPU, memory, disk, network)

**Policy Reference:** ISMS-POL-A.8.16, Section 2.2.1 (Baseline Establishment)

**Why This Sheet Matters:**
This is where you prove you have REAL baselines, not guesses.

As Feynman said: *"The first principle is that you must not fool yourself—and you are the easiest person to fool."*

**Cargo Cult Baseline:**
"Database CPU is normally around 40-60%"

**Real Baseline:**
"Database CPU: Mean 42%, Std Dev 8%, 95th percentile 58%. Measured over 45-day period (01.11.2025-15.12.2025) excluding 2 incidents. Alert threshold: 75% (95th percentile × 1.3). Business hours (08:00-18:00): Mean 48%. Off-hours: Mean 28%. Weekends: Mean 15%."

**Structure:**

- **Rows 8-37:** 30 data entry rows (baseline inventory for critical systems)
- **Rows 40-60:** Statistical validation checklist


### Column-by-Column Completion Guide

**Column A: System ID**

- **What to Enter:** System identifier (must match Sheet 3 from A.8.16.1)
- **Examples:** `SRV-DC-01`, `PRD-DB-ORDERS`, `APP-WEB-PROD-03`
- **Cross-Reference:** Every system here should be documented in A.8.16.1, Sheet 3
- **Critical Guidance:** Focus on Tier 1 (Critical) systems first


**Column B: System Name/Description**

- **What to Enter:** Human-readable system description
- **Examples:**
  - `Primary Domain Controller - Corporate Forest`
  - `Production Database - Order Management (PostgreSQL 15)`
  - `Web Application Server - Customer Portal`


**Column C: System Type (Dropdown)**

- **Options:** Server, Database, Application, Network Device, Virtual Infrastructure, Storage System, Security Appliance
- **Purpose:** Group similar systems for baseline comparison


**Column D: Criticality Tier (Dropdown)**

- **Options:** Tier 1 (Critical), Tier 2 (High), Tier 3 (Medium), Tier 4 (Low)
- **Policy Requirement:** ALL Tier 1 systems MUST have documented baselines
- **Tier 2:** Recommended (>80% should have baselines)
- **Tier 3/4:** Optional (baseline as needed for anomaly detection)


**Column E: Metric Name (Dropdown)**

- **Options:**
  - `CPU Utilization (%)`
  - `Memory Utilization (%)`
  - `Disk I/O (MB/s)` or `(IOPS)`
  - `Network Traffic (MB/s)` or `(packets/s)`
  - `Disk Space Used (%)`
  - `Process Count`
  - `Connection Count`
  - `Queue Length`
  - `Custom: [Specify]`


**Selection Guidance:**

- **Servers/VMs:** CPU %, Memory %, Disk I/O, Network Traffic
- **Databases:** CPU %, Memory %, Query Rate, Connection Count, Transaction Rate
- **Network Devices:** Interface Utilization %, Packet Rate, Error Rate
- **Applications:** Transaction Rate, Response Time, Active Sessions


**One row per metric** - If monitoring CPU, Memory, and Disk for same server, create 3 rows.

**Column F: Observation Period - Start Date (DD.MM.YYYY)**

- **What to Enter:** First day of baseline measurement period
- **Minimum Period:**
  - **Tier 1 Systems:** 30 days minimum (45+ days preferred)
  - **Tier 2 Systems:** 14 days minimum (30+ days preferred)
  - **Seasonal Systems:** 90+ days (to capture weekly/monthly cycles)
- **Example:** `01.11.2025`


**Column G: Observation Period - End Date (DD.MM.YYYY)**

- **What to Enter:** Last day of baseline measurement period
- **Example:** `15.12.2025` (45-day observation)
- **Validation:** End Date must be > Start Date


**Column H: Observation Duration (Days)**

- **Auto-Calculated:** `= Column G - Column F`
- **Display:** Number of days
- **Critical Threshold:**
  - ⚠️ <14 days: Baseline may not be statistically valid
  - ✅ 30-90 days: Good baseline period
  - ✅ >90 days: Excellent (captures seasonal variations)


**Column I: Incidents/Anomalies Excluded**

- **What to Enter:** Count and brief description of excluded events
- **Purpose:** Baselines should represent NORMAL behavior, not incident spikes
- **Examples:**
  - `2 incidents excluded: DDoS attack (05.11.2025), planned maintenance spike (10.12.2025)`
  - `1 exclusion: Security scan caused CPU spike (22.11.2025)`
  - `None` (if no incidents during observation period)
- **Critical:** MUST exclude known incidents/anomalies or baseline will be skewed
- **Document:** Which specific dates/times were excluded and why


**Column J: Mean (Average)**

- **What to Enter:** Arithmetic mean of metric during observation period
- **Formula:** `Sum of all values / Count of values`
- **Example:** CPU Mean = 42.3%
- **Units:** Must match metric (%, MB/s, count, etc.)
- **Source:** Calculate from monitoring platform (SIEM, Prometheus, CloudWatch, etc.)


**Column K: Median (50th Percentile)**

- **What to Enter:** Middle value when data sorted (50th percentile)
- **Example:** CPU Median = 41.8%
- **Why Important:** Median less affected by outliers than mean
- **Comparison:** If Median << Mean, you have high outliers skewing average


**Column L: Standard Deviation**

- **What to Enter:** Measure of data spread/variability
- **Interpretation:**
  - Low StdDev (<10% of mean): Stable, predictable behavior
  - High StdDev (>30% of mean): Highly variable, unpredictable
- **Example:** CPU StdDev = 8.2% (relatively stable)
- **Use Case:** Narrow baselines (mean ± 2×StdDev) for stable metrics, wide baselines for variable metrics


**Column M: 95th Percentile**

- **What to Enter:** Value below which 95% of observations fall
- **Example:** CPU 95th percentile = 58.2%
- **Why Important:** Common threshold basis (captures normal spikes, excludes outliers)
- **Interpretation:** 95% of the time, CPU is ≤58.2%


**Column N: 99th Percentile**

- **What to Enter:** Value below which 99% of observations fall
- **Example:** CPU 99th percentile = 68.5%
- **Use Case:** More conservative threshold for critical systems


**Column O: Min Value Observed**

- **What to Enter:** Lowest value seen during observation period
- **Example:** CPU Min = 12%
- **Use Case:** Detect anomalously LOW values (e.g., process crash, service stopped)


**Column P: Max Value Observed**

- **What to Enter:** Highest value seen during observation period
- **Example:** CPU Max = 94%
- **Validation:** Should be close to 99th percentile (if much higher, may indicate excluded incident)


**Column Q: Business Hours Profile (08:00-18:00) - Mean**

- **What to Enter:** Average value during business hours only
- **Example:** CPU Business Hours Mean = 48%
- **Time Definition:** Define organization's business hours (may vary by timezone/region)
- **Why Important:** Many systems have time-aware patterns (busier during workday)


**Column R: Off-Hours Profile (18:00-08:00) - Mean**

- **What to Enter:** Average value outside business hours
- **Example:** CPU Off-Hours Mean = 28%
- **Use Case:** Detect anomalies appropriate to time of day
  - 80% CPU at 2 AM may be suspicious if baseline is 28%
  - 80% CPU at 2 PM may be normal if baseline is 48%


**Column S: Weekend Profile - Mean**

- **What to Enter:** Average value during weekends (Saturday-Sunday)
- **Example:** CPU Weekend Mean = 15%
- **Use Case:** Many corporate systems have lower weekend utilization
- **Note:** If system has no weekend pattern, can leave blank or use same as business hours


**Column T: Alert Threshold (Derived)**

- **What to Enter:** Calculated threshold for alerting on anomalies
- **Common Derivation Methods:**


**Method 1: Percentile-Based (Recommended)**
```
Alert Threshold = 95th Percentile × 1.3
Example: 58.2% × 1.3 = 75.7% → Round to 76%
```
Allows for 5% of normal spikes plus 30% headroom before alerting.

**Method 2: Statistical (Mean + Multiple of StdDev)**
```
Alert Threshold = Mean + (3 × StdDev)
Example: 42.3% + (3 × 8.2%) = 66.9% → Round to 67%
```
Captures 99.7% of normal distribution.

**Method 3: Business Impact-Based**
```
Alert Threshold = Capacity Impact Level
Example: Database CPU >80% causes query slowdown → Threshold = 80%
```
Based on known performance degradation points.

**Document in Column U (Threshold Methodology):** Which method you used and why

**Column U: Threshold Methodology**

- **What to Enter:** Explanation of how threshold was derived
- **Examples:**
  - `95th percentile × 1.3 (allows normal spikes + 30% headroom)`
  - `Mean + 3×StdDev (captures 99.7% of normal behavior)`
  - `80% = known performance impact threshold per vendor guidance`
  - `Time-aware: Business hours = 75%, Off-hours = 50%`
- **Critical:** Auditors will ask "Why this threshold?" - document your reasoning


**Column V: Time-Aware Thresholds?**

- **Options (Dropdown):** Yes, No
- **Select "Yes" if:** Different thresholds for business/off-hours/weekends
- **Document in Column W:** Specific thresholds per time period
- **Example:**
  - Column V = "Yes"
  - Column W = "Business hours: 75%, Off-hours: 50%, Weekends: 40%"


**Column W: Time-Aware Threshold Details**

- **What to Enter:** Specific thresholds for each time period (if Column V = Yes)
- **Format:** `[Period]: [Threshold], [Period]: [Threshold]`
- **Example:** `Business hours (08:00-18:00 Mon-Fri): 75% CPU, Off-hours: 50% CPU, Weekends: 40% CPU`
- **Leave Blank if:** Column V = No (single threshold applies always)


**Column X: Baseline Valid From (DD.MM.YYYY)**

- **What to Enter:** Date this baseline becomes active
- **Typically:** Day after observation period ends
- **Example:** If observation ended 15.12.2025, baseline valid from 16.12.2025


**Column Y: Baseline Valid Until (DD.MM.YYYY)**

- **What to Enter:** Date baseline expires and must be re-established
- **Policy Requirement:**
  - **Tier 1 Systems:** Baseline valid 90 days maximum (quarterly review)
  - **Tier 2 Systems:** Baseline valid 180 days (semi-annual review)
  - **Rapidly Changing Systems:** Monthly review
- **Example:** Valid from 16.12.2025, valid until 15.03.2026 (90 days)
- **Auto-Calc:** `= Column X + 90 days` (for Tier 1)


**Column Z: Next Review Date (DD.MM.YYYY)**

- **What to Enter:** When baseline will be re-measured
- **Typically:** Same as "Valid Until" date
- **Trigger Review Early if:**
  - Major system changes (hardware upgrade, software migration)
  - Significant business changes (new product launch, workload shifts)
  - Detection effectiveness degrading (high false positives)


**Column AA: Baseline Owner**

- **What to Enter:** Person responsible for maintaining this baseline
- **Examples:**
  - `John Smith, Senior SOC Analyst`
  - `Database Team (DBA-Team@company.com)`
  - `Network Operations Center (NOC)`
- **Responsibility:** Update baseline when it expires, tune thresholds if needed


**Column AB: Detection Rule IDs Using This Baseline**

- **What to Enter:** Which detection rules depend on this baseline
- **Format:** Comma-separated rule IDs (reference Sheet 5)
- **Example:** `DET-001, DET-005, DET-023`
- **Purpose:** Understand impact if baseline changes (which alerts will be affected)
- **Cross-Reference:** These rule IDs should exist in Sheet 5 (Detection Rule Coverage)


**Column AC: Notes**

- **What to Enter:** Additional context, special considerations, known issues
- **Use Cases:**
  - **Seasonal Patterns:** "Baseline varies significantly in December (holiday shopping season)"
  - **Known Limitations:** "Baseline based on 30 days only (minimum) - recommend re-baseline with 60-90 days for better accuracy"
  - **System Changes:** "Baseline established before RAM upgrade (16GB→32GB) - may need adjustment"
  - **Data Quality:** "5% of data missing due to monitoring agent outage (05-07.11.2025) - excluded from baseline"


### Completing Sheet 2: Step-by-Step Process

**Step 1: Select Systems for Baseline (30-60 minutes)**

**Priority Order:**
1. **Tier 1 (Critical) Systems:** ALL must have baselines
2. **High False Positive Systems:** Systems generating alert noise (need better thresholds)
3. **Tier 2 (High) Systems:** Baseline >80%
4. **Anomaly-Prone Systems:** Systems with frequent unexplained behavior

**Start Small:** Begin with 5-10 critical systems, expand over time.

**Step 2: Extract Historical Data (1-2 hours)**

**For each system, extract metrics from monitoring platform:**

**Splunk Example:**
```spl
index=metrics host="SRV-DC-01" metric_name="cpu.percent"
earliest=-45d latest=now
| stats avg(value) as mean, median(value) as median, stdev(value) as stddev,
        perc95(value) as p95, perc99(value) as p99,
        min(value) as min, max(value) as max
```

**Prometheus Example:**
```promql
avg_over_time(node_cpu_seconds_total{instance="srv-dc-01"}[45d])
```

**CloudWatch Example:**
```aws cli
aws cloudwatch get-metric-statistics   --namespace AWS/EC2   --metric-name CPUUtilization   --dimensions Name=InstanceId,Value=i-0123456789   --start-time 2025-11-01T00:00:00Z   --end-time 2025-12-15T23:59:59Z   --period 300   --statistics Average,Minimum,Maximum
```

**Export to CSV/Excel for analysis.**

**Step 3: Calculate Statistical Profile (30-60 minutes per system)**

**Using Excel/Python/R:**

1. **Load time-series data** (timestamp, value)
2. **Exclude incidents:**

   - Filter out known incident dates/times
   - Remove outliers >3×StdDev (but document why)

3. **Calculate statistics:**

   - Mean: `=AVERAGE(data_range)`
   - Median: `=MEDIAN(data_range)`
   - StdDev: `=STDEV.P(data_range)`
   - 95th Percentile: `=PERCENTILE(data_range, 0.95)`
   - 99th Percentile: `=PERCENTILE(data_range, 0.99)`


**Step 4: Calculate Time-Aware Profiles (30 minutes per system)**

**Split data by time period:**

**Business Hours (08:00-18:00, Mon-Fri):**
```excel
=AVERAGEIFS(value_range, timestamp_range, ">=08:00", timestamp_range, "<=18:00", 
            weekday_range, "<6")
```

**Off-Hours (18:00-08:00, Mon-Fri):**
```excel
=AVERAGEIFS(value_range, timestamp_range, "<08:00" OR timestamp_range, ">18:00",
            weekday_range, "<6")
```

**Weekends (Sat-Sun, all day):**
```excel
=AVERAGEIFS(value_range, weekday_range, ">=6")
```

**Step 5: Derive Alert Thresholds (15-30 minutes per system)**

**Choose derivation method:**

**For Stable Systems (Low StdDev):**

- Use percentile method: `95th Percentile × 1.3`
- Results in tight thresholds (good for detecting small anomalies)


**For Variable Systems (High StdDev):**

- Use statistical method: `Mean + 3×StdDev`
- Results in wider thresholds (reduces false positives)


**For Systems with Known Impact:**

- Use business impact method: Set threshold at known degradation point
- Example: Database slows at 80% CPU → Threshold = 80%


**Document methodology in Column U.**

**Step 6: Implement Time-Aware Thresholds (if applicable)**

**Decision Criteria:**

- **If** Business Hours Mean vs Off-Hours Mean differ by >30% → Use time-aware thresholds
- **If** System shows clear weekly pattern → Use time-aware thresholds
- **If** System behavior stable across all times → Single threshold sufficient


**Example Implementation in SIEM:**
```spl
| eval alert_threshold = case(
    (date_hour >= 8 AND date_hour < 18 AND date_wday < 6), 75,  // Business hours
    (date_hour < 8 OR date_hour >= 18) AND date_wday < 6, 50,    // Off-hours weekday
    date_wday >= 6, 40)                                           // Weekend
| where cpu_percent > alert_threshold
```

**Step 7: Validate Baseline (1-2 hours)**

**Validation Checks:**

1. **Sanity Check:** Do statistics make sense?

   - Mean between Min and Max? ✓
   - 95th Percentile < 99th Percentile < Max? ✓
   - StdDev reasonable for metric type? ✓


2. **Time-Pattern Check:** Graph data over time

   - Are there clear daily/weekly patterns? → Time-aware thresholds needed
   - Are there trend lines (growing/shrinking over time)? → Note for next baseline review


3. **Incident Exclusion Check:**

   - Max value significantly higher than 99th percentile? → May have missed incident exclusion
   - Re-review observation period for anomalies


4. **Threshold Reasonableness:**

   - Alert threshold achievable? (not set at 100% where system can't reach)
   - Alert threshold not too sensitive? (would it fire constantly in production?)
   - Test threshold against last 7 days of data - how many alerts would it generate?


**Step 8: Document and Implement (30 minutes per system)**

1. **Fill Sheet 2** with all calculated values
2. **Create detection rules** in SIEM using derived thresholds (document rule IDs in Column AB)
3. **Store baseline calculations** as evidence (Sheet 8)
4. **Set calendar reminders** for baseline review (Column Z - Next Review Date)

### Critical Success Factors for Sheet 2

**You've Done This Right When:**
1. ✅ Every Tier 1 system has documented baseline with 30+ days observation
2. ✅ Statistical profiles calculated from actual data (not estimated)
3. ✅ Incidents/anomalies excluded from baseline period (documented)
4. ✅ Alert thresholds derived using documented methodology (not arbitrary)
5. ✅ Time-aware thresholds implemented where behavioral patterns exist
6. ✅ Baseline validity period and review dates set
7. ✅ Detection rules created and tied to baselines (Column AB populated)

**You're Fooling Yourself If:**

- ❌ Baselines are estimates ("CPU normally around 40-60%")
- ❌ Observation period <14 days (insufficient data)
- ❌ Incidents NOT excluded from baseline (skewed by attack spikes)
- ❌ Thresholds are arbitrary ("80% seems reasonable")
- ❌ Same threshold used 24/7 despite clear time patterns
- ❌ Baselines never reviewed/updated (set once, forgotten)


**Remember Feynman:** Show the data. Show the calculations. Show your work. If you can't explain WHY a threshold is set at 75%, you're guessing.

---

## Sheet 3: Access Pattern Baselines

**Purpose:** Document measured baselines for access patterns (authentication, privileged access, geographic access)

**Policy Reference:** ISMS-POL-A.8.16, Section 2.2.2 (Access Pattern Baselines)

**Why This Sheet Matters:**
Access anomalies are often early indicators of compromise:

- User logs in from impossible geographic locations (credential theft)
- Privileged access outside normal hours (insider threat, compromised admin)
- Authentication rate spikes (brute force attack)


But you can only detect "anomalous" if you know what "normal" looks like → baselines required.

**Structure:**

- **Rows 8-32:** 25 data entry rows (access pattern baselines)
- **Rows 35-50:** Access pattern analysis summary


### Column-by-Column Completion Guide

**Column A: User/Group/System ID**

- **What to Enter:** Identity being baselined
- **Examples:**
  - User: `jsmith`, `john.smith@company.com`
  - Group: `Domain Admins`, `Database Administrators`, `VPN Users`
  - Service Account: `svc_backup`, `app_api_account`
  - System: `APP-WEB-01` (for system-to-system authentication)
- **Focus Areas:**
  - **Privileged Users:** ALL admin accounts must have baselines
  - **High-Value Targets:** Executives, Finance, HR, IT admins
  - **Service Accounts:** Automated access patterns should be VERY consistent
  - **Generic Accounts:** Shared accounts (if they exist - note these are red flags)


**Column B: Identity Type (Dropdown)**

- **Options:** Individual User, Service Account, System Account, Group, Shared Account
- **Selection:**
  - **Individual User:** Personal account (john.smith)
  - **Service Account:** Application/automation account (svc_backup)
  - **System Account:** Computer/device account (APP-WEB-01$)
  - **Group:** Baseline for collective (all VPN users combined)
  - **Shared Account:** Multiple people using same creds (⚠️ security risk - should be eliminated)


**Column C: Access Type (Dropdown)**

- **Options:** Authentication (Login), Privileged Access (sudo/runas), Geographic Access, Remote Access (VPN), Resource Access (File/DB)
- **Purpose:** Different access types have different baseline patterns
- **Examples:**
  - **Authentication:** User login frequency, timing, source systems
  - **Privileged Access:** Admin commands, privilege escalation events
  - **Geographic:** Login locations (country, city, IP ranges)
  - **Remote Access:** VPN connections (when, from where, how often)
  - **Resource Access:** File access patterns, database queries


**Column D: Pattern Metric**

- **What to Enter:** Measurable metric defining normal access pattern
- **Examples:**
  - Authentication: `Logins per day`, `Logins per hour (business hours)`
  - Privileged Access: `Sudo commands per week`, `Admin sessions per day`
  - Geographic: `Login countries`, `Login IP ranges`
  - Timing: `Typical login hours (07:00-17:00 Mon-Fri)`
  - Remote Access: `VPN sessions per week`, `VPN duration (hours)`
  - Resource Access: `Files accessed per day`, `DB queries per hour`


**Column E: Observation Period (Start - End)**

- **Format:** `DD.MM.YYYY - DD.MM.YYYY`
- **Minimum Period:**
  - **Privileged Users:** 30 days (45+ preferred)
  - **Regular Users:** 14 days (30+ preferred)
  - **Service Accounts:** 14 days minimum (these should be VERY consistent)
- **Example:** `01.11.2025 - 15.12.2025 (45 days)`


**Column F: Statistical Profile - Mean**

- **What to Enter:** Average value for the metric
- **Examples:**
  - Mean logins per day: 2.3
  - Mean privileged access per week: 15
  - Mean files accessed per day: 45


**Column G: Statistical Profile - Median**

- **Example:** Median logins per day: 2.0


**Column H: Statistical Profile - Std Dev**

- **Interpretation:**
  - **Service Account StdDev should be LOW** (very consistent behavior)
  - **User StdDev may be MODERATE** (some day-to-day variation expected)
  - **High StdDev** may indicate irregular patterns (need investigation)


**Column I: Statistical Profile - Min/Max**

- **Format:** `Min / Max`
- **Example:** `0 / 8` (minimum 0 logins per day, maximum 8 logins per day)
- **Use Case:** Detect when user exceeds historical maximum (possible account compromise)


**Column J: Time-Aware Pattern - Typical Days/Hours**

- **What to Enter:** When access typically occurs
- **Examples:**
  - `Monday-Friday, 07:00-17:00 CET` (standard office hours)
  - `Monday-Friday, 06:00-22:00` (user works extended hours)
  - `24/7` (service account, always-on system)
  - `Saturday 02:00-04:00` (batch job runs weekends only)
  - `Monthly: Last Friday, 18:00-22:00` (month-end processing)
- **Purpose:** Detect access OUTSIDE typical pattern (e.g., login at 3 AM when user normally 08:00-17:00)


**Column K: Time-Aware Pattern - Business Hours Profile**

- **What to Enter:** Access behavior during business hours
- **Example:** `Mean 2.5 logins/day, 95th percentile: 4 logins`


**Column L: Time-Aware Pattern - Off-Hours Profile**

- **What to Enter:** Access behavior outside business hours
- **Example:** `Mean 0.1 logins/day (rare), Max observed: 2 (documented exceptions: on-call incidents)`
- **Detection Rule:** If off-hours access exceeds historical max + margin → Alert


**Column M: Geographic Pattern - Typical Locations**

- **What to Enter:** Where access normally originates
- **Examples:**
  - `Switzerland (Zurich office - IP range 203.0.113.0/24)`
  - `Switzerland, Germany (remote workers)`
  - `AWS eu-central-1 (Frankfurt datacenter - service account)`
  - `Multiple: Zurich office (70%), Home VPN (25%), Munich office (5%)`
- **Purpose:** Detect impossible travel (login from Zurich at 09:00, then Tokyo at 09:15)


**Column N: Geographic Pattern - Allowed Countries**

- **What to Enter:** Countries where login is expected (whitelist approach)
- **Format:** Comma-separated country codes
- **Example:** `CH, DE, AT, FR` (Switzerland, Germany, Austria, France - European employees)
- **Detection Rule:** Login from country NOT in this list → Alert (potential credential compromise)


**Column O: Remote Access Pattern (If Applicable)**

- **What to Enter:** VPN/remote access baseline
- **Examples:**
  - `VPN sessions: 3-5 per week, typical duration 6-8 hours`
  - `No VPN access (office-only user)`
  - `Always VPN (remote worker)`
- **Anomaly Example:** User with "No VPN access" suddenly connects via VPN → Investigate


**Column P: Privileged Access Pattern (If Applicable)**

- **What to Enter:** Admin/elevated access baseline (for privileged users only)
- **Examples:**
  - `Sudo commands: 10-20 per day (system admin)`
  - `Database admin queries: 5-15 per week`
  - `AD admin tasks: 2-3 per week (user account management)`
- **Critical Detection:** Privileged access from regular user account → High-severity alert


**Column Q: Alert Threshold Derived**

- **What to Enter:** Threshold for detecting anomalous access
- **Examples:**
  - `>6 logins per day` (95th percentile × 1.5)
  - `Login outside 06:00-22:00 window`
  - `Login from country not in CH/DE/AT/FR`
  - `>3 failed login attempts per hour` (brute force detection)
  - `VPN session from new device not seen before`


**Column R: Threshold Methodology**

- **What to Enter:** How threshold was derived
- **Examples:**
  - `95th percentile × 1.5 (statistical)`
  - `Outside typical time window (time-based)`
  - `Country not in whitelist (geographic)`
  - `Exceeds historical maximum (max-based)`


**Column S: Known Exceptions**

- **What to Enter:** Legitimate reasons for baseline deviation
- **Examples:**
  - `User travels to US quarterly for business (logins from US expected)`
  - `On-call rotation: Off-hours access expected 1 week per month`
  - `Month-end processing: File access spikes last 3 days of month`
  - `VPN from home during COVID pandemic (geo location varies)`
- **Purpose:** Reduce false positives by documenting expected exceptions


**Column T: Baseline Valid From/Until**

- **Format:** `DD.MM.YYYY - DD.MM.YYYY`
- **Validity Period:**
  - **Privileged Users:** 90 days (quarterly review)
  - **Regular Users:** 180 days (semi-annual review)
  - **Service Accounts:** 30 days (should be VERY stable - if pattern changes, investigate immediately)


**Column U: Next Review Date**

- **When:** Date to re-establish baseline
- **Triggers for Early Review:**
  - User role change (promotion, department transfer)
  - Access pattern significantly changes (remote worker becomes office-based)
  - High false positive rate (threshold too sensitive)


**Column V: Baseline Owner**

- **Who:** Person responsible for maintaining this access baseline
- **Examples:**
  - `SOC Team (for general user baselines)`
  - `Identity & Access Management Team (for privileged accounts)`
  - `Database Team (for DBA access patterns)`


**Column W: Detection Rule IDs**

- **What to Enter:** Which detection rules use this baseline
- **Example:** `DET-AUTH-001 (Excessive logins), DET-AUTH-005 (Off-hours access), DET-GEO-001 (Impossible travel)`
- **Cross-Reference:** These rule IDs should exist in Sheet 5


**Column X: Notes**

- **Use Cases:**
  - **Behavioral Changes:** "User baseline changed significantly after promotion to manager role (more meetings, less deep work)"
  - **Data Quality:** "VPN logs missing for 7 days due to system outage - baseline may be incomplete"
  - **Exceptions:** "User on sabbatical 01.01-31.01.2026 - no access expected during this period"


### Completing Sheet 3: Key Scenarios

**Scenario 1: Individual User - Standard Office Worker**
```
User ID: jsmith
Identity Type: Individual User
Access Type: Authentication (Login)
Pattern Metric: Logins per day
Observation: 01.11.2025 - 15.12.2025 (45 days)
Statistical Profile: Mean 2.1, Median 2.0, StdDev 0.8, Min 0, Max 4
Time Pattern: Mon-Fri 07:30-17:00 CET
Business Hours: Mean 2.1 logins/day
Off-Hours: Mean 0.05 logins/day (rare, only 2 instances in 45 days during on-call)
Geographic: Switzerland (Zurich office - 95%), Home VPN (5%)
Allowed Countries: CH
Alert Threshold: >5 logins/day OR login outside 06:00-19:00 OR login from non-CH country
Known Exceptions: None
```

**Scenario 2: Privileged User - System Administrator**
```
User ID: admin_jdoe
Identity Type: Individual User
Access Type: Privileged Access (sudo)
Pattern Metric: Sudo commands per day
Observation: 01.11.2025 - 15.12.2025 (45 days)
Statistical Profile: Mean 18, Median 16, StdDev 6, Min 5, Max 35
Time Pattern: Mon-Fri 08:00-18:00 (occasionally off-hours for on-call)
Business Hours: Mean 18 sudo/day
Off-Hours: Mean 3 sudo/day (on-call incidents)
Geographic: Switzerland (Zurich office - 80%), Home VPN (20%)
Allowed Countries: CH
Alert Threshold: >40 sudo/day OR privileged access from non-admin terminal OR geo location outside CH
Known Exceptions: On-call week 1 per month (higher off-hours activity expected)
```

**Scenario 3: Service Account - Backup Job**
```
User ID: svc_backup
Identity Type: Service Account
Access Type: Resource Access (File)
Pattern Metric: Files accessed per day
Observation: 01.11.2025 - 15.12.2025 (45 days)
Statistical Profile: Mean 15,234, Median 15,198, StdDev 421, Min 14,500, Max 16,100
Time Pattern: Daily 01:00-04:00 (automated backup window)
Geographic: Zurich Datacenter (single server 10.0.5.20)
Allowed Countries: CH (internal only)
Alert Threshold: Access outside 00:30-04:30 window OR files >20,000 OR files <10,000 OR source IP != 10.0.5.20
Known Exceptions: None (service account should be 100% consistent)
```

**Detection Rule for Service Account:**
```spl
index=file_access account="svc_backup"
| where (date_hour < 0 OR date_hour > 4) OR count > 20000 OR count < 10000 OR src_ip != "10.0.5.20"
| alert High "Service account accessing files outside normal pattern - possible compromise"
```

**Scenario 4: Detecting Impossible Travel**
```
User ID: jsmith
Login 1: 09:00 CET from Zurich, Switzerland (IP 203.0.113.50)
Login 2: 09:15 CET from Tokyo, Japan (IP 198.51.100.20)

Geographic Baseline: Switzerland only
Alert: "Impossible travel detected - 9,000 km in 15 minutes"
Status: CRITICAL - investigate immediately (likely credential theft)
```

### Critical Success Factors for Sheet 3

**You've Done This Right When:**
1. ✅ ALL privileged accounts (admins, DBAs) have documented baselines
2. ✅ Service accounts have VERY consistent baselines (low StdDev)
3. ✅ Geographic patterns documented (can detect impossible travel)
4. ✅ Time-aware patterns captured (can detect off-hours anomalies)
5. ✅ Known exceptions documented (reduces false positives)
6. ✅ Detection rules created and operational (Column W populated)

**You're Fooling Yourself If:**

- ❌ "Users log in 2-3 times per day" (vague, no data)
- ❌ Service account baseline has high StdDev (should be VERY consistent)
- ❌ No geographic baseline (can't detect credential theft from foreign country)
- ❌ Same threshold 24/7 (ignoring clear time patterns)
- ❌ Detection rules not implemented (baseline documentation without detection = useless)


---



**Purpose:** Document CPU, memory, disk, network baselines for critical systems

**Key Columns:**

- System Name, System Type, Criticality Tier
- Metric Name (CPU %, Memory %, Disk I/O MB/s, Network MB/s)
- Observation Period (start date, end date, duration, exclusions)
- Statistical Profile (mean, median, std dev, 95th %ile, 99th %ile)
- Time-Aware Profiles (business hours, off-hours, weekends)
- Alert Threshold (derived value, methodology documented)
- Baseline Validity Period, Next Review Date, Owner


## Sheet 3: Access Pattern Baselines

**Purpose:** Document user authentication, privileged access, geographic access baselines

**Key Columns:**

- User/Group/System, Access Type (authentication, privileged, geographic)
- Pattern Metric (logins/hour, timing window, location list)
- Statistical Profile, Time-Aware Baselines, Alert Threshold


## Sheet 4: Application Behavior Baselines

**Purpose:** Document transaction, API, database, file access, network baselines

**Key Columns:**

- Application Name, Baseline Category (transactions, API, database, file, network)
- Behavior Metric (transactions/min, API calls/min, queries/min, files/day, connections/hour)
- Statistical Profile, Alert Threshold


## Sheet 5: Detection Rule Coverage

**Purpose:** Inventory detection rules, map MITRE ATT&CK coverage, identify gaps

**Key Columns:**

- Rule ID, Rule Name, Rule Type (signature, anomaly, behavioral, correlation)
- MITRE ATT&CK Tactic, MITRE ATT&CK Technique ID
- Coverage Status (Covered, Partial, Not Covered)
- Severity, Status (Active, Disabled, Testing)


**MITRE ATT&CK Coverage Matrix:**

- Reconnaissance: [X rules cover / Y total techniques] = Z% coverage
- Initial Access: [coverage %]
- Execution: [coverage %]
- Persistence: [coverage %]
- Privilege Escalation: [coverage %]
- Defense Evasion: [coverage %]
- Credential Access: [coverage %]
- Discovery: [coverage %]
- Lateral Movement: [coverage %]
- Collection: [coverage %]
- Exfiltration: [coverage %]
- Command and Control: [coverage %]
- Impact: [coverage %]


## Sheet 6: Detection Effectiveness Metrics

**Purpose:** Measure detection effectiveness through testing and operational data

**Key Columns:**

- Detection Rule ID/Name
- Test Date, Test Type (simulated attack, purple team, production incident)
- Attack Technique Tested (MITRE ATT&CK ID)
- Detection Result (Detected/Missed)
- Alert Latency (time from attack to alert)
- False Positive Count (last 30 days)
- True Positive Rate, False Positive Rate, False Negative Rate


**Effectiveness Summary:**

- Overall Detection Rate: (Total Detected / Total Attacks) × 100
- Target: >90% for Critical/High severity threats
- Current: [calculated from test results]
- Gap: [target - current]

- Overall False Positive Rate: (False Alerts / Total Alerts) × 100
- Target: <20% for Critical alerts, <30% for High alerts
- Current: [calculated from alert data]
- Gap: [current - target if exceeds]

- Mean Time to Detect (MTTD): Average time from attack start to alert
- Target: <1 hour for Critical, <4 hours for High
- Current: [measured from tests + incidents]
- Gap: [current - target if exceeds]


---

# Evidence Collection

[Similar structure to A.8.16.1 - adapted for baseline/detection focus]

**Evidence Types Required:**

1. **Baseline Documentation**

   - Statistical profiles (Excel files with calculations)
   - Baseline templates (using ISMS-POL-A.8.16, Annex B)
   - Time-series graphs showing behavior patterns
   - Threshold derivation documentation


2. **Detection Rule Evidence**

   - SIEM rule exports (configuration files, screenshots)
   - MITRE ATT&CK coverage matrix
   - Rule descriptions and logic
   - Rule change history (tuning log)


3. **Effectiveness Test Results**

   - Test plans (which techniques tested)
   - Test logs (attack execution, alert generation)
   - Detection results (TP, FP, FN counts)
   - MTTD measurements per test


4. **Tuning Evidence**

   - False positive trends (before/after tuning)
   - Tuning decisions (why rule was modified)
   - Alert volume trends (improving or degrading)


---

# Common Pitfalls

## Pitfall 1: The "Gut Feel" Baseline

**Mistake:** Describing baselines qualitatively without numbers

**Example:**

- ❌ "Users normally log in around 9 AM"
- ❌ "Database is busy during business hours"
- ❌ "Web server handles moderate traffic"


**Why It's Wrong:**

- Not measurable (what's "around 9 AM"? 8:30-9:30? 9:00 exactly?)
- Not actionable (when do you alert? What's "busy" vs. "too busy"?)
- Not auditable (auditor asks: "Show me the baseline." You: "Uh... it's in my head?")


**How to Fix:**

- ✅ "User authentication: Mean 145 logins/hour (08:00-10:00), std dev 23, alert threshold 245/hour"
- ✅ "Database queries: Baseline 450 queries/min, 95th %ile 523, alert threshold 680 queries/min"
- ✅ "Web server requests: Mean 850 req/min, 95th %ile 1200, alert threshold 1560 req/min"


**Prevention:** If you can't write it with numbers, it's not a baseline.

## Pitfall 2: Confusing Detection Rules with Detection Effectiveness

**Mistake:** "We have 500 detection rules, therefore we're detecting threats"

**Why It's Wrong:**

- Quantity ≠ Quality (500 rules with 90% false positives = noise, not detection)
- No measurement of what's detected vs. missed
- No validation that rules actually work


**How to Fix:**

- Test sample of rules (simulate attacks, verify detection)
- Measure true positive rate (what % of attacks are caught?)
- Measure false positive rate (what % of alerts are noise?)
- Track Mean Time to Detect (MTTD) - how long to detect attacks?


**Example:**

- Organization had 800 detection rules
- Effectiveness testing revealed:
  - Only 40% of rules had generated any alerts in last 6 months (dead rules)
  - 30% had >50% false positive rate (noise generators)
  - 20% were actually effective (high TP rate, low FP rate)
  - 10% were unknown effectiveness (no testing data)
- After cleanup: 200 tuned rules with 75% avg TP rate, 15% avg FP rate


**Prevention:** Measure effectiveness, not just rule count.

## Pitfall 3: Static Baselines That Never Update

**Mistake:** Establish baselines once, never review or update

**Why It's Wrong:**

- Business changes (new users, new applications, infrastructure growth)
- Baselines become outdated (alert on normal behavior = false positives)
- Attacks become normalized (attacker activity included in "normal" baseline)


**How to Fix:**

- Review baselines quarterly (minimum)
- Update baselines when significant changes occur:
  - Infrastructure changes (migration, scaling)
  - Business process changes (new workflows, organizational restructuring)
  - Persistent deviations (sustained shift in normal behavior)
- Document baseline version history (track changes over time)


**Example:**

- Baseline established: Q1 2025 (100 users, 5000 events/day)
- Company doubled in size: Q3 2025 (200 users, 12000 events/day)
- Baseline not updated → Every day generated alerts (exceeded Q1 baseline)
- SOC fatigued, started ignoring alerts (dangerous!)
- Fix: Updated baseline Q4 2025, alerts returned to normal


**Prevention:** Set calendar reminders for quarterly baseline review.

## Pitfall 4: Ignoring Time-Aware Patterns

**Mistake:** Single baseline for all time periods (business hours, off-hours, weekends)

**Why It's Wrong:**

- Different behavior patterns:
  - Business hours: High activity (users working, applications busy)
  - Off-hours: Low activity (batch jobs, automated processes)
  - Weekends: Minimal activity (no users, only automated systems)
- Single baseline either:
  - Too permissive (misses off-hours attacks)
  - Too strict (false positives during business hours)


**How to Fix:**

- Create time-aware baselines:
  - Business hours (08:00-18:00 Mon-Fri): Mean 145, 95th %ile 189
  - Off-hours (18:00-08:00 Mon-Fri): Mean 12, 95th %ile 25
  - Weekends (Sat-Sun): Mean 8, 95th %ile 18
- Alert thresholds adjust based on time of day/week
- Attackers often operate off-hours (less likely to be noticed) - time-aware detection is critical


**Example:**

- Domain Controller authentication baseline (single, time-unaware):
  - Mean across 24/7: 65 logins/hour
  - Alert threshold: 100 logins/hour
  - Problem: Attacker at 3 AM with 50 logins = no alert (below threshold)
  - But 50 logins at 3 AM is 10× normal off-hours rate!

- Domain Controller authentication baseline (time-aware):
  - Business hours: Mean 145, alert threshold 245
  - Off-hours: Mean 5, alert threshold 15
  - Attacker at 3 AM with 50 logins = ALERT (far exceeds off-hours threshold of 15)


**Prevention:** Always separate business hours, off-hours, and weekend baselines.

## Pitfall 5: No Exclusion of Incidents from Baselines

**Mistake:** Include security incident periods in baseline observation

**Why It's Wrong:**

- Baselines should represent NORMAL behavior
- Security incidents are ANOMALIES (attacks, breaches, malware)
- Including incidents in baseline normalizes attack behavior
- Result: Attacks become "baseline" - detection rules won't trigger


**Example:**

- Baseline observation: 01.11.2025 - 31.12.2025 (60 days)
- Security incident: 15.12.2025 (ransomware, 10,000 file modifications/hour vs. normal 50/hour)
- If incident included in baseline:
  - Mean file modifications: 200/hour (contaminated by incident)
  - Alert threshold: 300/hour
  - Future ransomware at 10,000/hour triggers alert ✅
  - But "low and slow" ransomware at 250/hour does NOT trigger alert ❌ (below contaminated threshold)

- If incident excluded from baseline:
  - Mean file modifications: 50/hour (clean baseline)
  - Alert threshold: 100/hour
  - Both fast ransomware (10,000/hour) AND slow ransomware (250/hour) trigger alerts ✅


**How to Fix:**
1. Review incident history during baseline observation period
2. Identify incident dates/times and affected systems
3. Exclude incident periods from baseline calculation
4. Document exclusions (dates, reason, systems affected)

**Prevention:** Always cross-reference incident history before finalizing baselines.

[Additional pitfalls 6-10 in full document]

---

# Quality Checklist

**Baseline Quality:**

- [ ] All baselines have statistical profiles (mean, median, std dev, percentiles)
- [ ] No baselines use vague language ("around", "usually", "seems")
- [ ] Observation periods are ≥30 days (45-60 days preferred)
- [ ] Time-aware baselines created for systems with varying behavior patterns
- [ ] Incidents excluded from observation periods (documented)
- [ ] Thresholds derived with documented methodology (not guessed)
- [ ] Baseline validity periods and review dates documented


**Detection Rule Quality:**

- [ ] All active detection rules catalogued (rule ID, name, description)
- [ ] MITRE ATT&CK coverage mapped (tactics/techniques covered)
- [ ] Coverage gaps identified (tactics with no detection)
- [ ] High-priority gaps prioritized for remediation


**Effectiveness Measurement:**

- [ ] Sample of rules tested (not just assumed to work)
- [ ] True positive rate measured (not estimated)
- [ ] False positive rate measured from actual alert data
- [ ] MTTD measured for tested rules
- [ ] Target metrics defined (>90% TP rate, <20% FP rate, <1hr MTTD)


**Evidence Completeness:**

- [ ] Baseline documentation in standardized format (Annex B template)
- [ ] Detection rule exports collected
- [ ] Test results documented (attack simulations, detection results)
- [ ] Evidence Register complete with all evidence IDs and locations


---

# Review & Approval

[Same three-level approval process as A.8.16.1]

**Level 1: Technical Review (Detection Engineering / SOC Lead)**

- Validate statistical methodology
- Verify baselines are measurable
- Confirm detection rules are correctly mapped to MITRE ATT&CK
- Review effectiveness test results


**Level 2: Compliance Review (Security Manager / CISO)**

- Verify compliance with ISMS-POL-A.8.16, Section 2.2 requirements
- Assess risk of coverage gaps
- Validate remediation plans for gaps
- Approve tuning priorities


**Level 3: Executive Approval (CISO / CIO)**

- Accept residual risk from detection gaps
- Approve budget for remediation (new detection rules, tuning effort, testing)
- Approve quarterly baseline review commitment


---

# PART II: TECHNICAL SPECIFICATION

# Workbook Structure

**Filename:** `ISMS_A_8_16_2_Baseline_Detection_Assessment_YYYYMMDD.xlsx`
**Generator Script:** `generate_a816_2_baseline_detection.py`
**Total Sheets:** 9

## Sheet Overview

| Sheet # | Name | Purpose | Data Rows | Auto-Calc |
|---------|------|---------|-----------|-----------|
| 1 | Instructions & Legend | Workbook overview, color coding | 3 | Yes |
| 2 | 1. Baseline Inventory | System/user/application baseline definitions | 50 | Yes |
| 3 | 2. Detection Rules | Detection rule inventory and configuration | 50 | Yes |
| 4 | 3. MITRE ATT&CK Coverage | Attack technique coverage matrix | 30 | Yes |
| 5 | 4. Rule Performance | Detection rule effectiveness metrics | 30 | Yes |
| 6 | 5. Testing Validation | Detection testing and validation results | 20 | Yes |
| 7 | Summary Dashboard | Consolidated baseline/detection maturity | 0 | Yes |
| 8 | Evidence Register | Evidence tracking | 50 | No |
| 9 | Approval Sign-Off | Approval workflow | 3 | No |

# Sheet 2: System Utilization Baselines - Technical Spec

**Column Definitions:**

| Col | Header | Width | Type | Validation |
|-----|--------|-------|------|------------|
| A | System Name | 30 | Text | Reference ISMS-IMP-A.8.16.1 Sheet 3 |
| B | System Type | 20 | Dropdown | Server, Network Device, Security Appliance, Cloud Infrastructure |
| C | Criticality Tier | 15 | Dropdown | Tier 1 - Critical, Tier 2 - Standard, Tier 3 - Low |
| D | Metric Name | 25 | Dropdown | CPU Utilization %, Memory Utilization %, Disk I/O (MB/s), Network Bandwidth (MB/s), Process Count, Connection Count |
| E | Observation Start Date | 15 | Date | DD.MM.YYYY |
| F | Observation End Date | 15 | Date | DD.MM.YYYY |
| G | Observation Duration (Days) | 12 | Formula | =F-E |
| H | Exclusions (Incident Dates) | 25 | Text | Comma-separated dates |
| I | Mean (Average) | 12 | Number | ≥0 |
| J | Median (50th %ile) | 12 | Number | ≥0 |
| K | Std Deviation (σ) | 12 | Number | ≥0 |
| L | 95th Percentile | 12 | Number | ≥0 |
| M | 99th Percentile | 12 | Number | ≥0 |
| N | Time Context | 18 | Dropdown | All Hours, Business Hours, Off-Hours, Weekends |
| O | Alert Threshold | 12 | Number | >Mean |
| P | Threshold Methodology | 30 | Dropdown | 95th %ile × 1.3, Mean + 3σ, 99th %ile × 1.2, Other (explain in Notes) |
| Q | Baseline Valid From | 15 | Date | DD.MM.YYYY |
| R | Baseline Valid Until | 15 | Date | DD.MM.YYYY |
| S | Next Review Date | 15 | Date | DD.MM.YYYY |
| T | Owner | 25 | Text | Name, Role |
| U | Baseline Status | 15 | Dropdown | ✅ Active, ⚠️ Needs Review, ❌ Expired, 📋 Draft |
| V | Notes | 35 | Text | None |

**Conditional Formatting:**

- Baseline Status "❌ Expired": Red fill, bold text
- Observation Duration <30 days: Yellow fill (warning - insufficient observation)
- Alert Threshold ≤ Mean: Red fill (ERROR - threshold must exceed mean)


# Sheet 5: Detection Rule Coverage - Technical Spec

**Column Definitions:**

| Col | Header | Width | Type | Validation |
|-----|--------|-------|------|------------|
| A | Rule ID | 20 | Text | Unique identifier |
| B | Rule Name | 35 | Text | Descriptive name |
| C | Rule Type | 18 | Dropdown | Signature-Based, Anomaly-Based, Behavioral, Correlation, Threshold |
| D | Description | 40 | Text | What attack/behavior detected |
| E | MITRE Tactic | 20 | Dropdown | Reconnaissance, Initial Access, Execution, Persistence, Privilege Escalation, Defense Evasion, Credential Access, Discovery, Lateral Movement, Collection, Exfiltration, Command & Control, Impact |
| F | MITRE Technique ID | 15 | Text | Format: T#### |
| G | Severity | 12 | Dropdown | Critical, High, Medium, Low, Informational |
| H | Status | 15 | Dropdown | ✅ Active, 🔧 Testing, ⏸️ Disabled, 🗑️ Deprecated |
| I | Last Triggered Date | 15 | Date | DD.MM.YYYY |
| J | Alert Count (30d) | 12 | Number | ≥0 |
| K | False Positive Rate | 12 | Percentage | 0-100% |
| L | Coverage Status | 15 | Formula | =IF(H="✅ Active","✅ Covered","⚠️ Not Covered") |
| M | Notes | 30 | Text | Tuning notes, exceptions |

**MITRE ATT&CK Coverage Summary (Auto-Calculated):**
```excel
For each Tactic (Reconnaissance, Initial Access, etc.):

- Total Techniques in Tactic: [from MITRE framework]
- Techniques Covered: =COUNTIFS(TacticColumn,"Reconnaissance",StatusColumn,"✅ Active")
- Coverage %: =(Covered / Total) × 100
- Status: =IF(Coverage≥80%,"✅",IF(Coverage≥50%,"⚠️","❌"))

```

# Sheet 6: Detection Effectiveness - Technical Spec

**Column Definitions:**

| Col | Header | Width | Type | Validation |
|-----|--------|-------|------|------------|
| A | Rule ID | 20 | Text | Reference Sheet 5 Column A |
| B | Rule Name | 35 | Text | Reference Sheet 5 Column B |
| C | Test Date | 15 | Date | DD.MM.YYYY |
| D | Test Type | 18 | Dropdown | Simulated Attack, Purple Team, Red Team, Production Incident |
| E | MITRE Technique Tested | 15 | Text | T#### |
| F | Attack Executed? | 12 | Dropdown | Yes, No, Partial |
| G | Alert Generated? | 12 | Dropdown | Yes (TP), No (FN), False Alert (FP) |
| H | Time to Alert (minutes) | 12 | Number | ≥0 (if detected) |
| I | Alert Latency Status | 15 | Formula | =IF(H<60,"✅ <1hr",IF(H<240,"⚠️ 1-4hr","❌ >4hr")) |
| J | True Positives (30d) | 12 | Number | ≥0 |
| K | False Positives (30d) | 12 | Number | ≥0 |
| L | False Negatives (30d) | 12 | Number | ≥0 |
| M | TP Rate | 12 | Formula | =J/(J+L)×100 |
| N | FP Rate | 12 | Formula | =K/(J+K)×100 |
| O | Effectiveness Status | 15 | Formula | =IF(AND(M>90,N<20),"✅ Excellent",IF(AND(M>70,N<30),"⚠️ Acceptable","❌ Needs Tuning")) |
| P | Notes | 30 | Text | Test details, issues |

**Effectiveness Summary (Auto-Calculated):**
```excel
Overall Detection Rate: =AVERAGE(M:M) (target: >90%)
Overall FP Rate: =AVERAGE(N:N) (target: <20% Critical, <30% High)
Mean Time to Detect: =AVERAGE(H:H) (target: <60 min Critical, <240 min High)

Compliance Status:
=IF(AND(DetectionRate>90,FPRate<20,MTTD<60),"✅ Compliant",
   IF(AND(DetectionRate>70,FPRate<30,MTTD<240),"⚠️ Partial",
   "❌ Non-Compliant"))
```

---

# Implementation Complete

This specification enables comprehensive baseline and detection assessment with:

- Statistical baseline requirements (mean, median, std dev, percentiles)
- Time-aware baseline support (business hours, off-hours, weekends)
- MITRE ATT&CK coverage mapping
- Detection effectiveness measurement (TP/FP/FN rates, MTTD)
- Automated compliance scoring


**Total Document Length:** ~750 lines (framework implementation)

**Status:** ✅ COMPLETE - Ready for implementation and use

**Integration:** Builds on ISMS-IMP-A.8.16.1 (references monitoring infrastructure and log sources)

---

**END OF DOCUMENT**


## Sheet 4: Application Behavior Baselines

**Purpose:** Document measured baselines for application-specific behaviors (transactions, API calls, database queries, file operations)

**Policy Reference:** ISMS-POL-A.8.16, Section 2.2.3 (Application Behavior Monitoring)

**Why This Sheet Matters:**
Application-level anomalies often indicate:

- SQL injection attacks (abnormal query patterns)
- API abuse (excessive calls, unusual endpoints)
- Data exfiltration (abnormal file access volumes)
- Malware activity (unusual transaction patterns)


**Structure:**

- **Rows 8-32:** 25 data entry rows (application baselines)
- **Rows 35-50:** Application baseline summary


### Key Column Guidance (Condensed)

**Critical Columns:**

- **Application Name:** Which application is baselined
- **Baseline Category:** Transactions, API Calls, Database Queries, File Access, Network Connections
- **Behavior Metric:** Specific measurable behavior (e.g., "Orders processed per hour")
- **Statistical Profile:** Mean, Median, StdDev, 95th/99th percentile
- **Time-Aware Patterns:** Business hours vs. off-hours behavior
- **Alert Threshold:** Derived from statistical analysis
- **Threshold Methodology:** Document derivation method


**Example Application Baseline:**
```
Application: E-Commerce Platform
Category: Transactions
Metric: Orders processed per minute
Observation Period: 01.11.2025 - 15.12.2025 (45 days)
Statistical Profile:
  Business Hours (08:00-22:00): Mean 45 orders/min, StdDev 12, 95th %ile 68
  Off-Hours (22:00-08:00): Mean 8 orders/min, StdDev 3, 95th %ile 14
Alert Thresholds:
  Business Hours: >90 orders/min (95th percentile × 1.3)
  Off-Hours: >20 orders/min (95th percentile × 1.4)
  Low Threshold: <5 orders/min business hours (system degradation/outage)
```

**Application Baseline Categories:**

**1. Transaction Baselines:**

- E-commerce: Orders per minute, cart additions, checkout completions
- Financial: Transactions per hour, transfer volumes, payment processing
- Healthcare: Patient records accessed, prescriptions processed


**2. API Call Baselines:**

- REST API: Calls per minute by endpoint
- GraphQL: Queries per minute, response sizes
- Internal APIs: Service-to-service call rates


**3. Database Query Baselines:**

- Queries per minute (SELECT, INSERT, UPDATE, DELETE)
- Query response times
- Connection pool utilization
- Lock/wait events


**4. File Access Baselines:**

- Files read/written per hour
- File sizes transferred
- Directories accessed
- File operation types (create, modify, delete)


**5. Network Connection Baselines:**

- Outbound connections per minute
- Connection destinations (IPs, domains)
- Data transfer volumes
- Connection protocols


---

## Sheet 5: Detection Rule Coverage

**Purpose:** Inventory all detection rules and map coverage to MITRE ATT&CK framework

**Policy Reference:** ISMS-POL-A.8.16, Section 2.3 (Detection Capabilities)

**Why This Sheet Matters:**
You can have 500 detection rules, but if they all detect the same attack type, you have gaps.

**MITRE ATT&CK mapping answers:** "What attack techniques CAN we detect vs. CANNOT detect?"

**Structure:**

- **Rows 8-107:** 100 data entry rows (detection rule inventory)
- **Rows 110-135:** MITRE ATT&CK coverage matrix (auto-calculated)


### Key Column Guidance (Condensed)

**Essential Columns:**

- **Rule ID:** Unique identifier (DET-001, DET-002, etc.)
- **Rule Name:** Human-readable detection rule name
- **Rule Type:** Signature, Anomaly-Based, Behavioral, Correlation, Machine Learning
- **MITRE Tactic:** Which ATT&CK tactic (Reconnaissance, Initial Access, Execution, etc.)
- **MITRE Technique ID:** Specific technique (e.g., T1078 - Valid Accounts, T1190 - Exploit Public-Facing App)
- **Coverage Status:** Covered (rule active), Partial (limited detection), Not Covered (gap)
- **Severity:** Critical, High, Medium, Low
- **Status:** Active, Disabled, Testing, Development
- **False Positive Rate:** Count per 30 days
- **Last Tuned Date:** When rule was last adjusted


**MITRE ATT&CK Coverage Calculation (Auto-Calculated):**

```
For each MITRE Tactic:
  Total Techniques in Tactic: [from MITRE framework]
  Techniques Covered: COUNT(rules WHERE status=Active AND tactic=[this tactic])
  Coverage %: (Covered / Total) × 100
```

**Example Coverage Matrix:**
```
Initial Access: 15/20 techniques covered = 75% coverage
Execution: 25/40 techniques covered = 62.5% coverage
Persistence: 18/25 techniques covered = 72% coverage
Privilege Escalation: 10/20 techniques covered = 50% coverage ⚠️ GAP
...
```

**Critical Detection Gaps to Identify:**

- **Zero Coverage Tactics:** Entire MITRE tactic with 0 detection rules
- **Low Coverage (<50%):** Tactics with poor detection capability
- **Single Detection Point:** Only 1 rule covers many techniques (single point of failure)
- **Disabled Critical Rules:** High/Critical severity rules that are disabled (why?)


---

## Sheet 6: Detection Effectiveness Metrics

**Purpose:** Measure how well detection rules actually work (not just that they exist)

**Policy Reference:** ISMS-POL-A.8.16, Section 2.4 (Detection Effectiveness)

**Why This Sheet Matters:**
Having detection rules ≠ detecting threats.

**This sheet measures REALITY:**

- **True Positive Rate:** How often do we detect REAL attacks?
- **False Positive Rate:** How often do we alert on benign activity?
- **Mean Time to Detect (MTTD):** How fast do we detect attacks?


**Structure:**

- **Rows 8-57:** 50 data entry rows (effectiveness test results)
- **Rows 60-80:** Effectiveness summary metrics


### Key Column Guidance (Condensed)

**Essential Columns:**

- **Rule ID/Name:** Which detection rule being tested
- **Test Date:** When effectiveness test conducted
- **Test Type:** Simulated Attack, Purple Team Exercise, Production Incident, Penetration Test
- **MITRE Technique Tested:** What attack was executed (T-code)
- **Attack Executed Successfully?:** Yes, No, Partial
- **Alert Generated?:** Yes (True Positive), No (False Negative), False Alert (False Positive)
- **Time to Alert:** Minutes from attack execution to alert firing
- **Alert Latency Status:** ✅ <1hr, ⚠️ 1-4hr, ❌ >4hr
- **True Positives (30d):** Count of real attacks detected
- **False Positives (30d):** Count of false alerts
- **False Negatives (30d):** Count of attacks missed
- **TP Rate:** True Positive Rate (%) = TP / (TP + FN) × 100
- **FP Rate:** False Positive Rate (%) = FP / (FP + TP) × 100
- **Effectiveness Status:** ✅ Excellent (TP>90%, FP<20%), ⚠️ Acceptable (TP>70%, FP<30%), ❌ Needs Tuning


**Effectiveness Testing Methods:**

**1. Simulated Attacks (Atomic Red Team, Caldera):**
```bash
# Example: Test T1078 (Valid Accounts) detection
# Simulate credential spray attack
for user in userlist.txt; do
  ssh $user@target-system # (with wrong password)
done

# Expected: Alert "Brute Force Authentication" within 5 minutes
# Result: Alert fired at 3:42 (✅ True Positive, 3.7 min latency)
```

**2. Purple Team Exercises:**

- Red Team executes attack technique
- Blue Team monitors for detection
- Measure: Did we detect? How fast? How many false positives?


**3. Production Incident Analysis:**

- Review past security incidents
- Did detection rules fire?
- How long to detect?
- Were there missed indicators?


**Effectiveness Calculation Example:**
```
Detection Rule: DET-AUTH-001 (Failed Login Threshold)
30-Day Period:

Real Attacks (TP): 8 (detected 8 actual brute force attempts)
False Alerts (FP): 15 (alerted on legitimate behavior 15 times)
Missed Attacks (FN): 2 (2 brute force attempts NOT detected)

True Positive Rate: 8 / (8 + 2) × 100 = 80% ⚠️ (target: >90%)
False Positive Rate: 15 / (15 + 8) × 100 = 65% ❌ (target: <30%)
Mean Time to Detect: 8.5 minutes (✅ target: <60 min)

Status: ❌ Needs Tuning (high FP rate)
Remediation: Increase failed login threshold from 5 to 10 attempts
```

---

# Evidence Collection (Enhanced)

**Additional Evidence for Baseline & Detection Assessment:**

**1. Baseline Calculation Workbooks**

- Excel/CSV files with raw time-series data
- Statistical calculations (mean, median, StdDev, percentiles)
- Graphs showing behavioral patterns over time
- Incident exclusion documentation


**2. MITRE ATT&CK Coverage Reports**

- Navigator layers showing coverage (export from MITRE ATT&CK Navigator)
- Gap analysis documents (uncovered techniques)
- Coverage improvement roadmap


**3. Detection Effectiveness Test Reports**

- Test plans (which techniques, when tested)
- Test execution logs (commands run, expected results)
- Alert screenshots (proof of detection)
- MTTD measurements per test
- Purple Team exercise reports


**4. Tuning History**

- Detection rule change logs (before/after configurations)
- False positive trends (FP count over time)
- Tuning rationale (why threshold changed)


**5. Baseline Review Records**

- Previous baseline versions (for trend analysis)
- Baseline update justifications (why baseline changed)
- Stakeholder approvals for baseline changes


---

# Common Pitfalls (Expanded to 10)

## Pitfall 1: The "Gut Feel" Baseline
[ALREADY DOCUMENTED - KEEP EXISTING]

## Pitfall 2: Confusing Detection Rules with Detection Effectiveness
[ALREADY DOCUMENTED - KEEP EXISTING]

## Pitfall 3: Static Baselines That Never Update
[ALREADY DOCUMENTED - KEEP EXISTING]

## Pitfall 4: Ignoring Time-Aware Patterns
[ALREADY DOCUMENTED - KEEP EXISTING]

## Pitfall 5: No Exclusion of Incidents from Baselines
[ALREADY DOCUMENTED - KEEP EXISTING]

## Pitfall 6: Baselines Without Detection Rules

**The Mistake:**
Document beautiful baselines in Excel, but never implement detection rules in SIEM.

**Reality Check:**
Baseline documentation is USELESS if not translated into actual detections.

**How to Avoid:**

- Sheet 2, Column AB: Document which detection rules use each baseline
- Sheet 3, Column W: Document detection rule IDs
- Sheet 5: Verify every baseline has corresponding rule
- Test rules are actually firing (Sheet 6)


**Verification:**
For every baseline documented:
1. Find corresponding detection rule in SIEM
2. Verify rule is enabled (Status = Active)
3. Test rule with simulated data
4. Confirm alerts reaching SOC

**Red Flag:** Many baselines documented, but few detection rules in Sheet 5

---

## Pitfall 7: Comparing Apples to Oranges (Baseline Inconsistency)

**The Mistake:**
Different teams establish baselines using different methodologies, making comparison impossible.

**Examples:**

- Team A uses 95th percentile × 1.3
- Team B uses mean + 3×StdDev  
- Team C uses arbitrary thresholds
- Can't compare baseline quality or tune consistently


**How to Avoid:**

- Standardize threshold derivation (Column U methodology)
- Document methodology in ISMS-POL-A.8.16, Annex B
- Use same observation periods (30-45 days)
- Use same statistical tools (Excel, Python, R)


**Best Practice:**
Create baseline template with formulas pre-built, distribute to all teams.

---

## Pitfall 8: Detection Rules Disabled "Temporarily" (Forever)

**The Mistake:**
High false positive rate → Disable detection rule "until we can tune it" → Never re-enabled.

**Reality Check:**
Check your SIEM. How many rules have Status = "Disabled"? When were they disabled? By whom?

**Common Causes:**

- High FP rate (annoying SOC analysts)
- Performance impact (slow SIEM searches)
- "We'll tune it next quarter" (never happens)


**How to Avoid:**

- Sheet 5: Track disabled rules explicitly
- Require JUSTIFICATION for disabling (document in notes)
- Set REVIEW DATE for disabled rules (30-90 days max)
- CISO approval required to disable Critical/High severity rules


**Audit Question:**
"Show me all disabled detection rules and when you plan to re-enable them."

If answer is "uh..." → Gap.

---

## Pitfall 9: Testing Detection With Perfect Conditions

**The Mistake:**
Test detection rules in lab with clean data, no noise, perfect timing → Works great!

Deploy to production with real data, network latency, log delays → Doesn't work.

**Reality Check:**
Lab tests ≠ production effectiveness.

**How to Avoid:**

- Test in production (or production-like environment)
- Include network latency (log delay simulation)
- Include noisy background activity (not just attack in isolation)
- Test during peak hours (not just at 2 AM when nothing else happening)


**Purple Team Best Practice:**
Execute attack during business hours, with production systems under load, see if detection still works.

**Sheet 6:** Document test environment (Lab vs. Production) - production tests more credible.

---

## Pitfall 10: Alert Fatigue Leading to Baseline Abandonment

**The Mistake:**
Initial baseline too sensitive → Generates 100 alerts/day → SOC overwhelmed → "Just turn it off."

**Reality Check:**
If baseline generates constant alerts, problem is threshold not baseline concept.

**Symptoms:**

- SOC analysts ignoring alerts
- Rules disabled to reduce noise
- Tickets closed as "false positive" without investigation


**How to Avoid:**
1. **Start Conservative:** Set initial thresholds wider (99th percentile instead of 95th)
2. **Monitor FP Rate:** Track false positives daily for first week
3. **Tune Quickly:** If FP rate >30%, adjust threshold immediately
4. **Time-Aware Helps:** Different thresholds for business/off-hours reduces noise
5. **Whitelist Known Good:** Exclude legitimate behavior causing FPs

**Goal:** Alert volume SOC can handle (<50 per day across all rules for small SOC)

**Sheet 6 tracks this:** FP Rate per rule → Identify noisy rules → Tune or disable.

---

# Quality Checklist (Enhanced)

## Sheet-Specific Checks

**Sheet 2: System Utilization Baselines**

- [ ] All Tier 1 systems have baselines documented
- [ ] Observation period ≥30 days for each baseline
- [ ] Incidents excluded from baseline calculation (documented in Column I)
- [ ] Statistical profile complete (Mean, Median, StdDev, percentiles)
- [ ] Time-aware profiles documented where behavior varies by time
- [ ] Alert thresholds derived using documented methodology (not arbitrary)
- [ ] Detection rule IDs documented (Column AB) and rules exist in Sheet 5
- [ ] Baseline validity period set with review dates
- [ ] No placeholder values (all "TBD" fields filled)


**Sheet 3: Access Pattern Baselines**

- [ ] All privileged accounts (admins, DBAs) baselined
- [ ] Service accounts baselined (should be very consistent - low StdDev)
- [ ] Geographic patterns documented (can detect impossible travel)
- [ ] Time-aware patterns captured (typical hours documented)
- [ ] Known exceptions documented (reduces false positives)
- [ ] Alert thresholds appropriate for access type
- [ ] Detection rules created and operational
- [ ] Off-hours access baselines established (not just business hours)


**Sheet 4: Application Behavior Baselines**

- [ ] Critical applications baselined (Tier 1 apps)
- [ ] All five baseline categories covered (Transactions, API, Database, File, Network)
- [ ] Application behaviors measurable (not subjective)
- [ ] Thresholds account for business cycles (month-end, seasonal)
- [ ] Low threshold defined (detect degradation/outage, not just overload)


**Sheet 5: Detection Rule Coverage**

- [ ] All active detection rules documented
- [ ] MITRE ATT&CK mapping complete for each rule
- [ ] Coverage gaps identified (<50% coverage per tactic)
- [ ] Critical gaps have remediation plans
- [ ] Disabled rules documented with justification and review date
- [ ] False positive rates tracked
- [ ] Last tuned dates recent (<90 days for high-FP rules)


**Sheet 6: Detection Effectiveness**

- [ ] At least 20% of detection rules tested in last 90 days
- [ ] All Critical/High severity rules tested at least once
- [ ] Test types varied (not just simulated - include purple team, prod incidents)
- [ ] True Positive Rate measured (>90% target for Critical rules)
- [ ] False Positive Rate measured (<20% target for Critical, <30% High)
- [ ] MTTD measured (<60 min target for Critical, <4 hr High)
- [ ] Rules with poor effectiveness flagged for tuning


## Cross-Document Consistency

**A.8.16.1 ↔ A.8.16.2 Integration:**

- [ ] Systems with baselines (A.8.16.2, Sheet 2) are monitored (A.8.16.1, Sheet 3)
- [ ] Monitoring platforms (A.8.16.1, Sheet 2) support baseline calculations (sufficient data retention, query capability)
- [ ] Log sources (A.8.16.1, Sheet 3) provide data needed for baselines


## Overall Quality

**Baseline Quality:**

- [ ] >90% of Tier 1 systems have documented baselines
- [ ] Baselines based on ≥30 days observation (not estimates)
- [ ] Statistical rigor maintained (not arbitrary thresholds)
- [ ] All baselines have defined validity periods and review schedules


**Detection Coverage:**

- [ ] MITRE ATT&CK coverage ≥60% overall
- [ ] No tactics with 0% coverage (complete blind spots)
- [ ] Detection effectiveness tested (not just assumed)


**Evidence Quality:**

- [ ] All baseline calculations stored as evidence
- [ ] MITRE coverage matrix exported
- [ ] Detection test results documented
- [ ] Tuning history maintained


---

# Review & Approval (Same Structure as A.8.16.1)

**Three-Level Approval Workflow:**

**Level 1: Technical Review** (SOC Lead / Detection Engineering)

- Baseline calculations mathematically correct
- Detection rules properly configured
- MITRE coverage assessment accurate
- Effectiveness testing methodology sound


**Level 2: Compliance Review** (Security Manager / CISO)

- Policy compliance (Tier 1 baseline requirement met)
- Detection coverage adequate (≥60% MITRE coverage)
- Effectiveness targets met (TP>90%, FP<30%, MTTD<60min for Critical)
- Gaps documented with remediation plans


**Level 3: Executive Approval** (CISO)

- Detection strategy aligns with threat landscape
- Investment in detection capabilities justified
- Risk acceptance for coverage gaps documented
- Detection effectiveness improving over time


**Timeline:** 15 business days total (same as A.8.16.1)

---

**END OF SPECIFICATION**

---

*"Those who can imagine anything, can create the impossible."*
— Alan Turing
*Where bamboo antennas actually work.* 🎋
