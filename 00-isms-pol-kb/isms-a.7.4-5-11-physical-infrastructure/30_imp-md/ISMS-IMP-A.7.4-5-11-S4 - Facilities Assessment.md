# ISMS-IMP-A.7.4-5-11-S4: Facilities Assessment

**Document Classification:** Internal - ISMS Implementation Guide  
**Version:** 1.0  
**Effective Date:** [To be defined]  
**Review Cycle:** Annual  
**Owner:** Internal Audit / Facilities Manager  
**Approved By:** CISO

---

## Purpose

This implementation guide provides step-by-step procedures for conducting physical infrastructure compliance assessments to meet the assessment framework requirements (see POL-S5).

**Scope:** Monthly automated assessments, quarterly manual assessments, annual comprehensive assessments.

**Target Audience:** Internal Audit, Facilities Management, Security Operations, Compliance Officers.

---

## Table of Contents

1. [Assessment Overview](#1-assessment-overview)
2. [Monthly Automated Assessment](#2-monthly-automated-assessment)
3. [Quarterly Manual Assessment](#3-quarterly-manual-assessment)
4. [Annual Comprehensive Assessment](#4-annual-comprehensive-assessment)
5. [Assessment Workbook Usage](#5-assessment-workbook-usage)
6. [Dashboard Updates and Reporting](#6-dashboard-updates-and-reporting)

---

## 1. Assessment Overview

### 1.1 Assessment Frequency (Per POL-S5, Section 1.2)

- **Monthly Automated:** First week of each month (access logs, temperature excursions, utility uptime)
- **Quarterly Manual:** End of quarter - March 31, June 30, September 30, December 31 (comprehensive assessment)
- **Annual Comprehensive:** Q4 - October/November (audit-readiness assessment, all facilities)
- **Triggered:** After major incidents, facility changes, audit preparation

### 1.2 Assessment Tools

**Excel Workbooks (Pre-Generated):**
- ISMS_Assessment_Access_Monitoring.xlsx (A.7.4 assessment)
- ISMS_Assessment_Environmental_Protection.xlsx (A.7.5 assessment)
- ISMS_Assessment_Utility_Resilience.xlsx (A.7.11 assessment)
- ISMS_Dashboard_Physical_Infrastructure.xlsx (unified compliance dashboard)

**Supporting Data Sources:**
- Access control system (export access logs)
- CCTV system (camera inventory, retention verification)
- Environmental monitoring system (temperature/humidity data export)
- UPS monitoring system (battery health reports)
- Generator test logs (manual logs or automated system exports)
- Network monitoring system (ISP uptime reports)

### 1.3 Assessment Roles

**Assessor (Primary Role):**
- Facilities Manager (operational assessments) OR
- Internal Auditor (compliance assessments) OR
- Designated staff member (trained on assessment procedures)
- Responsibilities: Data collection, workbook completion, initial analysis

**ISO (Information Security Officer - Reviewer):**
- Reviews assessor's work (verify accuracy, completeness)
- Escalates findings to CISO (non-compliance items)

**CISO (Approver):**
- Final approval of assessment (sign-off on compliance score)
- Authorizes remediation plan (if non-compliance identified)

---

## 2. Monthly Automated Assessment

**Objective:** Collect automated metrics (access logs, temperature excursions, utility uptime) without manual facility inspection.

**Timeline:** First week of each month (assess previous month's data)

**Duration:** 2-4 hours

### 2.1 Data Collection

**Access Control Data (A.7.4):**
1. **Export access logs:** Export 30-day access log sample from access control system
   - Format: CSV (columns: timestamp, user, door, result)
   - Save to: \\fileserver\isms\assessments\access-logs\YYYY-MM_access_log.csv

2. **Count failed access attempts:**
   - Filter access log: result = "denied" AND NOT (user = invalid badge OR user = visitor)
   - Count legitimate failures (authorized users denied due to insufficient privileges, anti-passback, etc.)
   - Target: <5 per month

3. **Count after-hours access events:**
   - Filter access log: timestamp outside business hours (before 7 AM or after 6 PM) AND result = "granted"
   - Count events
   - Review: Are after-hours accesses authorized? (check against after-hours access list)

**Environmental Monitoring Data (A.7.5):**
1. **Export temperature data:** Export 30-day temperature monitoring data from environmental monitoring system
   - Format: CSV (columns: timestamp, sensor_id, location, temperature, humidity)
   - Save to: \\fileserver\isms\assessments\environmental\YYYY-MM_temperature.csv

2. **Count temperature excursions:**
   - Filter data: temperature < 18°C OR temperature > 27°C
   - Count excursion events (each continuous period outside range = 1 event)
   - Target: <5 excursions per month per facility

3. **Count environmental incidents:**
   - Query incident management system: incident_type = "environmental" AND incident_date BETWEEN [first day of month] AND [last day of month]
   - Count incidents (fire, flood, temperature causing damage or downtime)
   - Target: 0 major incidents per month

**Utility Monitoring Data (A.7.11):**
1. **Calculate power uptime:**
   - Export UPS monitoring data (30-day uptime/downtime)
   - Calculate: Uptime % = (Total minutes - Downtime minutes) / Total minutes × 100%
   - Target: 99.99% (critical facilities), 99.9% (standard facilities)

2. **Export UPS battery health:**
   - Export from UPS monitoring system (battery health percentage per UPS)
   - Target: >80% for all UPS

3. **Calculate HVAC uptime:**
   - Export HVAC monitoring data (30-day uptime/downtime)
   - Calculate: Uptime % = (Total minutes - Downtime minutes) / Total minutes × 100%
   - Target: 99.9% (critical), 99% (standard)

4. **Calculate ISP uptime:**
   - Export network monitoring data (ISP circuit uptime/downtime)
   - Calculate: Uptime % per ISP
   - Verify: Meets ISP SLA (typically 99.9%)

### 2.2 Dashboard Update

**Update ISMS_Dashboard_Physical_Infrastructure.xlsx:**

1. **Open dashboard workbook** (previous month's copy or template)

2. **Update Executive Dashboard worksheet:**
   - Month: [Month YYYY]
   - Failed access attempts: [Count]
   - Temperature excursions: [Count]
   - Power uptime: [XX.XX%]
   - HVAC uptime: [XX.XX%]
   - ISP uptime: [XX.XX%]
   - Dashboard auto-calculates compliance scores and trends

3. **Update Incident Trends worksheet:**
   - Add current month's incident counts (physical security, environmental, utility)

4. **Save dashboard:**
   - Save as: ISMS_Dashboard_Physical_Infrastructure_YYYY-MM.xlsx
   - Save to: \\fileserver\isms\dashboards\

### 2.3 Monthly Reporting

**Generate Monthly Summary Report (1-page):**

**Report Contents:**
- Assessment month: [Month YYYY]
- Overall compliance score: [XX%] (from dashboard)
- Metrics summary:
  - Failed access attempts: [X] (target <5) - ✅ PASS or ❌ FAIL
  - Temperature excursions: [X] (target <5) - ✅ PASS or ❌ FAIL
  - Power uptime: [XX.XX%] (target 99.99%/99.9%) - ✅ PASS or ❌ FAIL
  - HVAC uptime: [XX.XX%] (target 99.9%/99%) - ✅ PASS or ❌ FAIL
  - ISP uptime: [XX.XX%] (target 99.9%) - ✅ PASS or ❌ FAIL
- Findings (if any): List any metrics that failed to meet target
- Recommendations (if any): Remediation actions required

**Distribution:**
- Email to: CISO, Facilities Manager, Security Operations Manager
- Attachment: Monthly summary report (PDF or Word)
- Subject: "Physical Infrastructure Monthly Assessment - [Month YYYY]"

---

## 3. Quarterly Manual Assessment

**Objective:** Comprehensive assessment including manual facility inspection, testing compliance verification, operational metrics analysis.

**Timeline:** End of quarter (March 31, June 30, September 30, December 31)

**Duration:** 8-16 hours (depending on facility size)

### 3.1 Pre-Assessment Preparation

**1 Week Before Assessment:**

**Schedule Assessment:**
- Notify Facilities Manager: Assessment date/time, expected duration
- Request access to facilities (server rooms, equipment rooms, electrical rooms)
- Request test records (fire alarm tests, UPS tests, generator tests, water sensor tests from past quarter)

**Gather Data:**
- Collect monthly automated assessment data (past 3 months)
- Download assessment workbooks (if not already on file server)

### 3.2 Physical Security Monitoring Assessment (A.7.4)

**Use Workbook:** ISMS_Assessment_Access_Monitoring.xlsx

**Step 1: Access Control Coverage Verification**
- Walk facility perimeter, identify all entry/exit points (count)
- Verify badge readers installed at all entry/exit points (count readers)
- Calculate coverage: (Reader count / Entry point count) × 100%
- Target: 100%
- Document in workbook: Sheet "Access Log Analysis", Coverage section

**Step 2: CCTV Coverage Verification**
- Count CCTV cameras (from CCTV system inventory)
- Verify cameras cover all mandatory areas:
  - All building entrances/exits: Yes/No per entrance
  - Server rooms: Yes/No per server room
  - Parking entrances: Yes/No
  - Reception: Yes/No
- Calculate coverage: (Covered areas / Required areas) × 100%
- Target: 100%
- Document in workbook: Sheet "CCTV Coverage"

**Step 3: CCTV Retention Verification**
- Log in to CCTV system (NVR or cloud platform)
- Check oldest footage date (navigate to earliest recording, note date)
- Calculate retention: Days between today and oldest footage
- Target: 90 days (critical facilities), 30 days (standard facilities)
- Document in workbook: Sheet "CCTV Coverage", Retention section

**Step 4: Intrusion Detection Coverage Verification**
- Count intrusion detection sensors (from intrusion system inventory)
- Verify sensors cover all required areas:
  - All perimeter doors: Yes/No per door
  - Ground-floor windows: Yes/No
  - Server rooms (motion sensors): Yes/No per room
- Calculate coverage: (Covered areas / Required areas) × 100%
- Target: 100%
- Document in workbook: Sheet "Intrusion Detection"

**Step 5: Testing Compliance Verification**
- Request test records from Facilities Manager:
  - Access control tests (quarterly - 1 test required this quarter)
  - CCTV recording verification (monthly - 3 tests required this quarter)
  - Intrusion detection sensor tests (monthly - 3 tests required this quarter)
- Verify tests completed on time (within 7 days of scheduled date)
- Calculate compliance: (Completed tests / Required tests) × 100%
- Target: 100%
- Document in workbook: Appropriate sheets, Testing section

**Step 6: Incident Review**
- Query incident management system: Physical security incidents (past 3 months)
- Count incidents by severity (low, medium, high)
- Target: <2 high-severity incidents per year (0-1 per quarter acceptable)
- Document in workbook: Sheet "Physical Security Incidents"

### 3.3 Environmental Protection Assessment (A.7.5)

**Use Workbook:** ISMS_Assessment_Environmental_Protection.xlsx

**Step 1: Fire Detection Coverage Verification**
- Count smoke detectors (from fire alarm system inventory)
- Calculate coverage area: Detector count × Coverage per detector (typically 500-1000 sq ft per detector)
- Verify coverage ≥ facility area (100% coverage)
- Document in workbook: Sheet "Fire Detection Status"

**Step 2: Fire Suppression Coverage Verification**
- Verify sprinkler system coverage (from sprinkler system documentation) OR gas suppression coverage (from gas suppression documentation)
- Target: 100% of facility area covered
- Document in workbook: Sheet "Fire Suppression Status"

**Step 3: Water Detection Coverage Verification**
- Count water sensors (from water detection system inventory)
- Identify at-risk areas (server rooms, below-grade facilities, under HVAC)
- Verify sensors installed in all at-risk areas
- Calculate coverage: (Covered at-risk areas / Total at-risk areas) × 100%
- Target: 100%
- Document in workbook: Sheet "Water Detection Coverage"

**Step 4: Temperature Monitoring Coverage Verification**
- Count temperature sensors (from environmental monitoring system inventory)
- Count server rooms / datacenters
- Verify all server rooms have temperature monitoring
- Calculate coverage: (Monitored server rooms / Total server rooms) × 100%
- Target: 100%
- Document in workbook: Sheet "Temperature/Humidity Monitoring"

**Step 5: Testing Compliance Verification**
- Request test records:
  - Fire alarm detector tests (semi-annual - 0 or 1 test required this quarter depending on schedule)
  - Fire alarm system test (annual - 0 or 1 test required this year)
  - Water sensor tests (monthly - 3 tests required this quarter)
  - Fire drill (annual or biennial - 0 or 1 drill required depending on schedule)
- Verify tests completed on time
- Calculate compliance: (Completed tests / Required tests) × 100%
- Target: 100%
- Document in workbook: Appropriate sheets, Testing section

**Step 6: Environmental Incident Review**
- Query incident management system: Environmental incidents (past 3 months)
- Count incidents by type (fire, flood, temperature) and severity
- Target: 0 major environmental incidents per quarter
- Document in workbook: Sheet "Environmental Threat Incidents"

### 3.4 Utility Resilience Assessment (A.7.11)

**Use Workbook:** ISMS_Assessment_Utility_Resilience.xlsx

**Step 1: UPS Infrastructure Verification**
- Count UPS units (physical inspection or inventory)
- Verify UPS capacity vs. protected load:
  - UPS capacity (kVA): [From UPS nameplate]
  - Protected load (kW): [From load calculation or actual measurement]
  - Headroom: (UPS capacity - Protected load) / UPS capacity × 100%
  - Target: >20% headroom (allows for growth)
- Verify UPS runtime meets requirement: [From quarterly UPS load test]
  - Target: 15 min (critical), 5 min (standard)
- Export UPS battery health (from UPS monitoring system): [% per UPS]
  - Target: >80% all UPS
- Document in workbook: Sheet "Power Infrastructure"

**Step 2: Generator Verification (If Applicable)**
- Verify generator present and operational (physical inspection)
- Request generator test records:
  - Monthly no-load tests (3 required this quarter)
  - Quarterly 50% load test (1 required this quarter)
  - Annual 100% load test (1 required this year, Q4 typically)
- Verify tests completed on time, no failures
- Calculate compliance: (Completed tests / Required tests) × 100%
- Target: 100%
- Document in workbook: Sheet "Power Infrastructure", Generator section

**Step 3: HVAC Infrastructure Verification**
- Count HVAC units (physical inspection or inventory)
- Verify HVAC capacity vs. IT load:
  - HVAC capacity (tons or BTU/hr): [From HVAC nameplate]
  - IT heat load (kW × 3.41 BTU/Watt): [From load calculation]
  - Headroom: (HVAC capacity - IT load) / HVAC capacity × 100%
  - Target: >20% headroom
- Verify HVAC redundancy (if N+1 required per policy):
  - Count HVAC units, verify N+1 configuration
- Document in workbook: Sheet "HVAC Infrastructure"

**Step 4: ISP Infrastructure Verification (Critical Facilities)**
- Verify dual ISP (if required per policy):
  - ISP 1: [Carrier name, bandwidth, SLA]
  - ISP 2: [Carrier name, bandwidth, SLA]
  - Diverse carriers: Yes/No
- Request ISP SLA reports (past 3 months, from each ISP)
- Verify uptime meets SLA: [Actual uptime % vs. SLA %]
- Request ISP failover test record (quarterly - 1 required this quarter)
- Verify failover test completed, successful
- Document in workbook: Sheet "Telecommunications Infrastructure"

**Step 5: Utility Failure Event Review**
- Query incident management system: Utility failure events (past 3 months)
- Count events by type (power, HVAC, ISP) and duration
- Analyze impact (downtime caused, workarounds used)
- Document in workbook: Sheet "Utility Failure Events"

### 3.5 Assessment Completion

**Complete Evidence Register:**
- In each workbook, "Evidence Register" worksheet
- Document all evidence sources:
  - Access control configuration document: \\fileserver\isms\physical-security\access-control-config.pdf
  - CCTV system inventory: \\fileserver\isms\physical-security\cctv-inventory.xlsx
  - UPS test logs: \\fileserver\isms\facilities\ups-tests\YYYY-QX\
  - (etc.)

**Sign-Off Workflow:**
1. **Assessor:** Complete all worksheets, save workbook
2. **Assessor:** Sign "Approval Sign-Off" worksheet, date
3. **Email to ISO:** Send workbooks to ISO for review (attachment or file server link)
4. **ISO:** Review workbooks (verify data accuracy, check calculations)
5. **ISO:** Sign "Approval Sign-Off" worksheet, date
6. **Email to CISO:** Send reviewed workbooks to CISO for approval
7. **CISO:** Review compliance scores, approve (or request remediation if <75%)
8. **CISO:** Sign "Approval Sign-Off" worksheet, date
9. **Final Save:** Save approved workbooks to: \\fileserver\isms\assessments\YYYY-QX\

### 3.6 Quarterly Reporting

**Generate Quarterly Assessment Report:**

**Report Contents (10-15 pages):**
1. **Executive Summary** (1 page)
   - Assessment period: [Quarter YYYY]
   - Overall compliance score: [XX%]
   - Score by control: A.7.4 [XX%], A.7.5 [XX%], A.7.11 [XX%]
   - Compliance status: ✅ Compliant (>90%), ⚠️ Needs Improvement (75-89%), ❌ Non-Compliant (<75%)

2. **Assessment Results Summary** (1 page)
   - Table: All metrics with target, actual, pass/fail
   - Example:
     | Metric | Target | Actual | Status |
     |--------|--------|--------|--------|
     | Access control coverage | 100% | 100% | ✅ |
     | CCTV retention | 90 days | 85 days | ❌ |
     | (etc.) | | | |

3. **Findings** (2-5 pages)
   - Non-compliance items (metrics that failed to meet target)
   - For each finding:
     - Description: What is non-compliant
     - Risk: What is the risk (e.g., "Inadequate CCTV retention may prevent incident investigation")
     - Root cause: Why non-compliant (e.g., "Storage capacity insufficient, circular recording deleting footage at 85 days")
     - Recommendation: How to remediate (e.g., "Add storage capacity to NVR, increase to 2 TB")

4. **Recommendations** (1-2 pages)
   - Prioritized remediation actions
   - For each recommendation:
     - Action: What to do
     - Responsible: Who (Facilities Manager, IT Operations, etc.)
     - Timeline: When (within 30 days, 90 days, etc.)
     - Estimated cost: If applicable ($500 for additional NVR storage)

5. **Trend Analysis** (1-2 pages)
   - Graphs: Compliance score trends (past 4 quarters)
   - Incident trends (past 4 quarters)
   - Improvement areas: Metrics that improved quarter-over-quarter
   - Concern areas: Metrics that declined quarter-over-quarter

6. **Evidence Summary** (1 page)
   - List of evidence collected (reference Evidence Register worksheets in workbooks)

**Distribution:**
- CISO (approval required before distribution)
- Executive Management (quarterly update)
- Internal Audit (compliance monitoring)
- Facilities Manager, Security Operations Manager, IT Operations Manager (operational awareness)

---

## 4. Annual Comprehensive Assessment

**Objective:** Audit-readiness assessment, all facilities, all controls, all requirements.

**Timeline:** Q4 (October/November, before year-end)

**Duration:** 2-5 days (depending on number of facilities)

### 4.1 Annual Assessment Scope

**Comprehensive Scope (vs. Quarterly):**
- All facilities (quarterly may assess subset of facilities on rotation)
- All requirements (quarterly focuses on high-risk metrics)
- Detailed evidence collection (document everything for audit)

**Annual-Specific Items:**
- Annual test records (fire alarm system test, generator 100% load test, structural inspection)
- Annual documentation updates (policies, procedures, floor plans)
- Third-party evidence (colocation provider SOC 2 reports, cloud provider certifications - if applicable)

### 4.2 Annual Assessment Procedure

**Follow Quarterly Assessment Procedure (Section 3) with additions:**

**Additional Step 1: Third-Party Evidence Collection (Cloud/Colocation)**
- If cloud-only organization:
  - Request updated cloud provider SOC 2 Type II report (AWS, Azure, GCP)
  - Review physical and environmental protection controls section
  - Verify no adverse findings
  - Document in POL-S5 Evidence Register
- If colocation facility:
  - Request updated colocation provider SOC 2 Type II report
  - Request colocation provider SLA reports (past 12 months)
  - Review physical/environmental/utility sections
  - Verify no adverse findings, SLA compliance
  - Document in POL-S5 Evidence Register

**Additional Step 2: Documentation Review**
- Review all policies and procedures for accuracy:
  - POL-S2, POL-S3, POL-S4, POL-S5 (any updates required?)
  - IMP-S1, IMP-S2, IMP-S3, IMP-S4 (any updates required based on operational changes?)
- Review floor plans (access control, CCTV, intrusion detection, environmental sensors):
  - Are floor plans current? (reflect recent facility changes, equipment additions)
  - Update floor plans if needed
- Review Evidence Register:
  - Are all evidence locations current and accessible?
  - Test evidence retrieval (select 5 random items, verify retrievable within 24 hours)

**Additional Step 3: Annual Testing Verification**
- Verify annual-specific tests completed:
  - Fire alarm system test (annual professional inspection)
  - Generator 100% full load test (annual)
  - Sprinkler system inspection (annual professional inspection)
  - Gas suppression system test (annual functional test - if applicable)
  - Structural inspection (every 5 years - verify current or schedule if due)

### 4.3 Annual Reporting

**Generate Annual Comprehensive Report:**

**Report Contents (20-30 pages):**
1. **Executive Summary** (1-2 pages)
   - Similar to quarterly executive summary
   - Year-over-year comparison (this year vs. last year overall score)

2. **Assessment Results** (5-10 pages)
   - Detailed results per control (A.7.4, A.7.5, A.7.11)
   - All metrics with year-end status

3. **Findings and Recommendations** (5-10 pages)
   - All non-compliance items identified during year
   - Remediation actions completed, in progress, planned

4. **Trend Analysis** (2-5 pages)
   - 12-month trend charts (all metrics)
   - Incident analysis (annual totals, incident types, root causes)

5. **Audit Readiness** (2-5 pages)
   - Summary of evidence collected (prove audit-readiness)
   - Gap analysis (any remaining gaps before external audit)
   - Recommended timeline for external audit (if ready, or remediation needed first)

6. **Next Year Plan** (1-2 pages)
   - Planned improvements (new equipment, facility upgrades, testing frequency increases)
   - Budget forecast (capital expenses, operational expenses)

**Distribution:**
- Board of Directors (if applicable - annual governance update)
- Executive Management (annual comprehensive review)
- External Auditors (if preparing for ISO 27001 certification audit)
- All stakeholders from quarterly distribution

---

## 5. Assessment Workbook Usage

### 5.1 General Workbook Instructions

**Opening Workbook:**
- Open from file server: \\fileserver\isms\assessments\templates\ (use template for new assessment)
- OR: Open previous assessment, "Save As" new name (preserves previous data for comparison)

**Data Entry:**
- Yellow cells: Data entry required (fill in measured values)
- Green cells: Formulas (auto-calculated, do not edit)
- Example rows (first 10 rows): Pre-filled examples (can be deleted after understanding format)

**Emoji Dropdowns:**
- ✅ Compliant / Pass
- ❌ Non-Compliant / Fail
- ⚠️ Warning / Needs Improvement
- ⏳ In Progress

**Conditional Formatting:**
- Green highlight: Metric meets target (compliant)
- Red highlight: Metric fails to meet target (non-compliant)
- Yellow highlight: Metric close to target (warning)

### 5.2 Workbook-Specific Instructions

**ISMS_Assessment_Access_Monitoring.xlsx:**
- Sheet "Access Log Analysis": Enter access event counts (total entries, failed attempts, after-hours)
- Sheet "CCTV Coverage": Enter camera count, required area count, retention days
- Sheet "Intrusion Detection": Enter sensor count, protected area count, alarm counts
- Sheet "Physical Security Incidents": Enter incident details (date, type, severity, resolution)
- Overall A.7.4 Score: Auto-calculated on "Cover Sheet"

**ISMS_Assessment_Environmental_Protection.xlsx:**
- Sheet "Fire Detection Status": Enter detector count, facility area, test compliance
- Sheet "Fire Suppression Status": Enter suppression type, coverage area, inspection compliance
- Sheet "Water Detection Coverage": Enter sensor count, at-risk area count
- Sheet "Temperature/Humidity Monitoring": Enter sensor count, server room count, excursion count
- Overall A.7.5 Score: Auto-calculated on "Cover Sheet"

**ISMS_Assessment_Utility_Resilience.xlsx:**
- Sheet "Power Infrastructure": Enter UPS specifications, battery health, generator test compliance
- Sheet "HVAC Infrastructure": Enter HVAC specifications, capacity utilization
- Sheet "Telecommunications Infrastructure": Enter ISP details, SLA compliance, failover test results
- Sheet "Utility Failure Events": Enter failure details (date, type, duration, impact)
- Overall A.7.11 Score: Auto-calculated on "Cover Sheet"

### 5.3 Common Workbook Errors

**#DIV/0! Error:**
- Cause: Division by zero (e.g., calculating coverage percentage when total areas = 0)
- Fix: Enter valid data in denominator cell (total areas count)

**Compliance Score Showing 0% (But Data Entered):**
- Cause: Formulas not calculating (Excel calculation mode set to "Manual")
- Fix: Press F9 (recalculate all) or File → Options → Formulas → Calculation Options → Automatic

**Conditional Formatting Not Highlighting:**
- Cause: Conditional formatting rules corrupted or deleted
- Fix: Use fresh template workbook (copy data from corrupted workbook to fresh template)

---

## 6. Dashboard Updates and Reporting

### 6.1 Dashboard Update Procedure

**Monthly Dashboard Update (After Monthly Automated Assessment):**
1. Open ISMS_Dashboard_Physical_Infrastructure.xlsx (previous month or template)
2. Update "Executive Dashboard" worksheet:
   - Enter current month metrics (failed access, temperature excursions, power uptime, HVAC uptime, ISP uptime)
   - Dashboard auto-calculates compliance scores
3. Update "Incident Trends" worksheet:
   - Add current month's incident counts
4. Save as: ISMS_Dashboard_Physical_Infrastructure_YYYY-MM.xlsx
5. Distribute: Email to CISO, Facilities Manager, Security Operations Manager

**Quarterly Dashboard Update (After Quarterly Manual Assessment):**
1. Open current dashboard
2. Update all worksheets with comprehensive quarterly data:
   - "Access Monitoring Metrics": Update coverage percentages, incident counts
   - "Environmental Protection Metrics": Update coverage percentages, excursion counts
   - "Utility Uptime Metrics": Update uptime percentages, battery health
3. Review "Recommendations" worksheet:
   - Add new recommendations (from quarterly assessment findings)
   - Update status of existing recommendations (complete, in progress, planned)
4. Save and distribute with quarterly report

**Annual Dashboard Update:**
- Similar to quarterly, but comprehensive year-end update
- Generate trend charts (12-month view)
- Archive previous year's dashboards: \\fileserver\isms\dashboards\archive\YYYY\

### 6.2 Dashboard Distribution

**Monthly:**
- CISO, Facilities Manager, Security Operations Manager (email with dashboard attachment)

**Quarterly:**
- Above + Executive Management, Internal Audit (as part of quarterly report)

**Annual:**
- Above + Board of Directors (if applicable), External Auditors (as part of annual report)

### 6.3 Dashboard Presentation Tips

**For Executive Presentations:**
- Focus on "Executive Dashboard" worksheet (1-page summary)
- Highlight: Overall compliance score, trend (improving/declining), top 3 findings
- Avoid: Technical details (UPS battery health %, sensor counts) unless specifically requested

**For Operational Reviews:**
- Deep dive into specific metrics (access monitoring, environmental, utility)
- Show trend charts (identify patterns, seasonal variations)
- Discuss: Root causes of incidents, effectiveness of remediation actions

**For Audit Evidence:**
- Present dashboard as summary of continuous compliance monitoring
- Reference: Assessment workbooks (detailed evidence behind dashboard metrics)
- Demonstrate: Monthly/quarterly/annual assessment frequency (audit rigor)

---

**END OF ISMS-IMP-A.7.4-5-11-S4**

---

*"Facilities assessment is not just annual paperwork. It's continuous compliance monitoring—monthly automated data collection, quarterly manual verification, annual comprehensive audits—all documented in standardized workbooks and dashboards, providing audit-ready evidence of ISO 27001:2022 physical infrastructure security compliance."*
