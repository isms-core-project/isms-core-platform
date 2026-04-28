import { useState } from 'react'
import {
  Box,
  Card,
  CardContent,
  Typography,
  Button,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Chip,
  TextField,
  Select,
  MenuItem,
  FormControl,
  InputLabel,
  Tabs,
  Tab,
  Tooltip,
  Alert,
  Pagination,
  useTheme,
} from '@mui/material'
import {
  HistoryOutlined,
  FilterListOutlined,
  FileDownloadOutlined,
  SyncOutlined,
  ElectricalServicesOutlined,
  SecurityOutlined,
} from '@mui/icons-material'
import { useQuery } from '@tanstack/react-query'
import dayjs from 'dayjs'
import { adminApi } from '../api/admin'
import type { AuditLogParams } from '../api/admin'
import PageHeader from '../components/PageHeader'
import { useAuth } from '../store/AuthContext'

const SEV_DARK: Record<string, { bg: string; fg: string }> = {
  info:     { bg: 'rgba(68,114,196,0.2)',  fg: '#9DC3E6' },
  warning:  { bg: 'rgba(255,192,0,0.15)', fg: '#FFEB9C' },
  error:    { bg: 'rgba(255,100,0,0.18)', fg: '#FFB347' },
  critical: { bg: 'rgba(192,0,0,0.18)',   fg: '#FFC7CE' },
}
const SEV_LIGHT: Record<string, { bg: string; fg: string }> = {
  info:     { bg: 'rgba(68,114,196,0.15)',  fg: '#2E5099' },
  warning:  { bg: 'rgba(230,145,0,0.15)',   fg: '#7a4800' },
  error:    { bg: 'rgba(230,100,0,0.15)',   fg: '#7a2800' },
  critical: { bg: 'rgba(192,0,0,0.15)',     fg: '#9e0000' },
}

const CAT_DARK: Record<string, { bg: string; fg: string }> = {
  security: { bg: 'rgba(192,0,0,0.12)',        fg: '#FFC7CE' },
  workflow: { bg: 'rgba(68,114,196,0.12)',      fg: '#9DC3E6' },
  system:   { bg: 'rgba(255,255,255,0.07)',     fg: '#d9d9d9' },
}
const CAT_LIGHT: Record<string, { bg: string; fg: string }> = {
  security: { bg: 'rgba(192,0,0,0.12)',        fg: '#9e0000' },
  workflow: { bg: 'rgba(68,114,196,0.12)',      fg: '#2E5099' },
  system:   { bg: 'rgba(0,0,0,0.07)',           fg: '#555555' },
}

const STATUS_DARK: Record<string, { bg: string; fg: string }> = {
  success: { bg: 'rgba(112,173,71,0.15)', fg: '#C6EFCE' },
  error:   { bg: 'rgba(192,0,0,0.18)',    fg: '#FFC7CE' },
  running: { bg: 'rgba(255,192,0,0.15)', fg: '#FFEB9C' },
}
const STATUS_LIGHT: Record<string, { bg: string; fg: string }> = {
  success: { bg: 'rgba(46,125,50,0.15)',  fg: '#1b5e20' },
  error:   { bg: 'rgba(192,0,0,0.12)',    fg: '#9e0000' },
  running: { bg: 'rgba(230,145,0,0.15)', fg: '#7a4800' },
}

function fmtDuration(s: number | null): string {
  if (s === null) return '—'
  if (s < 60) return `${s}s`
  const m = Math.floor(s / 60)
  const rem = Math.round(s % 60)
  return rem > 0 ? `${m}m ${rem}s` : `${m}m`
}

// ---------------------------------------------------------------------------
// Audit Trail tab
// ---------------------------------------------------------------------------

function AuditTrailTab() {
  const { palette } = useTheme()
  const SEV_COLOR = palette.mode === 'light' ? SEV_LIGHT : SEV_DARK
  const CAT_COLOR = palette.mode === 'light' ? CAT_LIGHT : CAT_DARK
  const [page, setPage] = useState(1)
  const [filters, setFilters] = useState<AuditLogParams>({ page_size: 50 })
  const [draft, setDraft] = useState<AuditLogParams>({})

  const { data, isLoading } = useQuery({
    queryKey: ['logs', 'audit', page, filters],
    queryFn: () => adminApi.getAuditLog({ ...filters, page }),
    placeholderData: (prev) => prev,
  })

  function applyFilters() {
    setPage(1)
    setFilters({ page_size: 50, ...draft })
  }

  function clearFilters() {
    setDraft({})
    setPage(1)
    setFilters({ page_size: 50 })
  }

  return (
    <Card>
      <CardContent sx={{ pb: '12px !important' }}>
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 2 }}>
          <HistoryOutlined sx={{ color: 'primary.main' }} />
          <Typography variant="h6">Audit Trail</Typography>
          {data && (
            <Chip label={`${data.total} entries`} size="small" sx={{ height: 18, fontSize: '0.65rem' }} />
          )}
          {filters.category === 'security' && (
            <Chip
              label="Security filter active"
              size="small"
              icon={<SecurityOutlined sx={{ fontSize: '0.8rem !important' }} />}
              sx={{ height: 18, fontSize: '0.65rem', bgcolor: 'rgba(192,0,0,0.18)', color: palette.mode === 'light' ? '#9e0000' : '#FFC7CE' }}
            />
          )}
          <Box sx={{ ml: 'auto' }}>
            <Button
              size="small" variant="outlined" startIcon={<FileDownloadOutlined />}
              onClick={async () => {
                const all = await adminApi.getAuditLog({ ...filters, page: 1, page_size: 10000 })
                const header = 'timestamp,event_type,category,severity,actor_email,description,target_type,ip_address'
                const rows = all.items.map((e) =>
                  [e.created_at, e.event_type, e.category, e.severity,
                   e.actor_email ?? '', (e.description ?? '').replace(/"/g, '""'),
                   e.target_type ?? '', e.ip_address ?? '']
                    .map((v) => `"${v}"`).join(',')
                )
                const csv = [header, ...rows].join('\n')
                const a = document.createElement('a')
                a.href = URL.createObjectURL(new Blob([csv], { type: 'text/csv' }))
                a.download = `isms-audit-log-${new Date().toISOString().slice(0, 10)}.csv`
                a.click()
              }}
              sx={{ fontSize: '0.7rem' }}
            >
              Export CSV
            </Button>
          </Box>
        </Box>

        {/* Quick security filter */}
        <Box sx={{ display: 'flex', gap: 1, mb: 1.5 }}>
          <Button
            size="small" variant={filters.category === 'security' ? 'contained' : 'outlined'}
            startIcon={<SecurityOutlined />}
            onClick={() => {
              setPage(1)
              if (filters.category === 'security') {
                setFilters({ page_size: 50 })
                setDraft({})
              } else {
                setFilters({ page_size: 50, category: 'security' })
                setDraft({ category: 'security' })
              }
            }}
            color="error"
            sx={{ fontSize: '0.7rem' }}
          >
            Security Events
          </Button>
        </Box>

        {/* Filters */}
        <Box sx={{ display: 'flex', gap: 1.5, flexWrap: 'wrap', mb: 2, alignItems: 'flex-end' }}>
          <FormControl size="small" sx={{ minWidth: 120 }}>
            <InputLabel>Category</InputLabel>
            <Select
              value={draft.category ?? ''}
              onChange={(e) => setDraft((d) => ({ ...d, category: e.target.value || undefined }))}
              label="Category"
            >
              <MenuItem value="">All</MenuItem>
              <MenuItem value="security">Security</MenuItem>
              <MenuItem value="workflow">Workflow</MenuItem>
              <MenuItem value="system">System</MenuItem>
            </Select>
          </FormControl>

          <FormControl size="small" sx={{ minWidth: 110 }}>
            <InputLabel>Severity</InputLabel>
            <Select
              value={draft.severity ?? ''}
              onChange={(e) => setDraft((d) => ({ ...d, severity: e.target.value || undefined }))}
              label="Severity"
            >
              <MenuItem value="">All</MenuItem>
              <MenuItem value="info">Info</MenuItem>
              <MenuItem value="warning">Warning</MenuItem>
              <MenuItem value="error">Error</MenuItem>
              <MenuItem value="critical">Critical</MenuItem>
            </Select>
          </FormControl>

          <TextField
            size="small" label="Event type" placeholder="e.g. login"
            value={draft.event_type ?? ''}
            onChange={(e) => setDraft((d) => ({ ...d, event_type: e.target.value || undefined }))}
            sx={{ width: 160 }}
          />

          <TextField
            size="small" label="Actor email"
            value={draft.actor_email ?? ''}
            onChange={(e) => setDraft((d) => ({ ...d, actor_email: e.target.value || undefined }))}
            sx={{ width: 200 }}
          />

          <TextField
            size="small" label="From" type="date" InputLabelProps={{ shrink: true }}
            value={draft.date_from ?? ''}
            onChange={(e) => setDraft((d) => ({ ...d, date_from: e.target.value || undefined }))}
            sx={{ width: 150 }}
          />

          <TextField
            size="small" label="To" type="date" InputLabelProps={{ shrink: true }}
            value={draft.date_to ?? ''}
            onChange={(e) => setDraft((d) => ({ ...d, date_to: e.target.value || undefined }))}
            sx={{ width: 150 }}
          />

          <Button variant="outlined" size="small" startIcon={<FilterListOutlined />} onClick={applyFilters}>
            Apply
          </Button>
          <Button size="small" onClick={clearFilters}>Clear</Button>
        </Box>

        <TableContainer>
          <Table size="small">
            <TableHead>
              <TableRow>
                <TableCell>Event</TableCell>
                <TableCell>Category</TableCell>
                <TableCell>Severity</TableCell>
                <TableCell>Actor</TableCell>
                <TableCell>Target</TableCell>
                <TableCell>Description</TableCell>
                <TableCell>Time</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {isLoading && [...Array(5)].map((_, i) => (
                <TableRow key={i}>
                  {[...Array(7)].map((_, j) => (
                    <TableCell key={j}>
                      <Box sx={{ height: 14, bgcolor: 'rgba(255,255,255,0.05)', borderRadius: 1 }} />
                    </TableCell>
                  ))}
                </TableRow>
              ))}

              {!isLoading && data?.items.length === 0 && (
                <TableRow>
                  <TableCell colSpan={7} align="center" sx={{ py: 4 }}>
                    <Typography variant="body2" color="text.secondary">No audit log entries found.</Typography>
                  </TableCell>
                </TableRow>
              )}

              {data?.items.map((entry) => {
                const sc = SEV_COLOR[entry.severity] ?? SEV_COLOR.info
                const cc = CAT_COLOR[entry.category] ?? CAT_COLOR.system
                return (
                  <TableRow key={entry.id} hover>
                    <TableCell>
                      <Typography variant="body2" fontFamily="monospace" fontSize="0.75rem">
                        {entry.event_type}
                      </Typography>
                    </TableCell>
                    <TableCell>
                      <Chip label={entry.category} size="small" sx={{ fontSize: '0.65rem', height: 18, bgcolor: cc.bg, color: cc.fg }} />
                    </TableCell>
                    <TableCell>
                      <Chip label={entry.severity} size="small" sx={{ fontSize: '0.65rem', height: 18, bgcolor: sc.bg, color: sc.fg }} />
                    </TableCell>
                    <TableCell>
                      <Typography variant="caption" color="text.secondary">
                        {entry.actor_email ?? (entry.user_id ? entry.user_id.slice(0, 8) + '…' : '—')}
                      </Typography>
                    </TableCell>
                    <TableCell>
                      {entry.target_type ? (
                        <Typography variant="caption" color="text.secondary">
                          {entry.target_type}{entry.target_id ? ` · ${entry.target_id.slice(0, 8)}…` : ''}
                        </Typography>
                      ) : '—'}
                    </TableCell>
                    <TableCell sx={{ maxWidth: 300 }}>
                      <Typography variant="caption" color="text.secondary" sx={{ display: 'block', whiteSpace: 'normal', wordBreak: 'break-word' }}>
                        {entry.description ?? '—'}
                      </Typography>
                    </TableCell>
                    <TableCell>
                      <Tooltip title={dayjs(entry.created_at).format('DD MMM YYYY HH:mm:ss')}>
                        <Typography variant="caption" color="text.secondary" noWrap>
                          {dayjs(entry.created_at).format('DD MMM HH:mm')}
                        </Typography>
                      </Tooltip>
                    </TableCell>
                  </TableRow>
                )
              })}
            </TableBody>
          </Table>
        </TableContainer>

        {data && data.pages > 1 && (
          <Box sx={{ display: 'flex', justifyContent: 'center', mt: 2 }}>
            <Pagination
              count={data.pages}
              page={page}
              onChange={(_, p) => setPage(p)}
              size="small"
              color="primary"
            />
          </Box>
        )}
      </CardContent>
    </Card>
  )
}

// ---------------------------------------------------------------------------
// Feed Runs tab
// ---------------------------------------------------------------------------

const FEED_NAMES = ['nist_cve', 'cisa_kev', 'epss', 'euvd', 'mitre_attack', 'mitre_atlas']

function FeedRunsTab() {
  const { palette } = useTheme()
  const STATUS_COLOR = palette.mode === 'light' ? STATUS_LIGHT : STATUS_DARK
  const [feedFilter, setFeedFilter] = useState('')
  const [statusFilter, setStatusFilter] = useState('')

  const { data, isLoading, refetch, isFetching } = useQuery({
    queryKey: ['logs', 'feed-runs', feedFilter, statusFilter],
    queryFn: () =>
      adminApi.getFeedRuns({
        feed_name: feedFilter || undefined,
        status: statusFilter || undefined,
        limit: 300,
      }),
  })

  return (
    <Card>
      <CardContent sx={{ pb: '12px !important' }}>
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 2 }}>
          <SyncOutlined sx={{ color: 'primary.main' }} />
          <Typography variant="h6">Feed Runs</Typography>
          {data && (
            <Chip label={`${data.length} runs`} size="small" sx={{ height: 18, fontSize: '0.65rem' }} />
          )}
          <Box sx={{ ml: 'auto' }}>
            <Button
              size="small" variant="outlined" startIcon={<SyncOutlined />}
              onClick={() => refetch()}
              disabled={isFetching}
              sx={{ fontSize: '0.7rem' }}
            >
              Refresh
            </Button>
          </Box>
        </Box>

        <Box sx={{ display: 'flex', gap: 1.5, mb: 2, flexWrap: 'wrap', alignItems: 'center' }}>
          <FormControl size="small" sx={{ minWidth: 150 }}>
            <InputLabel>Feed</InputLabel>
            <Select value={feedFilter} onChange={(e) => setFeedFilter(e.target.value)} label="Feed">
              <MenuItem value="">All feeds</MenuItem>
              {FEED_NAMES.map((f) => <MenuItem key={f} value={f}>{f}</MenuItem>)}
            </Select>
          </FormControl>
          <FormControl size="small" sx={{ minWidth: 120 }}>
            <InputLabel>Status</InputLabel>
            <Select value={statusFilter} onChange={(e) => setStatusFilter(e.target.value)} label="Status">
              <MenuItem value="">All</MenuItem>
              <MenuItem value="success">Success</MenuItem>
              <MenuItem value="error">Error</MenuItem>
              <MenuItem value="running">Running</MenuItem>
            </Select>
          </FormControl>
        </Box>

        <TableContainer>
          <Table size="small">
            <TableHead>
              <TableRow>
                <TableCell>Feed</TableCell>
                <TableCell>Status</TableCell>
                <TableCell>Started</TableCell>
                <TableCell>Duration</TableCell>
                <TableCell>Items</TableCell>
                <TableCell>Error</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {isLoading && [...Array(4)].map((_, i) => (
                <TableRow key={i}>
                  {[...Array(6)].map((_, j) => (
                    <TableCell key={j}><Box sx={{ height: 14, bgcolor: 'rgba(255,255,255,0.05)', borderRadius: 1 }} /></TableCell>
                  ))}
                </TableRow>
              ))}
              {!isLoading && data?.length === 0 && (
                <TableRow>
                  <TableCell colSpan={6} align="center" sx={{ py: 4 }}>
                    <Typography variant="body2" color="text.secondary">No feed runs found.</Typography>
                  </TableCell>
                </TableRow>
              )}
              {data?.map((run) => {
                const sc = STATUS_COLOR[run.status] ?? STATUS_COLOR.success
                return (
                  <TableRow key={run.id} hover>
                    <TableCell>
                      <Typography variant="body2" fontFamily="monospace" fontSize="0.75rem">
                        {run.feed_name}
                      </Typography>
                    </TableCell>
                    <TableCell>
                      <Chip label={run.status} size="small" sx={{ fontSize: '0.65rem', height: 18, bgcolor: sc.bg, color: sc.fg }} />
                    </TableCell>
                    <TableCell>
                      <Tooltip title={run.started_at ? dayjs(run.started_at).format('DD MMM YYYY HH:mm:ss') : ''}>
                        <Typography variant="caption" color="text.secondary" noWrap>
                          {run.started_at ? dayjs(run.started_at).format('DD MMM HH:mm') : '—'}
                        </Typography>
                      </Tooltip>
                    </TableCell>
                    <TableCell>
                      <Typography variant="caption" color="text.secondary">
                        {fmtDuration(run.duration_seconds)}
                      </Typography>
                    </TableCell>
                    <TableCell>
                      <Typography variant="caption" color="text.secondary">
                        {run.item_count ?? '—'}
                      </Typography>
                    </TableCell>
                    <TableCell sx={{ maxWidth: 260 }}>
                      {run.error_message ? (
                        <Typography variant="caption" color="error.main" sx={{ whiteSpace: 'normal', wordBreak: 'break-word' }}>
                          {run.error_message}
                        </Typography>
                      ) : <Typography variant="caption" color="text.disabled">—</Typography>}
                    </TableCell>
                  </TableRow>
                )
              })}
            </TableBody>
          </Table>
        </TableContainer>
      </CardContent>
    </Card>
  )
}

// ---------------------------------------------------------------------------
// Connector Runs tab
// ---------------------------------------------------------------------------

function ConnectorRunsTab() {
  const [statusFilter, setStatusFilter] = useState('')

  const { data, isLoading, refetch, isFetching } = useQuery({
    queryKey: ['logs', 'connector-runs', statusFilter],
    queryFn: () =>
      adminApi.getConnectorRuns({
        status: statusFilter || undefined,
        limit: 300,
      }),
  })

  const hasLimited = data?.some((r) => r.history_limited)

  return (
    <Card>
      <CardContent sx={{ pb: '12px !important' }}>
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 2 }}>
          <ElectricalServicesOutlined sx={{ color: 'primary.main' }} />
          <Typography variant="h6">Connector Runs</Typography>
          {data && (
            <Chip label={`${data.length} runs`} size="small" sx={{ height: 18, fontSize: '0.65rem' }} />
          )}
          <Box sx={{ ml: 'auto' }}>
            <Button
              size="small" variant="outlined" startIcon={<SyncOutlined />}
              onClick={() => refetch()}
              disabled={isFetching}
              sx={{ fontSize: '0.7rem' }}
            >
              Refresh
            </Button>
          </Box>
        </Box>

        {hasLimited && (
          <Alert severity="info" sx={{ mb: 2, fontSize: '0.75rem' }}>
            Full run history requires OpenSearch. Showing last-run snapshot from database.
          </Alert>
        )}

        <Box sx={{ display: 'flex', gap: 1.5, mb: 2 }}>
          <FormControl size="small" sx={{ minWidth: 120 }}>
            <InputLabel>Status</InputLabel>
            <Select value={statusFilter} onChange={(e) => setStatusFilter(e.target.value)} label="Status">
              <MenuItem value="">All</MenuItem>
              <MenuItem value="success">Success</MenuItem>
              <MenuItem value="error">Error</MenuItem>
            </Select>
          </FormControl>
        </Box>

        <TableContainer>
          <Table size="small">
            <TableHead>
              <TableRow>
                <TableCell>Connector</TableCell>
                <TableCell>Status</TableCell>
                <TableCell>Started</TableCell>
                <TableCell>Finished</TableCell>
                <TableCell>Items</TableCell>
                <TableCell>Error</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {isLoading && [...Array(4)].map((_, i) => (
                <TableRow key={i}>
                  {[...Array(6)].map((_, j) => (
                    <TableCell key={j}><Box sx={{ height: 14, bgcolor: 'rgba(255,255,255,0.05)', borderRadius: 1 }} /></TableCell>
                  ))}
                </TableRow>
              ))}
              {!isLoading && data?.length === 0 && (
                <TableRow>
                  <TableCell colSpan={6} align="center" sx={{ py: 4 }}>
                    <Typography variant="body2" color="text.secondary">No connector runs found.</Typography>
                  </TableCell>
                </TableRow>
              )}
              {data?.map((run, idx) => {
                const sc = STATUS_COLOR[run.status] ?? STATUS_COLOR.success
                const items = run.evidence_count ?? run.item_count
                return (
                  <TableRow key={`${run.connector_id}-${idx}`} hover>
                    <TableCell>
                      <Typography variant="body2" fontFamily="monospace" fontSize="0.75rem">
                        {run.connector_name ?? run.connector_id.slice(0, 8) + '…'}
                      </Typography>
                      {run.history_limited && (
                        <Typography variant="caption" color="text.disabled" display="block">
                          last run only
                        </Typography>
                      )}
                    </TableCell>
                    <TableCell>
                      <Chip label={run.status} size="small" sx={{ fontSize: '0.65rem', height: 18, bgcolor: sc.bg, color: sc.fg }} />
                    </TableCell>
                    <TableCell>
                      <Tooltip title={run.started_at ? dayjs(run.started_at).format('DD MMM YYYY HH:mm:ss') : ''}>
                        <Typography variant="caption" color="text.secondary" noWrap>
                          {run.started_at ? dayjs(run.started_at).format('DD MMM HH:mm') : '—'}
                        </Typography>
                      </Tooltip>
                    </TableCell>
                    <TableCell>
                      <Typography variant="caption" color="text.secondary" noWrap>
                        {run.finished_at ? dayjs(run.finished_at).format('DD MMM HH:mm') : '—'}
                      </Typography>
                    </TableCell>
                    <TableCell>
                      <Typography variant="caption" color="text.secondary">
                        {items ?? '—'}
                      </Typography>
                    </TableCell>
                    <TableCell sx={{ maxWidth: 260 }}>
                      {run.error_message ? (
                        <Typography variant="caption" color="error.main" sx={{ whiteSpace: 'normal', wordBreak: 'break-word' }}>
                          {run.error_message}
                        </Typography>
                      ) : <Typography variant="caption" color="text.disabled">—</Typography>}
                    </TableCell>
                  </TableRow>
                )
              })}
            </TableBody>
          </Table>
        </TableContainer>
      </CardContent>
    </Card>
  )
}

// ---------------------------------------------------------------------------
// Main page
// ---------------------------------------------------------------------------

export default function Logs() {
  const [tab, setTab] = useState(0)
  const { user } = useAuth()

  if (!user || !['super_admin', 'admin'].includes(user.role)) {
    return (
      <Box sx={{ p: 3 }}>
        <Alert severity="error">Admin role required to access this page.</Alert>
      </Box>
    )
  }

  return (
    <Box>
      <PageHeader
        title="Logs"
        subtitle="Audit trail, feed run history, and connector run history"
      />

      <Box sx={{ borderBottom: 1, borderColor: 'divider', mb: 3 }}>
        <Tabs value={tab} onChange={(_, v) => setTab(v)} textColor="primary" indicatorColor="primary">
          <Tab label="Audit Trail"     icon={<HistoryOutlined fontSize="small" />}             iconPosition="start" sx={{ minHeight: 48 }} />
          <Tab label="Feed Runs"       icon={<SyncOutlined fontSize="small" />}                iconPosition="start" sx={{ minHeight: 48 }} />
          <Tab label="Connector Runs"  icon={<ElectricalServicesOutlined fontSize="small" />}  iconPosition="start" sx={{ minHeight: 48 }} />
        </Tabs>
      </Box>

      {tab === 0 && <AuditTrailTab />}
      {tab === 1 && <FeedRunsTab />}
      {tab === 2 && <ConnectorRunsTab />}
    </Box>
  )
}
