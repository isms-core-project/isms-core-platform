import { useState } from 'react'
import { useProduct } from '../store/ProductContext'
import {
  Alert,
  Box,
  Button,
  Card,
  CardContent,
  Chip,
  Collapse,
  Dialog,
  DialogActions,
  DialogContent,
  DialogTitle,
  FormControl,
  Grid,
  IconButton,
  InputLabel,
  MenuItem,
  Select,
  Skeleton,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  TextField,
  Tooltip,
  Typography,
  ToggleButton,
  ToggleButtonGroup,
} from '@mui/material'
import {
  AddOutlined,
  AttachFileOutlined,
  DeleteOutlined,
  EditOutlined,
  ExpandMoreOutlined,
  ExpandLessOutlined,
  FindInPageOutlined,
  LinkOffOutlined,
} from '@mui/icons-material'
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import dayjs from 'dayjs'
import { gapsApi } from '../api/gaps'
import { evidenceApi } from '../api/evidence'
import { controlsApi } from '../api/controls'
import { dashboardApi } from '../api/dashboard'
import { assessmentsApi } from '../api/assessmentsApi'
import PageHeader from '../components/PageHeader'
import MetricCard from '../components/MetricCard'
import StatusChip from '../components/StatusChip'
import type { GapRead, GapCreate, GapPatch } from '../api/types'

const SEVERITIES = ['critical', 'high', 'medium', 'low']
const STATUSES = ['open', 'in_progress', 'accepted', 'closed']
const PRODUCTS = ['framework', 'operational', 'both']

const SEV_COLOR: Record<string, string> = {
  critical: '#C00000',
  high: '#FF5722',
  medium: '#FF9800',
  low: '#4CAF50',
}

// ── Create dialog ────────────────────────────────────────────────────────────
function CreateGapDialog({
  open,
  onClose,
  onCreated,
  productFamily,
}: {
  open: boolean
  onClose: () => void
  onCreated: () => void
  productFamily: string
}) {
  const [form, setForm] = useState<GapCreate>({
    control_group_id: '',
    gap_description: '',
    severity: 'medium',
    product_type: 'both',
    owner: '',
    due_date: '',
    remediation_plan: '',
  })
  const [workbookId, setWorkbookId] = useState('')
  const [error, setError] = useState('')

  const { data: controls } = useQuery({
    queryKey: ['controls', productFamily],
    queryFn: () => controlsApi.list({ product_family: productFamily }),
  })

  const selectedGroupCode = (controls ?? []).find(c => c.id === form.control_group_id)?.group_code ?? ''
  const showWorkbookPicker = !!selectedGroupCode && form.product_type !== 'operational'

  const { data: generators = [] } = useQuery({
    queryKey: ['generators-for-group', selectedGroupCode],
    queryFn: () => assessmentsApi.getGeneratorsForGroup(selectedGroupCode),
    enabled: showWorkbookPicker,
  })

  const qc = useQueryClient()
  const mutation = useMutation({
    mutationFn: (body: GapCreate) => gapsApi.create(body),
    onSuccess: () => {
      qc.invalidateQueries({ queryKey: ['gaps'] })
      qc.invalidateQueries({ queryKey: ['dashboard', 'gaps'] })
      onCreated()
      onClose()
      setForm({ control_group_id: '', gap_description: '', severity: 'medium', product_type: 'both' })
      setWorkbookId('')
      setError('')
    },
    onError: (e: unknown) => {
      const msg = (e as { response?: { data?: { detail?: string } } })?.response?.data?.detail
      setError(msg ?? 'Failed to create gap')
    },
  })

  const handleSubmit = () => {
    if (!form.control_group_id) { setError('Select a control group'); return }
    if (!form.gap_description.trim()) { setError('Description is required'); return }
    mutation.mutate({
      ...form,
      owner: form.owner || undefined,
      due_date: form.due_date || undefined,
      remediation_plan: form.remediation_plan || undefined,
      workbook_document_id: workbookId || undefined,
    })
  }

  const set = (k: keyof GapCreate, v: string) => setForm((f) => ({ ...f, [k]: v }))

  return (
    <Dialog open={open} onClose={onClose} maxWidth="sm" fullWidth>
      <DialogTitle>Create Gap</DialogTitle>
      <DialogContent sx={{ display: 'flex', flexDirection: 'column', gap: 2, pt: '12px !important' }}>
        {error && <Alert severity="error">{error}</Alert>}

        <FormControl size="small" fullWidth required>
          <InputLabel>Control Group</InputLabel>
          <Select
            value={form.control_group_id}
            onChange={(e) => set('control_group_id', e.target.value)}
            label="Control Group"
          >
            {(controls ?? []).map((c) => (
              <MenuItem key={c.id} value={c.id}>
                <Typography variant="caption" sx={{ fontFamily: 'monospace', color: 'primary.light', mr: 1 }}>
                  {c.group_code.toUpperCase()}
                </Typography>
                {c.group_name}
              </MenuItem>
            ))}
          </Select>
        </FormControl>

        <TextField
          label="Description"
          size="small"
          required
          multiline
          minRows={2}
          value={form.gap_description}
          onChange={(e) => set('gap_description', e.target.value)}
        />

        <Box sx={{ display: 'flex', gap: 2 }}>
          <FormControl size="small" fullWidth>
            <InputLabel>Severity</InputLabel>
            <Select value={form.severity} onChange={(e) => set('severity', e.target.value)} label="Severity">
              {SEVERITIES.map((s) => (
                <MenuItem key={s} value={s}>{s.charAt(0).toUpperCase() + s.slice(1)}</MenuItem>
              ))}
            </Select>
          </FormControl>
          <FormControl size="small" fullWidth>
            <InputLabel>Product</InputLabel>
            <Select value={form.product_type} onChange={(e) => set('product_type', e.target.value)} label="Product">
              {PRODUCTS.map((p) => (
                <MenuItem key={p} value={p}>{p.charAt(0).toUpperCase() + p.slice(1)}</MenuItem>
              ))}
            </Select>
          </FormControl>
        </Box>

        {showWorkbookPicker && generators.length > 1 && (
          <FormControl size="small" fullWidth>
            <InputLabel>Workbook / IMP (optional)</InputLabel>
            <Select
              value={workbookId}
              onChange={(e) => setWorkbookId(e.target.value)}
              label="Workbook / IMP (optional)"
            >
              <MenuItem value="">Any</MenuItem>
              {generators.map((g) => (
                <MenuItem key={g.document_id} value={g.document_id}>
                  <Typography variant="caption" sx={{ fontFamily: 'monospace', color: 'primary.light', mr: 1 }}>
                    {g.document_id}
                  </Typography>
                  {g.workbook_name}
                </MenuItem>
              ))}
            </Select>
          </FormControl>
        )}

        <Box sx={{ display: 'flex', gap: 2 }}>
          <TextField
            label="Owner"
            size="small"
            fullWidth
            value={form.owner ?? ''}
            onChange={(e) => set('owner', e.target.value)}
          />
          <TextField
            label="Due Date"
            size="small"
            type="date"
            fullWidth
            InputLabelProps={{ shrink: true }}
            value={form.due_date ?? ''}
            onChange={(e) => set('due_date', e.target.value)}
          />
        </Box>

        <TextField
          label="Remediation Plan"
          size="small"
          multiline
          minRows={2}
          value={form.remediation_plan ?? ''}
          onChange={(e) => set('remediation_plan', e.target.value)}
        />
      </DialogContent>
      <DialogActions>
        <Button onClick={onClose} size="small">Cancel</Button>
        <Button onClick={handleSubmit} variant="contained" size="small" disabled={mutation.isPending}>
          Create Gap
        </Button>
      </DialogActions>
    </Dialog>
  )
}

// ── Evidence picker dialog ────────────────────────────────────────────────────
function EvidencePickerDialog({
  gap,
  open,
  onClose,
}: {
  gap: GapRead
  open: boolean
  onClose: () => void
}) {
  const qc = useQueryClient()
  const [search, setSearch] = useState('')

  const { data: allEvidence = [] } = useQuery({
    queryKey: ['evidence', 'for-picker', gap.control_group_id],
    queryFn: () => evidenceApi.list({ control_group_id: gap.control_group_id, limit: 200 }),
    enabled: open,
  })

  const { data: linked = [] } = useQuery({
    queryKey: ['gap-evidence', gap.id],
    queryFn: () => gapsApi.listEvidence(gap.id),
    enabled: open,
  })

  const linkedIds = new Set(linked.map((e) => e.id))

  const attachMutation = useMutation({
    mutationFn: (evidenceId: string) => gapsApi.attachEvidence(gap.id, evidenceId),
    onSuccess: () => {
      qc.invalidateQueries({ queryKey: ['gap-evidence', gap.id] })
      qc.invalidateQueries({ queryKey: ['gaps'] })
    },
  })

  const detachMutation = useMutation({
    mutationFn: (evidenceId: string) => gapsApi.detachEvidence(gap.id, evidenceId),
    onSuccess: () => {
      qc.invalidateQueries({ queryKey: ['gap-evidence', gap.id] })
      qc.invalidateQueries({ queryKey: ['gaps'] })
    },
  })

  const filtered = allEvidence.filter((e) =>
    !search || e.title.toLowerCase().includes(search.toLowerCase())
  )

  return (
    <Dialog open={open} onClose={onClose} maxWidth="sm" fullWidth>
      <DialogTitle sx={{ pb: 0.5 }}>
        Attach Evidence
        <Typography variant="caption" color="text.secondary" display="block">
          {gap.control_group_code.toUpperCase()} — {gap.control_group_name}
        </Typography>
      </DialogTitle>
      <DialogContent>
        <TextField
          fullWidth size="small" placeholder="Search evidence…"
          value={search} onChange={(e) => setSearch(e.target.value)}
          sx={{ mb: 1.5, mt: 0.5, '& .MuiInputBase-input': { fontSize: '0.8rem' } }}
        />
        {filtered.length === 0 && (
          <Typography variant="body2" color="text.secondary">
            No evidence found for this control group. Upload evidence first.
          </Typography>
        )}
        {filtered.map((ev) => {
          const isLinked = linkedIds.has(ev.id)
          return (
            <Box
              key={ev.id}
              sx={{
                display: 'flex', alignItems: 'center', gap: 1.5, py: 0.75,
                borderBottom: '1px solid', borderColor: 'divider',
              }}
            >
              <Box sx={{ flex: 1, minWidth: 0 }}>
                <Typography variant="body2" noWrap>{ev.title}</Typography>
                <Typography variant="caption" color="text.secondary">
                  {ev.evidence_type} · {ev.collected_date ?? 'no date'}
                </Typography>
              </Box>
              <Button
                size="small"
                variant={isLinked ? 'outlined' : 'contained'}
                color={isLinked ? 'error' : 'primary'}
                startIcon={isLinked ? <LinkOffOutlined /> : <AttachFileOutlined />}
                disabled={attachMutation.isPending || detachMutation.isPending}
                onClick={() => isLinked ? detachMutation.mutate(ev.id) : attachMutation.mutate(ev.id)}
                sx={{ fontSize: '0.7rem', whiteSpace: 'nowrap' }}
              >
                {isLinked ? 'Detach' : 'Attach'}
              </Button>
            </Box>
          )
        })}
      </DialogContent>
      <DialogActions>
        <Button onClick={onClose}>Done</Button>
      </DialogActions>
    </Dialog>
  )
}

// ── Inline edit row ──────────────────────────────────────────────────────────
function EditRow({ gap, onClose }: { gap: GapRead; onClose: () => void }) {
  const [form, setForm] = useState<GapPatch>({
    gap_description: gap.gap_description,
    severity: gap.severity,
    status: gap.status,
    owner: gap.owner ?? '',
    due_date: gap.due_date ?? '',
    remediation_plan: gap.remediation_plan ?? '',
  })
  const [error, setError] = useState('')
  const [evidenceOpen, setEvidenceOpen] = useState(false)

  const qc = useQueryClient()
  const mutation = useMutation({
    mutationFn: (body: GapPatch) => gapsApi.patch(gap.id, body),
    onSuccess: () => {
      qc.invalidateQueries({ queryKey: ['gaps'] })
      qc.invalidateQueries({ queryKey: ['dashboard', 'gaps'] })
      onClose()
    },
    onError: () => setError('Failed to save changes'),
  })

  const { data: linked = [] } = useQuery({
    queryKey: ['gap-evidence', gap.id],
    queryFn: () => gapsApi.listEvidence(gap.id),
  })

  const detachMutation = useMutation({
    mutationFn: (evidenceId: string) => gapsApi.detachEvidence(gap.id, evidenceId),
    onSuccess: () => {
      qc.invalidateQueries({ queryKey: ['gap-evidence', gap.id] })
      qc.invalidateQueries({ queryKey: ['gaps'] })
    },
  })

  const set = (k: keyof GapPatch, v: string | null) => setForm((f) => ({ ...f, [k]: v }))

  return (
    <>
      <EvidencePickerDialog gap={gap} open={evidenceOpen} onClose={() => setEvidenceOpen(false)} />
      <TableRow>
        <TableCell colSpan={7} sx={{ p: 2, bgcolor: 'rgba(68,114,196,0.06)' }}>
          {error && <Alert severity="error" sx={{ mb: 1 }}>{error}</Alert>}
          <Box sx={{ display: 'flex', flexDirection: 'column', gap: 1.5 }}>
            <TextField
              label="Description"
              size="small"
              multiline
              minRows={2}
              fullWidth
              value={form.gap_description ?? ''}
              onChange={(e) => set('gap_description', e.target.value)}
            />
            <Box sx={{ display: 'flex', gap: 2 }}>
              <FormControl size="small" fullWidth>
                <InputLabel>Severity</InputLabel>
                <Select value={form.severity ?? ''} onChange={(e) => set('severity', e.target.value)} label="Severity">
                  {SEVERITIES.map((s) => (
                    <MenuItem key={s} value={s}>{s.charAt(0).toUpperCase() + s.slice(1)}</MenuItem>
                  ))}
                </Select>
              </FormControl>
              <FormControl size="small" fullWidth>
                <InputLabel>Status</InputLabel>
                <Select value={form.status ?? ''} onChange={(e) => set('status', e.target.value)} label="Status">
                  {STATUSES.map((s) => (
                    <MenuItem key={s} value={s}>{s.replace('_', ' ')}</MenuItem>
                  ))}
                </Select>
              </FormControl>
              <TextField
                label="Owner"
                size="small"
                fullWidth
                value={form.owner ?? ''}
                onChange={(e) => set('owner', e.target.value)}
              />
              <TextField
                label="Due Date"
                size="small"
                type="date"
                fullWidth
                InputLabelProps={{ shrink: true }}
                value={form.due_date ?? ''}
                onChange={(e) => set('due_date', e.target.value || null)}
              />
            </Box>
            <TextField
              label="Remediation Plan"
              size="small"
              multiline
              minRows={2}
              fullWidth
              value={form.remediation_plan ?? ''}
              onChange={(e) => set('remediation_plan', e.target.value)}
            />

            {/* Evidence panel */}
            <Box>
              <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 0.75 }}>
                <Typography variant="caption" color="text.secondary" fontWeight={600}>
                  EVIDENCE LINKED
                </Typography>
                <Chip label={linked.length} size="small" sx={{ height: 16, fontSize: '0.62rem' }} />
                <Button
                  size="small"
                  variant="outlined"
                  startIcon={<AttachFileOutlined />}
                  onClick={() => setEvidenceOpen(true)}
                  sx={{ fontSize: '0.7rem', ml: 'auto' }}
                >
                  Attach Evidence
                </Button>
              </Box>
              {linked.length === 0 && (
                <Typography variant="caption" color="text.disabled">No evidence attached.</Typography>
              )}
              {linked.map((ev) => (
                <Box
                  key={ev.id}
                  sx={{
                    display: 'flex', alignItems: 'center', gap: 1, py: 0.5,
                    borderBottom: '1px solid', borderColor: 'divider',
                  }}
                >
                  <AttachFileOutlined sx={{ fontSize: 14, color: 'text.secondary' }} />
                  <Box sx={{ flex: 1, minWidth: 0 }}>
                    <Typography variant="caption" noWrap>{ev.title}</Typography>
                    <Typography variant="caption" color="text.secondary" sx={{ ml: 0.75 }}>
                      {ev.evidence_type}
                    </Typography>
                  </Box>
                  <Tooltip title="Remove link">
                    <IconButton
                      size="small"
                      onClick={() => detachMutation.mutate(ev.id)}
                      disabled={detachMutation.isPending}
                    >
                      <LinkOffOutlined sx={{ fontSize: 14 }} />
                    </IconButton>
                  </Tooltip>
                </Box>
              ))}
            </Box>

            <Box sx={{ display: 'flex', gap: 1 }}>
              <Button
                variant="contained"
                size="small"
                disabled={mutation.isPending}
                onClick={() => mutation.mutate({
                  ...form,
                  owner: form.owner || null,
                  due_date: form.due_date || null,
                  remediation_plan: form.remediation_plan || null,
                })}
              >
                Save
              </Button>
              <Button size="small" onClick={onClose}>Cancel</Button>
            </Box>
          </Box>
        </TableCell>
      </TableRow>
    </>
  )
}

// ── Gap row ──────────────────────────────────────────────────────────────────
function GapRow({ gap }: { gap: GapRead }) {
  const [editing, setEditing] = useState(false)
  const qc = useQueryClient()

  const deleteMutation = useMutation({
    mutationFn: () => gapsApi.delete(gap.id),
    onSuccess: () => {
      qc.invalidateQueries({ queryKey: ['gaps'] })
      qc.invalidateQueries({ queryKey: ['dashboard', 'gaps'] })
    },
  })

  const overdue = gap.due_date && gap.status !== 'closed' && dayjs(gap.due_date).isBefore(dayjs())

  return (
    <>
      <TableRow hover sx={{ opacity: gap.status === 'closed' ? 0.55 : 1 }}>
        <TableCell>
          <Typography variant="caption" sx={{ fontFamily: 'monospace', color: 'primary.light', fontWeight: 700 }}>
            {gap.control_group_code.toUpperCase()}
          </Typography>
          <Typography variant="caption" color="text.secondary" sx={{ display: 'block', lineHeight: 1.3 }}>
            {gap.control_group_name}
          </Typography>
        </TableCell>
        <TableCell sx={{ maxWidth: 300 }}>
          <Typography variant="caption" sx={{ display: '-webkit-box', WebkitLineClamp: 2, WebkitBoxOrient: 'vertical', overflow: 'hidden' }}>
            {gap.gap_description}
          </Typography>
        </TableCell>
        <TableCell>
          <Chip
            label={gap.severity}
            size="small"
            sx={{ fontSize: '0.65rem', height: 18, bgcolor: `${SEV_COLOR[gap.severity]}22`, color: SEV_COLOR[gap.severity], fontWeight: 700 }}
          />
        </TableCell>
        <TableCell><StatusChip status={gap.status} /></TableCell>
        <TableCell>
          <Typography variant="caption" color={gap.owner ? 'text.primary' : 'text.disabled'}>
            {gap.owner ?? '—'}
          </Typography>
        </TableCell>
        <TableCell>
          {gap.due_date ? (
            <Typography variant="caption" sx={{ color: overdue ? '#FFC7CE' : 'text.secondary' }}>
              {dayjs(gap.due_date).format('DD MMM YYYY')}
              {overdue && ' ⚠'}
            </Typography>
          ) : (
            <Typography variant="caption" color="text.disabled">—</Typography>
          )}
        </TableCell>
        <TableCell align="right" sx={{ whiteSpace: 'nowrap' }}>
          {gap.evidence_count > 0 && (
            <Chip
              label={`${gap.evidence_count} ev`}
              size="small"
              sx={{ height: 16, fontSize: '0.62rem', bgcolor: '#1a2a3a', color: '#9fc8f0', mr: 0.5 }}
            />
          )}
          <Tooltip title="Edit">
            <IconButton size="small" onClick={() => setEditing((v) => !v)}>
              {editing ? <ExpandLessOutlined fontSize="small" /> : <EditOutlined fontSize="small" />}
            </IconButton>
          </Tooltip>
          <Tooltip title="Delete">
            <IconButton
              size="small"
              onClick={() => { if (window.confirm('Delete this gap?')) deleteMutation.mutate() }}
              disabled={deleteMutation.isPending}
              sx={{ color: 'error.main' }}
            >
              <DeleteOutlined fontSize="small" />
            </IconButton>
          </Tooltip>
        </TableCell>
      </TableRow>
      {editing && <EditRow gap={gap} onClose={() => setEditing(false)} />}
    </>
  )
}

// ── Main page ────────────────────────────────────────────────────────────────
export default function Gaps() {
  const { product: globalProduct } = useProduct()
  const [severity, setSeverity] = useState('')
  const [status, setStatus] = useState('open')
  const [createOpen, setCreateOpen] = useState(false)

  const productParam = globalProduct === 'isms' ? undefined : globalProduct

  const { data, isLoading, error } = useQuery({
    queryKey: ['gaps', severity, status, productParam],
    queryFn: () => gapsApi.list({
      severity: severity || undefined,
      status: status || undefined,
      product: productParam,
    }),
  })

  // Dashboard summary for metrics
  const { data: summary } = useQuery({
    queryKey: ['dashboard', 'gaps', '', '', ''],
    queryFn: () => dashboardApi.getGaps({ limit: 1 }),
  })

  const critical = summary?.by_severity['critical'] ?? 0
  const high = summary?.by_severity['high'] ?? 0
  const open = summary?.by_status['open'] ?? 0

  return (
    <Box>
      <PageHeader
        title="Gap Analysis"
        subtitle={`${summary?.total ?? 0} total gaps · ${open} open`}
        actions={
          <Button
            variant="contained"
            size="small"
            startIcon={<AddOutlined />}
            onClick={() => setCreateOpen(true)}
          >
            Create Gap
          </Button>
        }
      />

      {/* Metrics */}
      {summary && (
        <Grid container spacing={2} sx={{ mb: 2 }}>
          <Grid item xs={6} sm={3}>
            <MetricCard title="Total" value={summary.total} icon={<FindInPageOutlined fontSize="small" />} />
          </Grid>
          <Grid item xs={6} sm={3}>
            <MetricCard title="Critical" value={critical} sx={critical > 0 ? { borderColor: '#C00000', '& h5': { color: '#C00000' } } : {}} />
          </Grid>
          <Grid item xs={6} sm={3}>
            <MetricCard title="High" value={high} sx={high > 0 ? { borderColor: '#FF5722', '& h5': { color: '#FF5722' } } : {}} />
          </Grid>
          <Grid item xs={6} sm={3}>
            <MetricCard title="Open" value={open} />
          </Grid>
        </Grid>
      )}

      {/* Filters */}
      <Card sx={{ mb: 2 }}>
        <CardContent sx={{ pb: '12px !important' }}>
          <Box sx={{ display: 'flex', gap: 2, flexWrap: 'wrap', alignItems: 'center' }}>
            <ToggleButtonGroup
              value={status}
              exclusive
              onChange={(_, v) => v !== null && setStatus(v)}
              size="small"
              sx={{
                '& .MuiToggleButton-root': {
                  px: 2, py: 0.4, fontSize: '0.78rem', fontWeight: 600,
                  borderColor: 'divider', color: 'text.secondary',
                  '&.Mui-selected': { color: 'primary.light', bgcolor: 'rgba(68,114,196,0.15)' },
                },
              }}
            >
              <ToggleButton value="">All</ToggleButton>
              <ToggleButton value="open">Open</ToggleButton>
              <ToggleButton value="in_progress">In Progress</ToggleButton>
              <ToggleButton value="accepted">Accepted</ToggleButton>
              <ToggleButton value="closed">Closed</ToggleButton>
            </ToggleButtonGroup>

            <FormControl size="small" sx={{ minWidth: 130 }}>
              <InputLabel>Severity</InputLabel>
              <Select value={severity} onChange={(e) => setSeverity(e.target.value)} label="Severity">
                <MenuItem value="">All</MenuItem>
                {SEVERITIES.map((s) => <MenuItem key={s} value={s}>{s.charAt(0).toUpperCase() + s.slice(1)}</MenuItem>)}
              </Select>
            </FormControl>

          </Box>
        </CardContent>
      </Card>

      {error && <Alert severity="error" sx={{ mb: 2 }}>Failed to load gaps.</Alert>}

      {!isLoading && (data ?? []).length === 0 && (
        <Alert severity="success">No gaps match the current filters.</Alert>
      )}

      {((data ?? []).length > 0 || isLoading) && (
        <TableContainer component={Card}>
          <Table size="small">
            <TableHead>
              <TableRow>
                <TableCell sx={{ width: 160 }}>Control Group</TableCell>
                <TableCell>Description</TableCell>
                <TableCell sx={{ width: 90 }}>Severity</TableCell>
                <TableCell sx={{ width: 100 }}>Status</TableCell>
                <TableCell sx={{ width: 120 }}>Owner</TableCell>
                <TableCell sx={{ width: 110 }}>Due Date</TableCell>
                <TableCell sx={{ width: 80 }} align="right">Actions</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {isLoading &&
                [...Array(6)].map((_, i) => (
                  <TableRow key={i}>
                    {[...Array(7)].map((_, j) => (
                      <TableCell key={j}><Skeleton variant="text" /></TableCell>
                    ))}
                  </TableRow>
                ))}
              {(data ?? []).map((gap) => (
                <GapRow key={gap.id} gap={gap} />
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      )}

      <CreateGapDialog
        open={createOpen}
        onClose={() => setCreateOpen(false)}
        onCreated={() => {}}
        productFamily={globalProduct.toUpperCase()}
      />
    </Box>
  )
}
