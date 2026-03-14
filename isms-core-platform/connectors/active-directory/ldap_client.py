"""LDAP client for Windows Active Directory (and compatible directories).

Supports:
  - Windows Server Active Directory (LDAP / LDAPS)
  - OpenLDAP (with minor schema differences)
  - FreeIPA (with Kerberos-compatible LDAP)

Environment variables:
  AD_SERVER       — LDAP server hostname or IP (e.g. dc01.corp.local)
  AD_PORT         — 389 (LDAP) or 636 (LDAPS). Default: 389
  AD_USE_SSL      — "true" to force LDAPS. Default: false
  AD_BIND_DN      — Bind DN (e.g. CN=svc_isms,OU=Service Accounts,DC=corp,DC=local)
  AD_BIND_PASS    — Bind account password
  AD_BASE_DN      — Search base (e.g. DC=corp,DC=local)
"""

import logging
import os
from datetime import datetime, timezone

import ldap3

logger = logging.getLogger(__name__)

# Active Directory timestamp epoch: 1 Jan 1601
_AD_EPOCH_DELTA = 11644473600  # seconds between 1601-01-01 and 1970-01-01

# Well-known privileged group names to flag in evidence
PRIVILEGED_GROUPS = {
    "Domain Admins",
    "Enterprise Admins",
    "Schema Admins",
    "Group Policy Creator Owners",
    "DNS Admins",
    "Account Operators",
    "Backup Operators",
    "Print Operators",
    "Server Operators",
    "Administrators",
}


def _ad_ts_to_iso(ad_ts: int | None) -> str | None:
    """Convert a Windows FILETIME (100-nanosecond intervals since 1601) to ISO 8601."""
    if not ad_ts or ad_ts in (0, 9223372036854775807):
        return None
    try:
        epoch_seconds = (int(ad_ts) / 10_000_000) - _AD_EPOCH_DELTA
        dt = datetime.fromtimestamp(epoch_seconds, tz=timezone.utc)
        return dt.isoformat()
    except Exception:
        return None


def _account_enabled(uac: int | None) -> bool:
    """Return True if the userAccountControl flag does NOT have ACCOUNTDISABLE (bit 1) set."""
    if uac is None:
        return True  # assume enabled if flag missing
    return not bool(int(uac) & 0x0002)


class LDAPClient:
    """Thin wrapper around ldap3 for AD/LDAP queries."""

    def __init__(self, **cfg) -> None:
        server_host = cfg.get('server') or os.environ["AD_SERVER"]
        port = int(cfg.get('port') or os.environ.get("AD_PORT", "389"))
        use_ssl = (cfg.get('use_ssl') or os.environ.get("AD_USE_SSL", "false")).lower() == "true"
        self.bind_dn = cfg.get('bind_dn') or os.environ["AD_BIND_DN"]
        self.bind_pass = cfg.get('bind_pass') or os.environ["AD_BIND_PASS"]
        self.base_dn = cfg.get('base_dn') or os.environ["AD_BASE_DN"]

        self._server = ldap3.Server(
            server_host,
            port=port,
            use_ssl=use_ssl,
            get_info=ldap3.ALL,
            connect_timeout=10,
        )

    def _connect(self) -> ldap3.Connection:
        conn = ldap3.Connection(
            self._server,
            user=self.bind_dn,
            password=self.bind_pass,
            auto_bind=ldap3.AUTO_BIND_TLS_BEFORE_BIND if not self._server.ssl else ldap3.AUTO_BIND_NO_TLS,
            read_only=True,
        )
        if not conn.bound:
            conn.bind()
        return conn

    def _search_all(
        self,
        conn: ldap3.Connection,
        search_filter: str,
        attributes: list[str],
    ) -> list[dict]:
        """Paged search returning all results as plain dicts."""
        results: list[dict] = []
        entry_gen = conn.extend.standard.paged_search(
            search_base=self.base_dn,
            search_filter=search_filter,
            search_scope=ldap3.SUBTREE,
            attributes=attributes,
            paged_size=500,
            generator=True,
        )
        for entry in entry_gen:
            if entry.get("type") != "searchResEntry":
                continue
            attrs = entry.get("attributes", {})
            results.append(attrs)
        return results

    # ── Public query methods ──────────────────────────────────────────────────

    def get_users(self) -> list[dict]:
        """Return all user objects with key attributes."""
        attrs = [
            "sAMAccountName",
            "displayName",
            "userPrincipalName",
            "mail",
            "department",
            "title",
            "userAccountControl",
            "whenCreated",
            "pwdLastSet",
            "lastLogonTimestamp",
            "distinguishedName",
            "memberOf",
        ]
        logger.info("Fetching users from AD...")
        with self._connect() as conn:
            raw = self._search_all(conn, "(objectClass=user)", attrs)

        users = []
        for u in raw:
            uac = u.get("userAccountControl")
            users.append({
                "sam": str(u.get("sAMAccountName", "")),
                "display_name": str(u.get("displayName", "")),
                "upn": str(u.get("userPrincipalName", "")),
                "mail": str(u.get("mail", "")),
                "department": str(u.get("department", "")),
                "title": str(u.get("title", "")),
                "account_enabled": _account_enabled(uac),
                "user_account_control": int(uac) if uac else None,
                "created": str(u.get("whenCreated", "")),
                "pwd_last_set": _ad_ts_to_iso(u.get("pwdLastSet")),
                "last_logon": _ad_ts_to_iso(u.get("lastLogonTimestamp")),
                "dn": str(u.get("distinguishedName", "")),
                "member_of": [str(g) for g in (u.get("memberOf") or [])],
            })
        logger.info("Fetched %d users", len(users))
        return users

    def get_groups(self) -> list[dict]:
        """Return all group objects."""
        attrs = [
            "sAMAccountName",
            "displayName",
            "description",
            "groupType",
            "distinguishedName",
            "member",
        ]
        logger.info("Fetching groups from AD...")
        with self._connect() as conn:
            raw = self._search_all(conn, "(objectClass=group)", attrs)

        groups = []
        for g in raw:
            gt = g.get("groupType")
            gt_int = int(gt) if gt else 0
            # groupType bit -2147483648 (0x80000000) = security group
            is_security = bool(gt_int & 0x80000000) if gt_int else False
            name = str(g.get("sAMAccountName", g.get("displayName", "")))
            groups.append({
                "name": name,
                "display_name": str(g.get("displayName", "")),
                "description": str(g.get("description", "")),
                "is_security": is_security,
                "group_type_raw": gt_int,
                "dn": str(g.get("distinguishedName", "")),
                "member_count": len(g.get("member") or []),
                "is_privileged": name in PRIVILEGED_GROUPS,
            })
        logger.info("Fetched %d groups", len(groups))
        return groups

    def get_privileged_group_members(self, groups: list[dict]) -> list[dict]:
        """For each privileged group, return its members (DN list → sam lookup)."""
        priv_groups = [g for g in groups if g["is_privileged"]]
        if not priv_groups:
            return []

        attrs = ["sAMAccountName", "distinguishedName", "displayName", "member"]
        assignments: list[dict] = []

        with self._connect() as conn:
            for pg in priv_groups:
                # Query the group by DN to get its member list
                conn.search(
                    search_base=pg["dn"],
                    search_filter="(objectClass=group)",
                    search_scope=ldap3.BASE,
                    attributes=attrs,
                )
                if not conn.entries:
                    continue
                entry = conn.entries[0]
                members = list(entry.member) if hasattr(entry, "member") else []
                for member_dn in members:
                    assignments.append({
                        "group_name": pg["name"],
                        "group_dn": pg["dn"],
                        "member_dn": str(member_dn),
                        "is_high_privilege": pg["name"] in {
                            "Domain Admins", "Enterprise Admins", "Schema Admins",
                            "Administrators",
                        },
                    })

        logger.info("Found %d privileged group memberships across %d groups",
                    len(assignments), len(priv_groups))
        return assignments

    def get_password_policy(self) -> dict | None:
        """Return the default domain password policy from the domain root."""
        attrs = [
            "minPwdLength",
            "pwdHistoryLength",
            "maxPwdAge",
            "minPwdAge",
            "lockoutThreshold",
            "lockoutDuration",
        ]
        try:
            with self._connect() as conn:
                conn.search(
                    search_base=self.base_dn,
                    search_filter="(objectClass=domainDNS)",
                    search_scope=ldap3.BASE,
                    attributes=attrs,
                )
                if not conn.entries:
                    return None
                entry = conn.entries[0]

                def _interval_to_minutes(val: int | None) -> int | None:
                    """Convert AD 100-ns negative interval to minutes."""
                    if val is None:
                        return None
                    try:
                        return abs(int(val)) // 10_000_000 // 60
                    except Exception:
                        return None

                return {
                    "min_pwd_length": int(entry.minPwdLength) if hasattr(entry, "minPwdLength") else None,
                    "pwd_history_length": int(entry.pwdHistoryLength) if hasattr(entry, "pwdHistoryLength") else None,
                    "max_pwd_age_minutes": _interval_to_minutes(entry.maxPwdAge.value if hasattr(entry, "maxPwdAge") else None),
                    "min_pwd_age_minutes": _interval_to_minutes(entry.minPwdAge.value if hasattr(entry, "minPwdAge") else None),
                    "lockout_threshold": int(entry.lockoutThreshold) if hasattr(entry, "lockoutThreshold") else None,
                    "lockout_duration_minutes": _interval_to_minutes(entry.lockoutDuration.value if hasattr(entry, "lockoutDuration") else None),
                }
        except Exception as e:
            logger.warning("Could not retrieve password policy: %s", e)
            return None
