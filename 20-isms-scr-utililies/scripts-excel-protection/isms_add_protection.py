#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
ISMS Framework - Sheet Protection Utility (v2 - Simplified & Robust)
================================================================================

Automatically adds sheet protection to ISMS assessment generator scripts.

**Usage:**
    # Add protection to single script
    python3 add_sheet_protection.py generate_a824_1.py
    
    # Dry run (preview changes without modifying)
    python3 add_sheet_protection.py --dry-run generate_a824_1.py
    
    # Process all scripts in directory
    python3 add_sheet_protection.py --all

**What It Does:**
1. Finds all functions that create sheets
2. Adds `ws.protection.sheet = True` at the end of each function
3. Creates .bak backup before modifying
4. Shows clear summary of changes

**Patterns Detected:**
- def create_*_sheet(ws):          # A.5.9 pattern
- def create_*(ws, styles):        # A.8.24 pattern  
- def create_*_*(ws, styles):      # Any create function

================================================================================
"""

import sys
import os
import re

def add_protection_to_script(filepath, dry_run=False):
    """Add sheet protection to all create functions in a script."""
    
    if not os.path.exists(filepath):
        print(f"❌ Error: File not found: {filepath}")
        return False
    
    print(f"\n{'='*80}")
    print(f"Processing: {os.path.basename(filepath)}")
    print(f"{'='*80}\n")
    
    # Read original file
    with open(filepath, 'r', encoding='utf-8') as f:
        original_lines = f.readlines()
    
    # Find all create functions
    create_functions = []
    for i, line in enumerate(original_lines):
        # Match: def create_XXXX(ws): or def create_XXXX(ws, styles):
        if re.match(r'\s*def create_\w+\(ws[,\)]', line):
            func_name = re.search(r'def (create_\w+)\(', line).group(1)
            create_functions.append((i, func_name))
    
    if not create_functions:
        print("⚠️  No sheet creation functions found")
        print("   (Looking for: def create_*(ws...) pattern)\n")
        return False
    
    print(f"Found {len(create_functions)} sheet creation functions:")
    for _, func_name in create_functions:
        print(f"  - {func_name}()")
    print()
    
    # Process each function
    modified_lines = original_lines.copy()
    changes_made = 0
    offset = 0  # Track line number changes from insertions
    
    print("Adding sheet protection...")
    
    for func_line_num, func_name in create_functions:
        # Find end of this function (next def or end of file)
        func_start = func_line_num + offset
        func_end = len(modified_lines) - 1
        
        for i in range(func_start + 1, len(modified_lines)):
            # Found next function definition
            if re.match(r'\s*def \w+\(', modified_lines[i]):
                func_end = i - 1
                break
        
        # Check if protection already exists in this function
        has_protection = False
        for i in range(func_start, func_end + 1):
            line_stripped = modified_lines[i].strip()
            if 'ws.protection.sheet = True' in line_stripped and not line_stripped.startswith('#'):
                has_protection = True
                break
        
        if has_protection:
            print(f"  ⊘ Skipped {func_name}() (already protected)")
            continue
        
        # Find last non-empty, non-comment line in function
        insert_after = func_end
        for i in range(func_end, func_start, -1):
            stripped = modified_lines[i].strip()
            if stripped and not stripped.startswith('#'):
                insert_after = i
                break
        
        # Determine indentation (use same as function body)
        indent = '    '  # Default
        for i in range(func_start + 1, min(func_start + 10, len(modified_lines))):
            stripped = modified_lines[i].strip()
            if stripped and not stripped.startswith('#') and not stripped.startswith('"""'):
                # Get leading whitespace
                indent = modified_lines[i][:len(modified_lines[i]) - len(modified_lines[i].lstrip())]
                break
        
        # Insert protection line
        protection_line = f"{indent}ws.protection.sheet = True\n"
        modified_lines.insert(insert_after + 1, '\n')
        modified_lines.insert(insert_after + 2, protection_line)
        
        print(f"  ✓ Added to {func_name}()")
        changes_made += 1
        offset += 2  # Account for 2 new lines
    
    print()
    
    if changes_made == 0:
        print("✓ All functions already have sheet protection\n")
        return True
    
    print(f"Summary: Added protection to {changes_made}/{len(create_functions)} functions\n")
    
    if dry_run:
        print("⚠️  DRY RUN MODE - No files modified")
        print("\nPreview of changes (first 5):")
        print("-" * 80)
        preview_count = 0
        for i, (orig, mod) in enumerate(zip(original_lines, modified_lines)):
            if orig != mod and preview_count < 5:
                print(f"Line {i+1}:  {mod.rstrip()}")
                preview_count += 1
        if preview_count == 0:
            print("(No line-by-line differences to show)")
        print()
        return True
    
    # Create backup
    backup_path = f"{filepath}.bak"
    with open(backup_path, 'w', encoding='utf-8') as f:
        f.writelines(original_lines)
    print(f"✓ Backup created: {backup_path}")
    
    # Write modified file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(modified_lines)
    print(f"✓ File updated: {filepath}\n")
    
    return True


def process_all_scripts(directory='.', dry_run=False):
    """Process all generator scripts in directory."""
    
    scripts = [f for f in os.listdir(directory) 
               if f.startswith('generate_') and f.endswith('.py')]
    
    if not scripts:
        print("❌ No generator scripts found (generate_*.py)")
        return False
    
    print(f"\n{'='*80}")
    print(f"Found {len(scripts)} generator scripts in {directory}")
    print(f"{'='*80}")
    
    success_count = 0
    for script in sorted(scripts):
        filepath = os.path.join(directory, script)
        if add_protection_to_script(filepath, dry_run):
            success_count += 1
    
    print(f"\n{'='*80}")
    print("SUMMARY")
    print(f"{'='*80}")
    print(f"Processed: {success_count}/{len(scripts)} scripts successfully")
    if dry_run:
        print("Mode: DRY RUN (no files modified)")
    else:
        print("Mode: LIVE (files modified, .bak backups created)")
    print()
    
    return True


def main():
    """Main execution."""
    
    print("="*80)
    print("ISMS Framework - Sheet Protection Utility v2")
    print("="*80)
    
    # Parse arguments
    dry_run = '--dry-run' in sys.argv
    all_scripts = '--all' in sys.argv
    
    if '--help' in sys.argv or len(sys.argv) == 1:
        print(__doc__)
        return 0
    
    if dry_run:
        print("\n⚠️  DRY RUN MODE - No files will be modified\n")
    
    if all_scripts:
        directory = '.'
        for arg in sys.argv:
            if arg.startswith('--dir='):
                directory = arg.split('=')[1]
        process_all_scripts(directory, dry_run)
    else:
        # Process specific script
        script_file = None
        for arg in sys.argv[1:]:
            if not arg.startswith('--'):
                script_file = arg
                break
        
        if script_file:
            add_protection_to_script(script_file, dry_run)
        else:
            print("❌ No script file specified\n")
            print("Usage:")
            print("  python3 add_sheet_protection.py <script.py>")
            print("  python3 add_sheet_protection.py --all")
            print("  python3 add_sheet_protection.py --dry-run <script.py>")
            return 1
    
    print("="*80)
    print("✅ Complete")
    print("="*80)
    print()
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
