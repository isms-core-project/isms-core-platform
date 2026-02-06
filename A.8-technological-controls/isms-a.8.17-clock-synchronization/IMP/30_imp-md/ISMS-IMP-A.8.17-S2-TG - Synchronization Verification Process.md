**ISMS-IMP-A.8.17-S2-TG - Synchronization Verification Process & Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.17: Clock Synchronization

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.17-S2-TG |
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

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.8.17-S2-UG.

---

# Technical Specification

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

<!-- QA_VERIFIED: 2026-02-06 -->
