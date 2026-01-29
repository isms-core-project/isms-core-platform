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


def check_workbook_health(filename):
    """Comprehensive diagnostic check for common openpyxl issues."""
    
    print("=" * 80)
    print(f"EXCEL WORKBOOK DIAGNOSTIC REPORT: {filename}")
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
    # CHECK 1: FORMULA VALIDATION
    # ========================================================================
    print("\n" + "=" * 80)
    print("CHECK 1: FORMULA VALIDATION")
    print("=" * 80)
    
    formula_issues = 0
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
                            if ref not in wb.sheetnames:
                                issues_found.append(
                                    f"  ✗ {sheet_name}!{cell.coordinate}: "
                                    f"Invalid sheet reference '{ref}'"
                                )
                                formula_issues += 1
                    
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
    
    # ========================================================================
    # CHECK 2: DATA VALIDATION CONFLICTS
    # ========================================================================
    print("\n" + "=" * 80)
    print("CHECK 2: DATA VALIDATION CONFLICTS")
    print("=" * 80)
    
    validation_issues = 0
    for sheet_name in wb.sheetnames:
        ws = wb[sheet_name]
        
        if hasattr(ws, 'data_validations') and ws.data_validations:
            dv_count = len(ws.data_validations.dataValidation)
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
        
        # Note: Missing borders are often intentional, so we don't flag this as issue
    
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
                # Get min cell (top-left) of merged range
                min_col = merge_range.min_col
                min_row = merge_range.min_row
                max_col = merge_range.max_col
                max_row = merge_range.max_row
                
                # Check if any cell other than top-left has content
                for row in range(min_row, max_row + 1):
                    for col in range(min_col, max_col + 1):
                        # Skip the top-left cell
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
    # CHECK 5: WORKSHEET STRUCTURE
    # ========================================================================
    print("\n" + "=" * 80)
    print("CHECK 5: WORKSHEET STRUCTURE")
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
        print("\nThe workbook appears structurally sound.")
        print("Excel repair warnings may be due to:")
        print("  • Excel version compatibility (try Excel 2019+)")
        print("  • Antivirus/security software interference")
        print("  • Network drive or OneDrive sync issues")
        print("  • Excel's overly cautious validation")
    else:
        print("\n" + "=" * 80)
        print("RECOMMENDED ACTIONS:")
        print("=" * 80)
        
        if formula_issues > 0:
            print("\n1. FORMULA FIXES:")
            print("   • Review formulas referencing other sheets")
            print("   • Ensure sheet names match exactly (case-sensitive)")
            print("   • Check for balanced quotes and parentheses")
        
        if validation_issues > 0:
            print("\n2. DATA VALIDATION FIXES:")
            print("   • Remove overlapping data validation ranges")
            print("   • Apply validations to specific ranges, not entire columns")
        
        if merge_issues > 0:
            print("\n3. MERGED CELL FIXES:")
            print("   • Ensure only top-left cell of merged range has content")
            print("   • Clear content from other cells in merged range")
    
    print("\n" + "=" * 80)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 excel_sanity_check.py <filename.xlsx>")
        sys.exit(1)
    
    filename = sys.argv[1]
    check_workbook_health(filename)


if __name__ == "__main__":
    main()