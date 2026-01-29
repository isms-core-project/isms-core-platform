#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
Generator Script Lock Remover - Create Unlocked Generator Versions
================================================================================

PURPOSE:
Create unlocked versions of Excel generator scripts by removing sheet protection code.

STRATEGY:
You have:
  - generate_a84_1_repository_access.py (with protection code)
  - generate_a84_2_branch_protection.py (with protection code)
  - generate_a84_3_compliance_dashboard.py (with protection code)

You want:
  - Locked generators (keep originals as-is)
  - Unlocked generators (remove protection code)

USAGE:
    python3 remove_script_locks.py <input_script.py> <output_script.py>
    python3 remove_script_locks.py --batch <input_dir> <output_dir>
    python3 remove_script_locks.py --scan <script.py>

EXAMPLES:
    # Create unlocked version of single generator:
    python3 remove_script_locks.py \
        generate_a84_1_repository_access.py \
        generate_a84_1_repository_access_UNLOCKED.py
    
    # Batch process entire directory:
    python3 remove_script_locks.py --batch ./generators_locked/ ./generators_unlocked/
    
    # Scan to find protection code:
    python3 remove_script_locks.py --scan generate_a84_1_repository_access.py

OUTPUT:
    Creates generator scripts that produce workbooks WITHOUT sheet protection.

WHAT IT REMOVES:
    - ws.protection.sheet = True
    - ws.protection.password = '...'
    - ws.protection.enable()
    - SheetProtection() calls
    - Protection-related parameters

ISMS CONTROL: A.8.4 - Access to Source Code
DOCUMENT TYPE: Utility Script
CREATED: 2025-01-26

================================================================================
"""

import sys
import re
from pathlib import Path


def scan_script_for_protection(filepath):
    """
    Scan a Python script for sheet protection code.
    
    Returns:
        dict with protection code locations
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        return {'error': f"Failed to read file: {e}"}
    
    protection_patterns = []
    
    for line_num, line in enumerate(lines, start=1):
        # Pattern 1: ws.protection.sheet = True
        if re.search(r'\.protection\.sheet\s*=\s*True', line):
            protection_patterns.append({
                'line': line_num,
                'pattern': 'ws.protection.sheet = True',
                'code': line.strip()
            })
        
        # Pattern 2: ws.protection.password = '...'
        if re.search(r'\.protection\.password\s*=', line):
            protection_patterns.append({
                'line': line_num,
                'pattern': 'ws.protection.password',
                'code': line.strip()
            })
        
        # Pattern 3: ws.protection.enable()
        if re.search(r'\.protection\.enable\(\)', line):
            protection_patterns.append({
                'line': line_num,
                'pattern': 'ws.protection.enable()',
                'code': line.strip()
            })
        
        # Pattern 4: SheetProtection import
        if re.search(r'from openpyxl.*import.*SheetProtection', line):
            protection_patterns.append({
                'line': line_num,
                'pattern': 'SheetProtection import',
                'code': line.strip()
            })
        
        # Pattern 5: SheetProtection() usage
        if re.search(r'SheetProtection\(', line) and 'import' not in line:
            protection_patterns.append({
                'line': line_num,
                'pattern': 'SheetProtection() call',
                'code': line.strip()
            })
    
    return {
        'filename': Path(filepath).name,
        'protection_code_found': len(protection_patterns) > 0,
        'protection_lines': len(protection_patterns),
        'patterns': protection_patterns
    }


def remove_protection_code(content):
    """
    Remove sheet protection code from script content.
    
    Args:
        content: String content of Python script
        
    Returns:
        (modified_content, list of changes)
    """
    lines = content.split('\n')
    modified_lines = []
    changes = []
    
    for line_num, line in enumerate(lines, start=1):
        original_line = line
        skip_line = False
        change_reason = None
        
        # Pattern 1: ws.protection.sheet = True
        if re.search(r'\.protection\.sheet\s*=\s*True', line):
            skip_line = True
            change_reason = 'Removed: ws.protection.sheet = True'
        
        # Pattern 2: ws.protection.password = '...'
        elif re.search(r'\.protection\.password\s*=', line):
            skip_line = True
            change_reason = 'Removed: ws.protection.password'
        
        # Pattern 3: ws.protection.enable()
        elif re.search(r'\.protection\.enable\(\)', line):
            skip_line = True
            change_reason = 'Removed: ws.protection.enable()'
        
        # Pattern 4: SheetProtection import (comment out instead of remove)
        elif re.search(r'from openpyxl.*import.*SheetProtection', line):
            # Comment out the import
            line = '# ' + line + '  # REMOVED: Not needed for unlocked version'
            change_reason = 'Commented: SheetProtection import'
        
        # Pattern 5: SheetProtection() usage
        elif re.search(r'SheetProtection\(', line) and 'import' not in line:
            skip_line = True
            change_reason = 'Removed: SheetProtection() call'
        
        # Pattern 6: Lines that set individual protection properties
        elif re.search(r'\.protection\.(selectLockedCells|selectUnlockedCells|formatCells)', line):
            skip_line = True
            change_reason = 'Removed: Protection property setting'
        
        if change_reason:
            changes.append({
                'line': line_num,
                'original': original_line.strip(),
                'action': change_reason,
                'removed': skip_line
            })
        
        if not skip_line:
            modified_lines.append(line)
    
    return '\n'.join(modified_lines), changes


def process_script(input_path, output_path=None):
    """
    Process a generator script to remove protection code.
    
    Args:
        input_path: Path to input script (with protection)
        output_path: Path to output script (without protection)
        
    Returns:
        dict with results
    """
    input_path = Path(input_path)
    
    # Determine output path
    if output_path is None:
        # Create _UNLOCKED version
        output_path = input_path.parent / f"{input_path.stem}_UNLOCKED{input_path.suffix}"
    else:
        output_path = Path(output_path)
    
    # Read input file
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return {'success': False, 'error': f"Failed to read input: {e}"}
    
    # Remove protection code
    modified_content, changes = remove_protection_code(content)
    
    # Write output file
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(modified_content)
    except Exception as e:
        return {'success': False, 'error': f"Failed to write output: {e}"}
    
    # Add header comment to output file
    header_comment = f"""# ============================================================================
# UNLOCKED VERSION - Generated from {input_path.name}
# 
# This script generates Excel workbooks WITHOUT sheet protection.
# Use for: Internal testing, development, debugging
# 
# For protected workbooks, use: {input_path.name}
# ============================================================================

"""
    
    try:
        with open(output_path, 'r', encoding='utf-8') as f:
            current_content = f.read()
        
        # Add header after shebang/encoding lines if present
        lines = current_content.split('\n')
        insert_pos = 0
        
        # Skip shebang and encoding
        for i, line in enumerate(lines):
            if line.startswith('#!') or 'coding' in line or line.startswith('# -*-'):
                insert_pos = i + 1
            else:
                break
        
        lines.insert(insert_pos, header_comment)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(lines))
    except:
        pass  # Header is optional
    
    return {
        'success': True,
        'input_file': str(input_path),
        'output_file': str(output_path),
        'changes_made': len(changes),
        'changes': changes
    }


def batch_process_scripts(input_dir, output_dir, pattern="generate_a84_*.py"):
    """
    Batch process multiple generator scripts.
    
    Args:
        input_dir: Directory with locked generators
        output_dir: Directory for unlocked generators
        pattern: File pattern to match
        
    Returns:
        dict with batch results
    """
    input_dir = Path(input_dir)
    output_dir = Path(output_dir)
    
    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Find matching files
    files = sorted(input_dir.glob(pattern))
    
    if not files:
        return {
            'success': False,
            'error': f"No files matching '{pattern}' found in {input_dir}"
        }
    
    results = []
    success_count = 0
    failure_count = 0
    
    for input_file in files:
        # Create output filename
        output_file = output_dir / f"{input_file.stem}_UNLOCKED{input_file.suffix}"
        
        print(f"Processing: {input_file.name}...", end=" ")
        
        result = process_script(input_file, output_file)
        
        if result['success']:
            print(f"✅ Removed {result['changes_made']} protection line(s)")
            success_count += 1
        else:
            print(f"❌ Failed: {result['error']}")
            failure_count += 1
        
        results.append({
            'filename': input_file.name,
            'result': result
        })
    
    return {
        'success': True,
        'total_files': len(files),
        'successful': success_count,
        'failed': failure_count,
        'results': results
    }


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    
    mode = sys.argv[1]
    
    # Scan mode - find protection code
    if mode == '--scan':
        if len(sys.argv) < 3:
            print("Error: --scan requires a script path")
            sys.exit(1)
        
        filepath = sys.argv[2]
        
        print(f"Scanning: {filepath}")
        print("=" * 70)
        
        result = scan_script_for_protection(filepath)
        
        if 'error' in result:
            print(f"❌ Error: {result['error']}")
            sys.exit(1)
        
        print(f"File: {result['filename']}")
        print(f"Protection code found: {'Yes' if result['protection_code_found'] else 'No'}")
        print(f"Protection lines: {result['protection_lines']}")
        print()
        
        if result['protection_lines'] > 0:
            print("Protection code locations:")
            for pattern in result['patterns']:
                print(f"  Line {pattern['line']}: {pattern['pattern']}")
                print(f"    {pattern['code']}")
        else:
            print("✅ No protection code found - already an unlocked generator")
        
        sys.exit(0)
    
    # Batch mode - process directory
    elif mode == '--batch':
        if len(sys.argv) < 4:
            print("Error: --batch requires <input_dir> <output_dir>")
            sys.exit(1)
        
        input_dir = sys.argv[2]
        output_dir = sys.argv[3]
        
        print("=" * 70)
        print("BATCH UNLOCK - A.8.4 Generator Scripts")
        print("=" * 70)
        print(f"Input directory:  {input_dir}")
        print(f"Output directory: {output_dir}")
        print()
        
        result = batch_process_scripts(input_dir, output_dir)
        
        if not result['success']:
            print(f"❌ Error: {result['error']}")
            sys.exit(1)
        
        print()
        print("=" * 70)
        print("SUMMARY")
        print("=" * 70)
        print(f"Total files processed: {result['total_files']}")
        print(f"✅ Successful: {result['successful']}")
        print(f"❌ Failed: {result['failed']}")
        
        if result['successful'] > 0:
            print()
            print("Unlocked generator scripts created:")
            for item in result['results']:
                if item['result']['success']:
                    print(f"  📝 {Path(item['result']['output_file']).name}")
        
        sys.exit(0 if result['failed'] == 0 else 1)
    
    # Single file mode
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else None
        
        if not Path(input_file).exists():
            print(f"❌ Error: File not found: {input_file}")
            sys.exit(1)
        
        print("=" * 70)
        print("CREATE UNLOCKED GENERATOR - ISMS A.8.4")
        print("=" * 70)
        print(f"Input:  {input_file}")
        
        if output_file:
            print(f"Output: {output_file}")
        else:
            output_file = Path(input_file).stem + "_UNLOCKED" + Path(input_file).suffix
            print(f"Output: {output_file} (auto-generated name)")
        
        print()
        print("Removing protection code...", end=" ")
        
        result = process_script(input_file, output_file)
        
        if not result['success']:
            print(f"\n❌ Failed: {result['error']}")
            sys.exit(1)
        
        print("✅ Done!")
        print()
        print(f"Changes made: {result['changes_made']}")
        
        if result['changes_made'] > 0:
            print("\nProtection code removed:")
            for change in result['changes']:
                action = "❌ Removed" if change['removed'] else "💬 Commented"
                print(f"  {action} (line {change['line']}): {change['action']}")
        else:
            print("\n⚠️  No protection code found - script may already be unlocked")
        
        print(f"\n📁 Unlocked generator: {result['output_file']}")
        print()
        print("Next steps:")
        print(f"  1. Run: python3 {result['output_file']}")
        print(f"  2. Verify: Generated workbook has NO sheet protection")
        print(f"  3. Compare with output from: python3 {input_file}")
        
        sys.exit(0)


if __name__ == '__main__':
    main()
