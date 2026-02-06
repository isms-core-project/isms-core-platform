**ISMS-IMP-A.5.9.1-UG - Asset Identification & Discovery**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.9: Inventory of Information and Other Associated Assets

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.9.1-UG |
| **Version** | 1.0 |
| **Assessment Area** | Asset Identification & Discovery Procedures |
| **Related Policy** | ISMS-POL-A.5.9, Section 2.1 (Asset Inventory Creation), Section 2.5 (Inventory Quality Standards) |
| **Purpose** | Document asset discovery procedures, verify completeness of inventory, and identify gaps in asset identification across all categories |
| **Target Audience** | Security Team, IT Operations, System Owners, Information Owners, Compliance Officers, Auditors |
| **Assessment Type** | Operational & Technical |
| **Review Cycle** | Quarterly or After Major Organizational Changes |
| **Date** | [Date]  |

### Version History

| Version | Date | Changes | Author |
|---------|------|--------|--------|
| 1.0 | [Date]  | Initial assessment specification following consolidated policy structure | ISMS Implementation Team |

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.5.9.1-TG.

---

**Audience:** Security Team, IT Operations, System Owners, Information Owners

---

## Assessment Overview

### What This Assessment Evaluates

This assessment documents HOW [Organization] identifies and discovers assets across all categories. This is the foundational "WHAT exists?" assessment that answers:

- **Information Assets**: What databases, documents, IP, and configurations exist?
- **IT Infrastructure**: What servers, storage, networking, and endpoints exist?
- **Applications**: What business apps, SaaS services, and development tools exist?
- **Physical Assets**: What facilities, media, and equipment exist?
- **Personnel Assets**: What key roles and competencies exist?

**Key Principle**: You cannot protect what you do not know you have. This assessment verifies that [Organization] has systematic procedures to discover assets and that the inventory is complete (no missing assets).

### Why This Matters

This assessment verifies [Organization]'s compliance with:

- **ISO/IEC 27001:2022 Control A.5.9**: Inventory of Information and Other Associated Assets
- **ISMS-POL-A.5.9, Requirement A.5.9-R1**: [Organization] SHALL maintain an inventory of information and associated assets
- **ISMS-POL-A.5.9, Section 2.5.1**: Completeness standard (95% for critical, 90% for standard)

**From Implementer Perspective**: Provides systematic methodology to find ALL assets so nothing is missed.

**From Auditor Perspective**: Demonstrates [Organization] knows what assets exist and has repeatable discovery process.

### Assessment Domains

This assessment covers **5 discovery domains** aligned with policy asset categories:

| Domain | Focus | What You'll Document |
|--------|-------|---------------------|
| **1. Information Asset Discovery** | Databases, documents, IP, configurations | Discovery methods, sources, completeness verification |
| **2. IT Infrastructure Discovery** | Servers, storage, networking, endpoints | Automated scans, CMDB integration, gap analysis |
| **3. Application Discovery** | Business apps, SaaS, development tools | Software inventory, license management, usage tracking |
| **4. Physical Asset Discovery** | Facilities, media, equipment | Physical audits, procurement records, location tracking |
| **5. Personnel Asset Discovery** | Key roles, competencies | HR integration, competency mapping, succession planning |

### Assessment Outputs

**Generated Workbook**: `ISMS_A_5_9_Asset_Discovery_Assessment_YYYYMMDD.xlsx`

**Sheets** (8 total):
1. **Instructions**: How to complete this assessment
2. **Info Asset Discovery**: Information asset discovery procedures and sources
3. **IT Infrastructure Discovery**: IT asset discovery methods and tools
4. **Application Discovery**: Application inventory methods and license tracking
5. **Physical Asset Discovery**: Physical asset audit procedures and location tracking
6. **Personnel Asset Discovery**: Key role and competency identification
7. **Completeness Analysis**: Gap analysis and coverage verification
8. **Evidence Register**: Documentation of discovery activities and findings

**Compliance Metrics Generated**:

- Discovery coverage percentage by category
- Completeness score (discovered vs. inventoried)
- Gap count and severity
- Evidence completeness score

---

## Prerequisites

### What You Need Before Starting

**1. Access to Asset Sources**:

- CMDB or IT asset management system (if exists)
- Procurement/purchasing system
- HR system (for personnel assets only - roles/competencies, NOT personal data)
- Document repositories (SharePoint, file servers, DMS)
- Cloud service inventory (AWS, Azure, GCP management consoles if applicable)
- Network management tools (for infrastructure discovery)

**2. Personnel**:

- **Security Team**: Leads assessment, consolidates findings
- **IT Operations**: Provides IT infrastructure discovery data
- **System Owners**: Identify applications and information assets
- **Facilities Team**: Support physical asset discovery
- **HR Representative**: Provide personnel asset information (generically)

**3. Documentation**:

- Network topology diagrams (if available)
- Data flow diagrams (if available)
- Organizational chart (for competency mapping)
- Previous inventory (if exists - for comparison)

**4. Tools** (optional but recommended):

- Network discovery tools (Nmap, network scanners)
- Vulnerability scanners (often have asset discovery features)
- Cloud asset inventory tools (cloud provider native tools)
- Software inventory tools (license management systems)

**5. Time Allocation**:

- **Initial Discovery**: 20-40 hours (varies greatly by organization size and complexity)
- **Quarterly Updates**: 4-8 hours (once processes established)
- **Evidence Collection**: 4-8 hours per quarter

---

## Assessment Workflow

### Step-by-Step Process

```
Phase 1: Preparation (Day 1-2)
├─ Gather prerequisites
├─ Assemble assessment team
├─ Schedule discovery activities
└─ Generate workbook from Python script

Phase 2: Discovery Execution (Day 3-10)
├─ Domain 1: Information Asset Discovery
├─ Domain 2: IT Infrastructure Discovery
├─ Domain 3: Application Discovery
├─ Domain 4: Physical Asset Discovery
└─ Domain 5: Personnel Asset Discovery

Phase 3: Completeness Analysis (Day 11-12)
├─ Compare discovered assets vs. existing inventory
├─ Calculate coverage percentages
├─ Identify gaps (assets found but not inventoried)
└─ Document discovery limitations

Phase 4: Evidence Collection (Day 13-14)
├─ Collect discovery scan outputs
├─ Document manual discovery activities
├─ Photograph physical asset audits (if applicable)
└─ Compile evidence register

Phase 5: Review & Approval (Day 15)
├─ Quality check against checklist
├─ Security Team review
├─ CISO approval
└─ Submit to compliance dashboard
```

**Timeline**: 15 working days for initial assessment, 5 days for quarterly updates

---

## Completing Each Sheet

### Sheet 1: Instructions

**Purpose**: Provides overview and guidance for completing this workbook.

**What to Do**:

- Read the instructions completely before starting
- Note the assessment scope and objectives
- Understand the color coding and validation rules
- Review the workflow diagram

**No data entry required** - informational only.

---

### Sheet 2: Information Asset Discovery

**Purpose**: Document procedures for discovering information assets (databases, documents, IP, configurations).

**What This Sheet Captures**:

- Discovery methods used for each information asset category
- Sources consulted (systems, repositories, documentation)
- Frequency of discovery activities
- Responsible parties
- Completeness assessment results
- Identified gaps

**Column Definitions**:

| Column | Purpose | How to Complete |
|--------|---------|-----------------|
| **Asset Category** | Type of information asset | Dropdown: Structured Data / Unstructured Documents / Records & Archives / Intellectual Property / Configuration & Parameters / Authentication & Cryptographic / Communication Records / Business Intelligence |
| **Discovery Method** | How assets in this category are found | Dropdown: Automated Scan / Manual Review / System Query / Document Search / Repository Analysis / Vendor Documentation / Interview |
| **Discovery Source** | Where you look for these assets | Free text: Specific systems, repositories, locations |
| **Discovery Tool** | Tool used (if automated) | Free text: Tool name/version or "Manual" |
| **Frequency** | How often discovery is performed | Dropdown: Real-time / Daily / Weekly / Monthly / Quarterly / Annually / Ad-hoc |
| **Responsible Party** | Who performs discovery | Free text: Role or team name |
| **Last Discovery Date** | When discovery last performed | Date field |
| **Assets Discovered** | Count of assets found | Numeric |
| **Assets Inventoried** | Count in inventory | Numeric |
| **Coverage %** | Inventoried/Discovered × 100 | Auto-calculated |
| **Gap Count** | Discovered but not inventoried | Auto-calculated |
| **Gap Severity** | Impact of missing assets | Dropdown: Critical / High / Medium / Low |
| **Remediation Plan** | How gaps will be addressed | Free text |
| **Target Date** | When gaps will be closed | Date field |
| **Evidence Reference** | Link to evidence | Reference to Evidence Register sheet |
| **Notes** | Additional context | Free text |

**How to Complete**:

1. **Start with Structured Data (Databases)**:

   - **Example**: "Production PostgreSQL databases discovered via database catalog queries"
   - **Discovery Method**: System Query
   - **Discovery Source**: "PostgreSQL system catalogs (pg_database, information_schema)"
   - **Discovery Tool**: "psql scripts or DBeaver"
   - **Frequency**: Monthly
   - **Responsible Party**: Database Team
   - **Last Discovery Date**: [Actual date]
   - **Assets Discovered**: [Count databases found]
   - **Assets Inventoried**: [Count currently in inventory]
   - **Coverage %**: [Auto-calculated - aim for ≥95%]
   - **Gap Count**: [Auto-calculated]
   - **Gap Severity**: Assess impact - databases are typically Critical or High
   - **Remediation Plan**: "Add missing databases to inventory by [date]"
   - **Evidence Reference**: "DISC-001" (create entry in Evidence Register)

2. **Continue with Unstructured Documents**:

   - Consider file servers, SharePoint sites, document management systems
   - **Example**: "Contract documents in legal repository"
   - **Discovery Method**: Repository Analysis
   - **Discovery Source**: "SharePoint Legal Site, /contracts folder"
   - **Discovery Tool**: "SharePoint API or manual review"
   - **Completeness Note**: Document repositories are challenging - focus on HIGH-VALUE documents (contracts, legal, IP), not every individual file

3. **Process Each Information Asset Category**:

   - Structured Data (databases, data warehouses)
   - Unstructured Documents (file servers, DMS, SharePoint)
   - Records & Archives (compliance retention systems)
   - Intellectual Property (source code repos, patent databases)
   - Configuration & Parameters (system configs, IaC templates)
   - Authentication & Cryptographic (key stores, certificate repositories)
   - Communication Records (email archives, chat logs)
   - Business Intelligence (BI tools, reports, dashboards)

**Common Pitfalls**:

- ❌ Trying to inventory every single file (millions of files is not feasible)
- ✅ Focus on HIGH-VALUE information assets and logical groupings
- ❌ Ignoring configuration files (these are critical for recovery!)
- ✅ Document configuration repositories, IaC templates, system configs
- ❌ Forgetting about archived data
- ✅ Check backup systems, archive storage, offline media

**Completeness Target**: ≥95% for Critical information assets, ≥90% for Standard

---

### Sheet 3: IT Infrastructure Discovery

**Purpose**: Document procedures for discovering IT infrastructure assets (servers, storage, networking, endpoints).

**What This Sheet Captures**:

- Discovery methods for each IT infrastructure category
- Automated scanning tools and configurations
- CMDB integration status
- Network topology verification
- Endpoint inventory completeness
- Cloud infrastructure discovery
- Physical datacenter assets

**Column Definitions**:

| Column | Purpose | How to Complete |
|--------|---------|-----------------|
| **Infrastructure Category** | Type of IT asset | Dropdown: Physical Servers / Virtual Machines / Containers / Storage Systems / Backup Infrastructure / Network Infrastructure / Endpoints / Cloud Infrastructure / Security Appliances |
| **Discovery Method** | How assets are found | Dropdown: Network Scan / Agent-Based / Agentless Scan / Cloud API / Hypervisor Query / CMDB / Physical Audit / SNMP Poll |
| **Discovery Tool** | Specific tool or system | Free text: Tool name/version |
| **Discovery Scope** | Network ranges, cloud accounts covered | Free text: IP ranges, VPCs, accounts |
| **Frequency** | How often scans run | Dropdown: Real-time / Daily / Weekly / Monthly / Quarterly |
| **Last Scan Date** | When discovery last executed | Date field |
| **Assets Discovered** | Count found in scan | Numeric |
| **Assets in CMDB/Inventory** | Count currently documented | Numeric |
| **Coverage %** | Documented/Discovered × 100 | Auto-calculated |
| **Gap Count** | Found but not documented | Auto-calculated |
| **Gap Severity** | Impact of missing assets | Dropdown: Critical / High / Medium / Low |
| **False Positive Rate** | % of discovered assets that are actually invalid | Numeric (0-100) |
| **Verification Method** | How you confirm discovery accuracy | Free text |
| **Responsible Party** | Who manages discovery | Free text: Team/role |
| **Remediation Plan** | How gaps will be addressed | Free text |
| **Target Date** | Gap closure deadline | Date field |
| **Evidence Reference** | Link to scan outputs | Reference to Evidence Register |
| **Notes** | Additional context | Free text |

**How to Complete**:

1. **Physical Servers**:

   - **Discovery Method**: Network Scan + Physical Audit (for datacenters)
   - **Discovery Tool**: "Nmap, Qualys, or datacenter inventory system"
   - **Discovery Scope**: "Production datacenter: 10.1.0.0/16, DR site: 10.2.0.0/16"
   - **Frequency**: Weekly (scans) + Quarterly (physical audit)
   - **Assets Discovered**: [Count from scan + physical count]
   - **Assets in CMDB**: [Count from CMDB query]
   - **Verification Method**: "Cross-reference scan with asset tags, serial numbers"
   - **False Positive Rate**: Typically 5-10% (printers, IoT devices, etc.)

2. **Virtual Machines**:

   - **Discovery Method**: Hypervisor Query
   - **Discovery Tool**: "VMware vCenter API / Hyper-V PowerShell / Cloud provider CLI"
   - **Frequency**: Daily (automated query)
   - **Verification**: Compare with hypervisor management console

3. **Containers**:

   - **Discovery Method**: Container Orchestrator API
   - **Discovery Tool**: "Kubernetes API / Docker API / Registry query"
   - **Note**: Container discovery is challenging due to ephemeral nature
   - **Approach**: Focus on container IMAGES and persistent services, not individual container instances

4. **Storage Systems**:

   - **Discovery Method**: SNMP Poll + Admin Console
   - **Discovery Tool**: "SAN management tools, NAS admin consoles"
   - **Include**: SAN, NAS, file servers, backup systems, cloud storage buckets

5. **Network Infrastructure**:

   - **Discovery Method**: SNMP Poll + Network Management System
   - **Discovery Tool**: "Network management platform (SolarWinds, PRTG, Nagios, etc.)"
   - **Scope**: Routers, switches, firewalls, load balancers, WAFs, VPN concentrators, wireless APs
   - **Verification**: Physical datacenter walk-through quarterly

6. **Endpoints**:

   - **Discovery Method**: Agent-Based (if endpoint management deployed)
   - **Discovery Tool**: "MDM, SCCM, Jamf, endpoint management agent"
   - **Challenge**: BYOD and unmanaged devices
   - **Approach**: Define what's IN SCOPE (company-owned, managed BYOD) vs. OUT OF SCOPE (personal devices)

7. **Cloud Infrastructure**:

   - **Discovery Method**: Cloud Provider API
   - **Discovery Tool**: "AWS Config, Azure Resource Graph, GCP Asset Inventory"
   - **Frequency**: Daily (cloud changes rapidly)
   - **Verification**: Cloud security posture management tools

**Common Pitfalls**:

- ❌ Only scanning accessible networks (missing DMZ, management networks)
- ✅ Scan ALL network segments including out-of-band management
- ❌ Ignoring ephemeral cloud resources
- ✅ Focus on persistent resources, document ephemeral patterns
- ❌ Missing endpoints outside corporate network
- ✅ Document endpoint management coverage, note gaps (remote workers, etc.)

**Completeness Target**: ≥98% for IT infrastructure (more stable than information)

---

### Sheet 4: Application Discovery

**Purpose**: Document procedures for discovering applications and software assets.

**What This Sheet Captures**:

- Business application inventory methods
- SaaS service discovery and license tracking
- Custom developed application catalog
- Software license management integration
- API and integration service mapping
- Development tool inventory

**Column Definitions**:

| Column | Purpose | How to Complete |
|--------|---------|-----------------|
| **Application Category** | Type of application | Dropdown: Business Application / SaaS Service / Custom Development / Mobile App / API/Integration / Development Tool / Collaboration Platform |
| **Discovery Method** | How applications are identified | Dropdown: License Management System / Procurement Records / Software Inventory Tool / Cloud SSO Logs / Expense Reports / User Survey / Development Repository |
| **Discovery Source** | Specific system or process | Free text: System name, URL, or procedure |
| **Discovery Tool** | Tool used for discovery | Free text: Tool name or "Manual" |
| **Frequency** | Discovery frequency | Dropdown: Real-time / Monthly / Quarterly / Annually / Upon Procurement |
| **Last Discovery Date** | When last performed | Date field |
| **Applications Discovered** | Count identified | Numeric |
| **Applications Inventoried** | Count in inventory | Numeric |
| **Coverage %** | Documented/Discovered × 100 | Auto-calculated |
| **Gap Count** | Found but not documented | Auto-calculated |
| **License Tracking** | Are licenses tracked? | Dropdown: Yes - Automated / Yes - Manual / No / N/A |
| **Usage Monitoring** | Is usage tracked? | Dropdown: Yes - Active Monitoring / Yes - Periodic Review / No |
| **Shadow IT Risk** | Risk of unapproved apps | Dropdown: High / Medium / Low / None |
| **Responsible Party** | Who manages discovery | Free text: Team/role |
| **Remediation Plan** | How gaps will be addressed | Free text |
| **Target Date** | Gap closure deadline | Date field |
| **Evidence Reference** | Link to evidence | Reference to Evidence Register |
| **Notes** | Additional context | Free text |

**How to Complete**:

1. **Business Applications** (ERP, CRM, HR systems, etc.):

   - **Discovery Method**: License Management System + Procurement Records
   - **Discovery Source**: "Software asset management tool, procurement database"
   - **Example**: "SAP ERP, Salesforce CRM, Workday HRIS"
   - **License Tracking**: Should be "Yes - Automated" or "Yes - Manual"
   - **Usage Monitoring**: Check if usage logs available

2. **SaaS Services**:

   - **Discovery Method**: Cloud SSO Logs + Expense Reports
   - **Discovery Source**: "Okta/Entra ID app catalog, corporate credit card statements"
   - **Challenge**: Shadow IT (users signing up for services without approval)
   - **Shadow IT Risk**: Assess based on industry (High for tech companies, Medium for others)
   - **Verification**: Cloud access security broker (CASB) if deployed

3. **Custom Developed Applications**:

   - **Discovery Method**: Development Repository + Deployment Records
   - **Discovery Source**: "GitHub/GitLab organization, CI/CD pipelines, server deployments"
   - **Discovery Tool**: "Git repository API, deployment tracking"
   - **Include**: Web apps, mobile apps, internal tools, APIs

4. **Mobile Applications**:

   - **Discovery Method**: Mobile Device Management (MDM)
   - **Discovery Source**: "MDM console (Jamf, Intune, MobileIron)"
   - **Scope**: Company-developed and approved third-party apps

5. **APIs and Integration Services**:

   - **Discovery Method**: API Gateway Logs + Integration Platform
   - **Discovery Source**: "API management platform, integration middleware"
   - **Example**: "REST APIs, SOAP services, message queues"
   - **Note**: Often overlooked but critical for data flow understanding

6. **Development Tools**:

   - **Discovery Method**: License Management + Software Inventory
   - **Discovery Source**: "IDE licenses, DevOps tool licenses, compiler licenses"
   - **Example**: "Visual Studio, IntelliJ IDEA, Docker Desktop licenses"

**Common Pitfalls**:

- ❌ Only tracking "official" apps (missing shadow IT)
- ✅ Multiple discovery methods to catch shadow IT (SSO logs, expense reports, network traffic analysis)
- ❌ Ignoring APIs and integration services
- ✅ Map data flows, document API inventory
- ❌ Forgetting about mobile apps
- ✅ Use MDM to track managed mobile apps

**Completeness Target**: ≥90% for applications (shadow IT makes 100% unrealistic)

---

### Sheet 5: Physical Asset Discovery

**Purpose**: Document procedures for discovering physical assets supporting operations.

**What This Sheet Captures**:

- Facility and datacenter inventory methods
- Removable media tracking procedures
- Physical security equipment inventory
- Paper document and printed material procedures
- Asset tag verification processes

**Column Definitions**:

| Column | Purpose | How to Complete |
|--------|---------|-----------------|
| **Physical Asset Category** | Type of physical asset | Dropdown: Facilities / Datacenter Infrastructure / Removable Media / Physical Security Equipment / Paper Documents / Printed Materials / Other Equipment |
| **Discovery Method** | How assets are identified | Dropdown: Physical Audit / Asset Tag Scan / Procurement Records / Facilities Management System / Media Log / Document Register |
| **Discovery Frequency** | How often audits performed | Dropdown: Monthly / Quarterly / Semi-Annually / Annually |
| **Last Audit Date** | When last performed | Date field |
| **Assets Discovered** | Count identified in audit | Numeric |
| **Assets Inventoried** | Count in inventory | Numeric |
| **Coverage %** | Documented/Discovered × 100 | Auto-calculated |
| **Gap Count** | Found but not documented | Auto-calculated |
| **Gap Severity** | Impact of missing assets | Dropdown: Critical / High / Medium / Low |
| **Location** | Where assets are located | Free text: Building, room, rack |
| **Asset Tagging** | Are assets physically tagged? | Dropdown: Yes - RFID / Yes - Barcode / Yes - Manual Label / No |
| **Tracking System** | System used for tracking | Free text: System name or "Manual register" |
| **Responsible Party** | Who manages physical assets | Free text: Facilities team, security team |
| **Remediation Plan** | How gaps will be addressed | Free text |
| **Target Date** | Gap closure deadline | Date field |
| **Evidence Reference** | Link to audit photos/records | Reference to Evidence Register |
| **Notes** | Additional context | Free text |

**How to Complete**:

1. **Facilities** (Buildings, Offices, Datacenters):

   - **Discovery Method**: Facilities Management System + Physical Audit
   - **Discovery Frequency**: Annually (full audit) + Quarterly (changes)
   - **What to Document**: All facilities within ISMS scope
   - **Include**: Office locations, datacenters, server rooms, wiring closets
   - **Asset Tagging**: Typically N/A for buildings

2. **Datacenter Infrastructure** (Racks, Power, Cooling):

   - **Discovery Method**: Physical Audit + Datacenter Management System
   - **Discovery Frequency**: Quarterly
   - **Include**: Server racks, UPS systems, HVAC equipment, fire suppression
   - **Asset Tagging**: Yes (physical labels on racks, equipment)
   - **Verification**: Walk-through with facilities team

3. **Removable Media** (USB drives, External drives, Backup tapes):

   - **Discovery Method**: Media Log + Physical Audit
   - **Discovery Frequency**: Monthly for backup tapes, Quarterly for other media
   - **Challenge**: Removable media often untracked or lost
   - **Best Practice**: Implement check-in/check-out log for all removable media
   - **Include**: USB drives, external hard drives, backup tapes, optical media, SD cards
   - **Critical**: Track WHO has media, WHERE it is, WHEN last verified

4. **Physical Security Equipment**:

   - **Discovery Method**: Security System Inventory + Physical Audit
   - **Include**: Access control readers, surveillance cameras, alarm systems, locks
   - **Frequency**: Quarterly
   - **Responsible Party**: Physical security team or facilities

5. **Paper Documents and Printed Materials**:

   - **Discovery Method**: Document Register + Physical Audit
   - **Challenge**: Virtually impossible to inventory every piece of paper
   - **Approach**: Focus on HIGH-VALUE paper documents:
     - Signed contracts (original copies)
     - Legal documents requiring physical signature
     - Archived records (compliance retention)
     - Classified documents (if applicable)
   - **Frequency**: Annually (full audit), Monthly (sensitive document register review)

6. **Other Equipment** (Printers, Scanners, Specialized Equipment):

   - **Discovery Method**: Asset Tag Scan + Procurement Records
   - **Asset Tagging**: Yes - barcode or RFID preferred
   - **Tracking System**: Physical asset management system

**Common Pitfalls**:

- ❌ Trying to inventory every piece of paper (not feasible)
- ✅ Focus on high-value documents with retention requirements
- ❌ Forgetting about removable media (USB drives, backup tapes)
- ✅ Implement strict check-in/check-out procedures for removable media
- ❌ Not physically verifying assets (trusting old records)
- ✅ Conduct physical walk-throughs quarterly

**Completeness Target**: ≥90% for physical assets (some drift is expected)

---

### Sheet 6: Personnel Asset Discovery

**Purpose**: Document procedures for identifying key roles and competencies (NOT individual persons).

**What This Sheet Captures**:

- Critical role identification procedures
- Specialized competency mapping
- Succession planning alignment
- Competency gap analysis
- Training and certification tracking

**CRITICAL PRIVACY NOTE**: This sheet documents ROLES and COMPETENCIES, never individual person records. Focus is on "what capabilities does [Organization] need and have" not "who are the people."

**Column Definitions**:

| Column | Purpose | How to Complete |
|--------|---------|-----------------|
| **Role/Competency** | Generic role or skill | Free text: Role title or competency name (NEVER person name) |
| **Category** | Type of personnel asset | Dropdown: Executive Role / Technical Role / Regulatory Role / Specialized Competency / Language Skill / Certification |
| **Business Criticality** | Impact if capability lost | Dropdown: Critical / High / Medium / Low |
| **Discovery Method** | How role/competency identified | Dropdown: Org Chart Analysis / Job Description Review / Competency Matrix / HR System / Succession Plan / Manager Interview |
| **Current Capacity** | How many people have this capability | Numeric (e.g., "3 DBAs", "2 CISSP certified") |
| **Required Capacity** | How many needed for operations | Numeric |
| **Capacity Gap** | Current - Required | Auto-calculated |
| **Succession Plan** | Is succession planning in place? | Dropdown: Yes - Documented / Yes - Informal / No |
| **Training Available** | Can capability be developed internally? | Dropdown: Yes - Internal / Yes - External / No / Unknown |
| **Last Review Date** | When competency last assessed | Date field |
| **Responsible Party** | Who manages this competency | Free text: Department, manager role |
| **Remediation Plan** | How gaps will be addressed | Free text |
| **Target Date** | Gap closure deadline | Date field |
| **Evidence Reference** | Link to HR reports, training records | Reference to Evidence Register |
| **Notes** | Additional context | Free text |

**How to Complete**:

1. **Executive Roles**:

   - **Example**: "Chief Information Security Officer (CISO)"
   - **Category**: Executive Role
   - **Business Criticality**: Critical
   - **Discovery Method**: Org Chart Analysis
   - **Current Capacity**: 1
   - **Required Capacity**: 1 (minimum)
   - **Succession Plan**: Should be "Yes - Documented" for C-level

2. **Technical Roles**:

   - **Example**: "Database Administrator (DBA) Competency"
   - **Category**: Technical Role
   - **Business Criticality**: High (if databases are critical to operations)
   - **Discovery Method**: Competency Matrix + Job Description Review
   - **Current Capacity**: 3 (three people have DBA skills)
   - **Required Capacity**: 2 (minimum for 24/7 coverage)
   - **Capacity Gap**: 3 - 2 = +1 (surplus, good)

3. **Regulatory Roles**:

   - **Example**: "Data Protection Officer (DPO)"
   - **Category**: Regulatory Role
   - **Business Criticality**: Critical (if GDPR/nDSG applies)
   - **Discovery Method**: Regulatory Requirement Analysis
   - **Current Capacity**: 1
   - **Succession Plan**: Document succession or external DPO backup

4. **Specialized Competencies**:

   - **Example**: "Legacy COBOL Programming"
   - **Category**: Specialized Competency
   - **Business Criticality**: Assess based on legacy system importance
   - **Current Capacity**: 1 (only one person knows this)
   - **Risk**: Single point of failure
   - **Remediation**: Knowledge transfer, documentation, or system modernization

5. **Certifications**:

   - **Example**: "CISSP Certification"
   - **Category**: Certification
   - **Current Capacity**: 2 (two staff hold CISSP)
   - **Required Capacity**: Depends on client requirements or internal standards
   - **Training Available**: Yes - External (ISC2 training)

6. **Language Skills**:

   - **Example**: "Mandarin Language Fluency"
   - **Category**: Language Skill
   - **Business Criticality**: Depends on customer/supplier base
   - **Current Capacity**: 1
   - **Note**: Only track business-critical languages

**Common Pitfalls**:

- ❌ Recording individual person names (privacy violation!)
- ✅ Record roles/competencies generically: "Senior Network Engineer (2 FTE)"
- ❌ Ignoring succession planning (what if key person leaves?)
- ✅ Document succession for all critical roles
- ❌ Only tracking executive roles
- ✅ Include technical specialists, regulatory roles, unique competencies

**Completeness Target**: 100% accuracy for personnel assets (critical roles MUST be documented)

---

### Sheet 7: Completeness Analysis

**Purpose**: Aggregate discovery results, calculate coverage metrics, and identify gaps across all categories.

**What This Sheet Captures**:

- Overall inventory completeness by category
- Gap prioritization by severity
- Remediation progress tracking
- Trending over time (compare to previous quarters)

**Column Definitions**:

| Column | Purpose | How to Complete |
|--------|---------|-----------------|
| **Asset Category** | High-level category | Auto-populated from other sheets |
| **Target Completeness %** | Policy requirement | Fixed: 95% (Critical), 90% (Standard), per policy Section 2.5.1 |
| **Current Completeness %** | Actual achievement | Auto-calculated from discovery sheets |
| **Gap vs. Target** | How far from target | Auto-calculated (Current - Target) |
| **Compliance Status** | Met target or not? | Auto-calculated: ✅ Compliant / ⚠️ At Risk / ❌ Non-Compliant |
| **Total Assets Discovered** | Count from discovery | Auto-summed from discovery sheets |
| **Total Assets Inventoried** | Count in inventory | Auto-summed from discovery sheets |
| **Gap Count** | Not yet inventoried | Auto-calculated |
| **Critical Gaps** | Gap severity = Critical | Auto-counted |
| **High Gaps** | Gap severity = High | Auto-counted |
| **Medium Gaps** | Gap severity = Medium | Auto-counted |
| **Low Gaps** | Gap severity = Low | Auto-counted |
| **Remediation Status** | Progress on gap closure | Dropdown: Not Started / In Progress / Completed / Blocked |
| **Target Closure Date** | When gaps will be closed | Date field |
| **Trend vs. Last Quarter** | Improving or degrading? | Dropdown: Improved / Stable / Degraded / N/A (first assessment) |
| **Notes** | Context on gaps | Free text |

**How to Complete**:

This sheet is largely **AUTO-POPULATED** from the other discovery sheets. Your role is to:

1. **Review Auto-Calculated Metrics**:

   - Verify completeness percentages make sense
   - Check gap counts align with your understanding

2. **Set Remediation Status**:

   - For each category with gaps, set status:
     - "Not Started": Haven't begun addressing gaps
     - "In Progress": Actively working on adding missing assets
     - "Completed": All gaps closed
     - "Blocked": Waiting on resources, approvals, or technical issues

3. **Set Target Closure Dates**:

   - Critical gaps: Within 30 days
   - High gaps: Within 60 days
   - Medium gaps: Within 90 days
   - Low gaps: Within 180 days or next planned inventory cycle

4. **Document Trends** (for quarterly updates):

   - Compare current quarter to previous quarter
   - "Improved": Completeness % increased
   - "Stable": Completeness % within 2% (no significant change)
   - "Degraded": Completeness % decreased (investigate why!)

**Interpretation Guide**:

| Completeness % | Compliance Status | Action Required |
|----------------|------------------|-----------------|
| ≥95% (Critical assets) or ≥90% (Standard) | ✅ Compliant | Maintain current discovery procedures |
| 85-94% (Critical) or 85-89% (Standard) | ⚠️ At Risk | Increase discovery frequency, allocate resources |
| <85% | ❌ Non-Compliant | Immediate action required, escalate to CISO |

**Example Interpretation**:

```
Asset Category: Information Assets - Databases
Target Completeness: 95% (Critical)
Current Completeness: 92%
Gap vs. Target: -3%
Compliance Status: ⚠️ At Risk
Remediation Status: In Progress
Action: Add 3 discovered databases to inventory by [date]
```

---

### Sheet 8: Evidence Register

**Purpose**: Document all evidence collected during discovery activities for audit trail.

**What This Sheet Captures**:

- Discovery scan outputs and reports
- Physical audit photos and documentation
- Interview notes and meeting minutes
- System queries and API outputs
- Reconciliation reports
- Evidence metadata and storage locations

**Column Definitions**:

| Column | Purpose | How to Complete |
|--------|---------|-----------------|
| **Evidence ID** | Unique identifier | Format: DISC-001, DISC-002, etc. |
| **Evidence Type** | Type of evidence | Dropdown: Scan Output / Audit Report / Query Result / Interview Notes / Photo / System Export / Reconciliation Report / Meeting Minutes |
| **Related Domain** | Which discovery domain | Dropdown: Information Assets / IT Infrastructure / Applications / Physical Assets / Personnel Assets / Multiple Domains |
| **Evidence Description** | What the evidence shows | Free text: Brief description |
| **Collection Date** | When evidence collected | Date field |
| **Collected By** | Who collected evidence | Free text: Name/role |
| **File Name** | Evidence file name | Free text: Actual filename |
| **Storage Location** | Where evidence stored | Free text: Path, URL, or physical location |
| **Evidence Format** | File type or format | Dropdown: PDF / Excel / CSV / JSON / XML / Photo (JPEG/PNG) / Text / Other |
| **Retention Period** | How long to keep | Dropdown: 1 Year / 3 Years / 5 Years / 7 Years / Permanent |
| **Access Restriction** | Who can access evidence | Dropdown: Public / Internal / Confidential / Restricted |
| **Evidence Quality** | Is evidence sufficient? | Dropdown: Complete / Partial / Insufficient |
| **Related Sheet** | Which sheet references this | Free text: Sheet name(s) |
| **Notes** | Additional context | Free text |

**How to Complete**:

For each discovery activity, create evidence record:

1. **Network Scan Evidence**:

   - **Evidence ID**: DISC-001
   - **Evidence Type**: Scan Output
   - **Related Domain**: IT Infrastructure
   - **Evidence Description**: "Nmap scan results for production network 10.1.0.0/16"
   - **Collection Date**: [Scan date]
   - **Collected By**: IT Operations
   - **File Name**: nmap_scan_10.1.0.0_16_20260122.xml
   - **Storage Location**: /evidence/discovery/network_scans/
   - **Evidence Format**: XML
   - **Retention Period**: 3 Years
   - **Access Restriction**: Confidential (contains internal IP addresses)
   - **Evidence Quality**: Complete
   - **Related Sheet**: Sheet 3 - IT Infrastructure Discovery

2. **Database Query Evidence**:

   - **Evidence ID**: DISC-002
   - **Evidence Type**: Query Result
   - **Related Domain**: Information Assets
   - **Evidence Description**: "PostgreSQL database catalog query results"
   - **File Name**: postgres_database_list_20260122.csv
   - **Evidence Format**: CSV
   - **Retention Period**: 3 Years

3. **Physical Audit Evidence**:

   - **Evidence ID**: DISC-003
   - **Evidence Type**: Photo
   - **Related Domain**: Physical Assets
   - **Evidence Description**: "Datacenter rack audit photos"
   - **File Name**: datacenter_rack_audit_20260122.zip (contains multiple photos)
   - **Evidence Format**: Photo (JPEG/PNG)
   - **Retention Period**: 3 Years

4. **SaaS Discovery Evidence**:

   - **Evidence ID**: DISC-004
   - **Evidence Type**: System Export
   - **Related Domain**: Applications
   - **Evidence Description**: "Okta application catalog export"
   - **File Name**: okta_apps_20260122.json
   - **Evidence Format**: JSON
   - **Retention Period**: 3 Years

5. **HR Competency Report**:

   - **Evidence ID**: DISC-005
   - **Evidence Type**: System Export
   - **Related Domain**: Personnel Assets
   - **Evidence Description**: "HR competency matrix (anonymized, roles only)"
   - **File Name**: hr_competency_matrix_20260122.xlsx
   - **Evidence Format**: Excel
   - **Access Restriction**: Restricted (even anonymized, treat carefully)
   - **Retention Period**: 3 Years

**Evidence Storage Best Practices**:

- Store evidence centrally (SharePoint, document management system)
- Organize by assessment period (Q1-2026, Q2-2026, etc.)
- Restrict access (only security team and auditors)
- Back up evidence (part of overall backup strategy)
- Maintain chain of custody for audit purposes

**Retention Periods** (per policy and regulatory requirements):

- Audit evidence: 7 years minimum (ISO 27001 requirement)
- Discovery scans: 3 years (sufficient for trend analysis)
- Photos: 3 years
- HR data: Check local data protection laws (typically 3-7 years)

---

## Evidence Collection

### What Evidence to Collect

**Discovery Scans and Reports**:

- Network scan outputs (Nmap, vulnerability scanner reports)
- CMDB extracts or queries
- Cloud API outputs (AWS Config, Azure Resource Graph)
- Database catalog queries
- Software inventory reports

**Physical Audit Documentation**:

- Photos of datacenter racks (with visible asset tags)
- Physical audit checklists (signed)
- Asset tag scan results (if RFID/barcode system)
- Walk-through observation notes

**System Queries and Exports**:

- Hypervisor VM lists
- Container registry inventories
- SaaS application catalogs (Okta, Entra ID)
- License management system exports
- Procurement records

**Reconciliation Reports**:

- Discovered vs. Inventoried comparison
- Gap analysis reports
- Variance explanations

**Meeting and Interview Documentation**:

- Meeting minutes from discovery coordination meetings
- Interview notes from system owners
- Email correspondence related to discovery

### How to Collect Evidence

**1. Automated Collection** (Preferred):

- Schedule automated scans (daily, weekly, monthly per frequency)
- Export results to central repository automatically
- Use APIs to extract data programmatically
- Maintain version history (compare current vs. previous scans)

**2. Manual Collection** (When Necessary):

- Conduct physical walk-throughs with camera or tablet
- Document observations in structured forms
- Collect signatures on audit checklists
- Scan paper documents to PDF

**3. Evidence Organization**:
```
/evidence/
├── 2026-Q1/
│   ├── information-assets/
│   │   ├── database-discovery/
│   │   └── document-repository-analysis/
│   ├── it-infrastructure/
│   │   ├── network-scans/
│   │   ├── cmdb-extracts/
│   │   └── cloud-api-outputs/
│   ├── applications/
│   │   ├── saas-catalogs/
│   │   └── license-reports/
│   ├── physical-assets/
│   │   ├── datacenter-audit-photos/
│   │   └── media-logs/
│   └── personnel-assets/
│       └── competency-reports/
└── 2026-Q2/
    └── [same structure]
```

**4. Chain of Custody**:

- Record WHO collected evidence
- Record WHEN evidence was collected
- Record WHERE evidence came from (source system)
- Record HOW evidence was collected (method, tool)
- Maintain evidence log (the Evidence Register sheet)

### Evidence Quality Criteria

**Complete Evidence**:

- ✅ Covers all asset categories
- ✅ Includes metadata (date, source, collector)
- ✅ Machine-readable format where possible (CSV, JSON, XML)
- ✅ Sufficient detail for verification
- ✅ Properly stored with access controls

**Partial Evidence**:

- ⚠️ Covers some but not all categories
- ⚠️ Missing metadata
- ⚠️ Format makes analysis difficult (unstructured text)
- ⚠️ Requires supplementary information to interpret

**Insufficient Evidence**:

- ❌ Major categories missing
- ❌ No metadata (can't verify currency)
- ❌ Cannot be independently verified
- ❌ Lost or corrupted files

---

## Common Pitfalls

### Pitfall 1: Trying to Discover EVERYTHING

**Problem**: Attempting to inventory every single file, email, or piece of paper.

**Why It Fails**: Millions of objects, not feasible, not valuable.

**Solution**: Focus on HIGH-VALUE and CRITICAL assets. Use grouping for low-risk commodity items.

**Example**: 

- ❌ "Inventory every employee's email (millions of messages)"
- ✅ "Inventory email system (Exchange/Gmail) + archive system + retention policies"

### Pitfall 2: One-Time Discovery Exercise

**Problem**: Treating discovery as one-time project instead of ongoing process.

**Why It Fails**: Assets change constantly (new servers, new apps, people leave).

**Solution**: Establish PERIODIC discovery cadence per policy:

- Critical assets: Quarterly minimum
- Standard assets: Semi-annually minimum
- Low-risk assets: Annually minimum

### Pitfall 3: Only Automated Discovery

**Problem**: Relying 100% on automated scans, missing assets that aren't network-visible.

**Why It Fails**: Not all assets are discoverable by network scans (offline systems, air-gapped networks, physical media, paper documents, personnel competencies).

**Solution**: Combine automated and manual methods:

- Automated: Network scans, API queries, CMDB extracts
- Manual: Physical audits, interviews, document review

### Pitfall 4: Ignoring Shadow IT

**Problem**: Only documenting "officially approved" applications, missing shadow IT.

**Why It Fails**: Users increasingly adopt SaaS without IT approval. These unapproved apps process company data.

**Solution**: Multiple discovery methods:

- SSO logs (Okta, Entra ID)
- Corporate credit card statements
- Network traffic analysis (CASB)
- User surveys

### Pitfall 5: Privacy Violations in Personnel Assets

**Problem**: Recording individual person names, personal details in personnel asset inventory.

**Why It Fails**: Violates GDPR/nDSG privacy requirements.

**Solution**: Document ROLES and COMPETENCIES only:

- ❌ "John Smith - Senior DBA, hired 2015, salary €80K"
- ✅ "Database Administrator competency (3 qualified staff)"

### Pitfall 6: Not Documenting Discovery Limitations

**Problem**: Claiming 100% completeness when discovery has known limitations.

**Why It Fails**: Auditors will find gaps. Better to acknowledge limitations upfront.

**Solution**: Document what you CAN'T discover:

- "Network scans cannot detect offline or powered-off systems"
- "Shadow IT discovery limited to corporate SSO; personal subscriptions not visible"
- "Paper document inventory limited to high-value contracts; routine correspondence not tracked"

### Pitfall 7: Poor Evidence Quality

**Problem**: Collecting evidence but not organizing it properly or maintaining metadata.

**Why It Fails**: Evidence without context is useless. Auditors need to verify evidence currency and authenticity.

**Solution**: Use Evidence Register sheet religiously:

- Every piece of evidence gets unique ID
- Record collection date, collector, source
- Store evidence centrally with access controls
- Maintain chain of custody

### Pitfall 8: Not Validating Discovery Results

**Problem**: Trusting automated scan results without verification.

**Why It Fails**: Scans have false positives (printers detected as servers) and false negatives (firewalled systems not detected).

**Solution**: Validate discoveries:

- Cross-reference scan results with CMDB
- Physical verification for critical assets
- Interview system owners
- Test-spot random sample (5-10% of assets)

---

## Quality Checklist

Before submitting this assessment, verify:

### Completeness Checks

- [ ] All 5 discovery domains completed (Information, IT, Applications, Physical, Personnel)
- [ ] Discovery methods documented for each asset category
- [ ] Discovery frequencies defined (aligned with policy Section 2.5.3)
- [ ] Responsible parties assigned for each discovery activity
- [ ] Evidence collected for each discovery method
- [ ] Evidence Register populated with all evidence items

### Accuracy Checks

- [ ] Asset counts verified (spot-check against source systems)
- [ ] Coverage percentages calculated correctly (auto-formulas working)
- [ ] Gap counts align with understanding (manual review)
- [ ] Severity assessments are realistic (Critical/High/Medium/Low)
- [ ] False positive rates estimated (especially for network scans)

### Compliance Checks

- [ ] Critical assets meet ≥95% completeness target
- [ ] Standard assets meet ≥90% completeness target
- [ ] Gaps have remediation plans (no gaps without plan)
- [ ] Target dates set for gap closure (Critical: 30 days, High: 60 days, Medium: 90 days)
- [ ] Non-compliant categories escalated to CISO

### Evidence Checks

- [ ] Evidence exists for each discovery activity
- [ ] Evidence has metadata (date, collector, source)
- [ ] Evidence is stored securely with access controls
- [ ] Evidence retention periods set per policy
- [ ] Evidence quality assessed (Complete/Partial/Insufficient)

### Privacy Checks (Critical!)

- [ ] Personnel assets documented as ROLES, not persons
- [ ] No individual names in personnel sheet
- [ ] HR data anonymized appropriately
- [ ] Sensitive evidence marked "Restricted" or "Confidential"

### Review Checks

- [ ] Security Team reviewed all sheets
- [ ] IT Operations validated IT infrastructure discovery
- [ ] System Owners validated application discovery
- [ ] Facilities Team validated physical asset discovery
- [ ] HR reviewed personnel asset approach (privacy compliance)

### Documentation Checks

- [ ] All required fields completed (no blank mandatory fields)
- [ ] Notes provided for unusual situations
- [ ] Trends documented (if quarterly update)
- [ ] Remediation plans are specific and actionable

---

## Review & Approval

### Review Process

**Step 1: Self-Review** (Assessment Preparer)

- Complete quality checklist above
- Fix any identified issues
- Prepare summary for reviewers

**Step 2: Technical Review** (IT Operations, System Owners)

- Validate discovery methods are appropriate
- Confirm asset counts are reasonable
- Verify technical evidence is sufficient
- Sign off on IT infrastructure, application, and information asset sections

**Step 3: Security Review** (Information Security Manager)

- Review completeness against policy requirements
- Assess gap severity and remediation plans
- Verify evidence quality
- Check privacy compliance (especially personnel assets)
- Prepare summary for CISO

**Step 4: CISO Approval**

- Review executive summary
- Assess compliance status (on-target or at-risk)
- Approve remediation plans and resource allocation
- Escalate critical gaps to Executive Management if necessary
- Sign approval

**Step 5: Submission to Compliance Dashboard**

- Export metrics to dashboard consolidation workbook
- Update ISMS-IMP-A.5.9.5 (Compliance Dashboard)
- Archive assessment workbook
- Store evidence per retention policy

### Approval Criteria

**Approve** if:

- ✅ All discovery domains completed
- ✅ Critical assets ≥85% completeness (minimum acceptable, 95% target)
- ✅ Standard assets ≥80% completeness (minimum acceptable, 90% target)
- ✅ Evidence quality rated "Complete" or "Partial" (not "Insufficient")
- ✅ Remediation plans exist for all gaps
- ✅ Privacy compliance verified

**Conditional Approval** (with remediation plan) if:

- ⚠️ Critical assets 75-84% completeness
- ⚠️ Standard assets 70-79% completeness
- ⚠️ Some evidence gaps but major evidence exists
- ⚠️ Remediation plans need refinement

**Reject** if:

- ❌ Critical assets <75% completeness
- ❌ Standard assets <70% completeness
- ❌ Major evidence gaps or insufficient evidence
- ❌ No remediation plans for critical gaps
- ❌ Privacy violations identified

### Approval Record

Document approval in assessment workbook:

| Role | Name | Date | Signature/Email | Comments |
|------|------|------|----------------|----------|
| Assessment Preparer | [Name] | [Date] | [Email] | Completed assessment per specification |
| IT Operations Review | [Name] | [Date] | [Email] | Validated IT discovery methods |
| Information Security Manager | [Name] | [Date] | [Email] | Reviewed for compliance, evidence quality |
| CISO | [Name] | [Date] | [Email] | Approved / Conditional / Rejected |

---


**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
