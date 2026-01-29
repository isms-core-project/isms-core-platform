#!/usr/bin/env python3
"""
isms_check_formula_quality.py
Comprehensive quality checker for Excel formula patterns in generator scripts

Checks for:
- Hardcoded dates (should use TODAY()/NOW())
- Volatile functions (performance impact)
- Off-by-one errors in ranges
- Inconsistent date/number formats
- Missing data validation
- Potential formula errors
- Best practice violations
"""

import re
import sys
from pathlib import Path
from collections import defaultdict

class FormulaQualityChecker:
    """Check Python generator scripts for Excel formula quality issues."""
    
    def __init__(self, script_path):
        self.script_path = Path(script_path)
        self.issues = defaultdict(list)
        self.warnings = defaultdict(list)
        self.content = ""
        
    def load_script(self):
        """Load script content."""
        with open(self.script_path, 'r', encoding='utf-8', errors='ignore') as f:
            self.content = f.read()
    
    def check_hardcoded_dates(self):
        """Check for hardcoded dates that should be dynamic."""
        # Pattern: "2024-01-01", "01/01/2024", etc in formulas
        patterns = [
            (r'"202\d-\d{2}-\d{2}"', "Hardcoded date (YYYY-MM-DD) - use TODAY() or NOW()"),
            (r'"\d{2}/\d{2}/202\d"', "Hardcoded date (MM/DD/YYYY) - use TODAY() or NOW()"),
            (r'"\d{4}-\d{2}-\d{2}"', "Hardcoded date - use TODAY() or NOW()"),
        ]
        
        for pattern, message in patterns:
            matches = re.finditer(pattern, self.content)
            for match in matches:
                line_num = self.content[:match.start()].count('\n') + 1
                self.warnings['hardcoded_dates'].append((line_num, match.group(0), message))
    
    def check_volatile_functions(self):
        """Check for volatile functions that recalculate on every change."""
        # NOW(), RAND(), RANDBETWEEN(), OFFSET(), INDIRECT() are volatile
        volatile_funcs = [
            ('NOW()', 'Volatile - recalculates constantly (use TODAY() if time not needed)'),
            ('RAND()', 'Volatile - recalculates constantly'),
            ('RANDBETWEEN(', 'Volatile - recalculates constantly'),
            ('OFFSET(', 'Volatile - consider INDEX/MATCH alternative'),
            ('INDIRECT(', 'Volatile - consider structured references'),
        ]
        
        for func, message in volatile_funcs:
            if func in self.content:
                # Find all occurrences
                for match in re.finditer(re.escape(func), self.content):
                    line_num = self.content[:match.start()].count('\n') + 1
                    self.warnings['volatile_functions'].append((line_num, func, message))
    
    def check_off_by_one_ranges(self):
        """Check for potential off-by-one errors in ranges."""
        # Pattern: ws.cell(row=X) then range that might include/exclude X incorrectly
        patterns = [
            # Range starts at row but cell is at row
            (r'row=(\d+).*value.*:(\1)["\)]', "Potential off-by-one: Range starts at same row as formula"),
            # Range ends at row but cell is at row
            (r'row=(\d+).*value.*(\1):', "Potential off-by-one: Range ends at same row as formula"),
        ]
        
        for pattern, message in patterns:
            matches = re.finditer(pattern, self.content, re.IGNORECASE)
            for match in matches:
                line_num = self.content[:match.start()].count('\n') + 1
                self.issues['off_by_one'].append((line_num, match.group(0)[:50], message))
    
    def check_date_format_consistency(self):
        """Check for inconsistent date formats."""
        formats = []
        
        # Find all date format strings
        date_format_pattern = r'number_format\s*=\s*["\']([^"\']*[dmyYhHsS][^"\']*)["\']'
        matches = re.finditer(date_format_pattern, self.content)
        
        for match in matches:
            fmt = match.group(1)
            line_num = self.content[:match.start()].count('\n') + 1
            formats.append((line_num, fmt))
        
        # Check for inconsistencies
        if len(set(f[1] for f in formats)) > 3:
            self.warnings['date_formats'].append((0, "", f"Multiple date formats found ({len(set(f[1] for f in formats))} different formats) - consider standardizing"))
    
    def check_missing_data_validation(self):
        """Check if data validation is used for input cells."""
        # Look for input cells without data validation
        input_cell_pattern = r'fill.*input_cell|FFFFCC'
        validation_pattern = r'DataValidation|data_validation'
        
        has_input_cells = re.search(input_cell_pattern, self.content)
        has_validation = re.search(validation_pattern, self.content)
        
        if has_input_cells and not has_validation:
            self.warnings['data_validation'].append((0, "", "Input cells found but no data validation used"))
    
    def check_formula_syntax(self):
        """Check for potential formula syntax errors."""
        issues_found = []
        
        # Unmatched parentheses in formulas
        formula_pattern = r'value\s*=\s*["\']=[^"\']*["\']'
        matches = re.finditer(formula_pattern, self.content)
        
        for match in matches:
            formula = match.group(0)
            line_num = self.content[:match.start()].count('\n') + 1
            
            # Count parentheses
            open_parens = formula.count('(')
            close_parens = formula.count(')')
            
            if open_parens != close_parens:
                self.issues['formula_syntax'].append((line_num, formula[:50], f"Unmatched parentheses: {open_parens} open, {close_parens} close"))
    
    def check_hardcoded_ranges(self):
        """Check for hardcoded ranges that might need to be dynamic."""
        # Pattern: Large hardcoded ranges like A1:Z1000
        pattern = r'[A-Z]+1:[A-Z]+\d{3,}'
        matches = re.finditer(pattern, self.content)
        
        for match in matches:
            range_ref = match.group(0)
            line_num = self.content[:match.start()].count('\n') + 1
            
            # Extract end row
            end_row = int(re.search(r'\d+$', range_ref).group())
            if end_row >= 1000:
                self.warnings['large_ranges'].append((line_num, range_ref, f"Large hardcoded range ({end_row} rows) - consider if dynamic range needed"))
    
    def check_percentage_formatting(self):
        """Check for inconsistent percentage handling."""
        # Look for percentage formulas
        patterns = [
            (r'&"%"', "Manual percentage string"),
            (r'number_format.*%', "Percentage number format"),
            (r'\*100&"%"', "Manual percentage calculation"),
        ]
        
        found_patterns = []
        for pattern, desc in patterns:
            if re.search(pattern, self.content):
                found_patterns.append(desc)
        
        if len(found_patterns) > 1:
            self.warnings['percentage_format'].append((0, "", f"Multiple percentage methods: {', '.join(found_patterns)} - consider standardizing"))
    
    def check_external_references(self):
        """Check for external workbook references."""
        # Pattern: [workbook.xlsx]Sheet!Cell
        pattern = r'\[ISMS-IMP-[^\]]+\.xlsx\][^!]+!'
        matches = list(re.finditer(pattern, self.content))
        
        if matches:
            # This is actually good for dashboards
            self.warnings['external_refs'].append((0, "", f"Uses external references ({len(matches)} found) - ensure source workbooks exist"))
    
    def check_sheet_name_consistency(self):
        """Check for consistent sheet naming."""
        # Extract sheet names
        sheet_pattern = r'create_sheet\(["\']([^"\']+)["\']\)|ws\.title\s*=\s*["\']([^"\']+)["\']'
        matches = re.finditer(sheet_pattern, self.content)
        
        sheets = []
        for match in matches:
            sheet_name = match.group(1) or match.group(2)
            if sheet_name:
                sheets.append(sheet_name)
        
        # Check for spaces vs underscores
        has_spaces = any(' ' in s for s in sheets)
        has_underscores = any('_' in s for s in sheets)
        
        if has_spaces and has_underscores:
            self.warnings['sheet_naming'].append((0, "", f"Mixed sheet naming: some with spaces, some with underscores"))
    
    def check_todo_fixme_comments(self):
        """Check for TODO/FIXME comments."""
        patterns = [
            (r'#\s*TODO', "TODO comment found"),
            (r'#\s*FIXME', "FIXME comment found"),
            (r'#\s*HACK', "HACK comment found"),
            (r'#\s*XXX', "XXX comment found"),
            (r'#\s*BUG', "BUG comment found"),
        ]
        
        for pattern, message in patterns:
            matches = re.finditer(pattern, self.content, re.IGNORECASE)
            for match in matches:
                line_num = self.content[:match.start()].count('\n') + 1
                # Get the full comment line
                line_start = self.content.rfind('\n', 0, match.start()) + 1
                line_end = self.content.find('\n', match.start())
                comment = self.content[line_start:line_end].strip()
                self.issues['todo_comments'].append((line_num, comment, message))
    
    def check_approval_fields(self):
        """Check for approval/sign-off sheets."""
        if 'Approval' not in self.content and 'Sign' not in self.content:
            self.warnings['approval'].append((0, "", "No approval/sign-off sheet detected - ISO 27001 may require"))
    
    def run_all_checks(self):
        """Run all quality checks."""
        self.load_script()
        
        self.check_hardcoded_dates()
        self.check_volatile_functions()
        self.check_off_by_one_ranges()
        self.check_date_format_consistency()
        self.check_missing_data_validation()
        self.check_formula_syntax()
        self.check_hardcoded_ranges()
        self.check_percentage_formatting()
        self.check_external_references()
        self.check_sheet_name_consistency()
        self.check_todo_fixme_comments()
        self.check_approval_fields()
    
    def generate_report(self):
        """Generate quality report."""
        print("="*80)
        print(f"QUALITY CHECK: {self.script_path.name}")
        print("="*80)
        
        total_issues = sum(len(v) for v in self.issues.values())
        total_warnings = sum(len(v) for v in self.warnings.values())
        
        if total_issues == 0 and total_warnings == 0:
            print("✅ No issues or warnings found")
            return True
        
        # Report issues (high priority)
        if self.issues:
            print("\n❌ ISSUES (Should Fix):")
            print("-"*80)
            for category, items in self.issues.items():
                if items:
                    print(f"\n{category.upper().replace('_', ' ')}:")
                    for line_num, content, message in items:
                        print(f"  Line {line_num}: {message}")
                        if content:
                            print(f"    {content}")
        
        # Report warnings (review recommended)
        if self.warnings:
            print("\n⚠️  WARNINGS (Review Recommended):")
            print("-"*80)
            for category, items in self.warnings.items():
                if items:
                    print(f"\n{category.upper().replace('_', ' ')}:")
                    for line_num, content, message in items:
                        if line_num > 0:
                            print(f"  Line {line_num}: {message}")
                        else:
                            print(f"  {message}")
                        if content and len(content) > 5:
                            print(f"    {content}")
        
        print("\n"+"="*80)
        print(f"SUMMARY: {total_issues} issue(s), {total_warnings} warning(s)")
        print("="*80)
        
        return total_issues == 0

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 isms_check_formula_quality.py <script.py> [script2.py ...]")
        print("\nExamples:")
        print("  python3 isms_check_formula_quality.py generate_a824_5_*.py")
        print("  python3 isms_check_formula_quality.py generate_*.py")
        sys.exit(1)
    
    files = sys.argv[1:]
    all_clean = True
    
    for filepath in files:
        if not Path(filepath).exists():
            print(f"❌ File not found: {filepath}")
            continue
        
        checker = FormulaQualityChecker(filepath)
        checker.run_all_checks()
        is_clean = checker.generate_report()
        
        if not is_clean:
            all_clean = False
        
        print("\n")
    
    return 0 if all_clean else 1

if __name__ == "__main__":
    sys.exit(main())
