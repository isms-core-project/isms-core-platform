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
  MITRE_ATTACK_V18: {
    latest: 'v19',
    status: 'pending',
    note: 'MITRE ATT&CK v19 — scheduled release 2026-04-28. Includes defense-evasion technique revisions.',
    eta: '2026-04-28',
  },
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

      <Typography variant="caption" color="text.disabled" sx={{ fontSize: '0.62rem', display: 'block', mt: 2 }}>
        <InfoOutlined sx={{ fontSize: 12, verticalAlign: 'middle', mr: 0.5 }} />
        Datasets are loaded from <code>datasets/data/*.json</code> on backend startup.
        To update a framework, replace its JSON bundle and rebuild the backend.
        Update availability is tracked in <code>FrameworkTracker.tsx</code> → <code>KNOWN_UPDATES</code>.
      </Typography>
    </Box>
  )
}
