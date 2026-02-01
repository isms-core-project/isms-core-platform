**ISMS-IMP-A.8.17-S1 — Time Source Configuration & Assessment**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.17: Clock Synchronization

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.17-S1 |
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

This document consists of two parts:

- **PART I: USER COMPLETION GUIDE** (Sections 1-8)
  - How to complete the Time Source Inventory Assessment workbook
  - Prerequisites, workflow, field-by-field guidance
  - Evidence collection, quality checks, and approval process

- **PART II: TECHNICAL SPECIFICATION** (Sections 9-onwards)
  - Section A: Implementation Guidance (platform-specific configurations and procedures)
  - Section B: Assessment Workbook Specification (Excel workbook structure, formulas, validation rules)


---

# PART I: USER COMPLETION GUIDE

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

**END OF PART I: USER COMPLETION GUIDE**

---

# PART II: TECHNICAL SPECIFICATION

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

<!-- QA_VERIFIED: 2026-01-31 -->
