import { useState } from 'react'
import {
  Alert,
  Box,
  Button,
  Card,
  CardContent,
  Chip,
  CircularProgress,
  Dialog,
  DialogActions,
  DialogContent,
  DialogTitle,
  Divider,
  FormControlLabel,
  IconButton,
  LinearProgress,
  MenuItem,
  Paper,
  Select,
  Snackbar,
  Switch,
  Tab,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Tabs,
  TextField,
  Tooltip,
  Typography,
} from '@mui/material'
import {
  AccountTreeOutlined,
  AddOutlined,
  ArchiveOutlined,
  CheckCircleOutlined,
  DeleteForeverOutlined,
  ErrorOutlined,
  InfoOutlined,
  HelpOutlineOutlined,
  HourglassEmptyOutlined,
  ArrowForwardOutlined,
  BugReportOutlined,
  CloudOutlined,
  ConfirmationNumberOutlined,
  DeleteOutlined,
  DeviceHubOutlined,
  ElectricalServicesOutlined,
  LanOutlined,
  ListAltOutlined,
  LockOutlined,
  MailOutlined,
  PeopleAltOutlined,
  PhoneAndroidOutlined,
  RouterOutlined,
  SearchOutlined,
  SecurityOutlined,
  SettingsOutlined,
  ShieldOutlined,
  SyncOutlined,
  ShowChartOutlined,
  StorageOutlined,
  TrackChangesOutlined,
  TravelExploreOutlined,
  VpnKeyOutlined,
  WarningAmberOutlined,
} from '@mui/icons-material'
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query'
import dayjs from 'dayjs'
import relativeTime from 'dayjs/plugin/relativeTime'
import { connectorsApi, CONNECTOR_CONFIG_SCHEMA, CONNECTOR_CONTROLS, KNOWN_SYSTEMS } from '../api/connectorsApi'
import type { ArchiveStats, ConfigField, ConnectorRead, ConnectorRegistered } from '../api/connectorsApi'
import PageHeader from '../components/PageHeader'

dayjs.extend(relativeTime)

// ── Connector catalogue ───────────────────────────────────────────────────────

const BUILT_SYSTEMS = new Set([
  // Microsoft
  'entra_id', 'defender', 'sentinel', 'intune', 'purview', 'o365',
  // Identity & Access
  'active_directory', 'openldap', 'freeipa', 'authentik', 'keycloak',
  // PAM
  'cyberark', 'devolutions', 'hashicorp_vault',
  // Network Security
  'fortigate', 'forti_analyzer', 'forti_manager', 'panw', 'cisco_asa', 'cisco_ise', 'zscaler',
  // EDR / Endpoint
  'crowdstrike', 'sentinelone', 'wazuh',
  // Vulnerability Management
  'tenable_sc', 'tenable_io', 'qualys', 'openvas',
  // ITSM
  'servicenow', 'jira',
  // Monitoring & SIEM
  'prtg', 'zabbix', 'graylog',
  // Asset Management
  'glpi', 'netbox',
  // Cloud Posture
  'aws_security_hub', 'azure_cspm', 'gcp_scc',
  // DevSecOps
  'github', 'gitlab',
  // Threat Intelligence
  'opencti', 'openaev', 'threat_intel',
  // Generic
  'siem',
])

const SYSTEM_ICON: Record<string, React.ElementType> = {
  entra_id:         PeopleAltOutlined,
  o365:             MailOutlined,
  defender:         ShieldOutlined,
  sentinel:         TrackChangesOutlined,
  intune:           PhoneAndroidOutlined,
  purview:          SearchOutlined,
  active_directory: AccountTreeOutlined,
  openldap:         AccountTreeOutlined,
  freeipa:          AccountTreeOutlined,
  authentik:        VpnKeyOutlined,
  keycloak:         VpnKeyOutlined,
  cisco_ise:        VpnKeyOutlined,
  cyberark:         LockOutlined,
  devolutions:      LockOutlined,
  hashicorp_vault:  LockOutlined,
  fortigate:        RouterOutlined,
  forti_analyzer:   StorageOutlined,
  forti_manager:    RouterOutlined,
  panw:             RouterOutlined,
  cisco_asa:        LanOutlined,
  zscaler:          CloudOutlined,
  crowdstrike:      ShieldOutlined,
  sentinelone:      ShieldOutlined,
  wazuh:            SecurityOutlined,
  tenable_sc:       BugReportOutlined,
  tenable_io:       BugReportOutlined,
  qualys:           SearchOutlined,
  openvas:          SearchOutlined,
  servicenow:       ConfirmationNumberOutlined,
  jira:             TrackChangesOutlined,
  prtg:             ShowChartOutlined,
  zabbix:           ShowChartOutlined,
  graylog:          StorageOutlined,
  glpi:             ListAltOutlined,
  netbox:           DeviceHubOutlined,
  aws_security_hub: CloudOutlined,
  azure_cspm:       CloudOutlined,
  gcp_scc:          CloudOutlined,
  github:           ElectricalServicesOutlined,
  gitlab:           ElectricalServicesOutlined,
  opencti:          TravelExploreOutlined,
  openaev:          ShieldOutlined,
  siem:             SecurityOutlined,
  threat_intel:     TravelExploreOutlined,
}

const CONNECTOR_CATEGORIES: { name: string; color: string; systems: string[] }[] = [
  {
    name: 'Microsoft',
    color: '#0078D4',
    systems: ['entra_id', 'o365', 'defender', 'sentinel', 'intune', 'purview'],
  },
  {
    name: 'Identity & Access',
    color: '#7B1FA2',
    systems: ['active_directory', 'openldap', 'freeipa', 'authentik', 'keycloak', 'cisco_ise'],
  },
  {
    name: 'PAM',
    color: '#37474F',
    systems: ['cyberark', 'devolutions', 'hashicorp_vault'],
  },
  {
    name: 'Network Security',
    color: '#C62828',
    systems: ['fortigate', 'forti_analyzer', 'forti_manager', 'panw', 'cisco_asa', 'zscaler'],
  },
  {
    name: 'EDR / Endpoint',
    color: '#AD1457',
    systems: ['crowdstrike', 'sentinelone', 'wazuh'],
  },
  {
    name: 'Vulnerability Management',
    color: '#E65100',
    systems: ['tenable_sc', 'tenable_io', 'qualys', 'openvas'],
  },
  {
    name: 'ITSM',
    color: '#1565C0',
    systems: ['servicenow', 'jira'],
  },
  {
    name: 'Monitoring & SIEM',
    color: '#2E7D32',
    systems: ['prtg', 'zabbix', 'graylog'],
  },
  {
    name: 'Asset Management',
    color: '#4E342E',
    systems: ['glpi', 'netbox'],
  },
  {
    name: 'Cloud Posture',
    color: '#00695C',
    systems: ['aws_security_hub', 'azure_cspm', 'gcp_scc'],
  },
  {
    name: 'DevSecOps',
    color: '#1A237E',
    systems: ['github', 'gitlab'],
  },
  {
    name: 'Filigran XTM',
    color: '#4527A0',
    systems: ['opencti', 'openaev'],
  },
  {
    name: 'Threat Intelligence',
    color: '#6A1B9A',
    systems: ['threat_intel'],
  },
  {
    name: 'Generic',
    color: '#546E7A',
    systems: ['siem'],
  },
]

// ── Poll interval options ─────────────────────────────────────────────────────

const INTERVAL_OPTIONS = [
  { value: 3600,   label: 'Every hour'     },
  { value: 21600,  label: 'Every 6 hours'  },
  { value: 43200,  label: 'Every 12 hours' },
  { value: 86400,  label: 'Daily (24h)'    },
  { value: 604800, label: 'Weekly (7 days)'},
]

function intervalLabel(seconds: number): string {
  return INTERVAL_OPTIONS.find((o) => o.value === seconds)?.label ?? `${seconds}s`
}

function PollIntervalSelect({
  value,
  onChange,
}: {
  value: number
  onChange: (v: number) => void
}) {
  return (
    <Box>
      <Typography variant="caption" color="text.secondary" sx={{ display: 'block', mb: 0.5 }}>
        Sync Frequency
      </Typography>
      <Select
        size="small"
        fullWidth
        value={value}
        onChange={(e) => onChange(Number(e.target.value))}
      >
        {INTERVAL_OPTIONS.map((o) => (
          <MenuItem key={o.value} value={o.value}>{o.label}</MenuItem>
        ))}
      </Select>
      <Typography variant="caption" color="text.secondary">
        How often the connector syncs evidence. Match to your control review cycle.
      </Typography>
    </Box>
  )
}

// ── Helpers ───────────────────────────────────────────────────────────────────

const STATUS_CHIP: Record<string, { label: string; color: 'success' | 'error' | 'default' }> = {
  active:   { label: 'Active',   color: 'success' },
  inactive: { label: 'Inactive', color: 'default' },
  error:    { label: 'Error',    color: 'error' },
}

function systemLabel(value: string) {
  return KNOWN_SYSTEMS.find((s) => s.value === value)?.label ?? value
}

function categoryColor(value: string) {
  return CONNECTOR_CATEGORIES.find((c) => c.systems.includes(value))?.color ?? '#666'
}

// ── Connector health ──────────────────────────────────────────────────────────
// error   → last_error is set (most recent sync failed)
// pending → never run
// healthy → last_run within 48h, no error
// stale   → last_run older than 48h or missing

type HealthState = 'error' | 'pending' | 'healthy' | 'stale'

function connectorHealth(c: ConnectorRead): HealthState {
  if (c.last_error) return 'error'
  if (!c.last_run) return 'pending'
  const ageHours = (Date.now() - new Date(c.last_run).getTime()) / 3_600_000
  return ageHours <= 48 ? 'healthy' : 'stale'
}

const HEALTH_CONFIG: Record<HealthState, { icon: React.ReactNode; label: string; color: string }> = {
  healthy: { icon: <CheckCircleOutlined sx={{ fontSize: 16, color: '#C6EFCE' }} />, label: 'Healthy', color: '#C6EFCE' },
  stale:   { icon: <HourglassEmptyOutlined sx={{ fontSize: 16, color: '#FFEB9C' }} />, label: 'Stale',   color: '#FFEB9C' },
  error:   { icon: <ErrorOutlined sx={{ fontSize: 16, color: '#FFC7CE' }} />,          label: 'Error',   color: '#FFC7CE' },
  pending: { icon: <HelpOutlineOutlined sx={{ fontSize: 16, color: '#9e9e9e' }} />,    label: 'Pending', color: '#9e9e9e' },
}

// ── Config field renderer ─────────────────────────────────────────────────────

function ConfigFields({
  fields,
  values,
  onChange,
}: {
  fields: ConfigField[]
  values: Record<string, string | boolean>
  onChange: (key: string, val: string | boolean) => void
}) {
  return (
    <Box sx={{ display: 'flex', flexDirection: 'column', gap: 1.5 }}>
      {fields.map((f) =>
        f.type === 'checkbox' ? (
          <FormControlLabel
            key={f.key}
            control={
              <Switch
                size="small"
                checked={!!values[f.key]}
                onChange={(e) => onChange(f.key, e.target.checked)}
              />
            }
            label={
              <Typography variant="body2">{f.label}</Typography>
            }
          />
        ) : (
          <TextField
            key={f.key}
            label={f.label}
            placeholder={f.placeholder}
            helperText={f.helperText}
            type={f.type === 'password' ? 'password' : 'text'}
            value={(values[f.key] as string) ?? ''}
            onChange={(e) => onChange(f.key, e.target.value)}
            required={f.required}
            size="small"
            fullWidth
            autoComplete="off"
            inputProps={{ spellCheck: false }}
          />
        )
      )}
    </Box>
  )
}

// ── Config Dialog (edit existing connector) ───────────────────────────────────

function ConfigDialog({
  connector,
  onClose,
}: {
  connector: ConnectorRead
  onClose: () => void
}) {
  const qc = useQueryClient()
  const fields = CONNECTOR_CONFIG_SCHEMA[connector.source_system] ?? []
  const sys = KNOWN_SYSTEMS.find((s) => s.value === connector.source_system)
  const [values, setValues] = useState<Record<string, string | boolean>>({})
  const [pollInterval, setPollInterval] = useState<number>(sys?.default_interval ?? 86400)
  const [displayName, setDisplayName] = useState(connector.name)
  const [retentionDays, setRetentionDays] = useState<string>(String(connector.retention_days ?? 90))
  const [saved, setSaved] = useState(false)

  const mutation = useMutation({
    mutationFn: async () => {
      await connectorsApi.updateConfig(connector.id, { ...values, poll_interval: pollInterval })
      if (displayName.trim() && displayName.trim() !== connector.name) {
        await connectorsApi.rename(connector.id, displayName.trim())
      }
      const days = parseInt(retentionDays, 10)
      if (!isNaN(days) && days > 0) {
        await connectorsApi.setRetention(connector.id, days)
      }
    },
    onSuccess: () => {
      qc.invalidateQueries({ queryKey: ['connectors'] })
      setSaved(true)
      setTimeout(onClose, 1200)
    },
  })

  function handleChange(key: string, val: string | boolean) {
    setValues((prev) => ({ ...prev, [key]: val }))
  }

  return (
    <Dialog open onClose={onClose} maxWidth="sm" fullWidth>
      <DialogTitle>
        Configure — {systemLabel(connector.source_system)}
        <Typography variant="body2" color="text.secondary" fontWeight={400} sx={{ mt: 0.25 }}>
          {connector.name}
        </Typography>
      </DialogTitle>
      <DialogContent sx={{ display: 'flex', flexDirection: 'column', gap: 2, pt: 2 }}>
        {mutation.isError && (
          <Alert severity="error">Failed to save config. Check backend logs.</Alert>
        )}
        {saved && <Alert severity="success">Config saved. Connector will pick it up on next poll.</Alert>}
        <Divider><Typography variant="caption" color="text.secondary">Display Name</Typography></Divider>
        <TextField
          label="Connector Name"
          size="small"
          value={displayName}
          onChange={(e) => setDisplayName(e.target.value)}
          helperText="Name shown in the Evidence table and Connectors list"
          fullWidth
        />
        {fields.length === 0 ? (
          <Alert severity="info">
            This connector is configured via environment variables in the Docker Compose file.
          </Alert>
        ) : (
          <>
            <Divider><Typography variant="caption" color="text.secondary">Credentials</Typography></Divider>
            <ConfigFields fields={fields} values={values} onChange={handleChange} />
          </>
        )}
        <Divider><Typography variant="caption" color="text.secondary">Schedule</Typography></Divider>
        <PollIntervalSelect value={pollInterval} onChange={setPollInterval} />
        <Divider><Typography variant="caption" color="text.secondary">Evidence Retention</Typography></Divider>
        <TextField
          label="Retention (days)"
          size="small"
          type="number"
          value={retentionDays}
          onChange={(e) => setRetentionDays(e.target.value)}
          helperText="Evidence older than this many days will be archived. Default: 90 days."
          inputProps={{ min: 1, max: 3650 }}
          sx={{ maxWidth: 200 }}
        />
      </DialogContent>
      <DialogActions>
        <Button onClick={onClose}>Close</Button>
        <Button
          variant="contained"
          disabled={mutation.isPending || saved}
          onClick={() => mutation.mutate()}
          startIcon={mutation.isPending ? <CircularProgress size={14} /> : undefined}
        >
          Save Config
        </Button>
      </DialogActions>
    </Dialog>
  )
}

// ── Last Sync Detail Dialog ───────────────────────────────────────────────────

function SyncDetailDialog({ connector, onClose }: { connector: ConnectorRead; onClose: () => void }) {
  const health = connector.last_error ? 'error' : !connector.last_run ? 'pending' : 'healthy'
  return (
    <Dialog open onClose={onClose} maxWidth="sm" fullWidth>
      <DialogTitle>
        Sync Details — {connector.name}
        <Typography variant="body2" color="text.secondary" fontWeight={400} sx={{ mt: 0.25 }}>
          {systemLabel(connector.source_system)}
        </Typography>
      </DialogTitle>
      <DialogContent sx={{ display: 'flex', flexDirection: 'column', gap: 2, pt: 2 }}>
        <Box sx={{ display: 'flex', gap: 2, flexWrap: 'wrap' }}>
          <Box sx={{ flex: 1, minWidth: 140 }}>
            <Typography variant="caption" color="text.secondary">Status</Typography>
            <Box>
              <Chip
                size="small"
                label={health === 'error' ? 'Error' : health === 'pending' ? 'Pending' : 'Healthy'}
                sx={{
                  bgcolor: health === 'error' ? '#FFC7CE' : health === 'pending' ? '#FFEB9C' : '#C6EFCE',
                  color: '#000',
                  fontSize: '0.7rem',
                  mt: 0.5,
                }}
              />
            </Box>
          </Box>
          <Box sx={{ flex: 1, minWidth: 140 }}>
            <Typography variant="caption" color="text.secondary">Last Sync</Typography>
            <Typography variant="body2">{connector.last_run ? dayjs(connector.last_run).format('DD MMM YYYY HH:mm:ss') : '—'}</Typography>
          </Box>
          <Box sx={{ flex: 1, minWidth: 140 }}>
            <Typography variant="caption" color="text.secondary">Last Item Count</Typography>
            <Typography variant="body2">{connector.last_item_count ?? '—'}</Typography>
          </Box>
          <Box sx={{ flex: 1, minWidth: 140 }}>
            <Typography variant="caption" color="text.secondary">Total Evidence</Typography>
            <Typography variant="body2">{connector.evidence_count}</Typography>
          </Box>
        </Box>
        {connector.last_error && (
          <>
            <Divider><Typography variant="caption" color="error">Last Error</Typography></Divider>
            <Box sx={{ bgcolor: 'rgba(255,0,0,0.05)', border: '1px solid rgba(255,0,0,0.2)', borderRadius: 1, p: 1.5 }}>
              <Typography variant="caption" color="text.secondary" sx={{ fontSize: '0.65rem' }}>
                {connector.last_error_at ? dayjs(connector.last_error_at).format('DD MMM YYYY HH:mm:ss') : ''}
              </Typography>
              <Typography variant="body2" sx={{ fontFamily: 'monospace', fontSize: '0.75rem', whiteSpace: 'pre-wrap', color: '#FFC7CE', mt: 0.5 }}>
                {connector.last_error}
              </Typography>
            </Box>
          </>
        )}
        <Divider><Typography variant="caption" color="text.secondary">Retention</Typography></Divider>
        <Typography variant="body2" color="text.secondary">
          Evidence older than <strong>{connector.retention_days ?? 90} days</strong> will be archived on the next archive run.
        </Typography>
      </DialogContent>
      <DialogActions>
        <Button onClick={onClose}>Close</Button>
      </DialogActions>
    </Dialog>
  )
}

// ── Archive Management Dialog ─────────────────────────────────────────────────

function ArchiveDialog({ onClose }: { onClose: () => void }) {
  const qc = useQueryClient()
  const [confirmPurge, setConfirmPurge] = useState(false)

  const { data: stats = [], isLoading } = useQuery<ArchiveStats[]>({
    queryKey: ['archive-stats'],
    queryFn: () => connectorsApi.getArchiveStats(),
  })

  const runArchive = useMutation({
    mutationFn: () => connectorsApi.runArchive(),
    onSuccess: () => { qc.invalidateQueries({ queryKey: ['archive-stats'] }); qc.invalidateQueries({ queryKey: ['connectors'] }) },
  })

  const purge = useMutation({
    mutationFn: () => connectorsApi.purgeArchived(),
    onSuccess: () => { qc.invalidateQueries({ queryKey: ['archive-stats'] }); setConfirmPurge(false) },
  })

  const totalActive = stats.reduce((s, r) => s + r.active, 0)
  const totalArchived = stats.reduce((s, r) => s + r.archived, 0)

  return (
    <Dialog open onClose={onClose} maxWidth="md" fullWidth>
      <DialogTitle>
        Evidence Archive
        <Typography variant="body2" color="text.secondary" fontWeight={400} sx={{ mt: 0.25 }}>
          Manage evidence retention. Archived items are hidden from the Evidence tab but not deleted.
        </Typography>
      </DialogTitle>
      <DialogContent sx={{ display: 'flex', flexDirection: 'column', gap: 2, pt: 2 }}>
        {/* Summary */}
        <Box sx={{ display: 'flex', gap: 2 }}>
          <Card sx={{ flex: 1 }}>
            <CardContent sx={{ pb: '12px !important' }}>
              <Typography variant="caption" color="text.secondary">Active Evidence</Typography>
              <Typography variant="h5" sx={{ fontWeight: 700, color: '#C6EFCE' }}>{totalActive}</Typography>
            </CardContent>
          </Card>
          <Card sx={{ flex: 1 }}>
            <CardContent sx={{ pb: '12px !important' }}>
              <Typography variant="caption" color="text.secondary">Archived</Typography>
              <Typography variant="h5" sx={{ fontWeight: 700, color: '#aaa' }}>{totalArchived}</Typography>
            </CardContent>
          </Card>
        </Box>

        {/* Per-connector table */}
        {isLoading ? <LinearProgress /> : (
          <TableContainer component={Paper} variant="outlined">
            <Table size="small">
              <TableHead>
                <TableRow>
                  <TableCell>Connector</TableCell>
                  <TableCell align="right">Retention</TableCell>
                  <TableCell align="right">Active</TableCell>
                  <TableCell align="right">Archived</TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {stats.map((row) => (
                  <TableRow key={row.connector_id}>
                    <TableCell>
                      <Typography variant="body2">{row.name}</Typography>
                      <Typography variant="caption" color="text.secondary" sx={{ fontFamily: 'monospace' }}>{row.source_system}</Typography>
                    </TableCell>
                    <TableCell align="right">
                      <Typography variant="body2">{row.retention_days}d</Typography>
                    </TableCell>
                    <TableCell align="right">
                      <Typography variant="body2" sx={{ color: '#C6EFCE' }}>{row.active}</Typography>
                    </TableCell>
                    <TableCell align="right">
                      <Typography variant="body2" color="text.secondary">{row.archived}</Typography>
                    </TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </TableContainer>
        )}

        {confirmPurge && (
          <Alert severity="error">
            This will <strong>permanently delete</strong> all {totalArchived} archived items. This cannot be undone.
          </Alert>
        )}
      </DialogContent>
      <DialogActions>
        {confirmPurge ? (
          <>
            <Button onClick={() => setConfirmPurge(false)}>Cancel</Button>
            <Button variant="contained" color="error" startIcon={purge.isPending ? <CircularProgress size={14} /> : <DeleteForeverOutlined />} onClick={() => purge.mutate()} disabled={purge.isPending}>
              Confirm Purge
            </Button>
          </>
        ) : (
          <>
            <Button onClick={onClose}>Close</Button>
            {totalArchived > 0 && (
              <Button variant="outlined" color="error" startIcon={<DeleteForeverOutlined />} onClick={() => setConfirmPurge(true)}>
                Purge Archived ({totalArchived})
              </Button>
            )}
            <Button
              variant="contained"
              startIcon={runArchive.isPending ? <CircularProgress size={14} /> : <ArchiveOutlined />}
              onClick={() => runArchive.mutate()}
              disabled={runArchive.isPending}
            >
              {runArchive.isPending ? 'Archiving…' : runArchive.isSuccess ? `Done (+${(runArchive.data as any)?.archived ?? 0} archived)` : 'Run Archive Now'}
            </Button>
          </>
        )}
      </DialogActions>
    </Dialog>
  )
}

// ── Registration Success Dialog ───────────────────────────────────────────────

function RegisteredDialog({ data, onClose }: { data: ConnectorRegistered; onClose: () => void }) {
  return (
    <Dialog open onClose={onClose} maxWidth="xs" fullWidth>
      <DialogTitle>Connector Registered</DialogTitle>
      <DialogContent>
        <Alert severity="success" sx={{ mb: 2 }}>
          <strong>{data.name}</strong> ({systemLabel(data.source_system)}) registered successfully.
        </Alert>
        <Typography variant="body2" color="text.secondary">
          The connectors worker will pick it up within 60 seconds. Set credentials via the ⚙ button.
        </Typography>
      </DialogContent>
      <DialogActions>
        <Button onClick={onClose} variant="contained">Done</Button>
      </DialogActions>
    </Dialog>
  )
}

// ── Register Dialog (two-step) ────────────────────────────────────────────────

function RegisterDialog({ onClose }: { onClose: () => void }) {
  const queryClient = useQueryClient()
  const [step, setStep] = useState<'pick' | 'name'>('pick')
  const [selectedSystem, setSelectedSystem] = useState('')
  const [name, setName] = useState('')
  const [configValues, setConfigValues] = useState<Record<string, string | boolean>>({})
  const [pollInterval, setPollInterval] = useState<number>(86400)
  const [registered, setRegistered] = useState<ConnectorRegistered | null>(null)

  const { data: existingConnectors = [] } = useQuery({
    queryKey: ['connectors'],
    queryFn: connectorsApi.list,
    staleTime: 30_000,
  })

  // Map source_system → health state for the catalogue
  const activeBySystem = new Map<string, HealthState>()
  for (const c of existingConnectors) {
    if (c.status === 'active') activeBySystem.set(c.source_system, connectorHealth(c))
  }

  const mutation = useMutation({
    mutationFn: async () => {
      const data = await connectorsApi.register({ name: name.trim(), source_system: selectedSystem })
      // Always save config (at minimum poll_interval)
      const hasCredentials = Object.values(configValues).some((v) => v !== '' && v !== false)
      if (hasCredentials || pollInterval !== 86400) {
        await connectorsApi.updateConfig(data.id, { ...configValues, poll_interval: pollInterval })
      }
      return data
    },
    onSuccess: (data) => {
      queryClient.invalidateQueries({ queryKey: ['connectors'] })
      setRegistered(data)
    },
  })

  function handleConfigChange(key: string, val: string | boolean) {
    setConfigValues((prev) => ({ ...prev, [key]: val }))
  }

  if (registered) return <RegisteredDialog data={registered} onClose={onClose} />

  // ── Step 1: system picker ──────────────────────────────────────────────────
  if (step === 'pick') {
    return (
      <Dialog open onClose={onClose} maxWidth="md" fullWidth scroll="paper">
        <DialogTitle>
          Select Source System
        </DialogTitle>

        <DialogContent dividers sx={{ px: 3, py: 2 }}>
          {CONNECTOR_CATEGORIES.map((cat) => {
            // only render categories where at least one system is in KNOWN_SYSTEMS
            const knownInCat = cat.systems.filter((v) => KNOWN_SYSTEMS.some((s) => s.value === v))
            if (knownInCat.length === 0) return null

            return (
              <Box key={cat.name} sx={{ mb: 3 }}>
                {/* Category header */}
                <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 1 }}>
                  <Box sx={{ width: 3, height: 14, borderRadius: 1, bgcolor: cat.color, flexShrink: 0 }} />
                  <Typography
                    variant="caption"
                    sx={{
                      fontWeight: 700,
                      letterSpacing: '0.07em',
                      textTransform: 'uppercase',
                      color: cat.color,
                    }}
                  >
                    {cat.name}
                  </Typography>
                </Box>

                {/* System cards */}
                <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 1 }}>
                  {knownInCat.map((sysValue) => {
                    const sys = KNOWN_SYSTEMS.find((s) => s.value === sysValue)
                    if (!sys) return null
                    const isBuilt = BUILT_SYSTEMS.has(sysValue)
                    const isSelected = selectedSystem === sysValue
                    const isOnPrem = sys.model === 'on-prem'
                    const Icon = SYSTEM_ICON[sysValue] ?? ElectricalServicesOutlined
                    const activeHealth = activeBySystem.get(sysValue)

                    return (
                      <Tooltip
                        key={sysValue}
                        title={isBuilt ? (isOnPrem ? 'On-premises connector (Model B)' : '') : 'Planned for v2.0'}
                        placement="top"
                        disableHoverListener={isBuilt && !isOnPrem}
                      >
                        <Paper
                          variant="outlined"
                          onClick={() => isBuilt && setSelectedSystem(sysValue)}
                          sx={{
                            width: 132,
                            p: 1.5,
                            cursor: isBuilt ? 'pointer' : 'not-allowed',
                            opacity: isBuilt ? 1 : 0.38,
                            borderColor: isSelected ? cat.color : 'divider',
                            borderWidth: isSelected ? 2 : 1,
                            bgcolor: isSelected ? `${cat.color}18` : 'background.paper',
                            transition: 'border-color 0.12s, background-color 0.12s',
                            '&:hover': isBuilt
                              ? { borderColor: cat.color, bgcolor: `${cat.color}0E` }
                              : {},
                            display: 'flex',
                            flexDirection: 'column',
                            gap: 0.75,
                            userSelect: 'none',
                          }}
                        >
                          <Icon
                            fontSize="small"
                            sx={{ color: isSelected ? cat.color : 'text.secondary' }}
                          />
                          <Typography
                            variant="body2"
                            fontWeight={isSelected ? 600 : 400}
                            sx={{ lineHeight: 1.3, fontSize: '0.775rem' }}
                          >
                            {sys.label}
                          </Typography>
                          <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 0.4, mt: 0.25 }}>
                            {isBuilt ? (
                              activeHealth ? (
                                <Chip
                                  icon={HEALTH_CONFIG[activeHealth].icon as React.ReactElement}
                                  label={activeHealth === 'error' ? 'Error' : 'Connected'}
                                  size="small"
                                  variant="outlined"
                                  sx={{
                                    height: 17,
                                    fontSize: '0.63rem',
                                    '& .MuiChip-label': { px: 0.5 },
                                    '& .MuiChip-icon': { ml: 0.4, mr: -0.25 },
                                    color: HEALTH_CONFIG[activeHealth].color,
                                    borderColor: HEALTH_CONFIG[activeHealth].color,
                                  }}
                                />
                              ) : (
                                <Chip
                                  label="Available"
                                  size="small"
                                  color="success"
                                  variant={isSelected ? 'filled' : 'outlined'}
                                  sx={{ height: 17, fontSize: '0.63rem', '& .MuiChip-label': { px: 0.6 } }}
                                />
                              )
                            ) : (
                              <Chip
                                label="Planned"
                                size="small"
                                variant="outlined"
                                sx={{ height: 17, fontSize: '0.63rem', '& .MuiChip-label': { px: 0.6 } }}
                              />
                            )}
                            {isOnPrem && (
                              <Chip
                                icon={<StorageOutlined style={{ fontSize: 10 }} />}
                                label="On-Prem"
                                size="small"
                                variant="outlined"
                                sx={{
                                  height: 17,
                                  fontSize: '0.63rem',
                                  '& .MuiChip-label': { px: 0.5 },
                                  '& .MuiChip-icon': { ml: 0.4 },
                                  color: 'text.secondary',
                                  borderColor: 'text.disabled',
                                }}
                              />
                            )}
                          </Box>
                        </Paper>
                      </Tooltip>
                    )
                  })}
                </Box>
              </Box>
            )
          })}
        </DialogContent>

        <DialogActions>
          <Button onClick={onClose}>Cancel</Button>
          <Button
            variant="contained"
            disabled={!selectedSystem}
            onClick={() => {
              const sys = KNOWN_SYSTEMS.find((s) => s.value === selectedSystem)
              setPollInterval(sys?.default_interval ?? 86400)
              setStep('name')
            }}
            endIcon={<ArrowForwardOutlined />}
          >
            Next
          </Button>
        </DialogActions>
      </Dialog>
    )
  }

  // ── Step 2: name + credentials ─────────────────────────────────────────────
  const sys = KNOWN_SYSTEMS.find((s) => s.value === selectedSystem)
  const Icon = SYSTEM_ICON[selectedSystem] ?? ElectricalServicesOutlined
  const color = categoryColor(selectedSystem)
  const configFields = CONNECTOR_CONFIG_SCHEMA[selectedSystem] ?? []

  return (
    <Dialog open onClose={onClose} maxWidth="sm" fullWidth>
      <DialogTitle>Register Connector</DialogTitle>
      <DialogContent sx={{ display: 'flex', flexDirection: 'column', gap: 2, pt: 2 }}>
        {mutation.isError && (
          <Alert severity="error">Registration failed. Check backend logs.</Alert>
        )}

        {/* Selected system summary */}
        <Paper
          variant="outlined"
          sx={{ p: 1.5, display: 'flex', alignItems: 'flex-start', gap: 1.5, borderColor: color }}
        >
          <Icon sx={{ color, fontSize: 28, mt: 0.25 }} />
          <Box sx={{ flex: 1, minWidth: 0 }}>
            <Typography variant="body2" fontWeight={600}>{sys?.label}</Typography>
            <Typography variant="caption" color="text.secondary">{sys?.product}</Typography>
            {(CONNECTOR_CONTROLS[selectedSystem] ?? []).length > 0 && (
              <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 0.4, mt: 0.75 }}>
                <Typography variant="caption" color="text.secondary" sx={{ mr: 0.5 }}>Evidence for:</Typography>
                {(CONNECTOR_CONTROLS[selectedSystem] ?? []).map((ctrl) => (
                  <Chip
                    key={ctrl}
                    label={ctrl}
                    size="small"
                    variant="outlined"
                    sx={{ height: 17, fontSize: '0.62rem', '& .MuiChip-label': { px: 0.6 }, color: color, borderColor: color + '66' }}
                  />
                ))}
              </Box>
            )}
          </Box>
          <Button size="small" onClick={() => setStep('pick')}>
            Change
          </Button>
        </Paper>

        <TextField
          label="Instance Name"
          placeholder={`${sys?.label ?? 'Connector'} — Your Org`}
          value={name}
          onChange={(e) => setName(e.target.value)}
          fullWidth
          size="small"
          autoFocus
          helperText="Identifies this connection (useful when registering multiple instances of the same system)"
        />

        {/* Credentials section */}
        {configFields.length > 0 && (
          <>
            <Divider>
              <Typography variant="caption" color="text.secondary">Credentials</Typography>
            </Divider>
            <ConfigFields fields={configFields} values={configValues} onChange={handleConfigChange} />
            <Typography variant="caption" color="text.secondary">
              Credentials are encrypted and stored in the database. The connector fetches them on startup.
              You can update them later via the ⚙ button in the connector table.
            </Typography>
          </>
        )}

        <Divider><Typography variant="caption" color="text.secondary">Schedule</Typography></Divider>
        <PollIntervalSelect value={pollInterval} onChange={setPollInterval} />
      </DialogContent>

      <DialogActions>
        <Button onClick={onClose}>Cancel</Button>
        <Button
          variant="contained"
          disabled={!name.trim() || mutation.isPending}
          onClick={() => mutation.mutate()}
          startIcon={mutation.isPending ? <CircularProgress size={14} /> : undefined}
        >
          Register
        </Button>
      </DialogActions>
    </Dialog>
  )
}

// ── Deregister Confirm ────────────────────────────────────────────────────────

function DeregisterDialog({
  connectorName,
  onConfirm,
  onClose,
}: {
  connectorName: string
  onConfirm: () => void
  onClose: () => void
}) {
  return (
    <Dialog open onClose={onClose} maxWidth="xs" fullWidth>
      <DialogTitle sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
        <WarningAmberOutlined color="warning" /> Deregister Connector
      </DialogTitle>
      <DialogContent>
        <Typography>
          Remove <strong>{connectorName}</strong>? All evidence ingested by this connector will be permanently deleted.
        </Typography>
      </DialogContent>
      <DialogActions>
        <Button onClick={onClose}>Cancel</Button>
        <Button variant="contained" color="error" onClick={onConfirm}>Deregister</Button>
      </DialogActions>
    </Dialog>
  )
}

// ── Main Page ─────────────────────────────────────────────────────────────────

export default function Connectors() {
  const queryClient = useQueryClient()
  const [showRegister, setShowRegister] = useState(false)
  const [deregisterTarget, setDeregisterTarget] = useState<{ id: string; name: string } | null>(null)
  const [configureTarget, setConfigureTarget] = useState<ConnectorRead | null>(null)
  const [syncDetailTarget, setSyncDetailTarget] = useState<ConnectorRead | null>(null)
  const [showArchive, setShowArchive] = useState(false)

  const { data: connectors = [], isLoading } = useQuery({
    queryKey: ['connectors'],
    queryFn: connectorsApi.list,
    refetchInterval: 30_000,
  })

  const deregisterMutation = useMutation({
    mutationFn: (id: string) => connectorsApi.deregister(id),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['connectors'] })
      setDeregisterTarget(null)
    },
  })

  const [syncingId, setSyncingId] = useState<string | null>(null)
  const [syncToast, setSyncToast] = useState(false)
  const syncMutation = useMutation({
    mutationFn: (id: string) => connectorsApi.triggerSync(id),
    onMutate: (id) => setSyncingId(id),
    onSuccess: () => {
      setSyncToast(true)
      queryClient.invalidateQueries({ queryKey: ['connectors'] })
    },
    onSettled: () => setSyncingId(null),
  })

  return (
    <Box>
      <PageHeader
        title="Connectors"
        subtitle="Automated evidence ingestion from external systems"
        icon={<ElectricalServicesOutlined />}
        actions={
          <Box sx={{ display: 'flex', gap: 1 }}>
            <Button
              variant="outlined"
              startIcon={<ArchiveOutlined />}
              onClick={() => setShowArchive(true)}
              size="small"
            >
              Archive
            </Button>
            <Button
              variant="contained"
              startIcon={<AddOutlined />}
              onClick={() => setShowRegister(true)}
              size="small"
            >
              Register Connector
            </Button>
          </Box>
        }
      />


      {isLoading ? (
        <Box sx={{ display: 'flex', justifyContent: 'center', py: 6 }}>
          <CircularProgress />
        </Box>
      ) : connectors.length === 0 ? (
        <Paper variant="outlined" sx={{ p: 4, textAlign: 'center' }}>
          <ElectricalServicesOutlined sx={{ fontSize: 48, color: 'text.disabled', mb: 1 }} />
          <Typography color="text.secondary">No connectors registered yet.</Typography>
          <Button
            variant="outlined"
            startIcon={<AddOutlined />}
            sx={{ mt: 2 }}
            onClick={() => setShowRegister(true)}
          >
            Register your first connector
          </Button>
        </Paper>
      ) : (
        <TableContainer component={Paper} variant="outlined">
          <Table size="small">
            <TableHead>
              <TableRow>
                <TableCell>Name</TableCell>
                <TableCell>Source System</TableCell>
                <TableCell>ISO Controls</TableCell>
                <TableCell>Status</TableCell>
                <TableCell>Health</TableCell>
                <TableCell>Schedule</TableCell>
                <TableCell>Last Sync</TableCell>
                <TableCell align="right">Items</TableCell>
                <TableCell align="right">Registered</TableCell>
                <TableCell />
              </TableRow>
            </TableHead>
            <TableBody>
              {connectors.map((c) => {
                const chip = STATUS_CHIP[c.status] ?? { label: c.status, color: 'default' as const }
                const Icon = SYSTEM_ICON[c.source_system] ?? ElectricalServicesOutlined
                const color = categoryColor(c.source_system)
                return (
                  <TableRow key={c.id} hover>
                    <TableCell>
                      <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                        <Icon sx={{ fontSize: 16, color }} />
                        <Typography variant="body2" fontWeight={500}>{c.name}</Typography>
                      </Box>
                    </TableCell>
                    <TableCell>
                      <Typography variant="body2" color="text.secondary">
                        {systemLabel(c.source_system)}
                      </Typography>
                    </TableCell>
                    <TableCell>
                      <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 0.4 }}>
                        {(CONNECTOR_CONTROLS[c.source_system] ?? []).slice(0, 5).map((ctrl) => (
                          <Chip
                            key={ctrl}
                            label={ctrl}
                            size="small"
                            variant="outlined"
                            sx={{ height: 16, fontSize: '0.6rem', '& .MuiChip-label': { px: 0.6 }, color: 'text.secondary', borderColor: 'divider' }}
                          />
                        ))}
                        {(CONNECTOR_CONTROLS[c.source_system] ?? []).length > 5 && (
                          <Chip
                            label={`+${(CONNECTOR_CONTROLS[c.source_system] ?? []).length - 5}`}
                            size="small"
                            variant="outlined"
                            sx={{ height: 16, fontSize: '0.6rem', '& .MuiChip-label': { px: 0.6 }, color: 'text.disabled' }}
                          />
                        )}
                      </Box>
                    </TableCell>
                    <TableCell>
                      <Chip label={chip.label} color={chip.color} size="small" />
                    </TableCell>
                    <TableCell>
                      {(() => {
                        const health = connectorHealth(c)
                        const hc = HEALTH_CONFIG[health]
                        const tooltipTitle = c.last_error
                          ? `Last error: ${c.last_error}`
                          : hc.label
                        return (
                          <Tooltip title={tooltipTitle} arrow>
                            <Box sx={{ display: 'flex', flexDirection: 'column', gap: 0.4 }}>
                              <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.5 }}>
                                {hc.icon}
                                <Typography variant="caption" sx={{ color: hc.color, fontWeight: 600, fontSize: '0.65rem' }}>
                                  {hc.label}
                                </Typography>
                              </Box>
                              {c.last_error && (
                                <Typography variant="caption" color="error.light"
                                  sx={{ fontSize: '0.58rem', maxWidth: 200, overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap', display: 'block' }}>
                                  {c.last_error}
                                </Typography>
                              )}
                            </Box>
                          </Tooltip>
                        )
                      })()}
                    </TableCell>
                    <TableCell>
                      <Typography variant="caption" color="text.secondary">
                        {intervalLabel(KNOWN_SYSTEMS.find((s) => s.value === c.source_system)?.default_interval ?? 86400)}
                      </Typography>
                    </TableCell>
                    <TableCell>
                      {c.sync_requested_at && (!c.last_run || new Date(c.sync_requested_at) > new Date(c.last_run)) ? (
                        <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.75 }}>
                          <CircularProgress size={11} thickness={5} />
                          <Typography variant="caption" color="text.secondary">Syncing…</Typography>
                        </Box>
                      ) : (
                        <Typography variant="body2" color="text.secondary">
                          {c.last_run ? dayjs(c.last_run).fromNow() : '—'}
                        </Typography>
                      )}
                    </TableCell>
                    <TableCell align="right">
                      <Typography variant="body2">{c.evidence_count}</Typography>
                    </TableCell>
                    <TableCell align="right">
                      <Typography variant="body2" color="text.secondary">
                        {dayjs(c.created_at).format('DD MMM YYYY')}
                      </Typography>
                    </TableCell>
                    <TableCell align="right">
                      <Box sx={{ display: 'flex', justifyContent: 'flex-end', gap: 0.5 }}>
                        <Tooltip title="Sync details">
                          <IconButton size="small" onClick={() => setSyncDetailTarget(c)}>
                            <InfoOutlined fontSize="small" sx={{ color: c.last_error ? '#FFC7CE' : 'text.secondary' }} />
                          </IconButton>
                        </Tooltip>
                        <Tooltip title="Sync now">
                          <span>
                            <IconButton
                              size="small"
                              disabled={syncingId === c.id}
                              onClick={() => syncMutation.mutate(c.id)}
                            >
                              <SyncOutlined
                                fontSize="small"
                                sx={{
                                  animation: syncingId === c.id ? 'spin 1s linear infinite' : 'none',
                                  '@keyframes spin': { '0%': { transform: 'rotate(0deg)' }, '100%': { transform: 'rotate(360deg)' } },
                                }}
                              />
                            </IconButton>
                          </span>
                        </Tooltip>
                        <Tooltip title="Configure credentials">
                          <IconButton
                            size="small"
                            onClick={() => setConfigureTarget(c)}
                          >
                            <SettingsOutlined fontSize="small" />
                          </IconButton>
                        </Tooltip>
                        <Tooltip title="Deregister connector">
                          <IconButton
                            size="small"
                            color="error"
                            onClick={() => setDeregisterTarget({ id: c.id, name: c.name })}
                          >
                            <DeleteOutlined fontSize="small" />
                          </IconButton>
                        </Tooltip>
                      </Box>
                    </TableCell>
                  </TableRow>
                )
              })}
            </TableBody>
          </Table>
        </TableContainer>
      )}

      <Snackbar
        open={syncToast}
        autoHideDuration={4000}
        onClose={() => setSyncToast(false)}
        message="Sync queued — connector will run within 30 s"
        anchorOrigin={{ vertical: 'bottom', horizontal: 'center' }}
      />

      {showRegister && <RegisterDialog onClose={() => setShowRegister(false)} />}
      {configureTarget && (
        <ConfigDialog connector={configureTarget} onClose={() => setConfigureTarget(null)} />
      )}
      {syncDetailTarget && (
        <SyncDetailDialog connector={syncDetailTarget} onClose={() => setSyncDetailTarget(null)} />
      )}
      {showArchive && <ArchiveDialog onClose={() => setShowArchive(false)} />}
      {deregisterTarget && (
        <DeregisterDialog
          connectorName={deregisterTarget.name}
          onConfirm={() => deregisterMutation.mutate(deregisterTarget.id)}
          onClose={() => setDeregisterTarget(null)}
        />
      )}
    </Box>
  )
}
