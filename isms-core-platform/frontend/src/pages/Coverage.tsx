import { useState, useMemo } from 'react'
import { useTheme } from '@mui/material/styles'
import { useProduct, PRODUCT_SUBTITLES, PRODUCT_COLORS } from '../store/ProductContext'
import { LockPersonOutlined, CloudOutlined, PsychologyOutlined, ExpandMoreOutlined, ExpandLessOutlined } from '@mui/icons-material'
import {
  Box,
  Card,
  CardContent,
  Collapse,
  IconButton,
  LinearProgress,
  Tab,
  Tabs,
  Typography,
  Select,
  MenuItem,
  FormControl,
  InputLabel,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Chip,
  Skeleton,
  Alert,
  Grid,
  TablePagination,
  Switch,
  FormControlLabel,
  Tooltip,
} from '@mui/material'
import { useQuery } from '@tanstack/react-query'
import { useNavigate } from 'react-router-dom'
import { dashboardApi, type CoverageGap } from '../api/dashboard'
import { projectsApi, type ProjectRead } from '../api/projectsApi'
import { useProject } from '../store/ProjectContext'
import { client } from '../api/client'
import { customFrameworksApi } from '../api/customFrameworksApi'
import PageHeader from '../components/PageHeader'

interface CoverageMapping {
  framework: string
  framework_code: string
  control_id: string
  control_title: string
  mapping_type: string
  confidence: number
}

interface CoverageRow {
  iso_control_id: string
  iso_control_title: string
  control_group_code: string
  mappings: CoverageMapping[]
}

interface RealCoverage {
  frameworks: string[]
  total_iso_controls: number
  total_mappings: number
  by_framework: Record<string, number>
  rows: CoverageRow[]
}

// Map product → source framework code prefix sent to the API
const PRODUCT_SOURCE_FRAMEWORK: Record<string, string> = {
  isms:    'ISO27001',
  privacy: 'ISO27701',
  cloud:   'ISO27017',
  ai:      'ISO42001',
}

const PRODUCT_ISO_LABEL: Record<string, string> = {
  isms:    'ISO 27001',
  privacy: 'ISO 27701',
  cloud:   'ISO 27018:2025',
  ai:      'ISO 42001',
}

// Human-readable label for the source control column
const SOURCE_CONTROL_LABEL: Record<string, string> = {
  isms:     'ISO 27001 Control',
  privacy:  'ISO 27701 Control',
  cloud:    'ISO 27017 Control',
  ai:       'ISO 42001 Control',
  ISO27017: 'ISO 27017 Control',
  ISO27018: 'ISO 27018 Control',
}

// ISO 27000-family extension standards — shown with amber accent in framework pills
const ISO_EXTENSIONS = new Set(['ISO27017', 'ISO27018', 'ISO27701'])

const CONFIDENCE_COLOR_DARK = (c: number) =>
  c >= 0.8 ? { bg: 'rgba(198,239,206,0.15)', color: '#C6EFCE' }
  : c >= 0.6 ? { bg: 'rgba(255,235,156,0.12)', color: '#FFEB9C' }
  : { bg: 'rgba(255,199,206,0.12)', color: '#FFC7CE' }

const CONFIDENCE_COLOR_LIGHT = (c: number) =>
  c >= 0.8 ? { bg: 'rgba(46,125,50,0.15)', color: '#1b5e20' }
  : c >= 0.6 ? { bg: 'rgba(230,145,0,0.15)', color: '#9a6500' }
  : { bg: 'rgba(192,0,0,0.12)', color: '#9e0000' }

const MISSING_CHIP_DARK: Record<string, { bg: string; color: string }> = {
  policy:      { bg: 'rgba(192,0,0,0.15)',    color: '#FFC7CE' },
  UG:          { bg: 'rgba(255,192,0,0.12)',   color: '#FFEB9C' },
  TG:          { bg: 'rgba(255,192,0,0.12)',   color: '#FFEB9C' },
  assessment:  { bg: 'rgba(192,0,0,0.15)',    color: '#FFC7CE' },
}

const MISSING_CHIP_LIGHT: Record<string, { bg: string; color: string }> = {
  policy:      { bg: 'rgba(192,0,0,0.12)',    color: '#9e0000' },
  UG:          { bg: 'rgba(230,145,0,0.15)',   color: '#9a6500' },
  TG:          { bg: 'rgba(230,145,0,0.15)',   color: '#9a6500' },
  assessment:  { bg: 'rgba(192,0,0,0.12)',    color: '#9e0000' },
}

// ── Inferred Coverage tab (DARK/LIGHT variants selected inside components) ────

interface InferredResult {
  framework: string
  framework_code: string
  total_controls: number
  covered_controls: number
  uncovered_controls: number
  coverage_pct: number
}

interface GapEntry {
  target_control_id: string
  target_control_title: string
  iso_controls_needed: { id: string; title: string }[]
}

const PCT_COLOR = (pct: number) =>
  pct >= 75 ? '#4CAF50' : pct >= 40 ? '#FF9800' : '#F44336'

function FrameworkCoverageCard({ result, projectId }: { result: InferredResult; projectId: string }) {
  const [expanded, setExpanded] = useState(false)
  const color = PCT_COLOR(result.coverage_pct)

  const { data: gapData, isLoading: gapLoading } = useQuery({
    queryKey: ['coverage-gap-map', result.framework_code, projectId],
    queryFn: () => client.get('/coverage/gap-map', { params: { target_framework: result.framework_code, project_id: projectId || undefined } }).then(r => r.data as { gaps: GapEntry[]; gap_count: number }),
    enabled: expanded,
  })

  return (
    <Box sx={{ border: '1px solid', borderColor: `${color}30`, borderRadius: 1.5, overflow: 'hidden', mb: 1 }}>
      <Box sx={{ display: 'flex', alignItems: 'center', gap: 2, px: 2, py: 1.25, bgcolor: `${color}08`, cursor: 'pointer' }} onClick={() => setExpanded(e => !e)}>
        <Box sx={{ flex: 1 }}>
          <Typography variant="body2" sx={{ fontWeight: 600, fontSize: '0.82rem' }}>{result.framework}</Typography>
          <Typography variant="caption" sx={{ fontSize: '0.65rem', color: 'text.disabled' }}>
            {result.covered_controls} / {result.total_controls} controls covered
          </Typography>
        </Box>
        <Box sx={{ width: 160 }}>
          <LinearProgress variant="determinate" value={result.coverage_pct}
            sx={{ height: 6, borderRadius: 3, bgcolor: `${color}20`, '& .MuiLinearProgress-bar': { bgcolor: color } }} />
        </Box>
        <Typography variant="body2" sx={{ fontWeight: 700, color, minWidth: 44, textAlign: 'right', fontSize: '0.9rem' }}>
          {result.coverage_pct}%
        </Typography>
        <IconButton size="small" sx={{ p: 0.25 }}>
          {expanded ? <ExpandLessOutlined sx={{ fontSize: 16 }} /> : <ExpandMoreOutlined sx={{ fontSize: 16 }} />}
        </IconButton>
      </Box>

      <Collapse in={expanded}>
        <Box sx={{ px: 2, py: 1.5, borderTop: '1px solid', borderColor: 'divider' }}>
          {gapLoading && <Skeleton height={40} />}
          {gapData && gapData.gap_count === 0 && (
            <Typography variant="caption" sx={{ color: 'success.main' }}>✓ Full coverage — all controls addressed</Typography>
          )}
          {gapData && gapData.gaps.length > 0 && (
            <>
              <Typography variant="caption" sx={{ fontWeight: 600, fontSize: '0.68rem', color: 'text.secondary', textTransform: 'uppercase', display: 'block', mb: 1 }}>
                {gapData.gap_count} uncovered controls
              </Typography>
              <Box sx={{ maxHeight: 280, overflowY: 'auto' }}>
                {gapData.gaps.map((g: GapEntry) => (
                  <Box key={g.target_control_id} sx={{ mb: 1, pb: 1, borderBottom: '1px solid', borderColor: 'divider', '&:last-child': { borderBottom: 'none', mb: 0, pb: 0 } }}>
                    <Typography variant="caption" sx={{ fontWeight: 600, fontSize: '0.72rem' }}>
                      {g.target_control_id} — {g.target_control_title}
                    </Typography>
                    {g.iso_controls_needed.length > 0 && (
                      <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 0.5, mt: 0.5 }}>
                        {g.iso_controls_needed.slice(0, 4).map(iso => (
                          <Chip key={iso.id} label={iso.id} size="small"
                            sx={{ height: 16, fontSize: '0.58rem', bgcolor: 'rgba(255,152,0,0.1)', color: '#FF9800' }} />
                        ))}
                        {g.iso_controls_needed.length > 4 && (
                          <Typography variant="caption" sx={{ fontSize: '0.6rem', color: 'text.disabled', alignSelf: 'center' }}>
                            +{g.iso_controls_needed.length - 4} more
                          </Typography>
                        )}
                      </Box>
                    )}
                  </Box>
                ))}
              </Box>
            </>
          )}
        </Box>
      </Collapse>
    </Box>
  )
}

function InferredCoverage() {
  const { activeProject } = useProject()
  const { product } = useProduct()
  const [projectId, setProjectId] = useState(activeProject?.id ?? '')

  const { data: projects } = useQuery({
    queryKey: ['projects-list'],
    queryFn: () => projectsApi.list(),
  })

  const { data, isLoading } = useQuery({
    queryKey: ['coverage-inferred', projectId],
    queryFn: () => client.get('/coverage/multi-framework', { params: { project_id: projectId || undefined } }).then(r => r.data as { assessed_controls: number; frameworks: InferredResult[] }),
  })

  return (
    <Box>
      <Box sx={{ display: 'flex', gap: 2, alignItems: 'center', mb: 2.5 }}>
        <FormControl size="small" sx={{ minWidth: 260 }}>
          <InputLabel>Project scope</InputLabel>
          <Select value={projectId} label="Project scope" onChange={e => setProjectId(e.target.value)}>
            <MenuItem value="">Org-wide (all assessments)</MenuItem>
            {(projects ?? []).map((p: ProjectRead) => (
              <MenuItem key={p.id} value={p.id}>{p.name}</MenuItem>
            ))}
          </Select>
        </FormControl>
        {data && (
          <Typography variant="caption" sx={{ color: 'text.disabled' }}>
            Based on {data.assessed_controls} assessed {PRODUCT_ISO_LABEL[product] ?? 'ISO 27001'} control groups
          </Typography>
        )}
      </Box>

      {isLoading && [0,1,2,3,4].map(i => <Skeleton key={i} height={52} sx={{ mb: 1 }} />)}

      {data?.frameworks.filter(f => f.total_controls > 0).map(r => (
        <FrameworkCoverageCard key={r.framework_code} result={r} projectId={projectId} />
      ))}

      {data?.frameworks.length === 0 && (
        <Alert severity="info" sx={{ mt: 2 }}>No crosswalk data loaded — run the dataset bootstrap to load framework mappings.</Alert>
      )}
    </Box>
  )
}

// ── Custom Framework Coverage ─────────────────────────────────────────────────

interface CustomCoverageControl {
  control_id: string
  title: string
  category: string | null
  covered: boolean
  matched_iso: string[]
}

interface CustomCoverageResult {
  framework_id: string
  framework_name: string
  short_code: string
  total_controls: number
  covered_controls: number
  coverage_pct: number
  controls: CustomCoverageControl[]
}

function CustomFrameworkCoverage({ frameworkId, frameworkName, shortCode, projectId }: {
  frameworkId: string
  frameworkName: string
  shortCode: string
  projectId: string
}) {
  const [expanded, setExpanded] = useState(false)
  const { palette } = useTheme()
  const isLight = palette.mode === 'light'

  const { data, isLoading } = useQuery({
    queryKey: ['coverage-custom', frameworkId, projectId],
    queryFn: () => client.get<CustomCoverageResult>(`/coverage/custom/${frameworkId}`, {
      params: { project_id: projectId || undefined },
    }).then(r => r.data),
  })

  const color = data ? PCT_COLOR(data.coverage_pct) : '#9E9E9E'

  return (
    <Box sx={{ border: '1px solid', borderColor: `${color}30`, borderRadius: 1.5, overflow: 'hidden', mb: 1 }}>
      <Box
        sx={{ display: 'flex', alignItems: 'center', gap: 2, px: 2, py: 1.25, bgcolor: `${color}08`, cursor: 'pointer' }}
        onClick={() => setExpanded(e => !e)}
      >
        <Chip
          label={shortCode}
          size="small"
          sx={{ height: 18, fontSize: '0.62rem', fontWeight: 700, bgcolor: isLight ? 'rgba(230,160,0,0.15)' : 'rgba(255,192,0,0.12)', color: isLight ? '#7a4800' : '#FFC000', borderRadius: 0.75 }}
        />
        <Box sx={{ flex: 1 }}>
          <Typography variant="body2" sx={{ fontWeight: 600, fontSize: '0.82rem' }}>{frameworkName}</Typography>
          {data && (
            <Typography variant="caption" sx={{ fontSize: '0.65rem', color: 'text.disabled' }}>
              {data.covered_controls} / {data.total_controls} controls covered
            </Typography>
          )}
          {isLoading && <Skeleton width={120} height={14} />}
        </Box>
        {data && (
          <>
            <Box sx={{ width: 160 }}>
              <LinearProgress
                variant="determinate"
                value={data.coverage_pct}
                sx={{ height: 6, borderRadius: 3, bgcolor: `${color}20`, '& .MuiLinearProgress-bar': { bgcolor: color } }}
              />
            </Box>
            <Typography variant="body2" sx={{ fontWeight: 700, color, minWidth: 44, textAlign: 'right', fontSize: '0.9rem' }}>
              {data.coverage_pct}%
            </Typography>
          </>
        )}
        <IconButton size="small" sx={{ p: 0.25 }}>
          {expanded ? <ExpandLessOutlined sx={{ fontSize: 16 }} /> : <ExpandMoreOutlined sx={{ fontSize: 16 }} />}
        </IconButton>
      </Box>

      <Collapse in={expanded}>
        <Box sx={{ px: 2, py: 1.5, borderTop: '1px solid', borderColor: 'divider' }}>
          {isLoading && <Skeleton height={40} />}
          {data && data.controls.length === 0 && (
            <Typography variant="caption" color="text.secondary">No controls defined for this framework.</Typography>
          )}
          {data && data.controls.length > 0 && (
            <Box sx={{ maxHeight: 320, overflowY: 'auto' }}>
              {data.controls.map(ctrl => (
                <Box
                  key={ctrl.control_id}
                  sx={{ display: 'flex', alignItems: 'flex-start', gap: 1.5, mb: 0.75, pb: 0.75, borderBottom: '1px solid', borderColor: 'divider', '&:last-child': { borderBottom: 'none', mb: 0, pb: 0 } }}
                >
                  <Box sx={{ width: 8, height: 8, borderRadius: '50%', mt: 0.6, flexShrink: 0, bgcolor: ctrl.covered ? (isLight ? '#2e7d32' : '#C6EFCE') : (isLight ? '#c62828' : '#FFC7CE') }} />
                  <Box sx={{ flex: 1, minWidth: 0 }}>
                    <Typography variant="caption" sx={{ fontWeight: 600, fontSize: '0.72rem', display: 'block' }}>
                      {ctrl.control_id}
                      {ctrl.category && (
                        <Typography component="span" variant="caption" sx={{ ml: 0.75, fontWeight: 400, color: 'text.disabled', fontSize: '0.65rem' }}>
                          {ctrl.category}
                        </Typography>
                      )}
                    </Typography>
                    <Typography variant="caption" color="text.secondary" sx={{ fontSize: '0.68rem', display: 'block', lineHeight: 1.3 }}>
                      {ctrl.title}
                    </Typography>
                    {ctrl.covered && ctrl.matched_iso.length > 0 && (
                      <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 0.4, mt: 0.4 }}>
                        {ctrl.matched_iso.slice(0, 5).map(ref => (
                          <Chip
                            key={ref}
                            label={ref}
                            size="small"
                            sx={{ height: 14, fontSize: '0.58rem', bgcolor: isLight ? 'rgba(46,125,50,0.12)' : 'rgba(198,239,206,0.1)', color: isLight ? '#1b5e20' : '#C6EFCE' }}
                          />
                        ))}
                        {ctrl.matched_iso.length > 5 && (
                          <Typography variant="caption" sx={{ fontSize: '0.6rem', color: 'text.disabled', alignSelf: 'center' }}>
                            +{ctrl.matched_iso.length - 5} more
                          </Typography>
                        )}
                      </Box>
                    )}
                  </Box>
                </Box>
              ))}
            </Box>
          )}
        </Box>
      </Collapse>
    </Box>
  )
}

// ── Main page ─────────────────────────────────────────────────────────────────

export default function Coverage() {
  const { product, ismsTier } = useProduct()
  const { palette } = useTheme()
  const isLight = palette.mode === 'light'
  const [activeTab, setActiveTab] = useState(0)
  const [selectedFramework, setSelectedFramework] = useState('')
  const [showUnmapped, setShowUnmapped] = useState(false)
  const [page, setPage] = useState(0)
  const [cloudSub, setCloudSub] = useState<'ISO27017' | 'ISO27018'>('ISO27017')
  const [gapProduct, setGapProduct] = useState<'framework' | 'operational'>(
    ismsTier === 'operational' ? 'operational' : 'framework'
  )
  const ROWS_PER_PAGE = 25
  const navigate = useNavigate()

  const sourceFramework = product === 'cloud'
    ? cloudSub
    : (PRODUCT_SOURCE_FRAMEWORK[product] ?? 'ISO27001')

  const { data, isLoading, error } = useQuery({
    queryKey: ['dashboard', 'coverage', sourceFramework],
    queryFn: () => dashboardApi.getCoverage({ source_framework: sourceFramework }),
  })

  const { data: gapsData } = useQuery({
    queryKey: ['coverage-gaps', gapProduct],
    queryFn: () => dashboardApi.getCoverageGaps(gapProduct),
  })
  const gaps: CoverageGap[] = gapsData ?? []

  const { data: customFrameworks } = useQuery({
    queryKey: ['custom-frameworks'],
    queryFn: () => customFrameworksApi.list(),
  })

  const cov = data as unknown as RealCoverage | undefined

  const activeFramework = selectedFramework || (cov?.frameworks[0] ?? '')

  const sortedFrameworks = useMemo(() => {
    if (!cov?.frameworks || !cov?.by_framework) return cov?.frameworks ?? []
    return [...new Set(cov.frameworks)]
      .sort((a, b) => (cov.by_framework[b] ?? 0) - (cov.by_framework[a] ?? 0))
  }, [cov])

  const filteredRows = useMemo(() => {
    if (!cov?.rows) return []
    if (showUnmapped) {
      // Show rows with NO mappings for the active framework
      return cov.rows.filter((row) =>
        !row.mappings.some((m) => m.framework === activeFramework)
      )
    }
    if (!activeFramework) return cov.rows
    return cov.rows.filter((row) =>
      row.mappings.some((m) => m.framework === activeFramework)
    )
  }, [cov, activeFramework, showUnmapped])

  const pagedRows = useMemo(() =>
    filteredRows.slice(page * ROWS_PER_PAGE, (page + 1) * ROWS_PER_PAGE),
    [filteredRows, page]
  )

  const frameworkCount = activeFramework ? (cov?.by_framework[activeFramework] ?? 0) : 0

  return (
    <Box>
      <PageHeader
        title="Framework Coverage"
        subtitle={activeTab === 0
          ? `${PRODUCT_SUBTITLES[product]} mapped to ${cov?.frameworks.length ?? '...'} frameworks · ${(cov?.total_mappings ?? 0).toLocaleString()} total mappings`
          : 'Inferred compliance coverage across target frameworks based on project assessments'}
        actions={
          activeTab === 0 && cov && (
            <FormControl size="small" sx={{ minWidth: 240 }}>
              <InputLabel>Framework</InputLabel>
              <Select
                value={activeFramework}
                onChange={(e) => setSelectedFramework(e.target.value)}
                label="Framework"
              >
                {sortedFrameworks.map((f) => (
                  <MenuItem key={f} value={f}>
                    <Box sx={{ display: 'flex', justifyContent: 'space-between', width: '100%', gap: 2 }}>
                      <span>{f}</span>
                      <Typography component="span" variant="caption" color="text.secondary">
                        {cov.by_framework[f] ?? 0}
                      </Typography>
                    </Box>
                  </MenuItem>
                ))}
              </Select>
            </FormControl>
          )
        }
      />

      <Tabs
        value={activeTab}
        onChange={(_, v) => setActiveTab(v)}
        sx={{ mb: 2.5, borderBottom: '1px solid', borderColor: 'divider', minHeight: 36, '& .MuiTab-root': { minHeight: 36, py: 0.75, fontSize: '0.8rem' } }}
      >
        <Tab label="Mapping Matrix" />
        <Tab label="Inferred Coverage" />
      </Tabs>

      {activeTab === 1 && <InferredCoverage />}

      {activeTab === 0 && <>

      {/* Cloud sub-framework toggle */}
      {product === 'cloud' && (
        <Box sx={{ display: 'flex', gap: 1, mb: 2 }}>
          {([
            { value: 'ISO27017' as const, label: 'ISO 27017', desc: 'Cloud Security' },
            { value: 'ISO27018' as const, label: 'ISO 27018', desc: 'PII in Cloud' },
          ]).map(({ value, label, desc }) => (
            <Box
              key={value}
              onClick={() => { setCloudSub(value); setSelectedFramework(''); setPage(0) }}
              sx={{
                px: 1.5, py: 0.75, borderRadius: 1, cursor: 'pointer',
                bgcolor: cloudSub === value
                  ? (isLight ? 'rgba(230,160,0,0.18)' : 'rgba(255,192,0,0.15)')
                  : (isLight ? 'rgba(0,0,0,0.04)' : 'rgba(255,255,255,0.04)'),
                border: `1px solid ${cloudSub === value ? (isLight ? 'rgba(180,110,0,0.4)' : '#FFC00050') : (isLight ? 'rgba(0,0,0,0.12)' : 'rgba(255,255,255,0.08)')}`,
                '&:hover': { bgcolor: isLight ? 'rgba(230,160,0,0.14)' : 'rgba(255,192,0,0.1)' },
              }}
            >
              <Typography variant="caption" fontWeight={cloudSub === value ? 700 : 400}
                color={cloudSub === value ? (isLight ? '#7a4800' : '#FFC000') : 'text.secondary'}>
                {label}
              </Typography>
              <Typography variant="caption" sx={{ ml: 1, opacity: 0.6 }}
                color={cloudSub === value ? (isLight ? '#7a4800' : '#FFC000') : 'text.disabled'}>
                {desc}
              </Typography>
            </Box>
          ))}
        </Box>
      )}

      {/* Summary cards */}
      {cov && (
        <Grid container spacing={2} sx={{ mb: 2 }}>
          <Grid item xs={6} sm={3}>
            <Card>
              <CardContent sx={{ pb: '12px !important' }}>
                <Typography variant="caption" color="text.secondary">Frameworks</Typography>
                <Typography variant="h4">{cov.frameworks.length}</Typography>
              </CardContent>
            </Card>
          </Grid>
          <Grid item xs={6} sm={3}>
            <Card>
              <CardContent sx={{ pb: '12px !important' }}>
                <Typography variant="caption" color="text.secondary">Total Mappings</Typography>
                <Typography variant="h4">{cov.total_mappings.toLocaleString()}</Typography>
              </CardContent>
            </Card>
          </Grid>
          <Grid item xs={6} sm={3}>
            <Card>
              <CardContent sx={{ pb: '12px !important' }}>
                <Typography variant="caption" color="text.secondary" noWrap>{activeFramework}</Typography>
                <Typography variant="h4">{frameworkCount}</Typography>
              </CardContent>
            </Card>
          </Grid>
          <Grid item xs={6} sm={3}>
            <Card>
              <CardContent sx={{ pb: '12px !important' }}>
                <Typography variant="caption" color="text.secondary">
                  {showUnmapped ? 'Unmapped Controls' : 'Controls Shown'}
                </Typography>
                <Typography variant="h4" color={showUnmapped ? 'error.light' : 'inherit'}>
                  {filteredRows.length}
                </Typography>
              </CardContent>
            </Card>
          </Grid>
        </Grid>
      )}

      {/* Unmapped toggle */}
      {cov && (
        <Box sx={{ mb: 1, display: 'flex', justifyContent: 'flex-end' }}>
          <FormControlLabel
            control={
              <Switch
                checked={showUnmapped}
                onChange={(e) => { setShowUnmapped(e.target.checked); setPage(0) }}
                size="small"
                sx={{ '& .MuiSwitch-thumb': { bgcolor: showUnmapped ? (isLight ? '#9e0000' : '#FFC7CE') : undefined } }}
              />
            }
            label={
              <Typography variant="caption" color={showUnmapped ? 'error.light' : 'text.secondary'}>
                Show unmapped only
              </Typography>
            }
          />
        </Box>
      )}

      {/* Framework selector pills */}
      {cov && (
        <Card sx={{ mb: 2 }}>
          <CardContent sx={{ pb: '12px !important' }}>
            <Typography variant="subtitle2" sx={{ mb: 1 }}>All Frameworks</Typography>
            <Box sx={{ display: 'flex', gap: 0.75, flexWrap: 'wrap' }}>
              {sortedFrameworks.map((f) => {
                const count = cov.by_framework[f] ?? 0
                const isActive = f === activeFramework
                const isExt = ISO_EXTENSIONS.has(f)
                return (
                  <Tooltip key={f} title={isExt ? 'ISO 27000-family extension standard' : ''} placement="top">
                    <Box
                      onClick={() => setSelectedFramework(f)}
                      sx={{
                        px: 1.25,
                        py: 0.4,
                        borderRadius: 1,
                        cursor: 'pointer',
                        bgcolor: isActive
                          ? (isExt ? (isLight ? 'rgba(230,160,0,0.22)' : 'rgba(255,192,0,0.2)') : 'rgba(68,114,196,0.2)')
                          : (isExt ? (isLight ? 'rgba(230,160,0,0.12)' : 'rgba(255,192,0,0.07)') : 'rgba(68,114,196,0.06)'),
                        border: `1px solid ${isActive ? (isExt ? (isLight ? 'rgba(230,160,0,0.5)' : '#FFC00050') : '#4472C450') : 'transparent'}`,
                        '&:hover': { bgcolor: isExt ? (isLight ? 'rgba(230,160,0,0.2)' : 'rgba(255,192,0,0.14)') : 'rgba(68,114,196,0.15)' },
                      }}
                    >
                      <Typography
                        variant="caption"
                        fontWeight={isActive ? 700 : 400}
                        color={isActive ? (isExt ? (isLight ? '#7a4800' : '#FFC000') : 'primary.light') : (isExt ? (isLight ? '#9a6500' : '#FFC00099') : 'text.secondary')}
                      >
                        {f}
                      </Typography>
                      <Typography
                        variant="caption"
                        sx={{ ml: 0.75, opacity: 0.6, color: isActive ? (isExt ? (isLight ? '#7a4800' : '#FFC000') : 'primary.light') : 'text.secondary' }}
                      >
                        {count}
                      </Typography>
                    </Box>
                  </Tooltip>
                )
              })}
            </Box>
          </CardContent>
        </Card>
      )}

      {error && <Alert severity="error" sx={{ mb: 2 }}>Failed to load coverage data.</Alert>}

      <TableContainer component={Card}>
        <Table size="small">
          <TableHead>
            <TableRow>
              <TableCell sx={{ width: 120 }}>
                {product === 'cloud' ? SOURCE_CONTROL_LABEL[sourceFramework] : (SOURCE_CONTROL_LABEL[product] ?? 'ISO Control')}
              </TableCell>
              <TableCell sx={{ width: 140 }}>Control Group</TableCell>
              <TableCell>{activeFramework || 'Framework'} Mappings</TableCell>
              <TableCell align="center" sx={{ width: 60 }}>Count</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {isLoading &&
              [...Array(8)].map((_, i) => (
                <TableRow key={i}>
                  {[...Array(4)].map((_, j) => (
                    <TableCell key={j}>
                      <Skeleton variant="text" />
                    </TableCell>
                  ))}
                </TableRow>
              ))}

            {pagedRows.map((row) => {
              const fwMappings = activeFramework
                ? row.mappings.filter((m) => m.framework === activeFramework)
                : row.mappings
              const CONFIDENCE_COLOR = isLight ? CONFIDENCE_COLOR_LIGHT : CONFIDENCE_COLOR_DARK
              return (
                <TableRow key={row.iso_control_id} hover>
                  <TableCell
                    sx={product !== 'isms' ? { cursor: 'pointer' } : undefined}
                    onClick={product !== 'isms' ? () => navigate(`/framework-controls/${sourceFramework}/${row.iso_control_id}`) : undefined}
                  >
                    <Typography
                      variant="body2"
                      fontWeight={600}
                      color="primary.light"
                      sx={{ fontFamily: 'monospace', fontSize: '0.75rem' }}
                    >
                      {row.iso_control_id}
                    </Typography>
                    <Typography variant="caption" color="text.secondary" sx={{ display: 'block', lineHeight: 1.3 }}>
                      {row.iso_control_title}
                    </Typography>
                  </TableCell>
                  <TableCell>
                    <Typography variant="caption" color="text.secondary" sx={{ fontFamily: 'monospace' }}>
                      {row.control_group_code}
                    </Typography>
                  </TableCell>
                  <TableCell>
                    <Box sx={{ display: 'flex', gap: 0.5, flexWrap: 'wrap' }}>
                      {fwMappings.slice(0, 6).map((m, idx) => {
                        const cc = CONFIDENCE_COLOR(m.confidence)
                        return (
                          <Chip
                            key={idx}
                            label={m.control_id}
                            size="small"
                            title={`${m.control_title} · ${Math.round(m.confidence * 100)}% confidence · ${m.mapping_type}`}
                            sx={{ fontSize: '0.68rem', height: 18, bgcolor: cc.bg, color: cc.color, cursor: 'default' }}
                          />
                        )
                      })}
                      {fwMappings.length > 6 && (
                        <Typography variant="caption" color="text.secondary" sx={{ alignSelf: 'center' }}>
                          +{fwMappings.length - 6} more
                        </Typography>
                      )}
                      {fwMappings.length === 0 && (
                        <Typography variant="caption" color="text.secondary">—</Typography>
                      )}
                    </Box>
                  </TableCell>
                  <TableCell align="center">
                    <Box sx={{ width: 10, height: 10, borderRadius: '50%', mx: 'auto', bgcolor: fwMappings.length > 0 ? (isLight ? '#2e7d32' : '#C6EFCE') : (isLight ? '#c62828' : '#FFC7CE') }} />
                  </TableCell>
                </TableRow>
              )
            })}

            {!isLoading && filteredRows.length === 0 && (
              <TableRow>
                <TableCell colSpan={4} align="center">
                  <Typography variant="body2" color="text.secondary" sx={{ py: 3 }}>
                    No mappings found{activeFramework ? ` for ${activeFramework}` : ''}.
                  </Typography>
                </TableCell>
              </TableRow>
            )}
          </TableBody>
        </Table>
        {filteredRows.length > ROWS_PER_PAGE && (
          <TablePagination
            component="div"
            count={filteredRows.length}
            page={page}
            onPageChange={(_, p) => setPage(p)}
            rowsPerPage={ROWS_PER_PAGE}
            rowsPerPageOptions={[ROWS_PER_PAGE]}
            sx={{ borderTop: '1px solid', borderColor: 'divider' }}
          />
        )}
      </TableContainer>

      {/* ── Content Coverage Gaps ─────────────────────────────────── */}
      <Box sx={{ mt: 4 }}>
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 2, mb: 1.5 }}>
          <Typography variant="h6" fontWeight={700}>
            Content Coverage Gaps
          </Typography>
          {product === 'isms' && (
            <>
              <Chip
                label={`${gaps.length} control${gaps.length !== 1 ? 's' : ''} affected`}
                size="small"
                sx={{
                  bgcolor: gaps.length === 0
                    ? (isLight ? 'rgba(46,125,50,0.15)' : 'rgba(198,239,206,0.15)')
                    : (isLight ? 'rgba(192,0,0,0.12)' : 'rgba(255,199,206,0.15)'),
                  color: gaps.length === 0
                    ? (isLight ? '#1b5e20' : '#C6EFCE')
                    : (isLight ? '#9e0000' : '#FFC7CE'),
                }}
              />
              <Box sx={{ ml: 'auto', display: 'flex', gap: 0.75 }}>
                {([
                  { value: 'framework' as const,   label: 'FW',  color: PRODUCT_COLORS.isms },
                  { value: 'operational' as const,  label: 'OP',  color: '#70AD47' },
                ]).map(({ value, label, color }) => (
                  <Chip
                    key={value}
                    label={label}
                    size="small"
                    onClick={() => setGapProduct(value)}
                    sx={{
                      cursor: 'pointer', fontSize: '0.72rem',
                      bgcolor: gapProduct === value ? `${color}30` : 'rgba(255,255,255,0.05)',
                      color: gapProduct === value ? color : 'text.secondary',
                      border: gapProduct === value ? `1px solid ${color}50` : '1px solid transparent',
                    }}
                  />
                ))}
              </Box>
            </>
          )}
        </Box>

        {(product === 'privacy' || product === 'cloud' || product === 'ai') && (
          <Box sx={{ display: 'flex', alignItems: 'center', gap: 1.5, py: 3, pl: 1 }}>
            {product === 'privacy'
              ? <LockPersonOutlined sx={{ color: `${PRODUCT_COLORS.privacy}50`, fontSize: 20 }} />
              : product === 'ai'
                ? <PsychologyOutlined sx={{ color: `${PRODUCT_COLORS.ai}50`, fontSize: 20 }} />
                : <CloudOutlined sx={{ color: `${PRODUCT_COLORS.cloud}50`, fontSize: 20 }} />
            }
            <Typography variant="body2" color="text.disabled">
              Content coverage gaps for {PRODUCT_SUBTITLES[product]} will appear here once control groups are imported.
            </Typography>
          </Box>
        )}

        {product === 'isms' && gaps.length === 0 && (
          <Alert severity="success" sx={{ fontSize: '0.85rem' }}>
            All controls have complete {gapProduct === 'framework' ? 'FW' : 'OP'} coverage — no artefacts missing.
          </Alert>
        )}
        {product === 'isms' && gaps.length > 0 && (
          <TableContainer component={Card} variant="outlined">
            <Table size="small">
              <TableHead>
                <TableRow>
                  <TableCell sx={{ fontWeight: 700, width: 90 }}>Code</TableCell>
                  <TableCell sx={{ fontWeight: 700 }}>Control Group</TableCell>
                  <TableCell sx={{ fontWeight: 700 }}>Section</TableCell>
                  <TableCell sx={{ fontWeight: 700 }}>Missing Artefacts</TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {gaps.map((gap) => (
                  <TableRow
                    key={gap.id}
                    hover
                    sx={{ cursor: 'pointer' }}
                    onClick={() => navigate(`/controls/${gap.id}`)}
                  >
                    <TableCell>
                      <Typography variant="caption" sx={{ fontFamily: 'monospace', color: 'primary.light' }}>
                        {gap.group_code}
                      </Typography>
                    </TableCell>
                    <TableCell>
                      <Typography variant="body2" fontWeight={600}>{gap.name}</Typography>
                    </TableCell>
                    <TableCell>
                      <Typography variant="caption" color="text.secondary">{gap.section_name}</Typography>
                    </TableCell>
                    <TableCell>
                      <Box sx={{ display: 'flex', gap: 0.5, flexWrap: 'wrap' }}>
                        {gap.missing.map((m) => {
                          const MISSING_CHIP = isLight ? MISSING_CHIP_LIGHT : MISSING_CHIP_DARK
                          return (
                            <Chip
                              key={m}
                              label={m}
                              size="small"
                              sx={{
                                fontSize: '0.65rem', height: 18,
                                bgcolor: MISSING_CHIP[m]?.bg ?? (isLight ? 'rgba(192,0,0,0.12)' : 'rgba(255,199,206,0.15)'),
                                color: MISSING_CHIP[m]?.color ?? (isLight ? '#9e0000' : '#FFC7CE'),
                              }}
                            />
                          )
                        })}
                      </Box>
                    </TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </TableContainer>
        )}
      </Box>

      {/* ── Custom Framework Coverage ─────────────────────────────── */}
      {customFrameworks && customFrameworks.length > 0 && (
        <Box sx={{ mt: 4 }}>
          <Typography variant="caption" sx={{ fontWeight: 700, fontSize: '0.68rem', color: 'text.secondary', textTransform: 'uppercase', letterSpacing: '0.08em', display: 'block', mb: 1.5 }}>
            Custom Frameworks
          </Typography>
          {customFrameworks.map(fw => (
            <CustomFrameworkCoverage
              key={fw.id}
              frameworkId={fw.id}
              frameworkName={fw.name}
              shortCode={fw.short_code}
              projectId=""
            />
          ))}
        </Box>
      )}

      </>}
    </Box>
  )
}
