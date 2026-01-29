#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
ISMS Framework - Complete Protection Status Scanner
================================================================================

Recursively scans all ISMS generator scripts to provide comprehensive report
on sheet protection implementation status across ALL controls.

**Purpose:**
- Find ALL ISMS generator scripts in directory tree
- Detect ALL sheet creation functions
- Check protection status for each function
- Generate comprehensive report (console + file)
- Provide actionable recommendations

**Usage:**
    # Scan current directory and subdirectories
    python3 scan_protection_status.py
    
    # Scan specific directory
    python3 scan_protection_status.py --dir /path/to/isms/scripts
    
    # Generate detailed report file
    python3 scan_protection_status.py --report protection_report.txt
    
    # Show only unprotected scripts
    python3 scan_protection_status.py --unprotected-only

**Output:**
- Console summary with color coding
- Detailed text report (optional)
- Statistics by control framework
- Actionable recommendations
- Priority list for implementation

================================================================================
"""

import os
import sys
import re
from datetime import datetime
from collections import defaultdict

class ScriptAnalyzer:
    """Analyzes a single Python script for sheet protection status."""
    
    def __init__(self, filepath):
        self.filepath = filepath
        self.filename = os.path.basename(filepath)
        self.rel_path = filepath
        self.functions = []
        self.protected_count = 0
        self.unprotected_count = 0
        self.control_id = self._extract_control_id()
        
    def _extract_control_id(self):
        """Extract control ID from filename."""
        # Pattern: generate_aXXX_Y_*.py or generate_aX_Y_Z_*.py
        match = re.search(r'generate_a(\d+(?:_\d+)*)', self.filename.lower())
        if match:
            parts = match.group(1).split('_')
            # Convert a59_1 -> A.5.9.1 or a824_3 -> A.8.24.3
            if len(parts) == 2:
                return f"A.{parts[0][0]}.{parts[0][1:]}.{parts[1]}"
            elif len(parts) == 3:
                return f"A.{parts[0]}.{parts[1]}.{parts[2]}"
            else:
                return f"A.{parts[0]}"
        return "Unknown"
    
    def analyze(self):
        """Analyze the script for protection status."""
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.split('\n')
            
            # Find all create functions
            for i, line in enumerate(lines):
                # Match: def create_XXXX(ws...):
                match = re.match(r'\s*def (create_\w+)\(ws[,\)]', line)
                if match:
                    func_name = match.group(1)
                    
                    # Find function end
                    func_end = len(lines) - 1
                    for j in range(i + 1, len(lines)):
                        if re.match(r'\s*def \w+\(', lines[j]):
                            func_end = j - 1
                            break
                    
                    # Check if protected
                    has_protection = False
                    for j in range(i, func_end + 1):
                        stripped = lines[j].strip()
                        if 'ws.protection.sheet = True' in stripped and not stripped.startswith('#'):
                            has_protection = True
                            break
                    
                    self.functions.append({
                        'name': func_name,
                        'line': i + 1,
                        'protected': has_protection
                    })
                    
                    if has_protection:
                        self.protected_count += 1
                    else:
                        self.unprotected_count += 1
            
            return True
            
        except Exception as e:
            print(f"  ⚠️  Error analyzing {self.filename}: {str(e)}")
            return False
    
    def get_status(self):
        """Get overall protection status."""
        if not self.functions:
            return 'NO_FUNCTIONS'
        elif self.unprotected_count == 0:
            return 'FULLY_PROTECTED'
        elif self.protected_count == 0:
            return 'NOT_PROTECTED'
        else:
            return 'PARTIALLY_PROTECTED'
    
    def get_completion_percentage(self):
        """Get percentage of protected functions."""
        total = len(self.functions)
        if total == 0:
            return 0
        return (self.protected_count / total) * 100


class ProtectionScanner:
    """Scans directory tree for all ISMS scripts and analyzes protection status."""
    
    def __init__(self, root_dir='.'):
        self.root_dir = root_dir
        self.scripts = []
        self.by_control = defaultdict(list)
        self.stats = {
            'total_scripts': 0,
            'total_functions': 0,
            'protected_functions': 0,
            'unprotected_functions': 0,
            'fully_protected_scripts': 0,
            'partially_protected_scripts': 0,
            'not_protected_scripts': 0,
        }
    
    def scan(self):
        """Scan directory tree for all generator scripts."""
        print(f"{'='*80}")
        print("ISMS Framework - Protection Status Scanner")
        print(f"{'='*80}\n")
        print(f"Scanning directory: {os.path.abspath(self.root_dir)}")
        print("Looking for: generate_*.py files\n")
        
        # Walk directory tree
        for root, dirs, files in os.walk(self.root_dir):
            # Skip hidden directories and common exclude patterns
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['__pycache__', 'venv', 'env']]
            
            for filename in files:
                if filename.startswith('generate_') and filename.endswith('.py'):
                    filepath = os.path.join(root, filename)
                    rel_path = os.path.relpath(filepath, self.root_dir)
                    
                    analyzer = ScriptAnalyzer(filepath)
                    analyzer.rel_path = rel_path
                    
                    if analyzer.analyze():
                        self.scripts.append(analyzer)
                        self.by_control[analyzer.control_id].append(analyzer)
        
        # Calculate statistics
        self.stats['total_scripts'] = len(self.scripts)
        
        for script in self.scripts:
            self.stats['total_functions'] += len(script.functions)
            self.stats['protected_functions'] += script.protected_count
            self.stats['unprotected_functions'] += script.unprotected_count
            
            status = script.get_status()
            if status == 'FULLY_PROTECTED':
                self.stats['fully_protected_scripts'] += 1
            elif status == 'PARTIALLY_PROTECTED':
                self.stats['partially_protected_scripts'] += 1
            elif status == 'NOT_PROTECTED':
                self.stats['not_protected_scripts'] += 1
        
        print(f"Found {len(self.scripts)} generator scripts\n")
    
    def print_summary(self, unprotected_only=False):
        """Print summary to console."""
        print(f"{'='*80}")
        print("SCAN RESULTS BY CONTROL FRAMEWORK")
        print(f"{'='*80}\n")
        
        # Sort controls
        controls = sorted(self.by_control.keys(), key=lambda x: (
            int(re.search(r'A\.(\d+)', x).group(1)) if re.search(r'A\.(\d+)', x) else 999,
            x
        ))
        
        for control_id in controls:
            scripts = self.by_control[control_id]
            
            # Skip if unprotected-only and all scripts are protected
            if unprotected_only and all(s.get_status() == 'FULLY_PROTECTED' for s in scripts):
                continue
            
            print(f"Control {control_id}")
            print("-" * 80)
            
            for script in sorted(scripts, key=lambda x: x.filename):
                status = script.get_status()
                total = len(script.functions)
                
                # Status symbols
                if status == 'FULLY_PROTECTED':
                    symbol = '✅'
                    status_text = f"PROTECTED ({script.protected_count}/{total})"
                elif status == 'NOT_PROTECTED':
                    symbol = '❌'
                    status_text = f"NOT PROTECTED (0/{total})"
                elif status == 'PARTIALLY_PROTECTED':
                    symbol = '⚠️ '
                    status_text = f"PARTIAL ({script.protected_count}/{total})"
                else:
                    symbol = '⊘'
                    status_text = "NO FUNCTIONS"
                
                # Skip fully protected if unprotected-only
                if unprotected_only and status == 'FULLY_PROTECTED':
                    continue
                
                print(f"  {symbol} {script.filename:50} {status_text}")
                
                # Show unprotected functions
                if script.unprotected_count > 0 and not unprotected_only:
                    for func in script.functions:
                        if not func['protected']:
                            print(f"      - {func['name']}() [Line {func['line']}]")
            
            print()
    
    def print_statistics(self):
        """Print overall statistics."""
        print(f"{'='*80}")
        print("OVERALL STATISTICS")
        print(f"{'='*80}\n")
        
        print(f"Total Scripts Found:        {self.stats['total_scripts']}")
        print(f"  ✅ Fully Protected:       {self.stats['fully_protected_scripts']}")
        print(f"  ⚠️  Partially Protected:   {self.stats['partially_protected_scripts']}")
        print(f"  ❌ Not Protected:         {self.stats['not_protected_scripts']}")
        print()
        
        print(f"Total Functions Found:      {self.stats['total_functions']}")
        print(f"  ✅ Protected:             {self.stats['protected_functions']}")
        print(f"  ❌ Unprotected:           {self.stats['unprotected_functions']}")
        print()
        
        if self.stats['total_functions'] > 0:
            pct = (self.stats['protected_functions'] / self.stats['total_functions']) * 100
            print(f"Overall Protection Rate:    {pct:.1f}%")
            
            if pct == 100:
                print("Status: ✅ ALL FUNCTIONS PROTECTED")
            elif pct >= 80:
                print("Status: ⚠️  MOSTLY PROTECTED - Some work needed")
            elif pct >= 50:
                print("Status: ⚠️  PARTIALLY PROTECTED - Significant work needed")
            else:
                print("Status: ❌ MOSTLY UNPROTECTED - Protection needed")
        print()
    
    def print_recommendations(self):
        """Print actionable recommendations."""
        unprotected_scripts = [s for s in self.scripts if s.get_status() != 'FULLY_PROTECTED']
        
        if not unprotected_scripts:
            print(f"{'='*80}")
            print("RECOMMENDATIONS")
            print(f"{'='*80}\n")
            print("✅ All scripts are fully protected!")
            print("   No action needed.\n")
            return
        
        print(f"{'='*80}")
        print("RECOMMENDATIONS - ACTION REQUIRED")
        print(f"{'='*80}\n")
        
        print(f"Scripts needing protection: {len(unprotected_scripts)}")
        print()
        
        # Priority 1: Completely unprotected scripts
        not_protected = [s for s in unprotected_scripts if s.get_status() == 'NOT_PROTECTED']
        if not_protected:
            print("PRIORITY 1 - Not Protected (0% complete):")
            print("-" * 80)
            for script in sorted(not_protected, key=lambda x: len(x.functions), reverse=True):
                print(f"  ❌ {script.rel_path}")
                print(f"     {len(script.functions)} functions need protection")
                print(f"     Command: python3 add_sheet_protection.py {script.rel_path}")
            print()
        
        # Priority 2: Partially protected scripts
        partial = [s for s in unprotected_scripts if s.get_status() == 'PARTIALLY_PROTECTED']
        if partial:
            print("PRIORITY 2 - Partially Protected:")
            print("-" * 80)
            for script in sorted(partial, key=lambda x: x.unprotected_count, reverse=True):
                pct = script.get_completion_percentage()
                print(f"  ⚠️  {script.rel_path}")
                print(f"     {script.unprotected_count}/{len(script.functions)} functions need protection ({pct:.0f}% complete)")
            print()
        
        # Quick fix command
        print("QUICK FIX - Process All Unprotected:")
        print("-" * 80)
        print("  # Preview changes")
        print("  python3 add_sheet_protection.py --dry-run --all")
        print()
        print("  # Apply to all scripts (creates .bak backups)")
        print("  python3 add_sheet_protection.py --all")
        print()
    
    def generate_report(self, filepath):
        """Generate detailed text report file."""
        with open(filepath, 'w', encoding='utf-8') as f:
            # Header
            f.write("="*80 + "\n")
            f.write("ISMS Framework - Sheet Protection Status Report\n")
            f.write("="*80 + "\n\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Scan Directory: {os.path.abspath(self.root_dir)}\n")
            f.write(f"Total Scripts Scanned: {len(self.scripts)}\n\n")
            
            # Statistics
            f.write("="*80 + "\n")
            f.write("OVERALL STATISTICS\n")
            f.write("="*80 + "\n\n")
            f.write(f"Scripts:\n")
            f.write(f"  Total:              {self.stats['total_scripts']}\n")
            f.write(f"  Fully Protected:    {self.stats['fully_protected_scripts']}\n")
            f.write(f"  Partially Protected: {self.stats['partially_protected_scripts']}\n")
            f.write(f"  Not Protected:      {self.stats['not_protected_scripts']}\n\n")
            
            f.write(f"Functions:\n")
            f.write(f"  Total:              {self.stats['total_functions']}\n")
            f.write(f"  Protected:          {self.stats['protected_functions']}\n")
            f.write(f"  Unprotected:        {self.stats['unprotected_functions']}\n\n")
            
            if self.stats['total_functions'] > 0:
                pct = (self.stats['protected_functions'] / self.stats['total_functions']) * 100
                f.write(f"Overall Protection Rate: {pct:.1f}%\n\n")
            
            # Detailed breakdown by control
            f.write("="*80 + "\n")
            f.write("DETAILED BREAKDOWN BY CONTROL\n")
            f.write("="*80 + "\n\n")
            
            controls = sorted(self.by_control.keys(), key=lambda x: (
                int(re.search(r'A\.(\d+)', x).group(1)) if re.search(r'A\.(\d+)', x) else 999,
                x
            ))
            
            for control_id in controls:
                f.write(f"\nControl {control_id}\n")
                f.write("-" * 80 + "\n")
                
                for script in sorted(self.by_control[control_id], key=lambda x: x.filename):
                    status = script.get_status()
                    f.write(f"\nScript: {script.rel_path}\n")
                    f.write(f"  Functions: {len(script.functions)}\n")
                    f.write(f"  Protected: {script.protected_count}\n")
                    f.write(f"  Unprotected: {script.unprotected_count}\n")
                    f.write(f"  Status: {status}\n")
                    
                    if script.functions:
                        f.write(f"  Function List:\n")
                        for func in script.functions:
                            status_mark = "✓" if func['protected'] else "✗"
                            f.write(f"    [{status_mark}] {func['name']}() - Line {func['line']}\n")
                
                f.write("\n")
            
            # Recommendations
            f.write("="*80 + "\n")
            f.write("RECOMMENDATIONS\n")
            f.write("="*80 + "\n\n")
            
            unprotected_scripts = [s for s in self.scripts if s.get_status() != 'FULLY_PROTECTED']
            
            if unprotected_scripts:
                f.write(f"Scripts needing attention: {len(unprotected_scripts)}\n\n")
                
                for script in sorted(unprotected_scripts, key=lambda x: x.unprotected_count, reverse=True):
                    f.write(f"{script.rel_path}\n")
                    f.write(f"  Command: python3 add_sheet_protection.py {script.rel_path}\n")
                    f.write(f"  Functions to protect: {script.unprotected_count}/{len(script.functions)}\n\n")
            else:
                f.write("All scripts are fully protected!\n")
        
        print(f"✓ Detailed report saved: {filepath}\n")


def main():
    """Main execution."""
    
    # Parse arguments
    root_dir = '.'
    report_file = None
    unprotected_only = False
    
    for i, arg in enumerate(sys.argv):
        if arg == '--dir' and i+1 < len(sys.argv):
            root_dir = sys.argv[i+1]
        elif arg == '--report' and i+1 < len(sys.argv):
            report_file = sys.argv[i+1]
        elif arg == '--unprotected-only':
            unprotected_only = True
        elif arg == '--help':
            print(__doc__)
            return 0
    
    # Run scanner
    scanner = ProtectionScanner(root_dir)
    scanner.scan()
    
    if scanner.stats['total_scripts'] == 0:
        print("⚠️  No generator scripts found.")
        print("   Make sure you're in the correct directory.\n")
        return 1
    
    # Print results
    scanner.print_summary(unprotected_only)
    scanner.print_statistics()
    scanner.print_recommendations()
    
    # Generate report file if requested
    if report_file:
        scanner.generate_report(report_file)
    
    print(f"{'='*80}")
    print("✅ Scan Complete")
    print(f"{'='*80}\n")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
