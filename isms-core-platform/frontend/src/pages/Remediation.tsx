import { useState } from 'react'
import {
  Alert, Box, Button, Chip, Dialog, DialogActions, DialogContent, DialogTitle,
  FormControl, IconButton, InputLabel, LinearProgress, MenuItem, Select,
  Skeleton, Snackbar, Tab, Tabs, TextField, Tooltip, Typography,
} from '@mui/material'
import {
  AddOutlined, CheckCircleOutlined, ConfirmationNumberOutlined, DeleteOutlined, EditOutlined,
  ErrorOutlined, HourglassEmptyOutlined, ScheduleOutlined, WarningAmberOutlined,
} from '@mui/icons-material'
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import dayjs from 'dayjs'
import {
  risksApi,
  type PoamItem,
  type RemediationAction,
  type RemediationActionCreate,
} from '../api/risksApi'
import { itsmApi } from '../api/itsmApi'
import { client } from '../api/client'
import { useProject } from '../store/ProjectContext'
import PageHeader from '../components/PageHeader'

// ── Helpers ───────────────────────────────────────────────────────────────────

const STATUS_META: Record<string, { label: string; color: string; icon: React.ReactNode }> = {
  planned:     { label: 'Planned',     color: '#9E9E9E', icon: <ScheduleOutlined sx={{ fontSize: 14 }} /> },
  in_progress: { label: 'In Progress', color: '#2196F3', icon: <HourglassEmptyOutlined sx={{ fontSize: 14 }} /> },
  completed:   { label: 'Completed',   color: '#4CAF50', icon: <CheckCircleOutlined sx={{ fontSize: 14 }} /> },
  cancelled:   { label: 'Cancelled',   color: '#F44336', icon: <ErrorOutlined sx={{ fontSize: 14 }} /> },
}

const EFFORT_COLOR: Record<string, string> = { low: '#4CAF50', medium: '#FF9800', high: '#F44336' }

function StatusChip({ status }: { status: string }) {
  const m = STATUS_META[status] ?? STATUS_META.planned
  return (
    <Chip
      icon={m.icon as any}
      label={m.label}
      size="small"
      sx={{ height: 20, fontSize: '0.62rem', fontWeight: 700, bgcolor: `${m.color}18`, color: m.color, border: `1px solid ${m.color}40`, '& .MuiChip-icon': { color: m.color, ml: '4px' } }}
    />
  )
}

function isOverdue(action: RemediationAction) {
  return action.eta && dayjs(action.eta).isBefore(dayjs(), 'day') && !['completed', 'cancelled'].includes(action.status)
}

// ── Summary cards ─────────────────────────────────────────────────────────────

function SummaryCards({ projectId }: { projectId?: string }) {
  const { data, isLoading } = useQuery({
    queryKey: ['remediation-summary', projectId],
    queryFn: () => risksApi.remediationSummary({ project_id: projectId }),
  })
  const cards = [
    { label: 'Total',       value: data?.total,       color: '#607D8B' },
    { label: 'Planned',     value: data?.planned,     color: '#9E9E9E' },
    { label: 'In Progress', value: data?.in_progress, color: '#2196F3' },
    { label: 'Completed',   value: data?.completed,   color: '#4CAF50' },
    { label: 'Overdue',     value: data?.overdue,     color: '#F44336' },
  ]
  return (
    <Box sx={{ display: 'flex', gap: 1.5, flexWrap: 'wrap', mb: 2.5 }}>
      {cards.map(c => (
        <Box key={c.label} sx={{ minWidth: 90, p: 1.5, borderRadius: 1.5, border: '1px solid', borderColor: `${c.color}30`, bgcolor: `${c.color}08` }}>
          {isLoading
            ? <Skeleton width={32} height={28} />
            : <Typography variant="h5" sx={{ fontWeight: 700, color: c.color, lineHeight: 1 }}>{c.value ?? 0}</Typography>}
          <Typography variant="caption" sx={{ fontSize: '0.65rem', color: 'text.secondary' }}>{c.label}</Typography>
        </Box>
      ))}
    </Box>
  )
}

// ── Action dialog ─────────────────────────────────────────────────────────────

function ActionDialog({ open, onClose, existing }: { open: boolean; onClose: () => void; existing?: RemediationAction }) {
  const qc = useQueryClient()
  const isEdit = !!existing

  const blank: RemediationActionCreate = { title: '', description: '', status: 'planned', effort: '', eta: '', progress: 0 }
  const [form, setForm] = useState<RemediationActionCreate>(existing ? {
    title: existing.title,
    description: existing.description ?? '',
    status: existing.status,
    effort: existing.effort ?? '',
    eta: existing.eta ?? '',
    progress: existing.progress,
    owner_id: existing.owner_id ?? undefined,
    risk_scenario_id: existing.risk_scenario_id ?? undefined,
  } : blank)
  const [error, setError] = useState('')

  const createMut = useMutation({
    mutationFn: (b: RemediationActionCreate) => risksApi.createRemediation(b),
    onSuccess: () => { qc.invalidateQueries({ queryKey: ['remediation'] }); qc.invalidateQueries({ queryKey: ['remediation-summary'] }); onClose() },
    onError: () => setError('Failed to save.'),
  })
  const updateMut = useMutation({
    mutationFn: (b: Partial<RemediationActionCreate>) => risksApi.updateRemediation(existing!.id, b),
    onSuccess: () => { qc.invalidateQueries({ queryKey: ['remediation'] }); qc.invalidateQueries({ queryKey: ['remediation-summary'] }); onClose() },
    onError: () => setError('Failed to save.'),
  })

  const isPending = createMut.isPending || updateMut.isPending
  const set = (k: keyof RemediationActionCreate, v: unknown) => setForm(f => ({ ...f, [k]: v }))

  function handleSubmit() {
    if (!form.title.trim()) { setError('Title is required.'); return }
    const body = { ...form, description: form.description || undefined, effort: (form.effort as string) || undefined, eta: (form.eta as string) || undefined }
    isEdit ? updateMut.mutate(body) : createMut.mutate(body)
  }

  return (
    <Dialog open={open} onClose={onClose} maxWidth="sm" fullWidth>
      <DialogTitle sx={{ pb: 0.5 }}>
        {isEdit ? 'Edit Action' : 'New Remediation Action'}
      </DialogTitle>
      <DialogContent sx={{ pt: '20px !important' }}>
        {error && <Alert severity="error" sx={{ mb: 2, py: 0.5 }}>{error}</Alert>}

        <TextField label="Title *" fullWidth size="small" sx={{ mb: 2 }}
          value={form.title} onChange={e => set('title', e.target.value)} />

        <TextField label="Description" fullWidth size="small" multiline rows={2} sx={{ mb: 2 }}
          value={form.description ?? ''} onChange={e => set('description', e.target.value)} />

        <Box sx={{ display: 'flex', gap: 1.5, mb: 2 }}>
          <FormControl size="small" sx={{ flex: 1 }}>
            <InputLabel>Status</InputLabel>
            <Select value={form.status ?? 'planned'} label="Status" onChange={e => set('status', e.target.value)}>
              {Object.entries(STATUS_META).map(([v, m]) => <MenuItem key={v} value={v}>{m.label}</MenuItem>)}
            </Select>
          </FormControl>
          <FormControl size="small" sx={{ flex: 1 }}>
            <InputLabel>Effort</InputLabel>
            <Select value={form.effort ?? ''} label="Effort" onChange={e => set('effort', e.target.value)}>
              <MenuItem value="">—</MenuItem>
              <MenuItem value="low">Low</MenuItem>
              <MenuItem value="medium">Medium</MenuItem>
              <MenuItem value="high">High</MenuItem>
            </Select>
          </FormControl>
        </Box>

        <Box sx={{ display: 'flex', gap: 1.5, mb: 2 }}>
          <TextField label="Target date" type="date" size="small" sx={{ flex: 1 }}
            InputLabelProps={{ shrink: true }}
            value={form.eta ?? ''} onChange={e => set('eta', e.target.value)} />
          <TextField label="Progress %" type="number" size="small" sx={{ flex: 1 }}
            inputProps={{ min: 0, max: 100 }}
            value={form.progress ?? 0} onChange={e => set('progress', Math.min(100, Math.max(0, Number(e.target.value))))} />
        </Box>
      </DialogContent>
      <DialogActions sx={{ px: 3, pb: 2 }}>
        <Button onClick={onClose} size="small">Cancel</Button>
        <Button variant="contained" size="small" onClick={handleSubmit} disabled={isPending}>
          {isPending ? 'Saving…' : isEdit ? 'Save' : 'Create'}
        </Button>
      </DialogActions>
    </Dialog>
  )
}

// ── ITSM push dialog ──────────────────────────────────────────────────────────

interface ItsmConnector { id: string; name: string; source_system: string }
interface PushResult { ticket_id: string; url: string | null; already_exists: boolean }

function ItsmPushDialog({
  open, onClose, actionId, onSuccess,
}: { open: boolean; onClose: () => void; actionId: string; onSuccess: (result: PushResult, connectorName: string) => void }) {
  const [connectorId, setConnectorId] = useState('')
  const [error, setError] = useState('')

  const { data: connectors = [], isLoading } = useQuery<ItsmConnector[]>({
    queryKey: ['itsm-connectors'],
    queryFn: () => client.get('/connectors').then(r =>
      (r.data as ItsmConnector[]).filter(c => ['jira', 'servicenow'].includes(c.source_system))
    ),
    enabled: open,
  })

  const pushMut = useMutation({
    mutationFn: () => itsmApi.pushRemediation(connectorId, actionId),
    onSuccess: (result) => {
      const conn = connectors.find(c => c.id === connectorId)
      onSuccess(result, conn?.name ?? connectorId)
      onClose()
    },
    onError: () => setError('Failed to push to ITSM.'),
  })

  function handlePush() {
    if (!connectorId) { setError('Select a connector.'); return }
    setError('')
    pushMut.mutate()
  }

  return (
    <Dialog open={open} onClose={onClose} maxWidth="xs" fullWidth>
      <DialogTitle sx={{ pb: 0.5 }}>Push to ITSM</DialogTitle>
      <DialogContent sx={{ pt: '20px !important' }}>
        {error && <Alert severity="error" sx={{ mb: 2, py: 0.5 }}>{error}</Alert>}
        {isLoading ? (
          <Skeleton height={40} />
        ) : connectors.length === 0 ? (
          <Alert severity="warning" sx={{ py: 0.5 }}>
            No Jira or ServiceNow connectors configured.
          </Alert>
        ) : (
          <FormControl size="small" fullWidth>
            <InputLabel>Connector</InputLabel>
            <Select value={connectorId} label="Connector" onChange={e => setConnectorId(e.target.value)}>
              {connectors.map(c => (
                <MenuItem key={c.id} value={c.id}>
                  {c.name}
                  <Typography component="span" variant="caption" sx={{ ml: 1, color: 'text.disabled' }}>
                    ({c.source_system})
                  </Typography>
                </MenuItem>
              ))}
            </Select>
          </FormControl>
        )}
      </DialogContent>
      <DialogActions sx={{ px: 3, pb: 2 }}>
        <Button onClick={onClose} size="small">Cancel</Button>
        <Button
          variant="contained" size="small"
          onClick={handlePush}
          disabled={pushMut.isPending || connectors.length === 0}
        >
          {pushMut.isPending ? 'Pushing…' : 'Push'}
        </Button>
      </DialogActions>
    </Dialog>
  )
}

// ── Action row ────────────────────────────────────────────────────────────────

function ActionRow({
  action, onEdit, onDelete,
}: { action: RemediationAction; onEdit: () => void; onDelete: () => void }) {
  const overdue = isOverdue(action)
  const [itsmOpen, setItsmOpen] = useState(false)
  const [snackbar, setSnackbar] = useState<{ open: boolean; message: string; url: string | null }>({
    open: false, message: '', url: null,
  })

  function handleItsmSuccess(result: PushResult, connectorName: string) {
    const prefix = result.already_exists ? 'Already in' : 'Pushed to'
    setSnackbar({
      open: true,
      message: `${prefix} ${connectorName}: ${result.ticket_id}`,
      url: result.url,
    })
  }

  return (
    <>
      <Box sx={{
        display: 'flex', alignItems: 'center', gap: 1, px: 2, py: 1.25,
        borderBottom: '1px solid', borderColor: 'divider',
        '&:hover': { bgcolor: 'action.hover' },
        bgcolor: overdue ? '#F4433606' : 'transparent',
      }}>
        <Box sx={{ flex: 3, minWidth: 0 }}>
          <Typography variant="body2" sx={{ fontWeight: 500, fontSize: '0.82rem', color: overdue ? 'error.main' : 'text.primary' }}>
            {action.title}
          </Typography>
          {action.risk_name && (
            <Typography variant="caption" sx={{ fontSize: '0.65rem', color: 'text.disabled' }}>
              Risk: {action.risk_name}
            </Typography>
          )}
        </Box>

        <Box sx={{ flex: 1.5, display: 'flex', alignItems: 'center', gap: 1 }}>
          <LinearProgress
            variant="determinate"
            value={action.progress}
            sx={{ flex: 1, height: 4, borderRadius: 2, bgcolor: 'action.hover', '& .MuiLinearProgress-bar': { bgcolor: STATUS_META[action.status]?.color ?? '#9E9E9E' } }}
          />
          <Typography variant="caption" sx={{ fontSize: '0.65rem', color: 'text.secondary', minWidth: 28 }}>
            {action.progress}%
          </Typography>
        </Box>

        <Box sx={{ flex: 1 }}>
          <StatusChip status={action.status} />
        </Box>

        {action.effort ? (
          <Chip label={action.effort} size="small" sx={{ height: 18, fontSize: '0.6rem', bgcolor: `${EFFORT_COLOR[action.effort]}18`, color: EFFORT_COLOR[action.effort], border: `1px solid ${EFFORT_COLOR[action.effort]}40` }} />
        ) : (
          <Box sx={{ width: 52 }} />
        )}

        <Box sx={{ minWidth: 80, textAlign: 'right' }}>
          {action.eta && (
            <Tooltip title={overdue ? 'Overdue' : ''}>
              <Typography variant="caption" sx={{ fontSize: '0.65rem', color: overdue ? 'error.main' : 'text.secondary', fontWeight: overdue ? 600 : 400 }}>
                {dayjs(action.eta).format('D MMM YY')}
              </Typography>
            </Tooltip>
          )}
        </Box>

        <Box sx={{ display: 'flex', gap: 0.25 }}>
          <Tooltip title="Push to ITSM">
            <IconButton size="small" onClick={() => setItsmOpen(true)} sx={{ p: 0.5, color: 'text.disabled' }}>
              <ConfirmationNumberOutlined sx={{ fontSize: 15 }} />
            </IconButton>
          </Tooltip>
          <IconButton size="small" onClick={onEdit} sx={{ p: 0.5 }}><EditOutlined sx={{ fontSize: 15 }} /></IconButton>
          <IconButton size="small" onClick={onDelete} sx={{ p: 0.5, color: 'error.light' }}><DeleteOutlined sx={{ fontSize: 15 }} /></IconButton>
        </Box>
      </Box>

      <ItsmPushDialog
        open={itsmOpen}
        onClose={() => setItsmOpen(false)}
        actionId={action.id}
        onSuccess={handleItsmSuccess}
      />

      <Snackbar
        open={snackbar.open}
        autoHideDuration={6000}
        onClose={() => setSnackbar(s => ({ ...s, open: false }))}
        message={
          snackbar.url ? (
            <span>
              {snackbar.message}{' '}
              <a href={snackbar.url} target="_blank" rel="noreferrer"
                style={{ color: '#90CAF9', fontWeight: 600 }}>
                View ticket
              </a>
            </span>
          ) : snackbar.message
        }
        anchorOrigin={{ vertical: 'bottom', horizontal: 'right' }}
      />
    </>
  )
}

// ── POA&M view ────────────────────────────────────────────────────────────────

const SOURCE_META: Record<string, { label: string; color: string }> = {
  risk: { label: 'Risk',       color: '#F44336' },
  gap:  { label: 'Gap',        color: '#FF9800' },
  tprm: { label: 'TPRM',      color: '#9C27B0' },
}

function PoamSummaryCards() {
  const { data, isLoading } = useQuery({
    queryKey: ['poam-summary'],
    queryFn: risksApi.poamSummary,
  })
  const cards = [
    { label: 'Total Open',    value: data?.total,      color: '#607D8B' },
    { label: 'Overdue',       value: data?.overdue,    color: '#F44336' },
    { label: 'Risk Treatments', value: data?.risk_count, color: '#F44336' },
    { label: 'Open Gaps',     value: data?.gap_count,  color: '#FF9800' },
    { label: 'TPRM Findings', value: data?.tprm_count, color: '#9C27B0' },
  ]
  return (
    <Box sx={{ display: 'flex', gap: 1.5, flexWrap: 'wrap', mb: 2.5 }}>
      {cards.map(c => (
        <Box key={c.label} sx={{ minWidth: 100, p: 1.5, borderRadius: 1.5, border: '1px solid', borderColor: `${c.color}30`, bgcolor: `${c.color}08` }}>
          {isLoading
            ? <Skeleton width={32} height={28} />
            : <Typography variant="h5" sx={{ fontWeight: 700, color: c.color, lineHeight: 1 }}>{c.value ?? 0}</Typography>}
          <Typography variant="caption" sx={{ fontSize: '0.65rem', color: 'text.secondary' }}>{c.label}</Typography>
        </Box>
      ))}
    </Box>
  )
}

function PoamRow({ item }: { item: PoamItem }) {
  const src = SOURCE_META[item.source] ?? { label: item.source, color: '#607D8B' }
  return (
    <Box sx={{
      display: 'flex', alignItems: 'center', gap: 1, px: 2, py: 1.25,
      borderBottom: '1px solid', borderColor: 'divider',
      '&:hover': { bgcolor: 'action.hover' },
      bgcolor: item.is_overdue ? '#F4433606' : 'transparent',
    }}>
      <Chip
        label={src.label}
        size="small"
        sx={{ height: 18, fontSize: '0.6rem', fontWeight: 700, minWidth: 40,
          bgcolor: `${src.color}18`, color: src.color, border: `1px solid ${src.color}40` }}
      />
      <Box sx={{ flex: 3, minWidth: 0 }}>
        <Typography variant="body2" sx={{ fontWeight: 500, fontSize: '0.82rem', color: item.is_overdue ? 'error.main' : 'text.primary', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
          {item.title}
        </Typography>
        {item.description && (
          <Typography variant="caption" sx={{ fontSize: '0.65rem', color: 'text.disabled', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap', display: 'block' }}>
            {item.description}
          </Typography>
        )}
      </Box>
      {item.control_code ? (
        <Chip label={item.control_code} size="small" sx={{ height: 18, fontSize: '0.6rem', fontFamily: 'monospace', bgcolor: 'action.hover' }} />
      ) : <Box sx={{ width: 60 }} />}
      <Box sx={{ minWidth: 80 }}>
        <Typography variant="caption" sx={{ fontSize: '0.65rem', color: 'text.secondary' }}>
          {item.status.replace('_', ' ')}
        </Typography>
      </Box>
      {item.severity && (
        <Typography variant="caption" sx={{ fontSize: '0.65rem', color: 'text.disabled', minWidth: 60 }}>
          {item.severity}
        </Typography>
      )}
      <Box sx={{ minWidth: 80, textAlign: 'right' }}>
        {item.eta && (
          <Tooltip title={item.is_overdue ? 'Overdue' : ''}>
            <Typography variant="caption" sx={{ fontSize: '0.65rem', color: item.is_overdue ? 'error.main' : 'text.secondary', fontWeight: item.is_overdue ? 600 : 400, display: 'flex', alignItems: 'center', gap: 0.5, justifyContent: 'flex-end' }}>
              {item.is_overdue && <WarningAmberOutlined sx={{ fontSize: 11 }} />}
              {dayjs(item.eta).format('D MMM YY')}
            </Typography>
          </Tooltip>
        )}
      </Box>
    </Box>
  )
}

function PoamView() {
  const [sourceFilter, setSourceFilter] = useState<string>('')

  const { data, isLoading } = useQuery({
    queryKey: ['poam', sourceFilter],
    queryFn: () => risksApi.listPoam(sourceFilter ? { source: sourceFilter } : undefined),
  })

  const sources = [
    { value: '',     label: 'All Sources' },
    { value: 'risk', label: 'Risk Treatments' },
    { value: 'gap',  label: 'Open Gaps' },
    { value: 'tprm', label: 'TPRM Findings' },
  ]

  return (
    <Box>
      <PoamSummaryCards />

      {/* Source filter pills */}
      <Box sx={{ display: 'flex', gap: 1, mb: 2, flexWrap: 'wrap' }}>
        {sources.map(s => (
          <Chip
            key={s.value}
            label={s.label}
            size="small"
            onClick={() => setSourceFilter(s.value)}
            variant={sourceFilter === s.value ? 'filled' : 'outlined'}
            sx={{
              fontWeight: sourceFilter === s.value ? 700 : 400,
              ...(s.value && sourceFilter === s.value && {
                bgcolor: `${SOURCE_META[s.value]?.color}18`,
                color: SOURCE_META[s.value]?.color,
                borderColor: `${SOURCE_META[s.value]?.color}60`,
              }),
            }}
          />
        ))}
        <Typography variant="caption" sx={{ ml: 'auto', color: 'text.disabled', alignSelf: 'center' }}>
          {data?.length ?? 0} item{data?.length !== 1 ? 's' : ''}
        </Typography>
      </Box>

      {/* Table header */}
      <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, px: 2, py: 0.75, bgcolor: 'action.hover', borderRadius: '8px 8px 0 0', border: '1px solid', borderColor: 'divider', borderBottom: 'none' }}>
        <Typography variant="caption" sx={{ width: 40, fontWeight: 600, fontSize: '0.7rem', color: 'text.secondary', textTransform: 'uppercase' }}>Source</Typography>
        <Typography variant="caption" sx={{ flex: 3, fontWeight: 600, fontSize: '0.7rem', color: 'text.secondary', textTransform: 'uppercase' }}>Title</Typography>
        <Typography variant="caption" sx={{ width: 60, fontWeight: 600, fontSize: '0.7rem', color: 'text.secondary', textTransform: 'uppercase' }}>Control</Typography>
        <Typography variant="caption" sx={{ minWidth: 80, fontWeight: 600, fontSize: '0.7rem', color: 'text.secondary', textTransform: 'uppercase' }}>Status</Typography>
        <Typography variant="caption" sx={{ minWidth: 60, fontWeight: 600, fontSize: '0.7rem', color: 'text.secondary', textTransform: 'uppercase' }}>Priority</Typography>
        <Typography variant="caption" sx={{ minWidth: 80, textAlign: 'right', fontWeight: 600, fontSize: '0.7rem', color: 'text.secondary', textTransform: 'uppercase' }}>ETA</Typography>
      </Box>

      <Box sx={{ border: '1px solid', borderColor: 'divider', borderRadius: '0 0 8px 8px', overflow: 'hidden' }}>
        {isLoading && [0, 1, 2, 3].map(i => (
          <Box key={i} sx={{ px: 2, py: 1.5, borderBottom: '1px solid', borderColor: 'divider' }}>
            <Skeleton height={20} />
          </Box>
        ))}
        {!isLoading && (!data || data.length === 0) && (
          <Box sx={{ py: 6, textAlign: 'center' }}>
            <Typography variant="body2" color="text.secondary">No open items.</Typography>
          </Box>
        )}
        {data?.map(item => <PoamRow key={`${item.source}-${item.id}`} item={item} />)}
      </Box>
    </Box>
  )
}

// ── Main page ─────────────────────────────────────────────────────────────────

export default function Remediation() {
  const qc = useQueryClient()
  const [tab, setTab] = useState(0)
  const [statusFilter, setStatusFilter] = useState('')
  const [dialogOpen, setDialogOpen] = useState(false)
  const [editing, setEditing] = useState<RemediationAction | undefined>()

  const { activeProject } = useProject()
  const projectId = activeProject?.id

  const { data, isLoading } = useQuery({
    queryKey: ['remediation', statusFilter, projectId],
    queryFn: () => risksApi.listRemediation({
      ...(statusFilter ? { status: statusFilter } : {}),
      project_id: projectId,
    }),
    enabled: tab === 0,
  })

  const deleteMut = useMutation({
    mutationFn: (id: string) => risksApi.deleteRemediation(id),
    onSuccess: () => {
      qc.invalidateQueries({ queryKey: ['remediation'] })
      qc.invalidateQueries({ queryKey: ['remediation-summary'] })
    },
  })

  function openCreate() { setEditing(undefined); setDialogOpen(true) }
  function openEdit(a: RemediationAction) { setEditing(a); setDialogOpen(true) }

  return (
    <Box sx={{ p: 3 }}>
      <PageHeader
        title="Remediation Tracker"
        subtitle="Plan of Action and Milestones (POA&M) — ISO 27001:2022 §6.1.3"
        actions={
          tab === 0 ? (
            <Tooltip title={!activeProject ? 'Select a project first to create remediation actions' : ''}>
              <span>
                <Button variant="contained" size="small" startIcon={<AddOutlined />}
                  onClick={openCreate} disabled={!activeProject}>
                  New Action
                </Button>
              </span>
            </Tooltip>
          ) : null
        }
      />

      <Tabs value={tab} onChange={(_, v) => setTab(v)} sx={{ mb: 2.5, borderBottom: 1, borderColor: 'divider' }}>
        <Tab label="Risk Treatments" sx={{ fontSize: '0.8rem', textTransform: 'none', minHeight: 40 }} />
        <Tab label="All Sources (POA&M)" sx={{ fontSize: '0.8rem', textTransform: 'none', minHeight: 40 }} />
      </Tabs>

      {tab === 0 && (
        <>
          {activeProject && (
            <Alert severity="info" sx={{ mb: 2, py: 0.5, fontSize: '0.8rem' }}>
              Showing actions for project: <strong>{activeProject.name}</strong>
              {activeProject.organisation_name ? ` — ${activeProject.organisation_name}` : ''}
            </Alert>
          )}

          <SummaryCards projectId={projectId} />

          <Box sx={{ display: 'flex', gap: 1.5, mb: 2, alignItems: 'center' }}>
            <FormControl size="small" sx={{ minWidth: 150 }}>
              <InputLabel>Status</InputLabel>
              <Select value={statusFilter} label="Status" onChange={e => setStatusFilter(e.target.value)}>
                <MenuItem value="">All statuses</MenuItem>
                {Object.entries(STATUS_META).map(([v, m]) => <MenuItem key={v} value={v}>{m.label}</MenuItem>)}
              </Select>
            </FormControl>
            {statusFilter && (
              <Button size="small" onClick={() => setStatusFilter('')} sx={{ textTransform: 'none', fontSize: '0.75rem' }}>
                Clear
              </Button>
            )}
            <Typography variant="caption" sx={{ ml: 'auto', color: 'text.disabled' }}>
              {data?.length ?? 0} action{data?.length !== 1 ? 's' : ''}
            </Typography>
          </Box>

          <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, px: 2, py: 0.75, bgcolor: 'action.hover', borderRadius: '8px 8px 0 0', border: '1px solid', borderColor: 'divider', borderBottom: 'none' }}>
            <Typography variant="caption" sx={{ flex: 3, fontWeight: 600, fontSize: '0.7rem', color: 'text.secondary', textTransform: 'uppercase' }}>Title / Risk</Typography>
            <Typography variant="caption" sx={{ flex: 1.5, fontWeight: 600, fontSize: '0.7rem', color: 'text.secondary', textTransform: 'uppercase' }}>Progress</Typography>
            <Typography variant="caption" sx={{ flex: 1, fontWeight: 600, fontSize: '0.7rem', color: 'text.secondary', textTransform: 'uppercase' }}>Status</Typography>
            <Typography variant="caption" sx={{ width: 52, fontWeight: 600, fontSize: '0.7rem', color: 'text.secondary', textTransform: 'uppercase' }}>Effort</Typography>
            <Typography variant="caption" sx={{ minWidth: 80, textAlign: 'right', fontWeight: 600, fontSize: '0.7rem', color: 'text.secondary', textTransform: 'uppercase' }}>ETA</Typography>
            <Box sx={{ width: 80 }} />
          </Box>

          <Box sx={{ border: '1px solid', borderColor: 'divider', borderRadius: '0 0 8px 8px', overflow: 'hidden' }}>
            {isLoading && [0, 1, 2, 3].map(i => (
              <Box key={i} sx={{ px: 2, py: 1.5, borderBottom: '1px solid', borderColor: 'divider' }}>
                <Skeleton height={20} />
              </Box>
            ))}
            {!isLoading && (!data || data.length === 0) && (
              <Box sx={{ py: 6, textAlign: 'center' }}>
                <Typography variant="body2" color="text.secondary">
                  {activeProject ? 'No remediation actions yet.' : 'Select a project to create remediation actions.'}
                </Typography>
                {activeProject && (
                  <Button variant="outlined" size="small" startIcon={<AddOutlined />} onClick={openCreate} sx={{ mt: 1.5 }}>
                    Create first action
                  </Button>
                )}
              </Box>
            )}
            {data?.map(a => (
              <ActionRow
                key={a.id}
                action={a}
                onEdit={() => openEdit(a)}
                onDelete={() => { if (confirm(`Delete "${a.title}"?`)) deleteMut.mutate(a.id) }}
              />
            ))}
          </Box>

          <ActionDialog
            open={dialogOpen}
            onClose={() => setDialogOpen(false)}
            existing={editing}
          />
        </>
      )}

      {tab === 1 && <PoamView />}
    </Box>
  )
}
