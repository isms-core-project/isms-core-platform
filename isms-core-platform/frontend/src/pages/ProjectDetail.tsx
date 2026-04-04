import { useState, useMemo, useEffect, useCallback, useRef } from 'react'
import {
  Alert,
  Box,
  Button,
  Checkbox,
  Chip,
  CircularProgress,
  Collapse,
  Dialog,
  DialogActions,
  DialogContent,
  DialogTitle,
  Drawer,
  Divider,
  FormControl,
  Grid,
  IconButton,
  InputAdornment,
  InputLabel,
  LinearProgress,
  MenuItem,
  Select,
  Skeleton,
  Tab,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  TableSortLabel,
  Switch,
  Tabs,
  TextField,
  Tooltip,
  Typography,
} from '@mui/material'
import {
  ArrowBackOutlined,
  AssignmentOutlined,
  BlockOutlined,
  CheckCircleOutlined,
  CloseOutlined,
  CodeOutlined,
  DeleteOutlined,
  EditOutlined,
  ErrorOutlined,
  ExpandMoreOutlined,
  FindInPageOutlined,
  FormatBoldOutlined,
  FormatItalicOutlined,
  FormatListBulletedOutlined,
  FormatListNumberedOutlined,
  HorizontalRuleOutlined,
  LibraryBooksOutlined,
  LockOutlined,
  PolicyOutlined,
  RestoreFromTrashOutlined,
  SaveOutlined,
  SearchOutlined,
  SyncOutlined,
  ShieldOutlined,
  UploadFileOutlined,
  WarningAmberOutlined,
  VerifiedOutlined,
  PlayArrowOutlined,
  AutoAwesomeOutlined,
} from '@mui/icons-material'
import dayjs from 'dayjs'
import { useEditor, EditorContent } from '@tiptap/react'
import StarterKit from '@tiptap/starter-kit'
import { Table as TiptapTable, TableRow as TiptapTableRow, TableHeader as TiptapTableHeader, TableCell as TiptapTableCell } from '@tiptap/extension-table'
import { Markdown } from 'tiptap-markdown'
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { useNavigate, useParams } from 'react-router-dom'
import { projectsApi, type DocVars, type LibraryChecklistItem, type LibraryImplItem, type LibraryPolicyItem, type ProjectChecklistRead } from '../api/projectsApi'
import { qaApi, type CorrelationResultRead, type ProjectQASummary } from '../api/qa'
import { gapsApi } from '../api/gaps'
import { evidenceApi } from '../api/evidence'
import { controlsApi } from '../api/controls'
import { regulatoryApi } from '../api/regulatoryApi'
import { useProject } from '../store/ProjectContext'
import { useAuth } from '../store/AuthContext'
import PageHeader from '../components/PageHeader'

/** Roles that may soft-delete and permanently delete project documents */
const CAN_DELETE_ROLES = new Set(['admin', 'isms_manager'])

const FAMILY_COLOR: Record<string, string> = {
  ISMS:    '#4472C4',
  PRIVACY: '#70309f',
  CLOUD:   '#0099cc',
}

const TOTAL_CG: Record<string, number> = { ISMS: 53, PRIVACY: 21, CLOUD: 12 }

const POL_TYPE_COLOR: Record<string, string> = {
  POL:    '#4472C4',
  'OP-POL': '#70AD47',
  INS:    '#9E9E9E',
}

const IMPL_TYPE_COLOR: Record<string, string> = {
  UG: '#4472C4',
  TG: '#ED7D31',
}

// ── Completeness panel ────────────────────────────────────────────────────────
function CompletenessPanel({
  productFamily,
  policyCodes,
  implCodes,
}: {
  productFamily: string
  policyCodes: string[]
  implCodes: string[]
}) {
  const color = FAMILY_COLOR[productFamily] ?? '#4472C4'
  const total = TOTAL_CG[productFamily] ?? 53
  const polUnique = new Set(policyCodes.filter(Boolean)).size
  const implUnique = new Set(implCodes.filter(Boolean)).size
  const polPct = Math.min(100, Math.round((polUnique / total) * 100))
  const implPct = Math.min(100, Math.round((implUnique / total) * 100))
  const overallPct = Math.round((polPct + implPct) / 2)

  function Bar({ label, count, pct }: { label: string; count: number; pct: number }) {
    return (
      <Box sx={{ mb: 1.5 }}>
        <Box sx={{ display: 'flex', justifyContent: 'space-between', mb: 0.3 }}>
          <Typography variant="caption" sx={{ fontSize: '0.69rem', color: 'text.secondary' }}>{label}</Typography>
          <Typography variant="caption" sx={{ fontSize: '0.69rem', color }}>{count}/{total}</Typography>
        </Box>
        <LinearProgress
          variant="determinate"
          value={pct}
          sx={{ height: 5, borderRadius: 3, bgcolor: `${color}18`, '& .MuiLinearProgress-bar': { bgcolor: color } }}
        />
      </Box>
    )
  }

  return (
    <Box sx={{ p: 2, border: '1px solid', borderColor: 'divider', borderRadius: 1.5, mb: 3 }}>
      <Box sx={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', mb: 2 }}>
        <Typography variant="caption" sx={{ fontWeight: 700, textTransform: 'uppercase', letterSpacing: '0.06em', fontSize: '0.65rem', color: 'text.secondary' }}>
          Project Completeness
        </Typography>
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.5 }}>
          <Typography variant="h5" sx={{ fontWeight: 700, color, lineHeight: 1, fontSize: '1.4rem' }}>{overallPct}%</Typography>
        </Box>
      </Box>
      <Bar label="Policy coverage" count={polUnique} pct={polPct} />
      <Bar label="Implementation coverage" count={implUnique} pct={implPct} />
      {overallPct < 100 && (
        <Typography variant="caption" sx={{ fontSize: '0.65rem', color: 'text.disabled', display: 'block', mt: 0.5 }}>
          {total - Math.max(polUnique, implUnique)} control group{total - Math.max(polUnique, implUnique) !== 1 ? 's' : ''} still missing documents
        </Typography>
      )}
      {overallPct === 100 && (
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.5, mt: 0.5 }}>
          <CheckCircleOutlined sx={{ fontSize: 13, color: '#4CAF50' }} />
          <Typography variant="caption" sx={{ fontSize: '0.65rem', color: '#4CAF50' }}>All control groups covered</Typography>
        </Box>
      )}
    </Box>
  )
}

// ── Document variables panel ──────────────────────────────────────────────────
function DocVarsPanel({ projectId, initial }: { projectId: string; initial: DocVars | null }) {
  const qc = useQueryClient()
  const [open, setOpen] = useState(false)
  const [dv, setDv] = useState<DocVars>(initial ?? {})
  const [saved, setSaved] = useState(false)

  const mutation = useMutation({
    mutationFn: (vars: DocVars) => projectsApi.update(projectId, { doc_vars: vars }),
    onSuccess: () => {
      qc.invalidateQueries({ queryKey: ['project', projectId] })
      setSaved(true)
      setTimeout(() => setSaved(false), 2000)
    },
  })

  function handleSave() {
    const cleaned: DocVars = Object.fromEntries(Object.entries(dv).filter(([, v]) => v)) as DocVars
    mutation.mutate(cleaned)
  }

  const set = (k: keyof DocVars, v: string) => { setDv(f => ({ ...f, [k]: v })); setSaved(false) }

  const hasMissing = !dv.ciso_name || !dv.effective_date

  return (
    <Box sx={{ mb: 2.5, border: '1px solid', borderColor: hasMissing ? 'warning.dark' : 'divider', borderRadius: 1.5, overflow: 'hidden' }}>
      <Box
        onClick={() => setOpen(o => !o)}
        sx={{ display: 'flex', alignItems: 'center', gap: 1, px: 2, py: 1.25, cursor: 'pointer', bgcolor: 'rgba(255,255,255,0.02)', '&:hover': { bgcolor: 'rgba(255,255,255,0.04)' } }}
      >
        <ExpandMoreOutlined sx={{ fontSize: 16, color: 'text.secondary', transition: 'transform 0.2s', transform: open ? 'rotate(0)' : 'rotate(-90deg)' }} />
        <Typography variant="caption" sx={{ fontWeight: 600, fontSize: '0.75rem', flex: 1 }}>
          Document Variables
        </Typography>
        {hasMissing ? (
          <Chip label="Incomplete" size="small" sx={{ height: 18, fontSize: '0.6rem', bgcolor: '#FF980018', color: '#FF9800' }} />
        ) : (
          <Chip label="Set" size="small" sx={{ height: 18, fontSize: '0.6rem', bgcolor: '#4CAF5018', color: '#4CAF50' }} />
        )}
        <Typography variant="caption" color="text.disabled" sx={{ fontSize: '0.65rem' }}>
          substituted into POL &amp; IMP when added to this project
        </Typography>
      </Box>

      <Collapse in={open}>
        <Box sx={{ px: 2, pb: 2, pt: 1 }}>
          <Typography variant="caption" color="text.disabled" sx={{ display: 'block', mb: 1.5, fontSize: '0.68rem' }}>
            These values replace <code>[CISO name]</code>, <code>[CEO Name]</code>, <code>[DPO name]</code>, <code>[Date to be set]</code>, <code>[Effective Date + 12 months]</code>, <code>[Organisation]</code> etc. in library documents when they are added to this project. The substituted content is stored in the project copy.
          </Typography>
          <Box sx={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 1.5, mb: 1.5 }}>
            <TextField label="Organisation" size="small" fullWidth disabled value="(from project settings)" />
            <TextField label="CISO name" size="small" fullWidth value={dv.ciso_name ?? ''}
              onChange={e => set('ciso_name', e.target.value)} placeholder="e.g. Jane Smith" />
            <TextField label="CEO name" size="small" fullWidth value={dv.ceo_name ?? ''}
              onChange={e => set('ceo_name', e.target.value)} placeholder="e.g. John Smith" />
            <TextField label="DPO name" size="small" fullWidth value={dv.dpo_name ?? ''}
              onChange={e => set('dpo_name', e.target.value)} placeholder="e.g. John Doe" />
            <TextField label="Legal entity name" size="small" fullWidth value={dv.legal_entity ?? ''}
              onChange={e => set('legal_entity', e.target.value)} placeholder="e.g. Acme Corp Ltd." />
            <TextField label="Effective date" size="small" fullWidth value={dv.effective_date ?? ''}
              onChange={e => set('effective_date', e.target.value)}
              placeholder="DD.MM.YYYY or YYYY-MM-DD" helperText="e.g. 01.01.2026" />
            <TextField label="Next review date" size="small" fullWidth value={dv.review_date ?? ''}
              onChange={e => set('review_date', e.target.value)}
              placeholder="DD.MM.YYYY or YYYY-MM-DD" helperText="e.g. 01.01.2027" />
            <TextField label="Classification" size="small" fullWidth value={dv.classification ?? ''}
              onChange={e => set('classification', e.target.value)} placeholder="Internal" />
          </Box>
          <Box sx={{ display: 'flex', gap: 1, flexWrap: 'wrap' }}>
            <Button
              size="small"
              variant={saved ? 'outlined' : 'contained'}
              startIcon={<SaveOutlined sx={{ fontSize: 14 }} />}
              onClick={handleSave}
              disabled={mutation.isPending}
              color={saved ? 'success' : 'primary'}
              sx={{ fontSize: '0.72rem' }}
            >
              {saved ? 'Saved' : 'Save Variables'}
            </Button>
            <ReapplyDocVarsButton projectId={projectId} />
          </Box>
        </Box>
      </Collapse>
    </Box>
  )
}

function ReapplyDocVarsButton({ projectId }: { projectId: string }) {
  const mutation = useMutation({
    mutationFn: () => projectsApi.reapplyDocVars(projectId),
  })
  const d = mutation.data
  return (
    <Tooltip title="Re-apply saved variables to all library-sourced policies and implementations. Save variables first, then click this.">
      <Button
        size="small"
        variant={d ? 'outlined' : 'outlined'}
        color={d ? 'success' : 'secondary'}
        startIcon={<SyncOutlined sx={{ fontSize: 14 }} />}
        onClick={() => mutation.mutate()}
        disabled={mutation.isPending}
        sx={{ fontSize: '0.72rem' }}
      >
        {mutation.isPending
          ? 'Re-applying…'
          : d
            ? `Done: ${d.updated_policies} POL · ${d.updated_implementations} IMP`
            : 'Re-apply to documents'}
      </Button>
    </Tooltip>
  )
}

// ── Library browser drawer ────────────────────────────────────────────────────
function LibraryBrowserDrawer({
  open, onClose, projectId, mode, onAdded,
}: {
  open: boolean
  onClose: () => void
  projectId: string
  mode: 'policies' | 'implementations'
  onAdded: () => void
}) {
  const qc = useQueryClient()
  const [search, setSearch] = useState('')
  const [typeFilter, setTypeFilter] = useState<string>('ALL')
  const [langFilter, setLangFilter] = useState<string>('ALL')
  const [selected, setSelected] = useState<Set<string>>(new Set())
  const [importing, setImporting] = useState(false)

  // Reset selection when drawer opens/mode changes
  useEffect(() => { setSelected(new Set()); setSearch(''); setTypeFilter('ALL'); setLangFilter('ALL') }, [open, mode])

  const { data: libPolicies } = useQuery({
    queryKey: ['library', 'policies', projectId, langFilter],
    queryFn: () => projectsApi.libraryPolicies(projectId, langFilter !== 'ALL' ? { language: langFilter } : undefined),
    enabled: open && mode === 'policies',
  })

  const { data: libImpls } = useQuery({
    queryKey: ['library', 'implementations', projectId],
    queryFn: () => projectsApi.libraryImpls(projectId),
    enabled: open && mode === 'implementations',
  })

  const addPolicyMutation = useMutation({
    mutationFn: (id: string) => projectsApi.addPolicy(projectId, { lib_policy_id: id }),
  })
  const addImplMutation = useMutation({
    mutationFn: (id: string) => projectsApi.addImpl(projectId, { lib_impl_id: id }),
  })

  const policyTypes = useMemo(() => {
    if (!libPolicies) return []
    return ['ALL', ...Array.from(new Set(libPolicies.map(p => p.policy_type)))]
  }, [libPolicies])

  const implTypes = ['ALL', 'UG', 'TG']
  const typeOptions = mode === 'policies' ? policyTypes : implTypes

  const filteredPolicies = useMemo(() => {
    if (!libPolicies) return []
    return libPolicies.filter(p => {
      const q = search.toLowerCase()
      const matchSearch = !search || p.document_id.toLowerCase().includes(q) || p.title.toLowerCase().includes(q) || p.control_group_code.toLowerCase().includes(q)
      return matchSearch && (typeFilter === 'ALL' || p.policy_type === typeFilter)
    })
  }, [libPolicies, search, typeFilter])

  const filteredImpls = useMemo(() => {
    if (!libImpls) return []
    return libImpls.filter(i => {
      const q = search.toLowerCase()
      const matchSearch = !search || i.document_id.toLowerCase().includes(q) || i.title.toLowerCase().includes(q) || i.control_group_code.toLowerCase().includes(q)
      return matchSearch && (typeFilter === 'ALL' || i.impl_type === typeFilter)
    })
  }, [libImpls, search, typeFilter])

  // Rows available for selection (not already added)
  const availableIds = useMemo(() => {
    const rows = mode === 'policies' ? filteredPolicies : filteredImpls
    return rows.filter((r: any) => !r.already_in_project).map((r: any) => r.id as string)
  }, [mode, filteredPolicies, filteredImpls])

  const allFilteredSelected = availableIds.length > 0 && availableIds.every(id => selected.has(id))
  const someSelected = availableIds.some(id => selected.has(id))

  function toggleSelectAll() {
    if (allFilteredSelected) {
      setSelected(s => { const n = new Set(s); availableIds.forEach(id => n.delete(id)); return n })
    } else {
      setSelected(s => new Set([...s, ...availableIds]))
    }
  }

  function toggleRow(id: string) {
    setSelected(s => { const n = new Set(s); n.has(id) ? n.delete(id) : n.add(id); return n })
  }

  async function handleImportSelected() {
    const ids = [...selected]
    if (!ids.length) return
    setImporting(true)
    try {
      for (const id of ids) {
        if (mode === 'policies') await addPolicyMutation.mutateAsync(id)
        else await addImplMutation.mutateAsync(id)
      }
      qc.invalidateQueries({ queryKey: [mode === 'policies' ? 'project-policies' : 'project-impls', projectId] })
      qc.invalidateQueries({ queryKey: ['project', projectId] })
      qc.invalidateQueries({ queryKey: ['library', mode === 'policies' ? 'policies' : 'implementations', projectId] })
      setSelected(new Set())
      onAdded()
      onClose()
    } finally {
      setImporting(false)
    }
  }

  const rows = mode === 'policies' ? filteredPolicies : filteredImpls

  return (
    <Drawer anchor="right" open={open} onClose={onClose} PaperProps={{ sx: { width: { xs: '100vw', md: 820 }, display: 'flex', flexDirection: 'column' } }}>
      {/* Header */}
      <Box sx={{ px: 3, py: 2, borderBottom: '1px solid', borderColor: 'divider', display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexShrink: 0 }}>
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
          <LibraryBooksOutlined sx={{ fontSize: 20, color: 'text.secondary' }} />
          <Box>
            <Typography variant="subtitle1" sx={{ fontWeight: 700, lineHeight: 1.2 }}>
              Library — {mode === 'policies' ? 'Policies' : 'Implementations'}
            </Typography>
            <Typography variant="caption" color="text.secondary">
              Select documents to import into this project
            </Typography>
          </Box>
        </Box>
        <IconButton size="small" onClick={onClose}><CloseOutlined fontSize="small" /></IconButton>
      </Box>

      {/* Filters */}
      <Box sx={{ px: 3, pt: 2, pb: 1.5, flexShrink: 0 }}>
        <TextField
          fullWidth size="small"
          placeholder="Search by code, title, control group…"
          value={search}
          onChange={e => setSearch(e.target.value)}
          InputProps={{ startAdornment: <InputAdornment position="start"><SearchOutlined sx={{ fontSize: 18, color: 'text.disabled' }} /></InputAdornment> }}
          sx={{ mb: 1.5 }}
        />
        <Box sx={{ display: 'flex', gap: 0.5, flexWrap: 'wrap', mb: mode === 'policies' ? 0.75 : 0 }}>
          {typeOptions.map(t => {
            const active = typeFilter === t
            return (
              <Chip key={t} label={t} size="small" onClick={() => setTypeFilter(t)}
                sx={{ height: 22, fontSize: '0.67rem', cursor: 'pointer', bgcolor: active ? 'primary.main' : 'transparent', color: active ? '#fff' : 'text.secondary', border: '1px solid', borderColor: active ? 'primary.main' : 'divider' }}
              />
            )
          })}
        </Box>
        {mode === 'policies' && (
          <Box sx={{ display: 'flex', gap: 0.5, alignItems: 'center' }}>
            <Typography variant="caption" color="text.disabled" sx={{ fontSize: '0.65rem', mr: 0.25 }}>Lang:</Typography>
            {(['ALL', 'EN', 'DE', 'FR', 'IT'] as const).map(l => {
              const active = langFilter === l
              return (
                <Chip key={l} label={l} size="small" onClick={() => setLangFilter(l)}
                  sx={{ height: 20, fontSize: '0.65rem', cursor: 'pointer', bgcolor: active ? 'secondary.main' : 'transparent', color: active ? '#fff' : 'text.secondary', border: '1px solid', borderColor: active ? 'secondary.main' : 'divider' }}
                />
              )
            })}
          </Box>
        )}
      </Box>

      <Divider />

      {/* Table */}
      <Box sx={{ flex: 1, overflowY: 'auto' }}>
        <TableContainer>
          <Table size="small" stickyHeader>
            <TableHead>
              <TableRow>
                <TableCell padding="checkbox" sx={{ py: 0.75 }}>
                  <Checkbox
                    size="small"
                    indeterminate={someSelected && !allFilteredSelected}
                    checked={allFilteredSelected}
                    onChange={toggleSelectAll}
                    disabled={availableIds.length === 0}
                  />
                </TableCell>
                <TableCell sx={{ fontSize: '0.69rem', py: 0.75 }}>Document ID</TableCell>
                <TableCell sx={{ fontSize: '0.69rem', py: 0.75 }}>Title</TableCell>
                <TableCell sx={{ fontSize: '0.69rem', py: 0.75 }}>Type</TableCell>
                <TableCell sx={{ fontSize: '0.69rem', py: 0.75 }}>Control Group</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {rows.map((r: any) => {
                const isAdded = r.already_in_project
                const isChecked = selected.has(r.id)
                return (
                  <TableRow
                    key={r.id}
                    hover={!isAdded}
                    selected={isChecked}
                    onClick={() => !isAdded && toggleRow(r.id)}
                    sx={{ cursor: isAdded ? 'default' : 'pointer', opacity: isAdded ? 0.5 : 1 }}
                  >
                    <TableCell padding="checkbox">
                      {isAdded ? (
                        <CheckCircleOutlined sx={{ fontSize: 16, color: '#4CAF50', ml: 1.5 }} />
                      ) : (
                        <Checkbox size="small" checked={isChecked} onChange={() => toggleRow(r.id)} onClick={e => e.stopPropagation()} />
                      )}
                    </TableCell>
                    <TableCell sx={{ fontSize: '0.72rem', py: 0.6, fontFamily: 'monospace' }}>
                      <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.5 }}>
                        {r.is_stacked && (
                          <Tooltip title="Stacked control — structure locked">
                            <LockOutlined sx={{ fontSize: 12, color: 'warning.main' }} />
                          </Tooltip>
                        )}
                        {r.document_id}
                      </Box>
                    </TableCell>
                    <TableCell sx={{ fontSize: '0.72rem', py: 0.6 }}>
                      <Typography variant="caption" sx={{ fontSize: '0.72rem', display: 'block', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap', maxWidth: 260 }}>
                        {r.title}
                      </Typography>
                    </TableCell>
                    <TableCell sx={{ py: 0.6 }}>
                      {mode === 'policies' ? (
                        <Chip label={r.policy_type} size="small" sx={{ height: 18, fontSize: '0.62rem', bgcolor: `${POL_TYPE_COLOR[r.policy_type] ?? '#9E9E9E'}20`, color: POL_TYPE_COLOR[r.policy_type] ?? '#9E9E9E' }} />
                      ) : (
                        <Chip label={r.impl_type} size="small" sx={{ height: 18, fontSize: '0.62rem', bgcolor: `${IMPL_TYPE_COLOR[r.impl_type] ?? '#9E9E9E'}20`, color: IMPL_TYPE_COLOR[r.impl_type] ?? '#9E9E9E' }} />
                      )}
                    </TableCell>
                    <TableCell sx={{ fontSize: '0.72rem', py: 0.6 }}>{r.control_group_code}</TableCell>
                  </TableRow>
                )
              })}
            </TableBody>
          </Table>
        </TableContainer>
      </Box>

      {/* Sticky footer */}
      <Box sx={{ px: 3, py: 1.5, borderTop: '1px solid', borderColor: 'divider', display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexShrink: 0 }}>
        <Typography variant="caption" color="text.secondary">
          {selected.size > 0 ? `${selected.size} selected` : `${availableIds.length} available`}
        </Typography>
        <Box sx={{ display: 'flex', gap: 1 }}>
          <Button size="small" variant="outlined" disabled={availableIds.length === 0 || importing}
            onClick={() => { setSelected(new Set(availableIds)) }}>
            Select all ({availableIds.length})
          </Button>
          <Button size="small" variant="contained" disabled={selected.size === 0 || importing}
            onClick={handleImportSelected}
            startIcon={importing ? <CircularProgress size={14} color="inherit" /> : undefined}
          >
            {importing ? 'Importing…' : `Import selected (${selected.size})`}
          </Button>
        </Box>
      </Box>
    </Drawer>
  )
}

// ── Document editor drawer ────────────────────────────────────────────────────
const EDITOR_STYLES = `
  .ProseMirror {
    outline: none;
    min-height: 100%;
    font-size: 0.82rem;
    line-height: 1.6;
    color: rgba(255,255,255,0.87);
  }
  .ProseMirror h1 { font-size: 1.25rem; font-weight: 700; margin: 1.2em 0 0.5em; }
  .ProseMirror h2 { font-size: 1.05rem; font-weight: 700; margin: 1em 0 0.4em; }
  .ProseMirror h3 { font-size: 0.92rem; font-weight: 700; margin: 0.8em 0 0.3em; }
  .ProseMirror p { margin: 0.4em 0; }
  .ProseMirror ul, .ProseMirror ol { padding-left: 1.4em; margin: 0.4em 0; }
  .ProseMirror li { margin: 0.15em 0; }
  .ProseMirror strong { font-weight: 700; }
  .ProseMirror em { font-style: italic; }
  .ProseMirror code { background: rgba(255,255,255,0.08); border-radius: 3px; padding: 0.1em 0.3em; font-family: monospace; font-size: 0.85em; }
  .ProseMirror pre { background: rgba(255,255,255,0.06); border-radius: 6px; padding: 0.8em 1em; overflow-x: auto; margin: 0.6em 0; }
  .ProseMirror pre code { background: none; padding: 0; }
  .ProseMirror blockquote { border-left: 3px solid rgba(255,255,255,0.2); padding-left: 1em; color: rgba(255,255,255,0.55); margin: 0.5em 0; }
  .ProseMirror hr { border: none; border-top: 1px solid rgba(255,255,255,0.12); margin: 1em 0; }
  .ProseMirror table { border-collapse: collapse; width: 100%; margin: 0.6em 0; font-size: 0.8rem; }
  .ProseMirror th, .ProseMirror td { border: 1px solid rgba(255,255,255,0.15); padding: 0.3em 0.6em; text-align: left; }
  .ProseMirror th { background: rgba(255,255,255,0.05); font-weight: 600; }
  .ProseMirror .selectedCell:after { background: rgba(68,114,196,0.15); }
  .ProseMirror p.is-editor-empty:first-child::before { content: attr(data-placeholder); color: rgba(255,255,255,0.25); pointer-events: none; float: left; height: 0; }
`

function ToolbarBtn({
  active, onClick, children, title,
}: { active?: boolean; onClick: () => void; children: React.ReactNode; title: string }) {
  return (
    <Tooltip title={title}>
      <IconButton
        size="small"
        onClick={onClick}
        sx={{
          p: 0.4, borderRadius: 0.75, fontSize: 13,
          color: active ? '#4472C4' : 'text.secondary',
          bgcolor: active ? '#4472C418' : 'transparent',
          '&:hover': { color: 'text.primary', bgcolor: 'rgba(255,255,255,0.06)' },
        }}
      >
        {children}
      </IconButton>
    </Tooltip>
  )
}

/**
 * Convert RST/Pandoc grid tables to GFM pipe tables so TipTap can render them.
 * Grid tables use +---+ separators and support multi-line cells; GFM doesn't.
 * Multi-line cell content is merged into a single line with space separation.
 */
function convertGridTables(md: string): string {
  const lines = md.split('\n')
  const result: string[] = []
  let i = 0

  while (i < lines.length) {
    const line = lines[i]

    if (/^\+[-=+]+\+/.test(line)) {
      // Collect all lines belonging to this grid table
      const tableLines: string[] = []
      while (i < lines.length && /^\+[-=+]+\+|^\|/.test(lines[i])) {
        tableLines.push(lines[i])
        i++
      }

      // Parse grid table rows (merging multi-line cells)
      const rows: string[][] = []
      let headerIdx = 0
      let currentRow: string[] | null = null

      for (const tl of tableLines) {
        if (/^\+[=+]+\+/.test(tl)) {
          // Header separator (+=====+)
          if (currentRow) { rows.push(currentRow); headerIdx = rows.length - 1; currentRow = null }
        } else if (/^\+[-+]+\+/.test(tl)) {
          // Row separator (+-----+)
          if (currentRow) { rows.push(currentRow); currentRow = null }
        } else if (tl.startsWith('|')) {
          const cells = tl.split('|').slice(1, -1).map(c => c.trim())
          if (currentRow === null) {
            currentRow = cells
          } else {
            // Continuation line — merge non-empty content into existing cells
            for (let c = 0; c < Math.min(cells.length, currentRow.length); c++) {
              if (cells[c]) currentRow[c] = currentRow[c] ? currentRow[c] + ' ' + cells[c] : cells[c]
            }
          }
        }
      }
      if (currentRow) rows.push(currentRow)

      if (rows.length === 0) continue

      const maxCols = Math.max(...rows.map(r => r.length))
      // Output header row
      result.push('| ' + rows[headerIdx].join(' | ') + ' |')
      result.push('| ' + Array(maxCols).fill('---').join(' | ') + ' |')
      // Output data rows
      for (let r = 0; r < rows.length; r++) {
        if (r === headerIdx) continue
        // Pad to maxCols if needed
        const row = [...rows[r]]
        while (row.length < maxCols) row.push('')
        result.push('| ' + row.join(' | ') + ' |')
      }
      result.push('')
    } else {
      result.push(line)
      i++
    }
  }

  return result.join('\n')
}

function DocEditorDrawer({
  open, onClose, projectId, docId, mode, title: docTitle, docType,
}: {
  open: boolean
  onClose: () => void
  projectId: string
  docId: string
  mode: 'policy' | 'implementation'
  title: string | null
  docType: string | null
}) {
  const qc = useQueryClient()
  const [sourceMode, setSourceMode] = useState(false)
  const [sourceContent, setSourceContent] = useState('')
  const [dirty, setDirty] = useState(false)
  const [saved, setSaved] = useState(false)

  const { data: doc, isLoading } = useQuery({
    queryKey: ['project-doc', projectId, docId, mode],
    queryFn: () => mode === 'policy'
      ? projectsApi.getPolicy(projectId, docId)
      : projectsApi.getImpl(projectId, docId),
    enabled: open && !!docId,
  })

  const editor = useEditor({
    extensions: [
      StarterKit,
      Markdown.configure({ html: false, tightLists: true }),
      TiptapTable.configure({ resizable: false }),
      TiptapTableRow,
      TiptapTableHeader,
      TiptapTableCell,
    ],
    content: '',
    onUpdate: () => setDirty(true),
  })

  // Populate editor when content loads
  useEffect(() => {
    if (editor && doc?.custom_content != null && !editor.isDestroyed) {
      const clean = convertGridTables(
        doc.custom_content
          .replace(/^<!--\s*ISMS-CORE:[^\n]*-->\s*\n?/m, '')
          .replace(/\n?<!--\s*QA_VERIFIED:[^\n]*-->\s*$/m, '')
          .trimStart()
      )
      editor.commands.setContent(clean)
      setSourceContent(clean)
      setDirty(false)
      setSaved(false)
    }
  }, [doc?.custom_content, editor])

  // Reset on close
  useEffect(() => {
    if (!open) {
      setSourceMode(false)
      setDirty(false)
      setSaved(false)
    }
  }, [open])

  const toggleSource = useCallback(() => {
    if (!sourceMode && editor && !editor.isDestroyed) {
      setSourceContent(editor.storage.markdown.getMarkdown())
    } else if (sourceMode && editor && !editor.isDestroyed) {
      editor.commands.setContent(sourceContent)
    }
    setSourceMode(v => !v)
    setDirty(true)
  }, [sourceMode, editor, sourceContent])

  const saveMutation = useMutation({
    mutationFn: (content: string) => mode === 'policy'
      ? projectsApi.updatePolicy(projectId, docId, { custom_content: content })
      : projectsApi.updateImpl(projectId, docId, { custom_content: content }),
    onSuccess: () => {
      qc.invalidateQueries({ queryKey: [mode === 'policy' ? 'project-policies' : 'project-impls', projectId] })
      setSaved(true)
      setDirty(false)
      setTimeout(() => setSaved(false), 3000)
    },
  })

  function handleSave() {
    const content = sourceMode
      ? sourceContent
      : (editor && !editor.isDestroyed ? editor.storage.markdown.getMarkdown() : '')
    saveMutation.mutate(content)
  }

  const typeColor = mode === 'policy' ? (POL_TYPE_COLOR[docType ?? ''] ?? '#4472C4') : (IMPL_TYPE_COLOR[docType ?? ''] ?? '#9E9E9E')

  return (
    <Drawer
      anchor="right"
      open={open}
      onClose={onClose}
      PaperProps={{ sx: { width: { xs: '100vw', md: 1200 }, bgcolor: '#1a1a2e', display: 'flex', flexDirection: 'column' } }}
    >
      <style>{EDITOR_STYLES}</style>

      {/* Header */}
      <Box sx={{ px: 2.5, py: 1.5, borderBottom: '1px solid', borderColor: 'divider', display: 'flex', alignItems: 'center', gap: 1.5, flexShrink: 0 }}>
        <Box sx={{ flex: 1, minWidth: 0 }}>
          <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 0.25 }}>
            {docType && (
              <Chip label={docType} size="small" sx={{ height: 18, fontSize: '0.6rem', bgcolor: `${typeColor}18`, color: typeColor }} />
            )}
            {dirty && !saved && (
              <Chip label="Unsaved" size="small" sx={{ height: 18, fontSize: '0.6rem', bgcolor: '#FF980018', color: '#FF9800' }} />
            )}
            {saved && (
              <Chip label="Saved" size="small" sx={{ height: 18, fontSize: '0.6rem', bgcolor: '#4CAF5018', color: '#4CAF50' }} />
            )}
          </Box>
          <Typography variant="subtitle2" sx={{ fontWeight: 700, fontSize: '0.88rem', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
            {docTitle ?? 'Untitled'}
          </Typography>
        </Box>
        <Button
          size="small"
          variant={saved ? 'outlined' : 'contained'}
          color={saved ? 'success' : 'primary'}
          startIcon={<SaveOutlined sx={{ fontSize: 14 }} />}
          onClick={handleSave}
          disabled={saveMutation.isPending || (!dirty && !saved)}
          sx={{ fontSize: '0.72rem', flexShrink: 0 }}
        >
          {saveMutation.isPending ? 'Saving…' : saved ? 'Saved' : 'Save'}
        </Button>
        <IconButton size="small" onClick={onClose} sx={{ color: 'text.secondary' }}>
          <CloseOutlined fontSize="small" />
        </IconButton>
      </Box>

      {/* Toolbar */}
      <Box sx={{ px: 1.5, py: 0.75, borderBottom: '1px solid', borderColor: 'divider', display: 'flex', alignItems: 'center', gap: 0.25, flexWrap: 'wrap', flexShrink: 0 }}>
        {!sourceMode && editor && (
          <>
            <ToolbarBtn title="Bold (Ctrl+B)" active={editor.isActive('bold')} onClick={() => editor.chain().focus().toggleBold().run()}>
              <FormatBoldOutlined sx={{ fontSize: 18 }} />
            </ToolbarBtn>
            <ToolbarBtn title="Italic (Ctrl+I)" active={editor.isActive('italic')} onClick={() => editor.chain().focus().toggleItalic().run()}>
              <FormatItalicOutlined sx={{ fontSize: 18 }} />
            </ToolbarBtn>
            <Divider orientation="vertical" flexItem sx={{ mx: 0.5, my: 0.25 }} />
            {([1, 2, 3] as const).map(level => (
              <ToolbarBtn key={level} title={`Heading ${level}`} active={editor.isActive('heading', { level })} onClick={() => editor.chain().focus().toggleHeading({ level }).run()}>
                <Typography sx={{ fontSize: '0.72rem', fontWeight: 700, lineHeight: 1, px: 0.25 }}>H{level}</Typography>
              </ToolbarBtn>
            ))}
            <Divider orientation="vertical" flexItem sx={{ mx: 0.5, my: 0.25 }} />
            <ToolbarBtn title="Bullet list" active={editor.isActive('bulletList')} onClick={() => editor.chain().focus().toggleBulletList().run()}>
              <FormatListBulletedOutlined sx={{ fontSize: 18 }} />
            </ToolbarBtn>
            <ToolbarBtn title="Ordered list" active={editor.isActive('orderedList')} onClick={() => editor.chain().focus().toggleOrderedList().run()}>
              <FormatListNumberedOutlined sx={{ fontSize: 18 }} />
            </ToolbarBtn>
            <Divider orientation="vertical" flexItem sx={{ mx: 0.5, my: 0.25 }} />
            <ToolbarBtn title="Inline code" active={editor.isActive('code')} onClick={() => editor.chain().focus().toggleCode().run()}>
              <CodeOutlined sx={{ fontSize: 18 }} />
            </ToolbarBtn>
            <ToolbarBtn title="Horizontal rule" active={false} onClick={() => editor.chain().focus().setHorizontalRule().run()}>
              <HorizontalRuleOutlined sx={{ fontSize: 18 }} />
            </ToolbarBtn>
          </>
        )}
        <Box sx={{ flex: 1 }} />
        <Button
          size="small"
          variant={sourceMode ? 'contained' : 'outlined'}
          onClick={toggleSource}
          sx={{ fontSize: '0.68rem', py: 0.25, px: 1, minWidth: 0, fontFamily: 'monospace' }}
        >
          {sourceMode ? 'WYSIWYG' : 'Source'}
        </Button>
      </Box>

      {/* Editor body */}
      <Box sx={{ flex: 1, overflow: 'auto', px: 3, py: 2 }}>
        {isLoading ? (
          <Box sx={{ pt: 4 }}>
            {[...Array(8)].map((_, i) => <Skeleton key={i} variant="text" sx={{ mb: 0.5, width: i % 3 === 0 ? '60%' : '100%' }} />)}
          </Box>
        ) : sourceMode ? (
          <TextField
            multiline
            fullWidth
            value={sourceContent}
            onChange={e => { setSourceContent(e.target.value); setDirty(true) }}
            variant="outlined"
            InputProps={{
              sx: {
                fontFamily: 'monospace',
                fontSize: '0.78rem',
                lineHeight: 1.6,
                alignItems: 'flex-start',
                '& textarea': { resize: 'none' },
              },
            }}
            minRows={30}
          />
        ) : (
          <Box sx={{ '& .ProseMirror': { minHeight: 600 } }}>
            <EditorContent editor={editor} />
          </Box>
        )}
      </Box>
    </Drawer>
  )
}

// ── Policies tab ──────────────────────────────────────────────────────────────
function PoliciesTab({ projectId, productFamily }: { projectId: string; productFamily: string }) {
  const qc = useQueryClient()
  const { user } = useAuth()
  const canDelete = CAN_DELETE_ROLES.has(user?.role ?? '')
  const [drawerOpen, setDrawerOpen] = useState(false)
  const [search, setSearch] = useState('')
  const [viewFilter, setViewFilter] = useState<'active' | 'archived'>('active')
  const [selected, setSelected] = useState<Set<string>>(new Set())
  const [editorDoc, setEditorDoc] = useState<{ id: string; title: string | null; docType: string | null } | null>(null)
  const [sortCol, setSortCol] = useState<'document_id' | 'title' | 'policy_type' | 'control_group_code'>('document_id')
  const [sortDir, setSortDir] = useState<'asc' | 'desc'>('asc')

  function handleSort(col: typeof sortCol) {
    if (col === sortCol) setSortDir(d => d === 'asc' ? 'desc' : 'asc')
    else { setSortCol(col); setSortDir('asc') }
  }

  const { data: policies, isLoading } = useQuery({
    queryKey: ['project-policies', projectId],
    queryFn: () => projectsApi.listPolicies(projectId),
  })

  const invalidate = () => {
    qc.invalidateQueries({ queryKey: ['project-policies', projectId] })
    qc.invalidateQueries({ queryKey: ['project', projectId] })
    qc.invalidateQueries({ queryKey: ['library', 'policies', projectId] })
    setSelected(new Set())
  }

  const softDeleteMutation = useMutation({
    mutationFn: (ids: string[]) => Promise.all(ids.map(id => projectsApi.updatePolicy(projectId, id, { status: 'archived' }))),
    onSuccess: invalidate,
  })
  const restoreMutation = useMutation({
    mutationFn: (ids: string[]) => Promise.all(ids.map(id => projectsApi.updatePolicy(projectId, id, { status: 'active' }))),
    onSuccess: invalidate,
  })
  const hardDeleteMutation = useMutation({
    mutationFn: (ids: string[]) => Promise.all(ids.map(id => projectsApi.removePolicy(projectId, id))),
    onSuccess: invalidate,
  })

  const activeAll = useMemo(() => policies?.filter(p => p.status !== 'archived') ?? [], [policies])
  const removedAll = useMemo(() => policies?.filter(p => p.status === 'archived') ?? [], [policies])

  const displayed = useMemo(() => {
    const base = viewFilter === 'active' ? activeAll : removedAll
    const filtered = !search ? base : (() => {
      const q = search.toLowerCase()
      return base.filter(p =>
        (p.document_id ?? '').toLowerCase().includes(q) ||
        (p.title ?? '').toLowerCase().includes(q) ||
        (p.control_group_code ?? '').toLowerCase().includes(q)
      )
    })()
    return [...filtered].sort((a, b) => {
      const av = (a[sortCol] ?? '').toLowerCase()
      const bv = (b[sortCol] ?? '').toLowerCase()
      return sortDir === 'asc' ? av.localeCompare(bv) : bv.localeCompare(av)
    })
  }, [viewFilter, activeAll, removedAll, search, sortCol, sortDir])

  const displayedIds = useMemo(() => displayed.map(p => p.id), [displayed])
  const allChecked = displayedIds.length > 0 && displayedIds.every(id => selected.has(id))
  const someChecked = displayedIds.some(id => selected.has(id))

  function toggleRow(id: string) {
    setSelected(prev => { const s = new Set(prev); s.has(id) ? s.delete(id) : s.add(id); return s })
  }
  function toggleAll() {
    if (allChecked) setSelected(new Set())
    else setSelected(new Set(displayedIds))
  }

  const selectedIds = [...selected]
  const isBusy = softDeleteMutation.isPending || restoreMutation.isPending || hardDeleteMutation.isPending

  const SH = ({ col, label }: { col: typeof sortCol; label: string }) => (
    <TableCell sortDirection={sortCol === col ? sortDir : false} sx={{ fontSize: '0.69rem', py: 0.75 }}>
      <TableSortLabel active={sortCol === col} direction={sortCol === col ? sortDir : 'asc'} onClick={() => handleSort(col)}
        sx={{ fontSize: '0.69rem', '& .MuiTableSortLabel-icon': { fontSize: 12 } }}>
        {label}
      </TableSortLabel>
    </TableCell>
  )

  const tableHead = (
    <TableHead>
      <TableRow>
        <TableCell padding="checkbox" sx={{ py: 0.5, pl: 1.5 }}>
          <Checkbox size="small" checked={allChecked} indeterminate={!allChecked && someChecked} onChange={toggleAll} />
        </TableCell>
        <SH col="document_id" label="Document ID" />
        <SH col="title" label="Title" />
        <SH col="policy_type" label="Type" />
        <SH col="control_group_code" label="Control Group" />
        <TableCell sx={{ fontSize: '0.69rem', py: 0.75 }}>Flags</TableCell>
        <TableCell sx={{ width: 60 }} />
      </TableRow>
    </TableHead>
  )

  return (
    <Box>
      {/* Toolbar */}
      <Box sx={{ display: 'flex', alignItems: 'center', gap: 1.5, mb: 1.5, flexWrap: 'wrap' }}>
        <TextField
          size="small" placeholder="Search policies…" value={search}
          onChange={e => setSearch(e.target.value)}
          InputProps={{ startAdornment: <InputAdornment position="start"><SearchOutlined sx={{ fontSize: 16, color: 'text.disabled' }} /></InputAdornment> }}
          sx={{ flex: 1, maxWidth: 300 }}
        />
        {/* View filter chips */}
        <Box sx={{ display: 'flex', gap: 0.75 }}>
          <Chip
            label={`Active (${activeAll.length})`} size="small" clickable
            onClick={() => { setViewFilter('active'); setSelected(new Set()) }}
            sx={{ fontSize: '0.7rem', bgcolor: viewFilter === 'active' ? 'primary.main' : undefined, color: viewFilter === 'active' ? 'primary.contrastText' : undefined }}
          />
          <Chip
            label={`Bin (${removedAll.length})`} size="small" clickable
            icon={<RestoreFromTrashOutlined sx={{ fontSize: 13, ml: 0.5 }} />}
            onClick={() => { setViewFilter('archived'); setSelected(new Set()) }}
            sx={{ fontSize: '0.7rem', bgcolor: viewFilter === 'archived' ? 'warning.main' : undefined, color: viewFilter === 'archived' ? '#fff' : undefined }}
          />
        </Box>
        <Button variant="outlined" size="small" startIcon={<LibraryBooksOutlined />} onClick={() => setDrawerOpen(true)} sx={{ ml: 'auto' }}>
          Add from Library
        </Button>
      </Box>

      {/* Bulk action bar */}
      {selectedIds.length > 0 && (
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, px: 1.5, py: 0.75, mb: 1, bgcolor: 'action.selected', borderRadius: 1, border: '1px solid', borderColor: 'divider' }}>
          <Typography variant="caption" sx={{ fontWeight: 600, mr: 1 }}>{selectedIds.length} selected</Typography>
          {viewFilter === 'active' ? (
            <Button size="small" color="warning" variant="outlined" disabled={isBusy}
              onClick={() => softDeleteMutation.mutate(selectedIds)}
              sx={{ py: 0, px: 1.2, fontSize: '0.7rem', height: 24 }}>
              Move to Bin
            </Button>
          ) : (
            <Button size="small" color="success" variant="outlined" disabled={isBusy}
              onClick={() => restoreMutation.mutate(selectedIds)}
              sx={{ py: 0, px: 1.2, fontSize: '0.7rem', height: 24 }}>
              Restore
            </Button>
          )}
          {canDelete && (
            <Button size="small" color="error" variant="outlined" disabled={isBusy}
              onClick={() => hardDeleteMutation.mutate(selectedIds)}
              sx={{ py: 0, px: 1.2, fontSize: '0.7rem', height: 24 }}>
              Delete permanently
            </Button>
          )}
          <Button size="small" onClick={() => setSelected(new Set())} sx={{ ml: 'auto', py: 0, px: 1, fontSize: '0.7rem', height: 24 }}>
            Clear
          </Button>
        </Box>
      )}

      {isLoading ? (
        <Box sx={{ py: 4, textAlign: 'center' }}><CircularProgress size={24} /></Box>
      ) : !displayed.length ? (
        <Box sx={{ py: 6, textAlign: 'center' }}>
          <PolicyOutlined sx={{ fontSize: 40, color: 'text.disabled', mb: 1 }} />
          <Typography variant="body2" color="text.secondary">
            {viewFilter === 'archived' ? 'Bin is empty' : (activeAll.length ? 'No matching policies' : 'No policies added yet — click "Add from Library" to start')}
          </Typography>
        </Box>
      ) : (
        <TableContainer sx={{ opacity: viewFilter === 'archived' ? 0.85 : 1 }}>
          <Table size="small">
            {tableHead}
            <TableBody>
              {displayed.map(p => (
                <TableRow key={p.id} hover
                  onClick={() => viewFilter === 'active' && setEditorDoc({ id: p.id, title: p.title, docType: p.policy_type })}
                  sx={{ cursor: viewFilter === 'active' ? 'pointer' : 'default' }}
                >
                  <TableCell padding="checkbox" sx={{ pl: 1.5 }} onClick={e => { e.stopPropagation(); toggleRow(p.id) }}>
                    <Checkbox size="small" checked={selected.has(p.id)} onChange={() => {}} />
                  </TableCell>
                  <TableCell sx={{ fontSize: '0.72rem', py: 0.6, fontFamily: 'monospace' }}>
                    {p.document_id ?? <Typography component="span" variant="caption" color="text.disabled">Custom</Typography>}
                  </TableCell>
                  <TableCell sx={{ fontSize: '0.72rem', py: 0.6, maxWidth: 220 }}>
                    <Typography variant="caption" sx={{ fontSize: '0.72rem', display: 'block', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap', textDecoration: viewFilter === 'archived' ? 'line-through' : 'none' }}>
                      {p.title ?? '—'}
                    </Typography>
                  </TableCell>
                  <TableCell sx={{ py: 0.6 }}>
                    {p.policy_type && (
                      <Chip label={p.policy_type} size="small" sx={{ height: 18, fontSize: '0.62rem', bgcolor: `${POL_TYPE_COLOR[p.policy_type] ?? '#9E9E9E'}20`, color: POL_TYPE_COLOR[p.policy_type] ?? '#9E9E9E' }} />
                    )}
                  </TableCell>
                  <TableCell sx={{ fontSize: '0.72rem', py: 0.6 }}>{p.control_group_code ?? '—'}</TableCell>
                  <TableCell sx={{ py: 0.6 }}>
                    <Box sx={{ display: 'flex', gap: 0.5 }}>
                      {p.stacking_locked && <Tooltip title="Stacked control — structure locked"><LockOutlined sx={{ fontSize: 14, color: 'warning.main' }} /></Tooltip>}
                      {p.is_edited && <Tooltip title="Edited — differs from Library version"><EditOutlined sx={{ fontSize: 14, color: '#4472C4' }} /></Tooltip>}
                      {p.stale_warning && <Tooltip title="Stale warning — IMP cross-references may no longer match this policy"><WarningAmberOutlined sx={{ fontSize: 14, color: '#FF9800' }} /></Tooltip>}
                    </Box>
                  </TableCell>
                  <TableCell align="right" sx={{ py: 0.6, width: 60 }} onClick={e => e.stopPropagation()}>
                    {viewFilter === 'active' ? (
                      <Tooltip title="Edit document">
                        <IconButton size="small" sx={{ p: 0.4, color: 'text.disabled', '&:hover': { color: 'primary.main' } }}
                          onClick={() => setEditorDoc({ id: p.id, title: p.title, docType: p.policy_type })}>
                          <EditOutlined sx={{ fontSize: 15 }} />
                        </IconButton>
                      </Tooltip>
                    ) : (
                      <Tooltip title="Restore">
                        <IconButton size="small" sx={{ p: 0.4, color: 'text.disabled', '&:hover': { color: 'success.main' } }}
                          onClick={() => restoreMutation.mutate([p.id])}>
                          <RestoreFromTrashOutlined sx={{ fontSize: 15 }} />
                        </IconButton>
                      </Tooltip>
                    )}
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      )}

      <LibraryBrowserDrawer
        open={drawerOpen} onClose={() => setDrawerOpen(false)}
        projectId={projectId} mode="policies"
        onAdded={() => {}}
      />
      {editorDoc && (
        <DocEditorDrawer
          open={!!editorDoc}
          onClose={() => setEditorDoc(null)}
          projectId={projectId}
          docId={editorDoc.id}
          mode="policy"
          title={editorDoc.title}
          docType={editorDoc.docType}
        />
      )}
    </Box>
  )
}

// ── Implementations tab ───────────────────────────────────────────────────────
function ImplementationsTab({ projectId }: { projectId: string }) {
  const qc = useQueryClient()
  const { user } = useAuth()
  const canDelete = CAN_DELETE_ROLES.has(user?.role ?? '')
  const [drawerOpen, setDrawerOpen] = useState(false)
  const [search, setSearch] = useState('')
  const [viewFilter, setViewFilter] = useState<'active' | 'archived'>('active')
  const [selected, setSelected] = useState<Set<string>>(new Set())
  const [editorDoc, setEditorDoc] = useState<{ id: string; title: string | null; docType: string | null } | null>(null)
  const [sortCol, setSortCol] = useState<'document_id' | 'title' | 'impl_type' | 'control_group_code'>('document_id')
  const [sortDir, setSortDir] = useState<'asc' | 'desc'>('asc')

  function handleSort(col: typeof sortCol) {
    if (col === sortCol) setSortDir(d => d === 'asc' ? 'desc' : 'asc')
    else { setSortCol(col); setSortDir('asc') }
  }

  const { data: impls, isLoading } = useQuery({
    queryKey: ['project-impls', projectId],
    queryFn: () => projectsApi.listImpls(projectId),
  })

  const invalidate = () => {
    qc.invalidateQueries({ queryKey: ['project-impls', projectId] })
    qc.invalidateQueries({ queryKey: ['project', projectId] })
    qc.invalidateQueries({ queryKey: ['library', 'implementations', projectId] })
    setSelected(new Set())
  }

  const softDeleteMutation = useMutation({
    mutationFn: (ids: string[]) => Promise.all(ids.map(id => projectsApi.updateImpl(projectId, id, { status: 'archived' }))),
    onSuccess: invalidate,
  })
  const restoreMutation = useMutation({
    mutationFn: (ids: string[]) => Promise.all(ids.map(id => projectsApi.updateImpl(projectId, id, { status: 'active' }))),
    onSuccess: invalidate,
  })
  const hardDeleteMutation = useMutation({
    mutationFn: (ids: string[]) => Promise.all(ids.map(id => projectsApi.removeImpl(projectId, id))),
    onSuccess: invalidate,
  })

  const activeAll = useMemo(() => impls?.filter(i => i.status !== 'archived') ?? [], [impls])
  const removedAll = useMemo(() => impls?.filter(i => i.status === 'archived') ?? [], [impls])

  const displayed = useMemo(() => {
    const base = viewFilter === 'active' ? activeAll : removedAll
    const filtered = !search ? base : (() => {
      const q = search.toLowerCase()
      return base.filter(i =>
        (i.document_id ?? '').toLowerCase().includes(q) ||
        (i.title ?? '').toLowerCase().includes(q) ||
        (i.control_group_code ?? '').toLowerCase().includes(q)
      )
    })()
    return [...filtered].sort((a, b) => {
      const av = (a[sortCol] ?? '').toLowerCase()
      const bv = (b[sortCol] ?? '').toLowerCase()
      return sortDir === 'asc' ? av.localeCompare(bv) : bv.localeCompare(av)
    })
  }, [viewFilter, activeAll, removedAll, search, sortCol, sortDir])

  const displayedIds = useMemo(() => displayed.map(i => i.id), [displayed])
  const allChecked = displayedIds.length > 0 && displayedIds.every(id => selected.has(id))
  const someChecked = displayedIds.some(id => selected.has(id))

  function toggleRow(id: string) {
    setSelected(prev => { const s = new Set(prev); s.has(id) ? s.delete(id) : s.add(id); return s })
  }
  function toggleAll() {
    if (allChecked) setSelected(new Set())
    else setSelected(new Set(displayedIds))
  }

  const selectedIds = [...selected]
  const isBusy = softDeleteMutation.isPending || restoreMutation.isPending || hardDeleteMutation.isPending

  const SH = ({ col, label }: { col: typeof sortCol; label: string }) => (
    <TableCell sortDirection={sortCol === col ? sortDir : false} sx={{ fontSize: '0.69rem', py: 0.75 }}>
      <TableSortLabel active={sortCol === col} direction={sortCol === col ? sortDir : 'asc'} onClick={() => handleSort(col)}
        sx={{ fontSize: '0.69rem', '& .MuiTableSortLabel-icon': { fontSize: 12 } }}>
        {label}
      </TableSortLabel>
    </TableCell>
  )

  const tableHead = (
    <TableHead>
      <TableRow>
        <TableCell padding="checkbox" sx={{ py: 0.5, pl: 1.5 }}>
          <Checkbox size="small" checked={allChecked} indeterminate={!allChecked && someChecked} onChange={toggleAll} />
        </TableCell>
        <SH col="document_id" label="Document ID" />
        <SH col="title" label="Title" />
        <SH col="impl_type" label="Type" />
        <SH col="control_group_code" label="Control Group" />
        <TableCell sx={{ fontSize: '0.69rem', py: 0.75 }}>Flags</TableCell>
        <TableCell sx={{ width: 60 }} />
      </TableRow>
    </TableHead>
  )

  return (
    <Box>
      <Box sx={{ display: 'flex', alignItems: 'center', gap: 1.5, mb: 1.5, flexWrap: 'wrap' }}>
        <TextField size="small" placeholder="Search implementations…" value={search}
          onChange={e => setSearch(e.target.value)}
          InputProps={{ startAdornment: <InputAdornment position="start"><SearchOutlined sx={{ fontSize: 16, color: 'text.disabled' }} /></InputAdornment> }}
          sx={{ flex: 1, maxWidth: 300 }}
        />
        <Box sx={{ display: 'flex', gap: 0.75 }}>
          <Chip
            label={`Active (${activeAll.length})`} size="small" clickable
            onClick={() => { setViewFilter('active'); setSelected(new Set()) }}
            sx={{ fontSize: '0.7rem', bgcolor: viewFilter === 'active' ? 'primary.main' : undefined, color: viewFilter === 'active' ? 'primary.contrastText' : undefined }}
          />
          <Chip
            label={`Bin (${removedAll.length})`} size="small" clickable
            icon={<RestoreFromTrashOutlined sx={{ fontSize: 13, ml: 0.5 }} />}
            onClick={() => { setViewFilter('archived'); setSelected(new Set()) }}
            sx={{ fontSize: '0.7rem', bgcolor: viewFilter === 'archived' ? 'warning.main' : undefined, color: viewFilter === 'archived' ? '#fff' : undefined }}
          />
        </Box>
        <Button variant="outlined" size="small" startIcon={<LibraryBooksOutlined />} onClick={() => setDrawerOpen(true)} sx={{ ml: 'auto' }}>
          Add from Library
        </Button>
      </Box>

      {selectedIds.length > 0 && (
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, px: 1.5, py: 0.75, mb: 1, bgcolor: 'action.selected', borderRadius: 1, border: '1px solid', borderColor: 'divider' }}>
          <Typography variant="caption" sx={{ fontWeight: 600, mr: 1 }}>{selectedIds.length} selected</Typography>
          {viewFilter === 'active' ? (
            <Button size="small" color="warning" variant="outlined" disabled={isBusy}
              onClick={() => softDeleteMutation.mutate(selectedIds)}
              sx={{ py: 0, px: 1.2, fontSize: '0.7rem', height: 24 }}>
              Move to Bin
            </Button>
          ) : (
            <Button size="small" color="success" variant="outlined" disabled={isBusy}
              onClick={() => restoreMutation.mutate(selectedIds)}
              sx={{ py: 0, px: 1.2, fontSize: '0.7rem', height: 24 }}>
              Restore
            </Button>
          )}
          {canDelete && (
            <Button size="small" color="error" variant="outlined" disabled={isBusy}
              onClick={() => hardDeleteMutation.mutate(selectedIds)}
              sx={{ py: 0, px: 1.2, fontSize: '0.7rem', height: 24 }}>
              Delete permanently
            </Button>
          )}
          <Button size="small" onClick={() => setSelected(new Set())} sx={{ ml: 'auto', py: 0, px: 1, fontSize: '0.7rem', height: 24 }}>
            Clear
          </Button>
        </Box>
      )}

      {isLoading ? (
        <Box sx={{ py: 4, textAlign: 'center' }}><CircularProgress size={24} /></Box>
      ) : !displayed.length ? (
        <Box sx={{ py: 6, textAlign: 'center' }}>
          <ShieldOutlined sx={{ fontSize: 40, color: 'text.disabled', mb: 1 }} />
          <Typography variant="body2" color="text.secondary">
            {viewFilter === 'archived' ? 'Bin is empty' : (activeAll.length ? 'No matching implementations' : 'No implementations added yet — click "Add from Library" to start')}
          </Typography>
        </Box>
      ) : (
        <TableContainer sx={{ opacity: viewFilter === 'archived' ? 0.85 : 1 }}>
          <Table size="small">
            {tableHead}
            <TableBody>
              {displayed.map(i => (
                <TableRow key={i.id} hover
                  onClick={() => viewFilter === 'active' && setEditorDoc({ id: i.id, title: i.title, docType: i.impl_type })}
                  sx={{ cursor: viewFilter === 'active' ? 'pointer' : 'default' }}
                >
                  <TableCell padding="checkbox" sx={{ pl: 1.5 }} onClick={e => { e.stopPropagation(); toggleRow(i.id) }}>
                    <Checkbox size="small" checked={selected.has(i.id)} onChange={() => toggleRow(i.id)} />
                  </TableCell>
                  <TableCell sx={{ fontSize: '0.72rem', py: 0.6, fontFamily: 'monospace' }}>
                    {i.document_id ?? <Typography component="span" variant="caption" color="text.disabled">Custom</Typography>}
                  </TableCell>
                  <TableCell sx={{ fontSize: '0.72rem', py: 0.6, maxWidth: 240 }}>
                    <Typography variant="caption" sx={{ fontSize: '0.72rem', display: 'block', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap', textDecoration: viewFilter === 'archived' ? 'line-through' : 'none' }}>
                      {i.title ?? '—'}
                    </Typography>
                  </TableCell>
                  <TableCell sx={{ py: 0.6 }}>
                    {i.impl_type && <Chip label={i.impl_type} size="small" sx={{ height: 18, fontSize: '0.62rem', bgcolor: `${IMPL_TYPE_COLOR[i.impl_type] ?? '#9E9E9E'}20`, color: IMPL_TYPE_COLOR[i.impl_type] ?? '#9E9E9E' }} />}
                  </TableCell>
                  <TableCell sx={{ fontSize: '0.72rem', py: 0.6 }}>{i.control_group_code ?? '—'}</TableCell>
                  <TableCell sx={{ py: 0.6 }}>
                    <Box sx={{ display: 'flex', gap: 0.5 }}>
                      {i.is_edited && <Tooltip title="Edited — differs from Library version"><EditOutlined sx={{ fontSize: 14, color: '#4472C4' }} /></Tooltip>}
                      {i.stale_warning && <Tooltip title="Stale warning — linked policy was edited; cross-references may no longer be accurate"><WarningAmberOutlined sx={{ fontSize: 14, color: '#FF9800' }} /></Tooltip>}
                    </Box>
                  </TableCell>
                  <TableCell align="right" sx={{ py: 0.6, width: 60 }} onClick={e => e.stopPropagation()}>
                    {viewFilter === 'active' ? (
                      <Tooltip title="Edit document">
                        <IconButton size="small" sx={{ p: 0.4, color: 'text.disabled', '&:hover': { color: 'primary.main' } }}
                          onClick={() => setEditorDoc({ id: i.id, title: i.title, docType: i.impl_type })}>
                          <EditOutlined sx={{ fontSize: 15 }} />
                        </IconButton>
                      </Tooltip>
                    ) : (
                      <Tooltip title="Restore">
                        <IconButton size="small" sx={{ p: 0.4, color: 'text.disabled', '&:hover': { color: 'success.main' } }}
                          onClick={() => restoreMutation.mutate([i.id])}>
                          <RestoreFromTrashOutlined sx={{ fontSize: 15 }} />
                        </IconButton>
                      </Tooltip>
                    )}
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      )}

      <LibraryBrowserDrawer open={drawerOpen} onClose={() => setDrawerOpen(false)} projectId={projectId} mode="implementations" onAdded={() => {}} />
      {editorDoc && (
        <DocEditorDrawer open={!!editorDoc} onClose={() => setEditorDoc(null)} projectId={projectId}
          docId={editorDoc.id} mode="implementation" title={editorDoc.title} docType={editorDoc.docType} />
      )}
    </Box>
  )
}

// ── Checklists tab (stub — Phase 5) ───────────────────────────────────────────
// ── Checklist detail drawer ───────────────────────────────────────────────────
function ChecklistDetailDrawer({
  projectId,
  checklist,
  onClose,
}: {
  projectId: string
  checklist: ProjectChecklistRead
  onClose: () => void
}) {
  const qc = useQueryClient()

  const { data, isLoading } = useQuery({
    queryKey: ['project-checklist-detail', projectId, checklist.id],
    queryFn: () => projectsApi.getChecklist(projectId, checklist.id),
  })

  const patchItem = useMutation({
    mutationFn: (body: { item_id: string; na: boolean; justification?: string | null }) =>
      projectsApi.patchChecklistItem(projectId, checklist.id, body),
    onSuccess: (updated) => {
      qc.setQueryData(['project-checklist-detail', projectId, checklist.id], updated)
      qc.invalidateQueries({ queryKey: ['project-checklists', projectId] })
    },
  })

  const items = data?.items ?? []
  const naCount = items.filter(i => i.na).length
  const total = items.length

  return (
    <Drawer anchor="right" open onClose={onClose} PaperProps={{ sx: { width: 680, p: 0, bgcolor: 'background.paper' } }}>
      <Box sx={{ p: 2.5, borderBottom: '1px solid', borderColor: 'divider', display: 'flex', alignItems: 'center', gap: 1.5 }}>
        <AssignmentOutlined sx={{ color: '#70AD47' }} />
        <Box sx={{ flex: 1, minWidth: 0 }}>
          <Typography variant="subtitle1" sx={{ fontWeight: 700, fontSize: '0.9rem', lineHeight: 1.2 }}>
            {checklist.title ?? checklist.control_group_name}
          </Typography>
          <Typography variant="caption" color="text.secondary">
            {checklist.control_group_code} · {checklist.product_type}
            {total > 0 && ` · ${naCount} of ${total} marked N/A`}
          </Typography>
        </Box>
        <Chip
          label={`${total - naCount} / ${total} applicable`}
          size="small"
          sx={{ fontSize: '0.68rem', bgcolor: '#70AD4720', color: '#70AD47' }}
        />
        <IconButton size="small" onClick={onClose}><CloseOutlined sx={{ fontSize: 18 }} /></IconButton>
      </Box>

      {isLoading ? (
        <Box sx={{ p: 3 }}><CircularProgress size={24} /></Box>
      ) : (
        <Box sx={{ overflow: 'auto', flex: 1 }}>
          <Table size="small" stickyHeader>
            <TableHead>
              <TableRow>
                <TableCell sx={{ fontSize: '0.68rem', py: 0.75, width: 42 }}>#</TableCell>
                <TableCell sx={{ fontSize: '0.68rem', py: 0.75 }}>Requirement</TableCell>
                <TableCell sx={{ fontSize: '0.68rem', py: 0.75, width: 80, textAlign: 'center' }}>N/A</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {items.map(item => (
                <TableRow
                  key={item.id}
                  sx={{
                    opacity: item.na ? 0.45 : 1,
                    bgcolor: item.na ? 'rgba(255,152,0,0.04)' : 'inherit',
                    transition: 'opacity 0.15s',
                  }}
                >
                  <TableCell sx={{ fontSize: '0.7rem', color: 'text.disabled', py: 0.5 }}>
                    {item.row_number}
                  </TableCell>
                  <TableCell sx={{ fontSize: '0.78rem', py: 0.75, lineHeight: 1.5 }}>
                    {item.na ? (
                      <Box>
                        <Typography variant="body2" sx={{ fontSize: '0.78rem', textDecoration: 'line-through', color: 'text.disabled' }}>
                          {item.item_text}
                        </Typography>
                        {item.justification && (
                          <Typography variant="caption" sx={{ color: '#FF9800', fontSize: '0.68rem', display: 'block', mt: 0.3 }}>
                            {item.justification}
                          </Typography>
                        )}
                      </Box>
                    ) : (
                      item.item_text
                    )}
                  </TableCell>
                  <TableCell sx={{ py: 0.5, textAlign: 'center' }}>
                    <Tooltip title={item.na ? 'Mark as applicable' : 'Mark as not applicable'}>
                      <Switch
                        size="small"
                        checked={item.na}
                        onChange={e => patchItem.mutate({ item_id: item.id, na: e.target.checked })}
                        disabled={patchItem.isPending}
                        sx={{
                          '& .MuiSwitch-switchBase.Mui-checked': { color: '#FF9800' },
                          '& .MuiSwitch-switchBase.Mui-checked + .MuiSwitch-track': { bgcolor: '#FF9800' },
                        }}
                      />
                    </Tooltip>
                  </TableCell>
                </TableRow>
              ))}
              {items.length === 0 && (
                <TableRow>
                  <TableCell colSpan={3} sx={{ textAlign: 'center', py: 4, color: 'text.disabled', fontSize: '0.8rem' }}>
                    No checklist items found
                  </TableCell>
                </TableRow>
              )}
            </TableBody>
          </Table>
        </Box>
      )}
    </Drawer>
  )
}

// ── Checklists tab ────────────────────────────────────────────────────────────
function ChecklistsTab({ projectId }: { projectId: string }) {
  const qc = useQueryClient()
  const [libraryOpen, setLibraryOpen] = useState(false)
  const [selected, setSelected] = useState<ProjectChecklistRead | null>(null)

  const { data: checklists = [], isLoading } = useQuery({
    queryKey: ['project-checklists', projectId],
    queryFn: () => projectsApi.listChecklists(projectId),
  })

  const { data: library = [], isLoading: libLoading } = useQuery({
    queryKey: ['project-library-checklists', projectId],
    queryFn: () => projectsApi.libraryChecklists(projectId),
    enabled: libraryOpen,
  })

  const addChecklist = useMutation({
    mutationFn: (libId: string) => projectsApi.addChecklist(projectId, libId),
    onSuccess: () => {
      qc.invalidateQueries({ queryKey: ['project-checklists', projectId] })
      qc.invalidateQueries({ queryKey: ['project-library-checklists', projectId] })
      qc.invalidateQueries({ queryKey: ['project', projectId] })
    },
  })

  const removeChecklist = useMutation({
    mutationFn: (cid: string) => projectsApi.removeChecklist(projectId, cid),
    onSuccess: () => {
      qc.invalidateQueries({ queryKey: ['project-checklists', projectId] })
      qc.invalidateQueries({ queryKey: ['project', projectId] })
    },
  })

  const PT_COLOR: Record<string, string> = {
    framework: '#4472C4', operational: '#70AD47', privacy: '#70309f', cloud: '#0099cc',
  }

  return (
    <Box>
      {/* Toolbar */}
      <Box sx={{ display: 'flex', justifyContent: 'flex-end', mb: 2 }}>
        <Button
          variant="outlined"
          size="small"
          startIcon={<LibraryBooksOutlined />}
          onClick={() => setLibraryOpen(true)}
          sx={{ fontSize: '0.78rem' }}
        >
          Browse Library SCRs
        </Button>
      </Box>

      {/* Checklist summary table */}
      {isLoading ? (
        <Box sx={{ display: 'flex', gap: 1, flexDirection: 'column' }}>
          {[...Array(3)].map((_, i) => <Skeleton key={i} height={48} variant="rounded" />)}
        </Box>
      ) : checklists.length === 0 ? (
        <Box sx={{ py: 6, textAlign: 'center' }}>
          <AssignmentOutlined sx={{ fontSize: 40, color: 'text.disabled', mb: 1 }} />
          <Typography variant="body2" color="text.secondary" sx={{ mb: 0.5 }}>No checklists added yet</Typography>
          <Typography variant="caption" color="text.disabled">
            Browse the library to clone SCR checklists — then toggle N/A on items that don't apply.
          </Typography>
        </Box>
      ) : (
        <Table size="small">
          <TableHead>
            <TableRow>
              <TableCell sx={{ fontSize: '0.69rem', py: 0.75 }}>Control Group</TableCell>
              <TableCell sx={{ fontSize: '0.69rem', py: 0.75 }}>Title</TableCell>
              <TableCell sx={{ fontSize: '0.69rem', py: 0.75 }}>Type</TableCell>
              <TableCell sx={{ fontSize: '0.69rem', py: 0.75 }} align="right">Items</TableCell>
              <TableCell sx={{ fontSize: '0.69rem', py: 0.75 }} align="right">N/A</TableCell>
              <TableCell sx={{ fontSize: '0.69rem', py: 0.75, width: 50 }} />
            </TableRow>
          </TableHead>
          <TableBody>
            {checklists.map(cl => {
              const ptColor = PT_COLOR[cl.product_type] ?? '#9E9E9E'
              return (
                <TableRow
                  key={cl.id}
                  hover
                  sx={{ cursor: 'pointer' }}
                  onClick={() => setSelected(cl)}
                >
                  <TableCell sx={{ fontSize: '0.72rem', fontFamily: 'monospace', color: 'primary.light', py: 0.6 }}>
                    {cl.control_group_code}
                  </TableCell>
                  <TableCell sx={{ fontSize: '0.78rem', py: 0.6, maxWidth: 260 }}>
                    <Typography noWrap sx={{ fontSize: 'inherit' }}>{cl.title ?? cl.control_group_name}</Typography>
                  </TableCell>
                  <TableCell sx={{ py: 0.6 }}>
                    <Chip label={cl.product_type} size="small" sx={{ height: 18, fontSize: '0.62rem', bgcolor: `${ptColor}18`, color: ptColor }} />
                  </TableCell>
                  <TableCell align="right" sx={{ fontSize: '0.78rem', py: 0.6 }}>{cl.item_count}</TableCell>
                  <TableCell align="right" sx={{ py: 0.6 }}>
                    {cl.na_count > 0 ? (
                      <Chip
                        icon={<BlockOutlined sx={{ fontSize: '11px !important' }} />}
                        label={cl.na_count}
                        size="small"
                        sx={{ height: 18, fontSize: '0.62rem', bgcolor: '#FF980018', color: '#FF9800' }}
                      />
                    ) : (
                      <Typography sx={{ fontSize: '0.72rem', color: 'text.disabled' }}>—</Typography>
                    )}
                  </TableCell>
                  <TableCell sx={{ py: 0.6 }} align="right" onClick={e => e.stopPropagation()}>
                    <Tooltip title="Remove from project">
                      <IconButton
                        size="small"
                        onClick={() => removeChecklist.mutate(cl.id)}
                        disabled={removeChecklist.isPending}
                        sx={{ color: 'text.disabled', '&:hover': { color: 'error.main' } }}
                      >
                        <DeleteOutlined sx={{ fontSize: 15 }} />
                      </IconButton>
                    </Tooltip>
                  </TableCell>
                </TableRow>
              )
            })}
          </TableBody>
        </Table>
      )}

      {/* Library drawer */}
      <Drawer anchor="right" open={libraryOpen} onClose={() => setLibraryOpen(false)} PaperProps={{ sx: { width: 620, p: 0 } }}>
        <Box sx={{ p: 2, borderBottom: '1px solid', borderColor: 'divider', display: 'flex', alignItems: 'center', gap: 1 }}>
          <LibraryBooksOutlined sx={{ color: '#70AD47' }} />
          <Typography variant="subtitle1" sx={{ fontWeight: 700, flex: 1 }}>Library SCR Checklists</Typography>
          <IconButton size="small" onClick={() => setLibraryOpen(false)}><CloseOutlined sx={{ fontSize: 18 }} /></IconButton>
        </Box>
        {libLoading ? (
          <Box sx={{ p: 3, display: 'flex', gap: 1, flexDirection: 'column' }}>
            {[...Array(6)].map((_, i) => <Skeleton key={i} height={44} variant="rounded" />)}
          </Box>
        ) : library.length === 0 ? (
          <Box sx={{ py: 6, textAlign: 'center' }}>
            <AssignmentOutlined sx={{ fontSize: 40, color: 'text.disabled', mb: 1 }} />
            <Typography variant="body2" color="text.secondary">No library checklists available</Typography>
            <Typography variant="caption" color="text.disabled" display="block" sx={{ mt: 0.5 }}>
              SCR checklists are imported via /admin/import-operational on the production server.
            </Typography>
          </Box>
        ) : (
          <Table size="small" stickyHeader>
            <TableHead>
              <TableRow>
                <TableCell sx={{ fontSize: '0.68rem', py: 0.75 }}>Document ID</TableCell>
                <TableCell sx={{ fontSize: '0.68rem', py: 0.75 }}>Title</TableCell>
                <TableCell sx={{ fontSize: '0.68rem', py: 0.75 }}>Type</TableCell>
                <TableCell sx={{ fontSize: '0.68rem', py: 0.75, width: 60 }} align="right">Items</TableCell>
                <TableCell sx={{ fontSize: '0.68rem', py: 0.75, width: 70 }} align="right" />
              </TableRow>
            </TableHead>
            <TableBody>
              {library.map(lib => {
                const ptColor = PT_COLOR[lib.product_type] ?? '#9E9E9E'
                return (
                  <TableRow key={lib.id} hover sx={{ opacity: lib.already_in_project ? 0.5 : 1 }}>
                    <TableCell sx={{ fontSize: '0.7rem', fontFamily: 'monospace', py: 0.6 }}>{lib.document_id}</TableCell>
                    <TableCell sx={{ fontSize: '0.78rem', py: 0.6, maxWidth: 220 }}>
                      <Typography noWrap sx={{ fontSize: 'inherit' }}>{lib.title}</Typography>
                      <Typography variant="caption" color="text.disabled" sx={{ fontSize: '0.65rem' }}>
                        {lib.control_group_code}
                      </Typography>
                    </TableCell>
                    <TableCell sx={{ py: 0.6 }}>
                      <Chip label={lib.product_type} size="small" sx={{ height: 18, fontSize: '0.62rem', bgcolor: `${ptColor}18`, color: ptColor }} />
                    </TableCell>
                    <TableCell align="right" sx={{ fontSize: '0.72rem', py: 0.6, color: 'text.secondary' }}>{lib.item_count}</TableCell>
                    <TableCell align="right" sx={{ py: 0.6 }}>
                      <Button
                        size="small"
                        variant={lib.already_in_project ? 'text' : 'outlined'}
                        disabled={lib.already_in_project || addChecklist.isPending}
                        onClick={() => addChecklist.mutate(lib.id)}
                        sx={{ fontSize: '0.7rem', minWidth: 60, py: 0.3 }}
                      >
                        {lib.already_in_project ? 'Added' : 'Add'}
                      </Button>
                    </TableCell>
                  </TableRow>
                )
              })}
            </TableBody>
          </Table>
        )}
      </Drawer>

      {/* Item detail drawer */}
      {selected && (
        <ChecklistDetailDrawer
          projectId={projectId}
          checklist={selected}
          onClose={() => setSelected(null)}
        />
      )}
    </Box>
  )
}

// ── Gaps tab ──────────────────────────────────────────────────────────────────
const SEV_COLOR: Record<string, string> = { critical: '#C00000', high: '#FF5722', medium: '#FF9800', low: '#4CAF50' }

function LogGapDialog({ open, onClose, projectId, productFamily }: { open: boolean; onClose: () => void; projectId: string; productFamily: string }) {
  const qc = useQueryClient()
  const [form, setForm] = useState({ control_group_id: '', gap_description: '', severity: 'medium', owner: '', due_date: '' })
  const [error, setError] = useState('')
  const set = (k: string, v: string) => setForm(f => ({ ...f, [k]: v }))

  const { data: controls } = useQuery({
    queryKey: ['controls', productFamily],
    queryFn: () => controlsApi.list({ product_family: productFamily }),
    enabled: open,
  })

  const mutation = useMutation({
    mutationFn: () => gapsApi.create({
      control_group_id: form.control_group_id,
      gap_description: form.gap_description,
      severity: form.severity,
      product_type: 'framework',
      owner: form.owner || undefined,
      due_date: form.due_date || undefined,
      project_id: projectId,
    }),
    onSuccess: () => {
      qc.invalidateQueries({ queryKey: ['project-gaps', projectId] })
      qc.invalidateQueries({ queryKey: ['project', projectId] })
      onClose()
      setForm({ control_group_id: '', gap_description: '', severity: 'medium', owner: '', due_date: '' })
      setError('')
    },
    onError: (e: any) => setError(e?.response?.data?.detail ?? 'Failed to log gap'),
  })

  const handleSubmit = () => {
    if (!form.control_group_id) { setError('Select a control group'); return }
    if (!form.gap_description.trim()) { setError('Description is required'); return }
    mutation.mutate()
  }

  return (
    <Dialog open={open} onClose={onClose} maxWidth="sm" fullWidth>
      <DialogTitle sx={{ fontSize: '1rem', fontWeight: 700 }}>Log Gap</DialogTitle>
      <DialogContent sx={{ display: 'flex', flexDirection: 'column', gap: 1.5, pt: '12px !important' }}>
        {error && <Alert severity="error" sx={{ py: 0.5 }}>{error}</Alert>}
        <FormControl size="small" fullWidth required>
          <InputLabel>Control Group</InputLabel>
          <Select value={form.control_group_id} onChange={e => set('control_group_id', e.target.value)} label="Control Group">
            {(controls ?? []).map(c => (
              <MenuItem key={c.id} value={c.id}>
                <Typography variant="caption" sx={{ fontFamily: 'monospace', color: 'primary.light', mr: 1 }}>{c.group_code.toUpperCase()}</Typography>
                {c.group_name}
              </MenuItem>
            ))}
          </Select>
        </FormControl>
        <TextField label="Description" size="small" multiline minRows={3} required fullWidth value={form.gap_description} onChange={e => set('gap_description', e.target.value)} />
        <Box sx={{ display: 'flex', gap: 1.5 }}>
          <FormControl size="small" sx={{ flex: 1 }}>
            <InputLabel>Severity</InputLabel>
            <Select value={form.severity} onChange={e => set('severity', e.target.value)} label="Severity">
              {['critical', 'high', 'medium', 'low'].map(s => <MenuItem key={s} value={s} sx={{ textTransform: 'capitalize' }}>{s}</MenuItem>)}
            </Select>
          </FormControl>
          <TextField label="Owner" size="small" sx={{ flex: 1 }} value={form.owner} onChange={e => set('owner', e.target.value)} placeholder="Optional" />
          <TextField label="Due date" size="small" sx={{ flex: 1 }} type="date" value={form.due_date} onChange={e => set('due_date', e.target.value)} InputLabelProps={{ shrink: true }} />
        </Box>
      </DialogContent>
      <DialogActions sx={{ px: 3, pb: 2 }}>
        <Button size="small" onClick={onClose}>Cancel</Button>
        <Button size="small" variant="contained" onClick={handleSubmit} disabled={mutation.isPending}>Log Gap</Button>
      </DialogActions>
    </Dialog>
  )
}

function GapsTab({ projectId, productFamily }: { projectId: string; productFamily: string }) {
  const navigate = useNavigate()
  const [logOpen, setLogOpen] = useState(false)

  const { data: gaps, isLoading } = useQuery({
    queryKey: ['project-gaps', projectId],
    queryFn: () => gapsApi.list({ project_id: projectId, limit: 200 }),
  })

  return (
    <Box>
      <Box sx={{ display: 'flex', alignItems: 'center', gap: 1.5, mb: 1.5 }}>
        <Typography variant="caption" color="text.secondary" sx={{ flex: 1 }}>
          {gaps?.length ?? 0} gap{gaps?.length !== 1 ? 's' : ''} logged
        </Typography>
        <Button size="small" variant="outlined" startIcon={<FindInPageOutlined />} onClick={() => setLogOpen(true)}>Log Gap</Button>
        <Button size="small" variant="text" onClick={() => navigate('/gaps')} sx={{ fontSize: '0.72rem', color: 'text.secondary' }}>Open Gaps page →</Button>
      </Box>

      {isLoading ? <Skeleton variant="rounded" height={120} /> : !gaps?.length ? (
        <Box sx={{ py: 6, textAlign: 'center' }}>
          <FindInPageOutlined sx={{ fontSize: 40, color: 'text.disabled', mb: 1 }} />
          <Typography variant="body2" color="text.secondary">No gaps logged for this project yet.</Typography>
        </Box>
      ) : (
        <TableContainer>
          <Table size="small">
            <TableHead>
              <TableRow>
                <TableCell sx={{ fontSize: '0.72rem', color: 'text.secondary' }}>Control</TableCell>
                <TableCell sx={{ fontSize: '0.72rem', color: 'text.secondary' }}>Description</TableCell>
                <TableCell sx={{ fontSize: '0.72rem', color: 'text.secondary' }}>Severity</TableCell>
                <TableCell sx={{ fontSize: '0.72rem', color: 'text.secondary' }}>Status</TableCell>
                <TableCell sx={{ fontSize: '0.72rem', color: 'text.secondary' }}>Created</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {gaps.map(g => (
                <TableRow key={g.id} hover sx={{ cursor: 'pointer' }} onClick={() => navigate('/gaps')}>
                  <TableCell sx={{ fontSize: '0.75rem', fontFamily: 'monospace', color: 'primary.light' }}>{g.control_group_code.toUpperCase()}</TableCell>
                  <TableCell sx={{ fontSize: '0.75rem', maxWidth: 300 }}>
                    <Typography variant="caption" sx={{ display: '-webkit-box', WebkitLineClamp: 2, WebkitBoxOrient: 'vertical', overflow: 'hidden' }}>{g.gap_description}</Typography>
                  </TableCell>
                  <TableCell>
                    <Chip label={g.severity} size="small" sx={{ height: 18, fontSize: '0.62rem', bgcolor: `${SEV_COLOR[g.severity] ?? '#9E9E9E'}18`, color: SEV_COLOR[g.severity] ?? '#9E9E9E' }} />
                  </TableCell>
                  <TableCell><Chip label={g.status} size="small" sx={{ height: 18, fontSize: '0.62rem' }} /></TableCell>
                  <TableCell sx={{ fontSize: '0.72rem', color: 'text.secondary', whiteSpace: 'nowrap' }}>{dayjs(g.created_at).format('D MMM YY')}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      )}

      <LogGapDialog open={logOpen} onClose={() => setLogOpen(false)} projectId={projectId} productFamily={productFamily} />
    </Box>
  )
}

// ── Evidence tab ──────────────────────────────────────────────────────────────
function UploadEvidenceDialog({ open, onClose, projectId }: { open: boolean; onClose: () => void; projectId: string }) {
  const qc = useQueryClient()
  const fileRef = useRef<HTMLInputElement>(null)
  const [title, setTitle] = useState('')
  const [evidenceType, setEvidenceType] = useState('document')
  const [notes, setNotes] = useState('')
  const [file, setFile] = useState<File | null>(null)
  const [error, setError] = useState('')

  const mutation = useMutation({
    mutationFn: () => {
      if (!file) throw new Error('No file selected')
      const fd = new FormData()
      fd.append('file', file)
      fd.append('title', title || file.name)
      fd.append('evidence_type', evidenceType)
      fd.append('notes', notes)
      fd.append('project_id', projectId)
      return evidenceApi.upload(fd)
    },
    onSuccess: () => {
      qc.invalidateQueries({ queryKey: ['project-evidence', projectId] })
      qc.invalidateQueries({ queryKey: ['project', projectId] })
      onClose()
      setTitle(''); setNotes(''); setFile(null); setError('')
    },
    onError: (e: any) => setError(e?.response?.data?.detail ?? 'Upload failed'),
  })

  return (
    <Dialog open={open} onClose={onClose} maxWidth="sm" fullWidth>
      <DialogTitle sx={{ fontSize: '1rem', fontWeight: 700 }}>Upload Evidence</DialogTitle>
      <DialogContent sx={{ display: 'flex', flexDirection: 'column', gap: 1.5, pt: '12px !important' }}>
        {error && <Alert severity="error" sx={{ py: 0.5 }}>{error}</Alert>}
        <Button variant="outlined" size="small" component="label" startIcon={<UploadFileOutlined />}>
          {file ? file.name : 'Choose file'}
          <input ref={fileRef} type="file" hidden onChange={e => setFile(e.target.files?.[0] ?? null)} />
        </Button>
        <TextField label="Title" size="small" fullWidth value={title} onChange={e => setTitle(e.target.value)} placeholder="Leave blank to use filename" />
        <FormControl size="small" fullWidth>
          <InputLabel>Evidence type</InputLabel>
          <Select value={evidenceType} onChange={e => setEvidenceType(e.target.value)} label="Evidence type">
            {['document', 'screenshot', 'log', 'certificate', 'report', 'policy', 'procedure', 'audit_report', 'test_result', 'other'].map(t => (
              <MenuItem key={t} value={t} sx={{ textTransform: 'capitalize', fontSize: '0.85rem' }}>{t.replace(/_/g, ' ')}</MenuItem>
            ))}
          </Select>
        </FormControl>
        <TextField label="Notes" size="small" fullWidth multiline minRows={2} value={notes} onChange={e => setNotes(e.target.value)} placeholder="Optional" />
      </DialogContent>
      <DialogActions sx={{ px: 3, pb: 2 }}>
        <Button size="small" onClick={onClose}>Cancel</Button>
        <Button size="small" variant="contained" onClick={() => mutation.mutate()} disabled={!file || mutation.isPending}>Upload</Button>
      </DialogActions>
    </Dialog>
  )
}

function EvidenceTab({ projectId }: { projectId: string }) {
  const navigate = useNavigate()
  const [uploadOpen, setUploadOpen] = useState(false)

  const { data: items, isLoading } = useQuery({
    queryKey: ['project-evidence', projectId],
    queryFn: () => evidenceApi.list({ project_id: projectId, limit: 200 }),
  })

  return (
    <Box>
      <Box sx={{ display: 'flex', alignItems: 'center', gap: 1.5, mb: 1.5 }}>
        <Typography variant="caption" color="text.secondary" sx={{ flex: 1 }}>
          {items?.length ?? 0} evidence item{items?.length !== 1 ? 's' : ''}
        </Typography>
        <Button size="small" variant="outlined" startIcon={<UploadFileOutlined />} onClick={() => setUploadOpen(true)}>Upload Evidence</Button>
        <Button size="small" variant="text" onClick={() => navigate('/evidence')} sx={{ fontSize: '0.72rem', color: 'text.secondary' }}>Open Evidence page →</Button>
      </Box>

      {isLoading ? <Skeleton variant="rounded" height={120} /> : !items?.length ? (
        <Box sx={{ py: 6, textAlign: 'center' }}>
          <UploadFileOutlined sx={{ fontSize: 40, color: 'text.disabled', mb: 1 }} />
          <Typography variant="body2" color="text.secondary">No evidence uploaded for this project yet.</Typography>
        </Box>
      ) : (
        <TableContainer>
          <Table size="small">
            <TableHead>
              <TableRow>
                <TableCell sx={{ fontSize: '0.72rem', color: 'text.secondary' }}>Title</TableCell>
                <TableCell sx={{ fontSize: '0.72rem', color: 'text.secondary' }}>Type</TableCell>
                <TableCell sx={{ fontSize: '0.72rem', color: 'text.secondary' }}>Control</TableCell>
                <TableCell sx={{ fontSize: '0.72rem', color: 'text.secondary' }}>Status</TableCell>
                <TableCell sx={{ fontSize: '0.72rem', color: 'text.secondary' }}>Uploaded</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {items.map(ev => (
                <TableRow key={ev.id} hover sx={{ cursor: 'pointer' }} onClick={() => navigate('/evidence')}>
                  <TableCell sx={{ fontSize: '0.75rem', maxWidth: 250 }}>
                    <Typography variant="caption" sx={{ display: 'block', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>{ev.title}</Typography>
                  </TableCell>
                  <TableCell sx={{ fontSize: '0.72rem', color: 'text.secondary' }}>{ev.evidence_type?.replace(/_/g, ' ')}</TableCell>
                  <TableCell sx={{ fontSize: '0.72rem', fontFamily: 'monospace', color: 'primary.light' }}>{ev.group_code?.toUpperCase() ?? '—'}</TableCell>
                  <TableCell><Chip label={ev.evidence_status} size="small" sx={{ height: 18, fontSize: '0.62rem' }} /></TableCell>
                  <TableCell sx={{ fontSize: '0.72rem', color: 'text.secondary', whiteSpace: 'nowrap' }}>{dayjs(ev.created_at).format('D MMM YY')}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      )}

      <UploadEvidenceDialog open={uploadOpen} onClose={() => setUploadOpen(false)} projectId={projectId} />
    </Box>
  )
}

// ── Compliance assessments tab ────────────────────────────────────────────────
const FRAMEWORK_CODES = ['NIS2', 'DORA', 'CIS_V8', 'BSI_IT_GRUNDSCHUTZ', 'TISAX', 'CH_NDSG', 'EU_CRA', 'EU_AI_ACT', 'EU_CLOUD_SOV']
const FRAMEWORK_COLORS: Record<string, string> = {
  NIS2: '#1565C0', DORA: '#6A1B9A', CIS_V8: '#2E7D32',
  BSI_IT_GRUNDSCHUTZ: '#E65100', TISAX: '#00838F',
  CH_NDSG: '#AD1457', EU_CRA: '#4527A0', EU_AI_ACT: '#283593',
  EU_CLOUD_SOV: '#01579B',
}

// Fetches assessments for all frameworks scoped to a project in a single query
async function fetchAllProjectAssessments(projectId: string) {
  const results = await Promise.all(
    FRAMEWORK_CODES.map(fc =>
      regulatoryApi.listAssessments(fc, { project_id: projectId })
        .then(items => items.map(a => ({ ...a, frameworkCode: fc })))
        .catch(() => [] as Array<ReturnType<typeof regulatoryApi.listAssessments> extends Promise<infer T> ? T[number] & { frameworkCode: string } : never>)
    )
  )
  return results.flat()
}

// ── Platform assessments tab (ISO 27001 workbook assessments) ─────────────────
function PlatformAssessmentsTab({ productFamily }: { productFamily: string }) {
  const navigate = useNavigate()
  const product = productFamily.toLowerCase()
  return (
    <Box sx={{ py: 2 }}>
      <Box sx={{ display: 'flex', alignItems: 'center', gap: 1.5, mb: 2 }}>
        <Typography variant="caption" color="text.secondary" sx={{ flex: 1 }}>
          Platform assessments are ISO 27001 workbook assessments. With this project active, new assessments will be linked to it automatically.
        </Typography>
        <Button size="small" variant="contained" startIcon={<AssignmentOutlined />} onClick={() => navigate('/assessments')}>
          Open Assessments
        </Button>
      </Box>
      <Box sx={{ p: 2.5, border: '1px solid', borderColor: 'divider', borderRadius: 1.5, textAlign: 'center' }}>
        <AssignmentOutlined sx={{ fontSize: 36, color: 'text.disabled', mb: 1 }} />
        <Typography variant="body2" color="text.secondary" sx={{ mb: 0.5 }}>
          Platform assessments are managed on the Assessments page.
        </Typography>
        <Typography variant="caption" color="text.disabled" sx={{ display: 'block', mb: 1.5 }}>
          Make this project active to automatically link new assessments to it.
        </Typography>
        <Button size="small" variant="outlined" onClick={() => navigate('/assessments')} sx={{ fontSize: '0.75rem' }}>
          Go to Assessments →
        </Button>
      </Box>
    </Box>
  )
}

const FRAMEWORK_ROUTES: Record<string, string> = {
  NIS2: '/nis2', DORA: '/dora', CIS_V8: '/cis-v8',
  BSI_IT_GRUNDSCHUTZ: '/bsi-it-grundschutz', TISAX: '/tisax',
  CH_NDSG: '/ch-ndsg', EU_CRA: '/eu-cra', EU_AI_ACT: '/eu-ai-act',
  EU_CLOUD_SOV: '/eu-cloud-sov',
}
const FRAMEWORK_LABELS: Record<string, string> = {
  NIS2: 'NIS2', DORA: 'DORA', CIS_V8: 'CIS v8',
  BSI_IT_GRUNDSCHUTZ: 'BSI IT-GS', TISAX: 'TISAX',
  CH_NDSG: 'nDSG', EU_CRA: 'EU CRA', EU_AI_ACT: 'EU AI Act',
  EU_CLOUD_SOV: 'Cloud Sov.',
}

function AssessmentsTab({ projectId }: { projectId: string }) {
  const navigate = useNavigate()

  const { data: allAssessments = [], isLoading } = useQuery({
    queryKey: ['project-assessments', projectId],
    queryFn: () => fetchAllProjectAssessments(projectId),
  })

  return (
    <Box>
      {/* Framework quick-start buttons */}
      <Box sx={{ mb: 2 }}>
        <Typography variant="caption" color="text.secondary" sx={{ display: 'block', mb: 1, fontSize: '0.7rem', textTransform: 'uppercase', letterSpacing: '0.06em' }}>
          New Assessment →
        </Typography>
        <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 0.75 }}>
          {FRAMEWORK_CODES.map(fc => {
            const color = FRAMEWORK_COLORS[fc] ?? '#1976d2'
            const existingCount = allAssessments.filter(a => a.frameworkCode === fc).length
            return (
              <Button
                key={fc}
                size="small"
                variant="outlined"
                onClick={() => navigate(FRAMEWORK_ROUTES[fc] ?? '/')}
                sx={{
                  fontSize: '0.7rem', py: 0.3, px: 1, borderColor: `${color}60`, color,
                  '&:hover': { borderColor: color, bgcolor: `${color}10` },
                }}
                endIcon={existingCount > 0
                  ? <Chip label={existingCount} size="small" sx={{ height: 16, fontSize: '0.58rem', bgcolor: `${color}20`, color, '& .MuiChip-label': { px: 0.5 } }} />
                  : undefined
                }
              >
                {FRAMEWORK_LABELS[fc] ?? fc}
              </Button>
            )
          })}
        </Box>
      </Box>

      <Divider sx={{ mb: 2 }} />

      {isLoading ? <Skeleton variant="rounded" height={120} /> : !allAssessments.length ? (
        <Box sx={{ py: 4, textAlign: 'center' }}>
          <ShieldOutlined sx={{ fontSize: 36, color: 'text.disabled', mb: 1 }} />
          <Typography variant="body2" color="text.secondary" sx={{ mb: 0.5 }}>
            No compliance assessments linked to this project yet.
          </Typography>
          <Typography variant="caption" color="text.disabled">
            Use the buttons above to start an assessment — it will appear here when this project is active.
          </Typography>
        </Box>
      ) : (
        <TableContainer>
          <Table size="small">
            <TableHead>
              <TableRow>
                <TableCell sx={{ fontSize: '0.72rem', color: 'text.secondary' }}>Framework</TableCell>
                <TableCell sx={{ fontSize: '0.72rem', color: 'text.secondary' }}>Assessment</TableCell>
                <TableCell sx={{ fontSize: '0.72rem', color: 'text.secondary' }}>Status</TableCell>
                <TableCell sx={{ fontSize: '0.72rem', color: 'text.secondary' }} align="right">Rated</TableCell>
                <TableCell sx={{ fontSize: '0.72rem', color: 'text.secondary' }} align="right">Compliant</TableCell>
                <TableCell sx={{ fontSize: '0.72rem', color: 'text.secondary' }}>Created</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {allAssessments.map(a => {
                const color = FRAMEWORK_COLORS[a.frameworkCode] ?? '#1976d2'
                const pct = a.total_requirements > 0
                  ? Math.round((a.compliant_count / a.total_requirements) * 100)
                  : null
                return (
                  <TableRow
                    key={a.id}
                    hover
                    sx={{ cursor: 'pointer' }}
                    onClick={() => navigate(FRAMEWORK_ROUTES[a.frameworkCode] ?? '/')}
                  >
                    <TableCell sx={{ py: 0.75 }}>
                      <Chip label={FRAMEWORK_LABELS[a.frameworkCode] ?? a.frameworkCode} size="small" sx={{ height: 18, fontSize: '0.62rem', bgcolor: `${color}18`, color }} />
                    </TableCell>
                    <TableCell sx={{ fontSize: '0.78rem', py: 0.75, maxWidth: 220 }}>
                      <Typography variant="caption" sx={{ fontSize: '0.78rem', display: 'block', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap', fontWeight: 600 }}>
                        {a.name}
                      </Typography>
                      {a.organisation && <Typography variant="caption" color="text.disabled" sx={{ fontSize: '0.68rem' }}>{a.organisation}</Typography>}
                    </TableCell>
                    <TableCell sx={{ py: 0.75 }}>
                      <Chip label={a.status} size="small" sx={{ height: 18, fontSize: '0.6rem', textTransform: 'capitalize',
                        bgcolor: a.status === 'complete' ? '#4CAF5018' : a.status === 'in_progress' ? '#4472C418' : '#9E9E9E18',
                        color: a.status === 'complete' ? '#4CAF50' : a.status === 'in_progress' ? '#4472C4' : '#9E9E9E',
                      }} />
                    </TableCell>
                    <TableCell sx={{ fontSize: '0.78rem', py: 0.75 }} align="right">
                      {a.rated_count}/{a.total_requirements}
                    </TableCell>
                    <TableCell sx={{ fontSize: '0.78rem', py: 0.75 }} align="right">
                      {pct !== null ? `${pct}%` : '—'}
                    </TableCell>
                    <TableCell sx={{ fontSize: '0.72rem', py: 0.75, color: 'text.secondary' }}>
                      {dayjs(a.created_at).format('D MMM YYYY')}
                    </TableCell>
                  </TableRow>
                )
              })}
            </TableBody>
          </Table>
        </TableContainer>
      )}
    </Box>
  )
}

// ── QA Tab (Phase 21) ──────────────────────────────────────────────────────────

const STATUS_COLOR: Record<string, string> = {
  pass: '#4CAF50',
  warning: '#FF9800',
  fail: '#f44336',
  needs_review: '#9E9E9E',
}

const STATUS_LABEL: Record<string, string> = {
  pass: 'Pass',
  warning: 'Warning',
  fail: 'Fail',
  needs_review: 'Review',
}

function QAScoreBar({ label, value, total }: { label: string; value: number; total: number }) {
  const pct = total ? Math.round((value / total) * 100) : 0
  return (
    <Box sx={{ mb: 0.75 }}>
      <Box sx={{ display: 'flex', justifyContent: 'space-between', mb: 0.2 }}>
        <Typography variant="caption" sx={{ fontSize: '0.68rem', color: 'text.secondary' }}>{label}</Typography>
        <Typography variant="caption" sx={{ fontSize: '0.68rem', color: 'text.primary' }}>{value} ({pct}%)</Typography>
      </Box>
      <LinearProgress
        variant="determinate"
        value={pct}
        sx={{
          height: 4,
          borderRadius: 2,
          bgcolor: 'rgba(255,255,255,0.06)',
          '& .MuiLinearProgress-bar': {
            bgcolor: label === 'Pass' ? '#4CAF50' : label === 'Warning' ? '#FF9800' : label === 'Fail' ? '#f44336' : '#9E9E9E',
          },
        }}
      />
    </Box>
  )
}

function ProjectQASummaryCard({ summary, method }: { summary: ProjectQASummary; method: string }) {
  const total = summary.total || 1
  return (
    <Box sx={{ p: 2, border: '1px solid', borderColor: 'divider', borderRadius: 1.5, mb: 2.5 }}>
      <Box sx={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', mb: 1.5 }}>
        <Typography variant="caption" sx={{ fontWeight: 700, textTransform: 'uppercase', letterSpacing: '0.06em', fontSize: '0.65rem', color: 'text.secondary' }}>
          {method === 'existence' ? 'Artefact Coverage' : method === 'keyword' ? 'Keyword Coverage' : 'Semantic Alignment'} — Last Run
        </Typography>
        <Box sx={{ display: 'flex', alignItems: 'baseline', gap: 0.5 }}>
          <Typography variant="h5" sx={{ fontWeight: 700, color: '#4CAF50', lineHeight: 1, fontSize: '1.4rem' }}>
            {Math.round(summary.pass_rate * 100)}%
          </Typography>
          <Typography variant="caption" sx={{ color: 'text.disabled', fontSize: '0.65rem' }}>pass rate</Typography>
        </Box>
      </Box>
      <QAScoreBar label="Pass" value={summary.pass} total={total} />
      <QAScoreBar label="Warning" value={summary.warning} total={total} />
      <QAScoreBar label="Fail" value={summary.fail} total={total} />
      <QAScoreBar label="Needs Review" value={summary.needs_review} total={total} />
      {summary.last_run && (
        <Typography variant="caption" sx={{ fontSize: '0.63rem', color: 'text.disabled', display: 'block', mt: 0.75 }}>
          Last run: {dayjs(summary.last_run).format('DD MMM YYYY HH:mm')}
        </Typography>
      )}
    </Box>
  )
}

const CROSSWALK_FRAMEWORKS = [
  { code: 'NIS2',                    label: 'NIS2 Directive' },
  { code: 'DORA',                    label: 'DORA' },
  { code: 'NIST_CSF_2.0',            label: 'NIST CSF 2.0' },
  { code: 'NIST_800_53_R5',          label: 'NIST SP 800-53 Rev 5' },
  { code: 'CIS_V8',                  label: 'CIS Controls v8' },
  { code: 'BSI_IT_GRUNDSCHUTZ',      label: 'BSI IT-Grundschutz' },
  { code: 'EU_GDPR',                 label: 'EU GDPR' },
  { code: 'TISAX',                   label: 'TISAX / VDA ISA' },
  { code: 'ISO27701',                label: 'ISO 27701' },
  { code: 'ISO27018',                label: 'ISO 27018' },
  { code: 'CYFUN_BE',                label: 'CyberFundamentals (BE)' },
  { code: 'BAFIN_BAIT',              label: 'BaFin BAIT (DE)' },
  { code: 'CSSF_LU',                 label: 'CSSF 20-750 (LU)' },
  { code: 'ACN_IT',                  label: 'ACN Guidelines (IT)' },
  { code: 'UK_NIS',                  label: 'UK NIS Regulations' },
  { code: 'UK_OPERATIONAL_RESILIENCE', label: 'UK Op. Resilience' },
]

function QATab({ projectId }: { projectId: string }) {
  const qc = useQueryClient()
  const [method, setMethod] = useState<string>('existence')
  const [refLib, setRefLib] = useState<string>('iso_corpus')
  const [language, setLanguage] = useState<string>('en')
  const [frameworkCodes, setFrameworkCodes] = useState<string[]>([])
  const [running, setRunning] = useState<string | null>(null)
  const [runResult, setRunResult] = useState<string | null>(null)

  const showFrameworkSelect = method !== 'existence' && (refLib === 'crosswalk' || refLib === 'both')

  const { data: summary, isLoading: summaryLoading } = useQuery({
    queryKey: ['project-qa-summary', projectId, method],
    queryFn: () => qaApi.getProjectSummary(projectId, method),
  })

  const { data: results, isLoading: resultsLoading } = useQuery({
    queryKey: ['project-qa-results', projectId, method],
    queryFn: () => qaApi.getProjectResults(projectId, { method, limit: 200 }),
    enabled: !!summary?.last_run,
  })

  async function handleRun(type: string) {
    setRunning(type)
    setRunResult(null)
    try {
      let res: { total: number; pass_count: number; warning_count: number; fail_count: number; duration_ms: number }
      const fw = showFrameworkSelect && frameworkCodes.length > 0 ? frameworkCodes : undefined
      if (type === 'existence') {
        res = await qaApi.runProjectExistence(projectId)
      } else if (type === 'keyword') {
        res = await qaApi.runProjectKeyword(projectId, refLib, language, fw)
      } else if (type === 'semantic_claude') {
        res = await qaApi.runProjectSemanticClaude(projectId, refLib, language, fw)
      } else {
        res = await qaApi.runProjectSemantic(projectId, refLib, language, fw)
      }
      setRunResult(`Complete — ${res.total} checked, ${res.pass_count} pass, ${res.warning_count} warning, ${res.fail_count} fail (${res.duration_ms}ms)`)
      qc.invalidateQueries({ queryKey: ['project-qa-summary', projectId] })
      qc.invalidateQueries({ queryKey: ['project-qa-results', projectId] })
    } catch (e: unknown) {
      const msg = e instanceof Error ? e.message : String(e)
      setRunResult(`Error: ${msg}`)
    } finally {
      setRunning(null)
    }
  }

  const statusCounts = (results ?? []).reduce<Record<string, number>>((acc, r) => {
    acc[r.qa_status] = (acc[r.qa_status] ?? 0) + 1
    return acc
  }, {})

  return (
    <Box>
      {/* Controls row */}
      <Box sx={{ display: 'flex', gap: 1.5, flexWrap: 'wrap', alignItems: 'center', mb: 2.5 }}>
        <FormControl size="small" sx={{ minWidth: 140 }}>
          <InputLabel sx={{ fontSize: '0.78rem' }}>Method</InputLabel>
          <Select value={method} label="Method" onChange={e => setMethod(e.target.value)} sx={{ fontSize: '0.78rem' }}>
            <MenuItem value="existence" sx={{ fontSize: '0.78rem' }}>Artefact Check</MenuItem>
            <MenuItem value="keyword" sx={{ fontSize: '0.78rem' }}>Keyword</MenuItem>
            <MenuItem value="semantic" sx={{ fontSize: '0.78rem' }}>Semantic (Mini LLM)</MenuItem>
            <MenuItem value="semantic_claude" sx={{ fontSize: '0.78rem' }}>Semantic (Claude AI)</MenuItem>
          </Select>
        </FormControl>

        {method !== 'existence' && (
          <FormControl size="small" sx={{ minWidth: 150 }}>
            <InputLabel sx={{ fontSize: '0.78rem' }}>Reference Library</InputLabel>
            <Select value={refLib} label="Reference Library" onChange={e => setRefLib(e.target.value)} sx={{ fontSize: '0.78rem' }}>
              <MenuItem value="iso_corpus" sx={{ fontSize: '0.78rem' }}>ISO Corpus</MenuItem>
              <MenuItem value="isms_library" sx={{ fontSize: '0.78rem' }}>ISMS Library POLs</MenuItem>
              <MenuItem value="crosswalk" sx={{ fontSize: '0.78rem' }}>Crosswalk only</MenuItem>
              <MenuItem value="both" sx={{ fontSize: '0.78rem' }}>ISO + Crosswalk (both)</MenuItem>
            </Select>
          </FormControl>
        )}

        {method !== 'existence' && (
          <FormControl size="small" sx={{ minWidth: 110 }}>
            <InputLabel sx={{ fontSize: '0.78rem' }}>Language</InputLabel>
            <Select value={language} label="Language" onChange={e => setLanguage(e.target.value)} sx={{ fontSize: '0.78rem' }}>
              <MenuItem value="en" sx={{ fontSize: '0.78rem' }}>EN</MenuItem>
              <MenuItem value="fr" sx={{ fontSize: '0.78rem' }}>FR</MenuItem>
              <MenuItem value="de" sx={{ fontSize: '0.78rem' }}>DE</MenuItem>
              <MenuItem value="it" sx={{ fontSize: '0.78rem' }}>IT</MenuItem>
            </Select>
          </FormControl>
        )}

        {showFrameworkSelect && (
          <FormControl size="small" sx={{ minWidth: 220 }}>
            <InputLabel sx={{ fontSize: '0.78rem' }}>Target Frameworks (optional)</InputLabel>
            <Select
              multiple
              label="Target Frameworks (optional)"
              value={frameworkCodes}
              onChange={e => setFrameworkCodes(typeof e.target.value === 'string' ? e.target.value.split(',') : e.target.value as string[])}
              renderValue={selected => (selected as string[]).map(c => CROSSWALK_FRAMEWORKS.find(f => f.code === c)?.label ?? c).join(', ')}
              sx={{ fontSize: '0.78rem' }}
            >
              {CROSSWALK_FRAMEWORKS.map(f => (
                <MenuItem key={f.code} value={f.code} sx={{ fontSize: '0.78rem' }}>
                  {f.label}
                </MenuItem>
              ))}
            </Select>
          </FormControl>
        )}

        <Button
          size="small"
          variant="contained"
          startIcon={running === method ? <CircularProgress size={13} color="inherit" /> : method === 'semantic_claude' ? <AutoAwesomeOutlined sx={{ fontSize: 15 }} /> : <PlayArrowOutlined sx={{ fontSize: 15 }} />}
          disabled={!!running}
          onClick={() => handleRun(method)}
          sx={{ fontSize: '0.72rem' }}
        >
          Run {method === 'existence' ? 'Artefact Check' : method === 'keyword' ? 'Keyword Check' : method === 'semantic_claude' ? 'Claude AI Check' : 'Semantic Check'}
        </Button>
      </Box>

      {runResult && (
        <Alert
          severity={runResult.startsWith('Error') ? 'error' : 'success'}
          onClose={() => setRunResult(null)}
          sx={{ mb: 2, fontSize: '0.78rem' }}
        >
          {runResult}
        </Alert>
      )}

      {/* Summary card */}
      {summaryLoading ? (
        <Skeleton variant="rectangular" height={120} sx={{ borderRadius: 1.5, mb: 2.5 }} />
      ) : summary && summary.total > 0 ? (
        <ProjectQASummaryCard summary={summary} method={method} />
      ) : (
        <Box sx={{ p: 2, mb: 2.5, border: '1px solid', borderColor: 'divider', borderRadius: 1.5, textAlign: 'center' }}>
          <VerifiedOutlined sx={{ fontSize: 28, color: 'text.disabled', mb: 0.5 }} />
          <Typography variant="body2" color="text.secondary" sx={{ fontSize: '0.78rem' }}>
            No QA results yet — run a check above to analyse this project's documents.
          </Typography>
        </Box>
      )}

      {/* Status filter chips */}
      {results && results.length > 0 && (
        <Box sx={{ display: 'flex', gap: 0.75, flexWrap: 'wrap', mb: 1.5 }}>
          {Object.entries(statusCounts).map(([st, cnt]) => (
            <Chip
              key={st}
              label={`${STATUS_LABEL[st] ?? st} (${cnt})`}
              size="small"
              sx={{ height: 20, fontSize: '0.65rem', bgcolor: `${STATUS_COLOR[st] ?? '#9E9E9E'}18`, color: STATUS_COLOR[st] ?? '#9E9E9E', border: `1px solid ${STATUS_COLOR[st] ?? '#9E9E9E'}40` }}
            />
          ))}
        </Box>
      )}

      {/* Results table */}
      {resultsLoading ? (
        <Skeleton variant="rectangular" height={200} sx={{ borderRadius: 1 }} />
      ) : results && results.length > 0 ? (
        <TableContainer>
          <Table size="small" stickyHeader>
            <TableHead>
              <TableRow>
                <TableCell sx={{ fontSize: '0.69rem', py: 0.75 }}>Control Group</TableCell>
                <TableCell sx={{ fontSize: '0.69rem', py: 0.75 }}>Status</TableCell>
                <TableCell sx={{ fontSize: '0.69rem', py: 0.75 }}>Score</TableCell>
                {method !== 'existence' && <TableCell sx={{ fontSize: '0.69rem', py: 0.75 }}>Coverage</TableCell>}
                {method !== 'existence' && <TableCell sx={{ fontSize: '0.69rem', py: 0.75 }}>Missing</TableCell>}
                {method === 'existence' && <TableCell sx={{ fontSize: '0.69rem', py: 0.75 }}>Present</TableCell>}
                {method === 'existence' && <TableCell sx={{ fontSize: '0.69rem', py: 0.75 }}>Missing</TableCell>}
              </TableRow>
            </TableHead>
            <TableBody>
              {results.map(r => (
                <TableRow key={r.id} sx={{ '&:hover': { bgcolor: 'rgba(255,255,255,0.02)' } }}>
                  <TableCell sx={{ py: 0.5 }}>
                    <Typography sx={{ fontSize: '0.72rem', fontFamily: 'monospace' }}>{r.control_group_code}</Typography>
                    <Typography sx={{ fontSize: '0.65rem', color: 'text.disabled' }}>{r.control_group_name}</Typography>
                  </TableCell>
                  <TableCell sx={{ py: 0.5 }}>
                    <Chip
                      label={STATUS_LABEL[r.qa_status] ?? r.qa_status}
                      size="small"
                      sx={{ height: 18, fontSize: '0.62rem', bgcolor: `${STATUS_COLOR[r.qa_status] ?? '#9E9E9E'}18`, color: STATUS_COLOR[r.qa_status] ?? '#9E9E9E' }}
                    />
                  </TableCell>
                  <TableCell sx={{ py: 0.5, fontSize: '0.72rem' }}>
                    {(r.correlation_strength * 100).toFixed(0)}%
                  </TableCell>
                  <TableCell sx={{ py: 0.5 }}>
                    <Typography sx={{ fontSize: '0.68rem', color: '#4CAF50' }}>
                      {r.coverage_keywords.join(', ') || '—'}
                    </Typography>
                  </TableCell>
                  <TableCell sx={{ py: 0.5 }}>
                    <Typography sx={{ fontSize: '0.68rem', color: r.missing_keywords.length ? '#f44336' : 'text.disabled' }}>
                      {r.missing_keywords.join(', ') || '—'}
                    </Typography>
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      ) : null}
    </Box>
  )
}

// ── Main page ──────────────────────────────────────────────────────────────────
export default function ProjectDetail() {
  const { id } = useParams<{ id: string }>()
  const navigate = useNavigate()
  const [tab, setTab] = useState(0)
  const { activeProjectId, setActiveProject } = useProject()

  const { data: project, isLoading } = useQuery({
    queryKey: ['project', id],
    queryFn: () => projectsApi.get(id!),
    enabled: !!id,
  })

  const { data: policies } = useQuery({
    queryKey: ['project-policies', id],
    queryFn: () => projectsApi.listPolicies(id!),
    enabled: !!id,
  })

  const { data: impls } = useQuery({
    queryKey: ['project-impls', id],
    queryFn: () => projectsApi.listImpls(id!),
    enabled: !!id,
  })

  if (isLoading || !project) {
    return <Box sx={{ py: 4, textAlign: 'center' }}><CircularProgress /></Box>
  }

  const fam = project.product_family
  const color = FAMILY_COLOR[fam] ?? '#4472C4'
  const policyCodes = (policies ?? []).map(p => p.control_group_code ?? '')
  const implCodes = (impls ?? []).map(i => i.control_group_code ?? '')

  return (
    <Box>
      {/* Breadcrumb */}
      <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 2 }}>
        <IconButton size="small" onClick={() => navigate('/projects')} sx={{ color: 'text.secondary' }}>
          <ArrowBackOutlined fontSize="small" />
        </IconButton>
        <Typography variant="caption" color="text.secondary" sx={{ cursor: 'pointer', '&:hover': { color: 'text.primary' } }} onClick={() => navigate('/projects')}>
          Projects
        </Typography>
        <Typography variant="caption" color="text.disabled">/</Typography>
        <Typography variant="caption" color="text.primary" sx={{ fontWeight: 600 }}>{project.name}</Typography>
      </Box>

      <PageHeader
        title={project.name}
        subtitle={project.organisation_name ?? undefined}
        actions={
          <Box sx={{ display: 'flex', gap: 1, alignItems: 'center' }}>
            <Chip
              label={fam}
              size="small"
              sx={{ height: 22, fontSize: '0.69rem', bgcolor: `${color}18`, color, border: `1px solid ${color}40` }}
            />
            <Chip
              label={project.status}
              size="small"
              sx={{ height: 22, fontSize: '0.69rem', bgcolor: project.status === 'active' ? '#4CAF5018' : '#9E9E9E18', color: project.status === 'active' ? '#4CAF50' : '#9E9E9E' }}
            />
            {activeProjectId === project.id ? (
              <Button size="small" variant="outlined" color="inherit" onClick={() => setActiveProject(null)} sx={{ fontSize: '0.72rem', py: 0.25 }}>
                Deactivate
              </Button>
            ) : (
              <Button size="small" variant="contained" onClick={() => setActiveProject(project)} sx={{ fontSize: '0.72rem', py: 0.25, bgcolor: color, '&:hover': { bgcolor: `${color}cc` } }}>
                Set Active
              </Button>
            )}
          </Box>
        }
      />

      {/* Completeness + metric row */}
      <Grid container spacing={2} sx={{ mb: 3 }}>
        <Grid item xs={12} md={6}>
          <CompletenessPanel
            productFamily={fam}
            policyCodes={policyCodes}
            implCodes={implCodes}
          />
        </Grid>
        <Grid item xs={12} md={6}>
          <Grid container spacing={1.5} sx={{ height: '100%' }}>
            {[
              { label: 'Policies', val: project.policy_count, color: '#4472C4' },
              { label: 'Implementations', val: project.implementation_count, color: '#ED7D31' },
              { label: 'Checklists', val: project.checklist_count, color: '#70AD47' },
            ].map(({ label, val, color: c }) => (
              <Grid item xs={4} key={label}>
                <Box sx={{ p: 1.5, border: '1px solid', borderColor: 'divider', borderRadius: 1.5, textAlign: 'center', height: '100%', display: 'flex', flexDirection: 'column', justifyContent: 'center' }}>
                  <Typography variant="h4" sx={{ fontWeight: 700, color: c, lineHeight: 1, mb: 0.25 }}>{val}</Typography>
                  <Typography variant="caption" color="text.secondary" sx={{ fontSize: '0.67rem' }}>{label}</Typography>
                </Box>
              </Grid>
            ))}
          </Grid>
        </Grid>
      </Grid>

      {/* Document Variables */}
      <DocVarsPanel projectId={id!} initial={project.doc_vars ?? null} />

      {/* Tabs */}
      {(() => {
        const checklistsDisabled = fam === 'ISMS' && project.project_subtype !== 'op'
        return (
          <Box sx={{ borderBottom: 1, borderColor: 'divider', mb: 2.5 }}>
            <Tabs value={tab} onChange={(_, v) => setTab(v)} sx={{ minHeight: 36, '& .MuiTab-root': { minHeight: 36, fontSize: '0.8rem', textTransform: 'none' } }}>
              <Tab label={`Policies (${project.policy_count})`} />
              <Tab label={`Implementations (${project.implementation_count})`} />
              <Tab
                label={`Checklists (${project.checklist_count})`}
                disabled={checklistsDisabled}
                title={checklistsDisabled ? 'SCR Checklists are only available for ISMS Operational (OP) projects' : undefined}
                sx={checklistsDisabled ? { opacity: 0.4 } : {}}
              />
              <Tab label="Gaps" icon={<FindInPageOutlined sx={{ fontSize: 15 }} />} iconPosition="start" />
              <Tab label="Evidence" icon={<UploadFileOutlined sx={{ fontSize: 15 }} />} iconPosition="start" />
              <Tab label="Assessments" icon={<AssignmentOutlined sx={{ fontSize: 15 }} />} iconPosition="start" />
              <Tab label="Compliance" icon={<ShieldOutlined sx={{ fontSize: 15 }} />} iconPosition="start" />
              <Tab label="QA" icon={<VerifiedOutlined sx={{ fontSize: 15 }} />} iconPosition="start" />
            </Tabs>
          </Box>
        )
      })()}

      {tab === 0 && <PoliciesTab projectId={id!} productFamily={fam} />}
      {tab === 1 && <ImplementationsTab projectId={id!} />}
      {tab === 2 && <ChecklistsTab projectId={id!} />}
      {tab === 3 && <GapsTab projectId={id!} productFamily={fam} />}
      {tab === 4 && <EvidenceTab projectId={id!} />}
      {tab === 5 && <PlatformAssessmentsTab productFamily={fam} />}
      {tab === 6 && <AssessmentsTab projectId={id!} />}
      {tab === 7 && <QATab projectId={id!} />}
    </Box>
  )
}
