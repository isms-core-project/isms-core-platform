import { useState } from 'react'
import { useProduct, PRODUCT_SUBTITLES, PRODUCT_COLORS } from '../store/ProductContext'
import {
  Box, Card, CardContent, Typography, Chip, Skeleton, Alert,
  Button, IconButton, Tooltip, Collapse, Table, TableBody,
  TableCell, TableContainer, TableHead, TableRow, LinearProgress,
  Dialog, DialogTitle, DialogContent, DialogActions,
  FormControl, InputLabel, Select, MenuItem,
  TextField, InputAdornment,
} from '@mui/material'
import {
  AddOutlined, DeleteOutlined, AssignmentOutlined,
  FolderOpenOutlined, ExpandMoreOutlined, ExpandLessOutlined,
  SearchOutlined, PersonOutlined, CalendarTodayOutlined,
  FlagOutlined, OpenInNewOutlined,
} from '@mui/icons-material'
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { useNavigate } from 'react-router-dom'
import { assessmentsApi, AssessmentListItem } from '../api/assessmentsApi'
import { controlsApi } from '../api/controls'
import PageHeader from '../components/PageHeader'
import AssessmentFormDrawer from '../components/AssessmentFormDrawer'

// ── Status helpers ─────────────────────────────────────────────────────────

type AssessmentStatus = 'not_started' | 'in_progress' | 'complete'

function getStatus(a: AssessmentListItem): AssessmentStatus {
  if (a.items_total === 0) return 'not_started'
  if (a.overall_score != null && a.overall_score >= 80) return 'complete'
  return 'in_progress'
}

const STATUS_STYLE: Record<AssessmentStatus, { label: string; bg: string; color: string }> = {
  not_started: { label: 'Not Started', bg: 'rgba(255,255,255,0.06)',  color: '#888' },
  in_progress:  { label: 'In Progress', bg: 'rgba(255,192,0,0.12)',   color: '#FFC000' },
  complete:     { label: 'Complete',    bg: 'rgba(198,239,206,0.15)', color: '#C6EFCE' },
}

function StatusChipLocal({ a }: { a: AssessmentListItem }) {
  const s = STATUS_STYLE[getStatus(a)]
  return <Chip label={s.label} size="small" sx={{ fontSize: '0.65rem', height: 18, bgcolor: s.bg, color: s.color, fontWeight: 600 }} />
}

function isPlatform(a: AssessmentListItem) {
  return a.file_path === 'platform:webui' || a.document_id.startsWith('ISMS-ASS-')
}

// ── Compliance bar ─────────────────────────────────────────────────────────

function ComplianceBar({ a }: { a: AssessmentListItem }) {
  const { items_total: total, items_compliant: compliant, items_partial: partial, items_non_compliant: nonCompliant, items_na: na } = a
  if (!total) return <Typography variant="caption" color="text.disabled">No items yet</Typography>
  return (
    <Box>
      <Box sx={{ display: 'flex', height: 5, borderRadius: 2.5, overflow: 'hidden', bgcolor: 'rgba(255,255,255,0.06)' }}>
        {(compliant ?? 0) > 0 && <Box sx={{ flex: compliant, bgcolor: '#C6EFCE' }} />}
        {(partial  ?? 0) > 0 && <Box sx={{ flex: partial,   bgcolor: '#FFEB9C' }} />}
        {(nonCompliant ?? 0) > 0 && <Box sx={{ flex: nonCompliant, bgcolor: '#FFC7CE' }} />}
        {(na ?? 0) > 0 && <Box sx={{ flex: na, bgcolor: '#444' }} />}
      </Box>
      <Box sx={{ display: 'flex', gap: 1.5, mt: 0.4, flexWrap: 'wrap' }}>
        <Typography variant="caption" color="text.disabled">{total} items</Typography>
        {a.overall_score != null && (
          <Typography variant="caption" sx={{ color: '#9DC3E6', fontWeight: 600 }}>{a.overall_score}%</Typography>
        )}
      </Box>
    </Box>
  )
}

// ── Platform assessment card ───────────────────────────────────────────────

function PlatformCard({ a, onDelete, onOpen }: {
  a: AssessmentListItem
  onDelete: () => void
  onOpen: () => void
}) {
  const navigate = useNavigate()
  const meta = a.summary ?? {}

  return (
    <Card sx={{ mb: 1.5, bgcolor: 'rgba(68,114,196,0.05)', border: '1px solid rgba(68,114,196,0.12)', '&:hover': { borderColor: 'rgba(68,114,196,0.25)' } }}>
      <CardContent sx={{ p: '12px 16px !important' }}>
        <Box sx={{ display: 'flex', alignItems: 'flex-start', gap: 1.5 }}>

          {/* Left: core info */}
          <Box sx={{ flex: 1, minWidth: 0 }}>
            <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 0.5, flexWrap: 'wrap' }}>
              <Typography variant="caption" sx={{ fontFamily: 'monospace', color: 'primary.light', fontSize: '0.7rem' }}>
                {a.document_id}
              </Typography>
              <StatusChipLocal a={a} />
              <Chip label={a.product_type} size="small" sx={{ fontSize: '0.6rem', height: 16,
                bgcolor: a.product_type === 'framework' ? 'rgba(68,114,196,0.15)'
                  : a.product_type === 'privacy' ? `${PRODUCT_COLORS.privacy}22`
                  : a.product_type === 'cloud'   ? `${PRODUCT_COLORS.cloud}22`
                  : 'rgba(112,173,71,0.15)',
                color: a.product_type === 'framework' ? '#4472C4'
                  : a.product_type === 'privacy' ? PRODUCT_COLORS.privacy
                  : a.product_type === 'cloud'   ? PRODUCT_COLORS.cloud
                  : '#70AD47' }} />
            </Box>

            <Typography
              variant="body2" fontWeight={700} sx={{ cursor: 'pointer', '&:hover': { color: 'primary.light' } }}
              onClick={() => navigate(`/controls/${a.control_group_id}`)}
            >
              {a.workbook_name}
            </Typography>
            <Typography variant="caption" color="text.secondary">
              {a.group_code.toUpperCase()} — {a.group_name}
            </Typography>

            {/* Metadata row */}
            <Box sx={{ display: 'flex', gap: 2, mt: 1, flexWrap: 'wrap' }}>
              {meta.assessor && (
                <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.4 }}>
                  <PersonOutlined sx={{ fontSize: 12, color: 'text.disabled' }} />
                  <Typography variant="caption" color="text.secondary">{meta.assessor}</Typography>
                </Box>
              )}
              {meta.purpose && (
                <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.4 }}>
                  <FlagOutlined sx={{ fontSize: 12, color: 'text.disabled' }} />
                  <Typography variant="caption" color="text.secondary">{meta.purpose}</Typography>
                </Box>
              )}
              {meta.target_date && (
                <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.4 }}>
                  <CalendarTodayOutlined sx={{ fontSize: 12, color: 'text.disabled' }} />
                  <Typography variant="caption" color="text.secondary">Due {meta.target_date}</Typography>
                </Box>
              )}
              {meta.scope && (
                <Typography variant="caption" color="text.disabled" sx={{ fontStyle: 'italic' }} noWrap>
                  {meta.scope}
                </Typography>
              )}
            </Box>

            <Box sx={{ mt: 1 }}>
              <ComplianceBar a={a} />
            </Box>
          </Box>

          {/* Right: actions */}
          <Box sx={{ display: 'flex', flexDirection: 'column', gap: 0.5, flexShrink: 0 }}>
            <Tooltip title="Open assessment">
              <IconButton size="small" onClick={onOpen}
                sx={{ color: 'primary.light', bgcolor: 'rgba(68,114,196,0.1)', '&:hover': { bgcolor: 'rgba(68,114,196,0.2)' } }}>
                <OpenInNewOutlined sx={{ fontSize: 16 }} />
              </IconButton>
            </Tooltip>
            <Tooltip title="Delete">
              <IconButton size="small" onClick={onDelete}
                sx={{ color: 'error.main', opacity: 0.4, '&:hover': { opacity: 1 } }}>
                <DeleteOutlined sx={{ fontSize: 16 }} />
              </IconButton>
            </Tooltip>
          </Box>
        </Box>
      </CardContent>
    </Card>
  )
}

// ── Main page ──────────────────────────────────────────────────────────────

export default function Assessments() {
  const navigate = useNavigate()
  const queryClient = useQueryClient()
  const { product, ismsTier } = useProduct()

  // Platform section state
  const [statusFilter, setStatusFilter] = useState<'' | AssessmentStatus>('')
  const [deleteTarget, setDeleteTarget] = useState<{ id: string; name: string } | null>(null)
  const [drawerGroup, setDrawerGroup] = useState<{ code: string; name: string; product: string; generatorId?: string } | null>(null)
  const [newDialogOpen, setNewDialogOpen] = useState(false)
  const [selectedProduct, setSelectedProduct] = useState<'framework' | 'operational'>(
    ismsTier === 'operational' ? 'operational' : 'framework'
  )
  const [selectedGroupCode, setSelectedGroupCode] = useState('')
  const [selectedGeneratorId, setSelectedGeneratorId] = useState('')

  // Library section state
  const [libOpen, setLibOpen] = useState(false)
  const [libSearch, setLibSearch] = useState('')

  const isIsms = product === 'isms'

  const { data: all = [], isLoading } = useQuery({
    queryKey: ['assessments', product],
    queryFn: () => assessmentsApi.list({ product_family: product.toUpperCase() }),
  })

  const { data: groups = [] } = useQuery({
    queryKey: ['control-groups-new-dialog', isIsms ? selectedProduct : product],
    queryFn: () => isIsms
      ? controlsApi.list({ product: selectedProduct })
      : controlsApi.list({ product_family: product.toUpperCase() }),
    enabled: newDialogOpen,
  })

  const { data: generatorsForGroup = [] } = useQuery({
    queryKey: ['generators-for-group', selectedGroupCode],
    queryFn: () => assessmentsApi.getGeneratorsForGroup(selectedGroupCode),
    enabled: newDialogOpen && !!selectedGroupCode && selectedProduct === 'framework',
  })

  const deleteMutation = useMutation({
    mutationFn: (id: string) => assessmentsApi.deleteAssessment(id),
    onSuccess: () => {
      setDeleteTarget(null)
      queryClient.invalidateQueries({ queryKey: ['assessments'] })
    },
  })

  const platform = all.filter(isPlatform)
  const library  = all.filter(a => !isPlatform(a))

  function matchesTier(productType: string) {
    if (product !== 'isms' || ismsTier === 'all') return true
    return productType === ismsTier
  }

  const filteredPlatform = platform.filter(a =>
    matchesTier(a.product_type) && (!statusFilter || getStatus(a) === statusFilter)
  )

  const filteredLibrary = library.filter(a => {
    if (product !== 'isms' && a.product_type !== product) return false
    if (!matchesTier(a.product_type)) return false
    if (libSearch) {
      const q = libSearch.toLowerCase()
      return a.document_id.toLowerCase().includes(q) ||
             a.workbook_name.toLowerCase().includes(q) ||
             a.group_code.toLowerCase().includes(q)
    }
    return true
  })

  const tierPlatform = platform.filter(a => matchesTier(a.product_type))
  const notStarted  = tierPlatform.filter(a => getStatus(a) === 'not_started').length
  const inProgress  = tierPlatform.filter(a => getStatus(a) === 'in_progress').length
  const complete    = tierPlatform.filter(a => getStatus(a) === 'complete').length

  // Auto-select generator when only one exists for the group
  const needsGeneratorPick = selectedGroupCode && selectedProduct === 'framework' && generatorsForGroup.length > 1
  const autoGeneratorId = generatorsForGroup.length === 1 ? generatorsForGroup[0].document_id : undefined

  function handleNewFromDialog() {
    const g = groups.find(g => g.group_code === selectedGroupCode)
    if (!g) return
    // If multiple generators and none selected yet, don't proceed
    if (needsGeneratorPick && !selectedGeneratorId) return
    const genId = selectedGeneratorId || autoGeneratorId
    setNewDialogOpen(false)
    setSelectedGroupCode('')
    setSelectedGeneratorId('')
    setDrawerGroup({ code: g.group_code, name: g.group_name, product: isIsms ? selectedProduct : product, generatorId: genId })
  }

  return (
    <Box>
      <PageHeader
        title="Assessments"
        subtitle={`${product !== 'isms' ? PRODUCT_SUBTITLES[product] + ' · ' : ''}Platform assessments and workbook library`}
        actions={
          <Button variant="contained" size="small" startIcon={<AddOutlined />}
            onClick={() => setNewDialogOpen(true)} sx={{ fontSize: '0.78rem' }}>
            New Assessment
          </Button>
        }
      />

      {/* ── Platform Assessments ── */}
      <Box sx={{ mb: 4 }}>
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 1.5, mb: 2, flexWrap: 'wrap' }}>
          <AssignmentOutlined sx={{ fontSize: 18, color: 'primary.light' }} />
          <Typography variant="subtitle2" fontWeight={700} color="primary.light">
            Platform Assessments
          </Typography>
          <Chip label={tierPlatform.length} size="small" sx={{ fontSize: '0.65rem', height: 18 }} />

          {/* Status summary pills — clickable filter */}
          <Box sx={{ display: 'flex', gap: 0.75, ml: 1 }}>
            {([
              { key: '' as const,           label: 'All',          count: tierPlatform.length, bg: 'rgba(255,255,255,0.07)', color: 'text.secondary' },
              { key: 'not_started' as const, label: 'Not Started', count: notStarted,      bg: 'rgba(255,255,255,0.06)', color: '#888' },
              { key: 'in_progress' as const, label: 'In Progress', count: inProgress,      bg: 'rgba(255,192,0,0.12)',   color: '#FFC000' },
              { key: 'complete' as const,    label: 'Complete',    count: complete,        bg: 'rgba(198,239,206,0.15)', color: '#C6EFCE' },
            ]).map(({ key, label, count, bg, color }) => (
              <Chip
                key={key}
                label={`${label} ${count}`}
                size="small"
                onClick={() => setStatusFilter(key)}
                sx={{
                  fontSize: '0.65rem', height: 20, cursor: 'pointer',
                  bgcolor: statusFilter === key ? bg : 'transparent',
                  color: statusFilter === key ? color : 'text.disabled',
                  border: '1px solid',
                  borderColor: statusFilter === key ? color + '40' : 'rgba(255,255,255,0.08)',
                  fontWeight: statusFilter === key ? 700 : 400,
                  '&:hover': { bgcolor: bg, color },
                }}
              />
            ))}
          </Box>
        </Box>

        {isLoading && <Skeleton variant="rectangular" height={80} sx={{ borderRadius: 2 }} />}

        {!isLoading && tierPlatform.length === 0 && (
          <Box
            onClick={() => setNewDialogOpen(true)}
            sx={{
              p: 3, borderRadius: 2, textAlign: 'center', cursor: 'pointer',
              border: '1px dashed rgba(68,114,196,0.3)', bgcolor: 'rgba(68,114,196,0.03)',
              '&:hover': { bgcolor: 'rgba(68,114,196,0.07)', borderColor: 'rgba(68,114,196,0.5)' },
            }}
          >
            <AddOutlined sx={{ color: 'text.disabled', mb: 0.5 }} />
            <Typography variant="body2" color="text.secondary">
              No platform assessments yet — fill in your data directly, no Excel required.
            </Typography>
            <Typography variant="caption" color="primary.light" sx={{ mt: 0.5, display: 'block' }}>
              Click to start a new assessment
            </Typography>
          </Box>
        )}

        {!isLoading && tierPlatform.length > 0 && filteredPlatform.length === 0 && (
          <Alert severity="info">No assessments match the selected status filter.</Alert>
        )}

        {filteredPlatform.map((a) => (
          <PlatformCard
            key={a.id}
            a={a}
            onDelete={() => setDeleteTarget({ id: a.id, name: a.workbook_name })}
            onOpen={() => navigate(`/controls/${a.control_group_id}`)}
          />
        ))}
      </Box>

      {/* ── Workbook Library ── */}
      <Box>
        <Box
          onClick={() => setLibOpen(v => !v)}
          sx={{ display: 'flex', alignItems: 'center', gap: 1, cursor: 'pointer', mb: libOpen ? 1.5 : 0,
                py: 1, px: 1.5, borderRadius: 1.5, bgcolor: 'rgba(255,255,255,0.03)',
                border: '1px solid rgba(255,255,255,0.07)',
                '&:hover': { bgcolor: 'rgba(255,255,255,0.06)' } }}
        >
          <FolderOpenOutlined sx={{ fontSize: 16, color: 'text.secondary' }} />
          <Typography variant="caption" fontWeight={700} color="text.secondary"
            sx={{ textTransform: 'uppercase', letterSpacing: '0.06em', fontSize: '0.7rem', flex: 1 }}>
            Workbook Library
          </Typography>
          <Chip label={filteredLibrary.length} size="small" sx={{ fontSize: '0.6rem', height: 16 }} />
          {libOpen ? <ExpandLessOutlined sx={{ fontSize: 16, color: 'text.disabled' }} /> : <ExpandMoreOutlined sx={{ fontSize: 16, color: 'text.disabled' }} />}
        </Box>

        <Collapse in={libOpen}>
          {/* Library filters */}
          <Box sx={{ display: 'flex', gap: 2, mb: 1.5, flexWrap: 'wrap', alignItems: 'center' }}>
            <TextField size="small" placeholder="Search workbooks…" value={libSearch}
              onChange={e => setLibSearch(e.target.value)} sx={{ flex: 1, minWidth: 200 }}
              InputProps={{ startAdornment: <InputAdornment position="start"><SearchOutlined sx={{ fontSize: 16, color: 'text.secondary' }} /></InputAdornment> }} />
          </Box>

          <TableContainer component={Card}>
            <Table size="small">
              <TableHead>
                <TableRow>
                  <TableCell>Control Group</TableCell>
                  <TableCell>Workbook</TableCell>
                  <TableCell sx={{ width: 90 }}>Product</TableCell>
                  <TableCell sx={{ width: 60, textAlign: 'center' }}>Sheets</TableCell>
                  <TableCell sx={{ width: 220 }}>Compliance</TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {filteredLibrary.map((a) => (
                  <TableRow key={a.id} hover sx={{ cursor: 'pointer' }}
                    onClick={() => navigate(`/controls/${a.control_group_id}`)}>
                    <TableCell>
                      <Typography variant="caption" sx={{ fontFamily: 'monospace', color: 'primary.light', fontWeight: 700 }}>
                        {a.group_code.toUpperCase()}
                      </Typography>
                      <Typography variant="caption" color="text.secondary" sx={{ display: 'block', lineHeight: 1.3 }}>
                        {a.group_name}
                      </Typography>
                    </TableCell>
                    <TableCell>
                      <Typography variant="caption" sx={{ fontFamily: 'monospace', color: 'text.secondary', fontSize: '0.68rem' }}>
                        {a.document_id}
                      </Typography>
                      <Typography variant="body2" fontWeight={600} sx={{ lineHeight: 1.3 }}>{a.workbook_name}</Typography>
                    </TableCell>
                    <TableCell>
                      <Chip label={a.product_type} size="small" sx={{ fontSize: '0.65rem', height: 18,
                        bgcolor: a.product_type === 'framework' ? 'rgba(68,114,196,0.15)'
                          : a.product_type === 'privacy' ? `${PRODUCT_COLORS.privacy}22`
                          : a.product_type === 'cloud'   ? `${PRODUCT_COLORS.cloud}22`
                          : 'rgba(112,173,71,0.15)',
                        color: a.product_type === 'framework' ? '#4472C4'
                          : a.product_type === 'privacy' ? PRODUCT_COLORS.privacy
                          : a.product_type === 'cloud'   ? PRODUCT_COLORS.cloud
                          : '#70AD47' }} />
                    </TableCell>
                    <TableCell align="center">
                      <Typography variant="caption">{a.sheets_count}</Typography>
                    </TableCell>
                    <TableCell>
                      {(a.items_total ?? 0) > 0 ? (
                        <Box sx={{ display: 'flex', height: 5, borderRadius: 2.5, overflow: 'hidden', bgcolor: 'rgba(255,255,255,0.06)' }}>
                          {(a.items_compliant ?? 0) > 0 && <Box sx={{ flex: a.items_compliant, bgcolor: '#C6EFCE' }} />}
                          {(a.items_partial ?? 0) > 0 && <Box sx={{ flex: a.items_partial, bgcolor: '#FFEB9C' }} />}
                          {(a.items_non_compliant ?? 0) > 0 && <Box sx={{ flex: a.items_non_compliant, bgcolor: '#FFC7CE' }} />}
                          {(a.items_na ?? 0) > 0 && <Box sx={{ flex: a.items_na, bgcolor: '#444' }} />}
                        </Box>
                      ) : (
                        <Typography variant="caption" color="text.disabled">No items</Typography>
                      )}
                    </TableCell>
                  </TableRow>
                ))}
                {filteredLibrary.length === 0 && (
                  <TableRow>
                    <TableCell colSpan={5} align="center">
                      <Typography variant="body2" color="text.secondary" sx={{ py: 2 }}>
                        No workbooks match the current filters.
                      </Typography>
                    </TableCell>
                  </TableRow>
                )}
              </TableBody>
            </Table>
          </TableContainer>
        </Collapse>
      </Box>

      {/* ── Select product + control group dialog ── */}
      <Dialog open={newDialogOpen} onClose={() => { setNewDialogOpen(false); setSelectedGroupCode('') }} maxWidth="xs" fullWidth>
        <DialogTitle>New Assessment</DialogTitle>
        <DialogContent sx={{ pt: '8px !important', display: 'flex', flexDirection: 'column', gap: 2 }}>

          {/* Step 1 — product type (ISMS only: Framework vs Operational) */}
          {isIsms ? (
            <Box>
              <Typography variant="caption" color="text.secondary" sx={{ display: 'block', mb: 1 }}>
                Assessment type
              </Typography>
              <Box sx={{ display: 'flex', gap: 1 }}>
                {(['framework', 'operational'] as const).map((p) => {
                  const active = selectedProduct === p
                  return (
                    <Box
                      key={p}
                      onClick={() => { setSelectedProduct(p); setSelectedGroupCode('') }}
                      sx={{
                        flex: 1, p: 1.5, borderRadius: 2, cursor: 'pointer', textAlign: 'center',
                        border: '1px solid',
                        borderColor: active ? (p === 'framework' ? 'rgba(68,114,196,0.6)' : 'rgba(112,173,71,0.6)') : 'rgba(255,255,255,0.1)',
                        bgcolor: active ? (p === 'framework' ? 'rgba(68,114,196,0.12)' : 'rgba(112,173,71,0.1)') : 'transparent',
                        '&:hover': { borderColor: p === 'framework' ? 'rgba(68,114,196,0.5)' : 'rgba(112,173,71,0.5)' },
                      }}
                    >
                      <Box sx={{ width: 8, height: 8, borderRadius: '50%', bgcolor: p === 'framework' ? '#4472C4' : '#70AD47', mx: 'auto', mb: 0.5 }} />
                      <Typography variant="body2" fontWeight={active ? 700 : 400}
                        color={active ? (p === 'framework' ? 'primary.light' : '#70AD47') : 'text.secondary'}>
                        {p === 'framework' ? 'Framework' : 'Operational'}
                      </Typography>
                      <Typography variant="caption" color="text.disabled" sx={{ fontSize: '0.62rem' }}>
                        {p === 'framework' ? 'ISO 27001 full controls' : 'Simplified operational'}
                      </Typography>
                    </Box>
                  )
                })}
              </Box>
            </Box>
          ) : (
            <Box sx={{
              p: 1.5, borderRadius: 2, textAlign: 'center',
              border: `1px solid ${product === 'privacy' ? 'rgba(180,120,255,0.4)' : 'rgba(41,182,246,0.4)'}`,
              bgcolor: product === 'privacy' ? 'rgba(180,120,255,0.08)' : 'rgba(41,182,246,0.08)',
            }}>
              <Typography variant="body2" fontWeight={700}
                color={product === 'privacy' ? '#B478FF' : '#29B6F6'}>
                {product === 'privacy' ? 'Privacy' : 'Cloud'}
              </Typography>
              <Typography variant="caption" color="text.disabled" sx={{ fontSize: '0.62rem' }}>
                {product === 'privacy' ? 'ISO 27701:2025 privacy controls' : 'ISO 27018:2025 cloud controls'}
              </Typography>
            </Box>
          )}

          {/* Step 2 — control group */}
          <FormControl size="small" fullWidth>
            <InputLabel>Control Group</InputLabel>
            <Select
              value={selectedGroupCode}
              onChange={e => { setSelectedGroupCode(e.target.value); setSelectedGeneratorId('') }}
              label="Control Group"
            >
              <MenuItem value=""><em>Select…</em></MenuItem>
              {groups.map(g => (
                <MenuItem key={g.group_code} value={g.group_code}>
                  <Typography component="span" sx={{ fontFamily: 'monospace', fontSize: '0.75rem', color: 'primary.light', mr: 1 }}>
                    {g.group_code.toUpperCase()}
                  </Typography>
                  {g.group_name}
                </MenuItem>
              ))}
            </Select>
          </FormControl>

          {/* Step 3 — IMP / workbook picker (only for stacked/multi-generator groups) */}
          {needsGeneratorPick && (
            <Box>
              <Typography variant="caption" color="text.secondary" sx={{ display: 'block', mb: 1 }}>
                Select assessment workbook
              </Typography>
              <Box sx={{ display: 'flex', flexDirection: 'column', gap: 0.75 }}>
                {generatorsForGroup.map((gen) => {
                  const active = selectedGeneratorId === gen.document_id
                  return (
                    <Box
                      key={gen.document_id}
                      onClick={() => setSelectedGeneratorId(gen.document_id)}
                      sx={{
                        p: 1.25, borderRadius: 1.5, cursor: 'pointer',
                        border: '1px solid',
                        borderColor: active ? 'rgba(68,114,196,0.6)' : 'rgba(255,255,255,0.08)',
                        bgcolor: active ? 'rgba(68,114,196,0.12)' : 'transparent',
                        '&:hover': { borderColor: 'rgba(68,114,196,0.4)', bgcolor: 'rgba(68,114,196,0.06)' },
                      }}
                    >
                      <Box sx={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between' }}>
                        <Typography variant="body2" fontWeight={active ? 700 : 400} color={active ? 'primary.light' : 'text.primary'}>
                          {gen.workbook_name}
                        </Typography>
                        <Typography variant="caption" color="text.disabled">{gen.sheet_count} sheets</Typography>
                      </Box>
                      <Typography variant="caption" sx={{ fontFamily: 'monospace', color: 'text.disabled', fontSize: '0.65rem' }}>
                        {gen.document_id}
                      </Typography>
                    </Box>
                  )
                })}
              </Box>
            </Box>
          )}

        </DialogContent>
        <DialogActions sx={{ px: 3, pb: 2 }}>
          <Button onClick={() => { setNewDialogOpen(false); setSelectedGroupCode(''); setSelectedGeneratorId('') }}>Cancel</Button>
          <Button variant="contained"
            disabled={!selectedGroupCode || (needsGeneratorPick && !selectedGeneratorId)}
            onClick={handleNewFromDialog}>
            Continue
          </Button>
        </DialogActions>
      </Dialog>

      {/* ── Delete confirm ── */}
      <Dialog open={!!deleteTarget} onClose={() => setDeleteTarget(null)} maxWidth="xs" fullWidth>
        <DialogTitle>Delete Platform Assessment?</DialogTitle>
        <DialogContent>
          <Typography variant="body2">
            <strong>{deleteTarget?.name}</strong> and all its data will be permanently removed.
            This cannot be undone.
          </Typography>
          {deleteMutation.isError && <Alert severity="error" sx={{ mt: 1.5 }}>Delete failed. Try again.</Alert>}
        </DialogContent>
        <DialogActions sx={{ px: 3, pb: 2 }}>
          <Button onClick={() => setDeleteTarget(null)} disabled={deleteMutation.isPending}>Cancel</Button>
          <Button variant="contained" color="error" disabled={deleteMutation.isPending}
            startIcon={<DeleteOutlined />}
            onClick={() => deleteTarget && deleteMutation.mutate(deleteTarget.id)}>
            {deleteMutation.isPending ? 'Deleting…' : 'Delete'}
          </Button>
        </DialogActions>
      </Dialog>

      {/* ── Assessment Form Drawer ── */}
      {drawerGroup && (
        <AssessmentFormDrawer
          open={!!drawerGroup}
          onClose={() => {
            setDrawerGroup(null)
            queryClient.invalidateQueries({ queryKey: ['assessments'] })
          }}
          groupCode={drawerGroup.code}
          groupName={drawerGroup.name}
          productType={drawerGroup.product}
          generatorId={drawerGroup.generatorId}
        />
      )}
    </Box>
  )
}
