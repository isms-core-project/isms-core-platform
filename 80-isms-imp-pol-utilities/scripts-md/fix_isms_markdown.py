#!/usr/bin/env python3
"""
ISMS Markdown Formatter - Recursive Edition
Comprehensive markdown formatting tool for clean Pandoc/Word conversion

Fixes:
    1. Document structure (headers → bold, header demotion, numbering removal)
    2. List formatting (blank lines before/after lists)

Usage:
    python3 fix_isms_markdown.py <directory> [OPTIONS]
    
Options:
    --dry-run           Show what would change without modifying files
    --structure-only    Only fix document structure
    --lists-only        Only fix list formatting
    --no-structure      Skip document structure fixes
    --no-lists          Skip list formatting fixes
    --no-backup         Skip creating backup files (not recommended)
    
Examples:
    python3 fix_isms_markdown.py /path/to/isms/docs
    python3 fix_isms_markdown.py /path/to/isms/docs --dry-run
    python3 fix_isms_markdown.py /path/to/isms/docs --structure-only
    python3 fix_isms_markdown.py /path/to/isms/docs --lists-only --no-backup
"""

import re
import sys
import shutil
from pathlib import Path
from typing import List, Tuple, Dict
from datetime import datetime


# =============================================================================
# DOCUMENT STRUCTURE FIXES
# =============================================================================

def detect_structure(lines: List[str]) -> dict:
    """
    Detect document structure to identify title, subtitle, and metadata sections.
    
    Returns dict with:
        - title_line: Line number of title (first #)
        - subtitle_line: Line number of subtitle (first ##)
        - metadata_sections: List of line numbers for metadata sections
        - first_content_line: Where actual numbered content starts
    """
    structure = {
        'title_line': None,
        'subtitle_line': None,
        'metadata_sections': [],
        'first_content_line': None
    }
    
    found_title = False
    found_subtitle = False
    
    for i, line in enumerate(lines):
        # First # header = title
        if not found_title and re.match(r'^#\s+', line):
            structure['title_line'] = i
            found_title = True
            continue
        
        # First ## header after title = subtitle
        if found_title and not found_subtitle and re.match(r'^##\s+', line):
            structure['subtitle_line'] = i
            found_subtitle = True
            continue
        
        # After subtitle, look for metadata sections (before numbered content)
        if found_subtitle and structure['first_content_line'] is None:
            # Check if this is a metadata section (Dokumentenlenkung, etc.)
            if re.match(r'^##\s+(?![\d.]+\s)', line):
                # This is a ## header without numbering before content starts
                header_text = re.sub(r'^##\s+', '', line).strip().lower()
                
                # Common metadata section names
                metadata_keywords = [
                    'dokumentenlenkung', 'document control',
                    'versionsverzeichnis', 'version history',
                    'änderungsverzeichnis', 'change log'
                ]
                
                if any(keyword in header_text for keyword in metadata_keywords):
                    structure['metadata_sections'].append(i)
                    continue
            
            # First ## with numbering = start of content
            if re.match(r'^##\s+[\d.]+\s', line):
                structure['first_content_line'] = i
                break
    
    return structure


def convert_to_bold(line: str) -> str:
    """Convert a markdown header to bold text."""
    # Remove # characters and surrounding whitespace
    text = re.sub(r'^#+\s+', '', line).strip()
    return f"**{text}**"


def demote_header(line: str) -> str:
    """
    Demote header by one level (remove one #).
    
    ## Title → # Title
    ### Subtitle → ## Subtitle
    """
    match = re.match(r'^(#+)\s+(.+)$', line)
    if match:
        hashes = match.group(1)
        title = match.group(2)
        
        if len(hashes) > 1:
            # Remove one #
            new_hashes = hashes[:-1]
            return f"{new_hashes} {title}"
        else:
            # Already at top level, keep as is
            return line
    return line


def remove_manual_numbering(line: str) -> str:
    """
    Remove manual numbering from headers.
    
    ## 1. Title → ## Title
    ### 1.1 Subtitle → ### Subtitle
    """
    match = re.match(r'^(#+)\s+([\d.]+)\s+(.+)$', line)
    if match:
        hashes = match.group(1)
        title = match.group(3)
        return f"{hashes} {title}"
    return line


def fix_document_structure(content: str, dry_run: bool = False) -> Tuple[str, dict]:
    """
    Fix document structure for clean Pandoc numbering.
    
    Returns:
        (fixed_content, statistics)
    """
    lines = content.split('\n')
    fixed_lines = []
    
    stats = {
        'title_converted': False,
        'subtitle_converted': False,
        'metadata_sections_converted': 0,
        'headers_demoted': 0,
        'numbers_removed': 0,
        'changes': []
    }
    
    # Detect document structure
    structure = detect_structure(lines)
    
    for i, line in enumerate(lines):
        original_line = line
        
        # Convert title to bold
        if i == structure['title_line']:
            if not dry_run:
                line = convert_to_bold(line)
            stats['title_converted'] = True
            stats['changes'].append({
                'line': i + 1,
                'type': 'title_to_bold',
                'before': original_line,
                'after': line if not dry_run else original_line
            })
        
        # Convert subtitle to bold
        elif i == structure['subtitle_line']:
            if not dry_run:
                line = convert_to_bold(line)
            stats['subtitle_converted'] = True
            stats['changes'].append({
                'line': i + 1,
                'type': 'subtitle_to_bold',
                'before': original_line,
                'after': line if not dry_run else original_line
            })
        
        # Convert metadata sections to bold
        elif i in structure['metadata_sections']:
            if not dry_run:
                line = convert_to_bold(line)
            stats['metadata_sections_converted'] += 1
            stats['changes'].append({
                'line': i + 1,
                'type': 'metadata_to_bold',
                'before': original_line,
                'after': line if not dry_run else original_line
            })
        
        # Process content headers (after first_content_line)
        elif structure['first_content_line'] is not None and i >= structure['first_content_line']:
            if re.match(r'^#+\s+', line):
                # Remove manual numbering first
                if re.match(r'^#+\s+[\d.]+\s', line):
                    if not dry_run:
                        line = remove_manual_numbering(line)
                    stats['numbers_removed'] += 1
                    stats['changes'].append({
                        'line': i + 1,
                        'type': 'number_removed',
                        'before': original_line,
                        'after': line if not dry_run else original_line
                    })
                
                # Then demote header
                if not dry_run:
                    line = demote_header(line)
                stats['headers_demoted'] += 1
                
                # Only add to changes if not already added for number removal
                if not re.match(r'^#+\s+[\d.]+\s', original_line):
                    stats['changes'].append({
                        'line': i + 1,
                        'type': 'header_demoted',
                        'before': original_line,
                        'after': line if not dry_run else original_line
                    })
        
        fixed_lines.append(line)
    
    return '\n'.join(fixed_lines), stats


# =============================================================================
# LIST FORMATTING FIXES
# =============================================================================

def is_list_item(line: str) -> bool:
    """Check if line is a list item (numbered or bulleted)."""
    return bool(re.match(r'^\s*[\d+.*-]\s+', line))


def get_list_indent(line: str) -> int:
    """Get indentation level of a list item."""
    match = re.match(r'^(\s*)', line)
    return len(match.group(1)) if match else 0


def fix_list_formatting(content: str, dry_run: bool = False) -> Tuple[str, dict]:
    """
    Fix list formatting by ensuring blank lines before and after lists.
    
    Returns:
        (fixed_content, statistics)
    """
    lines = content.split('\n')
    fixed_lines = []
    
    stats = {
        'blank_lines_added': 0,
        'changes': []
    }
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Check if this is the start of a list
        if is_list_item(line):
            # Check if previous line exists and isn't blank
            if i > 0 and lines[i-1].strip():
                # Need blank line before list
                if not dry_run:
                    fixed_lines.append('')
                stats['blank_lines_added'] += 1
                stats['changes'].append({
                    'line': i,
                    'type': 'Added blank line before list'
                })
            
            # Add all list items
            list_start = i
            while i < len(lines) and (is_list_item(lines[i]) or not lines[i].strip()):
                fixed_lines.append(lines[i])
                i += 1
            
            # Check if next line exists and isn't blank
            if i < len(lines) and lines[i].strip():
                # Need blank line after list
                if not dry_run:
                    fixed_lines.append('')
                stats['blank_lines_added'] += 1
                stats['changes'].append({
                    'line': i,
                    'type': 'Added blank line after list'
                })
            
            continue
        
        fixed_lines.append(line)
        i += 1
    
    return '\n'.join(fixed_lines), stats


def validate_lists(content: str) -> List[str]:
    """
    Validate list formatting and return list of warnings.
    """
    lines = content.split('\n')
    warnings = []
    
    i = 0
    while i < len(lines):
        if is_list_item(lines[i]):
            list_start = i
            indent = get_list_indent(lines[i])
            marker = re.match(r'^\s*([\d+.*-])', lines[i]).group(1)
            
            # Check consistency within this list
            j = i
            while j < len(lines) and (is_list_item(lines[j]) or not lines[j].strip()):
                if is_list_item(lines[j]):
                    next_match = re.match(r'^(\s*)([\d+.*-])', lines[j])
                    if next_match:
                        next_indent = len(next_match.group(1))
                        next_marker = next_match.group(2)
                        if next_indent == indent and next_marker != marker:
                            warnings.append(f"Line {i}-{j+1}: Inconsistent list markers ('{marker}' vs '{next_marker}')")
                            break
                j += 1
            
            i = j
        else:
            i += 1
    
    return warnings


# =============================================================================
# MAIN PROCESSING
# =============================================================================

def process_document(content: str, options: dict) -> Tuple[str, dict]:
    """
    Process document with selected fixes.
    
    Args:
        content: Original markdown content
        options: Dict with 'fix_structure', 'fix_lists', 'dry_run' flags
        
    Returns:
        (processed_content, combined_statistics)
    """
    stats = {
        'structure': None,
        'lists': None
    }
    
    processed_content = content
    
    # Apply document structure fixes
    if options.get('fix_structure', True):
        processed_content, stats['structure'] = fix_document_structure(
            processed_content, 
            dry_run=options.get('dry_run', False)
        )
    
    # Apply list formatting fixes
    if options.get('fix_lists', True):
        processed_content, stats['lists'] = fix_list_formatting(
            processed_content,
            dry_run=options.get('dry_run', False)
        )
    
    return processed_content, stats


def create_backup(file_path: Path, options: dict) -> bool:
    """
    Create a backup of the file before modification.
    
    Returns True if backup was created, False if skipped.
    """
    if options.get('no_backup', False):
        return False
    
    if options.get('dry_run', False):
        return False
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_path = file_path.with_suffix(f'.{timestamp}.bak')
    
    try:
        shutil.copy2(file_path, backup_path)
        return True
    except Exception as e:
        print(f"    ⚠️  Warning: Could not create backup: {e}")
        return False


def find_markdown_files(directory: Path) -> List[Path]:
    """
    Recursively find all .md files in directory and subdirectories.
    """
    return sorted(directory.rglob('*.md'))


def print_file_summary(file_path: Path, stats: dict, options: dict, backup_created: bool):
    """Print summary for a single file."""
    has_changes = (
        (stats['structure'] and stats['structure']['changes']) or
        (stats['lists'] and stats['lists']['changes'])
    )
    
    if not has_changes:
        print(f"  ✅ No changes needed")
        return
    
    # Count total changes
    total_changes = 0
    if stats['structure']:
        total_changes += len(stats['structure']['changes'])
    if stats['lists']:
        total_changes += len(stats['lists']['changes'])
    
    if options['dry_run']:
        print(f"  🔍 Would make {total_changes} changes")
    else:
        print(f"  ✅ Applied {total_changes} changes")
        if backup_created:
            print(f"  💾 Backup created")


def process_file(file_path: Path, options: dict) -> dict:
    """
    Process a single markdown file.
    
    Returns statistics dict.
    """
    try:
        # Read file
        content = file_path.read_text(encoding='utf-8')
        
        # Process document
        processed_content, stats = process_document(content, options)
        
        # Check if any changes were made
        has_changes = (
            (stats['structure'] and stats['structure']['changes']) or
            (stats['lists'] and stats['lists']['changes'])
        )
        
        backup_created = False
        
        if has_changes and not options['dry_run']:
            # Create backup
            backup_created = create_backup(file_path, options)
            
            # Write fixed content
            file_path.write_text(processed_content, encoding='utf-8')
        
        return {
            'success': True,
            'stats': stats,
            'has_changes': has_changes,
            'backup_created': backup_created
        }
        
    except Exception as e:
        return {
            'success': False,
            'error': str(e),
            'has_changes': False,
            'backup_created': False
        }


def main():
    """Main entry point."""
    if len(sys.argv) < 2 or '--help' in sys.argv or '-h' in sys.argv:
        print(__doc__)
        sys.exit(0 if '--help' in sys.argv or '-h' in sys.argv else 1)
    
    # Parse arguments
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    flags = [a for a in sys.argv[1:] if a.startswith('--')]
    
    options = {
        'dry_run': '--dry-run' in flags,
        'no_backup': '--no-backup' in flags,
        'fix_structure': '--structure-only' in flags or '--no-lists' in flags or (
            '--lists-only' not in flags and '--no-structure' not in flags
        ),
        'fix_lists': '--lists-only' in flags or '--no-structure' in flags or (
            '--structure-only' not in flags and '--no-lists' not in flags
        )
    }
    
    # Handle mutually exclusive options
    if '--structure-only' in flags:
        options['fix_lists'] = False
    if '--lists-only' in flags:
        options['fix_structure'] = False
    if '--no-structure' in flags:
        options['fix_structure'] = False
    if '--no-lists' in flags:
        options['fix_lists'] = False
    
    if not args:
        print("❌ Error: Please specify a directory")
        print("\nUsage: python3 fix_isms_markdown.py <directory> [OPTIONS]")
        sys.exit(1)
    
    target_dir = Path(args[0])
    
    if not target_dir.exists():
        print(f"❌ Error: Directory not found: {target_dir}")
        sys.exit(1)
    
    if not target_dir.is_dir():
        print(f"❌ Error: Not a directory: {target_dir}")
        sys.exit(1)
    
    print("=" * 70)
    print("ISMS MARKDOWN FORMATTER - RECURSIVE EDITION")
    print("=" * 70)
    print()
    print(f"📂 Target directory: {target_dir}")
    
    # Find all markdown files
    print("🔍 Searching for Markdown files...")
    md_files = find_markdown_files(target_dir)
    
    if not md_files:
        print("  ⚠️  No Markdown files found")
        return
    
    print(f"  📝 Found {len(md_files)} Markdown file(s)")
    print()
    
    # Print options
    print("⚙️  Options:")
    if options['dry_run']:
        print("  🔍 DRY RUN - No files will be modified")
    if options['no_backup']:
        print("  ⚠️  NO BACKUP - Backups disabled")
    else:
        print("  💾 Backups enabled")
    
    fixes = []
    if options['fix_structure']:
        fixes.append("Structure")
    if options['fix_lists']:
        fixes.append("Lists")
    print(f"  🔧 Fixes: {', '.join(fixes) if fixes else 'None'}")
    print()
    
    # Process all files
    print("=" * 70)
    print("PROCESSING FILES")
    print("=" * 70)
    print()
    
    results = {
        'total': len(md_files),
        'processed': 0,
        'changed': 0,
        'unchanged': 0,
        'errors': 0,
        'backups': 0
    }
    
    for file_path in md_files:
        # Show relative path for readability
        try:
            rel_path = file_path.relative_to(target_dir)
        except ValueError:
            rel_path = file_path
        
        print(f"📄 {rel_path}")
        
        result = process_file(file_path, options)
        
        if result['success']:
            results['processed'] += 1
            print_file_summary(file_path, result['stats'], options, result['backup_created'])
            
            if result['has_changes']:
                results['changed'] += 1
                if result['backup_created']:
                    results['backups'] += 1
            else:
                results['unchanged'] += 1
        else:
            results['errors'] += 1
            print(f"  ❌ Error: {result['error']}")
        
        print()
    
    # Print final summary
    print("=" * 70)
    print("FINAL SUMMARY")
    print("=" * 70)
    print()
    print(f"Total files found:       {results['total']}")
    print(f"Files processed:         {results['processed']}")
    print(f"Files changed:           {results['changed']}")
    print(f"Files unchanged:         {results['unchanged']}")
    if results['errors'] > 0:
        print(f"Errors:                  {results['errors']}")
    if not options['no_backup'] and not options['dry_run']:
        print(f"Backups created:         {results['backups']}")
    print()
    
    if options['dry_run']:
        print("🔍 DRY RUN COMPLETE - No files were modified")
        print(f"\nTo apply changes, run without --dry-run:")
        print(f"  python3 fix_isms_markdown.py {target_dir}")
    elif results['changed'] > 0:
        print("✅ PROCESSING COMPLETE!")
        print()
        print("Your documents now have:")
        if options['fix_structure']:
            print("  ✅ Title/subtitle as bold text (not headers)")
            print("  ✅ Metadata sections as bold text")
            print("  ✅ Content headers demoted one level")
            print("  ✅ No manual numbering")
        if options['fix_lists']:
            print("  ✅ Proper blank lines before lists")
        print()
        print("Convert to Word with Pandoc using your reference template:")
        print("  pandoc <file.md> \\")
        print("      --from markdown+pipe_tables+grid_tables \\")
        print("      --to docx \\")
        print("      --number-sections \\")
        print("      --reference-doc=bithawk-isms-reference.docx \\")
        print("      --output <file.docx>")
    else:
        print("✅ All files are already properly formatted!")
    
    print()


if __name__ == '__main__':
    main()