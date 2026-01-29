# ISMS-IMP-A.8.23.2 - Network Coverage Assessment
## Assessment Specification with User Completion Guide
### ISO/IEC 27001:2022 Control A.8.23: Web Filtering

---

## Document Control

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.23.2 |
| **Version** | 1.0 |
| **Assessment Area** | Web Filtering Network Coverage & Deployment Topology |
| **Related Policy** | ISMS-POL-A.8.23, Section 2.1 (Threat Protection Requirements) |
| **Purpose** | Verify WHERE web filtering is applied across network topology, identify coverage gaps, and ensure comprehensive protection across all network segments where users/devices access the internet |
| **Target Audience** | Network Engineers, Security Engineers, Infrastructure Team, System Administrators, System Owners, Compliance Officers, Auditors, Workbook Developers (Python/Excel script maintainers) |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Quarterly or After Major Infrastructure Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Web Filtering Network Coverage assessment workbook | ISMS Implementation Team |

### Document Structure

This document consists of two parts:

- **PART I: USER COMPLETION GUIDE**
  - Assessment Overview
  - Prerequisites
  - Assessment Workflow
  - Question-by-Question Guidance
  - Evidence Collection
  - Common Pitfalls
  - Quality Checklist
  - Review & Approval

- **PART II: TECHNICAL SPECIFICATION**
  - Workbook Structure
  - Sheet-by-Sheet Specifications
  - Cell Styling Reference

**Target Audiences:**

- **Part I:** Assessment users (Network Team, Security Team, Infrastructure Team, System Owners)
- **Part II:** Workbook developers (Python/Excel script maintainers)

---

# PART I: USER COMPLETION GUIDE

**Audience:** Network Team, Security Team, Infrastructure Team, System Owners

---

## Assessment Overview

### What This Assessment Evaluates

This assessment verifies WHERE web filtering is deployed across [Organization]'s network topology. Unlike Assessment 1 (which documents WHAT filtering solutions you have), this assessment focuses on COVERAGE - ensuring every network segment where users access the internet has appropriate filtering protection.

### Why This Matters

This assessment verifies [Organization]'s compliance with:

- ISO/IEC 27001:2022 Control A.8.23: Web Filtering
- ISMS-POL-A.8.23, Section 2.1 (Threat Protection Requirements): Threat Protection Requirements (Section 2.1.1: "SHALL apply web filtering across all network segments")

Web-based threats don't respect network boundaries. A single unprotected network segment becomes an attacker entry point. This assessment ensures comprehensive coverage by systematically mapping every network segment to deployed filtering solutions, calculating coverage percentages, and identifying gaps.

### What You'll Document

- Complete inventory of network segments (LAN, WLAN, VPN, cloud, guest, branch, mobile, etc.)
- Traffic flow and filtering enforcement points for each segment
- Which filtering solutions protect which segments
- Coverage percentages (0-100% for each segment)
- Coverage gaps and remediation plans
- Approved exemptions (with justification and approval)
- Verification test results confirming filtering effectiveness

**Key Principle:** This assessment is **topology-agnostic**. You document YOUR specific network architecture (whatever it is) and verify filtering coverage across ALL segments. The framework adapts to any network design - traditional perimeter, cloud-first, zero-trust, hybrid, etc.

### How This Relates to Other Assessments

- **ISMS-IMP-A.8.23.1** (Infrastructure): Documents WHAT filtering solutions you have
- **ISMS-IMP-A.8.23.2** (THIS): Documents WHERE those solutions are deployed
- **ISMS-IMP-A.8.23.3** (Policy Configuration): Documents HOW those solutions are configured

All three must align - solutions identified in Assessment 1 should appear in Coverage Matrix here.

**Estimated Time:** 6-12 hours depending on network complexity

---

## Prerequisites

Before starting this assessment, ensure you have:

**Access & Permissions:**

- Access to network diagrams and topology documentation
- Access to VLAN/subnet configurations
- Access to firewall/routing policies
- Access to DHCP/DNS server configurations
- Access to VPN concentrator configurations
- Access to WiFi controller configurations
- Access to cloud service consoles (if applicable)
- Ability to perform connectivity tests from various segments

### Required Information

- Complete network topology diagrams (Layer 2 and Layer 3)
- VLAN assignments and IP addressing schemes
- List of all physical locations (offices, datacenters, branches)
- Remote access methods (VPN, direct cloud, zero-trust)
- Cloud infrastructure architecture (if applicable)
- Guest/partner network configurations
- Mobile device management policies

**Completed Prerequisites:**

- ISMS-IMP-A.8.23.1 (Infrastructure Assessment) should be complete
- You should know which filtering solutions you have deployed
- Network architecture should be reasonably stable (not mid-migration)

**People to Consult:**

- Network Team (topology, VLANs, routing)
- Infrastructure Team (datacenter, cloud architecture)
- WiFi/Wireless Team (WLAN configurations)
- Remote Access Team (VPN, zero-trust)
- Site Managers (branch office networks)
- Cloud Architects (cloud networking)
- Security Operations (monitoring, verification testing)

**Time Allocation:**

- Network segment inventory: 2-4 hours
- Coverage mapping: 2-3 hours
- Gap identification: 1-2 hours
- Verification testing: 2-4 hours
- Documentation and evidence: 1-2 hours

---

## Assessment Workflow

Follow this systematic approach to complete the assessment:

**Step 1: Initial Setup (30 minutes)**

1. Open the workbook: `ISMS-IMP-A.8.23.2_Network_Coverage_[YYYYMMDD].xlsx`
2. Read the "Instructions & Legend" sheet completely
3. Fill in yellow highlighted fields in Document Information section
4. Gather network diagrams and topology documentation
5. Have Assessment 1 (Infrastructure) results available for reference

**Step 2: Network Segment Inventory (2-4 hours)**

This is the CRITICAL foundation - if you miss segments here, you'll miss coverage gaps.

1. Go to "Network_Segment_Inventory" sheet
2. Walk through your network systematically:

   - **Physical locations:** List every office, datacenter, branch
   - **For each location:** What LANs exist? What VLANs?
   - **Wireless:** Corporate WiFi, guest WiFi (separate segment IDs)
   - **Remote access:** VPN pools, direct cloud access
   - **Cloud infrastructure:** VDI, DaaS, virtual desktops
   - **Special segments:** DMZ, dev/test, IoT/OT, partner access
   - **Mobile devices:** Laptops/phones when NOT on VPN
3. For EACH segment, document:

   - Segment Name (descriptive, e.g., "HQ Corp LAN", "Branch 01 WiFi")
   - Segment Type (use dropdown - helps categorize)
   - Location/Site (physical or logical)
   - Subnet/VLAN (network addressing)
   - User count (approximate)
   - Device count (approximate)
   - Internet access? (Yes/No/Restricted)
   - Filtering required? (Yes/No/N/A)
   - Filtering status (✅/⚠️/❌/🔄/🚫)
   - Which filtering solution(s) protect it
   - Coverage percentage (0-100%)
4. Don't skip segments because "only 3 users" - document EVERYTHING
5. For complex segments, use Segment Detail Template (rows 60+) for analysis

### Common segments people forget

- Management/OOB networks (IPMI, iLO, out-of-band)
- Building systems (HVAC, security cameras, badge readers)
- Printer/scanner VLANs
- Voice/VoIP VLANs (if they have internet access)
- Development/staging environments
- Disaster recovery sites
- Partner extranets
- Legacy systems on isolated VLANs

**Step 3: Coverage Matrix Mapping (2-3 hours)**

1. Go to "Coverage_Matrix" sheet
2. List all filtering solutions across top (columns) - these come from Assessment 1
3. List all network segments down left side (rows) - these come from your inventory
4. For each intersection (segment + solution):

   - If this solution protects this segment: Enter coverage percentage
   - If not: Leave blank or mark with "—"
5. Calculate total coverage per segment (sum across solutions)
6. Set status based on total coverage:

   - 100%: ✅ Protected
   - 75-99%: ⚠️ Partial
   - 1-74%: ⚠️ Partial (concerning)
   - 0%: ❌ Unprotected (critical!)
   - Exempt: 🚫 (must have exemption record)
7. Let formulas calculate summary metrics

**Example Coverage Matrix:**

 | Segment | Perimeter Filter | Cloud Filter | Endpoint Agent | Total | Status | 
 | --------- | ----------------- | -------------- | ---------------- | ------- | -------- | 
 | Corp LAN | 100% | - | - | 100% | ✅ | 
 | Guest WiFi | 100% | - | - | 100% | ✅ | 
 | VPN Users | 40% | 60% | - | 100% | ⚠️ Multiple | 
 | Branch 01 | - | 100% | - | 100% | ✅ | 
 | Mobile (no VPN) | - | - | 80% | 80% | ⚠️ Partial | 

**Step 4: Gap Identification (1-2 hours)**

1. Go to "Gap_Identification" sheet
2. For EVERY segment with:

   - <100% coverage (unless approved exemption)
   - 0% coverage (critical priority!)
   - Partial coverage (<100%)
3. Document the gap:

   - Which segment is affected
   - What % is uncovered
   - Why (technical limitation, deployment gap, design decision)
   - Risk level (Critical/High/Medium/Low)
   - Remediation plan
   - Owner and target date
4. Prioritize:

   - 0% coverage on production segments = CRITICAL
   - <100% on high-risk segments = HIGH
   - Partial coverage on low-risk segments = MEDIUM

**Step 5: Device Inventory (Optional, 1-2 hours)**

If you have specific devices/endpoints that require tracking:

1. Go to "Device_Inventory" sheet
2. Document devices by category:

   - Corporate laptops
   - Corporate desktops
   - Mobile devices (phones/tablets)
   - Virtual desktops
3. For each device/category:

   - Count
   - Filtering method (network-based vs. agent-based)
   - Coverage status
   - Any unprotected devices

**Step 6: Exemption Register (30 minutes - 1 hour)**

For any segments marked "🚫 Exempt":

1. Go to "Exemption_Register" sheet
2. Document EVERY exemption:

   - Exemption ID (EXE-001, EXE-002, etc.)
   - Which segment(s) are exempt
   - Exemption type (Full/Partial/Temporary/Category/Technical)
   - Business justification (why is exemption needed?)
   - Compensating controls (what mitigates the risk?)
   - Approved by (name + date)
   - Expiration date (if temporary)
   - Status (Active/Expired/Revoked)
3. Link exemption ID back to segment inventory (column N)
4. Ensure all exemptions have proper approval evidence

### Common exemptions

- Medical devices with FDA restrictions
- Industrial control systems (ICS/SCADA)
- Legacy systems incompatible with filtering
- Development environments (with compensating controls)
- Partner-managed infrastructure
- Temporary migration/testing situations

**Step 7: Coverage Verification Testing (2-4 hours)**

Verify that filtering actually works on each segment:

1. Go to "Coverage_Verification" sheet
2. For each network segment (prioritize production/high-risk):

   - Plan test from that segment
   - Execute test (manual browse, automated scan, curl/wget)
   - Test known malicious URL (use test sites, not real malware!)
   - Test known blocked category (if using category filtering)
   - Verify HTTPS inspection (if enabled)
   - Document results
3. Common test methods:

   - **Manual browse test:** Access test sites from segment
   - **Automated scan:** Run Nmap/Nessus with HTTP probes
   - **Curl/wget test:** Command-line URL tests
   - **Browser extension:** Use filtering checker tools
   - **Vendor tool:** Use filtering solution's test function
4. Test results:

   - Pass: Filtering working as expected
   - Fail: Filtering not working (gap!)
   - Partial: Filtering working but incomplete
   - Inconclusive: Test couldn't determine
5. For failures: Create gap entry, investigate immediately

**Safe test sites for filtering verification:**

- EICAR test file (anti-malware test)
- Filtering vendor's own test pages
- testmyids.com (security product testing)
- \*DO NOT\* test with actual malware URLs

**Step 8: Evidence Collection (1-2 hours)**

1. Go to "Evidence_Register" sheet
2. Collect evidence for ALL claims:

   - Network topology diagrams
   - VLAN configurations
   - Firewall policies showing filtering enforcement
   - DHCP/DNS configs (proxy settings, DNS redirection)
   - VPN concentrator configs
   - WiFi controller configs
   - Cloud service dashboards
   - NAC policies
   - Exemption approval emails/tickets
   - Test results (screenshots, logs)
3. For each piece of evidence:

   - Assign Evidence ID (EVD-001, etc.)
   - Describe what it proves
   - Note where it's stored
   - Mark verification status

**Step 9: Quality Check (30 minutes)**

Before submitting for review, verify:

- [ ] All network segments documented (no missed segments)
- [ ] Coverage percentages add up correctly
- [ ] All segments with <100% coverage have gap entries
- [ ] All exemptions have proper approval and justification
- [ ] Verification testing completed for critical segments
- [ ] Evidence collected and referenced
- [ ] Formulas calculating correctly
- [ ] No segments marked "Unprotected" without gap/exemption entry

**Step 10: Review & Approval (1-2 weeks)**

1. Go to "Approval_Sign_Off" sheet
2. Complete "Assessment Completed By" section
3. Submit to Network Team Lead for technical review
4. Submit to Information Security Officer for compliance review
5. Address any review comments
6. Obtain CISO approval
7. Set next review date (typically +3 months)

---

## Question-by-Question Guidance

This section provides detailed guidance for completing each field in the assessment workbook.

### Network_Segment_Inventory Sheet

**Q: Segment ID**

- **Auto-generated:** SEG-001, SEG-002, SEG-003, etc.
- **Purpose:** Unique identifier for cross-referencing
- **Usage:** Reference this ID in Coverage Matrix, Gap Analysis, Exemption Register

**Q: Segment Name**

- **What to enter:** Descriptive name for this network segment
- **Examples:**
  - "Corporate HQ LAN - Floor 3"
  - "Guest WiFi - Building A"
  - "VPN - Remote Workers"
  - "Branch Office 01 - Chicago"
  - "DMZ - Public Web Servers"
  - "Dev Environment - Staging"
- **Guidelines:**
  - Be specific enough to distinguish from other segments
  - Include location if helpful
  - Use consistent naming scheme
  - Avoid cryptic abbreviations
- **Common mistakes:** Vague names like "LAN", "WiFi" (which LAN? which WiFi?)

**Q: Segment Type**

- **Dropdown options:** On-Premises LAN, WLAN, VPN, Cloud Endpoints, Guest, DMZ, Branch, Mobile, IoT/OT, Dev/Test, Other
- **How to choose:**
  - **On-Premises LAN:** Wired corporate network
  - **WLAN:** Any WiFi network (corporate, guest, separate entries)
  - **VPN:** Remote access via VPN
  - **Cloud Endpoints:** Virtual desktops, DaaS, Windows 365
  - **Guest:** Visitor/partner networks
  - **DMZ:** Demilitarized zone, public-facing
  - **Branch:** Remote office networks
  - **Mobile:** Devices NOT on VPN (direct internet)
  - **IoT/OT:** Internet of Things, Operational Technology
  - **Dev/Test:** Development, staging, lab environments
  - **Other:** Specialized segments not fitting above
- **Note:** Same physical network with different purposes = separate segments
  - Example: "Guest WiFi" (segment 1) vs. "Corp WiFi" (segment 2) even if same access points

**Q: Location/Site**

- **What to enter:** Physical or logical location
- **Examples:**
  - "Headquarters - Zurich"
  - "Branch Office - Geneva"
  - "Datacenter - Primary"
  - "AWS us-east-1"
  - "Azure West Europe"
  - "Remote (distributed)"
- **Why it matters:** Geographic distribution affects filtering architecture
- **For cloud:** Specify cloud region, not just "cloud"
- **For remote:** "Remote (distributed)" or "Home offices"

**Q: Subnet/VLAN**

- **What to enter:** Network address or VLAN ID
- **Examples:**
  - "192.168.10.0/24"
  - "10.50.0.0/16"
  - "VLAN 100"
  - "VLAN 250 (172.16.50.0/24)"
  - "100.64.0.0/10 (VPN pool)"
  - "N/A (cloud DHCP)"
- **Where to find:** Network diagrams, VLAN config, DHCP scope config
- **For VPN:** Document VPN IP pool
- **For cloud:** May be dynamic ("Azure vNet 10.0.0.0/16") or N/A
- **Why it matters:** Proves this is a distinct segment

**Q: User Count**

- **What to enter:** Approximate number of users who access this segment
- **Format:** Number (e.g., 150)
- **Rounding:** OK to round to nearest 10 or 50
- **Where to find:** 
  - AD group membership (if segment is user-based)
  - DHCP lease count (approximate)
  - WiFi controller concurrent user stats
  - Employee directory + location mapping
- **For guest networks:** Peak concurrent users
- **For VPN:** Licensed VPN user count
- **If unknown:** Best estimate (mark as "~150" in notes)

**Q: Device Count**

- **What to enter:** Approximate number of devices on this segment
- **Format:** Number
- **May be higher than user count:** Multiple devices per user (laptop + phone)
- **Where to find:**
  - DHCP lease count
  - NAC device inventory
  - Asset management system
  - WiFi controller associated devices
- **Include:** All devices, not just workstations (IoT, printers, etc.)

**Q: Internet Access?**

- **Dropdown options:** Yes, No, Restricted
- **Choose "Yes":** Segment has direct internet access
- **Choose "No":** Segment has NO internet access (isolated)
- **Choose "Restricted":** Limited internet access (specific destinations only)
- **Why it matters:** If No = filtering not needed; if Yes/Restricted = filtering required
- **Cross-check:** "No" internet access means "Filtering Required?" should be "N/A"

**Q: Filtering Required?**

- **Dropdown options:** Yes, No, N/A
- **Choose "Yes":** This segment requires web filtering per policy
- **Choose "No":** Segment exempt from filtering requirement (needs exemption record)
- **Choose "N/A":** Segment has no internet access (nothing to filter)
- **Policy reference:** ISMS-POL-A.8.23, Section 2.1 (Threat Protection Requirements) Section 2.1.1
- **If "No":** Must have corresponding exemption entry with approval

**Q: Filtering Status**

- **Dropdown options:** ✅ Protected, ⚠️ Partial, ❌ Unprotected, 🔄 Planned, 🚫 Exempt
- **Choose "✅ Protected":** 100% coverage, filtering operational
- **Choose "⚠️ Partial":** Some coverage but <100%
- **Choose "❌ Unprotected":** 0% coverage (critical!)
- **Choose "🔄 Planned":** Not protected yet, deployment planned
- **Choose "🚫 Exempt":** Approved exemption from filtering
- **Cross-check:** Must match Coverage % field
  - 100% = ✅
  - 1-99% = ⚠️
  - 0% = ❌ or 🚫
- **Audit flag:** ❌ Unprotected requires immediate explanation or remediation plan

**Q: Filtering Solution(s)**

- **What to enter:** Which solution(s) from Assessment 1 protect this segment
- **Examples:**
  - "Perimeter Firewall Filter"
  - "Zscaler Cloud Filter"
  - "Endpoint Agent + Perimeter Backup"
  - "Multiple (see Coverage Matrix)"
- **Where to find:** Network diagrams, solution documentation from Assessment 1
- **If multiple solutions:** List primary, or reference Coverage Matrix for detail
- **If none:** Enter "None (see gap GAP-XXX)" or "Exempt (EXE-XXX)"
- **Cross-check:** Solutions listed here must exist in Assessment 1

**Q: Coverage %**

- **What to enter:** Percentage of this segment protected by filtering
- **Format:** Number 0-100
- **How to calculate:**
  - 100%: All users/devices on this segment are filtered
  - 50%: Half protected, half unprotected
  - 0%: No filtering at all
- **Examples:**
  - VPN pool with 500 licensed users, 500 connected: 100%
  - Branch with 50 users, 40 protected via cloud filter, 10 unfiltered: 80%
  - Guest WiFi with 100% traffic routed through filter: 100%
- **Where to verify:** Coverage Matrix (sum of solution coverages)
- **Common errors:**
  - Assuming 100% when not verified (test it!)
  - Not accounting for bypass methods
  - Forgetting mobile devices when off-network

**Q: Bypass Methods**

- **What to enter:** Any known ways users/devices can bypass filtering
- **Examples:**
  - "VPN to external provider"
  - "Mobile hotspot tethering"
  - "Proxy servers (Tor, web proxies)"
  - "SSH tunneling"
  - "Direct 4G/5G internet"
  - "None known"
- **Why it matters:** Known bypass = reduced effective coverage
- **If bypasses exist:** 
  - Adjust coverage % accordingly
  - Document as gap if unacceptable
  - Implement compensating controls
- **Policy:** Some bypasses acceptable with controls, others not

**Q: Exemption ID**

- **What to enter:** Reference to Exemption_Register entry
- **Format:** EXE-001, EXE-002, etc. (or blank if not exempt)
- **When to use:** Only when segment status is "🚫 Exempt"
- **Cross-check:** Exemption ID must exist in Exemption_Register sheet
- **If exempt without ID:** Missing approval - must obtain or remediate

**Q: Evidence**

- **What to enter:** Where evidence is located proving this segment's filtering status
- **Examples:**
  - "EVD-015 (network diagram)"
  - "EVD-022 (VLAN config)"
  - "EVD-033 (firewall policy)"
  - "EVD-041 (test results from SEG-010)"
- **Reference:** Evidence IDs from Evidence_Register sheet
- **Multiple pieces OK:** "EVD-015, EVD-022, EVD-033"

### Segment Detail Template (Rows 60+)

For complex or critical segments, provide detailed analysis:

**Traffic Flow Section:**

- **Inbound:** Where does traffic come FROM to reach this segment?
  - Example: "From internet via perimeter firewall, filtered by Fortigate"
- **Outbound:** Where does traffic GO from this segment?
  - Example: "To internet via default gateway 192.168.10.1, filtered at gateway"
- **Lateral:** Does traffic move to other segments?
  - Example: "Yes, can reach Corp LAN via routing (filtered), cannot reach DMZ (blocked)"

**Filtering Implementation Section:**

- **Enforcement Point:** WHERE in the traffic flow is filtering applied?
  - Examples: "At perimeter firewall", "On endpoint (agent)", "Cloud redirect via DNS"
- **Technology:** Which solution?
  - Reference solution from Assessment 1
- **Policy Applied:** Which filtering policy rules?
  - Example: "Standard Corporate Policy (blocks malware + adult content)"
- **HTTPS Inspection:** Is encrypted traffic inspected?
  - Yes/No/Partial (affects threat detection capability)

**User Profile Section:**

- **User Types:** Who uses this segment?
  - Employees, Contractors, Guests, Partners, External, Mix
- **Risk Level:** How critical is protecting this segment?
  - High (exec, finance, sensitive data), Medium (general staff), Low (guest, test)
- **Acceptable Use:** Do users follow acceptable use policy?
  - Generally yes, Some violations, Frequent violations, Exempt from AUP

**Technical Details Section:**

- **Default Gateway:** IP address of gateway (where traffic exits)
- **DNS Servers:** IP addresses (important - DNS-based filtering uses this)
- **Proxy Settings:** How are proxies configured?
  - Automatic (PAC file/WPAD), Manual (explicit proxy), None
- **Authentication:** How are users authenticated?
  - Required (must auth), Optional (transparent), None (open access)

**Gaps/Issues Section:**

- **Coverage Gaps:** Describe any filtering gaps
  - Example: "HTTPS inspection not enabled - cannot inspect encrypted traffic"
- **Bypass Risks:** Known ways to bypass
  - Example: "Users can enable mobile hotspot, bypassing corporate filter"
- **Remediation Plan:** How will you close gaps?
  - Example: "Deploy endpoint agents to all laptops by Q2 2026"

### Coverage_Matrix Sheet

This sheet is mostly auto-populated from Network_Segment_Inventory, but you verify coverage percentages:

**For each cell (Segment + Solution intersection):**

- **If solution protects this segment:** Enter coverage % (1-100)
- **If solution does NOT protect:** Leave blank or "—"
- **If partial coverage:** Enter actual % (e.g., 60%)

**Total Coverage column:**

- Auto-calculates sum across solutions
- Should NOT exceed 100% (overlapping coverage is still 100% protection)
- Formula should use: =MIN(SUM(solutions), 100)

**Status column:**

- Auto-determines based on Total Coverage:
  - =100%: ✅ Protected
  - 1-99%: ⚠️ Partial
  - 0%: ❌ Unprotected OR 🚫 Exempt (check exemption register)

**Coverage Heatmap:**

- Review the summary distribution
- 100% coverage should be majority (>80% of segments)
- <100% coverage requires gap analysis
- 0% coverage without exemption = CRITICAL issue

### Gap_Identification Sheet

**Q: Gap ID**

- **Format:** GAP-001, GAP-002, etc.
- **Auto-generated** or manual entry
- **Purpose:** Track gaps across multiple assessments

**Q: Gap Description**

- **What to enter:** Clear, specific description of the coverage gap
- **Good examples:**
  - "SEG-010 (Branch 05 LAN) has 0% filtering coverage - no solution deployed"
  - "SEG-003 (VPN pool) has only 60% coverage - 200 users lack endpoint agents"
  - "SEG-015 (Guest WiFi) has partial HTTPS inspection (not enabled)"
- **Bad examples:**
  - "Some segments not covered" (too vague)
  - "Need more filtering" (not specific)

**Q: Affected Segment(s)**

- **What to enter:** Which segment(s) have this gap
- **Format:** Segment ID(s) from inventory
- **Examples:**
  - "SEG-010"
  - "SEG-003, SEG-004, SEG-005"
  - "All branch segments (SEG-020 through SEG-030)"

**Q: Current Coverage %**

- **What to enter:** Current coverage percentage
- **Pulls from:** Network_Segment_Inventory Coverage % field
- **Example:** "0%", "60%", "85%"

**Q: Target Coverage %**

- **What to enter:** Target coverage after remediation
- **Usually:** 100% (full coverage)
- **Sometimes:** <100% if partial exemption or compensating controls
- **Example:** "100%" or "95% (5% exempt per EXE-003)"

**Q: Risk Level**

- **Dropdown:** Critical / High / Medium / Low
- **Choose "Critical":**
  - 0% coverage on production segments with sensitive data
  - 0% coverage on segments with >100 users
  - Bypass methods allowing unfiltered internet access
- **Choose "High":**
  - <50% coverage on production segments
  - 0% coverage on smaller segments (<50 users)
  - Partial coverage with significant exposure
- **Choose "Medium":**
  - 50-90% coverage on production
  - 0% coverage on dev/test environments
- **Choose "Low":**
  - 90-99% coverage (minor gaps)
  - Coverage gaps on low-risk segments

**Q: Business Impact**

- **What to enter:** What's the impact if this gap is exploited?
- **Examples:**
  - "Users on SEG-010 exposed to malware, phishing, inappropriate content"
  - "Breach could compromise customer data (high-risk segment)"
  - "Limited impact - low-risk dev environment, no production data"
- **Consider:** Data sensitivity, user types, regulatory requirements

**Q: Root Cause**

- **What to enter:** WHY does this gap exist?
- **Examples:**
  - "Filtering solution not deployed to branch offices yet"
  - "Endpoint agents not installed on contractor laptops"
  - "HTTPS inspection disabled due to certificate issues"
  - "Legacy firewall lacks modern filtering features"
  - "Budget constraints delayed upgrade"
- **Be honest:** Root cause analysis drives effective remediation

**Q: Remediation Plan**

- **What to enter:** HOW will you close this gap?
- **Good examples:**
  - "Deploy cloud filtering service to all branches (project in progress)"
  - "Mandate endpoint agent installation, revoke network access for non-compliant devices"
  - "Upgrade perimeter firewall to model with HTTPS inspection, deploy Q2 2026"
  - "Implement DNS-based filtering as interim solution until full deployment"
- **Bad examples:**
  - "Fix it" (not a plan)
  - "Buy better firewall" (not specific enough)
- **Include:** Specific actions, technologies, timelines

**Q: Owner**

- **What to enter:** Who is responsible for remediation?
- **Format:** Name or role
- **Examples:**
  - "Network Team Lead"
  - "Jane Smith (Infrastructure)"
  - "Security Team + Branch Office Managers"
- **Must be:** Someone with authority and resources

**Q: Target Date**

- **What to enter:** When will gap be closed?
- **Format:** DD.MM.YYYY
- **Be realistic:** Based on resources, complexity, dependencies
- **Critical gaps:** <30 days
- **High gaps:** 30-90 days
- **Medium gaps:** 90-180 days
- **Low gaps:** >180 days (or "next budget cycle")

**Q: Status**

- **Dropdown:** Open / In Progress / Resolved / Accepted Risk / Exempt
- **Choose "Open":** Gap identified, remediation not started
- **Choose "In Progress":** Actively working on remediation
- **Choose "Resolved":** Gap closed, coverage achieved
- **Choose "Accepted Risk":** Management accepts risk, no remediation
- **Choose "Exempt":** Approved exemption, gap remains by design

**Q: Dependencies**

- **What to enter:** What must happen BEFORE this gap can be closed?
- **Examples:**
  - "Budget approval (pending Q2 budget cycle)"
  - "Network upgrade to support filtering appliance"
  - "Certificate infrastructure for HTTPS inspection"
  - "Vendor contract negotiation"
  - "None"
- **Why it matters:** Explains delays, manages expectations

### Device_Inventory Sheet

(Optional - use if tracking specific devices/endpoints)

**Q: Device ID**

- **Auto-generated:** DEV-001, DEV-002, etc.
- **Or use:** Asset tag, serial number, hostname

**Q: Device Type**

- **Dropdown:** Laptop, Desktop, Smartphone, Tablet, Virtual Desktop, Other
- **Categorize** by form factor/type

**Q: Owner/User**

- **What to enter:** Who uses this device
- **Format:** Name or department
- **For shared devices:** "Shared - Marketing" or "Kiosk - Lobby"

**Q: Location/Segment**

- **What to enter:** Which network segment does this device normally use?
- **Examples:**
  - "SEG-001 (Corp LAN) + SEG-003 (VPN when remote)"
  - "SEG-010 (Branch 05)"
  - "Mobile (various networks)"

**Q: Filtering Method**

- **Dropdown:** Yes (endpoint agent), No (network-based), Hybrid
- **Choose "Yes (endpoint agent)":** Device has filtering agent installed
- **Choose "No (network-based)":** Relies on network filtering only
- **Choose "Hybrid":** Both endpoint agent AND network filtering

**Q: Agent Installed?**

- **If filtering method = "Yes" or "Hybrid":** What agent?
- **Examples:**
  - "Zscaler App v3.2"
  - "Cisco AnyConnect + Umbrella Roaming Client"
  - "N/A (network-based only)"

**Q: Coverage Status**

- **What to enter:** Is this device adequately protected?
- **Examples:**
  - "✅ Protected (agent installed + network filter)"
  - "⚠️ Partial (network filter only, no agent)"
  - "❌ Unprotected (no agent, no network filter)"

**Q: Last Verified**

- **What to enter:** When was filtering last verified on this device?
- **Format:** DD.MM.YYYY
- **How to verify:** User accessed known blocked site, verified block

### Exemption_Register Sheet

**Q: Exemption ID**

- **Format:** EXE-001, EXE-002, etc.
- **Purpose:** Cross-reference to Network_Segment_Inventory

**Q: Segment(s) Affected**

- **What to enter:** Which segment(s) are exempt
- **Format:** Segment ID(s)
- **Examples:**
  - "SEG-025"
  - "SEG-030, SEG-031, SEG-032"

**Q: Exemption Type**

- **Dropdown:** Full Exemption, Partial Exemption, Temporary Exemption, Category Exemption, Technical Exemption
- **Choose "Full Exemption":** No filtering at all on this segment
- **Choose "Partial Exemption":** Some filtering capabilities exempt
- **Choose "Temporary Exemption":** Time-limited exemption
- **Choose "Category Exemption":** Exempt from category filtering only (threat protection still required)
- **Choose "Technical Exemption":** Technical limitation prevents filtering

**Q: Business Justification**

- **What to enter:** WHY is exemption needed?
- **Good examples:**
  - "Medical device segment - FDA validation prohibits network modifications"
  - "ICS/SCADA network - filtering incompatible with real-time control protocols"
  - "Legacy financial system - uses proprietary protocols incompatible with modern filtering"
  - "Temporary exemption - system migration in progress, filtering to be deployed after cutover"
- **Bad examples:**
  - "Don't want to" (not a justification)
  - "Too expensive" (needs risk acceptance, not exemption)

**Q: Compensating Controls**

- **What to enter:** What OTHER controls mitigate risk?
- **Examples:**
  - "Network isolated from internet (no direct internet access)"
  - "Application-layer security (all access via secure gateway)"
  - "Strict NAC policy (only authorized devices can connect)"
  - "Intensive monitoring and alerting (SOC reviews all traffic)"
  - "Time-limited exemption (30 days only)"
- **REQUIRED:** Exemptions without compensating controls = unacceptable risk

**Q: Requested By**

- **What to enter:** Who requested the exemption
- **Format:** Name + date
- **Example:** "Dr. John Smith (Medical Device Manager), 15.01.2026"

**Q: Approved By**

- **What to enter:** Who approved the exemption
- **Format:** Name + date
- **Authority level:** Must be appropriate for risk (typically CISO or C-level)
- **Example:** "Jane Doe (CISO), 20.01.2026"
- **Evidence:** Must have approval email/ticket (link in Evidence column)

**Q: Approval Date**

- **What to enter:** Date exemption was approved
- **Format:** DD.MM.YYYY

**Q: Expiration Date**

- **What to enter:** When does exemption expire?
- **Format:** DD.MM.YYYY
- **For permanent:** "N/A (permanent pending review)" or far-future date
- **For temporary:** Specific date
- **Review:** Exempt segments should be reviewed annually minimum

**Q: Status**

- **Dropdown:** Active / Expired / Revoked / Under Review
- **Choose "Active":** Exemption currently in effect
- **Choose "Expired":** Exemption period ended (must renew or remediate)
- **Choose "Revoked":** Exemption cancelled before expiry
- **Choose "Under Review":** Being re-evaluated

**Q: Evidence Location**

- **What to enter:** Where is approval documented?
- **Format:** Evidence ID(s)
- **Examples:**
  - "EVD-055 (CISO approval email)"
  - "EVD-056 (risk acceptance form)"
  - "EVD-057 (medical device validation report)"

### Coverage_Verification Sheet

**Q: Test ID**

- **Format:** TEST-001, TEST-002, etc.
- **Purpose:** Track individual verification tests

**Q: Segment Tested**

- **What to enter:** Which segment was tested
- **Format:** Segment ID
- **Example:** "SEG-010"

**Q: Test Date**

- **What to enter:** When test was performed
- **Format:** DD.MM.YYYY

**Q: Test Method**

- **Dropdown:** Manual Browse Test, Automated Scan, Curl/wget Test, Browser Extension, Vendor Tool, Penetration Test, Other
- **Choose "Manual Browse Test":** Human accessed test sites from segment
- **Choose "Automated Scan":** Script/tool tested multiple URLs
- **Choose "Curl/wget Test":** Command-line HTTP test
- **Choose "Browser Extension":** Used filtering verification extension
- **Choose "Vendor Tool":** Filtering vendor's test function
- **Choose "Penetration Test":** Part of formal pentest
- **Choose "Other":** Describe in notes

**Q: Test Target**

- **What to enter:** What was tested?
- **Examples:**
  - "EICAR test file (malware block)"
  - "Known phishing site (phishing block)"
  - "Adult content category (category block)"
  - "HTTPS inspection (decrypt + re-encrypt)"
  - "Bypass attempt (VPN to external service)"

**Q: Expected Result**

- **What to enter:** What SHOULD happen?
- **Examples:**
  - "Block page displayed"
  - "Connection refused"
  - "Download blocked with alert"
  - "HTTPS inspection certificate presented"

**Q: Actual Result**

- **What to enter:** What ACTUALLY happened?
- **Examples:**
  - "Block page displayed (as expected)"
  - "Site accessible (FAILED - should be blocked)"
  - "Partial block (HTTP blocked, HTTPS allowed)"

**Q: Test Result**

- **Dropdown:** Pass / Fail / Partial / Inconclusive
- **Choose "Pass":** Filtering working as expected
- **Choose "Fail":** Filtering NOT working (critical!)
- **Choose "Partial":** Filtering partially working
- **Choose "Inconclusive":** Test couldn't determine (retest needed)

**Q: Verification Status**

- **Dropdown:** ✅ Verified / ❌ Failed / ⚠️ Needs Retest
- **Overall status for this segment**

**Q: Tester Name**

- **What to enter:** Who performed the test
- **Format:** Name or role
- **Example:** "Security Analyst - John Smith"

**Q: Notes**

- **What to enter:** Any additional observations
- **Examples:**
  - "Test performed from wireless subnet 10.50.0.0/24"
  - "HTTPS inspection working but certificate warning appeared"
  - "Bypass via mobile hotspot confirmed (gap GAP-015)"

**Q: Evidence**

- **What to enter:** Screenshot/log proving test results
- **Format:** Evidence ID(s)
- **Examples:**
  - "EVD-080 (screenshot of block page)"
  - "EVD-081 (curl output showing connection refused)"

### Evidence_Register Sheet

**Q: Evidence ID**

- **Format:** EVD-001, EVD-002, etc.
- **Sequential numbering**

**Q: Evidence Type**

- **Dropdown:** Network Diagram, VLAN Config, Firewall Policy, VPN Config, WiFi Config, Cloud Dashboard, NAC Policy, Exemption Approval, Test Results, Monitoring Report, Change Record, Other
- **Choose appropriate type** for categorization

**Q: Description**

- **What to enter:** What does this evidence prove?
- **Examples:**
  - "Network topology diagram showing all VLANs and filtering enforcement points"
  - "VLAN 100 configuration showing default gateway routing through filtering appliance"
  - "Screenshot of SEG-010 test showing successful block of malware test site"
  - "CISO email approval of exemption EXE-003 for medical device network"

**Q: Related Sheet/Row**

- **What to enter:** Where in the assessment is this evidence used?
- **Format:** Sheet name + row/cell
- **Examples:**
  - "Network_Segment_Inventory - SEG-010"
  - "Exemption_Register - EXE-003"
  - "Coverage_Verification - TEST-025"

**Q: Location/Path**

- **What to enter:** Where is the evidence file stored?
- **Examples:**
  - "Evidence/A.8.23.2/Network_Diagrams/HQ_Topology_2026.pdf"
  - "SharePoint > ISMS > Evidence > A.8.23.2 > Configs > VLAN_Config_Export_20260115.txt"
  - "Confluence > Security > Web Filtering > Test Results"
  - "Email > CISO > Exemption Approvals > Medical_Device_Approval_20260110.msg"

**Q: Date Collected**

- **What to enter:** When was this evidence collected?
- **Format:** DD.MM.YYYY
- **Why it matters:** Evidence age affects validity

**Q: Collected By**

- **What to enter:** Who collected this evidence?
- **Format:** Name
- **Example:** "John Smith (Network Team)"

**Q: Verification Status**

- **Dropdown:** Verified / Pending / Not Verified
- **Choose "Verified":** Evidence reviewed and confirmed valid
- **Choose "Pending":** Evidence collected, not yet reviewed
- **Choose "Not Verified":** Evidence needs verification

---

## Evidence Collection

### What Constitutes Acceptable Evidence

Auditors need to verify your network coverage claims. Acceptable evidence includes:

**Network Architecture Evidence:**

- Complete network topology diagrams (Layer 2, Layer 3)
- VLAN configuration files
- Subnet allocation documentation
- IP address management (IPAM) exports
- Network segmentation diagrams

**Filtering Enforcement Evidence:**

- Firewall policies showing filtering rules
- Routing configurations (default gateways)
- DHCP configurations (DNS servers, proxy PAC files)
- DNS server configurations (filtering redirects)
- Proxy auto-config (PAC) files
- VPN split-tunnel configurations

**VPN Configuration Evidence:**

- VPN concentrator configurations
- VPN IP pool assignments
- VPN routing tables
- Client VPN profiles

**WiFi Configuration Evidence:**

- WiFi controller configurations
- SSID settings and client isolation
- Captive portal configurations
- RADIUS/authentication integration

**Cloud Architecture Evidence:**

- Cloud network diagrams (VNets, VPCs, subnets)
- Cloud routing tables
- Cloud firewall/NSG rules
- VDI/DaaS filtering configurations

**NAC Evidence:**

- Network Access Control policies
- Device posture requirements
- Endpoint compliance rules

**Exemption Evidence:**

- Exemption request forms
- Approval emails/tickets
- Risk acceptance documentation
- Compensating control documentation

**Verification Evidence:**

- Test results (screenshots, logs)
- Penetration test reports
- Monitoring reports showing filtering activity
- Block logs from each segment

### How to Organize Evidence

1. Create folder structure: `Evidence/A.8.23.2_Network_Coverage/`
2. Subfolders:

   - `Network_Diagrams/`
   - `VLAN_Configs/`
   - `Firewall_Policies/`
   - `VPN_Configs/`
   - `WiFi_Configs/`
   - `Cloud_Architecture/`
   - `Exemption_Approvals/`
   - `Test_Results/`
3. Use consistent naming: `EVD-001_HQ_Network_Topology.pdf`
4. Sanitize: Remove passwords, sensitive internal IPs if necessary
5. Version control: Include date in filename
6. Cross-reference: Link Evidence IDs to assessment claims

---

## Common Pitfalls

**Pitfall 1: Incomplete Segment Inventory**

- **Problem:** Missing network segments, especially edge cases
- **Common missed segments:**
  - Management/OOB networks
  - Building systems (HVAC, cameras)
  - Printer VLANs
  - VoIP VLANs (if internet-connected)
  - DR/backup sites
  - Legacy systems
  - Partner extranets
- **Solution:** Walk through network systematically with network team, review network diagrams, check VLAN lists
- **Consequence:** Coverage gaps go undetected, audit finding

**Pitfall 2: Assuming 100% Coverage Without Verification**

- **Problem:** Marking segments "Protected" without actual testing
- **Solution:** Perform verification tests from each segment
- **Common surprise:** "We thought it was filtered but VPN split-tunnel bypasses it"
- **Consequence:** False sense of security, actual gaps undetected

**Pitfall 3: Not Accounting for Mobile Devices**

- **Problem:** Assuming laptops/phones are always on VPN or corporate network
- **Reality:** Mobile devices connect from anywhere (home WiFi, coffee shops, hotels, mobile hotspot)
- **Solution:** 
  - Document mobile segment separately
  - Deploy endpoint agents for always-on protection
  - Use cloud-based filtering that follows devices
- **Consequence:** Large portion of workforce unprotected

**Pitfall 4: Forgetting About Bypass Methods**

- **Problem:** Not considering how users can circumvent filtering
- **Common bypasses:**
  - Personal VPN services
  - Mobile hotspot tethering
  - SSH tunneling
  - Proxy services (Tor, web proxies)
  - Direct 4G/5G connections
- **Solution:** Document known bypasses, assess risk, implement compensating controls
- **Consequence:** Coverage percentage overstated

**Pitfall 5: Exemptions Without Proper Approval**

- **Problem:** Marking segments "Exempt" without formal risk acceptance
- **Solution:** Every exemption needs:
  - Business justification
  - Compensating controls
  - Formal approval (CISO or C-level)
  - Documentation in Exemption Register
- **Consequence:** Audit finding, unaccepted risk

**Pitfall 6: Confusing "Filtering Capable" with "Filtering Deployed"**

- **Problem:** Network infrastructure CAN support filtering but isn't configured
- **Example:** "Firewall has web filtering module but it's not enabled"
- **Solution:** Verify filtering is actually operational, not just possible
- **Consequence:** False confidence in coverage

**Pitfall 7: Not Coordinating with Infrastructure Assessment**

- **Problem:** Coverage assessment doesn't align with Infrastructure assessment
- **Solution:** Solutions listed here must match solutions from Assessment 1
- **Cross-check:** Every filtering solution in Coverage Matrix should exist in Assessment 1
- **Consequence:** Audit confusion, inconsistent documentation

**Pitfall 8: Ignoring Branch Offices**

- **Problem:** Focusing only on headquarters, forgetting branch locations
- **Reality:** Branch offices often have independent internet connections
- **Solution:** Document EVERY physical location
- **Consequence:** Large coverage gaps in branch networks

**Pitfall 9: Cloud Blind Spot**

- **Problem:** Not considering cloud-based resources
- **Cloud segments often missed:**
  - Virtual desktops (VDI, DaaS, Windows 365)
  - Cloud workloads with direct internet (not backhauled)
  - SaaS application access
- **Solution:** Review cloud architecture, consult cloud team
- **Consequence:** Cloud resources unprotected

**Pitfall 10: Stale Network Documentation**

- **Problem:** Using outdated network diagrams
- **Solution:** Verify current state, update diagrams if needed
- **Common issue:** "We decommissioned that VLAN 6 months ago" or "We added 5 new branches"
- **Consequence:** Assessment doesn't reflect reality

**Pitfall 11: Percentage Calculation Errors**

- **Problem:** Coverage % doesn't match reality
- **Common errors:**
  - Adding up overlapping coverage (60% + 60% = 120%? No, it's 100%)
  - Assuming 100% when partial deployment
  - Not accounting for mobile/remote workers
- **Solution:** Be precise, verify numbers, use formulas correctly
- **Consequence:** Overstated coverage, missed gaps

**Pitfall 12: No Verification Testing**

- **Problem:** Documenting coverage without testing
- **Solution:** Actually test from each segment
- **Reality check:** "Network diagram says filtered, but test shows bypass"
- **Consequence:** Paper compliance, not real protection

---

## Quality Checklist

Before submitting for review, verify all of the following:

**Completeness Check:**

- [ ] All network segments documented (walked through entire network)
- [ ] All physical locations included (HQ, branches, datacenters, remote)
- [ ] All VLAN/subnets accounted for
- [ ] VPN pools documented
- [ ] Cloud infrastructure included
- [ ] Mobile/remote devices addressed
- [ ] Guest networks documented
- [ ] Special-purpose networks included (DMZ, IoT, dev/test)

**Coverage Verification:**

- [ ] Coverage Matrix completed for all segments
- [ ] Coverage percentages calculated correctly
- [ ] Total coverage per segment ≤100%
- [ ] Segments with <100% coverage have gap entries
- [ ] Segments with 0% coverage have gap OR exemption entries
- [ ] Verification testing completed for critical segments
- [ ] Test results documented in Coverage_Verification sheet

**Gap Analysis:**

- [ ] Every gap identified and documented
- [ ] All gaps have risk levels assigned
- [ ] All gaps have remediation plans
- [ ] All gaps have owners and target dates
- [ ] Critical gaps prioritized (0% coverage on production)
- [ ] Dependencies noted for delayed remediations

**Exemption Management:**

- [ ] All exempt segments have Exemption Register entries
- [ ] All exemptions have business justification
- [ ] All exemptions have compensating controls
- [ ] All exemptions have proper approval evidence
- [ ] Temporary exemptions have expiration dates
- [ ] Exemption IDs cross-referenced correctly

**Evidence Check:**

- [ ] Evidence Register populated
- [ ] Evidence collected for all key claims
- [ ] Evidence file names match Evidence IDs
- [ ] Evidence organized in folder structure
- [ ] Sensitive information sanitized
- [ ] Evidence verification status marked

**Cross-Reference Check:**

- [ ] Filtering solutions match Assessment 1 (Infrastructure)
- [ ] Segment IDs used consistently across all sheets
- [ ] Evidence IDs referenced correctly
- [ ] Exemption IDs match Exemption Register
- [ ] Gap IDs unique and sequential

**Formula Validation:**

- [ ] Coverage percentages calculate correctly
- [ ] Total coverage formulas working
- [ ] Coverage heatmap formulas calculating
- [ ] Conditional formatting displays correctly
- [ ] No #REF! or #DIV/0! errors

**Final Review:**

- [ ] Spell-check completed
- [ ] Consistent terminology throughout
- [ ] Date format consistent (DD.MM.YYYY)
- [ ] File naming convention followed
- [ ] Assessment status set appropriately (Draft/Final)

---

## Review & Approval

**Step 1: Self-Review (You)**

Before submitting, review your own work:

1. Run through Quality Checklist above
2. Verify segment inventory is complete (didn't miss any segments)
3. Check coverage percentages make sense
4. Ensure critical gaps have remediation plans
5. Confirm exemptions have proper approvals

**Step 2: Network Team Review**

Submit to Network Team Lead for technical verification:

1. Verify network topology is accurately represented
2. Confirm VLAN/subnet assignments correct
3. Validate traffic flow descriptions
4. Check filtering enforcement points
5. Review bypass methods identified
6. Typical turnaround: 3-5 days

**Step 3: Technical Testing (Optional)**

If time permits, have Security Team perform independent verification testing:

1. Select sample of segments (prioritize high-risk)
2. Perform filtering tests
3. Confirm claimed coverage
4. Document any discrepancies
5. Update assessment based on findings

**Step 4: Information Security Officer Review**

Submit to ISO for official review:

1. Go to "Approval_Sign_Off" sheet
2. Complete "Assessment Completed By" section
3. Send workbook + evidence folder to ISO
4. ISO reviews for:

   - Policy compliance (all segments addressed)
   - Gap severity assessment (risk-appropriate)
   - Exemption justification (properly approved)
   - Evidence adequacy (audit-ready)
   - Remediation plan feasibility (resourced, scheduled)
5. ISO provides recommendation: Approve / Approve with Conditions / Reject / Require Rework
6. Typical turnaround: 3-5 business days

**Step 5: Address Review Comments**

If ISO requests changes:

1. Document all feedback received
2. Make requested corrections
3. Update version/date in document
4. Re-verify affected sections
5. Resubmit with change summary
6. Typical turnaround: 2-3 days for revisions

**Step 6: CISO Approval**

Final approval from CISO:

1. ISO forwards to CISO with recommendation
2. CISO reviews:

   - Overall coverage status (% protected)
   - Critical gaps and remediation plans
   - Exemption acceptability
   - Resource requirements for gap remediation
   - Risk acceptance for known gaps
3. CISO decision: Approved / Approved with Conditions / Rejected
4. "Approved with Conditions" = proceed but must close specific gaps by specific dates
5. Typical turnaround: 2-3 business days

**Step 7: Documentation & Communication**

Once approved:

1. Set assessment status to "Final"
2. Set next review date (typically +3 months)
3. File completed assessment in document management system
4. Notify gap owners of their remediation assignments
5. Update network diagrams if discrepancies found
6. Communicate exemptions to relevant teams
7. Create calendar reminders for:

   - Gap remediation target dates
   - Temporary exemption expiration dates
   - Next quarterly review date

### Approval Timeline Expectations

- Self-review: 2-3 hours
- Network team review: 3-5 days
- Testing verification: 2-4 days (if performed)
- ISO review: 3-5 business days
- Revisions (if needed): 2-3 days
- CISO approval: 2-3 business days
- **Total: 2-3 weeks from submission to final approval**

**If Assessment is Rejected:**

Common rejection reasons and solutions:

1. **Incomplete segment inventory:** Walk through network again with team, update inventory
2. **Coverage claims not verified:** Perform actual testing, document results
3. **Gaps lack remediation plans:** Develop specific plans with owners and dates
4. **Exemptions improperly justified:** Obtain proper approvals, document compensating controls
5. **Evidence inadequate:** Collect missing evidence, organize properly

---

**END OF PART I: USER COMPLETION GUIDE**

---

# PART II: TECHNICAL SPECIFICATION

## Workbook Structure

### Sheet 1: Instructions & Legend

#### Header Section
- **Title:** "ISMS-IMP-A.8.23.2 – Network Coverage Assessment"
- **Subtitle:** "ISO/IEC 27001:2022 - Control A.8.23: Web Filtering"
- **Styling:** Dark blue header (003366), white text, centered, 40px height

#### Document Information Block
```
Document ID:           ISMS-IMP-A.8.23.2
Assessment Area:       Network Coverage & Deployment Topology
Related Policy:        ISMS-POL-A.8.23, Section 2.1 (Threat Protection Requirements)
Version:               1.0
Assessment Date:       [USER INPUT - yellow cell]
Completed By:          [USER INPUT - yellow cell]
Organization:          [USER INPUT - yellow cell]
Review Cycle:          Quarterly
```

**Audience:** Workbook developers, Python script maintainers

**Note:** This section provides technical specifications for workbook generation and maintenance. Users completing the assessment should refer to Part I above.

---

## Workbook Structure

### Sheet 1: Instructions & Legend

#### Header Section
- **Title:** "ISMS-IMP-A.8.23.2 — Network Coverage Assessment"
- **Subtitle:** "ISO/IEC 27001:2022 - Control A.8.23: Web Filtering"
- **Styling:** Dark blue header (003366), white text, centered, 40px height

#### Document Information Block
```plaintext
Document ID:           ISMS-IMP-A.8.23.2
Assessment Area:       Network Coverage & Deployment Topology
Related Policy:        ISMS-POL-A.8.23, Section 2.1 (Threat Protection Requirements)
Version:               1.0
Assessment Date:       [USER INPUT - yellow cell]
Completed By:          [USER INPUT - yellow cell]
Organization:          [USER INPUT - yellow cell]
Review Cycle:          Quarterly
```

#### How to Use This Workbook
1. Complete Network_Segment_Inventory for EVERY network segment in your environment
2. Document YOUR specific network architecture (office LANs, WLANs, VPN, cloud, etc.)
3. Map filtering solutions to network segments in Coverage_Matrix
4. Calculate coverage percentages and identify gaps
5. Document any devices/segments exempt from filtering in Exemption_Register
6. Track evidence in Evidence_Register
7. Review and approve via Approval_Sign_Off
8. Update quarterly or after network topology changes
9. Coordinate with ISMS-IMP-A.8.23.1 (Infrastructure Assessment)

#### Status Legend
 | Symbol | Status | Description | Color Code | 
 | -------- | -------- | ------------- | ------------ | 
 | ✅ | Protected | Web filtering active and operational | Green (C6EFCE) | 
 | ⚠️ | Partial | Partial coverage or limited protection | Yellow (FFEB9C) | 
 | ❌ | Unprotected | No web filtering deployed | Red (FFC7CE) | 
 | 🔄 | Planned | Protection planned with target date | Blue (B4C7E7) | 
 | 🚫 | Exempt | Approved exemption (documented) | Gray (D9D9D9) | 

#### Network Segment Types (Examples)
Organizations map THEIR environment to these generic types:

- **On-Premises LANs** (corporate office networks)
- **Wireless Networks (WLAN)** (corporate WiFi, guest WiFi)
- **Remote Access / VPN** (remote workers, site-to-site VPN)
- **Cloud-Based Endpoints** (VDI, DaaS, Windows 365, virtual desktops)
- **Guest/Partner Networks** (visitor access, vendor access)
- **DMZ / Extranet** (public-facing services, partner connections)
- **Branch Offices** (remote sites, field offices)
- **Mobile Devices** (smartphones, tablets, laptops outside VPN)
- **IoT/OT Networks** (building systems, manufacturing, special-purpose)
- **Development/Test Networks** (staging environments, labs)

#### Acceptable Evidence (Examples)
- ✓ Network topology diagrams
- ✓ VLAN configurations and documentation
- ✓ Firewall/routing policies showing filtering enforcement
- ✓ DHCP configurations (DNS redirection, proxy settings)
- ✓ VPN concentrator configurations
- ✓ Cloud service dashboards (showing endpoint protection)
- ✓ WiFi controller configurations
- ✓ Network access control (NAC) policies
- ✓ Exemption request approvals (email, tickets)
- ✓ Coverage verification tests/reports
- ✓ Network monitoring dashboards
- ✓ Change management records for network modifications

---

## Sheet 2: Network_Segment_Inventory

### Purpose
Document EVERY network segment where users/devices can access the internet. This is the foundation for coverage analysis.

### Header Section
**Row 1:** "NETWORK SEGMENT INVENTORY"  
**Row 2:** "Document all network segments requiring web filtering protection"

### Column Structure (Rows 4+)

 | Column | Header | Width | Type | Validation | 
 | -------- | -------- | ------- | ------ | ------------ | 
 | A | Segment ID | 15 | Text | Auto-generated (SEG-001) | 
 | B | Segment Name | 30 | Text | Customer fills in | 
 | C | Segment Type | 25 | Dropdown | On-Premises LAN, WLAN, VPN, Cloud Endpoints, Guest, DMZ, Branch, Mobile, IoT/OT, Dev/Test, Other | 
 | D | Location/Site | 25 | Text | Physical or logical location | 
 | E | Subnet/VLAN | 20 | Text | Network address (e.g., 192.168.10.0/24, VLAN 100) | 
 | F | User Count | 12 | Number | Approximate users on this segment | 
 | G | Device Count | 12 | Number | Approximate devices | 
 | H | Internet Access? | 15 | Dropdown | Yes, No, Restricted | 
 | I | Filtering Required? | 15 | Dropdown | Yes, No, N/A | 
 | J | Filtering Status | 18 | Dropdown | ✅ Protected, ⚠️ Partial, ❌ Unprotected, 🔄 Planned, 🚫 Exempt | 
 | K | Filtering Solution(s) | 30 | Text | Which solution(s) protect this segment? | 
 | L | Coverage % | 12 | Number | 0-100% | 
 | M | Bypass Methods | 25 | Text | Any known ways to bypass filtering? | 
 | N | Exemption ID | 15 | Text | If exempt, reference exemption | 
 | O | Evidence | 35 | Text | Evidence location | 

**Data Rows:** 50 rows for segment documentation

### Segment Details Template (Rows 60+)

For each critical segment, provide detailed analysis:

**Segment Detail Section (repeatable):**
```
SEGMENT: [Segment Name from inventory]
────────────────────────────────────────────────────────────

Traffic Flow:
  • Inbound:  [Describe]
  • Outbound: [Describe]
  • Lateral:  [Describe]

Filtering Implementation:
  • Enforcement Point:    [Where is filtering applied?]
  • Technology:           [Which solution?]
  • Policy Applied:       [Which filtering policy?]
  • HTTPS Inspection:     [Yes/No/Partial]

User Profile:
  • User Types:           [Employees/Guests/Contractors/etc.]
  • Risk Level:           [High/Medium/Low]
  • Acceptable Use:       [Compliance with AUP?]

Technical Details:
  • Default Gateway:      [IP address or N/A]
  • DNS Servers:          [IP addresses]
  • Proxy Settings:       [Automatic/Manual/None]
  • Authentication:       [Required/Optional/None]

Gaps/Issues:
  • Coverage Gaps:        [Describe any gaps]
  • Bypass Risks:         [Known bypass methods?]
  • Remediation Plan:     [If gaps exist]
```

---

## Sheet 3: Coverage_Matrix

### Purpose
Cross-reference network segments with filtering solutions to visualize coverage.

### Header
**Row 1:** "NETWORK COVERAGE MATRIX"  
**Row 2:** "Map filtering solutions to network segments"

### Matrix Structure (Rows 4+)

 | Network Segment | Solution 1 | Solution 2 | Solution 3 | Solution 4 | Total Coverage | Status | 
 | ----------------- | ----------- | ----------- | ----------- | ----------- | ---------------- | -------- | 
 | [SEG-001] Corp LAN | ✅ 100% | - | - | - | 100% | ✅ Protected | 
 | [SEG-002] Guest WiFi | - | ✅ 100% | - | - | 100% | ✅ Protected | 
 | [SEG-003] VPN | ⚠️ 60% | - | ⚠️ 40% | - | 100% | ⚠️ Multiple | 
 | ... |  |  |  |  |  |  | 

**Legend:**

- ✅ XX% = Protected by this solution (percentage coverage)
- ❌ = Not protected by this solution
- ⚠️ = Partial coverage
- 🚫 = Exempt from this solution

**Summary Row (auto-calculated):**

- Total segments assessed: [COUNT]
- Fully protected (100%): [COUNT]
- Partially protected (<100%): [COUNT]
- Unprotected (0%): [COUNT]
- Exempted: [COUNT]

### Coverage Heatmap Section

Visual representation of coverage quality:

 | Coverage Level | Segment Count | % of Total | Status | 
 | ---------------- | --------------- | ------------ | -------- | 
 | 100% Coverage | [Formula] | [Formula] | ✅ Good | 
 | 75-99% Coverage | [Formula] | [Formula] | ⚠️ Needs Attention | 
 | 50-74% Coverage | [Formula] | [Formula] | ⚠️ Risk | 
 | <50% Coverage | [Formula] | [Formula] | ❌ Critical | 
 | 0% Coverage | [Formula] | [Formula] | ❌ Urgent | 
 | Exempt | [Formula] | [Formula] | 🚫 Approved | 

**Overall Network Coverage Score:** [Formula calculating weighted average]

---

## Sheet 4: Gap_Identification

### Purpose
Document segments with insufficient filtering coverage and track remediation.

### Header
**Row 1:** "COVERAGE GAPS & REMEDIATION TRACKING"  
**Row 2:** "Identify unprotected/partially protected segments and plan remediation"

### Gap Register (Rows 4+)

 | Gap ID | Segment ID | Segment Name | Current Coverage | Gap Description | Risk Level | Impact | Remediation Plan | Owner | Target Date | Status | Budget | 
 | -------- | ----------- | -------------- | ------------------ | ----------------- | ------------ | -------- | ------------------ | ------- | ------------- | -------- | -------- | 
 | GAP-001 | [Auto-pull] | [Auto-pull] | XX% | [Describe gap] | Dropdown | Text | Text | Text | Date | Dropdown | Dropdown | 

**Columns:**

- **Gap ID:** Auto-generated (GAP-001, GAP-002, etc.)
- **Segment ID:** Reference to Network_Segment_Inventory
- **Current Coverage:** Percentage (0-100%)
- **Risk Level:** Critical / High / Medium / Low
- **Impact:** Business impact description
- **Remediation Plan:** How will gap be closed?
- **Status:** Open / In Progress / Resolved / Accepted Risk / Exempt

**Data Rows:** 30 rows for gap tracking

### Gap Summary Metrics

 | Risk Level | Gap Count | % of Total | Avg Time Open | 
 | ------------ | ----------- | ------------ | --------------- | 
 | Critical | [Formula] | [Formula] | [Formula] | 
 | High | [Formula] | [Formula] | [Formula] | 
 | Medium | [Formula] | [Formula] | [Formula] | 
 | Low | [Formula] | [Formula] | [Formula] | 

### Key Metrics

- Total gaps identified: [Formula]
- Gaps resolved: [Formula]
- Gaps remaining: [Formula]
- Average remediation time: [Formula] days
- Segments at risk: [Formula]

---

## Sheet 5: Device_Inventory

### Purpose
Track individual devices/endpoints and their filtering protection status (especially for BYOD, mobile, remote workers).

### Header
**Row 1:** "DEVICE-LEVEL FILTERING INVENTORY"  
**Row 2:** "Track endpoint protection for mobile/remote devices"

### Device Registry (Rows 4+)

 | Device ID | Device Type | OS | User/Owner | Primary Network | Filtering Solution | Agent-Based? | Status | Last Verified | Evidence | 
 | ----------- | ------------- | ---- | ----------- | ----------------- | -------------------- | -------------- | -------- | --------------- | ---------- | 
 | DEV-001 | Dropdown | Text | Text | Dropdown | Text | Dropdown | Dropdown | Date | Text | 

**Columns:**

- **Device ID:** Auto-generated
- **Device Type:** Laptop / Desktop / Smartphone / Tablet / Virtual Desktop / Other
- **OS:** Windows / macOS / Linux / iOS / Android / ChromeOS / Other
- **User/Owner:** Employee name or department
- **Primary Network:** Which segment is this device usually on?
- **Filtering Solution:** Which solution protects this device?
- **Agent-Based?:** Yes (endpoint agent) / No (network-based) / Hybrid
- **Status:** ✅ Protected / ⚠️ Partial / ❌ Unprotected / 🔄 Pending
- **Last Verified:** Date of last verification

**Data Rows:** 100 rows for device tracking

**Use Cases:**

- BYOD (Bring Your Own Device) programs
- Remote workers outside VPN
- Mobile devices (smartphones/tablets)
- Executive/VIP devices requiring special attention
- Contractor/temporary worker devices

### Device Summary

 | Device Type | Total | Protected | Unprotected | Coverage % | 
 | ------------- | ------- | ----------- | ------------- | ------------ | 
 | Laptops | [Formula] | [Formula] | [Formula] | [Formula] | 
 | Desktops | [Formula] | [Formula] | [Formula] | [Formula] | 
 | Smartphones | [Formula] | [Formula] | [Formula] | [Formula] | 
 | Tablets | [Formula] | [Formula] | [Formula] | [Formula] | 
 | Virtual Desktops | [Formula] | [Formula] | [Formula] | [Formula] | 
 | Other | [Formula] | [Formula] | [Formula] | [Formula] | 

---

## Sheet 6: Exemption_Register

### Purpose
Document approved exemptions from web filtering requirements with business justification.

### Header
**Row 1:** "FILTERING EXEMPTION REGISTER"  
**Row 2:** "Document approved exceptions to web filtering requirements"

### Exemption Registry (Rows 4+)

 | Exemption ID | Segment/Device | Exemption Type | Business Justification | Risk Assessment | Compensating Controls | Approved By | Approval Date | Review Date | Status | Evidence | 
 | -------------- | --------------- | ---------------- | ------------------------ | ----------------- | ---------------------- | ------------- | --------------- | ------------- | -------- | ---------- | 
 | EXM-001 | Text | Dropdown | Text | Text | Text | Text | Date | Date | Dropdown | Text | 

**Columns:**

- **Exemption ID:** Auto-generated (EXM-001)
- **Segment/Device:** What is exempt?
- **Exemption Type:** Dropdown:
  - Full Exemption (no filtering)
  - Partial Exemption (reduced filtering)
  - Temporary Exemption (time-limited)
  - Category Exemption (specific categories allowed)
  - Technical Exemption (incompatibility)
- **Business Justification:** Why is exemption necessary?
- **Risk Assessment:** What risks does this create?
- **Compensating Controls:** How is risk mitigated?
  - Enhanced monitoring
  - Network segmentation
  - Restricted access
  - Alternative controls
- **Approved By:** Name and role (must be CISO or delegate)
- **Approval Date:** When was exemption granted?
- **Review Date:** When must exemption be reviewed? (max 12 months)
- **Status:** Active / Expired / Revoked / Under Review
- **Evidence:** Link to approval documentation

**Data Rows:** 20 rows for exemption tracking

### Exemption Summary

 | Exemption Type | Active Count | Expired/Overdue | Avg Duration | 
 | ---------------- | -------------- | ----------------- | -------------- | 
 | Full Exemption | [Formula] | [Formula] | [Formula] | 
 | Partial Exemption | [Formula] | [Formula] | [Formula] | 
 | Temporary Exemption | [Formula] | [Formula] | [Formula] | 
 | Category Exemption | [Formula] | [Formula] | [Formula] | 
 | Technical Exemption | [Formula] | [Formula] | [Formula] | 

**Alert Conditions:**

- ⚠️ Exemptions >12 months old require re-approval
- ⚠️ Exemptions without compensating controls = HIGH RISK
- ⚠️ >10% of segments exempt = escalate to CISO

---

## Sheet 7: Coverage_Verification

### Purpose
Document testing/verification that filtering is actually working on each segment.

### Header
**Row 1:** "COVERAGE VERIFICATION LOG"  
**Row 2:** "Test and verify filtering effectiveness per network segment"

### Verification Log (Rows 4+)

 | Verification ID | Segment ID | Segment Name | Test Date | Tester | Test Method | Test Results | Issues Found | Status | Next Test Date | 
 | ----------------- | ----------- | -------------- | ----------- | -------- | ------------- | -------------- | -------------- | -------- | ---------------- | 
 | VER-001 | [Pull] | [Pull] | Date | Text | Dropdown | Text | Text | Dropdown | [Formula] | 

**Columns:**

- **Verification ID:** Auto-generated
- **Segment ID:** Reference to Network_Segment_Inventory
- **Test Date:** When was verification performed?
- **Tester:** Who performed the test?
- **Test Method:** Dropdown:
  - Manual Browse Test (attempt to access blocked sites)
  - Automated Scan (security tool)
  - Curl/wget Test (command-line)
  - Browser Extension Test
  - Vendor Verification Tool
  - Penetration Test
  - Other
- **Test Results:** Pass / Fail / Partial / Inconclusive
- **Issues Found:** Description of any problems
- **Status:** ✅ Verified / ❌ Failed / ⚠️ Needs Retest
- **Next Test Date:** [Auto-calculate: Test Date + 90 days]

**Data Rows:** 50 rows for verification tracking

### Test Checklist Template

For each segment, verify:
```
☐ Malicious URL blocked (test with EICAR or known bad domains)
☐ Phishing site blocked (test with PhishTank samples)
☐ Known malware download blocked
☐ HTTPS sites properly filtered (if HTTPS inspection enabled)
☐ Logging working (blocked attempts logged)
☐ Bypass methods ineffective (proxy bypass, VPN bypass, etc.)
☐ User experience acceptable (latency, false positives)
☐ Exemptions working as intended
```

---

## Sheet 8: Evidence_Register

### Purpose
Centralized evidence repository linking to all supporting documentation.

### Header
**Row 1:** "EVIDENCE REGISTER"  
**Row 2:** "Document all evidence supporting network coverage assessment"

### Evidence Inventory (Rows 4-103, 100 rows)

 | Evidence ID | Evidence Type | Description | Related Sheet/Row | Location/Path | Date Collected | Collected By | Verification Status | 
 | ------------- | --------------- | ------------- | ------------------- | --------------- | ---------------- | -------------- | ------------------- | 
 | EVD-001 | Dropdown | Text | Text | Text | Date | Text | Dropdown | 

**Evidence Types:**

- Network Diagram
- VLAN Configuration
- Firewall Policy
- VPN Configuration
- WiFi Controller Config
- Cloud Dashboard Screenshot
- NAC Policy
- Exemption Approval
- Test Results
- Monitoring Report
- Change Record
- Other

**Data Rows:** 100 rows

---

## Sheet 9: Approval_Sign_Off

### Purpose
Formal approval workflow for completed assessment.

### Assessment Summary (Rows 3-10)
```
Assessment Document:        ISMS-IMP-A.8.23.2 - Network Coverage
Assessment Period:          [USER INPUT]
Total Segments Assessed:    [Formula from Network_Segment_Inventory]
Fully Protected:            [Formula - 100% coverage segments]
Partially Protected:        [Formula - <100% coverage segments]
Unprotected:                [Formula - 0% coverage segments]
Exempted:                   [Formula from Exemption_Register]
Overall Coverage Score:     [Formula]%
Critical Gaps:              [Formula from Gap_Identification]
Assessment Status:          [Dropdown: Draft/Final/Requires Remediation/Re-assessment]
```

### Completed By (Rows 12-18)
- Name, Role, Department, Email, Date, Signature

### Reviewed By - Network Administrator (Rows 20-26)
- Name, Date, Review Notes, Recommendation

### Reviewed By - Information Security Officer (Rows 28-34)
- Name, Date, Review Notes, Recommendation

### Approved By - CISO (Rows 36-42)
- Name, Date, Approval Decision, Conditions/Notes

### Next Review Details (Rows 44-47)
- Next Review Date: [Auto-calculate +3 months]
- Review Responsible
- Special Considerations

---

## Cell Styling Reference

### Header Styles
- **Main Header:** Font: Calibri 14pt bold white, Fill: 003366 (dark blue)
- **Subheader:** Font: Calibri 11pt bold white, Fill: 4472C4 (blue)
- **Column Header:** Font: Calibri 10pt bold black, Fill: D9D9D9 (gray)

### Input Cell Styles
- **Fill:** FFFFCC (light yellow)
- **Alignment:** Left/center, wrapped
- **Border:** Thin black on all sides

### Status Fills
- **Protected (✅):** C6EFCE (green)
- **Partial (⚠️):** FFEB9C (yellow)
- **Unprotected (❌):** FFC7CE (red)
- **Planned (🔄):** B4C7E7 (blue)
- **Exempt (🚫):** D9D9D9 (gray)

---

## Freeze Panes

- **Network_Segment_Inventory:** Freeze at A5
- **Coverage_Matrix:** Freeze at A5
- **All other assessment sheets:** Freeze at A5
- **Evidence_Register:** Freeze at A5
- **Approval_Sign_Off:** Freeze at A3

---

## File Naming Convention

**Format:** `ISMS-IMP-A.8.23.2_Network_Coverage_YYYYMMDD.xlsx`

**Example:** `ISMS-IMP-A.8.23.2_Network_Coverage_20260101.xlsx`

---

## Quarterly Review Cycle

1. Review network segment inventory for changes (new VLANs, cloud services, etc.)
2. Re-verify filtering coverage on all segments
3. Update Coverage_Matrix with current status
4. Test filtering effectiveness (Coverage_Verification)
5. Review and renew exemptions (max 12 months)
6. Update gap remediation status
7. Re-calculate overall coverage score
8. Address any new critical gaps
9. Update approval sign-off
10. Coordinate with ISMS-IMP-A.8.23.1 (Infrastructure changes)

---

## Integration Points

### Related Documents
- ISMS-POL-A.8.23, Section 2.1 (Threat Protection Requirements): Threat Protection Requirements
- ISMS-IMP-A.8.23.1: Filtering Infrastructure Assessment (which solutions are deployed)
- ISMS-IMP-A.8.23.3: Policy Configuration Assessment (which policies apply where)
- ISMS-IMP-A.8.23.5: Compliance Dashboard (pulls coverage data)
- Network Architecture Documentation
- Change Management: Link network changes to coverage updates
- Risk Register: Link coverage gaps to risk IDs

### Audit Trail
- All network segments documented
- Coverage percentages calculated and tracked
- Exemptions formally approved and reviewed
- Verification tests documented
- Evidence maintained for all claims
- Approval sign-off with quarterly reviews

---

**END OF SPECIFICATION**

*"Cargo cult ISMS says 'we have web filtering.' Systems engineering says 'we have verified 97.3% coverage across 47 network segments with 3 approved exemptions and quarterly verification testing.'"*

**Network Coverage Score = Evidence ÷ Theater** ✅