#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
Excel Sanity Checker - A.8.24.X [Domain Name] Assessment Workbook
================================================================================

SPECIALIZED diagnostic for [Data Transmission/Data Storage/Authentication/
Key Management/Compliance Dashboard] assessment workbooks.

**Purpose:**
Domain-specific validation tailored to the unique structure and requirements
of A.8.24.X assessment workbooks.

**Checks Performed:**
- Domain-specific sheet structure validation
- Formula integrity for domain-specific calculations
- Data validation rules specific to this assessment type
- [Domain-specific validation logic]

**When to Use:**
- After generating A.8.24.X assessment workbook
- Before stakeholder distribution
- When Excel shows repair warnings for this specific domain

**Usage:**
    python3 excel_sanity_check_a824_X.py ISMS_A_8_24_X_Assessment_YYYYMMDD.xlsx

**Differences from General Checker:**
This specialized checker validates domain-specific requirements that the
general checker cannot verify (custom sheet structures, domain-specific
formulas, assessment-specific data validation rules).

Control Reference: ISO/IEC 27001:2022 Annex A Control A.8.24
Assessment Domain: [X] of 4 ([Domain Name])
Script Type: Domain-Specific QA Utility
Version: 1.0
================================================================================
"""

import sys
import re
from openpyxl import load_workbook
from openpyxl.utils import get_column_letter


# ============================================================================
# A.8.24.5 SPECIFIC VALIDATION DATA
# ============================================================================

EXPECTED_SHEETS = [
    "Executive Dashboard",
    "Gap Analysis",
    "Risk Register",
    "Remediation Roadmap",
    "KPIs & Metrics",
    "Evidence Register",
    "Action Items & Follow-up",
    "Audit & Compliance Log",
    "Approval Sign-Off",
]

REQUIRED_DOCUMENT_INFO = [
    "Document ID",
    "Report Type",
    "Related Policy",
    "Version",
]

# Expected source workbooks for external links
EXPECTED_SOURCE_WORKBOOKS = [
    "ISMS-IMP-A.8.24.1.xlsx",
    "ISMS-IMP-A.8.24.2.xlsx",
    "ISMS-IMP-A.8.24.3.xlsx",
    "ISMS-IMP-A.8.24.4.xlsx",
]

# Expected data row counts per sheet
EXPECTED_DATA_ROWS = {
    "Gap Analysis": 200,          # Detailed gap register
    "Risk Register": 100,         # Detailed risk register
    "Remediation Roadmap": 200,   # Detailed remediation register
    "Evidence Register": 500,     # Detailed evidence register
    "Action Items & Follow-up": 200,  # Detailed action register
    "Audit & Compliance Log": 100,    # Audit register
}

# Expected sections in Executive Dashboard
EXECUTIVE_DASHBOARD_SECTIONS = [
    "OVERALL CRYPTOGRAPHY COMPLIANCE STATUS",
    "COMPLIANCE BY ASSESSMENT AREA",
    "KEY PERFORMANCE INDICATORS",
    "TOP 5 CRITICAL SECURITY GAPS",
    "EXECUTIVE SUMMARY",
]

# Expected sections in KPIs & Metrics
KPI_SECTIONS = [
    "COMPLIANCE METRICS",
    "RISK METRICS",
    "REMEDIATION METRICS",
    "TECHNICAL IMPLEMENTATION METRICS",
]


# ============================================================================
# GENERIC EXCEL VALIDATION
# ============================================================================

def check_workbook_health(filename):
    """Comprehensive diagnostic check for common openpyxl issues."""
    
    print("=" * 80)
    print(f"EXCEL WORKBOOK DIAGNOSTIC REPORT: {filename}")
    print("ISMS-IMP-A.8.24.5 - Compliance Summary Dashboard")
    print("=" * 80)
    
    issues_found = []
    warnings_found = []
    
    try:
        wb = load_workbook(filename, data_only=False)
        print(f"\n✓ Workbook loaded successfully")
        print(f"  Sheets found: {len(wb.sheetnames)}")
        
    except Exception as e:
        print(f"\n✗ CRITICAL: Cannot load workbook: {e}")
        return
    
    # ========================================================================
    # CHECK 0: A.8.24.5 SPECIFIC STRUCTURE VALIDATION
    # ========================================================================
    print("\n" + "=" * 80)
    print("CHECK 0: A.8.24.5 STRUCTURE VALIDATION")
    print("=" * 80)
    
    structure_issues = 0
    
    # Check for expected sheets
    missing_sheets = []
    for sheet in EXPECTED_SHEETS:
        if sheet not in wb.sheetnames:
            missing_sheets.append(sheet)
            structure_issues += 1
    
    if missing_sheets:
        issues_found.append(f"  ✗ Missing required sheets: {', '.join(missing_sheets)}")
        print(f"  ✗ Missing {len(missing_sheets)} required sheet(s)")
    else:
        print(f"  ✓ All {len(EXPECTED_SHEETS)} required sheets present")
    
    # Check for unexpected sheets
    unexpected_sheets = []
    for sheet in wb.sheetnames:
        if sheet not in EXPECTED_SHEETS:
            unexpected_sheets.append(sheet)
    
    if unexpected_sheets:
        warnings_found.append(f"  ⚠ Unexpected sheets found: {', '.join(unexpected_sheets)}")
        print(f"  ⚠ Found {len(unexpected_sheets)} unexpected sheet(s)")
    
    # Validate document information fields in Executive Dashboard
    if "Executive Dashboard" in wb.sheetnames:
        ws = wb["Executive Dashboard"]
        found_fields = []
        for row in ws.iter_rows(min_row=1, max_row=20):
            for cell in row:
                if cell.value and isinstance(cell.value, str):
                    for field in REQUIRED_DOCUMENT_INFO:
                        if field in cell.value:
                            found_fields.append(field)
        
        missing_fields = [f for f in REQUIRED_DOCUMENT_INFO if f not in found_fields]
        if missing_fields:
            warnings_found.append(f"  ⚠ Missing document info fields: {', '.join(missing_fields)}")
    
    # Validate Executive Dashboard sections
    if "Executive Dashboard" in wb.sheetnames:
        ws = wb["Executive Dashboard"]
        found_sections = []
        for row in ws.iter_rows(min_row=1, max_row=100):
            for cell in row:
                if cell.value and isinstance(cell.value, str):
                    for section in EXECUTIVE_DASHBOARD_SECTIONS:
                        if section in cell.value.upper():
                            found_sections.append(section)
        
        missing_sections = [s for s in EXECUTIVE_DASHBOARD_SECTIONS if s not in found_sections]
        if missing_sections:
            warnings_found.append(f"  ⚠ Executive Dashboard: Missing sections: {', '.join(missing_sections)}")
        else:
            print(f"  ✓ Executive Dashboard: All {len(EXECUTIVE_DASHBOARD_SECTIONS)} sections found")
    
    # Validate KPI categories
    if "KPIs & Metrics" in wb.sheetnames:
        ws = wb["KPIs & Metrics"]
        found_categories = []
        for row in ws.iter_rows(min_row=1, max_row=200):
            for cell in row:
                if cell.value and isinstance(cell.value, str):
                    for category in KPI_SECTIONS:
                        if category in cell.value.upper():
                            found_categories.append(category)
        
        missing_categories = [c for c in KPI_SECTIONS if c not in found_categories]
        if missing_categories:
            warnings_found.append(f"  ⚠ KPIs & Metrics: Missing categories: {', '.join(missing_categories)}")
        else:
            print(f"  ✓ KPIs & Metrics: All {len(KPI_SECTIONS)} categories found")
    
    if structure_issues == 0:
        print("  ✓ Workbook structure matches A.8.24.5 specification")
    
    # ========================================================================
    # CHECK 0A: EXTERNAL WORKBOOK LINKS VALIDATION
    # ========================================================================
    print("\n" + "=" * 80)
    print("CHECK 0A: EXTERNAL WORKBOOK LINKS VALIDATION")
    print("=" * 80)
    
    external_link_issues = 0
    found_external_refs = set()
    
    if "Executive Dashboard" in wb.sheetnames:
        ws = wb["Executive Dashboard"]
        
        for row in ws.iter_rows(min_row=1, max_row=50):
            for cell in row:
                if cell.value and isinstance(cell.value, str) and cell.value.startswith('='):
                    formula = cell.value
                    
                    # Check for external workbook references [filename.xlsx]
                    external_refs = re.findall(r'\[([^\]]+\.xlsx)\]', formula)
                    for ref in external_refs:
                        found_external_refs.add(ref)
        
        if found_external_refs:
            print(f"  ✓ Found {len(found_external_refs)} external workbook references:")
            for ref in sorted(found_external_refs):
                print(f"    - {ref}")
            
            # Check if all expected source workbooks are referenced
            missing_refs = []
            for expected in EXPECTED_SOURCE_WORKBOOKS:
                if expected not in found_external_refs:
                    missing_refs.append(expected)
            
            if missing_refs:
                warnings_found.append(f"  ⚠ Missing external references: {', '.join(missing_refs)}")
                print(f"  ⚠ Expected source workbooks not found in formulas:")
                for ref in missing_refs:
                    print(f"    - {ref}")
            else:
                print(f"  ✓ All {len(EXPECTED_SOURCE_WORKBOOKS)} expected source workbooks referenced")
        else:
            warnings_found.append("  ⚠ No external workbook links found in Executive Dashboard")
            print("  ⚠ WARNING: No external workbook links detected")
            print("  This dashboard relies on external data - links may be broken!")
    
    # ========================================================================
    # CHECK 1: FORMULA VALIDATION
    # ========================================================================
    print("\n" + "=" * 80)
    print("CHECK 1: FORMULA VALIDATION")
    print("=" * 80)
    
    formula_issues = 0
    inter_sheet_refs = {}
    
    for sheet_name in wb.sheetnames:
        ws = wb[sheet_name]
        for row in ws.iter_rows():
            for cell in row:
                if cell.value and isinstance(cell.value, str) and cell.value.startswith('='):
                    formula = cell.value
                    
                    # Check for common formula issues
                    if "'" in formula:
                        # Sheet references with special characters
                        sheet_refs = re.findall(r"'([^']+)'!", formula)
                        for ref in sheet_refs:
                            if ref not in wb.sheetnames and "[" not in ref:
                                issues_found.append(
                                    f"  ✗ {sheet_name}!{cell.coordinate}: "
                                    f"Invalid sheet reference '{ref}'"
                                )
                                formula_issues += 1
                            
                            # Track inter-sheet references
                            if ref in wb.sheetnames:
                                if sheet_name not in inter_sheet_refs:
                                    inter_sheet_refs[sheet_name] = set()
                                inter_sheet_refs[sheet_name].add(ref)
                    
                    # Check for common syntax issues
                    if formula.count('(') != formula.count(')'):
                        issues_found.append(
                            f"  ✗ {sheet_name}!{cell.coordinate}: "
                            f"Unbalanced parentheses in formula"
                        )
                        formula_issues += 1
                    
                    # Check for double quotes issues
                    if formula.count('"') % 2 != 0:
                        issues_found.append(
                            f"  ✗ {sheet_name}!{cell.coordinate}: "
                            f"Unbalanced quotes in formula"
                        )
                        formula_issues += 1
    
    if formula_issues == 0:
        print("  ✓ All formulas appear syntactically valid")
    else:
        print(f"  ✗ Found {formula_issues} formula issues")
    
    # Report inter-sheet dependencies
    if inter_sheet_refs:
        print("\n  Inter-sheet formula dependencies:")
        for source, targets in sorted(inter_sheet_refs.items()):
            print(f"    {source} → {', '.join(sorted(targets))}")
    
    # ========================================================================
    # CHECK 2: DATA VALIDATION CONFLICTS
    # ========================================================================
    print("\n" + "=" * 80)
    print("CHECK 2: DATA VALIDATION CONFLICTS")
    print("=" * 80)
    
    validation_issues = 0
    total_validations = 0
    for sheet_name in wb.sheetnames:
        ws = wb[sheet_name]
        
        if hasattr(ws, 'data_validations') and ws.data_validations:
            dv_count = len(ws.data_validations.dataValidation)
            total_validations += dv_count
            print(f"  {sheet_name}: {dv_count} data validations")
            
            # Check for overlapping ranges (simplified)
            all_ranges = []
            for dv in ws.data_validations.dataValidation:
                if hasattr(dv, 'sqref') and dv.sqref:
                    all_ranges.extend(str(dv.sqref).split())
            
            if len(all_ranges) != len(set(all_ranges)):
                warnings_found.append(
                    f"  ⚠ {sheet_name}: Potentially overlapping data validation ranges"
                )
                validation_issues += 1
    
    print(f"  Total data validations across all sheets: {total_validations}")
    
    if validation_issues == 0:
        print("  ✓ No obvious data validation conflicts")
    
    # ========================================================================
    # CHECK 3: STYLE CONSISTENCY
    # ========================================================================
    print("\n" + "=" * 80)
    print("CHECK 3: STYLE CONSISTENCY")
    print("=" * 80)
    
    style_issues = 0
    for sheet_name in wb.sheetnames:
        ws = wb[sheet_name]
        
        cells_without_font = 0
        cells_without_border = 0
        
        sample_size = 0
        for row in ws.iter_rows(min_row=1, max_row=50):
            for cell in row:
                if cell.value:
                    sample_size += 1
                    if not hasattr(cell, 'font') or cell.font is None:
                        cells_without_font += 1
                    if not hasattr(cell, 'border') or cell.border is None:
                        cells_without_border += 1
        
        if cells_without_font > 0:
            warnings_found.append(
                f"  ⚠ {sheet_name}: {cells_without_font}/{sample_size} "
                f"cells missing font attributes"
            )
    
    if style_issues == 0:
        print("  ✓ Style attributes appear consistent")
    
    # ========================================================================
    # CHECK 4: MERGED CELLS VALIDATION
    # ========================================================================
    print("\n" + "=" * 80)
    print("CHECK 4: MERGED CELLS VALIDATION")
    print("=" * 80)
    
    merge_issues = 0
    total_merges = 0
    for sheet_name in wb.sheetnames:
        ws = wb[sheet_name]
        
        if hasattr(ws, 'merged_cells') and ws.merged_cells:
            merge_count = len(ws.merged_cells.ranges)
            total_merges += merge_count
            print(f"  {sheet_name}: {merge_count} merged cell ranges")
            
            # Check if merged cells have content in non-top-left cells
            for merge_range in ws.merged_cells.ranges:
                min_col = merge_range.min_col
                min_row = merge_range.min_row
                max_col = merge_range.max_col
                max_row = merge_range.max_row
                
                for row in range(min_row, max_row + 1):
                    for col in range(min_col, max_col + 1):
                        if row == min_row and col == min_col:
                            continue
                        
                        cell = ws.cell(row=row, column=col)
                        if cell.value:
                            cell_coord = f"{get_column_letter(col)}{row}"
                            warnings_found.append(
                                f"  ⚠ {sheet_name}!{cell_coord}: "
                                f"Merged cell has content in non-primary cell"
                            )
                            merge_issues += 1
    
    if total_merges > 0:
        print(f"  Total merged ranges across all sheets: {total_merges}")
    
    if merge_issues == 0:
        print("  ✓ Merged cells appear properly formatted")
    else:
        print(f"  ✗ Found {merge_issues} merged cell content issues")
    
    # ========================================================================
    # CHECK 5: WORKSHEET STRUCTURE & DATA ROWS
    # ========================================================================
    print("\n" + "=" * 80)
    print("CHECK 5: WORKSHEET STRUCTURE & DATA ROWS")
    print("=" * 80)
    
    for sheet_name in wb.sheetnames:
        ws = wb[sheet_name]
        
        # Check for excessive dimensions
        if ws.max_row > 10000:
            warnings_found.append(
                f"  ⚠ {sheet_name}: Large worksheet ({ws.max_row} rows)"
            )
        
        if ws.max_column > 100:
            warnings_found.append(
                f"  ⚠ {sheet_name}: Wide worksheet ({ws.max_column} columns)"
            )
        
        # Check expected data row counts
        if sheet_name in EXPECTED_DATA_ROWS:
            expected_rows = EXPECTED_DATA_ROWS[sheet_name]
            print(f"  {sheet_name}: Expected ~{expected_rows} data rows")
    
    print("  ✓ Worksheet dimensions within reasonable limits")
    
    # ========================================================================
    # SUMMARY REPORT
    # ========================================================================
    print("\n" + "=" * 80)
    print("DIAGNOSTIC SUMMARY")
    print("=" * 80)
    
    if issues_found:
        print(f"\n❌ CRITICAL ISSUES FOUND: {len(issues_found)}")
        for issue in issues_found:
            print(issue)
    
    if warnings_found:
        print(f"\n⚠️  WARNINGS: {len(warnings_found)}")
        for warning in warnings_found:
            print(warning)
    
    if not issues_found and not warnings_found:
        print("\n✅ NO ISSUES DETECTED")
        print("\nThe workbook appears structurally sound and matches A.8.24.5 specification.")
        print("Excel repair warnings may be due to:")
        print("  • Excel version compatibility (try Excel 2019+)")
        print("  • Antivirus/security software interference")
        print("  • Network drive or OneDrive sync issues")
        print("  • Excel's overly cautious validation")
        print("  • Unresolved external workbook links (this is expected before setup)")
    else:
        print("\n" + "=" * 80)
        print("RECOMMENDED ACTIONS:")
        print("=" * 80)
        
        if structure_issues > 0:
            print("\n0. STRUCTURE FIXES:")
            print("   • Verify all required sheets are present")
            print("   • Check sheet names match specification exactly")
            print("   • Ensure document information fields are complete")
            print("   • Verify all required sections exist in each sheet")
        
        if external_link_issues > 0 or not found_external_refs:
            print("\n0A. EXTERNAL LINKS FIXES:")
            print("   • This dashboard REQUIRES external workbook links to function")
            print("   • Ensure all 4 source workbooks are in the same folder:")
            print("     - ISMS-IMP-A.8.24.1.xlsx (Data Transmission)")
            print("     - ISMS-IMP-A.8.24.2.xlsx (Data Storage)")
            print("     - ISMS-IMP-A.8.24.3.xlsx (Authentication)")
            print("     - ISMS-IMP-A.8.24.4.xlsx (Key Management)")
            print("   • Run normalize_assessment_files.py first to standardize filenames")
            print("   • Open dashboard and click 'Update Links' when prompted")
        
        if formula_issues > 0:
            print("\n1. FORMULA FIXES:")
            print("   • Review formulas referencing other sheets")
            print("   • Ensure sheet names match exactly (case-sensitive)")
            print("   • Check for balanced quotes and parentheses")
            print("   • Verify external workbook references are correct")
        
        if validation_issues > 0:
            print("\n2. DATA VALIDATION FIXES:")
            print("   • Remove overlapping data validation ranges")
            print("   • Apply validations to specific ranges, not entire columns")
        
        if merge_issues > 0:
            print("\n3. MERGED CELL FIXES:")
            print("   • Ensure only top-left cell of merged range has content")
            print("   • Clear content from other cells in merged range")
    
    print("\n" + "=" * 80)
    print("A.8.24.5 SPECIFIC NOTES:")
    print("=" * 80)
    print("\nExpected structure:")
    print("  • 9 sheets total")
    print("  • Executive Dashboard:")
    print("    - Document information (10 fields)")
    print("    - Overall compliance status scorecard (4 metrics)")
    print("    - Compliance by assessment area (4 areas + total)")
    print("    - KPI table (10+ KPIs)")
    print("    - Top 5 critical security gaps")
    print("    - Executive summary with achievements/concerns")
    print("    - EXTERNAL LINKS to 4 source assessment workbooks")
    print()
    print("  • Gap Analysis:")
    print("    - Gap summary statistics (4 areas + total)")
    print("    - Detailed gap register (200 rows)")
    print("    - Columns: Gap ID, Assessment Area, Source, System, Description, etc.")
    print()
    print("  • Risk Register:")
    print("    - Risk distribution summary")
    print("    - Risk by assessment area")
    print("    - Detailed risk register (100 rows)")
    print("    - Inherent and residual risk scoring")
    print()
    print("  • Remediation Roadmap:")
    print("    - Roadmap summary (overall progress)")
    print("    - Progress by assessment area")
    print("    - Detailed remediation register (200 rows)")
    print("    - Timeline tracking with days remaining formulas")
    print()
    print("  • KPIs & Metrics:")
    print("    - 4 KPI categories (50+ total KPIs):")
    print("      1. Compliance Metrics (15 KPIs)")
    print("      2. Risk Metrics (10 KPIs)")
    print("      3. Remediation Metrics (11 KPIs)")
    print("      4. Technical Implementation Metrics (15 KPIs)")
    print()
    print("  • Evidence Register:")
    print("    - Evidence summary statistics (4 areas + total)")
    print("    - Detailed evidence register (500 rows)")
    print("    - Retention period tracking and destruction date formulas")
    print()
    print("  • Action Items & Follow-up:")
    print("    - Action summary dashboard (by status and priority)")
    print("    - Detailed action register (200 rows)")
    print("    - Days open/remaining formulas and on-time status")
    print()
    print("  • Audit & Compliance Log:")
    print("    - Audit summary (by audit type)")
    print("    - Audit register (100 rows)")
    print()
    print("  • Approval Sign-Off:")
    print("    - 3-level approval workflow")
    print("    - Document status tracking")
    print()
    print("CRITICAL SUCCESS FACTORS:")
    print("  1. External workbook links MUST be configured")
    print("  2. Source workbooks must use exact filenames")
    print("  3. All files must be in same folder for links to work")
    print("  4. Run normalization script before using dashboard")
    print("  5. Click 'Update Links' when opening dashboard")
    print("\n" + "=" * 80)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 excel_sanity_check_a824_5.py <filename.xlsx>")
        print("\nExample:")
        print("  python3 excel_sanity_check_a824_5.py ISMS-IMP-A.8.24.5_Compliance_Summary_Dashboard_20251231.xlsx")
        sys.exit(1)
    
    filename = sys.argv[1]
    check_workbook_health(filename)


if __name__ == "__main__":
    main()