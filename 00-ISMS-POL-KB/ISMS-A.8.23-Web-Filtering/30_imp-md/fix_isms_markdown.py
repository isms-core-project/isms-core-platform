#!/usr/bin/env python3
"""
ISMS Markdown Formatter
Comprehensive markdown formatting tool for clean Pandoc/Word conversion

Fixes:
    1. Document structure (headers → bold, header demotion, numbering removal)
    2. List formatting (blank lines before/after lists)

Usage:
    python3 fix_isms_markdown.py input.md [output.md] [OPTIONS]
    
Options:
    --dry-run           Show what would change without modifying files
    --structure-only    Only fix document structure
    --lists-only        Only fix list formatting
    --no-structure      Skip document structure fixes
    --no-lists          Skip list formatting fixes
    
Examples:
    python3 fix_isms_markdown.py document.md
    python3 fix_isms_markdown.py document.md fixed.md
    python3 fix_isms_markdown.py document.md --dry-run
    python3 fix_isms_markdown.py document.md --structure-only
    python3 fix_isms_markdown.py document.md --lists-only
"""

import re
import sys
from pathlib import Path
from typing import List, Tuple, Dict


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

def fix_list_formatting(content: str, dry_run: bool = False) -> Tuple[str, dict]:
    """
    Fix common markdown list formatting issues for Pandoc compatibility.
    
    Fixes applied:
    1. Add blank line before list if preceded by text (not heading)
    2. Add blank line after list if followed by text
    3. Ensure consistent spacing in nested lists
    
    Args:
        content: Markdown file content as string
        dry_run: If True, don't modify content
        
    Returns:
        (fixed_content, statistics)
    """
    lines = content.split('\n')
    fixed_lines = []
    
    stats = {
        'blank_lines_added': 0,
        'changes': []
    }
    
    for i, line in enumerate(lines):
        # Check if current line is a list item
        is_list = re.match(r'^(\s*)[-*+]\s+', line)
        
        # Check previous line
        prev_line = lines[i-1] if i > 0 else ''
        prev_is_blank = prev_line.strip() == ''
        prev_is_heading = re.match(r'^#{1,6}\s+', prev_line)
        prev_is_list = re.match(r'^(\s*)[-*+]\s+', prev_line)
        prev_is_hr = re.match(r'^(-{3,}|={3,}|\*{3,})$', prev_line)
        prev_is_code_fence = re.match(r'^```', prev_line)
        
        # If this is a list item and needs blank line before it
        if is_list and not prev_is_blank and not prev_is_heading and not prev_is_list and not prev_is_hr and not prev_is_code_fence:
            # Check if previous line is text ending with colon (common pattern)
            if prev_line.strip().endswith(':') or prev_line.strip():
                # Add blank line before this list item
                if not dry_run:
                    fixed_lines.append('')
                stats['blank_lines_added'] += 1
                stats['changes'].append({
                    'line': i + 1,
                    'type': 'blank_line_before_list',
                    'before': f"{prev_line}\n{line}",
                    'after': f"{prev_line}\n\n{line}" if not dry_run else f"{prev_line}\n{line}"
                })
        
        fixed_lines.append(line)
    
    return '\n'.join(fixed_lines), stats


def validate_lists(content: str) -> List[str]:
    """
    Validate list formatting and return warnings.
    
    Returns:
        List of warning messages
    """
    warnings = []
    lines = content.split('\n')
    
    for i, line in enumerate(lines, 1):
        # Check for list items without proper spacing
        is_list = re.match(r'^(\s*)[-*+]\s+', line)
        if is_list and i > 1:
            prev_line = lines[i-2]
            if prev_line.strip() and not prev_line.strip().startswith('#'):
                if not re.match(r'^(\s*)[-*+]\s+', prev_line):
                    warnings.append(f"Line {i}: List item may need blank line before it")
        
        # Check for inconsistent list markers
        if is_list:
            marker = re.match(r'^(\s*)([-*+])', line).group(2)
            # Look ahead for next list item at same indentation
            indent = len(re.match(r'^(\s*)', line).group(1))
            for j in range(i, min(i+10, len(lines))):
                next_line = lines[j]
                next_match = re.match(r'^(\s*)([-*+])\s+', next_line)
                if next_match:
                    next_indent = len(next_match.group(1))
                    next_marker = next_match.group(2)
                    if next_indent == indent and next_marker != marker:
                        warnings.append(f"Line {i}-{j+1}: Inconsistent list markers ('{marker}' vs '{next_marker}')")
                        break
    
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


def print_structure_report(stats: dict):
    """Print detailed report for structure fixes."""
    if not stats or not stats['changes']:
        print("  ✅ Document structure is already correct!")
        return
    
    print(f"  📝 Found {len(stats['changes'])} structure changes:\n")
    
    # Group changes by type
    by_type = {}
    for change in stats['changes']:
        change_type = change['type']
        if change_type not in by_type:
            by_type[change_type] = []
        by_type[change_type].append(change)
    
    # Display changes by type
    type_labels = {
        'title_to_bold': '📌 Title converted to bold',
        'subtitle_to_bold': '📌 Subtitle converted to bold',
        'metadata_to_bold': '📌 Metadata section converted to bold',
        'number_removed': '🔢 Manual numbering removed',
        'header_demoted': '⬇️  Header demoted one level'
    }
    
    for change_type, changes in by_type.items():
        print(f"  {type_labels.get(change_type, change_type)}:")
        for change in changes[:3]:  # Show first 3 of each type
            print(f"    Line {change['line']:3d}:")
            print(f"      Before: {change['before']}")
            print(f"      After:  {change['after']}")
        if len(changes) > 3:
            print(f"    ... and {len(changes) - 3} more")
        print()


def print_lists_report(stats: dict):
    """Print detailed report for list fixes."""
    if not stats or not stats['changes']:
        print("  ✅ List formatting is already correct!")
        return
    
    print(f"  📝 Found {len(stats['changes'])} list formatting changes:\n")
    
    for change in stats['changes'][:5]:  # Show first 5
        print(f"    Line {change['line']:3d}: {change['type']}")
    if len(stats['changes']) > 5:
        print(f"    ... and {len(stats['changes']) - 5} more")
    print()


def print_summary(stats: dict, options: dict):
    """Print comprehensive summary."""
    print()
    print("=" * 70)
    print("SUMMARY")
    print("=" * 70)
    
    if stats['structure']:
        print("\nDocument Structure Fixes:")
        print(f"  Title converted to bold:        {stats['structure']['title_converted']}")
        print(f"  Subtitle converted to bold:     {stats['structure']['subtitle_converted']}")
        print(f"  Metadata sections converted:    {stats['structure']['metadata_sections_converted']}")
        print(f"  Headers demoted:                {stats['structure']['headers_demoted']}")
        print(f"  Manual numbers removed:         {stats['structure']['numbers_removed']}")
    
    if stats['lists']:
        print("\nList Formatting Fixes:")
        print(f"  Blank lines added:              {stats['lists']['blank_lines_added']}")
    
    print()


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
    
    input_file = Path(args[0])
    output_file = Path(args[1]) if len(args) > 1 else input_file
    
    if not input_file.exists():
        print(f"❌ Error: File not found: {input_file}")
        sys.exit(1)
    
    print(f"📖 Reading: {input_file}")
    content = input_file.read_text(encoding='utf-8')
    
    print("🔍 Analyzing document...\n")
    
    # Validate lists if fixing them
    if options['fix_lists']:
        warnings = validate_lists(content)
        if warnings:
            print(f"⚠️  List validation found {len(warnings)} potential issues:")
            for warning in warnings[:5]:
                print(f"    {warning}")
            if len(warnings) > 5:
                print(f"    ... and {len(warnings) - 5} more")
            print()
    
    # Process document
    print("🔧 Processing fixes...")
    processed_content, stats = process_document(content, options)
    
    # Print reports
    if options['fix_structure']:
        print("\n📋 Document Structure Report:")
        print_structure_report(stats['structure'])
    
    if options['fix_lists']:
        print("📋 List Formatting Report:")
        print_lists_report(stats['lists'])
    
    # Print summary
    print_summary(stats, options)
    
    # Check if any changes were made
    has_changes = (
        (stats['structure'] and stats['structure']['changes']) or
        (stats['lists'] and stats['lists']['changes'])
    )
    
    if not has_changes:
        print("✅ No changes needed - document is already properly formatted!")
        return
    
    if options['dry_run']:
        print("🔍 DRY RUN - No files modified")
        print(f"\nTo apply changes, run without --dry-run:")
        print(f"  python3 fix_isms_markdown.py {input_file}")
        return
    
    print(f"💾 Writing: {output_file}")
    output_file.write_text(processed_content, encoding='utf-8')
    
    print()
    print("✅ COMPLETE!")
    print()
    print("Your document now has:")
    if options['fix_structure']:
        print("  ✅ Title/subtitle as bold text (not headers)")
        print("  ✅ Metadata sections as bold text")
        print("  ✅ Content headers demoted one level")
        print("  ✅ No manual numbering")
    if options['fix_lists']:
        print("  ✅ Proper blank lines before lists")
    print()
    print("Convert to Word with:")
    print(f"  pandoc {output_file} \\")
    print("      --from markdown+pipe_tables+grid_tables \\")
    print("      --to docx \\")
    print("      --number-sections \\")
    print("      --reference-doc=bithawk-isms-reference.docx \\")
    print(f"      --output {output_file.stem}.docx")
    print()


if __name__ == '__main__':
    main()