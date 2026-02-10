<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.17-S1-UG:framework:UG:a.8.17-s1 -->
**ISMS-IMP-A.8.17-S1-UG - Time Source Configuration & Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.17: Clock Synchronization

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.17-S1-UG |
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

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.8.17-S1-TG.

---

**Audience:** Network Engineers, System Administrators, ISMS Officers completing the Time Source Inventory Assessment

---

# Assessment Overview

## Purpose & Scope

**Assessment Name:** ISMS-IMP-A.8.17-S1 - Time Source Inventory Assessment

**What This Assessment Covers:**

This assessment documents the time source infrastructure that provides authoritative time for all organizational systems. Think of this as mapping the "root of truth" for time across your entire IT environment. This assessment answers critical questions:

- **What are our authoritative time sources?** (GPS, NIST, Cloudflare, NTP Pool, etc.)
- **Do we have sufficient redundancy?** (Policy requires minimum 2 sources)
- **What is our internal NTP infrastructure?** (Which servers synchronize clients?)
- **Are we compliant with policy requirements?** (Stratum levels, availability, monitoring)
- **What is our time synchronization hierarchy?** (Stratum 0/1/2 architecture)

**Key Principle:** "Garbage time in = garbage logs out." Without authoritative, redundant time sources, every timestamp in every log becomes unreliable. This assessment ensures your time infrastructure is rock-solid.

Think of this as documenting the "master clocks" for your organization - just like a radio station needs atomic clocks for precise broadcast timing, your organization needs documented, authoritative time sources for logging, authentication, and forensics.

## What You'll Document

**Workbook Sheets You'll Complete:**

1. **Time_Sources** - External authoritative time sources (Stratum 0/1)

   - Public time services (NIST, Cloudflare, NTP Pool)
   - GPS-based time servers
   - Atomic clock sources
   - Provider details, SLAs, last verification dates
   - Status and availability

2. **Internal_NTP_Servers** - Organization's internal NTP infrastructure (Stratum 2)

   - NTP server inventory (hostnames, IP addresses)
   - Upstream source configuration
   - Redundancy groups and peer relationships
   - Monitoring status and health checks
   - Geographic distribution

3. **Hierarchy** - Visual representation of time synchronization architecture

   - Auto-generated diagram showing Stratum 0/1/2 relationships
   - Source-to-server-to-client data flow
   - Redundancy visualization

4. **Compliance_Summary** - Assessment results and policy compliance metrics

   - Count of external sources (requirement: ≥2)
   - Count of internal servers (requirement: ≥2)
   - Monitoring coverage percentage
   - Gap identification and remediation tracking

## How This Relates to Other A.8.17 Assessments

| Assessment | Focus | Relationship to A.8.17-S1 |
|------------|-------|---------------------------|
| **ISMS-IMP-A.8.17-S1** | **Time Source Infrastructure** | **THIS assessment - documents WHAT time sources exist** |
| ISMS-IMP-A.8.17-S2 | System Synchronization Verification | Uses S1 results to verify systems sync to documented sources |

**Assessment Flow:**
1. **A.8.17-S1 (THIS):** "We have NIST + Cloudflare as Stratum 1, plus 4 internal NTP servers"
2. **A.8.17-S2 (NEXT):** "95% of 1,234 systems are syncing to those 4 internal NTP servers"

You MUST complete S1 first - you can't verify systems synchronize (S2) until you've documented what they should synchronize TO (S1).

## Who Should Complete This Assessment

**Primary Stakeholders:**

1. **Network Engineers** - Know external time sources, NTP server deployments, network architecture
2. **Network Operations Manager** - Accountable for NTP infrastructure per policy
3. **System Administrators** - Understand NTP server configurations and monitoring
4. **ISMS Officer** - Conducts compliance assessment against policy requirements
5. **Security Engineers** - Validate time sources are trusted and secured

**Required Skills:**

- **NTP/Time Services Knowledge** - Understand Stratum levels, NTP hierarchy, time source types
- **Network Infrastructure Knowledge** - Know organization's NTP server deployments and configurations
- **Basic Time Source Selection** - Can evaluate GPS vs. NIST vs. NTP Pool vs. cloud providers
- **Monitoring Systems Familiarity** - Know how to verify monitoring is configured for NTP servers

**You DON'T need to be an NTP expert!** The assessment provides guidance on what constitutes authoritative sources, acceptable Stratum levels, and policy requirements.

## Time Commitment

- **Initial assessment (first time):** 3-6 hours
  - 1 hour: Identify all external time sources (DNS lookups, config reviews)
  - 1-2 hours: Inventory internal NTP servers (server list, configs, monitoring status)
  - 30 minutes: Document provider information and SLAs
  - 1 hour: Verify monitoring configurations
  - 30 minutes: Collect evidence (configs, screenshots)
  - 30 minutes-1 hour: Gap analysis and compliance review

- **Quarterly updates:** 1-2 hours
  - 30 minutes: Re-verify external source availability
  - 30 minutes: Check internal server health
  - 30 minutes: Update any configuration changes
  - 30 minutes: Review and close remediated gaps

**Pro Tip:** First assessment takes longer because you're discovering infrastructure. Subsequent quarterly reviews are much faster - just verify nothing changed and update "Last Verified" dates.

## Expected Outputs

Upon completion, you will have:

1. ✅ **Complete time source inventory** - All external authoritative sources documented
2. ✅ **Internal NTP server catalog** - Every internal NTP server with config details
3. ✅ **Redundancy verification** - Proof of ≥2 external sources and ≥2 internal servers (policy requirement)
4. ✅ **Stratum hierarchy map** - Visual showing time synchronization architecture
5. ✅ **Monitoring coverage** - Verification that NTP infrastructure is monitored with alerting
6. ✅ **Compliance status** - Pass/fail against policy requirements (REQ-817-001 through REQ-817-008)
7. ✅ **Gap identification** - All non-compliant areas documented with remediation plans
8. ✅ **Evidence register** - Config files, monitoring screenshots, SLA documentation

**What This Looks Like for Audit:**

When an auditor asks: *"How does your organization ensure accurate time across all systems?"*

You hand them this assessment and say:

> "We synchronize to two Stratum 1 external sources: NIST and Cloudflare. We operate 4 redundant internal NTP servers (Stratum 2) across two datacenters. All servers are monitored with alerting. 100% of our NTP infrastructure meets policy requirements. All documentation is in this assessment."

**Auditor reaction:** ✅ "This demonstrates systematic time source management with appropriate redundancy and monitoring. Excellent."

---

# Prerequisites

## Required Information

Before starting, gather the following:

**External Time Source Information:**

- [ ] **List of configured external time sources** from NTP server configs (`/etc/chrony.conf`, `/etc/ntp.conf`, etc.)
- [ ] **DNS names or IP addresses** for all external time services
- [ ] **Provider information** (NIST, Cloudflare, NTP Pool, cloud provider, GPS vendor)

**Internal NTP Server Information:**

- [ ] **Complete list of internal NTP servers** from asset inventory or server management system
- [ ] **NTP server configurations** (which external sources they use)
- [ ] **Peer relationships** (which NTP servers are configured as peers)
- [ ] **Geographic locations** (datacenter, region for each server)

**Monitoring Information:**

- [ ] **Monitoring system configuration** showing NTP server monitoring
- [ ] **Alert definitions** for NTP service failures
- [ ] **Recent health check data** for NTP servers

**Access Requirements:**

- [ ] **SSH/console access** to internal NTP servers (to review configs)
- [ ] **Monitoring system access** (to verify NTP monitoring)
- [ ] **DNS/Network documentation** access

## Required Tools

**For Configuration Review:**

- SSH client to access NTP servers
- Text editor to view config files (`/etc/chrony.conf`, `/etc/ntp.conf`)

**For Verification:**

- `nslookup` or `dig` for DNS resolution of time sources
- `chronyc tracking` or `ntpq -p` to verify NTP server synchronization
- Monitoring system UI to check NTP service status

**For Documentation:**

- Network diagrams (if available) showing NTP server placement
- Asset management system for server inventory

## Policy Requirements to Review

Before starting, familiarize yourself with key policy requirements from **ISMS-POL-A.8.17**:

**From Section 2.1 (External Authoritative Time Sources):**

- **REQ-817-001**: Minimum TWO (2) authoritative time sources required
- **REQ-817-002**: External sources must be Stratum 0 or Stratum 1 (primary sources required, Stratum 2+ acceptable for supplementary sources like NTP Pool)
- **REQ-817-003**: >99.9% uptime for each authoritative source
- **REQ-817-004**: Geographic diversity recommended for resilience

**From Section 2.2 (Internal NTP Infrastructure):**

- **REQ-817-005**: Minimum TWO (2) internal NTP servers required
- **REQ-817-006**: Internal servers must be Stratum 2 (synchronized to Stratum 1 external sources)
- **REQ-817-007**: High availability configuration with automatic failover
- **REQ-817-008**: Continuous monitoring with automated alerting for NTP infrastructure

You'll be verifying compliance with these requirements in the assessment.

---

# Assessment Workflow

## Recommended Completion Order

**STEP 1:** Identify external time sources

- Review NTP server configurations (`/etc/chrony.conf`, `/etc/ntp.conf`)
- Extract all `server` or `pool` directives
- Document public sources (NIST, Cloudflare, NTP Pool) vs. private (GPS, organization-owned)

**STEP 2:** Research provider information

- For public sources (NIST, Cloudflare): Document well-known details
- For GPS/atomic clocks: Document vendor and model
- For cloud providers (AWS Time Sync, Azure NTP): Document service SLA

**STEP 3:** Verify external source availability

- Use `nslookup` or `dig` to resolve hostnames
- Optional: Use `chronyc tracking` to verify sources are reachable from NTP servers

**STEP 4:** Document in Time_Sources sheet

- Fill one row per external time source
- Mark required fields ([*]) as mandatory
- Use dropdown selections for Type and Status

**STEP 5:** Inventory internal NTP servers

- Get server list from asset management or infrastructure documentation
- For each NTP server, note: hostname, IP, location, monitoring status

**STEP 6:** Review NTP server configurations

- SSH to each internal NTP server
- Check `chronyc tracking` or `ntpq -p` to see upstream sources
- Identify peer servers (other internal NTP servers in peer relationship)

**STEP 7:** Document in Internal_NTP_Servers sheet

- Fill one row per internal NTP server
- Document upstream sources (from Time_Sources sheet)
- Note peer servers, monitoring status

**STEP 8:** Review auto-generated Hierarchy sheet

- Verify visualization accurately reflects your architecture
- Check that external sources → internal servers relationships are correct

**STEP 9:** Review Compliance_Summary sheet

- Check compliance metrics (≥2 external, ≥2 internal, 100% monitoring)
- Document any gaps in gaps table
- Create remediation plans for non-compliance

**STEP 10:** Collect evidence

- Save NTP config files
- Screenshot monitoring dashboards
- Document provider SLAs

**STEP 11:** Internal review and approval

- Peer review for technical accuracy
- ISMS Officer review for policy compliance

## Data Sources

**Where to find information for this assessment:**

**External Time Sources:**

- `/etc/chrony.conf` (Linux chrony config) - look for `server` or `pool` lines
- `/etc/ntp.conf` (Linux ntp config) - look for `server` lines
- Windows NTP config: `w32tm /query /configuration`
- Network device configs (show ntp servers)

**Internal NTP Server Inventory:**

- Asset management system (CMDB)
- Server inventory spreadsheets
- Infrastructure documentation
- Network diagrams

**Monitoring Status:**

- Nagios/Zabbix/Prometheus dashboards
- SIEM NTP service checks
- Custom monitoring scripts

---

# Sheet-by-Sheet Completion Guidance

## Sheet: Time_Sources (External Authoritative Time Sources)

**Purpose:** Document all external authoritative time sources that provide time to your internal NTP infrastructure.

**Column-by-Column Guidance:**

| Column | Field Name | Required? | Guidance | Where to Find This |
|--------|------------|-----------|----------|-------------------|
| A | **Source Name [*]** | REQUIRED | DNS hostname or descriptive name of time source | NTP server config (`/etc/chrony.conf`, `/etc/ntp.conf`) |
| | | | Example: `time.nist.gov`, `time.cloudflare.com`, `0.pool.ntp.org` | Look for `server` or `pool` directives |
| | | | **For GPS:** Use model/location like `GPS-DC1-Roof` | Asset inventory, vendor docs |
| | | | **Tip:** Use official DNS name, not IP address (IPs may change) | |
| B | **Type [*]** | REQUIRED | Select from dropdown | Identify based on source |
| | | | **Dropdown options:** 🛰️ GPS \| 🏛️ NIST \| 🌐 NTP Pool \| ☁️ Cloudflare \| 📍 Google \| 🏢 Regional Government \| ⚛️ Atomic Clock \| ☁️ Cloud Provider \| 📋 Other | |
| | | | **GPS**: Organization-owned GPS receiver | Physical hardware on premise |
| | | | **NIST**: time.nist.gov or time-*.nist.gov servers | |
| | | | **NTP Pool**: *.pool.ntp.org servers | |
| | | | **Cloudflare**: time.cloudflare.com | |
| | | | **Google**: time.google.com | |
| | | | **Regional Government**: Country-specific time services (e.g., ptbtime1.ptb.de for Germany) | |
| | | | **Atomic Clock**: Organization-owned atomic clock | |
| | | | **Cloud Provider**: AWS Time Sync, Azure NTP, GCP NTP | Cloud documentation |
| C | **IP/Hostname [*]** | REQUIRED | Full DNS name or IP address | Same as column A (usually DNS name) |
| | | | Example: `time.nist.gov`, `169.254.169.123` (AWS), `216.239.35.0` (Google) | NTP config, DNS lookup |
| | | | **Prefer DNS names** over IP addresses (more resilient to provider changes) | |
| D | **Stratum [*]** | REQUIRED | Stratum level reported by source | Provider documentation or `chronyc sources` output |
| | | | **IMPORTANT:** Per ISMS Copilot correction, distinguish: | ISMS-POL-A.8.17 Section 2.1 |
| | | | **Primary sources (required):** Stratum 0 or 1 (GPS, NIST, government services) | |
| | | | **Supplementary sources (acceptable):** Stratum 2+ (NTP Pool, cloud providers) | |
| | | | **Policy requirement:** At least 2 PRIMARY (Stratum 0/1) sources required | |
| | | | Example: `0` (GPS/atomic clock), `1` (NIST), `2` (NTP Pool) | |
| E | **Geographic Location** | Optional | Physical location or geographic distribution | Provider documentation |
| | | | Example: `United States`, `Global (Anycast)`, `Europe`, `On-premises (Zurich datacenter)` | |
| | | | **For cloud:** Note global distribution (e.g., `Global (Anycast)` for Cloudflare) | Cloud provider docs |
| | | | **For GPS:** Note specific location (`Datacenter 1 Roof, Zurich`) | Physical site survey |
| F | **Provider** | Optional | Organization or entity providing the time service | Well-known for public services |
| | | | Example: `NIST`, `Cloudflare`, `NTP Pool Project`, `Google`, `Amazon Web Services`, `GPS Vendor XYZ` | |
| G | **Availability SLA** | Optional | Service level agreement or expected uptime | Provider documentation |
| | | | **Public sources:** Usually `Public (no SLA)` or `Best Effort` | NIST/Cloudflare docs |
| | | | **Commercial sources:** Actual SLA percentage (e.g., `99.99% uptime`) | Vendor contract |
| | | | **Organization-owned:** Internal SLA or `N/A` | |
| H | **Last Verified [*]** | REQUIRED | Date YOU verified this source is configured and reachable | Today's date when completing assessment |
| | | | **Format:** YYYY-MM-DD | Example: `2026-01-16` |
| | | | **Update quarterly:** Each assessment cycle, update this date after re-verification | |
| | | | **How to verify:** DNS lookup, ping, or check `chronyc sources` showing source is reached | |
| I | **Status** | Optional | Current operational status | Monitoring system, manual verification |
| | | | **Dropdown:** ✅ Active \| ❌ Inactive \| ⚠️ Testing \| ♻️ Decommissioned | |
| | | | **Active**: Currently in use and working | |
| | | | **Inactive**: Configured but not currently used (backup) | |
| | | | **Testing**: Being evaluated for production use | |
| | | | **Decommissioned**: No longer used, pending removal from configs | |
| J | **Notes** | Optional | Any additional context | Free text |
| | | | Example: `Primary authoritative source`, `Backup to NIST`, `Requires VPN connection`, `GPS antenna on datacenter roof` | |

**How Many Rows to Complete:**

- **Minimum:** 2 rows (policy requires ≥2 external authoritative sources per REQ-817-001)
- **Typical:** 2-4 rows (primary + backup sources)
- **Common pattern:** 2-3 primary sources (Stratum 0/1) + NTP Pool as supplementary

**Example Completed Rows:**

| Source Name | Type | IP/Hostname | Stratum | Location | Provider | SLA | Last Verified | Status | Notes |
|-------------|------|-------------|---------|----------|----------|-----|---------------|--------|-------|
| time.nist.gov | 🏛️ NIST | time.nist.gov | 1 | United States | NIST | Public (no SLA) | 2026-01-16 | ✅ Active | Primary authoritative source |
| time.cloudflare.com | ☁️ Cloudflare | time.cloudflare.com | 1 | Global (Anycast) | Cloudflare | Public (no SLA) | 2026-01-16 | ✅ Active | Secondary authoritative source |
| 0.pool.ntp.org | 🌐 NTP Pool | 0.pool.ntp.org | 2 | Global | NTP Pool Project | Public (no SLA) | 2026-01-16 | ✅ Active | Supplementary backup source |

**Policy Compliance Check:**

- [ ] At least 2 PRIMARY sources (Stratum 0/1) documented? (REQ-817-001, REQ-817-002)
- [ ] All sources have Type selected from dropdown?
- [ ] All sources have Stratum level documented?
- [ ] All sources have Last Verified date within last 90 days?
- [ ] At least one source has geographic diversity (if multiple sources from different providers)?
- [ ] Supplementary sources (Stratum 2+) clearly distinguished from primary?

**Common Mistakes to Avoid:**

- ❌ **Only documenting one source** - Policy requires ≥2 for redundancy
- ❌ **Confusing internal NTP servers with external sources** - This sheet is EXTERNAL only (put internal servers in next sheet)
- ❌ **Not distinguishing primary vs supplementary sources** - Mark Stratum 0/1 as primary, Stratum 2+ as supplementary per policy
- ❌ **Using outdated Last Verified dates** - Update every quarterly assessment
- ❌ **Documenting sources not actually in use** - Only document sources configured in NTP server configs
- ❌ **Missing geographic information** - Helps demonstrate resilience against regional outages

---

## Sheet: Internal_NTP_Servers (Internal NTP Infrastructure)

**Purpose:** Document all internal NTP servers that synchronize to external sources and provide time to client systems.

**Column-by-Column Guidance:**

| Column | Field Name | Required? | Guidance | Where to Find This |
|--------|------------|-----------|----------|-------------------|
| A | **Server Name [*]** | REQUIRED | Hostname of internal NTP server | Asset management, server inventory |
| | | | Example: `ntp1.dc1.example.com`, `ntp-primary.example.com`, `time-server-01` | DNS, server configs |
| | | | **Use FQDN** for clarity and consistency | |
| B | **IP Address [*]** | REQUIRED | Primary IP address | DNS lookup, network documentation |
| | | | Example: `10.0.1.10`, `192.168.1.50` | `nslookup` or `dig` |
| C | **Stratum [*]** | REQUIRED | Expected Stratum level (should be 2 or 3) | `chronyc tracking` or `ntpq -p` output |
| | | | **Policy requirement (REQ-817-006):** Internal servers MUST be Stratum 2 | ISMS-POL-A.8.17 Section 2.2 |
| | | | **Stratum 2**: Synchronized to Stratum 1 external sources (correct) | |
| | | | **Stratum 3**: Synchronized to Stratum 2 servers (acceptable for secondary tier) | |
| | | | **⚠️ Stratum 16**: UNSYNCHRONIZED (FAILURE - needs remediation) | |
| D | **Upstream Sources [*]** | REQUIRED | Which external time sources this server synchronizes to | `/etc/chrony.conf`, `chronyc sources` |
| | | | Example: `time.nist.gov, time.cloudflare.com` | NTP config file |
| | | | **Must match sources from Time_Sources sheet** | Cross-reference |
| | | | List multiple sources comma-separated | |
| E | **Location/Datacenter** | Optional | Physical or logical location | Asset management, network diagrams |
| | | | Example: `Datacenter 1 (Zurich)`, `AWS eu-west-1`, `Azure West Europe` | |
| | | | **Helps verify geographic distribution** per REQ-817-005 | |
| F | **Redundancy Group** | Optional | Logical grouping for failover | Infrastructure documentation |
| | | | Example: `Primary`, `Secondary`, `DC1-Group`, `Cloud-NTP` | |
| | | | Helps demonstrate high availability (REQ-817-007) | |
| G | **Peer Servers** | Optional | Other internal NTP servers configured as peers | `/etc/chrony.conf`, `/etc/ntp.conf` |
| | | | Example: `ntp2.dc1.example.com, ntp3.dc1.example.com` | Look for `peer` directives in config |
| | | | Peer relationships improve consistency and failover | |
| H | **Monitoring Status [*]** | REQUIRED | Is this server monitored with alerting? | Monitoring system (Nagios, Zabbix, etc.) |
| | | | **IMPORTANT (ISMS Copilot correction):** Dropdown expanded to four states: | |
| | | | ✅ **Monitored with Alerting** - NTP service monitored AND alerts configured (REQUIRED per REQ-817-008) | |
| | | | ⚠️ **Monitored (No Alerting)** - Monitored but no alerting (NON-COMPLIANT) | |
| | | | ❌ **Not Monitored** - No monitoring configured (NON-COMPLIANT) | |
| | | | 🔧 **Monitoring Failed** - Monitoring configured but broken (NEEDS REMEDIATION) | |
| | | | **Policy requirement:** ALL internal NTP servers MUST have "Monitored with Alerting" | |
| I | **Last Health Check [*]** | REQUIRED | Date of last health check verification | Monitoring system, manual check |
| | | | **Format:** YYYY-MM-DD | Example: `2026-01-16` |
| | | | **ISMS Copilot correction:** Reference verification frequency requirements: | |
| | | | **7 days**: Maximum age for compliance metric calculations | ISMS-POL-A.8.17 Section 3.2 |
| | | | **30 days**: Maximum policy threshold for compliance | |
| | | | **Update quarterly:** Re-verify health during each assessment | |
| J | **Status [*]** | REQUIRED | Current operational status | Monitoring system, `chronyc tracking` |
| | | | **Dropdown:** ✅ Active \| ❌ Inactive \| 🛠️ Maintenance \| ⚠️ Failed | |
| | | | **Active**: Running and synchronized | |
| | | | **Inactive**: Server exists but NTP service not running | |
| | | | **Maintenance**: Temporarily offline for updates | |
| | | | **Failed**: Service failure, not synchronizing (Stratum 16) | |
| K | **Notes** | Optional | Additional context | Free text |
| | | | Example: `Primary NTP server for DC1`, `Syncs to GPS on roof`, `Redundant pair with ntp2` | |

**How Many Rows to Complete:**

- **Minimum:** 2 rows (policy requires ≥2 internal NTP servers per REQ-817-005)
- **Typical:** 2-6 rows (depends on datacenter count and redundancy requirements)
- **Best Practice:** At least 2 per datacenter/region for local redundancy

**Example Completed Rows:**

| Server Name | IP Address | Stratum | Upstream Sources | Location | Group | Peers | Monitoring Status | Last Health | Status | Notes |
|-------------|------------|---------|------------------|----------|-------|-------|-------------------|-------------|--------|-------|
| ntp1.dc1.example.com | 10.0.1.10 | 2 | time.nist.gov, time.cloudflare.com | Datacenter 1 (Zurich) | Primary | ntp2.dc1.example.com | ✅ Monitored with Alerting | 2026-01-16 | ✅ Active | Primary NTP for DC1 |
| ntp2.dc1.example.com | 10.0.1.11 | 2 | time.nist.gov, time.cloudflare.com | Datacenter 1 (Zurich) | Primary | ntp1.dc1.example.com | ✅ Monitored with Alerting | 2026-01-16 | ✅ Active | Peer of ntp1 |
| ntp1.dc2.example.com | 10.0.2.10 | 2 | time.nist.gov, 0.pool.ntp.org | Datacenter 2 (Geneva) | Secondary | ntp2.dc2.example.com | ✅ Monitored with Alerting | 2026-01-16 | ✅ Active | Primary NTP for DC2 |

**Policy Compliance Check:**

- [ ] At least 2 internal NTP servers documented? (REQ-817-005)
- [ ] All servers show Stratum 2 or 3? (REQ-817-006 - Stratum 2 required for primary tier)
- [ ] All servers have "✅ Monitored with Alerting" status? (REQ-817-008)
- [ ] All servers have Last Health Check within 30 days? (Updated per verification frequency requirements)
- [ ] All servers synchronized to external sources from Time_Sources sheet? (Cross-reference column D)
- [ ] Geographic distribution across datacenters documented? (REQ-817-004 - recommended)
- [ ] Peer relationships configured for high availability? (REQ-817-007)

**Common Mistakes to Avoid:**

- ❌ **Only documenting one NTP server** - Policy requires ≥2 for redundancy
- ❌ **Selecting "Monitored (No Alerting)"** - Policy requires alerting, not just monitoring
- ❌ **Not updating Last Health Check dates** - Must verify health quarterly
- ❌ **Upstream Sources don't match Time_Sources sheet** - Should reference same external sources
- ❌ **Stratum 16 with Status "Active"** - Stratum 16 = not synchronized = must be "Failed" status
- ❌ **Missing peer configurations** - High availability (REQ-817-007) requires peer relationships

---

## Sheet: Hierarchy (Time Synchronization Architecture)

**Purpose:** Auto-generated visualization of time synchronization hierarchy from Stratum 0/1/2 sources.

**THIS SHEET IS AUTO-CALCULATED/GENERATED** - You don't manually fill it in.

**What You'll See:**

The script generates a visual representation showing:

**Stratum 0/1 Level (External Authoritative Sources):**

- All sources from Time_Sources sheet
- Color-coded by type (GPS, NIST, NTP Pool, etc.)

**Stratum 2 Level (Internal NTP Servers):**

- All servers from Internal_NTP_Servers sheet
- Connected to their upstream sources

**Data Flow Arrows:**

- External Source → Internal NTP Server relationships
- Peer relationships between internal servers

**What to Review:**

1. **Does the hierarchy accurately reflect your architecture?**

   - Verify external sources are at top (Stratum 0/1)
   - Verify internal servers in middle (Stratum 2)
   - Client systems would be Stratum 3 (not shown in this assessment)

2. **Are all upstream source relationships correct?**

   - Each internal server should connect to sources from Time_Sources sheet
   - If a server shows connection to unlisted source → update Time_Sources sheet

3. **Is redundancy visible?**

   - You should see multiple paths from external → internal
   - No single point of failure in time infrastructure

**If Hierarchy Doesn't Match Reality:**

Go back and correct:

- Time_Sources sheet (add missing external sources)
- Internal_NTP_Servers sheet Column D (Upstream Sources) - ensure all are listed

---

## Sheet: Compliance_Summary (Policy Compliance Metrics & Gap Tracking)

**Purpose:** Auto-calculated compliance metrics and manual gap documentation.

**THIS SHEET HAS BOTH AUTO-CALCULATED AND MANUAL SECTIONS**

**Auto-Calculated Compliance Metrics:**

| Metric | Policy Requirement | Actual | Status |
|--------|-------------------|--------|--------|
| **External Time Sources** | ≥2 (REQ-817-001) | [Auto-count from Time_Sources] | ✅ PASS / ❌ FAIL |
| **Primary Sources (Stratum 0/1)** | ≥2 (REQ-817-002) | [Auto-count Stratum 0/1] | ✅ PASS / ❌ FAIL |
| **Internal NTP Servers** | ≥2 (REQ-817-005) | [Auto-count from Internal_NTP_Servers] | ✅ PASS / ❌ FAIL |
| **Stratum 2 Compliance** | 100% (REQ-817-006) | [% servers Stratum 2 or 3] | ✅ PASS / ❌ FAIL |
| **Monitoring with Alerting** | 100% (REQ-817-008) | [% servers "✅ Monitored with Alerting"] | ✅ PASS / ❌ FAIL |
| **Active Server Status** | 100% | [% servers Status = Active] | ✅ PASS / ⚠️ WARNING |

**Common Gaps Table (MANUAL ENTRY - YOU complete this):**

| Gap ID | Description | Severity | Impact | Remediation Plan | Responsible | Target Date | Status |
|--------|-------------|----------|--------|------------------|-------------|-------------|--------|
| GAP-001 | Only 1 external source configured | Critical | Single point of failure | Add Cloudflare as 2nd source | Network Ops | 2026-02-01 | Open |
| GAP-002 | ntp3.dc2 not monitored with alerting | High | No failure detection | Configure Nagios alert | Monitoring Team | 2026-01-31 | In Progress |

**How to Complete Common Gaps:**

1. **Review each compliance metric** - Any "❌ FAIL" or "⚠️ WARNING" is a gap
2. **For each gap, document:**

   - **Gap ID**: Sequential (GAP-001, GAP-002, etc.)
   - **Description**: What's non-compliant?
   - **Severity**: Critical (policy violation) / High (best practice) / Medium / Low
   - **Impact**: What breaks? Example: "Cannot correlate logs if single source fails"
   - **Remediation Plan**: Specific action to fix (not vague "improve")
   - **Responsible**: Person/team who will fix it
   - **Target Date**: When will it be fixed? (YYYY-MM-DD)
   - **Status**: Open / In Progress / Completed / Deferred

**Special Note (ISMS Copilot Correction):**

**For gaps that cannot be remediated within 90 days or require permanent exceptions:**

Reference **ISMS-POL-A.8.17 Section 3.3 (Exception Management)** for formal exception process. Gaps requiring exceptions include:

- Air-gapped systems without GPS access
- Vendor limitations preventing NTP configuration
- Systems requiring >90 days for remediation

Document exception request separately per policy Section 3.3, including:

- Risk assessment
- Compensating controls
- Formal approval from CISO or Executive Management

---

# Evidence Collection

## Required Evidence Types

**Configuration Evidence:**

- [ ] **NTP server config files** - `/etc/chrony.conf` or `/etc/ntp.conf` from each internal NTP server
- [ ] **Upstream source verification** - Output of `chronyc sources -v` or `ntpq -p` showing external sources

**Monitoring Evidence:**

- [ ] **Monitoring dashboard screenshots** - Showing all internal NTP servers monitored
- [ ] **Alert configuration** - Proof that alerting is configured (alert definitions, notification settings)
- [ ] **Recent health checks** - Monitoring system logs showing recent NTP service checks

**Provider Documentation:**

- [ ] **Public source documentation** - Links to NIST/Cloudflare/NTP Pool documentation (if using public sources)
- [ ] **SLA documentation** - Vendor contracts or SLA pages (if using commercial sources)
- [ ] **GPS/Atomic clock specs** - Vendor documentation (if using physical time sources)

**Compliance Evidence:**

- [ ] **This completed assessment workbook** - With all sheets filled
- [ ] **Network diagrams** - Showing NTP server placement (optional but helpful)

## How to Collect Evidence

**For NTP Configuration Files:**

```bash
# On each internal NTP server (Linux with chrony)
sudo cat /etc/chrony.conf > evidence-ntp-config-ntp1.dc1.txt

# Or for traditional ntp
sudo cat /etc/ntp.conf > evidence-ntp-config-ntp1.dc1.txt

# Verify upstream sources
chronyc sources -v > evidence-ntp-sources-ntp1.dc1.txt

# Or for traditional ntp
ntpq -p > evidence-ntp-peers-ntp1.dc1.txt
```

**For Monitoring Screenshots:**

1. Open monitoring system (Nagios, Zabbix, Prometheus, etc.)
2. Navigate to NTP service checks
3. Capture screenshot showing:

   - All internal NTP servers listed
   - Service status (UP/OK)
   - Alert configuration visible

4. Save as `evidence-ntp-monitoring-[date].png`

**For Alert Configuration:**

Export or screenshot alert definitions showing:

- NTP service down alert
- NTP sync failure alert
- Notification recipients

## Evidence Naming Convention

```
Evidence Type: NTP-[SERVER/CATEGORY]-[DATE].ext

Examples:
NTP-config-ntp1.dc1-20260116.txt          (Config file)
NTP-sources-ntp1.dc1-20260116.txt         (Source verification)
NTP-monitoring-dashboard-20260116.png     (Screenshot)
NTP-alert-config-20260116.pdf            (Alert definitions)
NTP-provider-sla-cloudflare.pdf          (Provider SLA)
```

## Where to Store Evidence

**Options:**
1. **Embedded in workbook** - Add sheet called "Evidence" with file attachments (Excel supports this)
2. **Network share** - `\\fileserver\ISMS\Evidence\A.8.17\S1\2026-Q1\`
3. **Document management** - SharePoint, Confluence, etc.
4. **Reference in workbook** - Put file paths in Notes columns

**Recommendation:** Store centrally (option 2 or 3), reference paths in workbook Notes fields.

---

# Common Pitfalls & How to Avoid Them

## Confusing External and Internal Sources

**MISTAKE:**
Documenting internal NTP servers (ntp1.example.com) in the Time_Sources sheet.

**WHY IT'S WRONG:**
Time_Sources sheet is for EXTERNAL authoritative sources only (NIST, Cloudflare, GPS, etc.). Internal servers go in Internal_NTP_Servers sheet.

**HOW TO AVOID:**

- **Time_Sources sheet**: Only document sources your internal NTP servers sync TO
- **Internal_NTP_Servers sheet**: Only document NTP servers YOU operate
- If it's inside your organization and YOU manage it → Internal_NTP_Servers
- If it's external (NIST, Cloudflare, etc.) → Time_Sources

## Not Distinguishing Primary vs Supplementary Sources

**MISTAKE:**
Marking NTP Pool (Stratum 2) as equal to NIST (Stratum 1) without noting primary/supplementary distinction.

**WHY IT'S WRONG:**
ISMS Copilot correction requires distinguishing:

- **Primary sources** (Stratum 0/1 REQUIRED): GPS, NIST, government services
- **Supplementary sources** (Stratum 2+ acceptable): NTP Pool, cloud providers

Policy requires at least 2 PRIMARY sources.

**HOW TO AVOID:**

- In Notes column, mark NIST/GPS as "Primary authoritative source"
- Mark NTP Pool/cloud as "Supplementary backup source"
- Ensure at least 2 Stratum 0/1 sources exist

## Selecting "Monitored (No Alerting)" Status

**MISTAKE:**
Documenting internal NTP servers as "⚠️ Monitored (No Alerting)" and considering it compliant.

**WHY IT'S WRONG:**
ISMS Copilot correction clarified that REQ-817-008 requires ALERTING, not just monitoring. "Monitored (No Alerting)" = NON-COMPLIANT.

**HOW TO AVOID:**

- ALL internal NTP servers MUST have "✅ Monitored with Alerting" status
- If monitoring exists but no alerts → Document as gap, add alerting
- Configure alerts for: NTP service down, sync failure, Stratum 16

## Outdated "Last Verified" or "Last Health Check" Dates

**MISTAKE:**
Keeping "Last Verified" dates from 6 months ago without re-verification.

**WHY IT'S WRONG:**
Policy compliance requires recent verification (7-day for metrics, 30-day maximum). Stale dates make assessment invalid.

**HOW TO AVOID:**

- Update "Last Verified" to current date when completing quarterly assessment
- Update "Last Health Check" to current date after checking monitoring
- Set calendar reminder for quarterly re-verification

## Only Documenting One Time Source

**MISTAKE:**
Documenting only time.nist.gov as single external source.

**WHY IT'S WRONG:**
REQ-817-001 requires minimum 2 external authoritative sources for redundancy. Single source = non-compliant.

**HOW TO AVOID:**

- Add second source (Cloudflare, NTP Pool, another NIST server)
- Document in Time_Sources sheet
- Configure internal NTP servers to use both
- Verify with `chronyc sources` or `ntpq -p`

## Missing Geographic Diversity Documentation

**MISTAKE:**
Not documenting geographic location, making it impossible to assess resilience.

**WHY IT'S WRONG:**
While not mandatory, REQ-817-004 recommends geographic diversity. Without location documentation, you can't demonstrate it.

**HOW TO AVOID:**

- Fill "Geographic Location" column for all sources
- For public sources: Note global distribution (e.g., "Global (Anycast)")
- For internal servers: Note datacenter/region
- This helps demonstrate resilience planning

---

# Quality Checklist

Before submitting for approval, verify:

**Data Completeness:**

- [ ] All required fields ([*]) completed in Time_Sources sheet
- [ ] All required fields ([*]) completed in Internal_NTP_Servers sheet
- [ ] At least 2 rows in Time_Sources (external sources)
- [ ] At least 2 rows with Stratum 0/1 in Time_Sources (primary sources)
- [ ] At least 2 rows in Internal_NTP_Servers (internal NTP servers)
- [ ] All "Last Verified" and "Last Health Check" dates within 30 days

**Data Accuracy:**

- [ ] Upstream Sources in Internal_NTP_Servers match sources in Time_Sources sheet
- [ ] All Stratum levels are realistic (0, 1, 2, or 3 - never 16 for Active servers)
- [ ] DNS names resolve correctly (verified with nslookup/dig)
- [ ] Provider information is accurate (verified against provider websites)

**Policy Compliance:**

- [ ] ≥2 external authoritative sources (REQ-817-001)
- [ ] ≥2 primary sources with Stratum 0/1 (REQ-817-002)
- [ ] ≥2 internal NTP servers (REQ-817-005)
- [ ] All internal servers Stratum 2 or 3 (REQ-817-006)
- [ ] 100% of internal servers "✅ Monitored with Alerting" (REQ-817-008)
- [ ] All Active servers have Last Health Check within 30 days (7-day for compliance metric)

**Gap Documentation:**

- [ ] All non-compliant items documented in Compliance_Summary gaps table
- [ ] All gaps have severity rating
- [ ] All gaps have remediation plans with target dates
- [ ] Permanent exceptions reference ISMS-POL-A.8.17 Section 3.3

**Evidence:**

- [ ] NTP config files collected (minimum 1 per internal server)
- [ ] Monitoring screenshots showing all servers monitored
- [ ] Alert configuration documented
- [ ] Evidence files named consistently
- [ ] Evidence storage location documented

**Professional Presentation:**

- [ ] No spelling errors or typos
- [ ] Consistent formatting in Notes fields
- [ ] Dropdown selections used (not free text where dropdowns exist)
- [ ] Example rows removed or clearly marked as examples

---

# Review & Approval Process

## Internal Review (Before Submission)

**Step 1: Self-Review**

- Use Quality Checklist above
- Spot-check external source reachability (DNS lookup, ping)
- Verify internal server inventory is complete (cross-check with asset management)

**Step 2: Peer Review** (Recommended)

- Have another Network Engineer review technical accuracy
- Focus on: Are upstream sources correct? Are Stratum levels right? Is monitoring actually configured?

**Step 3: ISMS Officer Review** (Required)

- ISMS Officer checks policy compliance
- Verifies: ≥2 sources? 100% monitoring with alerting? All gaps documented?

## Formal Approval Workflow

**Level 1: Network Operations Manager**

- **Reviews:** Technical accuracy, NTP infrastructure completeness
- **Approves:** External source selection, internal server configurations
- **Sign-off location:** Compliance_Summary sheet → Approval section

**Level 2: Chief Information Security Officer (CISO)**

- **Reviews:** Policy compliance, gap remediation plans, risk acceptance
- **Approves:** Assessment meets ISMS requirements
- **Sign-off location:** Compliance_Summary sheet → Approval section

**Level 3: Executive Management** (if <100% compliance)

- **Reviews:** Risk of non-compliance, budget for remediation
- **Approves:** Risk acceptance for low compliance or extended remediation timelines
- **Sign-off location:** Compliance_Summary sheet → Executive Approval section

## Approval Criteria

**Assessment will be APPROVED if:**

- All required fields completed
- ≥2 external sources documented (including ≥2 primary Stratum 0/1)
- ≥2 internal NTP servers documented
- Compliance ≥90% OR documented risk acceptance for <90%
- All gaps have remediation plans
- Evidence collected and accessible

**Assessment will be REJECTED if:**

- Missing required fields (Source Name, Stratum, etc.)
- <2 external sources OR <2 primary sources (policy violation)
- <2 internal NTP servers (policy violation)
- Internal servers not monitored with alerting (no remediation plan)
- Gaps without remediation plans
- No evidence collected

## Post-Approval

**After approval:**
1. **File final version** in ISMS document repository
2. **Update ISMS tracking** (S1 assessment completed date)
3. **Schedule next quarterly assessment** (set calendar reminder)
4. **Begin gap remediation** (assign to responsible parties from gaps table)
5. **Provide to S2 assessment** (S2 needs S1 results to verify client systems sync to documented servers)
6. **Provide to auditors** when requested

**Quarterly Updates:**

- Re-verify external source availability (DNS lookups, ping tests)
- Check internal server health (monitoring dashboards)
- Update "Last Verified" and "Last Health Check" dates
- Close remediated gaps, add new gaps if found
- Refresh Compliance_Summary metrics
- Brief review/approval (not full formal approval unless compliance drops significantly)

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
