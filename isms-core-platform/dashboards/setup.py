#!/usr/bin/env python3
"""
OpenSearch Dashboards — bootstrap index patterns + sample dashboards.
Idempotent: uses overwrite=true on import.

Startup sequence:
  1. Seed OpenSearch indices with field mappings
  2. Read those mappings back and embed them in index-pattern saved objects
  3. Import everything (index patterns + visualizations + dashboards) in one call

Embedding fields directly in the saved object works on every OSD version.
The OSD Index Patterns API and /fields/refresh endpoint are Kibana-era APIs
that do not exist in OpenSearch Dashboards.
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
    # nvd-cve is created by the feeds container; adding here so setup can
    # seed field mappings for the index pattern even on a fresh deploy.
    # PUT is skipped if the index already exists (HEAD check).
    "nvd-cve": {
        "mappings": {
            "properties": {
                "cve_id":          {"type": "keyword"},
                "title":           {"type": "text"},
                "description":     {"type": "text"},
                "published":       {"type": "date"},
                "last_modified":   {"type": "date"},
                "severity":        {"type": "keyword"},
                "cvss_base_score": {"type": "float"},
                "cvss_vector":     {"type": "keyword"},
                "cpe_affected":    {"type": "keyword"},
                "in_kev":          {"type": "boolean"},
                "in_euvd":         {"type": "boolean"},
                "euvd_id":         {"type": "keyword"},
                "epss_score":      {"type": "float"},
                "references":      {"type": "text"},
                "indexed_at":      {"type": "date"},
            }
        }
    },
    "cisa-kev": {
        "mappings": {
            "properties": {
                "cve_id":             {"type": "keyword"},
                "vendor_project":     {"type": "keyword"},
                "product":            {"type": "keyword"},
                "vulnerability_name": {"type": "text", "fields": {"keyword": {"type": "keyword", "ignore_above": 512}}},
                "date_added":         {"type": "date", "format": "yyyy-MM-dd||strict_date_optional_time"},
                "short_description":  {"type": "text"},
                "required_action":    {"type": "text"},
                "due_date":           {"type": "date", "format": "yyyy-MM-dd||strict_date_optional_time"},
                "known_ransomware":   {"type": "boolean"},
                "notes":              {"type": "text"},
                "indexed_at":         {"type": "date"},
            }
        }
    },
    "evidence-000001": {
        "aliases": {"evidence": {"is_write_index": True}},
        "settings": {
            "index.plugins.index_state_management.rollover_alias": "evidence"
        },
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
        "aliases": {"audit-logs": {"is_write_index": True}},
        "settings": {
            "index.plugins.index_state_management.rollover_alias": "audit-logs"
        },
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
        "aliases": {"connector-runs": {"is_write_index": True}},
        "settings": {
            "index.plugins.index_state_management.rollover_alias": "connector-runs"
        },
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

# Maps ES type → (OSD type, searchable, aggregatable, readFromDocValues)
_TYPE_MAP = {
    "date":    ("date",    True,  True,  True),
    "keyword": ("string",  True,  True,  True),
    "text":    ("string",  True,  False, False),
    "integer": ("number",  True,  True,  True),
    "long":    ("number",  True,  True,  True),
    "float":   ("number",  True,  True,  True),
    "double":  ("number",  True,  True,  True),
    "boolean": ("boolean", True,  True,  True),
    "ip":      ("ip",      True,  True,  True),
}

_META_FIELDS = [
    {"name": "_id",     "type": "string",  "esTypes": ["_id"],     "searchable": True,  "aggregatable": False, "readFromDocValues": False},
    {"name": "_index",  "type": "string",  "esTypes": ["_index"],  "searchable": True,  "aggregatable": False, "readFromDocValues": False},
    {"name": "_score",  "type": "number",  "esTypes": [],          "searchable": False, "aggregatable": False, "readFromDocValues": False},
    {"name": "_source", "type": "_source", "esTypes": ["_source"], "searchable": False, "aggregatable": False, "readFromDocValues": False},
    {"name": "_type",   "type": "string",  "esTypes": ["_type"],   "searchable": True,  "aggregatable": True,  "readFromDocValues": False},
]


def _os_request(method: str, path: str, body: dict = None):
    url = f"{OPENSEARCH_URL}{path}"
    data = json.dumps(body).encode() if body else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            raw = resp.read()
            return json.loads(raw) if raw else {}
    except urllib.error.HTTPError as exc:
        return {"_status": exc.code, "_body": exc.read().decode(errors="replace")}


def seed_opensearch_indices():
    print("Seeding OpenSearch indices with field mappings...", flush=True)
    for name, body in INDICES.items():
        check = _os_request("HEAD", f"/{name}")
        if isinstance(check, dict) and check.get("_status") == 404:
            result = _os_request("PUT", f"/{name}", body)
            if result.get("acknowledged"):
                print(f"  created: {name}", flush=True)
            else:
                print(f"  WARNING creating {name}: {result}", flush=True)
        else:
            print(f"  exists:  {name}", flush=True)


def get_osd_fields(alias_name: str) -> str:
    """Read the OpenSearch mapping for an alias and return OSD-format fields JSON.

    Embedding this in the index-pattern saved object means OSD knows every
    field immediately — no post-import refresh call needed, no version-specific
    API dependency.
    """
    result = _os_request("GET", f"/{alias_name}/_mapping")
    props = {}
    for idx_data in result.values():
        props = idx_data.get("mappings", {}).get("properties", {})
        break

    fields = list(_META_FIELDS)
    for field_name, field_def in props.items():
        es_type = field_def.get("type", "keyword")
        osd_type, searchable, aggregatable, rfdv = _TYPE_MAP.get(
            es_type, ("string", True, True, True)
        )
        fields.append({
            "name": field_name,
            "type": osd_type,
            "esTypes": [es_type],
            "searchable": searchable,
            "aggregatable": aggregatable,
            "readFromDocValues": rfdv,
            "count": 0,
            "scripted": False,
            "indexed": True,
        })
        # Add .keyword subfield for text fields that have one
        for sub_name, sub_def in field_def.get("fields", {}).items():
            sub_es = sub_def.get("type", "keyword")
            sub_osd, sub_s, sub_a, sub_rfdv = _TYPE_MAP.get(
                sub_es, ("string", True, True, True)
            )
            fields.append({
                "name": f"{field_name}.{sub_name}",
                "type": sub_osd,
                "esTypes": [sub_es],
                "searchable": sub_s,
                "aggregatable": sub_a,
                "readFromDocValues": sub_rfdv,
                "count": 0,
                "scripted": False,
                "indexed": True,
                "subType": {"multi": {"parent": field_name}},
            })

    return json.dumps(fields)


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


def set_dark_mode():
    # theme:darkMode cannot be set via env var or opensearch_dashboards.yml —
    # it is a runtime UI setting that must be pushed via the settings API.
    try:
        _request(
            "POST",
            "/api/opensearch-dashboards/settings",
            json.dumps({"changes": {"theme:darkMode": True, "theme:version": "v7"}}).encode(),
        )
        print("Dark mode enabled (v7 theme).", flush=True)
    except Exception as exc:
        print(f"WARNING: could not set dark mode: {exc}", flush=True)


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


def _kql_metric(obj_id: str, title: str, index_id: str, kql: str = "") -> dict:
    """Metric count visualization with an optional KQL filter."""
    vis_state = {
        "title": title, "type": "metric",
        "params": {
            "addTooltip": True, "addLegend": False, "type": "metric",
            "metric": {
                "percentageMode": False, "useRanges": False,
                "colorSchema": "Green to Red", "metricColorMode": "None",
                "colorsRange": [{"from": 0, "to": 10000000}],
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
            "kibanaSavedObjectMeta": {"searchSourceJSON": json.dumps({
                "index": index_id,
                "query": {"query": kql, "language": "kuery"},
                "filter": [],
            })},
        },
        "references": [{"name": "kibanaSavedObjectMeta.searchSourceJSON.index",
                        "type": "index-pattern", "id": index_id}],
    }


def _count_table(obj_id: str, title: str, index_id: str,
                 bucket_field: str, size: int = 50) -> dict:
    """Data table: top N terms by count descending."""
    vis_state = {
        "title": title, "type": "table",
        "params": {
            "perPage": 25, "showPartialRows": False, "showMetricsAtAllLevels": False,
            "sort": {"columnIndex": None, "direction": None},
            "showTotal": False, "totalFunc": "sum", "percentageCol": "",
        },
        "aggs": [
            {"id": "1", "enabled": True, "type": "count", "schema": "metric", "params": {}},
            {"id": "2", "enabled": True, "type": "terms", "schema": "bucket",
             "params": {
                 "field": bucket_field, "orderBy": "1", "order": "desc",
                 "size": size, "otherBucket": False, "missingBucket": False,
                 "customLabel": bucket_field.replace("_", " ").replace(".", " ").title(),
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


def _top_table(obj_id: str, title: str, index_id: str,
               bucket_field: str, metric_field: str, size: int = 100) -> dict:
    """Data table: top N terms by max(metric_field) descending. metric_field must be numeric."""
    vis_state = {
        "title": title, "type": "table",
        "params": {
            "perPage": 25, "showPartialRows": False, "showMetricsAtAllLevels": False,
            "sort": {"columnIndex": None, "direction": None},
            "showTotal": False, "totalFunc": "sum", "percentageCol": "",
        },
        "aggs": [
            {"id": "1", "enabled": True, "type": "max", "schema": "metric",
             "params": {"field": metric_field, "customLabel": metric_field.replace("_", " ").title()}},
            {"id": "2", "enabled": True, "type": "terms", "schema": "bucket",
             "params": {
                 "field": bucket_field, "orderBy": "1", "order": "desc",
                 "size": size, "otherBucket": False, "missingBucket": False,
                 "customLabel": bucket_field.replace("_", " ").replace(".", " ").title(),
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

def build_objects(fields_by_id: dict) -> list:
    """Build all saved objects. Index patterns include pre-populated field lists
    read directly from OpenSearch mappings — no post-import refresh needed."""
    objs = []

    objs += [
        {"type": "index-pattern", "id": "ip-evidence",
         "attributes": {
             "title": "evidence-*",
             "timeFieldName": "collected_at",
             "fields": fields_by_id.get("ip-evidence", "[]"),
         },
         "references": []},
        {"type": "index-pattern", "id": "ip-audit-logs",
         "attributes": {
             "title": "audit-logs-*",
             "timeFieldName": "timestamp",
             "fields": fields_by_id.get("ip-audit-logs", "[]"),
         },
         "references": []},
        {"type": "index-pattern", "id": "ip-connector-runs",
         "attributes": {
             "title": "connector-runs-*",
             "timeFieldName": "started_at",
             "fields": fields_by_id.get("ip-connector-runs", "[]"),
         },
         "references": []},
        {"type": "index-pattern", "id": "ip-nvd-cve",
         "attributes": {
             "title": "nvd-cve",
             "timeFieldName": "published",
             "fields": fields_by_id.get("ip-nvd-cve", "[]"),
         },
         "references": []},
        {"type": "index-pattern", "id": "ip-cisa-kev",
         "attributes": {
             "title": "cisa-kev",
             "timeFieldName": "date_added",
             "fields": fields_by_id.get("ip-cisa-kev", "[]"),
         },
         "references": []},
    ]

    objs += [
        _metric("viz-ev-count",      "Evidence — Total Count",        "ip-evidence"),
        _timeline("viz-ev-time",     "Evidence — Over Time",          "ip-evidence", "collected_at"),
        _pie("viz-ev-connector",     "Evidence — By Connector",       "ip-evidence", "connector_id"),
        _pie("viz-ev-control",       "Evidence — By Control Group",   "ip-evidence", "control_ids"),
    ]

    objs += [
        _metric("viz-al-count",      "Audit Logs — Total Events",     "ip-audit-logs"),
        _timeline("viz-al-time",     "Audit Logs — Over Time",        "ip-audit-logs", "timestamp"),
        _pie("viz-al-user",          "Audit Logs — Top Users",        "ip-audit-logs", "user_email"),
        _pie("viz-al-action",        "Audit Logs — By Action",        "ip-audit-logs", "action"),
    ]

    objs += [
        _metric("viz-cr-count",      "Connector Runs — Total",        "ip-connector-runs"),
        _timeline("viz-cr-time",     "Connector Runs — Over Time",    "ip-connector-runs", "started_at"),
        _pie("viz-cr-status",        "Connector Runs — By Status",    "ip-connector-runs", "status"),
        _pie("viz-cr-connector",     "Connector Runs — By Connector", "ip-connector-runs", "connector_name"),
    ]

    # EPSS Risk Analytics
    objs += [
        _kql_metric("viz-epss-total", "EPSS — CVEs with Score",  "ip-nvd-cve", "epss_score: *"),
        _kql_metric("viz-epss-10p",   "EPSS — Score ≥ 10%",      "ip-nvd-cve", "epss_score >= 0.1"),
        _kql_metric("viz-epss-20p",   "EPSS — Score ≥ 20%",      "ip-nvd-cve", "epss_score >= 0.2"),
        _top_table("viz-epss-top",    "EPSS — Top 100 by Score", "ip-nvd-cve", "cve_id", "epss_score", 100),
    ]

    # CISA KEV Tracker
    objs += [
        _metric("viz-kev-total",       "KEV — Total Entries",          "ip-cisa-kev"),
        _timeline("viz-kev-time",      "KEV — Added Over Time",        "ip-cisa-kev", "date_added"),
        _pie("viz-kev-vendors",        "KEV — Top Vendors",            "ip-cisa-kev", "vendor_project"),
        _pie("viz-kev-products",       "KEV — Top Products",           "ip-cisa-kev", "product"),
        _pie("viz-kev-ransomware",     "KEV — Ransomware Association", "ip-cisa-kev", "known_ransomware"),
        _count_table("viz-kev-table",   "KEV — CVEs by Vendor",         "ip-cisa-kev", "vendor_project", 50),
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
    objs.append(_dashboard("dash-epss", "ISMS CORE — EPSS Risk Analytics", [
        ("viz-epss-total",  0,  0, 16, 5),
        ("viz-epss-10p",   16,  0, 16, 5),
        ("viz-epss-20p",   32,  0, 16, 5),
        ("viz-epss-top",    0,  5, 48, 15),
    ]))
    objs.append(_dashboard("dash-kev", "ISMS CORE — CISA KEV Tracker", [
        ("viz-kev-total",      0,  0, 12, 5),
        ("viz-kev-time",      12,  0, 36, 5),
        ("viz-kev-vendors",    0,  5, 16, 9),
        ("viz-kev-products",  16,  5, 16, 9),
        ("viz-kev-ransomware",32,  5, 16, 9),
        ("viz-kev-table",      0, 14, 48, 12),
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
    # Step 1: seed OpenSearch indices
    seed_opensearch_indices()

    # Step 2: read field mappings from OpenSearch to embed in index patterns
    print("\nReading field mappings from OpenSearch...", flush=True)
    fields_by_id = {
        "ip-evidence":       get_osd_fields("evidence"),
        "ip-audit-logs":     get_osd_fields("audit-logs"),
        "ip-connector-runs": get_osd_fields("connector-runs"),
        "ip-nvd-cve":        get_osd_fields("nvd-cve"),
        "ip-cisa-kev":       get_osd_fields("cisa-kev"),
    }
    for pid, fields_json in fields_by_id.items():
        count = len(json.loads(fields_json))
        print(f"  {pid}: {count} fields", flush=True)

    # Step 3: wait for OSD, apply dark mode, then import everything in one call
    wait_for_dashboards()
    set_dark_mode()

    print("\nImporting index patterns, visualizations, and dashboards...", flush=True)
    objects = build_objects(fields_by_id)
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
