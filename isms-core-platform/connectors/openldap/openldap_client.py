"""OpenLDAP client using ldap3.

Handles:
  - Simple bind authentication via bind_dn / bind_pass
  - Paged SUBTREE search across base_dn
  - Endpoints / object classes used:
      inetOrgPerson / person  → A.5.3 (user roster)
      groupOfNames / posixGroup → A.5.15-16-18 (group inventory)
      computer                → A.8.9 (network devices, if present)

Config keys: server, port (default 389), bind_dn, bind_pass, base_dn, use_ssl (default False)
Env vars:    OPENLDAP_SERVER, OPENLDAP_PORT, OPENLDAP_BIND_DN, OPENLDAP_BIND_PASS, OPENLDAP_BASE_DN
"""

import logging
import os

import ldap3

logger = logging.getLogger(__name__)

PAGE_SIZE = 500


class OpenLDAPClient:
    """Thin ldap3 wrapper for generic OpenLDAP directories."""

    def __init__(self, **cfg) -> None:
        server_host = cfg.get("server") or os.environ.get("OPENLDAP_SERVER", "")
        if not server_host:
            raise ValueError("OpenLDAP server is required (config key 'server' or OPENLDAP_SERVER env var)")
        port = int(cfg.get("port") or os.environ.get("OPENLDAP_PORT", "389"))
        use_ssl_raw = cfg.get("use_ssl") or os.environ.get("OPENLDAP_USE_SSL", "false")
        use_ssl = str(use_ssl_raw).lower() in ("true", "1", "yes")
        self.bind_dn = cfg.get("bind_dn") or os.environ.get("OPENLDAP_BIND_DN", "")
        self.bind_pass = cfg.get("bind_pass") or os.environ.get("OPENLDAP_BIND_PASS", "")
        self.base_dn = cfg.get("base_dn") or os.environ.get("OPENLDAP_BASE_DN", "")

        if not self.bind_dn or not self.bind_pass:
            raise ValueError(
                "OpenLDAP bind credentials required (OPENLDAP_BIND_DN + OPENLDAP_BIND_PASS)"
            )
        if not self.base_dn:
            raise ValueError("OpenLDAP base DN required (OPENLDAP_BASE_DN)")

        self._server = ldap3.Server(
            server_host,
            port=port,
            use_ssl=use_ssl,
            get_info=ldap3.ALL,
            connect_timeout=10,
        )

    # ── Connection ────────────────────────────────────────────────────────────

    def _connect(self) -> ldap3.Connection:
        conn = ldap3.Connection(
            self._server,
            user=self.bind_dn,
            password=self.bind_pass,
            auto_bind=ldap3.AUTO_BIND_NO_TLS,
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
        """Paged SUBTREE search returning all results as plain dicts."""
        results: list[dict] = []
        entry_gen = conn.extend.standard.paged_search(
            search_base=self.base_dn,
            search_filter=search_filter,
            search_scope=ldap3.SUBTREE,
            attributes=attributes,
            paged_size=PAGE_SIZE,
            generator=True,
        )
        for entry in entry_gen:
            if entry.get("type") != "searchResEntry":
                continue
            results.append(entry.get("attributes", {}))
        return results

    # ── Public query methods ──────────────────────────────────────────────────

    def get_users(self) -> list[dict]:
        """All person entries: inetOrgPerson or person objectClass."""
        attrs = ["uid", "cn", "mail", "sn", "ou", "userPassword"]
        logger.info("Fetching users from OpenLDAP (base_dn=%s)...", self.base_dn)
        with self._connect() as conn:
            raw = self._search_all(
                conn,
                "(|(objectClass=inetOrgPerson)(objectClass=person))",
                attrs,
            )
        users = []
        for u in raw:
            users.append({
                "uid": str(u.get("uid", "")),
                "cn": str(u.get("cn", "")),
                "sn": str(u.get("sn", "")),
                "mail": str(u.get("mail", "")),
                "ou": str(u.get("ou", "")),
                # Presence of userPassword attribute indicates local password is set;
                # we never log the value itself.
                "has_password": bool(u.get("userPassword")),
            })
        logger.info("Fetched %d users", len(users))
        return users

    def get_groups(self) -> list[dict]:
        """All group entries: groupOfNames or posixGroup objectClass."""
        attrs = ["cn", "member", "memberUid", "description"]
        logger.info("Fetching groups from OpenLDAP (base_dn=%s)...", self.base_dn)
        with self._connect() as conn:
            raw = self._search_all(
                conn,
                "(|(objectClass=groupOfNames)(objectClass=posixGroup))",
                attrs,
            )
        groups = []
        for g in raw:
            # groupOfNames uses 'member' (DNs); posixGroup uses 'memberUid' (uids)
            members_dn = g.get("member") or []
            members_uid = g.get("memberUid") or []
            member_count = len(members_dn) + len(members_uid)
            groups.append({
                "cn": str(g.get("cn", "")),
                "description": str(g.get("description", "")),
                "member_count": member_count,
                "members_dn": [str(m) for m in members_dn][:50],
                "members_uid": [str(m) for m in members_uid][:50],
            })
        logger.info("Fetched %d groups", len(groups))
        return groups

    def get_computers(self) -> list[dict]:
        """Computer/device entries (objectClass=computer). Returns [] if not present."""
        attrs = ["cn", "description", "operatingSystem", "operatingSystemVersion"]
        logger.info("Fetching computer objects from OpenLDAP...")
        try:
            with self._connect() as conn:
                raw = self._search_all(conn, "(objectClass=computer)", attrs)
            computers = []
            for c in raw:
                computers.append({
                    "cn": str(c.get("cn", "")),
                    "description": str(c.get("description", "")),
                    "os": str(c.get("operatingSystem", "")),
                    "os_version": str(c.get("operatingSystemVersion", "")),
                })
            logger.info("Fetched %d computer objects", len(computers))
            return computers
        except Exception as e:
            logger.info("No computer objects found (normal for most OpenLDAP deployments): %s", e)
            return []
