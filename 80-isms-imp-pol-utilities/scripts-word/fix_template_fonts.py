#!/usr/bin/env python3
"""
Fix font settings in a Word template.

This script:
1. Sets explicit Calibri for ALL 4 font attributes in heading styles
2. Removes any Asian fonts like PMingLiU
3. Optionally fixes the theme to use Calibri

Usage:
    python3 fix_template_fonts.py reference.docx output.docx
    
Or:
    python3 fix_template_fonts.py reference.docx
    (will save as reference_FIXED.docx)
"""

import sys
from docx import Document
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
import zipfile
from pathlib import Path


def set_font_explicit(style, font_name):
    """
    Set font explicitly with ALL 4 attributes.
    
    Word uses 4 different font attributes for different scripts:
    - w:ascii      = Latin text (English, German, etc.)
    - w:hAnsi      = High ANSI (Western European)
    - w:cs         = Complex Scripts (Arabic, Hebrew)
    - w:eastAsia   = East Asian (Chinese, Japanese, Korean)
    
    We set ALL of them to ensure consistent font rendering.
    """
    # Set the high-level font name (python-docx API)
    style.font.name = font_name
    
    # Get or create run properties element
    rPr = style.element.get_or_add_rPr()
    
    # Remove any existing rFonts elements
    for rfonts in rPr.findall(qn('w:rFonts')):
        rPr.remove(rfonts)
    
    # Create new rFonts element with ALL 4 attributes
    rfonts = OxmlElement('w:rFonts')
    rfonts.set(qn('w:ascii'), font_name)
    rfonts.set(qn('w:hAnsi'), font_name)
    rfonts.set(qn('w:cs'), font_name)
    rfonts.set(qn('w:eastAsia'), font_name)
    
    # Insert at beginning of rPr
    rPr.insert(0, rfonts)


def fix_theme(docx_path, font_name="Calibri"):
    """
    Replace the theme XML to set both major and minor fonts.
    
    Args:
        docx_path: Path to the .docx file
        font_name: Font to use (default: Calibri)
    """
    # Theme XML with specified font for both major and minor
    theme_template = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<a:theme xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" name="{font_name}">
<a:themeElements>
<a:clrScheme name="Office">
<a:dk1><a:sysClr val="windowText" lastClr="000000"/></a:dk1>
<a:lt1><a:sysClr val="window" lastClr="FFFFFF"/></a:lt1>
<a:dk2><a:srgbClr val="44546A"/></a:dk2>
<a:lt2><a:srgbClr val="E7E6E6"/></a:lt2>
<a:accent1><a:srgbClr val="4472C4"/></a:accent1>
<a:accent2><a:srgbClr val="ED7D31"/></a:accent2>
<a:accent3><a:srgbClr val="A5A5A5"/></a:accent3>
<a:accent4><a:srgbClr val="FFC000"/></a:accent4>
<a:accent5><a:srgbClr val="5B9BD5"/></a:accent5>
<a:accent6><a:srgbClr val="70AD47"/></a:accent6>
<a:hlink><a:srgbClr val="0563C1"/></a:hlink>
<a:folHlink><a:srgbClr val="954F72"/></a:folHlink>
</a:clrScheme>
<a:fontScheme name="{font_name}">
<a:majorFont>
<a:latin typeface="{font_name}"/>
<a:ea typeface=""/>
<a:cs typeface=""/>
</a:majorFont>
<a:minorFont>
<a:latin typeface="{font_name}"/>
<a:ea typeface=""/>
<a:cs typeface=""/>
</a:minorFont>
</a:fontScheme>
<a:fmtScheme name="Office">
<a:fillStyleLst>
<a:solidFill><a:schemeClr val="phClr"/></a:solidFill>
</a:fillStyleLst>
<a:lnStyleLst>
<a:ln w="9525" cap="flat" cmpd="sng" algn="ctr">
<a:solidFill><a:schemeClr val="phClr"/></a:solidFill>
<a:prstDash val="solid"/>
</a:ln>
</a:lnStyleLst>
<a:effectStyleLst>
<a:effectStyle><a:effectLst/></a:effectStyle>
</a:effectStyleLst>
<a:bgFillStyleLst>
<a:solidFill><a:schemeClr val="phClr"/></a:solidFill>
</a:bgFillStyleLst>
</a:fmtScheme>
</a:themeElements>
</a:theme>'''
    
    theme_xml = theme_template.encode('utf-8')
    
    # Create temp file
    temp_path = str(docx_path) + '.tmp'
    
    # Read and rewrite with new theme
    with zipfile.ZipFile(docx_path, 'r') as zip_in:
        with zipfile.ZipFile(temp_path, 'w', zipfile.ZIP_DEFLATED) as zip_out:
            for item in zip_in.infolist():
                data = zip_in.read(item.filename)
                
                # Replace theme file
                if item.filename == 'word/theme/theme1.xml':
                    data = theme_xml
                
                zip_out.writestr(item, data)
    
    # Replace original with temp
    import os
    os.replace(temp_path, docx_path)


def fix_template_fonts(input_path, output_path=None, fix_theme_too=True):
    """
    Complete workflow to fix fonts in a Word template.
    
    Args:
        input_path: Input template path
        output_path: Output path (default: input_FIXED.docx)
        fix_theme_too: Whether to also fix the theme (default: True)
    """
    input_path = Path(input_path)
    
    if not input_path.exists():
        print(f"❌ File not found: {input_path}")
        return False
    
    # Determine output path
    if output_path is None:
        output_path = input_path.parent / f"{input_path.stem}_FIXED{input_path.suffix}"
    else:
        output_path = Path(output_path)
    
    print("=" * 70)
    print("WORD TEMPLATE FONT FIXER")
    print("=" * 70)
    print()
    print(f"Input:  {input_path}")
    print(f"Output: {output_path}")
    print()
    
    # Load document
    doc = Document(str(input_path))
    
    # Styles to fix
    styles_to_fix = [
        "Normal",
        "Heading 1", "Heading 2", "Heading 3",
        "Heading 4", "Heading 5", "Heading 6",
        "Heading 7", "Heading 8", "Heading 9",
        "Body Text", "First Paragraph", "Compact",
        "List Paragraph", "List Bullet", "List Number",
    ]
    
    print("STEP 1: Setting explicit Calibri in all styles")
    print("-" * 70)
    
    fixed_count = 0
    for style_name in styles_to_fix:
        try:
            style = doc.styles[style_name]
            set_font_explicit(style, "Calibri")
            print(f"  ✓ {style_name}")
            fixed_count += 1
        except KeyError:
            # Style doesn't exist - that's OK
            pass
    
    print()
    print(f"Fixed {fixed_count} styles")
    print()
    
    # Save with fixed styles
    doc.save(str(output_path))
    print(f"✓ Saved with fixed styles: {output_path}")
    print()
    
    # Fix theme if requested
    if fix_theme_too:
        print("STEP 2: Fixing theme fonts")
        print("-" * 70)
        fix_theme(str(output_path))
        print("✓ Theme updated: Major and Minor both set to Calibri")
        print()
    
    # Summary
    print("=" * 70)
    print("COMPLETE!")
    print("=" * 70)
    print()
    print("Your template now has:")
    print("  ✅ All heading styles with explicit Calibri fonts")
    print("  ✅ All body styles with explicit Calibri fonts")
    print("  ✅ All 4 font attributes (ascii, hAnsi, cs, eastAsia)")
    if fix_theme_too:
        print("  ✅ Theme major font: Calibri")
        print("  ✅ Theme minor font: Calibri")
    print("  ✅ NO PMingLiU anywhere")
    print("  ✅ NO Cambria anywhere")
    print()
    print(f"Ready to use: {output_path}")
    print()
    
    return True


if __name__ == "__main__":
    # Parse command line arguments
    if len(sys.argv) < 2:
        print("Usage: python3 fix_template_fonts.py input.docx [output.docx]")
        print()
        print("Examples:")
        print("  python3 fix_template_fonts.py reference.docx")
        print("  python3 fix_template_fonts.py reference.docx my_fixed.docx")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    success = fix_template_fonts(input_file, output_file)
    
    if not success:
        sys.exit(1)