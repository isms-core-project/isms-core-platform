**ISMS-IMP-A.5.9.2-UG - Inventory Maintenance**
**User Completion Guide**
### ISO/IEC 27001:2022 Control A.5.9: Inventory of Information and Other Associated Assets

---

**Document Control**

| Attribute | Value |
|-----------|-------|
| **Document ID** | ISMS-IMP-A.5.9.2-UG |
| **Version** | 1.0 |
| **Assessment Area** | Inventory Structure & Maintenance Procedures |
| **Related Policy** | ISMS-POL-A.5.9, Section 2.2 (Asset Categorization), Section 2.3 (Mandatory Inventory Attributes), Section 2.5 (Inventory Quality Standards), Section 2.6 (Integration Requirements) |
| **Purpose** | Document inventory structure, update procedures, integration mechanisms, and maintenance workflows |
| **Target Audience** | Security Team, IT Operations, System Owners, Information Owners, CMDB Administrators, Integration Engineers |
| **Assessment Type** | Operational & Technical |
| **Review Cycle** | Quarterly or After Inventory Structure Changes |
| **Date** | [Date] |

### Version History

| Version | Date | Changes | Author |
|---------|------|--------|--------|
| 1.0 | [Date] | Initial assessment specification following consolidated policy structure | ISMS Implementation Team |

### Document Structure

This is the **User Completion Guide**. The companion Technical Specification is documented in ISMS-IMP-A.5.9.2-TG.

---

**Audience:** Security Team, IT Operations, System Owners, CMDB Administrators

---

## Assessment Overview

### What This Assessment Evaluates

This assessment documents HOW [Organization] structures and maintains its asset inventory. This is the "HOW is it organized and kept current?" assessment that answers:

- **Inventory Structure**: What systems hold inventory data? How is it organized?
- **Update Procedures**: How are changes captured? What triggers updates?
- **Integration**: How does inventory integrate with CMDB, HR, procurement?
- **Maintenance Workflows**: Who updates what? When? How?
- **Data Quality**: How is accuracy and currency maintained?

**Key Principle**: Discovery finds assets (IMP-A.5.9-1). Maintenance keeps the inventory accurate and current over time. Without maintenance, inventory degrades rapidly.

### Why This Matters

This assessment verifies [Organization]'s compliance with:

- **ISO/IEC 27001:2022 Control A.5.9**: "...inventory...should be created and **maintained**"
- **ISMS-POL-A.5.9, Requirement A.5.9-R2**: Asset categorization requirements
- **ISMS-POL-A.5.9, Requirement A.5.9-R3**: Mandatory inventory attributes
- **ISMS-POL-A.5.9, Section 2.5**: Currency standards (maximum staleness by asset type)
- **ISMS-POL-A.5.9, Requirement A.5.9-R6**: Integration with other ISMS processes

**From Implementer Perspective**: Provides systematic procedures to keep inventory current without excessive manual effort.

**From Auditor Perspective**: Demonstrates [Organization] has sustainable processes to maintain inventory accuracy over time.

### Assessment Domains

This assessment covers **4 maintenance domains**:

| Domain | Focus | What You'll Document |
|--------|-------|---------------------|
| **1. Inventory Structure** | Systems, schemas, organization | Where inventory lives, how it's structured, access controls |
| **2. Update Procedures** | Triggers, workflows, timing | What triggers updates, who performs them, SLAs |
| **3. Integration Mechanisms** | CMDB, HR, procurement sync | Automated feeds, API integration, reconciliation |
| **4. Data Quality Maintenance** | Validation, reviews, cleansing | How quality is maintained, error correction, periodic reviews |

### Assessment Outputs

**Generated Workbook**: `ISMS_A_5_9_Inventory_Maintenance_Assessment_YYYYMMDD.xlsx`

**Sheets** (7 total):
1. **Instructions**: How to complete this assessment
2. **Inventory Structure**: Systems, schemas, organization, access
3. **Update Triggers & Workflows**: What triggers updates, procedures, SLAs
4. **Integration Architecture**: CMDB, HR, procurement integration
5. **Data Quality Controls**: Validation rules, review processes, error handling
6. **Maintenance Metrics**: Update timeliness, integration health, data quality KPIs
7. **Evidence Register**: Documentation of procedures, integration configs, review records

**Compliance Metrics Generated**:

- Update timeliness (% within SLA)
- Integration health (sync success rate)
- Data quality score (accuracy, completeness, currency)
- Review compliance (% reviews on schedule)

---

## Prerequisites

### What You Need Before Starting

**1. Access to Inventory Systems**:

- Asset inventory system(s) (CMDB, spreadsheets, database)
- CMDB if deployed (ServiceNow, BMC, Device42, etc.)
- HR system (for personnel asset integration)
- Procurement/finance system (for asset acquisition tracking)
- Document management system (for information assets)

**2. Personnel**:

- **Security Team**: Leads assessment, consolidates findings
- **IT Operations**: Provides CMDB/inventory system details
- **CMDB Administrator**: Documents structure, integration, workflows
- **System Owners**: Document application inventory maintenance
- **Integration Engineers**: Document API connections, data flows
- **HR Representative**: Explain HR system integration (if applicable)

**3. Documentation**:

- Inventory system architecture diagrams
- Data flow diagrams (inventory ↔ other systems)
- Integration configuration documentation
- Update procedure documents (if formalized)
- Previous assessment (if exists - for comparison)

**4. System Access**:

- Read access to inventory system(s)
- Access to integration logs/dashboards
- Access to CMDB configuration settings
- API documentation for integrations

**5. Time Allocation**:

- **Initial Assessment**: 15-25 hours (varies by inventory complexity)
- **Quarterly Updates**: 4-6 hours (once procedures documented)
- **Evidence Collection**: 3-5 hours per quarter

---

## Assessment Workflow

### Step-by-Step Process

```
Phase 1: Inventory Structure Documentation (Day 1-3)
├─ Identify all systems holding inventory data
├─ Document schema/structure for each system
├─ Map data fields to policy requirements
└─ Document access controls and permissions

Phase 2: Update Procedure Documentation (Day 4-6)
├─ Identify all update triggers (manual and automated)
├─ Document workflows for each trigger type
├─ Define SLAs for update timeliness
└─ Map responsibilities (who updates what)

Phase 3: Integration Architecture (Day 7-10)
├─ Document CMDB integration (if exists)
├─ Document HR system integration (if exists)
├─ Document procurement integration (if exists)
├─ Map data flows and reconciliation procedures
└─ Document API configurations and schedules

Phase 4: Data Quality Controls (Day 11-13)
├─ Document validation rules in inventory system
├─ Document review procedures (owner reviews, periodic audits)
├─ Document error correction workflows
└─ Document data quality monitoring

Phase 5: Metrics & Evidence (Day 14-15)
├─ Collect update timeliness metrics
├─ Collect integration health metrics
├─ Collect data quality metrics
├─ Compile evidence register
└─ Review and approval

Phase 6: Review & Approval (Day 16)
├─ Quality check against checklist
├─ Security Team review
├─ CISO approval
└─ Submit to compliance dashboard
```

**Timeline**: 16 working days for initial assessment, 4-6 days for quarterly updates

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

### Sheet 2: Inventory Structure

**Purpose**: Document where inventory data is stored and how it's organized.

**What This Sheet Captures**:

- Systems holding inventory data (CMDB, spreadsheets, databases)
- Schema/structure for each system (tables, fields, relationships)
- Mapping to policy mandatory attributes (Section 2.3)
- Access controls and permissions
- Version control and backup procedures

**Column Definitions**:

| Column | Purpose | How to Complete |
|--------|---------|-----------------|
| **Inventory System** | Name of system holding inventory | Free text: System name (e.g., "ServiceNow CMDB", "Asset Tracking Spreadsheet") |
| **System Type** | Category of system | Dropdown: CMDB / Database / Spreadsheet / Document Repository / Custom Application / SaaS Platform |
| **Asset Categories Stored** | Which asset types in this system | Free text: List categories (e.g., "IT Infrastructure, Applications") |
| **Primary/Secondary** | Is this the authoritative source? | Dropdown: Primary (authoritative) / Secondary (copy/cache) / Reference Only |
| **Data Structure** | How data is organized | Free text: Description (e.g., "SQL tables: ci_server, ci_storage, ci_network") |
| **Mandatory Attributes Coverage** | Which policy attributes included | Free text: List attributes from Policy Section 2.3 |
| **Missing Attributes** | Which policy attributes NOT included | Free text: List gaps |
| **Access Controls** | Who can view/edit | Free text: Role-based access description |
| **Update Mechanism** | How data enters this system | Dropdown: Manual Entry / API Integration / File Import / Discovery Scan / Multiple Methods |
| **Version Control** | How changes are tracked | Dropdown: Full Audit Log / Change Tracking / Timestamps Only / None |
| **Backup Frequency** | How often backed up | Dropdown: Real-time / Daily / Weekly / Monthly / None |
| **Backup Location** | Where backups stored | Free text: System/location |
| **Schema Documentation** | Is structure documented? | Dropdown: Yes - Comprehensive / Yes - Basic / No |
| **Documentation Location** | Where to find schema docs | Free text: URL, file path, or "N/A" |
| **Responsible Party** | Who manages this system | Free text: Role or team |
| **Notes** | Additional context | Free text |

**How to Complete**:

1. **Identify All Inventory Systems**:

   - Start with primary system (likely CMDB if you have one)
   - Include ALL systems with inventory data (even spreadsheets!)
   - Don't forget: Document repos, procurement systems, specialized tools

2. **Example 1: ServiceNow CMDB**:

   - **Inventory System**: "ServiceNow CMDB"
   - **System Type**: CMDB
   - **Asset Categories Stored**: "IT Infrastructure (servers, storage, networking, endpoints), Applications"
   - **Primary/Secondary**: Primary (authoritative)
   - **Data Structure**: "Configuration Item (CI) tables: cmdb_ci_server, cmdb_ci_storage, cmdb_ci_network_adapter, cmdb_ci_appl, etc. Relationships via cmdb_rel_ci table"
   - **Mandatory Attributes Coverage**: "Asset ID (sys_id), Name, Type (class), Owner (assigned_to), Location, Status (install_status), Criticality (business_criticality), Created Date, Last Updated"
   - **Missing Attributes**: "Data Classification (not in CMDB), Retention Period (not tracked)"
   - **Access Controls**: "Role-based: itil role for read, asset role for edit, admin for delete"
   - **Update Mechanism**: Multiple Methods (Discovery scans, API integrations, manual entry)
   - **Version Control**: Full Audit Log (sys_audit table)
   - **Backup Frequency**: Daily
   - **Backup Location**: "ServiceNow instance backups, AWS S3"
   - **Schema Documentation**: Yes - Comprehensive
   - **Documentation Location**: "ServiceNow docs.servicenow.com/cmdb, internal wiki: confluence.company.com/cmdb"
   - **Responsible Party**: "CMDB Administrator, IT Operations Team"

3. **Example 2: Asset Tracking Spreadsheet (if CMDB doesn't exist)**:

   - **Inventory System**: "Asset_Inventory_Master.xlsx"
   - **System Type**: Spreadsheet
   - **Asset Categories Stored**: "All categories (Information, IT, Applications, Physical, Personnel)"
   - **Primary/Secondary**: Primary (authoritative - no CMDB)
   - **Data Structure**: "Excel workbook with 5 sheets: Info_Assets, IT_Assets, Applications, Physical_Assets, Personnel_Assets. Columns match policy Section 2.3 attributes"
   - **Mandatory Attributes Coverage**: "All policy attributes included as columns"
   - **Missing Attributes**: "None (spreadsheet designed per policy)"
   - **Access Controls**: "SharePoint permissions: Security Team (edit), IT Ops (view), Management (view)"
   - **Update Mechanism**: Manual Entry
   - **Version Control**: Timestamps Only (Excel modified date, SharePoint version history)
   - **Backup Frequency**: Daily (SharePoint auto-backup)
   - **Backup Location**: "SharePoint Online, OneDrive for Business"
   - **Schema Documentation**: Yes - Basic (column headers documented in Instructions sheet)
   - **Documentation Location**: "SharePoint: /sites/InfoSec/Asset_Inventory/README.md"
   - **Responsible Party**: "Information Security Manager"

4. **Example 3: HR System (Personnel Assets)**:

   - **Inventory System**: "Workday HRIS"
   - **System Type**: SaaS Platform
   - **Asset Categories Stored**: "Personnel Assets (roles, competencies)"
   - **Primary/Secondary**: Primary for HR data, Reference Only for asset inventory (privacy - we don't copy person data)
   - **Data Structure**: "Workday data model: Worker, Position, Job Profile, Competency. Accessed via API for competency reporting"
   - **Mandatory Attributes Coverage**: "Role/Competency, Category (job family), Current Capacity (headcount), Succession Plan status"
   - **Missing Attributes**: "Business Criticality (HR doesn't track this), Last Review Date (not in HR system)"
   - **Access Controls**: "HR team only, API access for read-only competency reports"
   - **Update Mechanism**: API Integration (read-only, no write-back)
   - **Version Control**: Full Audit Log (Workday native)
   - **Backup Frequency**: Real-time (SaaS provider)
   - **Schema Documentation**: Yes - Comprehensive (Workday docs)
   - **Documentation Location**: "doc.workday.com, internal: /integrations/workday-api"
   - **Responsible Party**: "HR Systems Team, integration managed by IT"

**Common Pitfalls**:

- ❌ Only documenting the "official" inventory system (missing shadow spreadsheets)
- ✅ Document ALL systems with inventory data, even informal ones
- ❌ Assuming CMDB has all required attributes (often missing: classification, retention period)
- ✅ Map CMDB fields to policy attributes, identify gaps
- ❌ Not documenting access controls (auditors will ask!)
- ✅ Clearly describe who can view/edit inventory

**Completeness Check**: Every system holding inventory data should have a row in this sheet.

---

### Sheet 3: Update Triggers & Workflows

**Purpose**: Document what triggers inventory updates and how updates are performed.

**What This Sheet Captures**:

- Update triggers (events causing inventory changes)
- Workflows for each trigger type
- Responsible parties for each update type
- SLAs for update timeliness
- Manual vs. automated update procedures

**Column Definitions**:

| Column | Purpose | How to Complete |
|--------|---------|-----------------|
| **Update Trigger** | Event causing inventory update | Free text: Describe event (e.g., "New server deployed", "Employee termination") |
| **Trigger Category** | Type of trigger | Dropdown: Asset Acquisition / Asset Modification / Asset Disposal / Ownership Change / Location Change / Configuration Change / Status Change / Scheduled Review / Discovery Finding |
| **Asset Categories Affected** | Which asset types | Free text: List (e.g., "IT Infrastructure - Servers") |
| **Trigger Source** | What initiates the trigger | Dropdown: Change Management / Service Request / Procurement / HR System / Discovery Scan / Owner Request / Scheduled Process / Manual Detection |
| **Update Method** | How update is performed | Dropdown: Automated (API/Integration) / Semi-Automated (Form/Workflow) / Manual Entry / Discovery Scan Update |
| **Responsible Party** | Who performs update | Free text: Role/team |
| **Update Workflow** | Step-by-step procedure | Free text: Brief workflow description |
| **SLA - Update Timeframe** | Maximum time to update inventory | Dropdown: Real-time / Same Day / Within 1 Day / Within 3 Days / Within 1 Week / Within 1 Month |
| **SLA Achievement %** | Actual compliance with SLA | Numeric (0-100): Percentage |
| **Verification Method** | How update is verified | Free text: How you confirm update happened correctly |
| **Failure Handling** | What if update fails | Free text: Error handling procedure |
| **Evidence Location** | Where to find update records | Free text: System, log file, ticket system |
| **Integration Dependencies** | Required integrations | Free text: List dependent systems/APIs |
| **Last Review Date** | When workflow last reviewed | Date field |
| **Notes** | Additional context | Free text |

**How to Complete**:

1. **Asset Acquisition Triggers**:

**Example: New Server Deployed**

- **Update Trigger**: "New physical or virtual server deployed to production"
- **Trigger Category**: Asset Acquisition
- **Asset Categories Affected**: "IT Infrastructure - Servers"
- **Trigger Source**: Change Management (RFC approval)
- **Update Method**: Automated (API/Integration)
- **Responsible Party**: "IT Operations, triggered by CMDB discovery"
- **Update Workflow**: "1) RFC approved in Change Mgmt → 2) Server deployed → 3) Discovery scan detects new server → 4) Auto-creates CI in CMDB → 5) Alert to IT Ops for manual attribute completion (owner, criticality)"
- **SLA - Update Timeframe**: Within 1 Day
- **SLA Achievement %**: 94% (Q4 2025 data)
- **Verification Method**: "Weekly reconciliation report: deployed servers vs. CMDB CIs"
- **Failure Handling**: "If discovery doesn't detect within 24h, IT Ops manual entry, escalation to discovery tool team"
- **Evidence Location**: "ServiceNow Change Request tickets, CMDB audit log, Discovery scan logs"
- **Integration Dependencies**: "ServiceNow Discovery, Change Management module"
- **Last Review Date**: [Date]

**Example: New SaaS Application Procured**

- **Update Trigger**: "New SaaS application purchased/subscribed"
- **Trigger Category**: Asset Acquisition
- **Asset Categories Affected**: "Applications - SaaS Service"
- **Trigger Source**: Procurement (purchase order, expense report)
- **Update Method**: Semi-Automated (Form/Workflow)
- **Responsible Party**: "Application Owner (requestor)"
- **Update Workflow**: "1) SaaS procurement request → 2) Approval workflow → 3) Procurement creates PO → 4) Automated email to requestor: 'Please complete App Inventory Form' → 5) Requestor fills form (ServiceNow catalog item) → 6) Security Team reviews, adds to inventory → 7) Owner assigned"
- **SLA - Update Timeframe**: Within 1 Week
- **SLA Achievement %**: 78% (Q4 2025 - needs improvement)
- **Verification Method**: "Monthly reconciliation: Expense reports vs. Application inventory"
- **Failure Handling**: "If not added within 2 weeks, Security sends reminder, escalate to manager at 1 month"
- **Evidence Location**: "Procurement system tickets, ServiceNow catalog requests, Application inventory"
- **Integration Dependencies**: "Expense report system (Concur), ServiceNow Catalog"
- **Last Review Date**: [Date]

2. **Asset Modification Triggers**:

**Example: Server Configuration Change**

- **Update Trigger**: "Server configuration modified (OS patch, application install, settings change)"
- **Trigger Category**: Configuration Change
- **Asset Categories Affected**: "IT Infrastructure - Servers"
- **Trigger Source**: Change Management
- **Update Method**: Automated (API/Integration)
- **Responsible Party**: "Configuration Management process, automated via Discovery"
- **Update Workflow**: "1) RFC approved → 2) Change implemented → 3) Discovery scan (scheduled or triggered) → 4) CMDB auto-updated with new config data → 5) Alert if significant change (e.g., criticality threshold)"
- **SLA - Update Timeframe**: Within 1 Day (scheduled discovery runs daily)
- **SLA Achievement %**: 96%
- **Verification Method**: "Discovery scan reports, CMDB audit log"
- **Failure Handling**: "Manual entry if discovery fails, IT Ops notified"
- **Evidence Location**: "Change Management tickets, CMDB version history"
- **Integration Dependencies**: "ServiceNow Discovery, Change Management"

**Example: Asset Owner Change**

- **Update Trigger**: "Asset owner changes (employee role change, transfer, departure)"
- **Trigger Category**: Ownership Change
- **Asset Categories Affected**: "All categories (any owned asset)"
- **Trigger Source**: HR System (employee status change) OR Owner Request (transfer ownership)
- **Update Method**: Semi-Automated (Form/Workflow) + Manual
- **Responsible Party**: "Current Owner (initiates transfer) + New Owner (accepts) + Security Team (approves)"
- **Update Workflow**: "1) Owner change request submitted (ServiceNow form or HR trigger) → 2) Security Team validates new owner → 3) New owner accepts ownership (email acknowledgment) → 4) Inventory updated → 5) Notifications sent"
- **SLA - Update Timeframe**: Within 3 Days
- **SLA Achievement %**: 88%
- **Verification Method**: "Ownership transfer tracking log, acknowledgment emails"
- **Failure Handling**: "If new owner doesn't accept within 5 days, escalate to manager"
- **Evidence Location**: "ServiceNow ownership transfer requests, email confirmations"
- **Integration Dependencies**: "HR system (for employee status), Email"

3. **Asset Disposal Triggers**:

**Example: Server Decommissioned**

- **Update Trigger**: "Server decommissioned and removed from production"
- **Trigger Category**: Asset Disposal
- **Asset Categories Affected**: "IT Infrastructure - Servers"
- **Trigger Source**: Change Management
- **Update Method**: Semi-Automated (workflow updates status, manual verification)
- **Responsible Party**: "IT Operations"
- **Update Workflow**: "1) Decommission RFC approved → 2) Server shutdown and removed → 3) IT Ops updates CMDB status to 'Retired' → 4) After 30-day retention, Security approves permanent deletion → 5) CMDB CI marked 'Deleted' (soft delete, audit trail preserved)"
- **SLA - Update Timeframe**: Same Day (status change), 30 days (final deletion)
- **SLA Achievement %**: 92%
- **Verification Method**: "Discovery scan (should not detect decommissioned server), physical datacenter audit"
- **Failure Handling**: "If server still detected after decommission, investigate (zombie server?)"
- **Evidence Location**: "Change Management tickets, CMDB audit log, disposal records"
- **Integration Dependencies**: "Change Management, Physical asset disposal process"

4. **Scheduled Review Triggers**:

**Example: Annual Owner Review**

- **Update Trigger**: "Scheduled annual review by asset owner"
- **Trigger Category**: Scheduled Review
- **Asset Categories Affected**: "All categories"
- **Trigger Source**: Scheduled Process (automated email campaign)
- **Update Method**: Manual Entry (owner reviews and confirms/updates)
- **Responsible Party**: "Asset Owners (perform review) + Security Team (tracks completion)"
- **Update Workflow**: "1) Automated script generates 'Assets Owned by You' report → 2) Email sent to each owner: 'Please review your assets' → 3) Owner reviews inventory records, updates if needed → 4) Owner signs attestation form → 5) Security Team tracks completion, sends reminders"
- **SLA - Update Timeframe**: Within 1 Month (of scheduled date)
- **SLA Achievement %**: 73% (needs improvement - many owners miss deadline)
- **Verification Method**: "Attestation tracking spreadsheet, review completion dashboard"
- **Failure Handling**: "Reminder emails at 2 weeks, escalate to manager at 1 month overdue"
- **Evidence Location**: "Review schedule, attestation forms, email confirmations"
- **Integration Dependencies**: "Email, inventory reporting system"

**Common Pitfalls**:

- ❌ Only documenting "official" update procedures (missing ad-hoc manual updates)
- ✅ Document both formal and informal update methods
- ❌ Setting unrealistic SLAs (e.g., "real-time" for manual processes)
- ✅ SLAs should match actual capability and policy requirements
- ❌ Not measuring SLA achievement (no metrics = can't improve)
- ✅ Track actual update timeliness, calculate compliance percentage

**Completeness Check**: Every trigger type from Policy Section 2.5.3 should be documented.

---

### Sheet 4: Integration Architecture

**Purpose**: Document how inventory integrates with other systems (CMDB, HR, procurement).

**What This Sheet Captures**:

- System-to-system integrations
- Data flow direction (one-way, bi-directional)
- Integration method (API, file transfer, database sync)
- Synchronization frequency and schedule
- Reconciliation procedures
- Integration health monitoring

**Column Definitions**:

| Column | Purpose | How to Complete |
|--------|---------|-----------------|
| **Integration Name** | Descriptive name | Free text: Name of integration (e.g., "CMDB ↔ Procurement Sync") |
| **Source System** | System sending data | Free text: System name |
| **Target System** | System receiving data | Free text: System name |
| **Data Flow Direction** | One-way or bi-directional | Dropdown: Source → Target (one-way) / Source ↔ Target (bi-directional) / Target → Source (reverse one-way) |
| **Integration Method** | Technical approach | Dropdown: REST API / SOAP API / Database Sync / File Transfer (CSV/XML) / Message Queue / Webhook / Manual Export/Import |
| **Data Elements Transferred** | What data is synced | Free text: List fields/attributes |
| **Sync Frequency** | How often data syncs | Dropdown: Real-time / Every 15 minutes / Hourly / Daily / Weekly / Monthly / On-Demand |
| **Sync Schedule** | Specific timing | Free text: Time of day, day of week (e.g., "Daily at 2:00 AM UTC") |
| **Last Successful Sync** | When last ran successfully | Date/time field |
| **Sync Success Rate** | Percentage of successful syncs | Numeric (0-100): % |
| **Failure Handling** | What happens on error | Free text: Error handling procedure |
| **Reconciliation Procedure** | How to verify sync accuracy | Free text: How you check data matches |
| **Reconciliation Frequency** | How often reconciled | Dropdown: After Each Sync / Daily / Weekly / Monthly / Quarterly |
| **Health Monitoring** | How integration health tracked | Free text: Monitoring tool, dashboard, logs |
| **Responsible Party** | Who manages integration | Free text: Team/role |
| **Documentation Location** | Where to find integration docs | Free text: URL, wiki page, config file path |
| **Notes** | Additional context | Free text |

**How to Complete**:

1. **CMDB Integration** (if applicable):

**Example: ServiceNow Discovery → CMDB**

- **Integration Name**: "ServiceNow Discovery Auto-Population"
- **Source System**: "ServiceNow Discovery (Discovery & Service Mapping module)"
- **Target System**: "ServiceNow CMDB"
- **Data Flow Direction**: Source → Target (one-way, Discovery populates CMDB)
- **Integration Method**: REST API (native ServiceNow)
- **Data Elements Transferred**: "Server hostname, IP address, OS type/version, installed software, hardware specs (CPU, memory, disk), network interfaces, running services"
- **Sync Frequency**: Daily
- **Sync Schedule**: "Daily at 3:00 AM UTC (nightly discovery scans)"
- **Last Successful Sync**: [Current date/time from monitoring]
- **Sync Success Rate**: 98% (Q4 2025)
- **Failure Handling**: "Email alert to CMDB Admin, failed discoveries logged, retry next cycle"
- **Reconciliation Procedure**: "Weekly report: Compare discovery results vs. CMDB CI count, investigate discrepancies"
- **Reconciliation Frequency**: Weekly
- **Health Monitoring**: "ServiceNow Discovery dashboard, email alerts on failures"
- **Responsible Party**: "CMDB Administrator, IT Operations"
- **Documentation Location**: "ServiceNow instance: /discovery_configs, Internal wiki: /cmdb/discovery"

**Example: CMDB ↔ Change Management**

- **Integration Name**: "CMDB-Change Management Integration"
- **Source System**: "ServiceNow CMDB"
- **Target System**: "ServiceNow Change Management"
- **Data Flow Direction**: Source ↔ Target (bi-directional: Change updates CMDB, CMDB provides CI info to Change)
- **Integration Method**: REST API (native ServiceNow)
- **Data Elements Transferred**: "CI details to Change (for impact analysis), Status updates to CMDB (when CI changed via RFC)"
- **Sync Frequency**: Real-time
- **Sync Schedule**: "N/A (event-driven, triggers on Change or CMDB updates)"
- **Last Successful Sync**: [Current timestamp]
- **Sync Success Rate**: 99.5%
- **Failure Handling**: "Workflow stops, alert to Change/CMDB Admin, manual intervention required"
- **Reconciliation Procedure**: "Monthly audit: Verify RFCs have corresponding CMDB updates"
- **Reconciliation Frequency**: Monthly
- **Health Monitoring**: "ServiceNow integration health dashboard"
- **Responsible Party**: "CMDB Administrator, Change Management Team"

2. **HR System Integration** (for personnel assets):

**Example: Workday → Personnel Asset Inventory**

- **Integration Name**: "HR Competency Extract"
- **Source System**: "Workday HRIS"
- **Target System**: "Asset Inventory (Personnel Assets sheet)"
- **Data Flow Direction**: Source → Target (one-way, read-only from HR)
- **Integration Method**: REST API (Workday API, custom integration)
- **Data Elements Transferred**: "Job profiles (roles), competency counts (anonymized headcount), succession plan status, training completion"
- **Sync Frequency**: Weekly
- **Sync Schedule**: "Every Monday at 6:00 AM UTC"
- **Last Successful Sync**: [Date/time]
- **Sync Success Rate**: 96% (occasional API timeouts)
- **Failure Handling**: "Retry after 1 hour, email IT Integration team if 3 failures, manual export fallback"
- **Reconciliation Procedure**: "Monthly: Compare competency counts from API vs. manual HR report, verify accuracy"
- **Reconciliation Frequency**: Monthly
- **Health Monitoring**: "Integration middleware dashboard (MuleSoft/Workato), logs in /var/log/integrations/"
- **Responsible Party**: "IT Integration Team, HR Systems"
- **Documentation Location**: "Confluence: /integrations/workday-api, Code repo: github.com/org/workday-integration"
- **Notes**: "Privacy-compliant: Only aggregated competency data, no PII transferred"

3. **Procurement Integration** (for asset acquisition):

**Example: Procurement System → IT Asset Inventory**

- **Integration Name**: "Procurement Purchase Order Feed"
- **Source System**: "SAP Procurement"
- **Target System**: "CMDB / Asset Inventory"
- **Data Flow Direction**: Source → Target (one-way)
- **Integration Method**: File Transfer (CSV export from SAP, import to CMDB)
- **Data Elements Transferred**: "PO number, asset description, vendor, model, serial number (if available), purchase date, cost, assigned department"
- **Sync Frequency**: Daily
- **Sync Schedule**: "Daily at 8:00 AM UTC (after SAP overnight batch)"
- **Last Successful Sync**: [Date]
- **Sync Success Rate**: 89% (CSV format issues cause failures)
- **Failure Handling**: "Email alert to Procurement and IT Ops, manual review of failed records, fix and re-import"
- **Reconciliation Procedure**: "Monthly: Compare PO count vs. new CMDB CIs, ensure all procured assets inventoried"
- **Reconciliation Frequency**: Monthly
- **Health Monitoring**: "File transfer logs, CMDB import logs, dashboard in /monitoring/integrations"
- **Responsible Party**: "Procurement Team (export), IT Operations (import)"
- **Documentation Location**: "SAP export config: /sap/procurement/exports/, Import script: /scripts/import_po_to_cmdb.py"
- **Notes**: "Known issue: Serial numbers often missing in PO, requires manual follow-up"

4. **No Integration Example** (manual process):

**Example: Information Assets → Document Repository**

- **Integration Name**: "N/A - Manual Process"
- **Source System**: "SharePoint Document Libraries"
- **Target System**: "Asset Inventory (Information Assets sheet)"
- **Data Flow Direction**: Manual entry based on SharePoint
- **Integration Method**: Manual Export/Import
- **Data Elements Transferred**: "Document title, location (SharePoint site/library), owner, classification, retention period"
- **Sync Frequency**: Monthly
- **Sync Schedule**: "First Monday of each month"
- **Last Successful Sync**: [Date]
- **Sync Success Rate**: 100% (manual, always completes eventually)
- **Failure Handling**: "N/A (manual process, if delayed just takes longer)"
- **Reconciliation Procedure**: "Quarterly: IT runs SharePoint inventory report, compare vs. Asset Inventory, identify gaps"
- **Reconciliation Frequency**: Quarterly
- **Health Monitoring**: "Manual tracking (spreadsheet), no automated monitoring"
- **Responsible Party**: "Information Security Manager"
- **Documentation Location**: "Internal wiki: /procedures/sharepoint-inventory-update"
- **Notes**: "Target for automation in 2026 (SharePoint API integration planned)"

**Common Pitfalls**:

- ❌ Assuming integrations "just work" (no monitoring, no reconciliation)
- ✅ Document actual sync success rate, monitor health, reconcile regularly
- ❌ Not documenting manual processes (they're still integrations!)
- ✅ Even "manual export/import" is a data flow that should be documented
- ❌ Ignoring failed syncs (errors pile up over time)
- ✅ Track failures, document error handling, fix root causes

**Completeness Check**: Every system integration mentioned in Sheet 2 should have a row here.

---

### Sheet 5: Data Quality Controls

**Purpose**: Document how data quality is maintained in the inventory.

**What This Sheet Captures**:

- Data validation rules (prevent bad data entry)
- Review procedures (periodic checks for accuracy)
- Error detection and correction workflows
- Data quality metrics and monitoring
- Owner responsibilities for data quality

**Column Definitions**:

| Column | Purpose | How to Complete |
|--------|---------|-----------------|
| **Quality Control Type** | Category of control | Dropdown: Data Validation Rule / Mandatory Field / Format Check / Periodic Review / Automated Check / Owner Attestation / Reconciliation / Duplicate Detection |
| **Control Description** | What the control does | Free text: Describe control |
| **Applies To** | Which inventory systems/fields | Free text: System and field names |
| **Implementation** | How control is implemented | Dropdown: System Validation / Workflow Rule / Scheduled Script / Manual Process / Database Constraint |
| **Enforcement** | When control triggers | Dropdown: On Data Entry / On Save / On Submit / Scheduled (periodic) / On-Demand |
| **Error Handling** | What happens on violation | Free text: Error message, block save, alert, etc. |
| **Responsible Party** | Who manages this control | Free text: Role/team |
| **Effectiveness** | Is control working? | Dropdown: Effective / Partially Effective / Not Effective / Not Yet Measured |
| **Measurement Method** | How effectiveness measured | Free text: How you verify control works |
| **Last Assessed** | When control last checked | Date field |
| **Evidence Location** | Where to find proof | Free text: System logs, validation configs, reports |
| **Notes** | Additional context | Free text |

**How to Complete**:

1. **Data Validation Rules**:

**Example: Asset ID Uniqueness**

- **Quality Control Type**: Data Validation Rule
- **Control Description**: "Enforce unique Asset ID across entire inventory (prevent duplicates)"
- **Applies To**: "All inventory systems, Asset ID field"
- **Implementation**: Database Constraint (CMDB: sys_id primary key), Spreadsheet: Conditional formatting highlights duplicates
- **Enforcement**: On Save
- **Error Handling**: "CMDB: Save blocked with error 'Asset ID already exists'. Spreadsheet: Red highlight, manual fix required"
- **Responsible Party**: "CMDB Administrator (CMDB rules), Information Security Manager (spreadsheet)"
- **Effectiveness**: Effective
- **Measurement Method**: "Query inventory for duplicate Asset IDs (should return zero results)"
- **Last Assessed**: [Date]
- **Evidence Location**: "CMDB schema definition, Spreadsheet conditional formatting rules"

**Example: Owner Field Required**

- **Quality Control Type**: Mandatory Field
- **Control Description**: "Owner field cannot be empty (Policy Requirement A.5.9-R4: 100% owner assignment)"
- **Applies To**: "All inventory systems, Owner field"
- **Implementation**: System Validation (CMDB: required field), Spreadsheet: Data validation
- **Enforcement**: On Submit
- **Error Handling**: "Cannot submit without owner assigned, error message: 'Owner is required per ISMS-POL-A.5.9'"
- **Responsible Party**: "CMDB Administrator"
- **Effectiveness**: Effective
- **Measurement Method**: "Monthly report: Count records with NULL/empty Owner field (should be zero)"
- **Last Assessed**: [Date]
- **Evidence Location**: "CMDB field configuration, monthly data quality report"

**Example: Date Format Validation**

- **Quality Control Type**: Format Check
- **Control Description**: "Dates must be in DD.MM.YYYY format per policy"
- **Applies To**: "All date fields (Last Discovery Date, Last Review Date, Target Date, etc.)"
- **Implementation**: System Validation (CMDB: date picker enforces format), Spreadsheet: Data validation
- **Enforcement**: On Data Entry
- **Error Handling**: "Invalid format rejected, error: 'Please enter date as DD.MM.YYYY'"
- **Responsible Party**: "System administrators"
- **Effectiveness**: Effective
- **Measurement Method**: "Spot check random sample of date fields"
- **Last Assessed**: [Date]

2. **Periodic Reviews**:

**Example: Owner Annual Attestation**

- **Quality Control Type**: Owner Attestation
- **Control Description**: "Asset owners review and attest to accuracy of inventory records annually (Policy Section 2.5.3)"
- **Applies To**: "All asset categories"
- **Implementation**: Manual Process (automated email campaign, attestation tracking)
- **Enforcement**: Scheduled (annual)
- **Error Handling**: "Owners who don't complete receive reminder emails, escalation to manager after 30 days"
- **Responsible Party**: "Information Security Manager (coordinates), Asset Owners (perform)"
- **Effectiveness**: Partially Effective (73% completion rate Q4 2025, needs improvement)
- **Measurement Method**: "Track attestation completion percentage, calculate accuracy improvement post-review"
- **Last Assessed**: [Date]
- **Evidence Location**: "Attestation tracking spreadsheet, signed attestation forms, email archives"
- **Notes**: "Target: 95% completion by Q2 2026, implement automated reminders"

**Example: Quarterly Accuracy Sampling**

- **Quality Control Type**: Periodic Review
- **Control Description**: "Security Team samples 5% of inventory records quarterly, validates accuracy against source systems"
- **Applies To**: "All asset categories (stratified random sample)"
- **Implementation**: Manual Process (sampling script, manual verification)
- **Enforcement**: Scheduled (quarterly)
- **Error Handling**: "Errors documented, reported to asset owner for correction, tracked for trends"
- **Responsible Party**: "Information Security Team"
- **Effectiveness**: Effective
- **Measurement Method**: "Calculate accuracy rate from sample, track trend over time"
- **Last Assessed**: [Date]
- **Evidence Location**: "Quarterly accuracy reports, sampling methodology documentation"
- **Notes**: "Q4 2025 sample: 98% accuracy for IT assets, 94% for Information assets"

3. **Automated Checks**:

**Example: Staleness Detection**

- **Quality Control Type**: Automated Check
- **Control Description**: "Daily script identifies records exceeding maximum staleness per Policy Section 2.5.3"
- **Applies To**: "All inventory systems, Last Updated field"
- **Implementation**: Scheduled Script (runs daily at 1:00 AM)
- **Enforcement**: Scheduled (daily)
- **Error Handling**: "Email report to asset owners: 'Your assets need review', escalate to Security Team if >30 days overdue"
- **Responsible Party**: "IT Operations (script execution), Security Team (follow-up)"
- **Effectiveness**: Effective
- **Measurement Method**: "Track staleness alert count, monitor owner response time"
- **Last Assessed**: [Date]
- **Evidence Location**: "Script: /scripts/check_inventory_staleness.py, Daily reports: /reports/staleness/"
- **Notes**: "Thresholds from Policy: Critical=daily, High=3 days, Standard=7 days, Low=30 days"

**Example: CMDB-Discovery Reconciliation**

- **Quality Control Type**: Reconciliation
- **Control Description**: "Weekly comparison: CMDB server CIs vs. Discovery scan results, identify discrepancies"
- **Applies To**: "CMDB, IT Infrastructure - Servers"
- **Implementation**: Scheduled Script (ServiceNow reconciliation report)
- **Enforcement**: Scheduled (weekly)
- **Error Handling**: "Discrepancies reported to IT Ops: 'CIs in CMDB not in Discovery' and vice versa, manual investigation required"
- **Responsible Party**: "CMDB Administrator"
- **Effectiveness**: Effective
- **Measurement Method**: "Track discrepancy count over time, should trend toward zero"
- **Last Assessed**: [Date]
- **Evidence Location**: "ServiceNow reconciliation reports, CMDB health dashboard"

4. **Duplicate Detection**:

**Example: Duplicate Asset Detection**

- **Quality Control Type**: Duplicate Detection
- **Control Description**: "Monthly scan for potential duplicate assets (same name, similar attributes)"
- **Applies To**: "All inventory systems"
- **Implementation**: Scheduled Script (fuzzy matching algorithm)
- **Enforcement**: Scheduled (monthly)
- **Error Handling**: "Potential duplicates reported to Security Team, manual review to confirm, merge or mark as distinct"
- **Responsible Party**: "Information Security Manager"
- **Effectiveness**: Partially Effective (some false positives, manual review burden)
- **Measurement Method**: "Track duplicate count, validate accuracy of detection algorithm"
- **Last Assessed**: [Date]
- **Evidence Location**: "Duplicate detection reports, resolution tracking log"
- **Notes**: "Common false positive: 'Laptop-001' in different locations (same model, not duplicate)"

**Common Pitfalls**:

- ❌ Implementing controls but not measuring effectiveness
- ✅ Track control performance, calculate metrics, demonstrate improvement
- ❌ Relying only on automated checks (need manual reviews too)
- ✅ Combine automated validation with periodic human verification
- ❌ Ignoring validation errors (users work around controls)
- ✅ Monitor failed validation attempts, fix root causes

**Completeness Check**: All quality dimensions from Policy Section 2.5 should have controls.

---

### Sheet 6: Maintenance Metrics

**Purpose**: Aggregate metrics on maintenance effectiveness.

**What This Sheet Captures**:

- Update timeliness (% within SLA)
- Integration health (sync success rates)
- Data quality scores (accuracy, completeness, currency)
- Review compliance (% reviews completed on time)
- Trending over time

**This sheet is MOSTLY auto-populated** from other sheets, similar to Completeness Analysis in IMP-A.5.9-1.

**Column Definitions**:

| Column | Purpose | How to Complete |
|--------|---------|-----------------|
| **Metric Category** | Type of metric | Auto-populated: Update Timeliness / Integration Health / Data Quality / Review Compliance |
| **Metric Name** | Specific metric | Auto-populated from other sheets |
| **Target Value** | Policy requirement or SLA | From policy or set internally |
| **Current Value** | Actual achievement | Auto-calculated or manual entry |
| **Gap vs. Target** | Shortfall or surplus | Auto-calculated |
| **Compliance Status** | Met target or not | Auto-calculated: ✅ / ⚠️ / ❌ |
| **Measurement Period** | When measured | Date range |
| **Trend vs. Last Quarter** | Improving or degrading | Dropdown: Improved / Stable / Degraded / N/A |
| **Remediation Actions** | How to improve | Free text (if not compliant) |
| **Responsible Party** | Who owns improvement | Free text |
| **Notes** | Context | Free text |

**Example Metrics**:

1. **Update Timeliness**:

   - Metric: "% of updates within SLA (weighted across all trigger types)"
   - Target: 95%
   - Current: 89% (Q4 2025)
   - Compliance Status: ⚠️ At Risk
   - Trend: Stable (was 88% Q3)
   - Remediation: "Focus on SaaS app onboarding (only 78% compliant), automate reminder emails"

2. **Integration Health**:

   - Metric: "Average sync success rate across all integrations"
   - Target: 98%
   - Current: 96% (Q4 2025)
   - Compliance Status: ⚠️ At Risk
   - Trend: Improved (was 93% Q3)
   - Remediation: "Fix SAP procurement CSV format issues (causing 89% success rate)"

3. **Data Quality - Accuracy**:

   - Metric: "Accuracy % from quarterly sampling (stratified)"
   - Target: 95%
   - Current: 96% (Q4 2025 sample)
   - Compliance Status: ✅ Compliant
   - Trend: Improved (was 94% Q3)

4. **Review Compliance**:

   - Metric: "% of annual owner reviews completed on time"
   - Target: 95%
   - Current: 73% (Q4 2025)
   - Compliance Status: ❌ Non-Compliant
   - Trend: Degraded (was 78% Q3)
   - Remediation: "Implement automated reminders at T-14 days and T-7 days, escalate to management at T+7 days overdue"

---

### Sheet 7: Evidence Register

**Purpose**: Document all evidence related to maintenance procedures.

**What This Sheet Captures**:

- Procedure documentation (update workflows, integration configs)
- System configurations (validation rules, access controls)
- Review records (attestations, audit reports, sampling results)
- Metrics reports (SLA achievement, integration health, data quality)
- Evidence metadata for audit trail

**Column Definitions**: (Similar to IMP-A.5.9-1 Evidence Register)

| Column | Purpose | How to Complete |
|--------|---------|-----------------|
| **Evidence ID** | Unique identifier | Format: MAINT-001, MAINT-002, etc. |
| **Evidence Type** | Type of evidence | Dropdown: Procedure Document / System Configuration / Review Record / Metrics Report / Integration Config / Workflow Diagram / Meeting Minutes |
| **Related Domain** | Which maintenance domain | Dropdown: Inventory Structure / Update Procedures / Integration / Data Quality / All Domains |
| **Evidence Description** | What the evidence shows | Free text |
| **Collection Date** | When evidence collected | Date field |
| **Collected By** | Who collected | Free text |
| **File Name** | Evidence file name | Free text |
| **Storage Location** | Where stored | Free text |
| **Evidence Format** | File type | Dropdown: PDF / Excel / CSV / Screenshot / Config File / JSON / XML / Text / Other |
| **Retention Period** | How long to keep | Dropdown: 1 Year / 3 Years / 5 Years / 7 Years / Permanent |
| **Access Restriction** | Who can access | Dropdown: Public / Internal / Confidential / Restricted |
| **Evidence Quality** | Sufficient? | Dropdown: Complete / Partial / Insufficient |
| **Related Sheet** | Which sheet references | Free text |
| **Notes** | Additional context | Free text |

**Example Evidence**:

1. **MAINT-001**: ServiceNow CMDB schema documentation
2. **MAINT-002**: Asset update workflow diagram
3. **MAINT-003**: Workday API integration configuration file
4. **MAINT-004**: Q4 2025 SLA achievement report
5. **MAINT-005**: Owner attestation forms (Q4 2025)
6. **MAINT-006**: Quarterly accuracy sampling report
7. **MAINT-007**: Integration health dashboard screenshot

---

## Common Pitfalls

### Pitfall 1: Only Documenting "Official" Processes

**Problem**: Documenting idealized workflows that don't match reality.

**Why It Fails**: Auditors will find the actual process, gaps between documented and actual create audit findings.

**Solution**: Document ACTUAL procedures, even if imperfect:

- ❌ "All updates automated via API"
- ✅ "Most updates automated (94%), some manual (6% - SaaS apps, special cases)"

### Pitfall 2: Not Measuring SLA Compliance

**Problem**: Setting SLAs but never checking if they're met.

**Why It Fails**: Can't improve what you don't measure.

**Solution**: Track actual update times, calculate compliance percentage:

- Pull sample of updates (e.g., 100 from last quarter)
- Measure time from trigger to inventory update
- Calculate % within SLA

### Pitfall 3: Assuming Integrations "Just Work"

**Problem**: Not monitoring integration health, not reconciling data.

**Why It Fails**: Silent failures accumulate, inventory drifts from reality.

**Solution**:

- Monitor every integration (success rate, error logs)
- Reconcile periodically (compare source vs. target, identify discrepancies)
- Document ACTUAL sync success rate (not theoretical)

### Pitfall 4: Over-Engineering for Year 1

**Problem**: Trying to automate everything before certification.

**Why It Fails**: Automation takes time, Year 1 focus is demonstrating the process exists.

**Solution**: Document current state honestly:

- Manual processes are acceptable for Year 1 if documented
- "Manual entry, quarterly review" is compliant
- Plan automation roadmap for Year 2+

### Pitfall 5: Not Documenting Manual Processes

**Problem**: Only documenting automated integrations, ignoring manual procedures.

**Why It Fails**: Manual processes are still processes, need documentation.

**Solution**: Document manual workflows too:

- "Monthly: Security Manager exports SharePoint inventory to Excel, manual comparison with Asset Inventory, updates noted, changes made"
- Even if manual, it's documented and repeatable

### Pitfall 6: Ignoring Data Quality Drift

**Problem**: Implementing validation rules at setup, never checking if they're working.

**Why It Fails**: Users find workarounds, data quality degrades over time.

**Solution**:

- Periodically test validation rules (try to enter bad data, should be blocked)
- Sample data quality (5-10% quarterly)
- Track data quality metrics over time

### Pitfall 7: No Owner Accountability

**Problem**: Owners assigned but never required to review/attest.

**Why It Fails**: Owners forget they own assets, inventory becomes stale.

**Solution**:

- Annual (minimum) owner review requirement
- Track attestation completion
- Escalate non-compliance to management

---

## Quality Checklist

Before submitting this assessment, verify:

### Inventory Structure Checks

- [ ] All systems holding inventory data documented
- [ ] Schema/structure documented for each system
- [ ] Mandatory attributes mapped to policy requirements
- [ ] Gaps identified (attributes missing from systems)
- [ ] Access controls documented
- [ ] Backup procedures documented

### Update Procedure Checks

- [ ] All trigger types from policy documented
- [ ] Workflows documented for each trigger
- [ ] SLAs defined (aligned with policy maximum staleness)
- [ ] Responsible parties assigned
- [ ] SLA achievement measured (percentage calculated)
- [ ] Failure handling procedures documented

### Integration Checks

- [ ] All system integrations documented
- [ ] Data flows mapped (source → target)
- [ ] Integration methods specified (API, file, etc.)
- [ ] Sync frequencies documented
- [ ] Reconciliation procedures defined
- [ ] Integration health monitored (success rates tracked)
- [ ] Manual processes documented (if applicable)

### Data Quality Checks

- [ ] Validation rules documented
- [ ] Mandatory fields enforced
- [ ] Periodic review procedures defined
- [ ] Error detection and correction workflows documented
- [ ] Data quality metrics tracked
- [ ] Control effectiveness measured

### Metrics Checks

- [ ] Update timeliness calculated
- [ ] Integration health calculated
- [ ] Data quality scores calculated
- [ ] Review compliance calculated
- [ ] Trends vs. previous quarter documented
- [ ] Remediation actions defined (if non-compliant)

### Evidence Checks

- [ ] Procedure documents collected
- [ ] System configurations exported
- [ ] Review records compiled
- [ ] Metrics reports generated
- [ ] Evidence metadata complete
- [ ] Evidence stored securely

### Cross-Cutting Checks

- [ ] All required fields completed
- [ ] Notes provided for unusual situations
- [ ] Trends documented (if quarterly update)
- [ ] Remediation plans are specific and actionable
- [ ] Responsible parties assigned for all items

---

## Review & Approval

### Review Process

**Step 1: Self-Review** (Assessment Preparer)

- Complete quality checklist above
- Fix any identified issues
- Prepare summary for reviewers

**Step 2: Technical Review** (CMDB Administrator, IT Operations)

- Validate integration documentation is accurate
- Confirm update procedures match reality
- Verify system configurations documented correctly
- Sign off on technical accuracy

**Step 3: Security Review** (Information Security Manager)

- Review compliance against policy requirements
- Assess metric targets and achievement
- Verify data quality controls are sufficient
- Check evidence quality
- Prepare summary for CISO

**Step 4: CISO Approval**

- Review maintenance effectiveness metrics
- Assess compliance status (on-target or at-risk)
- Approve remediation plans and resource allocation
- Escalate significant gaps to Executive Management if necessary
- Sign approval

**Step 5: Submission to Compliance Dashboard**

- Export metrics to dashboard consolidation workbook
- Update ISMS-IMP-A.5.9.5 (Compliance Dashboard)
- Archive assessment workbook
- Store evidence per retention policy

### Approval Criteria

**Approve** if:

- ✅ All inventory systems documented
- ✅ Update procedures documented for all trigger types
- ✅ SLA achievement ≥80% overall
- ✅ Integration health ≥90%
- ✅ Data quality ≥85% (minimum acceptable, 95% target)
- ✅ Evidence quality rated "Complete" or "Partial"

**Conditional Approval** (with remediation plan) if:

- ⚠️ SLA achievement 70-79%
- ⚠️ Integration health 80-89%
- ⚠️ Data quality 75-84%
- ⚠️ Remediation plans need refinement

**Reject** if:

- ❌ Major systems undocumented
- ❌ SLA achievement <70%
- ❌ Integration health <80%
- ❌ Data quality <75%
- ❌ No remediation plans for critical gaps

### Approval Record

Document approval in assessment workbook:

| Role | Name | Date | Signature/Email | Comments |
|------|------|------|----------------|----------|
| Assessment Preparer | [Name] | [Date] | [Email] | Completed assessment per specification |
| CMDB Administrator Review | [Name] | [Date] | [Email] | Validated system and integration accuracy |
| Information Security Manager | [Name] | [Date] | [Email] | Reviewed for compliance, metrics quality |
| CISO | [Name] | [Date] | [Email] | Approved / Conditional / Rejected |

---

**END OF USER GUIDE**

---

*"The measure of intelligence is the ability to change."*
— Albert Einstein

<!-- QA_VERIFIED: 2026-02-06 -->
