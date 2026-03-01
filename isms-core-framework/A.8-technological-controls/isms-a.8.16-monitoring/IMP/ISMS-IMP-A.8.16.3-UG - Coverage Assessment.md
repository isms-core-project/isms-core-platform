<!-- ISMS-CORE:IMP:ISMS-IMP-A.8.16.3-UG:framework:UG:a.8.16.3 -->
**ISMS-IMP-A.8.16.3-UG - Coverage Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.16: Monitoring Activities

---

**Document Control**

| Attribute | Value |
|-------|-------|
| **Document Title** | Coverage Assessment |
| **Document Type** | Implementation Specification |
| **Document ID** | ISMS-IMP-A.8.16.3-UG |
| **Related Policy** | ISMS-POL-A.8.16 (Monitoring) |
| **Control Reference** | ISO/IEC 27001:2022 Annex A.8.16 (Monitoring Activities) |
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

- ISMS-POL-A.8.16 (Monitoring)
- ISMS-IMP-A.8.16.1 (Monitoring Infrastructure Assessment)
- ISMS-IMP-A.8.16.2 (Baseline & Detection Assessment)
- ISMS-IMP-A.8.16.4 (Alert Management & Response Assessment)

---

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.8.16.3-TG.

---

**IMPLEMENTATION NOTE:**

This assessment **DEPENDS ON** completion of:

- **ISMS-IMP-A.8.16.1** (Monitoring Infrastructure Assessment) - provides monitoring platform inventory
- **ISMS-IMP-A.8.16.2** (Baseline & Detection Assessment) - provides baseline and detection rule status

Cross-references between assessments are critical for accurate coverage analysis.

**Document Length:** ~2,200 lines total (Part I: ~1,800 lines + Part II: ~400 lines)

---

## Workbook at a Glance

| # | Sheet Name | Purpose |
|---|-----------|---------|
| 1 | Instructions & Legend | How to use this workbook and understand the colour coding |
| 2 | 1. Asset Coverage | Assess monitoring coverage across assets |
| 3 | 2. Network Coverage | Assess monitoring coverage across network segments |
| 4 | 3. User Identity Coverage | Assess monitoring coverage for user and identity activity |
| 5 | 4. Application Coverage | Assess monitoring coverage for applications |
| 6 | 5. Gap Analysis | Identify monitoring coverage gaps and blind spots |
| 7 | Evidence Register | Store and reference evidence supporting assessments |
| 8 | Summary Dashboard | Compliance status and key metrics overview |
| 9 | Approval Sign-Off | Management review sign-off and certification |

---

# EXECUTIVE SUMMARY

## What This Assessment Does

**ISMS-IMP-A.8.16.3** assesses monitoring COVERAGE - answering the critical question: **"What are we monitoring vs. what SHOULD we be monitoring?"**

This assessment maps your entire organisation's attack surface and verifies monitoring coverage:

**Key Questions Answered:**
1. **Asset Coverage:** Are all assets inventoried and appropriately monitored?
2. **Network Coverage:** Are all network segments, zones, and entry/exit points monitored?
3. **Identity Coverage:** Are all user accounts, privileged accounts, and service accounts monitored?
4. **Application Coverage:** Are all applications, services, and APIs monitored?
5. **Blind Spots:** Where are our monitoring gaps? What can attackers do without detection?

## Why This Assessment Matters

**The Coverage Problem:**
Most organisations believe they have comprehensive monitoring, but in reality:

- Only 40-60% of critical assets are actually monitored
- Network blind spots exist (legacy VLANs, guest networks, OT/IoT)
- Shadow IT and cloud resources are unmonitored
- Service accounts and non-human identities overlooked
- Third-party SaaS applications have no visibility

**This assessment prevents false confidence** by:

- Forcing complete asset inventory (you can't monitor what you don't know exists)
- Mapping monitoring coverage systematically (not relying on assumptions)
- Identifying blind spots with risk assessment
- Documenting remediation plans with accountability

**Anti-Cargo-Cult Principle:**
Saying "we have monitoring" means nothing if you can't show:

- **WHAT** specific assets/networks/users/apps are monitored
- **WHERE** monitoring gaps exist
- **WHY** gaps exist (technical limitation, business decision, temporary condition)
- **WHEN** gaps will be closed

This assessment provides that evidence.

## How This Relates to Other A.8.16 Assessments

| Assessment | Focus | Relationship to A.8.16.3 |
|-----------|-------|--------------------------|
| ISMS-IMP-A.8.16.1 | Infrastructure | Provides monitoring platforms available → A.8.16.3 maps what they monitor |
| ISMS-IMP-A.8.16.2 | Baselines & Detection | Provides baseline/detection status → A.8.16.3 validates coverage is complete |
| **ISMS-IMP-A.8.16.3** | **Coverage** | **WHERE monitoring deployed** (THIS ASSESSMENT) |
| ISMS-IMP-A.8.16.4 | Alert Management | Uses coverage data to understand alert context |

**Dependency Chain:**
```
A.8.16.1 (Infrastructure) → A.8.16.3 (Coverage)
A.8.16.2 (Baselines) → A.8.16.3 (Coverage)
A.8.16.3 (Coverage) → A.8.16.4 (Alert Management)
```

**You cannot accurately assess coverage without knowing:**

- What monitoring platforms exist (A.8.16.1)
- What baselines/detections are established (A.8.16.2)

## How to Use This Document

### For Asset Owners & IT Operations:

**You are the SOURCE OF TRUTH** for what exists in the organisation.

**Your Role:**

- Provide complete asset inventory (servers, network devices, endpoints, cloud resources)
- Identify asset criticality and data classification
- Verify monitoring status (is this asset actually being monitored?)
- Explain gaps (why isn't this critical server monitored yet?)

**Expected Time:** 10-20 hours depending on asset count and inventory quality

### For Security Operations (SOC):

**You verify monitoring from the SIEM perspective.**

**Your Role:**

- Cross-check asset inventory against SIEM data sources
- Identify assets claiming to be "monitored" but no logs received
- Document log types collected per asset
- Verify baselines and detection rules are active

**Expected Time:** 8-15 hours

### For Network Teams:

**You document network topology and segment coverage.**

**Your Role:**

- Map all network segments, VLANs, subnets
- Identify monitoring placement (span ports, TAPs, flow collectors)
- Document network blind spots (unmonitored segments)
- Explain network security zones and monitoring requirements

**Expected Time:** 5-10 hours

### For Application Teams:

**You document application inventory and monitoring integration.**

**Your Role:**

- List all applications (on-prem, cloud, SaaS)
- Verify application logging is forwarded to monitoring
- Document API monitoring coverage
- Identify applications with no monitoring capability

**Expected Time:** 5-10 hours

### For Auditors & Compliance Officers:

**Use this assessment as evidence of ISO 27001:2022 Control A.8.16 compliance.**

This assessment provides:

- Comprehensive coverage inventory (not sampling)
- Gap documentation with risk assessment and remediation plans
- Traceability from policy requirements to implementation evidence
- Executive dashboard showing coverage metrics

---

# Assessment Overview

## Purpose & Scope

**Assessment Name:** ISMS-IMP-A.8.16.3 - Coverage Assessment

This assessment documents WHERE monitoring is deployed across your organisation's entire attack surface.

**Core Purpose:**
Prevent blind spots by systematically mapping monitoring coverage against your complete asset inventory, network topology, identity systems, and application portfolio.

**Scope Boundaries:**

**IN SCOPE:**

- All organisational assets (on-premises, cloud, hybrid)
- All network segments and security zones
- All user accounts and service accounts
- All applications (commercial, custom, SaaS)
- All entry/exit points (internet gateways, partner connections, remote access)

**OUT OF SCOPE:**

- Monitoring platform technical capabilities (covered in A.8.16.1)
- Baseline and detection rule quality (covered in A.8.16.2)
- Alert handling procedures (covered in A.8.16.4)

## Key Principle: Coverage is Binary

An asset/network/user/application is EITHER monitored OR NOT monitored. There is no "maybe."

**Coverage States:**

- ✅ **Full Coverage:** Monitoring deployed, logs verified, baselines established, detection active
- ⚠️ **Partial Coverage:** Monitoring deployed but incomplete (some logs missing, no baselines, detection gaps)
- ❌ **No Coverage:** Zero monitoring (not sending any logs to monitoring platform)
- **N/A:** Out of scope (decommissioned, air-gapped by design, exception approved)

**Partial Coverage is a GAP** - treat it as such. Document what's missing and remediate.

## What You'll Document

### Sheet 2: Asset Inventory & Coverage

- Complete organisational asset inventory
- Asset criticality, data classification, regulatory scope
- Current monitoring status per asset
- Coverage gaps and remediation plans

### Sheet 3: Network Segment Coverage

- All network segments, VLANs, subnets, security zones
- Monitoring placement (span ports, TAPs, NetFlow, cloud VPC flow logs)
- Network entry/exit points (internet gateways, VPN, partner connections)
- Network blind spots and risk assessment

### Sheet 4: User & Identity Coverage

- User account inventory (employees, contractors, third-party)
- Privileged account coverage (domain admins, DBAs, cloud admins)
- Service account coverage (application accounts, automation accounts)
- Identity system monitoring (AD, Entra ID/Entra ID, Okta, LDAP)

### Sheet 5: Application & Service Coverage

- Application inventory (on-prem, cloud, SaaS)
- Application logging capability and status
- API monitoring coverage
- Database monitoring coverage
- Critical business services coverage

## Policy References

This assessment implements requirements from:

**Primary Policy References:**

- **ISMS-POL-A.8.16, Section 2.1.2 (Log Source Coverage)**
  - Requirement: All Critical (Tier 1) systems MUST be monitored
  - Requirement: >80% of High (Tier 2) systems monitored
  - Requirement: >60% of Medium (Tier 3) systems monitored
- **ISMS-POL-A.8.16, Section 2.1.3 (Monitoring Coverage Assessment)**
  - Requirement: Quarterly coverage assessment
  - Requirement: Blind spot identification and risk documentation
  - Requirement: Gap remediation plans with timelines

**Supporting Policy References:**

- ISMS-POL-00 (Regulatory Applicability Framework)
- ISMS-POL-A.8.16, Section 2.1.1 (Monitoring Infrastructure Requirements)

**Regulatory Context:**

- ISO/IEC 27001:2022 A.8.16: Monitoring activities
- GDPR Article 32: Technical measures including monitoring
- PCI DSS v4.0.1 10.2: Audit log coverage requirements
- HIPAA §164.312(b): Audit controls

## Expected Outputs

After completing this assessment, you will have:

1. **Complete Coverage Inventory**

   - Every asset with monitoring status documented
   - Every network segment with monitoring placement mapped
   - Every user/service account with monitoring verified
   - Every application with logging status documented

2. **Coverage Metrics**

   - Overall coverage percentage (monitored / total assets)
   - Coverage by criticality tier (Tier 1: __%, Tier 2: __%, Tier 3: __%)
   - Coverage by asset type (servers: __%, network: __%, endpoints: __%)
   - Coverage by regulatory scope (PCI: __%, HIPAA: __%, GDPR: __%)

3. **Blind Spot Inventory**

   - List of unmonitored critical assets
   - List of unmonitored network segments
   - List of unmonitored privileged accounts
   - Risk assessment for each blind spot

4. **Gap Remediation Plan**

   - Prioritized list of gaps (Critical → High → Medium)
   - Remediation actions with assigned owners
   - Target completion dates per policy requirements
   - Resource requirements (budget, tools, staff)

5. **Evidence Package**

   - Asset inventory exports
   - Network diagrams with monitoring placement
   - SIEM data source lists
   - Coverage validation reports
   - Gap remediation tracking

6. **Executive Dashboard**

   - Coverage compliance status (✅ Compliant, ⚠️ Partial, ❌ Non-Compliant)
   - Key metrics visualization
   - Trend analysis (coverage improving/degrading)
   - Risk summary (high-risk blind spots)

---

# Prerequisites & Information Needed

Before starting this assessment, you MUST have:

## Completed Prerequisites

**REQUIRED:**

- ✅ **ISMS-IMP-A.8.16.1 completed** - You need to know what monitoring platforms exist
- ✅ **Asset inventory available** - CMDB, asset management system, or manual inventory
- ✅ **Network documentation** - Network diagrams, VLAN maps, IP address management

**RECOMMENDED:**

- ✅ **ISMS-IMP-A.8.16.2 completed** - Baseline and detection status enhances coverage assessment
- ✅ **Cloud resource inventory** - AWS Config, Azure Resource Graph, GCP Asset Inventory

## Asset Inventory Data

**Required Information for Each Asset:**

- Asset ID / Hostname
- Asset Type (Server, Network Device, Endpoint, Cloud Resource, etc.)
- Operating System / Platform
- Location (datacenter, cloud region, office location)
- Business Unit / Department owner
- Data classification (Confidential, Internal, Public)
- Criticality tier (Critical, High, Medium, Low)
- Regulatory scope (PCI-DSS, HIPAA, GDPR, etc.)

**Sources:**

- CMDB (ServiceNow, Jira Assets, Device42)
- Active Directory (for Windows systems)
- Cloud provider APIs (AWS, Azure, GCP)
- Network management systems (SolarWinds, LibreNMS)
- Endpoint management (SCCM, Intune, Jamf)

**Quality Check:** Asset inventory should be <90 days old (updated within last quarter)

## Network Topology Data

**Required Information:**

- All network segments / VLANs with IP ranges
- Network security zones (DMZ, Internal, Partner, Guest)
- Network monitoring placement (span ports, TAPs, NetFlow sources)
- Internet entry/exit points (firewalls, routers, gateways)
- Remote access infrastructure (VPN concentrators, cloud connectors)

**Sources:**

- Network diagrams (Visio, draw.io, NetBrain)
- IP Address Management (IPAM) systems
- VLAN configuration exports from core switches
- Firewall configuration showing zones/interfaces

## Identity System Data

**Required Information:**

- User account inventory (Active Directory, Entra ID, Okta, LDAP)
- Privileged account list (Domain Admins, Enterprise Admins, DBAs, Cloud Admins)
- Service account inventory (application accounts, automation accounts)
- Identity system monitoring status (AD audit logs, Entra ID sign-ins, Okta logs)

**Sources:**

- AD PowerShell exports: `Get-ADUser -Filter *`
- Entra ID portal → Users
- Okta admin console → Users
- Privileged Access Management (PAM) system

## Application Portfolio Data

**Required Information:**

- Application inventory (all production applications)
- Application type (on-premises, IaaS, PaaS, SaaS)
- Application criticality and data classification
- Logging capability (native logging, agent-based, API)
- Current logging status (logging to SIEM? Logs verified?)

**Sources:**

- Application portfolio management system
- Service catalog
- Cloud provider application inventories
- Application owner interviews

## Access Requirements

**System Access Needed:**

- Read access to asset management / CMDB
- Read access to monitoring platforms (SIEM, EDR, NDR)
- Read access to network management systems
- Read access to identity systems (AD, Entra ID, Okta)
- Read access to cloud environments (for resource inventory)

**Data Export Capability:**

- Ability to export asset lists to CSV/Excel
- Ability to export SIEM data source configurations
- Ability to query monitoring platform for log verification

**Coordination:**

- Schedule time with Asset Owners, Network Team, Application Teams
- Plan for stakeholder interviews (1-2 hours each)

## Time Commitment

**Assessment Duration:** 2-3 weeks for comprehensive coverage assessment

**Effort Breakdown:**

- Asset inventory validation: 15-25 hours
- Network coverage mapping: 8-12 hours
- Identity coverage assessment: 5-8 hours
- Application coverage review: 8-12 hours
- Gap analysis and remediation planning: 10-15 hours
- Documentation and approval: 5-8 hours

**Total Effort:** 50-80 hours (can be distributed across multiple team members)

**Team Composition:**

- Lead Assessor (SOC / Security Engineering): 30-40 hours
- Asset Owner / IT Operations: 10-15 hours
- Network Team: 5-8 hours
- Application Teams: 5-8 hours

---

# Assessment Workflow

## Phase 1: Data Collection & Inventory (Week 1)

**Activities:**
1. Export asset inventory from CMDB/asset management
2. Export SIEM data source list from A.8.16.1, Sheet 3
3. Collect network diagrams and VLAN documentation
4. Export identity system user/account lists
5. Gather application inventory from service catalog

**Deliverables:**

- Unified asset inventory (Excel/CSV)
- SIEM data source list
- Network topology maps
- Identity account lists
- Application portfolio list

**Key Stakeholders:** IT Operations, Network Team, Application Owners

**Timeline:** 5 business days

## Phase 2: Coverage Validation (Week 1-2)

**Activities:**
1. **Asset Coverage Validation:**

   - For each asset in inventory, verify monitoring status in SIEM
   - Query SIEM: `host="[asset-name]"` and check for recent logs
   - Document log types collected
   - Mark coverage status (Full, Partial, None)

2. **Network Coverage Validation:**

   - Map monitoring placement to network diagram
   - Identify network segments with/without monitoring
   - Verify NetFlow / flow log collection
   - Document blind spots

3. **Identity Coverage Validation:**

   - Verify user authentication logs reaching SIEM
   - Check privileged account monitoring coverage
   - Validate service account logging
   - Test identity system integration

4. **Application Coverage Validation:**

   - Check application logging configuration
   - Verify application logs in SIEM
   - Document applications with no logging capability
   - Identify SaaS applications with/without log export

**Deliverables:**

- Asset-by-asset coverage status
- Network segment coverage map
- Identity monitoring coverage report
- Application logging status matrix

**Key Stakeholders:** SOC Analysts, SIEM Administrators

**Timeline:** 8-10 business days

## Phase 3: Gap Analysis & Remediation Planning (Week 2)

**Activities:**
1. **Identify Coverage Gaps:**

   - List all assets with no/partial coverage
   - Prioritize by criticality and risk
   - Group gaps by root cause (technical, process, resource)

2. **Risk Assessment:**

   - For each gap, assess risk (likelihood × impact)
   - Document potential attack scenarios if unmonitored
   - Assign risk rating (Critical, High, Medium, Low)

3. **Remediation Planning:**

   - Define remediation actions per gap
   - Assign ownership (who will implement)
   - Set target dates per policy (30 days for Critical gaps)
   - Identify resource requirements (budget, tools, staff)

4. **Exception Management:**

   - Identify gaps requiring formal exceptions
   - Document compensating controls
   - Prepare exception requests for CISO approval

**Deliverables:**

- Gap inventory with risk ratings
- Remediation plan with owners and dates
- Exception request documentation
- Resource requirements summary

**Key Stakeholders:** Security Manager, Asset Owners, CISO

**Timeline:** 3-5 business days

## Phase 4: Documentation & Approval (Week 3)

**Activities:**
1. Complete all assessment sheets with validated data
2. Fill Evidence Register (Sheet 8) with supporting documentation
3. Generate Summary Dashboard (Sheet 7) with coverage metrics
4. Submit for three-level approval workflow

**Deliverables:**

- Completed ISMS-IMP-A.8.16.3 workbook
- Evidence package
- Executive summary presentation

**Key Stakeholders:** Security Management, Compliance, CISO

**Timeline:** 5-7 business days (including approval time)

---

# Completing Each Sheet

## Sheet 1: Instructions & Legend

**Purpose:** Workbook overview and color-coded legend

**What to Complete:**

- Assessment Date (DD.MM.YYYY)
- Completed By (your name and role)
- Organisation name
- Review cycle (typically Quarterly for coverage assessment)
- Next Review Date (auto-calculated: Assessment Date + 90 days)

**Time Required:** 5 minutes

**Read completely** - explains color coding used throughout workbook:

- ✅ Green: Full coverage, compliant
- ⚠️ Yellow: Partial coverage, needs attention
- ❌ Red: No coverage, critical gap
- ⬜ Gray: N/A or out of scope

---

## Sheet 2: Asset Inventory & Monitoring Coverage

**Purpose:** Document EVERY organisational asset and its monitoring coverage status

**Policy Reference:** ISMS-POL-A.8.16, Section 2.1.2 (Log Source Coverage)

**Why This Sheet Is Critical:**
This is your COMPLETE attack surface inventory. If an asset exists but isn't documented here, it's a blind spot.

**Attackers love blind spots** - systems you don't know about can't be monitored.

**Structure:**

- **Rows 8-50:** 43 data entry rows (comprehensive asset inventory)
- **Rows 53-75:** Coverage summary metrics (auto-calculated)

### Column-by-Column Completion Guide

**Column A: Asset ID**

- **What to Enter:** Unique identifier for each asset
- **Examples:** `SRV-DC-01`, `FW-EDGE-DMZ-01`, `aws-ec2-i-0a1b2c3d`
- **Source:** CMDB, asset management system, or defined naming convention
- **Critical:** MUST match asset IDs used in A.8.16.1, Sheet 3 for cross-reference

**Column B: Asset Name**

- **What to Enter:** Human-readable asset name/description
- **Examples:**
  - `Primary Domain Controller - Corporate Forest`
  - `DMZ Firewall - Internet Gateway`
  - `Production Web Server - Customer Portal`
  - `AWS RDS - Order Database`

**Column C: Asset Type (Dropdown)**

- **Options:** Server, Network Device, Security Device, Endpoint, Cloud Resource, Database, Application, Container, IoT Device, Other
- **Selection Guide:**
  - **Server:** Physical/virtual servers (Windows, Linux, Unix)
  - **Network Device:** Switches, routers, load balancers, proxies
  - **Security Device:** Firewalls, IDS/IPS, WAF, DLP appliances
  - **Endpoint:** Workstations, laptops, thin clients
  - **Cloud Resource:** AWS EC2/RDS, Azure VMs/SQL, GCP Compute
  - **Database:** Standalone database servers (Oracle, PostgreSQL, MySQL, SQL Server)
  - **Application:** Application servers, middleware, web servers
  - **Container:** Docker hosts, Kubernetes nodes
  - **IoT Device:** Building automation, sensors, IP cameras

**Column D: Operating System**

- **What to Enter:** OS with version
- **Examples:** `Windows Server 2022`, `Ubuntu 22.04 LTS`, `Cisco IOS 15.7`

**Column E: Location**

- **What to Enter:** Physical or logical location
- **Examples:**
  - On-premises: `Zurich Datacenter - Rack A12`
  - Cloud: `AWS eu-central-1 (Frankfurt)`, `Azure West Europe`
  - Office: `London Office - IT Closet`

**Column F: Business Unit**

- **What to Enter:** Which department/team owns this asset
- **Examples:** `IT Operations`, `Finance`, `HR`, `Sales`, `Engineering`
- **Purpose:** Accountability and remediation ownership

**Column G: Asset Owner**

- **What to Enter:** Person responsible for this asset
- **Format:** `Name, Email` or `Team Name`
- **Examples:** `John Smith, john.smith@company.com`, `Database Team`

**Column H: Data Classification (Dropdown)**

- **Options:** Confidential, Internal, Public
- **Selection Guide:**
  - **Confidential:** PII, financial data, trade secrets, authentication credentials
  - **Internal:** Business data not for public distribution
  - **Public:** Information intended for public consumption
- **Policy Impact:** Confidential data = Tier 1 (Critical), MUST be monitored

**Column I: Criticality (Dropdown)**

- **Options:** Critical, High, Medium, Low
- **Selection Criteria (same as A.8.16.1):**
  - **Critical (Tier 1):** Security infrastructure, financial systems, regulated data, external-facing
  - **High (Tier 2):** Business-critical apps, internal file servers, network core
  - **Medium (Tier 3):** Development/test, corporate workstations, collaboration tools
  - **Low (Tier 4):** Guest systems, non-critical IoT

**Column J: Regulatory Scope (Dropdown)**

- **Options:** PCI-DSS, HIPAA, GDPR, SOX, Multiple, None
- **Purpose:** Regulatory requirements may mandate monitoring
- **Examples:**
  - PCI-DSS: All cardholder data environment (CDE) systems
  - HIPAA: All systems processing PHI
  - GDPR: Systems processing EU personal data
  - SOX: Financial reporting systems

**Column K: Monitoring Required (Dropdown)**

- **Options:** Mandatory, Recommended, Optional, N/A
- **Auto-Logic from Criticality:**
  - Critical → Mandatory
  - High → Recommended (effectively mandatory, allows exceptions)
  - Medium → Recommended
  - Low → Optional
- **Override:** Can manually set if regulatory scope mandates monitoring

**Column L: Currently Monitored (Dropdown)**

- **Options:** Yes, No, Partial
- **How to Verify:**

  1. Check A.8.16.1, Sheet 3 (Log Source Coverage) - is this asset listed?
  2. Log into SIEM and search: `host="[asset-name]"` (last 24 hours)
  3. If logs found → Yes
  4. If some logs but incomplete → Partial
  5. If no logs → No

**Critical Verification:** Don't assume - ACTUALLY search SIEM for logs

**Column M: Log Types Collected**

- **What to Enter:** Specific log types being collected (if monitored)
- **Examples:**
  - Windows: `Security, System, Application, PowerShell`
  - Linux: `syslog, auth.log, audit.log`
  - Firewall: `Traffic logs, Config changes, VPN logs`
  - Database: `Authentication, Query logs, DDL changes`
- **Leave Blank if:** Not monitored

**Column N: Monitoring Platform**

- **What to Enter:** Which monitoring platform receives logs
- **Examples:** `Splunk-Production-SIEM`, `Microsoft-Sentinel`, `QRadar`
- **Cross-Reference:** Must match platform name from A.8.16.1, Sheet 2

**Column O: Baseline Established (Dropdown)**

- **Options:** Yes, No, N/A
- **How to Verify:** Check A.8.16.2, Sheet 2/3/4 - is this asset baselined?
- **Policy Requirement:** All Tier 1 assets MUST have baselines

**Column P: Detection Rules Active**

- **What to Enter:** Count of detection rules monitoring this asset
- **How to Find:** Check A.8.16.2, Sheet 5 - count rules where this asset is in scope
- **Example:** `5 rules` (failed login, CPU spike, unauthorised access, process anomaly, network anomaly)

**Column Q: Last Log Verified (DD.MM.YYYY)**

- **What to Enter:** Date you verified logs are actually flowing
- **How to Verify:**

  1. Search SIEM for this specific asset
  2. Check timestamp of most recent log
  3. Document today's date (verification date)

- **Example:** `20.01.2026` (verified logs received within 24 hours)

**Column R: Coverage Status (Dropdown)**

- **Options:** ✅ Full Coverage, ⚠️ Partial Coverage, ❌ No Coverage, N/A
- **Selection Logic:**

| Monitoring Required | Currently Monitored | Baseline | Detection Rules | Coverage Status |
|---------------------|---------------------|----------|-----------------|-----------------|
| Mandatory | Yes | Yes | Yes (multiple) | ✅ Full Coverage |
| Mandatory | Yes | No | Some | ⚠️ Partial Coverage |
| Mandatory | Yes | No | No | ⚠️ Partial Coverage |
| Mandatory | No | N/A | N/A | ❌ No Coverage (CRITICAL GAP) |
| Recommended | Yes | Yes | Yes | ✅ Full Coverage |
| Recommended | No | N/A | N/A | ⚠️ Partial Coverage |
| Optional | Any | Any | Any | N/A (optional - no requirement) |

**Red Flag:** Critical asset with "❌ No Coverage" = HIGHEST PRIORITY gap

**Column S: Gap Reason**

- **What to Enter:** WHY coverage gap exists (if ⚠️ Partial or ❌ No Coverage)
- **Examples:**
  - `Agent deployment pending change control approval - scheduled 01.02.2026`
  - `Legacy system incompatible with modern SIEM agents - custom collector required`
  - `Cloud resource auto-scaled yesterday - not yet onboarded to monitoring`
  - `System air-gapped by design - network isolated from monitoring infrastructure`
  - `Budget constraints - monitoring platform license limit reached`

**Column T: Exception Approved (Dropdown)**

- **Options:** Yes, No, N/A
- **Select "Yes" ONLY if:**
  - Formal exception request submitted
  - CISO approved in writing
  - Compensating controls documented
- **Document in Column W (Notes):** Exception ID, approval date, approver name

**Column U: Target Coverage Date (DD.MM.YYYY)**

- **What to Enter:** When will gap be closed?
- **Policy Requirements:**
  - **Critical assets (Tier 1):** 30 days maximum
  - **High assets (Tier 2):** 90 days maximum
  - **Medium assets (Tier 3):** 180 days maximum
- **Example:** `15.02.2026` (30 days from today for Critical asset gap)

**Column V: Responsible Party**

- **What to Enter:** Who will close this gap?
- **Examples:**
  - `IT Operations - Server Team`
  - `Cloud Engineering - AWS Team`
  - `John Smith, Senior SysAdmin`
- **Purpose:** Accountability for gap closure

**Column W: Notes**

- **What to Enter:** Additional context, special considerations
- **Use Cases:**
  - Exception details: `Exception EXE-A816-025 approved by CISO on 15.01.2026. Compensating control: Physical access restricted, network isolated.`
  - Technical details: `Monitoring requires TLS certificate installation - certificate request in progress`
  - Temporary status: `System being decommissioned 28.02.2026 - monitoring not required`

---

### Completing Sheet 2: Step-by-Step Process

**Step 1: Export Base Asset Inventory (30-60 minutes)**

**From CMDB/Asset Management:**
```sql
SELECT asset_id, asset_name, asset_type, os, location, business_unit, 
       owner, data_classification, criticality, regulatory_scope
FROM asset_inventory
WHERE status = 'Active'
ORDER BY criticality, asset_type
```

**From Active Directory (Windows systems):**
```powershell
Get-ADComputer -Filter * -Properties OperatingSystem, Description, Location |
Select Name, OperatingSystem, Description, Location |
Export-CSV "AD_Assets.csv"
```

**From Cloud Providers:**
```bash
# AWS EC2 instances
aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId,Tags[?Key==`Name`].Value|[0],State.Name]' --output table

# Azure VMs
az vm list --query '[].{Name:name, ResourceGroup:resourceGroup, Location:location}' -o table

# GCP Compute instances
gcloud compute instances list --format="table(name,zone,status)"
```

**Step 2: Import to Sheet 2 (15-30 minutes)**

1. Copy asset data into Columns A-J (Asset ID through Regulatory Scope)
2. Leave Columns K-W blank initially (will fill during verification)
3. Sort by Criticality (Critical first) then Asset Type

**Step 3: Verify Monitoring Status Asset-by-Asset (MOST TIME-CONSUMING: 5-15 hours)**

**For each asset:**

**Verification Process:**
1. **Check A.8.16.1, Sheet 3** - Is this asset documented as monitored?
2. **Search SIEM:**
   ```
   host="[asset-name]" OR host="[asset-id]" OR source=[ip-address]
   earliest=-24h latest=now
   ```
3. **If logs found:**

   - Column L = "Yes"
   - Column M = List log types present
   - Column N = Monitoring platform name
   - Column Q = Today's date

4. **If no logs found:**

   - Column L = "No"
   - Column M-N-Q = Leave blank

5. **If some logs but incomplete:**

   - Column L = "Partial"
   - Column M = List which logs ARE collected
   - Document missing logs in Column S

**Batch Verification Technique (for large environments):**
```spl
| inputlookup asset_inventory.csv
| join type=left asset_id [
    search index=* earliest=-7d latest=now
    | stats count, latest(_time) as last_log by host
    | rename host as asset_id
]
| eval monitored = if(isnull(count), "No", "Yes")
| eval days_since_log = round((now() - last_log) / 86400, 1)
| table asset_id, monitored, count, days_since_log
```

**Step 4: Check Baseline and Detection Status (1-2 hours)**

**For each monitored asset:**

1. **Check A.8.16.2, Sheet 2/3/4** - Is baseline documented?

   - If Yes → Column O = "Yes"
   - If No → Column O = "No"

2. **Check A.8.16.2, Sheet 5** - Count detection rules covering this asset

   - Count rules where asset is in scope
   - Column P = Count

**Step 5: Determine Coverage Status (30-60 minutes)**

**Apply logic from Column R selection guide:**

- Full Coverage: Monitored + Baseline + Detection Rules
- Partial Coverage: Monitored but missing baseline OR missing detection
- No Coverage: Not monitored at all

**Step 6: Document Gaps and Remediation Plans (2-4 hours)**

**For each asset with ⚠️ Partial or ❌ No Coverage:**

1. **Investigate WHY:**

   - Technical limitation?
   - Resource constraint?
   - Process gap?
   - Awaiting approval?

2. **Document in Column S:** Root cause

3. **Determine if exception needed:**

   - Air-gapped system (by design)
   - Legacy system (end-of-life, no agent support)
   - Temporary condition (awaiting decommission)
   - If Yes → Submit exception request

4. **Set target date** (Column U) per policy timelines

5. **Assign ownership** (Column V) to person who will remediate

**Step 7: Review Coverage Summary (30 minutes)**

**Auto-Calculated Metrics (Rows 53-75):**

- **Total Assets:** Count of all assets
- **Assets Monitored:** Count where Column L = "Yes"
- **Overall Coverage %:** (Monitored / Total) × 100

**Coverage by Criticality:**

- **Critical (Tier 1):** ___% (Policy: 100% required)
- **High (Tier 2):** ___% (Policy: >80%)
- **Medium (Tier 3):** ___% (Policy: >60%)
- **Low (Tier 4):** ___% (No requirement)

**Coverage by Asset Type:**

- Servers: ___%
- Network Devices: ___%
- Security Devices: ___%
- Endpoints: ___%
- Cloud Resources: ___%
- Databases: ___%

**Critical Gaps:**

- Count of Tier 1 assets with No Coverage: ___ (CRITICAL)
- Count of Tier 2 assets with No Coverage: ___ (HIGH)
- Count of assets with Partial Coverage: ___ (MEDIUM)

**Compliance Status:**

- ✅ Compliant: All policy requirements met
- ⚠️ Partial: Some gaps exist, remediation plans in place
- ❌ Non-Compliant: Critical gaps without plans

---

## Sheet 3: Network Segment Coverage

**Purpose:** Map network topology and verify monitoring placement across all segments

**Policy Reference:** ISMS-POL-A.8.16, Section 2.1.3 (Network Coverage)

**Why This Sheet Matters:**
Network blind spots allow attackers to move laterally undetected. You might monitor individual systems, but if network traffic between them is unmonitored, you miss:

- Lateral movement
- Data exfiltration
- Command & control (C2) traffic
- Reconnaissance scans

**Structure:**

- **Rows 8-32:** 25 data entry rows (network segment inventory)
- **Rows 35-50:** Network coverage analysis

### Key Columns Guide

**Column A: Network Segment ID**

- **Format:** `NET-[Location]-[Type]-[#]`
- **Examples:** `NET-ZRH-DMZ-01`, `NET-AWS-PROD-VPC-01`, `NET-BRANCH-GUEST-WiFi`

**Column B: Network Name/Description**

- **Examples:**
  - `Zurich Datacenter - DMZ Segment (Public-Facing Servers)`
  - `AWS Production VPC - Application Tier`
  - `Corporate LAN - Finance Department VLAN`

**Column C: Network Type (Dropdown)**

- **Options:** Internet-Facing (DMZ), Internal Production, Internal Corporate, Development/Test, Guest/Public, Partner Extranet, Management Network, OT/ICS Network, Cloud VPC/VNet
- **Purpose:** Different network types have different monitoring requirements

**Column D: IP Range/Subnet**

- **What to Enter:** CIDR notation or IP range
- **Examples:** `10.1.100.0/24`, `192.168.10.0/24`, `172.16.0.0/16`, `AWS VPC: 10.0.0.0/16`

**Column E: VLAN ID (if applicable)**

- **Examples:** `VLAN 100`, `VLAN 250 (Finance)`, `N/A (Cloud)`, `Multiple`

**Column F: Security Zone (Dropdown)**

- **Options:** Internet, DMZ, Internal-Trusted, Internal-Restricted, Partner, Guest, Management, OT/ICS
- **Purpose:** Security zones define trust boundaries and monitoring requirements

**Column G: Criticality (Dropdown)**

- **Options:** Critical, High, Medium, Low
- **Selection:**
  - **Critical:** Internet-facing, DMZ, management networks, OT/ICS
  - **High:** Internal production networks
  - **Medium:** Corporate LANs, development networks
  - **Low:** Guest networks (isolated)

**Column H: Systems/Assets on Segment**

- **What to Enter:** Count and types of systems
- **Examples:**
  - `15 servers (web, app, database)`
  - `200 workstations (Finance dept)`
  - `5 network devices (firewalls, switches)`
  - `50+ cloud resources (auto-scaled)`

**Column I: Monitoring Method (Dropdown)**

- **Options:**
  - `SPAN Port (Port Mirroring)`
  - `Network TAP (Physical)`
  - `NetFlow / IPFIX`
  - `Cloud VPC Flow Logs`
  - `Endpoint Agents Only`
  - `None`
- **Purpose:** Document HOW network traffic is monitored

**Column J: Monitoring Platform**

- **What to Enter:** Which platform receives network data
- **Examples:** `Palo Alto Firewall + Splunk`, `AWS VPC Flow Logs → S3 → SIEM`, `Zeek IDS → SIEM`

**Column K: Traffic Types Monitored (Dropdown, Multi-Select)**

- **Options:** North-South (Internet), East-West (Internal), Inbound, Outbound, DNS, DHCP, Authentication, All
- **Critical:** East-West traffic monitoring detects lateral movement

**Column L: Monitoring Coverage Status (Dropdown)**

- **Options:** ✅ Full Coverage, ⚠️ Partial Coverage, ❌ No Coverage, N/A
- **Selection:**
  - **Full:** Traffic monitored in both directions, logs verified
  - **Partial:** Only North-South monitored (missing East-West), or intermittent collection
  - **None:** Zero network monitoring on this segment

**Column M: Blind Spot Risk**

- **What to Enter:** What attacks could go undetected due to monitoring gaps?
- **Examples:**
  - `Lateral movement between finance servers undetected`
  - `Data exfiltration to cloud storage via HTTPS (encrypted, unmonitored)`
  - `C2 beaconing on non-standard ports may be missed`

**Column N: Entry/Exit Points**

- **What to Enter:** How traffic enters/exits this segment
- **Examples:**
  - `Firewall FW-EDGE-01 (monitored)`
  - `VPN concentrator VPN-CONC-02 (logs to SIEM)`
  - `AWS Internet Gateway (VPC Flow Logs enabled)`
  - `Multiple access points - not all monitored ⚠️`

**Column O: Last Traffic Verified (DD.MM.YYYY)**

- **How to Verify:** Query monitoring platform for network traffic from this segment
- **Example:** Search NetFlow for source IPs in subnet `10.1.100.0/24` - confirm data within 24 hours

**Column P: Gap Remediation Plan**

- **Examples:**
  - `Deploy network TAP on core switch SW-CORE-01 - target 15.02.2026`
  - `Enable VPC Flow Logs on AWS production VPC - in progress`
  - `Exception: Guest network isolated, no business need for monitoring`

### Network Coverage Scenarios

**Scenario 1: Internet-Facing DMZ (Full Coverage)**
```
Network: NET-ZRH-DMZ-01
Description: DMZ Segment - Public Web Servers
IP Range: 203.0.113.0/24
Security Zone: DMZ
Criticality: Critical
Monitoring Method: Firewall logs + IDS (inline) + SPAN port to NDR
Monitoring Platform: Palo Alto Firewall → Splunk, Zeek IDS → Splunk
Traffic Types: North-South (all), East-West (between DMZ servers)
Coverage Status: ✅ Full Coverage
Entry/Exit: Firewall FW-EDGE-01 (all traffic inspected)
```

**Scenario 2: Internal Network (Partial Coverage - East-West Gap)**
```
Network: NET-CORP-FIN-01
Description: Finance Department VLAN
IP Range: 10.50.10.0/24
Security Zone: Internal-Restricted
Criticality: High
Monitoring Method: Endpoint agents only (no network monitoring)
Traffic Types: North-South monitored via firewall, East-West NOT monitored ⚠️
Coverage Status: ⚠️ Partial Coverage
Blind Spot Risk: Lateral movement between finance workstations undetected
Gap Plan: Deploy SPAN port on switch SW-FLOOR3 to capture East-West traffic - target 01.03.2026
```

**Scenario 3: Cloud VPC (Full Coverage)**
```
Network: NET-AWS-PROD-VPC
Description: AWS Production VPC - Application Tier
IP Range: 10.0.0.0/16
Security Zone: Internal-Trusted (cloud)
Criticality: Critical
Monitoring Method: VPC Flow Logs + CloudTrail API logs
Monitoring Platform: AWS VPC Flow Logs → S3 → Lambda → Splunk
Traffic Types: All (North-South via IGW/NAT, East-West between subnets)
Coverage Status: ✅ Full Coverage
Entry/Exit: Internet Gateway (VPC Flow Logs enabled), Direct Connect to on-prem (Flow Logs)
```

---

## Sheet 4: User & Identity Coverage

**Purpose:** Verify monitoring coverage for all user accounts, privileged accounts, and identity systems

**Policy Reference:** ISMS-POL-A.8.16, Section 2.2.2 (Identity Monitoring)

**Why This Sheet Matters:**
Compromised credentials are the #1 initial access vector. Without identity monitoring:

- Credential theft goes undetected
- Privileged access abuse is invisible
- Account compromise spreads laterally

**Structure:**

- **Rows 8-32:** 25 data entry rows (identity coverage inventory)
- **Rows 35-50:** Identity coverage summary

### Key Columns Guide

**Column A: Identity System**

- **What to Enter:** Which identity platform
- **Examples:** `Active Directory (on-prem)`, `Entra ID / Entra ID`, `Okta`, `AWS IAM`, `LDAP`

**Column B: Account Type (Dropdown)**

- **Options:** User Accounts, Privileged Accounts (Admins), Service Accounts, System Accounts, Shared Accounts, Guest Accounts
- **Purpose:** Different account types require different monitoring

**Column C: Account Count**

- **What to Enter:** How many accounts of this type
- **Examples:**
  - `User Accounts: 1,250`
  - `Domain Admins: 12`
  - `Service Accounts: 85`

**Column D: Monitoring Coverage**

- **What to Monitor:**
  - **User Accounts:** Authentication logs (login success/failure), password changes, account modifications
  - **Privileged Accounts:** ALL activity (authentication, privilege escalation, admin commands, resource access)
  - **Service Accounts:** Authentication, unusual activity (should be very consistent)

**Column E: Log Types Collected**

- **Examples:**
  - AD: `Security Event 4624 (Logon), 4625 (Failed Logon), 4720 (User Created), 4740 (Account Locked), 4768-4770 (Kerberos)`
  - Entra ID: `Sign-in logs, Audit logs, Risky sign-ins`
  - Okta: `System logs, Authentication events, Admin actions`

**Column F: Baseline Established?**

- **Cross-Reference:** A.8.16.2, Sheet 3 (Access Pattern Baselines)
- **Policy:** All privileged accounts MUST have baselines

**Column G: Coverage Status**

- **Selection:**
  - ✅ Full: All authentication and activity logged, baseline established, detection active
  - ⚠️ Partial: Authentication logged but no baseline, or gaps in activity monitoring
  - ❌ None: Zero monitoring

**Column H: Gap / Remediation**

- **Examples:**
  - `Service accounts not baselined - establishing baselines Q1 2026`
  - `Guest accounts not logged - enabling audit policy`

### Identity Coverage Checklist

**Critical Privileged Accounts (MUST Monitor - 100%):**

- [ ] Domain Admins / Enterprise Admins (AD)
- [ ] Global Administrators (Entra ID)
- [ ] Root / sudo users (Linux)
- [ ] Database Administrators (DBAs)
- [ ] Cloud Admins (AWS root, Azure Subscription Admin, GCP Org Admin)
- [ ] Security Admins (SIEM, EDR, firewall admins)

**User Accounts (>80% Coverage):**

- [ ] Employee accounts
- [ ] Contractor accounts
- [ ] Remote workers (VPN authentication)

**Service Accounts (100% Coverage for Critical Systems):**

- [ ] Backup accounts
- [ ] Application service accounts
- [ ] Automation/orchestration accounts

---

## Sheet 5: Application & Service Coverage

**Purpose:** Document monitoring coverage for all applications and business services

**Policy Reference:** ISMS-POL-A.8.16, Section 2.2.3 (Application Monitoring)

**Why This Sheet Matters:**
Applications are where business logic and data processing occur. Without application monitoring:

- Application-layer attacks invisible (SQL injection, XSS, API abuse)
- Business logic abuse undetected
- Data access anomalies missed

**Structure:**

- **Rows 8-32:** 25 data entry rows (application inventory)
- **Rows 35-50:** Application coverage summary

### Key Columns Guide

**Column A: Application Name**

- **Examples:** `Customer Portal`, `ERP (SAP)`, `Email (Office 365)`, `CRM (Salesforce)`, `Order Management API`

**Column B: Application Type (Dropdown)**

- **Options:** On-Premises, IaaS (Cloud VM), PaaS (Cloud App Service), SaaS (Third-Party), Container-Based
- **Purpose:** Different types have different logging capabilities

**Column C: Criticality**

- **Based on:** Business impact if unavailable, data sensitivity, regulatory scope

**Column D: Logging Capability (Dropdown)**

- **Options:**
  - `Native Logging (Built-in)`
  - `Agent-Based (Requires Agent)`
  - `API/Webhook (Log Export)`
  - `Syslog Forward`
  - `No Logging (Limitation)`
- **Purpose:** Not all apps can log, especially legacy or third-party SaaS

**Column E: Log Types Available**

- **Examples:**
  - Web App: `Access logs, Error logs, Application events, Audit trail`
  - Database: `Authentication, Query logs, DDL changes, Privilege changes`
  - API: `API calls, Authentication, Rate limit violations, Errors`
  - SaaS: `Admin actions, User activity, Data access (if available)`

**Column F: Logs Forwarded to SIEM?**

- **Options:** Yes, No, Partial
- **Verify:** Search SIEM for application logs

**Column G: Baseline Established?**

- **Cross-Reference:** A.8.16.2, Sheet 4 (Application Behavior Baselines)

**Column H: Coverage Status**

- ✅ Full: Logs forwarded, baseline established, detection active
- ⚠️ Partial: Logs forwarded but no baseline, or limited log types
- ❌ None: No logging or logs not forwarded

**Column I: Gap / Remediation**

- **Examples:**
  - `SaaS app (Salesforce) - API log export not configured - enabling Q1 2026`
  - `Legacy application no logging capability - compensating control: database query monitoring`

---

# Evidence Collection

**Evidence Types Required:**

**1. Asset Inventory Documentation**

- CMDB exports (asset lists with criticality, owner, classification)
- Cloud resource inventory reports (AWS Config, Azure Resource Graph)
- Active Directory computer inventory
- Network device inventory from network management system

**2. Coverage Validation Evidence**

- SIEM data source lists (what's configured)
- SIEM query results showing log verification (screenshots)
- Asset-by-asset coverage validation reports
- "Monitored vs. Inventory" comparison analysis

**3. Network Coverage Evidence**

- Network topology diagrams with monitoring placement marked
- VLAN configuration exports
- NetFlow / VPC Flow Log configuration screenshots
- Network TAP / SPAN port documentation

**4. Identity Coverage Evidence**

- User account exports (AD, Entra ID, Okta)
- Privileged account inventory
- Service account inventory
- Identity system audit log configuration screenshots

**5. Application Coverage Evidence**

- Application portfolio inventory
- Application logging capability assessment
- SaaS log export configurations
- Application log samples in SIEM

**6. Gap Remediation Documentation**

- Gap inventory with risk assessments
- Remediation project plans
- Budget requests for monitoring expansion
- Exception approval documentation

---

# Common Pitfalls

## Pitfall 1: Asset Inventory is Stale

**The Mistake:**
Using 12-month-old asset inventory. "We have 500 servers" → Reality: 650 servers (150 unmonitored).

**Reality Check:**
IT environments change constantly:

- New servers deployed
- Cloud resources auto-scale
- Systems decommissioned (but not removed from inventory)
- Shadow IT appears

**How to Avoid:**

- Use asset inventory updated within last 90 days
- Cross-check multiple sources (CMDB, AD, cloud APIs, network scans)
- Discovery scans to find unknown assets
- Automate inventory sync where possible

**Red Flag:** Asset inventory "Last Updated" is >6 months ago

---

## Pitfall 2: Confusing "Configured" with "Working"

**The Mistake:**
Asset marked "Monitored" in CMDB → Assume logs are flowing → Actually, agent stopped 6 months ago.

**Reality Check:**
Just because monitoring is configured doesn't mean it's working:

- Agents crash and don't restart
- Log forwarding breaks after system updates
- Network changes break connectivity
- Disk full prevents local log writing

**How to Avoid:**

- ALWAYS verify by searching SIEM for recent logs
- Don't trust configuration - verify actual log delivery
- Automated monitoring health checks

**Verification Process:**
For every asset marked "Monitored":
1. Search SIEM: `host=[asset]` (last 24 hours)
2. If no logs → Status = "No" (not Monitored)
3. Document verification date

---

## Pitfall 3: Network Coverage Limited to North-South Only

**The Mistake:**
"We monitor network traffic" → Only firewall logs (Internet traffic) → Missing East-West (internal lateral movement).

**Reality Check:**
Most attacks involve lateral movement AFTER initial compromise:

- Phishing email → Compromised workstation → Pivot to servers
- If you only see Internet traffic, you miss the pivot

**How to Avoid:**

- Deploy monitoring for BOTH North-South AND East-West traffic
- Use SPAN ports, TAPs, or NetFlow on internal switches
- Monitor traffic between VLANs/subnets

**Coverage Matrix:**
| Traffic Direction | Monitoring Method | Purpose |
|-------------------|-------------------|---------|
| North-South (Internet) | Firewall logs, IDS | External threats |
| East-West (Internal) | SPAN/TAP, NetFlow | Lateral movement |
| Inbound | WAF, IPS | Incoming attacks |
| Outbound | DLP, Proxy logs | Data exfiltration |

---

## Pitfall 4: Privileged Account Monitoring Gaps

**The Mistake:**
Monitor user logins, but don't specifically monitor admin accounts differently.

**Reality Check:**
Privileged accounts ARE the crown jewels:

- Domain Admin compromise = full network control
- DBA compromise = all database access
- Cloud Admin = entire cloud environment

**How to Avoid:**

- Separate privileged account monitoring (not lumped with regular users)
- ALL privileged activity logged (not just authentication)
- Baselines for privileged accounts (A.8.16.2, Sheet 3)
- Real-time alerting on privileged account anomalies

**Privileged Account Must-Haves:**

- [ ] Authentication (all attempts)
- [ ] Privilege escalation (sudo, runas)
- [ ] Admin commands executed
- [ ] Resource access (files, databases, cloud resources)
- [ ] Account modifications (creating new admins)

---

## Pitfall 5: Service Account Blind Spot

**The Mistake:**
"Service accounts are automated - no need to monitor."

**Reality Check:**
Service accounts are HIGH-VALUE TARGETS:

- Often have elevated privileges
- Credentials stored in scripts/config files (sometimes plaintext)
- Compromise allows persistent access (no interactive login alerts)
- Activity should be VERY consistent (deviations indicate compromise)

**How to Avoid:**

- Inventory ALL service accounts
- Monitor authentication and activity
- Establish strict baselines (low StdDev expected)
- Alert on ANY deviation from baseline

**Service Account Baseline Example:**
```
Account: svc_backup
Normal: Login daily at 01:00, access 15,000 files, logout at 03:00
Anomaly: Login at 14:30 (unusual time) → ALERT
```

---

## Pitfall 6: Cloud Resource Visibility Gap

**The Mistake:**
Comprehensive on-premises monitoring, zero cloud visibility.

**Reality Check:**
"Lift and shift" to cloud doesn't mean monitoring came with it:

- EC2 instances may not have agents
- VPC Flow Logs not enabled by default
- CloudTrail logs not forwarded to SIEM
- Lambda, S3, RDS - different logging mechanisms

**How to Avoid:**

- Include ALL cloud resources in asset inventory
- Enable cloud-native logging (CloudTrail, VPC Flow, Activity Logs)
- Forward cloud logs to central SIEM
- Monitor cloud control plane (API calls, console access)

**Cloud Coverage Checklist:**

- [ ] Compute (EC2, VMs, App Services)
- [ ] Network (VPC Flow, NSG Flows, Cloud Firewall)
- [ ] Identity (IAM, Managed Identity, Service Principals)
- [ ] Data (S3, Blob Storage, RDS, SQL Database)
- [ ] Control Plane (CloudTrail, Activity Log, Cloud Logging)

---

## Pitfall 7: SaaS Application Monitoring Gap

**The Mistake:**
"It's a SaaS app - the vendor handles security" → No monitoring of user activity, data access, or admin actions.

**Reality Check:**
SaaS apps are PART OF YOUR ATTACK SURFACE:

- Compromised O365 account = email access, OneDrive exfiltration
- Salesforce admin compromise = all customer data
- Slack compromise = sensitive communications exposed

**How to Avoid:**

- Inventory ALL SaaS applications
- Enable audit logging where available
- Export logs to SIEM (via API, webhook, CASB)
- Monitor admin actions, data access, external sharing

**SaaS Logging Options:**
| SaaS App | Logging Capability | Integration Method |
|----------|--------------------|--------------------|
| Office 365 | Audit logs, sign-ins | Graph API, Entra ID logs |
| Salesforce | Event Monitoring, Login History | REST API, Event Log Files |
| Okta | System logs | Webhook, API |
| Slack | Audit logs (paid tiers) | API |
| GitHub | Audit logs | Webhooks |

---

## Pitfall 8: OT/ICS Network Assumed Isolated (Not Monitored)

**The Mistake:**
"Our OT network is air-gapped - no monitoring needed."

**Reality Check:**
OT networks often have hidden connectivity:

- Remote vendor access
- Historian servers bridging IT/OT
- Engineering workstations with dual NICs
- Wireless access points

**How to Avoid:**

- Map ALL OT network segments
- Monitor OT/IT boundaries (where they connect)
- Passive monitoring for OT (don't disrupt operations)
- Baseline OT traffic (very consistent, deviations suspicious)

**OT Monitoring Considerations:**

- **Passive only:** TAPs, not SPAN (no performance impact)
- **Protocol-aware:** Modbus, DNP3, IEC 61850 parsing
- **Baseline deviation detection:** OT very predictable
- **Safety critical:** Monitor without affecting operations

---

## Pitfall 9: Coverage Assessment is One-Time Event

**The Mistake:**
Complete comprehensive coverage assessment → Shelf it → Never update → Environment changes → Assessment stale.

**Reality Check:**
Coverage degrades over time:

- New systems deployed (not onboarded to monitoring)
- Monitoring agents break (not replaced)
- Cloud resources scale up (new instances unmonitored)
- Network changes introduce blind spots

**How to Avoid:**

- **Quarterly coverage reviews** (policy requirement)
- Automated coverage monitoring (alert when assets detected but not monitored)
- New asset onboarding process includes monitoring
- Change management triggers coverage re-assessment

**Continuous Monitoring Approach:**
```spl
# Daily check: Assets in inventory but not in SIEM
| inputlookup asset_inventory.csv
| join type=left asset_id [search index=* earliest=-7d | stats count by host | rename host as asset_id]
| where isnull(count)
| table asset_id, asset_name, criticality
| outputlookup unmonitored_assets.csv
```

---

## Pitfall 10: No Risk Prioritization for Gaps

**The Mistake:**
Gap list: 200 unmonitored systems → Treat all equally → Overwhelmed → Paralysis.

**Reality Check:**
Not all gaps are equal:

- Unmonitored Critical asset with Confidential data = HIGHEST RISK
- Unmonitored Low priority test system = LOW RISK

**How to Avoid:**

- Risk-prioritize gaps (Criticality × Data Classification × Regulatory Scope)
- Address Critical gaps FIRST (30-day timeline)
- Defer Low priority gaps (or accept risk)

**Gap Risk Matrix:**
| Criticality | Data Classification | Risk Level | Remediation Timeline |
|-------------|---------------------|------------|----------------------|
| Critical | Confidential | **CRITICAL** | 30 days |
| Critical | Internal | **HIGH** | 60 days |
| High | Confidential | **HIGH** | 60 days |
| High | Internal | **MEDIUM** | 90 days |
| Medium | Any | **LOW** | 180 days |
| Low | Any | **ACCEPT RISK** | Optional |

---

# Quality Checklist

## Sheet 2: Asset Inventory & Coverage

- [ ] Asset inventory complete (all production assets documented)
- [ ] Asset inventory current (updated within 90 days)
- [ ] All Critical assets have criticality documented
- [ ] Monitoring status VERIFIED (searched SIEM, not assumed)
- [ ] "Last Log Verified" within policy timeframes (7 days Tier 1, 30 days Tier 2)
- [ ] Coverage gaps documented with reasons (Column S)
- [ ] All Tier 1 gaps have remediation plans (Column U, V)
- [ ] Exceptions formally approved (Column T = Yes + documentation)
- [ ] Coverage summary metrics calculated correctly
- [ ] Tier 1 coverage ≥100% OR gaps have approved exceptions

## Sheet 3: Network Segment Coverage

- [ ] All network segments documented (no missing VLANs/subnets)
- [ ] Network monitoring methods documented per segment
- [ ] Both North-South AND East-West traffic considered
- [ ] Internet entry/exit points all monitored
- [ ] VPN/remote access points monitored
- [ ] Cloud VPC/VNet flow logs enabled
- [ ] Network blind spots identified and risk-assessed
- [ ] Critical network gaps have remediation plans

## Sheet 4: User & Identity Coverage

- [ ] All identity systems documented (AD, Entra ID, Okta, AWS IAM, etc.)
- [ ] Privileged accounts 100% monitored
- [ ] Service accounts inventoried and monitored
- [ ] User authentication logs forwarded to SIEM
- [ ] Identity system baselines established (cross-check A.8.16.2)
- [ ] Guest accounts monitored or isolated
- [ ] Shared accounts identified (flag for remediation)

## Sheet 5: Application & Service Coverage

- [ ] Application inventory complete (on-prem, cloud, SaaS)
- [ ] Critical applications 100% monitored
- [ ] SaaS application logging enabled where possible
- [ ] Application logging limitations documented
- [ ] Database activity monitored
- [ ] API monitoring coverage documented
- [ ] Applications with no logging have compensating controls

## Cross-Assessment Validation

- [ ] A.8.16.1, Sheet 3 (Log Source Coverage) matches A.8.16.3, Sheet 2 (Asset Coverage)
- [ ] Monitoring platforms (A.8.16.1) support coverage documented here
- [ ] Baselines (A.8.16.2) exist for monitored assets
- [ ] No contradictions between assessments

## Overall Quality

- [ ] >90% of Tier 1 assets monitored (or exceptions approved)
- [ ] >80% of Tier 2 assets monitored
- [ ] Network coverage includes both North-South and East-West
- [ ] 100% of privileged accounts monitored
- [ ] Evidence register complete (Sheet 8)
- [ ] All gaps have documented remediation plans with owners and dates
- [ ] No "TBD" or placeholder values remaining

---

# Review & Approval

**Three-Level Approval Workflow (same as A.8.16.1 and A.8.16.2):**

**Level 1: Technical Review** (SOC Lead, IT Operations Manager)

- **Focus:** Coverage data accuracy, gap analysis validity
- **Timeline:** 2-3 business days
- **Criteria:**
  - Asset inventory complete and current
  - Monitoring status verified (not assumed)
  - Network coverage accurately mapped
  - Identity and application coverage validated

**Level 2: Compliance Review** (Security Manager, CISO)

- **Focus:** Policy compliance, risk assessment, remediation adequacy
- **Timeline:** 3-5 business days
- **Criteria:**
  - Tier 1 coverage ≥100% (or approved exceptions)
  - Tier 2/3 coverage meets thresholds (>80%, >60%)
  - Critical gaps have remediation plans ≤30 days
  - Risk acceptance documented for approved exceptions

**Level 3: Executive Approval** (CISO)

- **Focus:** Strategic alignment, investment requirements, risk acceptance
- **Timeline:** 5-7 business days
- **Criteria:**
  - Coverage gaps align with risk appetite
  - Budget requirements for gap closure identified
  - High-risk blind spots either remediated or risk accepted
  - Coverage improving over time (trend analysis)

**Total Approval Timeline:** 15 business days

**Post-Approval Actions:**
1. Extract gap remediation list from Sheets 2-5
2. Create project tickets for each gap
3. Track progress in project management system
4. Report coverage metrics monthly to management
5. Schedule next quarterly review (90 days)

---

**END OF USER GUIDE**

---

*"Blind spots in monitoring are open doors to attackers."*
— Anon

<!-- QA_VERIFIED: 2026-03-01 -->
