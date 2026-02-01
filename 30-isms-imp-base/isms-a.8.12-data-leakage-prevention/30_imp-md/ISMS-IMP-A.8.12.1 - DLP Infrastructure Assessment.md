**ISMS-IMP-A.8.12.1 - DLP Infrastructure Assessment**
**Assessment Specification with User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.12: Data Leakage Prevention

# PART I: USER COMPLETION GUIDE

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.12.1 |
| **Version** | 1.0 |
| **Assessment Area** | DLP Infrastructure and Technology Deployment |
| **Related Policy** | ISMS-POL-A.8.12 (Data Leakage Prevention Policy) |
| **Purpose** | Assess implementation of DLP technologies across network, endpoint, email, cloud, web, and database channels to verify coverage, capability maturity, and integration effectiveness |
| **Target Audience** | DLP Administrators, Security Engineers, IT Infrastructure Teams, SOC Analysts, CISO, Compliance Officers |
| **Assessment Type** | Technical & Operational Infrastructure Review |
| **Review Cycle** | Quarterly or After Major DLP Deployment Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial specification for DLP Infrastructure assessment | ISMS Implementation Team |

---

# PART I: USER COMPLETION GUIDE
**Audience:** DLP Administrators, Security Engineers, IT Infrastructure Teams, SOC Analysts

---

# Assessment Overview

## What This Assessment Measures

This assessment evaluates [Organization]'s **DLP technology infrastructure** to ensure compliance with ISO/IEC 27001:2022 Control A.8.12 and applicable regulatory requirements.

**Scope:** 6 DLP technology domains covering all data egress channels:
1. **DLP Technology Inventory** - Complete catalog of all deployed DLP solutions
2. **Network DLP** - Inline/TAP appliances, protocols inspected, SSL/TLS inspection
3. **Endpoint DLP** - Agent deployment coverage, OS support, offline capability
4. **Email DLP** - Gateway integration, cloud email DLP, content inspection
5. **Cloud & CASB DLP** - SaaS monitoring, cloud storage protection, API-based DLP
6. **Web & Database DLP** - Proxy integration, database activity monitoring

**Assessment Output:** Excel workbook with ~80 infrastructure checkpoints documenting current DLP deployment architecture, coverage gaps, integration status, and vendor lifecycle management.

## Why This Matters

**ISO 27001:2022 Control A.8.12 Requirement:**
> *"Data leakage prevention measures should be applied to systems, networks and any other devices that process, store or transmit sensitive information."*

**Regulatory Context:**

- **Swiss nDSG (Art. 26):** Requires appropriate technical measures to prevent unauthorized data disclosure
- **EU GDPR (Art. 32):** Mandates technical measures to ensure security of personal data processing
- **Industry Standards:** PCI DSS (Req. 3, 4), HIPAA Security Rule, SOC 2 all require data exfiltration protection


**Business Impact:**

- **Data Breaches:** 60% of breaches involve data exfiltration that DLP could prevent (Verizon DBIR)
- **Compliance Violations:** Inadequate DLP = demonstrable failure to implement technical safeguards
- **Insider Threats:** DLP is primary defense against malicious and negligent insider data theft
- **Operational Risk:** DLP infrastructure gaps create blind spots for data exfiltration


**Why Infrastructure Assessment Matters:**

- **Coverage Verification:** Do we actually protect all egress channels or just some?
- **Capability Assessment:** Can our DLP detect modern exfiltration techniques (encrypted channels, cloud storage, API abuse)?
- **Integration Validation:** Is DLP isolated or integrated with SIEM, SOC, IAM for effective response?
- **Lifecycle Management:** Are DLP solutions current, supported, or approaching end-of-life?


## Who Should Complete This Assessment

**Primary Responsibility:** DLP Administrators, Security Engineers, IT Infrastructure Teams

**Required Knowledge:**

- [Organization]'s DLP technology stack (vendors, versions, deployment models)
- Network architecture and data flow paths (where DLP sensors are deployed)
- Integration points with security ecosystem (SIEM, SOC, IAM, ticketing)
- Licensing and vendor support status for all DLP solutions


**Support Roles:**

- **Network Engineers:** Network DLP appliance configurations, traffic routing, SSL inspection
- **Endpoint Teams:** Endpoint agent deployment status, OS coverage, VDI integration
- **Email Administrators:** Email gateway DLP, cloud email protection (M365 Purview, Google Workspace DLP)
- **Cloud/SaaS Teams:** CASB deployment, cloud DLP configurations, API-based monitoring
- **Database Administrators:** Database Activity Monitoring (DAM) integration, query logging
- **Procurement/Vendor Management:** License expiry dates, support contracts, end-of-life schedules


## Time Estimate

**Total Assessment Time:** 4-6 hours (depending on DLP infrastructure complexity)

**Breakdown:**

- **Information Gathering:** 1-2 hours (inventory all DLP technologies, collect architecture diagrams, review licensing)
- **Assessment Completion:** 2-3 hours (complete all 6 domain sheets, verify configurations)
- **Evidence Collection:** 30-60 minutes (screenshots, configuration exports, architecture diagrams)
- **Quality Review:** 30-60 minutes (self-check using Section 7 quality checklist)


**Pro Tip:** For organizations with complex multi-vendor DLP environments (>5 different DLP products), consider splitting assessment across multiple team members:

- Network Engineer: Network DLP sheet
- Endpoint Team: Endpoint DLP sheet
- Email Admin: Email DLP sheet
- Cloud Team: Cloud/CASB DLP sheet
- Database Team: Database DAM sheet
- DLP Admin: Technology Inventory + consolidation


**Coordination:** If split across teams, designate one DLP Administrator as coordinator to consolidate and ensure consistency.

## Connection to Policy

This assessment implements **ISMS-POL-A.8.12 (Data Leakage Prevention Policy)** Section 2.2 (Channel Protection Requirements) which mandates:

**Policy Requirements Verified by This Assessment:**

- **Section 2.2 - Channel Protection:** DLP controls deployed across all data egress channels (email, web, endpoint, network, cloud, mobile)
- **Section 3.1 - Roles & Responsibilities:** Security Team accountable for DLP deployment and maintenance
- **Section 3.2 - Assessment & Verification:** Quarterly infrastructure review for coverage gaps and capability maturity
- **Section 4.2 - Implementation Resources:** Use of structured assessment workbooks (this document) for evidence-based compliance


**Policy Authority:** Chief Information Security Officer (CISO)  
**Compliance Status:** Mandatory for all systems processing Internal, Confidential, or Restricted data

**Relationship to Other Assessments:**

- **A.8.12.2 (Data Classification):** Defines WHAT data to protect → THIS assessment verifies WHERE DLP is deployed to protect it
- **A.8.12.3 (Channel Coverage):** Verifies policy configurations → THIS assessment verifies technical infrastructure exists
- **A.8.12.4 (Monitoring & Response):** Assesses alerting effectiveness → THIS assessment verifies DLP solutions can generate alerts
- **A.8.12.5 (Compliance Dashboard):** Consolidates all assessments → THIS assessment provides infrastructure compliance metrics


## Critical: DLP Technology Lifecycle Management

**⚠️ IMPORTANT - Vendor End-of-Life (EOL) Tracking:**

DLP solutions approaching vendor end-of-life create significant security and compliance risks:

**EOL Risk Categories:**

| Status | Risk Level | Action Required |
|--------|-----------|------------------|
| **Current & Supported** | Low | Continue normal operations, maintain support contracts |
| **Approaching EOL (<12 months)** | Medium | **Migration planning required**, identify replacement, budget approval |
| **EOL but extended support available** | High | **Evaluate extended support cost vs. migration**, document risk acceptance |
| **EOL with no support** | **Critical** | **Immediate migration required**, cannot demonstrate control effectiveness |

**Common DLP Vendor EOL Examples:**

- Symantec DLP (acquired by Broadcom) - Complex licensing, support model changes
- McAfee DLP (now Trellix) - Rebranding, product roadmap changes
- Forcepoint DLP - Ownership changes, product strategy shifts
- Legacy on-premise solutions → Cloud migration pressure


**What This Means for Your Assessment:**
1. **Document all DLP product versions** - Not just "Forcepoint DLP" but "Forcepoint DLP v9.1.2"
2. **Check vendor EOL schedules** - Visit vendor websites, review support portals, contact account managers
3. **Verify support contract status** - Active support = patches, updates, technical assistance
4. **If approaching EOL:** Create remediation plan with migration timeline (typically 6-12 months for DLP migration)
5. **If past EOL with no support:** Escalate to CISO immediately - this is a **critical compliance gap**

**Evidence to Collect:**

- Vendor support contract documentation
- EOL announcement emails or vendor communications
- Migration plan (if EOL approaching)
- Risk acceptance documentation (if extended EOL operation approved by CISO)


---

# Prerequisites

## Access Required

Before starting this assessment, ensure you have access to:

**Infrastructure Documentation:**

- [ ] Network architecture diagrams (showing DLP appliance placement, traffic flows)
- [ ] DLP deployment architecture diagrams (inline vs. TAP, coverage maps)
- [ ] Data flow diagrams (egress points, internet gateways, cloud connections)
- [ ] Configuration Management Database (CMDB) or asset inventory (DLP systems registered)


**System Access:**

- [ ] DLP management console(s) (Forcepoint, Symantec, Microsoft Purview, etc.)
- [ ] Network DLP appliance administration (web GUI, SSH/CLI access)
- [ ] Endpoint DLP management console (agent deployment status, policy distribution)
- [ ] Email gateway administration (DLP integration, content inspection rules)
- [ ] CASB administration portal (cloud DLP policies, SaaS monitoring)
- [ ] Web proxy administration (DLP integration, SSL inspection configuration)
- [ ] Database Activity Monitoring console (if deployed)
- [ ] SIEM access (to verify DLP log integration, alert routing)


**Documentation Systems:**

- [ ] Policy repository (access to ISMS-POL-A.8.12)
- [ ] Licensing and vendor contract repository (support contracts, license counts, expiry dates)
- [ ] Change management records (recent DLP deployments, upgrades, configuration changes)
- [ ] Incident response records (DLP-related incidents, false positive tracking)


**Vendor Portals:**

- [ ] DLP vendor support portals (for EOL lookups, version currency checks)
- [ ] Cloud provider consoles (AWS, Azure, GCP for cloud-native DLP features)
- [ ] SaaS admin portals (M365 Admin Center, Google Workspace Admin for cloud email DLP)


## Knowledge Required

**Essential Understanding:**

- [Organization]'s DLP technology stack (what vendors/products are deployed where)
- Network topology and egress points (where data can leave the organization)
- Endpoint operating system landscape (Windows, macOS, Linux coverage requirements)
- Cloud services inventory (which SaaS applications require DLP monitoring)
- Integration architecture (how DLP connects to SIEM, SOC, ticketing, IAM)


**Technical Skills:**

- Ability to navigate DLP management consoles and interpret deployment status
- Understanding of network protocols and traffic routing (for network DLP assessment)
- Basic command-line skills (for checking endpoint agent status, log verification)
- Familiarity with licensing models (named user, device-based, data volume-based)


**NOT Required:**

- DLP rule/policy configuration expertise (covered in A.8.12.3 Channel Coverage Assessment)
- Deep packet inspection analysis
- Custom rule development or regex pattern creation
- DLP incident investigation (covered in A.8.12.4 Monitoring & Response Assessment)


## Tools Needed

**Data Collection Tools:**

- **DLP Management Console:** Primary source for deployment status, agent counts, version information
- **Network Scanning:** nmap or similar for verifying DLP appliance presence on network
- **Endpoint Inventory:** Endpoint management console (SCCM, Jamf, etc.) for agent deployment verification
- **SIEM Query Access:** To verify DLP log integration and volume


**Evidence Collection:**

- **Screenshot tool:** For capturing DLP console dashboards, deployment status, version info
- **Export capability:** For DLP inventory exports, license reports, configuration summaries
- **Diagram tool:** For documenting DLP architecture (if diagrams don't exist or need updating)


**Optional but Recommended:**

- **License management tool:** For tracking DLP license expiry, renewal dates
- **Vulnerability scanner:** To check DLP appliance patch status, known CVEs
- **Network traffic analyzer:** For verifying SSL/TLS inspection functionality


## Estimated Time Commitment

**Phase 1: Information Gathering (1-2 hours)**

- Access all DLP management consoles and collect deployment statistics
- Export DLP technology inventory (products, versions, deployment models)
- Review network diagrams to identify DLP appliance locations
- Collect licensing and support contract documentation
- Check vendor EOL schedules for all DLP products


**Phase 2: Technical Verification (1-2 hours)**

- Verify network DLP appliance operational status (inline mode, traffic volume, utilization)
- Check endpoint DLP agent deployment coverage (% of endpoints protected)
- Test email DLP integration (send test email, verify inspection)
- Review cloud CASB deployment status (connected SaaS apps, policy enforcement)
- Verify SIEM integration (DLP logs flowing, alert correlation working)


**Phase 3: Assessment Completion (1-2 hours)**

- Complete all 6 domain sheets in workbook (Technology Inventory, Network DLP, Endpoint DLP, Email DLP, Cloud/CASB DLP, Web/Database DLP)
- Assign status values (✅ Compliant / ⚠️ Partial / ❌ Non-Compliant) for each infrastructure item
- Document gaps and create remediation plans
- Collect evidence files (screenshots, exports, diagrams)
- Populate Evidence Register


**Phase 4: Quality Review (30-60 minutes)**

- Self-check using Quality Checklist (Section 7)
- Verify all mandatory fields completed (no blanks in Status columns)
- Review Summary Dashboard (compliance percentage calculated, gaps identified)
- Ensure remediation plans exist for all non-compliant items


**Total:** 4-6 hours for comprehensive infrastructure assessment

---

# Assessment Workflow

## Recommended Completion Sequence

**STEP 1: Initial Setup (10 minutes)**
1. Open assessment workbook: `ISMS-IMP-A.8.12.1_DLP_Infrastructure_Assessment_YYYYMMDD.xlsx`
2. Navigate to **Instructions_Legend** sheet - review response values and color coding
3. Complete **Organization Metadata** section (yellow cells):

   - Assessment Date: DD.MM.YYYY
   - Completed By: [Your Name]
   - Organization Name: [Organization]
   - Review Cycle: Quarterly


**STEP 2: DLP Technology Inventory (30-45 minutes)**
1. Navigate to **DLP_Technology_Inventory** sheet
2. Access all DLP management consoles and collect:

   - Technology names (vendor + product)
   - Deployment types (Network/Endpoint/Cloud/Email/Web/Database)
   - Versions (critical for EOL checking)
   - Deployment status (Production/Staging/Test/Decommissioned)
   - License information (type, expiry date, support contract status)

3. Complete one row per DLP technology
4. **Critical:** Document ALL DLP solutions, even decommissioned ones (audit trail)
5. Collect evidence: DLP console screenshots showing technology inventory

**STEP 3: Network DLP Assessment (30-45 minutes)**
1. Navigate to **Network_DLP** sheet
2. For each network DLP appliance:

   - Identify deployment mode (Inline/TAP/SPAN/Cloud Gateway)
   - List network segments covered (DMZ, Internal, Branch Offices)
   - Document protocols inspected (HTTP, HTTPS, SMTP, FTP, etc.)
   - Verify SSL/TLS inspection status
   - Check throughput capacity and current utilization
   - Assess technical capabilities (content inspection, pattern matching, fingerprinting, ML/AI)

3. Status determination (see Section 4.3 for rules)
4. Collect evidence: Network architecture diagram, DLP appliance configuration screenshot

**STEP 4: Endpoint DLP Assessment (30-45 minutes)**
1. Navigate to **Endpoint_DLP** sheet
2. For each endpoint DLP solution:

   - Document operating systems supported (Windows, macOS, Linux, VDI)
   - Calculate deployment coverage (% of endpoints with agent installed)
   - Verify offline protection capability
   - Check agent update mechanism (automatic, manual)
   - Assess channel coverage (USB, clipboard, print, screen capture, file operations)

3. Status determination (see Section 4.4 for rules)
4. Collect evidence: Endpoint management console screenshot showing agent deployment rate

**STEP 5: Email DLP Assessment (30 minutes)**
1. Navigate to **Email_DLP** sheet
2. Document email DLP architecture:

   - Email system (Exchange, M365, Google Workspace, etc.)
   - DLP integration point (gateway, cloud service, API-based)
   - Content inspection capabilities
   - Attachment scanning (file types, size limits)

3. Test email DLP (send test email with sensitive content pattern, verify detection)
4. Status determination (see Section 4.5 for rules)
5. Collect evidence: Email DLP policy screenshot, test email block notification

**STEP 6: Cloud & CASB DLP Assessment (30 minutes)**
1. Navigate to **Cloud_CASB_DLP** sheet
2. For Cloud Access Security Broker (CASB) or cloud-native DLP:

   - List connected SaaS applications (M365, Google Workspace, Salesforce, Dropbox, etc.)
   - Document DLP deployment model (API-based, proxy-based, inline)
   - Verify data classification integration
   - Check policy enforcement status (monitor vs. block)

3. Status determination (see Section 4.6 for rules)
4. Collect evidence: CASB dashboard screenshot, connected apps list

**STEP 7: Web & Database DLP Assessment (30 minutes)**
1. Navigate to **Web_DLP** sheet (if web proxy DLP deployed)

   - Document web proxy integration
   - Verify SSL inspection for web uploads
   - Check cloud storage blocking (personal Dropbox, Google Drive, etc.)

2. Navigate to **Database_DAM** sheet (if database activity monitoring deployed)

   - Document database systems covered
   - Verify query logging and data export detection
   - Check alerting for bulk data extracts

3. Status determination (see Section 4.7 for rules)
4. Collect evidence: Proxy configuration, DAM policy screenshot

**STEP 8: Gap Analysis & Remediation Planning (30 minutes)**
1. Navigate to **Gap_Analysis** sheet
2. For each item marked ❌ Non-Compliant or ⚠️ Partial:

   - Describe the gap (what's missing or inadequate)
   - Assess risk level (Critical/High/Medium/Low)
   - Define remediation action (what needs to be done)
   - Assign ownership (who will fix it)
   - Set target date (when will it be fixed)

3. Prioritize gaps: Critical first, then High, Medium, Low

**STEP 9: Evidence Register & Final Review (15 minutes)**
1. Navigate to **Evidence_Register** sheet
2. Document all evidence collected:

   - Evidence ID (auto-generated: A812-1-INF-001, A812-1-INF-002, etc.)
   - Evidence Type (Screenshot, Configuration Export, Architecture Diagram, Test Result)
   - Evidence Description (what it shows)
   - File Location (where evidence file is stored)

3. Review **Summary_Dashboard** sheet:

   - Verify compliance percentage calculated correctly
   - Check critical gaps highlighted
   - Ensure KPIs populated


**STEP 10: Quality Check & Approval (15 minutes)**
1. Complete Quality Checklist (Section 7) - self-review
2. Navigate to **Approval_Sign-Off** sheet
3. Complete approval workflow (Section 8)
4. Save final workbook with completion date in filename

---

# Sheet-by-Sheet Guidance

## Sheet: DLP_Technology_Inventory

**Assessment Question:** *"What DLP technologies are currently deployed in your organization?"*

**How to Answer:**

- **Complete inventory:** List ALL DLP solutions, even if overlapping functionality (e.g., M365 Purview DLP + separate email gateway DLP)
- **Include decommissioned systems:** Document systems being phased out (audit trail, shows intentional decommissioning vs. forgotten systems)
- **One row per technology:** If you have Forcepoint Network DLP + Forcepoint Endpoint DLP, that's TWO rows (different deployment types)


**Field Guidance:**

| Field | How to Complete | Examples | Where to Find |
|-------|-----------------|----------|---------------|
| **Technology ID** | Unique identifier (your naming convention) | "DLP-001", "DLP-NFW-01", "DLP-EPT-01" | Create systematically |
| **Technology Name** | Vendor + Product | "Forcepoint DLP", "Microsoft Purview DLP", "Symantec DLP", "Netskope CASB" | DLP admin console, license docs |
| **Deployment Type** | Primary use case | Network/Endpoint/Cloud/Email/Web/Database | DLP architecture diagram |
| **Vendor** | Manufacturer | "Forcepoint", "Microsoft", "Broadcom (Symantec)", "Netskope" | License agreement |
| **Version** | Specific version | "9.1.2", "v8.15.1", "Cloud (SaaS - auto-updated)" | DLP console About/Help, CLI command |
| **Deployment Architecture** | How it's deployed | Inline/Monitor/Hybrid/Cloud-based | Network diagram, DLP docs |
| **Deployment Status** | Current state | Production/Staging/Test/Decommissioned | DLP console, system status |
| **License Type** | Licensing model | Perpetual/Subscription/Open Source | License agreement |
| **License Expiry** | Expiration date | DD.MM.YYYY | License portal, vendor email |
| **Support Contract** | Support status | Active/Expired/N/A | Vendor support portal |
| **EOL Date** | Vendor end-of-life date | DD.MM.YYYY or "Not announced" | Vendor EOL schedule website |
| **Primary Use Case** | Main purpose | "Email DLP", "USB blocking", "Cloud storage monitoring" | DLP deployment plan |
| **Integration Status** | SIEM/SOC integration | Integrated/Standalone/Partial | SIEM logs, SOC playbooks |
| **SIEM Integration** | Logs sent to SIEM | Yes/No/Partial/Planned/N/A | SIEM data source config |
| **SOC Integration** | SOC monitors DLP alerts | Yes/No/Partial/Planned/N/A | SOC runbooks, alert routing |
| **Evidence ID** | Evidence reference | A812-1-INF-001 | Create sequentially, link to Evidence Register |

**Status Determination:**

**✅ Compliant (Green):**

- Technology deployed in production with active support contract
- Version current (not EOL or approaching EOL <6 months)
- Integrated with SIEM for log aggregation
- SOC monitors DLP alerts
- License valid (>6 months until expiry)


**⚠️ Partial (Yellow):**

- Technology deployed but approaching EOL (6-12 months)
- Support contract active but license expiring soon (<6 months)
- SIEM integration partial (some logs sent, not all)
- SOC integration planned but not yet operational
- Technology in production but standalone (no integration)


**❌ Non-Compliant (Red):**

- Technology past vendor EOL with no support
- License expired
- Production technology with no SIEM integration (blind spot for security monitoring)
- No SOC monitoring (DLP alerts not acted upon)
- Decommissioned technology still processing production data (should be migrated off)


**N/A (Gray):**

- Test/staging environments (not subject to full requirements)
- Intentionally decommissioned systems documented as part of migration plan


**Compliance Checklist Guidance:**

- [ ] **Complete DLP technology inventory maintained**  

  *What this means:* Every DLP product deployed is documented  
  *How to verify:* Cross-check with asset inventory, procurement records, CMDB  
  *Common gap:* Shadow DLP deployments (department-level tools not centrally managed)

- [ ] **All production DLP technologies have active support contracts**  

  *Critical importance:* No support = no security patches = vulnerability exposure  
  *How to verify:* Check vendor support portal, confirm renewal dates  
  *Escalation:* If support expired, escalate to CISO immediately

- [ ] **DLP technologies integrated with SIEM for centralized logging**  

  *Why this matters:* DLP logs in isolation = no correlation with other security events  
  *How to verify:* SIEM query for DLP logs, confirm volume matches expected  
  *Target state:* 100% of production DLP solutions sending logs to SIEM

- [ ] **SOC monitors DLP alerts and has documented response procedures**  

  *Why this matters:* DLP without monitoring = useless (alerts ignored)  
  *How to verify:* Review SOC runbooks for DLP incident response  
  *Common gap:* DLP deployed but SOC not trained on alert handling

- [ ] **EOL tracking process in place for all DLP technologies**  

  *Best practice:* Proactive EOL management prevents last-minute migrations  
  *How to verify:* Quarterly review of vendor EOL schedules  
  *Trigger:* If EOL <12 months, migration plan must exist

**Evidence Examples:**

- Technology inventory export from DLP console: `EV-1.1-DLP-Inventory-20260119.xlsx`
- DLP architecture diagram showing all deployed solutions: `EV-1.1-DLP-Architecture-20260119.pdf`
- License agreement and support contract: `EV-1.1-License-Forcepoint-20260119.pdf`
- SIEM log volume report showing DLP integration: `EV-1.1-SIEM-DLP-Logs-20260119.png`
- Vendor EOL schedule screenshot: `EV-1.1-Vendor-EOL-Schedule-20260119.pdf`


---

## Sheet: Network_DLP

**Assessment Question:** *"Does your organization deploy network-based DLP appliances for traffic inspection?"*

**How to Answer:**

- **"Yes":** If you have dedicated network DLP appliances (inline, TAP, SPAN mode) inspecting traffic
- **"No":** If all DLP is cloud-based, endpoint-only, or email-gateway-only (no network appliances)
- **"Partial":** If network DLP deployed but only covers some network segments (e.g., DMZ only, not internal)


**Understanding the Requirement:**

**Network DLP Purpose:**

- Inspect data in transit across network (HTTP, HTTPS, FTP, SMTP, custom protocols)
- Detect exfiltration attempts regardless of endpoint protection status
- Catch unmanaged devices (BYOD, contractor laptops, IoT) that lack endpoint agents
- Provide network-level visibility for cloud services, webmail, file uploads


**Deployment Models:**

| Mode | Description | Pros | Cons | When to Use |
|------|-------------|------|------|-------------|
| **Inline** | DLP appliance in network path (active blocking) | Can block in real-time, enforce policy | Single point of failure risk, latency impact | High-security environments, policy enforcement critical |
| **TAP/SPAN** | Passive monitoring (copy of traffic) | No impact on network performance | Cannot block (detect only) | Initial deployment, large traffic volumes |
| **Hybrid** | Inline for critical segments, TAP for others | Balanced approach | Complex architecture | Mature DLP programs |
| **Cloud Gateway** | Cloud-based DLP service (tunnel traffic to cloud) | No on-premise hardware, automatic updates | Latency, dependency on cloud | Distributed organizations, remote workforce |

**Field Guidance:**

| Field | How to Complete | Examples | Where to Find |
|-------|-----------------|----------|---------------|
| **Appliance Name** | Descriptive name | "HQ-DLP-01", "Branch-DLP-Gateway", "Forcepoint-DMZ" | Network diagram, hostname |
| **Deployment Mode** | How traffic reaches DLP | Inline/TAP/SPAN/Cloud Gateway | Network diagram, DLP config |
| **Network Segments Covered** | What parts of network | "DMZ", "Internal Corporate", "Branch Offices", "Guest Network" | Network topology, VLAN documentation |
| **Protocols Inspected** | What traffic is analyzed | "HTTP, HTTPS, SMTP, FTP, FTPS" | DLP policy configuration |
| **SSL/TLS Inspection** | Decrypt HTTPS traffic | Yes/No/Partial/Planned/N/A | DLP SSL inspection config |
| **Throughput Capacity** | Maximum traffic volume | "10 Gbps", "5 Gbps", "1 Gbps" | Appliance specs, vendor datasheet |
| **Current Utilization %** | How much capacity used | "45%", "80%", "25%" | DLP console performance metrics |
| **Content Inspection** | Deep packet inspection | Yes/No/Partial/Planned/N/A | DLP capabilities test |
| **Pattern Matching (Regex)** | Regex pattern detection | Yes/No/Partial/Planned/N/A | DLP rule configuration |
| **Fingerprinting** | Document fingerprinting | Yes/No/Partial/Planned/N/A | DLP capabilities, test with fingerprinted file |
| **Machine Learning/AI** | AI-based detection | Yes/No/Partial/Planned/N/A | Vendor documentation, enabled features |
| **Blocking Capability** | Can block traffic | Yes/No/Partial/Planned/N/A | Deployment mode (inline = yes, TAP = no) |
| **High Availability** | Redundant appliances | Yes/No/N/A | HA configuration, failover testing |
| **Evidence ID** | Evidence reference | A812-1-NET-001 | Create sequentially |

**Status Determination:**

**✅ Compliant (Green):**

- Network DLP deployed in production covering all critical egress points
- Inline mode (can block) OR TAP mode with documented risk acceptance
- SSL/TLS inspection enabled for HTTPS traffic
- Protocols covering HTTP, HTTPS, SMTP, FTP minimum
- Content inspection, pattern matching, fingerprinting all operational
- Throughput capacity sufficient (utilization <70%)
- High availability configured (redundant appliances)
- SIEM integration confirmed


**⚠️ Partial (Yellow):**

- Network DLP deployed but only covers some segments (e.g., DMZ only, not internal)
- SSL/TLS inspection partial (some traffic decrypted, not all - certificate issues, exceptions)
- TAP/SPAN mode without plan to move to inline (acceptable short-term)
- Throughput utilization high (>70%) - performance risk
- No HA configuration (single point of failure)
- Some advanced features disabled (ML/AI, fingerprinting not enabled)


**❌ Non-Compliant (Red):**

- No network DLP deployed (all egress points unmonitored at network level)
- Network DLP deployed but not operational (appliance installed but not configured, bypass mode)
- SSL/TLS inspection disabled (HTTPS traffic = blind spot, majority of modern traffic)
- Throughput capacity exceeded (utilization >90% = dropped traffic, blind spots)
- Network DLP appliance EOL with no migration plan


**N/A (Gray):**

- [Organization] made risk-based decision not to deploy network DLP (e.g., small organization, all endpoint-based DLP)
- Requires CISO risk acceptance documentation


**Compliance Checklist Guidance:**

- [ ] **Network DLP appliances deployed at all internet egress points**  

  *What are egress points:* Internet gateway, DMZ connections, cloud connections, VPN concentrators  
  *How to verify:* Network topology review, trace all paths to internet  
  *Common gap:* Branch offices with direct internet access bypassing central DLP

- [ ] **SSL/TLS inspection enabled for encrypted traffic**  

  *Critical:* 90%+ of web traffic is HTTPS - without SSL inspection, DLP is blind  
  *How to verify:* Test with HTTPS file upload to cloud storage, verify DLP detection  
  *Common issue:* Certificate pinning, certificate trust issues prevent SSL inspection  
  *Workaround:* Deploy enterprise CA certificates to endpoints

- [ ] **Content inspection capabilities enabled (pattern matching, fingerprinting, ML/AI)**  

  *Why all three matter:*  

    - Pattern matching: Detects credit cards, SSNs, regex patterns  
    - Fingerprinting: Detects specific documents even if content modified  
    - ML/AI: Detects sensitive data without predefined patterns (context-aware)  

  *How to verify:* Test each capability with sample data

- [ ] **Network DLP integrated with SIEM for alert correlation**  

  *Why this matters:* Network DLP alert + endpoint alert + user behavior = higher confidence incident  
  *How to verify:* SIEM query for network DLP events, confirm correlation rules exist

- [ ] **High availability configuration tested and documented**  

  *Best practice:* HA for inline DLP (failover prevents network outage if appliance fails)  
  *How to verify:* Failover test (disable primary appliance, verify secondary takes over)  
  *Test frequency:* Semi-annually minimum

**Evidence Examples:**

- Network architecture diagram showing DLP placement: `EV-1.2-Network-Architecture-DLP-20260119.pdf`
- DLP appliance configuration screenshot (protocols, SSL inspection): `EV-1.2-DLP-Config-20260119.png`
- Throughput utilization graph: `EV-1.2-Throughput-Utilization-20260119.png`
- SSL inspection test results (test file upload blocked): `EV-1.2-SSL-Inspection-Test-20260119.pdf`
- HA configuration and failover test results: `EV-1.2-HA-Config-20260119.pdf`


---

## Sheet: Endpoint_DLP

**Assessment Question:** *"Does your organization deploy endpoint DLP agents on workstations and mobile devices?"*

**How to Answer:**

- **"Yes":** If endpoint DLP agents deployed on organizational devices (Windows, macOS, Linux, mobile)
- **"No":** If no endpoint-level DLP (relying entirely on network/email/cloud DLP)
- **Partial":** If endpoint DLP deployed but incomplete coverage (<90% of endpoints)


**Understanding the Requirement:**

**Endpoint DLP Purpose:**

- Monitor and control data transfers at the device level (USB, clipboard, print, screen capture, local file operations)
- Protect data when endpoint is off-network (remote workers, traveling employees, offline scenarios)
- Detect shadow IT and unapproved cloud storage usage
- Provide last line of defense if network DLP bypassed


**Why Endpoint DLP Matters:**

- **Remote Work Era:** Network DLP ineffective when employees work from home on VPN or direct internet
- **BYOD/Mobile:** Corporate data on personal devices requires endpoint-level protection
- **Insider Threats:** Malicious insiders specifically target endpoint channels (USB exfiltration, print to PDF)
- **Coverage Gaps:** Network DLP blind to encrypted traffic, local file operations, clipboard transfers


**Field Guidance:**

| Field | How to Complete | Examples | Where to Find |
|-------|-----------------|----------|---------------|
| **Endpoint Solution Name** | Product name | "Forcepoint Endpoint DLP", "Microsoft Purview Endpoint DLP", "Symantec Endpoint DLP" | DLP console |
| **Operating Systems Supported** | What OS | "Windows 10/11", "macOS 12+", "Linux (Ubuntu, RHEL)", "iOS", "Android" | Vendor documentation |
| **Total Endpoints** | Organization endpoint count | "1500", "5000", "250" | Asset inventory, endpoint management console |
| **Agents Deployed** | How many have agents | "1350", "4750", "230" | DLP console agent count |
| **Deployment Coverage %** | Percentage protected | "90%", "95%", "92%" | (Agents Deployed / Total Endpoints) × 100 |
| **Offline Protection** | Works when off-network | Yes/No/Partial/Planned/N/A | Test agent offline, DLP docs |
| **Agent Update Mechanism** | How agents update | Automatic/Manual/Scheduled | DLP agent configuration |
| **Channels Monitored** | What's protected | USB, Clipboard, Print, Screen Capture, File Operations, Network Shares | DLP policy configuration |
| **USB Blocking** | Removable media control | Block/Monitor/Allow with justification/N/A | DLP USB policy |
| **Cloud App Detection** | Shadow IT detection | Yes/No/Partial/Planned/N/A | Test with Dropbox/Google Drive upload |
| **Application Control** | Limit data transfer to specific apps | Yes/No/Partial/Planned/N/A | DLP application whitelist/blacklist |
| **Evidence ID** | Evidence reference | A812-1-EPT-001 | Create sequentially |

**Status Determination:**

**✅ Compliant (Green):**

- Endpoint DLP agents deployed on ≥95% of organizational endpoints
- All primary OS platforms covered (Windows, macOS minimum)
- Offline protection operational (agent works when off-network)
- Automatic agent updates configured
- All critical channels monitored (USB, clipboard, print, screen capture, file operations)
- USB blocking or monitor-with-justification policy enforced
- Cloud app detection enabled (detects shadow IT)
- SIEM integration confirmed


**⚠️ Partial (Yellow):**

- Endpoint DLP coverage 80-94% (most endpoints protected, some gaps)
- Some OS platforms not covered (e.g., Windows/macOS covered, Linux not covered)
- Offline protection partial (some features work offline, not all)
- Manual agent updates (operational risk, agents may become outdated)
- Some channels not monitored (e.g., USB monitored, clipboard not monitored)
- Cloud app detection planned but not yet implemented


**❌ Non-Compliant (Red):**

- Endpoint DLP coverage <80% (significant coverage gaps)
- Critical OS platforms not covered (e.g., macOS executives have no endpoint protection)
- No offline protection (agents only work on corporate network = remote workers unprotected)
- No agent update mechanism (agents never updated = security vulnerabilities, missed detection)
- USB not monitored or blocked (primary insider threat exfiltration vector unprotected)
- No SIEM integration (endpoint alerts isolated)


**N/A (Gray):**

- [Organization] has no endpoints requiring DLP (unlikely - would need risk acceptance)
- Specific OS platforms legitimately not in use (e.g., no Linux endpoints in environment)


**Compliance Checklist Guidance:**

- [ ] **Endpoint DLP agents deployed on ≥95% of organizational endpoints**  

  *Why 95% threshold:* 100% impossible (maintenance windows, new devices), but >95% shows diligent deployment  
  *How to calculate:* (Agents Deployed / Total Endpoints) × 100  
  *Common gaps:* Executive devices, contractor laptops, VDI sessions  
  *Remediation:* Mandatory agent deployment policy, automated installation via endpoint management

- [ ] **Offline protection tested and operational**  

  *Critical for remote workers:* Agent must enforce policy when endpoint is off corporate network  
  *How to test:* Disconnect endpoint from network, attempt USB file transfer, verify block/alert  
  *Common issue:* Agent requires network connectivity to check policy (fails offline)

- [ ] **USB blocking or strict monitoring enforced**  

  *Risk:* USB exfiltration is #1 insider threat method (easy, fast, high capacity)  
  *Policy options:*  

    - Block all USB (most secure, often impractical)  
    - Allow USB with DLP scan (pragmatic, balance security and usability)  
    - Allow USB with justification and logging (monitor mode)  

  *How to verify:* Test with USB drive, verify DLP intercepts transfer

- [ ] **Cloud app detection enabled (shadow IT visibility)**  

  *Why this matters:* Employees use personal Dropbox, Google Drive, WeTransfer to circumvent DLP  
  *How it works:* Endpoint DLP detects uploads to known cloud storage URLs  
  *How to test:* Upload file to personal Dropbox from protected endpoint, verify DLP detection  
  *Limitation:* Cannot block encrypted tunnels (VPN to bypass), requires network DLP cooperation

- [ ] **Automatic agent updates configured and tested**  

  *Operational requirement:* Agents must stay current with latest detection rules, patches  
  *How to verify:* Check DLP console update policy, verify recent agent versions deployed  
  *Test:* Simulate new agent version, verify automatic rollout

**Evidence Examples:**

- Endpoint DLP deployment coverage report: `EV-1.3-Endpoint-Coverage-20260119.xlsx`
- Agent version distribution report: `EV-1.3-Agent-Versions-20260119.png`
- Offline protection test results: `EV-1.3-Offline-Test-20260119.pdf`
- USB blocking test: `EV-1.3-USB-Block-Test-20260119.png`
- Cloud app detection test: `EV-1.3-Cloud-App-Detection-20260119.pdf`


---

# Evidence Collection

## General Evidence Guidelines

**Evidence Naming Convention:**
```
EV-[Domain]-[Category]-[Date].[ext]
```

**Format Breakdown:**

- **EV** = Evidence
- **Domain** = 1 (Infrastructure Assessment)
- **Category** = INF (Inventory), NET (Network), EPT (Endpoint), EML (Email), CLD (Cloud), WEB (Web), DAM (Database)
- **Date** = YYYYMMDD
- **ext** = pdf, png, jpg, xlsx, txt, json (as appropriate)


**Examples:**

- `EV-1-INF-DLP-Inventory-20260119.xlsx` - DLP technology inventory export
- `EV-1-NET-Architecture-20260119.pdf` - Network DLP architecture diagram
- `EV-1-EPT-Coverage-20260119.png` - Endpoint DLP deployment coverage screenshot
- `EV-1-EML-Test-20260119.pdf` - Email DLP blocking test results
- `EV-1-CLD-CASB-Apps-20260119.xlsx` - CASB connected applications list


**Storage Requirements:**

- **Location:** Centralized evidence repository (SharePoint, file share, ISMS document management system, dedicated evidence folder)
- **Folder Structure:** Organize by assessment domain, then by date

  ```
  /Evidence/
    /A.8.12.1_Infrastructure/
      /20260119_Q1_Assessment/
        EV-1-INF-DLP-Inventory-20260119.xlsx
        EV-1-NET-Architecture-20260119.pdf
        ...
  ```

- **Retention:** Audit cycle + 1 year minimum (typically 2 years for ISO 27001 certification cycle)
- **Sensitivity:** Mark evidence files according to data classification
  - DLP configuration exports may contain sensitive patterns (PII regex, trade secret keywords) = **Confidential**
  - Architecture diagrams showing security architecture = **Internal**
  - Sanitize any credentials, private keys, sensitive patterns before storing
- **Access Control:** Restrict to security team, auditors, compliance officers


**Evidence Quality Criteria:**

- **Timestamped:** Must show date/time of collection (screenshot timestamps, report generation dates)
- **Complete:** Full screenshots (not cropped unless sensitive data sanitization required), complete command output
- **Attributable:** Clear which system/service it documents (hostname, IP, URL visible)
- **Verifiable:** Auditor can reproduce the evidence collection process (document commands used, tools used)
- **Protected:** Stored securely, sanitized if contains credentials or sensitive data


## Evidence Types by Section

**Technology Inventory (Sheet 2):**

- DLP management console dashboard screenshot showing all deployed technologies: `EV-1-INF-Console-Dashboard-YYYYMMDD.png`
- Technology inventory export from DLP console: `EV-1-INF-Inventory-Export-YYYYMMDD.xlsx`
- DLP architecture diagram (network placement, integration points): `EV-1-INF-Architecture-YYYYMMDD.pdf`
- License agreements and support contracts: `EV-1-INF-License-[Vendor]-YYYYMMDD.pdf`
- Vendor EOL schedule: `EV-1-INF-EOL-Schedule-YYYYMMDD.pdf`
- SIEM integration verification (query showing DLP logs): `EV-1-INF-SIEM-Integration-YYYYMMDD.png`


**Network DLP (Sheet 3):**

- Network topology diagram showing DLP appliance placement: `EV-1-NET-Topology-YYYYMMDD.pdf`
- DLP appliance configuration screenshot (protocols, SSL inspection): `EV-1-NET-Appliance-Config-YYYYMMDD.png`
- Throughput utilization graph (30-day average): `EV-1-NET-Throughput-YYYYMMDD.png`
- SSL/TLS inspection test results: `EV-1-NET-SSL-Inspection-Test-YYYYMMDD.pdf`
- Protocol coverage test (HTTP, HTTPS, SMTP, FTP): `EV-1-NET-Protocol-Test-YYYYMMDD.txt`
- HA configuration and failover test: `EV-1-NET-HA-Config-YYYYMMDD.pdf`


**Endpoint DLP (Sheet 4):**

- Endpoint DLP deployment coverage report: `EV-1-EPT-Coverage-Report-YYYYMMDD.xlsx`
- Agent version distribution: `EV-1-EPT-Agent-Versions-YYYYMMDD.png`
- Offline protection test (agent disconnected from network): `EV-1-EPT-Offline-Test-YYYYMMDD.pdf`
- USB blocking test result: `EV-1-EPT-USB-Block-Test-YYYYMMDD.png`
- Cloud app detection test (Dropbox/Google Drive upload test): `EV-1-EPT-Cloud-App-Test-YYYYMMDD.pdf`
- Endpoint OS coverage breakdown: `EV-1-EPT-OS-Coverage-YYYYMMDD.xlsx`


**Email DLP (Sheet 5):**

- Email system DLP integration diagram: `EV-1-EML-Integration-Diagram-YYYYMMDD.pdf`
- Email DLP policy configuration screenshot: `EV-1-EML-Policy-Config-YYYYMMDD.png`
- Test email with sensitive content (blocked or quarantined): `EV-1-EML-Test-Email-YYYYMMDD.pdf`
- Email DLP detection rate statistics: `EV-1-EML-Detection-Stats-YYYYMMDD.xlsx`
- Attachment scanning configuration: `EV-1-EML-Attachment-Scan-Config-YYYYMMDD.png`


**Cloud & CASB DLP (Sheet 6):**

- CASB dashboard showing connected SaaS applications: `EV-1-CLD-CASB-Dashboard-YYYYMMDD.png`
- Connected applications list with DLP status: `EV-1-CLD-Connected-Apps-YYYYMMDD.xlsx`
- Cloud DLP policy configuration (M365, Google Workspace): `EV-1-CLD-Policy-Config-YYYYMMDD.png`
- API-based DLP test (file upload to monitored cloud storage): `EV-1-CLD-API-Test-YYYYMMDD.pdf`
- Data classification integration verification: `EV-1-CLD-Classification-Integration-YYYYMMDD.png`


**Web & Database DLP (Sheet 7):**

- Web proxy DLP integration configuration: `EV-1-WEB-Proxy-Config-YYYYMMDD.txt`
- SSL inspection for web uploads test: `EV-1-WEB-SSL-Upload-Test-YYYYMMDD.pdf`
- Cloud storage blocking test (personal Dropbox, Google Drive): `EV-1-WEB-Cloud-Storage-Block-YYYYMMDD.png`
- Database Activity Monitoring configuration: `EV-1-DAM-Config-YYYYMMDD.png`
- Database bulk export detection test: `EV-1-DAM-Bulk-Export-Test-YYYYMMDD.pdf`


---

# Common Pitfalls and How to Avoid Them

## "We have DLP installed, so we're compliant"

**Problem:** DLP technology deployed but not operational (installed but not configured, policies not enabled, alerts not monitored)

**Example:** Network DLP appliance deployed in network but configured in "monitor-only" mode with no one reviewing logs

**Solution:**

- Verify operational status: Check DLP console for active policies, recent alerts
- Test functionality: Send test data matching sensitive patterns, verify detection
- Confirm monitoring: Verify SOC receives and responds to DLP alerts
- Evidence requirement: Operational testing results, not just deployment confirmation


## "Our coverage is 85% - that's pretty good"

**Problem:** Treating 85% endpoint coverage as acceptable, but 15% gap = significant risk

**Reality Check:**

- 15% gap on 1000 endpoints = 150 unprotected devices
- Often, gap includes high-value targets (executives, engineering, finance)
- Insider threats specifically target unprotected devices


**Solution:**

- Set minimum threshold: 95% coverage required
- Identify gap: Which specific endpoints lack agents? Why?
- Prioritize closure: High-value endpoints first (executives, privileged users, sensitive data handlers)
- Document exceptions: If legitimate reason (incompatible OS, specific use case), require CISO approval


## "SSL inspection breaks applications, so we disabled it"

**Problem:** SSL/TLS inspection disabled due to compatibility issues, creating massive blind spot (90%+ of traffic is HTTPS)

**Why This Happens:**

- Certificate pinning in mobile apps (app rejects enterprise CA certificate)
- Application compatibility issues (legacy apps, VPN clients, health monitoring tools)
- Performance impact (SSL decryption adds latency)


**Solution:**

- Default: SSL inspection enabled
- Exceptions: Maintain whitelist of applications requiring SSL inspection bypass (banking apps, healthcare apps, specific business applications)
- Document risk: For each exception, document what sensitive data could be exfiltrated without detection
- Compensating controls: If SSL inspection disabled for channel, require endpoint DLP coverage
- Periodic review: Quarterly review of SSL inspection exceptions, work with vendors to resolve compatibility


## "We monitor DLP alerts, but don't have time to investigate them all"

**Problem:** High false positive rate causing alert fatigue, legitimate incidents missed in noise

**Root Causes:**

- Overly broad DLP rules (too many false positives)
- Insufficient tuning after initial deployment
- No prioritization (all alerts treated equally)
- Lack of automation (manual triage)


**Solution:**

- Tune aggressively: First 90 days post-deployment, dedicate resources to false positive reduction
- Risk-based prioritization: Critical alerts (Restricted data) → immediate response, Medium alerts (Confidential) → investigate within 4 hours, Low alerts (Internal) → weekly review
- Automate triage: Use SIEM correlation, user reputation scoring, context enrichment to auto-dismiss obvious false positives
- Measure effectiveness: Track false positive rate, target <10% false positive rate
- Acceptable false positive rate: 5-10% (balance between over-blocking and under-detecting)


## "Our DLP is cloud-based, so we don't need on-premise appliances"

**Problem:** Assuming cloud-only DLP (M365 Purview, Google Workspace DLP) provides complete coverage

**Reality:**

- Cloud DLP only protects cloud services (M365, Google Workspace)
- Gaps: Personal webmail, personal cloud storage, network file transfers, USB, local file operations
- Unmanaged devices: BYOD accessing corporate cloud data may lack endpoint agents


**Solution:**

- Layered approach: Cloud DLP + Endpoint DLP minimum
- Consider CASB: For monitoring SaaS applications beyond M365/Google (Salesforce, Dropbox, etc.)
- Network DLP: For environments with unmanaged devices (guest networks, contractor access)
- Coverage mapping: Explicitly document which channels are protected by which DLP solution


## "We're planning to deploy DLP next quarter"

**Problem:** "Planned" status for extended periods without actual deployment

**Anti-Pattern:**

- Quarter 1: "Planned"
- Quarter 2: "Planned"  
- Quarter 3: "Planned" (still in vendor evaluation)
- Quarter 4: "Planned" (budget issues)


**Solution:**

- If status = "Planned": Require target date and project plan
- Escalation: If "Planned" for >2 quarters without progress, escalate to CISO for resource prioritization or risk acceptance
- Interim controls: While deploying DLP, implement compensating controls (enhanced monitoring, user training, access restrictions)
- Risk documentation: Document residual risk of operating without DLP until deployment complete


---

# Quality Checklist (Self-Review Before Submission)

**Completeness Check:**

- [ ] All 11 sheets reviewed and completed (Instructions, 6 domain sheets, Gap Analysis, Evidence Register, Summary Dashboard, Approval Sign-Off)
- [ ] No blank mandatory fields (Status columns all have values)
- [ ] Response dropdowns used consistently (no free-text in Status columns)
- [ ] Evidence IDs reference actual evidence files (Evidence Register populated)
- [ ] Compliance percentages calculated and displayed in Summary Dashboard
- [ ] Gap Analysis sheet populated for ALL non-compliant and partial items
- [ ] Each gap has remediation action, owner, and target date


**Accuracy Check:**

- [ ] DLP technology versions verified (not just vendor name, specific version numbers)
- [ ] Endpoint coverage percentage calculated correctly (Agents Deployed ÷ Total Endpoints × 100)
- [ ] License expiry dates accurate (verified from vendor portal, not assumed)
- [ ] EOL dates confirmed from vendor websites or communications
- [ ] Integration status verified through testing (not just assumed based on configuration)
- [ ] Network topology reflects current state (not outdated diagrams)


**Evidence Quality:**

- [ ] Minimum evidence items collected:
  - Technology Inventory: 5 evidence items minimum
  - Network DLP: 4 evidence items minimum (architecture, config, throughput, SSL test)
  - Endpoint DLP: 4 evidence items minimum (coverage, offline test, USB test, cloud app test)
  - Email DLP: 3 evidence items minimum (policy, test email, detection stats)
  - Cloud/CASB DLP: 3 evidence items minimum (connected apps, policy, test)
  - Web/Database DLP: 2 evidence items minimum (config, test)
- [ ] Evidence files follow naming convention (EV-1-[Category]-[Description]-YYYYMMDD.ext)
- [ ] Screenshots timestamped and complete (not cropped unless sanitizing sensitive data)
- [ ] Sensitive data sanitized (credentials, private keys, sensitive regex patterns removed or redacted)
- [ ] Evidence stored in designated repository with proper access controls


**Status Determination Consistency:**

- [ ] Status values assigned using documented decision rules (Section 4)
- [ ] "Compliant" status has supporting evidence (not aspirational)
- [ ] "Partial" status has clear gap description (what's partial)
- [ ] "Non-Compliant" status has remediation plan (not just identification)
- [ ] "N/A" status has justification (why not applicable)


**Gap Analysis Quality:**

- [ ] All gaps prioritized by risk level (Critical/High/Medium/Low)
- [ ] Each gap has clear remediation action (specific, actionable)
- [ ] Ownership assigned to individuals/teams (not vague "IT" or "Security")
- [ ] Target dates realistic (considering resources, dependencies, complexity)
- [ ] Critical gaps have target dates ≤90 days
- [ ] High gaps have target dates ≤180 days


**Summary Dashboard Review:**

- [ ] Overall compliance percentage displayed (automated calculation)
- [ ] Critical gaps count accurate (matches Gap Analysis sheet)
- [ ] KPIs populated:
  - Total DLP technologies deployed
  - SIEM integration rate (% of DLP solutions sending logs to SIEM)
  - Endpoint coverage percentage
  - Average DLP technology age (time since deployment or last major update)
- [ ] Traffic light indicators working (green ≥90%, yellow 70-89%, red <70%)


**Final Checks:**

- [ ] Workbook filename includes date: `ISMS-IMP-A.8.12.1_DLP_Infrastructure_Assessment_YYYYMMDD.xlsx`
- [ ] Organization metadata completed (Assessment Date, Completed By, Organization Name)
- [ ] No example/template rows left in assessment sheets (gray rows deleted or marked clearly)
- [ ] Cell protection enabled (formula cells locked, input cells unlocked)
- [ ] Ready for Security Team review and CISO approval


**Self-Assessment Outcome:**

- [ ] Assessment complete and accurate → Ready for submission
- [ ] Minor corrections needed → Complete before submission
- [ ] Significant gaps identified → Re-assess incomplete areas before submission


---

# Review & Approval Process

## Assessment Metadata

**Assessment Period:** From _____________ to _____________  
**Assessment Date:** _____ . _____ . ___________ (DD.MM.YYYY)  
**Assessment Type:**

- [ ] Initial Baseline Assessment
- [ ] Quarterly Review (Q1 / Q2 / Q3 / Q4)
- [ ] Ad-Hoc Assessment (infrastructure change, incident-driven)
- [ ] Post-Remediation Validation


**Scope Changes Since Last Assessment:**

- [ ] No changes (standard quarterly review)
- [ ] New DLP technology deployed: _______________________
- [ ] DLP technology decommissioned: _______________________
- [ ] Major infrastructure change: _______________________
- [ ] Post-incident reassessment (Incident ID: _______)


## Completed By (Primary Assessor)

**Name:** _______________________  
**Role:** _______________________ (DLP Administrator, Security Engineer, IT Infrastructure Lead)  
**Email:** _______________________  
**Date Completed:** _____ . _____ . ___________ (DD.MM.YYYY)  
**Signature:** _______________________

**Time Invested:**

- Information Gathering: _____ hours
- Assessment Completion: _____ hours
- Evidence Collection: _____ hours
- Quality Review: _____ hours
- **Total: _____ hours**


**Challenges Encountered:**

- [ ] No significant challenges
- [ ] Access limitations (specify): _______________________
- [ ] Data unavailable (specify): _______________________
- [ ] Technical issues (specify): _______________________
- [ ] Other (specify): _______________________


## Reviewed By (Security Team Lead or DLP Manager)

**Name:** _______________________  
**Date:** _____ . _____ . ___________ (DD.MM.YYYY)  
**Signature:** _______________________

**Review Comments:**
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________

**Review Outcome:**

- [ ] Approved - Assessment complete and accurate
- [ ] Approved with minor corrections - Specific items to address: _______________________
- [ ] Requires revision - Significant issues identified, re-submit required


**Key Findings Highlighted:**

- Critical Gaps: _____ (count)
- High-Priority Gaps: _____ (count)
- Overall Compliance Rate: _____% (from Summary Dashboard)


## Approved By (CISO)

**Name:** _______________________  
**Date:** _____ . _____ . ___________ (DD.MM.YYYY)  
**Signature:** _______________________

**Approval Decision:**

- [ ] Approved - Compliance posture acceptable, remediation plans approved
- [ ] Approved with conditions - Remediation must be completed by: _____ . _____ . ___________
- [ ] Rejected - Re-assessment required due to: _______________________


**Risk Acceptance:**

For any documented exceptions/deviations, I accept the residual risk based on:

- [ ] Documented risk assessment completed
- [ ] Approved compensating controls in place
- [ ] Business justification acceptable
- [ ] Compliance with exception approval process (ISMS-POL-A.8.12 Section 3.3)


**Budget Approval (if remediation requires investment):**

Estimated remediation budget requirement: CHF _______________  

- [ ] Approved - Budget allocated from security program
- [ ] Requires further justification - Business case needed
- [ ] Deferred to next budget cycle - Interim risk acceptance documented


**Action Items for Executive Management:**

- [ ] None - Compliance posture acceptable
- [ ] Inform Board of critical gaps and remediation timeline
- [ ] Budget increase required for DLP infrastructure upgrades
- [ ] Policy exception approval required (high-risk acceptance)


## Next Review Date

**Next Scheduled Assessment:** _____ . _____ . ___________ (DD.MM.YYYY)

**Review Cycle:** Quarterly (every 3 months) or upon:

- Major DLP infrastructure changes (new deployment, decommissioning)
- Security incidents involving data exfiltration
- Policy updates (ISMS-POL-A.8.12 revisions)
- Vendor EOL announcements
- Failed audit findings
- Significant coverage gaps identified (requires interim review)


**Interim Monitoring (between formal assessments):**

- DLP technology health monitoring: Continuous (SIEM alerts, performance dashboards)
- Endpoint coverage tracking: Monthly (automated reports from endpoint management)
- License expiry tracking: Monthly (vendor management system)
- EOL schedule review: Quarterly (vendor communications monitoring)
- Remediation progress tracking: Monthly (project management updates)


## Distribution List

This assessment shall be distributed to:

- [ ] Chief Information Security Officer (CISO)
- [ ] Information Security Officer (ISO) / Security Manager
- [ ] DLP Administrator / DLP Program Manager
- [ ] IT Infrastructure Management
- [ ] Network Engineering team
- [ ] Endpoint Management team
- [ ] Email Administration team
- [ ] Cloud/SaaS Administration team
- [ ] SOC (Security Operations Center)
- [ ] Compliance team
- [ ] Internal Audit
- [ ] Data Protection Officer (DPO)
- [ ] Other: _______________________


**Storage Location:**

- **ISMS Repository:** `ISMS/Controls/A.8.12_Data_Leakage_Prevention/Assessments/Infrastructure/`
- **Filename:** `ISMS-IMP-A.8.12.1_DLP_Infrastructure_YYYYMMDD_APPROVED.xlsx`
- **Evidence Folder:** `ISMS/Controls/A.8.12_Data_Leakage_Prevention/Evidence/A.8.12.1_Infrastructure/YYYYMMDD/`


**Access Control:**

- Classification: **Internal** (contains sensitive infrastructure details)
- Access: Restricted to security team, IT management, auditors, compliance officers
- Retention: Audit cycle + 1 year minimum (typically 2 years)


---

**END OF PART I: USER COMPLETION GUIDE**

---

# PART II: TECHNICAL SPECIFICATION
**Audience:** Python Developers, Excel Workbook Developers, Quality Assurance, ISMS Implementation Team

---

# Workbook Structure Overview

## Sheet List

**Total Sheets:** 11

| # | Sheet Name | Rows (approx) | Purpose | User Input |
|---|------------|---------------|---------|------------|
| 1 | Instructions_Legend | 50 | User guidance, metadata, legend | Metadata only (yellow cells) |
| 2 | DLP_Technology_Inventory | 35 | Complete DLP inventory | Yes (data entry rows) |
| 3 | Network_DLP | 25 | Network appliance assessment | Yes (data entry rows) |
| 4 | Endpoint_DLP | 25 | Endpoint agent assessment | Yes (data entry rows) |
| 5 | Email_DLP | 20 | Email DLP assessment | Yes (data entry rows) |
| 6 | Cloud_CASB_DLP | 20 | Cloud/CASB DLP assessment | Yes (data entry rows) |
| 7 | Web_DLP | 20 | Web proxy DLP assessment | Yes (data entry rows) |
| 8 | Database_DAM | 20 | Database Activity Monitoring assessment | Yes (data entry rows) |
| 9 | Gap_Analysis | 45 | Gaps, remediation plans | Yes (gap details) |
| 10 | Evidence_Register | 105 | Evidence tracking | Yes (evidence entries) |
| 11 | Summary_Dashboard | 35 | KPIs, compliance metrics | No (automated formulas) |

**Total Assessment Items:** ~85 infrastructure checkpoints

---

# Detailed Sheet Specifications

## Sheet: Instructions_Legend

**Purpose:** Provide user guidance and assessment metadata

**Layout:** Read-only, informational content

**Sections:**

**A. Document Header (Rows 1-10)**

- Row 1-2: Workbook title and ID
  - Font: Calibri 18pt Bold
  - Cell A1: "ISMS-IMP-A.8.12.1: DLP Infrastructure Assessment"
  - Cell A2: "Assessment Workbook v2.0 - ISO/IEC 27001:2022 Control A.8.12"
- Row 3-10: Document metadata table
  - Columns: A (Field), B (Value)
  - Fields: Workbook ID, Assessment Area, Related Policy, Version, Date Created, Review Cycle


**B. Organization Metadata (Rows 12-20)**
**USER INPUT REQUIRED - Yellow Background**

| Row | Field | Column A | Column B (User Input) |
|-----|-------|----------|----------------------|
| 13 | Assessment Date | "Assessment Date:" | DD.MM.YYYY (data validation: date format) |
| 14 | Completed By | "Completed By:" | Text (name) |
| 15 | Organization Name | "Organization Name:" | Text |
| 16 | Review Cycle | "Review Cycle:" | Dropdown: Quarterly/Semi-Annual/Annual |

**C. How to Use This Workbook (Rows 22-38)**

- Numbered steps (1-10) matching Section 3 workflow from Part I
- Font: Calibri 11pt
- Key action items in bold


**D. Legend - Response Values (Rows 40-48)**

| Symbol | Meaning | Color | RGB |
|--------|---------|-------|-----|
| ✅ | Compliant | Green | 198, 239, 206 |
| ⚠️ | Partial | Yellow | 255, 235, 156 |
| ❌ | Non-Compliant | Red | 255, 199, 206 |
| 📋 | Planned | Blue | 180, 198, 231 |
| ⚪ | N/A | Gray | 217, 217, 217 |

**E. Color Coding Guide (Rows 50-55)**

- Yellow cells = User input required
- Green cells = Compliant status
- Red cells = Non-compliant status
- White cells = Assessment responses
- Gray cells = Informational/examples (to be deleted or overwritten)


**Cell Protection:**

- All cells protected (read-only)
- No user input on this sheet except metadata (rows 13-16)


**Print Settings:**

- Fit to 1 page wide
- Page orientation: Portrait


---

## Sheet: DLP_Technology_Inventory

**Purpose:** Complete inventory of all DLP solutions deployed

**Column Specifications:**

| Col | Header | Type | Width | Data Validation | Formula/Notes |
|-----|--------|------|-------|-----------------|---------------|
| A | Technology ID | Text | 15 | None | User input (e.g., DLP-001) |
| B | Technology Name | Text | 30 | None | User input (vendor + product) |
| C | Deployment Type | Dropdown | 18 | List: Network, Endpoint, Cloud, Email, Web, Database | Dropdown |
| D | Vendor | Text | 20 | None | User input |
| E | Version | Text | 15 | None | User input (specific version) |
| F | Deployment Architecture | Dropdown | 20 | List: Inline, Monitor, Hybrid, Cloud-based | Dropdown |
| G | Deployment Status | Dropdown | 18 | List: Production, Staging, Test, Decommissioned | Dropdown |
| H | License Type | Dropdown | 18 | List: Perpetual, Subscription, Open Source | Dropdown |
| I | License Expiry | Date | 15 | Date format (DD.MM.YYYY) | User input |
| J | Support Contract | Dropdown | 15 | List: Active, Expired, N/A | Dropdown |
| K | EOL Date | Date | 15 | Date format (DD.MM.YYYY) or Text "Not announced" | User input |
| L | Primary Use Case | Text | 35 | None | User input |
| M | Integration Status | Dropdown | 18 | List: Integrated, Standalone, Partial | Dropdown |
| N | SIEM Integration | Dropdown | 15 | List: Yes, No, Partial, Planned, N/A | Dropdown |
| O | SOC Integration | Dropdown | 15 | List: Yes, No, Partial, Planned, N/A | Dropdown |
| P | Status | Dropdown | 18 | List: ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A | Dropdown, conditional formatting |
| Q | Evidence ID | Text | 18 | None | User input (e.g., A812-1-INF-001) |

**Header Row:** Row 5 (Rows 1-4 reserved for sheet title, instructions)

- Font: Calibri 11pt Bold
- Fill: Dark Blue (RGB: 68, 114, 196)
- Text: White
- Border: All borders, medium weight


**Data Rows:** Rows 6-35 (30 rows total)

- Rows 6-10: Pre-populated example rows (Gray fill RGB: 242, 242, 242)
  - Example 1: Forcepoint DLP (Network)
  - Example 2: Forcepoint Endpoint DLP (Endpoint)
  - Example 3: Microsoft Purview DLP (Cloud)
  - Example 4: Symantec DLP (Email)
  - Example 5: Netskope CASB (Cloud)
- Rows 11-35: Blank for user input (White fill)
- Row height: 20


**Conditional Formatting:**

**Status Column (P):**

- Rule 1: If "✅ Compliant" → Green fill (RGB: 198, 239, 206), Green text
- Rule 2: If "⚠️ Partial" → Yellow fill (RGB: 255, 235, 156), Dark orange text
- Rule 3: If "❌ Non-Compliant" → Red fill (RGB: 255, 199, 206), Dark red text
- Rule 4: If "N/A" → Gray fill (RGB: 217, 217, 217), Gray text


**License Expiry Column (I):**

- Rule 1: If date < TODAY() → Red fill (expired)
- Rule 2: If date < TODAY()+180 → Yellow fill (expiring <6 months)
- Rule 3: If date >= TODAY()+180 → Green fill (valid)


**EOL Date Column (K):**

- Rule 1: If date < TODAY() → Red fill (past EOL)
- Rule 2: If date < TODAY()+365 → Yellow fill (approaching EOL <12 months)
- Rule 3: If date >= TODAY()+365 → Green fill (current)


**Cell Protection:**

- Header row (5): Protected
- Example rows (6-10): Protected (users can view but not edit examples)
- Data rows (11-35): Columns A-O Unprotected (user input), Column P (Status) Unprotected, Column Q (Evidence) Unprotected
- Allow: Insert rows, Sort, Filter


**Print Settings:**

- Fit to 1 page wide (landscape orientation)
- Repeat header row on all pages
- Page breaks: After row 20, after row 35


**Formulas:**
None in this sheet (data entry only). Summary calculations in Summary_Dashboard sheet.

---

## Sheet: Network_DLP

**Purpose:** Assess network-based DLP appliances

**Column Specifications:**

| Col | Header | Type | Width | Data Validation | Notes |
|-----|--------|------|-------|-----------------|-------|
| A | Appliance Name | Text | 30 | None | User input |
| B | Deployment Mode | Dropdown | 20 | List: Inline, TAP, SPAN, Cloud Gateway | Dropdown |
| C | Network Segments Covered | Text | 30 | None | CSV list (e.g., "DMZ, Internal") |
| D | Protocols Inspected | Text | 30 | None | CSV list (e.g., "HTTP, HTTPS, SMTP") |
| E | SSL/TLS Inspection | Dropdown | 18 | List: Yes, No, Partial, Planned, N/A | Dropdown |
| F | Throughput Capacity | Text | 18 | None | User input (e.g., "10 Gbps") |
| G | Current Utilization % | Number | 15 | 0-100 | User input numeric |
| H | Content Inspection | Dropdown | 18 | List: Yes, No, Partial, Planned, N/A | Dropdown |
| I | Pattern Matching (Regex) | Dropdown | 18 | List: Yes, No, Partial, Planned, N/A | Dropdown |
| J | Fingerprinting | Dropdown | 18 | List: Yes, No, Partial, Planned, N/A | Dropdown |
| K | Machine Learning/AI | Dropdown | 18 | List: Yes, No, Partial, Planned, N/A | Dropdown |
| L | Blocking Capability | Dropdown | 18 | List: Yes, No, Partial, N/A | Dropdown |
| M | High Availability | Dropdown | 15 | List: Yes, No, N/A | Dropdown |
| N | Status | Dropdown | 18 | List: ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A | Conditional formatting |
| O | Evidence ID | Text | 18 | None | User input |

**Header Row:** Row 5
**Data Rows:** Rows 6-25 (20 rows total)

- Rows 6-8: Pre-populated examples (Gray fill)
- Rows 9-25: Blank for user input


**Conditional Formatting:**

**Status Column (N):**

- Same as DLP_Technology_Inventory sheet Status column


**Utilization Column (G):**

- Rule 1: If >90 → Red fill (critical, over-capacity)
- Rule 2: If 70-90 → Yellow fill (warning, approaching capacity)
- Rule 3: If <70 → Green fill (acceptable)


**Cell Protection:** Same pattern as previous sheet

---

## Sheet: Endpoint_DLP

**Purpose:** Assess endpoint DLP agent deployment

**Column Specifications:**

| Col | Header | Type | Width | Data Validation | Formula/Notes |
|-----|--------|------|-------|-----------------|---------------|
| A | Endpoint Solution Name | Text | 35 | None | User input |
| B | Operating Systems Supported | Text | 35 | None | CSV list (e.g., "Windows 10/11, macOS 13+") |
| C | Total Endpoints | Number | 15 | Integer >0 | User input |
| D | Agents Deployed | Number | 15 | Integer ≥0 | User input |
| E | Deployment Coverage % | Calculated | 18 | Read-only | Formula: =(D/C)*100 |
| F | Offline Protection | Dropdown | 18 | List: Yes, No, Partial, Planned, N/A | Dropdown |
| G | Agent Update Mechanism | Dropdown | 20 | List: Automatic, Manual, Scheduled | Dropdown |
| H | Channels Monitored | Text | 40 | None | CSV list (e.g., "USB, Clipboard, Print") |
| I | USB Blocking | Dropdown | 18 | List: Block, Monitor, Allow with justification, N/A | Dropdown |
| J | Cloud App Detection | Dropdown | 18 | List: Yes, No, Partial, Planned, N/A | Dropdown |
| K | Application Control | Dropdown | 18 | List: Yes, No, Partial, Planned, N/A | Dropdown |
| L | Status | Dropdown | 18 | List: ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A | Conditional formatting |
| M | Evidence ID | Text | 18 | None | User input |

**Header Row:** Row 5
**Data Rows:** Rows 6-25 (20 rows total)

**Formulas:**

**Column E (Deployment Coverage %):**
```excel
Row 6: =IF(C6>0, ROUND((D6/C6)*100, 1), 0)
Copy down to row 25
```

**Conditional Formatting:**

**Coverage Column (E):**

- Rule 1: If ≥95 → Green fill (excellent coverage)
- Rule 2: If 80-94 → Yellow fill (acceptable coverage)
- Rule 3: If <80 → Red fill (insufficient coverage)


**Status Column (L):**

- Same as previous sheets


**Cell Protection:**

- Column E (Coverage %): Protected (calculated field)
- Other data columns: Unprotected


---

## Sheet: Email_DLP

**Purpose:** Assess email DLP integration

**Column Specifications:**

| Col | Header | Type | Width | Data Validation | Notes |
|-----|--------|------|-------|-----------------|-------|
| A | Email System | Text | 30 | None | E.g., "Microsoft Exchange 2019", "M365", "Google Workspace" |
| B | DLP Integration Point | Dropdown | 25 | List: Gateway, Cloud Service, API-based, Hybrid | Dropdown |
| C | Content Inspection | Dropdown | 18 | List: Yes, No, Partial, Planned, N/A | Dropdown |
| D | Attachment Scanning | Dropdown | 18 | List: Yes, No, Partial, Planned, N/A | Dropdown |
| E | Supported File Types | Text | 35 | None | CSV list (e.g., "PDF, DOCX, XLSX, ZIP") |
| F | Maximum Attachment Size | Text | 18 | None | E.g., "25 MB", "50 MB" |
| G | Encryption Support (S/MIME, PGP) | Dropdown | 25 | List: Yes, No, Partial, N/A | Dropdown |
| H | External Email Monitoring | Dropdown | 20 | List: Yes, No, Partial, N/A | Dropdown |
| I | Test Email Blocking Verified | Dropdown | 22 | List: Yes, No, Not Tested | Dropdown |
| J | Status | Dropdown | 18 | List: ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A | Conditional formatting |
| K | Evidence ID | Text | 18 | None | User input |

**Header Row:** Row 5
**Data Rows:** Rows 6-20 (15 rows total)

---

## Sheet: Cloud_CASB_DLP

**Purpose:** Assess cloud and CASB DLP capabilities

**Column Specifications:**

| Col | Header | Type | Width | Data Validation | Notes |
|-----|--------|------|-------|-----------------|-------|
| A | CASB/Cloud DLP Solution | Text | 35 | None | E.g., "Microsoft Purview", "Netskope", "Zscaler" |
| B | Connected SaaS Applications | Text | 40 | None | CSV list (e.g., "M365, Salesforce, Dropbox") |
| C | Deployment Model | Dropdown | 20 | List: API-based, Proxy-based, Inline, Hybrid | Dropdown |
| D | Data Classification Integration | Dropdown | 25 | List: Yes, No, Partial, Planned, N/A | Dropdown |
| E | Policy Enforcement Mode | Dropdown | 22 | List: Monitor Only, Block, Prompt User, Quarantine | Dropdown |
| F | Cloud Storage Monitoring | Dropdown | 22 | List: Yes, No, Partial, Planned, N/A | Dropdown |
| G | File Sharing Control | Dropdown | 20 | List: Yes, No, Partial, Planned, N/A | Dropdown |
| H | API Security Monitoring | Dropdown | 22 | List: Yes, No, Partial, Planned, N/A | Dropdown |
| I | Status | Dropdown | 18 | List: ✅ Compliant, ⚠️ Partial, ❌ Non-Compliant, N/A | Conditional formatting |
| J | Evidence ID | Text | 18 | None | User input |

**Header Row:** Row 5
**Data Rows:** Rows 6-20 (15 rows total)

---

## Sheet: Web_Database_DLP

**Purpose:** Assess web proxy and database DLP

**Sections:**

**Section A: Web Proxy DLP (Rows 5-15)**

| Col | Header | Type | Width | Data Validation |
|-----|--------|------|-------|-----------------|
| A | Web Proxy Solution | Text | 30 | None |
| B | DLP Integration | Dropdown | 18 | List: Yes, No, Partial, Planned, N/A |
| C | SSL Inspection (Web Uploads) | Dropdown | 22 | List: Yes, No, Partial, Planned, N/A |
| D | Cloud Storage Blocking | Dropdown | 22 | List: Block, Monitor, Allow, N/A |
| E | Blocked Services | Text | 40 | CSV list (e.g., "Dropbox Personal, Google Drive Personal") |
| F | Status | Dropdown | 18 | ✅/⚠️/❌/N/A |
| G | Evidence ID | Text | 18 | User input |

**Section B: Database Activity Monitoring (Rows 17-27)**

| Col | Header | Type | Width | Data Validation |
|-----|--------|------|-------|-----------------|
| A | Database System | Text | 30 | E.g., "SQL Server 2019", "Oracle 19c", "PostgreSQL" |
| B | DAM Solution | Text | 30 | E.g., "Imperva DAM", "Oracle Audit Vault", "Native Audit" |
| C | Query Logging | Dropdown | 18 | List: Yes, No, Partial, Planned, N/A |
| D | Bulk Export Detection | Dropdown | 20 | List: Yes, No, Partial, Planned, N/A |
| E | Alert Threshold | Text | 18 | E.g., ">10,000 rows", ">100 MB" |
| F | Status | Dropdown | 18 | ✅/⚠️/❌/N/A |
| G | Evidence ID | Text | 18 | User input |

---

## Sheet: Gap_Analysis

**Purpose:** Document gaps and remediation plans

**Column Specifications:**

| Col | Header | Type | Width | Notes |
|-----|--------|------|-------|-------|
| A | Gap ID | Text | 12 | Auto-generated: GAP-001, GAP-002, etc. |
| B | Domain | Dropdown | 20 | List: Technology Inventory, Network DLP, Endpoint DLP, Email DLP, Cloud/CASB DLP, Web/Database DLP |
| C | Gap Description | Text | 50 | User input (what's missing or inadequate) |
| D | Risk Level | Dropdown | 15 | List: Critical, High, Medium, Low |
| E | Impact if Not Remediated | Text | 40 | User input (business/security impact) |
| F | Remediation Action | Text | 50 | User input (what needs to be done) |
| G | Owner | Text | 25 | User input (person/team responsible) |
| H | Target Date | Date | 15 | DD.MM.YYYY |
| I | Status | Dropdown | 18 | List: Open, In Progress, Completed, Deferred |
| J | Evidence ID (Remediation) | Text | 22 | Evidence after remediation |

**Header Row:** Row 5
**Data Rows:** Rows 6-45 (40 rows for gaps)

**Conditional Formatting:**

**Risk Level Column (D):**

- If "Critical" → Red fill, white text
- If "High" → Orange fill, dark text
- If "Medium" → Yellow fill, dark text
- If "Low" → Light yellow fill, dark text


**Target Date Column (H):**

- If past due (< TODAY()) → Red fill
- If due soon (< TODAY()+30) → Yellow fill
- If future (>= TODAY()+30) → Green fill


**Status Column (I):**

- If "Open" → Red fill
- If "In Progress" → Yellow fill
- If "Completed" → Green fill
- If "Deferred" → Gray fill


**Cell Protection:**

- Column A (Gap ID): Protected (auto-generated)
- Other columns: Unprotected


---

## Sheet: Evidence_Register

**Purpose:** Track all evidence collected

**Column Specifications:**

| Col | Header | Type | Width | Notes |
|-----|--------|------|-------|-------|
| A | Evidence ID | Text | 15 | User input or auto-generated |
| B | Domain | Dropdown | 20 | List: Technology Inventory, Network DLP, Endpoint DLP, Email DLP, Cloud/CASB DLP, Web/Database DLP, Gap Remediation |
| C | Evidence Type | Dropdown | 25 | List: Screenshot, Configuration Export, Test Result, Architecture Diagram, Report, Documentation |
| D | Description | Text | 50 | User input (what evidence shows) |
| E | File Name | Text | 40 | Actual file name in repository |
| F | File Location | Text | 60 | Path or URL |
| G | Collection Date | Date | 15 | DD.MM.YYYY |
| H | Collected By | Text | 25 | Person who collected |
| I | Classification | Dropdown | 15 | List: Public, Internal, Confidential |

**Header Row:** Row 5
**Data Rows:** Rows 6-105 (100 rows for evidence)

**Formula for Evidence ID Auto-Generation:**
```excel
Row 6: =IF(B6<>"", "EV-"&TEXT(ROW()-5, "000"), "")
Copy down to row 105
```

**Cell Protection:**

- Column A (Evidence ID): Protected if formula present
- Other columns: Unprotected


---

## Sheet: Summary_Dashboard

**Purpose:** Executive summary and compliance KPIs

**Layout:** Not tabular, dashboard style with KPI boxes

**Key Metrics (Calculated):**

**A. Overall Compliance Rate (Cell B5):**
```excel
=ROUND(
  (COUNTIF(DLP_Technology_Inventory!P:P,"✅ Compliant") + 
   COUNTIF(Network_DLP!N:N,"✅ Compliant") + 
   COUNTIF(Endpoint_DLP!L:L,"✅ Compliant") + 
   COUNTIF(Email_DLP!J:J,"✅ Compliant") + 
   COUNTIF(Cloud_CASB_DLP!I:I,"✅ Compliant") + 
   COUNTIF(Web_Database_DLP!F:F,"✅ Compliant")) /
  (COUNTA(DLP_Technology_Inventory!P:P) - 1 + 
   COUNTA(Network_DLP!N:N) - 1 + 
   COUNTA(Endpoint_DLP!L:L) - 1 + 
   COUNTA(Email_DLP!J:J) - 1 + 
   COUNTA(Cloud_CASB_DLP!I:I) - 1 + 
   COUNTA(Web_Database_DLP!F:F) - 1) * 100,
1)
```

**B. Total DLP Technologies (Cell B7):**
```excel
=COUNTIF(DLP_Technology_Inventory!G:G, "Production")
```

**C. Critical Gaps Count (Cell B9):**
```excel
=COUNTIF(Gap_Analysis!D:D, "Critical")
```

**D. High Priority Gaps (Cell B10):**
```excel
=COUNTIF(Gap_Analysis!D:D, "High")
```

**E. Endpoint Coverage % (Cell B12):**
```excel
=AVERAGE(Endpoint_DLP!E:E)
```
(Average of all endpoint coverage percentages)

**F. SIEM Integration Rate (Cell B14):**
```excel
=ROUND(
  COUNTIF(DLP_Technology_Inventory!N:N, "Yes") /
  (COUNTIF(DLP_Technology_Inventory!G:G, "Production")) * 100,
1)
```

**Conditional Formatting for KPIs:**

**Overall Compliance Rate (B5):**

- If ≥90% → Green fill, dark green text
- If 70-89% → Yellow fill, dark orange text
- If <70% → Red fill, dark red text


**Critical Gaps Count (B9):**

- If =0 → Green fill
- If 1-3 → Yellow fill
- If >3 → Red fill


**Dashboard Layout:**

```
Row 2-3: Title "DLP Infrastructure Assessment - Summary Dashboard"
Row 5: Overall Compliance Rate: [XX%] [Conditional color]
Row 7: Total DLP Technologies: [XX]
Row 9: Critical Gaps: [XX] [Conditional color]
Row 10: High Priority Gaps: [XX]
Row 12: Average Endpoint Coverage: [XX%]
Row 14: SIEM Integration Rate: [XX%]
Row 16-20: Top 5 Critical Gaps (pulled from Gap_Analysis sheet)
Row 22-27: Recommended Immediate Actions
```

**Cell Protection:**

- All cells protected (dashboard is read-only, calculated)


---

## Sheet: Approval_Sign-Off

**Purpose:** Document approval workflow

**Layout:** Form-style, not tabular

**Sections:**

**Assessment Metadata (Rows 5-12):**

- Assessment Period: From [Date] to [Date]
- Assessment Date: [DD.MM.YYYY]
- Assessment Type: [Dropdown: Initial/Quarterly/Ad-Hoc/Post-Remediation]


**Completed By (Rows 14-20):**

- Name: [Text field]
- Role: [Text field]
- Email: [Text field]
- Date Completed: [Date field]
- Signature: [Text field or digital signature]
- Time Invested: [Number] hours


**Reviewed By (Rows 22-28):**

- Name, Date, Signature fields
- Review Outcome: [Dropdown: Approved/Approved with corrections/Requires revision]
- Comments: [Large text area]


**Approved By (CISO) (Rows 30-40):**

- Name, Date, Signature fields
- Approval Decision: [Dropdown: Approved/Approved with conditions/Rejected]
- Risk Acceptance: [Checkbox: Yes/No]
- Budget Approval: [Dropdown: Approved/Requires justification/Deferred]
- Budget Amount: CHF [Number]


**Next Review Date (Row 42):**

- Date: [DD.MM.YYYY]


**Cell Protection:**

- Field labels: Protected
- Input fields (dates, names, dropdowns): Unprotected


---

# Data Validation Rules Summary

## Dropdown Lists

**Status (All Assessment Sheets):**
```
List: ✅ Compliant,⚠️ Partial,❌ Non-Compliant,N/A
```

**Yes/No/Partial Response:**
```
List: Yes,No,Partial,Planned,N/A
```

**Deployment Type (Technology Inventory):**
```
List: Network,Endpoint,Cloud,Email,Web,Database
```

**Deployment Architecture:**
```
List: Inline,Monitor,Hybrid,Cloud-based
```

**Deployment Status:**
```
List: Production,Staging,Test,Decommissioned
```

**License Type:**
```
List: Perpetual,Subscription,Open Source
```

**Risk Level (Gap Analysis):**
```
List: Critical,High,Medium,Low
```

**Remediation Status:**
```
List: Open,In Progress,Completed,Deferred
```

## Date Validation

**Format:** DD.MM.YYYY (Swiss/European format)

**Validation Rule:**
```
Type: Date
Data: Between 01.01.2020 and 31.12.2030
Error Message: "Please enter a valid date in DD.MM.YYYY format"
```

## Number Validation

**Utilization Percentage:**
```
Type: Decimal
Data: Between 0 and 100
Error Message: "Enter a percentage between 0 and 100"
```

**Endpoint Counts:**
```
Type: Whole Number
Data: Greater than or equal to 0
Error Message: "Enter a valid endpoint count (0 or positive integer)"
```

---

# Conditional Formatting Rules

## Status Column Formatting

**Applied to:** All Status columns across assessment sheets

**Rule 1: Compliant**
```
Formula: =$P6="✅ Compliant"
Format: Fill RGB(198,239,206), Font Color Dark Green
```

**Rule 2: Partial**
```
Formula: =$P6="⚠️ Partial"
Format: Fill RGB(255,235,156), Font Color Dark Orange
```

**Rule 3: Non-Compliant**
```
Formula: =$P6="❌ Non-Compliant"
Format: Fill RGB(255,199,206), Font Color Dark Red
```

**Rule 4: N/A**
```
Formula: =$P6="N/A"
Format: Fill RGB(217,217,217), Font Color Gray
```

## Date-Based Formatting

**License Expiry:**
```
Rule 1: =I6<TODAY() → Red fill (expired)
Rule 2: =AND(I6>=TODAY(), I6<TODAY()+180) → Yellow fill (expiring soon)
Rule 3: =I6>=TODAY()+180 → Green fill (valid)
```

**EOL Date:**
```
Rule 1: =K6<TODAY() → Red fill (past EOL)
Rule 2: =AND(K6>=TODAY(), K6<TODAY()+365) → Yellow fill (approaching EOL)
Rule 3: =K6>=TODAY()+365 → Green fill (current)
```

**Gap Target Date:**
```
Rule 1: =H6<TODAY() → Red fill (overdue)
Rule 2: =AND(H6>=TODAY(), H6<TODAY()+30) → Yellow fill (due soon)
Rule 3: =H6>=TODAY()+30 → Green fill (on track)
```

## KPI Formatting (Summary Dashboard)

**Compliance Percentage:**
```
Rule 1: >=90 → Green fill
Rule 2: 70-89 → Yellow fill
Rule 3: <70 → Red fill
```

**Critical Gaps Count:**
```
Rule 1: =0 → Green fill
Rule 2: 1-3 → Yellow fill
Rule 3: >3 → Red fill
```

---

# Cell Protection Configuration

## Protected Cells (Locked)

**Across All Sheets:**

- Column headers (header row)
- Instructional text cells
- Example rows (gray fill)
- Formula cells (calculations in Summary Dashboard, Coverage % in Endpoint DLP)
- Auto-generated cells (Evidence ID if formula present, Gap ID)


## Unprotected Cells (Unlocked)

**User Input Areas:**

- Data entry rows in all assessment sheets
- Dropdown selection cells
- Text input fields
- Date input fields
- Evidence descriptions and file locations
- Gap analysis details
- Approval workflow fields


## Sheet Protection Settings

**For Each Sheet:**
```
Protection Enabled: Yes
Password: [To be set during workbook generation - recommend strong password]

Allow Users To:

- Select locked cells: Yes
- Select unlocked cells: Yes
- Format cells: Yes (for user notes)
- Insert rows: Yes (in assessment sheets for additional entries)
- Delete rows: No (prevent accidental deletion)
- Sort: Yes
- Use AutoFilter: Yes
- Use PivotTable reports: No

```

**Exceptions:**

- Instructions_Legend: Fully protected except metadata cells
- Summary_Dashboard: Fully protected (all calculated)
- Approval_Sign-Off: Only input fields unprotected


---

# Summary Dashboard Formulas (Detailed)

## Overall Compliance Rate

**Purpose:** Calculate percentage of compliant items across all assessment sheets

**Formula (Cell B5):**
```excel
=IFERROR(
  ROUND(
    (COUNTIF(DLP_Technology_Inventory!P6:P35,"✅ Compliant") + 
     COUNTIF(Network_DLP!N6:N25,"✅ Compliant") + 
     COUNTIF(Endpoint_DLP!L6:L25,"✅ Compliant") + 
     COUNTIF(Email_DLP!J6:J20,"✅ Compliant") + 
     COUNTIF(Cloud_CASB_DLP!I6:I20,"✅ Compliant") + 
     COUNTIF(Web_Database_DLP!F6:F15,"✅ Compliant") + 
     COUNTIF(Web_Database_DLP!F18:F27,"✅ Compliant")) /
    (COUNTA(DLP_Technology_Inventory!P6:P35) + 
     COUNTA(Network_DLP!N6:N25) + 
     COUNTA(Endpoint_DLP!L6:L25) + 
     COUNTA(Email_DLP!J6:J20) + 
     COUNTA(Cloud_CASB_DLP!I6:I20) + 
     COUNTA(Web_Database_DLP!F6:F15) + 
     COUNTA(Web_Database_DLP!F18:F27)) * 100,
  1),
0)
```

**Explanation:**

- Numerator: Count of ✅ Compliant across all Status columns
- Denominator: Count of all populated Status cells (excluding headers)
- ROUND to 1 decimal place
- IFERROR returns 0 if division by zero (empty workbook)


## Technology Count

**Formula (Cell B7):**
```excel
=COUNTIF(DLP_Technology_Inventory!G6:G35, "Production")
```

**Explanation:** Count only Production status (exclude Staging, Test, Decommissioned)

## Critical Gaps

**Formula (Cell B9):**
```excel
=COUNTIF(Gap_Analysis!D6:D45, "Critical")
```

## High Priority Gaps

**Formula (Cell B10):**
```excel
=COUNTIF(Gap_Analysis!D6:D45, "High")
```

## Average Endpoint Coverage

**Formula (Cell B12):**
```excel
=IFERROR(
  ROUND(
    AVERAGE(Endpoint_DLP!E6:E25),
  1),
"N/A")
```

**Explanation:** Average of Coverage % column (Column E in Endpoint_DLP)

## SIEM Integration Rate

**Formula (Cell B14):**
```excel
=IFERROR(
  ROUND(
    COUNTIF(DLP_Technology_Inventory!N6:N35, "Yes") /
    COUNTIF(DLP_Technology_Inventory!G6:G35, "Production") * 100,
  1),
0)
```

**Explanation:**

- Numerator: Count of "Yes" in SIEM Integration column for Production systems
- Denominator: Total Production systems
- Percentage calculation


---

# Python Script Integration Points

## Workbook Generation Script

**Script Name:** `generate_a812_1_dlp_infrastructure_assessment.py`

**Key Functions:**

```python
def create_workbook():
    """Initialize workbook and create all 11 sheets"""
    wb = openpyxl.Workbook()
    # Remove default sheet
    wb.remove(wb.active)
    # Create sheets in order
    sheets = [
        "Instructions_Legend",
        "DLP_Technology_Inventory",
        "Network_DLP",
        "Endpoint_DLP",
        "Email_DLP",
        "Cloud_CASB_DLP",
        "Web_Database_DLP",
        "Gap_Analysis",
        "Evidence_Register",
        "Summary_Dashboard",
        "Approval_Sign-Off"
    ]
    for sheet_name in sheets:
        wb.create_sheet(sheet_name)
    return wb

def setup_styles():
    """Define cell styles, fonts, fills"""
    # Header style
    header_fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
    header_font = Font(name="Calibri", size=11, bold=True, color="FFFFFF")
    # Compliant style
    compliant_fill = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")
    # Partial style
    partial_fill = PatternFill(start_color="FFEB9C", end_color="FFEB9C", fill_type="solid")
    # Non-compliant style
    noncompliant_fill = PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")
    # Return style dictionary
    return {
        'header': {'fill': header_fill, 'font': header_font},
        'compliant': {'fill': compliant_fill},
        'partial': {'fill': partial_fill},
        'noncompliant': {'fill': noncompliant_fill}
    }

def get_column_definitions(sheet_key):
    """Return column widths and headers for each sheet type"""
    # CUSTOMIZE: Adjust column definitions per sheet
    definitions = {
        'DLP_Technology_Inventory': {
            'widths': [15, 30, 18, 20, 15, 20, 18, 18, 15, 15, 15, 35, 18, 15, 15, 18, 18],
            'headers': ['Technology ID', 'Technology Name', 'Deployment Type', ...]
        },
        'Network_DLP': {
            'widths': [30, 20, 30, 30, 18, 18, 15, 18, 18, 18, 18, 18, 15, 18, 18],
            'headers': ['Appliance Name', 'Deployment Mode', ...]
        },
        # ... other sheets
    }
    return definitions.get(sheet_key, {})

def create_assessment_sheet(wb, sheet_name, config):
    """Generic function to create assessment sheet with validation"""
    ws = wb[sheet_name]
    # Set column widths
    for idx, width in enumerate(config['widths'], start=1):
        ws.column_dimensions[get_column_letter(idx)].width = width
    # Create headers (row 5)
    for idx, header in enumerate(config['headers'], start=1):
        cell = ws.cell(row=5, column=idx, value=header)
        cell.fill = config['styles']['header']['fill']
        cell.font = config['styles']['header']['font']
    # Add data validation dropdowns
    for validation_def in config['validations']:
        # Apply validation to range
        dv = DataValidation(type="list", formula1=validation_def['formula'], allow_blank=False)
        ws.add_data_validation(dv)
        dv.add(validation_def['range'])
    # Apply conditional formatting
    for cf_rule in config['conditional_formatting']:
        ws.conditional_formatting.add(cf_rule['range'], cf_rule['rule'])
    # Protect sheet
    ws.protection.sheet = True
    ws.protection.password = config.get('password', '')
    ws.protection.formatCells = True
    ws.protection.insertRows = True
    ws.protection.sort = True
    ws.protection.autoFilter = True

def create_summary_dashboard(wb):
    """Create Summary Dashboard with formulas"""
    ws = wb['Summary_Dashboard']
    # Overall Compliance Rate (B5)
    ws['B5'] = '=IFERROR(ROUND((COUNTIF(DLP_Technology_Inventory!P6:P35,"✅ Compliant")+...'
    # Other KPI formulas
    ws['B7'] = '=COUNTIF(DLP_Technology_Inventory!G6:G35, "Production")'
    ws['B9'] = '=COUNTIF(Gap_Analysis!D6:D45, "Critical")'
    # Apply conditional formatting to KPIs
    # ... (per specification above)

def create_evidence_register(wb):
    """Create Evidence Register with auto-numbering"""
    ws = wb['Evidence_Register']
    # Formula for Evidence ID (Column A)
    for row in range(6, 106):
        ws.cell(row=row, column=1, value=f'=IF(B{row}<>"", "EV-"&TEXT(ROW()-5, "000"), "")')

def save_workbook(wb, filename):
    """Save with proper filename format"""
    # CUSTOMIZE: Organization-specific output path
    today = datetime.now().strftime("%Y%m%d")
    output_filename = f"ISMS-IMP-A.8.12.1_DLP_Infrastructure_Assessment_{today}.xlsx"
    wb.save(output_filename)
    print(f"✅ Workbook created: {output_filename}")
```

## Quality Assurance Script

**Script Name:** `excel_sanity_check_a812_1.py`

**Purpose:** Validate generated workbook matches specification

```python
def validate_workbook_structure(filename):
    """Check sheet names, column counts, headers"""
    wb = openpyxl.load_workbook(filename)
    expected_sheets = ["Instructions_Legend", "DLP_Technology_Inventory", ...]
    assert wb.sheetnames == expected_sheets, "Sheet structure mismatch"

def validate_data_validation(filename):
    """Verify dropdown validations applied correctly"""
    wb = openpyxl.load_workbook(filename)
    ws = wb['DLP_Technology_Inventory']
    # Check column P has Status dropdown
    validations = ws.data_validations.dataValidation
    assert any("✅ Compliant,⚠️ Partial,❌ Non-Compliant,N/A" in str(dv.formula1) for dv in validations)

def validate_conditional_formatting(filename):
    """Verify conditional formatting rules present"""
    wb = openpyxl.load_workbook(filename)
    ws = wb['DLP_Technology_Inventory']
    # Check Status column has 4 rules (Compliant, Partial, Non-Compliant, N/A)
    cf_rules = ws.conditional_formatting
    assert len(cf_rules) >= 4, "Missing conditional formatting rules"

def validate_formulas(filename):
    """Test formula accuracy"""
    wb = openpyxl.load_workbook(filename)
    ws = wb['Summary_Dashboard']
    # Check Overall Compliance Rate formula present
    assert ws['B5'].value.startswith('=IFERROR(ROUND'), "Compliance formula missing"

def run_all_checks(filename):
    """Execute full validation suite"""
    print("Running quality checks...")
    validate_workbook_structure(filename)
    validate_data_validation(filename)
    validate_conditional_formatting(filename)
    validate_formulas(filename)
    print("✅ All checks passed")
```

---

# Version Control and Change Management

## Workbook Versioning

**Filename Format:**
```
ISMS-IMP-A.8.12.1_DLP_Infrastructure_Assessment_YYYYMMDD.xlsx
```

**Example:**
```
ISMS-IMP-A.8.12.1_DLP_Infrastructure_Assessment_20260119.xlsx
```

**Version Tracking:**

- Version number embedded in Instructions_Legend sheet (Document Control section)
- Version history table documenting changes between versions
- Change log maintained in separate CHANGELOG.md


## Workbook Updates

**When to Increment Version:**

- **Major version (1.0 → 2.0):** Structural changes (new sheets, column reordering, formula changes)
- **Minor version (2.0 → 2.1):** Content updates (dropdown options added, examples updated)
- **Patch version (2.1.0 → 2.1.1):** Bug fixes (typo corrections, formula fixes)


## Backward Compatibility

**Maintaining Compatibility:**

- Column additions: Always add to the right (don't insert in middle)
- Dropdown updates: Only add options (don't remove existing options used in data)
- Formula changes: Test against sample data before deploying


**Migration Path:**

- v1.0 workbooks can be migrated to v2.0 using `normalize_assessment_files_a812.py` script
- Migration script maps old column structure to new structure
- Data loss warnings if v2.0 removes features from v1.0


---

# Appendix: Technical Notes for Developers

## Color Palette (RGB Values)

**Status Colors:**

- Compliant Green: RGB(198, 239, 206)
- Partial Yellow: RGB(255, 235, 156)
- Non-Compliant Red: RGB(255, 199, 206)
- N/A Gray: RGB(217, 217, 217)
- Planned Blue: RGB(180, 198, 231)


**UI Colors:**

- Header Dark Blue: RGB(68, 114, 196)
- Header Text White: RGB(255, 255, 255)
- Example Row Gray: RGB(242, 242, 242)
- User Input Yellow: RGB(255, 255, 204)


## Font Standards

**Workbook-Wide:**

- Font Family: Calibri
- Header Font Size: 11pt Bold
- Data Font Size: 11pt Regular
- Title Font Size: 14-18pt Bold


## Excel Formula Best Practices

**IFERROR Usage:**

- Wrap division operations to handle #DIV/0 errors
- Return meaningful defaults (0 for percentages, "N/A" for text)


**Named Ranges:**

- Consider using named ranges for frequently referenced cells
- Example: Name cell Instructions_Legend!B13 as "AssessmentDate"


**Absolute vs Relative References:**

- Use absolute references ($A$1) for constant cells (headers, lookup tables)
- Use relative references (A1) for cells that change when copied


## Performance Optimization

**For Large Datasets:**

- Avoid volatile functions (NOW(), TODAY(), OFFSET()) in frequently recalculated cells
- Use structured references for table data
- Minimize conditional formatting ranges (apply only to data rows, not entire columns)
- Disable automatic calculation if workbook becomes slow (File > Options > Formulas > Manual calculation)


## Known Limitations and Workarounds

**Limitation 1: Excel Date Formats (DD.MM.YYYY vs MM/DD/YYYY)**

- Issue: Excel interprets dates based on system locale
- Workaround: Use TEXT() function to force DD.MM.YYYY display format
- Example: `=TEXT(I6, "DD.MM.YYYY")`


**Limitation 2: Emoji in Dropdowns (✅, ⚠️, ❌)**

- Issue: Some Excel versions don't display emoji in dropdowns
- Workaround: Provide text alternative: "Compliant [✅]", "Partial [⚠️]", etc.
- Test on target Excel versions before deployment


**Limitation 3: Sheet Protection Prevents Some Macros**

- Issue: Protected sheets block VBA automation
- Workaround: Unprotect sheet programmatically in macro, perform operation, re-protect
- Example: `ws.Unprotect Password:="password"` then `ws.Protect Password:="password"`


---

# Testing and Validation Checklist

**Pre-Deployment Testing:**

- [ ] Workbook opens in Excel 2016, 2019, Microsoft 365 without errors
- [ ] All 11 sheets present and correctly named
- [ ] Data validation dropdowns functional in all assessment sheets
- [ ] Conditional formatting displays correctly (colors match specification)
- [ ] Formulas calculate correctly (test with sample data)
- [ ] Summary Dashboard KPIs update when data entered in assessment sheets
- [ ] Evidence Register auto-numbering works
- [ ] Cell protection configured (locked cells cannot be edited, unlocked cells can)
- [ ] Sheet protection password set and documented
- [ ] Print settings configured (landscape for wide sheets, portrait for forms)
- [ ] No broken cell references (#REF!, #NAME? errors)
- [ ] File size reasonable (<5 MB for empty workbook)


**User Acceptance Testing:**

- [ ] Security team can complete assessment within estimated time (4-6 hours)
- [ ] Dropdown options are comprehensive (no "Other" needed excessively)
- [ ] Instructions clear (users don't require additional guidance)
- [ ] Evidence naming convention practical (users can follow consistently)
- [ ] Gap Analysis captures all necessary remediation details
- [ ] Approval workflow meets organizational approval process


**Quality Assurance:**

- [ ] No spelling errors in headers, instructions, dropdown options
- [ ] Dates in DD.MM.YYYY format throughout
- [ ] Colors consistent with organizational style guide (if applicable)
- [ ] Accessibility: Color contrast sufficient for color-blind users
- [ ] Examples realistic and helpful (not Lorem Ipsum placeholders)


---

**END OF PART II: TECHNICAL SPECIFICATION**

---

# Document Assembly Instructions

**To create the complete ISMS-IMP-A.8.12.1 specification:**

1. **Combine PART I and PART II:**

   - Part I (separate file): User Completion Guide
   - Part II (this file): Technical Specification


2. **Generate Excel Workbook:**

   - Run: `python3 generate_a812_1_dlp_infrastructure_assessment.py`
   - Output: `ISMS-IMP-A.8.12.1_DLP_Infrastructure_Assessment_YYYYMMDD.xlsx`


3. **Validate Workbook:**

   - Run: `python3 excel_sanity_check_a812_1.py ISMS-IMP-A.8.12.1_DLP_Infrastructure_Assessment_YYYYMMDD.xlsx`
   - Verify: All checks pass


4. **Deploy:**

   - Distribute workbook to assessment team
   - Provide Part I User Guide as reference
   - Collect completed assessments
   - Consolidate into ISMS-IMP-A.8.12.5 Compliance Dashboard


---

**Status:** Technical Specification Complete  
**Next Action:** Implement Python workbook generator per specification  
**Dependencies:** openpyxl library (install: `pip install openpyxl`)

---

**END OF SPECIFICATION**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

*Where bamboo antennas actually work.* 🎋
