import { useState } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import {
  Box,
  Card,
  CardContent,
  Typography,
  Grid,
  Tab,
  Tabs,
  Chip,
  Skeleton,
  Alert,
  IconButton,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Collapse,
  Tooltip,
  Button,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  LinearProgress,
} from '@mui/material'
import { ArrowBackOutlined, ExpandMoreOutlined, ExpandLessOutlined, AutoAwesomeOutlined, AddOutlined, DeleteOutlined, AssignmentOutlined, FolderOpenOutlined, ExploreOutlined } from '@mui/icons-material'
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { controlsApi } from '../api/controls'
import { assessmentsApi } from '../api/assessmentsApi'
import { useProduct } from '../store/ProductContext'
import StatusChip from '../components/StatusChip'
import AiAssistant from '../components/AiAssistant'
import DocPreviewDrawer from '../components/DocPreviewDrawer'
import AssessmentFormDrawer from '../components/AssessmentFormDrawer'

// Real API shapes
interface PolicyRow {
  id: string
  document_id: string
  title: string
  policy_type: string
  product_type: string
  requirements_count: number
  word_count: number
  source_label?: string | null
}

interface ImplRow {
  id: string
  document_id: string
  title: string
  impl_type: string
  word_count: number
}

interface ItemRow {
  id: string
  row_number: number
  item_text: string | null
  status: string
  owner: string | null
  due_date: string | null
  notes: string | null
}

interface SheetRow {
  id: string
  sheet_name: string
  sheet_type: string
  row_count: number
  items: ItemRow[]
}

interface AssessmentRow {
  id: string
  document_id: string
  workbook_name: string
  file_path: string
  product_type: string
  assessment_type: string
  sheets_count: number
  overall_score: number | null
  items_total: number
  items_compliant: number
  items_partial: number
  items_non_compliant: number
  items_na: number
  sheets: SheetRow[]
}

interface MappingRow {
  framework: string
  framework_code: string
  control_id: string
  control_title: string
  mapping_type: string
  confidence: number
}

interface IsoControlRow {
  control_id: string
  title: string
  description: string | null
  mappings: MappingRow[]
}

interface GapRow {
  id: string
  gap_type: string
  severity: string
  status: string
  description: string
}

interface EvidenceRow {
  id: string
  title: string
  evidence_type: string
  collected_date: string | null
  verified_by: string | null
}

interface RealControlDetail {
  id: string
  group_code: string
  name: string
  section: string
  section_name: string
  is_stacked: boolean
  has_framework: boolean
  has_operational: boolean
  framework_status: string
  operational_status: string
  stacked_control_ids: string[]
  policies: PolicyRow[]
  implementations: ImplRow[]
  assessments: AssessmentRow[]
  iso_controls: IsoControlRow[]
  gaps: GapRow[]
  evidence: EvidenceRow[]
  requirements_total: number
  gaps_open: number
  evidence_total: number
}

function TabPanel({ value, index, children }: { value: number; index: number; children: React.ReactNode }) {
  return value === index ? <Box sx={{ pt: 2 }}>{children}</Box> : null
}

function ComplianceBar({ total, compliant, partial, nonCompliant, na }: {
  total: number; compliant: number; partial: number; nonCompliant: number; na: number
}) {
  if (total === 0) return null
  return (
    <Box sx={{ mt: 1 }}>
      <Box sx={{ display: 'flex', height: 5, borderRadius: 2.5, overflow: 'hidden', bgcolor: 'rgba(255,255,255,0.06)' }}>
        {compliant > 0 && <Box sx={{ flex: compliant, bgcolor: '#C6EFCE' }} />}
        {partial > 0 && <Box sx={{ flex: partial, bgcolor: '#FFEB9C' }} />}
        {nonCompliant > 0 && <Box sx={{ flex: nonCompliant, bgcolor: '#FFC7CE' }} />}
        {na > 0 && <Box sx={{ flex: na, bgcolor: '#444' }} />}
      </Box>
      <Box sx={{ display: 'flex', gap: 1.5, mt: 0.4 }}>
        <Typography variant="caption" color="text.secondary">{total} items</Typography>
        {compliant > 0 && <Typography variant="caption" sx={{ color: '#C6EFCE' }}>{compliant} ✓</Typography>}
        {partial > 0 && <Typography variant="caption" sx={{ color: '#FFEB9C' }}>{partial} ~</Typography>}
        {nonCompliant > 0 && <Typography variant="caption" sx={{ color: '#FFC7CE' }}>{nonCompliant} ✗</Typography>}
        {na > 0 && <Typography variant="caption" color="text.disabled">{na} N/A</Typography>}
      </Box>
    </Box>
  )
}

const ITEM_STATUS_COLOR: Record<string, { bg: string; color: string; label: string }> = {
  compliant:      { bg: 'rgba(198,239,206,0.15)', color: '#C6EFCE', label: '✓' },
  partial:        { bg: 'rgba(255,235,156,0.12)', color: '#FFEB9C', label: '~' },
  non_compliant:  { bg: 'rgba(255,199,206,0.15)', color: '#FFC7CE', label: '✗' },
  na:             { bg: 'rgba(100,100,100,0.12)', color: '#888',    label: 'N/A' },
  not_applicable: { bg: 'rgba(100,100,100,0.12)', color: '#888',    label: 'N/A' },
  not_assessed:   { bg: 'transparent',             color: '#555',    label: '—' },
}

const STATUS_CYCLE = ['not_assessed', 'compliant', 'partial', 'non_compliant', 'na']
function nextStatus(current: string): string {
  const idx = STATUS_CYCLE.indexOf(current)
  return STATUS_CYCLE[(idx === -1 ? 1 : (idx + 1)) % STATUS_CYCLE.length]
}

function ItemStatusDot({ status }: { status: string }) {
  const s = ITEM_STATUS_COLOR[status] ?? ITEM_STATUS_COLOR.not_assessed
  return (
    <Box sx={{
      width: 6, height: 6, borderRadius: '50%', flexShrink: 0, mt: '5px',
      bgcolor: s.color === '#555' ? 'rgba(255,255,255,0.15)' : s.color,
    }} />
  )
}

function SheetItemsTable({ sheet, expanded, onToggle, onStatusChange }: {
  sheet: SheetRow
  expanded: boolean
  onToggle: () => void
  onStatusChange?: (itemId: string, newStatus: string) => void
}) {
  if (sheet.items.length === 0) return null
  return (
    <Box>
      <Box
        sx={{ display: 'flex', alignItems: 'center', gap: 0.5, cursor: 'pointer', py: 0.5, px: 1,
              bgcolor: 'rgba(68,114,196,0.06)', borderRadius: 1, mt: 0.5,
              '&:hover': { bgcolor: 'rgba(68,114,196,0.12)' } }}
        onClick={onToggle}
      >
        {expanded ? <ExpandLessOutlined sx={{ fontSize: 14 }} /> : <ExpandMoreOutlined sx={{ fontSize: 14 }} />}
        <Typography variant="caption" color="text.secondary">
          {sheet.items.length} checklist items
        </Typography>
        <Typography variant="caption" color="text.disabled" sx={{ ml: 'auto', fontSize: '0.6rem' }}>
          click item to cycle status
        </Typography>
      </Box>
      <Collapse in={expanded}>
        <Box sx={{ mt: 0.5 }}>
          {sheet.items.map((item) => {
            const sc = ITEM_STATUS_COLOR[item.status] ?? ITEM_STATUS_COLOR.not_assessed
            return (
              <Box
                key={item.id}
                onClick={() => onStatusChange?.(item.id, nextStatus(item.status))}
                sx={{
                  display: 'flex', gap: 1, py: 0.4, px: 1,
                  borderBottom: '1px solid rgba(255,255,255,0.04)',
                  cursor: onStatusChange ? 'pointer' : 'default',
                  bgcolor: sc.bg,
                  '&:hover': onStatusChange ? { bgcolor: 'rgba(68,114,196,0.08)' } : {},
                  borderLeft: `2px solid ${sc.color}40`,
                }}
              >
                <Typography variant="caption" sx={{ color: sc.color, fontWeight: 700, flexShrink: 0, minWidth: 20 }}>
                  {sc.label}
                </Typography>
                <Typography variant="caption" sx={{ flex: 1, color: 'text.primary', lineHeight: 1.4 }}>
                  {item.item_text ?? '—'}
                </Typography>
                {item.owner && (
                  <Typography variant="caption" color="text.disabled" sx={{ flexShrink: 0 }}>{item.owner}</Typography>
                )}
              </Box>
            )
          })}
        </Box>
      </Collapse>
    </Box>
  )
}

export default function ControlDetail() {
  const { id, code } = useParams<{ id?: string; code?: string }>()
  const identifier = code ?? id!
  const isCode = !!code
  const navigate = useNavigate()
  const queryClient = useQueryClient()
  const { product: productView } = useProduct()
  const [tab, setTab] = useState(0)
  const [expandedSheets, setExpandedSheets] = useState<Set<string>>(new Set())
  const [stackedFilter, setStackedFilter] = useState<string>('all')
  const [aiOpen, setAiOpen] = useState(false)
  const [docPreview, setDocPreview] = useState<{ id: string; docType: 'policy' | 'implementation'; documentId: string; title: string; typeLabel: string; typeColor?: string } | null>(null)
  const [assessmentDrawerOpen, setAssessmentDrawerOpen] = useState(false)
  const [deleteAssessmentTarget, setDeleteAssessmentTarget] = useState<{ id: string; name: string } | null>(null)
  const [generatorPickerOpen, setGeneratorPickerOpen] = useState(false)
  const [pickerGeneratorId, setPickerGeneratorId] = useState('')

  const { data, isLoading, error } = useQuery({
    queryKey: ['control', identifier],
    queryFn: () => isCode ? controlsApi.getByCode(identifier) : controlsApi.getById(identifier),
    enabled: !!identifier,
  })

  const statusMutation = useMutation({
    mutationFn: ({ itemId, status }: { itemId: string; status: string }) =>
      assessmentsApi.patchItem(itemId, status),
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ['control', identifier] }),
  })

  const deleteAssessmentMutation = useMutation({
    mutationFn: (id: string) => assessmentsApi.deleteAssessment(id),
    onSuccess: () => {
      setDeleteAssessmentTarget(null)
      queryClient.invalidateQueries({ queryKey: ['control', identifier] })
    },
  })

  const cg = data as unknown as RealControlDetail | undefined

  const { data: generatorsForGroup = [] } = useQuery({
    queryKey: ['generators-for-group', cg?.group_code ?? ''],
    queryFn: () => assessmentsApi.getGeneratorsForGroup(cg!.group_code),
    enabled: !!cg,
  })
  const needsGeneratorPick = generatorsForGroup.length > 1
  const drawerGeneratorId = needsGeneratorPick ? pickerGeneratorId : (generatorsForGroup[0]?.document_id ?? undefined)

  if (isLoading) {
    return (
      <Box>
        <Skeleton variant="text" width={300} height={40} />
        <Skeleton variant="rectangular" height={200} sx={{ mt: 2, borderRadius: 2 }} />
      </Box>
    )
  }

  if (error || !cg) {
    return <Alert severity="error">Control not found or failed to load.</Alert>
  }

  // Filter content by product view
  // ISMS = show all ISMS content; privacy/cloud = show matching product_type
  // INS docs go to Instructions tab, not Policies
  const visiblePolicies = cg.policies.filter(p =>
    p.policy_type !== 'INS' && (productView === 'isms' || p.product_type === productView)
  )
  const visibleInstructions = cg.policies.filter(p => p.policy_type === 'INS')
  // Implementation model has no product_type — control group ownership is already product-scoped
  const visibleImpls = cg.implementations
  const visibleAssessments = cg.assessments.filter(a =>
    productView === 'isms' || a.product_type === productView
  )

  // Tab index constants — keeps panel assignments readable
  const TAB_POLICIES = 0
  const TAB_INSTRUCTIONS = 1
  const TAB_IMPLEMENTATIONS = 2
  const TAB_ASSESSMENTS = 3
  const TAB_MAPPINGS = 4
  const TAB_EVIDENCE = 5
  const TAB_GAPS = 6

  const tabs = [
    { label: `Policies (${visiblePolicies.length})` },
    ...(visibleInstructions.length > 0 ? [{ label: `Instructions (${visibleInstructions.length})` }] : [{ label: 'Instructions (0)' }]),
    { label: `Implementations (${visibleImpls.length})` },
    { label: `Assessments (${visibleAssessments.length})` },
    { label: `ISO Mappings (${cg.iso_controls.length})` },
    { label: `Evidence (${cg.evidence_total})` },
    ...(cg.gaps.length > 0 ? [{ label: `Gaps (${cg.gaps.length})` }] : []),
  ]

  return (
    <Box>
      {/* Breadcrumb */}
      <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.5, mb: 2 }}>
        <Typography
          variant="caption"
          color="text.secondary"
          sx={{ cursor: 'pointer', '&:hover': { color: 'primary.light' } }}
          onClick={() => navigate('/')}
        >
          Overview
        </Typography>
        <Typography variant="caption" color="text.disabled">›</Typography>
        <Typography
          variant="caption"
          color="text.secondary"
          sx={{ cursor: 'pointer', '&:hover': { color: 'primary.light' } }}
          onClick={() => navigate('/controls')}
        >
          Controls
        </Typography>
        <Typography variant="caption" color="text.disabled">›</Typography>
        <Typography variant="caption" color="primary.light" fontWeight={600}>
          {cg.group_code.toUpperCase()}
        </Typography>
      </Box>

      {/* Header */}
      <Box sx={{ display: 'flex', alignItems: 'flex-start', gap: 1, mb: 3 }}>
        <IconButton size="small" onClick={() => navigate('/controls')} sx={{ mt: 0.25 }}>
          <ArrowBackOutlined fontSize="small" />
        </IconButton>

        <Box sx={{ flex: 1 }}>
          <Box sx={{ display: 'flex', gap: 0.75, alignItems: 'center', mb: 0.5, flexWrap: 'wrap' }}>
            <Typography variant="caption" sx={{ fontFamily: 'monospace', color: 'primary.light', fontWeight: 700, fontSize: '0.8rem' }}>
              {cg.group_code.toUpperCase()}
            </Typography>
            <Chip label={cg.section} size="small" sx={{ fontSize: '0.65rem', height: 18 }} />
            <Chip label={cg.section_name} size="small" sx={{ fontSize: '0.65rem', height: 18 }} />
            {cg.is_stacked && (
              <Chip label={`Stacked: ${cg.stacked_control_ids.join(', ')}`} size="small"
                sx={{ fontSize: '0.65rem', height: 18, bgcolor: 'rgba(255,192,0,0.15)', color: '#FFEB9C' }} />
            )}
            <StatusChip status={cg.framework_status} />
          </Box>
          <Typography variant="h4">{cg.name}</Typography>
        </Box>

        {/* AI button */}
        <Tooltip title="ISMS AI Assistant">
          <IconButton
            size="small"
            onClick={() => setAiOpen((v) => !v)}
            sx={{
              mt: 0.25, flexShrink: 0,
              color: aiOpen ? '#4472C4' : 'text.disabled',
              bgcolor: aiOpen ? 'rgba(68,114,196,0.15)' : 'transparent',
              border: '1px solid',
              borderColor: aiOpen ? 'rgba(68,114,196,0.4)' : 'rgba(255,255,255,0.08)',
              '&:hover': { bgcolor: 'rgba(68,114,196,0.15)', color: '#4472C4' },
            }}
          >
            <AutoAwesomeOutlined fontSize="small" />
          </IconButton>
        </Tooltip>

        {/* Compass button */}
        <Tooltip title="Analyse with ISMS Compass">
          <IconButton
            size="small"
            onClick={() => navigate(`/compass?group=${cg.group_code}`)}
            sx={{
              mt: 0.25, flexShrink: 0,
              color: 'text.disabled',
              border: '1px solid rgba(255,255,255,0.08)',
              '&:hover': { bgcolor: 'rgba(46,139,87,0.15)', color: '#C6EFCE' },
            }}
          >
            <ExploreOutlined fontSize="small" />
          </IconButton>
        </Tooltip>

        {/* Stats */}
        <Box sx={{ display: 'flex', gap: 2.5, flexShrink: 0 }}>
          {[
            { label: 'Policies', value: cg.policies.length },
            { label: 'Impls', value: cg.implementations.length },
            { label: 'Assessments', value: cg.assessments.length },
            { label: 'ISO Controls', value: cg.iso_controls.length },
            { label: 'Evidence', value: cg.evidence_total },
            { label: 'Open Gaps', value: cg.gaps_open },
          ].map(({ label, value }) => (
            <Box key={label} sx={{ textAlign: 'center' }}>
              <Typography variant="h5" color={label === 'Open Gaps' && value > 0 ? 'error.main' : 'primary.light'}>
                {value}
              </Typography>
              <Typography variant="caption" color="text.secondary">{label}</Typography>
            </Box>
          ))}
        </Box>
      </Box>

      {/* Tabs */}
      <Card>
        <Tabs
          value={tab}
          onChange={(_, v) => setTab(v)}
          sx={{ borderBottom: '1px solid', borderColor: 'divider', px: 2 }}
          variant="scrollable"
          scrollButtons="auto"
        >
          {tabs.map((t, i) => <Tab key={i} label={t.label} sx={{ fontSize: '0.8rem' }} />)}
        </Tabs>

        <CardContent>
          {/* Policies */}
          <TabPanel value={tab} index={TAB_POLICIES}>
            {visiblePolicies.length === 0 && <Alert severity="warning">No policies for the selected product.</Alert>}
            {visiblePolicies.map((pol) => {
              const isExternal = pol.product_type === 'external'
              return (
                <Box key={pol.id} onClick={() => setDocPreview({ id: pol.id, docType: 'policy', documentId: pol.document_id, title: pol.title, typeLabel: pol.policy_type, productType: pol.product_type })}
                  sx={{
                    mb: 1.5, p: 1.5, borderRadius: 2, cursor: 'pointer',
                    bgcolor: isExternal ? 'rgba(255,192,0,0.06)' : 'rgba(68,114,196,0.07)',
                    border: isExternal ? '1px solid rgba(255,192,0,0.25)' : '1px solid transparent',
                    '&:hover': { bgcolor: isExternal ? 'rgba(255,192,0,0.12)' : 'rgba(68,114,196,0.14)' },
                  }}
                >
                  {isExternal && (
                    <Typography variant="caption" sx={{ color: '#FFC000', fontWeight: 600, display: 'block', mb: 0.5, fontSize: '0.65rem' }}>
                      External Document{pol.source_label ? ` — ${pol.source_label}` : ''}
                    </Typography>
                  )}
                  <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                    <Box>
                      <Typography variant="caption" sx={{ fontFamily: 'monospace', color: isExternal ? '#FFC000' : 'primary.light' }}>
                        {pol.document_id}
                      </Typography>
                      <Typography variant="body2" fontWeight={600}>{pol.title}</Typography>
                    </Box>
                    <Box sx={{ display: 'flex', gap: 0.5, flexShrink: 0, flexWrap: 'wrap', justifyContent: 'flex-end' }}>
                      <Chip label={pol.policy_type} size="small" sx={{ fontSize: '0.65rem', height: 18 }} />
                      {isExternal
                        ? <Chip label="external" size="small" sx={{ fontSize: '0.65rem', height: 18, bgcolor: 'rgba(255,192,0,0.15)', color: '#FFC000' }} />
                        : <Chip label={pol.product_type} size="small" sx={{ fontSize: '0.65rem', height: 18 }} />
                      }
                      <Chip label={`${pol.word_count.toLocaleString()}w`} size="small" sx={{ fontSize: '0.65rem', height: 18, bgcolor: 'rgba(68,114,196,0.15)' }} />
                      {pol.requirements_count > 0 && (
                        <Chip label={`${pol.requirements_count} reqs`} size="small" sx={{ fontSize: '0.65rem', height: 18, bgcolor: '#1a3a27', color: '#C6EFCE' }} />
                      )}
                    </Box>
                  </Box>
                </Box>
              )
            })}
          </TabPanel>

          {/* Instructions */}
          <TabPanel value={tab} index={TAB_INSTRUCTIONS}>
            {visibleInstructions.length === 0 && (
              <Alert severity="info">No implementation guides (INS) for this control group.</Alert>
            )}
            {visibleInstructions.map((ins) => (
              <Box key={ins.id} onClick={() => setDocPreview({ id: ins.id, docType: 'policy', documentId: ins.document_id, title: ins.title, typeLabel: 'INS', typeColor: '#FFEB9C' })} sx={{ mb: 1.5, p: 1.5, bgcolor: 'rgba(255,192,0,0.06)', border: '1px solid rgba(255,192,0,0.15)', borderRadius: 2, cursor: 'pointer', '&:hover': { bgcolor: 'rgba(255,192,0,0.1)' } }}>
                <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                  <Box>
                    <Typography variant="caption" sx={{ fontFamily: 'monospace', color: '#FFEB9C' }}>
                      {ins.document_id}
                    </Typography>
                    <Typography variant="body2" fontWeight={600}>{ins.title}</Typography>
                  </Box>
                  <Box sx={{ display: 'flex', gap: 0.5, flexShrink: 0, flexWrap: 'wrap', justifyContent: 'flex-end' }}>
                    <Chip label="INS" size="small" sx={{ fontSize: '0.65rem', height: 18, bgcolor: 'rgba(255,192,0,0.15)', color: '#FFEB9C' }} />
                    <Chip label={`${ins.word_count.toLocaleString()}w`} size="small" sx={{ fontSize: '0.65rem', height: 18 }} />
                    {ins.requirements_count > 0 && (
                      <Chip label={`${ins.requirements_count} notes`} size="small" sx={{ fontSize: '0.65rem', height: 18, bgcolor: '#3d3200', color: '#FFEB9C' }} />
                    )}
                  </Box>
                </Box>
              </Box>
            ))}
          </TabPanel>

          {/* Implementations */}
          <TabPanel value={tab} index={TAB_IMPLEMENTATIONS}>
            {visibleImpls.length === 0 && <Alert severity="warning">No implementations for the selected product.</Alert>}
            <Grid container spacing={1}>
              {visibleImpls.map((impl) => (
                <Grid item xs={12} sm={6} key={impl.id}>
                  <Box onClick={() => setDocPreview({ id: impl.id, docType: 'implementation', documentId: impl.document_id, title: impl.title, typeLabel: impl.impl_type, typeColor: impl.impl_type === 'UG' ? '#C6EFCE' : '#FFEB9C' })} sx={{ p: 1.5, bgcolor: 'rgba(68,114,196,0.07)', borderRadius: 2, cursor: 'pointer', '&:hover': { bgcolor: 'rgba(68,114,196,0.14)' } }}>
                    <Box sx={{ display: 'flex', justifyContent: 'space-between', mb: 0.25 }}>
                      <Typography variant="caption" sx={{ fontFamily: 'monospace', color: 'primary.light' }}>
                        {impl.document_id}
                      </Typography>
                      <Box sx={{ display: 'flex', gap: 0.5 }}>
                        <Chip
                          label={impl.impl_type}
                          size="small"
                          sx={{
                            fontSize: '0.65rem', height: 18,
                            bgcolor: impl.impl_type === 'UG' ? '#1a3a27' : '#3d3200',
                            color: impl.impl_type === 'UG' ? '#C6EFCE' : '#FFEB9C',
                          }}
                        />
                        <Chip label={`${impl.word_count.toLocaleString()}w`} size="small" sx={{ fontSize: '0.65rem', height: 18 }} />
                      </Box>
                    </Box>
                    <Typography variant="body2" fontWeight={600} sx={{ lineHeight: 1.3 }}>
                      {impl.title}
                    </Typography>
                  </Box>
                </Grid>
              ))}
            </Grid>
          </TabPanel>

          {/* Assessments */}
          <TabPanel value={tab} index={TAB_ASSESSMENTS}>
            {(() => {
              const isPlatform = (a: AssessmentRow) => a.file_path === 'platform:webui' || a.document_id.startsWith('ISMS-ASS-')
              const platformAssessments = visibleAssessments.filter(isPlatform)
              const uploadedAssessments = visibleAssessments.filter(a => !isPlatform(a))

              return (
                <>
                  {/* ── Platform Assessments ── */}
                  <Box sx={{ mb: 3 }}>
                    <Box sx={{ display: 'flex', alignItems: 'center', mb: 1.5 }}>
                      <AssignmentOutlined sx={{ fontSize: 16, color: 'primary.light', mr: 0.75 }} />
                      <Typography variant="caption" fontWeight={700} color="primary.light" sx={{ flex: 1, textTransform: 'uppercase', letterSpacing: '0.06em', fontSize: '0.7rem' }}>
                        Conduct Assessment
                      </Typography>
                      <Button
                        size="small"
                        variant="contained"
                        startIcon={<AddOutlined />}
                        onClick={() => {
                          if (needsGeneratorPick) { setPickerGeneratorId(''); setGeneratorPickerOpen(true) }
                          else { setAssessmentDrawerOpen(true) }
                        }}
                        sx={{ fontSize: '0.75rem', fontWeight: 600 }}
                      >
                        New Assessment
                      </Button>
                    </Box>

                    {platformAssessments.length === 0 ? (
                      <Box
                        onClick={() => {
                          if (needsGeneratorPick) { setPickerGeneratorId(''); setGeneratorPickerOpen(true) }
                          else { setAssessmentDrawerOpen(true) }
                        }}
                        sx={{
                          p: 2.5, borderRadius: 2, cursor: 'pointer', textAlign: 'center',
                          border: '1px dashed rgba(68,114,196,0.3)',
                          bgcolor: 'rgba(68,114,196,0.03)',
                          '&:hover': { bgcolor: 'rgba(68,114,196,0.08)', borderColor: 'rgba(68,114,196,0.5)' },
                        }}
                      >
                        <AddOutlined sx={{ color: 'text.disabled', mb: 0.5 }} />
                        <Typography variant="body2" color="text.secondary">
                          No platform assessments yet — fill in your data directly, no Excel required.
                        </Typography>
                        <Typography variant="caption" color="primary.light" sx={{ mt: 0.5, display: 'block' }}>
                          Click to start
                        </Typography>
                      </Box>
                    ) : (
                      platformAssessments.map((asmnt) => (
                        <Box key={asmnt.id} sx={{ mb: 1.5, p: 1.5, bgcolor: 'rgba(68,114,196,0.06)', borderRadius: 2, border: '1px solid rgba(68,114,196,0.12)' }}>
                          <Box sx={{ display: 'flex', alignItems: 'flex-start', gap: 1 }}>
                            <Box sx={{ flex: 1, minWidth: 0 }}>
                              <Typography variant="caption" sx={{ fontFamily: 'monospace', color: 'primary.light' }}>
                                {asmnt.document_id}
                              </Typography>
                              <Typography variant="body2" fontWeight={600}>{asmnt.workbook_name}</Typography>
                              <Box sx={{ display: 'flex', gap: 0.5, mt: 0.25, flexWrap: 'wrap' }}>
                                <Chip label="platform" size="small" sx={{ fontSize: '0.6rem', height: 16, bgcolor: 'rgba(68,114,196,0.2)', color: 'primary.light' }} />
                                <Chip label={`${asmnt.items_total} items`} size="small" sx={{ fontSize: '0.6rem', height: 16 }} />
                                {asmnt.overall_score != null && (
                                  <Chip label={`${asmnt.overall_score}%`} size="small" sx={{ fontSize: '0.6rem', height: 16, bgcolor: '#1a3a27', color: '#C6EFCE' }} />
                                )}
                              </Box>
                            </Box>
                            <Tooltip title="Delete platform assessment">
                              <IconButton
                                size="small"
                                onClick={() => setDeleteAssessmentTarget({ id: asmnt.id, name: asmnt.workbook_name })}
                                sx={{ color: 'error.main', opacity: 0.4, flexShrink: 0, '&:hover': { opacity: 1 } }}
                              >
                                <DeleteOutlined sx={{ fontSize: 16 }} />
                              </IconButton>
                            </Tooltip>
                          </Box>
                          {asmnt.items_total > 0 && (
                            <ComplianceBar
                              total={asmnt.items_total}
                              compliant={asmnt.items_compliant}
                              partial={asmnt.items_partial}
                              nonCompliant={asmnt.items_non_compliant}
                              na={asmnt.items_na}
                            />
                          )}
                          {asmnt.items_total === 0 && (
                            <Box sx={{ mt: 1 }}>
                              <LinearProgress variant="determinate" value={0} sx={{ height: 4, borderRadius: 2, bgcolor: 'rgba(255,255,255,0.06)' }} />
                              <Typography variant="caption" color="text.disabled" sx={{ mt: 0.5, display: 'block' }}>
                                No items yet — open the assessment to start filling in data
                              </Typography>
                            </Box>
                          )}
                        </Box>
                      ))
                    )}
                  </Box>

                  {/* ── Uploaded Assessments (from Excel) ── */}
                  {uploadedAssessments.length > 0 && (
                    <Box>
                      <Box sx={{ display: 'flex', alignItems: 'center', mb: 1.5 }}>
                        <FolderOpenOutlined sx={{ fontSize: 16, color: 'text.secondary', mr: 0.75 }} />
                        <Typography variant="caption" fontWeight={700} color="text.secondary" sx={{ textTransform: 'uppercase', letterSpacing: '0.06em', fontSize: '0.7rem' }}>
                          Imported Workbooks
                        </Typography>
                      </Box>
                      {uploadedAssessments.map((asmnt) => (
                        <Box key={asmnt.id} sx={{ mb: 2, p: 1.5, bgcolor: 'rgba(68,114,196,0.05)', borderRadius: 2 }}>
                          <Typography variant="caption" sx={{ fontFamily: 'monospace', color: 'primary.light' }}>
                            {asmnt.document_id}
                          </Typography>
                          <Typography variant="body2" fontWeight={600}>{asmnt.workbook_name}</Typography>
                          <Box sx={{ display: 'flex', gap: 0.5, mt: 0.25, flexWrap: 'wrap' }}>
                            <Chip label={asmnt.assessment_type} size="small" sx={{ fontSize: '0.65rem', height: 18 }} />
                            <Chip label={asmnt.product_type} size="small" sx={{ fontSize: '0.65rem', height: 18 }} />
                            <Chip label={`${asmnt.sheets_count} sheets`} size="small" sx={{ fontSize: '0.65rem', height: 18 }} />
                          </Box>
                          <ComplianceBar
                            total={asmnt.items_total}
                            compliant={asmnt.items_compliant}
                            partial={asmnt.items_partial}
                            nonCompliant={asmnt.items_non_compliant}
                            na={asmnt.items_na}
                          />
                          <Box sx={{ mt: 1 }}>
                            {asmnt.sheets.map((sheet) => (
                              <Box key={sheet.id} sx={{ mb: 0.5 }}>
                                <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                                  <Typography variant="caption" fontWeight={600} sx={{ flex: 1 }}>{sheet.sheet_name}</Typography>
                                  <Chip label={sheet.sheet_type} size="small" sx={{ fontSize: '0.6rem', height: 16, bgcolor: sheet.sheet_type === 'assessment' ? 'rgba(68,114,196,0.2)' : 'rgba(255,255,255,0.06)' }} />
                                  {sheet.row_count > 0 && <Typography variant="caption" color="text.disabled">{sheet.row_count} rows</Typography>}
                                </Box>
                                <SheetItemsTable
                                  sheet={sheet}
                                  expanded={expandedSheets.has(sheet.id)}
                                  onToggle={() => setExpandedSheets(prev => {
                                    const next = new Set(prev)
                                    next.has(sheet.id) ? next.delete(sheet.id) : next.add(sheet.id)
                                    return next
                                  })}
                                  onStatusChange={(itemId, newStatus) =>
                                    statusMutation.mutate({ itemId, status: newStatus })
                                  }
                                />
                              </Box>
                            ))}
                          </Box>
                        </Box>
                      ))}
                    </Box>
                  )}
                </>
              )
            })()}
          </TabPanel>

          {/* ISO Mappings */}
          <TabPanel value={tab} index={TAB_MAPPINGS}>
            {cg.is_stacked && cg.stacked_control_ids.length > 1 && (
              <Box sx={{ display: 'flex', gap: 0.75, mb: 1.5, flexWrap: 'wrap', alignItems: 'center' }}>
                <Typography variant="caption" color="text.secondary">Filter:</Typography>
                {['all', ...cg.stacked_control_ids].map((sid) => (
                  <Chip
                    key={sid}
                    label={sid === 'all' ? 'All' : sid}
                    size="small"
                    onClick={() => setStackedFilter(sid)}
                    sx={{
                      fontSize: '0.68rem', height: 20, cursor: 'pointer',
                      bgcolor: stackedFilter === sid ? 'rgba(68,114,196,0.35)' : 'rgba(68,114,196,0.1)',
                      color: stackedFilter === sid ? 'primary.light' : 'text.secondary',
                      fontWeight: stackedFilter === sid ? 700 : 400,
                    }}
                  />
                ))}
              </Box>
            )}
            {cg.iso_controls.length === 0 && <Alert severity="info">No ISO controls linked.</Alert>}
            {cg.iso_controls
              .filter(iso => stackedFilter === 'all' || iso.control_id.startsWith(stackedFilter.replace('A.', 'A.')))
              .map((iso) => (
              <Box key={iso.control_id} sx={{ mb: 2, p: 1.5, bgcolor: 'rgba(68,114,196,0.07)', borderRadius: 2 }}>
                <Box sx={{ display: 'flex', gap: 1, alignItems: 'center', mb: iso.description ? 0.5 : 0.75 }}>
                  <Typography variant="caption" sx={{ fontFamily: 'monospace', color: 'primary.light', fontWeight: 700, fontSize: '0.8rem' }}>
                    {iso.control_id}
                  </Typography>
                  <Typography variant="body2" fontWeight={600}>{iso.title}</Typography>
                </Box>
                {iso.description && (
                  <Typography variant="caption" color="text.secondary" sx={{ display: 'block', mb: 0.75, lineHeight: 1.6, fontStyle: 'italic' }}>
                    {iso.description}
                  </Typography>
                )}
                {iso.mappings.length > 0 && (
                  <Box sx={{ display: 'flex', gap: 0.5, flexWrap: 'wrap' }}>
                    {iso.mappings.map((m, idx) => (
                      <Chip
                        key={idx}
                        label={`${m.control_id}`}
                        title={`${m.framework}: ${m.control_title}`}
                        size="small"
                        sx={{
                          fontSize: '0.68rem', height: 18,
                          bgcolor: 'rgba(112,173,71,0.12)', color: '#C6EFCE',
                        }}
                      />
                    ))}
                    <Typography variant="caption" color="text.secondary" sx={{ alignSelf: 'center' }}>
                      {iso.mappings.length} mappings across {[...new Set(iso.mappings.map(m => m.framework))].length} frameworks
                    </Typography>
                  </Box>
                )}
              </Box>
            ))}
          </TabPanel>

          {/* Evidence */}
          <TabPanel value={tab} index={TAB_EVIDENCE}>
            {cg.evidence.length === 0 && (
              <Alert severity="info">No evidence linked yet. Upload evidence via the Evidence page.</Alert>
            )}
            {cg.evidence.map((ev) => (
              <Box key={ev.id} sx={{ mb: 1, p: 1.5, bgcolor: 'rgba(68,114,196,0.07)', borderRadius: 2 }}>
                <Box sx={{ display: 'flex', justifyContent: 'space-between' }}>
                  <Typography variant="body2" fontWeight={600}>{ev.title}</Typography>
                  <StatusChip status={ev.verified_by ? 'green' : 'not_assessed'} />
                </Box>
                <Box sx={{ display: 'flex', gap: 0.5, mt: 0.5 }}>
                  <Chip label={ev.evidence_type} size="small" sx={{ fontSize: '0.65rem', height: 18 }} />
                  {ev.collected_date && (
                    <Typography variant="caption" color="text.secondary" sx={{ alignSelf: 'center' }}>
                      {ev.collected_date}
                    </Typography>
                  )}
                </Box>
              </Box>
            ))}
          </TabPanel>

          {/* Gaps */}
          {cg.gaps.length > 0 && (
            <TabPanel value={tab} index={TAB_GAPS}>
              {cg.gaps.map((gap) => (
                <Box key={gap.id} sx={{ mb: 1, p: 1.5, bgcolor: 'rgba(192,0,0,0.08)', border: '1px solid rgba(255,199,206,0.15)', borderRadius: 2 }}>
                  <Box sx={{ display: 'flex', gap: 1, alignItems: 'center', mb: 0.25 }}>
                    <StatusChip status={gap.severity} />
                    <StatusChip status={gap.status} />
                    <Typography variant="caption" color="text.secondary">{gap.gap_type}</Typography>
                  </Box>
                  <Typography variant="body2">{gap.description}</Typography>
                </Box>
              ))}
            </TabPanel>
          )}
        </CardContent>
      </Card>

      <AiAssistant
        open={aiOpen}
        onClose={() => setAiOpen(false)}
        controlId={cg.id}
        controlName={cg.name}
      />

      <DocPreviewDrawer
        open={!!docPreview}
        onClose={() => setDocPreview(null)}
        target={docPreview}
      />

      {/* Delete assessment confirm */}
      <Dialog open={!!deleteAssessmentTarget} onClose={() => setDeleteAssessmentTarget(null)} maxWidth="xs" fullWidth>
        <DialogTitle>Delete Platform Assessment?</DialogTitle>
        <DialogContent>
          <Typography variant="body2">
            <strong>{deleteAssessmentTarget?.name}</strong> and all its data will be permanently removed.
            This cannot be undone.
          </Typography>
          {deleteAssessmentMutation.isError && (
            <Alert severity="error" sx={{ mt: 1.5 }}>Delete failed. Try again.</Alert>
          )}
        </DialogContent>
        <DialogActions sx={{ px: 3, pb: 2 }}>
          <Button onClick={() => setDeleteAssessmentTarget(null)} disabled={deleteAssessmentMutation.isPending}>Cancel</Button>
          <Button
            variant="contained"
            color="error"
            disabled={deleteAssessmentMutation.isPending}
            startIcon={<DeleteOutlined />}
            onClick={() => deleteAssessmentTarget && deleteAssessmentMutation.mutate(deleteAssessmentTarget.id)}
          >
            {deleteAssessmentMutation.isPending ? 'Deleting…' : 'Delete'}
          </Button>
        </DialogActions>
      </Dialog>

      {/* Generator / workbook picker for stacked controls */}
      <Dialog open={generatorPickerOpen} onClose={() => setGeneratorPickerOpen(false)} maxWidth="sm" fullWidth>
        <DialogTitle>Choose Workbook to Assess</DialogTitle>
        <DialogContent>
          <Typography variant="body2" color="text.secondary" sx={{ mb: 2 }}>
            This control group has multiple workbooks. Select which one to assess:
          </Typography>
          <Box sx={{ display: 'flex', flexDirection: 'column', gap: 1 }}>
            {generatorsForGroup.map((gen) => (
              <Box
                key={gen.document_id}
                onClick={() => setPickerGeneratorId(gen.document_id)}
                sx={{
                  p: 1.5, borderRadius: 2, cursor: 'pointer',
                  border: '1px solid',
                  borderColor: pickerGeneratorId === gen.document_id ? 'primary.main' : 'rgba(255,255,255,0.1)',
                  bgcolor: pickerGeneratorId === gen.document_id ? 'rgba(68,114,196,0.18)' : 'rgba(68,114,196,0.05)',
                  '&:hover': { bgcolor: 'rgba(68,114,196,0.12)' },
                }}
              >
                <Typography variant="caption" sx={{ fontFamily: 'monospace', color: 'primary.light', display: 'block' }}>
                  {gen.document_id}
                </Typography>
                <Typography variant="body2" fontWeight={600}>{gen.workbook_name}</Typography>
                <Typography variant="caption" color="text.secondary">{gen.sheet_count} sheets</Typography>
              </Box>
            ))}
          </Box>
        </DialogContent>
        <DialogActions sx={{ px: 3, pb: 2 }}>
          <Button onClick={() => setGeneratorPickerOpen(false)}>Cancel</Button>
          <Button
            variant="contained"
            disabled={!pickerGeneratorId}
            onClick={() => { setGeneratorPickerOpen(false); setAssessmentDrawerOpen(true) }}
          >
            Continue
          </Button>
        </DialogActions>
      </Dialog>

      <AssessmentFormDrawer
        open={assessmentDrawerOpen}
        onClose={() => {
          setAssessmentDrawerOpen(false)
          queryClient.invalidateQueries({ queryKey: ['control', identifier] })
        }}
        groupCode={cg.group_code}
        groupName={cg.name}
        generatorId={drawerGeneratorId}
      />
    </Box>
  )
}
