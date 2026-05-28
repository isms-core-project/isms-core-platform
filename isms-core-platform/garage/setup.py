#!/usr/bin/env python3
"""
Garage S3 first-boot setup.
Runs once: assigns layout, creates buckets, imports access key + permissions.
Idempotent — skips silently if already configured.
Uses the Garage admin REST API (port 3903). No CLI binary required.
"""

import json
import os
import sys
import time
import urllib.error
import urllib.request

ADMIN_URL   = os.environ["GARAGE_ADMIN_URL"]          # http://isms-core-garage:3903
ADMIN_TOKEN = os.environ["GARAGE_ADMIN_TOKEN"]         # isms-core-garage-admin
ACCESS_KEY  = os.environ["GARAGE_ACCESS_KEY"]
SECRET_KEY  = os.environ["GARAGE_SECRET_KEY"]
BUCKETS     = ["isms-evidence", "isms-snapshots", "isms-exports"]
LAYOUT_CAP  = 10 * 1024 * 1024 * 1024  # 10 GiB


def api(method: str, path: str, data=None):
    url  = f"{ADMIN_URL}{path}"
    body = json.dumps(data).encode() if data is not None else None
    req  = urllib.request.Request(url, data=body, method=method)
    req.add_header("Authorization", f"Bearer {ADMIN_TOKEN}")
    if body:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            raw = resp.read()
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return None
        body_text = exc.read().decode(errors="replace")
        raise RuntimeError(f"HTTP {exc.code} {method} {path}: {body_text}") from exc


def wait_for_garage(retries: int = 60, delay: float = 2.0):
    print("Waiting for Garage admin API...", flush=True)
    url = f"{ADMIN_URL}/health"
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, method="GET")
            req.add_header("Authorization", f"Bearer {ADMIN_TOKEN}")
            with urllib.request.urlopen(req, timeout=10) as resp:
                resp.read()  # /health returns plain text "OK", not JSON — just check 200
            print("Garage is ready.", flush=True)
            return
        except Exception:
            if attempt % 10 == 9:
                print(f"  still waiting... ({attempt + 1}/{retries})", flush=True)
            time.sleep(delay)
    raise SystemExit("Garage did not become ready in time.")


def already_configured() -> bool:
    """True only when buckets exist AND our access key is present."""
    buckets = api("GET", "/v2/ListBuckets") or []
    existing = {
        alias
        for b in buckets
        for alias in b.get("globalAliases", [])
    }
    if "isms-evidence" not in existing:
        return False
    try:
        key = api("GET", f"/v2/GetKeyInfo?id={ACCESS_KEY}")
        return key is not None
    except RuntimeError:
        return False


def assign_layout():
    status  = api("GET", "/v2/GetClusterStatus")
    node_id = status["nodes"][0]["id"]
    print(f"Node: {node_id[:16]}...", flush=True)

    api("POST", "/v2/UpdateClusterLayout", [{"node_id": node_id, "zone": "dc1", "capacity": LAYOUT_CAP, "tags": []}])

    # Apply with current_version + 1 (never hardcode version)
    current = api("GET", "/v2/GetClusterLayout")
    version = current.get("version", 0) + 1
    api("POST", "/v2/ApplyClusterLayout", {"version": version})
    print(f"Layout assigned (dc1, 10 GiB, version {version}).", flush=True)


def create_buckets():
    existing = {
        alias
        for b in (api("GET", "/v2/ListBuckets") or [])
        for alias in b.get("globalAliases", [])
    }
    for name in BUCKETS:
        if name in existing:
            print(f"  bucket '{name}': already exists.", flush=True)
            continue
        result = api("POST", "/v2/CreateBucket", {"globalAlias": name})
        print(f"  bucket '{name}': {result['id'][:16]}...", flush=True)


def import_key() -> str:
    """Import access key. Returns the actual key ID assigned by Garage."""
    resp = api("POST", "/v2/ImportKey", {
        "accessKeyId":     ACCESS_KEY,
        "secretAccessKey": SECRET_KEY,
        "name":            "isms-core",
    })
    key_id = (resp or {}).get("accessKeyId", ACCESS_KEY)
    print(f"  key '{key_id}' imported.", flush=True)
    return key_id


def grant_permissions(key_id: str):
    bucket_list = api("GET", "/v2/ListBuckets") or []
    id_map = {
        alias: b["id"]
        for b in bucket_list
        for alias in b.get("globalAliases", [])
    }
    for name in BUCKETS:
        bucket_id = id_map.get(name)
        if not bucket_id:
            print(f"  WARNING: bucket '{name}' not found, skipping permissions.", flush=True)
            continue
        api("POST", "/v2/AllowBucketKey", {
            "bucketId":    bucket_id,
            "accessKeyId": key_id,
            "permissions": {"read": True, "write": True, "owner": True},
        })
        print(f"  permissions granted for '{name}'.", flush=True)


def main():
    wait_for_garage()

    if already_configured():
        print("Garage already configured — nothing to do.", flush=True)
        sys.exit(0)

    print("Configuring Garage...", flush=True)
    assign_layout()

    print("Creating buckets...", flush=True)
    create_buckets()

    print("Importing access key...", flush=True)
    key_id = import_key()

    print("Granting bucket permissions...", flush=True)
    grant_permissions(key_id)

    print("Garage setup complete.", flush=True)


if __name__ == "__main__":
    main()
