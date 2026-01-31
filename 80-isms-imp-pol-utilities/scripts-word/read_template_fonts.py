#!/usr/bin/env python3
"""
Read and display all font settings in a Word template.

Usage:
    python3 read_template_fonts.py reference.docx
    
Or just:
    python3 read_template_fonts.py
    (will look for reference.docx in current directory)
"""

import sys
from docx import Document
import zipfile
import re
from pathlib import Path


def read_template_fonts(docx_path):
    """Read and display all font settings from a Word template."""
    
    if not Path(docx_path).exists():
        print(f"❌ File not found: {docx_path}")
        print(f"Current directory: {Path.cwd()}")
        return
    
    print("=" * 70)
    print(f"FONT ANALYSIS: {docx_path}")
    print("=" * 70)
    print()
    
    # Load document
    doc = Document(docx_path)
    
    # ======================================================================
    # PART 1: High-level view (what python-docx sees)
    # ======================================================================
    
    print("1. HIGH-LEVEL VIEW (What python-docx reports):")
    print("-" * 70)
    
    styles_to_check = ["Normal", "Heading 1", "Heading 2", "Heading 3"]
    
    for style_name in styles_to_check:
        try:
            style = doc.styles[style_name]
            font = style.font.name if style.font.name else "(not set)"
            size = f"{style.font.size.pt}pt" if style.font.size else "(not set)"
            print(f"{style_name:15} Font: {font:15} Size: {size}")
        except KeyError:
            print(f"{style_name:15} NOT FOUND")
    
    print()
    
    # ======================================================================
    # PART 2: XML analysis (the ground truth)
    # ======================================================================
    
    print("2. XML ANALYSIS (The actual truth in the file):")
    print("-" * 70)
    
    with zipfile.ZipFile(docx_path, 'r') as z:
        styles_xml = z.read('word/styles.xml').decode('utf-8')
        
        # Check each heading style
        for heading_num in [1, 2, 3]:
            style_id = f"Heading{heading_num}"
            
            # Find the style definition
            pattern = f'<w:style[^>]*w:styleId="{style_id}"[^>]*>(.*?)</w:style>'
            match = re.search(pattern, styles_xml, re.DOTALL)
            
            if not match:
                print(f"\nHeading {heading_num}: NOT FOUND")
                continue
            
            style_xml = match.group(1)
            
            print(f"\nHeading {heading_num}:")
            
            # Look for rFonts element
            rfonts = re.search(r'<w:rFonts[^>]*/?>', style_xml)
            
            if not rfonts:
                print("  ⚠ NO rFonts element → Will inherit from theme")
                continue
            
            rfonts_tag = rfonts.group(0)
            print(f"  Raw XML: {rfonts_tag}")
            print()
            
            # Parse each font attribute
            attributes = [
                ('w:ascii', 'Latin text (English, German, etc.)'),
                ('w:hAnsi', 'High ANSI (Western European)'),
                ('w:cs', 'Complex Scripts (Arabic, Hebrew)'),
                ('w:eastAsia', 'East Asian (Chinese, Japanese, Korean)'),
            ]
            
            for attr_name, description in attributes:
                if f'{attr_name}=' in rfonts_tag:
                    font_match = re.search(f'{attr_name}="([^"]+)"', rfonts_tag)
                    if font_match:
                        font_value = font_match.group(1)
                        status = ""
                        
                        # Flag problematic fonts
                        if font_value == "PMingLiU":
                            status = " ← ⚠️ CHINESE FONT!"
                        elif font_value == "Cambria":
                            status = " ← ⚠️ Should be Calibri?"
                        elif font_value == "Calibri":
                            status = " ✅"
                        
                        print(f"    • {description:45} {font_value}{status}")
                    else:
                        print(f"    • {description:45} NOT SET → theme")
                else:
                    print(f"    • {description:45} NOT SET → theme")
    
    print()
    
    # ======================================================================
    # PART 3: Theme fonts
    # ======================================================================
    
    print("=" * 70)
    print("3. THEME FONTS (Fallback when style doesn't specify):")
    print("-" * 70)
    
    with zipfile.ZipFile(docx_path, 'r') as z:
        theme_xml = z.read('word/theme/theme1.xml').decode('utf-8')
        
        major = re.search(r'<a:majorFont>.*?<a:latin typeface="([^"]+)"', 
                         theme_xml, re.DOTALL)
        minor = re.search(r'<a:minorFont>.*?<a:latin typeface="([^"]+)"', 
                         theme_xml, re.DOTALL)
        
        major_font = major.group(1) if major else '?'
        minor_font = minor.group(1) if minor else '?'
        
        print(f"Major font (headings): {major_font}", end="")
        if major_font == "Cambria":
            print(" ⚠️ (Should be Calibri?)")
        elif major_font == "Calibri":
            print(" ✅")
        else:
            print()
        
        print(f"Minor font (body):     {minor_font}", end="")
        if minor_font == "Calibri":
            print(" ✅")
        else:
            print()
    
    print()
    
    # ======================================================================
    # PART 4: Summary and recommendations
    # ======================================================================
    
    print("=" * 70)
    print("4. SUMMARY:")
    print("-" * 70)
    print()
    
    with zipfile.ZipFile(docx_path, 'r') as z:
        styles_xml = z.read('word/styles.xml').decode('utf-8')
        theme_xml = z.read('word/theme/theme1.xml').decode('utf-8')
        
        issues = []
        
        # Check for PMingLiU
        if 'PMingLiU' in styles_xml:
            issues.append("❌ Found PMingLiU (Chinese font) in styles")
        
        # Check for Cambria in theme
        theme_major = re.search(r'<a:majorFont>.*?<a:latin typeface="([^"]+)"', 
                               theme_xml, re.DOTALL)
        if theme_major and theme_major.group(1) == "Cambria":
            issues.append("⚠️  Theme has Cambria for heading font")
        
        # Check if headings have explicit Calibri
        h1_explicit = 'w:ascii="Calibri"' in re.search(
            r'<w:style[^>]*w:styleId="Heading1"[^>]*>(.*?)</w:style>',
            styles_xml, re.DOTALL
        ).group(1) if re.search(
            r'<w:style[^>]*w:styleId="Heading1"[^>]*>(.*?)</w:style>',
            styles_xml, re.DOTALL
        ) else False
        
        if not h1_explicit:
            issues.append("⚠️  Headings don't have explicit Calibri (rely on theme)")
        
        if not issues:
            print("✅✅✅ PERFECT! Template looks good!")
        else:
            print("Issues found:")
            for issue in issues:
                print(f"  {issue}")
            print()
            print("Recommendation: Run fix_template_fonts.py to fix these issues")
    
    print()
    print("=" * 70)


if __name__ == "__main__":
    # Get filename from command line or use default
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "reference.docx"
    
    read_template_fonts(filename)