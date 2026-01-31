# Markdown → Word Conversion (ISMS Standard)

This document describes the **standard, secure, and reproducible** process to:
- Install Python dependencies on Ubuntu 24.04+
- Generate the Word reference template
- Convert Markdown (`.md`) to Word (`.docx`) using Pandoc
- Preserve file names and structure

---

## 1. Python Environment Setup (Ubuntu 24.04+)

Ubuntu 24.04 enforces **PEP 668** (externally managed Python environments).  
System-wide `pip install` is **not allowed**.

### 1.1 Install virtual environment support

```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip pandoc
1.2 Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate
```

You should now see (venv) in your shell prompt.

## 2. Install Python Dependencies
pip install python-docx

This installs dependencies inside the virtual environment only
(no impact on system Python).

## 3. Generate the Word Reference Template

Run the provided script:

python generate_isms_reference_docx_std.py
python generate_isms_reference_docx_pol.py

Output:

isms-reference.docx

This file is used as the Pandoc Word template (--reference-doc).

## 4. Convert Markdown to Word (Pandoc)

### 4.1 Basic conversion using reference template
pandoc input.md \
  --reference-doc=isms-reference.docx \
  -o output.docx

### 4.2 Keep the Markdown filename as Word filename (recommended)
pandoc "ISMS-POL-A.8.24 - Use of Cryptography.md" \
  --reference-doc=isms-reference.docx \
  -o "ISMS-POL-A.8.24.docx"

Markdown name ➜ Word name (1:1 mapping).

### 4.3 Add Table of Contents (typical for POL / IMP docs)

pandoc "input.md" \
  --reference-doc=isms-reference.docx \
  --toc \
  --toc-depth=3 \
  -o "input.docx"

pandoc "ISMS-POL-A.8.24 - Use of Cryptography.md" \
  --reference-doc=isms-reference.docx \
  --toc \
  --toc-depth=3 \
  -o "ISMS-POL-A.8.24.docx"

### 4.4 Batch convert all Markdown files in a folder

for f in *.md; do
  pandoc "$f" \
    --reference-doc=isms-reference.docx \
    -o "${f%.md}.docx"
done

for f in "./pol - md"/*.md; do
  pandoc "$f" \
    --reference-doc=isms-reference.docx \
    -o "./pol - word/$(basename "${f%.md}.docx")"
done

shopt -s nullglob
for f in "./pol - md"/*.md; do
  pandoc "$f" \
    --reference-doc=isms-reference.docx \
    -o "./pol - word/$(basename "${f%.md}.docx")"
done

## 5. Notes for ISMS / Audit

Word template is generated programmatically

Markdown is the single source of truth

Formatting consistency is enforced automatically

Python dependencies are isolated via venv

No modification of system-managed Python packages

This approach supports:

ISO/IEC 27001:2022 A.8.28 (Secure Coding)

A.7.5 (Documented Information)

Reproducibility and traceability

## 6. Deactivate Virtual Environment (when done)
deactivate


**End of document**