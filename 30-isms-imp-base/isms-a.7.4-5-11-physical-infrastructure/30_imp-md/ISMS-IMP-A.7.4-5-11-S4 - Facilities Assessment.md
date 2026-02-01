**ISMS-IMP-A.7.4-5-11-S4: Compliance Dashboard & Assessment Process**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.7.4: Physical Security Monitoring

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.7.4-5-11-S4 |
| **Version** | 1.0 |
| **Assessment Area** | Consolidated Physical Infrastructure Compliance - Dashboard & Assessment Process |
| **Related Policy** | ISMS-POL-A.7.4-5-11, Section 5 (Assessment & Verification Framework) |
| **Purpose** | Define assessment process (monthly/quarterly/annual) and consolidated compliance dashboard for Controls A.7.4, A.7.5, A.7.11 |
| **Target Audience** | Internal Audit, Facilities Management, Security Operations, Compliance Officers, CISO, External Auditors |
| **Assessment Type** | Process & Dashboard Specification |
| **Review Cycle** | Annual |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for Compliance Dashboard and assessment process | ISMS Implementation Team |

### Document Structure

This document consists of two parts:

- **PART I: USER COMPLETION GUIDE**
  - Assessment Process Overview
  - Monthly Automated Assessment
  - Quarterly Manual Assessment
  - Annual Comprehensive Assessment
  - Dashboard Usage
  - Quality & Approval

- **PART II: TECHNICAL SPECIFICATION**
  - Dashboard Workbook Structure
  - Assessment Integration
  - Reporting Templates
  - Audit Evidence Framework


---

# PART I: USER COMPLETION GUIDE

## Assessment Process Overview

### Purpose & Scope

**Assessment Name:** ISMS-IMP-A.7.4-5-11-S4 - Compliance Dashboard & Assessment Process

#### What This Assessment Framework Covers

This is the **CONSOLIDATED assessment framework** that brings together Controls A.7.4, A.7.5, and A.7.11 into a unified compliance view. This framework defines:

- **Assessment frequency:** Monthly automated, quarterly manual, annual comprehensive
- **Assessment process:** How to conduct each assessment type
- **Dashboard integration:** How individual assessments (S1, S2, S3) feed into unified dashboard
- **Reporting:** Monthly summary, quarterly report, annual comprehensive report
- **Evidence framework:** Audit-ready evidence collection across all physical infrastructure


#### Key Principle

This is NOT a separate assessment workbook - it's the **PROCESS** for conducting assessments and the **DASHBOARD** that consolidates results from:

- ISMS-IMP-A.7.4-5-11-S1 (Physical Monitoring Assessment)
- ISMS-IMP-A.7.4-5-11-S2 (Environmental Protection Assessment)
- ISMS-IMP-A.7.4-5-11-S3 (Utility Resilience Assessment)


#### How This Integrates with Individual Assessments

| Assessment | Focus | Frequency | Feeds Into Dashboard |
|------------|-------|-----------|---------------------|
| ISMS-IMP-A.7.4-5-11-S1 | Physical Monitoring (A.7.4) | Quarterly + Annual | Access control score, CCTV score, intrusion detection score |
| ISMS-IMP-A.7.4-5-11-S2 | Environmental Protection (A.7.5) | Quarterly + Annual | Fire detection score, water detection score, temperature monitoring score |
| ISMS-IMP-A.7.4-5-11-S3 | Utility Resilience (A.7.11) | Quarterly + Annual | Power infrastructure score, HVAC score, telecommunications score |
| **ISMS-IMP-A.7.4-5-11-S4** | **Compliance Dashboard** | **Monthly + Quarterly + Annual** | **Overall physical infrastructure compliance score, trends, incidents** |

### Assessment Types

#### Monthly Automated Assessment

**Duration:** 2-4 hours  
**Frequency:** First week of each month (assess previous month's data)  
**Scope:** Automated metrics only - no facility inspection required

**What's Assessed:**

- Access logs (failed access attempts, after-hours access)
- Temperature excursions (from environmental monitoring system)
- Utility uptime (power, HVAC, ISP uptime percentages)
- Incident counts (physical security, environmental, utility incidents)


**Deliverable:** 1-page monthly summary dashboard update

#### Quarterly Manual Assessment

**Duration:** 8-16 hours (depending on facility count)  
**Frequency:** End of quarter (March 31, June 30, September 30, December 31)  
**Scope:** Comprehensive assessment including facility inspections

**What's Assessed:**

- Complete ISMS-IMP-A.7.4-5-11-S1 (Physical Monitoring) assessment
- Complete ISMS-IMP-A.7.4-5-11-S2 (Environmental Protection) assessment
- Complete ISMS-IMP-A.7.4-5-11-S3 (Utility Resilience) assessment
- Testing compliance verification (monthly/quarterly tests current)
- Facility inspections (coverage verification, equipment condition)


**Deliverable:** Quarterly compliance report (5-10 pages) + updated dashboard

#### Annual Comprehensive Assessment

**Duration:** 20-30 hours (comprehensive audit-readiness assessment)  
**Frequency:** Q4 (October/November - before external audit typically scheduled Q1)  
**Scope:** Comprehensive assessment + audit preparation + documentation review

**What's Assessed:**

- All quarterly assessment items (comprehensive)
- Annual-specific testing (fire alarm annual test, generator full load test, sprinkler inspection)
- Documentation review (policies, procedures, floor plans current)
- Evidence register verification (all evidence retrievable)
- Colocation/cloud provider audit report review (if applicable)
- 12-month trend analysis (year-over-year comparison)


**Deliverable:** Annual comprehensive report (20-30 pages) + audit-ready evidence package

### Who Conducts Assessments

#### Assessment Roles

**Assessor (Primary):**

- **Monthly:** Facilities Manager or Security Operations staff
- **Quarterly:** Facilities Manager + Security Operations Manager (collaborative)
- **Annual:** Internal Audit (independent assessment for audit readiness)


**Reviewer (Secondary):**

- Security Operations Manager (monthly)
- CISO (quarterly/annual)


**Approver:**

- CISO (all assessments)


### Expected Outputs

Upon completion of this assessment framework, you will have:

1. ✅ **Monthly dashboard updates** - Tracking metrics month-over-month
2. ✅ **Quarterly compliance reports** - Comprehensive assessment results
3. ✅ **Annual audit report** - Audit-ready evidence package
4. ✅ **Consolidated compliance score** - Single score for Controls A.7.4/A.7.5/A.7.11
5. ✅ **Trend analysis** - 12-month trends identifying patterns
6. ✅ **Gap remediation tracking** - Status of all non-compliant items
7. ✅ **Evidence register** - All supporting documentation organized for audit
8. ✅ **Board/Executive reporting** - High-level summaries for governance

---

## Monthly Automated Assessment

### Purpose

Collect **automated metrics** (access logs, temperature data, utility uptime) without requiring facility inspections. This provides continuous compliance monitoring between quarterly manual assessments.

### Timeline

**Frequency:** First week of each month (assess previous month's data)  
**Duration:** 2-4 hours  
**Example:** First week of February, assess January data

### Data Collection Process

#### Step 1: Access Control Data (Control A.7.4)

**What to Collect:**

- Export 30-day access log from access control system (previous month)
- Format: CSV with columns: timestamp, user, door, result (granted/denied)


**What to Calculate:**
1. **Failed access attempts** (legitimate users denied due to insufficient privileges, anti-passback)

   - Filter: result = "denied" AND user is not "invalid badge" or "visitor"
   - Count: Number of failed attempts
   - Target: <5 per month


2. **After-hours access events** (successful access outside business hours)

   - Filter: timestamp outside 07:00-18:00 AND result = "granted"
   - Count: Number of after-hours accesses
   - Verify: Cross-check against after-hours access authorization list


**Document in Dashboard:**

- Failed access attempts: [Count] (✅ if <5, ❌ if ≥5)
- After-hours access: [Count] (verify all authorized)


#### Step 2: Environmental Monitoring Data (Control A.7.5)

**What to Collect:**

- Export 30-day temperature/humidity data from environmental monitoring system
- Format: CSV with columns: timestamp, sensor_id, location, temperature, humidity


**What to Calculate:**
1. **Temperature excursions** (temperature outside acceptable range)

   - Filter: temperature <18°C OR temperature >27°C
   - Count: Number of excursion events (continuous period outside range = 1 event)
   - Target: <5 excursions per month per facility


2. **Environmental incidents** (fire alarms, water damage, HVAC failures)

   - Query incident management system for environmental incidents in previous month
   - Count: Number of incidents
   - Target: 0 major incidents


**Document in Dashboard:**

- Temperature excursions: [Count] (✅ if <5, ⚠️ if 5-10, ❌ if >10)
- Environmental incidents: [Count] (✅ if 0, ❌ if >0 major)


#### Step 3: Utility Monitoring Data (Control A.7.11)

**What to Collect:**

- Export 30-day utility uptime data (UPS, HVAC, ISP uptime/downtime)
- UPS battery health reports (current battery health percentage)


**What to Calculate:**
1. **Power uptime** (UPS uptime percentage)

   - Calculate: (Total minutes - Downtime minutes) / Total minutes × 100%
   - Target: 99.99% (Tier 1 critical), 99.9% (Tier 2 standard)


2. **HVAC uptime** (HVAC system uptime percentage)

   - Calculate: (Total minutes - Downtime minutes) / Total minutes × 100%
   - Target: 99.9% (Tier 1), 99% (Tier 2)


3. **ISP uptime** (ISP circuit uptime percentage)

   - Calculate: Uptime % per ISP circuit
   - Target: ≥99.9% (verify meets ISP SLA)


4. **UPS battery health** (battery capacity percentage)

   - Extract: Current battery health % from UPS monitoring
   - Target: >80% for all UPS


**Document in Dashboard:**

- Power uptime: [XX.XX%] (✅ if ≥target, ❌ if <target)
- HVAC uptime: [XX.XX%] (✅ if ≥target, ❌ if <target)
- ISP uptime: [XX.XX%] (✅ if ≥target, ❌ if <target)
- UPS battery health: [List any UPS <80%] (✅ if all >80%, ❌ if any <80%)


### Dashboard Update Process

#### Step 1: Open Dashboard Workbook

**File:** ISMS_Dashboard_Physical_Infrastructure_YYYY-MM.xlsx  
**Location:** \\fileserver\isms\dashboards\ (or SharePoint)

**Option A:** Copy previous month's dashboard, save as new month  
**Option B:** Use dashboard template (if first time)

#### Step 2: Update Executive Dashboard Sheet

Navigate to "Executive Dashboard" worksheet.

**Update fields (yellow cells):**

- Assessment Month: [Month YYYY] (e.g., "January 2026")
- Failed Access Attempts: [Count from Step 1]
- Temperature Excursions: [Count from Step 2]
- Power Uptime: [XX.XX% from Step 3]
- HVAC Uptime: [XX.XX% from Step 3]
- ISP Uptime: [XX.XX% from Step 3]
- UPS Battery Health: [Pass/Fail based on Step 3]
- Environmental Incidents: [Count from Step 2]


**Formulas auto-calculate:**

- Overall Compliance Score (percentage)
- Month-over-month trend (improving/declining)
- Status indicators (green/amber/red)


#### Step 3: Update Incident Trends Sheet

Navigate to "Incident Trends" worksheet.

**Add row for current month:**

- Month: [Month YYYY]
- Physical Security Incidents: [Count - from access control system or incident management]
- Environmental Incidents: [Count - from Step 2]
- Utility Incidents: [Count - from utility monitoring or incident management]


**Chart auto-updates** showing 12-month incident trend

#### Step 4: Save Dashboard

**Save as:** ISMS_Dashboard_Physical_Infrastructure_YYYY-MM.xlsx  
**Example:** ISMS_Dashboard_Physical_Infrastructure_2026-01.xlsx

### Monthly Reporting

#### Generate 1-Page Monthly Summary

**Report Format:** Email body (not separate attachment) or PDF (1 page)

**Template:**

```
Subject: Physical Infrastructure Monthly Assessment - [Month YYYY]

To: CISO, Facilities Manager, Security Operations Manager

--- MONTHLY SUMMARY ---

Assessment Month: [Month YYYY]
Overall Compliance Score: [XX%]

Metrics Summary:
✅ Failed Access Attempts: [X] (target <5) - PASS
⚠️ Temperature Excursions: [X] (target <5) - WARNING
✅ Power Uptime: [XX.XX%] (target 99.99%) - PASS
✅ HVAC Uptime: [XX.XX%] (target 99.9%) - PASS
❌ ISP Uptime: [XX.XX%] (target 99.9%) - FAIL

Findings:

- Temperature excursions above target (7 events in Building A - HVAC capacity investigation required)
- ISP uptime below SLA (Primary ISP outage 15.01.2026, 45 minutes - ticket #12345 with ISP)


Recommendations:

- Schedule HVAC capacity assessment for Building A (Q1 2026)
- Review ISP SLA compliance with Primary ISP (request credit for outage)


Dashboard attached: ISMS_Dashboard_Physical_Infrastructure_2026-01.xlsx

Assessor: [Name], [Title]
Date: [DD.MM.YYYY]
```

**Distribution:**

- Email to: CISO, Facilities Manager, Security Operations Manager
- Attachment: Dashboard workbook


**Timeline:** Complete by 7th day of month

---

## Quarterly Manual Assessment

### Purpose

Conduct **comprehensive assessment** including facility inspections, testing compliance verification, and detailed analysis. This validates monthly automated metrics with hands-on verification.

### Timeline

**Frequency:** End of quarter (March 31, June 30, September 30, December 31)  
**Duration:** 8-16 hours (depending on number of facilities)  
**Example:** Q1 assessment conducted week of March 25-31

### Assessment Process

#### Week Before Quarter-End: Preparation

**Day -7 to -5:**
1. Schedule facility access (coordinate with Facilities Manager)
2. Prepare assessment workbooks (S1, S2, S3 - copy from templates or previous quarter)
3. Gather historical data:

   - Access control logs (last 90 days)
   - Environmental monitoring data (last 90 days)
   - Utility uptime reports (last 90 days)
   - Testing records (UPS tests, generator tests, fire alarm tests, ISP failover tests)

4. Review previous quarter's findings (verify remediation actions completed)

#### Quarter-End Week: Data Collection

**Day 1-2: Complete Individual Assessments (8-12 hours)**

Follow the detailed procedures in:

- **ISMS-IMP-A.7.4-5-11-S1** (Physical Monitoring Assessment) - Complete all sheets
- **ISMS-IMP-A.7.4-5-11-S2** (Environmental Protection Assessment) - Complete all sheets
- **ISMS-IMP-A.7.4-5-11-S3** (Utility Resilience Assessment) - Complete all sheets


**Output:** Three completed assessment workbooks (S1, S2, S3) with compliance scores

**Day 3: Facility Inspections (3-4 hours)**

**Physical walk-through of each facility:**
1. **Access control verification:**

   - Verify badge readers operational at all entry/exit points
   - Test sample badge reader (badge swipe → door unlock)
   - Check for blind spots (entry/exit points without access control)


2. **CCTV verification:**

   - Verify cameras online and recording (check NVR/VMS status)
   - Spot-check video quality (review sample footage)
   - Check for blind spots (coverage gaps)


3. **Intrusion detection verification:**

   - Verify alarm panel online and armed (check panel status)
   - Test sample sensor (if possible without triggering full alarm)


4. **Fire detection verification:**

   - Verify fire alarm panel online (check panel status)
   - Visual inspection of smoke detectors (no obstructions, no damage)


5. **Environmental protection verification:**

   - Verify water detection sensors in place (server rooms, below-grade areas)
   - Verify temperature sensors online and reading correctly


6. **Utility infrastructure verification:**

   - Verify UPS online and battery health acceptable (check UPS display)
   - Verify generator accessible and fuel level adequate (visual check)
   - Verify HVAC units running (listen for compressor, check airflow)


**Document findings:** Note any discrepancies between documented systems and physical reality

**Day 4: Dashboard Consolidation (2-3 hours)**

**Update Compliance Dashboard:**
1. Open ISMS_Dashboard_Physical_Infrastructure_QYYYY-QX.xlsx (quarterly dashboard)
2. Import compliance scores from S1, S2, S3 assessments:

   - Access Monitoring Score (from S1, Sheet 6 Summary Dashboard)
   - Environmental Protection Score (from S2, Sheet 5 Summary Dashboard)
   - Utility Resilience Score (from S3, Sheet 5 Summary Dashboard)

3. Dashboard auto-calculates overall physical infrastructure compliance score
4. Review trend charts (current quarter vs. previous quarters)
5. Document gaps identified during assessments

#### Week After Quarter-End: Reporting

**Day 5-7: Generate Quarterly Report (2-4 hours)**

**Report Structure (5-10 pages):**

1. **Executive Summary** (1 page)

   - Overall compliance score: [XX%]
   - Quarter-over-quarter trend: [Improving/Stable/Declining]
   - Key findings: [Top 3 findings requiring attention]
   - Recommendations: [Top 3 recommended actions]


2. **Assessment Results by Control** (2-4 pages)

   - **Control A.7.4 (Physical Monitoring):** [XX%] - [Summary of findings]
     - Access Control: [Score, key gaps if any]
     - CCTV: [Score, key gaps if any]
     - Intrusion Detection: [Score, key gaps if any]
   - **Control A.7.5 (Environmental Protection):** [XX%] - [Summary of findings]
     - Fire Detection/Suppression: [Score, key gaps if any]
     - Water Detection: [Score, key gaps if any]
     - Temperature Monitoring: [Score, key gaps if any]
   - **Control A.7.11 (Utility Resilience):** [XX%] - [Summary of findings]
     - Power Infrastructure: [Score, key gaps if any]
     - HVAC: [Score, key gaps if any]
     - Telecommunications: [Score, key gaps if any]


3. **Detailed Findings** (1-2 pages)

   - Non-compliant items (red status)
   - Partial compliance items (amber status)
   - Root causes identified


4. **Remediation Plan** (1-2 pages)

   - Immediate actions required (next 30 days)
   - Short-term actions (next 90 days)
   - Long-term actions (next 12 months)
   - Resource requirements (budget, personnel)


5. **Appendices**

   - Appendix A: Compliance scores detail (from S1, S2, S3 dashboards)
   - Appendix B: Evidence register summary (count of evidence items collected)


**Distribution:**

- CISO (primary recipient)
- Executive Management (quarterly governance update)
- Facilities Manager (operational owner)
- Security Operations Manager (monitoring owner)
- Internal Audit (compliance oversight)


**Timeline:** Complete within 10 days after quarter-end

---

## Annual Comprehensive Assessment

### Purpose

Conduct **audit-readiness assessment** - comprehensive evaluation of all physical infrastructure with focus on audit evidence collection, documentation review, and year-over-year analysis.

### Timeline

**Frequency:** Once per year, Q4 (October/November - ahead of typical Q1 external audit schedule)  
**Duration:** 20-30 hours (comprehensive)  
**Example:** Conducted October 15 - November 15

### Assessment Process

#### Weeks 1-2: Quarterly Assessment + Additional Items

**Days 1-4: Complete Full Quarterly Assessment**

- Follow all Quarterly Manual Assessment steps (above)
- Complete S1, S2, S3 assessments
- Conduct facility inspections
- Update dashboard


**Day 5-7: Annual-Specific Testing Verification**

**Verify annual tests completed (or overdue):**

1. **Fire Alarm System Annual Test**

   - Required: Professional inspection and testing by certified technician
   - Verify: Last test date within 12 months
   - Evidence: Test report from certified technician
   - If overdue: Flag as critical gap, schedule immediately


2. **Generator Full Load Test (100% Capacity)**

   - Required: Annual test at 100% load (vs. quarterly tests at 50% load)
   - Verify: Last test date within 12 months
   - Evidence: Generator test log showing 100% load achieved, runtime verified
   - If overdue: Flag as critical gap, schedule immediately


3. **Sprinkler System Inspection**

   - Required: Professional inspection by certified technician (flow test, pressure test)
   - Verify: Last inspection within 12 months
   - Evidence: Inspection report from certified technician
   - If overdue: Flag as critical gap, schedule immediately


4. **Gas Suppression System Test** (if applicable - datacenters with gas suppression)

   - Required: Annual functional test (verify discharge sequence without full release)
   - Verify: Last test date within 12 months
   - Evidence: Test report from gas suppression service provider
   - If overdue: Flag as critical gap, schedule immediately


5. **Structural Inspection** (building integrity)

   - Required: Every 5 years (or as required by local building codes)
   - Verify: Last inspection within 5 years
   - Evidence: Structural engineer report
   - If overdue: Flag for scheduling (not critical if <6 years overdue)


**Document in Annual Report:** Status of all annual-specific tests

#### Week 3: Documentation Review

**Day 8-10: Policy and Procedure Review (6-8 hours)**

**Review all physical infrastructure policies and procedures:**

1. **ISMS-POL-A.7.4-5-11** (Consolidated Policy)

   - Review: Policy current and accurate?
   - Check: Any operational changes requiring policy updates?
   - Verify: Regulatory applicability current (FINMA, DORA, NIS2 if applicable)


2. **Implementation Guides (IMP-S1, S2, S3, S4)**

   - Review: Procedures current and accurate?
   - Check: Any process changes requiring procedure updates?
   - Verify: Assessment workbooks match procedures


3. **Floor Plans and Diagrams**

   - Access control floor plans (badge reader locations)
   - CCTV floor plans (camera placements)
   - Intrusion detection floor plans (sensor locations)
   - Environmental sensor floor plans (temperature sensors, water sensors)
   - Fire detection floor plans (smoke detector locations)
   - Network diagrams (ISP connectivity, dual ISP paths)
   - Update: Any changes required (facility renovations, equipment moves)


**Document in Annual Report:** Summary of documentation review (current/outdated)

**Day 11-12: Evidence Register Verification (4-6 hours)**

**Verify all evidence retrievable:**

1. **Sample 10-20 evidence items** from Evidence Registers (S1, S2, S3)
2. **Attempt retrieval** from documented locations (network share, SharePoint)
3. **Verify evidence quality:**

   - Screenshots readable and show expected content
   - Testing logs complete and show dates claimed
   - Fire marshal inspection reports authentic (stamped/signed)
   - ISP SLA reports match contracted terms

4. **Document retrieval success rate:** [XX/20 retrieved successfully]
5. **Fix broken links:** Update Evidence Register with correct locations if any moved
6. **Flag missing evidence:** Critical gap if key evidence missing

**Document in Annual Report:** Evidence register verification results

#### Week 4: Colocation/Cloud Provider Audit Review (if applicable)

**If using colocation facilities or cloud providers:**

**Day 13-14: Third-Party Audit Report Review (4-6 hours)**

**Obtain and review audit reports:**

1. **Colocation provider audit reports:**

   - SOC 2 Type II report (covering physical security controls)
   - ISO 27001 certificate (if provider certified)
   - Fire marshal inspection (building-level)
   - Recent security assessments


2. **Cloud provider compliance documentation:**

   - AWS/Azure/GCP compliance certifications (ISO 27001, SOC 2)
   - Physical security white papers
   - Shared responsibility model documentation


**Review focus areas:**

- Physical access controls (badge systems, mantraps, security guards)
- Environmental protection (fire detection/suppression, cooling redundancy)
- Utility resilience (power redundancy, generator capacity, ISP connectivity)
- Verify no adverse findings in audit reports
- Verify provider controls meet ISO 27001:2022 A.7.4/A.7.5/A.7.11 requirements


**Document in Annual Report:** Third-party audit report summary

#### Week 5: Trend Analysis & Annual Reporting

**Day 15-18: 12-Month Trend Analysis (6-8 hours)**

**Analyze trends across entire year:**

1. **Monthly metrics trends (12 months):**

   - Failed access attempts (monthly count chart)
   - Temperature excursions (monthly count chart)
   - Power uptime (monthly percentage chart)
   - HVAC uptime (monthly percentage chart)
   - ISP uptime (monthly percentage chart)
   - Identify: Seasonal patterns, degrading trends, improvements


2. **Quarterly compliance scores (4 quarters):**

   - Overall compliance score (Q1, Q2, Q3, Q4)
   - Control A.7.4 score trend
   - Control A.7.5 score trend
   - Control A.7.11 score trend
   - Year-over-year comparison (this year Q4 vs. last year Q4)


3. **Incident analysis (12 months):**

   - Total incidents by type (physical security, environmental, utility)
   - Incident severity distribution (Critical, High, Medium, Low)
   - Top 5 incident root causes
   - Repeat incidents (same root cause multiple times)


**Document in Annual Report:** Trend analysis with charts

**Day 19-20: Generate Annual Comprehensive Report (8-10 hours)**

**Report Structure (20-30 pages):**

1. **Executive Summary** (2 pages)

   - Overall compliance score: [XX%] (annual average)
   - Year-over-year comparison: [This year vs. last year]
   - Key achievements: [Top 3 improvements]
   - Key challenges: [Top 3 persistent gaps]
   - Audit readiness assessment: [Ready / Remediation required]


2. **Assessment Results by Control** (5-10 pages)

   - Detailed results per control (A.7.4, A.7.5, A.7.11)
   - All facilities documented
   - All metrics with year-end status
   - Compliance score breakdown


3. **Findings and Recommendations** (5-10 pages)

   - All non-compliance items identified during year
   - Remediation actions: Completed, In Progress, Planned
   - Resource requirements (budget, personnel)
   - Timeline for remediation


4. **Trend Analysis** (3-5 pages)

   - 12-month trend charts (all metrics)
   - Seasonal patterns identified
   - Year-over-year comparison
   - Incident analysis (types, root causes, repeat incidents)


5. **Annual Testing Compliance** (2-3 pages)

   - Fire alarm annual test: [Date, Result]
   - Generator full load test: [Date, Result]
   - Sprinkler inspection: [Date, Result]
   - Gas suppression test: [Date, Result if applicable]
   - Structural inspection: [Date, Result if within 5 years]
   - Summary: All annual tests current? [Yes/No]


6. **Documentation Review** (2-3 pages)

   - Policy/procedure review summary
   - Floor plan currency
   - Evidence register verification results
   - Documentation gaps identified


7. **Third-Party Audit Review** (1-2 pages if applicable)

   - Colocation provider audit report summary
   - Cloud provider compliance documentation review
   - No adverse findings? [Yes/No]


8. **Audit Readiness Statement** (2-3 pages)

   - Summary of evidence collected (prove audit-readiness)
   - Gap analysis (any remaining gaps before external audit)
   - Recommended audit timeline (if ready, or remediation timeline if not ready)
   - Audit preparation checklist


9. **Next Year Plan** (2-3 pages)

   - Planned improvements (equipment upgrades, facility expansions)
   - Budget forecast (capital expenses, operational expenses)
   - Assessment process improvements (automation opportunities)


**Distribution:**

- **Board of Directors** (if applicable - annual governance update)
- **Executive Management** (C-suite - annual comprehensive review)
- **External Auditors** (if preparing for ISO 27001 certification audit)
- **Internal Audit** (audit evidence package)
- All stakeholders from quarterly distribution


**Timeline:** Complete within 30 days of starting annual assessment

---

## Dashboard Usage

### Dashboard Workbook Overview

**File:** ISMS_Dashboard_Physical_Infrastructure_YYYY-MM.xlsx (monthly) or _QYYYY-QX.xlsx (quarterly)

**Purpose:** Unified view of Controls A.7.4, A.7.5, A.7.11 compliance

**Sheets:**
1. **Instructions & Legend** - Assessment metadata and dashboard usage guide
2. **Executive Dashboard** - Consolidated compliance view with key metrics
3. **Gap Analysis** - Critical findings and remediation tracking
4. **KPIs & Metrics** - Performance indicators across all controls
5. **Evidence Register** - Consolidated audit evidence documentation
6. **Approval & Sign-Off** - Multi-level approval workflow

### How to Use Dashboard

#### Monthly Dashboard Update

**After completing Monthly Automated Assessment:**

1. Open previous month's dashboard (or template if first time)
2. Navigate to "Executive Dashboard" sheet
3. Update yellow input cells:

   - Assessment Month
   - Failed Access Attempts
   - Temperature Excursions
   - Power Uptime
   - HVAC Uptime
   - ISP Uptime
   - UPS Battery Health Status

4. Dashboard auto-calculates compliance score
5. Save as new month's dashboard
6. Distribute to CISO, Facilities Manager, Security Operations Manager

**Time Required:** 30-60 minutes

#### Quarterly Dashboard Update

**After completing Quarterly Manual Assessment:**

1. Open current quarter's dashboard
2. Import compliance scores from S1, S2, S3 assessment workbooks:

   - Access Monitoring Score (from S1 Summary Dashboard)
   - CCTV Score (from S1)
   - Intrusion Detection Score (from S1)
   - Fire Detection Score (from S2)
   - Water Detection Score (from S2)
   - Temperature Monitoring Score (from S2)
   - Power Infrastructure Score (from S3)
   - HVAC Score (from S3)
   - Telecommunications Score (from S3)

3. Navigate to "Gap Analysis" sheet, update findings and remediation status
4. Navigate to "KPIs & Metrics" sheet, update all performance indicators
5. Navigate to "Evidence Register" sheet, consolidate evidence from S1, S2, S3
6. Navigate to "Approval & Sign-Off" sheet, complete approval workflow
7. Dashboard auto-calculates overall compliance score
8. Save and attach to quarterly report

**Time Required:** 1-2 hours

### Dashboard Presentation Tips

**For Executive Presentations (Board/C-Suite):**

- Use "Executive Dashboard" sheet only (1-page summary)
- Focus on: Overall compliance score, trend (improving/declining), top 3 findings
- Avoid technical details unless specifically requested
- Time: 5-10 minute presentation


**For Operational Reviews (Facilities/Security teams):**

- Deep dive into "Metrics Detail" sheet
- Show trend charts from "Incident Trends" sheet
- Discuss root causes, remediation effectiveness
- Time: 30-60 minute review


**For Audit Evidence (Internal/External Auditors):**

- Present dashboard as summary of continuous compliance monitoring
- Reference S1, S2, S3 workbooks as detailed evidence
- Demonstrate monthly/quarterly/annual assessment rigor
- Time: Auditor-driven (provide dashboard + workbooks for auditor self-review)


---

## Quality & Approval

### Quality Checklist for Assessments

**Monthly Assessment:**

- [ ] All automated data collected (access logs, temperature data, utility uptime)
- [ ] Metrics calculated correctly (failed access, excursions, uptime percentages)
- [ ] Dashboard updated with current month
- [ ] Trends chart updated
- [ ] Monthly summary report generated
- [ ] Distributed to stakeholders by 7th day of month


**Quarterly Assessment:**

- [ ] S1, S2, S3 assessments completed (all sheets)
- [ ] Facility inspections conducted (all facilities)
- [ ] Testing compliance verified (monthly/quarterly tests current)
- [ ] Dashboard updated with quarterly scores
- [ ] Quarterly report generated (5-10 pages)
- [ ] Distributed to stakeholders within 10 days after quarter-end


**Annual Assessment:**

- [ ] Full quarterly assessment completed
- [ ] Annual-specific tests verified (fire alarm, generator full load, sprinkler, gas suppression)
- [ ] Documentation review completed (policies, procedures, floor plans)
- [ ] Evidence register verification completed (sample retrieval successful)
- [ ] Third-party audit reports reviewed (if applicable)
- [ ] 12-month trend analysis completed
- [ ] Annual comprehensive report generated (20-30 pages)
- [ ] Audit readiness statement included
- [ ] Distributed to Board/Executive/Auditors within 30 days


### Approval Workflow

**Monthly Assessment:**

- **Level 1:** Assessor (Facilities Manager or Security Operations staff)
- **Level 2:** CISO (review and approval)
- Timeline: Complete within 7 days of month-end


**Quarterly Assessment:**

- **Level 1:** Assessor (Facilities Manager + Security Operations Manager)
- **Level 2:** CISO (review and approval)
- **Level 3:** Executive Management (acknowledgment)
- Timeline: Complete within 10 days after quarter-end


**Annual Assessment:**

- **Level 1:** Assessor (Internal Audit - independent assessment)
- **Level 2:** Facilities Manager (operational verification)
- **Level 3:** CISO (executive approval)
- **Level 4:** Board of Directors (governance oversight if applicable)
- Timeline: Complete within 30 days


---

# PART II: TECHNICAL SPECIFICATION

## Dashboard Workbook Structure

### Workbook Overview

**File Name:** ISMS-IMP-A.7.4.S4_Compliance_Dashboard_YYYYMMDD.xlsx

**Generation:** Automated via Python script (generate_a74_4_compliance_dashboard.py)

**Sheet Count:** 6 worksheets

**Purpose:** Unified compliance view for Controls A.7.4, A.7.5, A.7.11

### Sheet Organization

| Sheet # | Sheet Name | Purpose | Type | Update Frequency |
|---------|------------|---------|------|------------------|
| 1 | Instructions & Legend | Dashboard usage guide and assessment metadata | Read-only Reference | Template only |
| 2 | Executive Dashboard | Consolidated compliance view with key metrics | Manual input + Formulas | Monthly/Quarterly |
| 3 | Gap Analysis | Critical findings and remediation tracking | Manual input | Quarterly |
| 4 | KPIs & Metrics | Performance indicators across all controls | Manual input + Formulas | Monthly/Quarterly |
| 5 | Evidence Register | Consolidated audit evidence documentation | Data Entry | Quarterly |
| 6 | Approval & Sign-Off | Multi-level approval workflow | Data Entry | Quarterly/Annual |

---

## Sheet-by-Sheet Specifications

### Sheet 1: Instructions & Legend

**Purpose:** Assessment metadata and dashboard usage guide

**Layout:**

**Row 1:** Header
- Merged cells A1:G1
- Text: "ISMS-IMP-A.7.4.S4 - Physical Infrastructure Compliance Dashboard\nISO/IEC 27001:2022 - Controls A.7.4/A.7.5/A.7.11: Physical Infrastructure Security"
- Style: Navy blue background, white bold text, 14pt, center-aligned

**Rows 3-11:** Document Information Table
- Document ID, Dashboard Type, Related Policies, Version, Generation Date, Generated By, Organization, Reporting Period
- User input fields (yellow): Generated By, Organization, Reporting Period

**Rows 13-17:** Dashboard Purpose
- Bullet points describing consolidation of physical infrastructure assessments

**Rows 18-30:** How to Use This Dashboard
- Navigation guidance for each sheet

### Sheet 2: Executive Dashboard

**Purpose:** Consolidated compliance view with key metrics

**Layout:**

**Section 1: Header (Rows 1-2)**
- Row 1: "Physical Infrastructure Security - Executive Dashboard"
- Row 2: "ISO/IEC 27001:2022 Controls A.7.4/A.7.5/A.7.11 - Assessment Period: [Specify Period]"

**Section 2: Overall Compliance (Rows 4-10)**

| Control | Compliance Score | Status | Critical Gaps | High Priority | Medium Priority |
|---------|-----------------|--------|---------------|---------------|-----------------|
| A.7.4 - Physical Security Monitoring | [XX%] | [Status] | [Count] | [Count] | [Count] |
| A.7.5 - Environmental Protection | [XX%] | [Status] | [Count] | [Count] | [Count] |
| A.7.11 - Utility Resilience | [XX%] | [Status] | [Count] | [Count] | [Count] |
| OVERALL PHYSICAL INFRASTRUCTURE | [XX%] | [Status] | [Total] | [Total] | [Total] |

**Section 3: Key Metrics (Rows 12-21)**

| Metric Category | Current Value | Target | Status | Trend |
|-----------------|---------------|--------|--------|-------|
| Access Control Coverage | [%] | 100% | [Status] | [Trend] |
| CCTV System Coverage | [%] | 100% | [Status] | [Trend] |
| Fire Suppression Readiness | [%] | 100% | [Status] | [Trend] |
| Power Uptime (UPS) | [%] | 99.99% | [Status] | [Trend] |
| HVAC Availability | [%] | 99.95% | [Status] | [Trend] |

**Conditional Formatting:**
- Status column: Green for Compliant, Amber for Partial, Red for Non-Compliant

### Sheet 3: Gap Analysis

**Purpose:** Critical findings and remediation tracking

**Layout:**

**Header Row:** "Physical Infrastructure Security - Gap Analysis"

**Column Headers:**

| Gap ID | Control | Finding | Severity | Impact | Current State | Required State | Remediation Action | Target Date |
|--------|---------|---------|----------|--------|---------------|----------------|-------------------|-------------|

**Columns:**
- Gap ID: Unique identifier (GAP-001, GAP-002, etc.)
- Control: A.7.4, A.7.5, or A.7.11
- Finding: Description of gap identified
- Severity: Critical (Red), High (Amber), Medium, Low
- Impact: High, Medium, Low
- Current State: Current configuration/status
- Required State: Policy requirement
- Remediation Action: What action required
- Target Date: Target completion date

**Conditional Formatting:**
- Severity: Red background for Critical, Orange for High

### Sheet 4: KPIs & Metrics

**Purpose:** Performance indicators across all controls

**Layout:**

**Header Row:** "Physical Infrastructure Security - KPIs & Metrics"

**Column Headers:**

| KPI | Measurement | Current | Target | Status | Trend | Notes |
|-----|-------------|---------|--------|--------|-------|-------|

**Sample KPIs:**
- Access Control System Uptime (Percentage)
- Failed Access Attempts (Count/Month)
- Visitor Policy Compliance (Percentage)
- CCTV System Availability (Percentage)
- Video Retention Compliance (Percentage)
- Environmental Alarms (Count/Month)
- Fire Drill Completion (Annual Count)
- Power Uptime (Percentage)
- Generator Test Success (Percentage)
- HVAC Uptime (Percentage)

**Conditional Formatting:**
- Status: Green if Met, Amber if Near, Red if Failed

### Sheet 5: Evidence Register

**Purpose:** Consolidated audit evidence documentation

**Layout:**

**Header Row:** "Physical Infrastructure Security - Evidence Register"

**Column Headers:**

| Evidence ID | Control | Evidence Type | Description | Collection Date | Collector | Location/Link | Status |
|-------------|---------|---------------|-------------|-----------------|-----------|---------------|--------|

**Columns:**
- Evidence ID: Unique identifier (EV-A74-001, EV-A75-001, EV-A711-001)
- Control: A.7.4, A.7.5, or A.7.11
- Evidence Type: Access Logs, CCTV Footage, Inspection Report, Test Results, etc.
- Description: What evidence demonstrates
- Collection Date: When evidence collected
- Collector: Who collected (input cell)
- Location/Link: Path to evidence file
- Status: Collected (checkmark indicator)

### Sheet 6: Approval & Sign-Off

**Purpose:** Multi-level approval workflow

**Layout:**

**Header Row:** "Physical Infrastructure Security Dashboard - Approval & Sign-Off"

**Rows 3-10:** Review and Approval Workflow

| Role | Name | Review Date | Approval Status | Signature/Comments |
|------|------|-------------|-----------------|-------------------|
| Physical Security Manager | [Input] | [Input] | [Input] | [Input] |
| Facilities Manager | [Input] | [Input] | [Input] | [Input] |
| IT Infrastructure Manager | [Input] | [Input] | [Input] | [Input] |
| CISO / Information Security Manager | [Input] | [Input] | [Input] | [Input] |
| Risk & Compliance Officer | [Input] | [Input] | [Input] | [Input] |

**Cell Styling:**
- Role column: Bold text, gray background
- Input cells: Yellow background


---

## Assessment Integration

### How Individual Assessments Feed Dashboard

**Monthly Automated Assessment:**

- Data flows: Raw metrics (access logs, temp data, uptime) → Dashboard "Executive Dashboard" sheet
- Manually entered into dashboard (no automated import)
- Frequency: Monthly


**Quarterly Manual Assessment:**

- Data flows: S1, S2, S3 compliance scores → Dashboard "Executive Dashboard" sheet
- Manually imported from S1/S2/S3 Summary Dashboards
- Frequency: Quarterly


**Data Flow Diagram:**

```
Monthly Data Sources
├── Access Control System → Access Logs Export → Dashboard (Failed Access Attempts)
├── Environmental Monitoring → Temp Data Export → Dashboard (Temperature Excursions)
└── Utility Monitoring → Uptime Reports → Dashboard (Power/HVAC/ISP Uptime)

Quarterly Assessments
├── ISMS-IMP-A.7.4-5-11-S1 (Physical Monitoring)
│   └── Summary Dashboard (Sheet 6) → Overall A.7.4 Score → Dashboard
├── ISMS-IMP-A.7.4-5-11-S2 (Environmental Protection)
│   └── Summary Dashboard (Sheet 5) → Overall A.7.5 Score → Dashboard
└── ISMS-IMP-A.7.4-5-11-S3 (Utility Resilience)
    └── Summary Dashboard (Sheet 5) → Overall A.7.11 Score → Dashboard

Dashboard Consolidation
└── Overall Physical Infrastructure Compliance Score = (A.7.4 × 0.35) + (A.7.5 × 0.35) + (A.7.11 × 0.30)
```

---

## Reporting Templates

### Monthly Summary Template

**Format:** Email body or 1-page PDF  
**Recipients:** CISO, Facilities Manager, Security Operations Manager

**Sections:**
1. Assessment Month
2. Overall Compliance Score
3. Metrics Summary (table with targets and actual values)
4. Findings (list any failed metrics)
5. Recommendations (immediate actions required)

### Quarterly Report Template

**Format:** 5-10 page document (Word or PDF)  
**Recipients:** Executive Management, Internal Audit, all monthly recipients

**Sections:**
1. Executive Summary (1 page)
2. Assessment Results by Control (2-4 pages)
3. Detailed Findings (1-2 pages)
4. Remediation Plan (1-2 pages)
5. Appendices (compliance scores detail, evidence register summary)

### Annual Comprehensive Report Template

**Format:** 20-30 page document (Word or PDF)  
**Recipients:** Board of Directors, Executive Management, External Auditors, Internal Audit

**Sections:**
1. Executive Summary (2 pages)
2. Assessment Results by Control (5-10 pages)
3. Findings and Recommendations (5-10 pages)
4. Trend Analysis (3-5 pages)
5. Annual Testing Compliance (2-3 pages)
6. Documentation Review (2-3 pages)
7. Third-Party Audit Review (1-2 pages if applicable)
8. Audit Readiness Statement (2-3 pages)
9. Next Year Plan (2-3 pages)

---

## Audit Evidence Framework

### Evidence Organization

**Folder Structure:**

```
\\fileserver\isms\assessments\
├── templates\
│   ├── ISMS_Assessment_Access_Monitoring_TEMPLATE.xlsx
│   ├── ISMS_Assessment_Environmental_Protection_TEMPLATE.xlsx
│   ├── ISMS_Assessment_Utility_Resilience_TEMPLATE.xlsx
│   └── ISMS_Dashboard_Physical_Infrastructure_TEMPLATE.xlsx
├── 2025\
│   ├── Q1\
│   │   ├── ISMS_Assessment_Access_Monitoring_2025-Q1.xlsx (S1)
│   │   ├── ISMS_Assessment_Environmental_Protection_2025-Q1.xlsx (S2)
│   │   ├── ISMS_Assessment_Utility_Resilience_2025-Q1.xlsx (S3)
│   │   ├── ISMS_Dashboard_Physical_Infrastructure_2025-Q1.xlsx
│   │   ├── Quarterly_Report_2025-Q1.pdf
│   │   └── Evidence\
│   │       ├── Sheet2_AccessControl\
│   │       ├── Sheet3_CCTV\
│   │       └── ... (evidence from S1, S2, S3)
│   ├── Q2\ (same structure)
│   ├── Q3\ (same structure)
│   └── Q4\ (same structure + Annual Report)
└── 2026\ (same structure)
```

### Evidence Retention

**Retention Periods:**

- Assessment workbooks (S1, S2, S3, S4): 3 years minimum
- Monthly dashboards: 3 years minimum
- Quarterly reports: 3 years minimum
- Annual reports: Permanent
- Supporting evidence (screenshots, logs, inspection reports): 3 years minimum


**Backup:**

- All evidence backed up weekly to offsite storage
- Annual reports backed up to permanent archive


### Audit Deliverable Package

**When preparing for external audit, provide:**

1. **Current Year Assessments:**

   - All 4 quarterly assessment workbooks (S1, S2, S3 for each quarter)
   - All 12 monthly dashboards
   - All 4 quarterly reports
   - Annual comprehensive report


2. **Evidence Register:**

   - Consolidated evidence register from all S1, S2, S3 assessments
   - Index of all evidence files (file name, location, what it demonstrates)


3. **Policies and Procedures:**

   - ISMS-POL-A.7.4-5-11 (Consolidated Policy)
   - ISMS-IMP-A.7.4-5-11-S1, S2, S3, S4 (Implementation Guides)


4. **Trending and Analysis:**

   - 12-month trend charts (all metrics)
   - Year-over-year comparison
   - Incident analysis summary


5. **Remediation Tracking:**

   - Gap remediation tracker (from Dashboard Sheet 5 "Recommendations")
   - Status of all identified gaps (Complete, In Progress, Planned)


**Audit Timeline:**

- External auditor typically requests evidence 2-4 weeks before on-site audit
- Prepare audit deliverable package during annual assessment (November)
- Keep updated through Q1 (typical audit season)


---

**END OF SPECIFICATION**

---

*"In some sort of crude sense, which no vulgarity, no humor, no overstatement can quite extinguish, the physicists have known sin."*
— J. Robert Oppenheimer

*Where bamboo antennas actually work.* 🎋
