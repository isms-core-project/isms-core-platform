/**
 * Crosswalk Tracker
 * Admin overview of all cross-framework mapping axes — counts, sprint dates,
 * and pending update flags. Mirrors the FrameworkTracker pattern.
 */
import { useMemo } from 'react'
import {
  Box,
  Card,
  CardContent,
  Chip,
  Skeleton,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Tooltip,
  Typography,
} from '@mui/material'
import {
  CheckCircleOutlined,
  WarningAmberOutlined,
  UpdateOutlined,
  InfoOutlined,
  AccountTreeOutlined,
} from '@mui/icons-material'
import { useQuery } from '@tanstack/react-query'
import { client } from '../api/client'
import PageHeader from '../components/PageHeader'

interface AxisRow {
  source_framework: string
  target_framework: string
  count: number
}

interface AxesResponse {
  axes: AxisRow[]
  total_mappings: number
  total_axes: number
}

// Pending / available reviews — update this when a source framework has a new version
// or when a new axis should be added. Same pattern as FrameworkTracker KNOWN_UPDATES.
const KNOWN_REVIEWS: Record<string, { status: 'pending' | 'review'; note: string; eta?: string }> = {
  'NIST_800_53_R5 → MITRE_ATTACK_V18': {
    status: 'pending',
    note: 'MITRE ATT&CK v19 scheduled 2026-04-28 — update STIX bundle and remap ATT&CK axis after release.',
    eta: '2026-04-28',
  },
  'ISO27001_2022 → ISO27017': {
    status: 'pending',
    note: 'ISO 27017:2025 revision in progress — re-validate cloud control mappings on official release.',
  },
  'ISO27017 → ISO27001_2022': {
    status: 'pending',
    note: 'ISO 27017:2025 revision in progress — re-validate reverse cloud mappings on official release.',
  },
  'ISO27017 → CSA_CCM_V4_1': {
    status: 'pending',
    note: 'ISO 27017:2025 revision in progress — review CCM cloud mappings after new ISO release.',
  },
  'ISO27017 → NIST_CSF_2.0': {
    status: 'pending',
    note: 'ISO 27017:2025 revision in progress — review NIST CSF cloud mappings after new ISO release.',
  },
}

// Sprint history — content_hash → human date shown in Last Sprint column
const SPRINT_DATES: Record<string, string> = {
  crosswalk_v3:         '2026-04-17',
  crosswalk_v2:         '2026-04-17',
  iso42001_crosswalk_v4:'2026-04-17',
  iso42001_crosswalk_v2:'2026-04-17',
  iso42005_crosswalk_v3:'2026-04-17',
}

// Source framework → file that holds its axes
const SOURCE_FILE: Record<string, string> = {
  ISO42001:        'iso42001_crosswalk.json',
  ISO42005:        'iso42005_crosswalk.json',
  ISO27001_2022:   'crosswalk.json',
  ISO27017:        'crosswalk.json',
  ISO27018:        'crosswalk.json',
  ISO27701:        'crosswalk.json',
  NIST_800_53_R5:  'crosswalk.json',
  NIST_AI_RMF:     'crosswalk.json',
}

// Source framework display labels
const FW_LABEL: Record<string, string> = {
  ISO27001_2022:  'ISO 27001:2022',
  ISO27017:       'ISO 27017',
  ISO27018:       'ISO 27018',
  ISO27701:       'ISO 27701',
  ISO42001:       'ISO 42001:2023',
  ISO42005:       'ISO 42005:2025',
  NIST_800_53_R5: 'NIST SP 800-53 R5',
  NIST_AI_RMF:    'NIST AI RMF',
}

// Source framework → accent colour
const FW_COLOR: Record<string, string> = {
  ISO27001_2022:  '#1565C0',
  ISO27017:       '#0277BD',
  ISO27018:       '#00838F',
  ISO27701:       '#6A1B9A',
  ISO42001:       '#E65100',
  ISO42005:       '#BF360C',
  NIST_800_53_R5: '#2E7D32',
  NIST_AI_RMF:    '#1B5E20',
}

function fwColor(code: string) {
  return FW_COLOR[code] ?? '#455A64'
}

function SummaryCard({ label, value, sub, color }: { label: string; value: string | number; sub?: string; color?: string }) {
  return (
    <Card sx={{ flex: 1, minWidth: 140 }}>
      <CardContent sx={{ pb: '12px !important' }}>
        <Typography variant="caption" color="text.secondary" sx={{ fontSize: '0.68rem', textTransform: 'uppercase', letterSpacing: '0.06em' }}>
          {label}
        </Typography>
        <Typography variant="h5" sx={{ fontWeight: 700, color: color ?? 'text.primary', lineHeight: 1.2, mt: 0.5 }}>
          {value}
        </Typography>
        {sub && <Typography variant="caption" color="text.secondary" sx={{ fontSize: '0.65rem' }}>{sub}</Typography>}
      </CardContent>
    </Card>
  )
}

export default function CrosswalkTracker() {
  const { data, isLoading } = useQuery<AxesResponse>({
    queryKey: ['crosswalk-axes'],
    queryFn: () => client.get('/frameworks/crosswalk/axes').then(r => r.data),
  })

  const { grouped, reviewCount, pendingCount } = useMemo(() => {
    if (!data) return { grouped: {} as Record<string, AxisRow[]>, reviewCount: 0, pendingCount: 0 }
    const g: Record<string, AxisRow[]> = {}
    let reviewCount = 0
    let pendingCount = 0
    for (const axis of data.axes) {
      const src = axis.source_framework
      if (!g[src]) g[src] = []
      g[src].push(axis)
      const key = `${axis.source_framework} → ${axis.target_framework}`
      const r = KNOWN_REVIEWS[key]
      if (r?.status === 'review')  reviewCount++
      if (r?.status === 'pending') pendingCount++
    }
    return { grouped: g, reviewCount, pendingCount }
  }, [data])

  const sourceOrder = ['ISO27001_2022', 'ISO27017', 'ISO27018', 'ISO27701', 'ISO42001', 'ISO42005', 'NIST_800_53_R5', 'NIST_AI_RMF']

  return (
    <Box sx={{ p: 3, maxWidth: 1200 }}>
      <PageHeader
        title="Crosswalk Tracker"
        subtitle="Cross-framework mapping axes — coverage, sprint history, and pending update flags"
      />

      {/* Summary row */}
      <Box sx={{ display: 'flex', gap: 2, mb: 3, flexWrap: 'wrap' }}>
        {isLoading ? (
          [1,2,3,4].map(i => <Skeleton key={i} variant="rectangular" width={140} height={80} sx={{ borderRadius: 1 }} />)
        ) : (
          <>
            <SummaryCard label="Total axes" value={data?.total_axes ?? 0} sub="source → target pairs" />
            <SummaryCard label="Total mappings" value={(data?.total_mappings ?? 0).toLocaleString()} sub="across all 3 crosswalk files" />
            <SummaryCard
              label="Review flagged"
              value={reviewCount}
              sub="axes needing manual review"
              color={reviewCount > 0 ? '#FF9800' : '#4CAF50'}
            />
            <SummaryCard
              label="Pending releases"
              value={pendingCount}
              sub="axes pending source update"
              color={pendingCount > 0 ? '#42A5F5' : '#9E9E9E'}
            />
          </>
        )}
      </Box>

      {isLoading && <Skeleton variant="rectangular" height={200} sx={{ borderRadius: 1 }} />}

      {!isLoading && data && sourceOrder
        .filter(src => grouped[src]?.length > 0)
        .map(src => {
          const axes = grouped[src]
          const srcTotal = axes.reduce((s, a) => s + a.count, 0)
          const color = fwColor(src)
          return (
            <Box key={src} sx={{ mb: 3 }}>
              <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 1 }}>
                <Box sx={{ width: 4, height: 20, borderRadius: 1, bgcolor: color }} />
                <Typography variant="body2" sx={{ fontWeight: 700, fontSize: '0.8rem', color }}>
                  {FW_LABEL[src] ?? src}
                </Typography>
                <Typography variant="caption" color="text.secondary">
                  ({axes.length} ax{axes.length !== 1 ? 'es' : 'is'} · {srcTotal.toLocaleString()} mappings)
                </Typography>
                <Chip
                  label={SOURCE_FILE[src] ?? 'crosswalk.json'}
                  size="small"
                  sx={{ height: 16, fontSize: '0.58rem', fontFamily: 'monospace', bgcolor: 'action.hover', ml: 0.5 }}
                />
              </Box>

              <TableContainer sx={{ border: '1px solid', borderColor: 'divider', borderRadius: 1 }}>
                <Table size="small">
                  <TableHead>
                    <TableRow sx={{ bgcolor: 'background.paper' }}>
                      <TableCell sx={{ fontSize: '0.68rem', fontWeight: 700, color: 'text.secondary', textTransform: 'uppercase' }}>Axis</TableCell>
                      <TableCell sx={{ fontSize: '0.68rem', fontWeight: 700, color: 'text.secondary', textTransform: 'uppercase' }} align="right">Mappings</TableCell>
                      <TableCell sx={{ fontSize: '0.68rem', fontWeight: 700, color: 'text.secondary', textTransform: 'uppercase' }}>Last Sprint</TableCell>
                      <TableCell sx={{ fontSize: '0.68rem', fontWeight: 700, color: 'text.secondary', textTransform: 'uppercase' }}>Status</TableCell>
                    </TableRow>
                  </TableHead>
                  <TableBody>
                    {axes.map(axis => {
                      const key = `${axis.source_framework} → ${axis.target_framework}`
                      const rev = KNOWN_REVIEWS[key]
                      return (
                        <TableRow key={key} hover sx={{ '&:last-child td': { border: 0 } }}>
                          <TableCell>
                            <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.75 }}>
                              <AccountTreeOutlined sx={{ fontSize: 12, color: 'text.disabled' }} />
                              <Typography variant="body2" sx={{ fontWeight: 600, fontSize: '0.78rem' }}>
                                {axis.source_framework}
                              </Typography>
                              <Typography variant="caption" color="text.disabled" sx={{ fontSize: '0.7rem' }}>→</Typography>
                              <Typography variant="body2" sx={{ fontSize: '0.78rem' }}>
                                {axis.target_framework}
                              </Typography>
                            </Box>
                          </TableCell>
                          <TableCell align="right">
                            <Typography variant="body2" sx={{ fontSize: '0.75rem', fontWeight: 600 }}>
                              {axis.count.toLocaleString()}
                            </Typography>
                          </TableCell>
                          <TableCell>
                            <Typography variant="caption" color="text.secondary" sx={{ fontSize: '0.7rem', fontFamily: 'monospace' }}>
                              2026-04-17
                            </Typography>
                          </TableCell>
                          <TableCell>
                            {!rev && (
                              <Chip
                                icon={<CheckCircleOutlined sx={{ fontSize: 13 }} />}
                                label="Current"
                                size="small"
                                sx={{ height: 18, fontSize: '0.6rem', bgcolor: 'rgba(76,175,80,0.1)', color: '#4CAF50', '& .MuiChip-icon': { color: '#4CAF50' } }}
                              />
                            )}
                            {rev?.status === 'review' && (
                              <Tooltip title={rev.note}>
                                <Chip
                                  icon={<WarningAmberOutlined sx={{ fontSize: 13 }} />}
                                  label="Review due"
                                  size="small"
                                  sx={{ height: 18, fontSize: '0.6rem', bgcolor: 'rgba(255,152,0,0.1)', color: '#FF9800', '& .MuiChip-icon': { color: '#FF9800' } }}
                                />
                              </Tooltip>
                            )}
                            {rev?.status === 'pending' && (
                              <Tooltip title={`${rev.note}${rev.eta ? ` ETA: ${rev.eta}` : ''}`}>
                                <Chip
                                  icon={<UpdateOutlined sx={{ fontSize: 13 }} />}
                                  label={rev.eta ? `Pending (${rev.eta})` : 'Pending release'}
                                  size="small"
                                  sx={{ height: 18, fontSize: '0.6rem', bgcolor: 'rgba(66,165,245,0.1)', color: '#42A5F5', '& .MuiChip-icon': { color: '#42A5F5' } }}
                                />
                              </Tooltip>
                            )}
                          </TableCell>
                        </TableRow>
                      )
                    })}
                  </TableBody>
                </Table>
              </TableContainer>
            </Box>
          )
        })
      }

      <Typography variant="caption" color="text.disabled" sx={{ fontSize: '0.62rem', display: 'block', mt: 2 }}>
        <InfoOutlined sx={{ fontSize: 12, verticalAlign: 'middle', mr: 0.5 }} />
        Axis counts are live from the database. Review flags are tracked in{' '}
        <code>CrosswalkTracker.tsx</code> → <code>KNOWN_REVIEWS</code>.
        Sprint dates update manually after each mapping sprint.
        Files: <code>crosswalk.json</code> · <code>iso42001_crosswalk.json</code> · <code>iso42005_crosswalk.json</code>.
      </Typography>
    </Box>
  )
}
