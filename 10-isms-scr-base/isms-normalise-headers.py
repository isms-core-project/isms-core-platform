#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
ISMS-IMP-A.8.24.1 - Data Transmission Cryptography Assessment Excel Generator
================================================================================

ISO/IEC 27001:2022 Control A.8.24: Use of Cryptography
Assessment Domain 1 of 4: Data Transmission Cryptographic Controls

--------------------------------------------------------------------------------
SAMPLE SCRIPT - REQUIRES CUSTOMIZATION FOR YOUR ORGANIZATION
--------------------------------------------------------------------------------

This script is a TEMPLATE/SAMPLE implementation and MUST be adapted to match
your organization's specific data transmission infrastructure, cryptographic
standards, and assessment requirements.

Key customization areas:
1. Protocol implementations and versions (match your actual infrastructure)
2. Cipher suite requirements and scoring criteria (adapt to your risk profile)
3. Certificate management systems (specific to your PKI infrastructure)
4. Integration points and data flows (based on your network architecture)
5. Compliance thresholds (aligned with your regulatory requirements)

DO NOT use this script without reviewing and adapting all sections marked
with "# CUSTOMIZE:" comments throughout the code.

Reference Pattern: Based on ISMS-A.8.24 Use of Cryptography Assessment Framework

--------------------------------------------------------------------------------
DESCRIPTION
--------------------------------------------------------------------------------

This script generates a comprehensive Excel assessment workbook for evaluating
cryptographic controls protecting data in transit across all network transmission
scenarios.

**Purpose:**
Enables systematic assessment of encryption implementation for data transmission
against ISO 27001:2022 Control A.8.24 requirements, supporting evidence-based
validation of cryptographic protection during network communication.

**Assessment Scope:**
- TLS/SSL protocol versions and cipher suites
- VPN encryption standards and implementations
- API communication security (REST, SOAP, GraphQL)
- File transfer protocols (SFTP, FTPS, SCP)
- Email encryption (S/MIME, PGP, TLS)
- Database connection encryption
- Internal network segmentation encryption
- Certificate lifecycle management
- Deprecated protocol identification
- Gap analysis and remediation planning
- Evidence collection for audit readiness

**Generated Workbook Structure:**
1. Instructions & Legend - Assessment guidance and cryptographic standards
2. TLS/SSL Assessment - Web services, APIs, and HTTPS implementations
3. VPN Assessment - Site-to-site and remote access VPN encryption
4. File Transfer Assessment - Secure file transfer protocol implementations
5. Email Security Assessment - Email encryption and signing mechanisms
6. Database Encryption - Database connection and replication encryption
7. Certificate Management - PKI infrastructure and certificate lifecycle
8. Protocol Inventory - Comprehensive protocol usage across infrastructure
9. Gap Analysis - Non-compliant protocols and remediation requirements
10. Evidence Register - Audit evidence tracking and documentation
11. Approval & Sign-Off - Stakeholder review and approval workflow

**Key Features:**
- Data validation with cryptographic standard dropdown lists
- Conditional formatting for protocol/cipher compliance status
- Automated gap identification for deprecated algorithms
- Protected formulas with unprotected input cells
- Evidence linkage for audit traceability
- Multi-stakeholder approval workflow
- Integration with vulnerability scanning results

**Integration:**
This assessment feeds into the A.8.24.5 Compliance Dashboard, which
consolidates data from all four cryptographic assessment domains for
executive oversight and audit readiness.

--------------------------------------------------------------------------------
REQUIREMENTS
--------------------------------------------------------------------------------

System Requirements:
    - Python 3.8 or higher
    - openpyxl library for Excel generation

Installation:
    Ubuntu/Debian:
        sudo apt install python3-openpyxl
    
    Or via pip:
        pip3 install openpyxl

Dependencies:
    - openpyxl (Python Excel library)
    - datetime (standard library)

--------------------------------------------------------------------------------
USAGE
--------------------------------------------------------------------------------

Basic Usage:
    python3 generate_a824_1_data_transmission_assessment.py

Advanced Usage:
    # Generate with custom output directory
    python3 generate_a824_1_data_transmission_assessment.py --output /path/to/dir
    
    # Generate with specific date suffix
    python3 generate_a824_1_data_transmission_assessment.py --date 20250115

Output:
    File: ISMS_A_8_24_1_Data_Transmission_Assessment_YYYYMMDD.xlsx
    Location: Current directory (or specified output path)

Post-Generation Steps:
    1. Review and customize cryptographic standards to match your risk profile
    2. Inventory all data transmission systems and protocols
    3. Complete protocol assessments for each system/service
    4. Validate cipher suites against current best practices
    5. Review certificate management lifecycle
    6. Conduct gap analysis for deprecated/weak protocols
    7. Define remediation actions with timelines
    8. Collect and link audit evidence (configs, scan results)
    9. Obtain stakeholder approvals
    10. Feed results into A.8.24.5 Compliance Dashboard

--------------------------------------------------------------------------------
METADATA
--------------------------------------------------------------------------------

Control Reference:    ISO/IEC 27001:2022 Annex A Control A.8.24
Assessment Domain:    1 of 4 (Data Transmission Cryptographic Controls)
Framework Version:    1.0
Script Version:       1.0
Author:               [Developer Name / Organisation]
Date:                 [Date to be set]
Last Modified:        [Date to be set]
Python Version:       3.8+
License:              [Organisation License/Terms]

Related Documents:
    - ISMS-POL-A.8.24: Use of Cryptography Policy (Governance)
    - ISMS-IMP-A.8.24.1: Data Transmission Cryptography Implementation Guide
    - ISMS-IMP-A.8.24.2: Data Storage Cryptography Assessment (Domain 2)
    - ISMS-IMP-A.8.24.3: Authentication Cryptography Assessment (Domain 3)
    - ISMS-IMP-A.8.24.4: Key Management Assessment (Domain 4)
    - ISMS-IMP-A.8.24.5: Compliance Dashboard (Consolidation)

--------------------------------------------------------------------------------
CHANGE HISTORY
--------------------------------------------------------------------------------

Version 1.0 - [Date to be set]
    - Initial release
    - Implements full assessment framework per ISMS-IMP-A.8.24.1 specification
    - Supports comprehensive data transmission cryptography evaluation
    - Integrated with A.8.24.5 Compliance Dashboard

[Future changes to be documented here]

--------------------------------------------------------------------------------
IMPORTANT NOTES
--------------------------------------------------------------------------------

**Cryptographic Standards:**
Cryptographic algorithms and protocols evolve rapidly. Review industry standards
(NIST, BSI, ECRYPT) quarterly and update assessment criteria accordingly.
Deprecated algorithms (MD5, SHA-1, 3DES, RC4) must be identified and remediated.

**Audit Considerations:**
This assessment generates audit evidence per ISO 27001:2022 requirements.
Ensure all fields are completed accurately and evidence is properly linked.
Auditors will expect verification of protocol versions and cipher suites.

**Data Protection:**
Assessment workbooks contain sensitive infrastructure details including:
- System endpoints and network topology
- Certificate details and PKI infrastructure
- Vulnerability information and security gaps

Handle in accordance with your organization's data classification policies.

**Maintenance:**
Review and update assessment:
- Quarterly: Check for new cryptographic vulnerabilities
- Semi-annually: Update cipher suite recommendations
- Annually: Complete reassessment of all systems
- Ad-hoc: When infrastructure changes or new threats emerge

**Quality Assurance:**
Have cryptography SMEs and network security engineers validate assessments
before using results for compliance reporting or remediation decisions.

**Regulatory Alignment:**
Ensure cryptographic standards align with applicable regulatory requirements:
- Payment processing: PCI DSS cryptographic requirements
- Healthcare: HIPAA encryption standards
- Finance: Regional banking encryption requirements
- Government: Jurisdiction-specific cryptographic mandates

Customize assessment criteria to include regulatory-specific requirements.

================================================================================
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
ISMS-A.8.24 - Assessment File Normalizer Utility
================================================================================

ISO/IEC 27001:2022 Control A.8.24: Use of Cryptography
Quality Assurance Utility: Excel Assessment File Normalization & Validation

--------------------------------------------------------------------------------
SAMPLE SCRIPT - REQUIRES CUSTOMIZATION FOR YOUR ORGANIZATION
--------------------------------------------------------------------------------

This script is a TEMPLATE/SAMPLE implementation and MUST be adapted to match
your organization's specific assessment file standards and validation requirements.

Key customization areas:
1. Expected file naming conventions (match your organizational standards)
2. Workbook structure validation rules (specific to your A.8.24 assessments)
3. Data format normalization rules (adapt to your data standards)
4. Validation severity thresholds (based on your quality requirements)
5. Output formatting preferences (align with your reporting needs)

DO NOT use this script without reviewing and adapting all sections marked
with "# CUSTOMIZE:" comments throughout the code.

Reference Pattern: Based on ISMS-A.8.24 Use of Cryptography Assessment Framework

--------------------------------------------------------------------------------
DESCRIPTION
--------------------------------------------------------------------------------

This script normalizes and validates A.8.24 cryptographic assessment Excel
workbooks to ensure consistency, data quality, and compliance with framework
standards before consolidation into the compliance dashboard.

**Purpose:**
Ensures all cryptographic assessment workbooks meet quality standards and
structural requirements, preventing data consolidation errors and improving
audit evidence reliability.

**Key Functions:**
1. File Naming Validation
   - Verify naming convention compliance
   - Check date format validity (YYYYMMDD suffix)
   - Identify versioning inconsistencies

2. Workbook Structure Validation
   - Verify presence of required sheets
   - Validate column headers and data types
   - Check for missing or extra sheets
   - Ensure protected/unprotected cells are correct

3. Data Normalization
   - Standardize dropdown values (case, spacing, terminology)
   - Normalize date formats (DD.MM.YYYY)
   - Clean whitespace and formatting inconsistencies
   - Validate data type compliance (text vs. numbers)

4. Content Validation
   - Check for incomplete assessments
   - Identify placeholder/sample data not replaced
   - Validate formula integrity
   - Verify conditional formatting rules

5. Evidence Linkage Validation
   - Check evidence references are populated
   - Validate evidence file paths/URLs
   - Identify broken evidence links

6. Compliance Scoring Validation
   - Verify scoring formula correctness
   - Validate compliance percentage calculations
   - Check for scoring anomalies or errors

7. Quality Reporting
   - Generate validation report with findings
   - Categorize issues by severity (Critical, High, Medium, Low)
   - Provide remediation guidance
   - Track validation history

**Validation Scope:**
- ISMS_A_8_24_1_Data_Transmission_Assessment_YYYYMMDD.xlsx
- ISMS_A_8_24_2_Data_Storage_Assessment_YYYYMMDD.xlsx
- ISMS_A_8_24_3_Authentication_Assessment_YYYYMMDD.xlsx
- ISMS_A_8_24_4_Key_Management_Assessment_YYYYMMDD.xlsx

**Output:**
- Normalized assessment workbooks (with _normalized suffix if changes made)
- Validation report (text or Excel format)
- Issue summary for remediation

**Quality Checks Performed:**

Critical Issues (Must Fix Before Consolidation):
- Missing required sheets
- Incorrect sheet names
- Invalid data types in key columns
- Broken formulas
- Missing compliance scores

High Priority Issues (Should Fix):
- Incomplete assessments (missing data)
- Inconsistent dropdown values
- Missing evidence references
- Date format inconsistencies

Medium Priority Issues (Recommended Fix):
- Formatting inconsistencies
- Whitespace issues
- Non-standard terminology
- Missing optional fields

Low Priority Issues (Nice to Fix):
- Cosmetic formatting variations
- Optional field inconsistencies
- Documentation completeness

--------------------------------------------------------------------------------
REQUIREMENTS
--------------------------------------------------------------------------------

System Requirements:
    - Python 3.8 or higher
    - openpyxl library for Excel processing

Installation:
    Ubuntu/Debian:
        sudo apt install python3-openpyxl
    
    Or via pip:
        pip3 install openpyxl

Dependencies:
    - openpyxl (Python Excel library)
    - datetime (standard library)
    - os (standard library)
    - re (standard library - regex for validation)

--------------------------------------------------------------------------------
USAGE
--------------------------------------------------------------------------------

Basic Usage:
    # Validate all A.8.24 assessment files in current directory
    python3 normalize_assessment_files_a824.py

Advanced Usage:
    # Validate files in specific directory
    python3 normalize_assessment_files_a824.py --input-dir /path/to/assessments
    
    # Validate with automatic normalization
    python3 normalize_assessment_files_a824.py --normalize
    
    # Validate specific assessment domain only
    python3 normalize_assessment_files_a824.py --domain 1
    
    # Generate detailed validation report
    python3 normalize_assessment_files_a824.py --report detailed
    
    # Dry run mode (report issues without modifying files)
    python3 normalize_assessment_files_a824.py --dry-run
    
    # Specify output directory for normalized files
    python3 normalize_assessment_files_a824.py --normalize --output-dir /path/to/output

Command-Line Options:
    --input-dir PATH       Directory containing assessment workbooks
    --output-dir PATH      Directory for normalized workbooks (default: input-dir)
    --normalize            Apply normalization fixes automatically
    --domain N             Validate specific domain only (1-4)
    --report TYPE          Report format: summary|detailed|excel (default: summary)
    --dry-run              Validate only, don't modify files
    --severity LEVEL       Minimum severity to report: critical|high|medium|low
    --backup               Create backup before normalization (recommended)

Output Files:
    If --normalize used:
        - Original files: [filename]_backup_YYYYMMDD.xlsx (if --backup)
        - Normalized files: [filename] (updated in place) OR
        - Normalized files: [filename]_normalized.xlsx (if different output-dir)
    
    Validation report:
        - Console output (summary)
        - Text file: A824_Assessment_Validation_Report_YYYYMMDD.txt
        - Excel file: A824_Assessment_Validation_Report_YYYYMMDD.xlsx (if --report excel)

Workflow Examples:

    1. Initial validation (before consolidation):
       python3 normalize_assessment_files_a824.py --dry-run --report detailed
    
    2. Normalize and fix issues:
       python3 normalize_assessment_files_a824.py --normalize --backup
    
    3. Validate after normalization:
       python3 normalize_assessment_files_a824.py --severity high
    
    4. Generate audit-ready validation report:
       python3 normalize_assessment_files_a824.py --report excel

--------------------------------------------------------------------------------
METADATA
--------------------------------------------------------------------------------

Control Reference:    ISO/IEC 27001:2022 Annex A Control A.8.24
Utility Type:         Quality Assurance - Assessment Normalization & Validation
Framework Version:    1.0
Script Version:       1.0
Author:               [Developer Name / Organisation]
Date:                 [Date to be set]
Last Modified:        [Date to be set]
Python Version:       3.8+
License:              [Organisation License/Terms]

Related Documents:
    - ISMS-POL-A.8.24: Use of Cryptography Policy (Governance)
    - ISMS-IMP-A.8.24.1: Data Transmission Assessment (Domain 1)
    - ISMS-IMP-A.8.24.2: Data Storage Assessment (Domain 2)
    - ISMS-IMP-A.8.24.3: Authentication Assessment (Domain 3)
    - ISMS-IMP-A.8.24.4: Key Management Assessment (Domain 4)
    - ISMS-IMP-A.8.24.5: Compliance Dashboard (Consolidation)

Related Scripts:
    - generate_a824_1_data_transmission_assessment.py
    - generate_a824_2_data_storage_assessment.py
    - generate_a824_3_authentication_assessment.py
    - generate_a824_4_key_management_assessment.py
    - generate_a824_5_compliance_summary_dashboard.py
    - consolidate_a824_dashboard.py

--------------------------------------------------------------------------------
CHANGE HISTORY
--------------------------------------------------------------------------------

Version 1.0 - [Date to be set]
    - Initial release
    - Implements comprehensive validation framework
    - Supports automated normalization of all four assessment domains
    - Generates quality assurance reports for audit readiness

[Future changes to be documented here]

--------------------------------------------------------------------------------
IMPORTANT NOTES
--------------------------------------------------------------------------------

**Quality Assurance Philosophy:**
This script embodies "don't fool yourself" engineering - it catches the errors
humans make when filling out assessments, ensuring data quality before
consolidation. Think of it as your "Red Team" reviewer.

**Validation vs. Normalization:**
- Validation: Identifies issues without modifying files (--dry-run)
- Normalization: Automatically fixes issues where safe to do so (--normalize)
- Some issues require human judgment and cannot be auto-normalized

**Backup Recommendation:**
ALWAYS use --backup flag when normalizing files. Assessment workbooks contain
valuable data collection effort. Don't risk data loss.

**Pre-Consolidation Requirement:**
Run this script BEFORE consolidate_a824_dashboard.py to ensure clean input data.
Dashboard consolidation assumes normalized, validated assessment workbooks.

**Audit Considerations:**
Validation reports demonstrate quality assurance processes to auditors.
Keep validation reports as evidence of systematic quality control.

**Data Integrity:**
Script validates but does not alter actual assessment data values (e.g.,
compliance scores, technical findings). It only normalizes format and structure.
Technical accuracy remains assessor's responsibility.

**False Positives:**
Some validation warnings may be acceptable based on your specific context.
Review validation report and use judgment - don't blindly "fix" everything.

**Schema Changes:**
If you modify assessment workbook structures (add sheets, change columns),
update this script's validation rules accordingly. Out-of-sync validation
rules will generate false positives/negatives.

**Performance:**
Script processes Excel files in memory. For very large assessment workbooks
(>50MB), consider increasing available memory or processing files individually.

**Error Handling:**
Script continues processing all files even if one fails validation. Check
final summary for any files that couldn't be processed.

================================================================================
"""


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
Excel Workbook Sanity Checker - ISMS A.8.24 Assessment Workbooks
================================================================================

Diagnostic utility for troubleshooting Excel's "file level validation and repair"
warnings when opening A.8.24 cryptographic assessment workbooks.

**Purpose:**
Identifies common openpyxl-generated Excel issues that trigger repair warnings:
- Formula syntax errors and invalid sheet references
- Data validation conflicts and overlapping ranges
- Style attribute inconsistencies
- Merged cell content issues
- Worksheet structure problems

**When to Use:**
- Excel displays repair warnings when opening generated workbooks
- After modifying assessment generator scripts
- Before distributing workbooks to stakeholders
- Quality assurance validation before consolidation

**Usage:**
    python3 excel_sanity_check_a824.py ISMS_A_8_24_X_Assessment_YYYYMMDD.xlsx
    
    Works with any A.8.24 assessment workbook (domains 1-5)

**Output:**
- Diagnostic report with issue categorization (Critical/Warning)
- Recommended remediation actions
- Structural health summary

**Related Scripts:**
- excel_sanity_check_a824_1.py through _5.py (domain-specific checkers)
- excel_style_object_checker_a824.py (deep style analysis)
- excel_style_object_patcher_a824.py (automated style fixes)

Control Reference: ISO/IEC 27001:2022 Annex A Control A.8.24
Script Type: Quality Assurance Utility
Version: 1.0
================================================================================
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
Dashboard Data Consolidation Script - ISMS A.8.23 Web Filtering Framework
================================================================================

ISO/IEC 27001:2022 Control A.8.23: Web Filtering
Alternative Data Integration Method for Compliance Dashboard

--------------------------------------------------------------------------------
DATA CONSOLIDATION UTILITY - ALTERNATIVE TO EXTERNAL WORKBOOK LINKING
--------------------------------------------------------------------------------

This utility provides an alternative method for populating the A.8.23.5
Compliance Dashboard with data from source assessment workbooks (A.8.23.1
through A.8.23.4) by directly copying user-entered data rather than using
external workbook formula references.

**Primary Approach vs. Alternative Approach:**

**Primary (Recommended): External Workbook Formula Linking**
- Dashboard contains formulas like: ='[ISMS-IMP-A.8.23.1.xlsx]Gap_Analysis'!$B$15
- Data updates automatically when source files change
- Dashboard and source files must be in same directory
- Requires "Update Links" when opening dashboard
- Real-time data synchronization
- See: generate_a823_5_compliance_dashboard.py

**Alternative (This Script): Direct Data Consolidation**
- Reads data from source workbooks programmatically
- Copies data values (not formulas) into dashboard
- Creates static snapshot of compliance status
- Works with dashboard and sources in different locations
- Requires manual re-run when source data changes
- Useful when external links don't work or aren't desired

**When to Use This Script:**

1. **External Links Don't Work**
   - Excel security settings prevent external workbook links
   - SharePoint/OneDrive environments where linking fails
   - Email distribution requires self-contained workbooks
   - Recipient systems block external references

2. **Static Snapshots Required**
   - Monthly/quarterly compliance reporting archives
   - Board presentations requiring frozen data
   - Audit evidence packages with point-in-time data
   - Historical compliance tracking over time

3. **Simplified Distribution**
   - Single-file distribution to stakeholders
   - No dependency on source file availability
   - Recipients don't have access to source assessments
   - Reduced file size (no external references)

4. **Data Consolidation Flexibility**
   - Selective data inclusion from sources
   - Custom data transformation during consolidation
   - Multi-source aggregation and calculations
   - Data validation during import

**When NOT to Use This Script:**

- If external workbook linking works reliably → Use primary approach
- If real-time data updates are needed → Use external linking
- If dashboard and sources will always be co-located → Use external linking
- For initial dashboard setup → Use generate_a823_5_compliance_dashboard.py first

**Purpose:**
Reads user-entered data from all relevant sheets in the four normalized
assessment workbooks and writes consolidated data into corresponding
dashboard sheets, preserving the Executive Dashboard's external formulas
while populating detail sheets with actual assessment data.

**What It Does:**

1. **Validates Source Availability**
   - Checks all four normalized workbooks exist
   - Validates dashboard workbook is accessible
   - Reports missing files before attempting consolidation

2. **Reads Source Data**
   - Opens each source workbook in data-only mode
   - Reads user-entered data from configured sheets
   - Extracts relevant columns and rows per mapping
   - Skips empty rows and merged cell areas

3. **Consolidates into Dashboard**
   - Maps source sheets to target dashboard sheets
   - Writes data to appropriate dashboard locations
   - Adds source labels for traceability
   - Preserves existing dashboard structure

4. **Preserves Executive Dashboard**
   - Does NOT modify Executive Dashboard sheet
   - Retains external workbook formula references
   - Allows hybrid approach (formulas + consolidated data)

5. **Provides Consolidation Statistics**
   - Reports sheets processed and rows consolidated
   - Shows data distribution across dashboard sheets
   - Identifies any skipped or missing sheets

**Consolidation Mapping:**
The script uses a comprehensive mapping structure defining:
- Source workbook → Source sheet → Target dashboard sheet
- Starting row for data extraction
- Column ranges to include
- Source labels for traceability
- Data organization in dashboard

Example mapping:
```python
"wb1": {  # A.8.23.1 Infrastructure
    "Gap_Analysis": {
        "target": "Gap Analysis",          # Dashboard sheet
        "start_row": 10,                   # Begin reading at row 10
        "columns": "A:R",                  # Include columns A through R
        "label": "Domain 1: Infrastructure"  # Source identifier
    },
    ...
}
```

**Supported Source Workbooks:**
- ISMS-IMP-A.8.23.1.xlsx (Filtering Infrastructure Assessment)
- ISMS-IMP-A.8.23.2.xlsx (Network Coverage Assessment)
- ISMS-IMP-A.8.23.3.xlsx (Policy Configuration Assessment)
- ISMS-IMP-A.8.23.4.xlsx (Monitoring & Response Assessment)

These are the normalized file names created by normalize_assessment_files_a823.py

**Target Dashboard Sheets:**
- Gap Analysis (consolidated gaps from all 4 domains)
- Evidence Register (consolidated evidence from all 4 domains)
- Risk Register (risk assessments from domains 1, 3)
- KPIs & Metrics (performance metrics from domains 1, 2, 4)
- Audit & Compliance Log (detailed assessment data)
- Action Items & Follow-up (exceptions, alerts, follow-up items)

**Executive Dashboard Sheet:**
- NOT modified by this script
- Retains external workbook formula references
- Pulls summary metrics from other dashboard sheets
- Allows hybrid linking + consolidation approach

--------------------------------------------------------------------------------
USAGE
--------------------------------------------------------------------------------

**Basic Usage:**
    python3 consolidate_a823_dashboard.py ISMS-IMP-A.8.23.5_Compliance_Dashboard_20250124.xlsx

**Prerequisites:**
    1. Generate dashboard first:
       python3 generate_a823_5_compliance_dashboard.py
    
    2. Normalize source assessment files:
       python3 normalize_assessment_files_a823.py
    
    3. Ensure all files are accessible:
       - ISMS-IMP-A.8.23.1.xlsx
       - ISMS-IMP-A.8.23.2.xlsx
       - ISMS-IMP-A.8.23.3.xlsx
       - ISMS-IMP-A.8.23.4.xlsx
       - Dashboard file (provided as argument)

**File Location Requirements:**
    Source workbooks must be in CURRENT DIRECTORY when running script:
    - ISMS-IMP-A.8.23.1.xlsx (in current directory)
    - ISMS-IMP-A.8.23.2.xlsx (in current directory)
    - ISMS-IMP-A.8.23.3.xlsx (in current directory)
    - ISMS-IMP-A.8.23.4.xlsx (in current directory)
    
    Dashboard can be in any directory (specify full path if needed)

**Example Session:**
    $ python3 consolidate_a823_dashboard.py ISMS-IMP-A.8.23.5_Dashboard_20250124.xlsx
    ================================================================================
    ISMS A.8.23 - DASHBOARD DATA CONSOLIDATION
    ================================================================================
    
    Dashboard: ISMS-IMP-A.8.23.5_Dashboard_20250124.xlsx
    Started: 2025-01-24 14:30:15
    
    Checking source workbooks...
      ✅ ISMS-IMP-A.8.23.1.xlsx
      ✅ ISMS-IMP-A.8.23.2.xlsx
      ✅ ISMS-IMP-A.8.23.3.xlsx
      ✅ ISMS-IMP-A.8.23.4.xlsx
    
    Loading dashboard...
      ✅ Dashboard loaded (10 sheets)
    
    ================================================================================
    CONSOLIDATING DATA FROM SOURCE WORKBOOKS
    ================================================================================
    
    📁 Processing: ISMS-IMP-A.8.23.1.xlsx
      ✅ Gap_Analysis → Gap Analysis: 12 rows
      ✅ Evidence_Register → Evidence Register: 8 rows
      ✅ Solution_Details_Template → Audit & Compliance Log: 3 rows
      [... additional sheets ...]
    
    📁 Processing: ISMS-IMP-A.8.23.2.xlsx
      ✅ Gap_Identification → Gap Analysis: 5 rows
      [... additional sheets ...]
    
    [... processing workbooks 3 and 4 ...]
    
    ================================================================================
    SAVING CONSOLIDATED DASHBOARD
    ================================================================================
    ✅ Dashboard saved successfully
    
    ================================================================================
    CONSOLIDATION COMPLETE
    ================================================================================
    
    📊 Statistics:
      • Source sheets read: 34
      • Total rows consolidated: 247
    
    📋 By Dashboard Sheet:
      • Action Items & Follow-up: 28 rows
      • Audit & Compliance Log: 89 rows
      • Evidence Register: 31 rows
      • Gap Analysis: 44 rows
      • KPIs & Metrics: 38 rows
      • Risk Register: 17 rows
    
    ✅ Completed: 2025-01-24 14:30:42
    
    ================================================================================
    🎯 Dashboard now contains all user-entered data from assessments!
       Open in Excel and click 'Update Links' to refresh formulas.
    ================================================================================

**Exit Codes:**
    0 = Consolidation successful
    1 = Consolidation failed (missing files, errors during processing)

**Re-Running Consolidation:**
    Safe to re-run this script when assessment data is updated:
    - Existing dashboard data will be overwritten
    - Updated source data will be consolidated
    - Statistics will reflect new data volumes
    - No data loss in source workbooks (read-only access)

**Workflow Integration:**

    **Initial Setup (One-Time):**
    1. Generate dashboard: python3 generate_a823_5_compliance_dashboard.py
    2. Normalize assessments: python3 normalize_assessment_files_a823.py
    3. Consolidate data: python3 consolidate_a823_dashboard.py dashboard.xlsx
    
    **Monthly/Quarterly Updates:**
    1. Update source assessments with new data
    2. Re-normalize (if file names changed): python3 normalize_assessment_files_a823.py
    3. Re-consolidate: python3 consolidate_a823_dashboard.py dashboard.xlsx
    
    **Static Snapshot Creation:**
    1. Run consolidation with date-stamped dashboard name
    2. Archive consolidated dashboard for reporting period
    3. Create new dashboard for next period

--------------------------------------------------------------------------------
REQUIREMENTS
--------------------------------------------------------------------------------

System Requirements:
    - Python 3.8 or higher
    - openpyxl library for Excel manipulation

Installation:
    Ubuntu/Debian:
        sudo apt install python3-openpyxl
    
    Or via pip:
        pip3 install openpyxl

Dependencies:
    - openpyxl (Excel file reading and writing)
    - sys, os (standard library)
    - datetime (standard library)

**Required Files:**
    - Four normalized assessment workbooks (A.8.23.1 through A.8.23.4)
    - Generated dashboard workbook (A.8.23.5)
    - This consolidation script

**File Naming:**
    Source workbooks MUST be named exactly:
    - ISMS-IMP-A.8.23.1.xlsx
    - ISMS-IMP-A.8.23.2.xlsx
    - ISMS-IMP-A.8.23.3.xlsx
    - ISMS-IMP-A.8.23.4.xlsx
    
    Dashboard can have any name (passed as command-line argument)

--------------------------------------------------------------------------------
CONSOLIDATION MAPPING STRUCTURE
--------------------------------------------------------------------------------

**How It Works:**
The script uses a detailed mapping dictionary (CONSOLIDATION_MAP) that defines
which data to extract from which source sheets and where to place it in the
dashboard.

**Mapping Components:**

1. **Source Workbook Key** (wb1, wb2, wb3, wb4)
   - Maps to normalized assessment file names
   - wb1 = ISMS-IMP-A.8.23.1.xlsx (Infrastructure)
   - wb2 = ISMS-IMP-A.8.23.2.xlsx (Network Coverage)
   - wb3 = ISMS-IMP-A.8.23.3.xlsx (Policy Configuration)
   - wb4 = ISMS-IMP-A.8.23.4.xlsx (Monitoring & Response)

2. **Source Sheet Name**
   - Exact sheet name in source workbook
   - Examples: Gap_Analysis, Evidence_Register, Threat_Protection

3. **Target Dashboard Sheet**
   - Destination sheet in dashboard workbook
   - Examples: Gap Analysis, Risk Register, KPIs & Metrics

4. **Start Row**
   - Row number to begin reading data (typically row 10)
   - Skips headers and instructions

5. **Column Range**
   - Columns to include (e.g., "A:R" includes columns A through R)
   - Defines data width for each source

6. **Source Label**
   - Descriptive label added to consolidated data
   - Enables traceability back to source domain

**Total Mapped Sources:**
- Domain 1 (Infrastructure): 8 source sheets → 4 dashboard sheets
- Domain 2 (Network Coverage): 7 source sheets → 4 dashboard sheets
- Domain 3 (Policy Configuration): 9 source sheets → 3 dashboard sheets
- Domain 4 (Monitoring & Response): 9 source sheets → 4 dashboard sheets
- Total: 33 source sheets consolidated into 6 dashboard sheets

**Customization:**
To modify consolidation behavior, edit CONSOLIDATION_MAP dictionary:
- Add/remove source sheets
- Change target dashboard sheets
- Adjust column ranges
- Modify source labels
- Change starting rows

--------------------------------------------------------------------------------
DATA CONSOLIDATION PROCESS
--------------------------------------------------------------------------------

**Step-by-Step Process:**

1. **Validation Phase**
   - Verify dashboard file exists and is accessible
   - Check all four source workbooks are present
   - Report any missing files before proceeding

2. **Dashboard Loading**
   - Open dashboard workbook in read-write mode
   - Validate expected sheets exist
   - Prepare for data consolidation

3. **Source Processing Loop**
   For each source workbook (A.8.23.1 through A.8.23.4):
   
   a. Open source workbook in data-only mode (values, not formulas)
   b. For each configured source sheet:
      - Locate source sheet by name
      - Read data starting from specified row
      - Extract specified column range
      - Stop at first completely empty row
      - Skip merged cell areas safely
   
   c. For each extracted data block:
      - Locate target dashboard sheet
      - Find first available row for writing
      - Add source label for traceability
      - Write data values (not formulas)
      - Track consolidation statistics

4. **Dashboard Preservation**
   - Executive Dashboard sheet is NOT modified
   - External formula references remain intact
   - Hybrid approach maintained (formulas + consolidated data)

5. **Save and Report**
   - Save modified dashboard workbook
   - Generate consolidation statistics
   - Report data distribution across dashboard sheets
   - Provide completion timestamp

**Data Handling:**
- Source workbooks opened in data-only mode (formulas evaluated to values)
- Empty rows terminate data extraction for each source
- Merged cells are safely skipped (no write attempts)
- Existing dashboard data is overwritten on re-consolidation
- Source workbooks remain unmodified (read-only access)

**Error Handling:**
- Missing source files reported before consolidation starts
- Missing source sheets logged but don't stop consolidation
- Missing target sheets logged and skipped
- Cell write errors caught and logged
- Dashboard save failures reported with error details

--------------------------------------------------------------------------------
INTEGRATION WITH A.8.23 FRAMEWORK
--------------------------------------------------------------------------------

**Position in Workflow:**

This script provides an ALTERNATIVE data integration method. The standard
workflow uses external workbook formula linking. This consolidation approach
is used when external linking isn't suitable or desired.

**Standard Workflow (External Linking - Recommended):**
```
Assessments → Normalization → Dashboard Generation → Link Update → Distribution
(A.8.23.1-4)     (normalize)      (generate_a823_5)    (Excel)    (Stakeholders)
```

**Alternative Workflow (Data Consolidation - This Script):**
```
Assessments → Normalization → Dashboard Generation → Data Consolidation → Distribution
(A.8.23.1-4)     (normalize)      (generate_a823_5)   (this script)   (Stakeholders)
                                                             ↓
                                                    Static Snapshot
```

**Hybrid Workflow (Combined Approach):**
```
Assessments → Normalization → Dashboard Generation → Link Update + Consolidation
(A.8.23.1-4)     (normalize)      (generate_a823_5)        (Both)
                                                             ↓
                                              Exec formulas + Detail data
```

**Related Scripts:**
- generate_a823_1_filtering_infrastructure.py (creates A.8.23.1)
- generate_a823_2_network_coverage.py (creates A.8.23.2)
- generate_a823_3_policy_configuration.py (creates A.8.23.3)
- generate_a823_4_monitoring_response.py (creates A.8.23.4)
- normalize_assessment_files_a823.py (normalizes file names)
- generate_a823_5_compliance_dashboard.py (creates dashboard)
- sanity_check_a823_dashboard.py (pre-flight check)
- excel_sanity_check_a823.py (workbook validation)

**Comparison: External Linking vs. Data Consolidation**

| Aspect | External Linking | Data Consolidation |
|--------|------------------|-------------------|
| **Setup** | One-time generation | Generate + consolidate |
| **Updates** | Automatic (Excel refresh) | Manual re-run required |
| **File Dependency** | Must be co-located | Can be separate |
| **Distribution** | Requires source files | Self-contained |
| **Excel Security** | May be blocked | Always works |
| **Historical Tracking** | Overwrites data | Create dated snapshots |
| **Data Type** | Live formulas | Static values |
| **Use Case** | Real-time reporting | Point-in-time reporting |

--------------------------------------------------------------------------------
METADATA
--------------------------------------------------------------------------------

Control Reference:    ISO/IEC 27001:2022 Annex A Control A.8.23
Script Type:          Data Consolidation / Alternative Integration Method
Framework Component:  A.8.23.5 Compliance Dashboard Support
Framework Version:    1.0
Script Version:       1.0
Author:               [Developer Name / Organisation]
Date:                 [Date to be set]
Last Modified:        [Date to be set]
Python Version:       3.8+
License:              [Organisation License/Terms]

Input Files:
    - ISMS-IMP-A.8.23.1.xlsx (Filtering Infrastructure Assessment)
    - ISMS-IMP-A.8.23.2.xlsx (Network Coverage Assessment)
    - ISMS-IMP-A.8.23.3.xlsx (Policy Configuration Assessment)
    - ISMS-IMP-A.8.23.4.xlsx (Monitoring & Response Assessment)
    - Dashboard workbook (ISMS-IMP-A.8.23.5_*.xlsx)

Output:
    - Modified dashboard workbook with consolidated data
    - Console statistics showing consolidation results

Related Quality Tools:
    - normalize_assessment_files_a823.py (file preparation)
    - generate_a823_5_compliance_dashboard.py (dashboard creation)
    - excel_sanity_check_a823.py (workbook validation)

--------------------------------------------------------------------------------
CHANGE HISTORY
--------------------------------------------------------------------------------

Version 1.0 - [Date to be set]
    - Initial release
    - Comprehensive consolidation mapping for all 4 assessment domains
    - 33 source sheets → 6 dashboard sheets
    - Preserves Executive Dashboard external formulas
    - Safe merged cell handling
    - Detailed consolidation statistics

[Future changes to be documented here]

--------------------------------------------------------------------------------
IMPORTANT NOTES
--------------------------------------------------------------------------------

**File Modification:**
- Source workbooks are read in data-only mode (NOT modified)
- Dashboard workbook IS modified (data written to detail sheets)
- Executive Dashboard sheet is NOT modified (formulas preserved)
- Always backup dashboard before first consolidation

**Re-Running Consolidation:**
- Safe to re-run when source data is updated
- Existing consolidated data is overwritten
- No cumulative effect (fresh consolidation each time)
- Statistics reflect current consolidation only

**Source File Requirements:**
- Must use EXACT normalized file names
- Must be in current directory when running script
- Must be readable .xlsx format (not .xls or .xlsm)
- Must contain expected sheet names from mapping

**Dashboard Requirements:**
- Must be generated by generate_a823_5_compliance_dashboard.py
- Must contain expected target sheet names
- Must be writable (not read-only or open in Excel)
- Should be backed up before first consolidation

**Mapping Maintenance:**
- CONSOLIDATION_MAP must match actual assessment sheet names
- Changing assessment structures requires mapping updates
- Adding custom sheets requires mapping additions
- Verify mapping after generator script modifications

**Performance:**
- Typical consolidation time: 10-30 seconds
- Depends on data volume in source workbooks
- Progress is displayed for each source workbook
- Large datasets (1000+ rows) may take longer

**Limitations:**
- Does not preserve formulas from source workbooks
- Does not copy cell formatting or styles
- Does not handle Excel tables or charts
- Does not validate data during consolidation
- Assumes source data is already validated

**Best Practices:**
1. Complete source assessments before consolidation
2. Run normalization script before consolidation
3. Validate source workbooks with excel_sanity_check_a823.py
4. Backup dashboard before first consolidation
5. Review consolidation statistics after each run
6. Test hybrid approach (formulas + consolidation) in dev first
7. Document when/why consolidation approach is used vs. external linking

**Troubleshooting Common Issues:**

**Issue: "ERROR: Dashboard file not found"**
Solution: Verify dashboard path is correct, check file exists

**Issue: "MISSING: ISMS-IMP-A.8.23.N.xlsx"**
Solution: Run normalize_assessment_files_a823.py to create normalized files

**Issue: "Sheet 'X' not found, skipping"**
Solution: Source workbook missing expected sheet, check assessment generator

**Issue: "Target sheet 'X' not in dashboard, skipping"**
Solution: Dashboard missing expected sheet, regenerate dashboard

**Issue: "No data" for multiple sheets**
Solution: Source workbooks may be empty or data in unexpected location

**Issue: "ERROR saving dashboard"**
Solution: Dashboard may be open in Excel, close it before consolidation

**Audit Considerations:**
- Consolidation creates static point-in-time snapshot
- Consolidation timestamp is recorded in statistics
- Source data traceability via source labels
- Useful for monthly/quarterly compliance reporting archives
- Executive Dashboard formulas still provide real-time if links enabled

**Data Protection:**
- Consolidated dashboard inherits data classification from sources
- Source workbooks remain unmodified and unaffected
- Dashboard may contain aggregated sensitive compliance data
- Handle according to organization's data classification policy

**Alternative to This Script:**
If external workbook linking works reliably in your environment, consider
using the standard approach (generate dashboard + enable "Update Links")
instead of data consolidation for automatic updates and reduced maintenance.

================================================================================
END OF HEADER - SCRIPT CODE FOLLOWS
================================================================================
"""