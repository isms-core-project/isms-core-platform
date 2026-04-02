import { useState } from 'react'
import {
  Alert, Box, Button, Chip, Dialog, DialogActions, DialogContent, DialogTitle,
  FormControl, IconButton, InputLabel, LinearProgress, MenuItem, Select,
  Skeleton, TextField, Tooltip, Typography,
} from '@mui/material'
import {
  AddOutlined, CheckCircleOutlined, DeleteOutlined, EditOutlined,
  ErrorOutlined, HourglassEmptyOutlined, ScheduleOutlined,
} from '@mui/icons-material'
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import dayjs from 'dayjs'
import {
  risksApi,
  type RemediationAction,
  type RemediationActionCreate,
} from '../api/risksApi'
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

function SummaryCards() {
  const { data, isLoading } = useQuery({ queryKey: ['remediation-summary'], queryFn: risksApi.remediationSummary })
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

// ── Action row ────────────────────────────────────────────────────────────────

function ActionRow({ action, onEdit, onDelete }: { action: RemediationAction; onEdit: () => void; onDelete: () => void }) {
  const overdue = isOverdue(action)
  return (
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
        <IconButton size="small" onClick={onEdit} sx={{ p: 0.5 }}><EditOutlined sx={{ fontSize: 15 }} /></IconButton>
        <IconButton size="small" onClick={onDelete} sx={{ p: 0.5, color: 'error.light' }}><DeleteOutlined sx={{ fontSize: 15 }} /></IconButton>
      </Box>
    </Box>
  )
}

// ── Main page ─────────────────────────────────────────────────────────────────

export default function Remediation() {
  const qc = useQueryClient()
  const [statusFilter, setStatusFilter] = useState('')
  const [dialogOpen, setDialogOpen] = useState(false)
  const [editing, setEditing] = useState<RemediationAction | undefined>()

  const { data, isLoading } = useQuery({
    queryKey: ['remediation', statusFilter],
    queryFn: () => risksApi.listRemediation(statusFilter ? { status: statusFilter } : {}),
  })

  const deleteMut = useMutation({
    mutationFn: (id: string) => risksApi.deleteRemediation(id),
    onSuccess: () => { qc.invalidateQueries({ queryKey: ['remediation'] }); qc.invalidateQueries({ queryKey: ['remediation-summary'] }) },
  })

  function openCreate() { setEditing(undefined); setDialogOpen(true) }
  function openEdit(a: RemediationAction) { setEditing(a); setDialogOpen(true) }

  return (
    <Box sx={{ p: 3, maxWidth: 1100, mx: 'auto' }}>
      <PageHeader
        title="Remediation Tracker"
        subtitle="Plan of Action and Milestones (POA&M) — ISO 27001:2022 §6.1.3"
        action={<Button variant="contained" size="small" startIcon={<AddOutlined />} onClick={openCreate}>New Action</Button>}
      />

      <SummaryCards />

      {/* Filters */}
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

      {/* Table header */}
      <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, px: 2, py: 0.75, bgcolor: 'action.hover', borderRadius: '8px 8px 0 0', border: '1px solid', borderColor: 'divider', borderBottom: 'none' }}>
        <Typography variant="caption" sx={{ flex: 3, fontWeight: 600, fontSize: '0.7rem', color: 'text.secondary', textTransform: 'uppercase' }}>Title / Risk</Typography>
        <Typography variant="caption" sx={{ flex: 1.5, fontWeight: 600, fontSize: '0.7rem', color: 'text.secondary', textTransform: 'uppercase' }}>Progress</Typography>
        <Typography variant="caption" sx={{ flex: 1, fontWeight: 600, fontSize: '0.7rem', color: 'text.secondary', textTransform: 'uppercase' }}>Status</Typography>
        <Typography variant="caption" sx={{ width: 52, fontWeight: 600, fontSize: '0.7rem', color: 'text.secondary', textTransform: 'uppercase' }}>Effort</Typography>
        <Typography variant="caption" sx={{ minWidth: 80, textAlign: 'right', fontWeight: 600, fontSize: '0.7rem', color: 'text.secondary', textTransform: 'uppercase' }}>ETA</Typography>
        <Box sx={{ width: 56 }} />
      </Box>

      <Box sx={{ border: '1px solid', borderColor: 'divider', borderRadius: '0 0 8px 8px', overflow: 'hidden' }}>
        {isLoading && [0, 1, 2, 3].map(i => (
          <Box key={i} sx={{ px: 2, py: 1.5, borderBottom: '1px solid', borderColor: 'divider' }}>
            <Skeleton height={20} />
          </Box>
        ))}

        {!isLoading && (!data || data.length === 0) && (
          <Box sx={{ py: 6, textAlign: 'center' }}>
            <Typography variant="body2" color="text.secondary">No remediation actions yet.</Typography>
            <Button variant="outlined" size="small" startIcon={<AddOutlined />} onClick={openCreate} sx={{ mt: 1.5 }}>
              Create first action
            </Button>
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
    </Box>
  )
}
