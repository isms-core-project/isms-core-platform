FROM python:3.12-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt \
    && useradd -r -u 1000 -m -s /bin/false appuser

# Base shared library
COPY base /app/base

# ── Microsoft ──────────────────────────────────────────────────────────────────
COPY active-directory  /app/active-directory
COPY defender          /app/defender
COPY entra-id          /app/entra-id
COPY intune            /app/intune
COPY o365              /app/o365
COPY purview           /app/purview
COPY sentinel          /app/sentinel

# ── Identity & Access ──────────────────────────────────────────────────────────
COPY authentik         /app/authentik
COPY freeipa           /app/freeipa
COPY keycloak          /app/keycloak
COPY openldap          /app/openldap

# ── PAM ───────────────────────────────────────────────────────────────────────
COPY cyberark          /app/cyberark
COPY devolutions       /app/devolutions
COPY hashicorp-vault   /app/hashicorp-vault

# ── Network Security ───────────────────────────────────────────────────────────
COPY cisco-asa         /app/cisco-asa
COPY cisco-ise         /app/cisco-ise
COPY forti-analyzer    /app/forti-analyzer
COPY forti-manager     /app/forti-manager
COPY fortigate         /app/fortigate
COPY panw              /app/panw
COPY zscaler           /app/zscaler

# ── EDR / Endpoint ─────────────────────────────────────────────────────────────
COPY crowdstrike       /app/crowdstrike
COPY sentinelone       /app/sentinelone
COPY wazuh             /app/wazuh

# ── Vulnerability Management ───────────────────────────────────────────────────
COPY openvas           /app/openvas
COPY qualys            /app/qualys
COPY tenable-io        /app/tenable-io
COPY tenable-sc        /app/tenable-sc

# ── ITSM ───────────────────────────────────────────────────────────────────────
COPY jira              /app/jira
COPY servicenow        /app/servicenow

# ── Monitoring & SIEM ──────────────────────────────────────────────────────────
COPY graylog           /app/graylog
COPY prtg              /app/prtg
COPY zabbix            /app/zabbix

# ── Asset Management ───────────────────────────────────────────────────────────
COPY glpi              /app/glpi
COPY netbox            /app/netbox

# ── Cloud Posture ──────────────────────────────────────────────────────────────
COPY aws-security-hub  /app/aws-security-hub
COPY azure-cspm        /app/azure-cspm
COPY gcp-scc           /app/gcp-scc

# ── DevSecOps ──────────────────────────────────────────────────────────────────
COPY github            /app/github
COPY gitlab            /app/gitlab

# ── Threat Intelligence ────────────────────────────────────────────────────────
COPY openaev           /app/openaev
COPY opencti           /app/opencti
COPY threat-intel      /app/threat-intel

# ── Generic ────────────────────────────────────────────────────────────────────
COPY siem              /app/siem

# Orchestrator
COPY runner.py .

# Base on sys.path so all connector.py files can do: from base import ...
ENV PYTHONPATH=/app

RUN chown -R appuser:appuser /app
USER appuser

CMD ["python", "runner.py"]
