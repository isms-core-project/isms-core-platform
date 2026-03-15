import { useState, useCallback, useRef } from 'react'
import { useNavigate } from 'react-router-dom'
import {
  Box, Card, CardContent, Typography, Chip, Skeleton, Alert, Snackbar,
  Button, IconButton, Tooltip, Collapse, LinearProgress,
  Dialog, DialogTitle, DialogContent, DialogActions,
  TextField, Select, MenuItem,
  Table, TableBody, TableCell, TableContainer, TableHead, TableRow,
  CircularProgress,
} from '@mui/material'
import {
  AddOutlined, DeleteOutlined, DownloadOutlined,
  ExpandMoreOutlined, ExpandLessOutlined, ArrowBackOutlined,
  GridViewOutlined, CheckCircleOutlineOutlined, RadioButtonUncheckedOutlined,
  EditOutlined, SaveOutlined, UploadFileOutlined, SummarizeOutlined,
} from '@mui/icons-material'
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { nistApi, NistImportResult, NistProfileSummary, NistFullProfile, NistRating } from '../api/nistApi'
import PageHeader from '../components/PageHeader'

// ── Constants ──────────────────────────────────────────────────────────────

const FUNCTION_COLORS: Record<string, string> = {
  GV: '#4472C4', ID: '#ED7D31', PR: '#70AD47',
  DE: '#FFC000', RS: '#FF5252', RC: '#9966CC',
}

const FUNCTION_NAMES: Record<string, string> = {
  GV: 'Govern', ID: 'Identify', PR: 'Protect',
  DE: 'Detect', RS: 'Respond', RC: 'Recover',
}

const TIER_LABELS: Record<number, string> = {
  1: 'Partial', 2: 'Risk Informed', 3: 'Repeatable', 4: 'Adaptive',
}

const FUNCTION_ORDER = ['GV', 'ID', 'PR', 'DE', 'RS', 'RC']

// ── Helpers ────────────────────────────────────────────────────────────────

function tierColor(tier: number | null): string {
  if (!tier) return 'rgba(255,255,255,0.1)'
  if (tier === 1) return '#FF5252'
  if (tier === 2) return '#FFC000'
  if (tier === 3) return '#70AD47'
  return '#4472C4'
}

function gapColor(gap: number): string {
  if (gap <= 0) return '#C6EFCE'
  if (gap === 1) return '#FFC000'
  return '#FF5252'
}

function FunctionScoreBar({ code, avg, total, rated }: { code: string; avg: number | null; total: number; rated: number }) {
  const color = FUNCTION_COLORS[code] ?? '#888'
  const pct = total > 0 ? (rated / total) * 100 : 0
  return (
    <Box>
      <Box sx={{ display: 'flex', justifyContent: 'space-between', mb: 0.3 }}>
        <Typography variant="caption" sx={{ fontSize: '0.65rem', color, fontWeight: 600 }}>{code}</Typography>
        <Typography variant="caption" sx={{ fontSize: '0.6rem', color: 'text.disabled' }}>
          {avg != null ? `T${avg.toFixed(1)}` : '\u2014'} {rated}/{total}
        </Typography>
      </Box>
      <LinearProgress variant="determinate" value={Math.min(100, pct)}
        sx={{ height: 3, borderRadius: 2, bgcolor: 'rgba(255,255,255,0.06)', '& .MuiLinearProgress-bar': { bgcolor: color } }} />
    </Box>
  )
}

// ── Profile card ───────────────────────────────────────────────────────────

function ProfileCard({ profile, onOpen, onDelete }: { profile: NistProfileSummary; onOpen: () => void; onDelete: () => void }) {
  const pct = profile.total_subcategories > 0 ? (profile.rated_count / profile.total_subcategories) * 100 : 0
  const statusColor = profile.status === 'complete' ? '#C6EFCE' : profile.status === 'in_progress' ? '#FFC000' : '#888'
  const statusBg = profile.status === 'complete' ? 'rgba(198,239,206,0.12)' : profile.status === 'in_progress' ? 'rgba(255,192,0,0.1)' : 'rgba(255,255,255,0.05)'
  const statusLabel = profile.status === 'complete' ? 'Complete' : profile.status === 'in_progress' ? 'In Progress' : 'Draft'

  return (
    <Card sx={{ mb: 1.5, bgcolor: 'rgba(68,114,196,0.04)', border: '1px solid rgba(68,114,196,0.12)', cursor: 'pointer', '&:hover': { borderColor: 'rgba(68,114,196,0.3)' } }} onClick={onOpen}>
      <CardContent sx={{ p: '14px 16px !important' }}>
        <Box sx={{ display: 'flex', gap: 2 }}>
          <Box sx={{ position: 'relative', width: 52, height: 52, flexShrink: 0, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
            <CircularProgress variant="determinate" value={100} size={52} thickness={3} sx={{ position: 'absolute', color: 'rgba(255,255,255,0.06)' }} />
            <CircularProgress variant="determinate" value={Math.min(100, pct)} size={52} thickness={3} sx={{ position: 'absolute', color: '#4472C4' }} />
            <Box sx={{ textAlign: 'center' }}>
              <Typography sx={{ fontSize: '0.7rem', fontWeight: 700, lineHeight: 1, color: 'primary.light' }}>{profile.rated_count}</Typography>
              <Typography sx={{ fontSize: '0.52rem', color: 'text.disabled', lineHeight: 1 }}>/{profile.total_subcategories}</Typography>
            </Box>
          </Box>

          <Box sx={{ flex: 1, minWidth: 0 }}>
            <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 0.5, flexWrap: 'wrap' }}>
              <Typography variant="body2" fontWeight={700} noWrap sx={{ flex: 1, minWidth: 0 }}>{profile.name}</Typography>
              <Chip label={statusLabel} size="small" sx={{ fontSize: '0.6rem', height: 16, bgcolor: statusBg, color: statusColor, fontWeight: 600 }} />
            </Box>
            {profile.description && (
              <Typography variant="caption" color="text.secondary" sx={{ display: 'block', mb: 0.75 }} noWrap>{profile.description}</Typography>
            )}
            <Box sx={{ display: 'flex', gap: 2, flexWrap: 'wrap' }}>
              {profile.assessor && (
                <Typography variant="caption" color="text.disabled" sx={{ fontSize: '0.65rem' }}>
                  Assessor: <span style={{ color: '#ccc' }}>{profile.assessor}</span>
                </Typography>
              )}
              {profile.avg_current_tier != null && (
                <Typography variant="caption" color="text.disabled" sx={{ fontSize: '0.65rem' }}>
                  Avg: <span style={{ color: tierColor(Math.round(profile.avg_current_tier)) }}>T{profile.avg_current_tier.toFixed(1)}</span>
                </Typography>
              )}
            </Box>
            {profile.function_scores && profile.function_scores.length > 0 && (
              <Box sx={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '4px 12px', mt: 1 }}>
                {FUNCTION_ORDER.map(fc => {
                  const fs = profile.function_scores.find(f => f.function_code === fc)
                  if (!fs) return null
                  return <FunctionScoreBar key={fc} code={fc} avg={fs.avg_current} total={fs.total_count} rated={fs.rated_count} />
                })}
              </Box>
            )}
          </Box>

          <Box sx={{ flexShrink: 0 }} onClick={e => e.stopPropagation()}>
            <Tooltip title="Delete profile">
              <IconButton size="small" onClick={onDelete} sx={{ color: 'error.main', opacity: 0.4, '&:hover': { opacity: 1 } }}>
                <DeleteOutlined sx={{ fontSize: 16 }} />
              </IconButton>
            </Tooltip>
          </Box>
        </Box>
      </CardContent>
    </Card>
  )
}

// ── Detail: tier select ────────────────────────────────────────────────────

function TierSelect({ value, onChange, disabled }: { value: number | null; onChange: (v: number | null) => void; disabled?: boolean }) {
  return (
    <Select
      value={value ?? 0}
      onChange={e => {
        const v = Number(e.target.value)
        onChange(v === 0 ? null : v)
      }}
      size="small"
      disabled={disabled}
      sx={{ fontSize: '0.72rem', height: 26, minWidth: 130, '& .MuiOutlinedInput-notchedOutline': { borderColor: 'rgba(255,255,255,0.1)' } }}
    >
      <MenuItem value={0}><em style={{ color: '#666', fontSize: '0.72rem' }}>Not Rated</em></MenuItem>
      {[1, 2, 3, 4].map(t => (
        <MenuItem key={t} value={t} sx={{ fontSize: '0.72rem' }}>
          <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.75 }}>
            <Box sx={{ width: 6, height: 6, borderRadius: '50%', bgcolor: tierColor(t) }} />
            T{t} {'—'} {TIER_LABELS[t]}
          </Box>
        </MenuItem>
      ))}
    </Select>
  )
}

// ── Detail: function section ───────────────────────────────────────────────

type RatingOverrides = Record<string, { current_tier?: number | null; target_tier?: number | null; notes?: string | null }>

function FunctionSection({ functionCode, ratings, overrides, onOverride, saving }: {
  functionCode: string
  ratings: NistRating[]
  overrides: RatingOverrides
  onOverride: (subcategoryId: string, field: 'current_tier' | 'target_tier' | 'notes', value: number | null | string) => void
  saving: boolean
}) {
  const [open, setOpen] = useState(true)
  const color = FUNCTION_COLORS[functionCode] ?? '#888'

  const ratedCount = ratings.filter(r => {
    const ov = overrides[r.subcategory_id]
    const cur = ov && 'current_tier' in ov ? ov.current_tier : r.current_tier
    return cur != null
  }).length

  return (
    <Card sx={{ mb: 1.5, border: `1px solid ${color}22`, bgcolor: `${color}05` }}>
      <Box onClick={() => setOpen(v => !v)} sx={{ display: 'flex', alignItems: 'center', gap: 1.5, px: 2, py: 1.25, cursor: 'pointer', borderBottom: open ? `1px solid ${color}22` : 'none', '&:hover': { bgcolor: `${color}08` } }}>
        <Box sx={{ width: 28, height: 28, borderRadius: 1, bgcolor: `${color}22`, display: 'flex', alignItems: 'center', justifyContent: 'center', flexShrink: 0 }}>
          <Typography sx={{ fontSize: '0.7rem', fontWeight: 800, color, lineHeight: 1 }}>{functionCode}</Typography>
        </Box>
        <Box sx={{ flex: 1 }}>
          <Typography variant="body2" fontWeight={700} sx={{ color }}>{FUNCTION_NAMES[functionCode]}</Typography>
          <Typography variant="caption" color="text.disabled" sx={{ fontSize: '0.62rem' }}>{ratedCount} of {ratings.length} rated</Typography>
        </Box>
        <LinearProgress variant="determinate" value={ratings.length > 0 ? (ratedCount / ratings.length) * 100 : 0}
          sx={{ width: 80, height: 4, borderRadius: 2, bgcolor: 'rgba(255,255,255,0.06)', '& .MuiLinearProgress-bar': { bgcolor: color } }} />
        <Box sx={{ color: 'text.disabled', ml: 0.5 }}>
          {open ? <ExpandLessOutlined sx={{ fontSize: 16 }} /> : <ExpandMoreOutlined sx={{ fontSize: 16 }} />}
        </Box>
      </Box>

      <Collapse in={open} timeout={180} unmountOnExit>
        <TableContainer>
          <Table size="small">
            <TableHead>
              <TableRow sx={{ '& th': { fontSize: '0.65rem', color: 'text.disabled', fontWeight: 600, py: 0.75, borderColor: 'rgba(255,255,255,0.06)' } }}>
                <TableCell sx={{ width: 100 }}>ID</TableCell>
                <TableCell>Title</TableCell>
                <TableCell sx={{ width: 145 }}>Current Tier</TableCell>
                <TableCell sx={{ width: 145 }}>Target Tier</TableCell>
                <TableCell sx={{ width: 48, textAlign: 'center' }}>Gap</TableCell>
                <TableCell sx={{ width: 160 }}>Notes</TableCell>
                <TableCell sx={{ width: 80 }}>ISO 27001</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {ratings.map(r => {
                const ov = overrides[r.subcategory_id] ?? {}
                const currentTier = 'current_tier' in ov ? ov.current_tier! : r.current_tier
                const targetTier = 'target_tier' in ov ? ov.target_tier! : r.target_tier
                const gap = currentTier != null && targetTier != null ? targetTier - currentTier : null
                return (
                  <TableRow key={r.subcategory_id} sx={{ '& td': { borderColor: 'rgba(255,255,255,0.04)', py: 0.6 }, '&:hover': { bgcolor: 'rgba(255,255,255,0.02)' } }}>
                    <TableCell>
                      <Typography variant="caption" sx={{ fontFamily: 'monospace', color, fontSize: '0.68rem', fontWeight: 600 }}>{r.subcategory_code}</Typography>
                    </TableCell>
                    <TableCell>
                      <Typography variant="caption" sx={{ fontSize: '0.72rem', lineHeight: 1.35, display: 'block' }}>{r.subcategory_title}</Typography>
                    </TableCell>
                    <TableCell>
                      <TierSelect value={currentTier} onChange={v => onOverride(r.subcategory_id, 'current_tier', v)} disabled={saving} />
                    </TableCell>
                    <TableCell>
                      <TierSelect value={targetTier} onChange={v => onOverride(r.subcategory_id, 'target_tier', v)} disabled={saving} />
                    </TableCell>
                    <TableCell align="center">
                      {gap != null ? (
                        <Chip label={gap > 0 ? `+${gap}` : gap === 0 ? '\u2713' : `${gap}`} size="small"
                          sx={{ fontSize: '0.6rem', height: 16, fontWeight: 700, bgcolor: `${gapColor(gap)}22`, color: gapColor(gap) }} />
                      ) : (
                        <Typography variant="caption" color="text.disabled">{'—'}</Typography>
                      )}
                    </TableCell>
                    <TableCell>
                      <TextField
                        size="small"
                        variant="standard"
                        placeholder="Notes…"
                        defaultValue={r.notes ?? ''}
                        onBlur={e => {
                          const v = e.target.value.trim() || null
                          if (v !== (r.notes ?? null)) onOverride(r.subcategory_id, 'notes', v)
                        }}
                        inputProps={{ style: { fontSize: '0.68rem', padding: '2px 0' } }}
                        sx={{ width: '100%', '& .MuiInput-underline:before': { borderColor: 'rgba(255,255,255,0.1)' } }}
                      />
                    </TableCell>
                    <TableCell>
                      <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 0.25 }}>
                        {r.iso_mappings.slice(0, 3).map(iso => (
                          <Chip key={iso} label={iso} size="small" sx={{ fontSize: '0.55rem', height: 14, bgcolor: 'rgba(68,114,196,0.15)', color: '#9DC3E6' }} />
                        ))}
                        {r.iso_mappings.length > 3 && (
                          <Chip label={`+${r.iso_mappings.length - 3}`} size="small" sx={{ fontSize: '0.55rem', height: 14, bgcolor: 'rgba(255,255,255,0.06)', color: 'text.disabled' }} />
                        )}
                      </Box>
                    </TableCell>
                  </TableRow>
                )
              })}
            </TableBody>
          </Table>
        </TableContainer>
      </Collapse>
    </Card>
  )
}

// ── Profile detail ─────────────────────────────────────────────────────────

function ProfileDetail({ profileId, onBack, onDelete }: { profileId: string; onBack: () => void; onDelete: () => void }) {
  const queryClient = useQueryClient()
  const navigate = useNavigate()
  const [overrides, setOverrides] = useState<RatingOverrides>({})
  const [editName, setEditName] = useState(false)
  const [nameVal, setNameVal] = useState('')
  const [importResult, setImportResult] = useState<NistImportResult | null>(null)
  const [importError, setImportError] = useState<string | null>(null)
  const [importLoading, setImportLoading] = useState(false)
  const importInputRef = useRef<HTMLInputElement | null>(null)
  const saveTimer = useRef<ReturnType<typeof setTimeout> | null>(null)

  const { data, isLoading, isError } = useQuery<NistFullProfile>({
    queryKey: ['nist-full-profile', profileId],
    queryFn: () => nistApi.getFullProfile(profileId),
  })
  const dataRef = useRef<NistFullProfile | undefined>(undefined)
  dataRef.current = data

  const upsertMutation = useMutation({
    mutationFn: (ratings: Parameters<typeof nistApi.upsertRatings>[1]) =>
      nistApi.upsertRatings(profileId, ratings),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['nist-full-profile', profileId] })
      queryClient.invalidateQueries({ queryKey: ['nist-profiles'] })
    },
  })

  const updateProfileMutation = useMutation({
    mutationFn: (patch: Parameters<typeof nistApi.updateProfile>[1]) =>
      nistApi.updateProfile(profileId, patch),
    onSuccess: () => {
      setEditName(false)
      queryClient.invalidateQueries({ queryKey: ['nist-full-profile', profileId] })
      queryClient.invalidateQueries({ queryKey: ['nist-profiles'] })
    },
  })

  const handleOverride = useCallback((subcategoryId: string, field: 'current_tier' | 'target_tier' | 'notes', value: number | null | string) => {
    setOverrides(prev => ({ ...prev, [subcategoryId]: { ...(prev[subcategoryId] ?? {}), [field]: value as never } }))
    if (saveTimer.current) clearTimeout(saveTimer.current)
    saveTimer.current = setTimeout(() => {
      setOverrides(current => {
        const entries = Object.entries(current)
        if (entries.length > 0) {
          const ratings = entries.map(([id, ov]) => {
            const original = dataRef.current?.ratings.find(r => r.subcategory_id === id)
            return {
              subcategory_id: id,
              current_tier: ov.current_tier !== undefined ? ov.current_tier : (original?.current_tier ?? null),
              target_tier: ov.target_tier !== undefined ? ov.target_tier : (original?.target_tier ?? null),
              notes: ov.notes !== undefined ? ov.notes : (original?.notes ?? null),
            }
          })
          upsertMutation.mutate(ratings)
        }
        return {}
      })
    }, 1200)
  }, [upsertMutation])

  function handleExportCsv() {
    nistApi.exportCsv(profileId).then(blob => {
      const url = URL.createObjectURL(blob)
      const a = document.createElement('a')
      a.href = url
      a.download = `NIST-CSF-Assessment-${profileId}.csv`
      a.click()
      URL.revokeObjectURL(url)
    })
  }

  function handleExportXlsx() {
    nistApi.exportXlsx(profileId).then(blob => {
      const url = URL.createObjectURL(blob)
      const a = document.createElement('a')
      a.href = url
      a.download = `NIST-CSF-Assessment-${profileId}.xlsx`
      a.click()
      URL.revokeObjectURL(url)
    })
  }

  async function handleImportFile(e: React.ChangeEvent<HTMLInputElement>) {
    const file = e.target.files?.[0]
    if (!file) return
    e.target.value = ''
    setImportLoading(true)
    try {
      const result = await nistApi.importXlsx(profileId, file)
      setImportResult(result)
      queryClient.invalidateQueries({ queryKey: ['nist-full-profile', profileId] })
      queryClient.invalidateQueries({ queryKey: ['nist-profiles'] })
    } catch {
      setImportError('Import failed — check the file is a NIST CSF 2.0 template (.xlsx).')
    } finally {
      setImportLoading(false)
    }
  }

  if (isLoading) return <Skeleton variant="rectangular" height={200} sx={{ borderRadius: 2 }} />
  if (isError || !data) return <Alert severity="error">Failed to load profile.</Alert>

  const byFunction: Record<string, NistRating[]> = {}
  for (const r of data.ratings) {
    if (!byFunction[r.function_code]) byFunction[r.function_code] = []
    byFunction[r.function_code].push(r)
  }

  const rated = data.ratings.filter(r => {
    const ov = overrides[r.subcategory_id]
    const cur = ov && 'current_tier' in ov ? ov.current_tier : r.current_tier
    return cur != null
  }).length

  return (
    <Box>
      <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 3 }}>
        <Tooltip title="Back to profiles">
          <IconButton size="small" onClick={onBack} sx={{ mr: 0.5 }}>
            <ArrowBackOutlined sx={{ fontSize: 18 }} />
          </IconButton>
        </Tooltip>
        <Box sx={{ flex: 1, minWidth: 0 }}>
          {editName ? (
            <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
              <TextField value={nameVal} onChange={e => setNameVal(e.target.value)} size="small" autoFocus sx={{ flex: 1 }}
                onKeyDown={e => { if (e.key === 'Enter') updateProfileMutation.mutate({ name: nameVal }); if (e.key === 'Escape') setEditName(false) }} />
              <IconButton size="small" onClick={() => updateProfileMutation.mutate({ name: nameVal })}>
                <SaveOutlined sx={{ fontSize: 16 }} />
              </IconButton>
            </Box>
          ) : (
            <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.75 }}>
              <Typography variant="h6" fontWeight={700}>{data.profile.name}</Typography>
              <Tooltip title="Rename">
                <IconButton size="small" onClick={() => { setNameVal(data.profile.name); setEditName(true) }} sx={{ opacity: 0.4, '&:hover': { opacity: 1 } }}>
                  <EditOutlined sx={{ fontSize: 14 }} />
                </IconButton>
              </Tooltip>
            </Box>
          )}
          <Typography variant="caption" color="text.secondary">
            NIST CSF 2.0{data.profile.assessor ? ` \u00B7 ${data.profile.assessor}` : ''}{data.profile.scope ? ` \u00B7 ${data.profile.scope}` : ''}
          </Typography>
        </Box>
        <Box sx={{ display: 'flex', gap: 0.75, alignItems: 'center' }}>
          {(upsertMutation.isPending || importLoading) && <CircularProgress size={14} sx={{ color: 'text.disabled' }} />}
          <Chip icon={rated === 106 ? <CheckCircleOutlineOutlined sx={{ fontSize: 12 }} /> : <RadioButtonUncheckedOutlined sx={{ fontSize: 12 }} />}
            label={`${rated}/106`} size="small" sx={{ fontSize: '0.65rem', height: 20, bgcolor: 'rgba(68,114,196,0.12)', color: '#9DC3E6' }} />
          <Tooltip title="Import from NIST XLSX template">
            <IconButton size="small" onClick={() => importInputRef.current?.click()} sx={{ color: '#4472C4', bgcolor: 'rgba(68,114,196,0.1)', '&:hover': { bgcolor: 'rgba(68,114,196,0.2)' } }}>
              <UploadFileOutlined sx={{ fontSize: 16 }} />
            </IconButton>
          </Tooltip>
          <Tooltip title="Export XLSX">
            <IconButton size="small" onClick={handleExportXlsx} sx={{ color: '#70AD47', bgcolor: 'rgba(112,173,71,0.1)', '&:hover': { bgcolor: 'rgba(112,173,71,0.2)' } }}>
              <DownloadOutlined sx={{ fontSize: 16 }} />
            </IconButton>
          </Tooltip>
          <Tooltip title="Export CSV">
            <IconButton size="small" onClick={handleExportCsv} sx={{ color: '#8B9CC8', bgcolor: 'rgba(139,156,200,0.08)', '&:hover': { bgcolor: 'rgba(139,156,200,0.15)' } }}>
              <DownloadOutlined sx={{ fontSize: 14 }} />
            </IconButton>
          </Tooltip>
          <Tooltip title="View full report">
            <IconButton size="small" onClick={() => navigate(`/nist-csf/${profileId}/report`)} sx={{ color: '#FFC000', bgcolor: 'rgba(255,192,0,0.1)', '&:hover': { bgcolor: 'rgba(255,192,0,0.2)' } }}>
              <SummarizeOutlined sx={{ fontSize: 16 }} />
            </IconButton>
          </Tooltip>
          <Tooltip title="Delete profile">
            <IconButton size="small" onClick={onDelete} sx={{ color: 'error.main', opacity: 0.5, '&:hover': { opacity: 1 } }}>
              <DeleteOutlined sx={{ fontSize: 16 }} />
            </IconButton>
          </Tooltip>
          <input ref={importInputRef} type="file" accept=".xlsx" style={{ display: 'none' }} onChange={handleImportFile} />
        </Box>
      </Box>

      {upsertMutation.isError && <Alert severity="error" sx={{ mb: 2 }}>Failed to save ratings.</Alert>}
      <Snackbar open={!!importResult} autoHideDuration={6000} onClose={() => setImportResult(null)}
        anchorOrigin={{ vertical: 'bottom', horizontal: 'center' }}>
        <Alert severity="success" onClose={() => setImportResult(null)} sx={{ fontSize: '0.78rem' }}>
          Imported {importResult?.imported} ratings. Skipped: {importResult?.skipped}.
          {importResult && importResult.not_found.length > 0 && ` Not found: ${importResult.not_found.length}.`}
        </Alert>
      </Snackbar>
      <Snackbar open={!!importError} autoHideDuration={6000} onClose={() => setImportError(null)}
        anchorOrigin={{ vertical: 'bottom', horizontal: 'center' }}>
        <Alert severity="error" onClose={() => setImportError(null)} sx={{ fontSize: '0.78rem' }}>{importError}</Alert>
      </Snackbar>
      <Typography variant="caption" color="text.disabled" sx={{ display: 'block', mb: 2, fontStyle: 'italic' }}>Changes auto-save after 1.2s.</Typography>

      {FUNCTION_ORDER.map(fc => {
        const ratings = byFunction[fc] ?? []
        if (ratings.length === 0) return null
        return <FunctionSection key={fc} functionCode={fc} ratings={ratings} overrides={overrides} onOverride={handleOverride} saving={upsertMutation.isPending} />
      })}
    </Box>
  )
}

// ── Main page ──────────────────────────────────────────────────────────────

export default function NistCsf() {
  const queryClient = useQueryClient()
  const [selectedProfileId, setSelectedProfileId] = useState<string | null>(null)
  const [createOpen, setCreateOpen] = useState(false)
  const [deleteTarget, setDeleteTarget] = useState<{ id: string; name: string } | null>(null)
  const [newName, setNewName] = useState('')
  const [newDescription, setNewDescription] = useState('')
  const [newAssessor, setNewAssessor] = useState('')
  const [newScope, setNewScope] = useState('')

  const { data: profiles = [], isLoading } = useQuery<NistProfileSummary[]>({
    queryKey: ['nist-profiles'],
    queryFn: nistApi.listProfiles,
  })

  const createMutation = useMutation({
    mutationFn: nistApi.createProfile,
    onSuccess: (created) => {
      queryClient.invalidateQueries({ queryKey: ['nist-profiles'] })
      setCreateOpen(false)
      setNewName(''); setNewDescription(''); setNewAssessor(''); setNewScope('')
      setSelectedProfileId(created.id)
    },
  })

  const deleteMutation = useMutation({
    mutationFn: (id: string) => nistApi.deleteProfile(id),
    onSuccess: () => {
      setDeleteTarget(null)
      setSelectedProfileId(null)
      queryClient.invalidateQueries({ queryKey: ['nist-profiles'] })
    },
  })

  if (selectedProfileId) {
    return (
      <Box>
        <ProfileDetail
          profileId={selectedProfileId}
          onBack={() => setSelectedProfileId(null)}
          onDelete={() => {
            const p = profiles.find(p => p.id === selectedProfileId)
            if (p) setDeleteTarget({ id: p.id, name: p.name })
          }}
        />
        <Dialog open={!!deleteTarget} onClose={() => setDeleteTarget(null)} maxWidth="xs" fullWidth>
          <DialogTitle>Delete NIST CSF Profile?</DialogTitle>
          <DialogContent>
            <Typography variant="body2"><strong>{deleteTarget?.name}</strong> and all its ratings will be permanently removed.</Typography>
            {deleteMutation.isError && <Alert severity="error" sx={{ mt: 1.5 }}>Delete failed.</Alert>}
          </DialogContent>
          <DialogActions sx={{ px: 3, pb: 2 }}>
            <Button onClick={() => setDeleteTarget(null)} disabled={deleteMutation.isPending}>Cancel</Button>
            <Button variant="contained" color="error" disabled={deleteMutation.isPending} startIcon={<DeleteOutlined />}
              onClick={() => deleteTarget && deleteMutation.mutate(deleteTarget.id)}>
              {deleteMutation.isPending ? 'Deleting\u2026' : 'Delete'}
            </Button>
          </DialogActions>
        </Dialog>
      </Box>
    )
  }

  return (
    <Box>
      <PageHeader
        title="NIST CSF 2.0"
        subtitle="Cybersecurity Framework assessments — 106 subcategories, Tier 1–4, ISO 27001 crosswalk"
        actions={
          <Button variant="contained" size="small" startIcon={<AddOutlined />} onClick={() => setCreateOpen(true)} sx={{ fontSize: '0.78rem' }}>
            New Assessment
          </Button>
        }
      />

      <Box sx={{ display: 'flex', gap: 1, mb: 2, flexWrap: 'wrap' }}>
        {FUNCTION_ORDER.map(fc => (
          <Chip key={fc} icon={<GridViewOutlined sx={{ fontSize: 12 }} />}
            label={`${fc} \u2014 ${FUNCTION_NAMES[fc]}`} size="small"
            sx={{ fontSize: '0.65rem', height: 20, bgcolor: `${FUNCTION_COLORS[fc]}18`, color: FUNCTION_COLORS[fc], fontWeight: 600 }} />
        ))}
      </Box>

      <Box sx={{ display: 'flex', gap: 1, mb: 3, flexWrap: 'wrap' }}>
        {[1, 2, 3, 4].map(t => (
          <Chip key={t} label={`T${t} \u2014 ${TIER_LABELS[t]}`} size="small"
            sx={{ fontSize: '0.65rem', height: 20, bgcolor: `${tierColor(t)}18`, color: tierColor(t) }} />
        ))}
      </Box>

      {isLoading && [1, 2].map(i => <Skeleton key={i} variant="rectangular" height={120} sx={{ borderRadius: 2, mb: 1.5 }} />)}

      {!isLoading && profiles.length === 0 && (
        <Box onClick={() => setCreateOpen(true)} sx={{ p: 4, borderRadius: 2, textAlign: 'center', cursor: 'pointer', border: '1px dashed rgba(68,114,196,0.3)', bgcolor: 'rgba(68,114,196,0.03)', '&:hover': { bgcolor: 'rgba(68,114,196,0.07)' } }}>
          <GridViewOutlined sx={{ color: 'text.disabled', mb: 1, fontSize: 32 }} />
          <Typography variant="body2" color="text.secondary">No NIST CSF 2.0 assessments yet.</Typography>
          <Typography variant="caption" color="primary.light" sx={{ mt: 0.5, display: 'block' }}>Click to create your first assessment profile</Typography>
        </Box>
      )}

      {profiles.map(p => (
        <ProfileCard key={p.id} profile={p} onOpen={() => setSelectedProfileId(p.id)} onDelete={() => setDeleteTarget({ id: p.id, name: p.name })} />
      ))}

      <Dialog open={createOpen} onClose={() => setCreateOpen(false)} maxWidth="xs" fullWidth>
        <DialogTitle>New NIST CSF 2.0 Assessment</DialogTitle>
        <DialogContent sx={{ pt: '8px !important', display: 'flex', flexDirection: 'column', gap: 2 }}>
          <TextField label="Profile Name" value={newName} onChange={e => setNewName(e.target.value)} size="small" fullWidth required autoFocus />
          <TextField label="Description" value={newDescription} onChange={e => setNewDescription(e.target.value)} size="small" fullWidth multiline rows={2} />
          <TextField label="Assessor" value={newAssessor} onChange={e => setNewAssessor(e.target.value)} size="small" fullWidth />
          <TextField label="Scope" value={newScope} onChange={e => setNewScope(e.target.value)} size="small" fullWidth />
          {createMutation.isError && <Alert severity="error">Failed to create profile.</Alert>}
        </DialogContent>
        <DialogActions sx={{ px: 3, pb: 2 }}>
          <Button onClick={() => setCreateOpen(false)}>Cancel</Button>
          <Button variant="contained" disabled={!newName.trim() || createMutation.isPending}
            onClick={() => createMutation.mutate({ name: newName.trim(), description: newDescription || undefined, assessor: newAssessor || undefined, scope: newScope || undefined })}>
            {createMutation.isPending ? 'Creating\u2026' : 'Create'}
          </Button>
        </DialogActions>
      </Dialog>

      <Dialog open={!!deleteTarget} onClose={() => setDeleteTarget(null)} maxWidth="xs" fullWidth>
        <DialogTitle>Delete NIST CSF Profile?</DialogTitle>
        <DialogContent>
          <Typography variant="body2"><strong>{deleteTarget?.name}</strong> and all its ratings will be permanently removed.</Typography>
          {deleteMutation.isError && <Alert severity="error" sx={{ mt: 1.5 }}>Delete failed.</Alert>}
        </DialogContent>
        <DialogActions sx={{ px: 3, pb: 2 }}>
          <Button onClick={() => setDeleteTarget(null)} disabled={deleteMutation.isPending}>Cancel</Button>
          <Button variant="contained" color="error" disabled={deleteMutation.isPending} startIcon={<DeleteOutlined />}
            onClick={() => deleteTarget && deleteMutation.mutate(deleteTarget.id)}>
            {deleteMutation.isPending ? 'Deleting\u2026' : 'Delete'}
          </Button>
        </DialogActions>
      </Dialog>
    </Box>
  )
}
