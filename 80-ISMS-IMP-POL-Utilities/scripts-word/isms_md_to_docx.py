#!/usr/bin/env python3
"""
ISMS Markdown to DOCX Converter
Converts ISMS policy/procedure markdown documents to professional Word format

Usage:
    python3 isms_md_to_docx.py ISMS-POL-A.8.24.md
    python3 isms_md_to_docx.py --all  # Convert all ISMS-*.md files
    python3 isms_md_to_docx.py --template custom.docx ISMS-POL-A.8.24.md
"""

import sys
import subprocess
import glob
from pathlib import Path


def convert_to_docx(md_file, template_file=None, add_toc=True):
    """
    Convert markdown file to DOCX with proper ISMS formatting.
    
    Args:
        md_file: Path to markdown file
        template_file: Optional Word template for styling
        add_toc: Add table of contents
    """
    
    md_path = Path(md_file)
    
    if not md_path.exists():
        print(f"❌ ERROR: File not found: {md_file}")
        return False
    
    # Generate output filename
    output_file = md_path.stem + ".docx"
    
    print(f"\n{'='*80}")
    print(f"Converting: {md_file}")
    print(f"Output:     {output_file}")
    print(f"{'='*80}\n")
    
    # Build pandoc command
    cmd = [
        "pandoc",
        str(md_path),
        "-o", output_file,
        "-f", "markdown+pipe_tables+grid_tables",  # Enable advanced table support
        "--standalone",  # Complete document
    ]
    
    # Add table of contents
    if add_toc:
        cmd.extend([
            "--toc",
            "--toc-depth=3",
        ])
    
    # Add reference template if provided
    if template_file and Path(template_file).exists():
        cmd.extend(["--reference-doc", template_file])
        print(f"📄 Using template: {template_file}")
    
    # Metadata for professional appearance
    cmd.extend([
        "-V", "geometry:margin=1in",  # 1-inch margins
        "-V", "fontsize=11pt",
        "-V", "linestretch=1.15",  # Slight line spacing
    ])
    
    try:
        # Run pandoc
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"✅ SUCCESS: {output_file} created")
            
            # Get file size
            size_kb = Path(output_file).stat().st_size / 1024
            print(f"   File size: {size_kb:.1f} KB")
            
            return True
        else:
            print(f"❌ ERROR: Pandoc conversion failed")
            print(f"   {result.stderr}")
            return False
            
    except FileNotFoundError:
        print("❌ ERROR: pandoc not found!")
        print("   Install: sudo apt install pandoc")
        return False
    except Exception as e:
        print(f"❌ ERROR: {e}")
        return False


def convert_all_isms_files(template_file=None):
    """Convert all ISMS-*.md files in current directory."""
    
    # Find all ISMS markdown files
    md_files = sorted(glob.glob("ISMS-*.md"))
    
    if not md_files:
        print("❌ No ISMS-*.md files found in current directory")
        return
    
    print(f"\n{'='*80}")
    print(f"Found {len(md_files)} ISMS markdown file(s)")
    print(f"{'='*80}")
    
    for md_file in md_files:
        print(f"\n  • {md_file}")
    
    # Confirm
    response = input(f"\nConvert all {len(md_files)} files? [y/N]: ")
    if response.lower() != 'y':
        print("Cancelled.")
        return
    
    # Convert each file
    success_count = 0
    for md_file in md_files:
        if convert_to_docx(md_file, template_file):
            success_count += 1
    
    print(f"\n{'='*80}")
    print(f"SUMMARY: {success_count}/{len(md_files)} files converted successfully")
    print(f"{'='*80}\n")


def create_reference_template():
    """Create a basic reference template for ISMS documents."""
    
    template_md = """# ISMS Document Template

This is a reference template for ISMS documents.

## 1. Purpose

Example section content.

### 1.1 Subsection

More content here.

## 2. Scope

Example scope section.

### 2.1 Applicability

- Bullet point 1
- Bullet point 2
- Bullet point 3

## 3. Requirements

| Requirement ID | Description | Priority |
|----------------|-------------|----------|
| REQ-001        | Example     | High     |
| REQ-002        | Example     | Medium   |

## 4. Procedures

1. Step one
2. Step two
3. Step three
"""
    
    # Write template markdown
    with open("isms_template.md", "w") as f:
        f.write(template_md)
    
    # Convert to DOCX
    cmd = [
        "pandoc",
        "isms_template.md",
        "-o", "isms_reference_template.docx",
        "--toc",
        "--standalone"
    ]
    
    try:
        subprocess.run(cmd, check=True, capture_output=True)
        print("✅ Created: isms_reference_template.docx")
        print("   Customize this in Word, then use as --template")
        
        # Clean up
        Path("isms_template.md").unlink()
        
    except Exception as e:
        print(f"❌ ERROR creating template: {e}")


def main():
    if len(sys.argv) < 2:
        print("ISMS Markdown to DOCX Converter")
        print("="*80)
        print("\nUsage:")
        print("  python3 isms_md_to_docx.py <file.md>")
        print("  python3 isms_md_to_docx.py --all")
        print("  python3 isms_md_to_docx.py --template <template.docx> <file.md>")
        print("  python3 isms_md_to_docx.py --create-template")
        print("\nExamples:")
        print("  # Convert single file")
        print("  python3 isms_md_to_docx.py ISMS-POL-A.8.24.md")
        print("\n  # Convert all ISMS-*.md files")
        print("  python3 isms_md_to_docx.py --all")
        print("\n  # Use custom Word template for styling")
        print("  python3 isms_md_to_docx.py --template company_template.docx ISMS-POL-A.8.24.md")
        print("\n  # Create reference template to customize")
        print("  python3 isms_md_to_docx.py --create-template")
        print("\nFeatures:")
        print("  ✓ Automatic table of contents (3 levels)")
        print("  ✓ Professional formatting (1-inch margins, 11pt font)")
        print("  ✓ Advanced table support (pipe tables, grid tables)")
        print("  ✓ Custom Word template support")
        print("  ✓ Batch conversion of all ISMS files")
        sys.exit(1)
    
    # Parse arguments
    template_file = None
    md_file = None
    
    i = 1
    while i < len(sys.argv):
        arg = sys.argv[i]
        
        if arg == '--all':
            convert_all_isms_files(template_file)
            return
        elif arg == '--create-template':
            create_reference_template()
            return
        elif arg == '--template':
            if i + 1 < len(sys.argv):
                template_file = sys.argv[i + 1]
                i += 1
            else:
                print("ERROR: --template requires a filename")
                sys.exit(1)
        elif not arg.startswith('--'):
            md_file = arg
        
        i += 1
    
    # Convert single file
    if md_file:
        convert_to_docx(md_file, template_file)
    else:
        print("ERROR: No markdown file specified")
        sys.exit(1)


if __name__ == "__main__":
    main()