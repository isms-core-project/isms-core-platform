import { useState } from 'react'
import {
  Alert, Box, Button, Chip, Dialog, DialogActions, DialogContent, DialogTitle,
  FormControl, Grid, IconButton, InputLabel, MenuItem, Select, Skeleton,
  Slider, TextField, Tooltip, Typography,
} from '@mui/material'
import {
  AddOutlined, DeleteOutlined, EditOutlined, HowToRegOutlined, WarningAmberOutlined,
} from '@mui/icons-material'
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import dayjs from 'dayjs'
import { risksApi, type RiskScenario, type RiskScenarioCreate, type RiskAcceptance } from '../api/risksApi'
import { useProject } from '../store/ProjectContext'
import PageHeader from '../components/PageHeader'

// ── Colour helpers ────────────────────────────────────────────────────────────

const LEVEL_COLOR: Record<string, string> = {
  low:      '#4CAF50',
  medium:   '#FF9800',
  high:     '#F44336',
  critical: '#9C27B0',
}

const TREATMENT_LABEL: Record<string, string> = {
  pending:  'Pending',
  accept:   'Accept',
  mitigate: 'Mitigate',
  transfer: 'Transfer',
  avoid:    'Avoid',
}

const STATUS_COLOR: Record<string, string> = {
  open:         '#F44336',
  in_treatment: '#FF9800',
  closed:       '#4CAF50',
  accepted:     '#9E9E9E',
}

function LevelChip({ level }: { level: string }) {
  const color = LEVEL_COLOR[level] ?? '#9E9E9E'
  return (
    <Chip
      label={level.toUpperCase()}
      size="small"
      sx={{ height: 20, fontSize: '0.62rem', fontWeight: 700, bgcolor: `${color}18`, color, border: `1px solid ${color}40` }}
    />
  )
}

// ── Heatmap ───────────────────────────────────────────────────────────────────

function RiskHeatmap() {
  const { data } = useQuery({ queryKey: ['risk-heatmap'], queryFn: risksApi.heatmap })
  if (!data) return null

  const size = 36

  return (
    <Box>
      <Typography variant="caption" sx={{ fontSize: '0.68rem', color: 'text.secondary', mb: 1, display: 'block' }}>
        Risk Heatmap — open scenarios (probability × impact)
      </Typography>
      <Box sx={{ display: 'flex', gap: 0.5, alignItems: 'flex-end' }}>
        {/* Y-axis labels */}
        <Box sx={{ display: 'flex', flexDirection: 'column-reverse', gap: 0.5, mr: 0.5, pb: 3 }}>
          {data.probability_labels.map((l, i) => (
            <Box key={i} sx={{ height: size, display: 'flex', alignItems: 'center', justifyContent: 'flex-end' }}>
              <Typography variant="caption" sx={{ fontSize: '0.57rem', color: 'text.disabled', whiteSpace: 'nowrap' }}>
                {l}
              </Typography>
            </Box>
          ))}
        </Box>

        <Box>
          {/* Grid */}
          <Box sx={{ display: 'flex', flexDirection: 'column-reverse', gap: 0.5 }}>
            {[1, 2, 3, 4, 5].map(p => (
              <Box key={p} sx={{ display: 'flex', gap: 0.5 }}>
                {[1, 2, 3, 4, 5].map(i => {
                  const cell = data.cells.find(c => c.p === p && c.i === i)!
                  const color = LEVEL_COLOR[cell.level] ?? '#9E9E9E'
                  return (
                    <Tooltip key={i} title={`P${p}×I${i}: ${cell.count} scenario${cell.count !== 1 ? 's' : ''}`}>
                      <Box
                        sx={{
                          width: size, height: size, borderRadius: 0.75,
                          bgcolor: `${color}${cell.count > 0 ? '30' : '10'}`,
                          border: `1px solid ${color}${cell.count > 0 ? '60' : '20'}`,
                          display: 'flex', alignItems: 'center', justifyContent: 'center',
                          transition: 'all 0.15s',
                        }}
                      >
                        {cell.count > 0 && (
                          <Typography variant="caption" sx={{ fontSize: '0.65rem', fontWeight: 700, color }}>
                            {cell.count}
                          </Typography>
                        )}
                      </Box>
                    </Tooltip>
                  )
                })}
              </Box>
            ))}
          </Box>

          {/* X-axis labels */}
          <Box sx={{ display: 'flex', gap: 0.5, mt: 0.5 }}>
            {data.impact_labels.map((l, i) => (
              <Box key={i} sx={{ width: size, textAlign: 'center' }}>
                <Typography variant="caption" sx={{ fontSize: '0.52rem', color: 'text.disabled', display: 'block' }}>
                  {l.split(' ')[0]}
                </Typography>
              </Box>
            ))}
          </Box>
        </Box>
      </Box>
      <Typography variant="caption" sx={{ fontSize: '0.6rem', color: 'text.disabled', mt: 0.5, display: 'block' }}>
        Y = Probability · X = Impact
      </Typography>
    </Box>
  )
}

// ── Create / Edit dialog ──────────────────────────────────────────────────────

function RiskDialog({
  open, onClose, existing,
}: { open: boolean; onClose: () => void; existing?: RiskScenario }) {
  const qc = useQueryClient()
  const isEdit = !!existing

  const [form, setForm] = useState<RiskScenarioCreate>(existing ? {
    name: existing.name,
    description: existing.description ?? '',
    threat_source: existing.threat_source ?? '',
    threat_event: existing.threat_event ?? '',
    probability: existing.probability,
    impact: existing.impact,
    treatment_status: existing.treatment_status,
    treatment_notes: existing.treatment_notes ?? '',
    residual_probability: existing.residual_probability ?? undefined,
    residual_impact: existing.residual_impact ?? undefined,
    target_date: existing.target_date ?? '',
    status: existing.status,
  } : {
    name: '', description: '', threat_source: '', threat_event: '',
    probability: 1, impact: 1, treatment_status: 'pending',
    treatment_notes: '', status: 'open',
  })
  const [error, setError] = useState('')

  const createMutation = useMutation({
    mutationFn: (body: RiskScenarioCreate) => risksApi.create(body),
    onSuccess: () => { qc.invalidateQueries({ queryKey: ['risks'] }); qc.invalidateQueries({ queryKey: ['risk-heatmap'] }); qc.invalidateQueries({ queryKey: ['risk-summary'] }); onClose() },
    onError: () => setError('Failed to save risk scenario.'),
  })
  const updateMutation = useMutation({
    mutationFn: (body: RiskScenarioCreate) => risksApi.update(existing!.id, body),
    onSuccess: () => { qc.invalidateQueries({ queryKey: ['risks'] }); qc.invalidateQueries({ queryKey: ['risk-heatmap'] }); qc.invalidateQueries({ queryKey: ['risk-summary'] }); onClose() },
    onError: () => setError('Failed to update risk scenario.'),
  })

  const isPending = createMutation.isPending || updateMutation.isPending

  function handleSubmit() {
    if (!form.name.trim()) { setError('Name is required.'); return }
    const body: RiskScenarioCreate = {
      ...form,
      description: form.description || undefined,
      threat_source: form.threat_source || undefined,
      threat_event: form.threat_event || undefined,
      treatment_notes: form.treatment_notes || undefined,
      target_date: form.target_date || undefined,
    }
    isEdit ? updateMutation.mutate(body) : createMutation.mutate(body)
  }

  const set = (k: keyof RiskScenarioCreate, v: unknown) => setForm(f => ({ ...f, [k]: v }))

  return (
    <Dialog open={open} onClose={onClose} maxWidth="sm" fullWidth>
      <DialogTitle sx={{ pb: 0.5 }}>
        {isEdit ? 'Edit Risk Scenario' : 'New Risk Scenario'}
        <Typography variant="caption" color="text.secondary" display="block">
          ISO 27001:2022 Clause 6.1.2 — Risk identification and assessment
        </Typography>
      </DialogTitle>
      <DialogContent sx={{ pt: '20px !important' }}>
        {error && <Alert severity="error" sx={{ mb: 2, py: 0.5 }}>{error}</Alert>}

        <TextField label="Risk name *" fullWidth size="small" sx={{ mb: 2 }}
          value={form.name} onChange={e => set('name', e.target.value)}
          placeholder="e.g. Unauthorised access to customer data" />

        <TextField label="Description" fullWidth size="small" multiline rows={2} sx={{ mb: 2 }}
          value={form.description ?? ''} onChange={e => set('description', e.target.value)} />

        <Box sx={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 1.5, mb: 2 }}>
          <TextField label="Threat source" size="small"
            value={form.threat_source ?? ''} onChange={e => set('threat_source', e.target.value)}
            placeholder="e.g. External attacker" />
          <TextField label="Threat event" size="small"
            value={form.threat_event ?? ''} onChange={e => set('threat_event', e.target.value)}
            placeholder="e.g. Phishing / credential theft" />
        </Box>

        {/* Probability × Impact sliders */}
        <Box sx={{ bgcolor: 'rgba(255,255,255,0.03)', border: '1px solid', borderColor: 'divider', borderRadius: 1.5, p: 2, mb: 2 }}>
          <Typography variant="caption" sx={{ fontSize: '0.7rem', fontWeight: 600, display: 'block', mb: 1.5 }}>
            Inherent Risk
          </Typography>
          <Box sx={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 2 }}>
            <Box>
              <Typography variant="caption" color="text.secondary" sx={{ fontSize: '0.68rem' }}>
                Probability: <strong>{form.probability}</strong>/5
              </Typography>
              <Slider size="small" min={1} max={5} step={1} marks value={form.probability}
                onChange={(_, v) => set('probability', v as number)}
                sx={{ color: LEVEL_COLOR.medium }} />
            </Box>
            <Box>
              <Typography variant="caption" color="text.secondary" sx={{ fontSize: '0.68rem' }}>
                Impact: <strong>{form.impact}</strong>/5
              </Typography>
              <Slider size="small" min={1} max={5} step={1} marks value={form.impact}
                onChange={(_, v) => set('impact', v as number)}
                sx={{ color: LEVEL_COLOR.high }} />
            </Box>
          </Box>
        </Box>

        <Box sx={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 1.5, mb: 2 }}>
          <FormControl size="small">
            <InputLabel>Treatment</InputLabel>
            <Select label="Treatment" value={form.treatment_status ?? 'pending'}
              onChange={e => set('treatment_status', e.target.value)}>
              {Object.entries(TREATMENT_LABEL).map(([k, v]) => <MenuItem key={k} value={k}>{v}</MenuItem>)}
            </Select>
          </FormControl>
          <FormControl size="small">
            <InputLabel>Status</InputLabel>
            <Select label="Status" value={form.status ?? 'open'}
              onChange={e => set('status', e.target.value)}>
              <MenuItem value="open">Open</MenuItem>
              <MenuItem value="in_treatment">In Treatment</MenuItem>
              <MenuItem value="accepted">Accepted</MenuItem>
              <MenuItem value="closed">Closed</MenuItem>
            </Select>
          </FormControl>
        </Box>

        <TextField label="Treatment notes" fullWidth size="small" multiline rows={2} sx={{ mb: 2 }}
          value={form.treatment_notes ?? ''} onChange={e => set('treatment_notes', e.target.value)}
          placeholder="Describe the treatment plan or acceptance rationale" />

        <TextField label="Target date" fullWidth size="small" sx={{ mb: 2 }}
          value={form.target_date ?? ''} onChange={e => set('target_date', e.target.value)}
          placeholder="YYYY-MM-DD" helperText="Target date to close or complete treatment" />
      </DialogContent>
      <DialogActions sx={{ px: 3, pb: 2 }}>
        <Button onClick={onClose} disabled={isPending}>Cancel</Button>
        <Button variant="contained" onClick={handleSubmit} disabled={isPending}>
          {isEdit ? 'Save' : 'Create'}
        </Button>
      </DialogActions>
    </Dialog>
  )
}

// ── Acceptance dialog ─────────────────────────────────────────────────────────

function AcceptanceDialog({ risk, open, onClose }: { risk: RiskScenario; open: boolean; onClose: () => void }) {
  const qc = useQueryClient()
  const [justification, setJustification] = useState('')
  const [expiryDate, setExpiryDate] = useState('')
  const [error, setError] = useState('')

  const { data: history } = useQuery({
    queryKey: ['acceptances', risk.id],
    queryFn: () => risksApi.listAcceptances(risk.id),
    enabled: open,
  })

  const createMut = useMutation({
    mutationFn: () => risksApi.createAcceptance(risk.id, { justification, expiry_date: expiryDate || undefined }),
    onSuccess: () => {
      qc.invalidateQueries({ queryKey: ['risks'] })
      qc.invalidateQueries({ queryKey: ['acceptances', risk.id] })
      setJustification(''); setExpiryDate('')
    },
    onError: () => setError('Failed to record acceptance.'),
  })

  const revokeMut = useMutation({
    mutationFn: (acceptId: string) => risksApi.revokeAcceptance(risk.id, acceptId),
    onSuccess: () => { qc.invalidateQueries({ queryKey: ['risks'] }); qc.invalidateQueries({ queryKey: ['acceptances', risk.id] }) },
  })

  function handleSubmit() {
    if (!justification.trim()) { setError('Justification is required.'); return }
    setError('')
    createMut.mutate()
  }

  return (
    <Dialog open={open} onClose={onClose} maxWidth="sm" fullWidth>
      <DialogTitle sx={{ pb: 0.5 }}>
        Risk Acceptance
        <Typography variant="caption" color="text.secondary" display="block">{risk.name}</Typography>
      </DialogTitle>
      <DialogContent sx={{ pt: '20px !important' }}>
        {error && <Alert severity="error" sx={{ mb: 2, py: 0.5 }}>{error}</Alert>}

        <TextField
          label="Justification *" fullWidth size="small" multiline rows={3} sx={{ mb: 2 }}
          value={justification} onChange={e => setJustification(e.target.value)}
          placeholder="Explain why the residual risk is acceptable and who has approved it" />

        <TextField
          label="Expiry date" type="date" size="small" fullWidth sx={{ mb: 2 }}
          InputLabelProps={{ shrink: true }}
          value={expiryDate} onChange={e => setExpiryDate(e.target.value)}
          helperText="Leave blank for permanent acceptance" />

        <Button variant="outlined" size="small" onClick={handleSubmit} disabled={createMut.isPending} startIcon={<HowToRegOutlined />}>
          {createMut.isPending ? 'Recording…' : 'Record Acceptance'}
        </Button>

        {history && history.length > 0 && (
          <Box sx={{ mt: 2.5 }}>
            <Typography variant="caption" sx={{ fontWeight: 600, fontSize: '0.7rem', color: 'text.secondary', textTransform: 'uppercase', display: 'block', mb: 1 }}>
              Acceptance History
            </Typography>
            {history.map((a: RiskAcceptance) => (
              <Box key={a.id} sx={{ p: 1.5, mb: 1, borderRadius: 1, border: '1px solid', borderColor: a.status === 'active' ? 'success.dark' : 'divider', bgcolor: a.status === 'active' ? '#4CAF5008' : 'transparent' }}>
                <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                  <Box>
                    <Typography variant="caption" sx={{ fontSize: '0.72rem', fontWeight: 500 }}>{a.approver_name}</Typography>
                    <Typography variant="caption" color="text.secondary" sx={{ fontSize: '0.65rem', display: 'block' }}>
                      {dayjs(a.created_at).format('D MMM YYYY')}
                      {a.expiry_date && ` · Expires ${dayjs(a.expiry_date).format('D MMM YYYY')}`}
                    </Typography>
                  </Box>
                  <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.75 }}>
                    <Chip label={a.status} size="small" sx={{ height: 18, fontSize: '0.6rem', textTransform: 'capitalize',
                      bgcolor: a.status === 'active' ? '#4CAF5018' : '#9E9E9E18',
                      color: a.status === 'active' ? '#4CAF50' : '#9E9E9E',
                    }} />
                    {a.status === 'active' && (
                      <Tooltip title="Revoke">
                        <IconButton size="small" sx={{ p: 0.25, color: 'error.light' }} onClick={() => { if (confirm('Revoke this acceptance?')) revokeMut.mutate(a.id) }}>
                          <DeleteOutlined sx={{ fontSize: 13 }} />
                        </IconButton>
                      </Tooltip>
                    )}
                  </Box>
                </Box>
                <Typography variant="caption" color="text.secondary" sx={{ fontSize: '0.67rem', mt: 0.5, display: 'block' }}>
                  {a.justification}
                </Typography>
              </Box>
            ))}
          </Box>
        )}
      </DialogContent>
      <DialogActions sx={{ px: 3, pb: 2 }}>
        <Button onClick={onClose} size="small">Close</Button>
      </DialogActions>
    </Dialog>
  )
}

// ── Risk row ──────────────────────────────────────────────────────────────────

function RiskRow({ risk }: { risk: RiskScenario }) {
  const qc = useQueryClient()
  const [editOpen, setEditOpen] = useState(false)
  const [acceptOpen, setAcceptOpen] = useState(false)

  const deleteMutation = useMutation({
    mutationFn: () => risksApi.delete(risk.id),
    onSuccess: () => { qc.invalidateQueries({ queryKey: ['risks'] }); qc.invalidateQueries({ queryKey: ['risk-heatmap'] }); qc.invalidateQueries({ queryKey: ['risk-summary'] }) },
  })

  function handleDelete() {
    if (window.confirm(`Delete risk "${risk.name}"?`)) deleteMutation.mutate()
  }

  const statusColor = STATUS_COLOR[risk.status] ?? '#9E9E9E'

  return (
    <>
      <Box
        sx={{
          display: 'grid',
          gridTemplateColumns: '1fr 90px 90px 100px 110px 80px 72px',
          alignItems: 'center',
          gap: 1.5,
          px: 2, py: 1.25,
          borderBottom: '1px solid',
          borderColor: 'divider',
          '&:hover': { bgcolor: 'rgba(255,255,255,0.02)' },
        }}
      >
        {/* Name + threat */}
        <Box sx={{ minWidth: 0 }}>
          <Typography variant="body2" sx={{ fontWeight: 500, fontSize: '0.82rem', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
            {risk.name}
          </Typography>
          {risk.threat_source && (
            <Typography variant="caption" color="text.disabled" sx={{ fontSize: '0.67rem' }}>
              {risk.threat_source}
            </Typography>
          )}
        </Box>

        {/* Inherent */}
        <Box sx={{ textAlign: 'center' }}>
          <Typography variant="caption" sx={{ fontSize: '0.62rem', color: 'text.disabled', display: 'block' }}>P{risk.probability}×I{risk.impact}</Typography>
          <LevelChip level={risk.risk_level} />
        </Box>

        {/* Residual */}
        <Box sx={{ textAlign: 'center' }}>
          {risk.residual_level ? (
            <>
              <Typography variant="caption" sx={{ fontSize: '0.62rem', color: 'text.disabled', display: 'block' }}>P{risk.residual_probability}×I{risk.residual_impact}</Typography>
              <LevelChip level={risk.residual_level} />
            </>
          ) : (
            <Typography variant="caption" color="text.disabled" sx={{ fontSize: '0.67rem' }}>—</Typography>
          )}
        </Box>

        {/* Treatment */}
        <Typography variant="caption" sx={{ fontSize: '0.75rem', color: 'text.secondary' }}>
          {TREATMENT_LABEL[risk.treatment_status] ?? risk.treatment_status}
        </Typography>

        {/* Owner */}
        <Typography variant="caption" color="text.secondary" sx={{ fontSize: '0.72rem', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
          {risk.owner_name ?? '—'}
        </Typography>

        {/* Target date */}
        <Typography variant="caption" color="text.disabled" sx={{ fontSize: '0.7rem' }}>
          {risk.target_date ? dayjs(risk.target_date).format('DD MMM YY') : '—'}
        </Typography>

        {/* Status + actions */}
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.5 }}>
          <Box sx={{ width: 7, height: 7, borderRadius: '50%', bgcolor: statusColor, flexShrink: 0 }} />
          <Tooltip title="Record acceptance">
            <IconButton size="small" onClick={() => setAcceptOpen(true)} sx={{ p: 0.4, color: risk.treatment_status === 'accept' ? 'success.main' : 'text.disabled', '&:hover': { color: 'success.main' } }}>
              <HowToRegOutlined sx={{ fontSize: 14 }} />
            </IconButton>
          </Tooltip>
          <Tooltip title="Edit">
            <IconButton size="small" onClick={() => setEditOpen(true)} sx={{ p: 0.4, color: 'text.disabled', '&:hover': { color: 'primary.main' } }}>
              <EditOutlined sx={{ fontSize: 14 }} />
            </IconButton>
          </Tooltip>
          <Tooltip title="Delete">
            <IconButton size="small" onClick={handleDelete} disabled={deleteMutation.isPending} sx={{ p: 0.4, color: 'text.disabled', '&:hover': { color: 'error.main' } }}>
              <DeleteOutlined sx={{ fontSize: 14 }} />
            </IconButton>
          </Tooltip>
        </Box>
      </Box>

      {editOpen && <RiskDialog open={editOpen} onClose={() => setEditOpen(false)} existing={risk} />}
      {acceptOpen && <AcceptanceDialog risk={risk} open={acceptOpen} onClose={() => setAcceptOpen(false)} />}
    </>
  )
}

// ── Main page ─────────────────────────────────────────────────────────────────

export default function RiskRegister() {
  const [createOpen, setCreateOpen] = useState(false)
  const [filterLevel,     setFilterLevel]     = useState('')
  const [filterTreatment, setFilterTreatment] = useState('')
  const [filterStatus,    setFilterStatus]    = useState('')

  const { activeProject } = useProject()
  const projectId = activeProject?.id

  const { data: summary } = useQuery({
    queryKey: ['risk-summary', projectId],
    queryFn: () => risksApi.summary({ project_id: projectId }),
  })
  const { data: risks, isLoading } = useQuery({
    queryKey: ['risks', filterLevel, filterTreatment, filterStatus, projectId],
    queryFn: () => risksApi.list({
      risk_level:       filterLevel     || undefined,
      treatment_status: filterTreatment || undefined,
      status:           filterStatus    || undefined,
      project_id:       projectId,
    }),
  })

  return (
    <Box sx={{ p: 3 }}>
      <PageHeader
        title="Risk Register"
        subtitle={activeProject
          ? `${activeProject.name} · ISO 27001:2022 §6.1.2`
          : 'ISO 27001:2022 Clause 6.1.2 — identify, analyse, and treat information security risks'}
        actions={
          <Tooltip title={!activeProject ? 'Select a project first to log risks' : ''}>
            <span>
              <Button variant="contained" size="small" startIcon={<AddOutlined />}
                onClick={() => setCreateOpen(true)} disabled={!activeProject}>
                New Risk
              </Button>
            </span>
          </Tooltip>
        }
      />

      {activeProject && (
        <Alert severity="info" sx={{ mb: 2, py: 0.5, fontSize: '0.8rem' }}>
          Showing risks for project: <strong>{activeProject.name}</strong>
          {activeProject.organisation_name ? ` — ${activeProject.organisation_name}` : ''}
        </Alert>
      )}

      {/* Summary row */}
      {summary && (
        <Grid container spacing={1.5} sx={{ mb: 3 }}>
          {[
            { label: 'Total', value: summary.total, color: 'text.secondary' },
            { label: 'Critical', value: summary.critical, color: LEVEL_COLOR.critical },
            { label: 'High',     value: summary.high,     color: LEVEL_COLOR.high },
            { label: 'Medium',   value: summary.medium,   color: LEVEL_COLOR.medium },
            { label: 'Low',      value: summary.low,      color: LEVEL_COLOR.low },
            { label: 'Open',     value: summary.open,     color: STATUS_COLOR.open },
            { label: 'In Treatment', value: summary.in_treatment, color: STATUS_COLOR.in_treatment },
            { label: 'Closed',   value: summary.closed,   color: STATUS_COLOR.closed },
          ].map(({ label, value, color }) => (
            <Grid item key={label}>
              <Box sx={{ px: 1.5, py: 0.75, border: '1px solid', borderColor: 'divider', borderRadius: 1.5, textAlign: 'center', minWidth: 72 }}>
                <Typography variant="h6" sx={{ fontWeight: 700, fontSize: '1.1rem', color, lineHeight: 1 }}>{value}</Typography>
                <Typography variant="caption" color="text.disabled" sx={{ fontSize: '0.65rem' }}>{label}</Typography>
              </Box>
            </Grid>
          ))}
        </Grid>
      )}

      <Grid container spacing={3} sx={{ mb: 3 }}>
        {/* Heatmap */}
        <Grid item xs={12} md={5}>
          <Box sx={{ border: '1px solid', borderColor: 'divider', borderRadius: 1.5, p: 2 }}>
            <RiskHeatmap />
          </Box>
        </Grid>

        {/* Filters */}
        <Grid item xs={12} md={7}>
          <Box sx={{ display: 'flex', gap: 1.5, flexWrap: 'wrap', alignItems: 'center', pt: { md: 3 } }}>
            <FormControl size="small" sx={{ minWidth: 120 }}>
              <InputLabel>Level</InputLabel>
              <Select label="Level" value={filterLevel} onChange={e => setFilterLevel(e.target.value)}>
                <MenuItem value="">All</MenuItem>
                {['critical', 'high', 'medium', 'low'].map(l => (
                  <MenuItem key={l} value={l}><Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}><Box sx={{ width: 8, height: 8, borderRadius: '50%', bgcolor: LEVEL_COLOR[l] }} />{l}</Box></MenuItem>
                ))}
              </Select>
            </FormControl>
            <FormControl size="small" sx={{ minWidth: 130 }}>
              <InputLabel>Treatment</InputLabel>
              <Select label="Treatment" value={filterTreatment} onChange={e => setFilterTreatment(e.target.value)}>
                <MenuItem value="">All</MenuItem>
                {Object.entries(TREATMENT_LABEL).map(([k, v]) => <MenuItem key={k} value={k}>{v}</MenuItem>)}
              </Select>
            </FormControl>
            <FormControl size="small" sx={{ minWidth: 110 }}>
              <InputLabel>Status</InputLabel>
              <Select label="Status" value={filterStatus} onChange={e => setFilterStatus(e.target.value)}>
                <MenuItem value="">All</MenuItem>
                <MenuItem value="open">Open</MenuItem>
                <MenuItem value="in_treatment">In Treatment</MenuItem>
                <MenuItem value="accepted">Accepted</MenuItem>
                <MenuItem value="closed">Closed</MenuItem>
              </Select>
            </FormControl>
          </Box>
        </Grid>
      </Grid>

      {/* Table header */}
      <Box
        sx={{
          display: 'grid',
          gridTemplateColumns: '1fr 90px 90px 100px 110px 80px 72px',
          gap: 1.5, px: 2, py: 0.75,
          bgcolor: 'rgba(255,255,255,0.03)',
          borderRadius: '8px 8px 0 0',
          border: '1px solid', borderColor: 'divider', borderBottom: 'none',
        }}
      >
        {['Risk', 'Inherent', 'Residual', 'Treatment', 'Owner', 'Target', ''].map((h, i) => (
          <Typography key={i} variant="caption" sx={{ fontSize: '0.65rem', textTransform: 'uppercase', letterSpacing: '0.06em', color: 'text.disabled', fontWeight: 600 }}>
            {h}
          </Typography>
        ))}
      </Box>

      {/* Rows */}
      <Box sx={{ border: '1px solid', borderColor: 'divider', borderTop: 'none', borderRadius: '0 0 8px 8px', overflow: 'hidden' }}>
        {isLoading
          ? Array.from({ length: 4 }).map((_, i) => (
              <Box key={i} sx={{ px: 2, py: 1.5, borderBottom: '1px solid', borderColor: 'divider' }}>
                <Skeleton variant="text" width="60%" height={20} />
              </Box>
            ))
          : !risks?.length
          ? (
            <Box sx={{ py: 8, textAlign: 'center' }}>
              <WarningAmberOutlined sx={{ fontSize: 40, color: 'text.disabled', mb: 1.5 }} />
              <Typography color="text.secondary" variant="body2">No risk scenarios yet.</Typography>
              <Typography color="text.disabled" variant="caption" sx={{ display: 'block', mb: 2 }}>
                Create your first risk to comply with ISO 27001:2022 Clause 6.1.2
              </Typography>
              <Button variant="contained" size="small" startIcon={<AddOutlined />} onClick={() => setCreateOpen(true)}>
                New Risk
              </Button>
            </Box>
          )
          : risks.map(r => <RiskRow key={r.id} risk={r} />)
        }
      </Box>

      <RiskDialog open={createOpen} onClose={() => setCreateOpen(false)} />
    </Box>
  )
}
