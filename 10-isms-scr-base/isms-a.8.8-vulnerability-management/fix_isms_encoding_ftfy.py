#!/usr/bin/env python3
# =============================================================================
# SPDX-License-Identifier: AGPL-3.0-or-later OR LicenseRef-ISMS-Commercial
# Copyright (c) 2025-2026 ISMS Core Contributors
#
# This file is part of ISMS Core.
#
# ISMS Core is dual-licensed:
#   1. AGPL 3.0 (Open Source) - See LICENSE-AGPL.txt
#   2. Commercial License - Contact vendor for proprietary use
#
# You may use this file under either license, at your option.
# =============================================================================
"""
fix_isms_encoding_ftfy.py

Universal Unicode encoding fixer using the ftfy library.
Automatically detects and repairs mojibake (UTF-8 double-encoding) in Python files.

Features:
- Recursive directory scanning
- AUTOMATIC BACKUPS (creates .bak files before modifying)
- Detailed reporting with corruption examples
- Summary statistics
- Export report to file

Usage:
    # Fix single file (auto-backup to script.py.bak)
    python3 fix_isms_encoding_ftfy.py --dry-run *.py
    python3 fix_isms_encoding_ftfy.py script.py
    python3 fix_isms_encoding_ftfy.py *.py
    
    python3 fix_isms_encoding_ftfy.py ./10_generator_utf --dry-run
    python3 fix_isms_encoding_ftfy.py ./ --dry-run
    
    # Fix all .py files in current directory
    python3 fix_isms_encoding_ftfy.py *.py
    
    # Recursively scan directory
    python3 fix_isms_encoding_ftfy.py --recursive /path/to/scripts
    python3 fix_isms_encoding_ftfy.py --recursive ./10_generator_utf

    # Scan current directory recursively
    python3 fix_isms_encoding_ftfy.py --recursive .
    
    # Preview with detailed report (no backup needed)
    python3 fix_isms_encoding_ftfy.py --dry-run --report corruption_report.txt --recursive .
    
    # Fix with report
    python3 fix_isms_encoding_ftfy.py --report fixed.txt --recursive .
    
    # Skip backup (NOT RECOMMENDED)
    python3 fix_isms_encoding_ftfy.py --no-backup script.py

Author: Greg & Claude AI
Date: 2026-01-16
Purpose: Fix encoding issues in ISMS automation scripts
"""

# =============================================================================
# Standard Library Imports
# =============================================================================
import logging
import sys
import argparse
import shutil
from pathlib import Path
from datetime import datetime
from typing import List, Dict

# =============================================================================
# Logging Configuration
# =============================================================================
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
logger = logging.getLogger(__name__)


try:
    import ftfy
except ImportError:
    print("Error: ftfy library not installed")
    print("Install with: pip install ftfy --break-system-packages")
    sys.exit(1)


def find_python_files(path: Path, recursive: bool = False) -> List[Path]:
    """Find all Python files in path."""
    files = []
    
    if path.is_file():
        if path.suffix == '.py':
            return [path]
        return []
    
    if not path.is_dir():
        return []
    
    if recursive:
        files = list(path.rglob('*.py'))
    else:
        files = list(path.glob('*.py'))
    
    # Filter out __pycache__ and other common excludes
    excluded = {'__pycache__', '.git', '.venv', 'venv', 'node_modules', '.tox', 'dist', 'build'}
    files = [f for f in files if not any(excl in f.parts for excl in excluded)]
    
    # Also filter out backup files
    files = [f for f in files if not f.name.endswith('.bak')]
    
    return files


def get_corruption_sample(original: str, fixed: str, max_samples: int = 5) -> List[Dict[str, str]]:
    """Extract examples of corrupted text that was fixed."""
    samples = []
    
    # Split into lines and compare
    orig_lines = original.split('\n')
    fixed_lines = fixed.split('\n')
    
    for i, (orig, fix) in enumerate(zip(orig_lines, fixed_lines), 1):
        if orig != fix and len(samples) < max_samples:
            # Find the differences
            if len(orig) < 200 and len(fix) < 200:  # Only show reasonable length
                samples.append({
                    'line': i,
                    'before': orig.strip(),
                    'after': fix.strip()
                })
    
    return samples


def create_backup(filepath: Path) -> Path:
    """Create backup of file with .bak extension."""
    backup_path = filepath.with_suffix(filepath.suffix + '.bak')
    
    # If backup already exists, add timestamp
    if backup_path.exists():
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_path = filepath.with_suffix(f'.{timestamp}.bak')
    
    shutil.copy2(filepath, backup_path)
    return backup_path


def fix_file(filepath: Path, dry_run: bool = False, show_samples: bool = False, 
             do_backup: bool = True) -> Dict:
    """Fix mojibake in a single file using ftfy."""
    result = {
        'path': filepath,
        'success': False,
        'changed': False,
        'error': None,
        'samples': [],
        'backup_path': None
    }
    
    try:
        # Read file
        with open(filepath, 'r', encoding='utf-8') as f:
            original = f.read()
        
        # Fix using ftfy
        fixed = ftfy.fix_text(original)
        
        # Check if anything changed
        if fixed == original:
            result['success'] = True
            return result
        
        result['changed'] = True
        
        # Get corruption samples if requested
        if show_samples:
            result['samples'] = get_corruption_sample(original, fixed)
        
        if dry_run:
            result['success'] = True
            return result
        
        # Create backup before modifying
        if do_backup:
            try:
                backup_path = create_backup(filepath)
                result['backup_path'] = backup_path
            except Exception as e:
                result['error'] = f"Backup failed: {e}"
                return result
        
        # Write fixed file
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(fixed)
        
        result['success'] = True
        
    except Exception as e:
        result['error'] = str(e)
    
    return result


def generate_report(results: List[Dict], report_file: Path, dry_run: bool, backup_enabled: bool):
    """Generate detailed report of encoding fixes."""
    
    with open(report_file, 'w', encoding='utf-8') as f:
        # Header
        f.write("=" * 80 + "\n")
        f.write("ISMS ENCODING FIX REPORT\n")
        f.write("=" * 80 + "\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"Mode: {'DRY RUN (preview only)' if dry_run else 'ACTUAL FIX'}\n")
        f.write(f"Backup: {'Enabled' if backup_enabled else 'DISABLED'}\n")
        f.write("\n")
        
        # Summary
        total = len(results)
        successful = sum(1 for r in results if r['success'])
        fixed = sum(1 for r in results if r['changed'])
        failed = sum(1 for r in results if not r['success'])
        backed_up = sum(1 for r in results if r.get('backup_path'))
        
        f.write("SUMMARY\n")
        f.write("-" * 80 + "\n")
        f.write(f"Total files processed: {total}\n")
        f.write(f"Files with corruption: {fixed}\n")
        f.write(f"Files already clean:   {successful - fixed}\n")
        f.write(f"Failed to process:     {failed}\n")
        if backed_up > 0:
            f.write(f"Backups created:       {backed_up}\n")
        f.write("\n")
        
        # Detailed results for changed files
        if fixed > 0:
            f.write("FILES WITH ENCODING ISSUES\n")
            f.write("=" * 80 + "\n\n")
            
            for result in results:
                if result['changed']:
                    f.write(f"File: {result['path']}\n")
                    if result.get('backup_path'):
                        f.write(f"Backup: {result['backup_path']}\n")
                    f.write("-" * 80 + "\n")
                    
                    if result['samples']:
                        f.write("Corruption examples:\n\n")
                        for sample in result['samples']:
                            f.write(f"  Line {sample['line']}:\n")
                            f.write(f"    BEFORE: {sample['before']}\n")
                            f.write(f"    AFTER:  {sample['after']}\n\n")
                    else:
                        f.write("  (Corruption detected, run with --verbose for examples)\n")
                    
                    f.write("\n")
        
        # Backup instructions
        if backed_up > 0 and not dry_run:
            f.write("BACKUP RESTORATION\n")
            f.write("=" * 80 + "\n\n")
            f.write("If you need to restore original files:\n\n")
            for result in results:
                if result.get('backup_path'):
                    f.write(f"  cp {result['backup_path']} {result['path']}\n")
            f.write("\nOr to restore all backups:\n")
            f.write("  for f in *.bak; do cp \"$f\" \"${f%.bak}\"; done\n\n")
        
        # Failed files
        if failed > 0:
            f.write("FAILED FILES\n")
            f.write("=" * 80 + "\n\n")
            
            for result in results:
                if not result['success']:
                    f.write(f"File: {result['path']}\n")
                    f.write(f"Error: {result['error']}\n\n")
        
        # Footer
        f.write("=" * 80 + "\n")
        f.write('"The first principle is that you must not fool yourself\n')
        f.write('and you are the easiest person to fool." - Richard Feynman\n')
        f.write("\n")
        f.write("Anti-cargo-cult ISMS: Evidence-based compliance automation\n")
        f.write("=" * 80 + "\n")


def main():
    parser = argparse.ArgumentParser(
        description='Fix Unicode encoding corruption in Python files using ftfy',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s script.py                    # Fix single file (auto-backup)
  %(prog)s *.py                         # Fix all .py in current dir
  %(prog)s -r /path/to/scripts          # Recursively scan directory
  %(prog)s -r . --dry-run               # Preview recursive scan
  %(prog)s -r . --report report.txt     # Generate report file
  %(prog)s -r . -d --report preview.txt # Dry run with report
  
BACKUP: By default, creates .bak files before modifying.
Use --no-backup to skip (NOT RECOMMENDED for production files).
        """
    )
    
    parser.add_argument(
        'paths',
        nargs='*',
        default=['.'],
        help='Files or directories to process (default: current directory)'
    )
    
    parser.add_argument(
        '-r', '--recursive',
        action='store_true',
        help='Recursively scan directories for Python files'
    )
    
    parser.add_argument(
        '-d', '--dry-run',
        action='store_true',
        help='Preview changes without modifying files'
    )
    
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Show detailed output including corruption examples'
    )
    
    parser.add_argument(
        '--report',
        type=str,
        metavar='FILE',
        help='Generate detailed report to FILE'
    )
    
    parser.add_argument(
        '--no-backup',
        action='store_true',
        help='Skip creating .bak backup files (NOT RECOMMENDED)'
    )
    
    args = parser.parse_args()
    
    # Banner
    print("=" * 80)
    print("ISMS Encoding Fix Utility (ftfy-powered)")
    print("Automatically detects and repairs UTF-8 mojibake")
    print("=" * 80)
    
    if args.dry_run:
        print("\nDRY RUN MODE - No files will be modified\n")
    elif args.no_backup:
        print("\nWARNING: Backup disabled - original files will be overwritten!\n")
    else:
        print("\nBackup enabled - .bak files will be created\n")
    
    # Collect files
    all_files = []
    
    for path_str in args.paths:
        path = Path(path_str)
        
        if not path.exists():
            print(f"Warning: Path does not exist: {path}")
            continue
        
        if path.is_file():
            if path.suffix == '.py':
                all_files.append(path)
        else:
            files = find_python_files(path, args.recursive)
            all_files.extend(files)
    
    if not all_files:
        print("\nNo Python files found\n")
        return 1
    
    # Remove duplicates and sort
    all_files = sorted(set(all_files))
    
    if args.recursive:
        print(f"\nRecursively scanned for Python files")
    
    print(f"Found {len(all_files)} Python file(s) to process\n")
    
    # Process files
    results = []
    show_samples = args.verbose or args.report
    do_backup = not args.no_backup and not args.dry_run
    
    for filepath in all_files:
        if args.verbose or (not args.recursive and len(all_files) < 20):
            print(f"  {filepath}...", end=' ')
        elif args.recursive and len(all_files) >= 20:
            # For large recursive scans, show progress every 10 files
            if len(results) % 10 == 0:
                print(f"  Progress: {len(results)}/{len(all_files)} files processed...", end='\r')
        
        result = fix_file(filepath, dry_run=args.dry_run, show_samples=show_samples, 
                         do_backup=do_backup)
        results.append(result)
        
        if args.verbose or (not args.recursive and len(all_files) < 20):
            if result['success']:
                if result['changed']:
                    status = "FIXED" if not args.dry_run else "WOULD FIX"
                    print(status, end='')
                    if result.get('backup_path'):
                        print(f" (backup: {result['backup_path'].name})")
                    else:
                        print()
                    
                    # Show samples in verbose mode
                    if args.verbose and result['samples']:
                        for sample in result['samples'][:2]:  # Show first 2
                            print(f"    Line {sample['line']}: {sample['before'][:60]}...")
                else:
                    print("OK")
            else:
                print(f"ERROR: {result['error']}")
    
    if args.recursive and len(all_files) >= 20:
        print()  # Clear progress line
    
    # Summary
    print("\n" + "=" * 80)
    print("SUMMARY")
    print("=" * 80)
    
    successful = sum(1 for r in results if r['success'])
    fixed_count = sum(1 for r in results if r['success'] and r['changed'])
    failed = sum(1 for r in results if not r['success'])
    backed_up = sum(1 for r in results if r.get('backup_path'))
    
    print(f"\nProcessed: {len(results)} files")
    print(f"Fixed: {fixed_count} files")
    print(f"Already correct: {successful - fixed_count}")
    
    if backed_up > 0:
        print(f"Backups created: {backed_up} (.bak files)")
    
    if failed > 0:
        print(f"Failed: {failed}")
    
    # Generate report if requested
    if args.report:
        report_path = Path(args.report)
        generate_report(results, report_path, args.dry_run, do_backup)
        print(f"\nReport saved to: {report_path}")
    
    if args.dry_run and fixed_count > 0:
        print(f"\nRun without --dry-run to fix {fixed_count} file(s)")
    elif fixed_count > 0 and not args.dry_run:
        print(f"\nSuccessfully fixed {fixed_count} file(s)!")
        if backed_up > 0:
            print(f"\nTo restore originals: for f in *.bak; do cp \"$f\" \"${{f%.bak}}\"; done")
    elif fixed_count == 0:
        print("\nAll files have correct encoding!")
    
    print("\n" + "=" * 80)
    print('\n"The first principle is that you must not fool yourself')
    print('and you are the easiest person to fool." - Richard Feynman')
    print("\nAnti-cargo-cult ISMS: Evidence-based compliance automation")
    print("=" * 80 + "\n")
    
    return 0 if failed == 0 else 1


if __name__ == '__main__':
    sys.exit(main())

# =============================================================================
# QA_VERIFIED: 2026-01-31
# QA_STATUS: PASSED (syntax validated, structure verified)
# QA_TOOL: Claude Code Deep Scan
# QA_NOTE: STANDARDIZATION - License header, logging, main() pattern applied
# =============================================================================
