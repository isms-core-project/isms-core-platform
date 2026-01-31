# ISMS-IMP-A.8.23.1 - Filtering Infrastructure Assessment
## Assessment Specification with User Completion Guide
### ISO/IEC 27001:2022 Control A.8.23: Web Filtering

---

## Document Control

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.23.1 |
| **Version** | 1.0 |
| **Assessment Area** | Web Filtering Infrastructure & Technology Capabilities |
| **Related Policy** | ISMS-POL-A.8.23, Section 2.1 (Threat Protection Requirements), ISMS-POL-A.8.23, Section 2.2 (Category Filtering Approach) |
| **Purpose** | Document deployed web filtering technologies, assess capabilities against policy requirements, and identify gaps in a vendor-agnostic manner |
| **Target Audience** | Security Engineers, Network Engineers, IT Operations, System Administrators, Compliance Officers, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Quarterly or After Major Infrastructure Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial technical specification for Web Filtering assessment workbook | ISMS Implementation Team |

### Document Structure

This document consists of two parts:

- **PART I: USER COMPLETION GUIDE**
  - Assessment Overview
  - Prerequisites
  - Workflow
  - Completing Each Sheet
  - Evidence Collection
  - Common Pitfalls
  - Quality Checklist
  - Review & Approval

- **PART II: TECHNICAL SPECIFICATION**
  - Excel Workbook Structure
  - Sheet-by-Sheet Specifications
  - Cell Styling Reference
  - Integration Points

---

# PART I: USER COMPLETION GUIDE

## Assessment Overview

### Purpose & Scope

**Assessment Name:** ISMS-IMP-A.8.23.1 - Filtering Infrastructure Assessment

#### What This Assessment Covers

This assessment documents the web filtering TECHNOLOGY and INFRASTRUCTURE deployed in your environment. This is the foundational "WHAT do we have?" assessment that answers:

- What filtering solutions are deployed? (vendor, product, version)
- What capabilities do these solutions provide? (threat protection, URL categorization, HTTPS inspection, etc.)
- What is the licensing and support status?
- How are these solutions performing?
- What gaps exist between deployed capabilities and policy requirements?

#### Key Principle

This assessment is **completely vendor-agnostic and technology-independent**. You document YOUR specific solutions (whatever you use - Zscaler, Fortigate, Sophos, open-source Squid, cloud DNS filtering, whatever), and verify capabilities against generic policy requirements.

#### What You'll Document

- Every web filtering solution/technology in your environment
- Detailed capability assessment for each solution
- Licensing, support contracts, and maintenance status
- Performance metrics and reliability data
- Side-by-side comparison if you have multiple solutions
- Capability requirements matrix (policy vs. deployed capabilities)
- Licensing & support tracking
- Performance & incident tracking
- Gaps and remediation plans
- Supporting evidence

#### How This Relates to Other A.8.23 Assessments

| Assessment            | Focus                  | Relationship to A.8.23.1           |
|-----------------------|------------------------|------------------------------------|
| **ISMS-IMP-A.8.23.1** | **Infrastructure**     | **WHAT filtering solutions exist** |
| ISMS-IMP-A.8.23.2     | Network Coverage       | WHERE those solutions are deployed |
| ISMS-IMP-A.8.23.3     | Policy Configuration   | HOW those solutions are configured |
| ISMS-IMP-A.8.23.4     | Monitoring & Response  | HOW you monitor and respond        |
| ISMS-IMP-A.8.23.5     | Compliance Dashboard   | Consolidated view across all       |

This assessment (A.8.23.1) MUST be completed first - you can't assess coverage, configuration, or monitoring until you know what technology you have!

### Who Should Complete This Assessment

#### Primary Stakeholders

1. **Security Engineering** - Architecture, capability requirements
2. **Network Engineering** - Deployment models, integration points
3. **System Administrators** - Day-to-day operations, licensing
4. **IT Operations** - Performance monitoring, incident management
5. **Procurement** - Licensing costs, support contracts

#### Required Skills

- Understanding of web filtering technologies
- Familiarity with deployed solutions (access to admin consoles)
- Knowledge of network architecture
- Understanding of threat protection concepts

#### Time Commitment

- **Initial assessment:** 6-10 hours per solution (for detailed capability review)
- **Quarterly updates:** 1-2 hours per solution (update versions, performance data)

### Expected Outputs

Upon completion, you will have:

1. ✅ **Complete solution inventory** - Every filtering solution documented
2. ✅ **Detailed capability assessments** - Know exactly what each solution can do
3. ✅ **Technology comparison** - Side-by-side if multiple solutions
4. ✅ **Requirements matrix** - Policy requirements vs. deployed capabilities
5. ✅ **Licensing status** - All licenses and support contracts tracked
6. ✅ **Performance baseline** - Historical performance and incident data
7. ✅ **Gap analysis** - Identified capability gaps with remediation plans
8. ✅ **Evidence register** - Supporting documentation for audit
9. ✅ **Approved assessment** - Three-level approval workflow completed

---

## Prerequisites

### Information You'll Need

Before starting this assessment, gather:

#### 1. Solution Access

- Administrator access to all web filtering solutions
- Access to vendor management portals
- Access to licensing/support contract systems
- Access to monitoring dashboards

#### 2. Documentation

- Current network architecture diagrams
- Deployment documentation
- Configuration documentation
- Integration architecture

#### 3. Historical Data

- License agreements and support contracts
- Performance reports (last 90 days minimum)
- Incident reports related to filtering
- Change logs and maintenance records

#### 4. Policy Requirements

- ISMS-POL-A.8.23, Section 2.1 (Threat Protection Requirements)
- ISMS-POL-A.8.23, Section 2.2 (Category Filtering Approach)
- ISMS-POL-A.8.23, Section 2.4 (Logging and Monitoring)
- ISMS-POL-A.8.23, Section 3.3 (Exception Management)

### Required Tools

- Microsoft Excel (2016 or later) for workbook completion
- Access to admin consoles for each filtering solution
- Network monitoring tools
- Log analysis tools
- Screen capture tools (for evidence screenshots)

### Dependencies

This assessment has NO dependencies - it's the first assessment in the A.8.23 series and must be completed before others.

However, outputs from this assessment are INPUT to:
- A.8.23.2 (Network Coverage) - Needs solution list from Sheet 1
- A.8.23.3 (Policy Configuration) - Needs capability data from Sheets 3-6
- A.8.23.4 (Monitoring & Response) - Needs logging capabilities from Sheet 3
- A.8.23.5 (Compliance Dashboard) - Consolidates all data

---

## Workflow

### High-Level Process

```
1. PREPARE
   ↓
2. INVENTORY SOLUTIONS (Sheet 1)
   ↓
3. DOCUMENT EACH SOLUTION (Sheets 2a, 2b, 2c...)
   ↓
4. ASSESS CAPABILITIES (Sheets 3-6)
   ↓
5. TRACK LICENSING (Sheet 7)
   ↓
6. ANALYZE REQUIREMENTS (Sheet 8)
   ↓
7. TRACK PERFORMANCE (Sheet 9)
   ↓
8. REGISTER EVIDENCE (Sheet 10)
   ↓
9. IDENTIFY GAPS
   ↓
10. REVIEW & APPROVE
```

### Detailed Workflow

#### Phase 1: Preparation (1-2 hours)

**Objective:** Gather information and understand requirements

**Steps:**
1. Read this entire User Guide
2. Gather all prerequisites (see above)
3. Review policy requirements (ISMS-POL-A.8.23, Section 2.1 (Threat Protection Requirements), S2.2, S2.3, S2.4)
4. Identify all filtering solutions in your environment
5. Schedule time with SMEs (network engineers, security engineers)
6. Create working folder for evidence collection

**Deliverable:** List of all filtering solutions and SME availability

#### Phase 2: Solution Inventory (2-3 hours)

**Objective:** Complete Sheet 1 - Solution Inventory

**Steps:**
1. List EVERY filtering solution deployed
2. For each solution:
   - Document vendor, product, version
   - Identify deployment model (appliance, cloud, hybrid)
   - Determine primary purpose
   - Assess deployment status
   - Document protected user count
3. Verify completeness with network team
4. Cross-check with asset inventory

**Deliverable:** Complete Sheet 1 with all filtering solutions

**Quality Check:**
- ✓ All filtering solutions identified (perimeter, endpoint, cloud, DNS)
- ✓ No "unknown" or "TBD" values
- ✓ Status accurately reflects current state
- ✓ User counts are reasonable estimates

#### Phase 3: Detailed Solution Documentation (3-6 hours per solution)

**Objective:** Complete Sheet 2 templates for EACH solution

**Steps:**
For each solution in Sheet 1:
1. Copy Sheet 2 template
2. Rename (e.g., "Sheet 2a: Perimeter Filter", "Sheet 2b: Cloud Filter")
3. Complete Solution Identification section
4. Document all capability categories
5. List integration points
6. Capture performance metrics
7. Collect evidence (screenshots, config exports)

**Deliverable:** One completed Sheet 2 per solution

**Quality Check:**
- ✓ Every capability category assessed (not just "Yes" without details)
- ✓ Integration points documented
- ✓ Performance data is recent (< 30 days old)
- ✓ Evidence collected for key capabilities

#### Phase 4: Capability Assessment (2-4 hours)

**Objective:** Complete Sheets 3-6 for capability analysis

**Steps:**
1. **Sheet 3: Threat Protection Capabilities**
   - Document anti-malware capabilities
   - Document phishing protection
   - Document exploit prevention
   - Assess HTTPS inspection
   
2. **Sheet 4: Category Filtering Capabilities**
   - List URL category databases
   - Document custom categories
   - Assess granularity
   - Document updates
   
3. **Sheet 5: Logging & Monitoring Capabilities**
   - Document log collection
   - Assess log retention
   - Document SIEM integration
   - Review alerting capabilities
   
4. **Sheet 6: Advanced Capabilities**
   - DLP integration
   - SSL/TLS inspection
   - User/group policies
   - Reporting capabilities

**Deliverable:** Complete Sheets 3-6

**Quality Check:**
- ✓ All capabilities assessed for all solutions
- ✓ Evidence provided for critical capabilities
- ✓ Gaps identified and documented
- ✓ No "Unknown" or "Not Assessed" without justification

#### Phase 5: Licensing & Support (1-2 hours)

**Objective:** Complete Sheet 7 - Licensing & Support

**Steps:**
1. Document all licenses
2. Identify expiration dates
3. Calculate days until expiry
4. Document support contracts
5. Flag renewal requirements
6. Document procurement status

**Deliverable:** Complete Sheet 7

**Quality Check:**
- ✓ All licenses accounted for
- ✓ Expiration dates accurate
- ✓ Support contracts documented
- ✓ Renewal process identified

#### Phase 6: Requirements Matrix (2-3 hours)

**Objective:** Complete Sheet 8 - Capability Requirements Matrix

**Steps:**
1. Review policy requirements (ISMS-POL-A.8.23, Section 2.1 (Threat Protection Requirements), S2.2, S2.3, S2.4)
2. For each requirement:
   - Identify which solution(s) provide it
   - Assess compliance status
   - Document evidence
   - Identify gaps
3. Calculate compliance percentages
4. Prioritize gaps

**Deliverable:** Complete Sheet 8 with gap analysis

**Quality Check:**
- ✓ All policy requirements addressed
- ✓ Solution mapping is accurate
- ✓ Compliance status is honest (not optimistic)
- ✓ Gaps have remediation plans

#### Phase 7: Performance Tracking (1-2 hours)

**Objective:** Complete Sheet 9 - Performance & Incidents

**Steps:**
1. Collect performance data (last 90 days)
2. Document incidents
3. Calculate uptime
4. Assess performance trends
5. Identify recurring issues

**Deliverable:** Complete Sheet 9

**Quality Check:**
- ✓ Performance data is recent
- ✓ Incidents are comprehensive
- ✓ Uptime calculations are accurate
- ✓ Trends are analyzed

#### Phase 8: Evidence Registry (1 hour)

**Objective:** Complete Sheet 10 - Evidence Registry

**Steps:**
1. List all evidence collected
2. Organize by category
3. Document storage locations
4. Verify accessibility
5. Tag for audit readiness

**Deliverable:** Complete Sheet 10

**Quality Check:**
- ✓ All evidence listed
- ✓ Storage locations accessible
- ✓ Evidence is recent
- ✓ Audit-ready format

#### Phase 9: Gap Analysis & Remediation Planning (2-3 hours)

**Objective:** Identify and prioritize gaps

**Steps:**
1. Review all "Partial" or "Not Compliant" items
2. Categorize gaps:
   - Technical capability gaps
   - Licensing/support gaps
   - Performance gaps
   - Documentation gaps
3. Prioritize by risk
4. Create remediation plan
5. Assign owners
6. Set target dates

**Deliverable:** Gap analysis and remediation plan

**Quality Check:**
- ✓ All gaps identified
- ✓ Risk assessment is realistic
- ✓ Remediation plans are actionable
- ✓ Owners assigned
- ✓ Target dates are reasonable

#### Phase 10: Review & Approval (1-2 hours)

**Objective:** Three-level approval process

**Steps:**
1. **Self-review** (completer)
   - Check completeness
   - Verify accuracy
   - Validate evidence
   - Run quality checklist
   
2. **Technical review** (security/network engineer)
   - Review technical accuracy
   - Validate capability assessments
   - Check evidence quality
   - Approve or request changes
   
3. **Management review** (CISO or delegate)
   - Review gap analysis
   - Approve remediation plan
   - Allocate resources
   - Final approval

**Deliverable:** Approved assessment ready for compliance dashboard

**Quality Check:**
- ✓ All sections complete
- ✓ All reviewers have approved
- ✓ Evidence is audit-ready
- ✓ Gaps have remediation plans

---

## Completing Each Sheet

This section provides detailed guidance for completing each sheet in the workbook.

### Sheet 1: Solution Inventory

#### Purpose

Create a master list of ALL web filtering solutions deployed in your environment. This is your "single source of truth" for what filtering technology exists.

#### What to Document

For EACH filtering solution:
- Solution name (what YOU call it)
- Vendor/provider
- Product name
- Deployment model
- Primary purpose
- Status
- User count
- Integration points

#### Common Mistakes to Avoid

❌ **Incomplete inventory** - Forgetting endpoint filtering, cloud services, or DNS-based filtering  
❌ **Duplicate entries** - Same solution listed multiple times  
❌ **Vague names** - "Web Filter" instead of "Perimeter Web Filter - Fortigate 1000D"  
❌ **Missing cloud services** - Forgetting SaaS-based filtering (Zscaler, Cisco Umbrella, etc.)  
❌ **Ignoring DNS filtering** - DNS-based filtering IS web filtering  

#### How to Complete

**Step 1: Identify All Filtering Solutions**

Ask these questions:
1. What's filtering web traffic at the perimeter?
2. What's filtering on endpoints?
3. What DNS-based filtering is deployed?
4. What cloud filtering services are in use?
5. What's filtering for remote/VPN users?
6. What's filtering for guest networks?
7. Are there any proxy servers?
8. Any filtering for specific segments (OT, guest, IoT)?

**Step 2: For Each Solution, Gather Details**

- Log into admin console
- Check "About" or "System Info" pages
- Document exact version
- Review licensing
- Check deployment architecture
- Count protected users

**Step 3: Fill in the Inventory Sheet**

| Field | How to Complete |
|-------|-----------------|
| **Solution Name** | What YOUR organization calls it (e.g., "Corporate Perimeter Filter", "Endpoint Protection Suite") |
| **Vendor/Provider** | Exact vendor name (Fortigate, Sophos, Zscaler, Cisco, etc.) |
| **Product Name** | Specific product (Fortigate FortiGate 1000D, Zscaler Internet Access, etc.) |
| **Version** | Exact version from admin console |
| **Deployment Model** | Choose: On-Premises Appliance, Virtual Appliance, Cloud SaaS, Hybrid, DNS-Based, Proxy-Based |
| **Primary Purpose** | What's the MAIN reason it's deployed? (Threat Protection, Category Filtering, Compliance, etc.) |
| **Status** | Current operational status: ✅ Deployed / ⚠️ Partial / ❌ Not Deployed / 🔄 Planned |
| **User Count** | Approximate number of protected users |
| **Integration Points** | List key integrations (AD, SIEM, Proxy, DNS, Firewall, etc.) |

**Step 4: Verify Completeness**

- Review with network team
- Cross-check with asset inventory
- Check cloud service subscriptions
- Verify with security team

#### Evidence to Collect

- Network diagrams showing filtering placement
- Screenshots from admin consoles showing version info
- License agreements
- Architecture diagrams

#### Example Entries

```
Solution Name: Corporate Perimeter Filter
Vendor: Fortigate
Product: FortiGate 1000D
Version: 7.4.1
Deployment Model: On-Premises Appliance
Primary Purpose: Threat Protection + Category Filtering
Status: ✅ Deployed
User Count: ~500 (all corporate LAN users)
Integration Points: Active Directory (LDAP), SIEM (Syslog), Firewall (Adjacent)

Solution Name: Endpoint Web Protection
Vendor: Microsoft
Product: Defender for Endpoint
Version: Cloud (Latest)
Deployment Model: Cloud SaaS
Primary Purpose: Threat Protection
Status: ✅ Deployed
User Count: ~500 (all managed endpoints)
Integration Points: Entra ID (Native), Microsoft Sentinel (Native)

Solution Name: DNS Filtering Service
Vendor: Cisco
Product: Cisco Umbrella
Version: Cloud (Latest)
Deployment Model: DNS-Based Cloud
Primary Purpose: Threat Protection + Category Filtering
Status: ✅ Deployed
User Count: ~200 (remote/VPN users)
Integration Points: AD (LDAP), SIEM (API)
```

#### Quality Checklist

Before moving to next sheet, verify:

- [ ] All filtering solutions identified (perimeter, endpoint, cloud, DNS)
- [ ] No duplicate entries
- [ ] Solution names are descriptive
- [ ] Vendor and product names are exact
- [ ] Versions are current (not "Unknown")
- [ ] Deployment models are accurate
- [ ] Status reflects reality (not aspirational)
- [ ] User counts are reasonable estimates
- [ ] Integration points are listed
- [ ] Evidence collected

---

### Sheet 2: Solution Details Template (Create one per solution)

#### Purpose

Document detailed information about EACH filtering solution. You'll create multiple copies of this template - one for each solution listed in Sheet 1.

For example:
- Sheet 2a: Corporate Perimeter Filter (Fortigate)
- Sheet 2b: Endpoint Protection (Microsoft Defender)
- Sheet 2c: DNS Filtering (Cisco Umbrella)

#### What to Document

For EACH solution:
- Complete identification details
- All capability categories (threat protection, URL filtering, logging, etc.)
- Integration points
- Performance metrics
- Licensing details
- Support information

#### How to Complete

**Step 1: Copy the Template**

1. In Excel, right-click on "Sheet 2: Solution_Details_Template"
2. Select "Move or Copy"
3. Check "Create a copy"
4. Place at end
5. Rename to reflect the solution (e.g., "Sheet 2a: Perimeter Filter")

**Step 2: Solution Identification Section**

Fill in these fields from your admin console:

| Field | How to Complete | Where to Find It |
|-------|-----------------|------------------|
| **Solution Name** | What you call it | Your naming |
| **Vendor/Provider** | Company name | Admin console > About |
| **Product/Service** | Specific product | License agreement |
| **Version/Release** | Exact version | Admin console > System > Version |
| **Deployment Model** | How it's deployed | Architecture docs |
| **Deployment Date** | When first deployed | Change records |
| **Deployment Location** | Network segments | Network diagram |
| **Primary Purpose** | Main use case | Design docs |
| **Status** | Current state | Operations team |
| **Scope of Coverage** | What it protects | Architecture |
| **User Count** | Protected users | License count |
| **Integration Points** | What it connects to | Integration docs |

**Step 3: Capability Assessment**

For EACH capability category, assess:

**Threat Protection Capabilities:**
- Anti-malware/anti-virus scanning
- Phishing protection (URL analysis, brand detection)
- Exploit prevention (browser exploits, drive-by downloads)
- Command & control (C2) blocking
- Botnet detection
- Ransomware protection
- Zero-day threat protection
- Threat intelligence integration
- Sandbox/detonation capability
- Real-time threat updates

**URL Categorization & Filtering:**
- URL category database (vendor-provided)
- Number of categories
- Custom categories supported?
- Domain/URL whitelist/blacklist
- Time-based filtering
- User/group-based policies
- Application control
- Keyword filtering
- Safe search enforcement

**Content Inspection:**
- HTTP/HTTPS inspection (SSL/TLS decryption)
- Deep packet inspection
- File type blocking
- File size limits
- Archive inspection (ZIP, RAR, etc.)
- Encoding detection
- Protocol analysis

**Logging & Monitoring:**
- Web transaction logging
- Blocked request logging
- User activity logging
- Admin activity logging
- Log retention period
- Log export formats
- SIEM integration
- Real-time dashboards
- Alerting capabilities

**Access Control:**
- User authentication methods
- Group-based policies
- Time-based access
- Quota management
- Bandwidth management
- Application-level control
- Port/protocol restrictions

**Reporting & Analytics:**
- Built-in reports
- Custom report builder
- Executive dashboards
- User activity reports
- Threat reports
- Compliance reports
- Export capabilities
- Scheduled reports

**Management & Administration:**
- Admin access controls
- Role-based administration
- Configuration backup/restore
- Change logging
- Multi-admin support
- API access
- CLI access
- Remote management

**Performance & Scalability:**
- Throughput capacity
- Concurrent sessions
- Latency impact
- Failover/redundancy
- Load balancing
- Clustering support
- Scalability options

**Integration Capabilities:**
- Active Directory/LDAP
- SIEM integration
- Proxy chaining
- DNS integration
- Firewall integration
- Endpoint agent sync
- Email gateway integration
- DLP integration
- IAM/SSO integration
- Threat intelligence feeds

**Step 4: Rating Scale**

For each capability, use this scale:

| Rating | Description | When to Use |
|--------|-------------|-------------|
| ✅ **Full** | Capability fully deployed and functional | Feature works as expected, no limitations |
| ⚠️ **Partial** | Capability exists but limited/partially deployed | Feature exists but not fully utilized or has limitations |
| ❌ **None** | Capability not available or not deployed | Feature doesn't exist or not configured |
| N/A | Not applicable | Feature not needed for your use case |

**Step 5: Collect Evidence**

For critical capabilities, capture evidence:
- Screenshots from admin console
- Configuration exports (sanitized)
- Test results
- Performance reports
- Integration documentation

**Step 6: Performance Metrics**

Document current performance:
- Uptime (last 30/90 days)
- Average latency
- Peak throughput
- Blocked threats (last 30 days)
- False positive rate
- Incident count

#### Common Mistakes to Avoid

❌ **Checkbox mentality** - Marking "Yes" without understanding the capability  
❌ **Aspirational ratings** - Rating based on what's possible, not what's deployed  
❌ **Missing evidence** - Critical capabilities without supporting evidence  
❌ **Outdated information** - Using data from initial deployment, not current state  
❌ **Ignoring limitations** - Rating "Full" when significant limitations exist  

#### Quality Checklist

For each Sheet 2:

- [ ] Solution identification complete
- [ ] All capability categories assessed
- [ ] Ratings are honest (not optimistic)
- [ ] Evidence collected for critical capabilities
- [ ] Integration points documented
- [ ] Performance data is recent (<30 days)
- [ ] No "Unknown" or "TBD" without explanation
- [ ] Sheet renamed to reflect solution

---

### Sheet 3: Threat Protection Capabilities

#### Purpose

Deep dive into threat protection capabilities across ALL solutions. This sheet consolidates anti-malware, phishing protection, exploit prevention, and other threat-related capabilities.

#### What to Document

For each solution:
- Malware detection capabilities
- Phishing protection methods
- Exploit prevention features
- C2/botnet blocking
- Threat intelligence integration
- Update mechanisms
- Detection rates
- Evidence of capability

#### How to Complete

**Step 1: List All Solutions**

Copy solution names from Sheet 1 into the first column.

**Step 2: Assess Each Threat Protection Category**

**Anti-Malware/Anti-Virus:**
- What malware detection engines are used?
- What file types are scanned?
- Is archive scanning enabled?
- What's the update frequency?
- What's the detection rate?
- How are detections handled (block, quarantine, log)?

**Phishing Protection:**
- URL reputation checking?
- Brand impersonation detection?
- Lookalike domain detection?
- SSL/TLS certificate validation?
- Real-time analysis?
- User reporting mechanisms?

**Exploit Prevention:**
- Browser exploit protection?
- Drive-by download prevention?
- JavaScript analysis?
- PDF/Office document scanning?
- Zero-day protection mechanisms?

**C2/Botnet Detection:**
- Known C2 server blocking?
- Botnet communication detection?
- DNS tunneling detection?
- Algorithmically generated domains (DGA) detection?
- Periodic beaconing detection?

**Threat Intelligence:**
- Which threat intel feeds are used?
- Update frequency?
- Custom threat indicators supported?
- Integration with external TI platforms?
- Automated threat response?

**Step 3: Rating Guidelines**

| Capability | ✅ Full | ⚠️ Partial | ❌ None |
|------------|---------|-----------|---------|
| **Malware Scanning** | Multi-engine, all file types, archives | Single engine, limited file types | Not enabled |
| **Phishing Protection** | Real-time analysis, brand detection, user reporting | URL reputation only | Not enabled |
| **Exploit Prevention** | Browser exploits, document scanning, zero-day | Basic exploit signatures only | Not enabled |
| **C2 Blocking** | Multiple detection methods, DGA detection | Known C2 list only | Not enabled |
| **Threat Intelligence** | Multiple feeds, auto-updates, custom indicators | Single vendor feed | No TI integration |

**Step 4: Document Evidence**

For each "Full" rating, provide evidence:
- Configuration screenshots
- Detection statistics (last 30 days)
- Test results
- Threat feed subscriptions
- Update logs

**Step 5: Identify Gaps**

Where ratings are "Partial" or "None":
- Why doesn't this capability exist?
- Is it a licensing limitation?
- Is it a technical limitation?
- Is it a configuration issue?
- What's the risk if not addressed?
- What's the remediation plan?

#### Common Scenarios

**Scenario 1: Multi-Solution Environment**

You might have:
- Perimeter filter with full anti-malware
- Endpoint protection with advanced threat protection
- DNS filter with C2 blocking

Assessment:
- Each solution gets rated independently
- Document which solution provides which capability
- Identify overlaps (defense in depth) vs. gaps

**Scenario 2: Capability Exists But Not Enabled**

The solution CAN do something but it's not configured:
- Rate as ❌ None (based on CURRENT state)
- Document in notes: "Capability exists but not enabled due to [reason]"
- Include in gap analysis
- Create remediation plan if capability is required

**Scenario 3: Licensing Limitation**

The capability exists in higher tiers but you have basic license:
- Rate as ❌ None
- Document: "Requires [specific license tier]"
- Include cost in remediation plan
- Flag for procurement discussion

#### Evidence Examples

Good evidence:
- Screenshot showing malware engine versions and last update
- Report showing blocked threats (last 30 days)
- Configuration export showing enabled protection modules
- Test results from internal phishing simulation
- Threat feed subscription confirmation
- Performance metrics (throughput, latency)

Poor evidence:
- Generic marketing materials
- Vendor capability statements
- "We think it works" notes
- Outdated screenshots
- No evidence, just "Yes"

#### Quality Checklist

- [ ] All solutions from Sheet 1 are assessed
- [ ] Every threat protection category has a rating
- [ ] "Full" ratings have evidence
- [ ] Gaps are documented
- [ ] Overlapping capabilities noted (defense in depth)
- [ ] Update frequencies documented
- [ ] Detection/block statistics included
- [ ] No "Unknown" without explanation

---

### Sheet 4: Category Filtering Capabilities

#### Purpose

Assess URL categorization and content filtering capabilities across all solutions. This sheet documents what categories are available, how granular filtering is, and what custom controls exist.

#### What to Document

For each solution:
- URL category database details
- Number of categories
- Category granularity
- Custom category support
- Whitelist/blacklist capabilities
- Application control
- Safe search enforcement
- Update mechanisms

#### How to Complete

**Step 1: URL Category Database Assessment**

For each solution, document:

**Database Provider:**
- Who provides the URL database? (Vendor's own, third-party like Brightcloud, Webroot, etc.)
- How many URLs are in the database?
- How many categories exist?
- Update frequency?
- Coverage (what percentage of web is categorized)?

**Category Granularity:**
- How specific are categories?
- Example: "Social Media" vs. "Facebook", "Twitter", "LinkedIn" as separate categories
- Can you control subcategories independently?
- Industry-specific categories available?

**Custom Categories:**
- Can you create custom categories?
- How many custom categories allowed?
- Can you add URLs/domains manually?
- Can you import bulk lists?
- Wildcard support?
- Regular expression support?

**Step 2: Filtering Capability Assessment**

**URL/Domain Lists:**
- Whitelist capability?
- Blacklist capability?
- List size limits?
- Wildcard support?
- Time-based exceptions?
- User/group-specific exceptions?

**Application Control:**
- Does the solution recognize applications (not just URLs)?
- Social media apps?
- Messaging apps?
- File sharing apps?
- Streaming services?
- Gaming platforms?

**Content Analysis:**
- Keyword filtering?
- Language detection?
- Content classification (beyond URL category)?
- Real-time content analysis?
- Image analysis?
- Video content filtering?

**Safe Search Enforcement:**
- Google Safe Search?
- Bing Safe Search?
- YouTube Restricted Mode?
- Other search engines?
- Can users override?

**Time-Based Controls:**
- Schedule-based filtering?
- Different policies by time of day?
- Quota management (e.g., 30 min/day of social media)?
- Bandwidth shaping by category?

**Step 3: Policy Flexibility Assessment**

**User/Group Policies:**
- User-specific policies?
- Group-based policies (by AD group)?
- Role-based policies?
- Device type policies?
- Location-based policies?

**Action Options:**
- Block
- Warn (show message but allow)
- Redirect to safe page
- Time-limited access
- Quota-based access
- Log only (monitor without blocking)

**Step 4: Rating Guidelines**

| Capability | ✅ Full | ⚠️ Partial | ❌ None |
|------------|---------|-----------|---------|
| **URL Database** | Comprehensive (80M+ URLs), 100+ categories, daily updates | Basic (10M URLs), limited categories, weekly updates | No URL categorization |
| **Custom Categories** | Unlimited, bulk import, regex support | Limited number, manual entry only | No custom categories |
| **Whitelist/Blacklist** | Comprehensive, wildcards, time-based | Basic lists, manual entry | No list support |
| **Application Control** | 1000+ apps, granular control | Limited app recognition | No app control |
| **Safe Search** | All major search engines enforced | Some search engines | Not enforced |
| **Policy Flexibility** | User/group/time/quota policies | Basic group policies | Single global policy only |

**Step 5: Document Common Use Cases**

Show how your filtering supports business requirements:

**Example 1: Block social media except lunch hour**
- Social media category: BLOCKED
- Exception: Allow 12:00-13:00
- Applies to: All users except executives
- Evidence: Policy screenshot + test result

**Example 2: Allow educational sites, block others for classroom**
- Classroom group: Custom "Education" category = ALLOW
- All other categories: BLOCK
- Evidence: Group policy + category definition

**Example 3: Block file sharing except IT department**
- File sharing category: BLOCKED
- Exception: IT_Admin AD group = ALLOWED
- Evidence: Group-based policy + AD integration

**Step 6: Assess Coverage Gaps**

Common gaps to check:

**Uncategorized URLs:**
- What happens with uncategorized URLs?
- Default action (allow/block)?
- What percentage of web traffic is uncategorized?
- How do you handle it?

**New/Emerging Categories:**
- AI/ML tools (ChatGPT, etc.)
- Cryptocurrency/NFT sites
- Metaverse platforms
- What's your policy?

**False Categorization:**
- How often are sites miscategorized?
- How do users report issues?
- How quickly are corrections made?
- What's the interim solution?

#### Evidence to Collect

- Category list (screenshot or export)
- Custom category definitions
- Whitelist/blacklist (sanitized)
- Policy examples (screenshots)
- Safe search enforcement proof
- Application control list
- Test results showing policy enforcement

#### Common Mistakes

❌ **Assuming vendor claims** - "They say they have 80M URLs" vs. verifying in admin console  
❌ **Not testing policies** - Policies configured but never tested  
❌ **Ignoring exceptions** - Extensive exceptions undermining overall policy  
❌ **Static lists** - Whitelist/blacklist not reviewed in 2+ years  
❌ **No false positive tracking** - Users complaining but no formal process  

#### Quality Checklist

- [ ] URL database details documented
- [ ] Category count verified (not assumed)
- [ ] Custom categories listed
- [ ] Whitelist/blacklist size documented
- [ ] Policy examples provided
- [ ] Safe search enforcement verified
- [ ] Application control assessed
- [ ] Common use cases documented
- [ ] Gaps identified
- [ ] Evidence collected

---

### Sheet 5: Logging & Monitoring Capabilities

#### Purpose

Assess logging, monitoring, alerting, and reporting capabilities for web filtering. This sheet determines if you can detect issues, investigate incidents, and demonstrate compliance.

#### What to Document

For each solution:
- What logs are collected
- Log retention periods
- Log formats and accessibility
- SIEM integration status
- Real-time monitoring capabilities
- Alerting configurations
- Dashboard availability
- Reporting features

#### How to Complete

**Step 1: Log Collection Assessment**

For each solution, document what is logged:

**Transaction Logs:**
- Every web request (allowed + blocked)?
- Timestamp precision?
- Source IP/user identity?
- Destination URL/domain?
- Category/reputation?
- Action taken (allow/block/warn)?
- Protocol details?
- Data volume (uploaded/downloaded)?

**Security Event Logs:**
- Malware detections?
- Phishing attempts?
- Exploit attempts?
- C2 communications?
- Policy violations?
- Threat intelligence matches?
- DLP violations?

**Administrative Logs:**
- Admin logins?
- Configuration changes?
- Policy modifications?
- Whitelist/blacklist changes?
- User overrides/bypass attempts?
- System health events?

**System Logs:**
- Performance metrics?
- Capacity utilization?
- Errors/warnings?
- Service availability?
- Update events?

**Step 2: Log Retention Assessment**

| Log Type | Retention | Location | Accessibility |
|----------|-----------|----------|---------------|
| Transaction logs | How long? | Where stored? | Who can access? |
| Security events | How long? | Where stored? | Who can access? |
| Admin logs | How long? | Where stored? | Who can access? |
| System logs | How long? | Where stored? | Who can access? |

**Policy Requirements:**
- ISMS-POL-A.8.23, Section 2.4 (Logging and Monitoring) requires ≥90 days retention
- Check if your retention meets this
- Document if shorter retention exists and why

**Storage Considerations:**
- Where are logs stored? (local, central log server, SIEM, cloud)
- Storage capacity adequate?
- Log rotation configured?
- Backup of logs?
- Archive strategy for older logs?

**Step 3: Log Format & Accessibility**

**Log Formats:**
- What format? (Syslog, CEF, LEEF, JSON, CSV, proprietary)
- Structured or unstructured?
- Timezone handling?
- Unicode/international character support?

**Accessibility:**
- How do you query logs? (GUI, CLI, API, SIEM query language)
- Search capabilities? (full-text, field-based, regex)
- Export capabilities?
- Real-time vs. batch access?
- Access controls? (who can see what logs?)

**Step 4: SIEM Integration Assessment**

If you have a SIEM:

**Integration Method:**
- How are logs sent? (Syslog, API, agent, file transfer)
- Real-time or batch?
- What protocol? (TCP/UDP syslog, HTTPS API, etc.)
- Reliable delivery? (acknowledgment, retry logic)

**Data Volume:**
- Logs per second/minute/hour?
- SIEM can handle the volume?
- Any filtering/sampling before SIEM?
- Cost implications (SIEM licensed by volume)?

**Log Parsing:**
- Are logs parsed correctly in SIEM?
- Field extraction working?
- Timestamp parsing correct?
- Enrichment applied? (geolocation, threat intel, asset context)

**Correlation Rules:**
- Are there SIEM correlation rules for web filtering events?
- Example: Multiple blocks for same user → alert
- Example: C2 communication detected → ticket created
- Are rules tested and validated?

**Step 5: Real-Time Monitoring**

**Built-in Dashboards:**
- What dashboards exist in the filtering solution?
- What metrics are shown? (throughput, blocked threats, top users, top categories)
- Real-time or delayed?
- Customizable?
- Access controls?

**External Dashboards:**
- Do you have dashboards in SIEM, Grafana, or other tools?
- What metrics are tracked?
- Update frequency?
- Who monitors them?

**Key Metrics to Monitor:**
- Blocked threat count (by type)
- Policy violations
- Top blocked categories/URLs
- Top users (by allowed/blocked traffic)
- Bandwidth usage by category
- System performance (latency, throughput, uptime)
- Unusual patterns (spikes, drops)

**Step 6: Alerting Capabilities**

**Alert Types:**
- Security alerts (malware, phishing, C2, exploits)
- Policy violation alerts (user exceeded quota, accessed blocked category)
- System alerts (performance degradation, service down, license expiry)
- Operational alerts (logs not being collected, disk space low)

**Alert Configuration:**
- How are alerts configured? (thresholds, conditions, rules)
- Alert severity levels?
- Alert recipients (email, SMS, ticketing system, SIEM)
- Alert escalation?
- Alert suppression/deduplication?

**Alert Testing:**
- Have alerts been tested?
- When was last test?
- Do alerts actually work?
- Response time measured?

**Step 7: Reporting Capabilities**

**Built-in Reports:**
- What reports are available?
- Executive summary reports?
- User activity reports?
- Security threat reports?
- Compliance reports?
- Custom report builder?

**Report Schedule:**
- Can reports be scheduled?
- What frequency? (daily, weekly, monthly)
- Who receives them?
- Format? (PDF, CSV, HTML, email)

**Report Content:**
- Are reports meaningful?
- Actionable insights?
- Trend analysis?
- Comparison to previous periods?
- Compliance metrics included?

**Step 8: Rating Guidelines**

| Capability | ✅ Full | ⚠️ Partial | ❌ None |
|------------|---------|-----------|---------|
| **Transaction Logging** | All requests logged, full details | Some requests logged, limited details | No transaction logs |
| **Security Event Logging** | All security events with context | Some events, basic details | No security logging |
| **Log Retention** | ≥90 days, policy compliant | 30-89 days, not policy compliant | <30 days or no retention |
| **SIEM Integration** | Real-time, parsed, correlated | Batch transfer, basic parsing | No SIEM integration |
| **Dashboards** | Multiple, real-time, customizable | Basic dashboard, limited metrics | No dashboards |
| **Alerting** | Multiple alert types, tested, working | Basic alerts, not fully tested | No alerting |
| **Reporting** | Scheduled, comprehensive, actionable | Manual reports, basic content | No reporting |

#### Evidence to Collect

- Log sample (sanitized) showing log format and fields
- Log retention configuration screenshot
- SIEM integration documentation
- Dashboard screenshots
- Alert configuration screenshots
- Sample reports (executive summary, threat report)
- Alert test results
- Log volume metrics

#### Common Issues

**Issue 1: Logs Collected But Not Reviewed**
- Solution logs to SIEM but no one reviews
- Assessment: Partial logging capability
- Gap: No operational benefit from logs
- Remediation: Create review process, dashboards, alerts

**Issue 2: Log Retention Too Short**
- Logs kept for 30 days, policy requires 90 days
- Assessment: Partial compliance
- Gap: Can't investigate incidents >30 days old
- Remediation: Increase retention (check storage capacity and cost)

**Issue 3: SIEM Integration But Poor Parsing**
- Logs forwarded to SIEM but not parsed correctly
- Assessment: Partial SIEM integration
- Gap: Can't query/correlate effectively
- Remediation: Fix parsing, test field extraction

**Issue 4: Alerts Configured But Never Tested**
- Alert rules exist but no one knows if they work
- Assessment: Partial alerting
- Gap: False confidence in detection
- Remediation: Test all critical alerts, document response procedures

#### Quality Checklist

- [ ] All log types documented
- [ ] Retention periods verified (not assumed)
- [ ] Log format and accessibility assessed
- [ ] SIEM integration status confirmed
- [ ] Dashboards identified and accessed
- [ ] Alerting tested and validated
- [ ] Reporting capabilities assessed
- [ ] Gaps identified and prioritized
- [ ] Evidence collected

---

### Sheet 6: Advanced Capabilities

#### Purpose

Assess advanced and specialized capabilities that enhance security posture beyond basic web filtering. These are often differentiators between solutions and higher-tier licenses.

#### What to Document

For each solution:
- SSL/TLS inspection (HTTPS decryption)
- Data Loss Prevention (DLP) integration
- User behavior analytics
- Sandbox/detonation capability
- API availability
- Multi-tenancy support
- Cloud app control
- Advanced threat protection

#### How to Complete

**Step 1: SSL/TLS Inspection Assessment**

**Capability:**
- Can the solution decrypt and inspect HTTPS traffic?
- Certificate handling (trusted CA, on-the-fly certificate generation)
- Certificate pinning handling
- Certificate error handling

**Coverage:**
- What percentage of HTTPS traffic is inspected?
- Any exclusions? (banking, healthcare, government sites)
- User/group-based exclusions?
- Application-based exclusions?

**Performance Impact:**
- Latency increase from SSL inspection?
- Throughput reduction?
- CPU utilization?
- User complaints?

**Privacy & Legal:**
- Legal review completed?
- User notification/consent?
- HR policy updated?
- Employee privacy concerns addressed?

**Rating:**
- ✅ Full: Comprehensive HTTPS inspection, legal/privacy addressed, minimal performance impact
- ⚠️ Partial: Limited HTTPS inspection or significant exclusions or privacy concerns not fully addressed
- ❌ None: No HTTPS inspection or not enabled

**Step 2: DLP Integration**

**Integration Type:**
- Native DLP in filtering solution?
- Integration with external DLP platform?
- API integration or policy sync?

**DLP Capabilities:**
- What data types can be detected? (PCI, PII, PHI, IP, credentials)
- Pattern matching (regex)?
- Fingerprinting/exact data matching?
- Machine learning classification?

**DLP Actions:**
- Block upload/download?
- Alert only?
- Quarantine?
- Encrypt?
- Redact?

**Coverage:**
- HTTP/HTTPS web uploads?
- Cloud app uploads?
- Email attachments (if applicable)?
- Messaging apps?

**Rating:**
- ✅ Full: Comprehensive DLP, multiple data types, integrated actions
- ⚠️ Partial: Basic DLP or limited coverage
- ❌ None: No DLP capability

**Step 3: User Behavior Analytics (UBA)**

**Behavioral Monitoring:**
- Does solution track user behavior patterns?
- Baseline establishment?
- Anomaly detection?
- Risk scoring?

**Anomalies Detected:**
- Unusual download volume?
- Access to unusual sites/categories?
- Geographic anomalies?
- Time-of-day anomalies?
- Impossible travel?

**Response:**
- Automatic alert on anomaly?
- Increased monitoring/logging?
- Automatic policy tightening?
- Integration with SIEM/SOAR?

**Rating:**
- ✅ Full: Comprehensive UBA, anomaly detection, automated response
- ⚠️ Partial: Basic behavior tracking, manual review needed
- ❌ None: No UBA capability

**Step 4: Sandbox/Detonation**

**Capability:**
- Can solution detonate suspicious files?
- On-premises sandbox or cloud-based?
- What file types supported?
- Automatic or manual submission?

**Analysis:**
- What's analyzed? (file behavior, network connections, registry changes)
- Analysis depth (quick scan vs. deep analysis)?
- Analysis time (seconds, minutes)?
- Verdict reliability?

**Integration:**
- Automatic blocking based on sandbox verdict?
- Manual review option?
- Integration with threat intelligence?
- Quarantine capability?

**Rating:**
- ✅ Full: Automated detonation, comprehensive analysis, integrated blocking
- ⚠️ Partial: Manual detonation or limited file types
- ❌ None: No sandbox capability

**Step 5: API Availability**

**API Type:**
- RESTful API?
- SOAP API?
- GraphQL?
- CLI with structured output?

**API Capabilities:**
- Configuration management via API?
- Log retrieval via API?
- Report generation via API?
- User management via API?
- Allowlist/blocklist management via API?

**API Usage:**
- Current automation using API?
- Integration with ticketing system?
- Integration with orchestration platform?
- Custom scripts/tools?

**Documentation:**
- API documentation quality?
- Examples provided?
- SDKs/libraries available?
- Community support?

**Rating:**
- ✅ Full: Comprehensive API, well-documented, actively used
- ⚠️ Partial: Limited API or not actively used
- ❌ None: No API access

**Step 6: Cloud Application Control**

**Capability:**
- Can solution control cloud app usage?
- Which cloud apps recognized? (O365, Google Workspace, Salesforce, Box, Dropbox, etc.)
- Granular control (e.g., allow email, block file uploads in same app)?

**Cloud App Catalog:**
- How many cloud apps in catalog?
- App risk scoring?
- Shadow IT discovery?
- Sanctioned vs. unsanctioned apps?

**Controls:**
- Block access?
- Read-only access?
- Block file uploads/downloads?
- Block specific actions?
- Require MFA?

**Rating:**
- ✅ Full: Comprehensive cloud app catalog, granular control, shadow IT discovery
- ⚠️ Partial: Limited app catalog or basic block/allow
- ❌ None: No cloud app control

**Step 7: Other Advanced Capabilities**

Document any other specialized capabilities:
- Remote browser isolation
- Virtual desktop/app delivery integration
- Zero Trust Network Access (ZTNA) integration
- CASB functionality
- Advanced malware analysis (behavioral, machine learning)
- Threat hunting capabilities
- Automated response/remediation

#### Evidence to Collect

- HTTPS inspection configuration and certificate
- DLP policy examples and test results
- UBA dashboard/alerts
- Sandbox analysis reports
- API documentation and integration examples
- Cloud app catalog and control policies
- Performance metrics for advanced features

#### Quality Checklist

- [ ] HTTPS inspection assessed (capability, coverage, performance, legal)
- [ ] DLP integration documented
- [ ] UBA capability assessed
- [ ] Sandbox/detonation reviewed
- [ ] API availability confirmed
- [ ] Cloud app control evaluated
- [ ] Other advanced features documented
- [ ] Evidence collected for enabled features
- [ ] Performance impact of advanced features noted

---

### Sheet 7: Licensing & Support Tracking

#### Purpose

Track all licenses, support contracts, and maintenance agreements for web filtering solutions. Ensure no licensing gaps, upcoming expirations are visible, and support coverage is adequate.

#### What to Document

For each solution:
- License type and tier
- User/device count
- Expiration dates
- Days until expiry
- Support contract details
- Maintenance window
- Renewal process
- Costs (if appropriate)

#### How to Complete

**Step 1: License Inventory**

For each solution, document:

**License Details:**
- Solution name (from Sheet 1)
- License type (perpetual, subscription, concurrent, named user, device-based)
- License tier (basic, standard, premium, enterprise)
- Features included in this tier
- Quantity (user count, device count, throughput)

**License Status:**
- Current vs. actual usage
- Overdeployed? (using more than licensed)
- Underutilized? (paying for more than using)
- Compliance status

**Step 2: Expiration Tracking**

**Expiration Dates:**
- License expiration date
- Support contract expiration date
- Maintenance window expiration
- Subscription renewal date

**Days Until Expiry:**
- Calculate days from today
- Flag if <90 days
- Flag if <30 days
- Create renewal timeline

**Impact of Expiration:**
- What happens if license expires? (solution stops working, lose support, no updates)
- Business impact
- Mitigation plan

**Step 3: Support Contract Assessment**

**Support Level:**
- Basic support (email, business hours)
- Standard support (phone, extended hours)
- Premium support (24/7, dedicated engineer)
- On-site support included?

**Response Times:**
- Critical: Target response time
- High: Target response time
- Medium: Target response time
- Low: Target response time

**Support Channels:**
- Email
- Phone
- Web portal
- Chat
- On-site escalation

**Support Experience:**
- When did you last open a ticket?
- How was the response?
- Are response time SLAs met?
- Satisfaction with support quality?

**Step 4: Maintenance & Updates**

**Update Subscription:**
- Are updates included in support contract?
- Frequency of updates (continuous, quarterly, annual)
- Types of updates (features, security, bug fixes)
- Automatic updates or manual?

**Version Currency:**
- Current version deployed
- Latest version available
- How many versions behind?
- Upgrade path
- Upgrade complexity

**Step 5: Renewal Process**

**Renewal Timeline:**
- When to start renewal process? (90 days, 180 days before expiry)
- Who initiates renewal? (IT, procurement, vendor)
- Approval process
- Procurement lead time

**Cost Management:**
- Current license cost
- Expected renewal cost
- Budget available?
- Cost optimization opportunities?

**Vendor Relationship:**
- Primary vendor contact
- Account manager
- Technical account manager
- Contract vehicle (direct, reseller, MSP)

**Step 6: Integration with Procurement**

If your organization uses procurement/asset management systems:
- Is licensing data in that system?
- Is this assessment synced with that data?
- Who is source of truth?
- Update frequency

**Step 7: Rating Guidelines**

| Aspect | ✅ Good | ⚠️ At Risk | ❌ Critical |
|--------|---------|-----------|------------|
| **License Status** | Compliant, current, adequate capacity | Minor overdeployment or approaching capacity | Significant overdeployment or expired |
| **Expiration** | >90 days to expiry, renewal planned | 30-90 days to expiry, renewal in progress | <30 days to expiry or expired |
| **Support Coverage** | Active support, SLAs met, responsive | Basic support, limited hours | No active support or unresponsive vendor |
| **Version Currency** | Current or 1 version behind | 2-3 versions behind | >3 versions behind or EOL |

#### Evidence to Collect

- License agreements (current)
- Support contract (current)
- Proof of purchase
- Vendor invoices
- License keys/activation codes (securely stored)
- Vendor support portal screenshots
- Recent support ticket examples
- Renewal quotes (if available)

#### Common Issues

**Issue 1: License Expiration Not Tracked**
- No central tracking of expiration dates
- Multiple licenses expire at different times
- No proactive renewal process
- Gap: Risk of service interruption
- Remediation: Central license tracking (this sheet!), calendar reminders

**Issue 2: Over-Deployment**
- Licensed for 500 users, protecting 700
- Gap: License violation, audit risk
- Remediation: Purchase additional licenses or reduce deployment scope

**Issue 3: Paying for Unused Licenses**
- Licensed for 1000 users, protecting 400
- Gap: Cost inefficiency
- Remediation: Right-size licenses at renewal

**Issue 4: Support Contract Lapsed**
- Support contract expired 6 months ago
- Can't open tickets, no updates, no patches
- Gap: Security risk, compliance risk
- Remediation: Immediate renewal (may require back-payment)

**Issue 5: Version Currency**
- Running version from 3 years ago
- Gap: Missing security patches, features, vendor may not support old version
- Remediation: Upgrade plan, testing, deployment

#### Quality Checklist

- [ ] All licenses documented
- [ ] Expiration dates verified (not assumed)
- [ ] Days until expiry calculated
- [ ] Support contracts documented
- [ ] Support quality assessed
- [ ] Version currency checked
- [ ] Renewal process defined
- [ ] Evidence collected
- [ ] Costs documented (if appropriate)
- [ ] Upcoming renewals flagged

---

### Sheet 8: Capability Requirements Matrix

#### Purpose

Map policy requirements to deployed solutions. This is your compliance crosswalk - it shows WHAT requirements exist (from policy) and WHICH solutions satisfy them. This sheet reveals gaps that must be closed to achieve compliance.

#### What to Document

For each policy requirement:
- Requirement ID and description
- Which solution(s) provide this capability
- Compliance status (Compliant/Partial/Non-Compliant)
- Evidence availability
- Gap description (if not compliant)
- Remediation plan

#### How to Complete

**Step 1: Extract Policy Requirements**

Read these policy documents:
- ISMS-POL-A.8.23, Section 2.1 (Threat Protection Requirements)
- ISMS-POL-A.8.23, Section 2.2 (Category Filtering Approach)
- ISMS-POL-A.8.23, Section 2.4 (Logging and Monitoring)
- ISMS-POL-A.8.23, Section 3.3 (Exception Management)

List every SHALL, MUST, and SHOULD requirement.

**Step 2: Map Requirements to Solutions**

For each requirement, identify:
- Which solution(s) provide this capability?
- Is the capability fully deployed?
- Is it configured correctly?
- Is it working as expected?

**Example Requirements:**

| Req ID | Requirement | Solutions Providing | Status | Evidence |
|--------|-------------|--------------------| -------|----------|
| REQ-001 | SHALL block known malicious URLs | Perimeter Filter (Fortigate), Endpoint Protection (Defender) | ✅ Compliant | Config screenshot, block logs |
| REQ-002 | SHALL block phishing sites | Perimeter Filter, Endpoint Protection, DNS Filter (Umbrella) | ✅ Compliant | Test results, detection logs |
| REQ-003 | SHOULD support HTTPS inspection | Perimeter Filter (capable but not enabled) | ⚠️ Partial | Capability exists, not deployed |
| REQ-004 | SHALL log filtering events | All solutions | ✅ Compliant | Log samples from all solutions |
| REQ-005 | SHALL retain logs for ≥90 days | Perimeter Filter (90 days), Endpoint (30 days), DNS (180 days) | ⚠️ Partial | Endpoint logs only 30 days |
| REQ-006 | MUST support threat feed updates | All solutions | ✅ Compliant | Update schedules, last update timestamps |
| REQ-007 | SHOULD support user-based policies | Perimeter Filter (yes), Endpoint (yes), DNS (no) | ⚠️ Partial | DNS filter is IP-based only |
| REQ-008 | SHALL provide administrative audit logs | All solutions | ✅ Compliant | Admin log samples |
| REQ-009 | MUST have configuration backup capability | Perimeter (yes), Endpoint (cloud-based), DNS (cloud-based) | ✅ Compliant | Backup schedules |
| REQ-010 | SHOULD integrate with SIEM | Perimeter (yes), Endpoint (yes), DNS (no) | ⚠️ Partial | DNS logs not in SIEM yet |

**Step 3: Compliance Status Definitions**

Use these criteria:

| Status | Definition | When to Use |
|--------|------------|-------------|
| ✅ **Compliant** | Requirement fully met by one or more solutions | All aspects of requirement are satisfied, evidence exists, capability is operational |
| ⚠️ **Partial** | Requirement partially met or met by some solutions but not others | Capability exists but not fully deployed, OR some solutions comply but gaps exist |
| ❌ **Non-Compliant** | Requirement not met by any solution | Capability doesn't exist or not deployed at all |
| N/A | Not applicable | Requirement doesn't apply to your environment (document why) |

**Step 4: Evidence Assessment**

For each requirement, assess evidence:

| Evidence Status | Meaning |
|-----------------|---------|
| **Yes** | Evidence collected and documented |
| **No** | No evidence available (this is a gap!) |
| **Partial** | Some evidence but not complete |

If evidence = No, add to gap list and collect evidence.

**Step 5: Gap Analysis**

For every "Partial" or "Non-Compliant" requirement:

**Document the Gap:**
- What specifically is missing?
- Why is it missing? (technical limitation, budget, not implemented, etc.)
- What's the risk if not addressed?
- What's the business impact?

**Remediation Plan:**
- What needs to be done?
- Who's responsible?
- What resources are needed?
- Target completion date
- Dependencies

**Example Gap Analysis:**

**Gap: REQ-005 - Endpoint logs only retained 30 days**
- **Missing:** 60 additional days of log retention
- **Why:** Default cloud retention setting
- **Risk:** Can't investigate incidents >30 days old, non-compliant with policy
- **Impact:** Audit finding, inability to meet forensic requirements
- **Remediation:** Configure extended retention in cloud console
- **Owner:** Security Operations team
- **Cost:** $200/month for additional storage
- **Target Date:** 30 days
- **Dependencies:** Budget approval

**Gap: REQ-007 - DNS filter doesn't support user-based policies**
- **Missing:** User-based policy enforcement in DNS filtering
- **Why:** Technical limitation of current DNS filtering product (IP-based only)
- **Risk:** Less granular control for remote users
- **Impact:** Inconsistent policy enforcement for remote vs. office users
- **Remediation:** Upgrade to DNS solution with AD integration OR accept risk (remote users get less granular filtering)
- **Owner:** Network Engineering team
- **Cost:** $10,000/year license upgrade OR $0 (accept risk)
- **Target Date:** Next license renewal (6 months)
- **Dependencies:** Product evaluation, budget approval

**Step 6: Calculate Compliance Metrics**

**Overall Compliance:**
```
Total Requirements: 10
Compliant: 6 (60%)
Partial: 3 (30%)
Non-Compliant: 1 (10%)
```

**Compliance by Category:**
```
Threat Protection: 8 requirements, 75% compliant
Category Filtering: 5 requirements, 100% compliant
Logging & Monitoring: 4 requirements, 50% compliant (2 partial gaps)
Exception Management: 3 requirements, 100% compliant
```

**Trend (if this is a quarterly update):**
```
Q1 2026: 60% compliant
Q4 2025: 50% compliant
Q3 2025: 40% compliant
Trend: IMPROVING (+20% YoY)
```

#### Evidence to Collect

- Policy documents (as reference)
- Configuration screenshots proving compliance
- Test results
- Log samples
- Integration documentation
- Gap remediation plans
- Management approval for accepted risks

#### Common Mistakes

❌ **Optimistic assessment** - Marking "Compliant" when actually "Partial"  
❌ **Assuming capability** - "We think it does that" vs. verifying  
❌ **Ignoring SHALL vs. SHOULD** - All requirements matter, even SHOULD  
❌ **No remediation plans** - Identifying gaps without fixing them  
❌ **Evidence gap** - Claiming compliance without evidence  

#### Quality Checklist

- [ ] All policy requirements extracted
- [ ] Every requirement mapped to solution(s)
- [ ] Compliance status is honest (not optimistic)
- [ ] Evidence assessed for each requirement
- [ ] All gaps documented with remediation plans
- [ ] Compliance metrics calculated
- [ ] Management review of gaps and plans
- [ ] Accepted risks formally documented

---

### Sheet 9: Performance & Incident Tracking

#### Purpose

Track performance metrics, reliability, and incidents for all filtering solutions. This sheet provides operational visibility and helps identify chronic issues requiring attention.

#### What to Document

For each solution:
- Uptime/availability
- Performance metrics (latency, throughput)
- Capacity utilization
- Incident history
- Mean Time To Detect (MTTD)
- Mean Time To Resolve (MTTR)
- Recurring issues

#### How to Complete

**Step 1: Uptime & Availability Tracking**

For each solution, document:

**Availability Metrics:**
- Uptime (last 30 days): X%
- Uptime (last 90 days): Y%
- Availability target/SLA: Z%
- Downtime incidents: Count and duration
- Planned maintenance windows: Count and duration

**Calculation:**
```
Uptime % = (Total minutes - Downtime minutes) / Total minutes × 100

Example:
Last 30 days = 43,200 minutes
Downtime = 120 minutes (2 hours across 2 incidents)
Uptime = (43,200 - 120) / 43,200 × 100 = 99.72%
```

**Step 2: Performance Metrics**

**Latency:**
- Average latency added by filtering: X ms
- 95th percentile latency: Y ms
- Maximum observed latency: Z ms
- User complaints about performance: Yes/No

**Throughput:**
- Current average throughput: X Mbps or requests/second
- Peak throughput: Y Mbps
- Capacity limit: Z Mbps
- Utilization: (Current / Capacity) × 100 = %

**Resource Utilization:**
- CPU utilization: Average / Peak
- Memory utilization: Average / Peak
- Disk utilization: Current / Maximum
- Network utilization: Average / Peak

**Step 3: Incident Tracking**

For each incident (last 90 days):

**Incident Details:**
- Incident ID (from ticketing system)
- Date/time
- Duration
- Impact (users affected, service degradation)
- Root cause
- Resolution
- Recurrence (is this a repeat issue?)

**Incident Categories:**
- Service outage (complete failure)
- Performance degradation (slow but working)
- Configuration error (misconfiguration causing issues)
- False positives (legitimate sites blocked)
- False negatives (threats not blocked)
- Integration failure (SIEM, AD, etc. not working)
- Licensing issue (expiration, over-deployment)
- Hardware failure (for appliance-based)
- Software bug
- External dependency (ISP, cloud provider, etc.)

**Example Incident Log:**

| Incident | Date | Duration | Impact | Category | Root Cause | Resolution | Recurrence? |
|----------|------|----------|--------|----------|------------|------------|-------------|
| INC-12345 | 10.01.2026 | 45 min | 200 users | Service outage | Disk full (logs not rotated) | Cleared logs, fixed rotation | No (fixed) |
| INC-12348 | 15.01.2026 | 2 hours | All users | Performance degradation | HTTPS inspection CPU spike | Excluded heavy traffic sites | No (fixed) |
| INC-12350 | 18.01.2026 | 15 min | 50 users | False positive | Legitimate site miscategorized | Added to whitelist, reported to vendor | Yes (recurring) |
| INC-12355 | 25.01.2026 | 4 hours | All users | Integration failure | SIEM not receiving logs (network issue) | Fixed network ACL | No (fixed) |

**Step 4: Calculate MTTD and MTTR**

**Mean Time To Detect (MTTD):**
```
MTTD = Average time from incident start to incident detection

Example:
Incident 1: Detected after 5 minutes
Incident 2: Detected after 15 minutes
Incident 3: Detected after 10 minutes
MTTD = (5 + 15 + 10) / 3 = 10 minutes
```

**Mean Time To Resolve (MTTR):**
```
MTTR = Average time from incident detection to incident resolution

Example:
Incident 1: 45 minutes
Incident 2: 120 minutes
Incident 3: 15 minutes
MTTR = (45 + 120 + 15) / 3 = 60 minutes
```

**Target vs. Actual:**
- Target MTTD: ≤15 minutes → Actual: 10 minutes (✅ Meeting target)
- Target MTTR: ≤30 minutes → Actual: 60 minutes (⚠️ Not meeting target)

**Step 5: Recurring Issue Analysis**

Identify issues that occur repeatedly:

**Recurring Issue Template:**
- **Issue:** What keeps happening?
- **Frequency:** How often? (daily, weekly, monthly)
- **Impact:** What's affected each time?
- **Temporary Fix:** How is it resolved each time?
- **Root Cause:** Why does it keep happening?
- **Permanent Fix:** What's needed to prevent recurrence?
- **Owner:** Who will implement permanent fix?
- **Status:** Not started / In progress / Planned / Closed

**Example:**
- **Issue:** Specific legitimate business site keeps getting blocked
- **Frequency:** 2-3 times per month
- **Impact:** 10-20 users can't access site, productivity impact
- **Temporary Fix:** Add to whitelist each time
- **Root Cause:** Site uses dynamic IPs/CDNs, vendor database miscategorizes
- **Permanent Fix:** Create wildcard whitelist entry, escalate to vendor for permanent database fix
- **Owner:** Security Operations
- **Status:** In progress

**Step 6: Performance Trends**

Track trends over time (monthly):

| Month | Uptime | Avg Latency | Peak Throughput | Incidents | MTTR |
|-------|--------|-------------|-----------------|-----------|------|
| Jan 2026 | 99.7% | 8ms | 450 Mbps | 4 | 60 min |
| Dec 2025 | 99.5% | 7ms | 420 Mbps | 5 | 75 min |
| Nov 2025 | 99.8% | 9ms | 400 Mbps | 3 | 45 min |

**Trend Analysis:**
- Uptime: Stable (good)
- Latency: Stable (acceptable)
- Throughput: Increasing (approaching capacity? Monitor.)
- Incidents: Decreasing (good)
- MTTR: Improving (good)

#### Evidence to Collect

- Uptime reports from monitoring system
- Performance graphs (latency, throughput, resource utilization)
- Incident tickets (from ticketing system)
- Resolution documentation
- Post-incident reviews
- Capacity planning reports

#### Common Issues

**Issue: No Performance Baseline**
- Don't know what "normal" looks like
- Can't identify degradation
- Remediation: Establish baseline over 30 days, document normal ranges

**Issue: Incidents Not Documented**
- Issues occur but not tracked in ticketing system
- Can't calculate MTTD/MTTR
- Can't identify recurring issues
- Remediation: Enforce ticketing discipline, retrospective incident documentation

**Issue: Capacity Not Monitored**
- Don't know utilization level
- Surprise when hitting capacity limits
- Remediation: Implement capacity monitoring, set thresholds at 70% and 85%

**Issue: No Root Cause Analysis**
- Incidents resolved but root cause unknown
- Recurrence likely
- Remediation: Require RCA for all major incidents, document in ticket

#### Quality Checklist

- [ ] Uptime calculated for all solutions
- [ ] Performance metrics documented
- [ ] Capacity utilization tracked
- [ ] All incidents (last 90 days) documented
- [ ] MTTD and MTTR calculated
- [ ] Recurring issues identified
- [ ] Performance trends analyzed
- [ ] Evidence collected (reports, tickets)
- [ ] Capacity concerns flagged

---

### Sheet 10: Evidence Registry

#### Purpose

Central registry of ALL evidence collected during this assessment. This sheet provides an audit trail and makes it easy for auditors to find supporting documentation.

#### What to Document

For each piece of evidence:
- Evidence ID
- Description
- Category
- Related requirement/sheet
- Evidence type (screenshot, config export, report, etc.)
- Storage location
- Collection date
- Collected by
- Audit-ready status

#### How to Complete

**Step 1: Collect Evidence Throughout Assessment**

As you complete each sheet, collect evidence:
- Take screenshots with timestamps
- Export configurations (sanitized)
- Generate reports
- Capture logs (sanitized)
- Document integrations
- Record test results

**Step 2: Organize Evidence**

Create a folder structure:
```
Evidence/
├── Sheet1_Solution_Inventory/
│   ├── Network_Diagram_20260115.png
│   ├── Fortigate_Version_Screenshot.png
│   ├── License_Agreement_Fortigate.pdf
├── Sheet2_Solutions/
│   ├── Fortigate_Capability_Dashboard.png
│   ├── Defender_Config_Export.xml
│   ├── Umbrella_Integration_Diagram.png
├── Sheet3_Threat_Protection/
│   ├── Malware_Detection_Report_30days.pdf
│   ├── Phishing_Test_Results.xlsx
│   ├── Threat_Feed_Config.png
├── Sheet7_Licensing/
│   ├── Fortigate_License_Agreement.pdf
│   ├── Support_Contract_Cisco.pdf
├── Sheet8_Requirements/
│   ├── Compliance_Test_Results.xlsx
│   ├── Gap_Remediation_Plan.docx
├── Sheet9_Performance/
│   ├── Uptime_Report_90days.pdf
│   ├── Performance_Graphs.png
│   ├── Incident_Tickets_Export.csv
```

**Step 3: Fill in Evidence Registry**

For each evidence item:

| Field | Description | Example |
|-------|-------------|---------|
| **Evidence ID** | Unique ID | EVD-001, EVD-002, etc. |
| **Description** | What is this evidence? | Network diagram showing filtering placement |
| **Category** | Type of evidence | Technical Architecture |
| **Related To** | Which sheet/requirement? | Sheet 1 (Solution Inventory), REQ-001 |
| **Evidence Type** | Format | Network Diagram (PNG) |
| **File Name** | Actual file name | Network_Diagram_20260115.png |
| **Storage Location** | Where is it stored? | Evidence/Sheet1_Solution_Inventory/ |
| **Collection Date** | When collected? | 15.01.2026 |
| **Collected By** | Who collected it? | John Smith (Network Engineer) |
| **Audit-Ready?** | Ready for auditor? | Yes/No |

**Example Entries:**

| ID | Description | Category | Related To | Type | File Name | Location | Date | By | Audit-Ready? |
|----|-------------|----------|------------|------|-----------|----------|------|-----|--------------|
| EVD-001 | Network diagram showing filtering placement | Architecture | Sheet 1 | PNG | Network_Diagram_20260115.png | Evidence/Sheet1/ | 15.01.2026 | J. Smith | Yes |
| EVD-002 | Fortigate version and license info | Configuration | Sheet 1, 7 | Screenshot | Fortigate_Version.png | Evidence/Sheet1/ | 15.01.2026 | J. Smith | Yes |
| EVD-003 | Malware detection report (30 days) | Security | Sheet 3, REQ-001 | PDF | Malware_Report_Dec2025.pdf | Evidence/Sheet3/ | 10.01.2026 | S. Jones | Yes |
| EVD-004 | SIEM integration config | Integration | Sheet 5, REQ-010 | Config Export | SIEM_Integration.xml | Evidence/Sheet5/ | 12.01.2026 | A. Brown | Yes |
| EVD-005 | Fortigate support contract | Legal | Sheet 7 | PDF | Fortigate_Support_Contract.pdf | Evidence/Sheet7/ | 15.01.2026 | Procurement | Yes |
| EVD-006 | Uptime report (90 days) | Operations | Sheet 9 | PDF | Uptime_Report_Q4_2025.pdf | Evidence/Sheet9/ | 15.01.2026 | Ops Team | Yes |
| EVD-007 | Gap remediation plan | Compliance | Sheet 8 | DOCX | Gap_Remediation_Plan_Jan2026.docx | Evidence/Sheet8/ | 18.01.2026 | CISO | Yes |

**Step 4: Audit-Ready Checklist**

For evidence to be audit-ready:
- [ ] Clear, readable quality
- [ ] Timestamps visible (when applicable)
- [ ] Sensitive data sanitized (passwords, PII, internal IPs)
- [ ] Context provided (what are we looking at?)
- [ ] Source identified (which system/solution?)
- [ ] Collection date recent (<90 days preferred)
- [ ] File format accessible (PDF, PNG, XLSX - not proprietary)
- [ ] Organized and labeled clearly

**Step 5: Sanitization Guidelines**

Before collecting evidence, sanitize:

**Always Redact:**
- Passwords, API keys, secrets
- Internal IP addresses (replace with 10.x.x.x or description)
- Employee names (unless relevant)
- Customer data
- Proprietary algorithms
- License keys (just show that it exists, not the actual key)

**Sanitization Example:**

BEFORE (don't include):
```
Database Server: 192.168.50.10
API Key: sk_live_51234567890abcdefghij
Admin Password: MyS3cretP@ssw0rd!
```

AFTER (sanitized):
```
Database Server: [Internal_DB_Server]
API Key: sk_live_**********************ij
Admin Password: [Configured - Not Shown]
```

#### Evidence Categories

Organize evidence by these categories:
- **Architecture** - Network diagrams, deployment diagrams, integration diagrams
- **Configuration** - Config exports, policy screenshots, settings
- **Security** - Threat reports, detection logs, test results
- **Performance** - Uptime reports, performance graphs, capacity reports
- **Compliance** - Gap analysis, remediation plans, audit reports
- **Legal** - Licenses, contracts, agreements
- **Operational** - Incident tickets, change records, maintenance logs
- **Integration** - Integration documentation, API configs, log forwarding
- **Testing** - Test results, validation reports, proof-of-concept

#### Quality Checklist

- [ ] All evidence collected throughout assessment
- [ ] Evidence organized in clear folder structure
- [ ] Every piece of evidence registered in this sheet
- [ ] Evidence IDs unique and traceable
- [ ] Sensitive data sanitized
- [ ] All evidence is audit-ready quality
- [ ] Storage location accessible to auditors
- [ ] Collection dates recent
- [ ] Collectors identified
- [ ] No missing evidence for critical requirements

---

## Evidence Collection Best Practices

### General Guidelines

**Quality Over Quantity:**
- One high-quality screenshot > ten poor quality images
- Focus on evidence that PROVES compliance, not just suggests it
- Clear, readable, well-labeled evidence

**Timeliness:**
- Collect evidence when fresh (don't delay)
- Date all evidence
- Use timestamps in screenshots when possible
- Evidence >90 days old may not be accepted by auditors

**Organization:**
- Use consistent naming conventions
- Group by sheet/requirement
- Create an index (Sheet 10)
- Make it easy for auditors to find what they need

### Evidence Types

**Screenshots:**
- Capture entire window (show browser URL bar or app title)
- Include timestamps when possible
- Show enough context to understand what we're looking at
- Use annotation tools to highlight key information
- Save in PNG or JPEG format
- Resolution should be readable (not tiny)

**Configuration Exports:**
- Export from admin console when possible
- Sanitize before saving
- Include metadata (export date, system version)
- Save in accessible format (XML, JSON, CSV, not proprietary)

**Reports:**
- Use system-generated reports when possible
- Include report generation date
- Include timeframe covered (e.g., "Last 30 days")
- Executive summary sufficient, don't need raw data dumps

**Log Samples:**
- Sanitize before collecting
- Show log format and fields
- Include recent timestamp (prove logs are current)
- Don't need thousands of lines - just representative samples

**Test Results:**
- Document test methodology
- Include test date
- Show both positive (works) and negative (blocked) results
- Include screenshots of test execution

### Storage & Access

**Storage Options:**
- Secure file share (access-controlled)
- ISMS documentation repository
- Evidence management system (if available)
- Cloud storage (encrypted, access-controlled)

**Access Control:**
- Who needs access? (assessment team, auditors, management)
- Implement access controls
- Log access for audit trail
- Don't email evidence (use secure links)

**Retention:**
- Keep evidence for audit cycle (typically 1 year minimum)
- After audit, archive but don't delete
- Useful for year-over-year comparison

### Common Evidence Gaps

**Gap 1: "We do this but have no evidence"**
- Problem: Claiming compliance without proof
- Solution: Generate evidence retroactively if possible, or acknowledge gap

**Gap 2: Evidence exists but not collected**
- Problem: Evidence available but not documented
- Solution: Go back and collect it, update registry

**Gap 3: Evidence too old**
- Problem: Screenshots from 2 years ago
- Solution: Collect fresh evidence, show current state

**Gap 4: Evidence not sanitized**
- Problem: Sensitive data exposed in evidence
- Solution: Re-capture with sanitization, or redact before sharing

**Gap 5: Evidence not organized**
- Problem: Random files in random folders
- Solution: Organize per Sheet 10, create clear structure

---

## Common Pitfalls

This section highlights common mistakes to avoid when completing this assessment.

### Pitfall 1: Incomplete Solution Inventory

**Mistake:** Not identifying all filtering solutions in the environment

**Example:** Forgetting about:
- DNS-based filtering for remote users
- Endpoint protection that includes web filtering
- Cloud proxy services (Zscaler, Netskope, etc.)
- Specific segment filtering (OT, guest network, IoT)

**Why It Happens:**
- Focusing only on perimeter filtering
- Different teams manage different solutions
- Cloud services not tracked in asset inventory
- Endpoint features overlooked

**How to Avoid:**
- Ask network, security, and endpoint teams
- Review architecture diagrams
- Check cloud service subscriptions
- Walk through user workflows (office, remote, VPN, guest)

### Pitfall 2: Aspirational Assessment

**Mistake:** Rating capabilities based on what's POSSIBLE, not what's DEPLOYED

**Example:**
- Solution CAN do HTTPS inspection → rate as "Full"
- Reality: HTTPS inspection NOT enabled → should be "None"

**Why It Happens:**
- Pressure to show compliance
- Confusion about capability vs. deployment
- Optimism bias

**How to Avoid:**
- Rate current state, not future state
- Verify in admin console (don't assume)
- Test critical capabilities
- Document gaps honestly

### Pitfall 3: Missing Evidence

**Mistake:** Claiming compliance without supporting evidence

**Example:**
- Claim: "We block malware"
- Evidence: None (or just "Yes")
- Auditor: "Prove it"

**Why It Happens:**
- Assuming evidence exists
- Not collecting evidence during assessment
- Thinking description is enough

**How to Avoid:**
- Collect evidence as you go
- For every "Compliant" rating, collect evidence
- Use Sheet 10 (Evidence Registry)
- Think like an auditor: "What would I want to see?"

### Pitfall 4: Ignoring Partial Gaps

**Mistake:** Treating "Partial" as acceptable and not creating remediation plans

**Example:**
- Requirement: SHALL retain logs for ≥90 days
- Current: Retain for 30 days
- Assessment: "Partial" but no remediation plan

**Why It Happens:**
- "Close enough" mindset
- Assuming partial compliance is sufficient
- Remediation seems hard/expensive

**How to Avoid:**
- Every "Partial" requires a remediation plan
- Even if remediation is "accept risk" (document it)
- Prioritize based on risk
- Get management buy-in

### Pitfall 5: Data Quality Issues

**Mistake:** Inaccurate, outdated, or inconsistent data

**Examples:**
- Version numbers from 2 years ago
- User counts that don't match reality
- Performance data from initial deployment
- License counts that don't match procurement records

**Why It Happens:**
- Copy-paste from old assessments
- Not verifying in admin console
- Assumptions instead of facts

**How to Avoid:**
- Verify every data point
- Check admin consoles (don't assume)
- Cross-reference with other systems (asset inventory, procurement)
- Date all evidence

### Pitfall 6: Siloed Assessment

**Mistake:** Completing assessment in isolation without input from other teams

**Example:**
- Security team completes assessment
- Network team not consulted (they manage some solutions)
- Endpoint team not involved (they manage endpoint filtering)
- Result: Incomplete and inaccurate

**Why It Happens:**
- Assuming one team knows everything
- Not knowing who else is involved
- Time pressure

**How to Avoid:**
- Identify all stakeholders upfront
- Schedule collaboration sessions
- Review drafts with all teams
- Three-level approval process ensures review

### Pitfall 7: No Remediation Follow-Through

**Mistake:** Identifying gaps but never fixing them

**Example:**
- Assessment Q1 2026: "Gap: HTTPS inspection not enabled"
- Assessment Q2 2026: Same gap
- Assessment Q3 2026: Same gap
- Assessment Q4 2026: Same gap

**Why It Happens:**
- No ownership assigned
- No budget allocated
- Competing priorities
- "Assessment fatigue" (endless gap lists)

**How to Avoid:**
- Assign owners to every gap
- Get management commitment
- Set realistic timelines
- Track progress
- Escalate stalled remediations

### Pitfall 8: Copy-Paste Errors

**Mistake:** Copying content from other assessments or solutions without customization

**Example:**
- Sheet 2a (Fortigate) says "Cloud-based SaaS deployment"
- Reality: It's an on-premises appliance
- Reason: Copied from Sheet 2b (Zscaler) template

**Why It Happens:**
- Rushing through assessment
- Template reuse without customization
- Not reading what was pasted

**How to Avoid:**
- Review each entry carefully
- Verify facts in admin console
- Use templates as a starting point, not final content
- Quality review process

### Pitfall 9: Overlooking Integration Failures

**Mistake:** Assuming integrations work because they're configured

**Example:**
- SIEM integration configured
- Logs NOT actually flowing to SIEM
- Assessment: "Integrated with SIEM" ✅
- Reality: Integration broken for 3 months

**Why It Happens:**
- Checking configuration, not operation
- No validation/testing
- Integration set up once and forgotten

**How to Avoid:**
- Test every integration
- Check logs in destination system
- Verify data flow
- Include integration health in monitoring

### Pitfall 10: Ignoring Performance Impact

**Mistake:** Not documenting performance impact of filtering, especially HTTPS inspection

**Example:**
- Enable HTTPS inspection
- Users experience slowdowns
- Help desk flooded with complaints
- Assessment doesn't mention performance issues

**Why It Happens:**
- Focusing only on security capabilities
- Not monitoring user experience
- Not collecting feedback

**How to Avoid:**
- Monitor latency before/after changes
- Track user complaints
- Include performance metrics in assessment
- Balance security vs. usability

---

## Quality Checklist

Before submitting assessment for review, verify:

### Completeness

- [ ] All sheets completed (no blank sheets)
- [ ] All solutions from Sheet 1 have detailed assessment (Sheet 2)
- [ ] All capability categories assessed (Sheets 3-6)
- [ ] All policy requirements mapped (Sheet 8)
- [ ] Performance data collected (Sheet 9)
- [ ] Evidence registered (Sheet 10)

### Accuracy

- [ ] All data verified in admin consoles (not assumed)
- [ ] Version numbers current (<30 days old)
- [ ] User counts accurate (±10%)
- [ ] License counts match procurement records
- [ ] Performance data recent (<30 days)
- [ ] No copy-paste errors

### Honesty

- [ ] Ratings reflect CURRENT state, not aspirational
- [ ] Gaps documented honestly (not hidden)
- [ ] "Partial" ratings justified
- [ ] Limitations acknowledged
- [ ] No "Unknown" without explanation

### Evidence

- [ ] Evidence collected for all "Compliant" ratings
- [ ] Critical capabilities have supporting evidence
- [ ] All evidence sanitized (no passwords, internal IPs)
- [ ] Evidence organized and indexed (Sheet 10)
- [ ] Evidence is audit-ready quality

### Remediation

- [ ] All gaps have remediation plans
- [ ] Owners assigned to each gap
- [ ] Target dates set
- [ ] Resources identified (budget, tools, people)
- [ ] Management approval for major remediations

### Integration

- [ ] All integrations tested and verified working
- [ ] SIEM integration confirmed (logs actually flowing)
- [ ] AD/LDAP integration validated (user mapping works)
- [ ] API integrations tested
- [ ] Monitoring dashboards accessible

### Stakeholder Input

- [ ] Network team reviewed (for infrastructure accuracy)
- [ ] Security team reviewed (for capability assessment)
- [ ] Operations team reviewed (for performance data)
- [ ] Procurement reviewed (for licensing accuracy)
- [ ] Management reviewed (for gap priorities)

### Consistency

- [ ] No contradictions between sheets
- [ ] Solution names consistent across all sheets
- [ ] Compliance status consistent with evidence
- [ ] Gaps in Sheet 8 match capability assessments in Sheets 3-6

---

## Review & Approval

### Three-Level Approval Process

This assessment requires approval from three levels before it's considered complete and audit-ready.

#### Level 1: Technical Review

**Reviewer:** Security Engineer or Network Engineer (peer review)

**Focus:**
- Technical accuracy
- Capability assessments correct?
- Integration details accurate?
- Performance data reasonable?
- Evidence quality acceptable?

**Review Checklist:**
- [ ] Solution inventory complete
- [ ] Capability ratings accurate
- [ ] Integration details correct
- [ ] Performance data recent
- [ ] Technical evidence present

**Outcome:**
- Approve → Move to Level 2
- Request Changes → Return to completer with feedback

#### Level 2: Compliance Review

**Reviewer:** Information Security Manager or Compliance Officer

**Focus:**
- Policy compliance
- Requirements correctly mapped?
- Gaps properly identified?
- Remediation plans realistic?
- Evidence audit-ready?

**Review Checklist:**
- [ ] All policy requirements addressed
- [ ] Compliance status honest
- [ ] Gaps documented with plans
- [ ] Evidence is audit-ready
- [ ] No missing evidence for critical items

**Outcome:**
- Approve → Move to Level 3
- Request Changes → Return with feedback

#### Level 3: Management Approval

**Reviewer:** CISO, IT Director, or CTO

**Focus:**
- Strategic alignment
- Gap priorities acceptable?
- Resource allocation needed?
- Risk acceptance decisions?
- Budget implications understood?

**Review Checklist:**
- [ ] Gap priorities align with business risk
- [ ] Remediation plans are funded/resourced
- [ ] Accepted risks formally documented
- [ ] Timelines are realistic
- [ ] Overall assessment credible

**Outcome:**
- Approve → Assessment complete, ready for audit
- Request Changes → Return with feedback
- Escalate Issues → Discuss with executive leadership

### Approval Documentation

Document each approval:

| Level | Reviewer | Role | Review Date | Status | Comments |
|-------|----------|------|-------------|--------|----------|
| 1 | John Smith | Security Engineer | 18.01.2026 | Approved | Minor corrections to Sheet 3, otherwise good |
| 2 | Jane Doe | Compliance Officer | 20.01.2026 | Approved | Evidence quality excellent, ready for audit |
| 3 | Bob Wilson | CISO | [Date] | Approved | Approved gap priorities and Q1 remediation plan |

### Post-Approval Actions

Once approved:
1. Lock the assessment (no further edits without change control)
2. Store in ISMS documentation repository
3. Notify auditors that assessment is available
4. Begin remediation work on identified gaps
5. Schedule quarterly update

---

## Next Steps After Completion

### 1. Proceed to Other A.8.23 Assessments

This assessment (A.8.23.1) is now complete. Use the data collected here as INPUT to:

**A.8.23.2 - Network Coverage Assessment:**
- Use Sheet 1 (Solution Inventory) to identify what solutions need coverage assessment
- Use deployment models from Sheet 2 to understand where solutions are deployed

**A.8.23.3 - Policy Configuration Assessment:**
- Use capability data (Sheets 3-6) to understand what's configurable
- Use Sheet 8 (Requirements Matrix) to understand policy requirements

**A.8.23.4 - Monitoring & Response Assessment:**
- Use logging capabilities (Sheet 5) to assess what can be monitored
- Use SIEM integration details to understand log flows

**A.8.23.5 - Compliance Dashboard:**
- This assessment's data feeds into the consolidated compliance view
- Gap analysis from Sheet 8 is a key input

### 2. Execute Remediation Plans

From Sheet 8 (Gap Analysis):
1. Review prioritized gaps with management
2. Allocate resources (budget, people, time)
3. Assign ownership
4. Set milestones
5. Track progress
6. Update assessment as gaps are closed

### 3. Quarterly Updates

This assessment should be updated quarterly:

**What to Update:**
- Sheet 1: Any new solutions deployed?
- Sheet 2: Version updates, capability changes
- Sheet 7: License renewals, expirations
- Sheet 8: Gap closure progress
- Sheet 9: Performance trends, incidents
- Sheet 10: New evidence

**When to Update:**
- Quarterly (Q1, Q2, Q3, Q4)
- After major infrastructure changes
- After solution upgrades
- Before audits

### 4. Continuous Improvement

Use this assessment to drive improvements:
- Identify chronic performance issues → capacity planning
- Identify recurring incidents → root cause analysis
- Identify missing capabilities → roadmap planning
- Identify training needs → upskill teams

---

## Appendix: Terminology

**Terms used in this assessment:**

- **Solution:** A web filtering technology (appliance, cloud service, endpoint agent, DNS filter)
- **Capability:** A specific function that a solution can perform (e.g., malware scanning, URL categorization)
- **Requirement:** A SHALL or MUST or SHOULD statement from policy (ISMS-POL-A.8.23)
- **Gap:** A requirement that is not fully satisfied by deployed solutions
- **Evidence:** Documentation that proves compliance (screenshots, reports, configs, logs)
- **Compliance Status:** Compliant / Partial / Non-Compliant / N/A
- **Remediation:** Actions to close gaps and achieve compliance

---

**END OF PART I: USER COMPLETION GUIDE**

---



---

# PART II: TECHNICAL SPECIFICATION

## Workbook Structure

### Sheet 1: Instructions & Legend

#### Header Section
- **Title:** "ISMS-IMP-A.8.23.1 "“ Filtering Infrastructure Assessment"
- **Subtitle:** "ISO/IEC 27001:2022 - Control A.8.23: Web Filtering"
- **Styling:** Dark blue header (003366), white text, centered, 40px height

#### Document Information Block
```
Document ID:           ISMS-IMP-A.8.23.1
Assessment Area:       Web Filtering Infrastructure
Related Policy:        ISMS-POL-A.8.23, Section 2.1 (Threat Protection Requirements), S2.2
Version:               1.0
Assessment Date:       [USER INPUT - yellow cell]
Completed By:          [USER INPUT - yellow cell]
Organization:          [USER INPUT - yellow cell]
Review Cycle:          Quarterly
```

#### How to Use This Workbook
1. Complete the Solution_Details_Template for EACH filtering solution you have deployed
2. Fill in YOUR specific vendor/product names (this workbook is vendor-agnostic)
3. Use dropdown menus for standardized capability assessments
4. Document licensing, support contracts, and performance metrics
5. Complete the Technology_Comparison sheet if you have multiple solutions
6. Assess capabilities against policy requirements in Capability_Requirements sheet
7. Identify gaps in the Gap_Analysis sheet
8. Maintain the Evidence Register for audit traceability
9. Obtain final approval and sign-off

#### Status Legend
| Symbol | Status | Description | Color Code |
|--------|--------|-------------|------------|
| ✅ | Deployed | Solution deployed and operational | Green (C6EFCE) |
| ⚠️ | Partial | Partial deployment or limited functionality | Yellow (FFEB9C) |
| ❌ | Not Deployed | Solution not deployed | Red (FFC7CE) |
| 🔄 | Planned | Deployment planned with target date | Blue (B4C7E7) |
| N/A | Not Applicable | Not applicable to this environment | Gray |

#### Acceptable Evidence (Examples)
- âœ“ Network diagrams showing filtering placement
- âœ“ Configuration backups/exports (sanitized)
- âœ“ License agreements and support contracts
- âœ“ Performance monitoring dashboards (screenshots)
- âœ“ Vendor capability documentation
- âœ“ Integration architecture diagrams
- âœ“ Change management records for updates/patches
- âœ“ Incident response logs (filtering-related)
- âœ“ Administrative access logs
- âœ“ Compliance reports from the filtering solution
- âœ“ Threat intelligence feed configurations
- âœ“ HTTPS inspection certificates/policies

---

## Sheet 2: Solution_Details_Template

### Purpose
Document each web filtering solution deployed. Copy this template for each solution (e.g., Sheet 2a: Perimeter Filtering, Sheet 2b: Endpoint Filtering, Sheet 2c: Cloud Filtering).

### Header Section
**Row 1:** "WEB FILTERING SOLUTION DETAILS"  
**Row 2:** "Complete one copy of this template for EACH filtering solution deployed"

### Solution Identification Section (Rows 4-15)

| Field | Type | Notes |
|-------|------|-------|
| Solution Name/Description | Text | What YOU call this solution (e.g., "Perimeter Web Filter", "Cloud Filtering Service") |
| Vendor/Provider | Text | **Customer fills in** (e.g., Sophos, Fortigate, Zscaler, Cisco, etc.) |
| Product/Service Name | Text | **Customer fills in** specific product |
| Version/Release | Text | Current version deployed |
| Deployment Model | Dropdown | On-Premises Appliance, Virtual Appliance, Cloud-Based SaaS, Hybrid, DNS-Based, Proxy-Based, Other |
| Deployment Date | Date | When was it first deployed? |
| Deployment Location(s) | Text | Network segments where deployed (e.g., "Corporate HQ firewall", "All endpoints", "Branch offices") |
| Primary Purpose | Dropdown | Threat Protection, Category Filtering, Compliance (CIPA/etc), Bandwidth Management, Hybrid/All |
| Status | Dropdown | ✅ Deployed, ⚠️ Partial, âŒ Not Deployed, 🔄 Planned, N/A |
| Scope of Coverage | Text | What does this protect? (e.g., "All users on corporate LAN", "Remote VPN users", "Guest network") |
| User Count | Number | Approximate number of protected users |
| Integration Points | Text | What does it integrate with? (AD, SIEM, proxies, etc.) |

### Capability Assessment Section (Rows 17-45)

**Header:** "CAPABILITY ASSESSMENT (What can this solution do?)"

| Capability | Assessment | Evidence Location |
|------------|------------|------------------|
| **Threat Protection** | | |
| Blocks known malicious URLs | Dropdown: Yes / No / Partial / Unknown | Text |
| Blocks phishing sites | Dropdown: Yes / No / Partial / Unknown | Text |
| Malware download prevention | Dropdown: Yes / No / Partial / Unknown | Text |
| Ransomware protection | Dropdown: Yes / No / Partial / Unknown | Text |
| Exploit prevention | Dropdown: Yes / No / Partial / Unknown | Text |
| Zero-day threat protection | Dropdown: Yes / No / Partial / Unknown | Text |
| **URL Categorization** | | |
| Supports URL categorization | Dropdown: Yes / No / Not Used | Text |
| Number of categories available | Number | Text |
| Category database update frequency | Dropdown: Real-time / Daily / Weekly / Monthly / Unknown | Text |
| **Content Analysis** | | |
| HTTPS/SSL inspection capable | Dropdown: Yes / No / Partial | Text |
| HTTPS inspection enabled? | Dropdown: Yes / No / Planned / N/A | Text |
| File type filtering | Dropdown: Yes / No | Text |
| Data Loss Prevention (DLP) | Dropdown: Yes / No / Not Used | Text |
| **Policy Enforcement** | | |
| User-based policies | Dropdown: Yes / No | Text |
| Group-based policies | Dropdown: Yes / No | Text |
| Time-based policies | Dropdown: Yes / No / Not Used | Text |
| Location-based policies | Dropdown: Yes / No / Not Used | Text |
| **Logging & Monitoring** | | |
| Generates access logs | Dropdown: Yes / No | Text |
| Generates block/alert logs | Dropdown: Yes / No | Text |
| Real-time alerting | Dropdown: Yes / No / Not Configured | Text |
| Reporting/dashboards | Dropdown: Yes / No | Text |
| Log retention capability | Text (days/months) | Text |
| **Administration** | | |
| Centralized management | Dropdown: Yes / No / N/A | Text |
| Multi-admin support | Dropdown: Yes / No | Text |
| Role-based admin access | Dropdown: Yes / No | Text |
| Configuration backup/restore | Dropdown: Yes / No | Text |
| Change audit logging | Dropdown: Yes / No | Text |
| **Integration** | | |
| Active Directory integration | Dropdown: Yes / No / N/A | Text |
| SIEM integration | Dropdown: Yes / No / Not Configured | Text |
| Threat intelligence feeds | Dropdown: Yes / No / Not Configured | Text |
| API access for automation | Dropdown: Yes / No / Unknown | Text |

### Licensing & Support Section (Rows 47-58)

| Field | Type | Evidence |
|-------|------|----------|
| License Type | Dropdown: Perpetual / Subscription / Pay-per-use / Open Source / Unknown | Text |
| License Expiration Date | Date | Text |
| Licensed User/Device Count | Number | Text |
| Support Contract Active? | Dropdown: Yes / No / Expired | Text |
| Support Level | Dropdown: 24/7 / Business Hours / Community / None | Text |
| Support Expiration Date | Date | Text |
| Update/Patch Schedule | Dropdown: Automatic / Manual-Monthly / Manual-Quarterly / Ad-hoc | Text |
| Last Update Applied | Date | Text |
| Threat Database Version | Text | Text |
| Threat Database Last Updated | Date | Text |
| Annual License Cost | Number (optional) | Text |
| Annual Support Cost | Number (optional) | Text |

### Performance & Reliability Section (Rows 60-70)

| Metric | Value | Evidence |
|--------|-------|----------|
| Uptime SLA (if applicable) | Text (e.g., 99.9%) | Text |
| Actual uptime (last quarter) | Text | Text |
| Average latency impact | Text (ms) | Text |
| False positive rate | Dropdown: Low / Medium / High / Unknown | Text |
| False negative rate | Dropdown: Low / Medium / High / Unknown | Text |
| Incident count (last 12 months) | Number | Text |
| Performance monitoring enabled? | Dropdown: Yes / No | Text |
| Capacity utilization | Text (e.g., "40% of max throughput") | Text |
| Scalability | Dropdown: Scales well / At capacity / Unknown | Text |
| Redundancy/HA configured? | Dropdown: Yes / No / N/A | Text |

### Gap Identification Section (Rows 72-80)

| Gap Description | Severity | Target Remediation Date | Responsible Person |
|-----------------|----------|------------------------|-------------------|
| [Free text] | Dropdown: Critical / High / Medium / Low | Date | Text |
| [8 rows for gap documentation] | | | |

---

## Sheet 3: Technology_Comparison

### Purpose
If you have MULTIPLE filtering solutions, compare them side-by-side to identify coverage overlaps and gaps.

### Header
**Row 1:** "TECHNOLOGY COMPARISON MATRIX"  
**Row 2:** "Compare capabilities across all deployed filtering solutions"

### Comparison Table (Rows 4+)

| Capability | Solution 1 [Name] | Solution 2 [Name] | Solution 3 [Name] | Solution 4 [Name] | Best Coverage |
|------------|------------------|------------------|------------------|------------------|---------------|
| **Deployment Model** | [Auto-pull from Sheet 2] | [Auto-pull] | [Auto-pull] | [Auto-pull] | |
| **Threat Protection** | | | | | |
| Malicious URL blocking | Yes/No | Yes/No | Yes/No | Yes/No | Dropdown |
| Phishing protection | Yes/No | Yes/No | Yes/No | Yes/No | Dropdown |
| Malware prevention | Yes/No | Yes/No | Yes/No | Yes/No | Dropdown |
| **HTTPS Inspection** | Yes/No | Yes/No | Yes/No | Yes/No | Dropdown |
| **Policy Granularity** | | | | | |
| User-based | Yes/No | Yes/No | Yes/No | Yes/No | Dropdown |
| Group-based | Yes/No | Yes/No | Yes/No | Yes/No | Dropdown |
| **Logging** | Yes/No | Yes/No | Yes/No | Yes/No | Dropdown |
| **Support Quality** | [Manual rating] | [Manual rating] | [Manual rating] | [Manual rating] | |
| **Cost (Annual)** | [Optional] | [Optional] | [Optional] | [Optional] | |
| **Overall Rating** | Dropdown: Excellent/Good/Adequate/Poor | | | | |

**Notes Section:** Free text area for observations (e.g., "Solution 1 handles perimeter, Solution 2 handles endpoints - complementary")

---

## Sheet 4: Capability_Requirements

### Purpose
Map YOUR solutions' capabilities against POLICY REQUIREMENTS (from ISMS-POL-A.8.23).

### Header
**Row 1:** "CAPABILITY REQUIREMENTS vs. DEPLOYED SOLUTIONS"  
**Row 2:** "Verify policy compliance across all deployed filtering technologies"

### Requirements Checklist (Rows 4+)

| Requirement ID | Policy Requirement | Met by Solution(s) | Status | Gap? | Evidence |
|----------------|-------------------|-------------------|--------|------|----------|
| REQ-001 | SHALL block known malicious URLs | [Customer lists solutions] | Dropdown: ✅/⚠️/âŒ | Dropdown: Yes/No | Text |
| REQ-002 | SHALL block phishing sites | [Customer lists] | Dropdown: ✅/⚠️/âŒ | Dropdown: Yes/No | Text |
| REQ-003 | SHOULD support HTTPS inspection | [Customer lists] | Dropdown: ✅/⚠️/âŒ | Dropdown: Yes/No | Text |
| REQ-004 | SHALL log filtering events | [Customer lists] | Dropdown: ✅/⚠️/âŒ | Dropdown: Yes/No | Text |
| REQ-005 | SHALL retain logs for ≥90 days | [Customer lists] | Dropdown: ✅/⚠️/âŒ | Dropdown: Yes/No | Text |
| REQ-006 | MUST support threat feed updates | [Customer lists] | Dropdown: ✅/⚠️/âŒ | Dropdown: Yes/No | Text |
| REQ-007 | SHOULD support user-based policies | [Customer lists] | Dropdown: ✅/⚠️/âŒ | Dropdown: Yes/No | Text |
| REQ-008 | SHALL provide administrative audit logs | [Customer lists] | Dropdown: ✅/⚠️/âŒ | Dropdown: Yes/No | Text |
| REQ-009 | MUST have configuration backup capability | [Customer lists] | Dropdown: ✅/⚠️/âŒ | Dropdown: Yes/No | Text |
| REQ-010 | SHOULD integrate with SIEM | [Customer lists] | Dropdown: ✅/⚠️/âŒ | Dropdown: Yes/No | Text |

[Continue for ~30-40 requirements based on policy]

**Summary Metrics:**
- Total Requirements: [Auto-count]
- Requirements Met (✅): [Auto-count]
- Partially Met (⚠️): [Auto-count]
- Not Met (âŒ): [Auto-count]
- Compliance Rate: [Formula: Met / Total * 100%]

---

## Sheet 5: Integration_Architecture

### Purpose
Document how web filtering integrates with other security controls and infrastructure.

### Header
**Row 1:** "INTEGRATION ARCHITECTURE"  
**Row 2:** "Document integration points with existing infrastructure"

### Integration Inventory (Rows 4+)

| Integration Point    | Solution Name      | Integration Type                             | Status                           | Evidence |
|---------------------|--------------------|----------------------------------------------|----------------------------------|----------|
| Active Directory    | [Customer fills]   | Dropdown: Native/LDAP/RADIUS/SAML/None       | Dropdown: Active/Partial/Inactive| Text     |
| SIEM                | [Customer fills]   | Dropdown: Syslog/API/Agent/None              | Dropdown: Active/Partial/Inactive| Text     |
| Proxy Server        | [Customer fills]   | Dropdown: Integrated/Chained/Standalone      | Dropdown: Active/Partial/Inactive| Text     |
| DNS                 | [Customer fills]   | Dropdown: Redirect/Intercept/Passthrough     | Dropdown: Active/Partial/Inactive| Text     |
| Firewall            | [Customer fills]   | Dropdown: Integrated/Adjacent/Separate       | Dropdown: Active/Partial/Inactive| Text     |
| Endpoint Security   | [Customer fills]   | Dropdown: Agent-based/Policy-sync/None       | Dropdown: Active/Partial/Inactive| Text     |
| Email Gateway       | [Customer fills]   | Dropdown: Shared-policy/Independent          | Dropdown: Active/Partial/Inactive| Text     |
| Threat Intelligence | [Customer fills]   | Dropdown: Vendor-feed/Custom/None            | Dropdown: Active/Partial/Inactive| Text     |
| IAM/SSO             | [Customer fills]   | Dropdown: SAML/OAuth/LDAP/None               | Dropdown: Active/Partial/Inactive| Text     |
| DLP                 | [Customer fills]   | Dropdown: Integrated/API/None                | Dropdown: Active/Partial/Inactive| Text     |

### Network Architecture Notes
**Free text section (merged cells):**
- Where is filtering applied? (perimeter, endpoint, cloud, hybrid?)
- Traffic flow description
- Bypass scenarios (if any)
- Redundancy/failover configuration

---

## Sheet 6: Licensing_Support

### Purpose
Centralized view of all licenses and support contracts across filtering solutions.

### Header
**Row 1:** "LICENSING & SUPPORT STATUS"  
**Row 2:** "Maintain awareness of expiration dates and renewal requirements"

### License Registry (Rows 4+)

| Solution Name | License Type | User/Device Count | Expiration Date | Days Until Expiry | Status | Renewal Process Owner |
|---------------|--------------|-------------------|-----------------|-------------------|--------|--------------------|
| [Pull from Sheet 2] | [Auto-pull] | [Auto-pull] | [Auto-pull] | [Formula] | Dropdown: Active/Expiring Soon/Expired | Text |

**Conditional Formatting:**
- <30 days until expiry: Red fill
- 30-90 days: Yellow fill
- >90 days: Green fill

### Support Contract Registry (Rows 15+)

| Solution Name | Support Level | Expiration Date | Days Until Expiry | Last Support Ticket | Support Quality Rating |
|---------------|---------------|-----------------|-------------------|---------------------|----------------------|
| [Pull from Sheet 2] | [Auto-pull] | [Auto-pull] | [Formula] | Date | Dropdown: Excellent/Good/Poor |

### Update/Patch Status (Rows 25+)

| Solution Name | Update Schedule | Last Update Date | Days Since Update | Threat DB Version | DB Last Updated |
|---------------|-----------------|------------------|-------------------|-------------------|-----------------|
| [Pull from Sheet 2] | [Auto-pull] | [Auto-pull] | [Formula] | [Auto-pull] | [Auto-pull] |

**Alert Conditions:**
- >90 days since update: Flag for review
- Threat DB >7 days old: Flag for review

---

## Sheet 7: Performance_Metrics

### Purpose
Track performance and reliability metrics for filtering solutions.

### Header
**Row 1:** "PERFORMANCE METRICS & RELIABILITY TRACKING"  
**Row 2:** "Monitor uptime, latency, and incident trends"

### Uptime Tracking (Rows 4+)

| Solution Name | SLA Target | Q1 Actual | Q2 Actual | Q3 Actual | Q4 Actual | Annual Average | Met SLA? |
|---------------|------------|-----------|-----------|-----------|-----------|----------------|----------|
| [Solution 1] | Text | % | % | % | % | [Formula] | Dropdown: Yes/No |

### Latency Impact (Rows 12+)

| Solution Name | Baseline Latency (no filter) | With Filter | Impact (ms) | Acceptable? |
|---------------|------------------------------|-------------|-------------|-------------|
| [Solution 1] | Number | Number | [Formula] | Dropdown: Yes/No |

### False Positive/Negative Tracking (Rows 20+)

| Month | False Positives | False Negatives | User Complaints | Remediation Actions |
|-------|----------------|-----------------|-----------------|-------------------|
| 2025-01 | Number | Number | Number | Text |
| 2025-02 | Number | Number | Number | Text |
[12 rows for monthly tracking]

### Incident Log (Rows 35+)

| Date | Solution | Incident Type | Severity | Duration | Root Cause | Resolution |
|------|----------|---------------|----------|----------|------------|------------|
| Date | Dropdown | Dropdown: Outage/Performance/False Positive/Bypass/Other | Dropdown: Critical/High/Medium/Low | Text | Text | Text |

[20 rows for incident tracking]

---

## Sheet 8: Gap_Analysis

### Purpose
Consolidated gap identification and remediation tracking.

### Header
**Row 1:** "GAP ANALYSIS & REMEDIATION ROADMAP"  
**Row 2:** "Identify deficiencies and track remediation progress"

### Gap Register (Rows 4+)

| Gap ID | Gap Description | Affected Solution(s) | Policy Requirement | Risk Level | Impact | Remediation Plan | Owner | Target Date | Status | Budget Required |
|--------|----------------|---------------------|-------------------|------------|--------|-----------------|-------|-------------|--------|----------------|
| GAP-001 | [Customer describes gap] | [Solution name(s)] | [REQ-XXX from Sheet 4] | Dropdown: Critical/High/Medium/Low | Text | Text | Text | Date | Dropdown: Open/In Progress/Resolved/Closed | Dropdown: Yes/No |

[30-40 rows for gap tracking]

### Gap Summary Metrics

| Risk Level | Count | % of Total |
|------------|-------|------------|
| Critical | [Formula] | [Formula] |
| High | [Formula] | [Formula] |
| Medium | [Formula] | [Formula] |
| Low | [Formula] | [Formula] |

**Overall Gap Analysis:**
- Total Gaps Identified: [Formula]
- Gaps Resolved: [Formula]
- Resolution Rate: [Formula %]

---

## Sheet 9: Evidence_Register

### Purpose
Centralized evidence repository linking to all supporting documentation.

### Header
**Row 1:** "EVIDENCE REGISTER"  
**Row 2:** "Document all evidence supporting this assessment"

### Evidence Inventory (Rows 4-103, 100 rows)

| Evidence ID | Evidence Type | Description | Related Sheet/Row | Location/Path | Date Collected | Collected By | Verification Status |
|-------------|---------------|-------------|-------------------|---------------|----------------|--------------|-------------------|
| EVD-001 | Dropdown: Config File/Screenshot/Report/License/Contract/Log/Diagram/Policy/Other | Text | Text | Text | Date | Text | Dropdown: Verified/Pending/Not Verified |

[100 rows for evidence tracking]

---

## Sheet 10: Approval_Sign_Off

### Purpose
Formal approval workflow for completed assessment.

### Assessment Summary Section (Rows 3-8)
```
Assessment Document:        ISMS-IMP-A.8.23.1 - Filtering Infrastructure
Assessment Period:          [USER INPUT]
Total Solutions Assessed:   [Formula from Sheet 3]
Overall Compliance Rate:    [Formula from Sheet 4]
Critical Gaps:              [Formula from Sheet 8]
Assessment Status:          [Dropdown: Draft/Final/Requires Remediation/Re-assessment Required]
```

### Assessment Completed By (Rows 10-16)
```
Name:           [USER INPUT]
Role/Title:     [USER INPUT]
Department:     [USER INPUT]
Email:          [USER INPUT]
Date:           [USER INPUT - date picker]
Signature:      [USER INPUT]
```

### Reviewed By - Information Security Officer (Rows 18-24)
```
Name:           [USER INPUT]
Date:           [USER INPUT]
Review Notes:   [Text area - merged cells]
Recommendation: [Dropdown: Approve/Approve with Conditions/Reject/Require Rework]
```

### Approved By - CISO (Rows 26-32)
```
Name:               [USER INPUT]
Date:               [USER INPUT]
Approval Decision:  [Dropdown: Approved/Approved with Conditions/Rejected]
Conditions/Notes:   [Text area]
```

### Next Review Details (Rows 34-38)
```
Next Review Date:          [Date - auto-calculate +3 months]
Review Responsible:        [USER INPUT]
Special Considerations:    [Text area]
```

---

## Cell Styling Reference

### Header Styles
- **Main Header:** Font: Calibri 14pt bold white, Fill: 003366 (dark blue), Alignment: centered/wrapped, Height: 40px
- **Subheader:** Font: Calibri 11pt bold white, Fill: 4472C4 (blue), Alignment: centered/wrapped
- **Column Header:** Font: Calibri 10pt bold black, Fill: D9D9D9 (gray), Alignment: centered/wrapped, Border: thin all sides

### Input Cell Styles
- **Fill:** FFFFCC (light yellow)
- **Alignment:** Left/center, wrapped
- **Border:** Thin black on all sides

### Status Fills
- **Deployed (✅):** C6EFCE (green)
- **Partial (⚠️):** FFEB9C (yellow)
- **Not Deployed (âŒ):** FFC7CE (red)
- **Planned (🔄):** B4C7E7 (blue)

---

## Freeze Panes

- **Solution_Details_Template:** Freeze at A4 (headers visible)
- **All comparison/analysis sheets:** Freeze at A4
- **Evidence Register:** Freeze at A5
- **Approval Sign-Off:** Freeze at A3

---

## File Naming Convention

**Format:** `ISMS-IMP-A.8.23.1_Filtering_Infrastructure_YYYYMMDD.xlsx`

**Example:** `ISMS-IMP-A.8.23.1_Filtering_Infrastructure_20260101.xlsx`

---

## Quarterly Review Cycle

1. Review all solution details for accuracy (Sheet 2)
2. Update capability assessments based on changes
3. Verify license/support expiration dates (Sheet 6)
4. Update performance metrics (Sheet 7)
5. Review and update gap remediation status (Sheet 8)
6. Add new evidence entries (Sheet 9)
7. Re-calculate compliance rates (Sheet 4)
8. Address any new critical gaps
9. Update approval sign-off with quarterly review notes
10. Re-approval by CISO if significant changes

---

## Integration Points

### Related Documents
- ISMS-POL-A.8.23, Section 2.1 (Threat Protection Requirements): Threat Protection Requirements
- ISMS-POL-A.8.23, Section 2.2 (Category Filtering Approach): Category Filtering Requirements
- ISMS-IMP-A.8.23.2: Network Coverage Assessment
- ISMS-IMP-A.8.23.3: Policy Configuration Assessment
- ISMS-IMP-A.8.23.5: Compliance Dashboard (pulls data from this workbook)
- Risk Register: Link Gap IDs to Risk IDs
- Change Management: Link solution updates to change tickets
- Asset Inventory: Ensure filtering solutions are tracked as assets

### Audit Trail
- All evidence referenced in Evidence Register
- Gap remediation linked to project management
- License renewals tracked in procurement system
- Performance incidents linked to incident management
- Approval sign-off maintains complete audit trail

---

**END OF SPECIFICATION**

*"The first principle is that you must not fool yourself "” and you are the easiest person to fool."*  
"” Richard Feynman

**ISMS Maturity Indicator:** If you can complete this assessment WITHOUT mentioning vendor names in your policies, you understand the difference between compliance theater and systems engineering. ✅