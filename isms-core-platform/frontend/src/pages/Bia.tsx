import { useState } from 'react'
import {
  Alert, Box, Button, Chip, Dialog, DialogActions, DialogContent, DialogTitle,
  FormControl, FormControlLabel, IconButton, InputLabel, MenuItem, Select,
  Skeleton, Slider, Switch, TextField, Tooltip, Typography,
} from '@mui/material'
import {
  AddOutlined, CheckCircleOutlined, DeleteOutlined, EditOutlined,
} from '@mui/icons-material'
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import dayjs from 'dayjs'
import { biaApi, type BIARecord, type BIACreate } from '../api/biaApi'
import { useProject } from '../store/ProjectContext'
import PageHeader from '../components/PageHeader'

// ── Helpers ───────────────────────────────────────────────────────────────────

const ASSET_TYPES = ['process', 'system', 'service', 'data']
const ASSET_TYPE_COLORS: Record<string, string> = {
  process: '#2196F3',
  system:  '#9C27B0',
  service: '#FF9800',
  data:    '#4CAF50',
}

function impactColor(score: number): string {
  if (score <= 2) return '#4CAF50'
  if (score === 3) return '#FF9800'
  return '#F44336'
}

function AssetTypeChip({ type }: { type: string }) {
  const color = ASSET_TYPE_COLORS[type] ?? '#607D8B'
  return (
    <Chip
      label={type.charAt(0).toUpperCase() + type.slice(1)}
      size="small"
      sx={{
        height: 20, fontSize: '0.62rem', fontWeight: 700,
        bgcolor: `${color}18`, color, border: `1px solid ${color}40`,
      }}
    />
  )
}

function ImpactDot({ score }: { score: number | null }) {
  if (score == null) return <Typography variant="caption" sx={{ color: 'text.disabled' }}>—</Typography>
  const color = impactColor(score)
  return (
    <Tooltip title={`Avg impact: ${score.toFixed(1)} / 5`}>
      <Box sx={{ display: 'inline-flex', alignItems: 'center', gap: 0.5 }}>
        <Box sx={{ width: 8, height: 8, borderRadius: '50%', bgcolor: color }} />
        <Typography variant="caption" sx={{ fontSize: '0.7rem', color, fontWeight: 600 }}>
          {score.toFixed(1)}
        </Typography>
      </Box>
    </Tooltip>
  )
}

// ── Summary cards ─────────────────────────────────────────────────────────────

function SummaryCards({ projectId }: { projectId?: string }) {
  const { data, isLoading } = useQuery({
    queryKey: ['bia-summary', projectId],
    queryFn: () => biaApi.summary({ project_id: projectId }),
  })
  const cards = [
    { label: 'Total Assets',       value: data?.total,       color: '#607D8B', suffix: '' },
    { label: 'Recovery Tested',    value: data?.tested_pct != null ? `${Math.round(data.tested_pct)}%` : null, color: '#4CAF50', suffix: '' },
    { label: 'High Impact',        value: data?.high_impact, color: '#F44336', suffix: '' },
    { label: 'RTO Missing',        value: data?.rto_missing, color: '#FF9800', suffix: '' },
  ]
  return (
    <Box sx={{ display: 'flex', gap: 1.5, flexWrap: 'wrap', mb: 2.5 }}>
      {cards.map(c => (
        <Box
          key={c.label}
          sx={{
            minWidth: 100, p: 1.5, borderRadius: 1.5,
            border: '1px solid', borderColor: `${c.color}30`, bgcolor: `${c.color}08`,
          }}
        >
          {isLoading
            ? <Skeleton width={32} height={28} />
            : <Typography variant="h5" sx={{ fontWeight: 700, color: c.color, lineHeight: 1 }}>
                {c.value ?? 0}{c.suffix}
              </Typography>}
          <Typography variant="caption" sx={{ fontSize: '0.65rem', color: 'text.secondary' }}>{c.label}</Typography>
        </Box>
      ))}
    </Box>
  )
}

// ── BIA dialog ────────────────────────────────────────────────────────────────

const BLANK: BIACreate = {
  asset_name: '', asset_type: 'process',
  financial_impact: 3, operational_impact: 3, reputational_impact: 3, regulatory_impact: 3,
  recovery_tested: false,
}

const IMPACT_DIMS: { key: keyof BIACreate; label: string }[] = [
  { key: 'financial_impact',     label: 'Financial impact' },
  { key: 'operational_impact',   label: 'Operational impact' },
  { key: 'reputational_impact',  label: 'Reputational impact' },
  { key: 'regulatory_impact',    label: 'Regulatory impact' },
]

function BIADialog({
  open, onClose, existing, projectId,
}: { open: boolean; onClose: () => void; existing?: BIARecord; projectId?: string }) {
  const qc = useQueryClient()
  const isEdit = !!existing

  const [form, setForm] = useState<BIACreate>(existing ? {
    asset_name: existing.asset_name,
    asset_type: existing.asset_type,
    project_id: existing.project_id ?? undefined,
    rto_hours: existing.rto_hours ?? undefined,
    rpo_hours: existing.rpo_hours ?? undefined,
    mtpd_hours: existing.mtpd_hours ?? undefined,
    financial_impact: existing.financial_impact ?? 3,
    operational_impact: existing.operational_impact ?? 3,
    reputational_impact: existing.reputational_impact ?? 3,
    regulatory_impact: existing.regulatory_impact ?? 3,
    recovery_tested: existing.recovery_tested,
    last_tested_date: existing.last_tested_date ?? undefined,
    continuity_plan_ref: existing.continuity_plan_ref ?? undefined,
    notes: existing.notes ?? undefined,
  } : { ...BLANK, project_id: projectId })
  const [error, setError] = useState('')

  const invalidate = () => {
    qc.invalidateQueries({ queryKey: ['bia'] })
    qc.invalidateQueries({ queryKey: ['bia-summary'] })
  }
  const createMut = useMutation({
    mutationFn: (b: BIACreate) => biaApi.create(b),
    onSuccess: () => { invalidate(); onClose() },
    onError: () => setError('Failed to save.'),
  })
  const updateMut = useMutation({
    mutationFn: (b: Partial<BIACreate>) => biaApi.update(existing!.id, b),
    onSuccess: () => { invalidate(); onClose() },
    onError: () => setError('Failed to save.'),
  })

  const isPending = createMut.isPending || updateMut.isPending
  const set = (k: keyof BIACreate, v: unknown) => setForm(f => ({ ...f, [k]: v }))

  function handleSubmit() {
    if (!form.asset_name.trim()) { setError('Asset name is required.'); return }
    const body: BIACreate = {
      ...form,
      continuity_plan_ref: (form.continuity_plan_ref as string) || undefined,
      notes: (form.notes as string) || undefined,
      last_tested_date: (form.last_tested_date as string) || undefined,
    }
    isEdit ? updateMut.mutate(body) : createMut.mutate(body)
  }

  return (
    <Dialog open={open} onClose={onClose} maxWidth="sm" fullWidth>
      <DialogTitle sx={{ pb: 0.5 }}>{isEdit ? 'Edit BIA Record' : 'New BIA Record'}</DialogTitle>
      <DialogContent sx={{ pt: '20px !important' }}>
        {error && <Alert severity="error" sx={{ mb: 2, py: 0.5 }}>{error}</Alert>}

        <Box sx={{ display: 'flex', gap: 1.5, mb: 2 }}>
          <TextField label="Asset name *" size="small" sx={{ flex: 2 }}
            value={form.asset_name} onChange={e => set('asset_name', e.target.value)} />
          <FormControl size="small" sx={{ flex: 1 }}>
            <InputLabel>Type</InputLabel>
            <Select value={form.asset_type ?? 'process'} label="Type"
              onChange={e => set('asset_type', e.target.value)}>
              {ASSET_TYPES.map(t => <MenuItem key={t} value={t}>{t.charAt(0).toUpperCase() + t.slice(1)}</MenuItem>)}
            </Select>
          </FormControl>
        </Box>

        {/* RTO / RPO / MTPD */}
        <Box sx={{ mb: 1.5, pb: 0.75, borderBottom: '1px solid', borderColor: 'divider' }}>
          <Typography variant="caption" sx={{ fontWeight: 700, color: 'text.secondary', textTransform: 'uppercase', fontSize: '0.65rem' }}>
            Recovery objectives (hours)
          </Typography>
        </Box>
        <Box sx={{ display: 'flex', gap: 1.5, mb: 2, mt: 1 }}>
          <TextField label="RTO" type="number" size="small" sx={{ flex: 1 }}
            inputProps={{ min: 0 }}
            value={form.rto_hours ?? ''} onChange={e => set('rto_hours', e.target.value ? Number(e.target.value) : undefined)} />
          <TextField label="RPO" type="number" size="small" sx={{ flex: 1 }}
            inputProps={{ min: 0 }}
            value={form.rpo_hours ?? ''} onChange={e => set('rpo_hours', e.target.value ? Number(e.target.value) : undefined)} />
          <TextField label="MTPD" type="number" size="small" sx={{ flex: 1 }}
            inputProps={{ min: 0 }}
            value={form.mtpd_hours ?? ''} onChange={e => set('mtpd_hours', e.target.value ? Number(e.target.value) : undefined)} />
        </Box>

        {/* Impact sliders */}
        <Box sx={{ mb: 1.5, pb: 0.75, borderBottom: '1px solid', borderColor: 'divider' }}>
          <Typography variant="caption" sx={{ fontWeight: 700, color: 'text.secondary', textTransform: 'uppercase', fontSize: '0.65rem' }}>
            Business impact (1 = low, 5 = critical)
          </Typography>
        </Box>
        {IMPACT_DIMS.map(({ key, label }) => {
          const val = (form[key] as number) ?? 3
          return (
            <Box key={key} sx={{ display: 'flex', alignItems: 'center', gap: 2, mb: 1.5 }}>
              <Typography variant="caption" sx={{ minWidth: 150, fontSize: '0.75rem', color: 'text.secondary' }}>
                {label}
              </Typography>
              <Slider
                size="small"
                min={1} max={5} step={1}
                value={val}
                onChange={(_, v) => set(key, v as number)}
                marks
                sx={{ flex: 1, color: impactColor(val) }}
              />
              <Box sx={{
                minWidth: 24, height: 24, borderRadius: '50%',
                bgcolor: impactColor(val), display: 'flex', alignItems: 'center', justifyContent: 'center',
              }}>
                <Typography variant="caption" sx={{ fontSize: '0.65rem', fontWeight: 700, color: '#fff' }}>{val}</Typography>
              </Box>
            </Box>
          )
        })}

        {/* Recovery tested */}
        <Box sx={{ mb: 2, display: 'flex', alignItems: 'center', gap: 2 }}>
          <FormControlLabel
            control={
              <Switch size="small" checked={!!form.recovery_tested}
                onChange={e => set('recovery_tested', e.target.checked)} />
            }
            label={<Typography variant="caption" sx={{ fontSize: '0.78rem' }}>Recovery tested</Typography>}
          />
          {form.recovery_tested && (
            <TextField label="Last tested date" type="date" size="small" sx={{ flex: 1 }}
              InputLabelProps={{ shrink: true }}
              value={form.last_tested_date ?? ''}
              onChange={e => set('last_tested_date', e.target.value)} />
          )}
        </Box>

        <TextField label="Continuity plan ref" fullWidth size="small" sx={{ mb: 2 }}
          value={form.continuity_plan_ref ?? ''} onChange={e => set('continuity_plan_ref', e.target.value)} />

        <TextField label="Notes" fullWidth size="small" multiline rows={2}
          value={form.notes ?? ''} onChange={e => set('notes', e.target.value)} />
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

// ── BIA row ───────────────────────────────────────────────────────────────────

function BIARow({
  record, onEdit, onDelete,
}: { record: BIARecord; onEdit: () => void; onDelete: () => void }) {
  return (
    <Box sx={{
      display: 'flex', alignItems: 'center', gap: 1, px: 2, py: 1.25,
      borderBottom: '1px solid', borderColor: 'divider',
      '&:hover': { bgcolor: 'action.hover' },
    }}>
      {/* Asset name */}
      <Box sx={{ flex: 3, minWidth: 0 }}>
        <Typography variant="body2" sx={{ fontWeight: 500, fontSize: '0.82rem' }} noWrap>
          {record.asset_name}
        </Typography>
        {record.continuity_plan_ref && (
          <Typography variant="caption" sx={{ fontSize: '0.65rem', color: 'text.disabled' }}>
            Plan: {record.continuity_plan_ref}
          </Typography>
        )}
      </Box>

      {/* Type */}
      <Box sx={{ width: 80 }}>
        <AssetTypeChip type={record.asset_type} />
      </Box>

      {/* RTO */}
      <Box sx={{ width: 60, textAlign: 'center' }}>
        <Typography variant="caption" sx={{ fontSize: '0.72rem', color: record.rto_hours == null ? 'text.disabled' : '#FF9800' }}>
          {record.rto_hours != null ? `${record.rto_hours}h` : '—'}
        </Typography>
      </Box>

      {/* RPO */}
      <Box sx={{ width: 60, textAlign: 'center' }}>
        <Typography variant="caption" sx={{ fontSize: '0.72rem', color: record.rpo_hours == null ? 'text.disabled' : 'text.secondary' }}>
          {record.rpo_hours != null ? `${record.rpo_hours}h` : '—'}
        </Typography>
      </Box>

      {/* Impact */}
      <Box sx={{ width: 70, textAlign: 'center' }}>
        <ImpactDot score={record.avg_impact} />
      </Box>

      {/* Tested */}
      <Box sx={{ width: 80, textAlign: 'center' }}>
        {record.recovery_tested ? (
          <Tooltip title={record.last_tested_date ? `Tested ${dayjs(record.last_tested_date).format('D MMM YY')}` : 'Tested'}>
            <CheckCircleOutlined sx={{ fontSize: 16, color: '#4CAF50' }} />
          </Tooltip>
        ) : (
          <Box sx={{ width: 16, height: 16, borderRadius: '50%', bgcolor: 'action.hover', display: 'inline-block' }} />
        )}
      </Box>

      {/* Actions */}
      <Box sx={{ display: 'flex', gap: 0.25 }}>
        <IconButton size="small" onClick={onEdit} sx={{ p: 0.5 }}>
          <EditOutlined sx={{ fontSize: 15 }} />
        </IconButton>
        <IconButton size="small" onClick={onDelete} sx={{ p: 0.5, color: 'error.light' }}>
          <DeleteOutlined sx={{ fontSize: 15 }} />
        </IconButton>
      </Box>
    </Box>
  )
}

// ── Main page ─────────────────────────────────────────────────────────────────

export default function Bia() {
  const qc = useQueryClient()
  const [typeFilter, setTypeFilter] = useState('')
  const [dialogOpen, setDialogOpen] = useState(false)
  const [editing, setEditing] = useState<BIARecord | undefined>()

  const { activeProject } = useProject()
  const projectId = activeProject?.id

  const { data, isLoading } = useQuery({
    queryKey: ['bia', typeFilter, projectId],
    queryFn: () => biaApi.list({
      project_id: projectId,
      ...(typeFilter ? { asset_type: typeFilter } : {}),
    }),
  })

  const deleteMut = useMutation({
    mutationFn: (id: string) => biaApi.delete(id),
    onSuccess: () => {
      qc.invalidateQueries({ queryKey: ['bia'] })
      qc.invalidateQueries({ queryKey: ['bia-summary'] })
    },
  })

  function openCreate() { setEditing(undefined); setDialogOpen(true) }
  function openEdit(r: BIARecord) { setEditing(r); setDialogOpen(true) }

  return (
    <Box sx={{ p: 3 }}>
      <PageHeader
        title="Business Impact Analysis"
        subtitle={activeProject
          ? `${activeProject.name} · RTO/RPO modelling — ISO 27001:2022 §A.5.29`
          : 'RTO/RPO modelling and continuity planning — ISO 27001:2022 §A.5.29'}
        actions={
          <Tooltip title={!activeProject ? 'Select a project first to create BIA records' : ''}>
            <span>
              <Button variant="contained" size="small" startIcon={<AddOutlined />}
                onClick={openCreate} disabled={!activeProject}>
                New Record
              </Button>
            </span>
          </Tooltip>
        }
      />

      {activeProject && (
        <Alert severity="info" sx={{ mb: 2, py: 0.5, fontSize: '0.8rem' }}>
          Showing BIA records for project: <strong>{activeProject.name}</strong>
          {activeProject.organisation_name ? ` — ${activeProject.organisation_name}` : ''}
        </Alert>
      )}

      <SummaryCards projectId={projectId} />

      {/* Filters */}
      <Box sx={{ display: 'flex', gap: 1.5, mb: 2, alignItems: 'center' }}>
        <FormControl size="small" sx={{ minWidth: 150 }}>
          <InputLabel>Asset type</InputLabel>
          <Select value={typeFilter} label="Asset type" onChange={e => setTypeFilter(e.target.value)}>
            <MenuItem value="">All types</MenuItem>
            {ASSET_TYPES.map(t => (
              <MenuItem key={t} value={t}>{t.charAt(0).toUpperCase() + t.slice(1)}</MenuItem>
            ))}
          </Select>
        </FormControl>
        {typeFilter && (
          <Button size="small" onClick={() => setTypeFilter('')} sx={{ textTransform: 'none', fontSize: '0.75rem' }}>
            Clear
          </Button>
        )}
        <Typography variant="caption" sx={{ ml: 'auto', color: 'text.disabled' }}>
          {data?.length ?? 0} record{data?.length !== 1 ? 's' : ''}
        </Typography>
      </Box>

      {/* Table header */}
      <Box sx={{
        display: 'flex', alignItems: 'center', gap: 1, px: 2, py: 0.75,
        bgcolor: 'action.hover', borderRadius: '8px 8px 0 0',
        border: '1px solid', borderColor: 'divider', borderBottom: 'none',
      }}>
        <Typography variant="caption" sx={{ flex: 3, fontWeight: 600, fontSize: '0.7rem', color: 'text.secondary', textTransform: 'uppercase' }}>Asset / Plan</Typography>
        <Typography variant="caption" sx={{ width: 80, fontWeight: 600, fontSize: '0.7rem', color: 'text.secondary', textTransform: 'uppercase' }}>Type</Typography>
        <Typography variant="caption" sx={{ width: 60, textAlign: 'center', fontWeight: 600, fontSize: '0.7rem', color: 'text.secondary', textTransform: 'uppercase' }}>RTO</Typography>
        <Typography variant="caption" sx={{ width: 60, textAlign: 'center', fontWeight: 600, fontSize: '0.7rem', color: 'text.secondary', textTransform: 'uppercase' }}>RPO</Typography>
        <Typography variant="caption" sx={{ width: 70, textAlign: 'center', fontWeight: 600, fontSize: '0.7rem', color: 'text.secondary', textTransform: 'uppercase' }}>Impact</Typography>
        <Typography variant="caption" sx={{ width: 80, textAlign: 'center', fontWeight: 600, fontSize: '0.7rem', color: 'text.secondary', textTransform: 'uppercase' }}>Tested</Typography>
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
            <Typography variant="body2" color="text.secondary">
              {activeProject ? 'No BIA records yet.' : 'Select a project to create BIA records.'}
            </Typography>
            {activeProject && (
              <Button variant="outlined" size="small" startIcon={<AddOutlined />} onClick={openCreate} sx={{ mt: 1.5 }}>
                Create first record
              </Button>
            )}
          </Box>
        )}

        {data?.map(r => (
          <BIARow
            key={r.id}
            record={r}
            onEdit={() => openEdit(r)}
            onDelete={() => { if (confirm(`Delete "${r.asset_name}"?`)) deleteMut.mutate(r.id) }}
          />
        ))}
      </Box>

      <BIADialog
        open={dialogOpen}
        onClose={() => setDialogOpen(false)}
        existing={editing}
        projectId={projectId}
      />
    </Box>
  )
}
