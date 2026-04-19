#!/usr/bin/env python3
"""
OpenSearch Phase 2+3 setup — ISM policies, index templates, snapshot repository, SM policies.
Idempotent: creates or updates, never deletes existing data.
Replica count auto-detected: 0 for single-node, 1 for cluster.
Snapshot repository: only registered when GARAGE_ENDPOINT + GARAGE_ACCESS_KEY are set.

Run order in docker-compose: after opensearch is healthy, before backend.
"""

import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

OPENSEARCH_URL   = os.environ.get("OPENSEARCH_URL", "http://isms-core-opensearch:9200")
GARAGE_ENDPOINT  = os.environ.get("GARAGE_ENDPOINT", "")
GARAGE_ACCESS_KEY = os.environ.get("GARAGE_ACCESS_KEY", "")
GARAGE_SECRET_KEY = os.environ.get("GARAGE_SECRET_KEY", "")
GARAGE_BUCKET_SNAPSHOTS = os.environ.get("GARAGE_BUCKET_SNAPSHOTS", "isms-snapshots")
SCRIPTS_DIR      = Path(__file__).parent


def api(method: str, path: str, data=None) -> dict:
    url  = f"{OPENSEARCH_URL}{path}"
    body = json.dumps(data).encode() if data is not None else None
    req  = urllib.request.Request(url, data=body, method=method)
    req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            raw = resp.read()
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as exc:
        body_text = exc.read().decode(errors="replace")
        raise RuntimeError(f"HTTP {exc.code} {method} {path}: {body_text}") from exc


def wait_for_opensearch(retries: int = 60, delay: float = 3.0):
    print("Waiting for OpenSearch...", flush=True)
    for attempt in range(retries):
        try:
            health = api("GET", "/_cluster/health")
            status = health.get("status", "red")
            if status in ("green", "yellow"):
                nodes = health.get("number_of_nodes", 1)
                print(f"OpenSearch ready — {nodes} node(s), status: {status}", flush=True)
                return nodes
        except Exception:
            pass
        if attempt % 10 == 9:
            print(f"  still waiting... ({attempt + 1}/{retries})", flush=True)
        time.sleep(delay)
    raise SystemExit("OpenSearch did not become ready in time.")


def detect_replicas(node_count: int) -> int:
    replicas = 0 if node_count == 1 else 1
    print(f"Replica count: {replicas} ({'single-node' if replicas == 0 else '3-node cluster'})", flush=True)
    return replicas


def apply_ism_policies():
    policy_dir = SCRIPTS_DIR / "ism"
    for policy_file in sorted(policy_dir.glob("*.json")):
        policy_id = policy_file.stem
        payload   = json.loads(policy_file.read_text())

        try:
            existing = api("GET", f"/_plugins/_ism/policies/{policy_id}")
            seq  = existing.get("_seq_no")
            prim = existing.get("_primary_term")
            api("PUT", f"/_plugins/_ism/policies/{policy_id}?if_seq_no={seq}&if_primary_term={prim}", payload)
            print(f"  ISM policy updated:  {policy_id}", flush=True)
        except RuntimeError as exc:
            if "404" in str(exc):
                api("PUT", f"/_plugins/_ism/policies/{policy_id}", payload)
                print(f"  ISM policy created:  {policy_id}", flush=True)
            else:
                raise


def apply_index_templates(replicas: int):
    template_dir = SCRIPTS_DIR / "templates"
    for tmpl_file in sorted(template_dir.glob("*.json")):
        tmpl_name = tmpl_file.stem
        raw       = tmpl_file.read_text().replace('"__REPLICAS__"', str(replicas))
        payload   = json.loads(raw)

        api("PUT", f"/_index_template/{tmpl_name}", payload)
        print(f"  Index template upserted: {tmpl_name}", flush=True)


def register_snapshot_repository():
    if not GARAGE_ENDPOINT or not GARAGE_ACCESS_KEY or not GARAGE_SECRET_KEY:
        print("  Garage env not set — skipping snapshot repository registration.", flush=True)
        return

    payload = {
        "type": "s3",
        "settings": {
            "bucket": GARAGE_BUCKET_SNAPSHOTS,
            "endpoint": GARAGE_ENDPOINT.removeprefix("http://").removeprefix("https://"),
            "protocol": "http" if GARAGE_ENDPOINT.startswith("http://") else "https",
            "path_style_access": True,
            "region": "garage",
            "access_key": GARAGE_ACCESS_KEY,
            "secret_key": GARAGE_SECRET_KEY,
            "compress": True,
        }
    }

    try:
        api("PUT", "/_snapshot/garage-s3", payload)
        print("  Snapshot repository registered: garage-s3", flush=True)
    except RuntimeError as exc:
        print(f"  WARNING: snapshot repository registration failed: {exc}", flush=True)

    # Verify
    try:
        api("POST", "/_snapshot/garage-s3/_verify")
        print("  Snapshot repository verified OK.", flush=True)
    except RuntimeError as exc:
        print(f"  WARNING: repository verification failed (Garage may not be running): {exc}", flush=True)


def apply_sm_policies():
    sm_dir = SCRIPTS_DIR / "sm"
    if not sm_dir.exists():
        return

    if not GARAGE_ENDPOINT or not GARAGE_ACCESS_KEY:
        print("  Garage env not set — skipping SM snapshot policies.", flush=True)
        return

    for policy_file in sorted(sm_dir.glob("*.json")):
        policy_id = policy_file.stem
        payload   = json.loads(policy_file.read_text())

        try:
            existing = api("GET", f"/_plugins/_sm/policies/{policy_id}")
            seq  = existing.get("_seq_no")
            prim = existing.get("_primary_term")
            api("PUT", f"/_plugins/_sm/policies/{policy_id}?if_seq_no={seq}&if_primary_term={prim}", payload)
            print(f"  SM policy updated:  {policy_id}", flush=True)
        except RuntimeError as exc:
            if "404" in str(exc):
                api("POST", f"/_plugins/_sm/policies/{policy_id}", payload)
                print(f"  SM policy created:  {policy_id}", flush=True)
            else:
                print(f"  WARNING: SM policy {policy_id} failed: {exc}", flush=True)


def main():
    node_count = wait_for_opensearch()
    replicas   = detect_replicas(node_count)

    print("\nApplying ISM retention policies...", flush=True)
    apply_ism_policies()

    print("\nApplying index templates...", flush=True)
    apply_index_templates(replicas)

    print("\nRegistering Garage S3 snapshot repository...", flush=True)
    register_snapshot_repository()

    print("\nApplying SM snapshot policies...", flush=True)
    apply_sm_policies()

    print("\nOpenSearch setup complete.", flush=True)


if __name__ == "__main__":
    main()
