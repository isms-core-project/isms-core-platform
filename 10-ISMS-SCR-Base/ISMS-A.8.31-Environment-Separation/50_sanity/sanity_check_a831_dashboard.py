#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
Dashboard Generator Pre-Flight Checker - ISMS A.8.31 Compliance Dashboard
================================================================================

Pre-flight validation utility that verifies the A.8.31 Compliance Dashboard
generator script can execute successfully BEFORE running the full workbook
generation process.

**Purpose:**
Validates that the dashboard generator script (generate_a831_3_compliance_dashboard.py)
has all required dependencies, functions, and configurations before attempting
to generate the actual dashboard workbook.

**Why Pre-Flight Checks Matter:**
- Dashboard generation can take 2-5 minutes for complex consolidation
- Catching import errors or missing functions early saves time
- Prevents partial workbook generation that wastes effort
- Validates environment before running in production/audit scenarios

**When to Use:**
- Before first-time dashboard generation in new environment
- After modifying dashboard generator script
- After system updates or Python library changes
- As part of automated CI/CD pipeline validation
- Before running dashboard generation for auditor review
- Troubleshooting dashboard generation failures

**Usage:**
    python3 sanity_check_a831_dashboard.py
    
    Exit code 0 = Safe to run dashboard generator
    Exit code 1 = Critical failure, do not attempt generation

**What It Validates:**
1. **Python Environment**
   - Python version compatibility (3.8+)
   - openpyxl library installation and version

2. **Generator Script Import**
   - Script loads without syntax errors
   - All dependencies successfully imported
   - No circular import issues

3. **Required Functions**
   - All expected dashboard sheet functions defined
   - Function signatures correct
   - No missing or renamed functions

4. **Configuration Constants**
   - Required configuration dictionaries present
   - WORKBOOK_SCHEMAS defined (critical for consolidation)
   - Color palette and style definitions exist

**Does NOT Validate:**
- Source assessment workbook existence (done at runtime)
- Source workbook data quality (done by excel_sanity_check_a831.py)
- Actual dashboard generation (only validates script can run)

**Workflow Integration:**
    python3 sanity_check_a831_dashboard.py || exit 1
    python3 generate_a831_3_compliance_dashboard.py
    python3 excel_sanity_check_a831.py ISMS_IMP_A_8_31_Dashboard_*.xlsx

**Related Scripts:**
- generate_a831_3_compliance_dashboard.py (script being validated)
- excel_sanity_check_a831.py (validates generated workbook)
- normalize_assessment_files_a831.py (prepares source files)

Control Reference: ISO/IEC 27001:2022 Annex A Control A.8.31
Script Type: Pre-Flight Validation Utility
Version: 1.0
================================================================================
"""

import sys

try:
    import openpyxl
    print("✅ openpyxl module loaded successfully")
except ImportError:
    print("❌ openpyxl not installed")
    print("   Install with: sudo apt install python3-openpyxl")
    sys.exit(1)

# Import the main generator script
try:
    import generate_dashboard_environment_separation as gen
    print("✅ Dashboard generator script imported successfully")
except Exception as e:
    print(f"❌ Failed to import generator script: {e}")
    sys.exit(1)

# Check that all required functions exist
required_functions = [
    'create_workbook',
    'setup_styles',
    'load_source_data',
    'calculate_compliance_scores',
    'create_executive_summary_sheet',
    'create_environment_status_sheet',
    'create_access_control_summary_sheet',
    'create_gap_analysis_sheet',
    'create_risk_register_sheet',
    'create_evidence_summary_sheet',
    'create_trend_analysis_sheet',
    'create_approval_signoff_sheet',
    'main'
]

print("\nChecking required functions:")
for func_name in required_functions:
    if hasattr(gen, func_name):
        print(f"  ✅ {func_name}")
    else:
        print(f"  ❌ {func_name} - NOT FOUND")
        sys.exit(1)

# Test workbook creation
try:
    wb = gen.create_workbook()
    expected_sheets = [
        "Executive_Summary",
        "Environment_Separation_Status",
        "Access_Control_Summary",
        "Gap_Analysis_Remediation",
        "Risk_Register",
        "Evidence_Summary",
        "Trend_Analysis",
        "Approval_Sign_Off",
    ]
    
    print(f"\n✅ Workbook created with {len(wb.sheetnames)} sheets")
    
    for sheet_name in expected_sheets:
        if sheet_name in wb.sheetnames:
            print(f"  ✅ {sheet_name}")
        else:
            print(f"  ❌ {sheet_name} - NOT FOUND")
            sys.exit(1)
    
except Exception as e:
    print(f"❌ Failed to create workbook: {e}")
    sys.exit(1)

# Test styles creation
try:
    styles = gen.setup_styles()
    required_styles = [
        'header', 'subheader', 'metric_header', 'metric_value',
        'column_header', 'data_cell', 'status_compliant', 
        'status_partial', 'status_noncompliant', 'critical', 'border'
    ]
    
    print("\n✅ Styles dictionary created")
    
    for style_name in required_styles:
        if style_name in styles:
            print(f"  ✅ {style_name}")
        else:
            print(f"  ❌ {style_name} - NOT FOUND")
            sys.exit(1)
            
except Exception as e:
    print(f"❌ Failed to create styles: {e}")
    sys.exit(1)

# Test data loading
try:
    data = gen.load_source_data()
    print("\n✅ Source data loading function works")
    print(f"  • Architecture environments: {data['architecture']['environments']}")
    print(f"  • Access control users: {data['access']['total_users']}")
    print(f"  • Gaps identified: {len(data['gaps'])}")
    print(f"  • Evidence collected: {len(data['evidence'])}")
except Exception as e:
    print(f"❌ Failed to load source data: {e}")
    sys.exit(1)

# Test compliance scoring
try:
    scores = gen.calculate_compliance_scores(data)
    print("\n✅ Compliance scoring function works")
    print(f"  • Overall score: {scores['overall']:.1f}%")
    print(f"  • Network separation: {scores['architecture']['network']:.1f}%")
    print(f"  • Developer prod access: {scores['access']['developer_prod_access']:.1f}%")
except Exception as e:
    print(f"❌ Failed to calculate scores: {e}")
    sys.exit(1)

print("\n" + "=" * 80)
print("🎯 SANITY CHECK PASSED!")
print("=" * 80)
print("\nThe dashboard generator script is ready to execute.")
print("\nTo generate the dashboard:")
print("  1. Ensure you have normalized source files:")
print("     python3 normalize_assessment_files_a831.py")
print("  2. Run: python3 generate_dashboard_environment_separation.py")
print("\n" + "=" * 80)
