import { useState } from 'react'
import {
  Box,
  Card,
  CardContent,
  Typography,
  Button,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Chip,
  ToggleButton,
  ToggleButtonGroup,
  CircularProgress,
  Alert,
  LinearProgress,
  Tooltip,
  Grid,
  Divider,
  Tab,
  Tabs,
  TextField,
  IconButton,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  Stack,
  useTheme,
} from '@mui/material'
import {
  PlayArrowOutlined,
  CheckCircleOutlined,
  WarningAmberOutlined,
  ErrorOutlined,
  HelpOutlineOutlined,
  AddOutlined,
  DeleteOutlined,
  EditOutlined,
  PsychologyOutlined,
  AutoAwesomeOutlined,
  InfoOutlined,
  OpenInNewOutlined,
} from '@mui/icons-material'
import Popover from '@mui/material/Popover'
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { useNavigate } from 'react-router-dom'
import dayjs from 'dayjs'
import relativeTime from 'dayjs/plugin/relativeTime'
import { qaApi } from '../api/qa'
import type { ReferenceCorpusStatus, OrgProjectSummaryItem } from '../api/qa'
import type { CorrelationResultRead, QASummaryBucket, SynonymRule } from '../api/types'
import PageHeader from '../components/PageHeader'
import { useProduct, PRODUCT_SUBTITLES, PRODUCT_COLORS } from '../store/ProductContext'

dayjs.extend(relativeTime)

const STATUS_COLOR_DARK: Record<string, { bg: string; fg: string }> = {
  pass: { bg: '#1a3a27', fg: '#C6EFCE' },
  warning: { bg: '#3a2e00', fg: '#FFEB9C' },
  fail: { bg: '#3a0000', fg: '#FFC7CE' },
  needs_review: { bg: 'rgba(255,255,255,0.07)', fg: '#d9d9d9' },
}
const STATUS_COLOR_LIGHT: Record<string, { bg: string; fg: string }> = {
  pass: { bg: 'rgba(46,125,50,0.12)', fg: '#1b5e20' },
  warning: { bg: 'rgba(230,160,0,0.12)', fg: '#7a4800' },
  fail: { bg: 'rgba(192,0,0,0.12)', fg: '#9e0000' },
  needs_review: { bg: 'rgba(0,0,0,0.06)', fg: '#555' },
}

function SummaryCard({
  label,
  bucket,
  color,
}: {
  label: string
  bucket: QASummaryBucket
  color: string
}) {
  const { palette } = useTheme()
  const isLight = palette.mode === 'light'
  const STATUS_COLOR = isLight ? STATUS_COLOR_LIGHT : STATUS_COLOR_DARK
  const pct = Math.round(bucket.pass_rate * 100)
  return (
    <Card>
      <CardContent sx={{ pb: '12px !important' }}>
        <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 1 }}>
          <Typography variant="body2" color="text.secondary">{label}</Typography>
          <Typography variant="h5" fontWeight={700} sx={{ color }}>
            {pct}%
          </Typography>
        </Box>
        <LinearProgress
          variant="determinate"
          value={pct}
          sx={{
            mb: 1.5,
            height: 6,
            borderRadius: 3,
            bgcolor: isLight ? 'rgba(0,0,0,0.08)' : 'rgba(255,255,255,0.08)',
            '& .MuiLinearProgress-bar': { bgcolor: color },
          }}
        />
        <Box sx={{ display: 'flex', gap: 1, flexWrap: 'wrap' }}>
          <Chip label={`${bucket.pass_count} pass`} size="small" sx={{ fontSize: '0.65rem', height: 18, bgcolor: STATUS_COLOR.pass.bg, color: STATUS_COLOR.pass.fg }} />
          {bucket.warning_count > 0 && (
            <Chip label={`${bucket.warning_count} warn`} size="small" sx={{ fontSize: '0.65rem', height: 18, bgcolor: STATUS_COLOR.warning.bg, color: STATUS_COLOR.warning.fg }} />
          )}
          {bucket.fail_count > 0 && (
            <Chip label={`${bucket.fail_count} fail`} size="small" sx={{ fontSize: '0.65rem', height: 18, bgcolor: STATUS_COLOR.fail.bg, color: STATUS_COLOR.fail.fg }} />
          )}
          {bucket.needs_review_count > 0 && (
            <Chip label={`${bucket.needs_review_count} review`} size="small" sx={{ fontSize: '0.65rem', height: 18 }} />
          )}
          <Typography variant="caption" color="text.secondary" sx={{ alignSelf: 'center' }}>
            / {bucket.total}
          </Typography>
        </Box>
      </CardContent>
    </Card>
  )
}

function SynonymsTab() {
  const queryClient = useQueryClient()
  const [addOpen, setAddOpen] = useState(false)
  const [editRow, setEditRow] = useState<SynonymRule | null>(null)
  const [keyword, setKeyword] = useState('')
  const [synonymsText, setSynonymsText] = useState('')  // comma-separated input
  const [notes, setNotes] = useState('')
  const [editSynonymsText, setEditSynonymsText] = useState('')
  const [editNotes, setEditNotes] = useState('')

  const { data: rules = [], isLoading } = useQuery({
    queryKey: ['qa', 'synonyms'],
    queryFn: qaApi.getSynonyms,
  })

  const createMutation = useMutation({
    mutationFn: qaApi.createSynonym,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['qa', 'synonyms'] })
      setAddOpen(false)
      setKeyword(''); setSynonymsText(''); setNotes('')
    },
  })

  const updateMutation = useMutation({
    mutationFn: ({ id, body }: { id: string; body: { synonyms: string[]; notes?: string } }) =>
      qaApi.updateSynonym(id, body),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['qa', 'synonyms'] })
      setEditRow(null)
    },
  })

  const deleteMutation = useMutation({
    mutationFn: qaApi.deleteSynonym,
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ['qa', 'synonyms'] }),
  })

  function parseSynonyms(text: string): string[] {
    return text.split(',').map(s => s.trim().toLowerCase()).filter(Boolean)
  }

  function openEdit(rule: SynonymRule) {
    setEditRow(rule)
    setEditSynonymsText(rule.synonyms.join(', '))
    setEditNotes(rule.notes ?? '')
  }

  return (
    <Box>
      <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 2 }}>
        <Typography variant="body2" color="text.secondary">
          {rules.length} rules — used by the keyword correlation engine. Re-run keyword check after making changes.
        </Typography>
        <Button
          variant="contained"
          size="small"
          startIcon={<AddOutlined />}
          onClick={() => setAddOpen(true)}
        >
          Add Rule
        </Button>
      </Box>

      {isLoading && <CircularProgress size={20} />}

      <TableContainer component={Card}>
        <Table size="small">
          <TableHead>
            <TableRow>
              <TableCell sx={{ width: 160 }}>Keyword</TableCell>
              <TableCell>Synonyms</TableCell>
              <TableCell sx={{ width: 200 }}>Notes</TableCell>
              <TableCell sx={{ width: 80 }} align="right">Actions</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {rules.map((rule) => (
              <TableRow key={rule.id} hover>
                <TableCell>
                  <Typography variant="body2" fontWeight={600} sx={{ fontFamily: 'monospace', color: 'primary.light' }}>
                    {rule.keyword}
                  </Typography>
                </TableCell>
                <TableCell>
                  <Box sx={{ display: 'flex', gap: 0.5, flexWrap: 'wrap' }}>
                    {rule.synonyms.map((s) => (
                      <Chip key={s} label={s} size="small" sx={{ fontSize: '0.6rem', height: 16 }} />
                    ))}
                  </Box>
                </TableCell>
                <TableCell>
                  <Typography variant="caption" color="text.secondary">{rule.notes ?? '—'}</Typography>
                </TableCell>
                <TableCell align="right">
                  <Tooltip title="Edit synonyms">
                    <IconButton size="small" onClick={() => openEdit(rule)}>
                      <EditOutlined fontSize="small" />
                    </IconButton>
                  </Tooltip>
                  <Tooltip title="Delete rule">
                    <IconButton
                      size="small"
                      color="error"
                      onClick={() => deleteMutation.mutate(rule.id)}
                    >
                      <DeleteOutlined fontSize="small" />
                    </IconButton>
                  </Tooltip>
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>

      {/* Add dialog */}
      <Dialog open={addOpen} onClose={() => setAddOpen(false)} maxWidth="sm" fullWidth>
        <DialogTitle>Add Synonym Rule</DialogTitle>
        <DialogContent sx={{ display: 'flex', flexDirection: 'column', gap: 2, pt: '12px !important' }}>
          <TextField
            label="Keyword"
            size="small"
            value={keyword}
            onChange={(e) => setKeyword(e.target.value)}
            helperText="The ISO term to match (e.g. addressing)"
          />
          <TextField
            label="Synonyms"
            size="small"
            value={synonymsText}
            onChange={(e) => setSynonymsText(e.target.value)}
            helperText="Comma-separated equivalents (e.g. handling, managing, treating)"
          />
          <TextField
            label="Notes (optional)"
            size="small"
            value={notes}
            onChange={(e) => setNotes(e.target.value)}
          />
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setAddOpen(false)}>Cancel</Button>
          <Button
            variant="contained"
            disabled={!keyword.trim() || !synonymsText.trim() || createMutation.isPending}
            onClick={() => createMutation.mutate({
              keyword: keyword.trim().toLowerCase(),
              synonyms: parseSynonyms(synonymsText),
              notes: notes.trim() || undefined,
            })}
          >
            {createMutation.isPending ? 'Saving…' : 'Save'}
          </Button>
        </DialogActions>
      </Dialog>

      {/* Edit dialog */}
      <Dialog open={!!editRow} onClose={() => setEditRow(null)} maxWidth="sm" fullWidth>
        <DialogTitle>Edit — <em>{editRow?.keyword}</em></DialogTitle>
        <DialogContent sx={{ display: 'flex', flexDirection: 'column', gap: 2, pt: '12px !important' }}>
          <TextField
            label="Synonyms"
            size="small"
            value={editSynonymsText}
            onChange={(e) => setEditSynonymsText(e.target.value)}
            helperText="Comma-separated equivalents"
          />
          <TextField
            label="Notes (optional)"
            size="small"
            value={editNotes}
            onChange={(e) => setEditNotes(e.target.value)}
          />
        </DialogContent>
        <DialogActions>
          <Button onClick={() => setEditRow(null)}>Cancel</Button>
          <Button
            variant="contained"
            disabled={!editSynonymsText.trim() || updateMutation.isPending}
            onClick={() => editRow && updateMutation.mutate({
              id: editRow.id,
              body: {
                synonyms: parseSynonyms(editSynonymsText),
                notes: editNotes.trim() || undefined,
              },
            })}
          >
            {updateMutation.isPending ? 'Saving…' : 'Save'}
          </Button>
        </DialogActions>
      </Dialog>
    </Box>
  )
}

// ── Method legend ─────────────────────────────────────────────────────────────

interface LegendRow {
  label: string
  chipBg: string
  chipFg: string
  description: string
}

const METHOD_LEGEND: Record<string, { summary: string; thresholds: string; rows: LegendRow[]; auditRelevant?: boolean }> = {
  existence: {
    summary: 'Checks that each control group has its required artefacts in the database.',
    thresholds: 'PASS = all required artefacts present · WARNING = partial · FAIL = missing',
    auditRelevant: true,
    rows: [
      { label: 'policy', chipBg: '#1a3a27', chipFg: '#C6EFCE', description: 'Framework POL document imported' },
      { label: 'UG', chipBg: '#1a3a27', chipFg: '#C6EFCE', description: 'User Guide (UG) implementation imported' },
      { label: 'TG', chipBg: '#1a3a27', chipFg: '#C6EFCE', description: 'Technical Guide (TG) implementation imported' },
      { label: 'assessment', chipBg: '#1a3a27', chipFg: '#C6EFCE', description: 'Assessment workbook imported' },
      { label: 'missing', chipBg: '#3a0000', chipFg: '#FFC7CE', description: 'Artefact not found in DB' },
    ],
  },
  keyword: {
    summary: 'Extracts ISO 27001 control keywords and checks whether they appear in UG/TG content indexed in OpenSearch.',
    thresholds: 'PASS ≥ 60% · WARNING ≥ 35% · FAIL < 35%',
    auditRelevant: false,
    rows: [
      { label: 'keyword', chipBg: '#1a3a27', chipFg: '#C6EFCE', description: 'Exact or stem match found in implementation text (counts 1.0×)' },
      { label: '≈ keyword', chipBg: '#3a2e00', chipFg: '#FFEB9C', description: 'Synonym match — a related term was found (counts 0.7×). Hover for which synonym matched.' },
      { label: 'missing', chipBg: '#3a0000', chipFg: '#FFC7CE', description: 'Keyword not found by any method — genuine coverage gap' },
    ],
  },
  semantic: {
    summary: 'Encodes ISO control text and UG/TG content as embedding vectors (paraphrase-multilingual-MiniLM-L12-v2) then computes cosine similarity. No API key required — runs on CPU.',
    thresholds: 'PASS ≥ 0.42 · WARNING ≥ 0.28 · FAIL < 0.28  (cosine similarity; typical range 0.1–0.55)',
    auditRelevant: false,
    rows: [
      { label: '3w ISO', chipBg: 'rgba(68,114,196,0.15)', chipFg: '#9DC3E6', description: 'Word count of ISO text used as the query. Hover the chip for the full ISO text.' },
      { label: 'short ISO text', chipBg: '#3a2e00', chipFg: '#FFEB9C', description: 'ISO text < 15 words — score is less reliable. The control has no detailed description in the dataset, only a title.' },
    ],
  },
  semantic_claude: {
    summary: 'Claude AI (Haiku) reads the ISO control requirements and implementation content, then scores alignment 0–100 with a written explanation. Requires ANTHROPIC_API_KEY.',
    thresholds: 'PASS ≥ 70 · WARNING ≥ 45 · FAIL < 45  (out of 100)',
    auditRelevant: false,
    rows: [
      { label: 'Reasoning', chipBg: 'transparent', chipFg: '#d9d9d9', description: 'Claude\'s 2-3 sentence explanation of why this score was given. Hover the cell for the full text.' },
      { label: 'gap chip', chipBg: '#3a0000', chipFg: '#FFC7CE', description: 'Specific topic Claude identified as missing or insufficiently covered.' },
    ],
  },
}

function MethodLegendPopover({ method }: { method: string }) {
  const [anchor, setAnchor] = useState<HTMLButtonElement | null>(null)
  const { palette } = useTheme()
  const isLight = palette.mode === 'light'
  const legend = METHOD_LEGEND[method]
  if (!legend) return null

  function resolveChipBg(chipBg: string): string {
    if (chipBg === 'transparent') return 'transparent'
    if (chipBg === '#1a3a27') return isLight ? 'rgba(46,125,50,0.12)' : '#1a3a27'
    if (chipBg === '#3a2e00') return isLight ? 'rgba(230,160,0,0.12)' : '#3a2e00'
    if (chipBg === '#3a0000') return isLight ? 'rgba(192,0,0,0.12)' : '#3a0000'
    return chipBg
  }

  function resolveChipFg(chipBg: string, chipFg: string): string {
    if (chipBg === 'transparent') return isLight ? '#555' : chipFg
    if (chipBg === '#1a3a27') return isLight ? '#1b5e20' : '#C6EFCE'
    if (chipBg === '#3a2e00') return isLight ? '#7a4800' : '#FFEB9C'
    if (chipBg === '#3a0000') return isLight ? '#9e0000' : '#FFC7CE'
    return isLight ? (chipFg === '#9DC3E6' ? '#1565c0' : chipFg) : chipFg
  }

  return (
    <>
      <Tooltip title="What do the indicators mean?">
        <IconButton size="small" onClick={(e) => setAnchor(e.currentTarget)} sx={{ color: 'text.secondary' }}>
          <InfoOutlined fontSize="small" />
        </IconButton>
      </Tooltip>
      <Popover
        open={!!anchor}
        anchorEl={anchor}
        onClose={() => setAnchor(null)}
        anchorOrigin={{ vertical: 'bottom', horizontal: 'left' }}
        transformOrigin={{ vertical: 'top', horizontal: 'left' }}
        PaperProps={{ sx: { p: 2, maxWidth: 480, border: '1px solid rgba(128,128,128,0.2)' } }}
      >
        <Typography variant="body2" fontWeight={600} sx={{ mb: 0.5 }}>
          {METHOD_LABELS[method]}
        </Typography>
        <Typography variant="caption" color="text.secondary" sx={{ display: 'block', mb: 1 }}>
          {legend.summary}
        </Typography>

        {/* Audit relevance banner */}
        {legend.auditRelevant ? (
          <Box sx={{ mb: 1.5, px: 1, py: 0.5, bgcolor: isLight ? 'rgba(46,125,50,0.08)' : 'rgba(198,239,206,0.08)', borderRadius: 1, border: '1px solid ' + (isLight ? 'rgba(46,125,50,0.25)' : 'rgba(198,239,206,0.2)') }}>
            <Typography variant="caption" sx={{ color: isLight ? '#1b5e20' : '#C6EFCE', fontWeight: 600 }}>
              ✓ Audit-relevant — S1 proxy
            </Typography>
            <Typography variant="caption" color="text.secondary" sx={{ display: 'block', lineHeight: 1.4 }}>
              Pass/fail status here reflects whether required artefacts exist. Used as a Stage 1 readiness indicator.
            </Typography>
          </Box>
        ) : (
          <Box sx={{ mb: 1.5, px: 1, py: 0.5, bgcolor: isLight ? 'rgba(230,160,0,0.08)' : 'rgba(255,235,156,0.06)', borderRadius: 1, border: '1px solid ' + (isLight ? 'rgba(230,160,0,0.25)' : 'rgba(255,235,156,0.18)') }}>
            <Typography variant="caption" sx={{ color: isLight ? '#7a4800' : '#FFEB9C', fontWeight: 600 }}>
              ⓘ Informational only — does not affect audit status
            </Typography>
            <Typography variant="caption" color="text.secondary" sx={{ display: 'block', lineHeight: 1.4 }}>
              This score is a quality signal for internal review. It has no bearing on S1/S2 audit compliance.
            </Typography>
          </Box>
        )}

        <Box sx={{ mb: 1.5, px: 1, py: 0.75, bgcolor: isLight ? 'rgba(0,0,0,0.04)' : 'rgba(255,255,255,0.04)', borderRadius: 1 }}>
          <Typography variant="caption" sx={{ fontFamily: 'monospace', color: isLight ? '#7a4800' : '#FFEB9C' }}>
            {legend.thresholds}
          </Typography>
        </Box>

        <Typography variant="caption" fontWeight={600} color="text.secondary" sx={{ display: 'block', mb: 1, textTransform: 'uppercase', letterSpacing: '0.08em' }}>
          Indicators
        </Typography>
        <Box sx={{ display: 'flex', flexDirection: 'column', gap: 0.75 }}>
          {legend.rows.map((row) => (
            <Box key={row.label} sx={{ display: 'flex', alignItems: 'flex-start', gap: 1 }}>
              <Chip
                label={row.label}
                size="small"
                sx={{
                  fontSize: '0.6rem', height: 16, flexShrink: 0,
                  bgcolor: resolveChipBg(row.chipBg),
                  color: resolveChipFg(row.chipBg, row.chipFg),
                  border: row.chipBg === 'transparent' ? ('1px solid ' + (isLight ? 'rgba(0,0,0,0.25)' : 'rgba(255,255,255,0.2)')) : 'none',
                }}
              />
              <Typography variant="caption" color="text.secondary" sx={{ lineHeight: 1.4 }}>
                {row.description}
              </Typography>
            </Box>
          ))}
        </Box>

        <Divider sx={{ my: 1.5 }} />
        <Typography variant="caption" color="text.secondary">
          Status colours: <Box component="span" sx={{ color: isLight ? '#1b5e20' : '#C6EFCE' }}>green = pass</Box> · <Box component="span" sx={{ color: isLight ? '#7a4800' : '#FFEB9C' }}>amber = warning</Box> · <Box component="span" sx={{ color: isLight ? '#9e0000' : '#FFC7CE' }}>red = fail</Box> · grey = needs review
        </Typography>
      </Popover>
    </>
  )
}

const METHOD_LABELS: Record<string, string> = {
  existence: 'Existence Check',
  keyword: 'Keyword Correlation',
  semantic: 'Semantic Similarity (Mini LLM)',
  semantic_claude: 'Semantic Similarity (Claude AI)',
}

const METHOD_SUBTITLES: Record<string, string> = {
  existence: 'Verifies each control group has the required artefacts',
  keyword: 'Checks keyword coverage across all ISO standard implementations (27001 · 27701 · 27018)',
  semantic: 'Cosine similarity between ISO control text and implementation embeddings (paraphrase-multilingual-MiniLM-L12-v2)',
  semantic_claude: 'Claude AI scores how well each implementation addresses the relevant ISO control requirements',
}

const isSemantic = (m: string) => m === 'semantic' || m === 'semantic_claude'

const PRODUCT_TYPE_COLOR: Record<string, string> = {
  framework:   PRODUCT_COLORS.isms,
  isms:        PRODUCT_COLORS.isms,
  operational: '#70AD47',
  privacy:     PRODUCT_COLORS.privacy,
  cloud:       PRODUCT_COLORS.cloud,
}

function DetailsCell({ row, method }: { row: CorrelationResultRead; method: string }) {
  const { palette } = useTheme()
  const isLight = palette.mode === 'light'
  if (method === 'semantic_claude') {
    const reasoning = (row.metadata?.reasoning as string) ?? ''
    const model = (row.metadata?.model as string) ?? 'claude'
    return reasoning ? (
      <Tooltip title={reasoning} placement="left" arrow>
        <Box>
          <Typography variant="caption" color="text.secondary" sx={{ display: 'block', mb: 0.5 }}>
            {model.includes('haiku') ? 'Haiku' : model.includes('sonnet') ? 'Sonnet' : 'Claude'}
          </Typography>
          <Typography
            variant="caption"
            sx={{
              display: '-webkit-box',
              WebkitLineClamp: 2,
              WebkitBoxOrient: 'vertical',
              overflow: 'hidden',
              maxWidth: 260,
              color: 'text.secondary',
              cursor: 'default',
            }}
          >
            {reasoning}
          </Typography>
        </Box>
      </Tooltip>
    ) : <Typography variant="caption" color="text.secondary">—</Typography>
  }

  if (method === 'semantic') {
    const isoText = (row.metadata?.iso_text as string) ?? ''
    const isoWords = (row.metadata?.iso_word_count as number) ?? 0
    const implChars = (row.metadata?.impl_text_chars as number) ?? 0
    const shortIso = !!(row.metadata?.short_iso_text)
    const model = (row.metadata?.model as string) ?? 'paraphrase-multilingual-MiniLM-L12-v2'

    const tooltipContent = (
      <Box sx={{ maxWidth: 320 }}>
        <Typography variant="caption" sx={{ display: 'block', fontWeight: 600, mb: 0.5 }}>
          ISO text ({isoWords} words):
        </Typography>
        <Typography variant="caption" sx={{ display: 'block', fontStyle: 'italic', mb: 1 }}>
          {isoText || '—'}
        </Typography>
        <Typography variant="caption" color="text.secondary">
          Model: {model} · Impl content: {implChars} chars
        </Typography>
      </Box>
    )

    return (
      <Tooltip title={tooltipContent} placement="left" arrow>
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.5 }}>
          {shortIso && (
            <Chip
              label="short ISO text"
              size="small"
              sx={{ fontSize: '0.6rem', height: 16, bgcolor: isLight ? 'rgba(230,160,0,0.12)' : '#3a2e00', color: isLight ? '#7a4800' : '#FFEB9C', cursor: 'default' }}
            />
          )}
          <Chip
            icon={<PsychologyOutlined sx={{ fontSize: '12px !important' }} />}
            label={`${isoWords}w ISO`}
            size="small"
            sx={{
              fontSize: '0.6rem', height: 16, cursor: 'default',
              bgcolor: shortIso ? (isLight ? 'rgba(230,160,0,0.10)' : 'rgba(58,46,0,0.4)') : 'rgba(68,114,196,0.15)',
              color: shortIso ? (isLight ? '#7a4800' : '#FFEB9C') : (isLight ? '#1565c0' : '#9DC3E6'),
            }}
          />
        </Box>
      </Tooltip>
    )
  }

  // keyword / existence — existing chip rendering
  const hasExternal = !!(row.metadata?.has_external)
  const externalSources = (row.metadata?.external_sources as string[]) ?? []
  return (
    <Box sx={{ display: 'flex', gap: 0.5, flexWrap: 'wrap' }}>
      {row.coverage_keywords.map((k) => (
        <Chip
          key={k}
          label={k}
          size="small"
          sx={{ fontSize: '0.6rem', height: 16, bgcolor: isLight ? 'rgba(46,125,50,0.12)' : '#1a3a27', color: isLight ? '#1b5e20' : '#C6EFCE' }}
        />
      ))}
      {Object.entries((row.metadata?.synonym_matches as Record<string, string>) ?? {}).map(([kw, syn]) => (
        <Tooltip key={kw} title={`"${kw}" not found — matched via synonym "${syn}"`}>
          <Chip
            label={`≈ ${kw}`}
            size="small"
            sx={{ fontSize: '0.6rem', height: 16, bgcolor: isLight ? 'rgba(230,160,0,0.12)' : '#3a2e00', color: isLight ? '#7a4800' : '#FFEB9C', cursor: 'default' }}
          />
        </Tooltip>
      ))}
      {hasExternal && (
        <Tooltip title={`External document(s): ${externalSources.join(', ')}`}>
          <Chip
            label="⚠ External source"
            size="small"
            sx={{ fontSize: '0.6rem', height: 16, bgcolor: isLight ? 'rgba(230,160,0,0.12)' : 'rgba(255,192,0,0.15)', color: isLight ? '#7a4800' : '#FFC000', cursor: 'default' }}
          />
        </Tooltip>
      )}
      {row.coverage_keywords.length === 0 && !Object.keys(row.metadata?.synonym_matches ?? {}).length && !hasExternal && (
        <Typography variant="caption" color="text.secondary">—</Typography>
      )}
    </Box>
  )
}

function MissingCell({ row, method }: { row: CorrelationResultRead; method: string }) {
  const { palette } = useTheme()
  const isLight = palette.mode === 'light'
  if (method === 'semantic_claude') {
    const gaps = (row.metadata?.gaps as string[]) ?? row.missing_keywords
    return gaps.length ? (
      <Box sx={{ display: 'flex', gap: 0.5, flexWrap: 'wrap' }}>
        {gaps.map((g, i) => (
          <Chip
            key={i}
            label={g}
            size="small"
            sx={{ fontSize: '0.6rem', height: 16, bgcolor: isLight ? 'rgba(192,0,0,0.12)' : '#3a0000', color: isLight ? '#9e0000' : '#FFC7CE' }}
          />
        ))}
      </Box>
    ) : <Typography variant="caption" color="text.secondary">—</Typography>
  }

  if (method === 'semantic') {
    return <Typography variant="caption" color="text.secondary">—</Typography>
  }

  return (
    <Box sx={{ display: 'flex', gap: 0.5, flexWrap: 'wrap' }}>
      {row.missing_keywords.map((k) => (
        <Chip
          key={k}
          label={k}
          size="small"
          sx={{ fontSize: '0.6rem', height: 16, bgcolor: isLight ? 'rgba(192,0,0,0.12)' : '#3a0000', color: isLight ? '#9e0000' : '#FFC7CE' }}
        />
      ))}
      {row.missing_keywords.length === 0 && (
        <Typography variant="caption" color="text.secondary">—</Typography>
      )}
    </Box>
  )
}

function ReferenceCorpusTab() {
  const queryClient = useQueryClient()
  const [loadResult, setLoadResult] = useState<string | null>(null)
  const [loadError, setLoadError] = useState<string | null>(null)

  const { data: status, isLoading } = useQuery<ReferenceCorpusStatus>({
    queryKey: ['qa', 'reference-corpus', 'status'],
    queryFn: qaApi.getReferenceCorpusStatus,
    refetchInterval: 30_000,
  })

  const loadMutation = useMutation({
    mutationFn: qaApi.reloadReferenceCorpus,
    onSuccess: (data) => {
      queryClient.invalidateQueries({ queryKey: ['qa', 'reference-corpus'] })
      setLoadError(null)
      setLoadResult(
        `Loaded ${data.loaded_files} files — ${data.total_chunks.toLocaleString()} chunks indexed in ${(data.duration_ms / 1000).toFixed(1)}s.` +
        (data.failed_files > 0 ? ` (${data.failed_files} files failed)` : '')
      )
    },
    onError: (e: Error) => {
      setLoadResult(null)
      setLoadError(e.message || 'Failed to load reference corpus.')
    },
  })

  return (
    <Box>
      <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', mb: 2 }}>
        <Box>
          <Typography variant="body2" fontWeight={600} gutterBottom>ISO & Regulatory Reference Corpus</Typography>
          <Typography variant="caption" color="text.secondary">
            Normative text from all ISO/regulatory standards — indexed automatically on first boot.
            Use Reload only after updating seed files and rebuilding the container.
          </Typography>
        </Box>
        <Button
          variant="contained"
          size="small"
          startIcon={<PlayArrowOutlined />}
          onClick={() => loadMutation.mutate()}
          disabled={loadMutation.isPending || !status?.available}
        >
          {loadMutation.isPending ? 'Reloading…' : 'Reload from Seeds'}
        </Button>
      </Box>

      {loadMutation.isPending && (
        <Alert severity="info" sx={{ mb: 2, py: 0.5 }}>
          Reloading from seed files — this takes a few seconds…
        </Alert>
      )}
      {loadResult && <Alert severity="success" sx={{ mb: 2, py: 0.5 }}>{loadResult}</Alert>}
      {loadError  && <Alert severity="error"   sx={{ mb: 2, py: 0.5 }}>{loadError}</Alert>}

      {isLoading && <CircularProgress size={20} />}

      {status && !isLoading && (
        <>
          {!status.available && (
            <Alert severity="warning" sx={{ mb: 2, py: 0.5 }}>
              OpenSearch not available — reference corpus cannot be loaded.
            </Alert>
          )}

          {status.available && !status.indexed && (
            <Alert severity="info" sx={{ mb: 2, py: 0.5 }}>
              No reference corpus indexed yet. Click "Load / Reload Corpus" to extract and index all ISO documents.
            </Alert>
          )}

          {status.indexed && (
            <Box sx={{ mb: 2 }}>
              <Typography variant="body2" color="text.secondary" gutterBottom>
                {status.total_chunks.toLocaleString()} chunks indexed across {status.standards.length} standards
              </Typography>
            </Box>
          )}

          {status.standards.length > 0 && (
            <TableContainer component={Card}>
              <Table size="small">
                <TableHead>
                  <TableRow>
                    <TableCell>Standard</TableCell>
                    <TableCell align="right">Chunks</TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                  {status.standards.map((s) => (
                    <TableRow key={s.standard} hover>
                      <TableCell>
                        <Typography variant="body2" fontWeight={500}>{s.standard}</Typography>
                      </TableCell>
                      <TableCell align="right">
                        <Chip label={s.chunks.toLocaleString()} size="small"
                          sx={{ fontSize: '0.65rem', height: 18, bgcolor: 'rgba(255,255,255,0.06)' }} />
                      </TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
            </TableContainer>
          )}
        </>
      )}
    </Box>
  )
}

function ProjectHealthCard({ item, method }: { item: OrgProjectSummaryItem; method: string }) {
  const navigate = useNavigate()
  const { palette } = useTheme()
  const isLight = palette.mode === 'light'
  const STATUS_COLOR = isLight ? STATUS_COLOR_LIGHT : STATUS_COLOR_DARK
  const pct = Math.round(item.pass_rate * 100)
  const barColor =
    pct >= 80 ? (isLight ? '#1b5e20' : '#C6EFCE') :
    pct >= 50 ? (isLight ? '#7a4800' : '#FFEB9C') : (isLight ? '#9e0000' : '#FFC7CE')

  return (
    <Card
      sx={{ cursor: 'pointer', '&:hover': { bgcolor: 'rgba(255,255,255,0.04)' }, transition: 'background 0.15s' }}
      onClick={() => navigate(`/projects/${item.project_id}`)}
    >
      <CardContent sx={{ pb: '12px !important' }}>
        <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', mb: 0.75 }}>
          <Box sx={{ flex: 1, minWidth: 0 }}>
            <Typography
              variant="body2"
              fontWeight={600}
              sx={{ fontSize: '0.8rem', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}
            >
              {item.project_name}
            </Typography>
            <Chip
              label={item.product_family}
              size="small"
              sx={{
                height: 16, fontSize: '0.6rem', mt: 0.25,
                bgcolor: item.product_family === 'PRIVACY' ? 'rgba(112,48,159,0.15)' :
                         item.product_family === 'CLOUD' ? 'rgba(0,153,204,0.15)' :
                         item.product_family === 'AI' ? 'rgba(255,107,53,0.15)' : 'rgba(68,114,196,0.15)',
                color: item.product_family === 'PRIVACY' ? '#c084fc' :
                       item.product_family === 'CLOUD' ? '#67e8f9' :
                       item.product_family === 'AI' ? '#ff6b35' : '#93bbf5',
              }}
            />
          </Box>
          <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.5, ml: 1 }}>
            <Typography variant="h5" fontWeight={700} sx={{ color: barColor, lineHeight: 1 }}>
              {pct}%
            </Typography>
            <OpenInNewOutlined sx={{ fontSize: 13, color: 'text.disabled' }} />
          </Box>
        </Box>

        <LinearProgress
          variant="determinate"
          value={pct}
          sx={{
            mb: 1.5, height: 5, borderRadius: 3,
            bgcolor: isLight ? 'rgba(0,0,0,0.08)' : 'rgba(255,255,255,0.08)',
            '& .MuiLinearProgress-bar': { bgcolor: barColor },
          }}
        />

        <Box sx={{ display: 'flex', gap: 0.75, flexWrap: 'wrap' }}>
          <Chip label={`${item.pass} pass`} size="small"
            sx={{ fontSize: '0.62rem', height: 17, bgcolor: STATUS_COLOR.pass.bg, color: STATUS_COLOR.pass.fg }} />
          {item.warning > 0 && (
            <Chip label={`${item.warning} warn`} size="small"
              sx={{ fontSize: '0.62rem', height: 17, bgcolor: STATUS_COLOR.warning.bg, color: STATUS_COLOR.warning.fg }} />
          )}
          {item.fail > 0 && (
            <Chip label={`${item.fail} fail`} size="small"
              sx={{ fontSize: '0.62rem', height: 17, bgcolor: STATUS_COLOR.fail.bg, color: STATUS_COLOR.fail.fg }} />
          )}
          {item.needs_review > 0 && (
            <Chip label={`${item.needs_review} review`} size="small"
              sx={{ fontSize: '0.62rem', height: 17 }} />
          )}
          <Typography variant="caption" color="text.disabled" sx={{ alignSelf: 'center', fontSize: '0.62rem' }}>
            / {item.total}
          </Typography>
        </Box>

        {item.last_run && (
          <Typography variant="caption" color="text.disabled" sx={{ fontSize: '0.6rem', display: 'block', mt: 0.75 }}>
            {dayjs(item.last_run).fromNow()} · {METHOD_LABELS[method] ?? method}
          </Typography>
        )}
      </CardContent>
    </Card>
  )
}

function OrgProjectsTab() {
  const [method, setMethod] = useState<string>('existence')
  const { palette } = useTheme()
  const isLight = palette.mode === 'light'

  const { data: projects = [], isLoading } = useQuery({
    queryKey: ['qa', 'org-projects', method],
    queryFn: () => qaApi.getOrgProjectSummaries(method),
  })

  const avgPassRate = projects.length
    ? Math.round(projects.reduce((s, p) => s + p.pass_rate, 0) / projects.length * 100)
    : null

  return (
    <Box>
      <Box sx={{ display: 'flex', alignItems: 'center', gap: 2, mb: 2.5 }}>
        <ToggleButtonGroup
          value={method}
          exclusive
          onChange={(_, v) => v && setMethod(v)}
          size="small"
        >
          <ToggleButton value="existence">Existence</ToggleButton>
          <ToggleButton value="keyword">Keyword</ToggleButton>
          <ToggleButton value="semantic">Mini LLM</ToggleButton>
        </ToggleButtonGroup>

        {avgPassRate !== null && (
          <Typography variant="caption" color="text.secondary">
            {projects.length} project{projects.length !== 1 ? 's' : ''} — avg pass rate{' '}
            <Box component="span" sx={{ color: avgPassRate >= 80 ? (isLight ? '#1b5e20' : '#C6EFCE') : avgPassRate >= 50 ? (isLight ? '#7a4800' : '#FFEB9C') : (isLight ? '#9e0000' : '#FFC7CE'), fontWeight: 600 }}>
              {avgPassRate}%
            </Box>
          </Typography>
        )}
      </Box>

      {isLoading && (
        <Grid container spacing={2}>
          {[...Array(6)].map((_, i) => (
            <Grid item xs={12} sm={6} md={4} lg={3} key={i}>
              <Box sx={{ height: 120, bgcolor: 'rgba(255,255,255,0.04)', borderRadius: 1 }} />
            </Grid>
          ))}
        </Grid>
      )}

      {!isLoading && projects.length === 0 && (
        <Alert severity="info">
          No projects have run QA yet. Open a project and use the QA tab to run checks.
        </Alert>
      )}

      {!isLoading && projects.length > 0 && (
        <Grid container spacing={2}>
          {projects.map(p => (
            <Grid item xs={12} sm={6} md={4} lg={3} key={p.project_id}>
              <ProjectHealthCard item={p} method={method} />
            </Grid>
          ))}
        </Grid>
      )}
    </Box>
  )
}

export default function QA() {
  const queryClient = useQueryClient()
  const { product: activeProduct } = useProduct()
  const [tab, setTab] = useState(0)
  const [method, setMethod] = useState<string>('existence')
  const [product, setProduct] = useState<string>('all')
  const [status, setStatus] = useState<string>('all')
  const [runResult, setRunResult] = useState<string | null>(null)
  const { palette } = useTheme()
  const isLight = palette.mode === 'light'
  const STATUS_COLOR = isLight ? STATUS_COLOR_LIGHT : STATUS_COLOR_DARK
  const STATUS_ICON = {
    pass: <CheckCircleOutlined sx={{ fontSize: 14, color: isLight ? '#1b5e20' : '#C6EFCE' }} />,
    warning: <WarningAmberOutlined sx={{ fontSize: 14, color: isLight ? '#7a4800' : '#FFEB9C' }} />,
    fail: <ErrorOutlined sx={{ fontSize: 14, color: isLight ? '#9e0000' : '#FFC7CE' }} />,
    needs_review: <HelpOutlineOutlined sx={{ fontSize: 14, color: isLight ? '#555' : '#d9d9d9' }} />,
  }

  const { data: corpusStatus } = useQuery<ReferenceCorpusStatus>({
    queryKey: ['qa', 'reference-corpus', 'status'],
    queryFn: qaApi.getReferenceCorpusStatus,
    staleTime: 60_000,
  })

  const { data: summary } = useQuery({
    queryKey: ['qa', 'summary', method, product],
    queryFn: () => qaApi.getSummary(method, product),
  })

  const { data: results, isLoading } = useQuery({
    queryKey: ['qa', 'results', method, product, status],
    queryFn: () =>
      qaApi.getResults({
        method,
        product_type: product !== 'all' ? product : undefined,
        status: status !== 'all' ? status : undefined,
        limit: 200,
      }),
  })

  const existenceMutation = useMutation({
    mutationFn: qaApi.runExistence,
    onSuccess: (data) => {
      queryClient.invalidateQueries({ queryKey: ['qa'] })
      setRunResult(`Existence check complete in ${data.duration_ms}ms — ${data.pass_count} pass, ${data.warning_count} warning, ${data.fail_count} fail`)
    },
  })

  const keywordMutation = useMutation({
    mutationFn: qaApi.runKeyword,
    onSuccess: (data) => {
      queryClient.invalidateQueries({ queryKey: ['qa'] })
      setRunResult(`Keyword check complete in ${data.duration_ms}ms — ${data.pass_count} pass, ${data.warning_count} warning, ${data.fail_count} fail, ${data.needs_review_count} review`)
    },
  })

  const semanticMiniMutation = useMutation({
    mutationFn: qaApi.runSemanticMini,
    onSuccess: (data) => {
      queryClient.invalidateQueries({ queryKey: ['qa'] })
      setRunResult(`Mini LLM semantic check complete in ${data.duration_ms}ms — ${data.pass_count} pass, ${data.warning_count} warning, ${data.fail_count} fail, ${data.needs_review_count} review`)
    },
  })

  const semanticClaudeMutation = useMutation({
    mutationFn: qaApi.runSemanticClaude,
    onSuccess: (data) => {
      queryClient.invalidateQueries({ queryKey: ['qa'] })
      setRunResult(`Claude AI semantic check complete in ${data.duration_ms}ms — ${data.pass_count} pass, ${data.warning_count} warning, ${data.fail_count} fail, ${data.needs_review_count} review`)
    },
  })

  const isRunning =
    existenceMutation.isPending ||
    keywordMutation.isPending ||
    semanticMiniMutation.isPending ||
    semanticClaudeMutation.isPending

  const hasError =
    existenceMutation.isError ||
    keywordMutation.isError ||
    semanticMiniMutation.isError ||
    semanticClaudeMutation.isError

  const errorMsg =
    semanticClaudeMutation.error instanceof Error
      ? semanticClaudeMutation.error.message
      : 'Failed to run QA check.'

  const overallPct = summary ? Math.round(summary.overall_pass_rate * 100) : null
  const overallColor =
    overallPct === null ? 'text.secondary' :
    overallPct >= 80 ? (isLight ? '#1b5e20' : '#C6EFCE') :
    overallPct >= 50 ? (isLight ? '#7a4800' : '#FFEB9C') : (isLight ? '#9e0000' : '#FFC7CE')

  // Which product cards to show
  const isExistence = method === 'existence'
  const showFw  = product === 'all' || product === 'framework' || product === 'isms'
  const showOp  = isExistence && (product === 'all' || product === 'operational')
  const showPrv = product === 'all' || product === 'privacy'
  const showCld = product === 'all' || product === 'cloud'
  const showAi  = product === 'all' || product === 'ai'
  const methodSubtitle = METHOD_SUBTITLES[method] ?? ''

  return (
    <Box>
      <PageHeader
        title="QA"
        subtitle={tab === 0 ? methodSubtitle : tab === 1 ? 'Manage the synonym dictionary used by keyword correlation' : tab === 2 ? (corpusStatus?.indexed ? `ISO & regulatory normative corpus — ${corpusStatus.standards.length} standards, ${corpusStatus.total_chunks.toLocaleString()} indexed chunks` : 'ISO & regulatory normative corpus') : 'Per-project QA health — click any card to open the project QA tab'}
        actions={tab === 0 ? (
          <Stack direction="row" spacing={1} alignItems="center" flexWrap="wrap">
            {summary?.last_run && (
              <Typography variant="caption" color="text.secondary">
                Last run {dayjs(summary.last_run).fromNow()}
              </Typography>
            )}
            <Button
              variant={method === 'existence' ? 'contained' : 'outlined'}
              size="small"
              startIcon={existenceMutation.isPending ? <CircularProgress size={14} /> : <PlayArrowOutlined />}
              onClick={() => { setRunResult(null); setMethod('existence'); existenceMutation.mutate() }}
              disabled={isRunning}
            >
              {existenceMutation.isPending ? 'Running...' : 'Run Existence'}
            </Button>
            <Button
              variant={method === 'keyword' ? 'contained' : 'outlined'}
              size="small"
              color="secondary"
              startIcon={keywordMutation.isPending ? <CircularProgress size={14} /> : <PlayArrowOutlined />}
              onClick={() => { setRunResult(null); setMethod('keyword'); keywordMutation.mutate() }}
              disabled={isRunning}
            >
              {keywordMutation.isPending ? 'Running...' : 'Run Keyword'}
            </Button>
            <Button
              variant={method === 'semantic' ? 'contained' : 'outlined'}
              size="small"
              startIcon={semanticMiniMutation.isPending ? <CircularProgress size={14} /> : <PsychologyOutlined />}
              onClick={() => { setRunResult(null); setMethod('semantic'); semanticMiniMutation.mutate() }}
              disabled={isRunning}
              sx={{ borderColor: 'rgba(68,114,196,0.6)', color: method === 'semantic' ? undefined : '#9DC3E6' }}
            >
              {semanticMiniMutation.isPending ? 'Running...' : 'Run Mini LLM'}
            </Button>
            <Button
              variant={method === 'semantic_claude' ? 'contained' : 'outlined'}
              size="small"
              startIcon={semanticClaudeMutation.isPending ? <CircularProgress size={14} /> : <AutoAwesomeOutlined />}
              onClick={() => { setRunResult(null); setMethod('semantic_claude'); semanticClaudeMutation.mutate() }}
              disabled={isRunning}
              sx={{ borderColor: 'rgba(198,146,20,0.6)', color: method === 'semantic_claude' ? undefined : '#FFEB9C' }}
            >
              {semanticClaudeMutation.isPending ? 'Running...' : 'Run Claude AI'}
            </Button>
          </Stack>
        ) : undefined}
      />

      {runResult && (
        <Alert severity="success" onClose={() => setRunResult(null)} sx={{ mb: 2 }}>
          {runResult}
        </Alert>
      )}

      {hasError && (
        <Alert severity="error" sx={{ mb: 2 }}>{errorMsg}</Alert>
      )}

      {/* Top-level tabs */}
      <Tabs value={tab} onChange={(_, v) => setTab(v)} sx={{ mb: 2, borderBottom: 1, borderColor: 'divider' }}>
        <Tab label="Results" />
        <Tab label="Synonyms" />
        <Tab label="Reference Corpus" />
        <Tab label="Projects" />
      </Tabs>

      {tab === 1 && <SynonymsTab />}
      {tab === 2 && <ReferenceCorpusTab />}
      {tab === 3 && <OrgProjectsTab />}

      {tab === 0 && <>

      {/* Method toggle */}
      <Box sx={{ mb: 2, display: 'flex', alignItems: 'center', gap: 1 }}>
        <ToggleButtonGroup
          value={method}
          exclusive
          onChange={(_, v) => { if (v) { setMethod(v); setProduct('all'); setStatus('all') } }}
          size="small"
        >
          <ToggleButton value="existence">Existence</ToggleButton>
          <ToggleButton value="keyword">Keyword</ToggleButton>
          <ToggleButton value="semantic">
            <PsychologyOutlined sx={{ fontSize: 14, mr: 0.5 }} />
            Mini LLM
          </ToggleButton>
          <ToggleButton value="semantic_claude">
            <AutoAwesomeOutlined sx={{ fontSize: 14, mr: 0.5 }} />
            Claude AI
          </ToggleButton>
        </ToggleButtonGroup>
        <MethodLegendPopover method={method} />
      </Box>

      <Divider sx={{ mb: 2 }} />

      {/* Summary cards */}
      {summary && (
        <Grid container spacing={2} sx={{ mb: 2 }}>
          {/* Overall */}
          <Grid item xs={12} md={3}>
            <Card>
              <CardContent sx={{ pb: '12px !important', textAlign: 'center' }}>
                <Typography variant="caption" color="text.secondary">Overall Pass Rate</Typography>
                <Typography variant="h3" fontWeight={700} sx={{ color: overallColor }}>
                  {overallPct}%
                </Typography>
                <Typography variant="caption" color="text.secondary">
                  {summary.framework.pass_count + summary.operational.pass_count + summary.privacy.pass_count + summary.cloud.pass_count + (summary.ai?.pass_count ?? 0)}
                  {' / '}
                  {summary.framework.total + summary.operational.total + summary.privacy.total + summary.cloud.total + (summary.ai?.total ?? 0)} checks passing
                </Typography>
              </CardContent>
            </Card>
          </Grid>
          {showFw  && <Grid item xs={12} md={3}><SummaryCard label="Framework"   bucket={summary.framework}   color="#4472C4" /></Grid>}
          {showOp  && <Grid item xs={12} md={3}><SummaryCard label="Operational" bucket={summary.operational} color="#70AD47" /></Grid>}
          {showPrv && <Grid item xs={12} md={3}><SummaryCard label="Privacy"     bucket={summary.privacy}     color={PRODUCT_COLORS.privacy} /></Grid>}
          {showCld && <Grid item xs={12} md={3}><SummaryCard label="Cloud"       bucket={summary.cloud}       color={PRODUCT_COLORS.cloud} /></Grid>}
          {showAi  && summary.ai?.total > 0 && <Grid item xs={12} md={3}><SummaryCard label="AI"    bucket={summary.ai}          color="#ff6b35" /></Grid>}
        </Grid>
      )}

      {/* Filters */}
      <Box sx={{ display: 'flex', gap: 2, mb: 2, flexWrap: 'wrap' }}>
        {method === 'existence' && (
          <ToggleButtonGroup
            value={product}
            exclusive
            onChange={(_, v) => v && setProduct(v)}
            size="small"
          >
            <ToggleButton value="all">All</ToggleButton>
            <ToggleButton value="framework">Framework</ToggleButton>
            <ToggleButton value="operational">Operational</ToggleButton>
            <ToggleButton value="privacy">Privacy</ToggleButton>
            <ToggleButton value="cloud">Cloud</ToggleButton>
            <ToggleButton value="ai">AI</ToggleButton>
          </ToggleButtonGroup>
        )}
        {(method === 'keyword' || isSemantic(method)) && (
          <ToggleButtonGroup
            value={product}
            exclusive
            onChange={(_, v) => v && setProduct(v)}
            size="small"
          >
            <ToggleButton value="all">All</ToggleButton>
            <ToggleButton value="isms">ISMS</ToggleButton>
            <ToggleButton value="privacy">Privacy</ToggleButton>
            <ToggleButton value="cloud">Cloud</ToggleButton>
            <ToggleButton value="ai">AI</ToggleButton>
          </ToggleButtonGroup>
        )}

        <ToggleButtonGroup
          value={status}
          exclusive
          onChange={(_, v) => v && setStatus(v)}
          size="small"
        >
          <ToggleButton value="all">All</ToggleButton>
          <ToggleButton value="pass" sx={{ color: isLight ? '#1b5e20' : '#C6EFCE' }}>Pass</ToggleButton>
          <ToggleButton value="warning" sx={{ color: isLight ? '#7a4800' : '#FFEB9C' }}>Warning</ToggleButton>
          <ToggleButton value="fail" sx={{ color: isLight ? '#9e0000' : '#FFC7CE' }}>Fail</ToggleButton>
          <ToggleButton value="needs_review">Review</ToggleButton>
        </ToggleButtonGroup>

        {results && (
          <Typography variant="caption" color="text.secondary" sx={{ alignSelf: 'center' }}>
            {results.length} result{results.length !== 1 ? 's' : ''}
          </Typography>
        )}
      </Box>

      {/* Results table */}
      {!summary?.last_run && !isLoading && (
        <Alert severity="info">
          No {METHOD_LABELS[method] ?? method} results yet. Click the corresponding Run button above.
        </Alert>
      )}

      {(results?.length ?? 0) > 0 && (
        <TableContainer component={Card}>
          <Table size="small">
            <TableHead>
              <TableRow>
                <TableCell>Control Group</TableCell>
                {!isSemantic(method) && <TableCell>Product</TableCell>}
                <TableCell>Status</TableCell>
                <TableCell>Strength</TableCell>
                <TableCell>{method === 'semantic_claude' ? 'Reasoning' : method === 'semantic' ? 'Method' : 'Present'}</TableCell>
                <TableCell>{method === 'semantic_claude' ? 'Gaps' : method === 'semantic' ? '' : 'Missing'}</TableCell>
                <TableCell>Run</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {isLoading &&
                [...Array(6)].map((_, i) => (
                  <TableRow key={i}>
                    {[...Array(7)].map((_, j) => (
                      <TableCell key={j}>
                        <Box sx={{ height: 14, bgcolor: 'rgba(255,255,255,0.05)', borderRadius: 1 }} />
                      </TableCell>
                    ))}
                  </TableRow>
                ))}
              {results?.map((row) => {
                const sc = STATUS_COLOR[row.qa_status] ?? STATUS_COLOR.needs_review
                return (
                  <TableRow key={row.id} hover>
                    <TableCell>
                      <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.75 }}>
                        <Typography variant="body2" fontWeight={600}>
                          {row.control_group_code}
                        </Typography>
                        {row.metadata?.language && (
                          <Chip
                            label={(row.metadata.language as string).toUpperCase()}
                            size="small"
                            sx={{ fontSize: '0.55rem', height: 15, bgcolor: 'rgba(255,255,255,0.07)', color: 'text.secondary' }}
                          />
                        )}
                      </Box>
                      <Typography variant="caption" color="text.secondary">
                        {row.control_group_name}
                      </Typography>
                    </TableCell>
                    {!isSemantic(method) && (
                      <TableCell>
                        <Chip
                          label={row.product_type}
                          size="small"
                          sx={{
                            fontSize: '0.65rem',
                            height: 18,
                            bgcolor: `${PRODUCT_TYPE_COLOR[row.product_type] ?? '#888'}22`,
                            color: PRODUCT_TYPE_COLOR[row.product_type] ?? '#aaa',
                          }}
                        />
                      </TableCell>
                    )}
                    <TableCell>
                      <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.5 }}>
                        {STATUS_ICON[row.qa_status as keyof typeof STATUS_ICON]}
                        <Chip
                          label={row.qa_status.replace('_', ' ')}
                          size="small"
                          sx={{ fontSize: '0.65rem', height: 18, bgcolor: sc.bg, color: sc.fg }}
                        />
                      </Box>
                    </TableCell>
                    <TableCell>
                      <Tooltip title={`${Math.round(row.correlation_strength * 100)}%`}>
                        <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                          <LinearProgress
                            variant="determinate"
                            value={row.correlation_strength * 100}
                            sx={{
                              width: 60,
                              height: 6,
                              borderRadius: 3,
                              bgcolor: isLight ? 'rgba(0,0,0,0.08)' : 'rgba(255,255,255,0.08)',
                              '& .MuiLinearProgress-bar': {
                                bgcolor:
                                  row.qa_status === 'pass' ? (isLight ? '#1b5e20' : '#C6EFCE') :
                                  row.qa_status === 'warning' ? (isLight ? '#7a4800' : '#FFEB9C') : (isLight ? '#9e0000' : '#FFC7CE'),
                              },
                            }}
                          />
                          <Typography variant="caption" color="text.secondary">
                            {Math.round(row.correlation_strength * 100)}%
                          </Typography>
                        </Box>
                      </Tooltip>
                    </TableCell>
                    <TableCell><DetailsCell row={row} method={method} /></TableCell>
                    <TableCell><MissingCell row={row} method={method} /></TableCell>
                    <TableCell>
                      <Typography variant="caption" color="text.secondary">
                        {dayjs(row.run_date).format('DD MMM HH:mm')}
                      </Typography>
                    </TableCell>
                  </TableRow>
                )
              })}
            </TableBody>
          </Table>
        </TableContainer>
      )}

      </>}
    </Box>
  )
}
