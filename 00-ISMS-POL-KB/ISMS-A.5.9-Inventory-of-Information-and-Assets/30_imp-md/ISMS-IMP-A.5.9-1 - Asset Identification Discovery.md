# ISMS-IMP-A.5.9-1
## Asset Identification & Discovery Procedures
### ISO/IEC 27001:2022 Control A.5.9: Inventory of Information and Assets

---

## Document Overview

**Document ID:** ISMS-IMP-A.5.9-1  
**Implementation Area:** Asset Identification and Discovery  
**Related Policy:** ISMS-POL-A.5.9-S2 (Requirements Framework)  
**Purpose:** Provide systematic procedures for identifying and discovering all information and associated assets within [Organization]'s scope

**Key Principle:** Asset discovery is **NOT a one-time event**. It is a continuous process combining automated tools, manual procedures, and organizational knowledge to maintain an accurate and complete inventory.

---

## 1. Discovery Methodology Overview

### 1.1 Hybrid Approach (Recommended)

[Organization] should employ a combination of automated and manual discovery techniques:

```
┌─────────────────────────────────────────────────────────────┐
│                    DISCOVERY STRATEGY                        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  Automated Discovery          Manual Discovery              │
│  ├─ Network scanning          ├─ Business owner interviews  │
│  ├─ Agent-based discovery     ├─ Document review            │
│  ├─ API integration           ├─ Physical walkthroughs      │
│  ├─ Log analysis              ├─ HR system extraction       │
│  └─ CMDB synchronization      └─ Procurement review         │
│           │                            │                     │
│           └────────────┬───────────────┘                     │
│                        │                                     │
│                   RECONCILIATION                             │
│                 (Merge & Validate)                          │
│                        │                                     │
│                   ENRICHMENT                                 │
│             (Add business context)                          │
│                        │                                     │
│                INVENTORY SYSTEM                              │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

**Why Hybrid?**
- **Automated:** Efficient for technical assets, provides baseline
- **Manual:** Captures business context, information assets, relationships
- **Combined:** Achieves completeness that neither approach can alone

---

## 2. Automated Discovery Procedures

### 2.1 Network Scanning

**Purpose:** Identify all network-connected devices and systems

**Recommended Tools (Examples - [Organization] selects appropriate tools):**
- Network scanners: Nmap, Qualys, Rapid7 InsightVM, Tenable Nessus
- CMDB discovery: ServiceNow Discovery, BMC Discovery
- Cloud-native: AWS Config, Azure Resource Graph, GCP Asset Inventory
- Specialized: SolarWinds, ManageEngine OpManager

**Procedure:**

1. **Define Scan Scope**
   - All IP ranges within [Organization]'s control
   - Include: Corporate networks, branch offices, data centers, VPN ranges
   - Exclude: Out-of-scope networks (partners, ISP infrastructure)
   - Document exclusions with justification

2. **Configure Scan Parameters**
   - Frequency: Weekly for critical networks, monthly for stable segments
   - Scan type: Non-intrusive discovery (avoid disruption)
   - Credentials: Use read-only service accounts where authentication needed
   - Timing: Off-peak hours to minimize performance impact

3. **Execute Scans**
   - Run scheduled scans automatically
   - Perform on-demand scans after infrastructure changes
   - Capture results in structured format (CSV, JSON, API)

4. **Process Scan Results**
   - Extract discovered assets: IP address, hostname, MAC address, OS, open ports
   - Identify new assets (not in inventory)
   - Flag disappeared assets (in inventory but not discovered)
   - Update existing asset records with current technical attributes

5. **Handle Scan Conflicts**
   - **Multiple IPs for single asset:** Verify which is primary, document all
   - **Transient devices:** Determine if should be inventoried (guest devices may be excluded)
   - **Unidentifiable devices:** Investigate manually or escalate to network team

**Deliverable:** Automated scan results feed into reconciliation process

### 2.2 Agent-Based Discovery

**Purpose:** Collect detailed information from managed endpoints and servers

**Examples:**
- Endpoint management: Microsoft Intune, JAMF, VMware Workspace ONE
- Server agents: Chef, Puppet, Ansible facts collection
- Security agents: EDR platforms with asset inventory features
- Cloud agents: Cloud-native agents for SaaS/PaaS discovery

**Procedure:**

1. **Agent Deployment**
   - Deploy agents to all managed systems (workstations, servers, mobile devices)
   - Verify agent communication and data collection
   - Handle offline/disconnected devices (laptops, remote workers)

2. **Data Collection Configuration**
   - Collect: Hardware specs, installed software, configurations, patches
   - Schedule: Continuous or periodic (daily/weekly)
   - Storage: Central management console or CMDB

3. **Software Inventory**
   - Discover all installed applications
   - Identify unauthorized/shadow IT software
   - Determine software versions and license status

4. **Configuration Inventory**
   - Capture system configurations
   - Identify configuration drift
   - Document compliance with baselines

**Deliverable:** Detailed endpoint and server inventory with installed software

### 2.3 API-Based Discovery

**Purpose:** Discover cloud resources, SaaS applications, and API-accessible systems

**Examples:**
- **Cloud Platforms:** AWS API, Azure Resource Manager API, GCP API
- **SaaS Discovery:** Okta app catalog, Azure AD integrated apps, SSO logs
- **Identity Systems:** Active Directory, LDAP queries
- **Virtualization:** VMware vCenter API, Hyper-V, Proxmox

**Procedure:**

1. **API Access Configuration**
   - Create read-only service accounts/API keys
   - Document API endpoints and authentication methods
   - Test API connectivity and permissions

2. **Cloud Resource Discovery**
   - Query cloud provider APIs for all resources:
     - Compute: VMs, containers, serverless functions
     - Storage: S3 buckets, blob storage, databases
     - Networking: VPCs, load balancers, firewalls
     - Services: Managed services (RDS, Lambda, etc.)
   - Extract metadata: Resource IDs, tags, creation dates, owners

3. **SaaS Application Discovery**
   - Query identity provider for integrated applications
   - Analyze SSO logs to identify accessed SaaS services
   - Shadow IT detection: Analyze firewall/proxy logs for SaaS usage

4. **Integration with Inventory**
   - Map cloud resources to inventory records
   - Link SaaS apps to business owners
   - Track cloud cost allocation

**Deliverable:** Complete cloud and SaaS inventory

### 2.4 Log-Based Discovery

**Purpose:** Discover assets through analysis of logs and network traffic

**Data Sources:**
- **DHCP logs:** Devices requesting IP addresses
- **DNS logs:** Hostname resolution requests
- **Firewall logs:** Source/destination IPs and traffic patterns
- **Proxy logs:** Web access patterns revealing SaaS usage
- **Authentication logs:** User authentication to systems/applications
- **SIEM data:** Aggregated security event logs

**Procedure:**

1. **Log Collection**
   - Ensure comprehensive log collection from all sources
   - Centralize logs (SIEM, log management platform)
   - Retention: Minimum 90 days for discovery analysis

2. **Pattern Analysis**
   - **DHCP analysis:** Identify all devices receiving IPs over 30-90 days
   - **DNS analysis:** Identify frequently accessed internal/external services
   - **Traffic analysis:** Discover communication patterns and dependencies
   - **Authentication analysis:** Map users to accessed systems

3. **Anomaly Detection**
   - Identify assets communicating but not in inventory
   - Detect unusual traffic patterns
   - Flag potential shadow IT or unauthorized devices

4. **Reconciliation**
   - Cross-reference log-discovered assets with inventory
   - Investigate discrepancies
   - Update inventory with new findings

**Deliverable:** Log-derived asset list and communication patterns

### 2.5 CMDB Integration

**Purpose:** Leverage existing Configuration Management Database as asset source

**Assumption:** [Organization] has existing CMDB (ServiceNow, BMC, etc.)

**Procedure:**

1. **CMDB Assessment**
   - Evaluate CMDB completeness and accuracy
   - Identify gaps (CMDB may not include information assets)
   - Assess data quality and currency

2. **Data Extraction**
   - Export CMDB data via API or reporting
   - Extract: Configuration Items (CIs), attributes, relationships
   - Map CMDB fields to inventory schema

3. **Bi-Directional Sync Design**
   - **CMDB → Inventory:** Technical asset attributes
   - **Inventory → CMDB:** Owner assignments, classifications
   - Conflict resolution: Define authoritative source per attribute

4. **Ongoing Synchronization**
   - Schedule: Daily or real-time sync
   - Monitor sync errors and resolve
   - Maintain data consistency

**Deliverable:** Integrated CMDB-Inventory system or synchronized data

---

## 3. Manual Discovery Procedures

### 3.1 Structured Interviews with Business Owners

**Purpose:** Identify information assets and capture business context

**Why Manual?** Information assets (customer databases, IP, financial records) are not discovered by network scans—they require business knowledge.

**Procedure:**

1. **Identify Interview Targets**
   - Business unit leaders
   - Department heads
   - Process owners
   - Key personnel with specialized knowledge

2. **Prepare Interview Template**
   ```
   Interview Template - Information Asset Discovery
   
   Interviewee: ________________  Department: ________________
   Date: ________________        Interviewer: ________________
   
   1. What information does your department create, use, or maintain?
      - Structured data (databases, spreadsheets)
      - Documents (contracts, reports, manuals)
      - Records (financial, HR, legal)
      - Intellectual property (designs, source code, trade secrets)
   
   2. Where is this information stored?
      - Systems/applications used
      - File shares, SharePoint, cloud storage
      - Physical locations (filing cabinets, safes)
   
   3. Who owns this information?
      - Business owner (accountable for information)
      - Custodian (responsible for storage/protection)
   
   4. What is the criticality?
      - Impact if lost/unavailable
      - Impact if disclosed to unauthorized parties
      - Regulatory/legal requirements
   
   5. What systems depend on this information?
      - Applications that process it
      - Integrations and data flows
   
   6. Current challenges or concerns?
      - Access control issues
      - Backup/recovery concerns
      - Classification uncertainties
   ```

3. **Conduct Interviews**
   - Schedule 30-60 minute sessions
   - Use template to structure discussion
   - Capture detailed notes
   - Request supporting documentation

4. **Document Findings**
   - Create information asset records
   - Assign preliminary owners
   - Link information assets to associated technical assets
   - Flag items requiring further investigation

**Deliverable:** Information asset inventory with business context

### 3.2 Document Review

**Purpose:** Identify assets documented in existing organizational records

**Documents to Review:**
- **Architecture diagrams:** System architecture, network topology
- **Contracts:** Vendor agreements, SaaS subscriptions, support contracts
- **Procurement records:** Hardware purchases, software licenses
- **Project documentation:** New systems, migrations, implementations
- **Disaster recovery plans:** Critical systems and dependencies
- **Compliance documentation:** SOC 2 reports, audit findings
- **HR records:** Organizational charts, job descriptions (for personnel assets)

**Procedure:**

1. **Collect Documents**
   - Request from relevant departments (IT, procurement, legal, HR)
   - Access document management systems
   - Review project archives

2. **Extract Asset Information**
   - Identify mentioned systems, applications, information
   - Extract asset attributes: names, versions, locations, owners
   - Note dependencies and relationships

3. **Validate Against Inventory**
   - Cross-reference discovered assets with current inventory
   - Add missing assets
   - Update existing records with additional details

4. **Identify Inconsistencies**
   - Document discrepancies (e.g., documented system not discovered)
   - Investigate: Asset decommissioned? Documentation outdated?

**Deliverable:** Assets extracted from documentation

### 3.3 Physical Walkthroughs

**Purpose:** Discover physical assets and validate physical locations

**Scope:**
- Data centers and server rooms
- Network closets and telecommunications rooms
- Office spaces (workstations, printers, phones)
- Storage areas (backup media, archives)
- Facilities (HVAC, power, physical security systems)

**Procedure:**

1. **Plan Walkthrough**
   - Schedule with facilities/IT teams
   - Prepare asset capture tools: Mobile app, tablet with inventory form
   - Coordinate access to secure areas

2. **Conduct Walkthrough**
   - Room-by-room systematic inspection
   - Record: Asset type, model, serial number, location, condition
   - Photograph assets for visual reference (if policy permits)
   - Identify undocumented assets

3. **Record Physical Assets**
   - Create/update physical asset records
   - Assign asset tags/labels
   - Document location codes

4. **Reconciliation**
   - Compare physical findings to inventory
   - Investigate missing items (stolen? relocated? disposed?)
   - Update inventory with actual locations

**Deliverable:** Physical asset inventory with verified locations

### 3.4 HR System Extraction

**Purpose:** Identify personnel assets (key personnel, competencies, contractors)

**Data Sources:**
- Human Resources Information System (HRIS)
- Organizational charts
- Skills/competency databases
- Contractor management systems

**Procedure:**

1. **Coordinate with HR**
   - Explain asset inventory purpose (not performance review)
   - Address privacy concerns (limited data extraction)
   - Obtain necessary approvals

2. **Extract Data**
   - Key personnel: Executives, critical role holders
   - Competencies: Specialized skills, certifications
   - Contractors/vendors: Third-party dependencies
   - DO NOT extract: Full employee database (not necessary)

3. **Create Personnel Asset Records**
   - Record: Role/competency (not individuals)
   - Example: "Database Administrator Competency" not "John Smith"
   - Count: Number of people with competency
   - Criticality: Risk if competency lost

4. **Maintain Privacy**
   - Minimize personal data in inventory
   - Focus on organizational capabilities, not individuals
   - Comply with privacy regulations (GDPR, etc.)

**Deliverable:** Personnel asset records (roles/competencies)

### 3.5 Procurement Record Review

**Purpose:** Identify assets through purchase orders and procurement records

**Procedure:**

1. **Access Procurement System**
   - Request access to procurement database
   - Define timeframe: Last 3-5 years (depending on asset lifecycle)

2. **Extract Relevant Purchases**
   - IT equipment: Servers, laptops, networking gear
   - Software licenses: Applications, tools, platforms
   - Services: Cloud subscriptions, SaaS contracts
   - Support/maintenance contracts

3. **Map to Inventory**
   - Match purchases to existing inventory records
   - Add missing assets (purchased but not inventoried)
   - Flag potential "ghost assets" (purchased but not deployed)

4. **Validate Asset Status**
   - Verify purchased assets are deployed
   - Identify retired/disposed assets
   - Reconcile quantities

**Deliverable:** Procurement-validated asset list

---

## 4. Asset Categorization Guidance

### 4.1 Decision Framework

Use this decision tree to determine asset category:

```
Is it INFORMATION or SOMETHING THAT PROCESSES/STORES INFORMATION?

├─ INFORMATION (data, content, knowledge)
│  └─ Information Asset Categories:
│     ├─ Structured Data (databases, tables)
│     ├─ Unstructured Documents (files, emails)
│     ├─ Records & Archives (retained for compliance)
│     ├─ Intellectual Property (trade secrets, patents)
│     ├─ Configuration & Parameters (system configs)
│     ├─ Authentication & Cryptographic (keys, certificates)
│     ├─ Communication Records (emails, chats, call logs)
│     └─ Business Intelligence (reports, analytics)
│
└─ SOMETHING ELSE (system, device, facility, person)
   └─ Associated Asset Categories:
      ├─ IT Infrastructure (servers, storage, networking)
      ├─ Applications (software, SaaS, services)
      ├─ Physical Assets (facilities, media, equipment)
      └─ Personnel Assets (competencies, key roles)
```

### 4.2 Granularity Guidelines

**Question:** At what level should we inventory?

**Answer:** It depends on criticality and risk.

**Examples:**

| Asset Type | Too Granular | Appropriate | Too High-Level |
|------------|-------------|-------------|----------------|
| Servers | Each disk drive | Physical/virtual server | "All servers" |
| Applications | Each module/function | Application instance | "All applications" |
| Data | Each database row | Database or dataset | "All data" |
| Networks | Each switch port | Network device | "The network" |
| Files | Individual files | File share or repository | "All documents" |

**Guiding Principles:**
1. **Criticality:** Higher criticality → More detailed inventory
2. **Risk exposure:** Higher risk → More granular tracking
3. **Maintainability:** Must be sustainable to keep current
4. **Decision-making:** Sufficient detail to make risk/access decisions
5. **Regulatory:** May mandate specific granularity

### 4.3 Information vs. Associated Assets

**Common Confusion:** Is a database server an "information asset"?

**Answer:** NO. The **database server** is an **associated asset** (IT infrastructure). The **data IN the database** is the **information asset**.

**Examples:**

| Information Asset | Associated Asset |
|------------------|------------------|
| Customer database (the DATA) | SQL Server (the application) |
| Source code repository (the CODE) | GitHub (the platform) |
| Financial records (the RECORDS) | File server (the storage) |
| Email communications (the MESSAGES) | Exchange server (the system) |
| Contracts (the DOCUMENTS) | SharePoint site (the repository) |

**Why This Matters:**
- **Different owners:** Business owns information, IT owns systems
- **Different lifecycles:** Data may outlive systems
- **Different classifications:** Information has CIA rating, systems have different criteria
- **Different controls:** Information controls ≠ system controls

---

## 5. Owner Assignment Process

### 5.1 Owner Identification Decision Tree

```
Who should be the owner of this asset?

INFORMATION ASSET:
└─ Who has BUSINESS ACCOUNTABILITY for this information?
   ├─ Is it department-specific? → Department Head
   ├─ Is it process-specific? → Process Owner
   ├─ Is it organization-wide? → Chief [Function] Officer
   └─ Uncertain? → Escalate to management

ASSOCIATED ASSET (IT/Technical):
└─ Who has MANAGEMENT RESPONSIBILITY for this system?
   ├─ Business application? → Business Owner
   ├─ Infrastructure service? → IT Service Owner
   ├─ Shared platform? → Platform/Service Manager
   └─ Uncertain? → Chief Information Officer (temporary)

PHYSICAL ASSET:
└─ Who manages this facility/equipment?
   ├─ Data center? → Data Center Manager
   ├─ Office equipment? → Facilities Manager
   ├─ Security systems? → Security Manager
   └─ Uncertain? → Chief Operations Officer

PERSONNEL ASSET:
└─ Who manages this competency/role?
   ├─ Department competency? → Department Head
   ├─ Organization-wide competency? → Chief Human Resources Officer
   └─ Contractor/vendor? → Vendor Manager
```

### 5.2 Owner Assignment Procedure

**Step 1: Initial Assignment**
1. Assign owner based on decision tree
2. Document rationale
3. Flag uncertain assignments for escalation

**Step 2: Owner Notification**
1. Send owner acknowledgment form (see ISMS-POL-A.5.9-S5.B)
2. Include:
   - List of assets assigned to them
   - Owner responsibilities summary
   - Instructions for accepting/disputing assignment
3. Set response deadline (e.g., 2 weeks)

**Step 3: Owner Acknowledgment**
1. Owner reviews assigned assets
2. Owner accepts or disputes assignment
3. If disputed: Escalate to management for resolution

**Step 4: Handle Disputes**
1. Facilitate discussion between claimants
2. Management makes final decision
3. Document resolution
4. Update inventory

**Step 5: Temporary Assignments**
- If no clear owner: Assign to appropriate executive temporarily
- Flag for resolution within 30 days
- Escalate if unresolved

### 5.3 Special Cases

**Shared Ownership:**
- Some assets genuinely have multiple stakeholders
- Designate PRIMARY owner (accountability)
- Document secondary owners (interested parties)
- Example: Customer database
  - Primary: VP Sales (business accountability)
  - Secondary: CIO (system custodian), Legal (compliance), Security (protection)

**Decommissioned Assets:**
- Assign to person responsible for decommissioning
- Maintain ownership until secure disposal complete
- Transfer ownership to "Archive" owner if retention required

**Third-Party Owned Assets:**
- Owner: Contract/Vendor Manager
- Document: Vendor/provider name, contract reference
- Responsibility: Manage contract, ensure SLAs, coordinate

---

## 6. Common Pitfalls and Solutions

### 6.1 "We Already Have a CMDB"

**Pitfall:** Assuming CMDB = complete asset inventory

**Reality:**
- CMDBs focus on IT infrastructure (servers, networking, apps)
- CMDBs typically DON'T include:
  - Information assets (data, documents, IP)
  - Physical assets (facilities, media)
  - Personnel assets
  - Business context (owner, classification, criticality)

**Solution:**
1. Use CMDB as foundation for technical assets
2. Enrich CMDB data with security/business context
3. Supplement with information asset inventory
4. Integrate, don't duplicate

### 6.2 "Too Many Assets to Inventory"

**Pitfall:** Trying to inventory every single item to exhaustive detail

**Solution:**
1. **Prioritize:** Start with critical assets (see risk-based approach)
2. **Appropriate granularity:** Commodity assets can be grouped
3. **Phased approach:** 
   - Phase 1: Critical/high-risk assets (detailed)
   - Phase 2: Medium-risk assets (moderate detail)
   - Phase 3: Low-risk assets (grouped or sampled)
4. **Automation:** Use tools to reduce manual effort
5. **Continuous improvement:** Don't aim for perfection on day 1

**Risk-Based Prioritization:**

| Priority | Criteria | Inventory Detail |
|----------|----------|------------------|
| Critical | High business impact, regulated data, external-facing | Comprehensive, individual asset level |
| High | Moderate business impact, internal systems | Detailed, may group similar items |
| Medium | Low business impact, standard systems | Moderate, group commodity items |
| Low | Minimal impact, easily replaced | Minimal, may use representative samples |

### 6.3 "Ephemeral Cloud Assets"

**Pitfall:** Trying to inventory short-lived cloud resources (auto-scaling instances)

**Reality:** Cloud assets can exist for seconds/minutes (containers, serverless functions)

**Solution:**
1. **Service-level inventory:** Inventory the SERVICE, not individual instances
   - Example: "Web Application Auto-Scaling Group" not "Instance i-12345"
2. **Configuration-as-code:** Inventory the DEFINITION (Terraform, CloudFormation)
3. **Tagging strategy:** Tag cloud resources for automatic inventory updates
4. **API integration:** Use cloud APIs to query current state on-demand

**Example:**
- ❌ Don't inventory: Each EC2 instance in auto-scaling group
- ✅ Do inventory: "Customer Portal Web Service" (the service definition)
  - Document: Auto-scaling config, AMI, instance type, VPC, etc.

### 6.4 "Unknown Owners"

**Pitfall:** Significant assets with no clear owner

**Solution:**
1. **Investigation process:**
   - Who uses this asset?
   - Who requested it?
   - Who pays for it? (check procurement/billing)
   - What business process does it support?

2. **Escalation path:**
   - Week 1: Asset Management Team investigates
   - Week 2: Escalate to IT management
   - Week 3: Escalate to executive leadership
   - Week 4: Executive assigns owner OR approves decommissioning

3. **Temporary assignment:**
   - Assign to appropriate executive (CIO, COO, etc.)
   - Flag as "Owner TBD"
   - Mandatory review in 30 days

4. **Decommissioning consideration:**
   - If no one claims ownership → May not be needed
   - Evaluate for decommissioning
   - Requires approval before disposal

### 6.5 "Shadow IT"

**Pitfall:** Discovering unauthorized systems/services during inventory

**Reality:** Users often deploy solutions outside IT (cloud services, apps, devices)

**Solution:**
1. **Don't ignore:** Shadow IT is a real security risk
2. **Inventory anyway:** Document as-found
3. **Risk assessment:** Evaluate security risk
4. **Regularization process:**
   - Option 1: Bring under IT management (if needed)
   - Option 2: Migrate to approved alternative
   - Option 3: Decommission (if redundant)
   - Option 4: Accept risk with compensating controls
5. **Prevention:** Improve IT service catalog to reduce shadow IT drivers

---

## 7. Quality Assurance Procedures

### 7.1 Completeness Verification

**Objective:** Ensure all assets within scope are inventoried

**Methods:**

1. **Discovery Reconciliation**
   - Compare inventory to discovery results
   - Formula: `Completeness = (Inventoried Assets / Discovered Assets) × 100%`
   - Target: ≥95%
   - Investigate gaps

2. **Management Attestation**
   - Department heads certify their areas are complete
   - Process:
     - Provide each manager their department's asset list
     - Manager reviews and certifies OR identifies missing items
     - Manager signs attestation
   - Include in evidence register

3. **Sample Deep-Dive**
   - Select sample locations/departments
   - Conduct intensive discovery (all methods)
   - Compare to inventory
   - Extrapolate completeness estimate

4. **User Survey**
   - Survey users: "What systems/information do you use that you don't see in the inventory?"
   - Analyze responses
   - Investigate mentioned items

**Deliverable:** Completeness score and gap list

### 7.2 Accuracy Verification

**Objective:** Ensure inventory data is correct

**Methods:**

1. **Attribute Sampling**
   - Select random sample (e.g., 5% of assets)
   - Verify key attributes:
     - Technical: IP address, hostname, location (can check remotely)
     - Ownership: Contact owner to confirm (email/interview)
     - Classification: Validate with owner
   - Calculate accuracy: `(Correct Records / Sampled Records) × 100%`
   - Target: ≥95%

2. **Owner Attestation**
   - Send asset list to each owner
   - Owner reviews and confirms OR corrects
   - Document corrections
   - Calculate attestation rate

3. **System Integration Validation**
   - Compare inventory to authoritative sources:
     - AD/LDAP: Validate system records
     - CMDB: Cross-check technical attributes
     - HR system: Validate personnel records
   - Measure consistency

**Deliverable:** Accuracy score and correction list

### 7.3 Currency Verification

**Objective:** Ensure inventory is up-to-date

**Method:**
- Check last update date for each asset
- Target: ≥90% updated within review period (based on criticality)
- Flag overdue reviews

### 7.4 Reconciliation Process

**Frequency:** Weekly (automated), monthly (manual review)

**Procedure:**
1. Run automated discovery
2. Compare to inventory:
   - **New in discovery, not in inventory:** Add to inventory (new assets)
   - **In inventory, not in discovery:** Investigate (decommissioned? Offline? Scan miss?)
   - **In both but attributes differ:** Flag for review
3. Investigate discrepancies
4. Update inventory
5. Document decisions (why kept, removed, or updated)
6. Report reconciliation results

---

## 8. Integration with ISMS-POL-A.5.9-S2 Requirements

This implementation guidance supports the requirements defined in ISMS-POL-A.5.9-S2:

| S2 Requirement | Implementation in This Document |
|----------------|--------------------------------|
| R1: Information Asset Inventory | Section 3.1 (Interviews), 3.2 (Document review) |
| R2: Associated Asset Inventory | Section 2 (Automated discovery), 3.3 (Physical) |
| R3: Mandatory Attributes | Sections 2-5 (Discovery captures required attributes) |
| R4: Owner Assignment | Section 5 (Complete owner assignment process) |
| R5: Asset Categorization | Section 4 (Categorization guidance) |
| R6: Relationships | Sections 2.4 (Log analysis), 3.1 (Interviews) |
| R7: Lifecycle Management | Sections 6.4 (Decommissioning), 7.4 (Reconciliation) |
| R8: Integration with Controls | Implicitly throughout (inventory feeds other controls) |

---

## 9. Summary and Next Steps

### 9.1 Discovery Process Summary

```
PHASE 1: PREPARATION
├─ Define scope
├─ Select tools
├─ Assign roles
└─ Generate assessment workbook (ISMS_A_5_9_Information_Assets_YYYYMMDD.xlsx)

PHASE 2: AUTOMATED DISCOVERY
├─ Network scanning
├─ Agent-based discovery
├─ API integration
├─ Log analysis
└─ CMDB extraction

PHASE 3: MANUAL DISCOVERY
├─ Business owner interviews
├─ Document review
├─ Physical walkthroughs
├─ HR system extraction
└─ Procurement review

PHASE 4: RECONCILIATION
├─ Merge automated + manual results
├─ Eliminate duplicates
├─ Resolve conflicts
└─ Enrich with business context

PHASE 5: OWNER ASSIGNMENT
├─ Identify appropriate owners
├─ Send acknowledgment requests
├─ Resolve disputes
└─ Document final assignments

PHASE 6: QUALITY VERIFICATION
├─ Completeness assessment
├─ Accuracy sampling
├─ Currency check
└─ Gap remediation

PHASE 7: DOCUMENTATION
└─ Complete information asset workbook with evidence
```

### 9.2 Deliverable

**Primary Output:** ISMS_A_5_9_Information_Assets_YYYYMMDD.xlsx (generated by `generate_a59_1_information_assets.py`)

**Contents:**
- Information asset inventory with all mandatory attributes
- Owner assignments and acknowledgments
- Classification matrix
- Relationships to associated assets
- Evidence register
- Approval sign-off

### 9.3 Next Implementation Document

**ISMS-IMP-A.5.9-2** - Inventory Structure & Maintenance
- Inventory system design
- Integration architecture
- Maintenance workflows
- Data quality management

---

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 10.01.2026 | ISMS Implementation Team | Initial implementation guidance |

---

**Related Documents:**
- ISMS-POL-A.5.9 (Master Framework)
- ISMS-POL-A.5.9-S2 (Requirements Framework)
- ISMS-IMP-A.5.9-2 (Inventory Maintenance)
- ISMS-IMP-A.5.9-3 (Assessment Specifications)

---

*"You cannot protect what you don't know exists. Systematic discovery is the foundation of security."*

**Document Status:** Ready for implementation  
**Estimated Reading Time:** 45-60 minutes  
**Target Audience:** Asset management team, IT operations, security team, business owners
