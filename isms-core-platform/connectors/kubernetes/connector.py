"""Kubernetes Dashboard connector for ISMS CORE v2.0.

Polls the Kubernetes Dashboard API and posts evidence to:
  a.8.6   — Capacity management          (node health, pod counts, resource efficiency)
  a.8.16  — Monitoring of activities     (pod crashes, Warning events)
  a.8.8   — Technical vulnerability mgmt (policy audit score)
  a.8.24  — Use of cryptography          (TLS certificate expiry)

Endpoints used:
  GET /api/v1/summary    — cluster health snapshot (always)
  GET /api/v1/efficiency — per-container CPU/memory vs limits (requires metrics-server)

Environment variables required:
  ISMS_API_URL         — e.g. http://isms-core-backend:8000
  ISMS_API_TOKEN       — connector bearer token from /admin/connectors/register
  DASHBOARD_URL        — Kubernetes Dashboard base URL, e.g. http://10.0.0.60
  DASHBOARD_TOKEN      — Kubernetes SA token (admin-user)
  POLL_INTERVAL        — seconds between syncs (default: 300 = 5 min)
  BATCH_SIZE           — items per API call (default: 100)
"""

import logging
import os
import sys
import time
from datetime import datetime, timezone

import requests

sys.path.insert(0, "/app/base")

from base import EvidenceItem, ISMSConnectorBase

logger = logging.getLogger(__name__)

DASHBOARD_TIMEOUT = 30


class KubernetesConnector(ISMSConnectorBase):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.poll_interval = int(os.environ.get("POLL_INTERVAL", "300"))
        cfg = self._load_config()
        self.dashboard_url = (cfg.get("dashboard_url") or os.environ.get("DASHBOARD_URL", "")).rstrip("/")
        self.dashboard_token = cfg.get("dashboard_token") or os.environ.get("DASHBOARD_TOKEN", "")
        if not self.dashboard_url:
            raise ValueError("DASHBOARD_URL is required")
        if not self.dashboard_token:
            raise ValueError("DASHBOARD_TOKEN is required")

    def _fetch_summary(self) -> dict:
        resp = requests.get(
            f"{self.dashboard_url}/api/v1/summary",
            headers={"Authorization": f"Bearer {self.dashboard_token}"},
            timeout=DASHBOARD_TIMEOUT,
        )
        resp.raise_for_status()
        return resp.json()

    def _fetch_efficiency(self) -> dict | None:
        """Fetch per-container resource efficiency from the metrics-server.

        Returns None (non-fatal) if the metrics-server is not installed or the
        endpoint is unavailable — the rest of the sync continues normally.
        """
        try:
            resp = requests.get(
                f"{self.dashboard_url}/api/v1/efficiency",
                headers={"Authorization": f"Bearer {self.dashboard_token}"},
                timeout=DASHBOARD_TIMEOUT,
            )
            resp.raise_for_status()
            return resp.json()
        except Exception as exc:
            logger.warning("Efficiency endpoint unavailable (metrics-server installed?): %s", exc)
            return None

    def fetch(self, since: str | None) -> list[dict]:
        data = self._fetch_summary()
        data["_type"] = "k8s_summary_bundle"
        data["efficiency"] = self._fetch_efficiency()
        return [data]

    def transform(self, item: dict) -> EvidenceItem | None:
        return None

    def _transform_bundle(self, bundle: dict) -> list[EvidenceItem]:
        items: list[EvidenceItem] = []
        fetched_at = bundle.get("fetchedAt", datetime.now(timezone.utc).isoformat())
        cluster_name = bundle.get("clusterName") or "kubernetes"

        nodes = bundle.get("nodes", {})
        pods = bundle.get("pods", {})
        events = bundle.get("events", {})
        policy = bundle.get("policyAudit", {})
        certs = bundle.get("certs", {})

        # ── A.8.6 — Capacity management (node + pod health) ──────────────────
        total_nodes = nodes.get("total", 0)
        ready_nodes = nodes.get("ready", 0)
        not_ready = nodes.get("notReady", 0)
        crash_pods = pods.get("crashLoopBackOff", 0)
        oom_pods = pods.get("oomKilled", 0)
        failed_pods = pods.get("failed", 0)
        pending_pods = pods.get("pending", 0)
        total_pods = pods.get("total", 0)
        running_pods = pods.get("running", 0)

        unhealthy_pods = crash_pods + oom_pods + failed_pods

        if not_ready > 0 or crash_pods > 0:
            capacity_status = "non-compliant"
        elif oom_pods > 0 or failed_pods > 0 or pending_pods > 2:
            capacity_status = "attention-required"
        else:
            capacity_status = "compliant"

        items.append(EvidenceItem(
            group_code="a.8.6",
            title=(
                f"{cluster_name}: {ready_nodes}/{total_nodes} nodes ready, "
                f"{running_pods}/{total_pods} pods running"
                + (f", {crash_pods} CrashLoopBackOff" if crash_pods else "")
                + (f", {oom_pods} OOMKilled" if oom_pods else "")
            ),
            source_ref=f"{cluster_name}-capacity",
            classification="asset",
            status=capacity_status,
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "cluster_name": cluster_name,
                "nodes": nodes,
                "pods": pods,
            },
        ))

        # ── A.8.6 — Resource efficiency (metrics-server, optional) ───────────
        efficiency = bundle.get("efficiency")
        if efficiency and isinstance(efficiency, dict):
            containers = efficiency.get("containers") or []
            no_limits       = [c for c in containers if c.get("verdict") == "no-limits"]
            under_prov      = [c for c in containers if c.get("verdict") == "under-provisioned"]
            over_prov       = [c for c in containers if c.get("verdict") == "over-provisioned"]
            ok_count        = sum(1 for c in containers if c.get("verdict") == "ok")
            no_data_count   = sum(1 for c in containers if c.get("verdict") == "no-data")

            if under_prov:
                eff_status = "non-compliant"
            elif no_limits:
                eff_status = "attention-required"
            else:
                eff_status = "compliant"

            title_parts = [f"{cluster_name}: {len(containers)} containers"]
            if under_prov:
                title_parts.append(f"{len(under_prov)} under-provisioned (>80% of limit)")
            if no_limits:
                title_parts.append(f"{len(no_limits)} with no resource limits")
            if over_prov:
                title_parts.append(f"{len(over_prov)} over-provisioned")
            if not under_prov and not no_limits:
                title_parts.append(f"{ok_count} OK")

            def _container_detail(c: dict) -> dict:
                return {
                    "namespace":       c.get("namespace"),
                    "pod":             c.get("pod"),
                    "container":       c.get("container"),
                    "cpu_actual_m":    c.get("cpuActual"),
                    "cpu_limit_m":     c.get("cpuLimit"),
                    "cpu_request_m":   c.get("cpuRequest"),
                    "mem_actual_b":    c.get("memActual"),
                    "mem_limit_b":     c.get("memLimit"),
                    "mem_request_b":   c.get("memRequest"),
                    "cpu_verdict":     c.get("cpuVerdict"),
                    "mem_verdict":     c.get("memVerdict"),
                }

            items.append(EvidenceItem(
                group_code="a.8.6",
                title=", ".join(title_parts),
                source_ref=f"{cluster_name}-resource-efficiency",
                classification="asset",
                status=eff_status,
                event_date=fetched_at,
                raw={
                    "fetched_at":         fetched_at,
                    "cluster_name":       cluster_name,
                    "total_containers":   len(containers),
                    "no_limits":          len(no_limits),
                    "under_provisioned":  len(under_prov),
                    "over_provisioned":   len(over_prov),
                    "ok":                 ok_count,
                    "no_data":            no_data_count,
                    "under_provisioned_detail": [_container_detail(c) for c in under_prov[:20]],
                    "no_limits_detail":   [_container_detail(c) for c in no_limits[:20]],
                },
            ))

        # ── A.8.16 — Monitoring (Warning events + crash detail) ───────────────
        warning_count = events.get("warningCount", 0)
        recent_warnings = events.get("recentWarnings", [])

        monitoring_status = (
            "non-compliant" if crash_pods > 0 or oom_pods > 0
            else "attention-required" if warning_count > 10
            else "compliant"
        )

        items.append(EvidenceItem(
            group_code="a.8.16",
            title=(
                f"{cluster_name}: {warning_count} Warning events"
                + (f", {unhealthy_pods} unhealthy pod(s)" if unhealthy_pods else "")
            ),
            source_ref=f"{cluster_name}-monitoring",
            classification="incident" if unhealthy_pods > 0 else "network",
            status=monitoring_status,
            event_date=fetched_at,
            raw={
                "fetched_at": fetched_at,
                "cluster_name": cluster_name,
                "warning_count": warning_count,
                "unhealthy_pods": {
                    "crash_loop": crash_pods,
                    "oom_killed": oom_pods,
                    "failed": failed_pods,
                },
                "recent_warnings": recent_warnings[:20],
            },
        ))

        # ── A.8.8 — Technical vulnerability management (policy audit) ─────────
        audit_score = policy.get("score")
        if audit_score is not None:
            danger_count = policy.get("totalDanger", 0)
            warn_count = policy.get("totalWarn", 0)

            audit_status = (
                "non-compliant" if audit_score < 50
                else "attention-required" if audit_score < 75
                else "compliant"
            )

            items.append(EvidenceItem(
                group_code="a.8.8",
                title=(
                    f"{cluster_name}: policy audit score {audit_score}/100 "
                    f"({danger_count} danger, {warn_count} warnings)"
                ),
                source_ref=f"{cluster_name}-policy-audit",
                classification="policy",
                status=audit_status,
                event_date=fetched_at,
                raw={
                    "fetched_at": fetched_at,
                    "cluster_name": cluster_name,
                    "score": audit_score,
                    "total_danger": danger_count,
                    "total_warn": warn_count,
                },
            ))

        # ── A.8.24 — Use of cryptography (TLS cert expiry) ────────────────────
        cert_total = certs.get("total", 0)
        if cert_total > 0:
            expired = certs.get("expiredCount", 0)
            critical = certs.get("criticalCount", 0)
            warning = certs.get("warningCount", 0)

            cert_status = (
                "non-compliant" if expired > 0
                else "attention-required" if critical > 0
                else "attention-required" if warning > 0
                else "compliant"
            )

            items.append(EvidenceItem(
                group_code="a.8.24",
                title=(
                    f"{cluster_name}: {cert_total} TLS certs"
                    + (f", {expired} expired" if expired else "")
                    + (f", {critical} expiring ≤7d" if critical else "")
                    + (f", {warning} expiring ≤30d" if warning else "")
                    + (" — all valid" if not expired and not critical and not warning else "")
                ),
                source_ref=f"{cluster_name}-certs",
                classification="policy",
                status=cert_status,
                event_date=fetched_at,
                raw={
                    "fetched_at": fetched_at,
                    "cluster_name": cluster_name,
                    "total": cert_total,
                    "expired": expired,
                    "critical": critical,
                    "warning": warning,
                },
            ))

        return items

    def run(self) -> None:
        logger.info("Kubernetes connector starting (dashboard=%s, poll_interval=%ds)",
                    self.dashboard_url, self.poll_interval)
        while True:
            start = time.monotonic()
            try:
                state = self._load_state()
                since = state.get("last_run")
                logger.info("Starting Kubernetes sync (last_run=%s)", since or "never")

                bundles = self.fetch(since)
                all_items: list[EvidenceItem] = []
                for bundle in bundles:
                    all_items.extend(self._transform_bundle(bundle))

                logger.info("Transformed %d evidence items", len(all_items))

                if all_items:
                    accepted, skipped, errors = self._post_all(all_items)
                    logger.info("Ingest: accepted=%d skipped=%d errors=%d", accepted, skipped, errors)

                self._save_state({"last_run": datetime.now(timezone.utc).isoformat()})

            except Exception as e:
                logger.error("Sync failed: %s", e, exc_info=True)

            elapsed = time.monotonic() - start
            sleep_for = max(0, self.poll_interval - elapsed)
            logger.info("Next sync in %.0fs", sleep_for)
            self._sleep_with_sync_check(sleep_for)


if __name__ == "__main__":
    KubernetesConnector().run()
