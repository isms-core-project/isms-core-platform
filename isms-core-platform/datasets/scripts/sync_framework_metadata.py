"""
sync_framework_metadata.py

Reads all bundle JSON files in datasets/data/ and updates the `frameworks` table
in the DB to match the `framework` block in each file.

Use this after manually editing a dataset's framework name, version, description,
or source_url — the bundle_loader skips re-processing files whose content_hash
hasn't changed, so edits to framework metadata won't propagate via the normal
load path.

Usage:
    python3 datasets/scripts/sync_framework_metadata.py [--dry-run]

Options:
    --dry-run   Print planned changes without writing to the DB.

Requirements:
    DATABASE_URL env var (or .env file at project root).
"""

import argparse
import json
import os
import sys
from pathlib import Path

# Allow running from project root or datasets/scripts/
PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT / "backend" / "src"))

try:
    from dotenv import load_dotenv
    load_dotenv(PROJECT_ROOT / ".env")
except ImportError:
    pass

import psycopg2

DATA_DIR = PROJECT_ROOT / "datasets" / "data"

UPDATABLE_FIELDS = ["name", "version", "description", "source_url", "publisher", "jurisdiction"]


def get_connection():
    db_url = os.environ.get("DATABASE_URL")
    if not db_url:
        # Fallback: build from individual vars (matches docker-compose defaults)
        host = os.environ.get("POSTGRES_HOST", "localhost")
        port = os.environ.get("POSTGRES_PORT", "5432")
        user = os.environ.get("POSTGRES_USER", "isms_user")
        password = os.environ.get("POSTGRES_PASSWORD", "isms_pass")
        db = os.environ.get("POSTGRES_DB", "isms_db")
        db_url = f"postgresql://{user}:{password}@{host}:{port}/{db}"
    return psycopg2.connect(db_url)


def load_framework_blocks() -> list[dict]:
    """Return list of (file, framework_block) for every dataset with a framework key."""
    results = []
    for fp in sorted(DATA_DIR.glob("*.json")):
        try:
            data = json.loads(fp.read_text())
        except Exception:
            continue
        if not isinstance(data, dict):
            continue
        fw = data.get("framework")
        if fw and isinstance(fw, dict) and fw.get("id"):
            results.append({"file": fp.name, "framework": fw})
    return results


def fetch_db_frameworks(cur) -> dict[str, dict]:
    """Return dict keyed by UUID string of current DB framework rows."""
    cur.execute("SELECT id::text, name, version, description, source_url, publisher, jurisdiction FROM frameworks")
    return {
        row[0]: {
            "name": row[1],
            "version": row[2],
            "description": row[3],
            "source_url": row[4],
            "publisher": row[5],
            "jurisdiction": row[6],
        }
        for row in cur.fetchall()
    }


def sync(dry_run: bool = False):
    entries = load_framework_blocks()
    if not entries:
        print("No framework blocks found in datasets/data/ — nothing to do.")
        return

    conn = get_connection()
    cur = conn.cursor()
    db_frameworks = fetch_db_frameworks(cur)

    updated = 0
    skipped = 0
    not_found = 0

    for entry in entries:
        fw = entry["framework"]
        fw_id = fw["id"]
        filename = entry["file"]

        if fw_id not in db_frameworks:
            print(f"  NOT IN DB  {filename}  (id={fw_id}) — run bundle loader first")
            not_found += 1
            continue

        db = db_frameworks[fw_id]
        changes = {}
        for field in UPDATABLE_FIELDS:
            json_val = fw.get(field)
            db_val = db.get(field)
            if json_val is not None and json_val != db_val:
                changes[field] = {"from": db_val, "to": json_val}

        if not changes:
            skipped += 1
            continue

        print(f"  UPDATE  {filename}")
        for field, diff in changes.items():
            print(f"    {field}: {repr(diff['from'])} → {repr(diff['to'])}")

        if not dry_run:
            set_clause = ", ".join(f"{f} = %s" for f in changes)
            values = [changes[f]["to"] for f in changes] + [fw_id]
            cur.execute(
                f"UPDATE frameworks SET {set_clause} WHERE id::text = %s",
                values,
            )
        updated += 1

    if not dry_run:
        conn.commit()
        print(f"\nDone. {updated} updated, {skipped} unchanged, {not_found} not in DB.")
    else:
        print(f"\nDry run. {updated} would update, {skipped} unchanged, {not_found} not in DB.")

    cur.close()
    conn.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sync framework metadata from JSON datasets to DB.")
    parser.add_argument("--dry-run", action="store_true", help="Print changes without writing.")
    args = parser.parse_args()
    sync(dry_run=args.dry_run)
