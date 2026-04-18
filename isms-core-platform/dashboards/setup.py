#!/usr/bin/env python3
"""
OpenSearch Dashboards — bootstrap index patterns + sample dashboards.
Idempotent: uses overwrite=true on import.

Startup sequence:
  1. Seed OpenSearch indices with field mappings (so OSD can discover fields)
  2. Import OSD saved objects: index patterns, visualizations, dashboards

Objects created:
  Index patterns : evidence-*, audit-logs-*, connector-runs-*
  Dashboards     : Evidence Overview, Audit Logs, Connector Health
  Visualizations : 4 per dashboard (metric + timeline + 2 pies)
"""

import json
import os
import sys
import time
import urllib.error
import urllib.request

DASHBOARDS_URL  = os.environ.get("DASHBOARDS_URL",  "http://isms-core-dashboards:5601")
OPENSEARCH_URL  = os.environ.get("OPENSEARCH_URL",  "http://isms-core-opensearch:9200")


# ── OpenSearch index seeding ──────────────────────────────────────────────────

INDICES = {
    "evidence-000001": {
        "aliases": {"evidence": {}},
        "mappings": {
            "properties": {
                "collected_at":    {"type": "date"},
                "connector_id":    {"type": "keyword"},
                "control_ids":     {"type": "keyword"},
                "evidence_type":   {"type": "keyword"},
                "org_id":          {"type": "integer"},
                "status":          {"type": "keyword"},
                "title":           {"type": "text"},
            }
        },
    },
    "audit-logs-000001": {
        "aliases": {"audit-logs": {}},
        "mappings": {
            "properties": {
                "timestamp":       {"type": "date"},
                "user_email":      {"type": "keyword"},
                "action":          {"type": "keyword"},
                "resource_type":   {"type": "keyword"},
                "resource_id":     {"type": "keyword"},
                "org_id":          {"type": "integer"},
                "ip_address":      {"type": "ip"},
            }
        },
    },
    "connector-runs-000001": {
        "aliases": {"connector-runs": {}},
        "mappings": {
            "properties": {
                "started_at":      {"type": "date"},
                "finished_at":     {"type": "date"},
                "connector_name":  {"type": "keyword"},
                "connector_id":    {"type": "keyword"},
                "status":          {"type": "keyword"},
                "org_id":          {"type": "integer"},
                "evidence_count":  {"type": "integer"},
                "error_message":   {"type": "text"},
            }
        },
    },
}


def _os_request(method: str, path: str, body: dict = None):
    url = f"{OPENSEARCH_URL}{path}"
    data = json.dumps(body).encode() if body else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as exc:
        return {"_status": exc.code, "_body": exc.read().decode(errors="replace")}


def seed_opensearch_indices():
    print("Seeding OpenSearch indices with field mappings...", flush=True)
    for name, body in INDICES.items():
        # Check if already exists
        check = _os_request("HEAD", f"/{name}")
        if isinstance(check, dict) and check.get("_status") == 404:
            result = _os_request("PUT", f"/{name}", body)
            if result.get("acknowledged"):
                print(f"  created: {name}", flush=True)
            else:
                print(f"  WARNING creating {name}: {result}", flush=True)
        else:
            print(f"  exists:  {name}", flush=True)


# ── OSD HTTP ──────────────────────────────────────────────────────────────────

def _request(method: str, path: str, data: bytes = None,
             content_type: str = "application/json") -> dict:
    url = f"{DASHBOARDS_URL}{path}"
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("osd-xsrf", "true")
    if data:
        req.add_header("Content-Type", content_type)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            raw = resp.read()
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as exc:
        body = exc.read().decode(errors="replace")
        raise RuntimeError(f"HTTP {exc.code} {method} {path}: {body}") from exc


def wait_for_dashboards(retries: int = 60, delay: float = 3.0):
    print("Waiting for OpenSearch Dashboards...", flush=True)
    for attempt in range(retries):
        try:
            with urllib.request.urlopen(f"{DASHBOARDS_URL}/api/status", timeout=5) as r:
                if r.status == 200:
                    print("Dashboards ready.", flush=True)
                    return
        except Exception:
            pass
        if attempt % 10 == 9:
            print(f"  still waiting... ({attempt + 1}/{retries})", flush=True)
        time.sleep(delay)
    raise SystemExit("Dashboards did not become ready in time.")


# ── Saved-object builders ─────────────────────────────────────────────────────

def _ss(index_id: str) -> str:
    return json.dumps({
        "index": index_id,
        "query": {"query": "", "language": "kuery"},
        "filter": [],
    })


def _metric(obj_id: str, title: str, index_id: str) -> dict:
    vis_state = {
        "title": title, "type": "metric",
        "params": {
            "addTooltip": True, "addLegend": False, "type": "metric",
            "metric": {
                "percentageMode": False, "useRanges": False,
                "colorSchema": "Green to Red", "metricColorMode": "None",
                "colorsRange": [{"from": 0, "to": 10000}],
                "labels": {"show": True}, "invertColors": False,
                "style": {"bgFill": "#000", "bgColor": False,
                          "labelColor": False, "subText": "", "fontSize": 60},
            },
        },
        "aggs": [{"id": "1", "enabled": True, "type": "count",
                  "schema": "metric", "params": {}}],
    }
    return {
        "type": "visualization", "id": obj_id,
        "attributes": {
            "title": title,
            "visState": json.dumps(vis_state),
            "uiStateJSON": "{}",
            "kibanaSavedObjectMeta": {"searchSourceJSON": _ss(index_id)},
        },
        "references": [{"name": "kibanaSavedObjectMeta.searchSourceJSON.index",
                        "type": "index-pattern", "id": index_id}],
    }


def _timeline(obj_id: str, title: str, index_id: str, time_field: str) -> dict:
    vis_state = {
        "title": title, "type": "histogram",
        "params": {
            "type": "histogram",
            "grid": {"categoryLines": False},
            "categoryAxes": [{"id": "CategoryAxis-1", "type": "category",
                              "position": "bottom", "show": True,
                              "scale": {"type": "linear"},
                              "labels": {"show": True, "truncate": 100}, "title": {}}],
            "valueAxes": [{"id": "ValueAxis-1", "name": "LeftAxis-1",
                           "type": "value", "position": "left", "show": True,
                           "scale": {"type": "linear"},
                           "labels": {"show": True, "rotate": 0,
                                      "filter": False, "truncate": 100},
                           "title": {"text": "Count"}}],
            "seriesParams": [{"show": True, "type": "histogram", "mode": "stacked",
                              "data": {"label": "Count", "id": "1"},
                              "valueAxis": "ValueAxis-1",
                              "drawLinesBetweenPoints": True,
                              "lineWidth": 2, "showCircles": True}],
            "addTooltip": True, "addLegend": True, "legendPosition": "right",
            "times": [], "addTimeMarker": False, "labels": {"show": False},
        },
        "aggs": [
            {"id": "1", "enabled": True, "type": "count",
             "schema": "metric", "params": {}},
            {"id": "2", "enabled": True, "type": "date_histogram",
             "schema": "segment", "params": {
                 "field": time_field,
                 "useNormalizedEsInterval": True,
                 "interval": "auto",
                 "min_doc_count": 1,
                 "extended_bounds": {},
             }},
        ],
    }
    return {
        "type": "visualization", "id": obj_id,
        "attributes": {
            "title": title,
            "visState": json.dumps(vis_state),
            "uiStateJSON": "{}",
            "kibanaSavedObjectMeta": {"searchSourceJSON": _ss(index_id)},
        },
        "references": [{"name": "kibanaSavedObjectMeta.searchSourceJSON.index",
                        "type": "index-pattern", "id": index_id}],
    }


def _pie(obj_id: str, title: str, index_id: str, field: str) -> dict:
    vis_state = {
        "title": title, "type": "pie",
        "params": {
            "type": "pie", "addTooltip": True, "addLegend": True,
            "legendPosition": "right", "isDonut": True,
            "labels": {"show": False, "values": True,
                       "last_level": True, "truncate": 100},
        },
        "aggs": [
            {"id": "1", "enabled": True, "type": "count",
             "schema": "metric", "params": {}},
            {"id": "2", "enabled": True, "type": "terms",
             "schema": "segment", "params": {
                 "field": field, "orderBy": "1", "order": "desc",
                 "size": 10, "otherBucket": False, "missingBucket": False,
             }},
        ],
    }
    return {
        "type": "visualization", "id": obj_id,
        "attributes": {
            "title": title,
            "visState": json.dumps(vis_state),
            "uiStateJSON": "{}",
            "kibanaSavedObjectMeta": {"searchSourceJSON": _ss(index_id)},
        },
        "references": [{"name": "kibanaSavedObjectMeta.searchSourceJSON.index",
                        "type": "index-pattern", "id": index_id}],
    }


def _dashboard(obj_id: str, title: str, panels: list) -> dict:
    panels_json = []
    refs = []
    for i, (viz_id, x, y, w, h) in enumerate(panels, 1):
        key = str(i)
        panels_json.append({
            "panelIndex": key,
            "gridData": {"x": x, "y": y, "w": w, "h": h, "i": key},
            "version": "3.6.0",
            "type": "visualization",
            "id": viz_id,
            "embeddableConfig": {},
        })
        refs.append({"name": f"{key}:panel_{key}",
                     "type": "visualization", "id": viz_id})
    return {
        "type": "dashboard", "id": obj_id,
        "attributes": {
            "title": title,
            "hits": 0,
            "description": "",
            "panelsJSON": json.dumps(panels_json),
            "optionsJSON": json.dumps({
                "useMargins": True, "syncColors": False, "hidePanelTitles": False,
            }),
            "version": 1,
            "timeRestore": False,
            "kibanaSavedObjectMeta": {"searchSourceJSON": json.dumps({
                "query": {"language": "kuery", "query": ""}, "filter": [],
            })},
        },
        "references": refs,
    }


# ── Object catalogue ──────────────────────────────────────────────────────────

def build_objects() -> list:
    objs = []

    objs += [
        {"type": "index-pattern", "id": "ip-evidence",
         "attributes": {"title": "evidence-*", "timeFieldName": "collected_at"},
         "references": []},
        {"type": "index-pattern", "id": "ip-audit-logs",
         "attributes": {"title": "audit-logs-*", "timeFieldName": "timestamp"},
         "references": []},
        {"type": "index-pattern", "id": "ip-connector-runs",
         "attributes": {"title": "connector-runs-*", "timeFieldName": "started_at"},
         "references": []},
    ]

    objs += [
        _metric("viz-ev-count",      "Evidence — Total Count",        "ip-evidence"),
        _timeline("viz-ev-time",     "Evidence — Over Time",          "ip-evidence", "collected_at"),
        _pie("viz-ev-connector",     "Evidence — By Connector",       "ip-evidence", "connector_id.keyword"),
        _pie("viz-ev-control",       "Evidence — By Control Group",   "ip-evidence", "control_ids.keyword"),
    ]

    objs += [
        _metric("viz-al-count",      "Audit Logs — Total Events",     "ip-audit-logs"),
        _timeline("viz-al-time",     "Audit Logs — Over Time",        "ip-audit-logs", "timestamp"),
        _pie("viz-al-user",          "Audit Logs — Top Users",        "ip-audit-logs", "user_email.keyword"),
        _pie("viz-al-action",        "Audit Logs — By Action",        "ip-audit-logs", "action.keyword"),
    ]

    objs += [
        _metric("viz-cr-count",      "Connector Runs — Total",        "ip-connector-runs"),
        _timeline("viz-cr-time",     "Connector Runs — Over Time",    "ip-connector-runs", "started_at"),
        _pie("viz-cr-status",        "Connector Runs — By Status",    "ip-connector-runs", "status.keyword"),
        _pie("viz-cr-connector",     "Connector Runs — By Connector", "ip-connector-runs", "connector_name.keyword"),
    ]

    objs.append(_dashboard("dash-evidence", "ISMS CORE — Evidence Overview", [
        ("viz-ev-count",      0,  0, 12, 5),
        ("viz-ev-time",      12,  0, 36, 5),
        ("viz-ev-connector",  0,  5, 24, 9),
        ("viz-ev-control",   24,  5, 24, 9),
    ]))
    objs.append(_dashboard("dash-audit", "ISMS CORE — Audit Logs", [
        ("viz-al-count",      0,  0, 12, 5),
        ("viz-al-time",      12,  0, 36, 5),
        ("viz-al-user",       0,  5, 24, 9),
        ("viz-al-action",    24,  5, 24, 9),
    ]))
    objs.append(_dashboard("dash-connectors", "ISMS CORE — Connector Health", [
        ("viz-cr-count",      0,  0, 12, 5),
        ("viz-cr-time",      12,  0, 36, 5),
        ("viz-cr-status",     0,  5, 24, 9),
        ("viz-cr-connector", 24,  5, 24, 9),
    ]))

    return objs


# ── Import via multipart ──────────────────────────────────────────────────────

def import_objects(objects: list) -> dict:
    ndjson = "\n".join(json.dumps(o) for o in objects).encode()
    boundary = "----OSDSetupBoundary7x4kTrZu"
    body = (
        f"--{boundary}\r\n"
        f'Content-Disposition: form-data; name="file"; filename="setup.ndjson"\r\n'
        f"Content-Type: application/ndjson\r\n\r\n"
    ).encode() + ndjson + f"\r\n--{boundary}--\r\n".encode()

    return _request(
        "POST",
        "/api/saved_objects/_import?overwrite=true",
        data=body,
        content_type=f"multipart/form-data; boundary={boundary}",
    )


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    # Step 1: seed OpenSearch indices so OSD can discover field mappings
    seed_opensearch_indices()

    # Step 2: wait for OSD, then import saved objects
    wait_for_dashboards()

    print("\nImporting index patterns, visualizations, and dashboards...", flush=True)
    objects = build_objects()
    result = import_objects(objects)

    success = result.get("successCount", 0)
    errors  = result.get("errors", [])
    print(f"  objects imported: {success}", flush=True)
    if errors:
        for e in errors[:10]:
            print(f"  WARNING: {e}", flush=True)

    print("\nDashboards setup complete.", flush=True)


if __name__ == "__main__":
    main()
