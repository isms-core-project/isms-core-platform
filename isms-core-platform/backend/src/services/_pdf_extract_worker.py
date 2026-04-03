#!/usr/bin/env python3
"""Subprocess worker for PDF text extraction.

Called by iso_extractor._extract_with_pdfplumber() as an isolated process.
Running in a subprocess means the parent can killpg(SIGKILL) the entire
process group on timeout — works reliably even for C-extension hangs.

Tries PyMuPDF first (fast, low-memory), falls back to pdfplumber.
Outputs JSON to stdout: {"pages": [...], "total": N}

Usage: python _pdf_extract_worker.py <pdf_path> <max_pages>
"""
import json
import sys


def extract_with_pymupdf(path: str, max_pages: int) -> tuple[list[str], int]:
    import fitz  # type: ignore  # PyMuPDF
    doc = fitz.open(path)
    total = len(doc)
    pages: list[str] = []
    for i in range(min(total, max_pages)):
        page = doc[i]
        text = page.get_text("text")
        if text and len(text.strip()) > 20:
            pages.append(text.strip())
        page = None  # release immediately
    doc.close()
    return pages, total


def extract_with_pdfplumber(path: str, max_pages: int) -> tuple[list[str], int]:
    import pdfplumber  # type: ignore
    pages: list[str] = []
    total = 0
    with pdfplumber.open(path) as pdf:
        total = len(pdf.pages)
        for page in pdf.pages[:max_pages]:
            try:
                text = page.extract_text()
                if text and len(text.strip()) > 20:
                    pages.append(text)
            except Exception:
                continue
    return pages, total


def main() -> None:
    path = sys.argv[1]
    max_pages = int(sys.argv[2])

    try:
        try:
            pages, total = extract_with_pymupdf(path, max_pages)
        except ImportError:
            pages, total = extract_with_pdfplumber(path, max_pages)

        print(json.dumps({"pages": pages, "total": total}))
    except Exception as e:
        print(json.dumps({"pages": [], "total": 0, "error": str(e)}))


if __name__ == "__main__":
    main()
