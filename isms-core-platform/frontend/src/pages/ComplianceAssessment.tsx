import { useState, useRef, useCallback } from 'react'
import {
  Box, Typography, Button, Chip, LinearProgress, Select, MenuItem,
  TextField, Table, TableBody, TableCell, TableContainer, TableHead,
  TableRow, Paper, Dialog, DialogTitle, DialogContent, DialogActions,
  IconButton, Tooltip, Alert, Collapse, Divider,
} from '@mui/material'
import {
  AddOutlined, DeleteOutlined, ExpandMoreOutlined, ExpandLessOutlined,
  CheckCircleOutlined, CancelOutlined, RemoveCircleOutlined,
  RadioButtonUncheckedOutlined, PauseCircleOutlined,
  EditOutlined, ArrowBackOutlined,
} from '@mui/icons-material'
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { regulatoryApi, type AssessmentSummary, type FullAssessment, type RatingUpsert } from '../api/regulatoryApi'

// ── Constants ──────────────────────────────────────────────────────────────────

const SCORE_LABELS: Record<number, string> = {
  0: 'Non-compliant',
  1: 'Initial',
  2: 'Developing',
  3: 'Defined',
  4: 'Optimised',
}

const SCORE_COLORS: Record<number, string> = {
  0: '#f44336',
  1: '#FF9800',
  2: '#FFC107',
  3: '#8BC34A',
  4: '#4CAF50',
}

const STATUS_CONFIG = {
  not_assessed:   { label: 'Not Assessed', color: '#9e9e9e', icon: <RadioButtonUncheckedOutlined sx={{ fontSize: 14 }} /> },
  not_applicable: { label: 'N/A',          color: '#607d8b', icon: <RemoveCircleOutlined sx={{ fontSize: 14 }} /> },
  non_compliant:  { label: 'Non-Compliant', color: '#f44336', icon: <CancelOutlined sx={{ fontSize: 14 }} /> },
  partial:        { label: 'Partial',       color: '#FF9800', icon: <PauseCircleOutlined sx={{ fontSize: 14 }} /> },
  compliant:      { label: 'Compliant',     color: '#4CAF50', icon: <CheckCircleOutlined sx={{ fontSize: 14 }} /> },
}

const FRAMEWORK_META: Record<string, { name: string; subtitle: string; color: string; description: string }> = {
  NIS2: {
    name: 'NIS2 Directive',
    subtitle: 'EU 2022/2555',
    color: '#003399',
    description: 'Network and Information Security Directive 2 — Cybersecurity measures for essential and important entities.',
  },
  DORA: {
    name: 'DORA',
    subtitle: 'EU 2022/2554',
    color: '#1565C0',
    description: 'Digital Operational Resilience Act — ICT risk management for financial entities.',
  },
  CIS_V8: {
    name: 'CIS Controls',
    subtitle: 'v8',
    color: '#2E7D32',
    description: 'CIS Critical Security Controls v8 — 18 controls and 153 safeguards for enterprise cyber defence.',
  },
}

// ── Helpers ────────────────────────────────────────────────────────────────────

function ScoreBadge({ score }: { score: number | null }) {
  if (score === null) return <Typography variant="caption" color="text.disabled">—</Typography>
  return (
    <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.5 }}>
      <Box sx={{ width: 8, height: 8, borderRadius: '50%', bgcolor: SCORE_COLORS[score] }} />
      <Typography variant="caption" sx={{ color: SCORE_COLORS[score], fontWeight: 600 }}>
        {score} — {SCORE_LABELS[score]}
      </Typography>
    </Box>
  )
}

function StatusChip({ status }: { status: string }) {
  const cfg = STATUS_CONFIG[status as keyof typeof STATUS_CONFIG] ?? STATUS_CONFIG.not_assessed
  return (
    <Chip
      icon={cfg.icon}
      label={cfg.label}
      size="small"
      sx={{ bgcolor: cfg.color + '22', color: cfg.color, border: `1px solid ${cfg.color}44`, '& .MuiChip-icon': { color: cfg.color } }}
    />
  )
}

function ScoreBar({ value, max = 4, color }: { value: number | null; max?: number; color: string }) {
  if (value === null) return <Box sx={{ height: 6, bgcolor: 'rgba(255,255,255,0.08)', borderRadius: 3 }} />
  return (
    <Box sx={{ position: 'relative', height: 6, bgcolor: 'rgba(255,255,255,0.08)', borderRadius: 3, overflow: 'hidden' }}>
      <Box sx={{ position: 'absolute', left: 0, top: 0, height: '100%', width: `${Math.min(100, (value / max) * 100)}%`, bgcolor: color, borderRadius: 3, transition: 'width 0.4s ease' }} />
    </Box>
  )
}

// ── Create dialog ──────────────────────────────────────────────────────────────

function CreateDialog({
  open, frameworkCode, onClose,
}: { open: boolean; frameworkCode: string; onClose: () => void }) {
  const queryClient = useQueryClient()
  const [name, setName] = useState('')
  const [assessor, setAssessor] = useState('')
  const [org, setOrg] = useState('')
  const [scope, setScope] = useState('')

  const meta = FRAMEWORK_META[frameworkCode] ?? { name: frameworkCode }

  const mutation = useMutation({
    mutationFn: () => regulatoryApi.createAssessment(frameworkCode, {
      framework_code: frameworkCode,
      name,
      assessor: assessor || undefined,
      organisation: org || undefined,
      scope: scope || undefined,
    }),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['regulatory', frameworkCode, 'assessments'] })
      setName('')
      setAssessor('')
      setOrg('')
      setScope('')
      onClose()
    },
  })

  return (
    <Dialog open={open} onClose={onClose} maxWidth="sm" fullWidth>
      <DialogTitle>New {meta.name} Assessment</DialogTitle>
      <DialogContent sx={{ display: 'flex', flexDirection: 'column', gap: 2, pt: '16px !important' }}>
        <TextField label="Assessment Name" value={name} onChange={e => setName(e.target.value)} required fullWidth size="small" />
        <TextField label="Organisation" value={org} onChange={e => setOrg(e.target.value)} fullWidth size="small" />
        <TextField label="Assessor" value={assessor} onChange={e => setAssessor(e.target.value)} fullWidth size="small" />
        <TextField label="Scope" value={scope} onChange={e => setScope(e.target.value)} fullWidth size="small" multiline rows={2} />
      </DialogContent>
      <DialogActions sx={{ px: 3, pb: 2 }}>
        <Button onClick={onClose}>Cancel</Button>
        <Button variant="contained" disabled={!name || mutation.isPending} onClick={() => mutation.mutate()}>
          Create
        </Button>
      </DialogActions>
    </Dialog>
  )
}

// ── Assessment list card ───────────────────────────────────────────────────────

function AssessmentCard({
  assessment, frameworkCode, onSelect, onDelete,
}: {
  assessment: AssessmentSummary
  frameworkCode: string
  onSelect: (id: string) => void
  onDelete: (id: string) => void
}) {
  const meta = FRAMEWORK_META[frameworkCode] ?? { color: '#1976d2' }
  const pct = assessment.total_requirements > 0
    ? Math.round((assessment.rated_count / assessment.total_requirements) * 100)
    : 0
  const compliancePct = assessment.total_requirements > 0
    ? Math.round((assessment.compliant_count / assessment.total_requirements) * 100)
    : 0

  return (
    <Paper
      elevation={0}
      sx={{
        p: 2.5, border: '1px solid', borderColor: 'divider', borderRadius: 2, cursor: 'pointer',
        transition: 'border-color 0.15s, background 0.15s',
        '&:hover': { borderColor: meta.color, bgcolor: meta.color + '08' },
      }}
      onClick={() => onSelect(assessment.id)}
    >
      <Box sx={{ display: 'flex', alignItems: 'flex-start', justifyContent: 'space-between', mb: 1.5 }}>
        <Box>
          <Typography variant="subtitle1" fontWeight={600}>{assessment.name}</Typography>
          {assessment.organisation && (
            <Typography variant="caption" color="text.secondary">{assessment.organisation}</Typography>
          )}
        </Box>
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
          <Chip
            label={assessment.status.replace('_', ' ')}
            size="small"
            sx={{ textTransform: 'capitalize', fontSize: '0.65rem' }}
          />
          <IconButton
            size="small"
            onClick={e => { e.stopPropagation(); onDelete(assessment.id) }}
            sx={{ color: 'text.disabled', '&:hover': { color: 'error.main' } }}
          >
            <DeleteOutlined sx={{ fontSize: 16 }} />
          </IconButton>
        </Box>
      </Box>

      <Box sx={{ display: 'grid', gridTemplateColumns: '1fr 1fr 1fr', gap: 2, mb: 2 }}>
        <Box>
          <Typography variant="caption" color="text.secondary">Current Score</Typography>
          <Typography variant="body2" fontWeight={600} sx={{ color: assessment.avg_current_score !== null ? SCORE_COLORS[Math.round(assessment.avg_current_score)] : 'text.disabled' }}>
            {assessment.avg_current_score !== null ? assessment.avg_current_score.toFixed(1) : '—'}
          </Typography>
        </Box>
        <Box>
          <Typography variant="caption" color="text.secondary">Compliant</Typography>
          <Typography variant="body2" fontWeight={600} sx={{ color: '#4CAF50' }}>
            {assessment.compliant_count} / {assessment.total_requirements}
          </Typography>
        </Box>
        <Box>
          <Typography variant="caption" color="text.secondary">Gaps</Typography>
          <Typography variant="body2" fontWeight={600} sx={{ color: assessment.non_compliant_count > 0 ? '#f44336' : 'text.secondary' }}>
            {assessment.non_compliant_count + assessment.partial_count}
          </Typography>
        </Box>
      </Box>

      <Box sx={{ mb: 0.5 }}>
        <Box sx={{ display: 'flex', justifyContent: 'space-between', mb: 0.5 }}>
          <Typography variant="caption" color="text.secondary">Progress</Typography>
          <Typography variant="caption" color="text.secondary">{pct}%</Typography>
        </Box>
        <LinearProgress variant="determinate" value={pct} sx={{ height: 4, borderRadius: 2, bgcolor: 'rgba(255,255,255,0.1)', '& .MuiLinearProgress-bar': { bgcolor: meta.color } }} />
      </Box>

      {assessment.assessor && (
        <Typography variant="caption" color="text.secondary" sx={{ mt: 1, display: 'block' }}>
          Assessor: {assessment.assessor}
        </Typography>
      )}
    </Paper>
  )
}

// ── Detail view — requirement group section ────────────────────────────────────

interface GroupedReq {
  groupId: string
  groupTitle: string
  requirements: FullAssessment['requirements']
}

function groupRequirements(requirements: FullAssessment['requirements'], frameworkCode: string): GroupedReq[] {
  if (frameworkCode === 'DORA') {
    // Group by group_id (chapter code)
    const map = new Map<string, GroupedReq>()
    for (const r of requirements) {
      const gid = r.group_id ?? 'Other'
      const gtitle = r.group_title ?? 'Other'
      if (!map.has(gid)) map.set(gid, { groupId: gid, groupTitle: gtitle, requirements: [] })
      map.get(gid)!.requirements.push(r)
    }
    return Array.from(map.values())
  }
  // NIS2 — split by article prefix
  const measures: FullAssessment['requirements'] = []
  const reporting: FullAssessment['requirements'] = []
  for (const r of requirements) {
    if (r.control_id.startsWith('Art. 23')) reporting.push(r)
    else measures.push(r)
  }
  return [
    { groupId: 'Art21', groupTitle: 'Security Measures — Article 21(2)', requirements: measures },
    { groupId: 'Art23', groupTitle: 'Reporting Obligations — Article 23', requirements: reporting },
  ].filter(g => g.requirements.length > 0)
}

function RequirementSection({
  group, ratings, ratingMap, frameworkCode, onSave,
}: {
  group: GroupedReq
  ratings: FullAssessment['ratings']
  ratingMap: Map<string, FullAssessment['ratings'][number]>
  frameworkCode: string
  onSave: (upserts: RatingUpsert[]) => void
}) {
  const [expanded, setExpanded] = useState(true)
  const meta = FRAMEWORK_META[frameworkCode] ?? { color: '#1976d2' }

  const groupRatings = group.requirements.map(r => ratingMap.get(r.id))
  const rated = groupRatings.filter(r => r?.current_score !== null && r?.current_score !== undefined)
  const avgScore = rated.length > 0
    ? rated.reduce((s, r) => s + (r!.current_score ?? 0), 0) / rated.length
    : null

  return (
    <Box sx={{ mb: 3 }}>
      <Box
        sx={{ display: 'flex', alignItems: 'center', gap: 1.5, mb: 1.5, cursor: 'pointer', userSelect: 'none' }}
        onClick={() => setExpanded(v => !v)}
      >
        <IconButton size="small" sx={{ p: 0.25 }}>
          {expanded ? <ExpandLessOutlined sx={{ fontSize: 18 }} /> : <ExpandMoreOutlined sx={{ fontSize: 18 }} />}
        </IconButton>
        <Box sx={{ height: 3, width: 4, bgcolor: meta.color, borderRadius: 1 }} />
        <Typography variant="subtitle2" fontWeight={700} sx={{ color: meta.color }}>
          {group.groupTitle}
        </Typography>
        <Chip label={`${group.requirements.length} items`} size="small" sx={{ height: 18, fontSize: '0.6rem' }} />
        {avgScore !== null && (
          <Chip
            label={`Avg: ${avgScore.toFixed(1)} — ${SCORE_LABELS[Math.round(avgScore)]}`}
            size="small"
            sx={{ height: 18, fontSize: '0.6rem', bgcolor: SCORE_COLORS[Math.round(avgScore)] + '22', color: SCORE_COLORS[Math.round(avgScore)] }}
          />
        )}
      </Box>

      <Collapse in={expanded}>
        <TableContainer component={Paper} elevation={0} sx={{ border: '1px solid', borderColor: 'divider', borderRadius: 1.5 }}>
          <Table size="small">
            <TableHead>
              <TableRow sx={{ bgcolor: 'rgba(255,255,255,0.02)' }}>
                <TableCell sx={{ fontWeight: 600, width: 120 }}>Code</TableCell>
                <TableCell sx={{ fontWeight: 600 }}>Requirement</TableCell>
                <TableCell sx={{ fontWeight: 600, width: 170 }}>Current Score</TableCell>
                <TableCell sx={{ fontWeight: 600, width: 170 }}>Target Score</TableCell>
                <TableCell sx={{ fontWeight: 600, width: 160 }}>Status</TableCell>
                <TableCell sx={{ fontWeight: 600, width: 220 }}>Notes</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {group.requirements.map(req => (
                <RequirementRow
                  key={req.id}
                  req={req}
                  existing={ratingMap.get(req.id)}
                  onSave={upsert => onSave([upsert])}
                />
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </Collapse>
    </Box>
  )
}

function RequirementRow({
  req, existing, onSave,
}: {
  req: FullAssessment['requirements'][number]
  existing: FullAssessment['ratings'][number] | undefined
  onSave: (upsert: RatingUpsert) => void
}) {
  const [currentScore, setCurrentScore] = useState<number | ''>(existing?.current_score ?? '')
  const [targetScore, setTargetScore] = useState<number | ''>(existing?.target_score ?? '')
  const [ratingStatus, setRatingStatus] = useState(existing?.rating_status ?? 'not_assessed')
  const [notesValue, setNotesValue] = useState(existing?.notes ?? '')
  const [expanded, setExpanded] = useState(false)
  const saveTimer = useRef<ReturnType<typeof setTimeout> | null>(null)

  function scheduleSave(overrides?: Partial<{ current_score: number | null; target_score: number | null; rating_status: string; notes: string | null }>) {
    if (saveTimer.current) clearTimeout(saveTimer.current)
    saveTimer.current = setTimeout(() => {
      onSave({
        requirement_id: req.id,
        current_score: (overrides?.current_score !== undefined ? overrides.current_score : (currentScore !== '' ? currentScore : null)),
        target_score: (overrides?.target_score !== undefined ? overrides.target_score : (targetScore !== '' ? targetScore : null)),
        rating_status: overrides?.rating_status ?? ratingStatus,
        notes: overrides?.notes !== undefined ? overrides.notes : (notesValue || null),
      })
    }, 800)
  }

  function handleCurrentScore(v: number | '') {
    setCurrentScore(v)
    scheduleSave({ current_score: v !== '' ? v : null })
  }

  function handleTargetScore(v: number | '') {
    setTargetScore(v)
    scheduleSave({ target_score: v !== '' ? v : null })
  }

  function handleStatus(v: string) {
    setRatingStatus(v)
    scheduleSave({ rating_status: v })
  }

  function handleNotesBlur(v: string) {
    setNotesValue(v)
    scheduleSave({ notes: v || null })
  }

  return (
    <>
      <TableRow
        sx={{ '&:last-child td': { border: 0 }, '&:hover': { bgcolor: 'rgba(255,255,255,0.02)' } }}
      >
        <TableCell>
          <Tooltip title={req.description ?? ''} placement="right" arrow>
            <Typography variant="caption" fontFamily="monospace" sx={{ color: 'primary.light', cursor: 'help' }}>
              {req.control_id}
            </Typography>
          </Tooltip>
        </TableCell>
        <TableCell>
          <Box sx={{ display: 'flex', alignItems: 'flex-start', gap: 0.5 }}>
            <Typography variant="body2" sx={{ lineHeight: 1.4 }}>{req.title}</Typography>
            {req.description && (
              <IconButton size="small" sx={{ p: 0, mt: -0.25, color: 'text.disabled' }} onClick={() => setExpanded(v => !v)}>
                {expanded ? <ExpandLessOutlined sx={{ fontSize: 14 }} /> : <ExpandMoreOutlined sx={{ fontSize: 14 }} />}
              </IconButton>
            )}
          </Box>
          {expanded && req.description && (
            <Typography variant="caption" color="text.secondary" sx={{ display: 'block', mt: 0.5, lineHeight: 1.5 }}>
              {req.description}
            </Typography>
          )}
        </TableCell>
        <TableCell>
          <Select
            size="small"
            value={currentScore}
            onChange={e => handleCurrentScore(e.target.value as number | '')}
            displayEmpty
            sx={{ fontSize: '0.75rem', minWidth: 150 }}
          >
            <MenuItem value=""><em style={{ color: '#888' }}>Not set</em></MenuItem>
            {[0, 1, 2, 3, 4].map(s => (
              <MenuItem key={s} value={s}>
                <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                  <Box sx={{ width: 8, height: 8, borderRadius: '50%', bgcolor: SCORE_COLORS[s], flexShrink: 0 }} />
                  {s} — {SCORE_LABELS[s]}
                </Box>
              </MenuItem>
            ))}
          </Select>
        </TableCell>
        <TableCell>
          <Select
            size="small"
            value={targetScore}
            onChange={e => handleTargetScore(e.target.value as number | '')}
            displayEmpty
            sx={{ fontSize: '0.75rem', minWidth: 150 }}
          >
            <MenuItem value=""><em style={{ color: '#888' }}>Not set</em></MenuItem>
            {[0, 1, 2, 3, 4].map(s => (
              <MenuItem key={s} value={s}>
                <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                  <Box sx={{ width: 8, height: 8, borderRadius: '50%', bgcolor: SCORE_COLORS[s], flexShrink: 0 }} />
                  {s} — {SCORE_LABELS[s]}
                </Box>
              </MenuItem>
            ))}
          </Select>
        </TableCell>
        <TableCell>
          <Select
            size="small"
            value={ratingStatus}
            onChange={e => handleStatus(e.target.value)}
            sx={{ fontSize: '0.75rem', minWidth: 140 }}
          >
            {Object.entries(STATUS_CONFIG).map(([val, cfg]) => (
              <MenuItem key={val} value={val}>
                <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.75 }}>
                  <Box sx={{ color: cfg.color, display: 'flex', alignItems: 'center' }}>{cfg.icon}</Box>
                  {cfg.label}
                </Box>
              </MenuItem>
            ))}
          </Select>
        </TableCell>
        <TableCell>
          <TextField
            size="small"
            multiline
            maxRows={3}
            defaultValue={notesValue}
            onBlur={e => handleNotesBlur(e.target.value)}
            placeholder="Notes…"
            sx={{ fontSize: '0.75rem', width: '100%' }}
            inputProps={{ style: { fontSize: '0.75rem' } }}
          />
        </TableCell>
      </TableRow>
    </>
  )
}

// ── Detail view ────────────────────────────────────────────────────────────────

function AssessmentDetail({
  assessmentId, frameworkCode, onBack,
}: {
  assessmentId: string
  frameworkCode: string
  onBack: () => void
}) {
  const queryClient = useQueryClient()
  const meta = FRAMEWORK_META[frameworkCode] ?? { name: frameworkCode, color: '#1976d2', subtitle: '', description: '' }

  const { data, isLoading, error } = useQuery({
    queryKey: ['regulatory', frameworkCode, 'assessment', assessmentId],
    queryFn: () => regulatoryApi.getFullAssessment(frameworkCode, assessmentId),
  })

  const upsertMutation = useMutation({
    mutationFn: (ratings: RatingUpsert[]) => regulatoryApi.upsertRatings(frameworkCode, assessmentId, ratings),
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ['regulatory', frameworkCode, 'assessments'] }),
  })

  const [editingMeta, setEditingMeta] = useState(false)
  const [metaName, setMetaName] = useState('')
  const [metaAssessor, setMetaAssessor] = useState('')
  const [metaOrg, setMetaOrg] = useState('')
  const [metaScope, setMetaScope] = useState('')

  const updateMutation = useMutation({
    mutationFn: (upd: object) => regulatoryApi.updateAssessment(frameworkCode, assessmentId, upd),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['regulatory', frameworkCode, 'assessment', assessmentId] })
      queryClient.invalidateQueries({ queryKey: ['regulatory', frameworkCode, 'assessments'] })
      setEditingMeta(false)
    },
  })

  function startEdit() {
    if (!data) return
    setMetaName(data.assessment.name)
    setMetaAssessor(data.assessment.assessor ?? '')
    setMetaOrg(data.assessment.organisation ?? '')
    setMetaScope(data.assessment.scope ?? '')
    setEditingMeta(true)
  }

  function saveMeta() {
    updateMutation.mutate({ name: metaName, assessor: metaAssessor || null, organisation: metaOrg || null, scope: metaScope || null })
  }

  if (isLoading) return <LinearProgress sx={{ mt: 2 }} />
  if (error || !data) return <Alert severity="error">Failed to load assessment.</Alert>

  const { assessment, requirements, ratings } = data

  const ratingMap = new Map(ratings.map(r => [r.requirement_id, r]))
  const groups = groupRequirements(requirements, frameworkCode)

  const ratedCount = ratings.filter(r => r.current_score !== null).length
  const scoredRatings = ratings.filter(r => r.current_score !== null)
  const avgCurrent = scoredRatings.length > 0
    ? scoredRatings.reduce((s, r) => s + (r.current_score ?? 0), 0) / scoredRatings.length
    : null
  const compliantCount = ratings.filter(r => r.rating_status === 'compliant').length
  const partialCount = ratings.filter(r => r.rating_status === 'partial').length
  const nonCompliantCount = ratings.filter(r => r.rating_status === 'non_compliant').length
  const progressPct = requirements.length > 0 ? Math.round((ratedCount / requirements.length) * 100) : 0

  return (
    <Box>
      {/* Header */}
      <Box sx={{ display: 'flex', alignItems: 'flex-start', gap: 2, mb: 3 }}>
        <IconButton onClick={onBack} size="small" sx={{ mt: 0.5 }}>
          <ArrowBackOutlined />
        </IconButton>
        <Box sx={{ flex: 1 }}>
          {editingMeta ? (
            <Box sx={{ display: 'flex', flexDirection: 'column', gap: 1.5 }}>
              <TextField size="small" label="Name" value={metaName} onChange={e => setMetaName(e.target.value)} sx={{ maxWidth: 400 }} />
              <Box sx={{ display: 'flex', gap: 1.5, flexWrap: 'wrap' }}>
                <TextField size="small" label="Organisation" value={metaOrg} onChange={e => setMetaOrg(e.target.value)} sx={{ width: 220 }} />
                <TextField size="small" label="Assessor" value={metaAssessor} onChange={e => setMetaAssessor(e.target.value)} sx={{ width: 180 }} />
                <TextField size="small" label="Scope" value={metaScope} onChange={e => setMetaScope(e.target.value)} sx={{ width: 280 }} />
              </Box>
              <Box sx={{ display: 'flex', gap: 1 }}>
                <Button variant="contained" size="small" onClick={saveMeta} disabled={!metaName || updateMutation.isPending}>Save</Button>
                <Button size="small" onClick={() => setEditingMeta(false)}>Cancel</Button>
              </Box>
            </Box>
          ) : (
            <Box sx={{ display: 'flex', alignItems: 'flex-start', gap: 1 }}>
              <Box>
                <Typography variant="h5" fontWeight={700}>{assessment.name}</Typography>
                {(assessment.organisation || assessment.assessor) && (
                  <Typography variant="caption" color="text.secondary">
                    {[assessment.organisation, assessment.assessor ? `Assessor: ${assessment.assessor}` : null].filter(Boolean).join(' · ')}
                  </Typography>
                )}
              </Box>
              <IconButton size="small" sx={{ mt: 0.25, color: 'text.disabled' }} onClick={startEdit}>
                <EditOutlined sx={{ fontSize: 16 }} />
              </IconButton>
            </Box>
          )}
        </Box>
        <Box sx={{ display: 'flex', gap: 1, flexWrap: 'wrap' }}>
          <Select
            size="small"
            value={assessment.status}
            onChange={e => updateMutation.mutate({ status: e.target.value })}
            sx={{ fontSize: '0.75rem', minWidth: 120 }}
          >
            {[['draft', 'Draft'], ['in_progress', 'In Progress'], ['complete', 'Complete']].map(([v, l]) => (
              <MenuItem key={v} value={v}><Typography variant="caption">{l}</Typography></MenuItem>
            ))}
          </Select>
        </Box>
      </Box>

      {/* KPI strip */}
      <Box sx={{ display: 'grid', gridTemplateColumns: 'repeat(5, 1fr)', gap: 1.5, mb: 3 }}>
        {[
          { label: 'Assessed', value: `${ratedCount} / ${requirements.length}`, sub: `${progressPct}%`, color: meta.color },
          { label: 'Avg Score', value: avgCurrent !== null ? avgCurrent.toFixed(1) : '—', sub: avgCurrent !== null ? SCORE_LABELS[Math.round(avgCurrent)] : '', color: avgCurrent !== null ? SCORE_COLORS[Math.round(avgCurrent)] : '#9e9e9e' },
          { label: 'Compliant', value: compliantCount, sub: `${requirements.length > 0 ? Math.round((compliantCount / requirements.length) * 100) : 0}%`, color: '#4CAF50' },
          { label: 'Partial', value: partialCount, sub: '', color: '#FF9800' },
          { label: 'Non-Compliant', value: nonCompliantCount, sub: '', color: '#f44336' },
        ].map(kpi => (
          <Paper key={kpi.label} elevation={0} sx={{ p: 1.5, border: '1px solid', borderColor: 'divider', borderRadius: 1.5, borderTop: `3px solid ${kpi.color}` }}>
            <Typography variant="caption" color="text.secondary">{kpi.label}</Typography>
            <Typography variant="h6" fontWeight={700} sx={{ color: kpi.color, lineHeight: 1.2 }}>{kpi.value}</Typography>
            {kpi.sub && <Typography variant="caption" color="text.secondary">{kpi.sub}</Typography>}
          </Paper>
        ))}
      </Box>

      <LinearProgress
        variant="determinate"
        value={progressPct}
        sx={{ height: 5, borderRadius: 3, mb: 3, bgcolor: 'rgba(255,255,255,0.08)', '& .MuiLinearProgress-bar': { bgcolor: meta.color } }}
      />

      {/* Requirement groups */}
      {groups.map(group => (
        <RequirementSection
          key={group.groupId}
          group={group}
          ratings={ratings}
          ratingMap={ratingMap}
          frameworkCode={frameworkCode}
          onSave={upserts => upsertMutation.mutate(upserts)}
        />
      ))}
    </Box>
  )
}

// ── Main page ──────────────────────────────────────────────────────────────────

export default function ComplianceAssessment({ frameworkCode }: { frameworkCode: string }) {
  const queryClient = useQueryClient()
  const meta = FRAMEWORK_META[frameworkCode] ?? { name: frameworkCode, subtitle: '', color: '#1976d2', description: '' }
  const [createOpen, setCreateOpen] = useState(false)
  const [selectedId, setSelectedId] = useState<string | null>(null)
  const [deleteId, setDeleteId] = useState<string | null>(null)

  const { data: assessments = [], isLoading } = useQuery({
    queryKey: ['regulatory', frameworkCode, 'assessments'],
    queryFn: () => regulatoryApi.listAssessments(frameworkCode),
  })

  const deleteMutation = useMutation({
    mutationFn: (id: string) => regulatoryApi.deleteAssessment(frameworkCode, id),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['regulatory', frameworkCode, 'assessments'] })
      if (deleteId === selectedId) setSelectedId(null)
      setDeleteId(null)
    },
  })

  if (selectedId) {
    return (
      <AssessmentDetail
        assessmentId={selectedId}
        frameworkCode={frameworkCode}
        onBack={() => setSelectedId(null)}
      />
    )
  }

  return (
    <Box>
      {/* Page header */}
      <Box sx={{ display: 'flex', alignItems: 'flex-start', justifyContent: 'space-between', mb: 3 }}>
        <Box>
          <Box sx={{ display: 'flex', alignItems: 'center', gap: 1.5, mb: 0.5 }}>
            <Typography variant="h4" fontWeight={700}>{meta.name}</Typography>
            <Chip label={meta.subtitle} size="small" sx={{ bgcolor: meta.color + '22', color: meta.color, fontWeight: 600, fontSize: '0.7rem' }} />
          </Box>
          <Typography variant="body2" color="text.secondary" sx={{ maxWidth: 600 }}>{meta.description}</Typography>
        </Box>
        <Button
          variant="contained"
          startIcon={<AddOutlined />}
          onClick={() => setCreateOpen(true)}
          sx={{ bgcolor: meta.color, '&:hover': { bgcolor: meta.color + 'cc' }, flexShrink: 0 }}
        >
          New Assessment
        </Button>
      </Box>

      {/* Divider */}
      <Divider sx={{ mb: 3 }} />

      {/* Content */}
      {isLoading ? (
        <LinearProgress />
      ) : assessments.length === 0 ? (
        <Box sx={{ textAlign: 'center', py: 8 }}>
          <Typography variant="h6" color="text.secondary" gutterBottom>No assessments yet</Typography>
          <Typography variant="body2" color="text.disabled" sx={{ mb: 3 }}>
            Create your first {meta.name} assessment to get started.
          </Typography>
          <Button variant="outlined" startIcon={<AddOutlined />} onClick={() => setCreateOpen(true)}>
            New Assessment
          </Button>
        </Box>
      ) : (
        <Box sx={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(360px, 1fr))', gap: 2 }}>
          {assessments.map(a => (
            <AssessmentCard
              key={a.id}
              assessment={a}
              frameworkCode={frameworkCode}
              onSelect={setSelectedId}
              onDelete={setDeleteId}
            />
          ))}
        </Box>
      )}

      <CreateDialog
        open={createOpen}
        frameworkCode={frameworkCode}
        onClose={() => setCreateOpen(false)}
      />

      {/* Delete confirm */}
      <Dialog open={!!deleteId} onClose={() => setDeleteId(null)} maxWidth="xs" fullWidth>
        <DialogTitle>Delete Assessment</DialogTitle>
        <DialogContent>
          <Typography>This will permanently delete the assessment and all ratings. This cannot be undone.</Typography>
        </DialogContent>
        <DialogActions sx={{ px: 3, pb: 2 }}>
          <Button onClick={() => setDeleteId(null)}>Cancel</Button>
          <Button color="error" variant="contained" disabled={deleteMutation.isPending} onClick={() => deleteId && deleteMutation.mutate(deleteId)}>
            Delete
          </Button>
        </DialogActions>
      </Dialog>
    </Box>
  )
}
