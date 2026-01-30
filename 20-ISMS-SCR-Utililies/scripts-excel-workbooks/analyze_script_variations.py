#!/usr/bin/env python3
"""
ISMS Script Variation Analyzer
Purpose: Identify variations and patterns across Excel workbook generation scripts

Usage:
    python3 analyze_script_variations.py /path/to/scripts/folder

Author: Gregory Griffin
Date: 2026-01-31
"""

import os
import sys
import re
from pathlib import Path
from collections import Counter, defaultdict
from typing import Dict, List, Set, Tuple


class ScriptAnalyzer:
    """Analyze patterns and variations across Python scripts."""
    
    def __init__(self, scripts_dir: str):
        self.scripts_dir = Path(scripts_dir)
        self.scripts: List[Path] = []
        self.patterns: Dict[str, Counter] = defaultdict(Counter)
        self.variations: Dict[str, List[Tuple[str, str]]] = defaultdict(list)
        
    def find_scripts(self) -> None:
        """Find all Python scripts in directory."""
        self.scripts = sorted(self.scripts_dir.rglob("*.py"))
        print(f"📊 Found {len(self.scripts)} Python scripts\n")
        
    def analyze_imports(self) -> None:
        """Analyze import statements."""
        import_pattern = re.compile(r'^(?:from|import)\s+[\w.]+', re.MULTILINE)
        
        for script in self.scripts:
            try:
                content = script.read_text(encoding='utf-8')
                imports = import_pattern.findall(content)
                for imp in imports:
                    self.patterns['imports'][imp] += 1
            except Exception as e:
                print(f"⚠️  Error reading {script.name}: {e}")
    
    def analyze_function_names(self) -> None:
        """Analyze function definitions."""
        func_pattern = re.compile(r'^def\s+(\w+)\s*\(', re.MULTILINE)
        
        for script in self.scripts:
            try:
                content = script.read_text(encoding='utf-8')
                functions = func_pattern.findall(content)
                for func in functions:
                    self.patterns['functions'][func] += 1
                    self.variations['functions'].append((script.name, func))
            except Exception as e:
                print(f"⚠️  Error reading {script.name}: {e}")
    
    def analyze_workbook_naming(self) -> None:
        """Analyze workbook filename patterns."""
        # Look for various workbook naming patterns
        patterns = [
            (r'workbook_name\s*=\s*["\']([^"\']+)["\']', 'static_name'),
            (r'workbook_name\s*=\s*f["\']([^"\']+)["\']', 'f_string'),
            (r'filename\s*=\s*["\']([^"\']+)["\']', 'filename_var'),
            (r'\.to_excel\(["\']([^"\']+)["\']', 'direct_excel'),
        ]
        
        for script in self.scripts:
            try:
                content = script.read_text(encoding='utf-8')
                for pattern, pattern_type in patterns:
                    matches = re.findall(pattern, content)
                    for match in matches:
                        self.patterns['workbook_naming'][pattern_type] += 1
                        self.variations['workbook_naming'].append((script.name, match))
            except Exception as e:
                print(f"⚠️  Error reading {script.name}: {e}")
    
    def analyze_date_formats(self) -> None:
        """Analyze date formatting patterns."""
        date_patterns = [
            (r'strftime\(["\']([^"\']+)["\']\)', 'strftime'),
            (r'datetime\.now\(\)\.strftime\(["\']([^"\']+)["\']\)', 'datetime_now'),
            (r'date\(\)\.strftime\(["\']([^"\']+)["\']\)', 'date_only'),
        ]
        
        for script in self.scripts:
            try:
                content = script.read_text(encoding='utf-8')
                for pattern, pattern_type in date_patterns:
                    matches = re.findall(pattern, content)
                    for match in matches:
                        self.patterns['date_formats'][match] += 1
                        self.variations['date_formats'].append((script.name, match))
            except Exception as e:
                print(f"⚠️  Error reading {script.name}: {e}")
    
    def analyze_error_handling(self) -> None:
        """Analyze error handling approaches."""
        for script in self.scripts:
            try:
                content = script.read_text(encoding='utf-8')
                
                has_try_except = 'try:' in content and 'except' in content
                has_logging = 'logging.' in content or 'logger.' in content
                has_sys_exit = 'sys.exit' in content
                
                if has_try_except:
                    self.patterns['error_handling']['try_except'] += 1
                if has_logging:
                    self.patterns['error_handling']['logging'] += 1
                if has_sys_exit:
                    self.patterns['error_handling']['sys_exit'] += 1
                if not (has_try_except or has_logging or has_sys_exit):
                    self.patterns['error_handling']['none'] += 1
                    self.variations['error_handling'].append((script.name, "no error handling"))
                    
            except Exception as e:
                print(f"⚠️  Error reading {script.name}: {e}")
    
    def analyze_sheet_creation(self) -> None:
        """Analyze Excel sheet creation patterns."""
        sheet_patterns = [
            (r'workbook\.add_worksheet\(["\']([^"\']+)["\']\)', 'xlsxwriter'),
            (r'ExcelWriter.*engine=["\']([^"\']+)["\']', 'pandas_engine'),
            (r'sheet_name=["\']([^"\']+)["\']', 'pandas_sheet'),
        ]
        
        for script in self.scripts:
            try:
                content = script.read_text(encoding='utf-8')
                
                # Count sheets
                sheet_count = content.count('add_worksheet') + content.count('sheet_name=')
                if sheet_count > 0:
                    self.patterns['sheet_counts'][f'{sheet_count}_sheets'] += 1
                    
                # Identify patterns
                for pattern, pattern_type in sheet_patterns:
                    matches = re.findall(pattern, content)
                    for match in matches:
                        self.patterns['sheet_patterns'][pattern_type] += 1
                        
            except Exception as e:
                print(f"⚠️  Error reading {script.name}: {e}")
    
    def find_outliers(self, pattern_name: str, threshold: int = 5) -> List[str]:
        """Find patterns that appear less than threshold times (potential outliers)."""
        outliers = []
        for pattern, count in self.patterns[pattern_name].items():
            if count < threshold:
                outliers.append(f"{pattern} ({count} scripts)")
        return outliers
    
    def report(self) -> None:
        """Generate analysis report."""
        print("=" * 80)
        print("ISMS SCRIPT VARIATION ANALYSIS")
        print("=" * 80)
        print()
        
        # Summary
        print(f"📊 Total Scripts Analyzed: {len(self.scripts)}")
        print()
        
        # Imports Analysis
        print("=" * 80)
        print("📦 IMPORT PATTERNS")
        print("=" * 80)
        common_imports = self.patterns['imports'].most_common(10)
        for imp, count in common_imports:
            percentage = (count / len(self.scripts)) * 100
            print(f"  {imp:40s} {count:3d} scripts ({percentage:.1f}%)")
        
        outlier_imports = self.find_outliers('imports', threshold=5)
        if outlier_imports:
            print(f"\n  ⚠️  Rare imports (< 5 scripts):")
            for imp in outlier_imports[:10]:
                print(f"     • {imp}")
        print()
        
        # Function Names
        print("=" * 80)
        print("🔧 COMMON FUNCTION NAMES")
        print("=" * 80)
        common_funcs = self.patterns['functions'].most_common(10)
        for func, count in common_funcs:
            percentage = (count / len(self.scripts)) * 100
            print(f"  {func:40s} {count:3d} scripts ({percentage:.1f}%)")
        
        unique_funcs = sum(1 for count in self.patterns['functions'].values() if count == 1)
        print(f"\n  📊 Unique function names: {unique_funcs}")
        print()
        
        # Workbook Naming
        print("=" * 80)
        print("📄 WORKBOOK NAMING PATTERNS")
        print("=" * 80)
        for pattern_type, count in self.patterns['workbook_naming'].most_common():
            percentage = (count / len(self.scripts)) * 100
            print(f"  {pattern_type:40s} {count:3d} scripts ({percentage:.1f}%)")
        
        # Show sample variations
        if self.variations['workbook_naming']:
            print(f"\n  📋 Sample naming patterns:")
            samples = self.variations['workbook_naming'][:5]
            for script, pattern in samples:
                print(f"     {script:40s} → {pattern}")
        print()
        
        # Date Formats
        print("=" * 80)
        print("📅 DATE FORMAT PATTERNS")
        print("=" * 80)
        if self.patterns['date_formats']:
            for date_format, count in self.patterns['date_formats'].most_common():
                percentage = (count / len(self.scripts)) * 100
                print(f"  {date_format:40s} {count:3d} scripts ({percentage:.1f}%)")
        else:
            print("  ℹ️  No date formatting patterns found")
        print()
        
        # Error Handling
        print("=" * 80)
        print("⚠️  ERROR HANDLING APPROACHES")
        print("=" * 80)
        for approach, count in self.patterns['error_handling'].most_common():
            percentage = (count / len(self.scripts)) * 100
            print(f"  {approach:40s} {count:3d} scripts ({percentage:.1f}%)")
        
        if self.variations['error_handling']:
            print(f"\n  ⚠️  Scripts without error handling:")
            for script, _ in self.variations['error_handling'][:10]:
                print(f"     • {script}")
        print()
        
        # Sheet Patterns
        print("=" * 80)
        print("📊 EXCEL SHEET PATTERNS")
        print("=" * 80)
        for pattern, count in self.patterns['sheet_counts'].most_common():
            percentage = (count / len(self.scripts)) * 100
            print(f"  {pattern:40s} {count:3d} scripts ({percentage:.1f}%)")
        print()
        
        # Recommendations
        print("=" * 80)
        print("💡 RECOMMENDATIONS")
        print("=" * 80)
        
        # Check standardization level
        if self.patterns['date_formats']:
            most_common_date = self.patterns['date_formats'].most_common(1)[0]
            date_standardization = (most_common_date[1] / len(self.scripts)) * 100
            if date_standardization < 80:
                print(f"  ⚠️  Date format standardization: {date_standardization:.1f}%")
                print(f"     Consider standardizing on: {most_common_date[0]}")
        
        error_with_handling = self.patterns['error_handling'].get('try_except', 0)
        error_percentage = (error_with_handling / len(self.scripts)) * 100
        if error_percentage < 80:
            print(f"  ⚠️  Error handling coverage: {error_percentage:.1f}%")
            print(f"     Consider adding try/except to more scripts")
        
        if outlier_imports:
            print(f"  ℹ️  Found {len(outlier_imports)} rare imports")
            print(f"     Review if these are control-specific or accidental variations")
        
        # Overall assessment
        print()
        print("=" * 80)
        print("📊 OVERALL ASSESSMENT")
        print("=" * 80)
        
        # Calculate consistency score
        consistency_scores = []
        
        # Import consistency (top import vs total scripts)
        if self.patterns['imports']:
            top_import = self.patterns['imports'].most_common(1)[0][1]
            consistency_scores.append((top_import / len(self.scripts)) * 100)
        
        # Function consistency
        if self.patterns['functions']:
            top_func = self.patterns['functions'].most_common(1)[0][1]
            consistency_scores.append((top_func / len(self.scripts)) * 100)
        
        # Error handling consistency
        if error_with_handling:
            consistency_scores.append(error_percentage)
        
        if consistency_scores:
            avg_consistency = sum(consistency_scores) / len(consistency_scores)
            print(f"  Average Consistency Score: {avg_consistency:.1f}%")
            print()
            if avg_consistency >= 85:
                print("  ✅ EXCELLENT: High standardization across scripts")
                print("     Minor variations are likely intentional and control-specific")
            elif avg_consistency >= 70:
                print("  ✅ GOOD: Reasonable standardization")
                print("     Review outliers to ensure variations are intentional")
            else:
                print("  ⚠️  MODERATE: Significant variations detected")
                print("     Consider documenting why variations exist")
        
        print()


def main():
    """Main execution."""
    if len(sys.argv) != 2:
        print("Usage: python3 analyze_script_variations.py <scripts_directory>")
        print("Example: python3 analyze_script_variations.py ./50_scripts-excel/")
        sys.exit(1)
    
    scripts_dir = sys.argv[1]
    
    if not os.path.exists(scripts_dir):
        print(f"❌ Error: Directory not found: {scripts_dir}")
        sys.exit(1)
    
    print("🔍 ISMS CORE Script Variation Analyzer")
    print(f"📁 Analyzing: {scripts_dir}")
    print()
    
    analyzer = ScriptAnalyzer(scripts_dir)
    
    print("⏳ Finding scripts...")
    analyzer.find_scripts()
    
    print("⏳ Analyzing imports...")
    analyzer.analyze_imports()
    
    print("⏳ Analyzing function names...")
    analyzer.analyze_function_names()
    
    print("⏳ Analyzing workbook naming...")
    analyzer.analyze_workbook_naming()
    
    print("⏳ Analyzing date formats...")
    analyzer.analyze_date_formats()
    
    print("⏳ Analyzing error handling...")
    analyzer.analyze_error_handling()
    
    print("⏳ Analyzing sheet creation...")
    analyzer.analyze_sheet_creation()
    
    print()
    analyzer.report()
    
    print("=" * 80)
    print("🎋 Analysis complete! Built in Bamboo Land")
    print("=" * 80)


if __name__ == "__main__":
    main()
