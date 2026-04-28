/**
 * Framework Version Tracker
 * Shows all loaded compliance framework datasets, their current version,
 * known update availability, and dataset health metrics.
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
  InfoOutlined,
  UpdateOutlined,
  OpenInNewOutlined,
} from '@mui/icons-material'
import { useQuery } from '@tanstack/react-query'
import { client } from '../api/client'
import PageHeader from '../components/PageHeader'

interface FrameworkRow {
  id: string
  code: string
  name: string
  version: string | null
  publisher: string | null
  source_url: string | null
  jurisdiction: string | null
  controls_count: number
  loaded_at: string
}

// Known update availability — update this when new versions release.
// pending: version not yet released; available: released, platform not yet updated.
const KNOWN_UPDATES: Record<string, { latest: string; status: 'pending' | 'available'; note: string; eta?: string }> = {
  MITRE_ATTACK_V19: {
    latest: 'v19',
    status: 'available',
    note: 'MITRE ATT&CK v19 released 2026-04-28. TA0005 Defense Evasion → Stealth; new tactic TA0112 Defense Impairment. Dataset + crosswalk updated.',
  },
}

// ISO Reference Corpus & Glossary Standards — static registry
interface CorpusStandardRow {
  standard: string
  title: string
  domain: string
  edition: string
  status: 'current' | 'pending'
  note?: string
  eta?: string
}

const CORPUS_STANDARDS: CorpusStandardRow[] = [
  // Pending
  { standard: 'ISO/IEC 27000',      title: 'Information security management — Overview and vocabulary', domain: 'ISMS',             edition: 'FDIS (replacing 2018)', status: 'pending', note: 'FDIS ballot in progress — replaces ISO/IEC 27000:2018 with updated terminology aligned to ISO 27001:2022.', eta: '~June 2026' },
  // Cloud
  { standard: 'ISO/IEC 22123-1:2023', title: 'Cloud computing — Vocabulary', domain: 'Cloud Computing',  edition: '2023', status: 'current' },
  { standard: 'ISO/IEC 22123-2:2023', title: 'Cloud computing — Concepts',   domain: 'Cloud Computing',  edition: '2023', status: 'current' },
  { standard: 'ISO/IEC 22123-3:2023', title: 'Cloud computing — Reference Architecture (CCRA)', domain: 'Cloud Computing', edition: '2023', status: 'current' },
  // AI
  { standard: 'ISO/IEC 42001:2023',  title: 'AI management system (AIMS)',    domain: 'AI Management',    edition: '2023', status: 'current' },
  { standard: 'ISO/IEC 42005:2025',  title: 'AI system impact assessment',    domain: 'AI Management',    edition: '2025', status: 'current' },
  { standard: 'ISO/IEC 22989:2022',  title: 'AI concepts and terminology',    domain: 'AI Management',    edition: '2022', status: 'current' },
  // Infrastructure & IoT
  { standard: 'ISO/IEC 19395:2015',  title: 'Smart data centre resource monitoring', domain: 'Infrastructure', edition: '2015', status: 'current' },
  { standard: 'ISO/IEC 30141:2024',  title: 'IoT reference architecture',     domain: 'IoT',              edition: '2024', status: 'current' },
  { standard: 'ISO/IEC 24091:2019',  title: 'Data centre storage power efficiency', domain: 'Infrastructure', edition: '2019', status: 'current' },
]

const DOMAIN_COLOR: Record<string, string> = {
  'ISMS':             '#455A64',
  'Cloud Computing':  '#0288d1',
  'AI Management':    '#ff6b35',
  'Infrastructure':   '#00897b',
  'IoT':              '#6d4c41',
}

// Jurisdiction → display label
const JURISDICTION_LABEL: Record<string, string> = {
  INT: 'International',
  EU:  'European Union',
  US:  'United States',
  DE:  'Germany',
  CH:  'Switzerland',
  GB:  'United Kingdom',
  BE:  'Belgium',
  LU:  'Luxembourg',
  IT:  'Italy',
  FR:  'France',
  AT:  'Austria',
}

// Jurisdiction → accent colour
const JURISDICTION_COLOR: Record<string, string> = {
  INT: '#455A64',
  EU:  '#1565C0',
  US:  '#B71C1C',
  DE:  '#4E342E',
  CH:  '#C62828',
  GB:  '#1A237E',
  BE:  '#1B5E20',
  LU:  '#4A148C',
  IT:  '#006630',
  FR:  '#0D47A1',
  AT:  '#E65100',
}

function jurisColor(j: string | null) {
  return JURISDICTION_COLOR[j ?? 'INT'] ?? '#455A64'
}

function fmtDate(iso: string) {
  return new Date(iso).toLocaleDateString('en-GB', { day: '2-digit', month: 'short', year: 'numeric' })
}

// ── Summary cards ─────────────────────────────────────────────────────────────
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

export default function FrameworkTracker() {
  const { data: frameworks, isLoading } = useQuery<FrameworkRow[]>({
    queryKey: ['framework-tracker'],
    queryFn: () => client.get('/frameworks/').then(r => r.data),
  })

  const { grouped, totalControls, updateCount, pendingCount } = useMemo(() => {
    if (!frameworks) return { grouped: {}, totalControls: 0, updateCount: 0, pendingCount: 0 }
    const g: Record<string, FrameworkRow[]> = {}
    let totalControls = 0
    let updateCount = 0
    let pendingCount = 0
    for (const fw of frameworks) {
      const j = fw.jurisdiction ?? 'INT'
      if (!g[j]) g[j] = []
      g[j].push(fw)
      totalControls += fw.controls_count
      const upd = KNOWN_UPDATES[fw.code]
      if (upd?.status === 'available') updateCount++
      if (upd?.status === 'pending') pendingCount++
    }
    return { grouped: g, totalControls, updateCount, pendingCount }
  }, [frameworks])

  const jurisdictionOrder = ['INT', 'EU', 'US', 'CH', 'DE', 'GB', 'BE', 'LU', 'IT', 'FR', 'AT']

  return (
    <Box sx={{ p: 3, maxWidth: 1200 }}>
      <PageHeader
        title="Framework Version Tracker"
        subtitle="Loaded compliance dataset versions, update availability, and dataset health"
      />

      {/* Summary row */}
      <Box sx={{ display: 'flex', gap: 2, mb: 3, flexWrap: 'wrap' }}>
        {isLoading ? (
          [1,2,3,4].map(i => <Skeleton key={i} variant="rectangular" width={140} height={80} sx={{ borderRadius: 1 }} />)
        ) : (
          <>
            <SummaryCard label="Frameworks loaded" value={frameworks?.length ?? 0} />
            <SummaryCard label="Total controls" value={totalControls.toLocaleString()} />
            <SummaryCard
              label="Updates available"
              value={updateCount}
              sub="datasets behind latest release"
              color={updateCount > 0 ? '#FF9800' : '#4CAF50'}
            />
            <SummaryCard
              label="Pending releases"
              value={pendingCount}
              sub="upcoming versions to watch"
              color={pendingCount > 0 ? '#42A5F5' : '#9E9E9E'}
            />
          </>
        )}
      </Box>

      {/* Per-jurisdiction tables */}
      {isLoading && (
        <Skeleton variant="rectangular" height={200} sx={{ borderRadius: 1 }} />
      )}

      {!isLoading && frameworks && jurisdictionOrder
        .filter(j => grouped[j]?.length > 0)
        .map(j => (
          <Box key={j} sx={{ mb: 3 }}>
            <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 1 }}>
              <Box sx={{ width: 4, height: 20, borderRadius: 1, bgcolor: jurisColor(j) }} />
              <Typography variant="body2" sx={{ fontWeight: 700, fontSize: '0.8rem', color: jurisColor(j) }}>
                {JURISDICTION_LABEL[j] ?? j}
              </Typography>
              <Typography variant="caption" color="text.secondary">
                ({grouped[j].length} framework{grouped[j].length !== 1 ? 's' : ''})
              </Typography>
            </Box>

            <TableContainer sx={{ border: '1px solid', borderColor: 'divider', borderRadius: 1 }}>
              <Table size="small">
                <TableHead>
                  <TableRow sx={{ bgcolor: 'background.paper' }}>
                    <TableCell sx={{ fontSize: '0.68rem', fontWeight: 700, color: 'text.secondary', textTransform: 'uppercase' }}>Framework</TableCell>
                    <TableCell sx={{ fontSize: '0.68rem', fontWeight: 700, color: 'text.secondary', textTransform: 'uppercase' }}>Version</TableCell>
                    <TableCell sx={{ fontSize: '0.68rem', fontWeight: 700, color: 'text.secondary', textTransform: 'uppercase' }} align="right">Controls</TableCell>
                    <TableCell sx={{ fontSize: '0.68rem', fontWeight: 700, color: 'text.secondary', textTransform: 'uppercase' }}>Publisher</TableCell>
                    <TableCell sx={{ fontSize: '0.68rem', fontWeight: 700, color: 'text.secondary', textTransform: 'uppercase' }}>Loaded</TableCell>
                    <TableCell sx={{ fontSize: '0.68rem', fontWeight: 700, color: 'text.secondary', textTransform: 'uppercase' }}>Status</TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                  {grouped[j].map(fw => {
                    const upd = KNOWN_UPDATES[fw.code]
                    return (
                      <TableRow key={fw.id} hover sx={{ '&:last-child td': { border: 0 } }}>
                        <TableCell>
                          <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.75 }}>
                            <Typography variant="body2" sx={{ fontWeight: 600, fontSize: '0.78rem' }}>
                              {fw.name}
                            </Typography>
                            {fw.source_url && (
                              <Tooltip title={fw.source_url}>
                                <OpenInNewOutlined
                                  sx={{ fontSize: 13, color: 'text.disabled', cursor: 'pointer', '&:hover': { color: 'primary.main' } }}
                                  onClick={() => window.open(fw.source_url!, '_blank')}
                                />
                              </Tooltip>
                            )}
                          </Box>
                          <Typography variant="caption" color="text.disabled" sx={{ fontSize: '0.62rem' }}>
                            {fw.code}
                          </Typography>
                        </TableCell>
                        <TableCell>
                          <Typography variant="body2" sx={{ fontSize: '0.75rem', fontFamily: 'monospace' }}>
                            {fw.version ?? '—'}
                          </Typography>
                        </TableCell>
                        <TableCell align="right">
                          <Typography variant="body2" sx={{ fontSize: '0.75rem', fontWeight: 600 }}>
                            {fw.controls_count.toLocaleString()}
                          </Typography>
                        </TableCell>
                        <TableCell>
                          <Typography variant="caption" color="text.secondary" sx={{ fontSize: '0.7rem' }}>
                            {fw.publisher ?? '—'}
                          </Typography>
                        </TableCell>
                        <TableCell>
                          <Typography variant="caption" color="text.secondary" sx={{ fontSize: '0.7rem' }}>
                            {fmtDate(fw.loaded_at)}
                          </Typography>
                        </TableCell>
                        <TableCell>
                          {!upd && (
                            <Chip
                              icon={<CheckCircleOutlined sx={{ fontSize: 13 }} />}
                              label="Current"
                              size="small"
                              sx={{ height: 18, fontSize: '0.6rem', bgcolor: 'rgba(76,175,80,0.1)', color: '#4CAF50', '& .MuiChip-icon': { color: '#4CAF50' } }}
                            />
                          )}
                          {upd?.status === 'available' && (
                            <Tooltip title={upd.note}>
                              <Chip
                                icon={<WarningAmberOutlined sx={{ fontSize: 13 }} />}
                                label={`Update: ${upd.latest}`}
                                size="small"
                                sx={{ height: 18, fontSize: '0.6rem', bgcolor: 'rgba(255,152,0,0.1)', color: '#FF9800', '& .MuiChip-icon': { color: '#FF9800' } }}
                              />
                            </Tooltip>
                          )}
                          {upd?.status === 'pending' && (
                            <Tooltip title={`${upd.note}${upd.eta ? ` ETA: ${upd.eta}` : ''}`}>
                              <Chip
                                icon={<UpdateOutlined sx={{ fontSize: 13 }} />}
                                label={`Pending: ${upd.latest}${upd.eta ? ` (${upd.eta})` : ''}`}
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
        ))
      }

      {/* ISO Reference Corpus & Glossary Standards */}
      <Box sx={{ mt: 4, mb: 1 }}>
        <Typography variant="subtitle2" sx={{ fontWeight: 700, mb: 0.5 }}>
          ISO Reference Corpus &amp; Glossary Standards
        </Typography>
        <Typography variant="caption" color="text.secondary" sx={{ display: 'block', mb: 2 }}>
          ISO/IEC normative texts indexed in the reference corpus and exposed via the Glossary page.
        </Typography>
        <TableContainer sx={{ border: '1px solid', borderColor: 'divider', borderRadius: 1 }}>
          <Table size="small">
            <TableHead>
              <TableRow sx={{ bgcolor: 'background.paper' }}>
                <TableCell sx={{ fontSize: '0.68rem', fontWeight: 700, color: 'text.secondary', textTransform: 'uppercase' }}>Standard</TableCell>
                <TableCell sx={{ fontSize: '0.68rem', fontWeight: 700, color: 'text.secondary', textTransform: 'uppercase' }}>Title</TableCell>
                <TableCell sx={{ fontSize: '0.68rem', fontWeight: 700, color: 'text.secondary', textTransform: 'uppercase' }}>Domain</TableCell>
                <TableCell sx={{ fontSize: '0.68rem', fontWeight: 700, color: 'text.secondary', textTransform: 'uppercase' }}>Edition</TableCell>
                <TableCell sx={{ fontSize: '0.68rem', fontWeight: 700, color: 'text.secondary', textTransform: 'uppercase' }}>Status</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {CORPUS_STANDARDS.map(s => (
                <TableRow key={s.standard} hover sx={{ '&:last-child td': { border: 0 } }}>
                  <TableCell>
                    <Typography variant="body2" sx={{ fontWeight: 600, fontSize: '0.78rem', fontFamily: 'monospace' }}>
                      {s.standard}
                    </Typography>
                  </TableCell>
                  <TableCell>
                    <Typography variant="body2" sx={{ fontSize: '0.75rem' }}>{s.title}</Typography>
                  </TableCell>
                  <TableCell>
                    <Chip
                      label={s.domain}
                      size="small"
                      sx={{
                        height: 18, fontSize: '0.6rem',
                        bgcolor: `${DOMAIN_COLOR[s.domain] ?? '#455A64'}22`,
                        color: DOMAIN_COLOR[s.domain] ?? '#455A64',
                        fontWeight: 600,
                      }}
                    />
                  </TableCell>
                  <TableCell>
                    <Typography variant="body2" sx={{ fontSize: '0.75rem', fontFamily: 'monospace' }}>
                      {s.edition}
                    </Typography>
                  </TableCell>
                  <TableCell>
                    {s.status === 'current' && (
                      <Chip
                        icon={<CheckCircleOutlined sx={{ fontSize: 13 }} />}
                        label="Current"
                        size="small"
                        sx={{ height: 18, fontSize: '0.6rem', bgcolor: 'rgba(76,175,80,0.1)', color: '#4CAF50', '& .MuiChip-icon': { color: '#4CAF50' } }}
                      />
                    )}
                    {s.status === 'pending' && (
                      <Tooltip title={`${s.note ?? ''}${s.eta ? ` ETA: ${s.eta}` : ''}`}>
                        <Chip
                          icon={<UpdateOutlined sx={{ fontSize: 13 }} />}
                          label={`Pending${s.eta ? ` (${s.eta})` : ''}`}
                          size="small"
                          sx={{ height: 18, fontSize: '0.6rem', bgcolor: 'rgba(66,165,245,0.1)', color: '#42A5F5', '& .MuiChip-icon': { color: '#42A5F5' } }}
                        />
                      </Tooltip>
                    )}
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </Box>

      <Typography variant="caption" color="text.disabled" sx={{ fontSize: '0.62rem', display: 'block', mt: 2 }}>
        <InfoOutlined sx={{ fontSize: 12, verticalAlign: 'middle', mr: 0.5 }} />
        Compliance datasets loaded from <code>datasets/data/*.json</code> on backend startup.
        ISO corpus seed files live in <code>datasets/data/iso-reference/</code>.
        Update availability tracked in <code>FrameworkTracker.tsx</code> → <code>KNOWN_UPDATES</code> and <code>CORPUS_STANDARDS</code>.
      </Typography>
    </Box>
  )
}
