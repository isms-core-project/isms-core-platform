"""Phase 27 — NVD CVE feed.

Pulls the full NVD CVE dataset (weekly) and delta updates (daily) from the
NIST NVD REST API v2, indexing into OpenSearch `nvd-cve`.

Also extracts CPEs from HIGH/CRITICAL/KEV/EPSS≥0.1 CVEs (Option A) and
upserts them into `nvd-cpe` — no extra API calls needed.

Schedule:
  - Full pull : Sunday 01:00 UTC
  - Delta pull: Daily 03:00 UTC (uses lastModStartDate from last run)

Env:
  NIST_API_KEY          — optional, raises rate limit from 5→50 req/30s
  FEEDS_CVE_ENABLED     — toggle (default: true)
  OPENSEARCH_URL        — OpenSearch host (default: http://opensearch:9200)
"""

import logging
import os
import time
from datetime import date, datetime, timezone
from uuid import uuid4

import requests

from feeds.base import fail_run, finish_run, get_conn, start_run

logger = logging.getLogger(__name__)

NVD_CVE_URL  = "https://services.nvd.nist.gov/rest/json/cves/2.0"
PAGE_SIZE    = 2000
_RUN_NAME    = "nist_cve"

# Rate limit: 0.6s between requests without key, 0.1s with key
_SLEEP_NO_KEY = 0.65
_SLEEP_KEY    = 0.12


def _headers() -> dict:
    key = os.environ.get("NIST_API_KEY", "").strip()
    return {"apiKey": key} if key else {}


def _sleep_between_pages():
    key = os.environ.get("NIST_API_KEY", "").strip()
    time.sleep(_SLEEP_KEY if key else _SLEEP_NO_KEY)


def _parse_dt(s: str | None) -> str | None:
    if not s:
        return None
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00")).isoformat()
    except Exception:
        return None


def _extract_cvss(metrics: dict) -> tuple[float | None, str | None, str | None, float | None]:
    """Return (v3_score, v3_severity, v3_vector, v2_score)."""
    v3_score = v3_severity = v3_vector = v2_score = None

    for key in ("cvssMetricV31", "cvssMetricV30"):
        items = metrics.get(key) or []
        if items:
            cvss = items[0].get("cvssData", {})
            v3_score    = cvss.get("baseScore")
            v3_severity = cvss.get("baseSeverity")
            v3_vector   = cvss.get("vectorString")
            break

    items_v2 = metrics.get("cvssMetricV2") or []
    if items_v2:
        v2_score = items_v2[0].get("cvssData", {}).get("baseScore")

    return v3_score, v3_severity, v3_vector, v2_score


def _extract_cpes(configurations: list) -> list[str]:
    """Extract unique CPE URIs from the configurations block."""
    cpes: set[str] = set()
    for cfg in configurations:
        for node in cfg.get("nodes") or []:
            for match in node.get("cpeMatch") or []:
                uri = match.get("criteria")
                if uri and match.get("vulnerable"):
                    cpes.add(uri)
    return list(cpes)


def _extract_cwes(weaknesses: list) -> list[str]:
    cwes: set[str] = set()
    for w in weaknesses:
        for d in w.get("description") or []:
            val = d.get("value", "")
            if val.startswith("CWE-"):
                cwes.add(val)
    return list(cwes)


def _get_kev_cve_ids() -> set[str]:
    """Load all KEV CVE IDs from DB for in_kev flag."""
    try:
        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT cve_id FROM cisa_kev_entries")
                return {row[0] for row in cur.fetchall()}
    except Exception as e:
        logger.warning("Could not load KEV IDs: %s", e)
        return set()


def _get_epss_scores() -> dict[str, float]:
    """Load EPSS scores from DB for denormalization. Returns {cve_id: score}."""
    try:
        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute("SELECT cve_id, score FROM epss_scores")
                return {row[0]: float(row[1]) for row in cur.fetchall()}
    except Exception as e:
        logger.warning("Could not load EPSS scores: %s", e)
        return {}


def _get_os_client():
    """Get OpenSearch client from env."""
    from opensearchpy import OpenSearch
    url = os.environ.get("OPENSEARCH_URL", "http://opensearch:9200")
    return OpenSearch(hosts=[url], use_ssl=False, verify_certs=False, timeout=30)


def _ensure_nvd_indices(os_client) -> None:
    """Create nvd-cve and nvd-cpe if they don't exist."""
    cve_mapping = {
        "mappings": {"properties": {
            "cve_id":           {"type": "keyword"},
            "published":        {"type": "date"},
            "last_modified":    {"type": "date"},
            "vuln_status":      {"type": "keyword"},
            "description":      {"type": "text"},
            "cvss_v3_score":    {"type": "float"},
            "cvss_v3_severity": {"type": "keyword"},
            "cvss_v3_vector":   {"type": "keyword"},
            "cvss_v2_score":    {"type": "float"},
            "cwe_ids":          {"type": "keyword"},
            "cpe_affected":     {"type": "keyword"},
            "in_kev":           {"type": "boolean"},
            "epss_score":       {"type": "float"},
            "references":       {"type": "text"},
            "indexed_at":       {"type": "date"},
        }}
    }
    cpe_mapping = {
        "mappings": {"properties": {
            "cpe_uri":    {"type": "keyword"},
            "part":       {"type": "keyword"},
            "vendor":     {"type": "keyword"},
            "product":    {"type": "keyword"},
            "version":    {"type": "keyword"},
            "title":      {"type": "text"},
            "in_kev":     {"type": "boolean"},
            "source":     {"type": "keyword"},
            "indexed_at": {"type": "date"},
        }}
    }
    for idx, mapping in [("nvd-cve", cve_mapping), ("nvd-cpe", cpe_mapping)]:
        try:
            if not os_client.indices.exists(index=idx):
                os_client.indices.create(index=idx, body=mapping)
                logger.info("Created index: %s", idx)
        except Exception as e:
            logger.warning("Could not ensure index %s: %s", idx, e)


def _fetch_page(params: dict) -> dict:
    resp = requests.get(NVD_CVE_URL, headers=_headers(), params=params, timeout=60)
    resp.raise_for_status()
    return resp.json()


def _get_last_run_date() -> datetime | None:
    """Return the start time of the last successful CVE run."""
    try:
        with get_conn() as conn:
            with conn.cursor() as cur:
                cur.execute(
                    """
                    SELECT started_at FROM feed_runs
                    WHERE feed_name = %s AND status = 'success'
                    ORDER BY started_at DESC LIMIT 1
                    """,
                    (_RUN_NAME,),
                )
                row = cur.fetchone()
                return row[0] if row else None
    except Exception:
        return None


def run(full: bool = False) -> None:
    """Pull NVD CVE data.

    full=True  → fetch all CVEs (weekly)
    full=False → fetch only CVEs modified since last successful run (daily delta)
    """
    run_id = start_run(_RUN_NAME)
    mode   = "full" if full else "delta"
    logger.info("NVD CVE %s pull started", mode)

    try:
        os_client = _get_os_client()
        _ensure_nvd_indices(os_client)
    except Exception as exc:
        fail_run(run_id, f"OpenSearch init failed: {exc}")
        logger.error("NVD CVE: OpenSearch unavailable: %s", exc)
        return

    kev_ids    = _get_kev_cve_ids()
    epss_map   = _get_epss_scores()
    now_iso    = datetime.now(timezone.utc).isoformat()

    # Build base params
    params: dict = {"resultsPerPage": PAGE_SIZE, "startIndex": 0}
    if not full:
        last_run = _get_last_run_date()
        if last_run:
            params["lastModStartDate"] = last_run.strftime("%Y-%m-%dT%H:%M:%S.000")
            params["lastModEndDate"]   = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000")
            logger.info("Delta mode: changes since %s", last_run)
        else:
            logger.info("No previous run found — running full pull")
            full = True
            params.pop("lastModStartDate", None)
            params.pop("lastModEndDate", None)

    indexed_cve = 0
    indexed_cpe = 0
    # CPE dedup across pages
    cpe_seen: set[str] = set()

    # First page to get total
    try:
        first = _fetch_page(params)
    except Exception as exc:
        fail_run(run_id, str(exc))
        logger.error("NVD CVE first page failed: %s", exc)
        return

    total_results = first.get("totalResults", 0)
    logger.info("NVD CVE %s: %d CVEs to process", mode, total_results)

    pages_data = [first]
    start = PAGE_SIZE
    while start < total_results:
        _sleep_between_pages()
        try:
            page = _fetch_page({**params, "startIndex": start})
            pages_data.append(page)
        except Exception as exc:
            logger.warning("NVD CVE page at %d failed: %s — skipping", start, exc)
        start += PAGE_SIZE

    for page_data in pages_data:
        for item in page_data.get("vulnerabilities") or []:
            cve = item.get("cve") or {}
            cve_id = cve.get("id") or ""
            if not cve_id:
                continue

            # Description (prefer English)
            desc = ""
            for d in cve.get("descriptions") or []:
                if d.get("lang") == "en":
                    desc = d.get("value", "")
                    break

            metrics     = cve.get("metrics") or {}
            v3_score, v3_sev, v3_vec, v2_score = _extract_cvss(metrics)
            cpe_list    = _extract_cpes(cve.get("configurations") or [])
            cwe_list    = _extract_cwes(cve.get("weaknesses") or [])
            refs        = [r.get("url", "") for r in (cve.get("references") or []) if r.get("url")]
            in_kev      = cve_id in kev_ids
            epss_score  = epss_map.get(cve_id)

            doc = {
                "cve_id":           cve_id,
                "published":        _parse_dt(cve.get("published")),
                "last_modified":    _parse_dt(cve.get("lastModified")),
                "vuln_status":      cve.get("vulnStatus"),
                "description":      desc,
                "cvss_v3_score":    v3_score,
                "cvss_v3_severity": v3_sev,
                "cvss_v3_vector":   v3_vec,
                "cvss_v2_score":    v2_score,
                "cwe_ids":          cwe_list,
                "cpe_affected":     cpe_list,
                "in_kev":           in_kev,
                "epss_score":       epss_score,
                "references":       refs[:20],
            }

            try:
                os_client.index(index="nvd-cve", id=cve_id, body={**doc, "indexed_at": now_iso})
                indexed_cve += 1
            except Exception as e:
                logger.warning("Failed to index CVE %s: %s", cve_id, e)
                continue

            # ── Option A: extract CPEs from HIGH/CRITICAL/KEV/EPSS≥0.1 CVEs ──
            if cpe_list and (
                v3_sev in ("HIGH", "CRITICAL")
                or in_kev
                or (epss_score is not None and epss_score >= 0.1)
            ):
                for uri in cpe_list:
                    if uri in cpe_seen:
                        continue
                    cpe_seen.add(uri)
                    parts = uri.split(":")
                    # cpe:2.3:part:vendor:product:version:...
                    part    = parts[2] if len(parts) > 2 else ""
                    vendor  = parts[3] if len(parts) > 3 else ""
                    product = parts[4] if len(parts) > 4 else ""
                    version = parts[5] if len(parts) > 5 else ""
                    try:
                        os_client.index(
                            index="nvd-cpe",
                            id=uri,
                            body={
                                "cpe_uri":    uri,
                                "part":       part,
                                "vendor":     vendor,
                                "product":    product,
                                "version":    version,
                                "title":      f"{vendor} {product} {version}".strip(),
                                "in_kev":     in_kev,
                                "source":     "cve_config",
                                "indexed_at": now_iso,
                            },
                        )
                        indexed_cpe += 1
                    except Exception as e:
                        logger.warning("Failed to index CPE %s: %s", uri, e)

    finish_run(run_id, indexed_cve)
    logger.info("NVD CVE %s complete: %d CVEs, %d CPEs indexed", mode, indexed_cve, indexed_cpe)


def run_full() -> None:
    run(full=True)


def run_delta() -> None:
    run(full=False)
