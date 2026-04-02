import { useState } from 'react'
import {
  Alert, Box, Button, Checkbox, Chip, Dialog, DialogActions, DialogContent,
  DialogTitle, FormControl, FormControlLabel, IconButton, InputLabel, MenuItem,
  Select, Skeleton, Tab, Tabs, TextField, Tooltip, Typography,
} from '@mui/material'
import {
  AddOutlined, ArrowBackOutlined, DeleteOutlined, EditOutlined,
} from '@mui/icons-material'
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import dayjs from 'dayjs'
import {
  ebiosApi,
  type EbiosStudy, type EbiosFearedEvent, type EbiosRiskSource,
  type EbiosScenario, type EbiosAttackPath, type EbiosMeasure,
} from '../api/ebiosApi'
import PageHeader from '../components/PageHeader'

// ── Helpers ───────────────────────────────────────────────────────────────────

function toLabel(s: string) {
  return s.replace(/_/g, ' ').replace(/\b\w/g, c => c.toUpperCase())
}

const STUDY_STATUS_COLORS: Record<string, string> = {
  draft: '#607D8B',
  in_progress: '#FF9800',
  complete: '#4CAF50',
}

const MEASURE_STATUS_COLORS: Record<string, string> = {
  planned: '#607D8B',
  in_progress: '#FF9800',
  implemented: '#4CAF50',
}

const GRAVITY_COLORS: Record<number, string> = {
  1: '#4CAF50',
  2: '#FF9800',
  3: '#F44336',
  4: '#9C27B0',
}

const GRAVITY_LABELS: Record<number, string> = {
  1: 'Low',
  2: 'Medium',
  3: 'High',
  4: 'Critical',
}

function GravityText({ value }: { value: number | null }) {
  if (value == null) return <Typography variant="caption" color="text.disabled">—</Typography>
  const color = GRAVITY_COLORS[value] ?? '#607D8B'
  return (
    <Typography variant="caption" sx={{ fontWeight: 700, color, fontSize: '0.72rem' }}>
      {value} — {GRAVITY_LABELS[value] ?? value}
    </Typography>
  )
}

function StatusChip({ status, colorMap }: { status: string; colorMap: Record<string, string> }) {
  const color = colorMap[status] ?? '#607D8B'
  return (
    <Chip
      label={toLabel(status)}
      size="small"
      sx={{
        height: 20, fontSize: '0.62rem', fontWeight: 700,
        bgcolor: `${color}18`, color, border: `1px solid ${color}40`,
      }}
    />
  )
}

function CategoryChip({ label }: { label: string }) {
  return (
    <Chip
      label={toLabel(label)}
      size="small"
      sx={{ height: 20, fontSize: '0.62rem', fontWeight: 600, bgcolor: 'action.hover' }}
    />
  )
}

function RiskLevelChip({ level }: { level: number }) {
  const color = level >= 9 ? '#F44336' : level >= 4 ? '#FF9800' : '#4CAF50'
  return (
    <Chip
      label={level}
      size="small"
      sx={{
        height: 20, fontSize: '0.7rem', fontWeight: 800,
        bgcolor: `${color}18`, color, border: `1px solid ${color}40`,
      }}
    />
  )
}

// Table header helper
function TH({ children, width, flex, align }: {
  children: React.ReactNode
  width?: number | string; flex?: number; align?: 'center' | 'right'
}) {
  return (
    <Typography
      variant="caption"
      sx={{
        fontWeight: 600, fontSize: '0.7rem', color: 'text.secondary',
        textTransform: 'uppercase',
        ...(flex != null ? { flex } : {}),
        ...(width != null ? { width } : {}),
        ...(align ? { textAlign: align } : {}),
      }}
    >
      {children}
    </Typography>
  )
}

const ROW_SX = {
  display: 'flex', alignItems: 'center', gap: 1, px: 2, py: 1.25,
  borderBottom: '1px solid', borderColor: 'divider',
  '&:hover': { bgcolor: 'action.hover' },
}

const HEADER_SX = {
  display: 'flex', alignItems: 'center', gap: 1, px: 2, py: 0.75,
  bgcolor: 'action.hover', borderRadius: '8px 8px 0 0',
  border: '1px solid', borderColor: 'divider', borderBottom: 'none',
}

const TABLE_WRAP_SX = {
  border: '1px solid', borderColor: 'divider',
  borderRadius: '0 0 8px 8px', overflow: 'hidden',
}

const SCALE_OPTIONS = [1, 2, 3, 4]

// ── Summary cards ─────────────────────────────────────────────────────────────

function SummaryCards() {
  const { data, isLoading } = useQuery({
    queryKey: ['ebios-summary'],
    queryFn: ebiosApi.summary,
  })
  const cards = [
    { label: 'Studies',      value: data?.total_studies,      color: '#607D8B' },
    { label: 'Feared Events', value: data?.total_feared_events, color: '#9C27B0' },
    { label: 'Risk Sources',  value: data?.total_risk_sources,  color: '#F44336' },
    { label: 'Scenarios',     value: data?.total_scenarios,     color: '#FF9800' },
    { label: 'Attack Paths',  value: data?.total_attack_paths,  color: '#2196F3' },
    { label: 'Measures',      value: data?.total_measures,      color: '#4CAF50' },
  ]
  return (
    <Box sx={{ display: 'flex', gap: 1.5, flexWrap: 'wrap', mb: 2.5 }}>
      {cards.map(c => (
        <Box
          key={c.label}
          sx={{
            minWidth: 90, p: 1.5, borderRadius: 1.5,
            border: '1px solid', borderColor: `${c.color}30`, bgcolor: `${c.color}08`,
          }}
        >
          {isLoading
            ? <Skeleton width={32} height={28} />
            : <Typography variant="h5" sx={{ fontWeight: 700, color: c.color, lineHeight: 1 }}>{c.value ?? 0}</Typography>}
          <Typography variant="caption" sx={{ fontSize: '0.65rem', color: 'text.secondary' }}>{c.label}</Typography>
        </Box>
      ))}
    </Box>
  )
}

// ── Create Study Dialog ───────────────────────────────────────────────────────

const STUDY_STATUSES = ['draft', 'in_progress', 'complete']

function CreateStudyDialog({ open, onClose }: { open: boolean; onClose: () => void }) {
  const qc = useQueryClient()
  const [name, setName] = useState('')
  const [description, setDescription] = useState('')
  const [scope, setScope] = useState('')
  const [owner, setOwner] = useState('')
  const [status, setStatus] = useState('draft')
  const [startedAt, setStartedAt] = useState('')
  const [error, setError] = useState('')

  const mut = useMutation({
    mutationFn: () => ebiosApi.create({
      name, description: description || undefined, scope: scope || undefined,
      owner: owner || undefined, status,
      started_at: startedAt || undefined,
    }),
    onSuccess: () => {
      qc.invalidateQueries({ queryKey: ['ebios-studies'] })
      qc.invalidateQueries({ queryKey: ['ebios-summary'] })
      onClose()
      setName(''); setDescription(''); setScope(''); setOwner(''); setStatus('draft'); setStartedAt('')
    },
    onError: () => setError('Failed to create study.'),
  })

  function handleSubmit() {
    if (!name.trim()) { setError('Name is required.'); return }
    setError('')
    mut.mutate()
  }

  return (
    <Dialog open={open} onClose={onClose} maxWidth="sm" fullWidth>
      <DialogTitle sx={{ pb: 0.5 }}>New EBIOS RM Study</DialogTitle>
      <DialogContent sx={{ pt: '20px !important' }}>
        {error && <Alert severity="error" sx={{ mb: 2, py: 0.5 }}>{error}</Alert>}
        <TextField label="Study name *" fullWidth size="small" sx={{ mb: 2 }}
          value={name} onChange={e => setName(e.target.value)} />
        <TextField label="Description" fullWidth size="small" multiline rows={2} sx={{ mb: 2 }}
          value={description} onChange={e => setDescription(e.target.value)} />
        <TextField
          label="Scope" fullWidth size="small" multiline rows={2} sx={{ mb: 2 }}
          placeholder="What systems and processes are in scope"
          value={scope} onChange={e => setScope(e.target.value)}
        />
        <Box sx={{ display: 'flex', gap: 1.5, mb: 2 }}>
          <TextField label="Owner" size="small" sx={{ flex: 1 }}
            value={owner} onChange={e => setOwner(e.target.value)} />
          <FormControl size="small" sx={{ flex: 1 }}>
            <InputLabel>Status</InputLabel>
            <Select value={status} label="Status" onChange={e => setStatus(e.target.value)}>
              {STUDY_STATUSES.map(s => <MenuItem key={s} value={s}>{toLabel(s)}</MenuItem>)}
            </Select>
          </FormControl>
        </Box>
        <TextField label="Started at" type="date" size="small" fullWidth
          InputLabelProps={{ shrink: true }}
          value={startedAt} onChange={e => setStartedAt(e.target.value)} />
      </DialogContent>
      <DialogActions sx={{ px: 3, pb: 2 }}>
        <Button onClick={onClose} size="small">Cancel</Button>
        <Button variant="contained" size="small" onClick={handleSubmit} disabled={mut.isPending}>
          {mut.isPending ? 'Creating…' : 'Create'}
        </Button>
      </DialogActions>
    </Dialog>
  )
}

// ── Edit Study Dialog ─────────────────────────────────────────────────────────

function EditStudyDialog({
  open, onClose, study,
}: { open: boolean; onClose: () => void; study: EbiosStudy }) {
  const qc = useQueryClient()
  const [name, setName] = useState(study.name)
  const [status, setStatus] = useState(study.status)
  const [owner, setOwner] = useState(study.owner ?? '')
  const [error, setError] = useState('')

  // Keep form in sync if dialog re-opens for a different study
  const studyId = study.id
  const mut = useMutation({
    mutationFn: () => ebiosApi.update(studyId, {
      name: name.trim(),
      status,
      owner: owner.trim() || undefined,
    }),
    onSuccess: () => {
      qc.invalidateQueries({ queryKey: ['ebios-studies'] })
      onClose()
    },
    onError: () => setError('Failed to update study.'),
  })

  function handleSubmit() {
    if (!name.trim()) { setError('Name is required.'); return }
    setError('')
    mut.mutate()
  }

  return (
    <Dialog open={open} onClose={onClose} maxWidth="xs" fullWidth>
      <DialogTitle sx={{ pb: 0.5 }}>Edit Study</DialogTitle>
      <DialogContent sx={{ pt: '20px !important' }}>
        {error && <Alert severity="error" sx={{ mb: 2, py: 0.5 }}>{error}</Alert>}
        <TextField label="Study name *" fullWidth size="small" sx={{ mb: 2 }}
          value={name} onChange={e => setName(e.target.value)} />
        <Box sx={{ display: 'flex', gap: 1.5 }}>
          <TextField label="Owner" size="small" sx={{ flex: 1 }}
            value={owner} onChange={e => setOwner(e.target.value)} />
          <FormControl size="small" sx={{ flex: 1 }}>
            <InputLabel>Status</InputLabel>
            <Select value={status} label="Status" onChange={e => setStatus(e.target.value)}>
              {STUDY_STATUSES.map(s => <MenuItem key={s} value={s}>{toLabel(s)}</MenuItem>)}
            </Select>
          </FormControl>
        </Box>
      </DialogContent>
      <DialogActions sx={{ px: 3, pb: 2 }}>
        <Button onClick={onClose} size="small">Cancel</Button>
        <Button variant="contained" size="small" onClick={handleSubmit} disabled={mut.isPending}>
          {mut.isPending ? 'Saving…' : 'Save'}
        </Button>
      </DialogActions>
    </Dialog>
  )
}

// ── W1 — Feared Events ────────────────────────────────────────────────────────

const ASSET_TYPES = ['primary', 'secondary', 'supporting']

function W1FearedEvents({ studyId }: { studyId: string }) {
  const qc = useQueryClient()
  const [open, setOpen] = useState(false)
  const [assetName, setAssetName] = useState('')
  const [assetType, setAssetType] = useState('primary')
  const [description, setDescription] = useState('')
  const [gravity, setGravity] = useState<number>(2)
  const [error, setError] = useState('')

  const { data, isLoading } = useQuery({
    queryKey: ['ebios-study', studyId, 'feared-events'],
    queryFn: () => ebiosApi.listFearedEvents(studyId),
  })

  const createMut = useMutation({
    mutationFn: () => ebiosApi.createFearedEvent(studyId, {
      asset_name: assetName, asset_type: assetType,
      description: description || undefined, gravity,
    }),
    onSuccess: () => {
      qc.invalidateQueries({ queryKey: ['ebios-study', studyId, 'feared-events'] })
      qc.invalidateQueries({ queryKey: ['ebios-summary'] })
      setOpen(false); setAssetName(''); setDescription(''); setGravity(2); setError('')
    },
    onError: () => setError('Failed to create.'),
  })

  const deleteMut = useMutation({
    mutationFn: (feId: string) => ebiosApi.deleteFearedEvent(studyId, feId),
    onSuccess: () => {
      qc.invalidateQueries({ queryKey: ['ebios-study', studyId, 'feared-events'] })
      qc.invalidateQueries({ queryKey: ['ebios-summary'] })
    },
  })

  function handleSubmit() {
    if (!assetName.trim()) { setError('Asset name is required.'); return }
    setError(''); createMut.mutate()
  }

  return (
    <Box>
      <Box sx={{ display: 'flex', justifyContent: 'flex-end', mb: 1.5 }}>
        <Button variant="outlined" size="small" startIcon={<AddOutlined />} onClick={() => setOpen(true)}>
          Add Feared Event
        </Button>
      </Box>

      <Box sx={HEADER_SX}>
        <TH flex={3}>Asset / Description</TH>
        <TH width={100}>Type</TH>
        <TH width={130}>Gravity</TH>
        <Box sx={{ width: 40 }} />
      </Box>
      <Box sx={TABLE_WRAP_SX}>
        {isLoading && [0,1,2].map(i => (
          <Box key={i} sx={{ px: 2, py: 1.5, borderBottom: '1px solid', borderColor: 'divider' }}>
            <Skeleton height={20} />
          </Box>
        ))}
        {!isLoading && (!data || data.length === 0) && (
          <Box sx={{ py: 5, textAlign: 'center' }}>
            <Typography variant="body2" color="text.secondary">No feared events yet.</Typography>
          </Box>
        )}
        {data?.map((fe: EbiosFearedEvent) => (
          <Box key={fe.id} sx={ROW_SX}>
            <Box sx={{ flex: 3, minWidth: 0 }}>
              <Typography variant="body2" sx={{ fontWeight: 500, fontSize: '0.82rem' }} noWrap>
                {fe.asset_name}
              </Typography>
              {fe.description && (
                <Typography variant="caption" sx={{ fontSize: '0.65rem', color: 'text.disabled' }} noWrap>
                  {fe.description}
                </Typography>
              )}
            </Box>
            <Box sx={{ width: 100 }}>
              <CategoryChip label={fe.asset_type} />
            </Box>
            <Box sx={{ width: 130 }}>
              <GravityText value={fe.gravity} />
            </Box>
            <Box sx={{ width: 40 }}>
              <IconButton size="small" sx={{ p: 0.5, color: 'error.light' }}
                onClick={() => deleteMut.mutate(fe.id)}>
                <DeleteOutlined sx={{ fontSize: 15 }} />
              </IconButton>
            </Box>
          </Box>
        ))}
      </Box>

      <Dialog open={open} onClose={() => setOpen(false)} maxWidth="sm" fullWidth>
        <DialogTitle sx={{ pb: 0.5 }}>Add Feared Event</DialogTitle>
        <DialogContent sx={{ pt: '20px !important' }}>
          {error && <Alert severity="error" sx={{ mb: 2, py: 0.5 }}>{error}</Alert>}
          <TextField label="Asset name *" fullWidth size="small" sx={{ mb: 2 }}
            value={assetName} onChange={e => setAssetName(e.target.value)} />
          <Box sx={{ display: 'flex', gap: 1.5, mb: 2 }}>
            <FormControl size="small" sx={{ flex: 1 }}>
              <InputLabel>Asset type</InputLabel>
              <Select value={assetType} label="Asset type" onChange={e => setAssetType(e.target.value)}>
                {ASSET_TYPES.map(t => <MenuItem key={t} value={t}>{toLabel(t)}</MenuItem>)}
              </Select>
            </FormControl>
            <FormControl size="small" sx={{ flex: 1 }}>
              <InputLabel>Gravity</InputLabel>
              <Select value={gravity} label="Gravity" onChange={e => setGravity(Number(e.target.value))}>
                {SCALE_OPTIONS.map(v => (
                  <MenuItem key={v} value={v}>{v} — {GRAVITY_LABELS[v]}</MenuItem>
                ))}
              </Select>
            </FormControl>
          </Box>
          <TextField label="Description" fullWidth size="small" multiline rows={2}
            value={description} onChange={e => setDescription(e.target.value)} />
        </DialogContent>
        <DialogActions sx={{ px: 3, pb: 2 }}>
          <Button onClick={() => setOpen(false)} size="small">Cancel</Button>
          <Button variant="contained" size="small" onClick={handleSubmit} disabled={createMut.isPending}>
            {createMut.isPending ? 'Adding…' : 'Add'}
          </Button>
        </DialogActions>
      </Dialog>
    </Box>
  )
}

// ── W2 — Risk Sources ─────────────────────────────────────────────────────────

const RS_CATEGORIES = ['cybercriminal', 'state_actor', 'insider', 'hacktivist', 'competitor', 'natural']

function W2RiskSources({ studyId }: { studyId: string }) {
  const qc = useQueryClient()
  const [open, setOpen] = useState(false)
  const [name, setName] = useState('')
  const [category, setCategory] = useState('cybercriminal')
  const [motivation, setMotivation] = useState('')
  const [pertinence, setPertinence] = useState<number>(2)
  const [activity, setActivity] = useState<number>(2)
  const [resources, setResources] = useState<number>(2)
  const [error, setError] = useState('')

  const { data, isLoading } = useQuery({
    queryKey: ['ebios-study', studyId, 'risk-sources'],
    queryFn: () => ebiosApi.listRiskSources(studyId),
  })

  const createMut = useMutation({
    mutationFn: () => ebiosApi.createRiskSource(studyId, {
      name, category, motivation: motivation || undefined,
      pertinence, activity, resources,
    }),
    onSuccess: () => {
      qc.invalidateQueries({ queryKey: ['ebios-study', studyId, 'risk-sources'] })
      qc.invalidateQueries({ queryKey: ['ebios-summary'] })
      setOpen(false); setName(''); setMotivation(''); setError('')
    },
    onError: () => setError('Failed to create.'),
  })

  const deleteMut = useMutation({
    mutationFn: (rsId: string) => ebiosApi.deleteRiskSource(studyId, rsId),
    onSuccess: () => {
      qc.invalidateQueries({ queryKey: ['ebios-study', studyId, 'risk-sources'] })
      qc.invalidateQueries({ queryKey: ['ebios-summary'] })
    },
  })

  function handleSubmit() {
    if (!name.trim()) { setError('Name is required.'); return }
    setError(''); createMut.mutate()
  }

  return (
    <Box>
      <Box sx={{ display: 'flex', justifyContent: 'flex-end', mb: 1.5 }}>
        <Button variant="outlined" size="small" startIcon={<AddOutlined />} onClick={() => setOpen(true)}>
          Add Risk Source
        </Button>
      </Box>

      <Box sx={HEADER_SX}>
        <TH flex={3}>Name / Motivation</TH>
        <TH width={120}>Category</TH>
        <TH width={90} align="center">Pertinence</TH>
        <TH width={80} align="center">Activity</TH>
        <TH width={80} align="center">Resources</TH>
        <Box sx={{ width: 40 }} />
      </Box>
      <Box sx={TABLE_WRAP_SX}>
        {isLoading && [0,1,2].map(i => (
          <Box key={i} sx={{ px: 2, py: 1.5, borderBottom: '1px solid', borderColor: 'divider' }}>
            <Skeleton height={20} />
          </Box>
        ))}
        {!isLoading && (!data || data.length === 0) && (
          <Box sx={{ py: 5, textAlign: 'center' }}>
            <Typography variant="body2" color="text.secondary">No risk sources yet.</Typography>
          </Box>
        )}
        {data?.map((rs: EbiosRiskSource) => (
          <Box key={rs.id} sx={ROW_SX}>
            <Box sx={{ flex: 3, minWidth: 0 }}>
              <Typography variant="body2" sx={{ fontWeight: 500, fontSize: '0.82rem' }} noWrap>{rs.name}</Typography>
              {rs.motivation && (
                <Typography variant="caption" sx={{ fontSize: '0.65rem', color: 'text.disabled' }} noWrap>
                  {rs.motivation}
                </Typography>
              )}
            </Box>
            <Box sx={{ width: 120 }}><CategoryChip label={rs.category} /></Box>
            <Box sx={{ width: 90, textAlign: 'center' }}><GravityText value={rs.pertinence} /></Box>
            <Box sx={{ width: 80, textAlign: 'center' }}><GravityText value={rs.activity} /></Box>
            <Box sx={{ width: 80, textAlign: 'center' }}><GravityText value={rs.resources} /></Box>
            <Box sx={{ width: 40 }}>
              <IconButton size="small" sx={{ p: 0.5, color: 'error.light' }}
                onClick={() => deleteMut.mutate(rs.id)}>
                <DeleteOutlined sx={{ fontSize: 15 }} />
              </IconButton>
            </Box>
          </Box>
        ))}
      </Box>

      <Dialog open={open} onClose={() => setOpen(false)} maxWidth="sm" fullWidth>
        <DialogTitle sx={{ pb: 0.5 }}>Add Risk Source</DialogTitle>
        <DialogContent sx={{ pt: '20px !important' }}>
          {error && <Alert severity="error" sx={{ mb: 2, py: 0.5 }}>{error}</Alert>}
          <TextField label="Name *" fullWidth size="small" sx={{ mb: 2 }}
            value={name} onChange={e => setName(e.target.value)} />
          <FormControl size="small" fullWidth sx={{ mb: 2 }}>
            <InputLabel>Category</InputLabel>
            <Select value={category} label="Category" onChange={e => setCategory(e.target.value)}>
              {RS_CATEGORIES.map(c => <MenuItem key={c} value={c}>{toLabel(c)}</MenuItem>)}
            </Select>
          </FormControl>
          <TextField label="Motivation" fullWidth size="small" multiline rows={2} sx={{ mb: 2 }}
            value={motivation} onChange={e => setMotivation(e.target.value)} />
          <Box sx={{ display: 'flex', gap: 1.5 }}>
            {([['pertinence', pertinence, setPertinence], ['activity', activity, setActivity], ['resources', resources, setResources]] as const).map(([label, val, setter]) => (
              <FormControl key={label} size="small" sx={{ flex: 1 }}>
                <InputLabel>{toLabel(label)}</InputLabel>
                <Select value={val} label={toLabel(label)} onChange={e => setter(Number(e.target.value))}>
                  {SCALE_OPTIONS.map(v => (
                    <MenuItem key={v} value={v}>{v} — {GRAVITY_LABELS[v]}</MenuItem>
                  ))}
                </Select>
              </FormControl>
            ))}
          </Box>
        </DialogContent>
        <DialogActions sx={{ px: 3, pb: 2 }}>
          <Button onClick={() => setOpen(false)} size="small">Cancel</Button>
          <Button variant="contained" size="small" onClick={handleSubmit} disabled={createMut.isPending}>
            {createMut.isPending ? 'Adding…' : 'Add'}
          </Button>
        </DialogActions>
      </Dialog>
    </Box>
  )
}

// ── W3 — Strategic Scenarios ──────────────────────────────────────────────────

function W3Scenarios({ studyId }: { studyId: string }) {
  const qc = useQueryClient()
  const [open, setOpen] = useState(false)
  const [name, setName] = useState('')
  const [description, setDescription] = useState('')
  const [riskSourceId, setRiskSourceId] = useState('')
  const [fearedEventId, setFearedEventId] = useState('')
  const [likelihood, setLikelihood] = useState<number>(2)
  const [gravity, setGravity] = useState<number>(2)
  const [retained, setRetained] = useState(false)
  const [error, setError] = useState('')

  const { data, isLoading } = useQuery({
    queryKey: ['ebios-study', studyId, 'scenarios'],
    queryFn: () => ebiosApi.listScenarios(studyId),
  })
  const { data: riskSources } = useQuery({
    queryKey: ['ebios-study', studyId, 'risk-sources'],
    queryFn: () => ebiosApi.listRiskSources(studyId),
  })
  const { data: fearedEvents } = useQuery({
    queryKey: ['ebios-study', studyId, 'feared-events'],
    queryFn: () => ebiosApi.listFearedEvents(studyId),
  })

  const createMut = useMutation({
    mutationFn: () => ebiosApi.createScenario(studyId, {
      name, description: description || undefined,
      risk_source_id: riskSourceId || undefined,
      feared_event_id: fearedEventId || undefined,
      likelihood, gravity, retained,
    }),
    onSuccess: () => {
      qc.invalidateQueries({ queryKey: ['ebios-study', studyId, 'scenarios'] })
      qc.invalidateQueries({ queryKey: ['ebios-summary'] })
      setOpen(false); setName(''); setDescription(''); setRiskSourceId(''); setFearedEventId('')
      setLikelihood(2); setGravity(2); setRetained(false); setError('')
    },
    onError: () => setError('Failed to create.'),
  })

  const deleteMut = useMutation({
    mutationFn: (scId: string) => ebiosApi.deleteScenario(studyId, scId),
    onSuccess: () => {
      qc.invalidateQueries({ queryKey: ['ebios-study', studyId, 'scenarios'] })
      qc.invalidateQueries({ queryKey: ['ebios-summary'] })
    },
  })

  function handleSubmit() {
    if (!name.trim()) { setError('Name is required.'); return }
    setError(''); createMut.mutate()
  }

  function rsName(id: string | null) {
    if (!id) return '—'
    return riskSources?.find(r => r.id === id)?.name ?? '—'
  }
  function feName(id: string | null) {
    if (!id) return '—'
    return fearedEvents?.find(f => f.id === id)?.asset_name ?? '—'
  }

  return (
    <Box>
      <Box sx={{ display: 'flex', justifyContent: 'flex-end', mb: 1.5 }}>
        <Button variant="outlined" size="small" startIcon={<AddOutlined />} onClick={() => setOpen(true)}>
          Add Scenario
        </Button>
      </Box>

      <Box sx={HEADER_SX}>
        <TH flex={2}>Name</TH>
        <TH flex={1.5}>Risk Source</TH>
        <TH flex={1.5}>Feared Event</TH>
        <TH width={80} align="center">Likelihood</TH>
        <TH width={70} align="center">Gravity</TH>
        <TH width={70} align="center">Risk</TH>
        <TH width={70} align="center">Retained</TH>
        <Box sx={{ width: 40 }} />
      </Box>
      <Box sx={TABLE_WRAP_SX}>
        {isLoading && [0,1,2].map(i => (
          <Box key={i} sx={{ px: 2, py: 1.5, borderBottom: '1px solid', borderColor: 'divider' }}>
            <Skeleton height={20} />
          </Box>
        ))}
        {!isLoading && (!data || data.length === 0) && (
          <Box sx={{ py: 5, textAlign: 'center' }}>
            <Typography variant="body2" color="text.secondary">No scenarios yet.</Typography>
          </Box>
        )}
        {data?.map((sc: EbiosScenario) => (
          <Box key={sc.id} sx={ROW_SX}>
            <Box sx={{ flex: 2, minWidth: 0 }}>
              <Typography variant="body2" sx={{ fontWeight: 500, fontSize: '0.82rem' }} noWrap>{sc.name}</Typography>
            </Box>
            <Box sx={{ flex: 1.5, minWidth: 0 }}>
              <Typography variant="caption" sx={{ fontSize: '0.72rem', color: 'text.secondary' }} noWrap>
                {rsName(sc.risk_source_id)}
              </Typography>
            </Box>
            <Box sx={{ flex: 1.5, minWidth: 0 }}>
              <Typography variant="caption" sx={{ fontSize: '0.72rem', color: 'text.secondary' }} noWrap>
                {feName(sc.feared_event_id)}
              </Typography>
            </Box>
            <Box sx={{ width: 80, textAlign: 'center' }}><GravityText value={sc.likelihood} /></Box>
            <Box sx={{ width: 70, textAlign: 'center' }}><GravityText value={sc.gravity} /></Box>
            <Box sx={{ width: 70, textAlign: 'center' }}><RiskLevelChip level={sc.risk_level} /></Box>
            <Box sx={{ width: 70, textAlign: 'center' }}>
              <Typography variant="caption" sx={{ fontSize: '0.72rem', color: sc.retained ? '#4CAF50' : 'text.disabled' }}>
                {sc.retained ? 'Yes' : 'No'}
              </Typography>
            </Box>
            <Box sx={{ width: 40 }}>
              <IconButton size="small" sx={{ p: 0.5, color: 'error.light' }}
                onClick={() => deleteMut.mutate(sc.id)}>
                <DeleteOutlined sx={{ fontSize: 15 }} />
              </IconButton>
            </Box>
          </Box>
        ))}
      </Box>

      <Dialog open={open} onClose={() => setOpen(false)} maxWidth="sm" fullWidth>
        <DialogTitle sx={{ pb: 0.5 }}>Add Strategic Scenario</DialogTitle>
        <DialogContent sx={{ pt: '20px !important' }}>
          {error && <Alert severity="error" sx={{ mb: 2, py: 0.5 }}>{error}</Alert>}
          <TextField label="Name *" fullWidth size="small" sx={{ mb: 2 }}
            value={name} onChange={e => setName(e.target.value)} />
          <TextField label="Description" fullWidth size="small" multiline rows={2} sx={{ mb: 2 }}
            value={description} onChange={e => setDescription(e.target.value)} />
          <Box sx={{ display: 'flex', gap: 1.5, mb: 2 }}>
            <FormControl size="small" sx={{ flex: 1 }}>
              <InputLabel>Risk source</InputLabel>
              <Select value={riskSourceId} label="Risk source" onChange={e => setRiskSourceId(e.target.value)}>
                <MenuItem value="">— None —</MenuItem>
                {riskSources?.map(r => <MenuItem key={r.id} value={r.id}>{r.name}</MenuItem>)}
              </Select>
            </FormControl>
            <FormControl size="small" sx={{ flex: 1 }}>
              <InputLabel>Feared event</InputLabel>
              <Select value={fearedEventId} label="Feared event" onChange={e => setFearedEventId(e.target.value)}>
                <MenuItem value="">— None —</MenuItem>
                {fearedEvents?.map(f => <MenuItem key={f.id} value={f.id}>{f.asset_name}</MenuItem>)}
              </Select>
            </FormControl>
          </Box>
          <Box sx={{ display: 'flex', gap: 1.5, mb: 2 }}>
            <FormControl size="small" sx={{ flex: 1 }}>
              <InputLabel>Likelihood</InputLabel>
              <Select value={likelihood} label="Likelihood" onChange={e => setLikelihood(Number(e.target.value))}>
                {SCALE_OPTIONS.map(v => <MenuItem key={v} value={v}>{v} — {GRAVITY_LABELS[v]}</MenuItem>)}
              </Select>
            </FormControl>
            <FormControl size="small" sx={{ flex: 1 }}>
              <InputLabel>Gravity</InputLabel>
              <Select value={gravity} label="Gravity" onChange={e => setGravity(Number(e.target.value))}>
                {SCALE_OPTIONS.map(v => <MenuItem key={v} value={v}>{v} — {GRAVITY_LABELS[v]}</MenuItem>)}
              </Select>
            </FormControl>
          </Box>
          <FormControlLabel
            control={<Checkbox size="small" checked={retained} onChange={e => setRetained(e.target.checked)} />}
            label={<Typography variant="body2">Retained for treatment</Typography>}
          />
        </DialogContent>
        <DialogActions sx={{ px: 3, pb: 2 }}>
          <Button onClick={() => setOpen(false)} size="small">Cancel</Button>
          <Button variant="contained" size="small" onClick={handleSubmit} disabled={createMut.isPending}>
            {createMut.isPending ? 'Adding…' : 'Add'}
          </Button>
        </DialogActions>
      </Dialog>
    </Box>
  )
}

// ── W4 — Attack Paths ─────────────────────────────────────────────────────────

function W4AttackPaths({ studyId }: { studyId: string }) {
  const qc = useQueryClient()
  const [open, setOpen] = useState(false)
  const [name, setName] = useState('')
  const [description, setDescription] = useState('')
  const [scenarioId, setScenarioId] = useState('')
  const [mitreTechniques, setMitreTechniques] = useState('')
  const [difficulty, setDifficulty] = useState<number>(2)
  const [detectability, setDetectability] = useState<number>(2)
  const [error, setError] = useState('')

  const { data, isLoading } = useQuery({
    queryKey: ['ebios-study', studyId, 'attack-paths'],
    queryFn: () => ebiosApi.listAttackPaths(studyId),
  })
  const { data: scenarios } = useQuery({
    queryKey: ['ebios-study', studyId, 'scenarios'],
    queryFn: () => ebiosApi.listScenarios(studyId),
  })

  const createMut = useMutation({
    mutationFn: () => {
      const techniques = mitreTechniques
        .split('\n')
        .map(t => t.trim())
        .filter(Boolean)
      return ebiosApi.createAttackPath(studyId, {
        name, description: description || undefined,
        strategic_scenario_id: scenarioId || undefined,
        mitre_techniques: techniques,
        difficulty, detectability,
      })
    },
    onSuccess: () => {
      qc.invalidateQueries({ queryKey: ['ebios-study', studyId, 'attack-paths'] })
      qc.invalidateQueries({ queryKey: ['ebios-summary'] })
      setOpen(false); setName(''); setDescription(''); setScenarioId('')
      setMitreTechniques(''); setDifficulty(2); setDetectability(2); setError('')
    },
    onError: () => setError('Failed to create.'),
  })

  const deleteMut = useMutation({
    mutationFn: (apId: string) => ebiosApi.deleteAttackPath(studyId, apId),
    onSuccess: () => {
      qc.invalidateQueries({ queryKey: ['ebios-study', studyId, 'attack-paths'] })
      qc.invalidateQueries({ queryKey: ['ebios-summary'] })
    },
  })

  function handleSubmit() {
    if (!name.trim()) { setError('Name is required.'); return }
    setError(''); createMut.mutate()
  }

  function scName(id: string | null) {
    if (!id) return '—'
    return scenarios?.find(s => s.id === id)?.name ?? '—'
  }

  return (
    <Box>
      <Box sx={{ display: 'flex', justifyContent: 'flex-end', mb: 1.5 }}>
        <Button variant="outlined" size="small" startIcon={<AddOutlined />} onClick={() => setOpen(true)}>
          Add Attack Path
        </Button>
      </Box>

      <Box sx={HEADER_SX}>
        <TH flex={3}>Name / Scenario</TH>
        <TH width={100} align="center">MITRE Techs</TH>
        <TH width={90} align="center">Difficulty</TH>
        <TH width={110} align="center">Detectability</TH>
        <Box sx={{ width: 40 }} />
      </Box>
      <Box sx={TABLE_WRAP_SX}>
        {isLoading && [0,1,2].map(i => (
          <Box key={i} sx={{ px: 2, py: 1.5, borderBottom: '1px solid', borderColor: 'divider' }}>
            <Skeleton height={20} />
          </Box>
        ))}
        {!isLoading && (!data || data.length === 0) && (
          <Box sx={{ py: 5, textAlign: 'center' }}>
            <Typography variant="body2" color="text.secondary">No attack paths yet.</Typography>
          </Box>
        )}
        {data?.map((ap: EbiosAttackPath) => (
          <Box key={ap.id} sx={ROW_SX}>
            <Box sx={{ flex: 3, minWidth: 0 }}>
              <Typography variant="body2" sx={{ fontWeight: 500, fontSize: '0.82rem' }} noWrap>{ap.name}</Typography>
              <Typography variant="caption" sx={{ fontSize: '0.65rem', color: 'text.disabled' }} noWrap>
                {scName(ap.strategic_scenario_id)}
              </Typography>
            </Box>
            <Box sx={{ width: 100, textAlign: 'center' }}>
              {ap.mitre_techniques.length > 0 ? (
                <Tooltip title={ap.mitre_techniques.join(', ')}>
                  <Chip
                    label={`${ap.mitre_techniques.length} tech${ap.mitre_techniques.length !== 1 ? 's' : ''}`}
                    size="small"
                    sx={{ height: 20, fontSize: '0.62rem', bgcolor: '#2196F318', color: '#2196F3', border: '1px solid #2196F340' }}
                  />
                </Tooltip>
              ) : (
                <Typography variant="caption" color="text.disabled">—</Typography>
              )}
            </Box>
            <Box sx={{ width: 90, textAlign: 'center' }}><GravityText value={ap.difficulty} /></Box>
            <Box sx={{ width: 110, textAlign: 'center' }}><GravityText value={ap.detectability} /></Box>
            <Box sx={{ width: 40 }}>
              <IconButton size="small" sx={{ p: 0.5, color: 'error.light' }}
                onClick={() => deleteMut.mutate(ap.id)}>
                <DeleteOutlined sx={{ fontSize: 15 }} />
              </IconButton>
            </Box>
          </Box>
        ))}
      </Box>

      <Dialog open={open} onClose={() => setOpen(false)} maxWidth="sm" fullWidth>
        <DialogTitle sx={{ pb: 0.5 }}>Add Attack Path</DialogTitle>
        <DialogContent sx={{ pt: '20px !important' }}>
          {error && <Alert severity="error" sx={{ mb: 2, py: 0.5 }}>{error}</Alert>}
          <TextField label="Name *" fullWidth size="small" sx={{ mb: 2 }}
            value={name} onChange={e => setName(e.target.value)} />
          <TextField label="Description" fullWidth size="small" multiline rows={2} sx={{ mb: 2 }}
            value={description} onChange={e => setDescription(e.target.value)} />
          <FormControl size="small" fullWidth sx={{ mb: 2 }}>
            <InputLabel>Linked scenario</InputLabel>
            <Select value={scenarioId} label="Linked scenario" onChange={e => setScenarioId(e.target.value)}>
              <MenuItem value="">— None —</MenuItem>
              {scenarios?.map(s => <MenuItem key={s.id} value={s.id}>{s.name}</MenuItem>)}
            </Select>
          </FormControl>
          <TextField
            label="MITRE techniques (one per line, e.g. T1078)"
            fullWidth size="small" multiline rows={3} sx={{ mb: 2 }}
            placeholder={'T1078\nT1566\nT1486'}
            value={mitreTechniques} onChange={e => setMitreTechniques(e.target.value)}
          />
          <Box sx={{ display: 'flex', gap: 1.5 }}>
            <FormControl size="small" sx={{ flex: 1 }}>
              <InputLabel>Difficulty</InputLabel>
              <Select value={difficulty} label="Difficulty" onChange={e => setDifficulty(Number(e.target.value))}>
                {SCALE_OPTIONS.map(v => <MenuItem key={v} value={v}>{v} — {GRAVITY_LABELS[v]}</MenuItem>)}
              </Select>
            </FormControl>
            <FormControl size="small" sx={{ flex: 1 }}>
              <InputLabel>Detectability</InputLabel>
              <Select value={detectability} label="Detectability" onChange={e => setDetectability(Number(e.target.value))}>
                {SCALE_OPTIONS.map(v => <MenuItem key={v} value={v}>{v} — {GRAVITY_LABELS[v]}</MenuItem>)}
              </Select>
            </FormControl>
          </Box>
        </DialogContent>
        <DialogActions sx={{ px: 3, pb: 2 }}>
          <Button onClick={() => setOpen(false)} size="small">Cancel</Button>
          <Button variant="contained" size="small" onClick={handleSubmit} disabled={createMut.isPending}>
            {createMut.isPending ? 'Adding…' : 'Add'}
          </Button>
        </DialogActions>
      </Dialog>
    </Box>
  )
}

// ── W5 — Security Measures ────────────────────────────────────────────────────

const MEASURE_STATUSES = ['planned', 'in_progress', 'implemented']

function W5Measures({ studyId }: { studyId: string }) {
  const qc = useQueryClient()
  const [open, setOpen] = useState(false)
  const [name, setName] = useState('')
  const [description, setDescription] = useState('')
  const [scenarioId, setScenarioId] = useState('')
  const [status, setStatus] = useState('planned')
  const [isoControlRef, setIsoControlRef] = useState('')
  const [effectiveness, setEffectiveness] = useState<number>(2)
  const [dueDate, setDueDate] = useState('')
  const [owner, setOwner] = useState('')
  const [error, setError] = useState('')

  const { data, isLoading } = useQuery({
    queryKey: ['ebios-study', studyId, 'measures'],
    queryFn: () => ebiosApi.listMeasures(studyId),
  })
  const { data: scenarios } = useQuery({
    queryKey: ['ebios-study', studyId, 'scenarios'],
    queryFn: () => ebiosApi.listScenarios(studyId),
  })

  const createMut = useMutation({
    mutationFn: () => ebiosApi.createMeasure(studyId, {
      name, description: description || undefined,
      scenario_id: scenarioId || undefined, status,
      iso_control_ref: isoControlRef || undefined,
      effectiveness,
      due_date: dueDate || undefined,
      owner: owner || undefined,
    }),
    onSuccess: () => {
      qc.invalidateQueries({ queryKey: ['ebios-study', studyId, 'measures'] })
      qc.invalidateQueries({ queryKey: ['ebios-summary'] })
      setOpen(false); setName(''); setDescription(''); setScenarioId(''); setStatus('planned')
      setIsoControlRef(''); setEffectiveness(2); setDueDate(''); setOwner(''); setError('')
    },
    onError: () => setError('Failed to create.'),
  })

  const deleteMut = useMutation({
    mutationFn: (mId: string) => ebiosApi.deleteMeasure(studyId, mId),
    onSuccess: () => {
      qc.invalidateQueries({ queryKey: ['ebios-study', studyId, 'measures'] })
      qc.invalidateQueries({ queryKey: ['ebios-summary'] })
    },
  })

  function handleSubmit() {
    if (!name.trim()) { setError('Name is required.'); return }
    setError(''); createMut.mutate()
  }

  function scName(id: string | null) {
    if (!id) return '—'
    return scenarios?.find(s => s.id === id)?.name ?? '—'
  }

  return (
    <Box>
      <Box sx={{ display: 'flex', justifyContent: 'flex-end', mb: 1.5 }}>
        <Button variant="outlined" size="small" startIcon={<AddOutlined />} onClick={() => setOpen(true)}>
          Add Measure
        </Button>
      </Box>

      <Box sx={HEADER_SX}>
        <TH flex={3}>Measure / Scenario</TH>
        <TH width={110}>Status</TH>
        <TH flex={1.5}>ISO Control</TH>
        <TH width={90} align="center">Effectiveness</TH>
        <TH width={90} align="center">Due</TH>
        <TH flex={1}>Owner</TH>
        <Box sx={{ width: 40 }} />
      </Box>
      <Box sx={TABLE_WRAP_SX}>
        {isLoading && [0,1,2].map(i => (
          <Box key={i} sx={{ px: 2, py: 1.5, borderBottom: '1px solid', borderColor: 'divider' }}>
            <Skeleton height={20} />
          </Box>
        ))}
        {!isLoading && (!data || data.length === 0) && (
          <Box sx={{ py: 5, textAlign: 'center' }}>
            <Typography variant="body2" color="text.secondary">No measures yet.</Typography>
          </Box>
        )}
        {data?.map((m: EbiosMeasure) => (
          <Box key={m.id} sx={ROW_SX}>
            <Box sx={{ flex: 3, minWidth: 0 }}>
              <Typography variant="body2" sx={{ fontWeight: 500, fontSize: '0.82rem' }} noWrap>{m.name}</Typography>
              <Typography variant="caption" sx={{ fontSize: '0.65rem', color: 'text.disabled' }} noWrap>
                {scName(m.scenario_id)}
              </Typography>
            </Box>
            <Box sx={{ width: 110 }}>
              <StatusChip status={m.status} colorMap={MEASURE_STATUS_COLORS} />
            </Box>
            <Box sx={{ flex: 1.5, minWidth: 0 }}>
              <Typography variant="caption" sx={{ fontSize: '0.72rem', color: 'text.secondary' }} noWrap>
                {m.iso_control_ref ?? '—'}
              </Typography>
            </Box>
            <Box sx={{ width: 90, textAlign: 'center' }}><GravityText value={m.effectiveness} /></Box>
            <Box sx={{ width: 90, textAlign: 'center' }}>
              <Typography variant="caption" sx={{ fontSize: '0.72rem', color: 'text.secondary' }}>
                {m.due_date ? dayjs(m.due_date).format('D MMM YY') : '—'}
              </Typography>
            </Box>
            <Box sx={{ flex: 1, minWidth: 0 }}>
              <Typography variant="caption" sx={{ fontSize: '0.72rem', color: 'text.secondary' }} noWrap>
                {m.owner ?? '—'}
              </Typography>
            </Box>
            <Box sx={{ width: 40 }}>
              <IconButton size="small" sx={{ p: 0.5, color: 'error.light' }}
                onClick={() => deleteMut.mutate(m.id)}>
                <DeleteOutlined sx={{ fontSize: 15 }} />
              </IconButton>
            </Box>
          </Box>
        ))}
      </Box>

      <Dialog open={open} onClose={() => setOpen(false)} maxWidth="sm" fullWidth>
        <DialogTitle sx={{ pb: 0.5 }}>Add Security Measure</DialogTitle>
        <DialogContent sx={{ pt: '20px !important' }}>
          {error && <Alert severity="error" sx={{ mb: 2, py: 0.5 }}>{error}</Alert>}
          <TextField label="Name *" fullWidth size="small" sx={{ mb: 2 }}
            value={name} onChange={e => setName(e.target.value)} />
          <TextField label="Description" fullWidth size="small" multiline rows={2} sx={{ mb: 2 }}
            value={description} onChange={e => setDescription(e.target.value)} />
          <FormControl size="small" fullWidth sx={{ mb: 2 }}>
            <InputLabel>Linked scenario</InputLabel>
            <Select value={scenarioId} label="Linked scenario" onChange={e => setScenarioId(e.target.value)}>
              <MenuItem value="">— None —</MenuItem>
              {scenarios?.map(s => <MenuItem key={s.id} value={s.id}>{s.name}</MenuItem>)}
            </Select>
          </FormControl>
          <Box sx={{ display: 'flex', gap: 1.5, mb: 2 }}>
            <FormControl size="small" sx={{ flex: 1 }}>
              <InputLabel>Status</InputLabel>
              <Select value={status} label="Status" onChange={e => setStatus(e.target.value)}>
                {MEASURE_STATUSES.map(s => <MenuItem key={s} value={s}>{toLabel(s)}</MenuItem>)}
              </Select>
            </FormControl>
            <TextField label="ISO control ref" size="small" sx={{ flex: 1 }}
              placeholder="e.g. A.8.7"
              value={isoControlRef} onChange={e => setIsoControlRef(e.target.value)} />
          </Box>
          <Box sx={{ display: 'flex', gap: 1.5, mb: 2 }}>
            <FormControl size="small" sx={{ flex: 1 }}>
              <InputLabel>Effectiveness</InputLabel>
              <Select value={effectiveness} label="Effectiveness" onChange={e => setEffectiveness(Number(e.target.value))}>
                {SCALE_OPTIONS.map(v => <MenuItem key={v} value={v}>{v} — {GRAVITY_LABELS[v]}</MenuItem>)}
              </Select>
            </FormControl>
            <TextField label="Due date" type="date" size="small" sx={{ flex: 1 }}
              InputLabelProps={{ shrink: true }}
              value={dueDate} onChange={e => setDueDate(e.target.value)} />
          </Box>
          <TextField label="Owner" fullWidth size="small"
            value={owner} onChange={e => setOwner(e.target.value)} />
        </DialogContent>
        <DialogActions sx={{ px: 3, pb: 2 }}>
          <Button onClick={() => setOpen(false)} size="small">Cancel</Button>
          <Button variant="contained" size="small" onClick={handleSubmit} disabled={createMut.isPending}>
            {createMut.isPending ? 'Adding…' : 'Add'}
          </Button>
        </DialogActions>
      </Dialog>
    </Box>
  )
}

// ── Study Detail (tabs) ───────────────────────────────────────────────────────

const WORKSHOP_TABS = [
  { label: 'W1 — Feared Events', hint: 'Assets and feared events' },
  { label: 'W2 — Risk Sources',  hint: 'Threat actors and motivation' },
  { label: 'W3 — Scenarios',     hint: 'Strategic risk scenarios' },
  { label: 'W4 — Attack Paths',  hint: 'Operational attack paths' },
  { label: 'W5 — Measures',      hint: 'Security measures and treatment' },
]

function StudyDetail({
  study, onBack,
}: { study: EbiosStudy; onBack: () => void }) {
  const [tab, setTab] = useState(0)

  return (
    <Box>
      <Box sx={{ display: 'flex', alignItems: 'center', gap: 2, mb: 2.5 }}>
        <Button size="small" startIcon={<ArrowBackOutlined />} onClick={onBack}>
          Back to Studies
        </Button>
        <Box sx={{ flex: 1 }}>
          <Box sx={{ display: 'flex', alignItems: 'center', gap: 1.5 }}>
            <Typography variant="h6" sx={{ fontWeight: 700 }}>{study.name}</Typography>
            <StatusChip status={study.status} colorMap={STUDY_STATUS_COLORS} />
          </Box>
          {study.scope && (
            <Typography variant="caption" color="text.secondary" sx={{ fontSize: '0.72rem' }}>
              Scope: {study.scope}
            </Typography>
          )}
        </Box>
        {study.owner && (
          <Typography variant="caption" color="text.secondary" sx={{ fontSize: '0.72rem' }}>
            Owner: {study.owner}
          </Typography>
        )}
      </Box>

      <Box sx={{ borderBottom: 1, borderColor: 'divider', mb: 2.5 }}>
        <Tabs
          value={tab}
          onChange={(_, v) => setTab(v)}
          variant="scrollable"
          scrollButtons="auto"
          sx={{ '& .MuiTab-root': { fontSize: '0.78rem', textTransform: 'none', minWidth: 'auto', px: 2 } }}
        >
          {WORKSHOP_TABS.map((wt, i) => (
            <Tab key={i} label={wt.label} />
          ))}
        </Tabs>
      </Box>

      <Typography variant="caption" color="text.secondary" sx={{ display: 'block', mb: 2, fontSize: '0.72rem' }}>
        {WORKSHOP_TABS[tab].hint}
      </Typography>

      {tab === 0 && <W1FearedEvents studyId={study.id} />}
      {tab === 1 && <W2RiskSources studyId={study.id} />}
      {tab === 2 && <W3Scenarios studyId={study.id} />}
      {tab === 3 && <W4AttackPaths studyId={study.id} />}
      {tab === 4 && <W5Measures studyId={study.id} />}
    </Box>
  )
}

// ── Study list ────────────────────────────────────────────────────────────────

function StudyList({
  onSelect,
}: { onSelect: (study: EbiosStudy) => void }) {
  const qc = useQueryClient()
  const [statusFilter, setStatusFilter] = useState('')
  const [createOpen, setCreateOpen] = useState(false)
  const [editingStudy, setEditingStudy] = useState<EbiosStudy | null>(null)

  const { data, isLoading } = useQuery({
    queryKey: ['ebios-studies', statusFilter],
    queryFn: () => ebiosApi.list(statusFilter ? { status: statusFilter } : {}),
  })

  const deleteMut = useMutation({
    mutationFn: (id: string) => ebiosApi.delete(id),
    onSuccess: () => {
      qc.invalidateQueries({ queryKey: ['ebios-studies'] })
      qc.invalidateQueries({ queryKey: ['ebios-summary'] })
    },
  })

  return (
    <Box>
      <SummaryCards />

      {/* Filters + action */}
      <Box sx={{ display: 'flex', gap: 1.5, mb: 2, alignItems: 'center' }}>
        <FormControl size="small" sx={{ minWidth: 150 }}>
          <InputLabel>Status</InputLabel>
          <Select value={statusFilter} label="Status" onChange={e => setStatusFilter(e.target.value)}>
            <MenuItem value="">All</MenuItem>
            {STUDY_STATUSES.map(s => <MenuItem key={s} value={s}>{toLabel(s)}</MenuItem>)}
          </Select>
        </FormControl>
        {statusFilter && (
          <Button size="small" onClick={() => setStatusFilter('')} sx={{ textTransform: 'none', fontSize: '0.75rem' }}>
            Clear
          </Button>
        )}
        <Typography variant="caption" sx={{ ml: 'auto', color: 'text.disabled' }}>
          {data?.length ?? 0} stud{data?.length !== 1 ? 'ies' : 'y'}
        </Typography>
      </Box>

      {/* Table */}
      <Box sx={HEADER_SX}>
        <TH flex={3}>Study name</TH>
        <TH width={110}>Status</TH>
        <TH flex={1.5}>Owner</TH>
        <TH width={110} align="right">Created</TH>
        <Box sx={{ width: 76 }} />
      </Box>
      <Box sx={TABLE_WRAP_SX}>
        {isLoading && [0,1,2,3].map(i => (
          <Box key={i} sx={{ px: 2, py: 1.5, borderBottom: '1px solid', borderColor: 'divider' }}>
            <Skeleton height={20} />
          </Box>
        ))}
        {!isLoading && (!data || data.length === 0) && (
          <Box sx={{ py: 6, textAlign: 'center' }}>
            <Typography variant="body2" color="text.secondary">No EBIOS RM studies yet.</Typography>
            <Button variant="outlined" size="small" startIcon={<AddOutlined />}
              onClick={() => setCreateOpen(true)} sx={{ mt: 1.5 }}>
              Create first study
            </Button>
          </Box>
        )}
        {data?.map((s: EbiosStudy) => (
          <Box
            key={s.id}
            sx={{
              ...ROW_SX,
              cursor: 'pointer',
            }}
            onClick={() => onSelect(s)}
          >
            <Box sx={{ flex: 3, minWidth: 0 }}>
              <Typography variant="body2" sx={{ fontWeight: 600, fontSize: '0.82rem' }} noWrap>
                {s.name}
              </Typography>
              {s.description && (
                <Typography variant="caption" sx={{ fontSize: '0.65rem', color: 'text.disabled' }} noWrap>
                  {s.description}
                </Typography>
              )}
            </Box>
            <Box sx={{ width: 110 }}>
              <StatusChip status={s.status} colorMap={STUDY_STATUS_COLORS} />
            </Box>
            <Box sx={{ flex: 1.5, minWidth: 0 }}>
              <Typography variant="caption" sx={{ fontSize: '0.72rem', color: 'text.secondary' }} noWrap>
                {s.owner ?? '—'}
              </Typography>
            </Box>
            <Box sx={{ width: 110, textAlign: 'right' }}>
              <Typography variant="caption" sx={{ fontSize: '0.65rem', color: 'text.secondary' }}>
                {dayjs(s.created_at).format('D MMM YY')}
              </Typography>
            </Box>
            <Box sx={{ width: 76, display: 'flex', justifyContent: 'flex-end', gap: 0.25 }}
              onClick={e => e.stopPropagation()}>
              <IconButton size="small" sx={{ p: 0.5 }}
                onClick={() => setEditingStudy(s)}>
                <EditOutlined sx={{ fontSize: 15 }} />
              </IconButton>
              <IconButton size="small" sx={{ p: 0.5, color: 'error.light' }}
                onClick={() => { if (confirm(`Delete study "${s.name}"?`)) deleteMut.mutate(s.id) }}>
                <DeleteOutlined sx={{ fontSize: 15 }} />
              </IconButton>
            </Box>
          </Box>
        ))}
      </Box>

      <CreateStudyDialog open={createOpen} onClose={() => setCreateOpen(false)} />
      {editingStudy && (
        <EditStudyDialog
          open={!!editingStudy}
          onClose={() => setEditingStudy(null)}
          study={editingStudy}
        />
      )}
    </Box>
  )
}

// ── Main page ─────────────────────────────────────────────────────────────────

export default function Ebios() {
  const [selectedStudy, setSelectedStudy] = useState<EbiosStudy | null>(null)
  const [createOpen, setCreateOpen] = useState(false)

  return (
    <Box sx={{ p: 3 }}>
      <PageHeader
        title="EBIOS RM"
        subtitle="ANSSI 5-workshop risk methodology — feared events, risk sources, strategic scenarios, attack paths, security measures"
        actions={
          !selectedStudy ? (
            <Button variant="contained" size="small" startIcon={<AddOutlined />}
              onClick={() => setCreateOpen(true)}>
              New Study
            </Button>
          ) : undefined
        }
      />

      {selectedStudy ? (
        <StudyDetail study={selectedStudy} onBack={() => setSelectedStudy(null)} />
      ) : (
        <StudyList onSelect={setSelectedStudy} />
      )}

      <CreateStudyDialog open={createOpen} onClose={() => setCreateOpen(false)} />
    </Box>
  )
}
