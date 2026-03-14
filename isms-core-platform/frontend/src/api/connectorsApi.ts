import { client } from './client'

export interface ConnectorRead {
  id: string
  name: string
  source_system: string
  status: string
  last_run: string | null
  last_item_count: number | null
  sync_requested_at: string | null
  last_error: string | null
  last_error_at: string | null
  evidence_count: number
  retention_days: number | null
  created_at: string
}

export interface ArchiveStats {
  connector_id: string
  name: string
  source_system: string
  retention_days: number
  active: number
  archived: number
}

export interface ConnectorRegistered extends ConnectorRead {
  api_token: string
}

export interface ConnectorRegisterPayload {
  name: string
  source_system: string
}

export interface ConnectorEvidenceRead {
  id: string
  connector_id: string
  control_group_id: string
  group_code: string | null
  source_ref: string | null
  source_url: string | null
  title: string
  classification: string | null
  status: string | null
  event_date: string | null
  created_at: string
  raw: Record<string, unknown> | null
}

// ── Config schema ─────────────────────────────────────────────────────────────

export interface ConfigField {
  key: string
  label: string
  type: 'text' | 'password' | 'checkbox'
  placeholder?: string
  required?: boolean
  helperText?: string
}

/**
 * Per-system config field definitions.
 * Keys must match what Python client uses in cfg.get('key').
 * helperText shows required API permissions / setup instructions.
 */
export const CONNECTOR_CONFIG_SCHEMA: Record<string, ConfigField[]> = {
  // ── Microsoft ───────────────────────────────────────────────────────────────
  entra_id: [
    { key: 'tenant_id',     label: 'Tenant ID',          type: 'text',     required: true,  placeholder: 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx' },
    { key: 'client_id',     label: 'App (Client) ID',    type: 'text',     required: true,  placeholder: 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx' },
    { key: 'client_secret', label: 'Client Secret',      type: 'password', required: true,  helperText: 'App Registration → Certificates & secrets → New client secret. Required permissions: User.Read.All, GroupMember.Read.All, RoleManagement.Read.Directory, UserAuthenticationMethod.Read.All' },
  ],
  defender: [
    { key: 'tenant_id',     label: 'Tenant ID',          type: 'text',     required: true },
    { key: 'client_id',     label: 'App (Client) ID',    type: 'text',     required: true },
    { key: 'client_secret', label: 'Client Secret',      type: 'password', required: true,  helperText: 'App Registration permissions required (Application): Machine.Read.All, Vulnerability.Read.All, Alert.Read.All' },
  ],
  sentinel: [
    { key: 'tenant_id',       label: 'Tenant ID',          type: 'text',     required: true },
    { key: 'client_id',       label: 'App (Client) ID',    type: 'text',     required: true },
    { key: 'client_secret',   label: 'Client Secret',      type: 'password', required: true,  helperText: 'Required RBAC roles on the Log Analytics workspace: Microsoft Sentinel Reader + Log Analytics Reader + Monitoring Reader. Assign to the App Registration service principal via IAM → Add role assignment.' },
    { key: 'subscription_id', label: 'Subscription ID',    type: 'text',     required: true },
    { key: 'resource_group',  label: 'Resource Group',     type: 'text',     required: true },
    { key: 'workspace_name',  label: 'Workspace Name',     type: 'text',     required: true },
  ],
  intune: [
    { key: 'tenant_id',     label: 'Tenant ID',          type: 'text',     required: true },
    { key: 'client_id',     label: 'App (Client) ID',    type: 'text',     required: true },
    { key: 'client_secret', label: 'Client Secret',      type: 'password', required: true,  helperText: 'App Registration permissions (Application): DeviceManagementManagedDevices.Read.All, DeviceManagementConfiguration.Read.All' },
  ],
  purview: [
    { key: 'tenant_id',       label: 'Tenant ID',            type: 'text',     required: true },
    { key: 'client_id',       label: 'App (Client) ID',      type: 'text',     required: true },
    { key: 'client_secret',   label: 'Client Secret',        type: 'password', required: true,  helperText: 'App Registration → API permissions → Microsoft Graph → Application: InformationProtectionPolicy.Read.All (sensitivity labels) + RecordsManagement.Read.All (retention labels) + SecurityEvents.Read.All (DLP alerts). Grant admin consent after adding.' },
    { key: 'purview_account', label: 'Purview Account Name', type: 'text',     helperText: 'Optional — enables data catalogue evidence (Data Map / Collections)' },
  ],
  // ── Identity & Access ───────────────────────────────────────────────────────
  active_directory: [
    { key: 'server',    label: 'LDAP Server (hostname or IP)', type: 'text',     required: true, placeholder: 'dc01.corp.local' },
    { key: 'port',      label: 'Port',                         type: 'text',     placeholder: '389' },
    { key: 'bind_dn',   label: 'Bind DN',                      type: 'text',     required: true, placeholder: 'CN=svc-isms,OU=Service Accounts,DC=corp,DC=local' },
    { key: 'bind_pass', label: 'Bind Password',                type: 'password', required: true, helperText: 'Service account needs: Read access to users, groups, computers (domain Users/Domain Computers containers). No admin rights needed.' },
    { key: 'base_dn',   label: 'Base DN',                      type: 'text',     required: true, placeholder: 'DC=corp,DC=local' },
    { key: 'use_ssl',   label: 'Use LDAPS (port 636)',         type: 'checkbox' },
  ],
  openldap: [
    { key: 'server',    label: 'LDAP Server (hostname or IP)', type: 'text',     required: true, placeholder: 'ldap.corp.local' },
    { key: 'port',      label: 'Port',                         type: 'text',     placeholder: '389' },
    { key: 'bind_dn',   label: 'Bind DN',                      type: 'text',     required: true, placeholder: 'cn=isms-reader,dc=corp,dc=local' },
    { key: 'bind_pass', label: 'Bind Password',                type: 'password', required: true, helperText: 'Minimum: read access to inetOrgPerson, groupOfNames/posixGroup objects. No write access required.' },
    { key: 'base_dn',   label: 'Base DN',                      type: 'text',     required: true, placeholder: 'dc=corp,dc=local' },
    { key: 'use_ssl',   label: 'Use LDAPS (port 636)',         type: 'checkbox' },
  ],
  freeipa: [
    { key: 'url',        label: 'FreeIPA URL',    type: 'text',     required: true,  placeholder: 'https://ipa.corp.local' },
    { key: 'username',   label: 'Username',       type: 'text',     required: true,  placeholder: 'isms-reader' },
    { key: 'password',   label: 'Password',       type: 'password', required: true,  helperText: 'Create a dedicated service account with user_find, group_find, host_find, sudorule_find permissions. Admin → Users → Add User, then assign to ipausers group.' },
    { key: 'verify_ssl', label: 'Verify SSL',     type: 'checkbox' },
  ],
  authentik: [
    { key: 'url',        label: 'Authentik URL',  type: 'text',     required: true,  placeholder: 'https://authentik.corp.local' },
    { key: 'api_token',  label: 'API Token',      type: 'password', required: true,  helperText: 'Admin → Directory → Tokens → Create token (Intent: API). Token user needs: can_access_admin_interface + Read permissions on users, groups, applications, flows.' },
  ],
  keycloak: [
    { key: 'url',        label: 'Keycloak URL',   type: 'text',     required: true,  placeholder: 'https://keycloak.corp.local' },
    { key: 'username',   label: 'Admin Username', type: 'text',     required: true },
    { key: 'password',   label: 'Admin Password', type: 'password', required: true,  helperText: 'Service account needs realm-management client roles: view-users, view-clients, view-realm. Or use a dedicated realm admin account.' },
    { key: 'realm',      label: 'Realm',          type: 'text',     placeholder: 'master', helperText: 'Target realm to query (default: master)' },
  ],
  // ── PAM ──────────────────────────────────────────────────────────────────────
  cyberark: [
    { key: 'url',        label: 'PVWA URL (with https)',       type: 'text',     required: true,  placeholder: 'https://cyberark.corp.local' },
    { key: 'username',   label: 'Username',                   type: 'text',     required: true },
    { key: 'password',   label: 'Password',                   type: 'password', required: true,  helperText: 'Service account permissions needed: List Safes, View Safe Details, List Accounts, View Account Details, List Users. Use CyberArk built-in auth.' },
    { key: 'verify_ssl', label: 'Verify SSL',                 type: 'checkbox' },
  ],
  devolutions: [
    { key: 'dvls_url',    label: 'DVLS URL',          type: 'text',     required: true,  placeholder: 'https://10.0.0.71:5000',  helperText: 'Devolutions Server base URL. For the factory K8s deployment, this is https://10.0.0.71:5000 (MetalLB fixed IP, namespace: dvls-beta).' },
    { key: 'app_key',     label: 'Application Key',   type: 'text',     required: false, placeholder: 'xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx', helperText: 'Preferred: create an Application User in DVLS Administration > Application Users. Required permissions: Users (Read), Groups (Read), Connections (Read), Logs (Read), Sessions (Read).' },
    { key: 'app_secret',  label: 'Application Secret',type: 'password', required: false, helperText: 'Application User secret. Required permissions: Users (Read), Groups (Read), Connections (Read), Logs (Read), Sessions (Read).' },
    { key: 'username',    label: 'Admin Username',     type: 'text',     required: false, helperText: 'Fallback: admin username (used only if Application User not configured). Requires Administrator role.' },
    { key: 'password',    label: 'Admin Password',     type: 'password', required: false },
    { key: 'verify_ssl',  label: 'Verify SSL',         type: 'checkbox', helperText: 'Disable for internal deployments using self-signed certificates (default for K8s deployment).' },
  ],
  hashicorp_vault: [
    { key: 'url',        label: 'Vault URL',      type: 'text',     required: true,  placeholder: 'https://vault.corp.local:8200' },
    { key: 'token',      label: 'Vault Token',    type: 'password', required: true,  helperText: 'Create a dedicated policy: sys/policies/acl/* (read,list), sys/mounts (read), sys/auth (read), sys/audit (read,list), sys/leases/lookup/* (list). Token should have renewal disabled and short TTL.' },
    { key: 'namespace',  label: 'Namespace',      type: 'text',     helperText: 'Vault Enterprise only — e.g. admin/team-a' },
  ],
  // ── Network Security ────────────────────────────────────────────────────────
  fortigate: [
    { key: 'host',       label: 'FortiGate Host (IP or hostname)', type: 'text',     required: true, placeholder: '192.168.1.1' },
    { key: 'api_token',  label: 'REST API Token',                  type: 'password', required: true, helperText: 'System → Administrators → Create REST API Admin. Profile: Read-Only. Trusted Hosts: restrict to ISMS CORE IP.' },
    { key: 'vdom',       label: 'VDOM',                            type: 'text',     placeholder: 'root' },
    { key: 'verify_ssl', label: 'Verify SSL',                      type: 'checkbox' },
  ],
  forti_analyzer: [
    { key: 'host',       label: 'FortiAnalyzer Host (IP or hostname)', type: 'text',     required: true, placeholder: 'faz.corp.local' },
    { key: 'username',   label: 'Username',                           type: 'text',     required: true },
    { key: 'password',   label: 'Password',                           type: 'password', required: true, helperText: 'Create a read-only admin in System → Administrators. Profile: Standard_User with Log & Report: Read, Device Manager: Read.' },
    { key: 'verify_ssl', label: 'Verify SSL',                         type: 'checkbox' },
  ],
  forti_manager: [
    { key: 'host',       label: 'FortiManager Host (IP or hostname)', type: 'text',     required: true, placeholder: 'fmg.corp.local' },
    { key: 'username',   label: 'Username',                          type: 'text',     required: true },
    { key: 'password',   label: 'Password',                          type: 'password', required: true, helperText: 'Create a read-only admin in System → Administrators. Profile: Standard_User with Package access: Read, Device Manager: Read, ADOM access configured.' },
    { key: 'adom',       label: 'ADOM',                              type: 'text',     placeholder: 'root', helperText: 'Administrative Domain to query (default: root)' },
    { key: 'verify_ssl', label: 'Verify SSL',                        type: 'checkbox' },
  ],
  panw: [
    { key: 'host',          label: 'PAN-OS Host (IP or hostname)', type: 'text',     required: true, placeholder: '192.168.1.1' },
    { key: 'api_key',       label: 'API Key',                      type: 'password', required: true, helperText: 'Generate via: GET /api/?type=keygen&user=<user>&password=<pass>. Account needs: Operational Commands + Log Viewer read access.' },
    { key: 'vsys',          label: 'Virtual System',               type: 'text',     placeholder: 'vsys1' },
    { key: 'panorama',      label: 'Panorama managed',             type: 'checkbox' },
    { key: 'target_device', label: 'Target Device (Panorama serial)', type: 'text' },
    { key: 'verify_ssl',    label: 'Verify SSL',                   type: 'checkbox' },
  ],
  cisco_asa: [
    { key: 'host',       label: 'ASA Host (IP or hostname)', type: 'text',     required: true },
    { key: 'username',   label: 'Username',                  type: 'text',     required: true },
    { key: 'password',   label: 'Password',                  type: 'password', required: true, helperText: 'Service account privilege level: 5 (show commands). REST API must be enabled: http server enable. Some ASA versions use port 55443.' },
    { key: 'port',       label: 'REST API Port',             type: 'text',     placeholder: '443' },
    { key: 'verify_ssl', label: 'Verify SSL',                type: 'checkbox' },
  ],
  cisco_ise: [
    { key: 'host',       label: 'ISE Host (IP or hostname)', type: 'text',     required: true },
    { key: 'username',   label: 'Username (ERS Admin role)', type: 'text',     required: true },
    { key: 'password',   label: 'Password',                  type: 'password', required: true, helperText: 'Account requires ERS Admin or ERS Operator role. Enable ERS: Administration → Settings → API → Enable ERS for Read.' },
    { key: 'verify_ssl', label: 'Verify SSL',                type: 'checkbox' },
  ],
  zscaler: [
    { key: 'cloud_name',  label: 'Cloud Name',     type: 'text',     required: true,  placeholder: 'zscalerthree  (e.g. from zsapi.zscalerthree.net)' },
    { key: 'username',    label: 'Username',       type: 'text',     required: true },
    { key: 'password',    label: 'Password',       type: 'password', required: true },
    { key: 'api_key',     label: 'API Key',        type: 'password', required: true,  helperText: 'Admin Portal → Administration → API Key Management. Account requires Read-only Admin role or custom role with: Users & Groups Read, URL Filtering Read, Security Read.' },
  ],
  // ── EDR / Endpoint ──────────────────────────────────────────────────────────
  crowdstrike: [
    { key: 'client_id',     label: 'OAuth2 Client ID',     type: 'text',     required: true },
    { key: 'client_secret', label: 'OAuth2 Client Secret', type: 'password', required: true, helperText: 'Support App → API Clients → Add Client. Scopes required: Devices:Read, Detections:Read, Prevention Policies:Read.' },
    { key: 'base_url',      label: 'API Base URL',         type: 'text',     placeholder: 'https://api.crowdstrike.com', helperText: 'Change only for GovCloud: https://api.laggar.gcw.crowdstrike.com' },
  ],
  sentinelone: [
    { key: 'url',       label: 'SentinelOne URL',  type: 'text',     required: true,  placeholder: 'https://yourcompany.sentinelone.net' },
    { key: 'api_token', label: 'API Token',        type: 'password', required: true,  helperText: 'Settings → Users → Service Users → Generate API Token. Role required: Read-Only (Viewer) at Site or Account level.' },
    { key: 'site_id',   label: 'Site ID',          type: 'text',     helperText: 'Optional — filter to specific site. Leave blank for all sites.' },
  ],
  wazuh: [
    { key: 'url',        label: 'Wazuh Manager URL (with port)', type: 'text',     required: true,  placeholder: 'https://wazuh-manager.corp.local:55000' },
    { key: 'username',   label: 'API Username',                  type: 'text',     required: true },
    { key: 'password',   label: 'API Password',                  type: 'password', required: true,  helperText: 'Create a read-only role in Wazuh Dashboard: Security → Roles → Create. Permissions: agents:read, alerts:read, vulnerability_detector:read, manager:read.' },
    { key: 'verify_ssl', label: 'Verify SSL',                    type: 'checkbox' },
  ],
  // ── Vulnerability Management ─────────────────────────────────────────────────
  tenable_sc: [
    { key: 'host',       label: 'Tenable.sc Host (IP or hostname)', type: 'text',     required: true },
    { key: 'access_key', label: 'Access Key',   type: 'text',     helperText: 'Preferred: System → Users → [user] → API Keys (Tenable.sc 5.13+). No special permissions beyond the user account role.' },
    { key: 'secret_key', label: 'Secret Key',   type: 'password', helperText: 'Preferred: API key pair' },
    { key: 'username',   label: 'Username',     type: 'text',     helperText: 'Fallback: session token auth' },
    { key: 'password',   label: 'Password',     type: 'password', helperText: 'Fallback: session token auth' },
    { key: 'verify_ssl', label: 'Verify SSL',   type: 'checkbox' },
  ],
  tenable_io: [
    { key: 'access_key', label: 'Access Key',   type: 'text',     required: true,  helperText: 'Settings → My Account → API Keys → Generate. Account needs: Basic Access (Scan Operator or higher) to view assets and vulnerabilities.' },
    { key: 'secret_key', label: 'Secret Key',   type: 'password', required: true },
  ],
  qualys: [
    { key: 'username',   label: 'Username',      type: 'text',     required: true },
    { key: 'password',   label: 'Password',      type: 'password', required: true,  helperText: 'Service account requires: VM module access (Asset, Vulnerability) and PC module access (Policy Compliance). API access must be enabled for the account.' },
    { key: 'platform',   label: 'Platform URL',  type: 'text',     placeholder: 'https://qualysapi.qualys.com', helperText: 'Your Qualys platform URL (US1: qualysapi.qualys.com, EU: qualysapi.qualys.eu, etc.)' },
  ],
  openvas: [
    { key: 'host',       label: 'Greenbone / OpenVAS Host',         type: 'text',     required: true, placeholder: 'greenbone.corp.local' },
    { key: 'username',   label: 'Username',                         type: 'text',     required: true },
    { key: 'password',   label: 'Password',                         type: 'password', required: true, helperText: 'Account must have: Read access to scans, results, and tasks. Use a dedicated GMP service account.' },
    { key: 'port',       label: 'GMP Port',                         type: 'text',     placeholder: '9390' },
    { key: 'verify_ssl', label: 'Verify SSL',                       type: 'checkbox' },
  ],
  // ── ITSM ────────────────────────────────────────────────────────────────────
  servicenow: [
    { key: 'instance', label: 'Instance Name',              type: 'text',     required: true, placeholder: 'mycompany  (→ mycompany.service-now.com)' },
    { key: 'username', label: 'Service Account Username',   type: 'text',     required: true },
    { key: 'password', label: 'Password',                   type: 'password', required: true, helperText: 'Service account roles needed: itil (read incidents/changes), asset (read assets). REST API access is enabled by default. No write permissions required.' },
  ],
  jira: [
    { key: 'url',       label: 'Jira URL',     type: 'text',     required: true, placeholder: 'https://yourcompany.atlassian.net' },
    { key: 'username',  label: 'Email',        type: 'text',     required: true },
    { key: 'api_token', label: 'API Token',    type: 'password', required: true, helperText: 'Account settings → Security → API tokens. Account needs Browse Projects permission on the projects to be scanned. For JSM: Service Desk Team member role.' },
  ],
  // ── Monitoring ──────────────────────────────────────────────────────────────
  prtg: [
    { key: 'url',        label: 'PRTG URL',   type: 'text',     required: true, placeholder: 'https://prtg.corp.local' },
    { key: 'api_token',  label: 'API Token',  type: 'password', helperText: 'Preferred: Setup → Account Settings → API Token. Token permissions: Read access to all sensors and devices.' },
    { key: 'username',   label: 'Username',   type: 'text',     helperText: 'Used if no API token. Account role: Read-only.' },
    { key: 'password',   label: 'Password',   type: 'password', helperText: 'Used if no API token.' },
    { key: 'verify_ssl', label: 'Verify SSL', type: 'checkbox' },
  ],
  zabbix: [
    { key: 'url',      label: 'Zabbix URL',   type: 'text',     required: true,  placeholder: 'https://zabbix.corp.local' },
    { key: 'username', label: 'Username',     type: 'text',     required: true },
    { key: 'password', label: 'Password',     type: 'password', required: true,  helperText: 'Account requires: User role (minimum) for host/problem reads. Admin role needed to read user list.' },
  ],
  graylog: [
    { key: 'url',        label: 'Graylog URL',   type: 'text',     required: true,  placeholder: 'https://graylog.corp.local:9000' },
    { key: 'username',   label: 'Username',      type: 'text',     required: true },
    { key: 'password',   label: 'Password',      type: 'password', required: true,  helperText: 'Service account requires: Reader role (built-in) for stream + alert access. Create under System → Users.' },
    { key: 'verify_ssl', label: 'Verify SSL',    type: 'checkbox' },
  ],
  // ── Asset Management ─────────────────────────────────────────────────────────
  glpi: [
    { key: 'url',       label: 'GLPI URL',    type: 'text',     required: true, placeholder: 'https://glpi.corp.local' },
    { key: 'app_token', label: 'App Token',   type: 'password', required: true, helperText: 'Administration → API → Add API client → App Token. Enable API access in Setup → General → API.' },
    { key: 'username',  label: 'Username',    type: 'text',     required: true, helperText: 'Account needs Read access to Assets (Computers, Software, Network) and ITSM (Tickets). Use API session token auth.' },
    { key: 'password',  label: 'Password',    type: 'password', required: true },
  ],
  netbox: [
    { key: 'url',       label: 'NetBox URL',  type: 'text',     required: true, placeholder: 'https://netbox.corp.local' },
    { key: 'api_token', label: 'API Token',   type: 'password', required: true, helperText: 'Admin → Users → [user] → API Tokens → Add. Minimum permissions: Read access to DCIM (devices, sites, interfaces) and IPAM (IP addresses, prefixes). No write access required.' },
  ],
  // ── Cloud Posture ────────────────────────────────────────────────────────────
  aws_security_hub: [
    { key: 'access_key_id',     label: 'AWS Access Key ID',     type: 'text',     required: true },
    { key: 'secret_access_key', label: 'AWS Secret Access Key', type: 'password', required: true, helperText: 'IAM permissions needed: securityhub:GetFindings, securityhub:DescribeHub, securityhub:ListEnabledProductsForImport. Assign SecurityHubReadOnlyAccess managed policy or create a custom read-only policy.' },
    { key: 'region',            label: 'AWS Region',            type: 'text',     required: true, placeholder: 'eu-west-1' },
  ],
  azure_cspm: [
    { key: 'tenant_id',       label: 'Tenant ID (Directory ID)', type: 'text',     required: true,  helperText: 'Azure Portal → Entra ID → Overview → Tenant ID.' },
    { key: 'client_id',       label: 'App (Client) ID',          type: 'text',     required: true,  helperText: 'App Registration → Overview → Application (client) ID.' },
    { key: 'client_secret',   label: 'Client Secret',            type: 'password', required: true,  helperText: 'App Registration → Certificates & secrets → New client secret. Required RBAC roles on the subscription (IAM → Add role assignment): Reader + Security Reader + Monitoring Reader + Defender CSPM. Defender CSPM is required for Secure Score access.' },
    { key: 'subscription_id', label: 'Subscription ID',          type: 'text',     required: false, helperText: 'Optional. If blank, the connector auto-discovers all subscriptions accessible to the service principal.' },
  ],
  gcp_scc: [
    { key: 'org_id',             label: 'GCP Organisation ID',     type: 'text',     required: true,  placeholder: '123456789012' },
    { key: 'project_id',         label: 'GCP Project ID',          type: 'text',     helperText: 'Optional — for project-level asset queries' },
    { key: 'credentials_json',   label: 'Service Account JSON',    type: 'password', helperText: 'Paste the full service account key JSON. Or leave blank to use Application Default Credentials (GOOGLE_APPLICATION_CREDENTIALS env var). Roles needed: Security Center Findings Viewer, Security Center Assets Viewer (grant at org level).' },
  ],
  // ── DevSecOps ────────────────────────────────────────────────────────────────
  github: [
    { key: 'token', label: 'Personal Access Token (PAT)',  type: 'password', required: true, helperText: 'Settings → Developer settings → Personal access tokens (classic). Scopes: read:org, repo (for private repos), security_events (for code scanning / secret scanning). GitHub Advanced Security required for scanning alerts.' },
    { key: 'org',   label: 'Organisation Name',            type: 'text',     required: true, placeholder: 'my-github-org' },
    { key: 'url',   label: 'API URL',                      type: 'text',     placeholder: 'https://api.github.com', helperText: 'GitHub Enterprise Server only — e.g. https://github.corp.local/api/v3' },
  ],
  gitlab: [
    { key: 'token',    label: 'Personal Access Token (PAT)', type: 'password', required: true, helperText: 'User Settings → Access Tokens. Scopes: read_api, read_user. For security findings (Ultimate tier): security_dashboard permission. For audit events: Auditor role or Admin.' },
    { key: 'group_id', label: 'Group ID',                    type: 'text',     helperText: 'Optional — restrict to a specific group. Leave blank for instance-wide queries.' },
    { key: 'url',      label: 'GitLab URL',                  type: 'text',     placeholder: 'https://gitlab.com', helperText: 'Self-managed: e.g. https://gitlab.corp.local' },
  ],
  // ── Threat Intelligence ─────────────────────────────────────────────────────
  opencti: [
    { key: 'url',        label: 'OpenCTI URL', type: 'text',     required: true, placeholder: 'https://opencti.corp.local  or  https://app.opencti.io' },
    { key: 'token',      label: 'API Token',   type: 'password', required: true, helperText: 'Profile → API key (top-right menu → profile icon). Account needs: Threat-Intel read access (knowledge base).' },
    { key: 'verify_ssl', label: 'Verify SSL',  type: 'checkbox' },
  ],
  openaev: [
    { key: 'url',        label: 'OpenAEV URL', type: 'text',     required: true, placeholder: 'https://openaev.corp.local  or  https://app.openaev.io' },
    { key: 'token',      label: 'API Token',   type: 'password', required: true, helperText: 'Profile → API key (top-right menu → profile icon).' },
    { key: 'verify_ssl', label: 'Verify SSL',  type: 'checkbox' },
  ],
  // ── Microsoft 365 ────────────────────────────────────────────────────────────
  o365: [
    { key: 'tenant_id',     label: 'Tenant ID',       type: 'text',     required: true,  helperText: 'Azure Portal → Entra ID → Overview → Tenant ID.' },
    { key: 'client_id',     label: 'App (Client) ID', type: 'text',     required: true,  helperText: 'App Registration (client) ID. Required application permissions (no admin consent redirect): SecurityAlert.Read.All (unified security alerts), Policy.Read.All (Conditional Access policies). Optional: ThreatIndicators.Read.All.' },
    { key: 'client_secret', label: 'Client Secret',   type: 'password', required: true,  helperText: 'App Registration → Certificates & secrets. Grant admin consent for SecurityAlert.Read.All in API permissions after adding.' },
  ],
  // ── Generic ──────────────────────────────────────────────────────────────────
  siem: [
    { key: 'base_url',          label: 'SIEM Base URL',      type: 'text',     required: true,  placeholder: 'https://splunk.corp.local:8089', helperText: 'Base API URL for your SIEM. Works with Splunk (REST API port 8089), QRadar, Elastic SIEM, Logpoint, ArcSight, etc.' },
    { key: 'auth_type',         label: 'Auth Type',          type: 'text',     placeholder: 'api_key', helperText: 'api_key (Bearer token), basic (username + password), or token_endpoint (OAuth2 client credentials). Default: api_key.' },
    { key: 'api_key',           label: 'API Key / Token',    type: 'password', helperText: 'Used when auth_type=api_key. Sent as Authorization: Bearer <key>.' },
    { key: 'username',          label: 'Username',           type: 'text',     helperText: 'Used for basic auth or token_endpoint auth.' },
    { key: 'password',          label: 'Password',           type: 'password' },
    { key: 'alerts_endpoint',   label: 'Alerts Endpoint',    type: 'text',     placeholder: '/api/alerts', helperText: 'Path to the alerts or incidents list endpoint. Default: /api/alerts.' },
    { key: 'verify_ssl',        label: 'Verify SSL',         type: 'checkbox' },
  ],
  threat_intel: [
    { key: 'feed_url',      label: 'Feed URL',       type: 'text',     required: true,  placeholder: 'https://misp.corp.local  or  https://taxii.feed.com/taxii2', helperText: 'Supports: TAXII 2.1 (append /taxii2/ path), MISP instance REST API, or generic JSON array feed.' },
    { key: 'feed_type',     label: 'Feed Type',      type: 'text',     placeholder: 'json', helperText: 'taxii21 (STIX 2.1 via TAXII), misp (MISP REST API), or json (generic JSON array). Default: json.' },
    { key: 'auth_type',     label: 'Auth Type',      type: 'text',     placeholder: 'api_key', helperText: 'api_key or basic. Default: api_key.' },
    { key: 'api_key',       label: 'API Key',        type: 'password', helperText: 'MISP: Profile → Auth Key. TAXII: API key from provider. Generic: Bearer token.' },
    { key: 'username',      label: 'Username',       type: 'text',     helperText: 'For basic auth.' },
    { key: 'password',      label: 'Password',       type: 'password' },
    { key: 'collection_id', label: 'Collection ID',  type: 'text',     helperText: 'TAXII 2.1 only: collection ID to pull from (e.g. indicators, malware, campaign). Leave blank to use default.' },
    { key: 'verify_ssl',    label: 'Verify SSL',     type: 'checkbox' },
  ],
}

// ── ISO 27001 control mapping (which controls each connector provides evidence for) ───────────────

export const CONNECTOR_CONTROLS: Record<string, string[]> = {
  entra_id:          ['A.5.3', 'A.5.15', 'A.5.16', 'A.5.18', 'A.8.2', 'A.8.3', 'A.8.5'],
  defender:          ['A.8.1', 'A.8.7', 'A.8.18', 'A.8.19', 'A.8.8'],
  sentinel:          ['A.8.15', 'A.8.16', 'A.5.24', 'A.5.25', 'A.5.26', 'A.5.27', 'A.5.28'],
  intune:            ['A.8.1', 'A.8.18', 'A.8.19', 'A.8.7'],
  purview:           ['A.8.10', 'A.8.12'],
  active_directory:  ['A.5.3', 'A.5.15', 'A.5.16', 'A.5.18', 'A.8.2'],
  openldap:          ['A.5.3', 'A.5.15', 'A.5.16', 'A.5.18'],
  freeipa:           ['A.5.3', 'A.5.15', 'A.5.16', 'A.5.18', 'A.8.2'],
  authentik:         ['A.5.3', 'A.5.15', 'A.5.16', 'A.5.18', 'A.8.2', 'A.8.5'],
  keycloak:          ['A.5.3', 'A.5.15', 'A.5.16', 'A.5.18', 'A.8.2', 'A.8.5'],
  cyberark:          ['A.5.15', 'A.5.16', 'A.5.18', 'A.8.2', 'A.8.3', 'A.8.5'],
  devolutions:       ['A.5.3', 'A.5.15', 'A.5.16', 'A.5.18', 'A.8.2', 'A.8.3', 'A.8.15'],
  hashicorp_vault:   ['A.8.2', 'A.8.3', 'A.8.5', 'A.5.17', 'A.8.15'],
  fortigate:         ['A.8.20', 'A.8.21', 'A.8.22', 'A.8.23'],
  forti_analyzer:    ['A.8.15', 'A.8.16', 'A.8.1', 'A.8.18', 'A.8.19'],
  forti_manager:     ['A.8.1', 'A.8.18', 'A.8.20', 'A.8.21', 'A.8.22'],
  panw:              ['A.8.20', 'A.8.21', 'A.8.22', 'A.8.23'],
  cisco_asa:         ['A.8.20', 'A.8.21', 'A.8.22'],
  cisco_ise:         ['A.5.15', 'A.5.16', 'A.8.2', 'A.8.20', 'A.8.21'],
  zscaler:           ['A.8.20', 'A.8.22', 'A.8.23'],
  crowdstrike:       ['A.8.1', 'A.8.7', 'A.8.18', 'A.8.19', 'A.8.8'],
  sentinelone:       ['A.8.1', 'A.8.7', 'A.8.18', 'A.8.19', 'A.8.8'],
  wazuh:             ['A.8.1', 'A.8.7', 'A.8.18', 'A.8.19', 'A.8.15', 'A.8.16', 'A.8.8'],
  tenable_sc:        ['A.8.8'],
  tenable_io:        ['A.8.8'],
  qualys:            ['A.8.8'],
  openvas:           ['A.8.8'],
  servicenow:        ['A.5.24', 'A.5.25', 'A.5.26', 'A.5.27', 'A.5.28'],
  jira:              ['A.5.24', 'A.5.25', 'A.5.26', 'A.5.27', 'A.5.28'],
  prtg:              ['A.8.1', 'A.8.16', 'A.8.20'],
  zabbix:            ['A.8.1', 'A.8.16', 'A.8.20'],
  graylog:           ['A.8.15', 'A.8.16'],
  glpi:              ['A.5.9', 'A.8.1'],
  netbox:            ['A.5.9', 'A.8.1', 'A.8.20', 'A.8.21'],
  aws_security_hub:  ['A.8.8', 'A.5.23'],
  azure_cspm:        ['A.8.5', 'A.8.8', 'A.5.9', 'A.8.20', 'A.8.21', 'A.8.22', 'A.5.23'],
  gcp_scc:           ['A.8.8', 'A.5.23'],
  github:            ['A.8.25', 'A.8.26', 'A.8.28', 'A.8.29', 'A.5.3'],
  gitlab:            ['A.8.25', 'A.8.26', 'A.8.28', 'A.8.29', 'A.5.3'],
  o365:              ['A.5.15', 'A.5.16', 'A.5.18', 'A.8.1', 'A.8.5', 'A.8.7'],
  opencti:           ['A.5.7'],
  openaev:           ['A.5.7'],
  threat_intel:      ['A.5.7', 'A.8.16'],
  siem:              ['A.8.15', 'A.8.16'],
}

// ── KNOWN_SYSTEMS catalogue ────────────────────────────────────────────────────

// default_interval: recommended sync cadence in seconds, matched to ISO 27001 control review cycles
// Hourly (3600): alert/SIEM feeds — time-sensitive
// Daily (86400): identity, device, config, cloud posture — normal audit cadence
// Weekly (604800): vulnerability management — patch cycles are weekly/monthly
export const KNOWN_SYSTEMS: {
  value: string
  label: string
  product: string
  model: 'cloud' | 'on-prem' | 'both'
  default_interval: number
}[] = [
  // ── Microsoft ───────────────────────────────────────────────────────────────
  { value: 'entra_id',         label: 'Microsoft Entra ID',              product: 'ISMS / PRIV / CLD', model: 'cloud',   default_interval: 86400  },
  { value: 'defender',         label: 'Microsoft Defender for Endpoint', product: 'ISMS',               model: 'cloud',   default_interval: 86400  },
  { value: 'sentinel',         label: 'Microsoft Sentinel',              product: 'ISMS',               model: 'cloud',   default_interval: 3600   },
  { value: 'intune',           label: 'Microsoft Intune',                product: 'ISMS',               model: 'cloud',   default_interval: 86400  },
  { value: 'o365',             label: 'Microsoft Office 365',            product: 'ISMS',               model: 'cloud',   default_interval: 86400  },
  { value: 'purview',          label: 'Microsoft Purview',               product: 'ISMS / PRIV',        model: 'cloud',   default_interval: 86400  },
  // ── ITSM ────────────────────────────────────────────────────────────────────
  { value: 'servicenow',       label: 'ServiceNow ITSM',                 product: 'ISMS / PRIV',        model: 'both',    default_interval: 86400  },
  { value: 'jira',             label: 'Jira / JSM',                      product: 'ISMS / PRIV',        model: 'both',    default_interval: 86400  },
  // ── Network Security ────────────────────────────────────────────────────────
  { value: 'fortigate',        label: 'Fortinet FortiGate',              product: 'ISMS',               model: 'on-prem', default_interval: 86400  },
  { value: 'forti_analyzer',   label: 'Fortinet FortiAnalyzer',          product: 'ISMS',               model: 'on-prem', default_interval: 3600   },
  { value: 'forti_manager',    label: 'Fortinet FortiManager',           product: 'ISMS',               model: 'on-prem', default_interval: 86400  },
  { value: 'panw',             label: 'Palo Alto PAN-OS',                product: 'ISMS',               model: 'on-prem', default_interval: 86400  },
  { value: 'cisco_asa',        label: 'Cisco ASA / Firepower',           product: 'ISMS',               model: 'on-prem', default_interval: 86400  },
  { value: 'cisco_ise',        label: 'Cisco ISE',                       product: 'ISMS',               model: 'on-prem', default_interval: 86400  },
  { value: 'zscaler',          label: 'Zscaler ZIA',                     product: 'ISMS / PRIV',        model: 'cloud',   default_interval: 86400  },
  // ── EDR / Endpoint ──────────────────────────────────────────────────────────
  { value: 'crowdstrike',      label: 'CrowdStrike Falcon',              product: 'ISMS',               model: 'cloud',   default_interval: 86400  },
  { value: 'sentinelone',      label: 'SentinelOne',                     product: 'ISMS',               model: 'cloud',   default_interval: 86400  },
  { value: 'wazuh',            label: 'Wazuh (SIEM / EDR)',              product: 'ISMS',               model: 'on-prem', default_interval: 3600   },
  // ── Vulnerability Management ─────────────────────────────────────────────────
  { value: 'tenable_sc',       label: 'Tenable Security Center',         product: 'ISMS',               model: 'both',    default_interval: 604800 },
  { value: 'tenable_io',       label: 'Tenable Vulnerability Management',product: 'ISMS',               model: 'cloud',   default_interval: 604800 },
  { value: 'qualys',           label: 'Qualys VMDR',                     product: 'ISMS',               model: 'cloud',   default_interval: 604800 },
  { value: 'openvas',          label: 'OpenVAS / Greenbone',             product: 'ISMS',               model: 'on-prem', default_interval: 604800 },
  // ── Identity & Access ────────────────────────────────────────────────────────
  { value: 'active_directory', label: 'Windows Active Directory',        product: 'ISMS',               model: 'on-prem', default_interval: 86400  },
  { value: 'openldap',         label: 'OpenLDAP',                        product: 'ISMS',               model: 'on-prem', default_interval: 86400  },
  { value: 'freeipa',          label: 'FreeIPA / Red Hat IdM',           product: 'ISMS',               model: 'on-prem', default_interval: 86400  },
  { value: 'authentik',        label: 'Authentik (IdP)',                  product: 'ISMS / PRIV',        model: 'both',    default_interval: 86400  },
  { value: 'keycloak',         label: 'Keycloak (IdP)',                   product: 'ISMS / PRIV',        model: 'both',    default_interval: 86400  },
  // ── PAM ──────────────────────────────────────────────────────────────────────
  { value: 'cyberark',         label: 'CyberArk PAS',                   product: 'ISMS / PRIV',        model: 'on-prem', default_interval: 86400  },
  { value: 'devolutions',      label: 'Devolutions Server (DVLS)',        product: 'ISMS / PRIV',        model: 'on-prem', default_interval: 86400  },
  { value: 'hashicorp_vault',  label: 'HashiCorp Vault',                 product: 'ISMS',               model: 'both',    default_interval: 86400  },
  // ── Monitoring ───────────────────────────────────────────────────────────────
  { value: 'prtg',             label: 'PRTG Network Monitor',            product: 'ISMS',               model: 'on-prem', default_interval: 3600   },
  { value: 'zabbix',           label: 'Zabbix',                          product: 'ISMS',               model: 'on-prem', default_interval: 3600   },
  { value: 'graylog',          label: 'Graylog',                         product: 'ISMS',               model: 'both',    default_interval: 3600   },
  // ── Asset Management ─────────────────────────────────────────────────────────
  { value: 'glpi',             label: 'GLPI (ITSM / Asset Mgmt)',        product: 'ISMS',               model: 'on-prem', default_interval: 86400  },
  { value: 'netbox',           label: 'NetBox (IPAM / DCIM)',            product: 'ISMS',               model: 'on-prem', default_interval: 86400  },
  // ── Cloud Posture ────────────────────────────────────────────────────────────
  { value: 'aws_security_hub', label: 'AWS Security Hub',               product: 'CLD',                model: 'cloud',   default_interval: 86400  },
  { value: 'azure_cspm',       label: 'Azure CSPM (Defender for Cloud)', product: 'CLD',               model: 'cloud',   default_interval: 86400  },
  { value: 'gcp_scc',          label: 'GCP Security Command Center',    product: 'CLD',                model: 'cloud',   default_interval: 86400  },
  // ── DevSecOps ────────────────────────────────────────────────────────────────
  { value: 'github',           label: 'GitHub',                          product: 'ISMS',               model: 'both',    default_interval: 86400  },
  { value: 'gitlab',           label: 'GitLab',                          product: 'ISMS',               model: 'both',    default_interval: 86400  },
  // ── Filigran XTM ─────────────────────────────────────────────────────────────
  { value: 'opencti',          label: 'OpenCTI',                         product: 'ISMS',               model: 'both',    default_interval: 86400  },
  { value: 'openaev',          label: 'OpenAEV',                         product: 'ISMS',               model: 'both',    default_interval: 86400  },
  // ── Generic ──────────────────────────────────────────────────────────────────
  { value: 'siem',             label: 'Generic SIEM',                    product: 'SEC',                model: 'both',    default_interval: 3600   },
  { value: 'threat_intel',     label: 'Threat Intel Feed',               product: 'SEC',                model: 'both',    default_interval: 86400  },
]

// ── API ───────────────────────────────────────────────────────────────────────

export const connectorsApi = {
  list: () =>
    client.get<ConnectorRead[]>('/connectors/').then((r) => r.data),

  register: (body: ConnectorRegisterPayload) =>
    client.post<ConnectorRegistered>('/connectors/register', body).then((r) => r.data),

  deregister: (id: string) =>
    client.delete(`/connectors/${id}`),

  updateConfig: (id: string, config: Record<string, string | boolean>) =>
    client.put(`/connectors/${id}/config`, { config }),

  rename: (id: string, name: string) =>
    client.patch(`/connectors/${id}/rename`, { name }),

  triggerSync: (id: string) =>
    client.post(`/connectors/${id}/sync`),

  getEvidence: (groupCode: string, limit = 100) =>
    client.get<ConnectorEvidenceRead[]>(`/connectors/evidence/${groupCode}`, { params: { limit } }).then((r) => r.data),

  getAllEvidence: (limit = 200, product?: string) =>
    client.get<ConnectorEvidenceRead[]>('/connectors/evidence/', { params: { limit, product } }).then((r) => r.data),

  exportEvidenceCsvUrl: (product?: string) => {
    const q = product ? `?product=${product}` : ''
    return `/api/v1/connectors/evidence/export${q}`
  },

  // ── Archiving ──────────────────────────────────────────────────────────────
  getArchiveStats: () =>
    client.get<ArchiveStats[]>('/connectors/archive/stats').then((r) => r.data),

  runArchive: (connectorId?: string) =>
    client.post<{ archived: number }>('/connectors/archive/run', null, { params: connectorId ? { connector_id: connectorId } : {} }).then((r) => r.data),

  purgeArchived: (connectorId?: string) =>
    client.post<{ purged: number }>('/connectors/archive/purge', null, { params: connectorId ? { connector_id: connectorId } : {} }).then((r) => r.data),

  setRetention: (id: string, days: number | null) =>
    client.patch(`/connectors/${id}/retention`, { retention_days: days }),

  deleteEvidence: (id: string) =>
    client.delete(`/connectors/evidence/item/${id}`),

  deleteConnectorEvidence: (connectorId: string) =>
    client.delete(`/connectors/${connectorId}/evidence`),
}
