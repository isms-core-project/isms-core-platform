**ISMS-IMP-A.8.12.1-UG - DLP Infrastructure Assessment**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.12: Data Leakage Prevention

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.12.1-UG |
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

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
