# ISMS-IMP-A.8.16.2 - Baseline & Detection Assessment
## Excel Workbook Layout Specification
### ISO/IEC 27001:2022 Control A.8.16: Monitoring Activities

---

## Document Overview

**Document ID:** ISMS-IMP-A.8.16.2  
**Assessment Area:** Baseline Establishment & Anomaly Detection  
**Related Policy:** ISMS-POL-A.8.16-S2.2  
**Purpose:** Assess baseline documentation, anomaly detection capabilities, and detection rule effectiveness  
**Generator Script:** `generate_a816_2_baseline_detection.py`  
**Output Filename:** `ISMS-IMP-A.8.16.2_Baseline_Detection_YYYYMMDD.xlsx`

---

## Workbook Structure

**Total Sheets:** 9
1. Instructions & Legend
2. 1. Baseline Documentation
3. 2. Detection Rule Inventory
4. 3. Anomaly Detection Capabilities
5. 4. Threshold Configuration
6. 5. Detection Effectiveness
7. Summary Dashboard
8. Evidence Register
9. Approval Sign-Off

---

## Sheet 2: 1. Baseline Documentation

### Header
**Title:** "1. BASELINE DOCUMENTATION ASSESSMENT"  
**Policy Reference:** "Assess baseline establishment per ISMS-POL-A.8.16-S2.2.2"

### Assessment Question
"Are baselines documented for all critical systems with measurable metrics?"

### Column Headers (Row 6) - 22 Columns (A-V)

| Col | Header | Width | Type | Validation |
|-----|--------|-------|------|------------|
| A | System/Asset Name | 28 | Text | Free text |
| B | System Type | 22 | Dropdown | Domain Controller, Database Server, Firewall, VPN Gateway, Web Server, Application Server, Endpoint, Other |
| C | Criticality Tier | 15 | Dropdown | Tier 1 (Critical), Tier 2 (Standard), Tier 3 (Low) |
| D | System Owner | 20 | Text | Free text |
| E | Baseline Established | 16 | Dropdown | Yes, No, In Progress |
| F | Baseline Date | 14 | Text | DD.MM.YYYY |
| G | Observation Period (Days) | 18 | Text | Free text |
| H | Metrics Documented | 30 | Text | Free text (auth, network, resources) |
| I | Statistical Profile | 22 | Dropdown | Complete (Mean/Median/StdDev/95th), Partial, Minimal, None |
| J | Time-Aware Baselines | 18 | Dropdown | Yes (Business/Off-Hours/Weekend), Partial, No |
| K | Baseline Review Frequency | 20 | Dropdown | Quarterly, Semi-Annually, Annually, Never |
| L | Last Review Date | 14 | Text | DD.MM.YYYY |
| M | Next Review Date | 14 | Text | DD.MM.YYYY |
| N | Thresholds Derived | 16 | Dropdown | Yes, No, Partial |
| O | Threshold Methodology | 22 | Dropdown | 95th %ile × Multiplier, Static, Expert Judgment, None |
| P | Baseline Accuracy | 16 | Dropdown | High, Medium, Low, Unknown |
| Q | False Positive Rate | 16 | Text | Free text (%) |
| R | Baseline Approved By | 20 | Text | Free text |
| S | Documentation Location | 25 | Text | Free text (file path, URL) |
| T | Compliance Status | 18 | Dropdown | ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A |
| U | Issues/Gaps | 30 | Text | Free text |
| V | Remediation Priority | 18 | Dropdown | Critical, High, Medium, Low, None |

### Data Entry Rows
- **Rows 8-25:** 18 data entry rows (yellow-highlighted)
- **Row 7:** Example: "DC01-Primary, Domain Controller, Tier 1, IT Ops, Yes, 15.09.2025..."

### Compliance Checklist (Starting Row 27)
**Title:** "BASELINE DOCUMENTATION CHECKLIST"

1. 100% of Tier 1 (Critical) systems have documented baselines
2. >80% of Tier 2 (Standard) systems have documented baselines
3. Baselines include mean, median, std dev, 95th percentile
4. Time-aware baselines established (business hours, off-hours, weekend)
5. Observation period ≥30 days during known-good periods
6. Exclusions documented (incidents, maintenance windows)
7. Thresholds derived using documented methodology (95th × multiplier)
8. Baselines approved by system owner and SOC lead
9. Baseline review schedule defined (quarterly for Tier 1, semi-annually for Tier 2)
10. Reviews conducted on schedule
11. Baseline changes version controlled
12. False positive rates tracked (<25% target)
13. Baseline documentation stored in accessible location
14. Baseline templates used consistently
15. Baselines integrated with detection rules

**Auto-Score:** `=COUNTIF(C27:C41,"✅ Compliant")&" / 15"`

### Reference Tables (Starting Row 45)

**Table 1: Baseline Maturity Levels**
| Level | Description | Characteristics | Compliance |
|-------|-------------|-----------------|-----------|
| Level 0 | No Baselines | Subjective opinions, anecdotal | Non-Compliant |
| Level 1 | Basic Baselines | Critical systems, basic stats | Minimum Viable |
| Level 2 | Comprehensive | All systems, full stats, time-aware | Full Compliance |
| Level 3 | Automated | ML/AI, continuous adaptation | Excellence |

**Table 2: Required Metrics by System Type**
| System Type | Authentication Metrics | Network Metrics | System Metrics |
|-------------|----------------------|-----------------|----------------|
| Domain Controller | Logins/hour, failed auth, privileged access | Replication traffic, LDAP queries | CPU, memory, event logs |
| Database Server | Query count, connections, admin access | Data volume, connection sources | CPU, memory, disk I/O |
| Firewall | Connections/min, blocked attempts, rule hits | Throughput, session count | CPU, memory, interface utilization |

**Table 3: Threshold Derivation Methodology**
| Criticality | Risk Level | Multiplier | Example |
|-------------|-----------|------------|---------|
| Critical | High | 1.2x | 95th %ile = 150, threshold = 180 |
| Critical | Medium | 1.5x | 95th %ile = 150, threshold = 225 |
| Standard | Medium | 1.5x | 95th %ile = 100, threshold = 150 |
| Standard | Low | 2.0x | 95th %ile = 100, threshold = 200 |

---

## Sheet 3: 2. Detection Rule Inventory

### Header
**Title:** "2. DETECTION RULE INVENTORY"  
**Policy Reference:** "Assess detection rules per ISMS-POL-A.8.16-S2.2.5"

### Column Headers - 24 Columns (A-X)

| Col | Header | Width | Type |
|-----|--------|-------|------|
| A | Rule ID/Name | 28 | Text |
| B | Detection Type | 20 | Dropdown: Signature-Based, Threshold-Based, Anomaly-Based, Heuristic, Correlation |
| C | MITRE ATT&CK Technique | 22 | Text |
| D | Alert Severity | 15 | Dropdown: Critical, High, Medium, Low |
| E | Rule Description | 35 | Text |
| F | Data Sources Required | 30 | Text |
| G | Detection Logic | 35 | Text |
| H | Time Window | 15 | Text |
| I | Threshold Value | 15 | Text |
| J | Baseline-Derived | 16 | Dropdown: Yes, No, N/A |
| K | Rule Status | 16 | Dropdown: Active, Testing, Disabled, Retired |
| L | Created Date | 14 | Text: DD.MM.YYYY |
| M | Last Tuned | 14 | Text: DD.MM.YYYY |
| N | Tuning Frequency | 16 | Dropdown: Quarterly, Semi-Annually, Annually, As-Needed |
| O | Alert Volume (30d) | 16 | Text |
| P | False Positive Rate | 16 | Text: % |
| Q | True Positive Count | 16 | Text |
| R | Detection Rate (Testing) | 18 | Text: % |
| S | Last Tested | 14 | Text: DD.MM.YYYY |
| T | Rule Owner | 20 | Text |
| U | Playbook Reference | 22 | Text |
| V | Compliance Status | 18 | Dropdown: ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A |
| W | Issues/Gaps | 30 | Text |
| X | Tuning Priority | 16 | Dropdown: Critical, High, Medium, Low, None |

### Compliance Checklist
1. Detection rules documented in inventory
2. Each rule has unique ID
3. MITRE ATT&CK mapping documented
4. Severity classification assigned
5. Detection logic documented
6. Baseline-derived rules identified
7. Rules tested before production deployment
8. Testing results documented (detection rate >90% target)
9. False positive rate tracked (<25% overall, <10% critical)
10. High false positive rules tuned within 30 days
11. Rules reviewed quarterly (critical) / semi-annually (standard)
12. Tuning changes version controlled
13. Rule owner assigned
14. Playbook exists for each rule
15. Retired rules properly archived

---

## Sheet 4: 3. Anomaly Detection Capabilities

### Header
**Title:** "3. ANOMALY DETECTION CAPABILITIES"  
**Policy Reference:** "Assess anomaly detection per ISMS-POL-A.8.16-S2.2.4"

### Column Headers - 19 Columns (A-S)

| Col | Header | Width | Type |
|-----|--------|-------|------|
| A | Detection Method | 28 | Dropdown: Signature-Based, Threshold-Based, Anomaly-Based, Behavioral, Heuristic, Correlation |
| B | Use Cases | 30 | Text |
| C | Technology/Tool | 22 | Text |
| D | Implementation Status | 18 | Dropdown: ✅ Deployed, ⚠️ Partial, ❌ Not Deployed, Planned |
| E | Coverage (Systems) | 18 | Text: % or count |
| F | Baseline Dependency | 16 | Dropdown: High, Medium, Low, None |
| G | Machine Learning Used | 18 | Dropdown: Yes, No, Planned |
| H | Detection Accuracy | 16 | Text: % |
| I | False Positive Rate | 16 | Text: % |
| J | Alert Volume (30d) | 16 | Text |
| K | Mean Time to Detect | 16 | Text: minutes |
| L | Detection Rate | 16 | Text: % |
| M | Last Effectiveness Test | 16 | Text: DD.MM.YYYY |
| N | Strengths | 30 | Text |
| O | Limitations | 30 | Text |
| P | Integration Quality | 18 | Dropdown: Excellent, Good, Fair, Poor |
| Q | Compliance Status | 18 | Dropdown: ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A |
| R | Improvement Opportunities | 30 | Text |
| S | Priority | 16 | Dropdown: Critical, High, Medium, Low |

### Compliance Checklist
1. Multiple detection methodologies implemented
2. Signature-based detection deployed (mandatory)
3. Threshold-based detection deployed (mandatory for critical systems)
4. Anomaly-based detection deployed (recommended)
5. Correlation-based detection deployed (mandatory with SIEM)
6. Detection methods complement each other
7. Baseline-dependent methods have documented baselines
8. Detection accuracy measured (target >90%)
9. False positive rates acceptable (<25% overall)
10. Detection effectiveness tested quarterly

---

## Sheet 5: 4. Threshold Configuration

### Header
**Title:** "4. THRESHOLD CONFIGURATION ASSESSMENT"  
**Policy Reference:** "Assess thresholds per ISMS-POL-A.8.16-S2.2.3"

### Column Headers - 18 Columns (A-R)

| Col | Header | Width | Type |
|-----|--------|-------|------|
| A | System/Metric | 28 | Text |
| B | Metric Type | 22 | Text |
| C | Baseline 95th Percentile | 18 | Text |
| D | Criticality | 15 | Dropdown: Critical, High, Medium, Low |
| E | Risk Level | 15 | Dropdown: High, Medium, Low |
| F | Multiplier Applied | 14 | Text: e.g., 1.2x |
| G | Warning Threshold | 16 | Text |
| H | Critical Threshold | 16 | Text |
| I | Threshold Rationale | 30 | Text |
| J | Last Validated | 14 | Text: DD.MM.YYYY |
| K | Validation Method | 22 | Text |
| L | Alerts Generated (30d) | 18 | Text |
| M | False Positive Rate | 16 | Text: % |
| N | True Positive Count | 16 | Text |
| O | Adjustment Needed | 16 | Dropdown: Yes, No, Under Review |
| P | Compliance Status | 18 | Dropdown: ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A |
| Q | Issues/Notes | 30 | Text |
| R | Tuning Priority | 16 | Dropdown: Critical, High, Medium, Low, None |

### Compliance Checklist
1. Thresholds derived from documented baselines
2. Derivation methodology documented (95th × multiplier)
3. Multipliers justified based on criticality and risk
4. Multi-threshold alerting implemented (warning + critical)
5. Thresholds validated quarterly
6. False positive rates tracked per threshold
7. High false positive thresholds adjusted within 30 days
8. Threshold changes documented and approved
9. Thresholds tested before production deployment
10. Threshold configuration backed up

---

## Sheet 6: 5. Detection Effectiveness

### Header
**Title:** "5. DETECTION EFFECTIVENESS ASSESSMENT"  
**Policy Reference:** "Assess effectiveness per ISMS-POL-A.8.16-S2.2.8"

### Column Headers - 20 Columns (A-T)

| Col | Header | Width | Type |
|-----|--------|-------|------|
| A | Test Scenario/Attack Type | 30 | Text |
| B | MITRE ATT&CK Technique | 22 | Text |
| C | Test Method | 22 | Dropdown: Purple Team, Red Team, Atomic Red Team, Caldera, Manual Simulation, Other |
| D | Test Date | 14 | Text: DD.MM.YYYY |
| E | Tester/Team | 20 | Text |
| F | Detection Expected | 16 | Dropdown: Yes, No |
| G | Alert Generated | 16 | Dropdown: Yes, No |
| H | Detection Time (MTTD) | 16 | Text: minutes |
| I | Alert Severity | 15 | Dropdown: Critical, High, Medium, Low |
| J | Detection Rule(s) Triggered | 30 | Text |
| K | Detection Accuracy | 16 | Dropdown: Accurate, Partial, Inaccurate, Missed |
| L | False Negative | 15 | Dropdown: Yes, No |
| M | Root Cause (if missed) | 30 | Text |
| N | Remediation Action | 30 | Text |
| O | Remediation Status | 18 | Dropdown: Complete, In Progress, Planned, Deferred |
| P | Retest Date | 14 | Text: DD.MM.YYYY |
| Q | Retest Result | 16 | Dropdown: Passed, Failed, Pending |
| R | Compliance Status | 18 | Dropdown: ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A |
| S | Notes | 30 | Text |
| T | Priority | 16 | Dropdown: Critical, High, Medium, Low |

### Compliance Checklist
1. Detection effectiveness testing conducted quarterly
2. Test scenarios cover MITRE ATT&CK techniques
3. Critical attack types tested (credential dumping, lateral movement, exfiltration)
4. Testing methodology documented
5. Detection rate measured (target >90%)
6. Mean Time to Detect (MTTD) measured (target <5 min for critical)
7. False negatives tracked and analyzed
8. Gaps remediated within 30 days (critical) / 90 days (high)
9. Retesting conducted after remediation
10. Results reported to CISO quarterly

---

## Sheet 7: Summary Dashboard

### Section 1: Baseline Coverage (Rows 3-15)
- Total systems requiring baselines
- Systems with complete baselines
- Systems with partial baselines
- Systems without baselines
- Baseline completeness % (target: 100% Tier 1, >80% Tier 2)
- Baselines reviewed on schedule %
- Baseline staleness (overdue reviews)

### Section 2: Detection Rule Health (Rows 18-30)
- Total active detection rules
- Rules by severity (Critical/High/Medium/Low)
- Rules by type (Signature/Threshold/Anomaly/Correlation)
- Average false positive rate (target: <25%)
- Rules requiring tuning
- Rules tested in last 6 months %

### Section 3: Detection Effectiveness (Rows 33-45)
- Overall detection rate % (target: >90%)
- MTTD average (target: <5 min for critical)
- MITRE ATT&CK coverage % (techniques with detection)
- False negative rate % (target: <5% for critical threats)
- Tests conducted (last quarter)
- Gaps remediated / total gaps

### Section 4: Compliance Summary (Rows 48-58)
| Assessment Area | Total | Compliant | Partial | Non-Compliant | % |
|-----------------|-------|-----------|---------|---------------|---|
| 1. Baseline Documentation | Formula | Formula | Formula | Formula | Formula |
| 2. Detection Rule Inventory | Formula | Formula | Formula | Formula | Formula |
| 3. Anomaly Detection | Formula | Formula | Formula | Formula | Formula |
| 4. Threshold Configuration | Formula | Formula | Formula | Formula | Formula |
| 5. Detection Effectiveness | Formula | Formula | Formula | Formula | Formula |
| **OVERALL** | Formula | Formula | Formula | Formula | Formula |

### Section 5: Critical Gaps (Rows 67-75)
- Priority | Gap Description | Impact | System/Rule Affected | Target Date | Owner

---

## Sheets 8-9: Evidence Register & Approval Sign-Off
(Standard format as per IMP-A.8.16.1)

---

**END OF SPECIFICATION**