**ISMS-IMP-A.8.1-7-18-19-S1-UG - Endpoint Discovery Process**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.8.1: User Endpoint Devices

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.8.1-7-18-19-S1-UG |
| **Version** | 1.0 |
| **Assessment Area** | Endpoint Discovery and Inventory Management |
| **Related Policy** | ISMS-POL-A.8.1-7-18-19, Section 2.1.1 (Endpoint Inventory), Section 2.1.2 (Endpoint Classification) |
| **Purpose** | Document comprehensive endpoint discovery process, establish endpoint inventory, and classify endpoints to support all four endpoint security controls |
| **Target Audience** | Endpoint Administrators, Security Engineers, IT Operations, Asset Management, System Administrators, Compliance Officers, Auditors |
| **Assessment Type** | Technical & Operational |
| **Review Cycle** | Monthly (inventory updates), Quarterly (process review) |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | [Date] | Initial implementation guide for endpoint discovery and inventory | ISMS Implementation Team |

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.8.1-7-18-19-S1-TG.

---

## Assessment Overview

### Purpose & Scope

**Assessment Name:** ISMS-IMP-A.8.1-7-18-19-S1 - Endpoint Discovery Process

#### What This Assessment Covers

This assessment establishes the FOUNDATION for all endpoint security controls by discovering and inventorying ALL user endpoint devices in your environment. This is the critical "WHAT devices do we have?" assessment that answers:

- What endpoint devices exist? (laptops, desktops, mobile devices, tablets, IoT)
- Where are these endpoints? (on-premises, remote, mobile, branch offices)
- Who owns them? (corporate-owned, BYOD, contractor, guest)
- How are they managed? (MDM-enrolled, domain-joined, unmanaged)
- What is their current status? (active, inactive, lost/stolen, disposed)

#### Key Principle

**You cannot protect what you cannot see.** Complete endpoint inventory is the prerequisite for:

- A.8.1 (Endpoint Device Security) - Cannot apply security baselines to unknown devices
- A.8.7 (Malware Protection) - Cannot verify protection coverage without complete inventory
- A.8.18 (Privileged Utilities) - Cannot monitor privileged utility usage on unknown endpoints
- A.8.19 (Software Installation) - Cannot control software on undiscovered endpoints

**Target Coverage:** ≥95% of network-connected endpoints (target: 100%)

#### What You'll Document

- **Endpoint Inventory** (Inventory worksheet): Complete list of all discovered endpoints with mandatory attributes
- **Endpoint Classification** (Classification worksheet): Classification by device type, ownership model, and criticality
- **Discovery Methods** (Discovery_Methods worksheet): All discovery methods used and their coverage
- **Inventory Quality Metrics** (Quality_Metrics worksheet): Coverage rate, accuracy, staleness
- **Evidence Register** (Evidence worksheet): Supporting documentation for inventory accuracy
- **Gap Analysis** (Gaps worksheet): Undiscovered endpoints, reconciliation issues, remediation plans

#### How This Relates to Other A.8.1-7-18-19 Assessments

| Assessment | Focus | Relationship to S1 |
|------------|-------|-------------------|
| **ISMS-IMP-A.8.1-7-18-19-S1** | **Endpoint Discovery** | **WHAT endpoints exist** |
| ISMS-IMP-A.8.1-7-18-19-S2 | Security Baselines | Applies security configurations to discovered endpoints |
| ISMS-IMP-A.8.1-7-18-19-S3 | Malware Protection | Verifies protection coverage on discovered endpoints |
| ISMS-IMP-A.8.1-7-18-19-S4 | Software Controls | Manages software on discovered endpoints |
| ISMS-IMP-A.8.1-7-18-19-S5 | Privileged Utilities | Monitors privileged tools on discovered endpoints |
| ISMS-IMP-A.8.1-7-18-19-S6 | Assessment & Compliance | Consolidated compliance view across all endpoints |

This assessment (S1) MUST be completed first - you cannot assess baselines, protection, or software controls until you know what endpoints exist!

### Who Should Complete This Assessment

#### Primary Stakeholders

1. **Endpoint Administrators** - MDM/UEM platform management, device enrollment
2. **Asset Management** - Hardware asset tracking, lifecycle management
3. **Network Administrators** - Network-based discovery, DHCP lease analysis
4. **Security Engineering** - Discovery methodology, coverage verification
5. **IT Operations** - Active Directory management, cloud platform access

#### Required Skills

- Familiarity with endpoint management platforms (Intune, Jamf, SCCM, etc.)
- Understanding of network discovery techniques (network scanning, DHCP analysis)
- Access to Active Directory, Entra ID, or LDAP
- Basic scripting knowledge (PowerShell, Bash, or Python - helpful but not mandatory)

#### Time Commitment

- **Initial discovery:** 20-40 hours (depends on environment size and complexity)
- **Monthly updates:** 2-4 hours (automated discovery synchronization, manual reconciliation)
- **Quarterly review:** 4-8 hours (validate coverage, update classification, gap remediation)

### Expected Outputs

Upon completion, you will have:

1. ✅ **Complete endpoint inventory** - All discovered endpoints with mandatory attributes (≥95% coverage)
2. ✅ **Endpoint classification** - Every endpoint classified by type, ownership, criticality
3. ✅ **Discovery method documentation** - All discovery methods used and their effectiveness
4. ✅ **Quality metrics** - Coverage rate, accuracy percentage, inventory staleness
5. ✅ **Gap analysis** - Identified undiscovered endpoints with remediation plans
6. ✅ **Evidence register** - Supporting documentation (MDM exports, AD queries, network scans)
7. ✅ **Monthly update process** - Automated discovery synchronization established
8. ✅ **Approved inventory** - Three-level approval workflow completed

---

## Prerequisites

### Information You'll Need

Before starting this assessment, gather:

#### 1. System Access

- **MDM/UEM Platform Access**: Administrator access to Intune, Jamf, SCCM, Google Workspace MDM, VMware Workspace ONE, or other MDM platform
- **Active Directory Access**: Read access to Active Directory, Entra ID, or LDAP
- **Network Access**: Administrator access for network scanning (authorized network scans)
- **DHCP Server Access**: Access to DHCP lease databases
- **Cloud Platform Access**: Azure Portal, AWS Console, GCP Console (if endpoints hosted in cloud)
- **Asset Management System**: Access to hardware asset tracking system (ServiceNow, Asset Panda, etc.)

#### 2. Documentation

- Current network architecture diagrams (network segments, VLANs, subnets)
- Endpoint management architecture (MDM platforms, management servers)
- BYOD program documentation (if applicable)
- Contractor device agreements
- Guest network policies

#### 3. Tools & Software

- **Network Scanning Tools**: Nmap, Advanced IP Scanner, SolarWinds, Lansweeper, or equivalent
- **PowerShell/Bash/Python**: For scripting and automation (optional but recommended)
- **Excel Workbook**: Endpoint_Inventory.xlsx (generated by generate_a817_1_endpoint_inventory.py script)

#### 4. Approvals & Authorizations

- **Network Scanning Authorization**: Documented approval for active network scanning (may trigger IDS/IPS alerts)
- **Privacy Approval**: BYOD discovery must comply with employee privacy requirements (GDPR, FADP)
- **Data Access Authorization**: Permission to access endpoint management systems and user data

---

## Assessment Workflow

### High-Level Process

The endpoint discovery process follows a **six-phase approach**:

```
Phase 1: Planning & Scoping
   ↓
Phase 2: Automated Discovery (MDM, AD, Network Scanning)
   ↓
Phase 3: Manual Discovery (Surveys, Documentation Review)
   ↓
Phase 4: Data Consolidation & Deduplication
   ↓
Phase 5: Classification & Validation
   ↓
Phase 6: Ongoing Maintenance & Updates
```

**Estimated Timeline**: 2-4 weeks for initial discovery (depending on environment size)

### Detailed Workflow Steps

#### Phase 1: Planning & Scoping (1-2 days)

**Activities:**
1. Define endpoint discovery scope (device types, locations, ownership models)
2. Identify discovery methods appropriate for your environment
3. Obtain necessary access and authorizations
4. Schedule network scanning windows (if required)
5. Communicate with stakeholders (users, managers, compliance)

**Deliverable:** Discovery plan document with scope, methods, timeline, approvals

#### Phase 2: Automated Discovery (3-5 days)

**Activities:**
1. **MDM/UEM Export**: Export device inventory from Intune, Jamf, SCCM, etc.
2. **Active Directory Query**: Query AD for computer objects (domain-joined endpoints)
3. **Network Scanning**: Perform network scans to discover all networked devices
4. **DHCP Lease Analysis**: Extract DHCP leases to identify active endpoints
5. **Cloud Platform APIs**: Query Azure, AWS, GCP for cloud-hosted VMs

**Deliverable:** Raw discovery data from each source (CSV exports, scan results)

#### Phase 3: Manual Discovery (2-3 days)

**Activities:**
1. **User Surveys**: Send surveys to identify BYOD devices, unmanaged endpoints
2. **Documentation Review**: Review procurement records, asset databases
3. **Physical Inventory**: Walk data center, offices to identify unnetworked devices
4. **Exception Handling**: Document air-gapped devices, lab/test environments

**Deliverable:** Manual discovery records, survey responses, exception documentation

#### Phase 4: Data Consolidation & Deduplication (3-5 days)

**Activities:**
1. **Import Discovery Data**: Import all discovery sources into Endpoint_Inventory.xlsx
2. **Deduplication**: Identify and merge duplicate records (same device discovered multiple times)
3. **Data Normalization**: Standardize device names, OS versions, IP addresses
4. **Data Quality Validation**: Verify mandatory attributes populated, validate data accuracy

**Deliverable:** Consolidated endpoint inventory with duplicates removed

#### Phase 5: Classification & Validation (2-3 days)

**Activities:**
1. **Device Type Classification**: Classify endpoints as laptop, desktop, mobile, tablet, IoT, etc.
2. **Ownership Model Classification**: Classify as corporate-owned, BYOD, contractor, guest, lab/test
3. **Criticality Classification**: Classify as critical, high, medium, low based on data accessed
4. **Spot-Check Validation**: Manually verify random sample (20 endpoints) for accuracy
5. **Coverage Calculation**: Calculate coverage rate (discovered endpoints / expected endpoints)

**Deliverable:** Classified endpoint inventory with validation results

#### Phase 6: Ongoing Maintenance & Updates (Continuous)

**Activities:**
1. **Weekly Automated Sync**: Synchronize inventory with MDM, AD (automated via scripts)
2. **Monthly Reconciliation**: Reconcile automated discovery with manual records
3. **Quarterly Review**: Validate classification, update criticality, gap remediation
4. **Stale Endpoint Flagging**: Flag endpoints not seen >30 days for investigation
5. **New Device Enrollment**: Ensure new devices added to inventory within 24 hours

**Deliverable:** Up-to-date endpoint inventory (updated weekly, reviewed monthly)

---

## Sheet-by-Sheet Completion Guide

### Sheet 1: Inventory

**Purpose:** Complete list of all discovered endpoints with mandatory attributes

**Completion Steps:**

1. **Import Discovery Data**

   - Export device inventory from MDM platform (Intune, Jamf, SCCM)
   - Export computer objects from Active Directory
   - Import network scan results (Nmap, Lansweeper, etc.)
   - Import DHCP lease data
   - Import cloud platform VM lists (Azure, AWS, GCP)

2. **Populate Mandatory Attributes** (for each endpoint):

   - **Device_ID**: Unique identifier (serial number, UUID, asset tag)
   - **Hostname**: Computer/device name (DESKTOP-ABC123, iPhone-JohnSmith)
   - **Device_Type**: Laptop, Desktop, Smartphone, Tablet, IoT, VDI Client, etc.
   - **Operating_System**: OS and version (Windows 11 23H2, macOS 14.2, iOS 17.1)
   - **Owner**: Assigned user or department (John Smith, IT Department, Visitor)
   - **Ownership_Model**: Corporate-Owned, BYOD, Contractor, Guest, Lab/Test
   - **Location**: Physical location (Office, Remote, Mobile, Data Center, Branch Office)
   - **Network_Connection**: Wired, Wireless, VPN, Direct Internet
   - **Criticality**: Critical, High, Medium, Low
   - **Last_Seen**: Date/time of last successful network connection
   - **Discovery_Method**: MDM, Network Scan, Manual Entry, AD Query, DHCP Lease
   - **Discovery_Date**: Date device first added to inventory

3. **Data Quality Checks**

   - No blank Device_IDs (every endpoint must have unique identifier)
   - Hostname format consistent (standardized naming convention)
   - OS version format consistent (e.g., "Windows 11 23H2" not "Win11")
   - Last_Seen date within last 90 days (flag stale endpoints >30 days)

4. **Deduplication**

   - Identify duplicate records (same Device_ID from multiple sources)
   - Merge duplicates (keep most recent data, reconcile conflicts)
   - Mark merged records in Notes column

**Common Data Sources:**

- Intune: Devices → All devices → Export
- Jamf Pro: Devices → Computers → Advanced Search → Export
- SCCM: Assets and Compliance → Devices → Export
- Active Directory: PowerShell query `Get-ADComputer -Filter * -Properties *`
- Network Scan: Nmap output, Lansweeper export, SolarWinds report

**Quality Target:** ≥95% of expected endpoints discovered, <5% duplicate records

### Sheet 2: Classification

**Purpose:** Classify endpoints by device type, ownership model, and criticality

**Completion Steps:**

1. **Device Type Classification** (for each endpoint):

   - Review Inventory sheet Device_Type column
   - Verify device type accurate (laptop vs. desktop vs. mobile)
   - Use vendor/model to determine type if ambiguous
   - Flag unusual device types for manual review (e.g., IoT devices)

2. **Ownership Model Classification** (for each endpoint):

   - **Corporate-Owned**: Device purchased by organization (check asset database)
   - **BYOD**: Personal device used for work (check MDM enrollment type, user survey)
   - **Contractor**: Device owned by contractor/consultant (check user account type)
   - **Guest**: Temporary visitor device (check guest network access logs)
   - **Lab/Test**: Development, testing, QA endpoints (check device naming, location)

3. **Criticality Classification** (for each endpoint):

   - **Critical**: Endpoints accessing highly sensitive data (finance, HR, executive, legal)
     - Criteria: User role (executive, finance, HR), data classification (restricted/confidential)
   - **High**: Standard business endpoints (most corporate laptops/desktops)
     - Criteria: Corporate-owned, accesses internal systems, processes business data
   - **Medium**: Limited access endpoints (kiosks, guest devices with limited access)
     - Criteria: Restricted access, no sensitive data, public-facing
   - **Low**: Highly restricted endpoints (isolated lab devices, no data storage)
     - Criteria: Network isolated, no production data, test/development only

4. **Classification Rules Application**

   - Apply classification rules consistently across all endpoints
   - Document classification rationale in Notes column
   - Flag endpoints requiring manual classification decision

**Classification Decision Trees:**

**Ownership Model:**
```
1. Is device in asset database as purchased by organization?
   YES → Corporate-Owned
   NO → Go to step 2

2. Is device enrolled in MDM as personal device?
   YES → BYOD
   NO → Go to step 3

3. Is user a contractor or temporary staff?
   YES → Contractor
   NO → Go to step 4

4. Is device on guest network?
   YES → Guest
   NO → Review manually (likely Lab/Test)
```

**Criticality:**
```
1. Does user access restricted data (financial, HR, legal, executive)?
   YES → Critical
   NO → Go to step 2

2. Is device corporate-owned and accessing internal systems?
   YES → High
   NO → Go to step 3

3. Is device restricted to limited access (kiosk, guest)?
   YES → Medium
   NO → Low
```

**Quality Target:** 100% of endpoints classified

### Sheet 3: Discovery_Methods

**Purpose:** Document all discovery methods used and their effectiveness

**Completion Steps:**

1. **Method Documentation** (for each discovery method used):

   - **Method_Name**: MDM Export, AD Query, Network Scan, DHCP Lease, User Survey, etc.
   - **Technology**: Intune, Jamf, SCCM, Nmap, Active Directory, etc.
   - **Coverage_Type**: Managed Devices, Domain-Joined, All Networked, DHCP Clients, Self-Reported
   - **Endpoints_Discovered**: Count of endpoints discovered by this method
   - **Discovery_Frequency**: Daily, Weekly, Monthly, One-Time
   - **Automation_Status**: Fully Automated, Partially Automated, Manual
   - **Data_Quality**: High, Medium, Low (accuracy of discovered data)
   - **Limitations**: What this method CANNOT discover (e.g., "Network scan cannot discover offline devices")

2. **Coverage Analysis**

   - Calculate coverage rate per method: (Endpoints discovered / Total expected endpoints)
   - Identify gaps: What endpoints are missed by each method?
   - Document overlaps: How many endpoints discovered by multiple methods (good for validation)?

3. **Method Effectiveness Comparison**

   - Rank methods by coverage rate
   - Identify most reliable methods for your environment
   - Document recommended primary and secondary methods

**Example Methods:**

| Method | Coverage | Strengths | Limitations |
|--------|----------|-----------|-------------|
| MDM Export | Managed devices only | High accuracy, real-time data | Misses unmanaged devices |
| AD Query | Domain-joined only | Good coverage for Windows | Misses non-domain, mobile, BYOD |
| Network Scan | All networked devices | Comprehensive coverage | Can't identify users/ownership |
| DHCP Lease | DHCP clients | Quick discovery | Temporary IPs, no static devices |
| User Survey | BYOD, unmanaged | Captures self-reported devices | Low response rate, accuracy issues |

**Quality Target:** ≥3 discovery methods used, coverage gap <5%

### Sheet 4: Quality_Metrics

**Purpose:** Track inventory quality metrics over time

**Completion Steps:**

1. **Coverage Metrics**

   - **Total_Expected_Endpoints**: Estimated total endpoints (from asset database, user count estimates)
   - **Total_Discovered_Endpoints**: Count from Inventory sheet
   - **Coverage_Rate**: (Discovered / Expected) × 100%
   - **Coverage_Status**: Green (≥95%), Yellow (80-94%), Red (<80%)

2. **Accuracy Metrics**

   - **Spot_Check_Sample_Size**: Number of endpoints manually verified (recommend 20)
   - **Spot_Check_Accuracy**: Percentage of sample verified as accurate
   - **Accuracy_Status**: Green (≥95%), Yellow (80-94%), Red (<80%)

3. **Currency Metrics**

   - **Last_Inventory_Update**: Date of last inventory synchronization
   - **Stale_Endpoints_Count**: Endpoints not seen >30 days
   - **Stale_Endpoints_Percentage**: (Stale / Total) × 100%
   - **Currency_Status**: Green (<5% stale), Yellow (5-10% stale), Red (>10% stale)

4. **Duplicate Metrics**

   - **Duplicate_Records_Found**: Count of duplicate records identified
   - **Duplicate_Records_Merged**: Count of duplicates resolved
   - **Remaining_Duplicates**: Unresolved duplicates
   - **Duplication_Rate**: (Duplicates / Total) × 100%
   - **Duplication_Status**: Green (<5%), Yellow (5-10%), Red (>10%)

5. **Trend Tracking** (Monthly)

   - Track coverage rate month-over-month
   - Track accuracy month-over-month
   - Identify improving or degrading trends

**Quality Targets:**

- Coverage Rate: ≥95%
- Accuracy: ≥95%
- Stale Endpoints: <5%
- Duplication Rate: <5%

### Sheet 5: Evidence

**Purpose:** Document supporting evidence for inventory accuracy

**Completion Steps:**

1. **Evidence Collection** (for each discovery method):

   - **Evidence_Type**: MDM Export, AD Query Log, Network Scan Results, DHCP Lease Report, Survey Responses
   - **Evidence_Date**: Date evidence collected
   - **Evidence_File**: File name/path of evidence artifact
   - **Evidence_Description**: Brief description of evidence content
   - **Endpoints_Supported**: Count of endpoints validated by this evidence

2. **Evidence Storage**

   - Store evidence files in centralized location (SharePoint, network share)
   - Use consistent naming convention: `Evidence_<Type>_<Date>.ext`
   - Example: `Evidence_Intune_Export_2026-01-25.csv`

3. **Audit Trail**

   - Document who collected evidence (Evidence_Collector column)
   - Document approval/review (Reviewed_By, Reviewed_Date)
   - Maintain 12-month retention of evidence files

**Evidence Examples:**

- Intune device export CSV
- Active Directory computer query PowerShell log
- Nmap network scan output XML
- DHCP lease database export
- User survey response spreadsheet
- Asset database reconciliation report

**Quality Target:** ≥1 evidence artifact per discovery method, 12-month retention

### Sheet 6: Gaps

**Purpose:** Identify undiscovered endpoints and remediation plans

**Completion Steps:**

1. **Gap Identification**

   - **Gap_Description**: Description of gap (e.g., "BYOD devices not discovered", "Air-gapped lab devices missing")
   - **Gap_Type**: Discovery Method Gap, Coverage Gap, Classification Gap, Data Quality Gap
   - **Affected_Endpoints**: Estimate of how many endpoints affected
   - **Impact**: Critical, High, Medium, Low (based on affected endpoint criticality)
   - **Root_Cause**: Why this gap exists (e.g., "No BYOD discovery method implemented")

---

### Sheet 7: Baseline_Compliance (NEW)

**Purpose:** Document security baseline compliance status per endpoint (supports A.8.1 configuration requirements)

**Completion Steps:**

1. **For Each Endpoint Type** (Windows, macOS, Linux):
   - Baseline standard applied
   - Compliance status (compliant/non-compliant)
   - Configuration drift percentage
   - Last verification date

2. **Coverage Metrics:**
   - Endpoints on baseline by type
   - Compliance rate by OS
   - Non-compliant endpoint remediation plans

---

### Sheet 8: Encryption_Status (NEW)

**Purpose:** Verify full disk encryption (FDE) or file-level encryption per endpoint

**Completion Steps:**

1. **For Each Endpoint:**
   - Encryption type (FDE/File-Level/Container/None)
   - Encryption status (enabled/disabled/unknown)
   - Key escrow (keys secured/not secured)
   - Last verification date

2. **Coverage Analysis:**
   - FDE coverage % by ownership (corporate/BYOD)
   - Key escrow compliance
   - Unencrypted critical endpoints (gap)

---

### Sheet 9: Management_Enrollment (NEW)

**Purpose:** Track MDM/agent enrollment status and management coverage per endpoint

**Completion Steps:**

1. **For Each Endpoint:**
   - Management platform (Intune/Jamf/SCCM/etc or Unmanaged)
   - Enrollment status (enrolled/not enrolled)
   - Agent version and health status
   - Last check-in date

2. **Coverage Metrics:**
   - Management coverage % by OS type
   - Corporate vs. BYOD enrollment rates
   - Unmanaged critical endpoint identification

2. **Remediation Planning**

   - **Remediation_Plan**: Specific actions to close gap (e.g., "Implement user self-service BYOD enrollment")
   - **Remediation_Owner**: Person/team responsible for remediation
   - **Target_Date**: Target completion date for remediation
   - **Remediation_Status**: Not Started, In Progress, Completed, Deferred

3. **Gap Prioritization**

   - Prioritize gaps by Impact (Critical > High > Medium > Low)
   - Focus on gaps affecting critical endpoints first
   - Document risk acceptance for deferred gaps (with CISO approval)

**Common Gaps:**

- BYOD devices not discovered (no self-enrollment process)
- Air-gapped devices not inventoried (no manual discovery process)
- Contractor devices missing (no contractor onboarding/offboarding tracking)
- Guest devices not tracked (guest network monitoring not implemented)
- Stale endpoints not investigated (devices not seen >30 days, no follow-up)

**Quality Target:** All gaps documented, remediation plans for Critical/High gaps within 30 days

---

## Evidence Collection

### Required Evidence Types

For audit purposes, maintain the following evidence:

#### 1. Discovery Method Evidence

- **MDM Platform Exports**: Device inventory CSV/Excel exports from Intune, Jamf, SCCM
- **Active Directory Queries**: PowerShell query logs showing AD computer objects retrieved
- **Network Scan Results**: Nmap XML output, Lansweeper reports, network scan logs
- **DHCP Lease Exports**: DHCP lease database dumps
- **Cloud Platform Exports**: Azure VM lists, AWS EC2 instance lists, GCP Compute Engine lists

#### 2. Classification Evidence

- **Asset Database Reports**: Hardware asset records showing corporate ownership
- **MDM Enrollment Logs**: MAM/MDM enrollment showing BYOD vs. corporate classification
- **User Survey Responses**: Self-reported BYOD device submissions
- **Contractor Agreements**: Documentation of contractor-owned devices

#### 3. Validation Evidence

- **Spot-Check Results**: Random sample validation (20 endpoints) showing inventory accuracy
- **Coverage Calculations**: Coverage rate calculations (discovered / expected)
- **Reconciliation Reports**: Monthly reconciliation of automated discovery vs. manual records

#### 4. Approval Evidence

- **Approval Workflow**: Documented approvals (Data Owner, IT Security Manager, CISO)
- **Exception Approvals**: CISO-approved exceptions for undiscovered endpoints (air-gapped, etc.)

### Evidence Retention

- **Retention Period**: 12 months minimum
- **Storage Location**: Centralized repository (SharePoint, network share, document management system)
- **Access Controls**: Restrict access to authorized personnel (endpoint administrators, auditors)

---

## Common Pitfalls (10 Mistakes to Avoid)

### Single Discovery Method Only

**Mistake:** Relying on only MDM export or only network scanning  
**Why It's Wrong:** No single method achieves 100% coverage - managed devices miss BYOD, network scans miss offline devices  
**Solution:** Use minimum 3 discovery methods (MDM + AD + Network Scan recommended)

### Ignoring BYOD Devices

**Mistake:** Not implementing BYOD discovery method  
**Why It's Wrong:** BYOD devices access corporate data but remain undiscovered, cannot verify malware protection or software controls  
**Solution:** Implement user self-service BYOD enrollment, conduct user surveys

### No Deduplication Process

**Mistake:** Importing discovery data without deduplication  
**Why It's Wrong:** Same endpoint discovered multiple times (MDM + AD + Network Scan), inflates counts, creates data quality issues  
**Solution:** Implement deduplication by Device_ID, merge duplicate records, track merge history

### Stale Endpoints Not Flagged

**Mistake:** Not tracking Last_Seen date, no process to investigate stale endpoints  
**Why It's Wrong:** Inventory contains lost/stolen devices, disposed devices, inactive devices (inflates counts, reduces accuracy)  
**Solution:** Flag endpoints not seen >30 days, investigate monthly, remove disposed/lost devices

### No Classification Rules

**Mistake:** Subjective/inconsistent endpoint classification  
**Why It's Wrong:** Same device type classified differently by different administrators, criticality not based on data accessed  
**Solution:** Document classification rules, apply consistently, use decision trees

### Forgetting Air-Gapped Devices

**Mistake:** Assuming all endpoints are network-connected  
**Why It's Wrong:** Air-gapped lab devices, isolated security environments, OT devices exist but undiscovered  
**Solution:** Manual discovery process for air-gapped devices, physical inventory walks

### Privacy Violations in BYOD Discovery

**Mistake:** Deep-scanning BYOD devices, collecting personal data without consent  
**Why It's Wrong:** Violates GDPR/FADP privacy requirements, creates legal liability  
**Solution:** BYOD discovery limited to corporate container only, user consent required, privacy notice provided

### No Ongoing Maintenance

**Mistake:** One-time discovery, no weekly/monthly updates  
**Why It's Wrong:** Inventory becomes stale (new devices added, old devices removed), coverage degrades over time  
**Solution:** Weekly automated synchronization, monthly reconciliation, quarterly review

### Coverage Calculation Errors

**Mistake:** Calculating coverage as (Discovered / All Devices in MDM) instead of (Discovered / Expected Total)  
**Why It's Wrong:** Misses unmanaged devices entirely, falsely high coverage rate  
**Solution:** Estimate expected total endpoints (asset database + user count + BYOD estimates), calculate coverage against expected total

### No Approval Workflow

**Mistake:** Endpoint inventory not reviewed or approved by stakeholders  
**Why It's Wrong:** Data quality issues not caught, classification errors not corrected, no stakeholder buy-in  
**Solution:** Three-level approval workflow (Data Owner → IT Security Manager → CISO)

---

## Quality Checklist (50+ Items)

### Data Completeness (10 Items)

- [ ] 1. Every endpoint has unique Device_ID populated
- [ ] 2. Every endpoint has Hostname populated
- [ ] 3. Every endpoint has Device_Type populated
- [ ] 4. Every endpoint has Operating_System populated
- [ ] 5. Every endpoint has Owner populated
- [ ] 6. Every endpoint has Ownership_Model populated
- [ ] 7. Every endpoint has Location populated
- [ ] 8. Every endpoint has Criticality populated
- [ ] 9. Every endpoint has Last_Seen date populated
- [ ] 10. Every endpoint has Discovery_Method populated

### Data Quality (10 Items)

- [ ] 11. Device_IDs are truly unique (no duplicates)
- [ ] 12. Hostname format is consistent (standardized naming)
- [ ] 13. Operating_System format is consistent (e.g., "Windows 11 23H2")
- [ ] 14. Last_Seen dates are reasonable (within last 90 days for active devices)
- [ ] 15. IP addresses are valid format (IPv4 or IPv6)
- [ ] 16. MAC addresses are valid format (if collected)
- [ ] 17. Owner names match user directory (AD, Entra ID)
- [ ] 18. Location values are from approved list (not freeform text)
- [ ] 19. Criticality values are from approved list (Critical, High, Medium, Low only)
- [ ] 20. Duplicate records identified and merged

### Coverage (10 Items)

- [ ] 21. Coverage rate calculated: (Discovered / Expected) × 100%
- [ ] 22. Coverage rate ≥95% achieved (or gap documented with remediation plan)
- [ ] 23. Corporate-owned laptops: 100% discovered
- [ ] 24. Corporate-owned desktops: 100% discovered
- [ ] 25. Corporate-owned mobile devices: ≥95% discovered
- [ ] 26. BYOD devices: ≥80% discovered (or BYOD not implemented)
- [ ] 27. Contractor devices: ≥90% discovered (or contractor count documented)
- [ ] 28. Guest devices: Tracked (or guest access not provided)
- [ ] 29. Air-gapped devices: Manually inventoried (or none exist)
- [ ] 30. Lab/test devices: Documented (or none exist)

### Classification (10 Items)

- [ ] 31. 100% of endpoints classified by Device_Type
- [ ] 32. 100% of endpoints classified by Ownership_Model
- [ ] 33. 100% of endpoints classified by Criticality
- [ ] 34. Classification rules documented
- [ ] 35. Classification rules applied consistently
- [ ] 36. Critical endpoints identified (executives, finance, HR, legal)
- [ ] 37. BYOD devices identified (if BYOD program exists)
- [ ] 38. Contractor devices identified (if contractors have device access)
- [ ] 39. Guest devices identified (if guest network exists)
- [ ] 40. Lab/test devices identified (if lab environments exist)

### Discovery Methods (10 Items)

- [ ] 41. ≥3 discovery methods used
- [ ] 42. MDM/UEM export performed (Intune, Jamf, SCCM, etc.)
- [ ] 43. Active Directory query performed (if domain-joined endpoints exist)
- [ ] 44. Network scan performed (Nmap, Lansweeper, etc.)
- [ ] 45. DHCP lease analysis performed
- [ ] 46. Discovery methods documented in Discovery_Methods sheet
- [ ] 47. Discovery method coverage calculated per method
- [ ] 48. Discovery method limitations documented
- [ ] 49. Primary and secondary discovery methods identified
- [ ] 50. Automated discovery synchronization scheduled (weekly minimum)

### Evidence & Approval (10 Items)

- [ ] 51. Evidence artifacts collected for each discovery method
- [ ] 52. Evidence files stored in centralized location
- [ ] 53. Evidence retention policy implemented (12 months minimum)
- [ ] 54. Spot-check validation performed (20 endpoint sample)
- [ ] 55. Spot-check accuracy ≥95% achieved
- [ ] 56. Data Owner reviewed and approved inventory
- [ ] 57. IT Security Manager reviewed and approved inventory
- [ ] 58. CISO reviewed and approved inventory (or delegated approver)
- [ ] 59. Approval dates documented in workbook
- [ ] 60. Gaps documented with remediation plans for Critical/High gaps

---

## Review & Approval

### Three-Level Approval Workflow

#### Level 1: Data Owner Review

**Reviewer:** Endpoint Administrator, Asset Manager  
**Focus:** Data completeness and accuracy

**Review Checklist:**

- [ ] All mandatory attributes populated
- [ ] Data quality validation passed
- [ ] Duplicate records merged
- [ ] Stale endpoints flagged
- [ ] Classification rules applied consistently

**Approval Criteria:**

- Coverage rate ≥90% (or gaps documented)
- Accuracy ≥90% (spot-check validation)
- Duplication rate <10%

**Action:** Sign and date in workbook approval section

#### Level 2: IT Security Manager Review

**Reviewer:** IT Security Manager, Information Security Officer  
**Focus:** Classification accuracy, criticality determination, security implications

**Review Checklist:**

- [ ] Critical endpoints correctly identified
- [ ] Criticality classification appropriate (based on data accessed)
- [ ] BYOD devices identified and classified
- [ ] Security gaps identified and documented
- [ ] Remediation plans reasonable

**Approval Criteria:**

- 100% endpoints classified
- Critical endpoints identified correctly
- Security gaps have remediation plans

**Action:** Sign and date in workbook approval section

#### Level 3: CISO Review

**Reviewer:** Chief Information Security Officer (or delegated authority)  
**Focus:** Risk acceptance, exception approval, strategic gaps

**Review Checklist:**

- [ ] Coverage rate acceptable (≥95% or exceptions approved)
- [ ] Critical/High gaps have remediation plans
- [ ] Risk accepted for deferred gaps
- [ ] Inventory supports endpoint security controls (A.8.1, A.8.7, A.8.18, A.8.19)

**Approval Criteria:**

- Coverage rate ≥95% (or risk accepted)
- All Critical gaps have remediation plans with target dates <30 days
- Inventory quality supports audit readiness

**Action:** Sign and date in workbook approval section

### Post-Approval Actions

1. **Archive Approved Version:** Save approved workbook with date stamp (`Endpoint_Inventory_2026-01-25_Approved.xlsx`)
2. **Communicate Results:** Share inventory summary with stakeholders
3. **Schedule Updates:** Establish weekly automated synchronization
4. **Track Remediation:** Monitor gap remediation progress monthly
5. **Plan Next Review:** Schedule quarterly inventory review

---


**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
