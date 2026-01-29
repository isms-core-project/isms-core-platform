# ISMS-IMP-A.5.9-2
## Inventory Structure & Maintenance
### ISO/IEC 27001:2022 Control A.5.9: Inventory of Information and Assets

---

## Document Overview

**Document ID:** ISMS-IMP-A.5.9-2  
**Implementation Area:** Inventory System Structure and Maintenance Operations  
**Related Policy:** ISMS-POL-A.5.9-S2 (Requirements Framework), ISMS-POL-A.5.9-S3 (Implementation & Assessment)  
**Purpose:** Guide [Organization] in designing inventory system architecture, establishing maintenance workflows, and ensuring data quality

**Key Principle:** The inventory system is not just a database or spreadsheet—it's an operational tool that must integrate with existing systems, support daily operations, and remain current through systematic maintenance.

---

## 1. Inventory System Options

### 1.1 Decision Framework

**Question:** What type of inventory system should [Organization] implement?

**Answer:** It depends on [Organization]'s size, complexity, existing infrastructure, and resources.

```
Decision Tree: Selecting Inventory System Approach

Start: Does [Organization] have an existing CMDB/ITSM platform?
├─ YES, comprehensive CMDB
│  └─ Option 1: Extend CMDB with ISMS attributes
│     ├─ Pros: Single source of truth, existing workflows, IT familiarity
│     ├─ Cons: May not handle information assets well, customization needed
│     └─ Best for: Organizations with mature IT operations
│
├─ YES, basic CMDB
│  └─ Option 2: Hybrid (CMDB for IT + separate system for information assets)
│     ├─ Pros: Leverages existing tech investment, specialized handling
│     ├─ Cons: Synchronization complexity, dual maintenance
│     └─ Best for: Medium-sized organizations
│
└─ NO CMDB
   ├─ Small organization (<100 assets)?
   │  └─ Option 3: Spreadsheet-based with automation (Python + Excel)
   │     ├─ Pros: Low cost, flexible, easy to understand
   │     ├─ Cons: Manual effort, scaling limitations
   │     └─ Best for: Small organizations, initial implementations
   │
   └─ Larger organization (>100 assets)?
      └─ Option 4: Dedicated asset management tool or custom solution
         ├─ Pros: Purpose-built, scalable, feature-rich
         ├─ Cons: Cost, implementation time, vendor dependency
         └─ Best for: Large organizations, high asset counts
```

### 1.2 Option 1: Extend Existing CMDB/ITSM Platform

**Examples:** ServiceNow, BMC Remedy, Jira Service Management, Ivanti, etc.

**Implementation Approach:**

1. **Assess Current CMDB Capabilities**
   - Does it track Configuration Items (CIs)?
   - Can it handle custom attributes?
   - Does it support relationships between items?
   - Can it generate reports/dashboards?

2. **Extend CMDB Schema**
   - Add ISMS-required attributes:
     - Owner (business owner, not just technical contact)
     - Classification (Confidentiality, Integrity, Availability)
     - Status (Active, Archive, Decommissioned)
     - Review dates (Last Reviewed, Next Review Due)
     - Regulatory tags (GDPR, HIPAA, etc.)
   - Create new CI classes if needed:
     - Information Asset class (for data/documents)
     - Personnel Asset class (for competencies/roles)

3. **Configure Workflows**
   - Owner assignment and acknowledgment workflow
   - Review reminder workflow
   - Change notification workflow
   - Decommissioning approval workflow

4. **Integrate with ISMS Processes**
   - Link to risk management
   - Feed access control decisions
   - Support incident response
   - Enable vulnerability management

**Pros:**
- ✅ Single source of truth (IT + security)
- ✅ Existing IT staff familiarity
- ✅ Integrated with change management, incident management
- ✅ Usually has API for automation
- ✅ Audit trail and versioning built-in

**Cons:**
- ❌ CMDB platforms often IT-infrastructure-focused (servers, apps)
- ❌ May not handle information assets (data, documents) naturally
- ❌ Customization may require platform expertise
- ❌ Licensing costs if expanding user base
- ❌ IT terminology may confuse business owners

**Best For:** Organizations with mature ITSM practices and IT-heavy asset portfolios

### 1.3 Option 2: Dedicated Asset Management Tools

**Examples:** Snipe-IT (open-source), Asset Panda, InvGate Assets, etc.

**Implementation Approach:**

1. **Evaluate Tools**
   - Asset tracking capabilities (IT, physical, information)
   - Custom field support
   - Workflow automation
   - Reporting and dashboards
   - Integration APIs
   - Cost (licensing, hosting, maintenance)

2. **Deploy and Configure**
   - Install/subscribe to platform
   - Configure asset categories per ISMS-POL-A.5.9-S2
   - Define custom fields (owner, classification, etc.)
   - Set up user roles and permissions
   - Configure notifications (review reminders, change alerts)

3. **Integrate with Existing Systems**
   - Discovery tool integration (auto-populate technical assets)
   - Active Directory integration (users, authentication)
   - SIEM integration (security event correlation)
   - HR system integration (personnel assets)

4. **Migrate Existing Data**
   - Export from current systems
   - Clean and normalize data
   - Import to new platform
   - Validate migration completeness

**Pros:**
- ✅ Purpose-built for asset management
- ✅ Often includes discovery/scanning features
- ✅ User-friendly interfaces for non-IT users
- ✅ Mobile apps for physical asset tracking (barcode scanning, etc.)
- ✅ Lower cost than enterprise CMDB

**Cons:**
- ❌ Another system to maintain
- ❌ May not integrate as deeply with IT operations
- ❌ Requires user training and adoption
- ❌ Data synchronization with CMDB if both exist

**Best For:** Organizations without CMDB or needing specialized asset management

### 1.4 Option 3: Spreadsheet-Based (Enhanced with Automation)

**Approach:** Use Excel/Google Sheets as data store, enhance with Python scripts for automation

**Implementation Approach:**

1. **Design Spreadsheet Structure**
   - One workbook per asset category OR
   - One workbook with multiple sheets (by category)
   - Follow template structure from Python generators

2. **Implement Data Validation**
   - Dropdowns for controlled values
   - Conditional formatting for visual feedback
   - Formula-based calculations (review dates, etc.)
   - Protected cells for formulas

3. **Automate with Python Scripts**
   - Discovery integration: Import scan results
   - Data quality checks: Validate completeness, accuracy
   - Report generation: Compliance dashboards
   - Reminder notifications: Email alerts for overdue reviews

4. **Version Control**
   - Use file naming convention: `ISMS_A_5_9_Assets_YYYYMMDD_v##.xlsx`
   - Store in controlled location (SharePoint, file server)
   - Restrict write access to authorized personnel
   - Maintain backup copies

**Pros:**
- ✅ Zero/low cost (uses existing tools)
- ✅ Familiar to users (everyone knows Excel)
- ✅ Flexible and easy to customize
- ✅ No vendor lock-in
- ✅ Can start immediately

**Cons:**
- ❌ Manual effort for updates (no automated workflows)
- ❌ Limited scalability (>500 assets becomes challenging)
- ❌ Version control complexity (multiple users editing)
- ❌ No built-in audit trail
- ❌ Risk of human error (accidental deletion, formula breaks)

**Best For:** Small organizations (<100 assets), proof-of-concept, budget constraints

**Enhancement Strategy:**
If starting with spreadsheets, plan migration path to more robust system as organization grows.

### 1.5 Option 4: Custom Solution (Database + Web Interface)

**Approach:** Build custom inventory system tailored to [Organization]'s needs

**Implementation Approach:**

1. **Requirements Analysis**
   - Document specific needs
   - Identify integration points
   - Define user workflows
   - Determine reporting requirements

2. **Technology Selection**
   - Backend: PostgreSQL/MySQL database
   - Frontend: Web application (Python Flask/Django, Node.js, etc.)
   - API: RESTful API for integrations
   - Authentication: LDAP/SSO integration

3. **Development**
   - Database schema design (normalized, indexed)
   - Web interface (CRUD operations, search, reporting)
   - API endpoints for automation
   - Workflow automation (owner notifications, review reminders)

4. **Deployment**
   - Hosting (on-premise or cloud)
   - Security hardening
   - Backup/disaster recovery
   - Monitoring and maintenance

**Pros:**
- ✅ Tailored exactly to [Organization]'s needs
- ✅ Full control over features and integrations
- ✅ No licensing costs (beyond hosting)
- ✅ Can evolve with organization

**Cons:**
- ❌ High initial development effort
- ❌ Requires technical expertise to maintain
- ❌ Long time to implement
- ❌ Risk of technical debt if not maintained
- ❌ Staff turnover risk (knowledge loss)

**Best For:** Large organizations with development resources and unique requirements

---

## 2. Data Structure Design

### 2.1 Relational Model Principles

**Core Entities:**

```
┌─────────────────┐
│ INFORMATION     │
│ ASSET           │──┐
├─────────────────┤  │
│ PK: Asset_ID    │  │
│ Name            │  │
│ Type            │  │
│ Classification  │  │
│ Owner_ID (FK)   │  │
│ ...             │  │
└─────────────────┘  │
                     │
┌─────────────────┐  │  ┌─────────────────┐
│ ASSOCIATED      │  │  │ RELATIONSHIP    │
│ ASSET           │  │  │                 │
├─────────────────┤  │  ├─────────────────┤
│ PK: Asset_ID    │  └──│ Info_Asset_ID   │
│ Name            │     │ Assoc_Asset_ID  │
│ Type            │     │ Relationship    │
│ Custodian_ID    │     │ Description     │
│ ...             │     └─────────────────┘
└─────────────────┘
        │
        │
┌─────────────────┐
│ OWNER           │
├─────────────────┤
│ PK: Owner_ID    │
│ Name            │
│ Email           │
│ Department      │
│ Acknowledged    │
└─────────────────┘
```

**Normalization Guidelines:**

**Do Normalize:**
- Owner information (separate OWNER table)
  - Allows updating owner contact info in one place
  - Supports reporting by owner
- Lookup values (asset types, classifications)
  - Reference tables for controlled vocabularies
  - Enables consistent dropdown values

**Don't Over-Normalize:**
- Asset attributes that rarely repeat
  - Description, Serial Number, Location (keep in main table)
- Audit fields (Created Date, Updated Date, Reviewed Date)
  - Duplicating across tables is acceptable for audit trail

### 2.2 Field Naming Conventions

**Recommended Convention:**

- **Use clear, descriptive names:** `Asset_Name` not `AName`
- **Consistent prefixes for relationships:** `Owner_ID`, `Custodian_ID`
- **Dates include context:** `Created_Date`, `Last_Reviewed_Date`, `Next_Review_Date`
- **Boolean fields clearly stated:** `Is_Active`, `Requires_Encryption`, `Has_Backup`
- **Avoid reserved words:** Don't use `Order`, `Select`, `User` as field names

**Example Field Set (Information Asset):**

| Field Name | Data Type | Length | Nullable | Notes |
|------------|-----------|--------|----------|-------|
| Asset_ID | VARCHAR | 20 | NO | Primary Key (e.g., INFO-001) |
| Asset_Name | VARCHAR | 200 | NO | Descriptive name |
| Asset_Type | VARCHAR | 50 | NO | FK to ASSET_TYPE_LU table |
| Description | TEXT | - | YES | Detailed description |
| Owner_ID | VARCHAR | 20 | NO | FK to OWNER table |
| Custodian_ID | VARCHAR | 20 | YES | FK to CUSTODIAN table |
| Classification | VARCHAR | 30 | NO | Public/Internal/Confidential/Strictly Confidential |
| Status | VARCHAR | 20 | NO | Active/Archive/Decommissioned/Planned |
| Created_Date | DATE | - | NO | When asset was first recorded |
| Created_By | VARCHAR | 100 | NO | User who created record |
| Last_Updated_Date | DATETIME | - | YES | Last modification timestamp |
| Last_Updated_By | VARCHAR | 100 | YES | User who last modified |
| Last_Reviewed_Date | DATE | - | YES | Last owner review |
| Next_Review_Date | DATE | - | YES | Calculated based on classification |

### 2.3 Data Types and Validation

**String Fields:**
- Use VARCHAR with reasonable limits (prevents abuse)
- TEXT for long descriptions (no length limit needed)
- CHAR for fixed-length codes (e.g., CHAR(2) for country codes)

**Date/Time Fields:**
- DATE for calendar dates (Created, Reviewed)
- DATETIME for timestamps (Last_Updated includes time)
- Store in UTC, display in local timezone

**Numeric Fields:**
- INTEGER for counts (user count, asset count)
- DECIMAL for monetary values (cost, depreciation)
- Avoid FLOAT for financial data (precision issues)

**Boolean Fields:**
- BOOLEAN or TINYINT(1)
- 0 = False, 1 = True
- NOT NULL with default value

**Validation Rules (Database Level):**
```sql
-- Example constraints
ALTER TABLE Information_Asset
  ADD CONSTRAINT chk_classification 
    CHECK (Classification IN ('Public', 'Internal', 'Confidential', 'Strictly Confidential'));

ALTER TABLE Information_Asset
  ADD CONSTRAINT chk_status
    CHECK (Status IN ('Active', 'Archive', 'Decommissioned', 'Planned'));

ALTER TABLE Information_Asset
  ADD CONSTRAINT chk_review_date
    CHECK (Next_Review_Date IS NULL OR Next_Review_Date >= Last_Reviewed_Date);
```

### 2.4 Indexing Strategy

**Primary Keys:**
- All tables have primary key (unique identifier)
- Use meaningful IDs when possible (INFO-001, SRV-042)
- OR use auto-increment integers with separate display ID

**Foreign Keys:**
- Define FK relationships for referential integrity
- Ensure cascade rules appropriate (CASCADE, SET NULL, RESTRICT)

**Indexes for Performance:**
```sql
-- Frequently searched fields
CREATE INDEX idx_asset_owner ON Information_Asset(Owner_ID);
CREATE INDEX idx_asset_classification ON Information_Asset(Classification);
CREATE INDEX idx_asset_status ON Information_Asset(Status);
CREATE INDEX idx_next_review ON Information_Asset(Next_Review_Date);

-- Composite indexes for common queries
CREATE INDEX idx_owner_status ON Information_Asset(Owner_ID, Status);
CREATE INDEX idx_classification_review ON Information_Asset(Classification, Next_Review_Date);
```

**Index Guidelines:**
- Index foreign keys for JOIN performance
- Index fields used in WHERE clauses frequently
- Don't over-index (slows INSERT/UPDATE)
- Monitor and tune based on actual query patterns

---

## 3. Integration Architecture

### 3.1 CMDB Integration Strategy

**Scenario:** [Organization] has existing CMDB, wants to integrate with ISMS inventory

**Integration Pattern: Bi-Directional Sync**

```
┌──────────────────────┐         ┌──────────────────────┐
│                      │         │                      │
│    CMDB              │◄───────►│  ISMS Inventory      │
│  (ServiceNow, etc.)  │  Sync   │  (Custom System)     │
│                      │         │                      │
└──────────────────────┘         └──────────────────────┘
        │                                 │
        │ Technical Attributes            │ Security Attributes
        │ - IP Address                    │ - Owner
        │ - Hostname                      │ - Classification
        │ - Location                      │ - Last Reviewed
        │ - Model/Serial                  │ - Relationships
        │                                 │
        └─────────────┬───────────────────┘
                      │
               Reconciliation
                 Process
```

**Synchronization Strategy:**

1. **Define Authoritative Source Per Attribute**

| Attribute | Authoritative Source | Direction | Frequency |
|-----------|---------------------|-----------|-----------|
| Asset ID | CMDB | CMDB → ISMS | Real-time |
| Hostname | CMDB | CMDB → ISMS | Real-time |
| IP Address | CMDB | CMDB → ISMS | Hourly |
| Location | CMDB | CMDB → ISMS | Daily |
| Owner | ISMS | ISMS → CMDB | Daily |
| Classification | ISMS | ISMS → CMDB | On change |
| Last Reviewed | ISMS | ISMS only | N/A |
| Status | Both | Conflict resolution needed | On change |

2. **Implement Sync Mechanism**

**Option A: API-Based Real-Time Sync**
```python
# Example: CMDB webhook triggers ISMS update
@app.route('/webhook/cmdb_update', methods=['POST'])
def handle_cmdb_update():
    data = request.json
    asset_id = data['ci_id']
    
    # Update ISMS inventory
    update_isms_asset(
        asset_id=asset_id,
        hostname=data['hostname'],
        ip_address=data['ip_address'],
        location=data['location']
    )
    
    return {'status': 'success'}
```

**Option B: Scheduled Batch Sync**
```python
# Example: Nightly sync job
def sync_cmdb_to_isms():
    # Query CMDB API for all CIs
    cmdb_assets = fetch_cmdb_assets()
    
    for asset in cmdb_assets:
        # Check if exists in ISMS
        if exists_in_isms(asset['ci_id']):
            # Update technical attributes
            update_technical_attributes(asset)
        else:
            # Create new record
            create_isms_asset(asset)
    
    log_sync_results()
```

3. **Conflict Resolution Rules**

**When both systems have same field:**
- **Rule 1 - Timestamp Wins:** Most recent update is authoritative
- **Rule 2 - Manual Review:** Flag conflicts for human review
- **Rule 3 - Field Priority:** Define per-field precedence

**Example Conflict Resolution:**
```python
def resolve_conflict(cmdb_value, isms_value, cmdb_timestamp, isms_timestamp):
    """
    Resolve conflicts between CMDB and ISMS values.
    """
    # Rule 1: If one value is blank, use the other
    if not cmdb_value:
        return isms_value
    if not isms_value:
        return cmdb_value
    
    # Rule 2: If values identical, no conflict
    if cmdb_value == isms_value:
        return cmdb_value
    
    # Rule 3: Timestamp wins (most recent update)
    if cmdb_timestamp > isms_timestamp:
        log_conflict(f"CMDB value {cmdb_value} wins over ISMS {isms_value}")
        return cmdb_value
    else:
        log_conflict(f"ISMS value {isms_value} wins over CMDB {cmdb_value}")
        return isms_value
```

4. **Reconciliation Process**

**Weekly Reconciliation Report:**
- Assets in CMDB but not in ISMS (new discoveries)
- Assets in ISMS but not in CMDB (manual entries, information assets)
- Attribute mismatches (investigate and resolve)
- Decommissioned assets needing cleanup

### 3.2 Discovery Tool Integration

**Purpose:** Automatically populate inventory from network/endpoint discovery tools

**Integration Points:**

1. **Network Discovery (Nmap, Qualys, Rapid7)**
   - Schedule: Weekly scans
   - Import: IP, hostname, OS, open ports, services
   - Action: Create/update IT Infrastructure assets

2. **Endpoint Discovery (Intune, JAMF, Workspace ONE)**
   - Schedule: Real-time or daily
   - Import: Device info, installed software, patches
   - Action: Create/update endpoint assets

3. **Cloud Discovery (AWS Config, Azure Resource Graph)**
   - Schedule: Hourly or real-time (via events)
   - Import: Cloud resources, configurations, tags
   - Action: Create/update cloud assets

**Implementation Pattern:**
```python
# Example: Import network scan results
def import_network_scan(scan_file):
    """
    Import assets from network scan results.
    """
    scan_results = parse_scan_file(scan_file)
    
    for discovered_asset in scan_results:
        asset_id = generate_asset_id(discovered_asset)
        
        # Check if already exists
        existing = query_inventory(asset_id)
        
        if existing:
            # Update technical attributes only (don't overwrite owner, classification)
            update_technical_only(
                asset_id=asset_id,
                ip=discovered_asset['ip'],
                hostname=discovered_asset['hostname'],
                os=discovered_asset['os']
            )
        else:
            # New discovery - create record with defaults
            create_asset(
                asset_id=asset_id,
                ip=discovered_asset['ip'],
                hostname=discovered_asset['hostname'],
                os=discovered_asset['os'],
                status='Discovered',  # Requires review
                owner='TBD'  # Requires assignment
            )
            
            # Trigger owner assignment workflow
            notify_asset_management_team(asset_id)
```

### 3.3 HR System Integration

**Purpose:** Maintain personnel asset inventory (roles, competencies)

**Integration Approach:**

1. **Data Privacy Considerations**
   - **DO NOT** import full employee database into ISMS inventory
   - **DO** extract role/competency information
   - **Minimize** personal data (GDPR compliance)

2. **Extract Relevant Data**
   ```python
   # Example: Extract key roles and competencies
   def extract_personnel_assets():
       hr_data = query_hr_system()
       
       # Group by role/competency, not individual
       competencies = {}
       for employee in hr_data:
           if employee['is_critical_role']:
               role = employee['job_title']
               if role not in competencies:
                   competencies[role] = {
                       'count': 0,
                       'department': employee['department'],
                       'criticality': assess_criticality(role)
                   }
               competencies[role]['count'] += 1
       
       # Update inventory with competency assets
       for role, data in competencies.items():
           update_personnel_asset(
               asset_type='Competency',
               name=role,
               count=data['count'],
               department=data['department'],
               criticality=data['criticality']
           )
   ```

3. **Maintain Anonymity**
   - Inventory record: "Database Administrator Competency (3 people)"
   - NOT: "John Smith, Jane Doe, Bob Jones are DBAs"

4. **Trigger Updates**
   - New hire: Check if competency count needs update
   - Termination: Update competency count, flag succession risk
   - Role change: Update competency assignments

### 3.4 Procurement System Integration

**Purpose:** Automatically create inventory records for new purchases

**Integration Workflow:**

```
Purchase Order Created
         │
         ▼
    Procurement System
         │
         ▼
    Approved Purchase
         │
         ▼
   [Integration Trigger]
         │
         ├──► Create inventory placeholder
         │    - Asset ID: Assigned
         │    - Status: "On Order"
         │    - Expected Date: PO delivery date
         │
         ▼
    Asset Delivered
         │
         ▼
   [Delivery Notification]
         │
         ├──► Update inventory record
         │    - Status: "Received"
         │    - Serial Number: From delivery
         │    - Location: Receiving dock
         │
         ▼
   Asset Deployed
         │
         ▼
   [IT Deployment Process]
         │
         └──► Finalize inventory record
              - Status: "Active"
              - Owner: Assigned
              - Location: Final location
```

**Implementation:**
```python
# Example: Procurement system webhook
@app.route('/webhook/procurement', methods=['POST'])
def handle_procurement_event():
    data = request.json
    event_type = data['event']
    
    if event_type == 'purchase_approved':
        # Create placeholder
        create_asset_placeholder(
            purchase_order=data['po_number'],
            description=data['item_description'],
            expected_date=data['delivery_date'],
            status='On Order'
        )
    
    elif event_type == 'item_received':
        # Update with delivery info
        update_asset(
            purchase_order=data['po_number'],
            serial_number=data['serial'],
            status='Received',
            location='Receiving'
        )
    
    return {'status': 'processed'}
```

---

## 4. Maintenance Workflows

### 4.1 Update Procedures

**Manual Update Workflow:**

```
User identifies change needed
         │
         ▼
   Access inventory system
         │
         ▼
   Locate asset record
         │
         ▼
   Request update (if not owner)
         │
         ├──► If Owner: Edit directly
         │             ├─ Make changes
         │             ├─ Save
         │             └─ Audit log created
         │
         └──► If Not Owner: Submit change request
                          ├─ Owner notified
                          ├─ Owner approves/rejects
                          └─ If approved: Change applied
```

**Automated Update Triggers:**

| Trigger Event | Action | System |
|---------------|--------|--------|
| New asset discovered | Create inventory record with "TBD" owner | Discovery tool → Inventory |
| Asset decommissioned | Update status to "Decommissioned" | Change management → Inventory |
| Owner changes role | Notify asset management to reassign | HR system → Inventory |
| Configuration changed | Update technical attributes | CMDB → Inventory |
| Patch applied | Update version/patch level | Patch mgmt → Inventory |
| Access granted | Log in access history | IAM → Inventory |

**Bulk Update Procedures:**

When multiple assets need same change (e.g., location move, owner reassignment):

1. **Export affected assets** to spreadsheet
2. **Make changes** in spreadsheet (easier than one-by-one)
3. **Validate changes** (check mandatory fields, valid values)
4. **Import updated data** back to inventory
5. **Verify import** (check counts, spot-check records)
6. **Notify affected owners** of changes

### 4.2 Review Procedures

**Periodic Owner Review:**

```
Review Schedule:
├─ Strictly Confidential assets: Every 90 days
├─ Confidential assets: Every 180 days
├─ Internal assets: Every 365 days
└─ Public assets: Every 730 days

Review Process:
1. System identifies assets due for review (Next_Review_Date < Today)
2. Email sent to owner with asset list
3. Owner reviews each asset:
   ├─ Confirm still accurate (classification, status, description)
   ├─ Update if needed
   └─ Certify review complete
4. System updates Last_Reviewed_Date and calculates Next_Review_Date
5. Overdue reviews escalated after 14 days
```

**Review Email Template:**
```
Subject: Asset Review Required - Action Needed by [Date]

Dear [Owner Name],

You are listed as the owner of the following assets that are due for periodic review:

1. [Asset ID] - [Asset Name] - Classification: [Level] - Status: [Status]
2. [Asset ID] - [Asset Name] - Classification: [Level] - Status: [Status]
...

Please review each asset and confirm:
- Information is accurate and current
- Classification level is correct
- Status is correct (Active, Archive, Decommissioned)
- Description is up-to-date

To complete review:
[Link to review interface]

Review due by: [Date]

If you are no longer the appropriate owner, please contact: [Asset Management Team]

Questions? Reply to this email or contact [Support Email]
```

**Escalation for Overdue Reviews:**

- **Day 0:** Initial review notification sent
- **Day 7:** Reminder sent to owner
- **Day 14:** Escalation to owner's manager
- **Day 21:** Escalation to executive (CIO/CISO)
- **Day 30:** Asset flagged as "Review Overdue" in compliance reports

### 4.3 Change Approval Workflow

**Significant Changes Requiring Approval:**

- Classification level change (especially downgrades)
- Owner reassignment
- Asset decommissioning
- Status change (Active → Decommissioned)
- Bulk updates affecting >10 assets

**Approval Workflow:**
```python
# Example: Classification change requires approval
def request_classification_change(asset_id, new_classification, justification):
    """
    Request classification change with approval workflow.
    """
    asset = get_asset(asset_id)
    current_classification = asset['classification']
    
    # Create change request
    change_request = {
        'asset_id': asset_id,
        'field': 'classification',
        'current_value': current_classification,
        'proposed_value': new_classification,
        'justification': justification,
        'requested_by': get_current_user(),
        'requested_date': datetime.now(),
        'status': 'Pending'
    }
    
    # Determine approver
    if is_downgrade(current_classification, new_classification):
        # Downgrades require higher approval
        approver = get_ciso()
    else:
        # Upgrades require owner approval only
        approver = asset['owner']
    
    # Send approval request
    send_approval_request(change_request, approver)
    
    return change_request['id']

def process_approval(change_request_id, approved, comments):
    """
    Process approval decision.
    """
    change_request = get_change_request(change_request_id)
    
    if approved:
        # Apply change
        apply_change(
            asset_id=change_request['asset_id'],
            field=change_request['field'],
            new_value=change_request['proposed_value']
        )
        
        # Log approval
        log_change(
            asset_id=change_request['asset_id'],
            change=f"{change_request['field']} changed from {change_request['current_value']} to {change_request['proposed_value']}",
            approved_by=get_current_user(),
            justification=comments
        )
        
        change_request['status'] = 'Approved'
    else:
        # Reject
        change_request['status'] = 'Rejected'
        change_request['rejection_reason'] = comments
        
        # Notify requester
        notify_requester(change_request)
```

### 4.4 Exception Handling

**Common Exception Scenarios:**

1. **Temporary Owner Absence**
   - Owner on leave, vacation, etc.
   - Delegate review responsibilities temporarily
   - Document delegation in system

2. **Owner Departure**
   - Employee leaves organization
   - Reassign assets to manager or designated successor
   - Complete within 30 days

3. **Classification Dispute**
   - Owner and Security disagree on classification
   - Escalate to CISO for decision
   - Document rationale

4. **Asset in Transition**
   - System being migrated/upgraded
   - Mark status as "In Transition"
   - Define expected completion date
   - Review after transition complete

---

## 5. Data Quality Management

### 5.1 Validation Rules

**Mandatory Field Enforcement:**

```python
# Example: Validation before save
def validate_asset_record(asset):
    """
    Validate asset record before saving.
    Returns list of validation errors.
    """
    errors = []
    
    # Mandatory fields
    mandatory_fields = ['asset_id', 'name', 'type', 'owner', 'classification', 'status']
    for field in mandatory_fields:
        if not asset.get(field):
            errors.append(f"Mandatory field missing: {field}")
    
    # Data type validation
    if asset.get('created_date'):
        if not is_valid_date(asset['created_date']):
            errors.append("Invalid date format for created_date")
    
    # Format validation
    if asset.get('email'):
        if not is_valid_email(asset['email']):
            errors.append("Invalid email format")
    
    # Controlled vocabulary validation
    valid_classifications = ['Public', 'Internal', 'Confidential', 'Strictly Confidential']
    if asset.get('classification') not in valid_classifications:
        errors.append(f"Invalid classification: {asset['classification']}")
    
    # Business rule validation
    if asset.get('next_review_date') and asset.get('last_reviewed_date'):
        if asset['next_review_date'] < asset['last_reviewed_date']:
            errors.append("Next review date cannot be before last reviewed date")
    
    return errors
```

**Referential Integrity:**
- Owner exists in Owner table
- Asset type exists in Asset_Type_LU table
- Related assets exist (for relationships)

### 5.2 Quality Metrics

**Completeness Metrics:**

```python
# Example: Calculate completeness score
def calculate_completeness(asset):
    """
    Calculate completeness percentage for an asset.
    """
    total_fields = 20  # Total number of fields
    completed_fields = 0
    
    mandatory_weight = 2  # Mandatory fields count double
    optional_weight = 1
    
    # Check each field
    for field, value in asset.items():
        if value and value != '':
            if field in MANDATORY_FIELDS:
                completed_fields += mandatory_weight
            else:
                completed_fields += optional_weight
    
    # Normalize
    max_possible = (len(MANDATORY_FIELDS) * mandatory_weight) + 
                   ((total_fields - len(MANDATORY_FIELDS)) * optional_weight)
    
    completeness = (completed_fields / max_possible) * 100
    return completeness

# Inventory-wide completeness
def inventory_completeness_report():
    """
    Generate completeness report for entire inventory.
    """
    assets = get_all_assets()
    
    total = len(assets)
    fully_complete = 0  # 100% complete
    mostly_complete = 0  # 80-99% complete
    partial = 0  # 50-79% complete
    incomplete = 0  # <50% complete
    
    for asset in assets:
        score = calculate_completeness(asset)
        if score == 100:
            fully_complete += 1
        elif score >= 80:
            mostly_complete += 1
        elif score >= 50:
            partial += 1
        else:
            incomplete += 1
    
    return {
        'total': total,
        'fully_complete': fully_complete,
        'mostly_complete': mostly_complete,
        'partial': partial,
        'incomplete': incomplete,
        'overall_percentage': ((fully_complete + mostly_complete) / total) * 100
    }
```

**Accuracy Metrics:**

Measured through sampling and verification (see ISMS-IMP-A.5.9-3 for detailed assessment procedures).

**Currency Metrics:**

```sql
-- Assets reviewed within required timeframe
SELECT 
    Classification,
    COUNT(*) as Total_Assets,
    SUM(CASE WHEN Next_Review_Date >= CURDATE() THEN 1 ELSE 0 END) as Current,
    SUM(CASE WHEN Next_Review_Date < CURDATE() THEN 1 ELSE 0 END) as Overdue,
    (SUM(CASE WHEN Next_Review_Date >= CURDATE() THEN 1 ELSE 0 END) / COUNT(*)) * 100 as Currency_Percentage
FROM Information_Asset
WHERE Status = 'Active'
GROUP BY Classification;
```

**Target:** ≥90% currency across all asset categories

### 5.3 Data Quality Reporting

**Weekly Data Quality Report:**

```
ISMS Asset Inventory - Data Quality Report
Week of: [Date]

COMPLETENESS:
- Total Assets: 1,247
- Fully Complete (100%): 1,105 (88.6%)
- Mostly Complete (80-99%): 98 (7.9%)
- Needs Attention (<80%): 44 (3.5%)

OWNER ASSIGNMENT:
- Assets with Owners: 1,247 (100%) ✅
- Owner Acknowledgments: 1,180 (94.6%)
- Pending Acknowledgments: 67 (5.4%)

REVIEW CURRENCY:
- Current (reviewed on-time): 1,120 (89.8%)
- Overdue <30 days: 98 (7.9%)
- Overdue >30 days: 29 (2.3%) ⚠️

CLASSIFICATIONS:
- Strictly Confidential: 145 (11.6%)
- Confidential: 412 (33.0%)
- Internal: 568 (45.5%)
- Public: 122 (9.8%)

ACTIONS REQUIRED:
1. Follow up on 67 pending owner acknowledgments
2. Escalate 29 assets overdue >30 days
3. Complete 44 incomplete asset records

Contact: [Asset Management Team]
```

---

## 6. Access Control

### 6.1 Role-Based Access Control (RBAC)

**Roles and Permissions:**

| Role | View Assets | Edit Own Assets | Edit All Assets | Admin Functions |
|------|-------------|-----------------|-----------------|-----------------|
| **Asset Owner** | Own assets only | ✅ Yes | ❌ No | ❌ No |
| **Asset Custodian** | Associated assets | Technical attributes only | ❌ No | ❌ No |
| **Asset Manager** | All assets | ✅ Yes | ✅ Yes | Limited (reporting) |
| **Security Team** | All assets | Classification, reviews | ✅ Yes | Yes (quality checks) |
| **Auditor** | All assets (read-only) | ❌ No | ❌ No | Yes (audit logs) |
| **CISO** | All assets | ✅ Yes | ✅ Yes | ✅ Yes (all functions) |

### 6.2 Implementation Example

```python
# Example: Permission checking
def can_user_edit_asset(user, asset):
    """
    Check if user has permission to edit asset.
    """
    # CISO can edit everything
    if user.role == 'CISO':
        return True
    
    # Asset Manager can edit all
    if user.role == 'Asset Manager':
        return True
    
    # Security Team can edit classification and security attributes
    if user.role == 'Security Team':
        return True  # With restrictions on certain fields
    
    # Asset Owner can edit their own assets
    if user.role == 'Asset Owner' and asset.owner_id == user.user_id:
        return True
    
    # Asset Custodian can edit technical attributes only
    if user.role == 'Asset Custodian' and asset.custodian_id == user.user_id:
        return 'technical_only'
    
    # Default deny
    return False
```

### 6.3 Audit Logging

**Log All Changes:**
```python
# Example: Audit log entry
def log_change(asset_id, field, old_value, new_value, user, timestamp):
    """
    Log all changes to audit table.
    """
    audit_entry = {
        'asset_id': asset_id,
        'field_changed': field,
        'old_value': old_value,
        'new_value': new_value,
        'changed_by': user,
        'timestamp': timestamp,
        'ip_address': get_client_ip(),
        'session_id': get_session_id()
    }
    
    insert_audit_log(audit_entry)
```

**Audit Log Retention:** Minimum 3 years (per ISO 27001 requirements)

---

## 7. Integration with ISMS-POL-A.5.9

This implementation guidance supports the policy requirements:

| S2 Requirement | Implementation Section |
|----------------|----------------------|
| R7: Lifecycle Management | Section 4.1 (Update Procedures), 4.2 (Review Procedures) |
| R8: Integration | Section 3 (All integration points) |
| R9: Data Quality | Section 5 (Data Quality Management) |
| R10: Access Control | Section 6 (Access Control) |

---

## 8. Summary

**Key Takeaways:**

1. **System Selection:** Choose inventory system based on organization size, existing infrastructure, and resources
2. **Data Structure:** Design normalized, well-indexed database for performance and maintainability
3. **Integration:** Leverage existing systems (CMDB, HR, procurement) to reduce manual effort
4. **Maintenance:** Establish systematic workflows for updates, reviews, and quality assurance
5. **Quality:** Measure and improve completeness, accuracy, and currency continuously
6. **Access Control:** Implement RBAC with appropriate permissions and audit logging

**Next Implementation Document:** ISMS-IMP-A.5.9-3 - Assessment Specifications (detailed workbook specifications)

---

## Revision History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 10.01.2026 | ISMS Implementation Team | Initial implementation guidance |

---

**Related Documents:**
- ISMS-POL-A.5.9 (Master Framework)
- ISMS-POL-A.5.9-S2 (Requirements Framework)
- ISMS-POL-A.5.9-S3 (Implementation & Assessment)
- ISMS-IMP-A.5.9-1 (Asset Identification & Discovery)
- ISMS-IMP-A.5.9-3 (Assessment Specifications)

---

*"A well-maintained inventory system is not an overhead—it's the operational foundation of effective security."*

**Document Status:** Ready for implementation  
**Estimated Reading Time:** 50-60 minutes  
**Target Audience:** IT management, asset management team, security team, system architects
