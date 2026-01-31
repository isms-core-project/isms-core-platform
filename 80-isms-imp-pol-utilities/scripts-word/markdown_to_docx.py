#!/usr/bin/env python3
"""
markdown_to_docx.py

High-quality Markdown to DOCX converter using pypandoc
Works with complex markdown including tables, code blocks, lists, etc.

Requirements:
    sudo apt install pandoc python3-pip
    
    AND one of these (pypandoc wrapper needs underlying pandoc):
    - apt install pandoc (Linux)
    - brew install pandoc (macOS)
    - Download from: https://pandoc.org/installing.html (Windows)

Usage:
    python3 markdown_to_docx.py input.md output.docx
    python3 markdown_to_docx.py README.md ISMS-A.8.24-Suite-README.docx

Author: Greg (Security Engineering Team) 🎄
"""

import sys
import os
from pathlib import Path

try:
    import pypandoc
except ImportError:
    print("❌ Error: pypandoc not installed")
    print("   Install with: pip install pypandoc")
    print()
    print("   Also ensure pandoc is installed:")
    print("   - Linux: sudo apt install pandoc")
    print("   - macOS: brew install pandoc")
    print("   - Windows: https://pandoc.org/installing.html")
    sys.exit(1)


def convert_markdown_to_docx(input_file, output_file=None, reference_doc=None):
    """
    Convert Markdown to DOCX with high quality formatting.
    
    Args:
        input_file: Path to input .md file
        output_file: Path to output .docx file (optional, auto-generated if None)
        reference_doc: Path to reference .docx for styling (optional)
    
    Returns:
        Path to created DOCX file
    """
    input_path = Path(input_file)
    
    # Validate input
    if not input_path.exists():
        print(f"❌ Error: Input file not found: {input_file}")
        sys.exit(1)
    
    if not input_path.suffix.lower() in ['.md', '.markdown']:
        print(f"⚠️  Warning: Input file doesn't have .md extension: {input_file}")
        response = input("Continue anyway? (y/n): ").lower()
        if response != 'y':
            sys.exit(0)
    
    # Generate output filename if not provided
    if output_file is None:
        output_file = input_path.with_suffix('.docx')
    
    output_path = Path(output_file)
    
    # Check if output exists
    if output_path.exists():
        print(f"⚠️  Warning: Output file exists: {output_file}")
        response = input("Overwrite? (y/n): ").lower()
        if response != 'y':
            print("❌ Conversion cancelled")
            sys.exit(0)
    
    print(f"📄 Converting: {input_path.name}")
    print(f"📤 Output:     {output_path.name}")
    
    # Conversion options for best quality
    extra_args = [
        '--standalone',                    # Create standalone document
        '--toc',                          # Table of contents
        '--number-sections',              # Number headings
        '--highlight-style=tango',        # Code syntax highlighting
        '--wrap=preserve',                # Preserve line wrapping
    ]
    
    # Add reference doc if provided
    if reference_doc:
        ref_path = Path(reference_doc)
        if ref_path.exists():
            extra_args.append(f'--reference-doc={reference_doc}')
            print(f"🎨 Using reference style: {ref_path.name}")
        else:
            print(f"⚠️  Warning: Reference doc not found: {reference_doc}")
    
    try:
        # Perform conversion
        pypandoc.convert_file(
            str(input_path),
            'docx',
            outputfile=str(output_path),
            extra_args=extra_args
        )
        
        # Get file size
        size_kb = output_path.stat().st_size / 1024
        
        print()
        print("✅ Conversion successful!")
        print(f"   Output: {output_path.absolute()}")
        print(f"   Size:   {size_kb:.1f} KB")
        print()
        
        return output_path
        
    except Exception as e:
        print(f"\n❌ Conversion failed: {e}\n")
        
        # Check if pandoc is installed
        try:
            version = pypandoc.get_pandoc_version()
            print(f"   Pandoc version: {version}")
        except:
            print("   Pandoc not found!")
            print()
            print("   Install pandoc:")
            print("   - Linux: sudo apt install pandoc")
            print("   - macOS: brew install pandoc")
            print("   - Windows: https://pandoc.org/installing.html")
        
        sys.exit(1)


def main():
    """Main CLI interface."""
    print("=" * 70)
    print("Markdown to DOCX Converter")
    print("High-quality conversion using Pandoc")
    print("=" * 70)
    print()
    
    # Parse arguments
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python3 markdown_to_docx.py input.md [output.docx] [reference.docx]")
        print()
        print("Examples:")
        print("  python3 markdown_to_docx.py README.md")
        print("  python3 markdown_to_docx.py README.md MyDocument.docx")
        print("  python3 markdown_to_docx.py README.md output.docx template.docx")
        print()
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    reference_doc = sys.argv[3] if len(sys.argv) > 3 else None
    
    # Convert
    output_path = convert_markdown_to_docx(input_file, output_file, reference_doc)
    
    print("🎄 Merry Christmas! Now go enjoy those Penne with Shrimps! 🍝🦐")
    print("=" * 70)


if __name__ == "__main__":
    main()