import { useState, useMemo } from 'react'
import { useProduct, PRODUCT_SUBTITLES, PRODUCT_COLORS } from '../store/ProductContext'
import { LockPersonOutlined, CloudOutlined } from '@mui/icons-material'
import {
  Box,
  Card,
  CardContent,
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
}

// Human-readable label for the source control column
const SOURCE_CONTROL_LABEL: Record<string, string> = {
  isms:     'ISO 27001 Control',
  privacy:  'ISO 27701 Control',
  cloud:    'ISO 27017 Control',
  ISO27017: 'ISO 27017 Control',
  ISO27018: 'ISO 27018 Control',
}

// ISO 27000-family extension standards — shown with amber accent in framework pills
const ISO_EXTENSIONS = new Set(['ISO27017', 'ISO27018', 'ISO27701'])

const CONFIDENCE_COLOR = (c: number) =>
  c >= 0.8 ? { bg: 'rgba(198,239,206,0.15)', color: '#C6EFCE' }
  : c >= 0.6 ? { bg: 'rgba(255,235,156,0.12)', color: '#FFEB9C' }
  : { bg: 'rgba(255,199,206,0.12)', color: '#FFC7CE' }

const MISSING_CHIP: Record<string, { bg: string; color: string }> = {
  policy:      { bg: 'rgba(192,0,0,0.15)',    color: '#FFC7CE' },
  UG:          { bg: 'rgba(255,192,0,0.12)',   color: '#FFEB9C' },
  TG:          { bg: 'rgba(255,192,0,0.12)',   color: '#FFEB9C' },
  assessment:  { bg: 'rgba(192,0,0,0.15)',    color: '#FFC7CE' },
}

export default function Coverage() {
  const { product, ismsTier } = useProduct()
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

  const cov = data as unknown as RealCoverage | undefined

  const activeFramework = selectedFramework || (cov?.frameworks[0] ?? '')

  const sortedFrameworks = useMemo(() => {
    if (!cov?.frameworks || !cov?.by_framework) return cov?.frameworks ?? []
    return [...cov.frameworks].sort(
      (a, b) => (cov.by_framework[b] ?? 0) - (cov.by_framework[a] ?? 0)
    )
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
        title="Framework Coverage Matrix"
        subtitle={`${PRODUCT_SUBTITLES[product]} mapped to ${cov?.frameworks.length ?? '...'} frameworks · ${(cov?.total_mappings ?? 0).toLocaleString()} total mappings`}
        actions={
          cov && (
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
                bgcolor: cloudSub === value ? 'rgba(255,192,0,0.15)' : 'rgba(255,255,255,0.04)',
                border: `1px solid ${cloudSub === value ? '#FFC00050' : 'rgba(255,255,255,0.08)'}`,
                '&:hover': { bgcolor: 'rgba(255,192,0,0.1)' },
              }}
            >
              <Typography variant="caption" fontWeight={cloudSub === value ? 700 : 400}
                color={cloudSub === value ? '#FFC000' : 'text.secondary'}>
                {label}
              </Typography>
              <Typography variant="caption" sx={{ ml: 1, opacity: 0.6 }}
                color={cloudSub === value ? '#FFC000' : 'text.disabled'}>
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
                sx={{ '& .MuiSwitch-thumb': { bgcolor: showUnmapped ? '#FFC7CE' : undefined } }}
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
                          ? (isExt ? 'rgba(255,192,0,0.2)' : 'rgba(68,114,196,0.2)')
                          : (isExt ? 'rgba(255,192,0,0.07)' : 'rgba(68,114,196,0.06)'),
                        border: `1px solid ${isActive ? (isExt ? '#FFC00050' : '#4472C450') : 'transparent'}`,
                        '&:hover': { bgcolor: isExt ? 'rgba(255,192,0,0.14)' : 'rgba(68,114,196,0.15)' },
                      }}
                    >
                      <Typography
                        variant="caption"
                        fontWeight={isActive ? 700 : 400}
                        color={isActive ? (isExt ? '#FFC000' : 'primary.light') : (isExt ? '#FFC00099' : 'text.secondary')}
                      >
                        {f}
                      </Typography>
                      <Typography
                        variant="caption"
                        sx={{ ml: 0.75, opacity: 0.6, color: isActive ? (isExt ? '#FFC000' : 'primary.light') : 'text.secondary' }}
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
                    <Box sx={{ width: 10, height: 10, borderRadius: '50%', mx: 'auto', bgcolor: fwMappings.length > 0 ? '#C6EFCE' : '#FFC7CE' }} />
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
                sx={{ bgcolor: gaps.length === 0 ? 'rgba(198,239,206,0.15)' : 'rgba(255,199,206,0.15)', color: gaps.length === 0 ? '#C6EFCE' : '#FFC7CE' }}
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

        {(product === 'privacy' || product === 'cloud') && (
          <Box sx={{ display: 'flex', alignItems: 'center', gap: 1.5, py: 3, pl: 1 }}>
            {product === 'privacy'
              ? <LockPersonOutlined sx={{ color: `${PRODUCT_COLORS.privacy}50`, fontSize: 20 }} />
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
                        {gap.missing.map((m) => (
                          <Chip
                            key={m}
                            label={m}
                            size="small"
                            sx={{
                              fontSize: '0.65rem', height: 18,
                              bgcolor: MISSING_CHIP[m]?.bg ?? 'rgba(255,199,206,0.15)',
                              color: MISSING_CHIP[m]?.color ?? '#FFC7CE',
                            }}
                          />
                        ))}
                      </Box>
                    </TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </TableContainer>
        )}
      </Box>
    </Box>
  )
}
