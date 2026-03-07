<!-- ISMS-CORE:IMP:ISMS-IMP-A.7.11.S1-UG:framework:UG:a.7.4-5-11 -->
**ISMS-IMP-A.7.11.S1-UG - Utility Resilience Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.7.11: Supporting Utilities

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Utility Resilience Implementation |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.7.4-5-11-S3-UG |
| **Related Policy** | ISMS-POL-A.7.4-5-11-S3 (Physical Infrastructure) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.7.4 (Physical Security Monitoring) |
| **Document Creator** | Chief Information Security Officer (CISO) |
| **Document Owner** | CISO |
| **Created Date** | [Date] |
| **Version** | 1.0 |
| **Classification** | Internal |
| **Status** | Draft |

**Version History**:

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | [Date] | CISO | Initial implementation specification |

**Review Cycle**: Quarterly  
**Next Review Date**: [Effective Date + 90 days]

**Related Documents**:

- ISMS-POL-A.7.4-5-11-S3 (Physical Infrastructure)
- ISMS-IMP-A.7.4.S1 (Physical Monitoring Assessment)
- ISMS-IMP-A.7.4-5-11-S2 (Environmental Protection Implementation)

---

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.7.4-5-11-S3-TG.

---

## Workbook at a Glance

| # | Sheet Name | Purpose |
|---|-----------|---------|
| 1 | Instructions & Legend | How to use this workbook and understand the colour coding |
| 2 | Power Infrastructure | Assess power supply resilience and backup systems |
| 3 | HVAC | Evaluate heating, ventilation, and air conditioning systems |
| 4 | Telecommunications | Assess telecommunications resilience and redundancy |
| 5 | Evidence Register | Store and reference evidence supporting assessments |
| 6 | Summary Dashboard | Compliance status and key metrics overview |
| 7 | Approval Sign-Off | Management review sign-off and certification |

---

## Assessment Overview

### Purpose & Scope

**Assessment Name:** ISMS-IMP-A.7.4-5-11-S3 - Utility Resilience Assessment

#### What This Assessment Covers

This assessment documents the utility RESILIENCE infrastructure deployed in your facilities. This is the "WHAT utility backup systems do we have?" assessment that answers:

- What power protection systems are deployed? (UPS systems, backup generators, redundancy)
- What HVAC resilience systems are deployed? (redundant cooling units, capacity, monitoring)
- What telecommunications resilience systems are deployed? (dual ISP, diverse paths, failover)
- How are utility systems monitored? (real-time monitoring, alerting, dashboards)
- How are utility systems tested? (monthly UPS tests, generator load tests, ISP failover tests)
- What utility failure events have occurred? (power outages, HVAC failures, ISP outages)

#### Key Principle

This assessment is **completely vendor-agnostic and technology-independent**. You document YOUR specific systems (whatever you use - APC, Eaton for UPS; Generac, Kohler for generators; Carrier, Trane for HVAC; whatever ISPs you have), and verify capabilities against generic policy requirements from ISMS-POL-A.7.4-5-11, Section 4.

#### What You'll Document

**Power Infrastructure:**

- UPS systems (every UPS deployment across all facilities)
- UPS capacity (kVA rating, runtime at full load)
- Backup generators (capacity, fuel supply, runtime)
- Redundancy configuration (N, N+1, 2N)
- Testing records (monthly UPS self-tests, quarterly load tests, generator exercise)

**HVAC Infrastructure:**

- HVAC units (every cooling unit supporting server rooms/datacenters)
- Cooling capacity (BTU/kW ratings)
- Redundancy configuration (N, N+1, 2N cooling)
- Temperature monitoring and alerting
- HVAC failure procedures

**Telecommunications Infrastructure:**

- ISP circuits (primary and backup ISPs)
- Circuit types and bandwidth
- Diverse path verification (different carriers, different physical routes)
- Failover configuration (automatic BGP, manual failover)
- ISP failover testing

**Utility Monitoring:**

- Monitoring platforms (BMS, network monitoring, IoT platforms)
- Real-time monitoring coverage (power, HVAC, ISP)
- Alerting configurations (email, SMS, dashboards)
- Dashboard deployments

**Utility Failure Events:**

- Power outages and UPS/generator performance
- HVAC failures and temperature excursions
- ISP outages and failover performance
- Response times and impact

#### How This Relates to Other A.7.4-5-11 Assessments

| Assessment | Focus | Relationship to A.7.4-5-11-S3 |
|------------|-------|-------------------------------|
| ISMS-IMP-A.7.4.S1 | Physical Monitoring | Access control, CCTV, intrusion detection systems |
| ISMS-IMP-A.7.4-5-11-S2 | Environmental Protection | Fire, water, temperature protection systems |
| **ISMS-IMP-A.7.4-5-11-S3** | **Utility Resilience** | **UPS, generators, HVAC, ISP backup systems** |

This assessment (A.7.4-5-11-S3) focuses specifically on Control A.7.11 (Supporting Utilities). It complements assessments for A.7.4 (Physical Monitoring) and A.7.5 (Environmental Protection).

**Note:** There's overlap with environmental protection (HVAC provides temperature control documented in S2, HVAC resilience documented here in S3). This is intentional - both perspectives matter.

### Who Should Complete This Assessment

#### Primary Stakeholders

1. **Facilities Manager** - Overall utility infrastructure ownership
2. **Electricians** - UPS and generator expertise
3. **HVAC Technicians** - Cooling systems expertise
4. **IT Operations** - Network infrastructure and ISP management
5. **Network Engineers** - ISP redundancy and failover configuration
6. **Compliance Officers** - Audit requirements and evidence collection

#### Required Skills

- Understanding of UPS systems (capacity, runtime, battery maintenance)
- Familiarity with backup generators (capacity, fuel, testing)
- Knowledge of HVAC systems (cooling capacity, redundancy, monitoring)
- Understanding of ISP redundancy (dual ISP, BGP, failover)
- Understanding of facility criticality tiers (Tier 1 vs. Tier 2 requirements)
- Access to utility system admin consoles and testing records

#### Time Commitment

- **Initial assessment:** 10-15 hours (comprehensive review of all utility systems across facilities)
- **Quarterly updates:** 2-4 hours (update testing records, failure events, minor configuration changes)

### Expected Outputs

Upon completion, you will have:

1. ✅ **Complete system inventory** - Every UPS, generator, HVAC unit, ISP circuit documented
2. ✅ **Capacity assessment** - UPS runtime, generator runtime, HVAC capacity, ISP bandwidth documented
3. ✅ **Redundancy analysis** - N, N+1, 2N configuration documented per facility
4. ✅ **Testing compliance** - Monthly/quarterly testing records verified
5. ✅ **Monitoring status** - BMS integration, dashboard deployments, alerting configurations documented
6. ✅ **Failure event tracking** - Power outages, HVAC failures, ISP outages documented
7. ✅ **Performance metrics** - Response times, failover times, uptime percentages
8. ✅ **Gap analysis** - Identified gaps between deployed systems and policy requirements
9. ✅ **Evidence register** - Supporting documentation for audit
10. ✅ **Approved assessment** - Four-level approval workflow completed

---

## Prerequisites

### Information You'll Need

Before starting this assessment, gather:

#### 1. System Access

- Administrator access to all UPS systems (web interface, SNMP)
- Access to generator control panels and maintenance records
- Access to HVAC control systems (BMS if applicable, local controls)
- Access to network equipment (routers, firewalls for ISP configuration)
- Access to utility monitoring platforms (Nagios, Zabbix, PRTG, Datadog, BMS)
- Access to utility testing records and maintenance logs

#### 2. Documentation

- UPS system documentation (capacity specifications, battery age)
- Generator documentation (capacity specifications, fuel tank capacity)
- HVAC system documentation (cooling capacity specifications, unit counts)
- ISP contracts and SLAs (bandwidth, uptime guarantees)
- Network diagrams (ISP connectivity, diverse path documentation)
- Utility testing schedules and records

#### 3. Historical Data

- UPS testing logs (monthly self-tests, quarterly load tests - last 12 months)
- Generator testing logs (monthly exercise, quarterly load tests - last 12 months)
- HVAC maintenance records (filter changes, refrigerant checks, capacity tests)
- ISP uptime reports (from ISP SLA reports if available)
- Utility failure event logs (power outages, HVAC failures, ISP outages - last 12 months)
- Utility monitoring dashboards (current status)

#### 4. Policy Requirements

- ISMS-POL-A.7.4-5-11, Section 4 (Utility Resilience Requirements)
  - Section 4.1: Power Supply Resilience
  - Section 4.2: HVAC and Cooling Resilience
  - Section 4.3: Telecommunications Resilience
  - Section 4.4: Water Supply (if applicable)
  - Section 4.5: Utility Monitoring
  - Section 4.6: Utility Failure Testing

### Required Tools

- Microsoft Excel (2016 or later) for workbook completion
- Access to UPS web interfaces or SNMP monitoring tools
- Access to generator control panels (on-site)
- Access to HVAC control systems (BMS or local controls)
- Access to network equipment (routers, firewalls)
- Power meter (optional - if verifying UPS load)
- Screen capture tools (for evidence screenshots)

### Dependencies

This assessment has NO dependencies on other assessments - it can be completed independently.

However, outputs from this assessment are INPUT to:

- ISMS-IMP-A.7.4-5-11-S2 (Environmental Protection) - HVAC systems documented in both (temperature control in S2, HVAC resilience here in S3)

---

## Workflow

### High-Level Process

```
1. PREPARE
   ↓
2. INVENTORY SYSTEMS (Sheet 2: Power, Sheet 3: HVAC, Sheet 4: Telecom)
   ↓
3. ASSESS CAPACITY (UPS runtime, generator capacity, HVAC capacity, ISP bandwidth)
   ↓
4. VERIFY REDUNDANCY (N, N+1, 2N configurations)
   ↓
5. REVIEW TESTING RECORDS (Monthly UPS tests, generator exercises, ISP failover tests)
   ↓
6. DOCUMENT MONITORING (BMS, dashboards, alerting)
   ↓
7. REVIEW UTILITY FAILURES (power outages, HVAC failures, ISP outages)
   ↓
8. COLLECT EVIDENCE (Sheet 6: Evidence Register)
   ↓
9. REVIEW SUMMARY (Sheet 5: Summary Dashboard - automated scoring)
   ↓
10. QUALITY CHECK (Self-assessment against checklist)
    ↓
11. OBTAIN APPROVALS (Sheet 7: Approval Sign-Off)
    ↓
12. SUBMIT FOR AUDIT
```

### Detailed Step-by-Step

**Step 1: Preparation (Day 1 - 2 hours)**

- Read this Part I User Guide completely
- Review ISMS-POL-A.7.4-5-11, Section 4 requirements
- Gather all prerequisites (system access, documentation, testing records)
- Schedule time with Facilities Manager, Electricians, HVAC Technicians, Network Engineers
- Download or generate assessment workbook (Excel file)

**Step 2: System Inventory (Day 1-3 - 4-6 hours)**

- Open assessment workbook
- Complete Sheet 1 (Instructions & Legend) - organisation info, assessment date
- Complete Sheet 2 (Power Infrastructure) - inventory all UPS systems, generators, power redundancy
- Complete Sheet 3 (HVAC) - inventory all HVAC units, cooling capacity, redundancy
- Complete Sheet 4 (Telecommunications) - inventory all ISP circuits, bandwidth, diverse paths
- Document monitoring status (BMS integration, dashboards, alerting)

**Step 3: Capacity Assessment (Day 3-4 - 3-4 hours)**

- Calculate UPS runtime at current load (verify meets policy requirements - 15 min Tier 1, 5 min Tier 2)
- Calculate generator runtime based on fuel capacity (verify meets policy requirements - 24 hours Tier 1)
- Calculate HVAC capacity vs. current heat load (verify adequate cooling capacity)
- Verify ISP bandwidth adequate for current and projected usage
- Document capacity in respective sheets

**Step 4: Redundancy Verification (Day 4 - 2 hours)**

- Verify power redundancy configuration (N, N+1, 2N per facility tier)
- Verify HVAC redundancy configuration (N, N+1, 2N per facility tier)
- Verify ISP redundancy (dual ISP for critical facilities, single ISP with SLA for standard facilities)
- Verify diverse paths for dual ISP (different carriers, different physical routes)
- Document redundancy levels in respective sheets

**Step 5: Testing Records Review (Day 5-6 - 3-4 hours)**

- Review UPS testing records (monthly self-tests, quarterly load tests - verify all current)
- Review generator testing records (monthly exercise tests, quarterly load tests - verify all current)
- Review HVAC maintenance records (filter changes, refrigerant checks - verify regular maintenance)
- Review ISP failover testing records (quarterly tests for critical facilities with dual ISP)
- Document last testing dates and test results in respective sheets

**Step 6: Monitoring Documentation (Day 6 - 2 hours)**

- Verify utility monitoring platform deployed (BMS, Nagios, Zabbix, PRTG, Datadog)
- Verify UPS monitoring active (SNMP or cloud monitoring)
- Verify HVAC monitoring active (temperature sensors, BMS integration)
- Verify ISP monitoring active (ping tests, bandwidth monitoring)
- Document monitoring coverage and alerting configurations

**Step 7: Utility Failure Review (Day 7 - 2 hours)**

- Review power outage events (last 12 months)
- Review HVAC failure events (last 12 months)
- Review ISP outage events (last 12 months)
- Document UPS/generator performance during power outages (failover success, runtime achieved)
- Document HVAC failure impact (temperature excursions, duration)
- Document ISP outage impact (failover time if dual ISP, outage duration)

**Step 8: Evidence Collection (Day 7-8 - 2-3 hours)**

- Take screenshots of UPS web interfaces (capacity, battery health, current load)
- Take screenshots of generator control panels (fuel level, runtime hours)
- Take screenshots of HVAC control systems (unit status, temperature, capacity)
- Take screenshots of ISP monitoring (uptime, bandwidth utilization)
- Export UPS testing logs (monthly self-tests, quarterly load tests)
- Export generator testing logs (monthly exercise tests)
- Export ISP SLA reports (if available from ISP)
- Document evidence in Sheet 6 (Evidence Register)

**Step 9: Summary Review (Day 8 - 1 hour)**

- Review Sheet 5 (Summary Dashboard) - formulas automatically calculate compliance scores
- Verify compliance scores accurate
- Identify areas below threshold (red or amber status)
- Prepare gap remediation plan for non-compliant areas

**Step 10: Quality Check (Day 8 - 1 hour)**

- Complete self-assessment using Quality Checklist
- Verify all required fields completed
- Verify evidence register complete
- Verify formulas calculating correctly

**Step 11: Obtain Approvals (Day 9-14 - asynchronous)**

- Complete Sheet 7 (Approval Sign-Off) - Level 1: Assessor (you)
- Submit to Level 2: Facilities Manager
- After Level 2, submit to Level 3: CISO
- After Level 3, submit to Level 4: Compliance Officer

**Step 12: Submit for Audit**

- Assessment workbook is now audit-ready
- Provide to Internal Audit or External Auditors

---

## Completing Each Sheet

### Sheet 1: Instructions & Legend

**Purpose:** Assessment metadata and status legend

**What to Complete:**

- Assessment Date, Completed By, Organisation name
- Review status legend (green/amber/red)

**Time Required:** 5 minutes

### Sheet 2: Power Infrastructure

**Purpose:** Document all power protection systems (UPS, generators) and assess resilience

**Structure:** 100 data rows for documenting multiple facilities/systems

**What to Document (Per Facility):**

**Column A - Facility/System Name**
**Column B - UPS Vendor/Model:** "APC Smart-UPS SRT 10kVA", "Eaton 9PX 6kVA"
**Column C - UPS Capacity (kVA):** UPS nameplate rating
**Column D - UPS Runtime (Minutes):** Runtime at current load (or at full load if not yet deployed)
**Column E - UPS Redundancy:** Dropdown: "N (Single)", "N+1 (Parallel)", "2N (Dual)", "None"
**Column F - Backup Generator:** Dropdown: "Yes", "No", "N/A"
**Column G - Generator Capacity (kW):** Generator nameplate rating (if applicable)
**Column H - Generator Runtime (Hours):** Hours of runtime at full load based on fuel capacity
**Column I - Generator Fuel Type:** "Diesel", "Natural Gas", "Propane", "N/A"
**Column J - Last UPS Test Date:** Date of last quarterly UPS load test
**Column K - Last Generator Test Date:** Date of last monthly generator exercise test
**Column L - Power Monitoring:** Dropdown: "Yes - Real-time", "Partial", "No"
**Column M - Compliance Status:** Formula auto-calculates (green/amber/red)
**Column N - Notes**

**Compliance Logic:**

- Tier 1 critical facilities: UPS runtime ≥15 min, generator required, N+1 redundancy, testing current
- Tier 2 standard facilities: UPS runtime ≥5 min, generator optional, N configuration acceptable, testing current

**Time Required:** 45-60 minutes

### Sheet 3: HVAC

**Purpose:** Document all HVAC systems and assess cooling resilience

**Structure:** 100 data rows

**What to Document (Per Facility or HVAC Zone):**

**Column A - Facility/System Name**
**Column B - HVAC Vendor/Model:** "Carrier 30RB", "Trane CGAM"
**Column C - HVAC Unit Count:** Number of HVAC units
**Column D - Cooling Capacity (kW):** Total cooling capacity
**Column E - Current Heat Load (kW):** Actual heat load (IT equipment power consumption)
**Column F - Capacity Margin (%):** Formula: (Cooling Capacity - Heat Load) / Heat Load × 100
**Column G - HVAC Redundancy:** Dropdown: "N (Single)", "N+1", "2N", "None"
**Column H - Temperature Monitoring:** Dropdown: "Yes - Real-time", "Partial", "No"
**Column I - HVAC Monitoring:** Dropdown: "Yes - BMS", "Yes - Manual", "No"
**Column J - Last HVAC Maintenance:** Date of last maintenance
**Column K - Compliance Status:** Formula auto-calculates
**Column L - Notes**

**Compliance Logic:**

- Tier 1: N+1 redundancy required, real-time monitoring required, capacity margin >20%
- Tier 2: N configuration acceptable, monitoring recommended, capacity margin >10%

**Time Required:** 45-60 minutes

### Sheet 4: Telecommunications

**Purpose:** Document all ISP circuits and assess telecommunications resilience

**Structure:** 100 data rows

**What to Document (Per Facility):**

**Column A - Facility/System Name**
**Column B - Primary ISP:** ISP name and circuit type
**Column C - Primary Bandwidth (Mbps):** Contracted bandwidth
**Column D - Secondary ISP:** ISP name (if dual ISP), "None" if single ISP
**Column E - Secondary Bandwidth (Mbps):** Contracted bandwidth (if dual ISP)
**Column F - Diverse Path Verified:** Dropdown: "Yes - Different carriers + physical paths", "Partial - Different carriers only", "No", "N/A"
**Column G - Failover Configuration:** Dropdown: "Automatic - BGP", "Manual", "None", "N/A"
**Column H - Last Failover Test:** Date of last quarterly failover test (if dual ISP)
**Column I - ISP Monitoring:** Dropdown: "Yes - Real-time", "Partial", "No"
**Column J - Compliance Status:** Formula auto-calculates
**Column K - Notes**

**Compliance Logic:**

- Tier 1: Dual ISP required, diverse paths required, failover tested quarterly
- Tier 2: Single ISP with SLA acceptable

**Time Required:** 30-45 minutes

### Sheet 5: Summary Dashboard

**Purpose:** Automated compliance scoring and KPIs

**What to Review (Auto-Calculated):**

- Overall Compliance Score
- Power Infrastructure Score
- HVAC Score
- Telecommunications Score
- Utility Failure Metrics (power outages, HVAC failures, ISP outages last 12 months)
- Gap Summary

**Time Required:** 15-30 minutes review

### Sheet 6: Evidence Register

**Purpose:** Document all supporting evidence

**What to Document:**

- Evidence ID, Type, Description, Related Sheet/Item, File Name, Location, Collection Date

**Common Evidence:**

- UPS web interface screenshots
- Generator control panel photos
- HVAC system documentation
- ISP SLA reports
- Testing logs (UPS, generator, ISP failover)
- Utility monitoring dashboard screenshots

**Time Required:** 2-3 hours

### Sheet 7: Approval Sign-Off

**Purpose:** Four-level approval workflow

**Approval Levels:**

- Level 1: Assessor
- Level 2: Facilities Manager
- Level 3: CISO
- Level 4: Compliance Officer

**Time Required:** 5 minutes Level 1, then asynchronous

---

## Evidence Collection

### What Evidence to Collect

**1. Power Infrastructure Evidence**

- UPS web interface screenshots (capacity, battery health, current load, runtime remaining)
- Generator control panel photos (fuel level, runtime hours, alarms)
- UPS testing logs (monthly self-tests showing pass/fail, quarterly load tests showing runtime achieved)
- Generator testing logs (monthly exercise tests, quarterly load tests)
- Power redundancy diagrams (showing N, N+1, 2N configuration)

**2. HVAC Infrastructure Evidence**

- HVAC control system screenshots (unit count, status, capacity)
- Temperature monitoring screenshots (current temperature, alerts)
- HVAC maintenance records (filter changes, refrigerant checks, capacity tests)
- Cooling capacity calculations (heat load vs. cooling capacity)

**3. Telecommunications Evidence**

- ISP contracts and SLAs (bandwidth, uptime guarantees)
- ISP uptime reports (from ISP SLA reports if available)
- Network diagrams (dual ISP configuration, diverse paths)
- ISP failover testing logs (quarterly tests showing failover time)
- ISP monitoring screenshots (uptime, bandwidth utilization)

**4. Utility Monitoring Evidence**

- Utility monitoring dashboard screenshots (power, HVAC, ISP status)
- Monitoring platform configuration screenshots (alert settings)
- Sample monitoring alerts (email/SMS examples)

**5. Utility Failure Event Evidence**

- Power outage incident reports (UPS/generator performance, duration, impact)
- HVAC failure incident reports (temperature excursions, duration, resolution)
- ISP outage incident reports (failover performance, duration, impact)

### Evidence Storage

**Location:** \\server\ISMS\Assessments\A.7.4.3_Utility_Resilience\Evidence or SharePoint

**Organisation:** Evidence/Sheet2_Power/, Evidence/Sheet3_HVAC/, Evidence/Sheet4_Telecom/

**Retention:** 3 years minimum

---

## Common Pitfalls

### Pitfall 1: Confusing UPS Capacity with Runtime

**Problem:** Documenting UPS capacity (kVA) but not verifying actual runtime at current load

**Impact:** Assessment shows "10 kVA UPS" (sounds good) but runtime is only 3 minutes (below policy requirement of 5-15 minutes)

**How to Avoid:**

- UPS capacity (kVA) ≠ runtime
- Runtime depends on: UPS capacity, battery capacity, current load
- Verify runtime from UPS display or web interface (shows "X minutes remaining at current load")
- If runtime below requirement, either reduce load or add battery packs

### Pitfall 2: Assuming Generator "Works" Without Testing

**Problem:** Documenting "generator installed" but last test was 18 months ago

**Impact:** Generator may not start during actual power outage (battery dead, fuel stale, mechanical issues)

**How to Avoid:**

- Generator MUST be tested monthly (exercise test - run for 15-30 minutes)
- Generator MUST be tested quarterly under load (load test - actually power facility)
- If testing overdue, compliance status = Red
- Schedule testing immediately if overdue

### Pitfall 3: Ignoring HVAC Capacity Margin

**Problem:** Documenting HVAC capacity equals current heat load (0% margin)

**Impact:** Any equipment additions or HVAC unit failure results in overheating

**How to Avoid:**

- Calculate capacity margin: (Cooling Capacity - Heat Load) / Heat Load × 100%
- Policy requirement: >20% margin (Tier 1), >10% margin (Tier 2)
- If margin <10%, compliance status = Red, immediate action required (reduce load or add cooling)

### Pitfall 4: Claiming "Dual ISP" Without Diverse Paths

**Problem:** Documenting "Dual ISP" but both circuits from same carrier or same physical route

**Impact:** Single point of failure (carrier network outage, cable cut affects both circuits)

**How to Avoid:**

- Dual ISP requires: Different carriers AND different physical paths
- Verify with ISPs: Request diverse path documentation (different cable routes, different POPs)
- If same carrier or same path, diversity = "Partial" or "No", compliance status = Amber or Red

### Pitfall 5: Not Testing ISP Failover

**Problem:** Dual ISP configured but never tested (don't know if failover works)

**Impact:** During actual ISP outage, failover may not work (configuration error, BGP misconfiguration)

**How to Avoid:**

- ISP failover MUST be tested quarterly (policy requirement)
- Test procedure: Disconnect primary ISP, verify automatic failover (BGP) or perform manual failover, verify connectivity
- If failover never tested, compliance status = Amber or Red

### Pitfall 6: Missing Utility Failure Event Documentation

**Problem:** Not documenting actual utility failures (power outages, HVAC failures, ISP outages)

**Impact:** No data on system performance during actual events (did UPS/generator work? How long did HVAC failure take to resolve?)

**How to Avoid:**

- Document ALL utility failures from last 12 months
- Include: Event type, duration, UPS/generator performance, failover performance, impact, resolution
- If no failures, explicitly state "Zero utility failures in assessment period"

### Pitfall 7: Overlooking Battery Age

**Problem:** Documenting UPS exists but batteries are 6 years old (degraded capacity)

**Impact:** UPS runtime much shorter than nameplate rating (batteries provide only 50-60% of original capacity after 5 years)

**How to Avoid:**

- Check battery install date (UPS web interface or maintenance records)
- VRLA batteries: Replace every 3-5 years (policy recommendation)
- Lithium-ion batteries: Replace every 8-10 years
- If batteries >5 years old (VRLA), flag for replacement in Notes

### Pitfall 8: Not Integrating HVAC with Environmental Protection Assessment

**Problem:** HVAC documented in utility resilience (S3) but not coordinated with environmental protection (S2)

**Impact:** Conflicting data between assessments (S2 says temperature monitoring exists, S3 says no monitoring)

**How to Avoid:**

- HVAC appears in BOTH assessments: S2 (environmental protection - temperature monitoring), S3 (utility resilience - HVAC redundancy)
- Coordinate with environmental protection assessor
- Data should be consistent between assessments

### Pitfall 9: Formula Corruption

**Problem:** Accidentally overwriting formula cells

**How to Avoid:**

- Summary Dashboard and Compliance Status columns are FORMULA CELLS - do not edit
- If formula broken, refer to Part II Technical Specification

### Pitfall 10: Insufficient Evidence for Capacity Claims

**Problem:** Claiming "25 kW generator, 24-hour runtime" without evidence

**Impact:** Auditor cannot verify claims

**How to Avoid:**

- Capacity claims require evidence: Generator nameplate photo, fuel tank capacity calculation
- Runtime claims require evidence: Testing logs showing actual runtime achieved
- If no evidence, auditor will flag as unverified

---

## Quality Checklist

### Sheet 1: Instructions & Legend

- [ ] Assessment Date completed
- [ ] Completed By (name and role)
- [ ] Organisation name filled in

### Sheet 2: Power Infrastructure

- [ ] ALL facilities with UPS systems documented
- [ ] UPS vendor/model specified
- [ ] UPS capacity (kVA) accurate
- [ ] UPS runtime verified (from UPS display or web interface, not just nameplate)
- [ ] UPS redundancy configuration documented (N, N+1, 2N)
- [ ] Backup generator status accurate (Yes/No/N/A)
- [ ] Generator capacity and runtime documented (if applicable)
- [ ] Last UPS test date within 90 days (quarterly requirement)
- [ ] Last generator test date within 30 days (monthly exercise requirement)
- [ ] Power monitoring status verified
- [ ] Compliance status column showing green/amber/red
- [ ] Notes column completed for any amber/red status

### Sheet 3: HVAC

- [ ] ALL facilities with HVAC systems documented
- [ ] HVAC vendor/model specified
- [ ] HVAC unit count accurate
- [ ] Cooling capacity (kW) documented
- [ ] Current heat load estimated or measured
- [ ] Capacity margin calculated (auto-calculated if heat load entered)
- [ ] HVAC redundancy configuration documented
- [ ] Temperature monitoring status verified
- [ ] HVAC monitoring status verified (BMS or manual)
- [ ] Last HVAC maintenance date within 12 months
- [ ] Compliance status column showing green/amber/red
- [ ] Notes column completed for any amber/red status

### Sheet 4: Telecommunications

- [ ] ALL facilities with ISP circuits documented
- [ ] Primary ISP name and circuit type specified
- [ ] Primary bandwidth (Mbps) accurate
- [ ] Secondary ISP documented (if dual ISP) or "None" if single ISP
- [ ] Secondary bandwidth documented (if dual ISP)
- [ ] Diverse path verified (different carriers + physical paths, or N/A if single ISP)
- [ ] Failover configuration documented (Automatic BGP, Manual, or N/A)
- [ ] Last failover test date within 90 days (if dual ISP with failover)
- [ ] ISP monitoring status verified
- [ ] Compliance status column showing green/amber/red
- [ ] Notes column completed for any amber/red status

### Sheet 5: Summary Dashboard

- [ ] Overall Compliance Score displays
- [ ] Power Infrastructure Score displays
- [ ] HVAC Score displays
- [ ] Telecommunications Score displays
- [ ] Utility failure metrics display
- [ ] Gap summary auto-populates
- [ ] NO manual data entry in dashboard

### Sheet 6: Evidence Register

- [ ] At least 10 evidence items documented
- [ ] UPS web interface screenshots
- [ ] Generator testing logs
- [ ] HVAC system documentation
- [ ] ISP SLA reports or contracts
- [ ] Evidence files actually exist in documented location

**Evidence Minimum Requirements:**

- [ ] UPS configuration screenshot(s)
- [ ] UPS testing logs (monthly or quarterly)
- [ ] Generator testing logs (if applicable)
- [ ] HVAC capacity documentation
- [ ] ISP contract or SLA (showing bandwidth, uptime guarantee)
- [ ] Utility monitoring dashboard screenshot

### Sheet 7: Approval Sign-Off

- [ ] Level 1 (Assessor) completed
- [ ] Assessment ready for submission to Level 2 (Facilities Manager)

### Overall Quality

- [ ] No blank required fields
- [ ] No formula errors
- [ ] Consistent facility naming across sheets
- [ ] Dates in DD.MM.YYYY format
- [ ] Compliance status colors working
- [ ] Assessment tells complete story

### Final Checks

- [ ] Spell check completed
- [ ] Data accuracy spot-checked
- [ ] Evidence files spot-checked
- [ ] Second person review requested
- [ ] Assessment workbook saved in final location
- [ ] Evidence folder backed up

---

## Review & Approval

### Four-Level Approval Workflow

**Approval Sequence:** Assessor → Facilities Manager → CISO → Compliance Officer

### Level 1: Assessor (You)

**Responsibilities:**

- Complete all assessment sheets
- Collect all required evidence
- Perform self-assessment using Quality Checklist
- Complete Level 1 approval in Sheet 7

**Timeline:** Complete before submitting to Level 2

### Level 2: Facilities Manager

**Responsibilities:**

- Review all system inventories for completeness
- Verify capacity and runtime calculations accurate (UPS runtime, generator runtime, HVAC capacity margin)
- Verify testing records current (monthly generator tests, quarterly UPS tests, quarterly ISP failover tests)
- Spot-check evidence
- Complete Level 2 approval in Sheet 7

**Timeline:** 2-5 business days after receipt from Assessor

### Level 3: CISO

**Responsibilities:**

- Review Summary Dashboard (overall compliance score)
- Review gap summary
- Assess remediation resource requirements
- Approve remediation plan
- Complete Level 3 approval in Sheet 7

**Timeline:** 2-5 business days after Level 2 approval

### Level 4: Compliance Officer

**Responsibilities:**

- Review assessment for audit readiness
- Verify evidence completeness
- Certify assessment ready for audit
- Complete Level 4 approval in Sheet 7

**Timeline:** 1-3 business days after Level 3 approval

---

**END OF USER GUIDE**

---

*"Power is the foundation upon which all other controls rest."*
— Anon

<!-- QA_VERIFIED: 2026-03-01 -->
