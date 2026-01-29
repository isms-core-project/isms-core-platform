# ISMS A.8.24 - Use of Cryptography Assessment Workflow
# Command Reference Guide

## File Naming Convention
All generated workbooks use format: `ISMS_A_8_24_[N]_[Description]_Assessment_YYYYMMDD.xlsx`
Where [N] is domain number (1-5) and YYYYMMDD is generation date.

---

## PHASE 1: Generate Assessment Workbooks

### Option A: Generate Individual Workbooks
```bash
# Domain 1: Data Transmission Cryptography
python3 generate_a824_1_data_transmission_assessment.py

# Domain 2: Data Storage Cryptography
python3 generate_a824_2_data_storage_assessment.py

# Domain 3: Authentication Cryptography
python3 generate_a824_3_authentication_assessment.py

# Domain 4: Key Management
python3 generate_a824_4_key_management_assessment.py

# Domain 5: Compliance Dashboard (template)
python3 generate_a824_5_compliance_summary_dashboard.py
```

### Option B: Complete Workflow (Automated)
```bash
# Generate all workbooks in one command
python3 complete_workflow_824.py

# Or with options
python3 complete_workflow_824.py --verbose --backup --interactive
```

**Expected Output Files:**
- `ISMS_A_8_24_1_Data_Transmission_Assessment_YYYYMMDD.xlsx`
- `ISMS_A_8_24_2_Data_Storage_Assessment_YYYYMMDD.xlsx`
- `ISMS_A_8_24_3_Authentication_Assessment_YYYYMMDD.xlsx`
- `ISMS_A_8_24_4_Key_Management_Assessment_YYYYMMDD.xlsx`
- `ISMS_A_8_24_5_Compliance_Dashboard_YYYYMMDD.xlsx`

---

## PHASE 2: Quality Assurance - General Health Checks

### Generic Sanity Checker (Works for Any A.8.24 Workbook)
```bash
python3 excel_sanity_check_a824.py ISMS_A_8_24_1_Data_Transmission_Assessment_20250124.xlsx
python3 excel_sanity_check_a824.py ISMS_A_8_24_2_Data_Storage_Assessment_20250124.xlsx
python3 excel_sanity_check_a824.py ISMS_A_8_24_3_Authentication_Assessment_20250124.xlsx
python3 excel_sanity_check_a824.py ISMS_A_8_24_4_Key_Management_Assessment_20250124.xlsx
python3 excel_sanity_check_a824.py ISMS_A_8_24_5_Compliance_Dashboard_20250124.xlsx
```

### Domain-Specific Health Checks (Recommended)
```bash
# More thorough validation for specific assessment types
python3 excel_sanity_check_a824_1.py ISMS_A_8_24_1_Data_Transmission_Assessment_20250124.xlsx
python3 excel_sanity_check_a824_2.py ISMS_A_8_24_2_Data_Storage_Assessment_20250124.xlsx
python3 excel_sanity_check_a824_3.py ISMS_A_8_24_3_Authentication_Assessment_20250124.xlsx
python3 excel_sanity_check_a824_4.py ISMS_A_8_24_4_Key_Management_Assessment_20250124.xlsx
python3 excel_sanity_check_a824_5.py ISMS_A_8_24_5_Compliance_Dashboard_20250124.xlsx
```

---

## PHASE 3: Deep Diagnostics (If Issues Found)

### Style Object Analysis
```bash
# Deep inspection of style objects
python3 excel_style_object_checker_a824.py ISMS_A_8_24_1_Data_Transmission_Assessment_20250124.xlsx

# Save detailed report to file
python3 excel_style_object_checker_a824.py ISMS_A_8_24_1_Data_Transmission_Assessment_20250124.xlsx > style_report.txt
```

### Style Object Repair
```bash
# 1. DRY RUN - Preview fixes without applying
python3 excel_style_object_patcher_a824.py --dry-run ISMS_A_8_24_1_Data_Transmission_Assessment_20250124.xlsx

# 2. APPLY FIXES - With automatic backup
python3 excel_style_object_patcher_a824.py --backup ISMS_A_8_24_1_Data_Transmission_Assessment_20250124.xlsx

# 3. APPLY FIXES - Without backup (NOT recommended for production)
python3 excel_style_object_patcher_a824.py ISMS_A_8_24_1_Data_Transmission_Assessment_20250124.xlsx
```

---

## PHASE 4: Stakeholder Assessment Completion

**MANUAL PHASE**: Distribute workbooks to stakeholders for completion
- Technical teams complete Domains 1-4
- Evidence collection and documentation
- SME validation of technical assessments

---

## PHASE 5: Pre-Consolidation Validation

### Normalize Assessment Files
```bash
# Validate all assessments before consolidation
python3 normalize_assessment_files_a824.py --dry-run --report detailed

# Apply normalization with backup
python3 normalize_assessment_files_a824.py --normalize --backup

# Validate specific domain only
python3 normalize_assessment_files_a824.py --domain 1 --dry-run
```

**Validates:**
- File naming conventions
- Workbook structure consistency
- Data format normalization
- Evidence linkage completeness
- Formula integrity

---

## PHASE 6: Dashboard Consolidation

### Consolidate Assessments into Dashboard
```bash
# Auto-detect and consolidate all assessments
python3 consolidate_a824_dashboard.py

# Dry run - validate without writing
python3 consolidate_a824_dashboard.py --dry-run --verbose

# Production consolidation with backup
python3 consolidate_a824_dashboard.py --backup --pdf

# Incremental update (preserve manual edits)
python3 consolidate_a824_dashboard.py --incremental

# Specify input/output directories explicitly
python3 consolidate_a824_dashboard.py \
    --input-dir /path/to/assessments \
    --output-dir /path/to/dashboard
```

**Output:**
- `ISMS_A_8_24_5_Compliance_Dashboard_YYYYMMDD.xlsx` (populated)
- `A824_Dashboard_Consolidation_Log_YYYYMMDD.txt`
- `A824_Executive_Summary_YYYYMMDD.pdf` (if --pdf used)

---

## COMPLETE WORKFLOW AUTOMATION

### Full Lifecycle (Generation → Consolidation)
```bash
# First run: Generate workbooks
python3 complete_workflow_824.py --verbose --backup --interactive

# [MANUAL PHASE: Complete assessments]

# Second run: Normalize and consolidate
python3 complete_workflow_824.py --incremental --pdf-summary --notify-email ciso@example.com
```

### Quarterly Reassessment
```bash
# Skip generation, update existing assessments
python3 complete_workflow_824.py --incremental --backup
```

### Pre-Audit Validation
```bash
# Comprehensive validation without execution
python3 complete_workflow_824.py --validate-only --verbose
```

### Testing Before Production
```bash
# Simulate entire workflow
python3 complete_workflow_824.py --dry-run --verbose
```

---

## DIAGNOSTIC WORKFLOW (When Excel Shows Repair Warnings)
```bash
# Step 1: General validation
python3 excel_sanity_check_a824.py problematic_workbook.xlsx

# Step 2: If style issues found, deep analysis
python3 excel_style_object_checker_a824.py problematic_workbook.xlsx

# Step 3: Preview fixes
python3 excel_style_object_patcher_a824.py --dry-run problematic_workbook.xlsx

# Step 4: Apply fixes with backup
python3 excel_style_object_patcher_a824.py --backup problematic_workbook.xlsx

# Step 5: Re-validate
python3 excel_sanity_check_a824.py problematic_workbook.xlsx
```

---

## COMMON WORKFLOWS

### Initial Implementation (First Time)
```bash
# 1. Generate all workbooks
python3 complete_workflow_824.py --verbose --backup

# 2. Quality check before distribution
python3 excel_sanity_check_a824_1.py ISMS_A_8_24_1_*.xlsx
python3 excel_sanity_check_a824_2.py ISMS_A_8_24_2_*.xlsx
python3 excel_sanity_check_a824_3.py ISMS_A_8_24_3_*.xlsx
python3 excel_sanity_check_a824_4.py ISMS_A_8_24_4_*.xlsx

# 3. [Distribute to stakeholders for completion]

# 4. Normalize completed assessments
python3 normalize_assessment_files_a824.py --normalize --backup

# 5. Consolidate into dashboard
python3 consolidate_a824_dashboard.py --backup --pdf
```

### Quarterly Update (Existing Assessments)
```bash
# 1. [Update assessment workbooks with new data]

# 2. Normalize updates
python3 normalize_assessment_files_a824.py --normalize

# 3. Re-consolidate
python3 consolidate_a824_dashboard.py --incremental --pdf
```

### Pre-Audit Preparation
```bash
# Comprehensive validation
python3 complete_workflow_824.py --validate-only --verbose

# Generate fresh consolidated report
python3 consolidate_a824_dashboard.py --pdf
```

---

## TROUBLESHOOTING COMMANDS

### Check All Generated Files
```bash
ls -lh ISMS_A_8_24_*.xlsx
```

### Validate Script Availability
```bash
ls -1 *.py | grep -E "(generate|normalize|consolidate|excel_|complete)"
```

### Clean Up Old Backups
```bash
# List backups
ls -lh *_backup_*.xlsx

# Remove backups older than 30 days (CAREFUL!)
find . -name "*_backup_*.xlsx" -mtime +30 -delete
```

### Find Latest Assessment Files
```bash
# Find most recent workbooks
ls -lt ISMS_A_8_24_*_Assessment_*.xlsx | head -5
```

---

## EXIT CODES

All scripts use standard exit codes:
- `0` - Success
- `1` - Validation failure
- `2` - Data/execution error
- `3` - Consolidation error
- `4` - File I/O error
- `5` - Configuration error
- `10` - Quality gate halt (user declined to continue)

Check exit code:
```bash
python3 normalize_assessment_files_a824.py --dry-run
echo $?  # Shows exit code
```

---

## NOTES

**Date Format**: All dates in filenames use `YYYYMMDD` format (e.g., 20250124)

**Sudo**: Generally NOT needed for Python scripts unless writing to protected directories

**Backup Strategy**: Always use `--backup` flag for production workbooks

**Quality Gates**: Don't override quality gate warnings with `--continue-on-warning` unless you understand the risks

**Audit Trail**: Keep all workflow logs and validation reports for ISO 27001 audit evidence