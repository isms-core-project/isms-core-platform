#!/usr/bin/env python3
"""ISO Reference Seed Extractor.

Extracts and chunks all ISO/regulatory PDFs from the iso-reference directory
and saves them as JSON seed files into datasets/data/iso-reference/.

One JSON file per source document — so individual standards can be updated
independently when a new version is released.

Run all documents:
    cd 60-isms-core-api-factory/datasets
    python extract_iso_seeds.py --skip-download

Re-extract a single file (e.g. after a new ISO version or Acrobat TXT conversion):
    python extract_iso_seeds.py --file ISO_IEC_27002_2022(en).docx --skip-download

Or specify custom paths:
    python extract_iso_seeds.py \
        --iso-dir /path/to/97-isms-core-iso-regulatory \
        --output  /path/to/datasets/data/iso-reference

After running, commit the updated JSON files and rebuild the container.
The platform will auto-load them on next startup if the index is empty,
or use QA → Reference Corpus → Reload to force a refresh on a live system.

Requirements (local, not inside Docker):
    pip install pdfplumber python-docx
"""

import argparse
import json
import sys
from pathlib import Path

# Allow running from any directory by adding the backend src to path
_SCRIPT_DIR = Path(__file__).resolve().parent
_BACKEND_SRC = _SCRIPT_DIR.parent / "backend" / "src"
sys.path.insert(0, str(_BACKEND_SRC))

try:
    from services.iso_extractor import discover_documents, extract_chunks, infer_standard
except ImportError as e:
    print(f"ERROR: Cannot import iso_extractor — {e}")
    print("Make sure you have pdfplumber installed: pip install pdfplumber")
    sys.exit(1)


def _slugify(name: str) -> str:
    """Convert a string to a safe filename slug."""
    import re
    slug = name.lower()
    slug = re.sub(r"[^\w\s-]", "_", slug)
    slug = re.sub(r"[\s-]+", "_", slug)
    return slug.strip("_")


# ---------------------------------------------------------------------------
# Public documents to auto-download if not already present in iso-dir
# ---------------------------------------------------------------------------
_PUBLIC_DOCS: list[dict] = [
    {
        "url": "https://docs-prv.pcisecuritystandards.org/PCI%20DSS/Standard/PCI-DSS-v4_0_1.pdf",
        "dest": "PCI-DSS/PCI-DSS-v4_0_1.pdf",
        "standard": "PCI DSS v4.0.1",
    },
    # Add more public documents here as needed
]


def _download_public_docs(iso_dir: Path) -> None:
    """Download publicly available standards if not already present."""
    import ssl
    import urllib.request
    for doc in _PUBLIC_DOCS:
        dest = iso_dir / doc["dest"]
        if dest.exists():
            print(f"  Already present: {dest.name}")
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        print(f"  Downloading {doc['standard']}…", end="", flush=True)
        try:
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            with urllib.request.urlopen(doc["url"], context=ctx, timeout=60) as resp:
                dest.write_bytes(resp.read())
            print(f" done ({dest.stat().st_size // 1024} KB)")
        except Exception as e:
            print(f" FAILED: {e}")


def _process_file(doc_path: Path, output_dir: Path) -> tuple[int, str]:
    """Extract chunks from a single PDF/TXT/DOCX and write its JSON seed file.

    Returns (chunk_count, output_filename).
    Raises on error.
    """
    chunks = extract_chunks(doc_path)
    if not chunks:
        return 0, ""

    # Stamp source_file on every chunk
    for c in chunks:
        c["source_file"] = doc_path.name

    filename = f"{_slugify(doc_path.stem)}.json"
    out_path = output_dir / filename
    out_path.write_text(json.dumps(chunks, indent=2, ensure_ascii=False))
    return len(chunks), filename


def main():
    parser = argparse.ArgumentParser(description="Extract ISO reference seeds (one JSON per document)")
    parser.add_argument(
        "--iso-dir",
        default=str(_SCRIPT_DIR.parent.parent / "97-isms-core-iso-regulatory"),
        help="Path to the ISO regulatory directory (default: ../97-isms-core-iso-regulatory)",
    )
    parser.add_argument(
        "--output",
        default=str(_SCRIPT_DIR / "data" / "iso-reference"),
        help="Output directory for JSON seed files (default: data/iso-reference/)",
    )
    parser.add_argument(
        "--file",
        metavar="FILENAME",
        help="Process only this filename (e.g. ISO_IEC_27002_2022(en).docx). "
             "Searches recursively under --iso-dir.",
    )
    parser.add_argument(
        "--skip-download",
        action="store_true",
        help="Skip downloading public documents",
    )
    args = parser.parse_args()

    iso_dir = Path(args.iso_dir)
    output_dir = Path(args.output)

    if not iso_dir.exists():
        print(f"ERROR: ISO directory not found: {iso_dir}")
        sys.exit(1)

    output_dir.mkdir(parents=True, exist_ok=True)
    print(f"ISO source : {iso_dir}")
    print(f"Output dir : {output_dir}")
    print()

    if not args.skip_download:
        print("Downloading public documents…")
        _download_public_docs(iso_dir)
        print()

    # Single-file mode
    if args.file:
        matches = list(iso_dir.rglob(args.file))
        if not matches:
            print(f"ERROR: File not found under {iso_dir}: {args.file}")
            sys.exit(1)
        doc_path = matches[0]
        standard = infer_standard(doc_path)
        print(f"Single-file mode: {doc_path.name}  [{standard}]")
        try:
            count, filename = _process_file(doc_path, output_dir)
            if count:
                print(f"Written: {filename} ({count} chunks)")
                _update_manifest(output_dir)
            else:
                print("No chunks extracted — file skipped or unsupported.")
        except Exception as e:
            print(f"FAILED: {e}")
            sys.exit(1)
        return

    # Full run
    documents = discover_documents(iso_dir)
    print(f"Found {len(documents)} documents to process\n")

    total_chunks = 0
    written: list[dict] = []
    failed: list[str] = []

    for doc_path in documents:
        standard = infer_standard(doc_path)
        print(f"  → {doc_path.name[:60]:<60}  [{standard}]", end="", flush=True)
        try:
            count, filename = _process_file(doc_path, output_dir)
            if count:
                total_chunks += count
                written.append({"file": filename, "source": doc_path.name, "standard": standard, "chunks": count})
                print(f"  {count} chunks  →  {filename}")
            else:
                print("  (no chunks extracted)")
                failed.append(doc_path.name)
        except Exception as e:
            print(f"  FAILED: {e}")
            failed.append(doc_path.name)

    print()
    _update_manifest(output_dir, written, failed, total_chunks, len(documents))

    print("=" * 70)
    print(f"Done. {total_chunks:,} total chunks across {len(written)} files.")
    if failed:
        print(f"  {len(failed)} files failed/empty: {', '.join(failed)}")
    print(f"\nManifest: {output_dir / '_manifest.json'}")
    print("\nNext steps:")
    print("  1. git add datasets/data/iso-reference/")
    print("  2. git commit -m 'data: update ISO reference seeds'")
    print("  3. docker compose build backend && docker compose up -d backend")
    print("     (seeds auto-load on startup if index is empty)")
    print("  4. Or: QA → Reference Corpus → Reload (on a live system)")


def _update_manifest(
    output_dir: Path,
    written: list[dict] | None = None,
    failed: list[str] | None = None,
    total_chunks: int = 0,
    total_files_processed: int = 0,
) -> None:
    """Write / update _manifest.json from the current JSON files in output_dir."""
    if written is None:
        # Rebuild from existing JSON files on disk (used after single-file update)
        written = []
        total_chunks = 0
        for f in sorted(output_dir.glob("*.json")):
            if f.name.startswith("_"):
                continue
            try:
                chunks = json.loads(f.read_text(encoding="utf-8"))
                n = len(chunks)
                standard = chunks[0].get("standard", f.stem) if chunks else f.stem
                source = chunks[0].get("source_file", "") if chunks else ""
                written.append({"file": f.name, "source": source, "standard": standard, "chunks": n})
                total_chunks += n
            except Exception:
                pass
        total_files_processed = len(written)
        failed = []

    manifest = {
        "files": written,
        "total_chunks": total_chunks,
        "total_files_processed": total_files_processed,
        "failed_files": failed or [],
    }
    (output_dir / "_manifest.json").write_text(json.dumps(manifest, indent=2))


if __name__ == "__main__":
    main()
