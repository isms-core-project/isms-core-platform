**ISMS-IMP-A.8.17-S2 — Synchronization Verification Process & Assessment**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.17: Clock Synchronization

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.17-S2 |
| **Version** | 1.0 |
| **Assessment Area** | System-Level Time Synchronization Status & Drift Measurement |
| **Related Policy** | ISMS-POL-A.8.17 (Clock Synchronization Policy - Section 2.3, 2.4) |
| **Purpose** | Verify all systems are actively synchronized to approved time sources, measure time drift, identify synchronization failures |
| **Target Audience** | System Administrators, Network Engineers, Security Engineers, ISMS Officers, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Monthly or After Major Infrastructure Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Original Date] | Initial technical specification for synchronization verification procedures | Network Operations Manager |

### Document Structure

This document consists of two parts:

- **PART I: USER COMPLETION GUIDE** (Sections 1-8)
  - How to complete the System Synchronization Status Assessment workbook
  - Prerequisites, workflow, field-by-field guidance
  - Platform-specific verification commands, evidence collection
  - Quality checks and approval process

- **PART II: TECHNICAL SPECIFICATION** (Sections 9-onwards)
  - Section A: Implementation Guidance (platform-specific sync verification procedures)
  - Section B: Assessment Workbook Specification (Excel workbook structure, formulas, validation rules)

---

# PART I: USER COMPLETION GUIDE

**Audience:** System Administrators, Network Engineers, ISMS Officers completing the System Synchronization Status Assessment

---

# Assessment Overview

## Purpose & Scope

**Assessment Name:** ISMS-IMP-A.8.17-S2 - System Synchronization Status Assessment

**What This Assessment Covers:**

This assessment verifies that ALL organizational systems are ACTUALLY SYNCHRONIZED to approved time sources. While S1 documents WHAT time sources exist, S2 proves WHETHER systems use them correctly. This answers critical questions:

- **Which systems are successfully synchronized?** (Status: Synced vs. Not Synced)
- **What is the current time drift across infrastructure?** (Measure offset from authoritative time)
- **Which systems are failing to synchronize?** (Identify broken NTP configurations)
- **Do we meet policy drift thresholds?** (±1s general, ±100ms security-critical, ±10ms high-precision)
- **Are synchronization failures being detected and remediated?**

**Key Principle:** "Configuration ≠ Synchronization." Having NTP configured does NOT mean it's working. This assessment PROVES synchronization through measurement.

Think of this as a health check - just like checking if every patient actually HAS a pulse (not just that they're registered in the system), this assessment checks if every system actually SYNCS to time sources (not just that they're configured to).

## What You'll Document

**Workbook Sheets You'll Complete:**

1. **System_Inventory** - All systems requiring time synchronization

   - System names, types (server, network device, etc.), OS/platform
   - NTP server configuration (which NTP servers configured)
   - **Sync status** (✅ Synced / ❌ Not Synced / ⚠️ Sync Failed / ❓ Unknown)
   - **Current time drift** (measured in milliseconds)
   - Last sync timestamp, last verification date
   - Compliance status per policy thresholds

2. **Drift_Analysis** - Statistical analysis across infrastructure

   - Average drift, median drift, maximum drift
   - Drift distribution (how many systems in each drift range)
   - Trend analysis (is drift improving or degrading over time?)
   - Systems exceeding policy thresholds

3. **Gaps_Failures** - Systems NOT synchronized or exceeding drift

   - Root cause analysis (NTP server unreachable, firewall blocking UDP 123, misconfiguration)
   - Severity rating (Critical for security systems, High for general systems)
   - Remediation plans with responsible party and target date
   - Tracking until resolution

4. **Compliance_Summary** - Overall sync compliance metrics

   - **Compliance score:** (Systems synced / Total systems) × 100%
   - Policy requirement status (≥95% sync compliance)
   - Gap summary and remediation tracking
   - Executive summary for management reporting

## How This Relates to Other A.8.17 Assessments

| Assessment | Focus | Relationship to A.8.17-S2 |
|------------|-------|---------------------------|
| ISMS-IMP-A.8.17-S1 | Time Source Infrastructure | Documents WHAT time sources exist |
| **ISMS-IMP-A.8.17-S2** | **System Synchronization Verification** | **Proves WHETHER systems sync to those sources (this assessment)** |

**Assessment Flow:**
1. **A.8.17-S1 (FIRST):** "We have NIST + Cloudflare as Stratum 1, plus 4 internal NTP servers"
2. **A.8.17-S2 (THIS):** "95% of systems (1,234 of 1,300) are syncing with drift <500ms"

You CANNOT complete S2 without S1! You need to know which NTP servers exist before verifying systems sync to them.

## Who Should Complete This Assessment

**Primary Stakeholders:**

1. **System Administrators** - Run verification commands on managed systems, collect sync status
2. **Network Engineers** - Troubleshoot NTP connectivity issues (firewall, routing)
3. **ISMS Officer** - Conduct compliance assessments, track gap remediation
4. **Security Operations** - Monitor sync status for security-critical systems (SIEM, auth servers)

**Required Skills:**

- **Basic Linux/Windows administration** - Can SSH to servers, run commands
- **Understanding of NTP verification** - Know how to read `chronyc tracking` or `w32tm /query /status` output
- **Familiarity with system inventory** - Know where to find list of all systems (asset management, CMDB)
- **Basic statistics** - Understand average, median, drift distribution

**You DON'T need to be an NTP expert!** The assessment provides exact commands to run for each platform.

## Time Commitment

- **Initial assessment (first time):** 6-10 hours for 100 systems
  - 2 hours: Obtain system inventory from asset management (A.5.9)
  - 3-5 hours: Run verification commands on all systems (manual or scripted)
  - 1 hour: Analyze drift data and identify gaps
  - 1 hour: Document gaps and create remediation plans
  - 1 hour: Gather evidence (command outputs, screenshots)

- **Monthly updates:** 2-3 hours for 100 systems
  - 1-2 hours: Run verification commands (can be automated)
  - 30 minutes: Update drift measurements
  - 30 minutes: Review and close remediated gaps

**Pro Tip:** Automate sync status collection using configuration management (Ansible, Puppet) or monitoring systems. First assessment is manual; subsequent assessments can be 80% automated.

## Expected Outputs

Upon completion, you will have:

1. ✅ **Complete system inventory** - All systems documented with sync status
2. ✅ **Drift measurements** - Current time offset for every system
3. ✅ **Compliance score** - % of systems synchronized within policy thresholds
4. ✅ **Drift analysis** - Statistical insights (average, median, distribution, trends)
5. ✅ **Gap identification** - All sync failures documented with root causes
6. ✅ **Remediation tracking** - Plans for every gap with target dates
7. ✅ **Evidence register** - Command outputs, screenshots for audit
8. ✅ **Management reporting** - Executive summary for CISO/management

**What This Looks Like for Audit:**

When an auditor asks: *"How do you know all systems are synchronized to approved time sources?"*

You hand them this assessment and say:

> "We verified 1,234 systems in our inventory. 1,173 systems (95%) are synchronized with drift <500ms. We identified 61 systems with sync issues documented in Sheet 3, of which 48 are already remediated, and 13 have remediation plans with target dates. All verification evidence is in the workbook."

**Auditor reaction:** ✅ "This demonstrates systematic verification. Excellent."

---

# Prerequisites

## Required Information

Before starting, gather the following:

**System Inventory:**

- [ ] **Complete list of all systems** from A.5.9 Asset Management (servers, network devices, workstations requiring logging)
- [ ] **Asset criticality ratings** (Critical, High, Medium, Low) to prioritize sync verification
- [ ] **System ownership** (System Owner for each system)

**NTP Infrastructure (from S1):**

- [ ] **List of internal NTP servers** from ISMS-IMP-A.8.17-S1 (you should have completed this FIRST)
- [ ] **Expected NTP server configurations** per system type (e.g., servers should use ntp1.dc1, ntp2.dc1)

**Access Requirements:**

- [ ] **SSH/console access** to all systems for running verification commands
- [ ] **Privileged credentials** (`sudo` on Linux, Administrator on Windows)
- [ ] **Network access** to reach systems remotely

## Required Tools

**Verification Commands** (covered in detail in Section 4.2):

- **Linux (chrony):** `chronyc tracking`, `chronyc sources`
- **Linux (ntp):** `ntpq -p`, `ntpstat`
- **Windows:** `w32tm /query /status`, `w32tm /query /peers`
- **Network devices:** Platform-specific commands or SNMP queries
- **Cloud:** Provider-specific APIs or built-in verification

**Optional Automation Tools:**

- Configuration management (Ansible, Puppet, Chef) for bulk command execution
- Monitoring systems (Nagios, Zabbix) with NTP service checks
- Custom scripts (Python, PowerShell) for parsing command outputs

## Policy Requirements to Review

Before starting, familiarize yourself with drift thresholds from **ISMS-POL-A.8.17 Section 2.3**:

**Maximum Acceptable Time Drift (ISMS Copilot Correction - Updated):**

- **General systems:** Target <500ms, Compliance Threshold ±1 second (±1000 milliseconds)
- **Critical security systems:** Target <50ms, Compliance Threshold ±100 milliseconds (SIEM, authentication, certificate validation)
- **High-precision requirements:** Target <5ms, Compliance Threshold ±10 milliseconds (financial systems, regulatory compliance)

**Compliance Target:**

- **≥95% of systems** must be synchronized within acceptable drift
- **100% of critical security systems** must be synchronized

**Verification Frequency (ISMS Copilot Correction):**

- **7 days**: Maximum age for compliance metric calculations
- **30 days**: Maximum policy threshold for compliance

You'll be measuring every system against these thresholds in the Compliance column.

---

# Assessment Workflow

## Recommended Completion Order

**PREREQUISITE:** Complete ISMS-IMP-A.8.17-S1 (Time Source Assessment) FIRST!

**STEP 1:** Obtain system inventory

- Export from A.5.9 Asset Management system
- Import into System_Inventory sheet (or manually add)
- Verify all in-scope systems are listed

**STEP 2:** For each system, run verification commands

- SSH/console to system
- Run platform-appropriate verification command (see Section 4.2)
- Record sync status (Synced / Not Synced / Unknown)
- Record current drift in milliseconds
- Record last sync timestamp

**STEP 3:** Document findings in System_Inventory sheet

- Fill in NTP Server(s) Configured column
- Fill in Sync Status (dropdown)
- Fill in Current Drift (ms)
- Fill in Last Sync Time
- Update Last Verified to today's date
- Auto-calculated Compliance status will populate

**STEP 4:** Review Drift_Analysis sheet

- Auto-calculated statistics from System_Inventory
- Identify outliers (systems with excessive drift)
- Check trend: is drift improving or degrading?

**STEP 5:** Document all gaps in Gaps_Failures sheet

- Every system with Sync Status = ❌ Not Synced or Compliance = ❌ Non-Compliant
- Root cause analysis (why is it not syncing?)
- Severity rating based on system criticality
- Remediation plan with responsible party and target date

**STEP 6:** Review Compliance_Summary

- Overall compliance score (target: ≥95%)
- If <95%, escalate to management
- Track remediation progress

**STEP 7:** Collect evidence

- Save command outputs (text files or screenshots)
- Document evidence locations in workbook

**STEP 8:** Internal review and approval

- Peer review for technical accuracy
- ISMS Officer review for compliance
- Submit for formal approval

## Data Collection Methods

**Manual Collection** (small environments, <50 systems):

- SSH to each system individually
- Run verification command
- Copy output to workbook manually

**Semi-Automated Collection** (medium environments, 50-500 systems):

- Use Ansible/Puppet to run commands on all systems
- Collect outputs to central location
- Parse outputs and populate workbook

**Fully Automated Collection** (large environments, >500 systems):

- Integrate with monitoring system (Nagios, Zabbix)
- Use monitoring system's NTP service checks
- Export monitoring data to CSV, import to workbook

**Recommended:** Start manual for first assessment to understand the process, then automate for monthly updates.

---

# Sheet-by-Sheet Completion Guidance

## Sheet: System_Inventory (Core Assessment Data)

**Purpose:** Document every system's NTP synchronization status and drift measurement.

**Column-by-Column Guidance:**

| Column | Field Name | Required? | Guidance | Where to Find This |
|--------|------------|-----------|----------|-------------------|
| A | **System Name [*]** | REQUIRED | Hostname of the system | Asset management, server inventory |
| | | | Example: `web-server-01.example.com`, `firewall-dc1`, `sql-db-prod` | DNS, configuration management |
| | | | **Tip:** Use FQDN for servers, descriptive names for network devices | |
| B | **Asset ID** | Optional | Unique asset identifier from A.5.9 Asset Management | Asset management system |
| | | | Example: `ASSET-12345`, `SRV-WEB-001` | CMDB, asset tags |
| C | **Type [*]** | REQUIRED | Select from dropdown | System type |
| | | | **Dropdown options:** 🖥️ Server-Physical \| 💻 Server-Virtual \| ☁️ Server-Cloud \| 🌐 Network Device \| 🔒 Security Appliance \| 💼 Workstation \| 📦 Container Host \| 🔌 IoT Device \| 📋 Other | |
| D | **OS/Platform** | Optional | Operating system or platform | System documentation |
| | | | Example: `Ubuntu 22.04`, `Windows Server 2022`, `Cisco IOS 15.2`, `FortiOS 7.0` | `uname -a`, `ver`, device CLI |
| E | **Criticality** | Optional | System criticality rating from A.5.9 | Asset management |
| | | | **Dropdown:** 🔴 Critical \| 🟠 High \| 🟡 Medium \| 🟢 Low | Determines acceptable drift threshold |
| | | | **Critical systems** = ±100ms max drift (SIEM, auth servers, cert authorities) | |
| F | **NTP Server(s) Configured [*]** | REQUIRED | Which NTP servers this system is configured to use | NTP config file, verification command |
| | | | Example: `ntp1.dc1.example.com, ntp2.dc1.example.com` | `/etc/chrony.conf`, `chronyc sources` |
| | | | **Should match servers from S1 assessment!** | Verify against S1 Internal_NTP_Servers |
| G | **Sync Status [*]** | REQUIRED | Current synchronization status | Run verification command (see Section 4.2) |
| | | | **Dropdown:** ✅ Synced \| ❌ Not Synced \| ⚠️ Sync Failed \| ❓ Unknown \| ➖ Excluded | Platform-specific command |
| | | | **ISMS Copilot Correction:** Need explicit criteria for each status (see table below) | |
| H | **Stratum** | Optional | Stratum level reported by system | Verification command output |
| | | | Example: `3` (synchronized to Stratum 2 internal NTP server), `16` (FAILURE) | `chronyc tracking`: "Stratum : 3" |
| | | | **Stratum 16 = NOT SYNCHRONIZED** (system is broken) | `ntpq -p`: Stratum column |
| I | **Current Drift (ms) [*]** | REQUIRED | Time offset from authoritative source in milliseconds | Verification command output |
| | | | **Positive values:** System clock is FAST (ahead of NTP time) | `chronyc tracking`: "System time" |
| | | | **Negative values:** System clock is SLOW (behind NTP time) | Convert seconds to ms: multiply by 1000 |
| | | | Example: `+245` (+245ms fast), `-89` (-89ms slow), `1250` (1.25s drift - NON-COMPLIANT) | `w32tm /stripchart`: Offset column |
| | | | **Format:** Enter as number only (positive or negative), no units | |
| J | **Last Sync Time** | Optional | Timestamp of last successful NTP sync | Verification command output |
| | | | Example: `2026-01-16 14:23:45 UTC` | `chronyc tracking`: "Ref time (UTC)" |
| | | | **Format:** YYYY-MM-DD HH:MM:SS TZ | System logs, monitoring data |
| K | **Last Verified [*]** | REQUIRED | Date YOU verified this system's sync status | Today's date when you run command |
| | | | **Format:** YYYY-MM-DD | Example: `2026-01-16` |
| | | | **ISMS Copilot Correction:** Update per verification frequency requirements: | |
| | | | - 7 days maximum for compliance metrics | ISMS-POL-A.8.17 Section 3.2 |
| | | | - 30 days maximum for policy compliance | |
| L | **Compliance** | Auto-Calculated | Auto-populated based on drift threshold and system criticality | Formula-driven |
| | | | **Formula logic:** | |
| | | | - If Sync Status = ✅ Synced AND Drift within threshold → ✅ Compliant | |
| | | | - If Sync Status = ❌ Not Synced OR Drift exceeds threshold → ❌ Non-Compliant | |
| | | | - If Sync Status = ⚠️ Sync Failed → ⚠️ Partial | |
| | | | **Thresholds:** General ±1000ms, Critical ±100ms, High-Precision ±10ms | |
| M | **Notes** | Optional | Any additional context or troubleshooting notes | Free text |
| | | | Example: `Firewall blocking UDP 123 to NTP server`, `Scheduled for NTP config update Q2` | Document issues, exceptions |

**ISMS Copilot Correction: Explicit Sync Status Criteria Table**

| Status | Criteria | Stratum | Drift | Last Sync | Reach |
|--------|----------|---------|-------|-----------|-------|
| **✅ Synced** | System actively synchronized | 2-15 | Within threshold | <24 hours | >50% |
| **⚠️ Sync Failed** | Syncing but degraded | 2-15 | Exceeds threshold | Any | >25% |
| **❌ Not Synced** | No synchronization | 16 | N/A | >24 hours OR never | 0% |
| **❓ Unknown** | Cannot verify | Unknown | Unknown | Unknown | Unknown |
| **➖ Excluded** | Intentionally excluded (documented exception) | Any | Any | Any | Any |

**How Many Rows to Complete:**

- **Minimum:** All systems from A.5.9 Asset Inventory requiring time sync
- **Typical:** 100-1000+ systems depending on organization size
- **Note:** This is a LARGE sheet - consider automated collection for >100 systems

**Policy Compliance Check:**

- [ ] All systems from asset inventory documented?
- [ ] All "Active" systems have Sync Status verified (not "Unknown")?
- [ ] All drift measurements current (Last Verified within 30 days)?
- [ ] Overall compliance ≥95% (auto-calculated in Compliance_Summary)?
- [ ] All critical security systems have Compliance = ✅ Compliant?

**Common Mistakes to Avoid:**

- ❌ **Marking Unknown as Synced** - If you can't verify, status is Unknown (not Synced)
- ❌ **Wrong drift units** - Enter milliseconds only (not seconds)
- ❌ **Stale data** - Re-verify every month, update Last Verified date
- ❌ **Missing systems** - Cross-check with A.5.9 asset inventory to ensure completeness
- ❌ **Ignoring Stratum 16** - This means NOT SYNCHRONIZED, status must be ❌ Not Synced

---

## Platform-Specific Verification Commands

**How to Verify Sync Status Per Platform:**

### Linux - chrony (Most Modern Distros)

**Primary Command:** `chronyc tracking`

**What to Look For:**
```bash
$ chronyc tracking
Reference ID    : A29FC87B (ntp1.dc1.example.com)
Stratum         : 3
Ref time (UTC)  : Thu Jan 16 14:23:45 2026
System time     : 0.000245321 seconds fast of NTP time  ← DRIFT (245ms)
Leap status     : Normal  ← Must be "Normal" for Synced status
```

**How to Complete Workbook:**

- **Sync Status:** "Leap status : Normal" AND Stratum < 16 → ✅ Synced
- **Current Drift:** "System time : 0.000245 seconds fast" → **+245** ms (positive = fast)
- **Last Sync Time:** "Ref time (UTC)" value
- **Stratum:** "Stratum : 3"

**Secondary Command:** `chronyc sources -v`

- Shows which NTP servers are being used
- Use for **NTP Server(s) Configured** column

---

### Linux - ntp (Older Distros)

**Primary Command:** `ntpq -p`

**What to Look For:**
```bash
$ ntpq -p
     remote           refid      st t when poll reach   delay   offset  jitter
==============================================================================
*ntp1.dc1.local  .GPS.            2 u   64 1024  377    0.234  -89.123   2.456
+ntp2.dc1.local  .GPS.            2 u  128 1024  377    0.456   92.567   3.123
```

**How to Complete Workbook:**

- **Sync Status:** `*` (asterisk) in first column means actively synced → ✅ Synced
- **Current Drift:** "offset" column in milliseconds → **-89** ms (negative = slow)
- **Stratum:** "st" column for the `*` server → `3`

**Alternative:** `ntpstat` (simpler output)
```bash
$ ntpstat
synchronised to NTP server (10.0.1.10) at stratum 3
   time correct to within 89 ms  ← DRIFT
```

---

### Windows - W32Time

**Primary Command:** `w32tm /query /status`

**What to Look For:**
```powershell
C:\> w32tm /query /status
Leap Indicator: 0(no warning)
Stratum: 3 (secondary reference - syncd by (S)NTP)
Source: ntp1.dc1.example.com  ← NTP server
Last Successful Sync Time: 1/16/2026 2:23:45 PM
```

**How to Complete Workbook:**

- **Sync Status:** "Source" shows NTP server (not "Local CMOS Clock") → ✅ Synced
- **Stratum:** "Stratum: 3"
- **Last Sync Time:** "Last Successful Sync Time" value

**For Drift Measurement:** `w32tm /stripchart /computer:ntp1.dc1.example.com /samples:1`
```powershell
C:\> w32tm /stripchart /computer:ntp1.dc1.example.com /samples:1
The current time is 1/16/2026 2:23:45 PM.
14:23:45, +00.0002450s  ← DRIFT (+245ms)
```

**Current Drift:** `+00.0002450s` = **+245** ms

---

### Network Devices (Cisco, Juniper, etc.)

**Cisco IOS:**
```cisco
Router# show ntp associations

  address         ref clock     st  when  poll reach  delay  offset   disp
*~10.0.1.10       .GPS.          2    64  1024  377  1.234 -89.123  2.456
```

- **Sync Status:** `*` before IP → ✅ Synced
- **Current Drift:** "offset" column → **-89** ms

**Juniper JunOS:**
```juniper
user@router> show ntp associations
     remote           refid      st t when poll reach   delay   offset  jitter
==============================================================================
*10.0.1.10        .GPS.            2 u   64 1024  377    1.234  -89.123   2.456
```

**Similar to Linux ntpq output**

---

### Cloud Platforms

**AWS (Amazon Time Sync Service):**

- Uses link-local IP `169.254.169.123`
- Verify with `chronyc sources` - should show 169.254.169.123
- No drift measurement available (trust AWS)
- **Sync Status:** If source is 169.254.169.123 and Leap status Normal → ✅ Synced

**Azure:**

- Uses platform NTP service
- Check VM settings: Time synchronization enabled
- Verify with `w32tm /query /status` (Windows) or `chronyc` (Linux)

**GCP:**

- Uses metadata server `metadata.google.internal`
- Verify with `chronyc sources` - should show metadata.google.internal

---

## Sheet: Drift_Analysis (Statistical Insights)

**Purpose:** Auto-calculated statistical analysis of time drift across all systems.

**THIS SHEET IS AUTO-CALCULATED** - You don't fill it in manually.

**What You'll See:**

**Overall Statistics:**

- **Total Systems Assessed:** Count of rows in System_Inventory
- **Systems Synced:** Count where Sync Status = ✅ Synced
- **Systems Not Synced:** Count where Sync Status = ❌ Not Synced
- **Sync Compliance %:** (Systems Synced / Total Systems) × 100%

**Drift Metrics (ISMS Copilot Correction - Updated Targets):**

- **Average Drift:** Mean time offset across all synced systems
  - **Target:** <500ms (updated from 250ms per Copilot correction)
  - **Threshold:** <1000ms (1 second)
- **Median Drift:** Middle value (50th percentile)
- **Maximum Drift:** Largest offset observed (positive or negative)
- **Standard Deviation:** Variability in drift measurements

**Drift Distribution:**
| Drift Range | System Count | Percentage |
|-------------|--------------|------------|
| 0-10ms | XX | XX% |
| 10-100ms | XX | XX% |
| 100-500ms | XX | XX% |
| 500-1000ms | XX | XX% |
| >1000ms (Non-Compliant) | XX | XX% |

**What to Review:**

1. **Is average drift acceptable?** Target: <500ms average for general systems (updated)
2. **Is there a wide distribution?** High standard deviation indicates inconsistent sync
3. **How many systems exceed thresholds?** Any system >1000ms is non-compliant
4. **Trend analysis:** Compare to previous month - improving or degrading?

**Red Flags:**

- ⚠️ Average drift >500ms (indicates systemic NTP issue)
- ⚠️ >10% of systems in >1000ms range (major compliance gap)
- ⚠️ Increasing drift over time (NTP infrastructure degrading)

---

## Sheet: Gaps_Failures (Gap Documentation & Remediation)

**Purpose:** Document all systems with synchronization failures or excessive drift, including root cause and remediation plans.

**Column-by-Column Guidance:**

| Column | Field Name | Guidance |
|--------|------------|----------|
| A | **Gap ID** | Sequential: GAP-001, GAP-002, etc. |
| B | **System Name** | Copy from System_Inventory where Compliance = ❌ or Sync Status = ❌ |
| C | **Issue Description** | Brief: "Not synchronized - Stratum 16", "Drift 1250ms exceeds threshold" |
| D | **Root Cause** | Why is it failing? (see common causes below) |
| E | **Severity** | Critical (security system) / High (general system) / Medium / Low |
| F | **Impact** | What breaks? "Cannot correlate logs", "Certificate validation may fail" |
| G | **Remediation Plan** | Specific actions: "Update NTP config to use ntp1.dc1, restart chronyd" |
| H | **Responsible** | Person/team: "Network Eng - John Smith", "System Admin Team" |
| I | **Target Date** | When will it be fixed? YYYY-MM-DD |
| J | **Status** | Open / In Progress / Completed / Deferred |

**Common Root Causes and Remediation:**

| Root Cause | How to Detect | Remediation |
|------------|---------------|-------------|
| **NTP server unreachable** | `chronyc sources` shows "?" for reach | Check firewall rules (allow UDP 123), verify network routing |
| **Wrong NTP server configured** | NTP server not in S1 approved list | Update config to use approved internal NTP servers |
| **Firewall blocking UDP 123** | Packets not reaching NTP server | Add firewall rule allowing UDP 123 outbound to NTP servers |
| **NTP service not running** | `systemctl status chronyd` shows inactive | Start and enable service: `systemctl enable --now chronyd` |
| **Stratum 16 (unsynchronized)** | `chronyc tracking` shows Stratum 16 | Check upstream NTP servers are reachable and working |
| **VM time sync conflict** | VMware VM with both guest tools and NTP enabled | Disable VMware Tools time sync OR disable NTP (not both) |
| **Excessive network latency** | Very high "delay" values in ntpq/chronyc | Check network path to NTP server, consider closer NTP server |
| **System clock far off** | Drift >1000 seconds | Manual time correction, then restart NTP service |

**ISMS Copilot Correction: Exception Process Reference**

For gaps that cannot be remediated within 90 days or require permanent exceptions, add reference to **ISMS-POL-A.8.17 Section 3.3** for formal exception process.

---

## Sheet: Compliance_Summary (Executive Summary)

**Purpose:** High-level compliance metrics and management reporting.

**THIS SHEET HAS BOTH AUTO-CALCULATED AND MANUAL SECTIONS**

**Auto-Calculated Metrics (ISMS Copilot Correction - Updated Table):**

| Metric | Target | Compliance Threshold | Actual | Status |
|--------|--------|---------------------|--------|--------|
| **Overall Sync Compliance** | ≥98% | ≥95% | XX% | ✅ PASS / ❌ FAIL |
| **Critical Systems Sync** | 100% | 100% | XX% | ✅ PASS / ❌ FAIL |
| **Average Drift** | <500ms | <1000ms | XXms | ✅ PASS / ⚠️ WARNING |
| **Critical System Drift** | <50ms | <100ms | XXms | ✅ PASS / ⚠️ WARNING |
| **Systems Within Threshold** | ≥98% | ≥95% | XX% | ✅ PASS / ❌ FAIL |
| **Open Gaps** | 0 | N/A | XX | N/A |

**Policy Requirements Compliance:**

| Requirement | Evidence | Status |
|-------------|----------|--------|
| All systems synced to approved sources (POL Section 2.3) | System_Inventory sheet | ✅ / ❌ |
| Drift within thresholds (POL Section 2.3) | Drift_Analysis sheet | ✅ / ❌ |
| Sync failures detected and alerted (POL Section 2.4) | Gaps_Failures sheet | ✅ / ❌ |

**Executive Summary** (Manual - YOU write this):

*Brief narrative for management (3-5 sentences):*

- Overall compliance status
- Number of systems assessed
- Key gaps identified
- Remediation timeline
- Any risks or escalations

**Example:**
> "Assessed 1,234 systems for NTP synchronization compliance. 1,173 systems (95%) are synchronized within policy thresholds. Identified 61 sync failures, of which 48 are already remediated. Remaining 13 gaps have remediation plans with target completion by 2026-02-28. No critical security systems have sync failures."

---

# Evidence Collection

## Required Evidence Types

**Configuration Evidence:**

- [ ] **Sample command outputs** - `chronyc tracking`, `w32tm /query /status` for representative systems
- [ ] **NTP config files** - Sample `/etc/chrony.conf` files showing NTP server configuration

**Verification Evidence:**

- [ ] **Sync status screenshots** - 5-10 examples showing successful sync verification
- [ ] **Drift measurements** - Command outputs showing time offset calculations
- [ ] **Monitoring dashboards** - If using automated monitoring, screenshot showing sync status

**Gap Evidence:**

- [ ] **Failure examples** - Command outputs showing Stratum 16 or "Not Synced" status
- [ ] **Remediation proof** - Before/after outputs showing gap closure

**Compliance Evidence:**

- [ ] **This completed assessment workbook** - With all sheets filled
- [ ] **Management approval** - Email or signature on Compliance_Summary

**ISMS Copilot Correction: Evidence Retention Period**

Updated to **12-month minimum with 36-month recommendation** (changed from 90 days). Store evidence for at least 12 months to support annual audits and compliance reviews.

## How to Collect Evidence

**For Command Outputs:**

Save command output to text file:
```bash
# Linux
chronyc tracking > evidence-sync-status-web01.txt
chronyc sources -v >> evidence-sync-status-web01.txt

# Windows
w32tm /query /status > evidence-sync-status-sql01.txt
w32tm /query /peers >> evidence-sync-status-sql01.txt
```

## Evidence Naming Convention

```
Evidence Type: SYNC-[SYSTEM]-[DATE].ext

Examples:
SYNC-web-server-01-20260116.txt       (Command output)
SYNC-screenshot-firewall-dc1-20260116.png  (Screenshot)
SYNC-drift-analysis-20260116.xlsx     (Export of Drift_Analysis sheet)
```

## Where to Store Evidence

**Options:**
1. **Embedded in workbook** - Add sheet called "Evidence" with file attachments
2. **Network share** - `\\fileserver\ISMS\Evidence\A.8.17\S2\2026-01\`
3. **Document management** - SharePoint, Confluence, etc.

**Recommendation:** Store centrally (option 2 or 3), reference paths in workbook.

**Retention:** Minimum 12 months, recommended 36 months.

---

# Common Pitfalls & How to Avoid Them

## Confusing "Configured" with "Synced"

**MISTAKE:**
System has NTP configured in `/etc/chrony.conf`, so you mark it as "✅ Synced" without verifying.

**WHY IT'S WRONG:**
Configuration ≠ Synchronization. NTP may be configured but firewall blocks UDP 123.

**HOW TO AVOID:**

- ALWAYS run verification command
- Check for "Leap status : Normal" or "Source: [NTP server]"
- If you can't verify, status is ❓ Unknown (not ✅ Synced)

## Wrong Drift Units

**MISTAKE:**
`chronyc tracking` shows "System time : 0.000245 seconds fast", you enter **0.000245**.

**WHY IT'S WRONG:**
Column expects milliseconds, not seconds.

**HOW TO AVOID:**

- Convert seconds to milliseconds: Multiply by 1000
- 0.000245 seconds × 1000 = **0.245** ms
- Enter **0.245** or round to **0.2**

## Ignoring Stratum 16

**MISTAKE:**
System shows Stratum 16, but you mark as ⚠️ Degraded.

**WHY IT'S WRONG:**
**Stratum 16 = UNSYNCHRONIZED.** This is hard failure.

**HOW TO AVOID:**

- If Stratum 16 → Status = ❌ Not Synced
- Investigate immediately
- Document in Gaps_Failures

## Stale Data

**MISTAKE:**
Copying drift measurements from 6 months ago.

**WHY IT'S WRONG:**
Drift changes over time. Old data doesn't reflect current sync status.

**HOW TO AVOID:**

- Re-run verification commands monthly
- Update "Last Verified" to current date
- Flag systems with "Last Verified" >30 days

## Missing Systems from Inventory

**MISTAKE:**
Assessing only "known NTP systems", missing workstations, network devices.

**WHY IT'S WRONG:**
Policy requires ALL information processing systems generating logs.

**HOW TO AVOID:**

- Start with A.5.9 Asset Inventory
- Cross-check: Every server, network device, security appliance
- Document exclusion exceptions

## Not Documenting Gaps

**MISTAKE:**
Assessment shows 15 systems not synced, but Gaps_Failures sheet is empty.

**WHY IT'S WRONG:**
Auditor sees non-compliance with no remediation plan.

**HOW TO AVOID:**

- Every system with ❌ or Compliance = ❌ → Document in Gaps_Failures
- Every gap needs: Root cause, severity, remediation, responsible, target date

---

# Quality Checklist

Before submitting for approval, verify:

**Data Completeness:**

- [ ] All systems from A.5.9 asset inventory documented
- [ ] All required fields (marked [*]) completed
- [ ] No systems with Sync Status = ❓ Unknown (verify all)
- [ ] All drift measurements in milliseconds (not seconds)
- [ ] All "Last Verified" dates within last 30 days (7 days for compliance metrics)

**Data Accuracy:**

- [ ] Sync status verified with platform-specific commands
- [ ] Drift measurements match command outputs
- [ ] NTP server configurations cross-checked with S1 assessment
- [ ] No Stratum 16 systems marked as Synced

**Policy Compliance:**

- [ ] Overall sync compliance ≥95%
- [ ] All critical security systems 100% compliant
- [ ] Average drift <500ms (updated target)
- [ ] All systems exceeding drift thresholds documented in Gaps_Failures

**Gap Documentation:**

- [ ] All non-compliant systems documented in Gaps_Failures
- [ ] All gaps have root cause analysis
- [ ] All gaps have remediation plans with target dates
- [ ] Critical/high gaps have responsible party assigned
- [ ] Permanent exceptions reference POL Section 3.3

**Evidence:**

- [ ] Sample command outputs collected (10+ examples)
- [ ] Evidence retention minimum 12 months (updated)

---

# Review & Approval Process

## Internal Review (Before Submission)

**Step 1: Self-Review**

- Use Quality Checklist above
- Spot-check 10% of systems

**Step 2: Peer Review** (Recommended)

- Have another System Administrator review

**Step 3: ISMS Officer Review** (Required)

- Verifies compliance aspects

## Formal Approval Workflow

**Level 1: System Administrator / Network Engineer**

- Reviews technical accuracy
- Sign-off: Compliance_Summary sheet

**Level 2: CISO**

- Reviews policy compliance
- Sign-off: Compliance_Summary sheet

**Level 3: Executive Management** (if Compliance <90%)

- Reviews risk acceptance
- Sign-off: Compliance_Summary sheet

## Approval Criteria

**Assessment will be APPROVED if:**

- All systems documented
- All required fields completed
- Compliance ≥95% OR documented risk acceptance
- All gaps have remediation plans
- Evidence collected

**Assessment will be REJECTED if:**

- Missing systems
- >5% systems Status = ❓ Unknown
- Compliance <90% with no risk acceptance
- Gaps without remediation plans

## Post-Approval

**After approval:**
1. File final version
2. Update ISMS tracking
3. Schedule next monthly assessment
4. Track gap remediation
5. Provide to auditors when requested

---

**END OF PART I: USER COMPLETION GUIDE**

---

# PART II: TECHNICAL SPECIFICATION

**Audience:** Workbook developers, Python script maintainers, technical implementers

**Note:** This section provides technical specifications. Users completing the assessment should refer to Part I above.

**PART II will be delivered separately due to file size constraints.**

---

**TO BE CONTINUED IN PART 2**
# PART II: TECHNICAL SPECIFICATION

**Audience:** Workbook developers, Python script maintainers, technical implementers

**Note:** This section provides technical specifications for synchronization verification and assessment workbook structure. Users completing the assessment should refer to Part I above.

---

# Implementation Requirement Mapping

**This section maps policy requirements (REQ-817-xxx codes) to ISMS-POL-A.8.17 sections for traceability.**

## S2 Requirements (REQ-817-009 through REQ-817-016)

| Requirement ID | Policy Section | Requirement Summary |
|---------------|----------------|---------------------|
| REQ-817-009 | Section 2.3 | All in-scope systems must synchronize to approved time sources |
| REQ-817-010 | Section 2.3 | Automated time correction enabled on all systems |
| REQ-817-011 | Section 2.3 | Maximum acceptable drift: ±1 second (general), ±100ms (critical security), ±10ms (high-precision) |
| REQ-817-012 | Section 2.3 | Synchronization status logged and auditable |
| REQ-817-013 | Section 2.4 | Synchronization failures detected and alerted within [timeframe] |
| REQ-817-014 | Section 2.4 | ≥95% of systems actively synchronized within acceptable drift |
| REQ-817-015 | Section 2.4 | 100% compliance for security-critical systems (SIEM, authentication, etc.) |
| REQ-817-016 | Section 2.4 | Monthly system synchronization status assessments conducted |

**Note:** Requirement codes REQ-817-001 through REQ-817-008 are used in S1 (Time Source Configuration). This document uses REQ-817-009 through REQ-817-016.

---

# SECTION A: Implementation Guidance

## Introduction

This section provides technical guidance for verifying time synchronization status across diverse platforms and measuring time drift.

**Purpose:** Enable system administrators to systematically verify NTP synchronization on all organizational systems per ISMS-POL-A.8.17.

**Scope:** Per-system synchronization verification, drift measurement, gap identification, and remediation tracking.

**Related Documents:**

- ISMS-POL-A.8.17 (Clock Synchronization Policy - Sections 2.3, 2.4)
- ISMS-IMP-A.8.17-S1 (Time Source Configuration - defines WHAT NTP servers exist)
- ISMS-POL-A.5.9 (Asset Management - defines system inventory)

---

## Platform-Specific Verification Commands

### Linux - chrony (RHEL 8+, CentOS 8+, Fedora, Ubuntu 20.04+)

**Primary Verification Command:**

```bash
chronyc tracking
```

**Expected Output (Synced):**
```
Reference ID    : A29FC87B (ntp1.dc1.example.com)
Stratum         : 3
Ref time (UTC)  : Thu Jan 16 14:23:45 2026
System time     : 0.000245321 seconds fast of NTP time
Last offset     : +0.000123456 seconds
RMS offset      : 0.000234567 seconds
Frequency       : 12.345 ppm slow
Residual freq   : +0.001 ppm
Skew            : 0.123 ppm
Root delay      : 0.001234567 seconds
Root dispersion : 0.000234567 seconds
Update interval : 64.5 seconds
Leap status     : Normal
```

**Key Fields to Extract:**

- **Reference ID:** Shows which NTP server is being used
- **Stratum:** Should be 3 (client of Stratum 2 internal NTP server)
  - If Stratum 16 → NOT SYNCHRONIZED (failure)
- **System time:** Time offset in seconds
  - Positive value = system clock FAST
  - Negative value = system clock SLOW
  - Convert to milliseconds: multiply by 1000
- **Leap status:** Must be "Normal" for proper sync
  - "Not synchronized" = failure

**How to Complete Workbook:**

- **Sync Status:** If Stratum < 16 AND Leap status = Normal → ✅ Synced
- **Stratum:** Value from "Stratum" line
- **Current Drift (ms):** "System time" value × 1000
  - Example: 0.000245 seconds × 1000 = **0.245 ms**
- **Last Sync Time:** "Ref time (UTC)" value

**Secondary Command (List NTP Sources):**

```bash
chronyc sources -v
```

**Output:**
```
  .-- Source mode  '^' = server, '=' = peer, '#' = local clock.
 / .- Source state '*' = current best, '+' = combined, '-' = not combined,
| /             'x' = may be in error, '~' = too variable, '?' = unusable.
||                                                 .- xxxx [ yyyy ] +/- zzzz
||      Reachability register (octal) -.           |  xxxx = adjusted offset,
||      Log2(Polling interval) --.      |          |  yyyy = measured offset,
||                                \     |          |  zzzz = estimated error.
||                                 |    |           \
MS Name/IP address         Stratum Poll Reach LastRx Last sample               
===============================================================================
^* ntp1.dc1.example.com          2   6   377    34   -245us[ -268us] +/-   12ms
^+ ntp2.dc1.example.com          2   6   377    36   +123us[ +100us] +/-   14ms
```

**Key Fields:**

- **MS column:** `^*` = currently selected source (actively syncing)
- **Reach column:** 377 (octal) = 100% reachability = all recent polls successful
  - < 377 = some packet loss
  - 0 = completely unreachable
- **Last sample:** Time offset in microseconds (us)

**Use For:**

- **NTP Server(s) Configured:** List servers shown in Name/IP column
- **Verify connectivity:** Check Reach column

---

### Linux - ntp (Older distributions: RHEL 7, CentOS 7, Debian 9, Ubuntu 18.04)

**Primary Verification Command:**

```bash
ntpq -p
```

**Expected Output (Synced):**
```
     remote           refid      st t when poll reach   delay   offset  jitter
==============================================================================
*ntp1.dc1.local  .GPS.            2 u   64 1024  377    0.234  -89.123   2.456
+ntp2.dc1.local  .GPS.            2 u  128 1024  377    0.456   92.567   3.123
```

**Key Symbols:**

- `*` (asterisk) = Currently selected sync source
- `+` (plus) = Good source, combined with selected
- `-` (minus) = Good source, not combined
- `x` = False ticker (not used)
- `~` = Too variable
- ` ` (blank) = Discarded

**Key Columns:**

- **st (Stratum):** Should be 2 or 3 for internal NTP servers
- **when:** Seconds since last poll
- **poll:** Polling interval in seconds
- **reach:** Octal value showing reachability (377 = perfect)
- **offset:** Time offset in MILLISECONDS (this is already in ms!)
- **jitter:** Variance in offset measurements

**How to Complete Workbook:**

- **Sync Status:** If `*` present → ✅ Synced
- **Stratum:** st column for `*` server (typically 3)
- **Current Drift (ms):** "offset" column value (already in milliseconds)
  - Example: -89.123 → **-89** ms (negative = slow)
- **NTP Server(s) Configured:** List all servers in "remote" column

**Alternative Simple Command:**

```bash
ntpstat
```

**Output (Synced):**
```
synchronised to NTP server (10.0.1.10) at stratum 3 
   time correct to within 89 ms
   polling server every 1024 s
```

**Output (Not Synced):**
```
unsynchronised
   polling server every 64 s
```

---

### Windows - W32Time

**Primary Verification Command:**

```powershell
w32tm /query /status
```

**Expected Output (Synced):**
```
Leap Indicator: 0(no warning)
Stratum: 3 (secondary reference - syncd by (S)NTP)
Precision: -23 (119.209ns per tick)
Root Delay: 0.0156250s
Root Dispersion: 0.0468750s
ReferenceId: 0x0A000110 (source IP:  10.0.1.16)
Last Successful Sync Time: 1/16/2026 2:23:45 PM
Source: ntp1.dc1.example.com
Poll Interval: 10 (1024s)
```

**Key Fields:**

- **Leap Indicator:** 0 = no warning (normal)
- **Stratum:** Should be 3 (client of Stratum 2)
- **Source:** NTP server being used
  - If "Local CMOS Clock" → NOT SYNCED
- **Last Successful Sync Time:** Recent timestamp indicates active sync

**How to Complete Workbook:**

- **Sync Status:** If Source = NTP server (not "Local CMOS Clock") AND Stratum < 16 → ✅ Synced
- **Stratum:** Value from "Stratum" line
- **Last Sync Time:** "Last Successful Sync Time" value
- **NTP Server(s) Configured:** "Source" value

**To Measure Drift:**

```powershell
w32tm /stripchart /computer:ntp1.dc1.example.com /samples:1
```

**Output:**
```
Tracking ntp1.dc1.example.com [10.0.1.10:123].
The current time is 1/16/2026 2:23:45 PM.
14:23:45, +00.0002450s
```

**Extract Drift:**

- `+00.0002450s` = +0.000245 seconds = **+0.245 ms** (positive = fast)

**Alternative (PowerShell):**

```powershell
Get-Service w32time | Select-Object Status
w32tm /query /configuration | Select-String "NtpServer"
```

---

### Network Devices - Cisco IOS

**Verification Command:**

```cisco
Router# show ntp associations

  address         ref clock     st  when  poll reach  delay  offset   disp
*~10.0.1.10       .GPS.          2    64  1024  377  1.234 -89.123  2.456
 ~10.0.1.11       .GPS.          2   128  1024  377  1.456  92.567  3.123
```

**Symbols:**

- `*` = Synchronized to this peer
- `~` = Peer is reachable (NTP packet received)

**Key Columns:**

- **st (Stratum):** Upstream server stratum
- **reach:** 377 (octal) = all polls successful
- **offset:** Time offset in MILLISECONDS
- **disp (dispersion):** Estimate of error

**How to Complete Workbook:**

- **Sync Status:** If `*` present → ✅ Synced
- **Stratum:** Typically 3 (client of Stratum 2 server)
- **Current Drift (ms):** "offset" column (already in ms)
- **NTP Server(s) Configured:** List addresses

**Show NTP Status:**

```cisco
Router# show ntp status
Clock is synchronized, stratum 3, reference is 10.0.1.10
```

---

### Network Devices - Juniper JunOS

**Verification Command:**

```juniper
user@router> show ntp associations
     remote           refid      st t when poll reach   delay   offset  jitter
==============================================================================
*10.0.1.10        .GPS.            2 u   64 1024  377    1.234  -89.123   2.456
+10.0.1.11        .GPS.            2 u  128 1024  377    1.456   92.567   3.123
```

**Same format as Linux ntpq output**

**Show NTP Status:**

```juniper
user@router> show ntp status
status=06b4 leap_none, sync_ntp, 11 events, event_peer/strat_chg,
version="ntpd 4.2.0-a Mon Nov  8 12:00:00 UTC 2021 (1)",
processor="powerpc", system="JUNOS15.1", leap=00, stratum=3,
```

---

### Cloud Platforms - AWS

**AWS Time Sync Service:**

- Link-local IP: `169.254.169.123`
- All EC2 instances can access
- Stratum 3 (synchronized to AWS atomic clocks)

**Verification (Amazon Linux 2):**

```bash
chronyc sources -v | grep 169.254.169.123
```

**Expected:**
```
^* 169.254.169.123               3   6   377     2    -45us[  -68us] +/-  500us
```

**How to Complete Workbook:**

- **NTP Server(s) Configured:** 169.254.169.123
- **Sync Status:** If source shows `^*` → ✅ Synced
- **Stratum:** 3 (from AWS Time Sync)
- **Current Drift:** Extract from "Last sample" column

**Documentation:** https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/set-time.html

---

### Cloud Platforms - Azure

**Azure Time Sync:**

- Uses Hyper-V time integration by default
- Can optionally use time.windows.com

**Verification (Linux VM):**

Check Hyper-V time sync:
```bash
cat /sys/bus/vmbus/devices/*/class_id | grep -i "9527E630-D0AE-497b-ADCE-E80AB0175CAF"
```

If present → Hyper-V time sync enabled

**Verification (Windows VM):**

```powershell
w32tm /query /status
```

Should show synchronized status.

**How to Complete Workbook:**

- **NTP Server(s) Configured:** "Azure Hyper-V Time Sync" or "time.windows.com"
- **Sync Status:** Check `chronyc tracking` or `w32tm /query /status`
- **Notes:** "Using Azure platform time sync"

**Documentation:** https://docs.microsoft.com/en-us/azure/virtual-machines/linux/time-sync

---

### Cloud Platforms - GCP

**GCP NTP Service:**

- Uses `metadata.google.internal`
- Available on all Compute Engine instances

**Verification:**

```bash
chronyc sources -v | grep metadata
```

**Expected:**
```
^* metadata.google.internal      2   6   377    34   +123us[ +100us] +/-   12ms
```

**How to Complete Workbook:**

- **NTP Server(s) Configured:** metadata.google.internal
- **Sync Status:** If `^*` present → ✅ Synced
- **Stratum:** Typically 2 or 3

**Documentation:** https://cloud.google.com/compute/docs/instances/configure-ntp

---

### Virtualization Platforms

**VMware ESXi (Guest VMs):**

**WARNING:** Do NOT run both VMware Tools time sync AND NTP client simultaneously!

**Option 1: Use VMware Tools Time Sync (Recommended for most VMs)**

```bash
# Check if VMware Tools time sync is enabled
vmware-toolbox-cmd timesync status
```

**Output:** `Enabled` or `Disabled`

**If using VMware Tools time sync:**

- Disable chrony/ntpd
- **Sync Status:** Check VMware Tools status
- **NTP Server(s) Configured:** "VMware ESXi Host Time Sync"
- **Notes:** "Using VMware Tools time synchronization"

**Option 2: Use NTP Client (For time-sensitive servers)**

```bash
# Disable VMware Tools time sync
vmware-toolbox-cmd timesync disable

# Enable and configure chrony/ntpd
systemctl enable --now chronyd
```

**Then verify NTP sync normally with `chronyc tracking`**

---

**Hyper-V (Guest VMs):**

Similar to Azure (uses Hyper-V time integration).

**Check time sync status:**

```powershell
# Windows
w32tm /query /status

# Linux
timedatectl
```

---

**KVM/QEMU:**

Guests can use:
1. **Host time passthrough** (kvmclock)
2. **NTP client** (chrony/ntpd)

**Verify which is active:**

```bash
timedatectl
```

**Output shows:**
```
System clock synchronized: yes
              NTP service: active
```

If using NTP, verify normally with `chronyc tracking`.

---

### Container Hosts

**Docker Host:**

Containers inherit time from host. Verify HOST time sync (not individual containers).

**Check host:**
```bash
chronyc tracking
```

**How to Complete Workbook:**

- Document **container host** (not individual containers)
- Verify host is synced
- Note: "Container time inherited from host"

**Kubernetes Nodes:**

Each K8s node must have NTP configured. Verify each node:

```bash
kubectl get nodes
# Then SSH to each node and verify NTP
```

---

## Drift Measurement Methodology

### Understanding Time Drift

**Drift** = Difference between system clock and authoritative time source

**Positive Drift:** System clock is FAST (ahead of NTP time)

- Example: +250ms = system is 250 milliseconds ahead

**Negative Drift:** System clock is SLOW (behind NTP time)

- Example: -150ms = system is 150 milliseconds behind

**Acceptable Drift Thresholds (REQ-817-011):**

- **General systems:** ±1000 milliseconds (±1 second)
- **Critical security systems:** ±100 milliseconds
- **High-precision systems:** ±10 milliseconds

### Drift Calculation

**From chrony (Linux):**

`chronyc tracking` shows: `System time : 0.000245 seconds fast`

**Calculation:**
1. Extract value: 0.000245 seconds
2. Convert to milliseconds: 0.000245 × 1000 = 0.245 ms
3. Sign: "fast" = positive, "slow" = negative
4. **Result:** +0.245 ms (system is 0.245ms fast)

**From ntp (Linux):**

`ntpq -p` shows offset column: `-89.123`

**Calculation:**

- Already in milliseconds
- **Result:** -89.123 ms (system is 89ms slow)

**From Windows:**

`w32tm /stripchart` shows: `+00.0002450s`

**Calculation:**
1. Extract value: +00.0002450 seconds
2. Convert to milliseconds: 0.0002450 × 1000 = 0.245 ms
3. **Result:** +0.245 ms

### Drift Assessment

**Compliance Logic:**

```
IF Sync Status = "✅ Synced" THEN
    IF System Criticality = "🔴 Critical" THEN
        IF ABS(Drift) <= 100ms THEN "✅ Compliant"
        ELSE "❌ Non-Compliant"
    ELSE IF System Criticality = "High-Precision" THEN
        IF ABS(Drift) <= 10ms THEN "✅ Compliant"
        ELSE "❌ Non-Compliant"
    ELSE
        IF ABS(Drift) <= 1000ms THEN "✅ Compliant"
        ELSE "❌ Non-Compliant"
ELSE
    "❌ Non-Compliant" (not synchronized)
```

---

## Automated Sync Status Collection

### Ansible Playbook

**Example: Collect NTP status from all Linux servers**

```yaml
---

- name: Collect NTP Synchronization Status

  hosts: all_servers
  gather_facts: yes
  tasks:

    - name: Check if chrony is running

      systemd:
        name: chronyd
        state: started
      check_mode: yes
      register: chrony_status
      ignore_errors: yes

    - name: Get chrony tracking info

      command: chronyc tracking
      register: chrony_tracking
      when: chrony_status is succeeded

    - name: Save results to file

      delegate_to: localhost
      lineinfile:
        path: "/tmp/ntp_status_{{ inventory_hostname }}.txt"
        line: "{{ chrony_tracking.stdout }}"
        create: yes
      when: chrony_tracking is defined
```

**Run:**
```bash
ansible-playbook -i inventory.ini collect_ntp_status.yml
```

**Parse outputs and populate workbook.**

---

### PowerShell Script (Windows)

```powershell
# Collect NTP status from all Windows servers
$servers = Get-ADComputer -Filter {OperatingSystem -like "*Windows Server*"} | Select-Object -ExpandProperty Name

$results = @()
foreach ($server in $servers) {
    try {
        $status = Invoke-Command -ComputerName $server -ScriptBlock {
            w32tm /query /status /verbose
        }
        $results += [PSCustomObject]@{
            Server = $server
            Status = $status
        }
    } catch {
        Write-Warning "Failed to query $server: $_"
    }
}

# Export to CSV
$results | Export-Csv -Path "C:\Temp\ntp_status.csv" -NoTypeInformation
```

---

## Alert Configuration

### Nagios Monitoring

**Define NTP check:**

```bash
define command {
    command_name    check_ntp
    command_line    $USER1$/check_ntp_time -H $HOSTADDRESS$ -w 0.5 -c 1.0
}

define service {
    use                     generic-service
    host_name               web-server-01
    service_description     NTP Sync Status
    check_command           check_ntp
    notifications_enabled   1
    contact_groups          sysadmin
}
```

**Critical systems (tighter thresholds):**

```bash
define service {
    use                     critical-service
    host_name               siem-server
    service_description     NTP Sync Status (Critical)
    check_command           check_ntp!-w 0.05 -c 0.1  # 50ms warning, 100ms critical
    notifications_enabled   1
    contact_groups          security-ops
}
```

---

### Prometheus/Grafana

**Alert Rule:**

```yaml
groups:

- name: ntp_alerts

  rules:

  - alert: NTPNotSynchronized

    expr: node_timex_sync_status == 0
    for: 5m
    labels:
      severity: critical
    annotations:
      summary: "NTP not synchronized on {{ $labels.instance }}"
      description: "System clock not synchronized for 5 minutes"
      
  - alert: NTPHighDrift

    expr: abs(node_timex_offset_seconds) > 0.1  # 100ms
    for: 10m
    labels:
      severity: warning
    annotations:
      summary: "High time drift on {{ $labels.instance }}"
      description: "Time drift is {{ $value }}s (threshold: 0.1s)"
```

---

## Periodic Verification Schedules

**Monthly Assessment (REQ-817-016):**

**Week 1:**

- Run automated collection scripts
- Populate System_Inventory sheet
- Identify new sync failures

**Week 2:**

- Analyze Drift_Analysis sheet
- Document gaps in Gaps_Failures
- Create remediation plans

**Week 3:**

- Execute remediation plans
- Re-verify fixed systems
- Update compliance status

**Week 4:**

- Finalize assessment
- Submit for approval
- Report to management

**Quarterly Deep Dive:**

- Compare trends (is drift improving?)
- Review policy exceptions
- Assess monitoring effectiveness
- Update procedures based on lessons learned

---

## Troubleshooting Common Issues

### Stratum 16 (Unsynchronized)

**Symptoms:**

- `chronyc tracking` shows "Stratum : 16"
- `ntpq -p` shows no `*` in first column

**Root Causes:**
1. **NTP server unreachable** (firewall, network)
2. **NTP service not running**
3. **All upstream sources failed**
4. **System clock far off** (>1000s drift)

**Diagnosis:**
```bash
# Check NTP service
systemctl status chronyd

# Check upstream sources
chronyc sources -v

# Check firewall
sudo iptables -L | grep 123
```

**Remediation:**
1. Verify NTP service running
2. Check firewall allows UDP 123 outbound
3. Verify NTP servers reachable (ping)
4. If clock very wrong, set manually first

---

### High Drift (>1000ms)

**Symptoms:**

- System synced but drift exceeds threshold

**Root Causes:**
1. **Virtualization time drift** (VM host issues)
2. **Network latency** to NTP server
3. **Hardware clock drift** (poor quality clock)
4. **Temperature fluctuations**

**Diagnosis:**
```bash
# Check drift rate
chronyc tracking | grep "Frequency"

# Check network latency to NTP server
chronyc sources -v | grep delay
```

**Remediation:**
1. VMware: Enable VMware Tools time sync
2. Move to closer NTP server (lower latency)
3. Increase polling frequency
4. Hardware issue: Replace server if persistent

---

### Intermittent Sync Failures

**Symptoms:**

- Sometimes synced, sometimes not

**Root Causes:**
1. **Network instability**
2. **NTP server load** (too many clients)
3. **Firewall state table timeout**

**Diagnosis:**
```bash
# Check reachability history
chronyc sources -v
# Look at "Reach" column - should be 377
# Less than 377 = packet loss
```

**Remediation:**
1. Add more NTP servers for redundancy
2. Load balance across multiple servers
3. Adjust firewall timeout values

---

# SECTION B: Assessment Workbook Specification

## Workbook Overview

**Filename:** ISMS-A.8.17-Assessment-2-Sync-Status.xlsx

**Generated By:** `generate_assessment_2_sync_status.py`

**Purpose:** Template for documenting per-system NTP synchronization status and drift measurements

**Sheets:**
1. **Instructions** - Workbook usage instructions
2. **System_Inventory** - Per-system sync status and drift measurements
3. **Drift_Analysis** - Statistical drift analysis
4. **Gaps_Failures** - Gap tracking and remediation
5. **Compliance_Summary** - Compliance metrics and executive summary

**Total Sheets:** 5

---

## Common Styling Definitions

**Header Style:**

- Font: Bold, White (FFFFFF), Size 11
- Fill: Dark Blue (366092)
- Alignment: Center, Vertical Center, Wrap Text
- Border: Thin borders all sides

**Data Cell Style:**

- Alignment: Left, Vertical Center, Wrap Text
- Border: Thin borders all sides

**Center Style:**

- Alignment: Center, Vertical Center
- Border: Thin borders all sides

---

## Sheet 1: Instructions

**Purpose:** Workbook usage instructions.

**Layout:**

**Row 1-2:** Title Block

- A1: "ISMS A.8.17 - System Synchronization Status Assessment" (Bold 16, Dark Blue, Merged A1:F1)
- A2: "Generated: [Timestamp]" (Italic 10, Merged A2:F2)

**Row 4-5:** Document Metadata

- A4: "Document ID:" (Bold) | B4: "ISMS-IMP-A.8.17.2" (Bold, Dark Blue)
- A5: "Title:" (Bold) | B5: "System Synchronization Status Assessment"

**Row 7+:** Instructions content

**Column Widths:** A: 15, B: 80, C-F: 15

---

## Sheet 2: System_Inventory

**Purpose:** Document every system's sync status and drift.

**Headers (Row 1):**

| Column | Header | Width | Required | Dropdown/Validation |
|--------|--------|-------|----------|---------------------|
| A | System Name [*] | 30 | Yes | None |
| B | Asset ID | 15 | No | None |
| C | Type [*] | 20 | Yes | 🖥️ Server-Physical, 💻 Server-Virtual, ☁️ Server-Cloud, 🌐 Network Device, 🔒 Security Appliance, 💼 Workstation, 📦 Container Host, 🔌 IoT Device, 📋 Other |
| D | OS/Platform | 20 | No | None |
| E | Criticality | 15 | No | 🔴 Critical, 🟠 High, 🟡 Medium, 🟢 Low |
| F | NTP Server(s) Configured [*] | 35 | Yes | None |
| G | Sync Status [*] | 18 | Yes | ✅ Synced, ❌ Not Synced, ⚠️ Sync Failed, ❓ Unknown, ➖ Excluded |
| H | Stratum | 10 | No | 0-16 (integer validation) |
| I | Current Drift (ms) [*] | 18 | Yes | Number (positive or negative) |
| J | Last Sync Time | 22 | No | DateTime |
| K | Last Verified [*] | 18 | Yes | Date |
| L | Compliance | 15 | Auto | Formula-calculated |
| M | Notes | 40 | No | None |

**Data Validation:**

**Column C (Type):**

- Formula: `"🖥️ Server-Physical,💻 Server-Virtual,☁️ Server-Cloud,🌐 Network Device,🔒 Security Appliance,💼 Workstation,📦 Container Host,🔌 IoT Device,📋 Other"`

**Column E (Criticality):**

- Formula: `"🔴 Critical,🟠 High,🟡 Medium,🟢 Low"`

**Column G (Sync Status):**

- Formula: `"✅ Synced,❌ Not Synced,⚠️ Sync Failed,❓ Unknown,➖ Excluded"`

**Column H (Stratum):**

- Type: Whole number
- Range: 0-16

**Column L (Compliance - Formula):**
```excel
=IF(G2="✅ Synced",
    IF(E2="🔴 Critical",
        IF(ABS(I2)<=100,"✅ Compliant","❌ Non-Compliant"),
        IF(ABS(I2)<=1000,"✅ Compliant","❌ Non-Compliant")
    ),
    "❌ Non-Compliant"
)
```

**Example Rows:**

| System | Asset ID | Type | OS | Criticality | NTP Servers | Sync | Stratum | Drift | Last Sync | Last Verified | Compliance | Notes |
|--------|----------|------|----|----|-------------|------|---------|-------|-----------|---------------|------------|-------|
| web-01 | SRV-001 | 🖥️ Server-Physical | Ubuntu 22.04 | 🟠 High | ntp1.dc1, ntp2.dc1 | ✅ Synced | 3 | 0.5 | 2026-01-16 14:23 | 2026-01-16 | ✅ Compliant | chronyc verified |

**Freeze Panes:** A2

---

## Sheet 3: Drift_Analysis

**Purpose:** Auto-calculated drift statistics.

**THIS SHEET IS AUTO-CALCULATED**

**Metrics:**

- Total Systems: `=COUNTA(System_Inventory!A2:A1000)`
- Systems Synced: `=COUNTIF(System_Inventory!G2:G1000,"✅ Synced")`
- Sync Compliance %: `=(Systems Synced / Total Systems) * 100`
- Average Drift: `=AVERAGE(System_Inventory!I2:I1000)`
- Median Drift: `=MEDIAN(System_Inventory!I2:I1000)`
- Max Drift: `=MAX(ABS(System_Inventory!I2:I1000))`

**Drift Distribution Table:**

| Range | Formula | Expected |
|-------|---------|----------|
| 0-10ms | `=COUNTIFS(System_Inventory!I:I,">=0",System_Inventory!I:I,"<=10")+COUNTIFS(System_Inventory!I:I,">=-10",System_Inventory!I:I,"<0")` | Most systems |
| 10-100ms | Similar logic | Some systems |
| >1000ms | `=COUNTIF(System_Inventory!I:I,">1000")+COUNTIF(System_Inventory!I:I,"<-1000")` | Few/none |

---

## Sheet 4: Gaps_Failures

**Purpose:** Manual gap documentation.

**Headers:**

| Column | Header | Width |
|--------|--------|-------|
| A | Gap ID | 12 |
| B | System Name | 30 |
| C | Issue Description | 40 |
| D | Root Cause | 40 |
| E | Severity | 15 |
| F | Impact | 40 |
| G | Remediation Plan | 50 |
| H | Responsible | 25 |
| I | Target Date | 15 |
| J | Status | 18 |

**After table, add exception reference (ISMS Copilot Correction):**

> **For gaps requiring permanent exceptions:** Reference ISMS-POL-A.8.17 Section 3.3 for formal exception process.

---

## Sheet 5: Compliance_Summary

**Purpose:** Executive metrics.

**Section 1: Metrics (ISMS Copilot Correction - Updated):**

| Metric | Target | Compliance Threshold | Actual | Status |
|--------|--------|---------------------|--------|--------|
| Overall Sync | ≥98% | ≥95% | `=Drift_Analysis!B3` | `=IF(B3>=95,"✅","❌")` |
| Critical Systems | 100% | 100% | `=COUNTIFS(System_Inventory!E:E,"🔴 Critical",System_Inventory!L:L,"✅ Compliant")/COUNTIF(System_Inventory!E:E,"🔴 Critical")*100` | Formula |
| Average Drift | <500ms | <1000ms | `=Drift_Analysis!B6` | Formula |

**Section 2: Executive Summary (Manual):**

Text box for 3-5 sentence management summary.

---

## Python Script Reference

**Script File:** `generate_assessment_2_sync_status.py`

**Key Functions:**

- `create_styles()` - Styling definitions
- `create_instructions_sheet()` - Instructions
- `create_system_inventory_sheet()` - Main data sheet
- `create_drift_analysis_sheet()` - Statistics
- `create_gaps_failures_sheet()` - Gap tracking
- `create_compliance_summary_sheet()` - Executive summary

**To regenerate workbook:**
```bash
python3 generate_assessment_2_sync_status.py --output ISMS-A.8.17-Assessment-2-Sync-Status.xlsx
```

---

**END OF SPECIFICATION**

---

*"The only reason for time is so that everything doesn't happen at once."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-01-31 -->
