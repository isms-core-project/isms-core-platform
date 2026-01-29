#!/bin/bash
# md2docx - Quick markdown to docx converter
# Usage: ./md2docx README.md

if [ -z "$1" ]; then
    echo "Usage: $0 input.md [output.docx]"
    exit 1
fi

INPUT="$1"
OUTPUT="${2:-${INPUT%.md}.docx}"

if ! command -v pandoc &> /dev/null; then
    echo "❌ pandoc not installed"
    echo "   Linux: sudo apt install pandoc"
    echo "   macOS: brew install pandoc"
    exit 1
fi

echo "📄 Converting: $INPUT → $OUTPUT"

pandoc "$INPUT" \
    -o "$OUTPUT" \
    --standalone \
    --toc \
    --number-sections \
    --highlight-style=tango \
    --wrap=preserve

if [ $? -eq 0 ]; then
    echo "✅ Success! Output: $OUTPUT"
    ls -lh "$OUTPUT"
else
    echo "❌ Conversion failed"
    exit 1
fi