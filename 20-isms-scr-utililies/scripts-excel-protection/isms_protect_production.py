#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
ISMS Framework - Protect Production Scripts Only
================================================================================

Targets ONLY scripts in "10_generator_utf" folders across your ISMS framework.
This focuses on production scripts while skipping backups and originals.

**Purpose:**
- Reduce scope from 357 scripts to ~100 production scripts
- Protect only the scripts actually used for assessments
- Skip: 99_originals/, 97_backup/, 98_claude_ai/, etc.

**Usage:**
    # Preview what will be protected (safe - no changes)
    python3 protect_production_only.py --dry-run
    
    # Protect all production scripts
    python3 protect_production_only.py
    
    # Protect specific control (e.g., A.8.24)
    python3 protect_production_only.py --control a824
    
    # Generate before/after reports
    python3 protect_production_only.py --with-reports

**What It Does:**
1. Scans for scripts in */10_generator_utf/ paths only
2. Applies sheet protection to each
3. Creates .bak backups
4. Shows progress and statistics
5. Generates verification report

================================================================================
"""

import os
import sys
import subprocess
from pathlib import Path
from datetime import datetime

class ProductionScriptProtector:
    """Protects only production scripts (10_generator_utf folders)."""
    
    def __init__(self, base_dir='.', control_filter=None, dry_run=False):
        self.base_dir = Path(base_dir)
        self.control_filter = control_filter.lower() if control_filter else None
        self.dry_run = dry_run
        self.scripts_found = []
        self.scripts_protected = 0
        self.scripts_skipped = 0
        self.scripts_failed = 0
        
    def find_production_scripts(self):
        """Find all scripts in 10_generator_utf folders."""
        
        print("="*80)
        print("ISMS Framework - Production Script Protector")
        print("="*80)
        print()
        print(f"Base Directory: {self.base_dir.absolute()}")
        print(f"Target Folders: */10_generator_utf/")
        if self.control_filter:
            print(f"Filter: Scripts matching '{self.control_filter}'")
        if self.dry_run:
            print("Mode: DRY RUN (no changes will be made)")
        else:
            print("Mode: LIVE (scripts will be modified)")
        print()
        print("Scanning...")
        
        # Find all generate_*.py in 10_generator_utf folders
        for script_path in self.base_dir.rglob('10_generator_utf/generate_*.py'):
            # Apply control filter if specified
            if self.control_filter:
                if self.control_filter not in script_path.name.lower():
                    continue
            
            self.scripts_found.append(script_path)
        
        print(f"Found {len(self.scripts_found)} production scripts\n")
        
        if len(self.scripts_found) == 0:
            print("⚠️  No production scripts found!")
            print("   Make sure you're in the correct directory.")
            print(f"   Looking in: {self.base_dir.absolute()}")
            return False
        
        return True
    
    def protect_script(self, script_path, index, total):
        """Protect a single script using isms_add_protection.py"""
        
        rel_path = script_path.relative_to(self.base_dir)
        
        # Progress indicator
        progress = f"[{index}/{total}]"
        
        # Check if isms_add_protection.py exists
        protector_script = Path(__file__).parent / 'isms_add_protection.py'
        if not protector_script.exists():
            # Try current directory
            protector_script = Path('isms_add_protection.py')
            if not protector_script.exists():
                print(f"  {progress} ⚠️  SKIP: isms_add_protection.py not found")
                self.scripts_skipped += 1
                return False
        
        if self.dry_run:
            print(f"  {progress} [DRY-RUN] Would protect: {rel_path}")
            return True
        
        try:
            # Run isms_add_protection.py on this script
            result = subprocess.run(
                [sys.executable, str(protector_script), str(script_path)],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.returncode == 0:
                # Check if any changes were made
                if "All functions already have sheet protection" in result.stdout:
                    print(f"  {progress} ⊘  SKIP: {rel_path} (already protected)")
                    self.scripts_skipped += 1
                elif "functions modified" in result.stdout or "Added protection" in result.stdout:
                    # Extract number of functions protected
                    import re
                    match = re.search(r'(\d+) functions modified', result.stdout)
                    if match:
                        count = match.group(1)
                        print(f"  {progress} ✅ PROTECTED: {rel_path} ({count} functions)")
                    else:
                        print(f"  {progress} ✅ PROTECTED: {rel_path}")
                    self.scripts_protected += 1
                else:
                    print(f"  {progress} ✅ PROTECTED: {rel_path}")
                    self.scripts_protected += 1
                return True
            else:
                print(f"  {progress} ❌ FAILED: {rel_path}")
                if result.stderr:
                    print(f"      Error: {result.stderr[:100]}")
                self.scripts_failed += 1
                return False
                
        except subprocess.TimeoutExpired:
            print(f"  {progress} ❌ TIMEOUT: {rel_path}")
            self.scripts_failed += 1
            return False
        except Exception as e:
            print(f"  {progress} ❌ ERROR: {rel_path} - {str(e)}")
            self.scripts_failed += 1
            return False
    
    def protect_all(self):
        """Protect all found production scripts."""
        
        if not self.scripts_found:
            return False
        
        print("="*80)
        print("PROTECTING PRODUCTION SCRIPTS")
        print("="*80)
        print()
        
        total = len(self.scripts_found)
        
        for index, script_path in enumerate(self.scripts_found, 1):
            self.protect_script(script_path, index, total)
        
        return True
    
    def print_summary(self):
        """Print summary statistics."""
        
        print()
        print("="*80)
        print("SUMMARY")
        print("="*80)
        print()
        
        total = len(self.scripts_found)
        
        print(f"Total Scripts Found:     {total}")
        print(f"  ✅ Protected:          {self.scripts_protected}")
        print(f"  ⊘  Skipped:            {self.scripts_skipped} (already protected)")
        print(f"  ❌ Failed:             {self.scripts_failed}")
        print()
        
        if self.dry_run:
            print("Mode: DRY RUN - No files were modified")
            print()
            print("To apply changes, run without --dry-run:")
            print(f"  python3 {Path(__file__).name}")
        else:
            if self.scripts_protected > 0:
                print(f"✅ Successfully protected {self.scripts_protected} production scripts!")
                print()
                print("Next Steps:")
                print("  1. Run verification scan:")
                print("     python3 isms_scan_protection.py --dir . --report after_production.txt")
                print()
                print("  2. Check protection rate:")
                print("     grep 'Overall Protection Rate' after_production.txt")
            elif self.scripts_skipped == total:
                print("✅ All production scripts already protected!")
            else:
                print("⚠️  Some scripts could not be protected")
                print("   Check error messages above for details")
        
        print()


def generate_before_after_reports(base_dir):
    """Generate before and after scan reports."""
    
    print("="*80)
    print("GENERATING VERIFICATION REPORTS")
    print("="*80)
    print()
    
    # Check if scanner exists
    scanner_script = Path(__file__).parent / 'isms_scan_protection.py'
    if not scanner_script.exists():
        scanner_script = Path('isms_scan_protection.py')
        if not scanner_script.exists():
            print("⚠️  isms_scan_protection.py not found - skipping reports")
            return
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    
    # Before report
    print("Generating 'before' report...")
    before_report = f"production_scan_before_{timestamp}.txt"
    
    try:
        subprocess.run(
            [sys.executable, str(scanner_script), '--dir', str(base_dir), '--report', before_report],
            timeout=120
        )
        print(f"  ✓ Saved: {before_report}")
    except Exception as e:
        print(f"  ⚠️  Could not generate before report: {e}")
    
    print()


def main():
    """Main execution."""
    
    # Parse arguments
    base_dir = '.'
    control_filter = None
    dry_run = '--dry-run' in sys.argv
    with_reports = '--with-reports' in sys.argv
    
    for i, arg in enumerate(sys.argv):
        if arg == '--dir' and i+1 < len(sys.argv):
            base_dir = sys.argv[i+1]
        elif arg == '--control' and i+1 < len(sys.argv):
            control_filter = sys.argv[i+1]
        elif arg == '--help':
            print(__doc__)
            return 0
    
    # Generate before report if requested
    if with_reports and not dry_run:
        generate_before_after_reports(base_dir)
    
    # Create protector
    protector = ProductionScriptProtector(base_dir, control_filter, dry_run)
    
    # Find scripts
    if not protector.find_production_scripts():
        return 1
    
    # Show what will be done
    if dry_run:
        print("DRY RUN - Showing what would be protected:")
        print("-" * 80)
    
    # Protect scripts
    protector.protect_all()
    
    # Print summary
    protector.print_summary()
    
    # Generate after report if requested
    if with_reports and not dry_run and protector.scripts_protected > 0:
        print()
        print("Generating 'after' report...")
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        after_report = f"production_scan_after_{timestamp}.txt"
        
        scanner_script = Path(__file__).parent / 'isms_scan_protection.py'
        if not scanner_script.exists():
            scanner_script = Path('isms_scan_protection.py')
        
        if scanner_script.exists():
            try:
                subprocess.run(
                    [sys.executable, str(scanner_script), '--dir', str(base_dir), '--report', after_report],
                    timeout=120
                )
                print(f"  ✓ Saved: {after_report}")
                print()
                print("Compare reports to see improvement!")
            except Exception as e:
                print(f"  ⚠️  Could not generate after report: {e}")
    
    print("="*80)
    print("✅ Complete")
    print("="*80)
    print()
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
