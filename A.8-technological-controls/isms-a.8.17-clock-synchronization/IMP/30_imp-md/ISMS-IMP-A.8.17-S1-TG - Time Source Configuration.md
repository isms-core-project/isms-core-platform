**ISMS-IMP-A.8.17-S1-TG - Time Source Configuration & Assessment**
**Technical Specification**
### ISO/IEC 27001:2022 Control A.8.17: Clock Synchronization

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.17-S1-TG |
| **Version** | 1.0 |
| **Assessment Area** | Time Source Infrastructure & Configuration |
| **Related Policy** | ISMS-POL-A.8.17 (Clock Synchronization Policy - Section 2.1, 2.2) |
| **Purpose** | Document authoritative time sources and internal NTP infrastructure, assess compliance with policy requirements |
| **Target Audience** | Network Engineers, System Administrators, Security Engineers, ISMS Officers, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Quarterly or After Major Infrastructure Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Original Date] | Initial technical specification for time source configuration | Network Operations Manager |

### Document Structure

This is the **Technical Specification**. The companion User Completion Guide is documented in ISMS-IMP-A.8.17-S1-UG.

---

# Technical Specification

**Audience:** Workbook developers, Python script maintainers, technical implementers

**Note:** This section provides technical specifications for time source configuration and assessment workbook structure. Users completing the assessment should refer to Part I above.

**PART II will be delivered separately due to file size constraints.**

---

**TO BE CONTINUED IN PART 2**
# PART II: TECHNICAL SPECIFICATION

**Audience:** Workbook developers, Python script maintainers, technical implementers

**Note:** This section provides technical specifications for time source configuration and assessment workbook structure. Users completing the assessment should refer to Part I above.

---

# Implementation Requirement Mapping

**This section maps policy requirements (REQ-817-xxx codes) to ISMS-POL-A.8.17 sections for traceability.**

## S1 Requirements (REQ-817-001 through REQ-817-008)

| Requirement ID | Policy Section | Requirement Summary |
|---------------|----------------|---------------------|
| REQ-817-001 | Section 2.1 | Minimum TWO (2) authoritative time sources required |
| REQ-817-002 | Section 2.1 | Primary sources must be Stratum 0 or Stratum 1; supplementary sources (Stratum 2+) acceptable for NTP Pool and cloud providers |
| REQ-817-003 | Section 2.1 | >99.9% uptime for each authoritative source |
| REQ-817-004 | Section 2.1 | Geographic diversity recommended for resilience |
| REQ-817-005 | Section 2.2 | Minimum TWO (2) internal NTP servers required |
| REQ-817-006 | Section 2.2 | Internal servers must be Stratum 2 (synchronized to Stratum 1 external sources) |
| REQ-817-007 | Section 2.2 | High availability configuration with automatic failover |
| REQ-817-008 | Section 2.2 | Continuous monitoring with automated alerting for NTP infrastructure |

**Note:** Requirement codes REQ-817-001 through REQ-817-008 correspond to S1 (Time Source Configuration). Codes REQ-817-009 through REQ-817-016 are used in S2 (Synchronization Verification).

---

# SECTION A: Implementation Guidance

## Introduction

This section provides technical guidance for selecting, configuring, and managing authoritative time sources and internal NTP infrastructure.

**Purpose:** Enable network engineers and system administrators to implement time source infrastructure that meets policy requirements defined in ISMS-POL-A.8.17.

**Scope:** External authoritative time sources (Stratum 0/1) and internal NTP server deployment (Stratum 2).

**Related Documents:**

- ISMS-POL-A.8.17 (Clock Synchronization Policy)
- ISMS-POL-A.8.21 (Network Services Security - secures NTP infrastructure)
- ISMS-IMP-A.8.17-S2 (Synchronization Verification Process)

---

## Selecting Authoritative Time Sources

### External Public Time Sources

**NIST Time Services (United States)**

NIST (National Institute of Standards and Technology) operates public NTP servers providing Stratum 1 time synchronized to atomic clocks.

**Recommended Servers:**

- `time.nist.gov` - Load-balanced across multiple servers
- `time-a-g.nist.gov` through `time-d-g.nist.gov` - Specific servers

**Characteristics:**

- **Stratum:** 1
- **Availability:** Best effort (no SLA for public use)
- **Geographic Location:** United States
- **Access:** Public, no registration required
- **Usage Restrictions:** NIST requests limiting queries to 1-2 servers

**Configuration Example (chrony):**
```
server time.nist.gov iburst
```

**Configuration Example (ntp):**
```
server time.nist.gov iburst
```

**Verification:**
```bash
# Test reachability
ping time.nist.gov

# Verify NTP response
chronyc tracking  # Should show NIST as reference
```

**Documentation:** https://tf.nist.gov/tf-cgi/servers.cgi

---

**NTP Pool Project**

The NTP Pool Project is a cluster of volunteer time servers providing load-balanced NTP service globally.

**Recommended Usage:**

- `0.pool.ntp.org` through `3.pool.ntp.org` - Global pool
- `0.ch.pool.ntp.org` - Switzerland-specific pool
- `0.europe.pool.ntp.org` - European pool

**Characteristics:**

- **Stratum:** Typically 2-3 (volunteers sync to Stratum 1)
- **Availability:** Best effort (individual servers may vary)
- **Geographic Location:** Global distribution
- **Access:** Public, no registration required
- **Usage:** Pool automatically load-balances across healthy servers

**IMPORTANT (ISMS Copilot Correction):**
Per ISMS-POL-A.8.17 Section 2.1, NTP Pool servers are classified as **supplementary sources** (Stratum 2+ acceptable). They MAY be used for redundancy but SHALL NOT be the sole authoritative reference. Organization MUST have at least 2 PRIMARY sources (Stratum 0/1) such as NIST or GPS.

**Configuration Example (chrony):**
```
pool 0.pool.ntp.org iburst
pool 1.pool.ntp.org iburst
```

**Configuration Example (ntp):**
```
pool 0.pool.ntp.org iburst
pool 1.pool.ntp.org iburst
```

**Documentation:** https://www.pool.ntp.org/

---

**Cloudflare Time Services**

Cloudflare provides public NTP service (time.cloudflare.com) as Stratum 1 synchronized to atomic clocks with global Anycast distribution.

**Recommended Servers:**

- `time.cloudflare.com` - IPv4 and IPv6

**Characteristics:**

- **Stratum:** 1
- **Availability:** >99.9% (public SLA)
- **Geographic Location:** Global (Anycast - automatically routes to nearest datacenter)
- **Access:** Public, no registration required
- **Accuracy:** <1 millisecond typical

**Configuration Example (chrony):**
```
server time.cloudflare.com iburst
```

**Documentation:** https://developers.cloudflare.com/time-services/ntp/

---

**Google Public NTP**

Google provides public NTP service synchronized to atomic clocks with leap-smear support.

**Recommended Servers:**

- `time.google.com` - IPv4 and IPv6

**Characteristics:**

- **Stratum:** 1
- **Availability:** Best effort (no public SLA)
- **Geographic Location:** Global (Anycast)
- **Special Feature:** Leap-smear (gradually adjusts for leap seconds instead of stepping)

**Configuration Example (chrony):**
```
server time.google.com iburst
```

**Documentation:** https://developers.google.com/time

---

**Regional/National Time Services**

Many countries operate national time services:

| Country | Service | Servers |
|---------|---------|---------|
| Switzerland | METAS | ntp.metas.ch |
| Germany | PTB | ptbtime1.ptb.de, ptbtime2.ptb.de |
| UK | NPL | ntp1.npl.co.uk, ntp2.npl.co.uk |
| France | SYRTE | ntp.obspm.fr |

**Advantage:** May provide better latency for regional users, government-operated (trusted)

---

### GPS-Based Time Sources

GPS satellites broadcast atomic clock signals. GPS receivers provide Stratum 0 time.

**When to Use GPS:**

- Air-gapped environments without internet access
- Requirements for <1 microsecond accuracy
- Independence from external network services
- Critical infrastructure requiring sovereign time source

**Hardware Requirements:**

- GPS NTP appliance (e.g., Meinberg, EndRun, Symmetricom)
- GPS antenna with clear sky view
- Network connection to serve time to internal NTP servers

**Typical Deployment:**
```
GPS Receiver (Stratum 0)
    ↓
Internal NTP Server (Stratum 1 - directly connected to GPS)
    ↓
Other Internal NTP Servers (Stratum 2 - peer with GPS-connected server)
```

**Configuration Example (GPS-connected server):**
```
# chrony configuration for GPS receiver
refclock SHM 0 refid GPS precision 1e-9
```

**Considerations:**

- GPS antenna placement (roof, clear sky view, lightning protection)
- Backup power for GPS receiver
- Regular verification of GPS signal lock

---

### Atomic Clock Sources

Organizations can deploy atomic clocks (Rubidium, Cesium) for ultimate time accuracy.

**When to Use:**

- Financial trading systems (microsecond accuracy required)
- Scientific research (precision timing)
- Critical infrastructure (complete independence from external sources)
- Regulatory requirements (e.g., MiFID II timestamp requirements)

**Characteristics:**

- **Stratum:** 0 (primary reference)
- **Accuracy:** <1 nanosecond (Cesium), <100 nanoseconds (Rubidium)
- **Cost:** High (€20,000 - €100,000+)
- **Maintenance:** Annual calibration required

**Not Recommended Unless:**

- Specific regulatory or technical requirements demand atomic-level accuracy
- Budget supports acquisition and maintenance costs

---

## Internal NTP Server Deployment

### Architecture Design

**Minimum Configuration (REQ-817-005):**

```
External Stratum 1 Sources (≥2 required)
    ↓
Internal NTP Server 1 (Stratum 2)
Internal NTP Server 2 (Stratum 2)
    ↓
Client Systems (Stratum 3)
```

**Requirements:**

- Minimum 2 internal NTP servers
- Each server synchronizes to same external sources
- Servers configured as peers for consistency
- Geographic diversity recommended

---

**High-Availability Configuration (REQ-817-007):**

```
Primary Datacenter (DC1):
  External Sources: NIST, Cloudflare
      ↓
  ntp1.dc1 (Stratum 2) ←→ ntp2.dc1 (Stratum 2)
      ↓
  Clients in DC1

Secondary Datacenter (DC2):
  External Sources: NIST, NTP Pool
      ↓
  ntp1.dc2 (Stratum 2) ←→ ntp2.dc2 (Stratum 2)
      ↓
  Clients in DC2
```

**Features:**

- 2 NTP servers per datacenter (local redundancy)
- Peer relationships within each datacenter
- All servers sync to external sources independently
- Clients configure multiple NTP servers from same datacenter

---

**Hybrid Cloud Architecture:**

```
On-Premises:
  GPS Receiver (Stratum 0)
      ↓
  ntp1.dc1 (Stratum 1) ←→ ntp2.dc1 (Stratum 1)
      ↓
  On-prem clients

Cloud (AWS):
  AWS Time Sync (169.254.169.123)
      ↓
  Cloud instances (Stratum 2)
```

**Considerations:**

- Cloud instances use provider time services (AWS Time Sync, Azure NTP, GCP NTP)
- On-premises uses internal NTP infrastructure
- Hybrid systems may use VPN to access on-prem NTP if required

---

### NTP Server Platform Selection

**Linux (Recommended for Internal NTP Servers):**

**chrony:**

- Modern, accurate, efficient
- Better performance on virtual machines
- Handles intermittent network connectivity well
- Default on RHEL/CentOS 8+, Fedora, Ubuntu 20.04+

**ntpd (traditional):**

- Mature, widely deployed
- More configuration options
- Preferred for GPS/atomic clock integration
- Default on older Linux distributions

**Recommendation:** Use chrony for new deployments, ntpd for GPS integration or existing deployments.

**Windows Server:**

- Use W32Time (built-in Windows Time Service)
- Configure as NTP server using registry settings
- Less accurate than Linux chrony/ntpd but acceptable for Stratum 2 role

**Dedicated NTP Appliances:**

- Meinberg, EndRun, Symmetricom
- GPS-integrated, high-accuracy
- Expensive but turnkey solution
- Suitable for critical infrastructure

---

### Internal NTP Server Configuration

**Linux with chrony (Recommended):**

File: `/etc/chrony.conf`

```bash
# Upstream Stratum 1 sources
server time.nist.gov iburst
server time.cloudflare.com iburst
pool 0.pool.ntp.org iburst

# Peer with other internal NTP servers for consistency
peer ntp2.dc1.example.com

# Allow clients to query this server
allow 10.0.0.0/8
allow 192.168.0.0/16

# Log statistics
logdir /var/log/chrony
log measurements statistics tracking

# Step clock if offset > 1 second at startup
makestep 1.0 3

# Enable hardware timestamps if available
hwtimestamp *

# Local stratum to use if all sources fail (Stratum 10 = orphan mode)
local stratum 10
```

**Key Settings:**

- `iburst`: Sync faster at startup
- `peer`: Peer with other internal NTP servers
- `allow`: Permit client queries from specified networks
- `makestep`: Allow stepping clock at startup if far off
- `local stratum 10`: Orphan mode if all external sources fail

**Restart service:**
```bash
sudo systemctl restart chronyd
sudo systemctl enable chronyd
```

**Verify:**
```bash
chronyc tracking    # Show current sync status
chronyc sources -v  # Show all configured sources
```

---

**Linux with ntpd (Traditional):**

File: `/etc/ntp.conf`

```bash
# Upstream Stratum 1 sources
server time.nist.gov iburst
server time.cloudflare.com iburst
server 0.pool.ntp.org iburst
server 1.pool.ntp.org iburst

# Peer with other internal NTP servers
peer ntp2.dc1.example.com

# Access control
restrict default kod nomodify notrap nopeer noquery
restrict -6 default kod nomodify notrap nopeer noquery
restrict 10.0.0.0 mask 255.0.0.0 nomodify notrap
restrict 192.168.0.0 mask 255.255.0.0 nomodify notrap
restrict 127.0.0.1
restrict ::1

# Drift file
driftfile /var/lib/ntp/drift

# Log file
logfile /var/log/ntp.log
```

**Restart service:**
```bash
sudo systemctl restart ntpd
sudo systemctl enable ntpd
```

**Verify:**
```bash
ntpq -p    # Show peers
ntpstat    # Show sync status
```

---

**Windows Server W32Time:**

Configure via PowerShell:

```powershell
# Set NTP servers
w32tm /config /manualpeerlist:"time.nist.gov,0x8 time.cloudflare.com,0x8" /syncfromflags:manual /reliable:YES /update

# Set as NTP server (announce as time source)
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\W32Time\Config" -Name "AnnounceFlags" -Value 5

# Enable NTP server
Set-ItemProperty -Path "HKLM:\SYSTEM\CurrentControlSet\Services\W32Time\TimeProviders\NtpServer" -Name "Enabled" -Value 1

# Restart service
Restart-Service w32time

# Verify
w32tm /query /status
w32tm /query /peers
```

---

### Network Device NTP Configuration

**Cisco IOS:**

```cisco
! Configure NTP servers
ntp server time.nist.gov
ntp server time.cloudflare.com

! Peer with other network devices (optional)
ntp peer 10.0.1.11

! Set local time zone (optional)
clock timezone CET 1 0

! Enable NTP authentication (recommended)
ntp authenticate
ntp authentication-key 1 md5 <secret_key>
ntp trusted-key 1
ntp server time.nist.gov key 1
```

**Verify:**
```cisco
show ntp associations
show ntp status
```

---

**Juniper JunOS:**

```juniper
set system ntp server time.nist.gov
set system ntp server time.cloudflare.com
set system ntp peer 10.0.1.11
```

**Verify:**
```juniper
show ntp associations
show ntp status
```

---

## Cloud Time Services

### AWS Time Sync Service

AWS provides link-local NTP service synchronized to atomic clocks.

**Configuration:**

- Service IP: `169.254.169.123`
- Available on all EC2 instances in all regions
- Stratum 3 (synchronized to AWS atomic clocks)
- No additional cost

**Amazon Linux 2 (chrony):**

File: `/etc/chrony.conf`

```bash
# Use AWS Time Sync Service
server 169.254.169.123 prefer iburst minpoll 4 maxpoll 4

# Fallback to public sources
pool 0.pool.ntp.org iburst
```

**Verification:**
```bash
chronyc sources -v
# Should show 169.254.169.123 with '*' (selected)
```

**Documentation:** https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/set-time.html

---

### Azure NTP Service

Azure VMs synchronize time via Hyper-V time integration.

**Recommended Configuration (Linux):**

Disable NTP client, use Hyper-V time sync:

```bash
# Disable chronyd
sudo systemctl stop chronyd
sudo systemctl disable chronyd

# Verify Hyper-V time sync enabled
cat /sys/bus/vmbus/devices/*/class_id | grep -i "9527E630-D0AE-497b-ADCE-E80AB0175CAF"
```

**Alternative (Use Azure NTP servers):**

```bash
# /etc/chrony.conf
server time.windows.com iburst
```

**Documentation:** https://docs.microsoft.com/en-us/azure/virtual-machines/linux/time-sync

---

### GCP NTP Service

GCP provides `metadata.google.internal` as NTP server.

**Configuration:**

File: `/etc/chrony.conf` (Debian/Ubuntu)

```bash
server metadata.google.internal iburst
```

**Verification:**
```bash
chronyc sources -v
```

**Documentation:** https://cloud.google.com/compute/docs/instances/configure-ntp

---

## Monitoring & Alerting

### Monitoring Requirements (REQ-817-008)

**ISMS Copilot Correction:** Policy requires monitoring WITH ALERTING (not just monitoring).

**Required Checks:**
1. **NTP service running** - Process check for chronyd/ntpd
2. **Synchronization status** - Check Stratum (must be 2-3, not 16)
3. **Time drift** - Check offset from upstream sources
4. **Reachability** - Verify upstream sources reachable
5. **Health status** - Overall service health

**Alert Conditions:**

- NTP service stopped
- Stratum 16 (unsynchronized)
- Time drift >500ms
- All upstream sources unreachable
- Service health check failed

---

### Nagios Monitoring Example

**check_ntp_time plugin:**

```bash
# Define command
define command {
    command_name    check_ntp
    command_line    $USER1$/check_ntp_time -H $HOSTADDRESS$ -w 0.5 -c 1.0
}

# Define service
define service {
    use                     generic-service
    host_name               ntp1.dc1.example.com
    service_description     NTP Sync Status
    check_command           check_ntp
    notifications_enabled   1
    contact_groups          network-ops
}
```

**Custom check for Stratum 16:**

```bash
#!/bin/bash
# check_ntp_stratum.sh

stratum=$(chronyc tracking | grep "Stratum" | awk '{print $3}')

if [ "$stratum" == "16" ]; then
    echo "CRITICAL: NTP not synchronized (Stratum 16)"
    exit 2
elif [ "$stratum" -le "3" ]; then
    echo "OK: NTP synchronized (Stratum $stratum)"
    exit 0
else
    echo "WARNING: Unexpected stratum ($stratum)"
    exit 1
fi
```

---

### Prometheus/Grafana Monitoring

**node_exporter metrics:**

```yaml
# Prometheus scrape config
scrape_configs:

  - job_name: 'ntp_servers'

    static_configs:

      - targets:
        - 'ntp1.dc1.example.com:9100'
        - 'ntp2.dc1.example.com:9100'

```

**Useful metrics:**

- `node_timex_sync_status` - 1 if synchronized, 0 if not
- `node_timex_offset_seconds` - Time offset in seconds
- `node_timex_maxerror_seconds` - Maximum error estimate

**Alert rule:**

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
```

---

## Security Considerations

NTP infrastructure is security-critical and must be protected per ISMS-POL-A.8.21 (Network Services Security).

**Firewall Rules:**

- Allow UDP 123 outbound from internal NTP servers to external sources
- Allow UDP 123 inbound from client networks to internal NTP servers
- Block UDP 123 from internet to internal NTP servers (prevent external access)

**Access Control:**

- Limit NTP client queries to trusted networks only
- Use `restrict` directives in ntp.conf / `allow` in chrony.conf

**NTP Authentication (Optional but Recommended):**

chrony symmetric key authentication:

```bash
# /etc/chrony.keys

1 SHA256 HEX:<64-character-hex-key>

# /etc/chrony.conf
keyfile /etc/chrony.keys
server time.nist.gov key 1
```

**DDoS Protection:**

- Rate limit NTP queries (kisso, rate limiting features)
- Monitor for amplification attacks (monlist command disabled by default in modern versions)

---

## Troubleshooting

### Common Issues

**Problem:** Stratum 16 (unsynchronized)

**Causes:**

- No reachability to upstream sources
- Firewall blocking UDP 123
- Incorrect server configuration
- All upstream sources offline

**Diagnosis:**
```bash
chronyc sources -v   # Check reachability
ping time.nist.gov   # Test network connectivity
sudo tcpdump -i any port 123   # Check NTP traffic
```

**Solution:**

- Fix firewall rules
- Verify upstream servers in config are correct
- Check network routing

---

**Problem:** High time drift

**Causes:**

- System clock drift rate too high (hardware issue)
- Intermittent network connectivity
- Upstream source instability

**Diagnosis:**
```bash
chronyc tracking    # Check current offset
chronyc sourcestats # Check source statistics
```

**Solution:**

- Adjust polling interval
- Add more upstream sources
- Check hardware (virtualization time sync issues)

---

**Problem:** Time jumps backward/forward

**Causes:**

- Clock step threshold exceeded
- Leap second event
- Manual time change

**Diagnosis:**
```bash
grep "System clock wrong by" /var/log/messages
journalctl -u chronyd | grep "Step"
```

**Solution:**

- Configure `makestep` threshold appropriately
- For production systems, avoid stepping - use `slew` mode

---

# SECTION B: Assessment Workbook Specification

## Workbook Overview

**Filename:** ISMS-A.8.17-Assessment-1-Time-Sources.xlsx

**Generated By:** `generate_assessment_1_time_sources.py`

**Purpose:** Template for documenting authoritative time sources and internal NTP infrastructure

**Sheets:**
1. **Instructions** - Workbook usage instructions and legend
2. **Time_Sources** - External authoritative time sources (Stratum 0/1)
3. **Internal_NTP_Servers** - Organization's internal NTP servers (Stratum 2)
4. **Hierarchy** - Visual representation of time synchronization architecture
5. **Compliance_Summary** - Assessment results and compliance metrics

**Total Sheets:** 5

---

## Common Styling Definitions

**Header Style:**

- Font: Bold, White (FFFFFF), Size 11
- Fill: Dark Blue (366092)
- Alignment: Center, Vertical Center, Wrap Text
- Border: Thin borders all sides

**Title Style:**

- Font: Bold, Size 14, Dark Blue (366092)
- Alignment: Left, Vertical Center

**Data Cell Style:**

- Alignment: Left, Vertical Center, Wrap Text
- Border: Thin borders all sides

**Center Style:**

- Alignment: Center, Vertical Center
- Border: Thin borders all sides

---

## Sheet 1: Instructions

**Purpose:** Provide workbook usage instructions, status legend, and assessment guidance.

**Layout:**

**Row 1-2:** Title Block

- A1: "ISMS A.8.17 - Time Source Inventory Assessment" (Font: Bold 16, Dark Blue, Merged A1:F1)
- A2: "Generated: [Timestamp]" (Font: Italic 10, Merged A2:F2)

**Row 4-5:** Document Metadata

- A4: "Document ID:" (Bold) | B4: "ISMS-IMP-A.8.17.1" (Bold, Dark Blue)
- A5: "Title:" (Bold) | B5: "Time Source Infrastructure Assessment"

**Row 7+:** Instructions Content

- Purpose statement
- Sheet descriptions
- Completion guidance
- Status legend

**Column Widths:**

- A: 15
- B: 80
- C-F: 15 each

---

## Sheet 2: Time_Sources

**Purpose:** Document external authoritative time sources.

**Headers (Row 1):**

| Column | Header | Width | Required | Data Type | Dropdown/Validation |
|--------|--------|-------|----------|-----------|---------------------|
| A | Source Name [*] | 25 | Yes | Text | None |
| B | Type [*] | 18 | Yes | Dropdown | 🛰️ GPS, 🏛️ NIST, 🌐 NTP Pool, ☁️ Cloudflare, 📍 Google, 🏢 Regional Government, ⚛️ Atomic Clock, ☁️ Cloud Provider, 📋 Other |
| C | IP/Hostname [*] | 30 | Yes | Text | None |
| D | Stratum [*] | 10 | Yes | Dropdown | 0, 1, 2 |
| E | Geographic Location | 20 | No | Text | None |
| F | Provider | 20 | No | Text | None |
| G | Availability SLA | 18 | No | Text | None |
| H | Last Verified [*] | 15 | Yes | Date | None |
| I | Status | 12 | No | Dropdown | ✅ Active, ❌ Inactive, ⚠️ Testing, ♻️ Decommissioned |
| J | Notes | 40 | No | Text | None |

**Data Validation:**

**Column B (Type):**

- Type: List
- Formula: `"🛰️ GPS,🏛️ NIST,🌐 NTP Pool,☁️ Cloudflare,📍 Google,🏢 Regional Government,⚛️ Atomic Clock,☁️ Cloud Provider,📋 Other"`
- Error Message: "Please select a valid time source type"
- Error Title: "Invalid Type"
- Applies To: B2:B100

**Column D (Stratum):**

- Type: List
- Formula: `"0,1,2"`
- Error Message: "External sources should be Stratum 0, 1, or 2"
- Error Title: "Invalid Stratum"
- Applies To: D2:D100

**Column I (Status):**

- Type: List
- Formula: `"✅ Active,❌ Inactive,⚠️ Testing,♻️ Decommissioned"`
- Error Message: "Please select a valid status"
- Error Title: "Invalid Status"
- Applies To: I2:I100

**Example Rows (Rows 2-4):**

| Source Name | Type | IP/Hostname | Stratum | Location | Provider | SLA | Last Verified | Status | Notes |
|-------------|------|-------------|---------|----------|----------|-----|---------------|--------|-------|
| time.nist.gov | 🏛️ NIST | time.nist.gov | 1 | United States | NIST | Public (no SLA) | 2026-01-16 | ✅ Active | Primary authoritative source |
| time.cloudflare.com | ☁️ Cloudflare | time.cloudflare.com | 1 | Global (Anycast) | Cloudflare | Public (no SLA) | 2026-01-16 | ✅ Active | Secondary authoritative source |
| 0.pool.ntp.org | 🌐 NTP Pool | 0.pool.ntp.org | 2 | Global | NTP Pool Project | Public (no SLA) | 2026-01-16 | ✅ Active | Supplementary backup source |

**Empty Template Rows:** Rows 5-20 (formatted with borders, no data)

**Freeze Panes:** A2 (freeze header row)

---

## Sheet 3: Internal_NTP_Servers

**Purpose:** Document organization's internal NTP infrastructure.

**Headers (Row 1):**

| Column | Header | Width | Required | Data Type | Dropdown/Validation |
|--------|--------|-------|----------|-----------|---------------------|
| A | Server Name [*] | 25 | Yes | Text | None |
| B | IP Address [*] | 18 | Yes | Text | None |
| C | Stratum [*] | 10 | Yes | Dropdown | 2, 3 |
| D | Upstream Sources [*] | 35 | Yes | Text | None |
| E | Location/Datacenter [*] | 22 | Yes | Text | None |
| F | Redundancy Group | 18 | No | Text | None |
| G | Peer Servers | 30 | No | Text | None |
| H | Monitoring Status | 18 | No | Dropdown | ✅ Monitored with Alerting, ⚠️ Monitored (No Alerting), ❌ Not Monitored, 🔧 Monitoring Failed |
| I | Last Health Check [*] | 18 | Yes | Date | None |
| J | Status | 12 | No | Dropdown | ✅ Active, ❌ Inactive, 🛠️ Maintenance, ⚠️ Failed |
| K | Notes | 40 | No | Text | None |

**IMPORTANT (ISMS Copilot Correction):**

Column H (Monitoring Status) dropdown was expanded from 3 options to 4 options to capture alerting requirement per REQ-817-008:

**Original (Incorrect):**

- ✅ Monitored
- ❌ Not Monitored
- ⚠️ Monitoring Failed

**Corrected (Per Copilot):**

- ✅ Monitored with Alerting (REQUIRED for compliance)
- ⚠️ Monitored (No Alerting) (NON-COMPLIANT)
- ❌ Not Monitored (NON-COMPLIANT)
- 🔧 Monitoring Failed (NEEDS REMEDIATION)

**Data Validation:**

**Column C (Stratum):**

- Type: List
- Formula: `"2,3"`
- Error Message: "Internal NTP servers should be Stratum 2 or 3"
- Error Title: "Invalid Stratum"
- Applies To: C2:C100

**Column H (Monitoring Status):**

- Type: List
- Formula: `"✅ Monitored with Alerting,⚠️ Monitored (No Alerting),❌ Not Monitored,🔧 Monitoring Failed"`
- Error Message: "Please select a valid monitoring status"
- Error Title: "Invalid Monitoring Status"
- Applies To: H2:H100

**Column J (Status):**

- Type: List
- Formula: `"✅ Active,❌ Inactive,🛠️ Maintenance,⚠️ Failed"`
- Error Message: "Please select a valid status"
- Error Title: "Invalid Status"
- Applies To: J2:J100

**Example Rows (Rows 2-4):**

| Server Name | IP | Stratum | Upstream | Location | Group | Peers | Monitoring | Last Check | Status | Notes |
|-------------|----|---------|---------  |----------|-------|-------|------------|------------|--------|-------|
| ntp1.dc1.org.local | 10.0.1.10 | 2 | time.nist.gov, time.cloudflare.com | Datacenter 1 | Primary DC | ntp2.dc1.org.local | ✅ Monitored with Alerting | 2026-01-16 | ✅ Active | Primary NTP |
| ntp2.dc1.org.local | 10.0.1.11 | 2 | time.nist.gov, 0.pool.ntp.org | Datacenter 1 | Primary DC | ntp1.dc1.org.local | ✅ Monitored with Alerting | 2026-01-16 | ✅ Active | Secondary NTP |
| ntp1.dc2.org.local | 10.0.2.10 | 2 | time.cloudflare.com, 1.pool.ntp.org | Datacenter 2 | Secondary DC | ntp2.dc2.org.local | ✅ Monitored with Alerting | 2026-01-16 | ✅ Active | DR site NTP |

**Empty Template Rows:** Rows 5-20 (formatted with borders, no data)

**Freeze Panes:** A2 (freeze header row)

---

## Sheet 4: Hierarchy

**Purpose:** Visual representation of time synchronization architecture (auto-generated).

**THIS SHEET IS AUTO-CALCULATED/GENERATED** - No user input required.

**Layout:**

**Row 1:** Title

- A1: "Time Synchronization Hierarchy" (Font: Bold 14, Dark Blue, Merged A1:E1)

**Row 2:** Subtitle

- A2: "Stratum levels represent distance from authoritative time source (lower is better)" (Font: Italic 10, Merged A2:E2)

**Row 4+:** Stratum Level Table

| Stratum | Level | Description | Examples | Typical Accuracy |
|---------|-------|-------------|----------|------------------|
| 0 | Reference Clock | Primary time source (not network accessible) | GPS receiver, Atomic clock, Radio time signal | <1 microsecond |
| 1 | Primary Time Server | Directly connected to Stratum 0 device | GPS NTP appliance, NIST servers, Government time services | <10 microseconds |
| 2 | Secondary Time Server | Synchronized to Stratum 1 servers | Internal organizational NTP servers | <100 microseconds |
| 3+ | Client Systems | Synchronized to Stratum 2 servers | Servers, workstations, network devices | <1 millisecond |
| 16 | Unsynchronized | Not synchronized to any time source | Misconfigured or failed systems | N/A - FAILURE |

**Purpose:** Educate users on Stratum hierarchy and visualize organization's architecture.

---

## Sheet 5: Compliance_Summary

**Purpose:** Auto-calculated compliance metrics and gap tracking.

**Section 1: Auto-Calculated Compliance Metrics (Rows 1-10)**

| Metric | Policy Requirement | Actual | Status |
|--------|-------------------|--------|--------|
| External Time Sources | ≥2 (REQ-817-001) | =COUNTA(Time_Sources!A2:A100) | =IF(ACTUAL≥2,"✅ PASS","❌ FAIL") |
| Primary Sources (Stratum 0/1) | ≥2 (REQ-817-002) | =COUNTIFS(Time_Sources!D2:D100,"0")+COUNTIFS(Time_Sources!D2:D100,"1") | =IF(ACTUAL≥2,"✅ PASS","❌ FAIL") |
| Internal NTP Servers | ≥2 (REQ-817-005) | =COUNTA(Internal_NTP_Servers!A2:A100) | =IF(ACTUAL≥2,"✅ PASS","❌ FAIL") |
| Stratum 2 Compliance | 100% (REQ-817-006) | =COUNTIFS(Internal_NTP_Servers!C2:C100,"2",Internal_NTP_Servers!J2:J100,"✅ Active")/COUNTA(Internal_NTP_Servers!A2:A100)*100 | =IF(ACTUAL=100,"✅ PASS","❌ FAIL") |
| Monitoring with Alerting | 100% (REQ-817-008) | =COUNTIF(Internal_NTP_Servers!H2:H100,"✅ Monitored with Alerting")/COUNTA(Internal_NTP_Servers!A2:A100)*100 | =IF(ACTUAL=100,"✅ PASS","⚠️ WARNING") |
| Active Server Status | 100% | =COUNTIF(Internal_NTP_Servers!J2:J100,"✅ Active")/COUNTA(Internal_NTP_Servers!A2:A100)*100 | =IF(ACTUAL=100,"✅ PASS","⚠️ WARNING") |

**Section 2: Common Gaps Table (MANUAL ENTRY - Rows 15+)**

| Gap ID | Description | Severity | Impact | Remediation Plan | Responsible | Target Date | Status |
|--------|-------------|----------|--------|------------------|-------------|-------------|--------|
| [User fills] | [User fills] | Critical/High/Medium/Low | [User fills] | [User fills] | [User fills] | YYYY-MM-DD | Open/In Progress/Completed/Deferred |

**Section 3: Exception Management Note (ISMS Copilot Correction)**

After the gaps table, add paragraph:

> **For gaps that cannot be remediated within 90 days or require permanent exceptions:**
> 
> Reference **ISMS-POL-A.8.17 Section 3.3 (Exception Management)** for formal exception process. Submit exception request including risk assessment, compensating controls, and formal approval from CISO or Executive Management.

---

## Python Script Reference

**Script File:** `generate_assessment_1_time_sources.py`

**Script Location:** `/mnt/project/`

**Key Functions:**

- `create_styles()` - Defines all styling (lines 22-59)
- `create_instructions_sheet()` - Generates Instructions sheet (lines 66-129)
- `create_time_sources_sheet()` - Generates Time_Sources sheet (lines 131-223)
- `create_internal_ntp_servers_sheet()` - Generates Internal_NTP_Servers sheet (lines 225-318)
- `create_hierarchy_sheet()` - Generates Hierarchy sheet (lines 320-380)
- `create_compliance_summary_sheet()` - Generates Compliance_Summary sheet (lines 382-450)
- `main()` - Orchestrates workbook generation (lines 452-599)

**To regenerate workbook:**

```bash
cd /mnt/project
python3 generate_assessment_1_time_sources.py --output ISMS-A.8.17-Assessment-1-Time-Sources.xlsx
```

**Output:** Excel workbook ready for user completion per Part I User Guide.

---

**END OF SPECIFICATION**

---

*"Time is what keeps everything from happening at once."*
— Ray Cummings

<!-- QA_VERIFIED: 2026-02-06 -->
