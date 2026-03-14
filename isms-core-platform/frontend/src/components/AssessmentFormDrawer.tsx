/**
 * AssessmentFormDrawer — Phase 7.9
 * WebUI form renderer for creating/editing assessments from generator schema.
 * Opens as a right drawer from ControlDetail.
 */
import { useState, useEffect } from 'react'
import {
  Drawer, Box, Typography, IconButton, Tabs, Tab, Divider,
  Table, TableHead, TableRow, TableCell, TableBody, TableContainer,
  Select, MenuItem, TextField, Button, Chip, CircularProgress,
  Alert, Tooltip, Grid, FormControl, InputLabel,
} from '@mui/material'
import {
  CloseOutlined, AddOutlined, DeleteOutlined, SaveOutlined,
  AssignmentOutlined,
} from '@mui/icons-material'
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { assessmentsApi, FormSheet, AssessmentItemRead, AssessmentSheetRead } from '../api/assessmentsApi'

// ── Status chip colours ──────────────────────────────────────────────────────

const STATUS_CHIP: Record<string, { bg: string; fg: string; label: string }> = {
  compliant:     { bg: '#1a3a27', fg: '#C6EFCE', label: '✅ Compliant' },
  partial:       { bg: '#3a2e00', fg: '#FFEB9C', label: '⚠️ Partial' },
  non_compliant: { bg: '#3a0000', fg: '#FFC7CE', label: '❌ Non-Compliant' },
  na:            { bg: 'rgba(255,255,255,0.06)', fg: '#9e9e9e', label: '➖ N/A' },
  not_assessed:  { bg: 'rgba(255,255,255,0.04)', fg: '#666', label: '— Not assessed' },
}

// ── Blank row factory ────────────────────────────────────────────────────────

function blankRow(columns: FormSheet['columns']): Record<string, string> {
  const r: Record<string, string> = {}
  columns.forEach((c) => { r[c.header] = '' })
  return r
}

// ── Inline editable row ──────────────────────────────────────────────────────

interface EditRowProps {
  rowIndex: number
  columns: FormSheet['columns']
  values: Record<string, string>
  saved: boolean
  saving: boolean
  onCellChange: (header: string, value: string) => void
  onSave: () => void
  onDelete: () => void
}

function EditRow({ rowIndex, columns, values, saved, saving, onCellChange, onSave, onDelete }: EditRowProps) {
  return (
    <TableRow hover sx={{ '& td': { py: 0.5, px: 1 } }}>
      <TableCell sx={{ color: 'text.disabled', fontSize: '0.65rem', width: 32 }}>{rowIndex}</TableCell>
      {columns.map((col) => (
        <TableCell key={col.header} sx={{ minWidth: col.width ? Math.min(col.width * 6, 200) : 120 }}>
          {col.dv_values.length > 0 ? (
            <Select
              size="small"
              value={values[col.header] ?? ''}
              onChange={(e) => onCellChange(col.header, e.target.value)}
              displayEmpty
              sx={{ fontSize: '0.75rem', minWidth: 120, '& .MuiSelect-select': { py: 0.5 } }}
            >
              <MenuItem value=""><em>— select —</em></MenuItem>
              {col.dv_values.map((v) => (
                <MenuItem key={v} value={v} sx={{ fontSize: '0.75rem' }}>{v}</MenuItem>
              ))}
            </Select>
          ) : (
            <TextField
              size="small"
              value={values[col.header] ?? ''}
              onChange={(e) => onCellChange(col.header, e.target.value)}
              multiline={col.width > 30}
              maxRows={3}
              sx={{ fontSize: '0.75rem', '& input, & textarea': { fontSize: '0.75rem', py: 0.5 } }}
            />
          )}
        </TableCell>
      ))}
      <TableCell sx={{ width: 80 }}>
        <Box sx={{ display: 'flex', gap: 0.5 }}>
          <Tooltip title={saved ? 'Saved' : 'Save row'}>
            <IconButton size="small" onClick={onSave} disabled={saving || saved}
              sx={{ color: saved ? '#C6EFCE' : 'primary.main' }}>
              {saving ? <CircularProgress size={14} /> : <SaveOutlined sx={{ fontSize: 16 }} />}
            </IconButton>
          </Tooltip>
          <Tooltip title="Delete row">
            <IconButton size="small" color="error" onClick={onDelete}>
              <DeleteOutlined sx={{ fontSize: 16 }} />
            </IconButton>
          </Tooltip>
        </Box>
      </TableCell>
    </TableRow>
  )
}

// ── Saved (existing DB) row ──────────────────────────────────────────────────

function SavedRow({ item, columns, onDelete, onUpdate }: {
  item: AssessmentItemRead
  columns: FormSheet['columns']
  onDelete: () => void
  onUpdate: (header: string, value: string) => void
}) {
  const [editing, setEditing] = useState(false)
  const [vals, setVals] = useState<Record<string, string>>(item.col_data ?? {})

  useEffect(() => { setVals(item.col_data ?? {}) }, [item])

  const sc = STATUS_CHIP[item.status] ?? STATUS_CHIP.not_assessed

  return (
    <TableRow hover sx={{ '& td': { py: 0.5, px: 1 } }}>
      <TableCell sx={{ color: 'text.disabled', fontSize: '0.65rem', width: 32 }}>{item.row_number}</TableCell>
      {columns.map((col) => (
        <TableCell key={col.header} sx={{ minWidth: col.width ? Math.min(col.width * 6, 200) : 120 }}>
          {editing ? (
            col.dv_values.length > 0 ? (
              <Select size="small" value={vals[col.header] ?? ''} displayEmpty
                onChange={(e) => { const v = e.target.value; setVals(p => ({ ...p, [col.header]: v })); onUpdate(col.header, v) }}
                sx={{ fontSize: '0.75rem', minWidth: 120, '& .MuiSelect-select': { py: 0.5 } }}>
                <MenuItem value=""><em>— select —</em></MenuItem>
                {col.dv_values.map((v) => <MenuItem key={v} value={v} sx={{ fontSize: '0.75rem' }}>{v}</MenuItem>)}
              </Select>
            ) : (
              <TextField size="small" value={vals[col.header] ?? ''} multiline={col.width > 30} maxRows={3}
                onChange={(e) => { const v = e.target.value; setVals(p => ({ ...p, [col.header]: v })); onUpdate(col.header, v) }}
                sx={{ '& input, & textarea': { fontSize: '0.75rem', py: 0.5 } }} />
            )
          ) : (
            <Box onClick={() => setEditing(true)} sx={{ cursor: 'text', minHeight: 24 }}>
              {col.is_status_col && vals[col.header] ? (
                <Chip label={vals[col.header]} size="small"
                  sx={{ fontSize: '0.6rem', height: 18, bgcolor: sc.bg, color: sc.fg }} />
              ) : (
                <Typography variant="caption" sx={{ color: vals[col.header] ? 'text.primary' : 'text.disabled' }}>
                  {vals[col.header] || '—'}
                </Typography>
              )}
            </Box>
          )}
        </TableCell>
      ))}
      <TableCell sx={{ width: 80 }}>
        <Tooltip title="Delete row">
          <IconButton size="small" color="error" onClick={onDelete}>
            <DeleteOutlined sx={{ fontSize: 16 }} />
          </IconButton>
        </Tooltip>
      </TableCell>
    </TableRow>
  )
}

// ── Sheet tab panel ──────────────────────────────────────────────────────────

interface SheetPanelProps {
  formSheet: FormSheet
  assessmentId: string
  savedSheet: AssessmentSheetRead | undefined
  onRowAdded: () => void
  onRowDeleted: () => void
}

function SheetPanel({ formSheet, assessmentId, savedSheet, onRowAdded, onRowDeleted }: SheetPanelProps) {
  const qc = useQueryClient()
  const [pending, setPending] = useState<Record<string, string>[]>([])
  const [savingIdx, setSavingIdx] = useState<number | null>(null)
  const [savedIdxs, setSavedIdxs] = useState<Set<number>>(new Set())

  const existingRows = savedSheet?.items ?? []
  const nextRowNum = (savedSheet?.row_count ?? 0) + pending.length + 1

  const addMutation = useMutation({
    mutationFn: (rowData: { idx: number; vals: Record<string, string> }) => {
      const statusCol = formSheet.columns.find((c) => c.is_status_col || c.dv_values.some(v => v.toLowerCase().includes('compliant') || v.toLowerCase().includes('yes')))
      const statusDV = statusCol ? (rowData.vals[statusCol.header] ?? '') : ''
      const firstCol = formSheet.columns[0]
      return assessmentsApi.addRow(assessmentId, {
        sheet_name: formSheet.sheet_name,
        row_number: existingRows.length + rowData.idx + 1,
        item_text: firstCol ? (rowData.vals[firstCol.header] ?? '') : '',
        status: statusDV,
        col_data: rowData.vals,
      })
    },
    onSuccess: (_, vars) => {
      setSavingIdx(null)
      setSavedIdxs((s) => new Set([...s, vars.idx]))
      qc.invalidateQueries({ queryKey: ['assessment-sheets', assessmentId] })
      onRowAdded()
      // Remove from pending after brief delay so user sees saved state
      setTimeout(() => {
        setPending((p) => p.filter((_, i) => i !== vars.idx))
        setSavedIdxs((s) => { const n = new Set(s); n.delete(vars.idx); return n })
      }, 800)
    },
  })

  const updateMutation = useMutation({
    mutationFn: ({ itemId, header, value }: { itemId: string; header: string; value: string }) => {
      const col_data = { ...(savedSheet?.items.find(i => i.id === itemId)?.col_data ?? {}), [header]: value }
      const statusCol = formSheet.columns.find((c) => c.is_status_col || c.dv_values.some(v => v.toLowerCase().includes('compliant')))
      const statusDV = statusCol ? (col_data[statusCol.header] ?? '') : undefined
      return assessmentsApi.updateItem(itemId, { col_data, status: statusDV })
    },
    onSuccess: () => qc.invalidateQueries({ queryKey: ['assessment-sheets', assessmentId] }),
  })

  const deleteMutation = useMutation({
    mutationFn: (itemId: string) => assessmentsApi.deleteItem(itemId),
    onSuccess: () => {
      qc.invalidateQueries({ queryKey: ['assessment-sheets', assessmentId] })
      onRowDeleted()
    },
  })

  function addPendingRow() {
    setPending((p) => [...p, blankRow(formSheet.columns)])
  }

  return (
    <Box>
      {formSheet.subtitle_text && (
        <Typography variant="caption" color="text.secondary" sx={{ display: 'block', mb: 1, fontStyle: 'italic' }}>
          {formSheet.subtitle_text}
        </Typography>
      )}

      <TableContainer sx={{ maxHeight: 480, overflowY: 'auto', overflowX: 'auto' }}>
        <Table size="small" stickyHeader>
          <TableHead>
            <TableRow>
              <TableCell sx={{ width: 32, bgcolor: '#1e1e1e', color: 'text.disabled', fontSize: '0.6rem' }}>#</TableCell>
              {formSheet.columns.map((col) => (
                <TableCell key={col.header} sx={{ bgcolor: '#1e1e1e', fontSize: '0.7rem', fontWeight: 600, whiteSpace: 'nowrap' }}>
                  {col.header}
                  {col.is_status_col && <Chip label="status" size="small" sx={{ ml: 0.5, fontSize: '0.55rem', height: 14, bgcolor: 'rgba(68,114,196,0.2)', color: '#9DC3E6' }} />}
                </TableCell>
              ))}
              <TableCell sx={{ bgcolor: '#1e1e1e', width: 80 }} />
            </TableRow>
          </TableHead>
          <TableBody>
            {existingRows.map((item) => (
              <SavedRow
                key={item.id}
                item={item}
                columns={formSheet.columns}
                onDelete={() => deleteMutation.mutate(item.id)}
                onUpdate={(header, value) => updateMutation.mutate({ itemId: item.id, header, value })}
              />
            ))}
            {pending.map((vals, idx) => (
              <EditRow
                key={idx}
                rowIndex={existingRows.length + idx + 1}
                columns={formSheet.columns}
                values={vals}
                saved={savedIdxs.has(idx)}
                saving={savingIdx === idx}
                onCellChange={(header, value) =>
                  setPending((p) => p.map((r, i) => i === idx ? { ...r, [header]: value } : r))
                }
                onSave={() => {
                  setSavingIdx(idx)
                  addMutation.mutate({ idx, vals })
                }}
                onDelete={() => setPending((p) => p.filter((_, i) => i !== idx))}
              />
            ))}
          </TableBody>
        </Table>
      </TableContainer>

      <Box sx={{ mt: 1.5 }}>
        <Button size="small" startIcon={<AddOutlined />} onClick={addPendingRow} variant="outlined">
          Add Row
        </Button>
        {existingRows.length > 0 && (
          <Typography variant="caption" color="text.secondary" sx={{ ml: 2 }}>
            {existingRows.length} row{existingRows.length !== 1 ? 's' : ''} saved
          </Typography>
        )}
      </Box>
    </Box>
  )
}

// ── Main drawer ──────────────────────────────────────────────────────────────

interface Props {
  open: boolean
  onClose: () => void
  groupCode: string
  groupName: string
  productType?: string
  generatorId?: string
}

export default function AssessmentFormDrawer({ open, onClose, groupCode, groupName, productType = 'framework', generatorId }: Props) {
  const qc = useQueryClient()
  const [tab, setTab] = useState(0)
  const [assessmentId, setAssessmentId] = useState<string | null>(null)
  const [creating, setCreating] = useState(false)
  // Metadata form
  const [label, setLabel] = useState('')
  const [assessor, setAssessor] = useState('')
  const [scope, setScope] = useState('')
  const [purpose, setPurpose] = useState('')
  const [targetDate, setTargetDate] = useState('')

  // Reset when drawer opens or product/group changes
  useEffect(() => {
    if (open) {
      setAssessmentId(null); setTab(0)
      setLabel(''); setAssessor(''); setScope(''); setPurpose(''); setTargetDate('')
    }
  }, [open, groupCode, productType, generatorId])

  const { data: formSheets = [], isLoading: schemasLoading } = useQuery({
    queryKey: ['form-schema', groupCode, productType, generatorId],
    queryFn: () => assessmentsApi.getFormSchema(groupCode, productType, generatorId),
    enabled: open && !!groupCode,
  })

  const { data: sheets = [], refetch: refetchSheets } = useQuery({
    queryKey: ['assessment-sheets', assessmentId],
    queryFn: () => assessmentsApi.getSheets(assessmentId!),
    enabled: !!assessmentId,
  })

  // Live document ID preview
  const docIdPreview = (() => {
    const gc = groupCode.toUpperCase()
    const today = new Date().toISOString().slice(0, 10).replace(/-/g, '')
    if (label.trim()) {
      const slug = label.trim().replace(/[^a-zA-Z0-9-]/g, '-').replace(/-+/g, '-').replace(/^-|-$/g, '').slice(0, 20)
      return `ISMS-ASS-${gc}_${slug}_${today}`
    }
    return `ISMS-ASS-${gc}-${today}xxxxxx`
  })()

  async function handleStartAssessment() {
    setCreating(true)
    try {
      const a = await assessmentsApi.create(groupCode, productType, groupName, {
        label, assessor, scope, purpose, target_date: targetDate,
      })
      setAssessmentId(a.id)
      qc.invalidateQueries({ queryKey: ['assessments'] })
    } finally {
      setCreating(false)
    }
  }

  const noInputSheets = !schemasLoading && formSheets.length === 0 && !assessmentId

  return (
    <Drawer
      anchor="right"
      open={open}
      onClose={onClose}
      PaperProps={{ sx: { width: { xs: '100%', md: 'calc(100vw - 60px)' }, maxWidth: 1600, bgcolor: '#141414', borderLeft: '1px solid rgba(255,255,255,0.08)' } }}
    >
      {/* Header */}
      <Box sx={{ px: 3, py: 2, borderBottom: '1px solid rgba(255,255,255,0.08)', display: 'flex', alignItems: 'center', gap: 1 }}>
        <AssignmentOutlined sx={{ color: 'primary.main', fontSize: 20 }} />
        <Box sx={{ flex: 1 }}>
          <Typography variant="subtitle1" fontWeight={700}>{groupName}</Typography>
          <Typography variant="caption" color="text.secondary">{groupCode.toUpperCase()} — Platform Assessment</Typography>
        </Box>
        {assessmentId && (
          <Chip label="In Progress" size="small" sx={{ bgcolor: 'rgba(68,114,196,0.2)', color: '#9DC3E6', fontSize: '0.65rem' }} />
        )}
        <IconButton onClick={onClose} size="small"><CloseOutlined /></IconButton>
      </Box>

      <Box sx={{ px: 3, py: 2, flex: 1, overflowY: 'auto' }}>
        {schemasLoading && <CircularProgress size={24} />}

        {noInputSheets && productType !== 'operational' && (
          <Alert severity="info">No input sheets found for this control group.</Alert>
        )}
        {noInputSheets && productType === 'operational' && (
          <Box sx={{ mt: 2, p: 2.5, bgcolor: 'rgba(112,173,71,0.06)', border: '1px solid rgba(112,173,71,0.2)', borderRadius: 2 }}>
            <Typography variant="body2" fontWeight={600} sx={{ color: '#70AD47', mb: 1 }}>
              Operational assessments are in the Workbook Library
            </Typography>
            <Typography variant="body2" color="text.secondary">
              Operational platform forms are not yet available. The imported operational workbooks for{' '}
              <strong>{groupName}</strong> are accessible via the Workbook Library on this page.
            </Typography>
            <Typography variant="caption" color="text.disabled" sx={{ display: 'block', mt: 1 }}>
              Framework platform forms (ISO 27001 full controls) are fully supported — select Framework when starting a new assessment.
            </Typography>
          </Box>
        )}

        {!schemasLoading && formSheets.length > 0 && !assessmentId && (
          <Box sx={{ mt: 2, maxWidth: 800 }}>
            {/* Intro */}
            <Typography variant="body2" color="text.secondary" sx={{ mb: 2 }}>
              New platform assessment for <strong>{groupName}</strong> — {formSheets.length} input sheet{formSheets.length !== 1 ? 's' : ''}.
              Fill in your organisation's data directly, no Excel required.
            </Typography>
            <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 0.75, mb: 3 }}>
              {formSheets.map((s) => (
                <Chip key={s.sheet_name} label={s.sheet_name} size="small"
                  sx={{ fontSize: '0.65rem', bgcolor: 'rgba(68,114,196,0.1)', color: '#9DC3E6' }} />
              ))}
            </Box>

            {/* Metadata form */}
            <Box sx={{ p: 2.5, bgcolor: 'rgba(255,255,255,0.03)', borderRadius: 2, border: '1px solid rgba(255,255,255,0.07)', mb: 3 }}>
              <Typography variant="caption" fontWeight={700} color="primary.light" sx={{ textTransform: 'uppercase', letterSpacing: '0.06em', fontSize: '0.7rem', display: 'block', mb: 2 }}>
                Assessment Details
              </Typography>
              <Grid container spacing={2}>
                {/* Label / Name */}
                <Grid item xs={12} sm={6}>
                  <TextField
                    size="small" fullWidth label="Assessment Label"
                    placeholder="e.g. Q1-2026, Gap-Analysis (short label)"
                    value={label} onChange={(e) => setLabel(e.target.value.replace(/[^a-zA-Z0-9 \-_]/g, ''))}
                    inputProps={{ maxLength: 25 }}
                    helperText={
                      <span style={{ fontFamily: 'monospace', fontSize: '0.65rem', color: '#9DC3E6' }}>
                        {docIdPreview}
                      </span>
                    }
                  />
                </Grid>
                {/* Lead Assessor */}
                <Grid item xs={12} sm={6}>
                  <TextField
                    size="small" fullWidth label="Lead Assessor"
                    placeholder="e.g. Jane Smith — ISMS Manager"
                    value={assessor} onChange={(e) => setAssessor(e.target.value)}
                  />
                </Grid>
                {/* Purpose */}
                <Grid item xs={12} sm={6}>
                  <FormControl size="small" fullWidth>
                    <InputLabel>Purpose</InputLabel>
                    <Select value={purpose} onChange={(e) => setPurpose(e.target.value)} label="Purpose">
                      <MenuItem value=""><em>Select…</em></MenuItem>
                      <MenuItem value="Initial Assessment">Initial Assessment</MenuItem>
                      <MenuItem value="Re-assessment">Re-assessment</MenuItem>
                      <MenuItem value="Gap Analysis">Gap Analysis</MenuItem>
                      <MenuItem value="Audit Preparation">Audit Preparation</MenuItem>
                      <MenuItem value="Targeted Review">Targeted Review</MenuItem>
                      <MenuItem value="Continuous Monitoring">Continuous Monitoring</MenuItem>
                    </Select>
                  </FormControl>
                </Grid>
                {/* Target Completion */}
                <Grid item xs={12} sm={6}>
                  <TextField
                    size="small" fullWidth label="Target Completion Date"
                    type="date" value={targetDate} onChange={(e) => setTargetDate(e.target.value)}
                    InputLabelProps={{ shrink: true }}
                  />
                </Grid>
                {/* Scope */}
                <Grid item xs={12}>
                  <TextField
                    size="small" fullWidth label="Scope"
                    placeholder="Systems, departments, locations or processes in scope for this assessment"
                    value={scope} onChange={(e) => setScope(e.target.value)}
                    multiline rows={2}
                  />
                </Grid>
              </Grid>
            </Box>

            <Button
              variant="contained" size="large"
              startIcon={creating ? <CircularProgress size={14} /> : <AssignmentOutlined />}
              onClick={handleStartAssessment}
              disabled={creating}
            >
              {creating ? 'Creating…' : 'Start Assessment'}
            </Button>
          </Box>
        )}

        {assessmentId && formSheets.length > 0 && (
          <>
            <Tabs
              value={tab}
              onChange={(_, v) => setTab(v)}
              sx={{ mb: 2, borderBottom: 1, borderColor: 'divider' }}
              variant="scrollable"
              scrollButtons="auto"
            >
              {formSheets.map((s, i) => {
                const savedSheet = sheets.find((sh) => sh.sheet_name === s.sheet_name)
                return (
                  <Tab
                    key={s.sheet_name}
                    label={
                      <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.5 }}>
                        {s.sheet_name}
                        {(savedSheet?.row_count ?? 0) > 0 && (
                          <Chip label={savedSheet!.row_count} size="small"
                            sx={{ fontSize: '0.55rem', height: 14, bgcolor: '#1a3a27', color: '#C6EFCE' }} />
                        )}
                      </Box>
                    }
                    sx={{ fontSize: '0.75rem', minHeight: 40, textTransform: 'none' }}
                  />
                )
              })}
            </Tabs>

            {formSheets.map((formSheet, i) => (
              <Box key={formSheet.sheet_name} hidden={tab !== i}>
                {tab === i && (
                  <SheetPanel
                    formSheet={formSheet}
                    assessmentId={assessmentId}
                    savedSheet={sheets.find((sh) => sh.sheet_name === formSheet.sheet_name)}
                    onRowAdded={() => refetchSheets()}
                    onRowDeleted={() => refetchSheets()}
                  />
                )}
              </Box>
            ))}
          </>
        )}
      </Box>
    </Drawer>
  )
}
