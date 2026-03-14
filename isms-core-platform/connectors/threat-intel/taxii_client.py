"""Generic threat intelligence client supporting multiple feed types.

Feed types:
  taxii21  — TAXII 2.1 collections (STIX 2.1 objects via standard REST endpoints)
  misp     — MISP instance REST API (attribute restSearch)
  json     — Generic JSON array of indicator objects (custom/vendor feeds)

Normalised output format per indicator:
  {
    "type":         str,   # e.g. "ip-addr", "domain-name", "file", "url"
    "value":        str,   # the IOC value
    "threat_type":  str,   # malware, APT, phishing, ransomware, etc.
    "confidence":   int,   # 0–100 where available
    "valid_from":   str,   # ISO 8601 or ""
    "valid_until":  str,   # ISO 8601 or ""
    "source":       str,   # feed name / collection title
    "_raw":         dict,  # original object
  }

Config keys / env vars:
  feed_url       / THREAT_INTEL_FEED_URL      — feed endpoint URL (required)
  auth_type      / THREAT_INTEL_AUTH_TYPE     — api_key | basic (default: api_key)
  api_key        / THREAT_INTEL_API_KEY       — API key for api_key mode
  username       / THREAT_INTEL_USERNAME      — for basic auth
  password       / THREAT_INTEL_PASSWORD      — for basic auth
  feed_type      / THREAT_INTEL_FEED_TYPE     — taxii21 | misp | json (default: json)
  collection_id  / THREAT_INTEL_COLLECTION    — TAXII 2.1 collection ID
  verify_ssl     / THREAT_INTEL_VERIFY_SSL    — true/false (default: true)
"""

import logging
import os

import requests
from requests.auth import HTTPBasicAuth

logger = logging.getLogger(__name__)

_DEFAULT_TIMEOUT = 30

# STIX 2.1 type → normalised short type
_STIX_TYPE_MAP = {
    "ipv4-addr": "ip-addr",
    "ipv6-addr": "ip-addr",
    "domain-name": "domain-name",
    "url": "url",
    "file": "file",
    "email-addr": "email-addr",
    "autonomous-system": "asn",
    "network-traffic": "network",
    "vulnerability": "cve",
}


def _coerce_bool(val, default: bool = True) -> bool:
    if isinstance(val, bool):
        return val
    if isinstance(val, str):
        return val.lower() not in ("false", "0", "no")
    return default


class ThreatIntelClient:
    def __init__(
        self,
        feed_url: str = "",
        auth_type: str = "api_key",
        api_key: str = "",
        username: str = "",
        password: str = "",
        feed_type: str = "json",
        collection_id: str = "",
        verify_ssl: bool = True,
        **kwargs,
    ) -> None:
        self.feed_url = (
            feed_url or os.environ.get("THREAT_INTEL_FEED_URL", "")
        ).rstrip("/")
        self.auth_type = (
            auth_type or os.environ.get("THREAT_INTEL_AUTH_TYPE", "api_key")
        ).lower()
        self.api_key = api_key or os.environ.get("THREAT_INTEL_API_KEY", "")
        self.username = username or os.environ.get("THREAT_INTEL_USERNAME", "")
        self.password = password or os.environ.get("THREAT_INTEL_PASSWORD", "")
        self.feed_type = (
            feed_type or os.environ.get("THREAT_INTEL_FEED_TYPE", "json")
        ).lower()
        self.collection_id = collection_id or os.environ.get("THREAT_INTEL_COLLECTION", "")
        self.verify_ssl = _coerce_bool(
            os.environ.get("THREAT_INTEL_VERIFY_SSL", None) or verify_ssl
        )

        if not self.feed_url:
            raise ValueError(
                "Threat intel feed URL is required "
                "(config key 'feed_url' or THREAT_INTEL_FEED_URL env var)"
            )

        if not self.verify_ssl:
            import urllib3
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
            logger.warning("SSL verification disabled for ThreatIntelClient")

    # ── Auth helpers ──────────────────────────────────────────────────────────

    def _headers(self, accept: str = "application/json") -> dict:
        h = {"Accept": accept}
        if self.auth_type == "api_key" and self.api_key:
            h["Authorization"] = f"Bearer {self.api_key}"
        elif self.auth_type == "api_key":
            # Some feeds use a named header (e.g. MISP uses Authorization: Bearer)
            pass
        return h

    def _auth(self) -> HTTPBasicAuth | None:
        if self.auth_type == "basic":
            return HTTPBasicAuth(self.username, self.password)
        return None

    def _get(self, url: str, params: dict | None = None, accept: str = "application/json") -> requests.Response:
        resp = requests.get(
            url,
            headers=self._headers(accept=accept),
            auth=self._auth(),
            params=params or {},
            verify=self.verify_ssl,
            timeout=_DEFAULT_TIMEOUT,
        )
        resp.raise_for_status()
        return resp

    def _post(self, url: str, payload: dict, accept: str = "application/json") -> requests.Response:
        resp = requests.post(
            url,
            headers={**self._headers(accept=accept), "Content-Type": "application/json"},
            auth=self._auth(),
            json=payload,
            verify=self.verify_ssl,
            timeout=_DEFAULT_TIMEOUT,
        )
        resp.raise_for_status()
        return resp

    # ── Normalisation ─────────────────────────────────────────────────────────

    def _normalise_stix(self, obj: dict) -> dict | None:
        """Convert a STIX 2.1 SDO/SCO to the normalised indicator format.
        Only handles indicator objects — skips other STIX types.
        """
        object_type = obj.get("type", "")
        if object_type == "indicator":
            # STIX indicator — pattern contains the IOC
            pattern = obj.get("pattern", "")
            ioc_type = "unknown"
            ioc_value = pattern  # raw pattern as value
            # Try to extract type from pattern like [ipv4-addr:value = '...']
            if "ipv4-addr" in pattern:
                ioc_type = "ip-addr"
            elif "ipv6-addr" in pattern:
                ioc_type = "ip-addr"
            elif "domain-name" in pattern:
                ioc_type = "domain-name"
            elif "url:value" in pattern:
                ioc_type = "url"
            elif "file:hashes" in pattern or "MD5" in pattern or "SHA" in pattern:
                ioc_type = "file"
            elif "email-addr" in pattern:
                ioc_type = "email-addr"
            return {
                "type": ioc_type,
                "value": ioc_value,
                "threat_type": ", ".join(obj.get("indicator_types", [])),
                "confidence": obj.get("confidence", 0),
                "valid_from": obj.get("valid_from", ""),
                "valid_until": obj.get("valid_until", ""),
                "source": obj.get("created_by_ref", ""),
                "_raw": obj,
            }
        elif object_type in _STIX_TYPE_MAP:
            # Observable — treat as IOC
            ioc_type = _STIX_TYPE_MAP[object_type]
            ioc_value = (
                obj.get("value")
                or obj.get("name")
                or obj.get("number", "")
            )
            return {
                "type": ioc_type,
                "value": str(ioc_value),
                "threat_type": "",
                "confidence": obj.get("confidence", 0),
                "valid_from": obj.get("created", ""),
                "valid_until": obj.get("valid_until", ""),
                "source": obj.get("created_by_ref", ""),
                "_raw": obj,
            }
        return None

    def _normalise_misp(self, attr: dict) -> dict:
        """Convert a MISP attribute to the normalised indicator format."""
        return {
            "type": attr.get("type", "unknown"),
            "value": attr.get("value", ""),
            "threat_type": attr.get("category", ""),
            "confidence": int(float(attr.get("confidence", 0) or 0)),
            "valid_from": attr.get("timestamp", ""),
            "valid_until": "",
            "source": "misp",
            "_raw": attr,
        }

    def _normalise_json(self, item: dict) -> dict:
        """Pass-through normalisation for generic JSON feed items.
        Attempts to map common field names to the standard format.
        """
        ioc_type = (
            item.get("type")
            or item.get("indicator_type")
            or item.get("ioc_type")
            or item.get("category")
            or "unknown"
        )
        ioc_value = (
            item.get("value")
            or item.get("indicator")
            or item.get("ioc")
            or item.get("observable")
            or ""
        )
        threat_type = (
            item.get("threat_type")
            or item.get("tags")
            or item.get("malware_family")
            or ""
        )
        if isinstance(threat_type, list):
            threat_type = ", ".join(str(t) for t in threat_type)
        valid_from = (
            item.get("valid_from")
            or item.get("created")
            or item.get("created_at")
            or item.get("date")
            or item.get("first_seen")
            or ""
        )
        return {
            "type": str(ioc_type).lower(),
            "value": str(ioc_value),
            "threat_type": str(threat_type),
            "confidence": int(float(item.get("confidence", 0) or 0)),
            "valid_from": str(valid_from),
            "valid_until": str(item.get("valid_until") or item.get("expiration") or ""),
            "source": str(item.get("source") or item.get("feed") or ""),
            "_raw": item,
        }

    # ── TAXII 2.1 ─────────────────────────────────────────────────────────────

    def _taxii_get_collections(self) -> list[dict]:
        """List available TAXII 2.1 collections."""
        resp = self._get(
            f"{self.feed_url}/taxii2/",
            accept="application/taxii+json;version=2.1",
        )
        data = resp.json()
        return data.get("collections", [])

    def _taxii_get_objects(self, collection_id: str, limit: int) -> list[dict]:
        """Fetch objects from a TAXII 2.1 collection."""
        url = f"{self.feed_url}/taxii2/collections/{collection_id}/objects/"
        resp = self._get(
            url,
            params={"limit": limit},
            accept="application/taxii+json;version=2.1",
        )
        data = resp.json()
        return data.get("objects", [])

    # ── Public method ──────────────────────────────────────────────────────────

    def get_indicators(self, limit: int = 500) -> list[dict]:
        """Fetch threat indicators and return a normalised list.

        For taxii21: discovers collection if collection_id not set, fetches objects
        For misp:    uses /attributes/restSearch.json
        For json:    GET feed_url expecting a JSON array
        """
        normalised: list[dict] = []

        if self.feed_type == "taxii21":
            coll_id = self.collection_id
            if not coll_id:
                logger.info("No collection_id set — discovering TAXII 2.1 collections...")
                try:
                    collections = self._taxii_get_collections()
                    if collections:
                        coll_id = collections[0].get("id", "")
                        logger.info(
                            "Using first available collection: %s (%s)",
                            collections[0].get("title", ""),
                            coll_id,
                        )
                except Exception as e:
                    logger.error("TAXII collection discovery failed: %s", e)
                    return []

            if not coll_id:
                logger.error("TAXII 2.1: no collection_id available")
                return []

            logger.info("Fetching TAXII 2.1 objects (collection=%s, limit=%d) ...", coll_id, limit)
            try:
                objects = self._taxii_get_objects(coll_id, limit)
                logger.info("Fetched %d STIX objects", len(objects))
                for obj in objects:
                    norm = self._normalise_stix(obj)
                    if norm is not None:
                        normalised.append(norm)
            except Exception as e:
                logger.error("TAXII 2.1 object fetch failed: %s", e)

        elif self.feed_type == "misp":
            logger.info("Fetching MISP attributes (limit=%d) ...", limit)
            try:
                resp = self._post(
                    f"{self.feed_url}/attributes/restSearch.json",
                    payload={"limit": limit, "page": 1, "returnFormat": "json"},
                )
                data = resp.json()
                attributes = (
                    data.get("response", {}).get("Attribute", [])
                    or data.get("Attribute", [])
                    or (data if isinstance(data, list) else [])
                )
                logger.info("Fetched %d MISP attributes", len(attributes))
                for attr in attributes:
                    normalised.append(self._normalise_misp(attr))
            except Exception as e:
                logger.error("MISP attribute fetch failed: %s", e)

        else:
            # Generic JSON array
            logger.info("Fetching generic JSON threat feed (limit=%d) ...", limit)
            try:
                resp = self._get(self.feed_url, params={"limit": limit})
                data = resp.json()
                if isinstance(data, list):
                    items = data[:limit]
                else:
                    items = (
                        data.get("indicators")
                        or data.get("data")
                        or data.get("results")
                        or data.get("iocs")
                        or []
                    )
                    items = items[:limit]
                logger.info("Fetched %d indicators from JSON feed", len(items))
                for item in items:
                    normalised.append(self._normalise_json(item))
            except Exception as e:
                logger.error("JSON feed fetch failed: %s", e)

        logger.info("Normalised %d indicators total", len(normalised))
        return normalised

    def get_summary(self) -> dict:
        """Return {total_count, by_type, last_updated} — best effort from feed metadata.

        Tries common metadata endpoints. Falls back to {} if unavailable.
        The connector always computes its own summary from the indicators list,
        so this is supplemental context only.
        """
        meta_paths = ["/api/summary", "/api/metadata", "/api/stats", "/taxii2/"]
        for path in meta_paths:
            try:
                resp = self._get(
                    f"{self.feed_url}{path}",
                    accept="application/json",
                )
                data = resp.json()
                if isinstance(data, dict):
                    logger.debug("Feed summary fetched from %s", path)
                    return data
            except Exception:
                continue
        return {}
