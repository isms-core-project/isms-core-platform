**ISMS-IMP-A.8.17-S2-UG - Synchronization Verification Process & Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.17: Clock Synchronization

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.17-S2-UG |
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

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.8.17-S2-TG.

---

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

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
