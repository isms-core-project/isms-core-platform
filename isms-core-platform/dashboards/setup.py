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
                "edb_id":          {"type": "integer"},
                "edb_verified":    {"type": "boolean"},
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
    # ── Threat Intelligence indices (Phase 40e) ───────────────────────────────
    "ti-misp-circl": {"mappings": {"properties": {
        "ioc_type":     {"type": "keyword"},
        "value":        {"type": "keyword"},
        "source":       {"type": "keyword"},
        "confidence":   {"type": "integer"},
        "first_seen":   {"type": "date"},
        "last_seen":    {"type": "date"},
        "family_slugs": {"type": "keyword"},
        "actor_slugs":  {"type": "keyword"},
        "mitre_tids":   {"type": "keyword"},
        "tags":         {"type": "keyword"},
        "indexed_at":   {"type": "date"},
    }}},
    "ti-misp-botvrij": {"mappings": {"properties": {
        "ioc_type":     {"type": "keyword"},
        "value":        {"type": "keyword"},
        "source":       {"type": "keyword"},
        "confidence":   {"type": "integer"},
        "first_seen":   {"type": "date"},
        "last_seen":    {"type": "date"},
        "family_slugs": {"type": "keyword"},
        "actor_slugs":  {"type": "keyword"},
        "mitre_tids":   {"type": "keyword"},
        "tags":         {"type": "keyword"},
        "indexed_at":   {"type": "date"},
    }}},
    "ti-abuseipdb-blacklist": {"mappings": {"properties": {
        "ip":               {"type": "ip"},
        "abuse_score":      {"type": "integer"},
        "country_code":     {"type": "keyword"},
        "isp":              {"type": "keyword"},
        "usage_type":       {"type": "keyword"},
        "categories":       {"type": "integer"},
        "total_reports":    {"type": "integer"},
        "last_reported_at": {"type": "date"},
        "indexed_at":       {"type": "date"},
        # MaxMind GeoLite2 enrichment (free tier: country, city, ASN only)
        "geo_country":   {"type": "keyword"},
        "geo_city":      {"type": "keyword"},
        "geo_lat":       {"type": "float"},
        "geo_lon":       {"type": "float"},
        "geo_location":  {"type": "geo_point"},
        "geo_asn":       {"type": "integer"},
        "geo_org":       {"type": "keyword"},
        # IPInfo privacy enrichment
        "privacy_label":      {"type": "keyword"},
        "privacy_is_vpn":     {"type": "boolean"},
        "privacy_is_proxy":   {"type": "boolean"},
        "privacy_is_tor":     {"type": "boolean"},
        "privacy_is_hosting": {"type": "boolean"},
    }}},
    "ti-malpedia-families": {"mappings": {"properties": {
        "slug":        {"type": "keyword"},
        "name":        {"type": "text", "fields": {"keyword": {"type": "keyword", "ignore_above": 512}}},
        "aliases":     {"type": "keyword"},
        "description": {"type": "text"},
        "actor_slugs": {"type": "keyword"},
        "mitre_tids":  {"type": "keyword"},
        "updated_at":  {"type": "date"},
    }}},
    "ti-malpedia-actors": {"mappings": {"properties": {
        "slug":        {"type": "keyword"},
        "name":        {"type": "text", "fields": {"keyword": {"type": "keyword", "ignore_above": 512}}},
        "country":     {"type": "keyword"},
        "motivation":  {"type": "keyword"},
        "actor_type":  {"type": "keyword"},
        "description": {"type": "text"},
        "updated_at":  {"type": "date"},
    }}},
    # ── Phase 41 — new TI feed indices ───────────────────────────────────────
    "ti-malpedia-tools": {"mappings": {"properties": {
        "slug":       {"type": "keyword"},
        "name":       {"type": "text", "fields": {"keyword": {"type": "keyword", "ignore_above": 256}}},
        "aliases":    {"type": "keyword"},
        "mitre_tids": {"type": "keyword"},
        "updated_at": {"type": "date"},
    }}},
    "ti-urlhaus": {"mappings": {"properties": {
        "url":        {"type": "keyword"},
        "url_status": {"type": "keyword"},
        "threat":     {"type": "keyword"},
        "tags":       {"type": "keyword"},
        "date_added": {"type": "date"},
        "indexed_at": {"type": "date"},
    }}},
    "ti-threatfox": {"mappings": {"properties": {
        "ioc":         {"type": "keyword"},
        "ioc_type":    {"type": "keyword"},
        "threat_type": {"type": "keyword"},
        "malware":     {"type": "keyword"},
        "confidence":  {"type": "integer"},
        "tags":        {"type": "keyword"},
        "first_seen":  {"type": "date"},
        "indexed_at":  {"type": "date"},
    }}},
    "ti-sslbl": {"mappings": {"properties": {
        "sha1":       {"type": "keyword"},
        "reason":     {"type": "keyword"},
        "listed_at":  {"type": "date"},
        "indexed_at": {"type": "date"},
    }}},
    "ti-feodotracker": {"mappings": {"properties": {
        "ip":          {"type": "ip"},
        "port":        {"type": "integer"},
        "c2_status":   {"type": "keyword"},
        "malware":     {"type": "keyword"},
        "first_seen":  {"type": "date"},
        "last_online": {"type": "date"},
        "indexed_at":  {"type": "date"},
    }}},
    "ti-red-flag-domains": {"mappings": {"properties": {
        "domain":     {"type": "keyword"},
        "date_added": {"type": "date"},
        "indexed_at": {"type": "date"},
    }}},
    "ti-stopforumspam": {"mappings": {"properties": {
        "ip":         {"type": "ip"},
        "indexed_at": {"type": "date"},
    }}},
    "ti-malwarebazaar": {"mappings": {"properties": {
        "sha256":     {"type": "keyword"},
        "sha1":       {"type": "keyword"},
        "md5":        {"type": "keyword"},
        "file_name":  {"type": "keyword"},
        "file_type":  {"type": "keyword"},
        "signature":  {"type": "keyword"},
        "tags":       {"type": "keyword"},
        "first_seen": {"type": "date"},
        "indexed_at": {"type": "date"},
    }}},
    "ti-alienvault": {"mappings": {"properties": {
        "ioc":        {"type": "keyword"},
        "ioc_type":   {"type": "keyword"},
        "pulse_name": {"type": "text", "fields": {"keyword": {"type": "keyword"}}},
        "adversary":  {"type": "keyword"},
        "industries": {"type": "keyword"},
        "countries":  {"type": "keyword"},
        "malware":    {"type": "keyword"},
        "mitre_tids": {"type": "keyword"},
        "tlp":        {"type": "keyword"},
        "first_seen": {"type": "date"},
        "indexed_at": {"type": "date"},
    }}},
    # ── Exploit-DB (Phase 47) ─────────────────────────────────────────────────
    "exploitdb": {"mappings": {"properties": {
        "edb_id":         {"type": "integer"},
        "description":    {"type": "text", "fields": {"keyword": {"type": "keyword", "ignore_above": 512}}},
        "type":           {"type": "keyword"},
        "platform":       {"type": "keyword"},
        "verified":       {"type": "boolean"},
        "has_msf":        {"type": "boolean"},
        "date_published": {"type": "date", "format": "yyyy-MM-dd||strict_date_optional_time"},
        "author":         {"type": "keyword"},
        "tags":           {"type": "keyword"},
        "cve_refs":       {"type": "keyword"},
        "file_path":      {"type": "keyword"},
        "indexed_at":     {"type": "date"},
    }}},
    # ── Per-source evidence indices (Phase 39a) ───────────────────────────────
    # Common base fields shared by all per-source indices
    "evidence-entra-id": {"mappings": {"properties": {
        "org_id":          {"type": "keyword"},
        "connector_id":    {"type": "keyword"},
        "source_system":   {"type": "keyword"},
        "evidence_type":   {"type": "keyword"},
        "title":           {"type": "text"},
        "control_ids":     {"type": "keyword"},
        "collected_at":    {"type": "date"},
        "status":          {"type": "keyword"},
        # Entra ID promoted fields
        "user_principal":  {"type": "keyword"},
        "display_name":    {"type": "keyword"},
        "department":      {"type": "keyword"},
        "job_title":       {"type": "keyword"},
        "account_enabled": {"type": "boolean"},
        "is_compliant":    {"type": "boolean"},
        "is_managed":      {"type": "boolean"},
        "device_ownership":{"type": "keyword"},
        "os_name":         {"type": "keyword"},
        "email":           {"type": "keyword"},
        "group_names":     {"type": "keyword"},
    }}},
    "evidence-o365": {"mappings": {"properties": {
        "org_id":          {"type": "keyword"},
        "connector_id":    {"type": "keyword"},
        "source_system":   {"type": "keyword"},
        "evidence_type":   {"type": "keyword"},
        "title":           {"type": "text"},
        "control_ids":     {"type": "keyword"},
        "collected_at":    {"type": "date"},
        "status":          {"type": "keyword"},
        # O365 promoted fields
        "operation":       {"type": "keyword"},
        "workload":        {"type": "keyword"},
        "object_id":       {"type": "keyword"},
        "user_id":         {"type": "keyword"},
        "user_type":       {"type": "keyword"},
        "external_access": {"type": "boolean"},
        "client_ip":       {"type": "ip"},
        "result_status":   {"type": "keyword"},
    }}},
    "evidence-defender": {"mappings": {"properties": {
        "org_id":          {"type": "keyword"},
        "connector_id":    {"type": "keyword"},
        "source_system":   {"type": "keyword"},
        "evidence_type":   {"type": "keyword"},
        "title":           {"type": "text"},
        "control_ids":     {"type": "keyword"},
        "collected_at":    {"type": "date"},
        "status":          {"type": "keyword"},
        # Defender promoted fields
        "alert_severity":  {"type": "keyword"},
        "alert_status":    {"type": "keyword"},
        "alert_category":  {"type": "keyword"},
        "alert_id":        {"type": "keyword"},
        "machine_id":      {"type": "keyword"},
        "os_platform":     {"type": "keyword"},
        "cve_id":          {"type": "keyword"},
    }}},
    "evidence-sentinel": {"mappings": {"properties": {
        "org_id":          {"type": "keyword"},
        "connector_id":    {"type": "keyword"},
        "source_system":   {"type": "keyword"},
        "evidence_type":   {"type": "keyword"},
        "title":           {"type": "text"},
        "control_ids":     {"type": "keyword"},
        "collected_at":    {"type": "date"},
        "status":          {"type": "keyword"},
        # Sentinel promoted fields
        "alert_severity":  {"type": "keyword"},
        "incident_status": {"type": "keyword"},
        "incident_number": {"type": "integer"},
        "incident_title":  {"type": "text"},
        "tactics":         {"type": "keyword"},
    }}},
    "evidence-intune": {"mappings": {"properties": {
        "org_id":          {"type": "keyword"},
        "connector_id":    {"type": "keyword"},
        "source_system":   {"type": "keyword"},
        "evidence_type":   {"type": "keyword"},
        "title":           {"type": "text"},
        "control_ids":     {"type": "keyword"},
        "collected_at":    {"type": "date"},
        "status":          {"type": "keyword"},
        # Intune promoted fields
        "compliance_state":{"type": "keyword"},
        "device_name":     {"type": "keyword"},
        "os_version":      {"type": "keyword"},
        "device_id":       {"type": "keyword"},
        "user_principal":  {"type": "keyword"},
        "manufacturer":    {"type": "keyword"},
        "model":           {"type": "keyword"},
    }}},
    "evidence-crowdstrike": {"mappings": {"properties": {
        "org_id":          {"type": "keyword"},
        "connector_id":    {"type": "keyword"},
        "source_system":   {"type": "keyword"},
        "evidence_type":   {"type": "keyword"},
        "title":           {"type": "text"},
        "control_ids":     {"type": "keyword"},
        "collected_at":    {"type": "date"},
        "status":          {"type": "keyword"},
        # CrowdStrike promoted fields
        "alert_severity":  {"type": "keyword"},
        "alert_status":    {"type": "keyword"},
        "machine_name":    {"type": "keyword"},
        "tactic":          {"type": "keyword"},
        "technique":       {"type": "keyword"},
        "event_type":      {"type": "keyword"},
        "host_groups":     {"type": "keyword"},
    }}},
    "evidence-sentinelone": {"mappings": {"properties": {
        "org_id":          {"type": "keyword"},
        "connector_id":    {"type": "keyword"},
        "source_system":   {"type": "keyword"},
        "evidence_type":   {"type": "keyword"},
        "title":           {"type": "text"},
        "control_ids":     {"type": "keyword"},
        "collected_at":    {"type": "date"},
        "status":          {"type": "keyword"},
        # SentinelOne promoted fields
        "alert_severity":  {"type": "keyword"},
        "machine_name":    {"type": "keyword"},
        "classification":  {"type": "keyword"},
        "technique":       {"type": "keyword"},
        "tactic":          {"type": "keyword"},
    }}},
    "evidence-tenable": {"mappings": {"properties": {
        "org_id":          {"type": "keyword"},
        "connector_id":    {"type": "keyword"},
        "source_system":   {"type": "keyword"},
        "evidence_type":   {"type": "keyword"},
        "title":           {"type": "text"},
        "control_ids":     {"type": "keyword"},
        "collected_at":    {"type": "date"},
        "status":          {"type": "keyword"},
        # Tenable promoted fields (sc + io share same index)
        "severity":        {"type": "keyword"},
        "cvss_score":      {"type": "float"},
        "plugin_name":     {"type": "text", "fields": {"keyword": {"type": "keyword", "ignore_above": 512}}},
        "plugin_id":       {"type": "keyword"},
        "asset_id":        {"type": "keyword"},
        "fqdn":            {"type": "keyword"},
        "cve_id":          {"type": "keyword"},
    }}},
    "evidence-qualys": {"mappings": {"properties": {
        "org_id":          {"type": "keyword"},
        "connector_id":    {"type": "keyword"},
        "source_system":   {"type": "keyword"},
        "evidence_type":   {"type": "keyword"},
        "title":           {"type": "text"},
        "control_ids":     {"type": "keyword"},
        "collected_at":    {"type": "date"},
        "status":          {"type": "keyword"},
        # Qualys promoted fields
        "severity":        {"type": "keyword"},
        "qds_score":       {"type": "float"},
        "plugin_name":     {"type": "text", "fields": {"keyword": {"type": "keyword", "ignore_above": 512}}},
        "plugin_id":       {"type": "keyword"},
        "fqdn":            {"type": "keyword"},
        "detection_type":  {"type": "keyword"},
        "cve_id":          {"type": "keyword"},
    }}},
    "evidence-openvas": {"mappings": {"properties": {
        "org_id": {"type": "keyword"}, "connector_id": {"type": "keyword"},
        "source_system": {"type": "keyword"}, "evidence_type": {"type": "keyword"},
        "title": {"type": "text"}, "control_ids": {"type": "keyword"},
        "collected_at": {"type": "date"}, "status": {"type": "keyword"},
        "severity": {"type": "keyword"}, "plugin_name": {"type": "text"},
        "plugin_id": {"type": "keyword"}, "fqdn": {"type": "keyword"},
        "port": {"type": "keyword"}, "threat_level": {"type": "keyword"},
        "cve_id": {"type": "keyword"},
    }}},
    "evidence-purview": {"mappings": {"properties": {
        "org_id": {"type": "keyword"}, "connector_id": {"type": "keyword"},
        "source_system": {"type": "keyword"}, "evidence_type": {"type": "keyword"},
        "title": {"type": "text"}, "control_ids": {"type": "keyword"},
        "collected_at": {"type": "date"}, "status": {"type": "keyword"},
        "activity_type": {"type": "keyword"}, "workload": {"type": "keyword"},
        "user_id": {"type": "keyword"}, "object_name": {"type": "keyword"},
        "sensitivity_label": {"type": "keyword"}, "policy_name": {"type": "keyword"},
        "action": {"type": "keyword"},
    }}},
    "evidence-fortigate": {"mappings": {"properties": {
        "org_id": {"type": "keyword"}, "connector_id": {"type": "keyword"},
        "source_system": {"type": "keyword"}, "evidence_type": {"type": "keyword"},
        "title": {"type": "text"}, "control_ids": {"type": "keyword"},
        "collected_at": {"type": "date"}, "status": {"type": "keyword"},
        "log_type": {"type": "keyword"}, "log_subtype": {"type": "keyword"},
        "action": {"type": "keyword"}, "src_ip": {"type": "ip"},
        "dst_ip": {"type": "ip"}, "dst_port": {"type": "integer"},
        "protocol": {"type": "keyword"}, "policy_name": {"type": "keyword"},
        "severity": {"type": "keyword"},
    }}},
    "evidence-panw": {"mappings": {"properties": {
        "org_id": {"type": "keyword"}, "connector_id": {"type": "keyword"},
        "source_system": {"type": "keyword"}, "evidence_type": {"type": "keyword"},
        "title": {"type": "text"}, "control_ids": {"type": "keyword"},
        "collected_at": {"type": "date"}, "status": {"type": "keyword"},
        "log_type": {"type": "keyword"}, "log_subtype": {"type": "keyword"},
        "action": {"type": "keyword"}, "src_ip": {"type": "ip"},
        "dst_ip": {"type": "ip"}, "dst_port": {"type": "integer"},
        "protocol": {"type": "keyword"}, "policy_name": {"type": "keyword"},
        "severity": {"type": "keyword"}, "threat_name": {"type": "keyword"},
    }}},
    "evidence-cisco": {"mappings": {"properties": {
        "org_id": {"type": "keyword"}, "connector_id": {"type": "keyword"},
        "source_system": {"type": "keyword"}, "evidence_type": {"type": "keyword"},
        "title": {"type": "text"}, "control_ids": {"type": "keyword"},
        "collected_at": {"type": "date"}, "status": {"type": "keyword"},
        "message_id": {"type": "keyword"}, "severity": {"type": "keyword"},
        "src_ip": {"type": "ip"}, "dst_ip": {"type": "ip"},
        "dst_port": {"type": "integer"}, "protocol": {"type": "keyword"},
        "user_id": {"type": "keyword"}, "action": {"type": "keyword"},
    }}},
    "evidence-zscaler": {"mappings": {"properties": {
        "org_id": {"type": "keyword"}, "connector_id": {"type": "keyword"},
        "source_system": {"type": "keyword"}, "evidence_type": {"type": "keyword"},
        "title": {"type": "text"}, "control_ids": {"type": "keyword"},
        "collected_at": {"type": "date"}, "status": {"type": "keyword"},
        "action": {"type": "keyword"}, "url_category": {"type": "keyword"},
        "url": {"type": "keyword"}, "src_ip": {"type": "ip"},
        "user_id": {"type": "keyword"}, "cloud_name": {"type": "keyword"},
        "policy_name": {"type": "keyword"}, "threat_name": {"type": "keyword"},
    }}},
    "evidence-identity": {"mappings": {"properties": {
        "org_id": {"type": "keyword"}, "connector_id": {"type": "keyword"},
        "source_system": {"type": "keyword"}, "evidence_type": {"type": "keyword"},
        "title": {"type": "text"}, "control_ids": {"type": "keyword"},
        "collected_at": {"type": "date"}, "status": {"type": "keyword"},
        "username": {"type": "keyword"}, "user_principal": {"type": "keyword"},
        "distinguished_name": {"type": "keyword"}, "department": {"type": "keyword"},
        "account_enabled": {"type": "boolean"}, "account_expires": {"type": "date"},
        "group_names": {"type": "keyword"}, "last_logon": {"type": "date"},
    }}},
    "evidence-prtg": {"mappings": {"properties": {
        "org_id": {"type": "keyword"}, "connector_id": {"type": "keyword"},
        "source_system": {"type": "keyword"}, "evidence_type": {"type": "keyword"},
        "title": {"type": "text"}, "control_ids": {"type": "keyword"},
        "collected_at": {"type": "date"}, "status": {"type": "keyword"},
        "sensor_name": {"type": "keyword"}, "device_name": {"type": "keyword"},
        "group_name": {"type": "keyword"}, "sensor_status": {"type": "keyword"},
        "message": {"type": "text"}, "priority": {"type": "keyword"},
        "last_value": {"type": "keyword"},
    }}},
    "evidence-zabbix": {"mappings": {"properties": {
        "org_id": {"type": "keyword"}, "connector_id": {"type": "keyword"},
        "source_system": {"type": "keyword"}, "evidence_type": {"type": "keyword"},
        "title": {"type": "text"}, "control_ids": {"type": "keyword"},
        "collected_at": {"type": "date"}, "status": {"type": "keyword"},
        "host_name": {"type": "keyword"}, "trigger_name": {"type": "keyword"},
        "severity": {"type": "keyword"}, "alert_status": {"type": "keyword"},
        "metric_value": {"type": "keyword"}, "metric_units": {"type": "keyword"},
        "item_key": {"type": "keyword"},
    }}},
    "evidence-glpi": {"mappings": {"properties": {
        "org_id": {"type": "keyword"}, "connector_id": {"type": "keyword"},
        "source_system": {"type": "keyword"}, "evidence_type": {"type": "keyword"},
        "title": {"type": "text"}, "control_ids": {"type": "keyword"},
        "collected_at": {"type": "date"}, "status": {"type": "keyword"},
        "asset_name": {"type": "keyword"}, "asset_type": {"type": "keyword"},
        "serial_number": {"type": "keyword"}, "asset_tag": {"type": "keyword"},
        "asset_status": {"type": "keyword"}, "location": {"type": "keyword"},
        "assigned_tech": {"type": "keyword"},
    }}},
    "evidence-netbox": {"mappings": {"properties": {
        "org_id": {"type": "keyword"}, "connector_id": {"type": "keyword"},
        "source_system": {"type": "keyword"}, "evidence_type": {"type": "keyword"},
        "title": {"type": "text"}, "control_ids": {"type": "keyword"},
        "collected_at": {"type": "date"}, "status": {"type": "keyword"},
        "asset_name": {"type": "keyword"}, "asset_type": {"type": "keyword"},
        "serial_number": {"type": "keyword"}, "asset_tag": {"type": "keyword"},
        "asset_status": {"type": "keyword"}, "site": {"type": "keyword"},
        "role": {"type": "keyword"}, "primary_ip": {"type": "keyword"},
    }}},
    "evidence-cyberark": {"mappings": {"properties": {
        "org_id": {"type": "keyword"}, "connector_id": {"type": "keyword"},
        "source_system": {"type": "keyword"}, "evidence_type": {"type": "keyword"},
        "title": {"type": "text"}, "control_ids": {"type": "keyword"},
        "collected_at": {"type": "date"}, "status": {"type": "keyword"},
        "account_name": {"type": "keyword"}, "safe_name": {"type": "keyword"},
        "username": {"type": "keyword"}, "address": {"type": "keyword"},
        "platform": {"type": "keyword"}, "action": {"type": "keyword"},
        "reason": {"type": "text"},
    }}},
    "evidence-aws-security-hub": {"mappings": {"properties": {
        "org_id": {"type": "keyword"}, "connector_id": {"type": "keyword"},
        "source_system": {"type": "keyword"}, "evidence_type": {"type": "keyword"},
        "title": {"type": "text"}, "control_ids": {"type": "keyword"},
        "collected_at": {"type": "date"}, "status": {"type": "keyword"},
        "severity": {"type": "keyword"}, "finding_title": {"type": "text"},
        "finding_type": {"type": "keyword"}, "product_name": {"type": "keyword"},
        "aws_account_id": {"type": "keyword"}, "aws_region": {"type": "keyword"},
        "record_state": {"type": "keyword"}, "workflow_status": {"type": "keyword"},
    }}},
    "evidence-azure-cspm": {"mappings": {"properties": {
        "org_id": {"type": "keyword"}, "connector_id": {"type": "keyword"},
        "source_system": {"type": "keyword"}, "evidence_type": {"type": "keyword"},
        "title": {"type": "text"}, "control_ids": {"type": "keyword"},
        "collected_at": {"type": "date"}, "status": {"type": "keyword"},
        "severity": {"type": "keyword"}, "finding_title": {"type": "text"},
        "resource_type": {"type": "keyword"}, "resource_name": {"type": "keyword"},
        "subscription_id": {"type": "keyword"}, "compliance_status": {"type": "keyword"},
        "policy_name": {"type": "keyword"},
    }}},
    "evidence-gcp-scc": {"mappings": {"properties": {
        "org_id": {"type": "keyword"}, "connector_id": {"type": "keyword"},
        "source_system": {"type": "keyword"}, "evidence_type": {"type": "keyword"},
        "title": {"type": "text"}, "control_ids": {"type": "keyword"},
        "collected_at": {"type": "date"}, "status": {"type": "keyword"},
        "severity": {"type": "keyword"}, "finding_title": {"type": "text"},
        "finding_type": {"type": "keyword"}, "resource_name": {"type": "keyword"},
        "gcp_project_id": {"type": "keyword"}, "finding_state": {"type": "keyword"},
        "finding_class": {"type": "keyword"},
    }}},
    "evidence-threat-intel": {"mappings": {"properties": {
        "org_id": {"type": "keyword"}, "connector_id": {"type": "keyword"},
        "source_system": {"type": "keyword"}, "evidence_type": {"type": "keyword"},
        "title": {"type": "text"}, "control_ids": {"type": "keyword"},
        "collected_at": {"type": "date"}, "status": {"type": "keyword"},
        "indicator_type": {"type": "keyword"}, "indicator_name": {"type": "keyword"},
        "confidence": {"type": "integer"}, "pattern": {"type": "keyword"},
        "labels": {"type": "keyword"}, "valid_from": {"type": "date"},
        "valid_until": {"type": "date"}, "tlp": {"type": "keyword"},
        "severity": {"type": "keyword"}, "category": {"type": "keyword"},
        "source": {"type": "keyword"}, "indicator": {"type": "keyword"},
        "action": {"type": "keyword"}, "host_name": {"type": "keyword"},
        "user_id": {"type": "keyword"},
    }}},
    # ── Phase 39b — 10 additional connectors ─────────────────────────────────
    "evidence-wazuh": {"mappings": {"properties": {
        "org_id": {"type": "keyword"}, "connector_id": {"type": "keyword"},
        "source_system": {"type": "keyword"}, "evidence_type": {"type": "keyword"},
        "title": {"type": "text"}, "control_ids": {"type": "keyword"},
        "collected_at": {"type": "date"}, "status": {"type": "keyword"},
        "agent_count": {"type": "integer"}, "active_agent_count": {"type": "integer"},
        "disconnected_agent_count": {"type": "integer"},
        "critical_alerts": {"type": "integer"}, "high_alerts": {"type": "integer"},
        "total_cves": {"type": "integer"}, "critical_cves": {"type": "integer"},
        "high_cves": {"type": "integer"},
    }}},
    "evidence-forti-analyzer": {"mappings": {"properties": {
        "org_id": {"type": "keyword"}, "connector_id": {"type": "keyword"},
        "source_system": {"type": "keyword"}, "evidence_type": {"type": "keyword"},
        "title": {"type": "text"}, "control_ids": {"type": "keyword"},
        "collected_at": {"type": "date"}, "status": {"type": "keyword"},
        "device_count": {"type": "integer"}, "connected_count": {"type": "integer"},
        "disconnected_count": {"type": "integer"}, "log_device_count": {"type": "integer"},
        "incident_count": {"type": "integer"}, "critical_incident_count": {"type": "integer"},
    }}},
    "evidence-forti-manager": {"mappings": {"properties": {
        "org_id": {"type": "keyword"}, "connector_id": {"type": "keyword"},
        "source_system": {"type": "keyword"}, "evidence_type": {"type": "keyword"},
        "title": {"type": "text"}, "control_ids": {"type": "keyword"},
        "collected_at": {"type": "date"}, "status": {"type": "keyword"},
        "device_count": {"type": "integer"}, "up_count": {"type": "integer"},
        "down_count": {"type": "integer"}, "policy_count": {"type": "integer"},
        "deployed_policy_count": {"type": "integer"}, "pending_policy_count": {"type": "integer"},
        "firmware_template_count": {"type": "integer"},
    }}},
    "evidence-graylog": {"mappings": {"properties": {
        "org_id": {"type": "keyword"}, "connector_id": {"type": "keyword"},
        "source_system": {"type": "keyword"}, "evidence_type": {"type": "keyword"},
        "title": {"type": "text"}, "control_ids": {"type": "keyword"},
        "collected_at": {"type": "date"}, "status": {"type": "keyword"},
        "stream_count": {"type": "integer"}, "enabled_stream_count": {"type": "integer"},
        "alert_count": {"type": "integer"}, "unresolved_alert_count": {"type": "integer"},
    }}},
    "evidence-hashicorp-vault": {"mappings": {"properties": {
        "org_id": {"type": "keyword"}, "connector_id": {"type": "keyword"},
        "source_system": {"type": "keyword"}, "evidence_type": {"type": "keyword"},
        "title": {"type": "text"}, "control_ids": {"type": "keyword"},
        "collected_at": {"type": "date"}, "status": {"type": "keyword"},
        "vault_version": {"type": "keyword"}, "is_sealed": {"type": "boolean"},
        "engine_count": {"type": "integer"}, "auth_method_count": {"type": "integer"},
        "audit_enabled": {"type": "boolean"}, "audit_device_count": {"type": "integer"},
    }}},
    "evidence-devolutions": {"mappings": {"properties": {
        "org_id": {"type": "keyword"}, "connector_id": {"type": "keyword"},
        "source_system": {"type": "keyword"}, "evidence_type": {"type": "keyword"},
        "title": {"type": "text"}, "control_ids": {"type": "keyword"},
        "collected_at": {"type": "date"}, "status": {"type": "keyword"},
        "connection_count": {"type": "integer"}, "privileged_count": {"type": "integer"},
        "user_count": {"type": "integer"}, "active_user_count": {"type": "integer"},
        "mfa_enabled_count": {"type": "integer"}, "admin_count": {"type": "integer"},
    }}},
    "evidence-github": {"mappings": {"properties": {
        "org_id": {"type": "keyword"}, "connector_id": {"type": "keyword"},
        "source_system": {"type": "keyword"}, "evidence_type": {"type": "keyword"},
        "title": {"type": "text"}, "control_ids": {"type": "keyword"},
        "collected_at": {"type": "date"}, "status": {"type": "keyword"},
        "org": {"type": "keyword"}, "repo_count": {"type": "integer"},
        "alert_count": {"type": "integer"}, "critical_high_count": {"type": "integer"},
    }}},
    "evidence-gitlab": {"mappings": {"properties": {
        "org_id": {"type": "keyword"}, "connector_id": {"type": "keyword"},
        "source_system": {"type": "keyword"}, "evidence_type": {"type": "keyword"},
        "title": {"type": "text"}, "control_ids": {"type": "keyword"},
        "collected_at": {"type": "date"}, "status": {"type": "keyword"},
        "group_id": {"type": "keyword"}, "project_count": {"type": "integer"},
        "finding_count": {"type": "integer"}, "critical_high_count": {"type": "integer"},
        "member_count": {"type": "integer"},
    }}},
    "evidence-jira": {"mappings": {"properties": {
        "org_id": {"type": "keyword"}, "connector_id": {"type": "keyword"},
        "source_system": {"type": "keyword"}, "evidence_type": {"type": "keyword"},
        "title": {"type": "text"}, "control_ids": {"type": "keyword"},
        "collected_at": {"type": "date"}, "status": {"type": "keyword"},
        "incident_count": {"type": "integer"}, "open_incident_count": {"type": "integer"},
        "high_priority_count": {"type": "integer"}, "change_count": {"type": "integer"},
        "open_change_count": {"type": "integer"},
    }}},
    "evidence-servicenow": {"mappings": {"properties": {
        "org_id": {"type": "keyword"}, "connector_id": {"type": "keyword"},
        "source_system": {"type": "keyword"}, "evidence_type": {"type": "keyword"},
        "title": {"type": "text"}, "control_ids": {"type": "keyword"},
        "collected_at": {"type": "date"}, "status": {"type": "keyword"},
        "incident_count": {"type": "integer"}, "open_incident_count": {"type": "integer"},
        "p1_p2_count": {"type": "integer"}, "change_count": {"type": "integer"},
        "open_change_count": {"type": "integer"}, "pending_approval_count": {"type": "integer"},
    }}},
    # ── Generic evidence index (unchanged) ────────────────────────────────────
    "evidence-000001": {
        "aliases": {"evidence": {"is_write_index": True}},
        "settings": {
            "index.plugins.index_state_management.rollover_alias": "evidence"
        },
        "mappings": {
            "properties": {
                "collected_at":    {"type": "date"},
                "connector_id":    {"type": "keyword"},
                "source_system":   {"type": "keyword"},
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
    "boolean":   ("boolean",   True,  True,  True),
    "ip":        ("ip",        True,  True,  True),
    "geo_point": ("geo_point", True,  True,  True),
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


def _geo_map(obj_id: str, title: str, index_id: str, geo_field: str = "geo_location") -> dict:
    """Coordinate map (tile_map) over a geo_point field."""
    vis_state = {
        "title": title, "type": "tile_map",
        "params": {
            "colorSchema": "Yellow to Red",
            "mapType": "Scaled Circle Markers",
            "isDesaturated": False,
            "addTooltip": True,
            "heatClusterSize": 1.5,
            "legendPosition": "bottomright",
            "mapZoom": 2,
            "mapCenter": [0, 0],
            "wms": {
                "enabled": False,
                "url": "",
                "options": {"format": "image/png", "transparent": True},
            },
        },
        "aggs": [
            {"id": "1", "enabled": True, "type": "count",
             "schema": "metric", "params": {}},
            {"id": "2", "enabled": True, "type": "geohash_grid",
             "schema": "segment", "params": {
                 "field": geo_field,
                 "autoPrecision": True,
                 "precision": 2,
                 "useGeocentroid": True,
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


def _score_histogram(obj_id: str, title: str, index_id: str, field: str, interval: float) -> dict:
    """Bar chart histogram on a numeric field (not date). Good for score distributions."""
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
                           "labels": {"show": True, "rotate": 0, "filter": False, "truncate": 100},
                           "title": {"text": "CVE Count"}}],
            "seriesParams": [{"show": True, "type": "histogram", "mode": "stacked",
                              "data": {"label": "Count", "id": "1"},
                              "valueAxis": "ValueAxis-1",
                              "drawLinesBetweenPoints": True,
                              "lineWidth": 2, "showCircles": True}],
            "addTooltip": True, "addLegend": False, "legendPosition": "right",
            "times": [], "addTimeMarker": False, "labels": {"show": False},
        },
        "aggs": [
            {"id": "1", "enabled": True, "type": "count", "schema": "metric", "params": {}},
            {"id": "2", "enabled": True, "type": "histogram", "schema": "segment",
             "params": {"field": field, "interval": interval,
                        "min_doc_count": 1, "extended_bounds": {}}},
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


def _kql_pie(obj_id: str, title: str, index_id: str, field: str, kql: str) -> dict:
    """Pie chart with a KQL pre-filter."""
    vis_state = {
        "title": title, "type": "pie",
        "params": {
            "type": "pie", "addTooltip": True, "addLegend": True,
            "legendPosition": "right", "isDonut": True,
            "labels": {"show": False, "values": True, "last_level": True, "truncate": 100},
        },
        "aggs": [
            {"id": "1", "enabled": True, "type": "count", "schema": "metric", "params": {}},
            {"id": "2", "enabled": True, "type": "terms", "schema": "segment",
             "params": {"field": field, "orderBy": "1", "order": "desc",
                        "size": 10, "otherBucket": False, "missingBucket": False}},
        ],
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


def _kql_top_table(obj_id: str, title: str, index_id: str,
                   bucket_field: str, metric_field: str, kql: str, size: int = 50) -> dict:
    """Top-N table sorted by max(metric_field), pre-filtered with KQL."""
    vis_state = {
        "title": title, "type": "table",
        "params": {
            "perPage": 25, "showPartialRows": False, "showMetricsAtAllLevels": False,
            "sort": {"columnIndex": None, "direction": None},
            "showTotal": False, "totalFunc": "sum", "percentageCol": "",
        },
        "aggs": [
            {"id": "1", "enabled": True, "type": "max", "schema": "metric",
             "params": {"field": metric_field,
                        "customLabel": metric_field.replace("_", " ").title()}},
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
            "kibanaSavedObjectMeta": {"searchSourceJSON": json.dumps({
                "index": index_id,
                "query": {"query": kql, "language": "kuery"},
                "filter": [],
            })},
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
        # Per-source evidence index patterns (Phase 39a)
        {"type": "index-pattern", "id": "ip-evidence-entra-id",
         "attributes": {"title": "evidence-entra-id", "timeFieldName": "collected_at",
                        "fields": fields_by_id.get("ip-evidence-entra-id", "[]")}, "references": []},
        {"type": "index-pattern", "id": "ip-evidence-o365",
         "attributes": {"title": "evidence-o365", "timeFieldName": "collected_at",
                        "fields": fields_by_id.get("ip-evidence-o365", "[]")}, "references": []},
        {"type": "index-pattern", "id": "ip-evidence-defender",
         "attributes": {"title": "evidence-defender", "timeFieldName": "collected_at",
                        "fields": fields_by_id.get("ip-evidence-defender", "[]")}, "references": []},
        {"type": "index-pattern", "id": "ip-evidence-sentinel",
         "attributes": {"title": "evidence-sentinel", "timeFieldName": "collected_at",
                        "fields": fields_by_id.get("ip-evidence-sentinel", "[]")}, "references": []},
        {"type": "index-pattern", "id": "ip-evidence-intune",
         "attributes": {"title": "evidence-intune", "timeFieldName": "collected_at",
                        "fields": fields_by_id.get("ip-evidence-intune", "[]")}, "references": []},
        {"type": "index-pattern", "id": "ip-evidence-crowdstrike",
         "attributes": {"title": "evidence-crowdstrike", "timeFieldName": "collected_at",
                        "fields": fields_by_id.get("ip-evidence-crowdstrike", "[]")}, "references": []},
        {"type": "index-pattern", "id": "ip-evidence-sentinelone",
         "attributes": {"title": "evidence-sentinelone", "timeFieldName": "collected_at",
                        "fields": fields_by_id.get("ip-evidence-sentinelone", "[]")}, "references": []},
        {"type": "index-pattern", "id": "ip-evidence-tenable",
         "attributes": {"title": "evidence-tenable", "timeFieldName": "collected_at",
                        "fields": fields_by_id.get("ip-evidence-tenable", "[]")}, "references": []},
        {"type": "index-pattern", "id": "ip-evidence-qualys",
         "attributes": {"title": "evidence-qualys", "timeFieldName": "collected_at",
                        "fields": fields_by_id.get("ip-evidence-qualys", "[]")}, "references": []},
        # Additional per-source patterns
        {"type": "index-pattern", "id": "ip-evidence-openvas",
         "attributes": {"title": "evidence-openvas", "timeFieldName": "collected_at",
                        "fields": fields_by_id.get("ip-evidence-openvas", "[]")}, "references": []},
        {"type": "index-pattern", "id": "ip-evidence-purview",
         "attributes": {"title": "evidence-purview", "timeFieldName": "collected_at",
                        "fields": fields_by_id.get("ip-evidence-purview", "[]")}, "references": []},
        {"type": "index-pattern", "id": "ip-evidence-fortigate",
         "attributes": {"title": "evidence-fortigate", "timeFieldName": "collected_at",
                        "fields": fields_by_id.get("ip-evidence-fortigate", "[]")}, "references": []},
        {"type": "index-pattern", "id": "ip-evidence-panw",
         "attributes": {"title": "evidence-panw", "timeFieldName": "collected_at",
                        "fields": fields_by_id.get("ip-evidence-panw", "[]")}, "references": []},
        {"type": "index-pattern", "id": "ip-evidence-cisco",
         "attributes": {"title": "evidence-cisco", "timeFieldName": "collected_at",
                        "fields": fields_by_id.get("ip-evidence-cisco", "[]")}, "references": []},
        {"type": "index-pattern", "id": "ip-evidence-zscaler",
         "attributes": {"title": "evidence-zscaler", "timeFieldName": "collected_at",
                        "fields": fields_by_id.get("ip-evidence-zscaler", "[]")}, "references": []},
        {"type": "index-pattern", "id": "ip-evidence-identity",
         "attributes": {"title": "evidence-identity", "timeFieldName": "collected_at",
                        "fields": fields_by_id.get("ip-evidence-identity", "[]")}, "references": []},
        {"type": "index-pattern", "id": "ip-evidence-prtg",
         "attributes": {"title": "evidence-prtg", "timeFieldName": "collected_at",
                        "fields": fields_by_id.get("ip-evidence-prtg", "[]")}, "references": []},
        {"type": "index-pattern", "id": "ip-evidence-zabbix",
         "attributes": {"title": "evidence-zabbix", "timeFieldName": "collected_at",
                        "fields": fields_by_id.get("ip-evidence-zabbix", "[]")}, "references": []},
        {"type": "index-pattern", "id": "ip-evidence-glpi",
         "attributes": {"title": "evidence-glpi", "timeFieldName": "collected_at",
                        "fields": fields_by_id.get("ip-evidence-glpi", "[]")}, "references": []},
        {"type": "index-pattern", "id": "ip-evidence-netbox",
         "attributes": {"title": "evidence-netbox", "timeFieldName": "collected_at",
                        "fields": fields_by_id.get("ip-evidence-netbox", "[]")}, "references": []},
        {"type": "index-pattern", "id": "ip-evidence-cyberark",
         "attributes": {"title": "evidence-cyberark", "timeFieldName": "collected_at",
                        "fields": fields_by_id.get("ip-evidence-cyberark", "[]")}, "references": []},
        {"type": "index-pattern", "id": "ip-evidence-aws-security-hub",
         "attributes": {"title": "evidence-aws-security-hub", "timeFieldName": "collected_at",
                        "fields": fields_by_id.get("ip-evidence-aws-security-hub", "[]")}, "references": []},
        {"type": "index-pattern", "id": "ip-evidence-azure-cspm",
         "attributes": {"title": "evidence-azure-cspm", "timeFieldName": "collected_at",
                        "fields": fields_by_id.get("ip-evidence-azure-cspm", "[]")}, "references": []},
        {"type": "index-pattern", "id": "ip-evidence-gcp-scc",
         "attributes": {"title": "evidence-gcp-scc", "timeFieldName": "collected_at",
                        "fields": fields_by_id.get("ip-evidence-gcp-scc", "[]")}, "references": []},
        {"type": "index-pattern", "id": "ip-evidence-threat-intel",
         "attributes": {"title": "evidence-threat-intel", "timeFieldName": "collected_at",
                        "fields": fields_by_id.get("ip-evidence-threat-intel", "[]")}, "references": []},
        # Phase 39b — 10 additional connectors
        {"type": "index-pattern", "id": "ip-evidence-wazuh",
         "attributes": {"title": "evidence-wazuh", "timeFieldName": "collected_at",
                        "fields": fields_by_id.get("ip-evidence-wazuh", "[]")}, "references": []},
        {"type": "index-pattern", "id": "ip-evidence-forti-analyzer",
         "attributes": {"title": "evidence-forti-analyzer", "timeFieldName": "collected_at",
                        "fields": fields_by_id.get("ip-evidence-forti-analyzer", "[]")}, "references": []},
        {"type": "index-pattern", "id": "ip-evidence-forti-manager",
         "attributes": {"title": "evidence-forti-manager", "timeFieldName": "collected_at",
                        "fields": fields_by_id.get("ip-evidence-forti-manager", "[]")}, "references": []},
        {"type": "index-pattern", "id": "ip-evidence-graylog",
         "attributes": {"title": "evidence-graylog", "timeFieldName": "collected_at",
                        "fields": fields_by_id.get("ip-evidence-graylog", "[]")}, "references": []},
        {"type": "index-pattern", "id": "ip-evidence-hashicorp-vault",
         "attributes": {"title": "evidence-hashicorp-vault", "timeFieldName": "collected_at",
                        "fields": fields_by_id.get("ip-evidence-hashicorp-vault", "[]")}, "references": []},
        {"type": "index-pattern", "id": "ip-evidence-devolutions",
         "attributes": {"title": "evidence-devolutions", "timeFieldName": "collected_at",
                        "fields": fields_by_id.get("ip-evidence-devolutions", "[]")}, "references": []},
        {"type": "index-pattern", "id": "ip-evidence-github",
         "attributes": {"title": "evidence-github", "timeFieldName": "collected_at",
                        "fields": fields_by_id.get("ip-evidence-github", "[]")}, "references": []},
        {"type": "index-pattern", "id": "ip-evidence-gitlab",
         "attributes": {"title": "evidence-gitlab", "timeFieldName": "collected_at",
                        "fields": fields_by_id.get("ip-evidence-gitlab", "[]")}, "references": []},
        {"type": "index-pattern", "id": "ip-evidence-jira",
         "attributes": {"title": "evidence-jira", "timeFieldName": "collected_at",
                        "fields": fields_by_id.get("ip-evidence-jira", "[]")}, "references": []},
        {"type": "index-pattern", "id": "ip-evidence-servicenow",
         "attributes": {"title": "evidence-servicenow", "timeFieldName": "collected_at",
                        "fields": fields_by_id.get("ip-evidence-servicenow", "[]")}, "references": []},
        # Wildcard — all per-source evidence indices (Phase 39.11)
        {"type": "index-pattern", "id": "ip-evidence-wildcard",
         "attributes": {"title": "evidence-*", "timeFieldName": "collected_at",
                        "fields": fields_by_id.get("ip-evidence-wildcard", "[]")}, "references": []},
        {"type": "index-pattern", "id": "ip-nvd-cve",
         "attributes": {
             "title": "nvd-cve",
             "timeFieldName": "indexed_at",
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
        # Phase 40e — Threat Intelligence index patterns
        {"type": "index-pattern", "id": "ip-ti-misp",
         "attributes": {
             "title": "ti-misp-*",
             "timeFieldName": "last_seen",
             "fields": fields_by_id.get("ip-ti-misp", "[]"),
         },
         "references": []},
        {"type": "index-pattern", "id": "ip-ti-abuseipdb",
         "attributes": {
             "title": "ti-abuseipdb-blacklist",
             "timeFieldName": "indexed_at",
             "fields": fields_by_id.get("ip-ti-abuseipdb", "[]"),
         },
         "references": []},
        {"type": "index-pattern", "id": "ip-ti-malpedia-families",
         "attributes": {
             "title": "ti-malpedia-families",
             "timeFieldName": "updated_at",
             "fields": fields_by_id.get("ip-ti-malpedia-families", "[]"),
         },
         "references": []},
        {"type": "index-pattern", "id": "ip-ti-malpedia-actors",
         "attributes": {
             "title": "ti-malpedia-actors",
             "timeFieldName": "updated_at",
             "fields": fields_by_id.get("ip-ti-malpedia-actors", "[]"),
         },
         "references": []},
        # Phase 41 — new TI feed index patterns
        {"type": "index-pattern", "id": "ip-ti-malpedia-tools",
         "attributes": {"title": "ti-malpedia-tools", "timeFieldName": "updated_at",
                        "fields": fields_by_id.get("ip-ti-malpedia-tools", "[]")}, "references": []},
        {"type": "index-pattern", "id": "ip-ti-urlhaus",
         "attributes": {"title": "ti-urlhaus", "timeFieldName": "date_added",
                        "fields": fields_by_id.get("ip-ti-urlhaus", "[]")}, "references": []},
        {"type": "index-pattern", "id": "ip-ti-threatfox",
         "attributes": {"title": "ti-threatfox", "timeFieldName": "first_seen",
                        "fields": fields_by_id.get("ip-ti-threatfox", "[]")}, "references": []},
        {"type": "index-pattern", "id": "ip-ti-sslbl",
         "attributes": {"title": "ti-sslbl", "timeFieldName": "listed_at",
                        "fields": fields_by_id.get("ip-ti-sslbl", "[]")}, "references": []},
        {"type": "index-pattern", "id": "ip-ti-feodotracker",
         "attributes": {"title": "ti-feodotracker", "timeFieldName": "first_seen",
                        "fields": fields_by_id.get("ip-ti-feodotracker", "[]")}, "references": []},
        {"type": "index-pattern", "id": "ip-ti-red-flag-domains",
         "attributes": {"title": "ti-red-flag-domains", "timeFieldName": "date_added",
                        "fields": fields_by_id.get("ip-ti-red-flag-domains", "[]")}, "references": []},
        {"type": "index-pattern", "id": "ip-ti-stopforumspam",
         "attributes": {"title": "ti-stopforumspam", "timeFieldName": "indexed_at",
                        "fields": fields_by_id.get("ip-ti-stopforumspam", "[]")}, "references": []},
        {"type": "index-pattern", "id": "ip-ti-malwarebazaar",
         "attributes": {"title": "ti-malwarebazaar", "timeFieldName": "first_seen",
                        "fields": fields_by_id.get("ip-ti-malwarebazaar", "[]")}, "references": []},
        # Phase 50 — AlienVault OTX
        {"type": "index-pattern", "id": "ip-ti-alienvault",
         "attributes": {"title": "ti-alienvault", "timeFieldName": "first_seen",
                        "fields": fields_by_id.get("ip-ti-alienvault", "[]")}, "references": []},
        # Phase 47 — Exploit-DB index pattern
        {"type": "index-pattern", "id": "ip-exploitdb",
         "attributes": {
             "title": "exploitdb",
             "timeFieldName": "date_published",
             "fields": fields_by_id.get("ip-exploitdb", "[]"),
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
        _kql_metric(     "viz-epss-total", "EPSS — CVEs Indexed",              "ip-nvd-cve", "epss_score: *"),
        _kql_metric(     "viz-epss-10p",   "EPSS — Score ≥ 50% (High Risk)",   "ip-nvd-cve", "epss_score >= 0.5"),
        _kql_metric(     "viz-epss-20p",   "EPSS — Score ≥ 90% (Extreme)",     "ip-nvd-cve", "epss_score >= 0.9"),
        _score_histogram("viz-epss-hist",  "EPSS — Score Distribution",        "ip-nvd-cve", "epss_score", 0.05),
        _kql_pie(        "viz-epss-kev",   "High-Risk CVEs — KEV Status",      "ip-nvd-cve", "in_kev", "epss_score >= 0.1"),
        _kql_top_table(  "viz-epss-top",   "EPSS — Top 50 High-Risk CVEs",     "ip-nvd-cve", "cve_id", "epss_score", "epss_score >= 0.01", 50),
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
        ("viz-epss-hist",   0,  5, 32, 11),
        ("viz-epss-kev",   32,  5, 16, 11),
        ("viz-epss-top",    0, 16, 48, 14),
    ]))
    objs.append(_dashboard("dash-kev", "ISMS CORE — CISA KEV Tracker", [
        ("viz-kev-total",      0,  0, 12, 5),
        ("viz-kev-time",      12,  0, 36, 5),
        ("viz-kev-vendors",    0,  5, 16, 9),
        ("viz-kev-products",  16,  5, 16, 9),
        ("viz-kev-ransomware",32,  5, 16, 9),
        ("viz-kev-table",      0, 14, 48, 12),
    ]))

    # ── Phase 39b — Connector Dashboards ─────────────────────────────────────

    # Entra ID Entity Analytics
    objs += [
        _metric(    "viz-entra-total",       "Entra ID — Total Entities",         "ip-evidence-entra-id"),
        _kql_metric("viz-entra-noncompliant","Entra ID — Non-Compliant Devices",  "ip-evidence-entra-id", "is_compliant: false"),
        _kql_metric("viz-entra-disabled",    "Entra ID — Disabled Accounts",      "ip-evidence-entra-id", "account_enabled: false"),
        _timeline(  "viz-entra-time",        "Entra ID — Sync Over Time",         "ip-evidence-entra-id", "collected_at"),
        _pie(       "viz-entra-dept",        "Entra ID — By Department",          "ip-evidence-entra-id", "department"),
        _pie(       "viz-entra-ownership",   "Entra ID — Device Ownership",       "ip-evidence-entra-id", "device_ownership"),
        _pie(       "viz-entra-os",          "Entra ID — OS Distribution",        "ip-evidence-entra-id", "os_name"),
        _count_table("viz-entra-groups",     "Entra ID — Top Groups",             "ip-evidence-entra-id", "group_names", 25),
    ]
    objs.append(_dashboard("dash-entra-id", "ISMS CORE — Entra ID Entity Analytics", [
        ("viz-entra-total",        0,  0, 16, 5),
        ("viz-entra-noncompliant", 16, 0, 16, 5),
        ("viz-entra-disabled",     32, 0, 16, 5),
        ("viz-entra-time",          0, 5, 48, 8),
        ("viz-entra-dept",          0,13, 16, 9),
        ("viz-entra-ownership",    16,13, 16, 9),
        ("viz-entra-os",           32,13, 16, 9),
        ("viz-entra-groups",        0,22, 48,10),
    ]))

    # O365 Audit
    objs += [
        _metric(    "viz-o365-total",        "O365 — Total Audit Events",         "ip-evidence-o365"),
        _kql_metric("viz-o365-external",     "O365 — External Access Events",     "ip-evidence-o365", "external_access: true"),
        _kql_metric("viz-o365-failures",     "O365 — Failed Operations",          "ip-evidence-o365", "result_status: Failed"),
        _timeline(  "viz-o365-time",         "O365 — Events Over Time",           "ip-evidence-o365", "collected_at"),
        _pie(       "viz-o365-workload",     "O365 — By Workload",                "ip-evidence-o365", "workload"),
        _pie(       "viz-o365-operation",    "O365 — By Operation",               "ip-evidence-o365", "operation"),
        _count_table("viz-o365-users",       "O365 — Top Users by Event Count",   "ip-evidence-o365", "user_id", 25),
    ]
    objs.append(_dashboard("dash-o365", "ISMS CORE — O365 Audit", [
        ("viz-o365-total",     0,  0, 16, 5),
        ("viz-o365-external", 16,  0, 16, 5),
        ("viz-o365-failures", 32,  0, 16, 5),
        ("viz-o365-time",      0,  5, 48, 8),
        ("viz-o365-workload",  0, 13, 16, 9),
        ("viz-o365-operation",16, 13, 16, 9),
        ("viz-o365-users",    32, 13, 16, 9),
    ]))

    # Microsoft Defender
    objs += [
        _metric(    "viz-def-total",         "Defender — Total Alerts",           "ip-evidence-defender"),
        _kql_metric("viz-def-critical",      "Defender — High Severity Alerts",   "ip-evidence-defender", "alert_severity: High"),
        _kql_metric("viz-def-open",          "Defender — Open Alerts",            "ip-evidence-defender", "alert_status: New"),
        _timeline(  "viz-def-time",          "Defender — Alerts Over Time",       "ip-evidence-defender", "collected_at"),
        _pie(       "viz-def-severity",      "Defender — By Severity",            "ip-evidence-defender", "alert_severity"),
        _pie(       "viz-def-category",      "Defender — By Category",            "ip-evidence-defender", "alert_category"),
        _count_table("viz-def-machines",     "Defender — Top Affected Machines",  "ip-evidence-defender", "machine_id", 25),
    ]
    objs.append(_dashboard("dash-defender", "ISMS CORE — Microsoft Defender", [
        ("viz-def-total",     0,  0, 16, 5),
        ("viz-def-critical", 16,  0, 16, 5),
        ("viz-def-open",     32,  0, 16, 5),
        ("viz-def-time",      0,  5, 48, 8),
        ("viz-def-severity",  0, 13, 16, 9),
        ("viz-def-category", 16, 13, 16, 9),
        ("viz-def-machines", 32, 13, 16, 9),
    ]))

    # ── Phase 39b — Vulnerability Dashboard (39.10) ───────────────────────────
    # Covers evidence-tenable (tenable_sc + tenable_io) and evidence-qualys
    objs += [
        # Tenable row
        _metric(    "viz-vuln-ten-total",    "Tenable — Total Findings",          "ip-evidence-tenable"),
        _kql_metric("viz-vuln-ten-critical", "Tenable — Critical Findings",       "ip-evidence-tenable", "severity: Critical"),
        _kql_metric("viz-vuln-ten-high",     "Tenable — High Findings",           "ip-evidence-tenable", "severity: High"),
        _timeline(  "viz-vuln-ten-time",     "Tenable — Findings Over Time",      "ip-evidence-tenable", "collected_at"),
        _pie(       "viz-vuln-ten-severity", "Tenable — By Severity",             "ip-evidence-tenable", "severity"),
        _count_table("viz-vuln-ten-assets",  "Tenable — Top Affected Assets",     "ip-evidence-tenable", "fqdn", 25),
        _count_table("viz-vuln-ten-cves",    "Tenable — Top CVEs",                "ip-evidence-tenable", "cve_id", 25),
        # Qualys row
        _metric(    "viz-vuln-qua-total",    "Qualys — Total Findings",           "ip-evidence-qualys"),
        _kql_metric("viz-vuln-qua-critical", "Qualys — Critical/Urgent (Sev 5)",  "ip-evidence-qualys", "severity: 5"),
        _kql_metric("viz-vuln-qua-high",     "Qualys — High (Sev 4)",             "ip-evidence-qualys", "severity: 4"),
        _timeline(  "viz-vuln-qua-time",     "Qualys — Findings Over Time",       "ip-evidence-qualys", "collected_at"),
        _pie(       "viz-vuln-qua-severity", "Qualys — By Severity",              "ip-evidence-qualys", "severity"),
        _count_table("viz-vuln-qua-assets",  "Qualys — Top Affected Assets",      "ip-evidence-qualys", "fqdn", 25),
        _count_table("viz-vuln-qua-cves",    "Qualys — Top CVEs",                 "ip-evidence-qualys", "cve_id", 25),
    ]
    objs.append(_dashboard("dash-vuln", "ISMS CORE — Vulnerability Findings", [
        # Row 0 — Tenable metrics
        ("viz-vuln-ten-total",     0,  0, 16, 5),
        ("viz-vuln-ten-critical", 16,  0, 16, 5),
        ("viz-vuln-ten-high",     32,  0, 16, 5),
        # Row 5 — Tenable timeline + severity + top assets
        ("viz-vuln-ten-time",      0,  5, 48, 8),
        ("viz-vuln-ten-severity",  0, 13, 16, 9),
        ("viz-vuln-ten-assets",   16, 13, 16, 9),
        ("viz-vuln-ten-cves",     32, 13, 16, 9),
        # Row 22 — Qualys metrics
        ("viz-vuln-qua-total",     0, 22, 16, 5),
        ("viz-vuln-qua-critical", 16, 22, 16, 5),
        ("viz-vuln-qua-high",     32, 22, 16, 5),
        # Row 27 — Qualys timeline + severity + top assets
        ("viz-vuln-qua-time",      0, 27, 48, 8),
        ("viz-vuln-qua-severity",  0, 35, 16, 9),
        ("viz-vuln-qua-assets",   16, 35, 16, 9),
        ("viz-vuln-qua-cves",     32, 35, 16, 9),
    ]))

    # ── Phase 39.11 — Evidence Overview (wildcard — all sources) ─────────────
    # Replaces the generic ip-evidence dashboard with a cross-source roll-up.
    # ip-evidence-wildcard uses title evidence-* covering all 44 connector indices.
    objs += [
        _metric(     "viz-ev-all-total",     "Evidence — Total (All Sources)",    "ip-evidence-wildcard"),
        _timeline(   "viz-ev-all-time",      "Evidence — Over Time (All Sources)","ip-evidence-wildcard", "collected_at"),
        _pie(        "viz-ev-all-source",    "Evidence — By Source System",       "ip-evidence-wildcard", "source_system"),
        _count_table("viz-ev-all-connector", "Evidence — By Connector",           "ip-evidence-wildcard", "connector_id", 50),
        _count_table("viz-ev-all-control",   "Evidence — By Control Group",       "ip-evidence-wildcard", "control_ids", 50),
    ]
    objs.append(_dashboard("dash-evidence", "ISMS CORE — Evidence Overview", [
        ("viz-ev-all-total",      0,  0, 12, 5),
        ("viz-ev-all-time",      12,  0, 36, 5),
        ("viz-ev-all-source",     0,  5, 16, 9),
        ("viz-ev-all-connector", 16,  5, 16, 9),
        ("viz-ev-all-control",   32,  5, 16, 9),
    ]))

    # ── Phase 40e — Threat Intelligence Dashboards ───────────────────────────

    # MISP IOC Explorer (CIRCL + Botvrij combined via ti-misp-* wildcard)
    # mitre_tids/family_slugs/actor_slugs are empty for CIRCL/Botvrij feeds — these
    # public feeds provide raw IOCs without ATT&CK/Malpedia enrichment.
    # Useful fields with actual data: ioc_type, source, tags, confidence.
    objs += [
        _metric(     "viz-ti-misp-total",    "MISP — Total IOCs",                 "ip-ti-misp"),
        _kql_metric( "viz-ti-misp-circl",    "MISP — CIRCL Events",               "ip-ti-misp", "source: circl_misp"),
        _kql_metric( "viz-ti-misp-botvrij",  "MISP — Botvrij Events",             "ip-ti-misp", "source: botvrij_misp"),
        _timeline(   "viz-ti-misp-time",     "MISP — IOCs Over Time",             "ip-ti-misp", "last_seen"),
        _pie(        "viz-ti-misp-type",     "MISP — By IOC Type",                "ip-ti-misp", "ioc_type"),
        _pie(        "viz-ti-misp-source",   "MISP — By Source Feed",             "ip-ti-misp", "source"),
        _count_table("viz-ti-misp-tags",     "MISP — Top Tags",                   "ip-ti-misp", "tags", 30),
        _score_histogram("viz-ti-misp-conf", "MISP — Confidence Distribution",    "ip-ti-misp", "confidence", 10),
    ]
    objs.append(_dashboard("dash-ti-misp", "ISMS CORE — MISP Threat Intelligence", [
        ("viz-ti-misp-total",    0,  0, 16, 5),
        ("viz-ti-misp-circl",   16,  0, 16, 5),
        ("viz-ti-misp-botvrij", 32,  0, 16, 5),
        ("viz-ti-misp-time",     0,  5, 48, 8),
        ("viz-ti-misp-type",     0, 13, 16, 9),
        ("viz-ti-misp-source",  16, 13, 16, 9),
        ("viz-ti-misp-conf",    32, 13, 16, 9),
        ("viz-ti-misp-tags",     0, 22, 48,10),
    ]))

    # AbuseIPDB Blacklist
    # Feed uses confidenceMinimum=100 → all IPs have abuse_score=100 (not useful for metrics).
    # Geo enrichment via MaxMind GeoLite2 City (geo_*). Privacy enrichment via IPInfo (privacy_*).
    objs += [
        _metric(     "viz-ti-abuse-total",   "AbuseIPDB — Blacklisted IPs",          "ip-ti-abuseipdb"),
        _pie(        "viz-ti-abuse-country", "AbuseIPDB — By Country",               "ip-ti-abuseipdb", "country_code"),
        _pie(        "viz-ti-abuse-privacy", "AbuseIPDB — By Privacy Type",          "ip-ti-abuseipdb", "privacy_label"),
        _timeline(   "viz-ti-abuse-time",    "AbuseIPDB — Last Reported Over Time",  "ip-ti-abuseipdb", "last_reported_at"),
        _geo_map(    "viz-ti-abuse-geomap",  "AbuseIPDB — IP Geolocation Map",       "ip-ti-abuseipdb"),
        _count_table("viz-ti-abuse-city",    "AbuseIPDB — Top Cities",               "ip-ti-abuseipdb", "geo_city", 25),
        _count_table("viz-ti-abuse-asn",     "AbuseIPDB — Top ASNs",                 "ip-ti-abuseipdb", "geo_org", 25),
        _count_table("viz-ti-abuse-isp",     "AbuseIPDB — Top ISPs",                 "ip-ti-abuseipdb", "isp", 25),
    ]
    objs.append(_dashboard("dash-ti-abuseipdb", "ISMS CORE — AbuseIPDB Blacklist", [
        ("viz-ti-abuse-total",    0,  0, 16, 8),
        ("viz-ti-abuse-country", 16,  0, 16, 8),
        ("viz-ti-abuse-privacy", 32,  0, 16, 8),
        ("viz-ti-abuse-time",     0,  8, 48, 8),
        ("viz-ti-abuse-geomap",   0, 16, 48,22),
        ("viz-ti-abuse-city",     0, 38, 48, 9),
        ("viz-ti-abuse-asn",      0, 47, 48, 9),
        ("viz-ti-abuse-isp",      0, 56, 48, 9),
    ]))

    # Malpedia — Malware Families
    objs += [
        _metric(     "viz-ti-mal-fam-total",   "Malpedia — Malware Families",          "ip-ti-malpedia-families"),
        _count_table("viz-ti-mal-fam-tids",    "Families — Top ATT&CK TIDs",           "ip-ti-malpedia-families", "mitre_tids", 25),
    ]

    # Malpedia — Threat Actors + Tools
    # actor_type is mapped as keyword → aggregate directly, no .keyword suffix needed.
    # actor_slugs on families is empty (attribution not resolved from API) → removed.
    # Tools and Families share mitre_tids field → compare ATT&CK coverage side by side.
    objs += [
        _metric(     "viz-ti-mal-act-total",   "Malpedia — Threat Actors",             "ip-ti-malpedia-actors"),
        _pie(        "viz-ti-mal-act-country", "Actors — By Country",                  "ip-ti-malpedia-actors", "country"),
        _pie(        "viz-ti-mal-act-motiv",   "Actors — By Motivation",               "ip-ti-malpedia-actors", "motivation"),
        _pie(        "viz-ti-mal-act-type",    "Actors — APT vs Ransomware Groups",    "ip-ti-malpedia-actors", "actor_type"),
        _metric(     "viz-ti-mal-tool-total",  "Malpedia — Tools",                     "ip-ti-malpedia-tools"),
        _count_table("viz-ti-mal-tool-tids",   "Tools — Top ATT&CK TIDs",             "ip-ti-malpedia-tools", "mitre_tids", 25),
    ]
    objs.append(_dashboard("dash-ti-malpedia", "ISMS CORE — Malpedia Atlas", [
        # Summary metrics row
        ("viz-ti-mal-fam-total",    0,  0, 16, 5),
        ("viz-ti-mal-act-total",   16,  0, 16, 5),
        ("viz-ti-mal-tool-total",  32,  0, 16, 5),
        # Actors analysis row
        ("viz-ti-mal-act-country",  0,  5, 16, 9),
        ("viz-ti-mal-act-motiv",   16,  5, 16, 9),
        ("viz-ti-mal-act-type",    32,  5, 16, 9),
        # Families + Tools MITRE coverage row
        ("viz-ti-mal-fam-tids",     0, 14, 24, 9),
        ("viz-ti-mal-tool-tids",   24, 14, 24, 9),
    ]))

    # ── URLhaus ───────────────────────────────────────────────────────────────
    # Fields: url_status (keyword), threat (keyword), tags (keyword), date_added (date)
    # url_status values: online / offline / unknown
    # threat values: malware_download, botnet_cc, phishing, etc.
    objs += [
        _metric(     "viz-ti-uh-total",   "URLhaus — Malicious URLs",         "ip-ti-urlhaus"),
        _kql_metric( "viz-ti-uh-online",  "URLhaus — Currently Online",       "ip-ti-urlhaus", "url_status: online"),
        _kql_metric( "viz-ti-uh-malware", "URLhaus — Malware Download URLs",  "ip-ti-urlhaus", "threat: malware_download"),
        _timeline(   "viz-ti-uh-time",    "URLhaus — URLs Added Over Time",   "ip-ti-urlhaus", "date_added"),
        _pie(        "viz-ti-uh-status",  "URLhaus — By Status",              "ip-ti-urlhaus", "url_status"),
        _pie(        "viz-ti-uh-threat",  "URLhaus — By Threat Category",     "ip-ti-urlhaus", "threat"),
        _count_table("viz-ti-uh-tags",    "URLhaus — Top Tags",               "ip-ti-urlhaus", "tags", 25),
    ]
    objs.append(_dashboard("dash-ti-urlhaus", "ISMS CORE — URLhaus", [
        ("viz-ti-uh-total",    0,  0, 16, 5),
        ("viz-ti-uh-online",  16,  0, 16, 5),
        ("viz-ti-uh-malware", 32,  0, 16, 5),
        ("viz-ti-uh-time",     0,  5, 48, 8),
        ("viz-ti-uh-status",   0, 13, 24, 9),
        ("viz-ti-uh-threat",  24, 13, 24, 9),
        ("viz-ti-uh-tags",     0, 22, 48,10),
    ]))

    # ── ThreatFox ─────────────────────────────────────────────────────────────
    # Fields: ioc_type (keyword), threat_type (keyword), malware (keyword),
    #         confidence (integer 0-100), tags (keyword), first_seen (date)
    objs += [
        _metric(          "viz-ti-tf-total",    "ThreatFox — IOCs Indexed",              "ip-ti-threatfox"),
        _kql_metric(      "viz-ti-tf-highconf", "ThreatFox — High Confidence (≥90)",     "ip-ti-threatfox", "confidence >= 90"),
        _timeline(        "viz-ti-tf-time",     "ThreatFox — IOCs Over Time",            "ip-ti-threatfox", "first_seen"),
        _pie(             "viz-ti-tf-ioctype",  "ThreatFox — By IOC Type",              "ip-ti-threatfox", "ioc_type"),
        _pie(             "viz-ti-tf-threat",   "ThreatFox — By Threat Type",           "ip-ti-threatfox", "threat_type"),
        _score_histogram( "viz-ti-tf-conf",     "ThreatFox — Confidence Distribution",  "ip-ti-threatfox", "confidence", 10),
        _count_table(     "viz-ti-tf-malware",  "ThreatFox — Top Malware Families",     "ip-ti-threatfox", "malware", 25),
    ]
    objs.append(_dashboard("dash-ti-threatfox", "ISMS CORE — ThreatFox", [
        ("viz-ti-tf-total",     0,  0, 24, 5),
        ("viz-ti-tf-highconf", 24,  0, 24, 5),
        ("viz-ti-tf-time",      0,  5, 48, 8),
        ("viz-ti-tf-ioctype",   0, 13, 16, 9),
        ("viz-ti-tf-threat",   16, 13, 16, 9),
        ("viz-ti-tf-conf",     32, 13, 16, 9),
        ("viz-ti-tf-malware",   0, 22, 48,10),
    ]))

    # ── SSLBL C2 Blacklist ────────────────────────────────────────────────────
    # Fields: sha1 (keyword), reason (keyword), listed_at (date)
    # reason values: Dridex botnet C2, Emotet botnet C2, etc.
    objs += [
        _metric(     "viz-ti-ssl-total",  "SSLBL — Blacklisted Certificates",   "ip-ti-sslbl"),
        _timeline(   "viz-ti-ssl-time",   "SSLBL — Listings Over Time",          "ip-ti-sslbl", "listed_at"),
        _count_table("viz-ti-ssl-reason", "SSLBL — By Botnet / Reason",          "ip-ti-sslbl", "reason", 20),
    ]
    objs.append(_dashboard("dash-ti-sslbl", "ISMS CORE — SSLBL C2 Blacklist", [
        ("viz-ti-ssl-total",   0,  0, 12, 5),
        ("viz-ti-ssl-time",   12,  0, 36, 5),
        ("viz-ti-ssl-reason",  0,  5, 48,12),
    ]))

    # ── Feodo Tracker ─────────────────────────────────────────────────────────
    # Fields: port (integer), c2_status (keyword), malware (keyword), first_seen (date)
    # c2_status: online / offline  |  malware: Dridex, Emotet, QakBot, etc.
    objs += [
        _metric(     "viz-ti-fd-total",   "Feodo — C2 Servers Tracked",         "ip-ti-feodotracker"),
        _kql_metric( "viz-ti-fd-online",  "Feodo — Currently Online",           "ip-ti-feodotracker", "c2_status: online"),
        _kql_metric( "viz-ti-fd-offline", "Feodo — Offline / Historic",         "ip-ti-feodotracker", "c2_status: offline"),
        _pie(        "viz-ti-fd-malware", "Feodo — By Malware Family",          "ip-ti-feodotracker", "malware"),
        _pie(        "viz-ti-fd-status",  "Feodo — Online vs Offline",          "ip-ti-feodotracker", "c2_status"),
        _timeline(   "viz-ti-fd-time",    "Feodo — C2 Servers First Seen",      "ip-ti-feodotracker", "first_seen"),
        _count_table("viz-ti-fd-ports",   "Feodo — Top C2 Ports",              "ip-ti-feodotracker", "port", 15),
    ]
    objs.append(_dashboard("dash-ti-feodo", "ISMS CORE — Feodo Tracker", [
        ("viz-ti-fd-total",    0,  0, 16, 5),
        ("viz-ti-fd-online",  16,  0, 16, 5),
        ("viz-ti-fd-offline", 32,  0, 16, 5),
        ("viz-ti-fd-malware",  0,  5, 24, 9),
        ("viz-ti-fd-status",  24,  5, 24, 9),
        ("viz-ti-fd-time",     0, 14, 48, 8),
        ("viz-ti-fd-ports",    0, 22, 48, 9),
    ]))

    # ── MalwareBazaar ─────────────────────────────────────────────────────────
    # Fields: file_type (keyword), signature (keyword), tags (keyword), first_seen (date)
    # signature: malware family name assigned by analysts
    objs += [
        _metric(     "viz-ti-mb-total",   "MalwareBazaar — Samples Indexed",    "ip-ti-malwarebazaar"),
        _kql_metric( "viz-ti-mb-sig",     "MalwareBazaar — With Signature",     "ip-ti-malwarebazaar", "signature: *"),
        _timeline(   "viz-ti-mb-time",    "MalwareBazaar — Samples Over Time",  "ip-ti-malwarebazaar", "first_seen"),
        _pie(        "viz-ti-mb-ftype",   "MalwareBazaar — By File Type",       "ip-ti-malwarebazaar", "file_type"),
        _count_table("viz-ti-mb-sig-tbl", "MalwareBazaar — Top Malware Families (Signature)", "ip-ti-malwarebazaar", "signature", 25),
        _count_table("viz-ti-mb-tags",    "MalwareBazaar — Top Tags",           "ip-ti-malwarebazaar", "tags", 25),
    ]
    objs.append(_dashboard("dash-ti-malwarebazaar", "ISMS CORE — MalwareBazaar", [
        ("viz-ti-mb-total",    0,  0, 24, 5),
        ("viz-ti-mb-sig",     24,  0, 24, 5),
        ("viz-ti-mb-time",     0,  5, 48, 8),
        ("viz-ti-mb-ftype",    0, 13, 16, 9),
        ("viz-ti-mb-sig-tbl", 16, 13, 32, 9),
        ("viz-ti-mb-tags",     0, 22, 48,10),
    ]))

    # ── AlienVault OTX ────────────────────────────────────────────────────────
    # Fields: ioc_type (keyword), adversary (keyword), industries (keyword),
    #         countries (keyword), malware (keyword), mitre_tids (keyword), tlp (keyword)
    objs += [
        _metric(     "viz-ti-otx-total",     "AlienVault OTX — IOCs Indexed",          "ip-ti-alienvault"),
        _timeline(   "viz-ti-otx-time",      "AlienVault OTX — IOCs Over Time",        "ip-ti-alienvault", "first_seen"),
        _pie(        "viz-ti-otx-type",      "AlienVault OTX — By IOC Type",           "ip-ti-alienvault", "ioc_type"),
        _pie(        "viz-ti-otx-tlp",       "AlienVault OTX — By TLP",                "ip-ti-alienvault", "tlp"),
        _count_table("viz-ti-otx-adversary", "AlienVault OTX — Top Adversaries",       "ip-ti-alienvault", "adversary", 25),
        _count_table("viz-ti-otx-malware",   "AlienVault OTX — Top Malware Families",  "ip-ti-alienvault", "malware", 25),
        _count_table("viz-ti-otx-tids",      "AlienVault OTX — Top ATT&CK Techniques", "ip-ti-alienvault", "mitre_tids", 25),
        _count_table("viz-ti-otx-industry",  "AlienVault OTX — Top Targeted Industries","ip-ti-alienvault", "industries", 20),
    ]
    objs.append(_dashboard("dash-ti-alienvault", "ISMS CORE — AlienVault OTX", [
        ("viz-ti-otx-total",      0,  0, 24, 5),
        ("viz-ti-otx-time",      24,  0, 24, 5),
        ("viz-ti-otx-type",       0,  5, 16, 9),
        ("viz-ti-otx-tlp",       16,  5, 16, 9),
        ("viz-ti-otx-adversary", 32,  5, 16, 9),
        ("viz-ti-otx-malware",    0, 14, 24,10),
        ("viz-ti-otx-tids",      24, 14, 24,10),
        ("viz-ti-otx-industry",   0, 24, 48, 9),
    ]))

    # ── Red Flag Domains + Stopforumspam (combined blocklists) ────────────────
    # Red Flag Domains: domain (keyword), date_added (date) — minimal fields
    # Stopforumspam: ip (ip), indexed_at (date) — minimal fields
    # Combined into one dashboard — both are simple blocklist feeds
    objs += [
        _metric(   "viz-ti-rfd-total",  "Red Flag Domains — Blocked Domains",     "ip-ti-red-flag-domains"),
        _timeline( "viz-ti-rfd-time",   "Red Flag Domains — Added Over Time",      "ip-ti-red-flag-domains", "date_added"),
        _metric(   "viz-ti-sfs-total",  "Stopforumspam — Blocked IPs",             "ip-ti-stopforumspam"),
        _timeline( "viz-ti-sfs-time",   "Stopforumspam — Indexed Over Time",       "ip-ti-stopforumspam", "indexed_at"),
    ]
    objs.append(_dashboard("dash-ti-blocklists", "ISMS CORE — Blocklists (RFD + SFS)", [
        ("viz-ti-rfd-total",  0,  0, 24, 5),
        ("viz-ti-sfs-total", 24,  0, 24, 5),
        ("viz-ti-rfd-time",   0,  5, 48, 8),
        ("viz-ti-sfs-time",   0, 13, 48, 8),
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
        "ip-evidence":               get_osd_fields("evidence"),
        "ip-audit-logs":             get_osd_fields("audit-logs"),
        "ip-connector-runs":         get_osd_fields("connector-runs"),
        "ip-nvd-cve":                get_osd_fields("nvd-cve"),
        "ip-cisa-kev":               get_osd_fields("cisa-kev"),
        # Per-source evidence indices (Phase 39a — all connectors)
        "ip-evidence-entra-id":          get_osd_fields("evidence-entra-id"),
        "ip-evidence-o365":              get_osd_fields("evidence-o365"),
        "ip-evidence-defender":          get_osd_fields("evidence-defender"),
        "ip-evidence-sentinel":          get_osd_fields("evidence-sentinel"),
        "ip-evidence-intune":            get_osd_fields("evidence-intune"),
        "ip-evidence-purview":           get_osd_fields("evidence-purview"),
        "ip-evidence-crowdstrike":       get_osd_fields("evidence-crowdstrike"),
        "ip-evidence-sentinelone":       get_osd_fields("evidence-sentinelone"),
        "ip-evidence-tenable":           get_osd_fields("evidence-tenable"),
        "ip-evidence-qualys":            get_osd_fields("evidence-qualys"),
        "ip-evidence-openvas":           get_osd_fields("evidence-openvas"),
        "ip-evidence-fortigate":         get_osd_fields("evidence-fortigate"),
        "ip-evidence-panw":              get_osd_fields("evidence-panw"),
        "ip-evidence-cisco":             get_osd_fields("evidence-cisco"),
        "ip-evidence-zscaler":           get_osd_fields("evidence-zscaler"),
        "ip-evidence-identity":          get_osd_fields("evidence-identity"),
        "ip-evidence-prtg":              get_osd_fields("evidence-prtg"),
        "ip-evidence-zabbix":            get_osd_fields("evidence-zabbix"),
        "ip-evidence-glpi":              get_osd_fields("evidence-glpi"),
        "ip-evidence-netbox":            get_osd_fields("evidence-netbox"),
        "ip-evidence-cyberark":          get_osd_fields("evidence-cyberark"),
        "ip-evidence-aws-security-hub":  get_osd_fields("evidence-aws-security-hub"),
        "ip-evidence-azure-cspm":        get_osd_fields("evidence-azure-cspm"),
        "ip-evidence-gcp-scc":           get_osd_fields("evidence-gcp-scc"),
        "ip-evidence-threat-intel":      get_osd_fields("evidence-threat-intel"),
        # Phase 39b — 10 additional connectors
        "ip-evidence-wazuh":             get_osd_fields("evidence-wazuh"),
        "ip-evidence-forti-analyzer":    get_osd_fields("evidence-forti-analyzer"),
        "ip-evidence-forti-manager":     get_osd_fields("evidence-forti-manager"),
        "ip-evidence-graylog":           get_osd_fields("evidence-graylog"),
        "ip-evidence-hashicorp-vault":   get_osd_fields("evidence-hashicorp-vault"),
        "ip-evidence-devolutions":       get_osd_fields("evidence-devolutions"),
        "ip-evidence-github":            get_osd_fields("evidence-github"),
        "ip-evidence-gitlab":            get_osd_fields("evidence-gitlab"),
        "ip-evidence-jira":              get_osd_fields("evidence-jira"),
        "ip-evidence-servicenow":        get_osd_fields("evidence-servicenow"),
        # Wildcard — all per-source evidence indices (Phase 39.11)
        "ip-evidence-wildcard":          get_osd_fields("evidence-*"),
        # Phase 40e — Threat Intelligence indices
        "ip-ti-misp":                    get_osd_fields("ti-misp-*"),
        "ip-ti-abuseipdb":               get_osd_fields("ti-abuseipdb-blacklist"),
        "ip-ti-malpedia-families":       get_osd_fields("ti-malpedia-families"),
        "ip-ti-malpedia-actors":         get_osd_fields("ti-malpedia-actors"),
        # Phase 41 — new TI feeds
        "ip-ti-malpedia-tools":          get_osd_fields("ti-malpedia-tools"),
        "ip-ti-urlhaus":                 get_osd_fields("ti-urlhaus"),
        "ip-ti-threatfox":               get_osd_fields("ti-threatfox"),
        "ip-ti-sslbl":                   get_osd_fields("ti-sslbl"),
        "ip-ti-feodotracker":            get_osd_fields("ti-feodotracker"),
        "ip-ti-red-flag-domains":        get_osd_fields("ti-red-flag-domains"),
        "ip-ti-stopforumspam":           get_osd_fields("ti-stopforumspam"),
        "ip-ti-malwarebazaar":           get_osd_fields("ti-malwarebazaar"),
        # Phase 50 — AlienVault OTX
        "ip-ti-alienvault":              get_osd_fields("ti-alienvault"),
        # Phase 47 — Exploit-DB
        "ip-exploitdb":                  get_osd_fields("exploitdb"),
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
