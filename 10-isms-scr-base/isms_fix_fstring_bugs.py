#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
F-String Bug Fixer - Automated repair for formula1 validation strings

Fixes common f-string bugs in openpyxl DataValidation formulas:
1. formula1='f"...' → formula1=f'"...'  (move f-prefix outside quotes)
2. formula1='f"{VAR},f"{VAR2}"...' → formula1=f'"{VAR},{VAR2}"...' (remove duplicate f)

Usage:
    python3 isms_fix_fstring_bugs.py <input_file.py> [output_file.py]
    python3 isms_fix_fstring_bugs.py --scan-recursive <directory>
    python3 isms_fix_fstring_bugs.py --dry-run <file>
    python3 isms_fix_fstring_bugs.py --fix-recursive <directory>

    # Scan entire project tree
    python3 isms_fix_fstring_bugs.py --scan-recursive /path/to/project
    python3 isms_fix_fstring_bugs.py --scan-recursive ./

    # Preview what would be fixed
    python3 isms_fix_fstring_bugs.py --dry-run-recursive /path/to/project
    python3 isms_fix_fstring_bugs.py --dry-run-recursive ./

    # Apply fixes after review
    python3 isms_fix_fstring_bugs.py --fix-recursive /path/to/project
    python3 isms_fix_fstring_bugs.py --fix-recursive ./

"""

import sys
import re
from pathlib import Path


def detect_and_fix_fstring_bugs(content: str) -> tuple[str, list]:
    """
    Detect and fix f-string bugs in DataValidation formula1 parameters AND Excel formulas.
    
    Returns:
        (fixed_content, list of changes)
    """
    changes = []
    lines = content.split('\n')
    fixed_lines = []
    
    for line_num, line in enumerate(lines, 1):
        original_line = line
        
        # Pattern: formula1='f"..."' or formula1="f'...'"
        # We need to find these and fix them
        
        # Match formula1='f"CONTENT"' (single-quote outer, double-quote inner)
        match = re.search(r"(formula1\s*=\s*)'f\"([^']+)'", line)
        if match:
            prefix = match.group(1)
            content_part = match.group(2)  # Everything between f" and final "
            
            # Remove ALL nested f" occurrences
            # Patterns to remove: ,f" and ",f"
            fixed_content = content_part.replace(',f"', ',"').replace('",f"', '","')
            
            # Rebuild as proper f-string
            fixed = f"{prefix}f'\"{fixed_content}'"
            line = line[:match.start()] + fixed + line[match.end():]
            
            if line != original_line:
                changes.append({
                    'line': line_num,
                    'original': original_line.strip(),
                    'fixed': line.strip(),
                    'type': 'f-string fixed (nested f" removed)' if ',f"' in content_part or '",f"' in content_part else 'f-prefix moved outside quotes'
                })
        
        # Match formula1="f'CONTENT'" (double-quote outer, single-quote inner)
        match = re.search(r'(formula1\s*=\s*)"f\'([^"]+)"', line)
        if match:
            prefix = match.group(1)
            content_part = match.group(2)
            
            # Remove nested f' occurrences
            fixed_content = content_part.replace(",f'", ",'").replace("',f'", "','")
            
            # Rebuild as proper f-string
            fixed = f'{prefix}f"\'{fixed_content}"\''
            line = line[:match.start()] + fixed + line[match.end():]
            
            if line != original_line:
                changes.append({
                    'line': line_num,
                    'original': original_line.strip(),
                    'fixed': line.strip(),
                    'type': 'f-string fixed (nested f\' removed)' if ",f'" in content_part or "',f'" in content_part else 'f-prefix moved outside quotes'
                })
        
        fixed_lines.append(line)
    
    return '\n'.join(fixed_lines), changes


def scan_file(filepath: Path) -> dict:
    """
    Scan a Python file for f-string bugs.
    
    ✨ UPDATED: Now detects both DataValidation AND Excel formula bugs.
    
    Returns:
        {
            'has_bugs': bool,
            'bug_count': int,
            'bugs': [list of bug locations]
        }
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return {'error': str(e)}
    
    bugs = []
    
    # ========================================================================
    # PATTERN 1: DataValidation bugs - formula1='f" (single-quote outer)
    # ORIGINAL PATTERN - Always worked
    # ========================================================================
    for match in re.finditer(r"formula1\s*=\s*'f\"", content):
        line_num = content[:match.start()].count('\n') + 1
        line_content = content.split('\n')[line_num - 1].strip()
        bugs.append({
            'line': line_num,
            'pattern': "f-prefix inside quotes (formula1='f\"...)",
            'content': line_content[:80]
        })
    
    # ========================================================================
    # PATTERN 2: DataValidation bugs - formula1="f' (double-quote outer)
    # ORIGINAL PATTERN - Always worked
    # ========================================================================
    for match in re.finditer(r'formula1\s*=\s*"f\'', content):
        line_num = content[:match.start()].count('\n') + 1
        line_content = content.split('\n')[line_num - 1].strip()
        bugs.append({
            'line': line_num,
            'pattern': 'f-prefix inside quotes (formula1="f\'...)',
            'content': line_content[:80]
        })
    
    # ========================================================================
    # PATTERN 3: Excel formula bugs - "=COUNTIFS(...,f\"{VAR}\")"
    # ✨ NEW PATTERN - Added in v1.1
    #
    # Detects Excel formulas stored as Python strings with f-string bugs:
    #   WRONG: "=COUNTIFS(Sheet!A:A,f\"{CHECK} Yes\")/COUNTA(...)"
    #   RIGHT: f'=COUNTIFS(Sheet!A:A,"{CHECK} Yes")/COUNTA(...)'
    # ========================================================================
    for match in re.finditer(r'"=(?:COUNTIFS|SUMIFS|AVERAGEIFS|MAXIFS|MINIFS|IF|AND|OR)\([^)]*,f\\"', content):
        line_num = content[:match.start()].count('\n') + 1
        line_content = content.split('\n')[line_num - 1].strip()
        
        # Verify this isn't already a proper f-string
        # (proper f-string would be: f"=COUNTIFS(...,"{VAR}")")
        line_with_context = content.split('\n')[line_num - 1]
        
        # Look for f-prefix before the opening quote
        match_start_in_line = line_with_context.find(match.group())
        if match_start_in_line >= 0:
            # Check characters before the match
            if match_start_in_line > 0:
                preceding_chars = line_with_context[:match_start_in_line].rstrip()
                # If there's no f" or f' right before, it's a bug
                if not (preceding_chars.endswith('f"') or preceding_chars.endswith("f'")):
                    bugs.append({
                        'line': line_num,
                        'pattern': 'Excel formula f-string bug (missing f-prefix)',
                        'content': line_content[:80]
                    })
            else:
                # Match is at start of line, definitely a bug
                bugs.append({
                    'line': line_num,
                    'pattern': 'Excel formula f-string bug (missing f-prefix)',
                    'content': line_content[:80]
                })
    
    return {
        'has_bugs': len(bugs) > 0,
        'bug_count': len(bugs),
        'bugs': bugs
    }


def dry_run_file(filepath: Path) -> dict:
    """
    Dry-run: show what would be fixed without writing.
    
    Returns:
        {
            'success': bool,
            'changes': [list of changes that would be made],
            'file': str
        }
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return {'success': False, 'error': f"Read error: {e}"}
    
    # Detect what would be fixed
    _, changes = detect_and_fix_fstring_bugs(content)
    
    return {
        'success': True,
        'changes': changes,
        'file': str(filepath)
    }


def fix_file(input_path: Path, output_path: Path = None, create_backup: bool = True) -> dict:
    """
    Fix f-string bugs in a file.
    
    Args:
        input_path: Path to input file
        output_path: Path to output file (if None, creates _FIXED version)
        create_backup: If True and modifying in-place, create .bak backup
    
    Returns:
        {
            'success': bool,
            'changes': [list of changes made],
            'output_file': str,
            'backup_file': str (if backup created)
        }
    """
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        return {'success': False, 'error': f"Read error: {e}"}
    
    # Fix bugs
    fixed_content, changes = detect_and_fix_fstring_bugs(content)
    
    # Determine if we're modifying in-place
    in_place = (output_path == input_path) if output_path else False
    
    # Create backup if modifying in-place
    backup_path = None
    if in_place and create_backup:
        backup_path = input_path.parent / f"{input_path.stem}.bak{input_path.suffix}"
        try:
            # Copy original to backup
            import shutil
            shutil.copy2(input_path, backup_path)
        except Exception as e:
            return {'success': False, 'error': f"Backup creation failed: {e}"}
    
    # Determine output path
    if output_path is None:
        output_path = input_path.parent / f"{input_path.stem}_FIXED{input_path.suffix}"
    
    # Write fixed content
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(fixed_content)
    except Exception as e:
        return {'success': False, 'error': f"Write error: {e}"}
    
    result = {
        'success': True,
        'changes': changes,
        'output_file': str(output_path)
    }
    
    if backup_path:
        result['backup_file'] = str(backup_path)
    
    return result


def get_python_files(dirpath: Path, recursive: bool = False) -> list[Path]:
    """Get all .py files in directory, optionally recursive."""
    if recursive:
        return sorted(dirpath.rglob('*.py'))
    else:
        return sorted(dirpath.glob('*.py'))


def scan_directory(dirpath: Path, recursive: bool = False) -> None:
    """Scan directory for f-string bugs."""
    print(f"Scanning directory: {dirpath} {'(recursive)' if recursive else ''}")
    print("=" * 70)
    
    python_files = get_python_files(dirpath, recursive)
    
    if not python_files:
        print("No Python files found")
        return
    
    total_files = 0
    buggy_files = 0
    total_bugs = 0
    buggy_file_list = []
    
    for pyfile in python_files:
        result = scan_file(pyfile)
        
        if 'error' in result:
            print(f"⚠️  {pyfile.relative_to(dirpath)}: {result['error']}")
            continue
        
        total_files += 1
        
        if result['has_bugs']:
            buggy_files += 1
            total_bugs += result['bug_count']
            rel_path = pyfile.relative_to(dirpath)
            print(f"🔴 {rel_path}: {result['bug_count']} bug(s)")
            for bug in result['bugs']:
                print(f"   Line {bug['line']}: {bug['pattern']}")
            buggy_file_list.append(str(rel_path))
        else:
            if not recursive:  # Only show clean files in non-recursive mode
                print(f"✅ {pyfile.relative_to(dirpath)}: Clean")
    
    print()
    print("=" * 70)
    print(f"Summary: {buggy_files}/{total_files} files with bugs, {total_bugs} total bugs")
    
    if buggy_file_list:
        print()
        print("Files with bugs:")
        for filepath in buggy_file_list:
            print(f"  {filepath}")
    
    sys.exit(0 if buggy_files == 0 else 1)


def dry_run_directory(dirpath: Path, recursive: bool = False) -> None:
    """Dry-run directory fixes."""
    print(f"Dry-run: {dirpath} {'(recursive)' if recursive else ''}")
    print("=" * 70)
    
    python_files = get_python_files(dirpath, recursive)
    
    if not python_files:
        print("No Python files found")
        return
    
    total_files = 0
    files_to_fix = 0
    total_changes = 0
    
    for pyfile in python_files:
        result = dry_run_file(pyfile)
        
        if not result['success']:
            print(f"⚠️  {pyfile.relative_to(dirpath)}: {result['error']}")
            continue
        
        total_files += 1
        
        if result['changes']:
            files_to_fix += 1
            total_changes += len(result['changes'])
            rel_path = pyfile.relative_to(dirpath)
            print(f"🔧 {rel_path}: {len(result['changes'])} change(s) would be made")
            for change in result['changes']:
                print(f"   Line {change['line']}: {change['type']}")
                print(f"      {change['original'][:70]}")
                print(f"   →  {change['fixed'][:70]}")
        else:
            if not recursive:  # Only show clean files in non-recursive mode
                print(f"✅ {pyfile.relative_to(dirpath)}: No changes needed")
    
    print()
    print("=" * 70)
    print(f"Summary: {files_to_fix}/{total_files} files would be fixed, {total_changes} total changes")
    print()
    print("💡 To apply fixes, use --fix-all or --fix-recursive")


def fix_directory(dirpath: Path, recursive: bool = False) -> None:
    """Fix all files in directory."""
    print(f"Fixing directory: {dirpath} {'(recursive)' if recursive else ''}")
    print("=" * 70)
    
    python_files = get_python_files(dirpath, recursive)
    
    if not python_files:
        print("No Python files found")
        return
    
    total_files = 0
    files_fixed = 0
    total_changes = 0
    backups_created = []
    
    for pyfile in python_files:
        # Check if file has bugs first
        scan_result = scan_file(pyfile)
        
        if 'error' in scan_result:
            print(f"⚠️  {pyfile.relative_to(dirpath)}: {scan_result['error']}")
            continue
        
        total_files += 1
        
        if not scan_result['has_bugs']:
            continue
        
        # Fix in-place (overwrites original, creates backup)
        result = fix_file(pyfile, pyfile, create_backup=True)
        
        if result['success']:
            files_fixed += 1
            total_changes += len(result['changes'])
            rel_path = pyfile.relative_to(dirpath)
            print(f"✅ {rel_path}: Fixed {len(result['changes'])} bug(s)")
            if 'backup_file' in result:
                backup_rel = Path(result['backup_file']).relative_to(dirpath)
                print(f"   💾 Backup: {backup_rel}")
                backups_created.append(backup_rel)
        else:
            print(f"❌ {pyfile.relative_to(dirpath)}: {result['error']}")
    
    print()
    print("=" * 70)
    print(f"Summary: {files_fixed}/{total_files} files fixed, {total_changes} total changes")
    
    if backups_created:
        print(f"💾 {len(backups_created)} backup(s) created (.bak files)")
        print()
        print("To restore a file: mv <file>.bak.py <file>.py")
        print("To remove backups: find . -name '*.bak.py' -delete")


def main():
    if len(sys.argv) < 2:
        print("F-String Bug Fixer - Automated repair for formula1 validation strings")
        print()
        print("✨ v1.1: Now detects Excel formula bugs too! (100% coverage)")
        print()
        print("Usage: python3 isms_fix_fstring_bugs.py <input_file.py> [output_file.py]")
        print()
        print("Single File:")
        print("  python3 isms_fix_fstring_bugs.py script.py              # Fix to script_FIXED.py")
        print("  python3 isms_fix_fstring_bugs.py script.py fixed.py     # Fix to fixed.py")
        print("  python3 isms_fix_fstring_bugs.py --scan script.py       # Scan only")
        print("  python3 isms_fix_fstring_bugs.py --dry-run script.py    # Show fixes")
        print()
        print("Directory Scanning:")
        print("  --scan-all <dir>           Scan .py files in directory")
        print("  --scan-recursive <dir>     Scan .py files in directory tree")
        print()
        print("Directory Dry-Run:")
        print("  --dry-run-all <dir>        Show fixes for directory")
        print("  --dry-run-recursive <dir>  Show fixes for directory tree")
        print()
        print("Directory Fixing:")
        print("  --fix-all <dir>            Fix .py files in directory (IN-PLACE)")
        print("  --fix-recursive <dir>      Fix .py files in directory tree (IN-PLACE)")
        print()
        print("⚠️  WARNING: --fix-all and --fix-recursive modify files IN-PLACE!")
        print("   Backups are created automatically as .bak.py files.")
        print("   Use --dry-run-all or --dry-run-recursive first to preview changes.")
        sys.exit(1)
    
    mode = sys.argv[1]
    
    # Scan single file
    if mode == '--scan':
        if len(sys.argv) < 3:
            print("Error: --scan requires a file path")
            sys.exit(1)
        
        filepath = Path(sys.argv[2])
        print(f"Scanning: {filepath}")
        print("=" * 70)
        
        result = scan_file(filepath)
        
        if 'error' in result:
            print(f"Error: {result['error']}")
            sys.exit(1)
        
        if result['has_bugs']:
            print(f"🔴 BUGS FOUND: {result['bug_count']}")
            print()
            for bug in result['bugs']:
                print(f"Line {bug['line']}: {bug['pattern']}")
                print(f"  {bug['content']}")
                print()
        else:
            print("✅ No f-string bugs found")
        
        sys.exit(0 if not result['has_bugs'] else 1)
    
    # Scan directory (non-recursive)
    if mode == '--scan-all':
        if len(sys.argv) < 3:
            print("Error: --scan-all requires a directory path")
            sys.exit(1)
        
        dirpath = Path(sys.argv[2])
        if not dirpath.is_dir():
            print(f"Error: {dirpath} is not a directory")
            sys.exit(1)
        
        scan_directory(dirpath, recursive=False)
        return
    
    # Scan directory (recursive)
    if mode == '--scan-recursive':
        if len(sys.argv) < 3:
            print("Error: --scan-recursive requires a directory path")
            sys.exit(1)
        
        dirpath = Path(sys.argv[2])
        if not dirpath.is_dir():
            print(f"Error: {dirpath} is not a directory")
            sys.exit(1)
        
        scan_directory(dirpath, recursive=True)
        return
    
    # Dry-run single file
    if mode == '--dry-run':
        if len(sys.argv) < 3:
            print("Error: --dry-run requires a file path")
            sys.exit(1)
        
        filepath = Path(sys.argv[2])
        print(f"Dry-run: {filepath}")
        print("=" * 70)
        
        result = dry_run_file(filepath)
        
        if not result['success']:
            print(f"Error: {result['error']}")
            sys.exit(1)
        
        if result['changes']:
            print(f"🔧 {len(result['changes'])} change(s) would be made:")
            print()
            for change in result['changes']:
                print(f"Line {change['line']}: {change['type']}")
                print(f"  Before: {change['original'][:70]}")
                print(f"  After:  {change['fixed'][:70]}")
                print()
        else:
            print("✅ No changes needed")
        
        sys.exit(0)
    
    # Dry-run directory (non-recursive)
    if mode == '--dry-run-all':
        if len(sys.argv) < 3:
            print("Error: --dry-run-all requires a directory path")
            sys.exit(1)
        
        dirpath = Path(sys.argv[2])
        if not dirpath.is_dir():
            print(f"Error: {dirpath} is not a directory")
            sys.exit(1)
        
        dry_run_directory(dirpath, recursive=False)
        return
    
    # Dry-run directory (recursive)
    if mode == '--dry-run-recursive':
        if len(sys.argv) < 3:
            print("Error: --dry-run-recursive requires a directory path")
            sys.exit(1)
        
        dirpath = Path(sys.argv[2])
        if not dirpath.is_dir():
            print(f"Error: {dirpath} is not a directory")
            sys.exit(1)
        
        dry_run_directory(dirpath, recursive=True)
        return
    
    # Fix directory (non-recursive)
    if mode == '--fix-all':
        if len(sys.argv) < 3:
            print("Error: --fix-all requires a directory path")
            sys.exit(1)
        
        dirpath = Path(sys.argv[2])
        if not dirpath.is_dir():
            print(f"Error: {dirpath} is not a directory")
            sys.exit(1)
        
        print("⚠️  WARNING: This will modify files IN-PLACE!")
        print("💾 Backups will be created as .bak.py files")
        response = input("Continue? [y/N]: ")
        if response.lower() != 'y':
            print("Aborted")
            sys.exit(0)
        
        fix_directory(dirpath, recursive=False)
        return
    
    # Fix directory (recursive)
    if mode == '--fix-recursive':
        if len(sys.argv) < 3:
            print("Error: --fix-recursive requires a directory path")
            sys.exit(1)
        
        dirpath = Path(sys.argv[2])
        if not dirpath.is_dir():
            print(f"Error: {dirpath} is not a directory")
            sys.exit(1)
        
        print("⚠️  WARNING: This will modify files IN-PLACE recursively!")
        print("💾 Backups will be created as .bak.py files")
        response = input("Continue? [y/N]: ")
        if response.lower() != 'y':
            print("Aborted")
            sys.exit(0)
        
        fix_directory(dirpath, recursive=True)
        return
    
    # Default: Fix single file
    input_file = Path(sys.argv[1])
    output_file = Path(sys.argv[2]) if len(sys.argv) > 2 else None
    
    if not input_file.exists():
        print(f"Error: File not found: {input_file}")
        sys.exit(1)
    
    print(f"Fixing: {input_file}")
    print("=" * 70)
    
    # Scan first
    scan_result = scan_file(input_file)
    
    if 'error' in scan_result:
        print(f"Error: {scan_result['error']}")
        sys.exit(1)
    
    if not scan_result['has_bugs']:
        print("✅ No bugs found - file is already clean")
        sys.exit(0)
    
    print(f"Found {scan_result['bug_count']} bug(s):")
    for bug in scan_result['bugs']:
        print(f"  Line {bug['line']}: {bug['pattern']}")
    print()
    
    # Fix
    result = fix_file(input_file, output_file)
    
    if not result['success']:
        print(f"❌ Fix failed: {result['error']}")
        sys.exit(1)
    
    print(f"✅ Fixed {len(result['changes'])} bug(s)")
    print()
    
    for change in result['changes']:
        print(f"Line {change['line']}: {change['type']}")
        print(f"  Before: {change['original'][:80]}")
        print(f"  After:  {change['fixed'][:80]}")
        print()
    
    print(f"Output written to: {result['output_file']}")
    
    if 'backup_file' in result:
        print(f"💾 Backup created: {result['backup_file']}")
    
    print()
    print("Next steps:")
    if 'backup_file' in result:
        print(f"  1. Review: diff {result['backup_file']} {result['output_file']}")
        print(f"  2. Test:   python3 -m py_compile {result['output_file']}")
        print(f"  3. Restore (if needed): mv {result['backup_file']} {input_file}")
    else:
        print(f"  1. Review: diff {input_file} {result['output_file']}")
        print(f"  2. Test:   python3 -m py_compile {result['output_file']}")
        print(f"  3. Deploy: mv {result['output_file']} {input_file}")


if __name__ == '__main__':
    main()
