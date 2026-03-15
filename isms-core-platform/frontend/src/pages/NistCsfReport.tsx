import { useParams, useNavigate } from 'react-router-dom'
import { useQuery } from '@tanstack/react-query'
import {
  Box, Typography, Chip, Grid, Stack, LinearProgress,
  Table, TableHead, TableBody, TableRow, TableCell, TableContainer,
  Button, GlobalStyles, Divider,
} from '@mui/material'
import {
  ArrowBackOutlined, PrintOutlined,
  DownloadOutlined,
} from '@mui/icons-material'
import {
  RadarChart, PolarGrid, PolarAngleAxis, PolarRadiusAxis,
  Radar, ResponsiveContainer, Legend, Tooltip,
  BarChart, Bar, XAxis, YAxis, Cell,
} from 'recharts'
import { nistApi, NistRating } from '../api/nistApi'

// ── Constants (duplicated from NistCsf to keep this module self-contained) ────

const FUNCTION_COLORS: Record<string, string> = {
  GV: '#4472C4', ID: '#ED7D31', PR: '#70AD47',
  DE: '#FFC000', RS: '#FF5252', RC: '#9966CC',
}
const FUNCTION_NAMES: Record<string, string> = {
  GV: 'Govern', ID: 'Identify', PR: 'Protect',
  DE: 'Detect', RS: 'Respond', RC: 'Recover',
}
const TIER_LABELS: Record<number, string> = {
  1: 'Partial', 2: 'Risk Informed', 3: 'Repeatable', 4: 'Adaptive',
}
const FUNCTION_ORDER = ['GV', 'ID', 'PR', 'DE', 'RS', 'RC']

function tierColor(tier: number | null): string {
  if (!tier) return 'rgba(255,255,255,0.08)'
  if (tier === 1) return '#FF5252'
  if (tier === 2) return '#FFC000'
  if (tier === 3) return '#70AD47'
  return '#4472C4'
}

function TierBadge({ tier }: { tier: number | null }) {
  if (!tier) return <Typography variant="caption" color="text.disabled">{'—'}</Typography>
  return (
    <Box sx={{
      display: 'inline-flex', alignItems: 'center', gap: 0.5,
      px: 1, py: 0.25, borderRadius: 1,
      bgcolor: `${tierColor(tier)}22`, border: `1px solid ${tierColor(tier)}44`,
    }}>
      <Box sx={{ width: 6, height: 6, borderRadius: '50%', bgcolor: tierColor(tier) }} />
      <Typography sx={{ fontSize: '0.7rem', fontWeight: 700, color: tierColor(tier) }}>
        T{tier}
      </Typography>
    </Box>
  )
}

// ── Radar custom label ─────────────────────────────────────────────────────────

function RadarLabel({ x, y, payload }: { x?: number; y?: number; payload?: { value: string } }) {
  if (!payload) return null
  const fc = Object.entries(FUNCTION_NAMES).find(([, v]) => v === payload.value)?.[0] ?? ''
  return (
    <text x={x} y={y} textAnchor="middle" dominantBaseline="central"
      style={{ fontSize: '10px', fill: FUNCTION_COLORS[fc] ?? '#8B9CC8', fontWeight: 700 }}>
      {payload.value}
    </text>
  )
}

// ── Gap bar (visual indicator) ────────────────────────────────────────────────

function GapBar({ current, target }: { current: number | null; target: number | null }) {
  if (current === null) return <Typography variant="caption" color="text.disabled">{'—'}</Typography>
  const pct = (current / 4) * 100
  const tpct = target ? (target / 4) * 100 : null
  return (
    <Box sx={{ width: 80, position: 'relative' }}>
      <Box sx={{ height: 6, borderRadius: 3, bgcolor: 'rgba(255,255,255,0.08)', overflow: 'hidden' }}>
        <Box sx={{ width: `${pct}%`, height: '100%', bgcolor: tierColor(current), borderRadius: 3 }} />
      </Box>
      {tpct !== null && (
        <Box sx={{
          position: 'absolute', top: 0, left: `${tpct}%`,
          width: 2, height: 6, bgcolor: '#70AD47',
          transform: 'translateX(-50%)',
        }} />
      )}
    </Box>
  )
}

// ── Print styles ──────────────────────────────────────────────────────────────

const PRINT_STYLES = (
  <GlobalStyles styles={{
    '@media print': {
      'nav, header, [class*="MuiDrawer"], [class*="MuiAppBar"], .no-print': {
        display: 'none !important',
      },
      body: { background: '#0a0f1e !important' },
      '.print-page': { padding: '0 !important' },
    },
  }} />
)

// ── Main component ────────────────────────────────────────────────────────────

export default function NistCsfReport() {
  const { id } = useParams<{ id: string }>()
  const navigate = useNavigate()

  const summaryQ = useQuery({
    queryKey: ['nist-summary', id],
    queryFn: () => nistApi.getProfileSummary(id!),
    enabled: !!id,
  })
  const fullQ = useQuery({
    queryKey: ['nist-full', id],
    queryFn: () => nistApi.getFullProfile(id!),
    enabled: !!id,
  })

  if (summaryQ.isLoading || fullQ.isLoading) {
    return <Box sx={{ p: 4 }}><LinearProgress /></Box>
  }
  if (!summaryQ.data || !fullQ.data) {
    return <Box sx={{ p: 4 }}><Typography color="error">Profile not found.</Typography></Box>
  }

  const summary = summaryQ.data
  const full = fullQ.data
  const profile = full.profile

  // ── Derived data ────────────────────────────────────────────────────────────

  const radarData = FUNCTION_ORDER.map(fc => {
    const fs = summary.function_scores.find(s => s.function_code === fc)
    return {
      subject: FUNCTION_NAMES[fc],
      current: fs?.avg_current ?? 0,
      target: fs?.avg_target ?? 0,
    }
  })

  const barData = FUNCTION_ORDER.map(fc => {
    const fs = summary.function_scores.find(s => s.function_code === fc)
    return {
      fc,
      name: FUNCTION_NAMES[fc],
      current: fs?.avg_current ?? 0,
      target: fs?.avg_target ?? 0,
      rated: fs?.rated_count ?? 0,
      total: fs?.total_count ?? 0,
    }
  })

  const gapRatings: NistRating[] = full.ratings
    .filter(r => r.current_tier !== null && r.target_tier !== null && r.target_tier > r.current_tier)
    .sort((a, b) => (b.target_tier! - b.current_tier!) - (a.target_tier! - a.current_tier!))

  const totalGap = full.ratings.reduce((acc, r) => {
    if (r.current_tier !== null && r.target_tier !== null) acc += r.target_tier - r.current_tier
    return acc
  }, 0)

  const handlePrint = () => window.print()

  const handleExportXlsx = async () => {
    const blob = await nistApi.exportXlsx(id!)
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = `NIST-CSF-${profile.name.replace(/\s+/g, '-')}.xlsx`
    a.click()
    URL.revokeObjectURL(url)
  }

  // ── Render ──────────────────────────────────────────────────────────────────

  return (
    <Box className="print-page" sx={{ p: 3, maxWidth: 1200, mx: 'auto' }}>
      {PRINT_STYLES}

      {/* ── Top bar ── */}
      <Stack direction="row" alignItems="flex-start" justifyContent="space-between" mb={3}>
        <Box>
          <Stack direction="row" alignItems="center" gap={1} mb={0.5}>
            <Box sx={{ width: 3, height: 32, bgcolor: '#4472C4', borderRadius: 2 }} />
            <Typography variant="h5" sx={{ fontWeight: 700, letterSpacing: '-0.02em' }}>
              NIST CSF 2.0 Assessment Report
            </Typography>
          </Stack>
          <Typography variant="h6" color="text.secondary" sx={{ fontWeight: 400, ml: '11px' }}>
            {profile.name}
          </Typography>
          <Stack direction="row" gap={1} mt={1} ml="11px" flexWrap="wrap">
            {profile.assessor && (
              <Chip label={`Assessor: ${profile.assessor}`} size="small" sx={{ fontSize: '0.68rem' }} />
            )}
            {profile.scope && (
              <Chip label={`Scope: ${profile.scope}`} size="small" sx={{ fontSize: '0.68rem' }} />
            )}
            <Chip
              label={profile.status.charAt(0).toUpperCase() + profile.status.slice(1)}
              size="small"
              sx={{ fontSize: '0.68rem', bgcolor: '#4472C422', color: '#4472C4' }}
            />
            <Chip
              label={new Date(profile.updated_at).toLocaleDateString('en-GB', { day: '2-digit', month: 'short', year: 'numeric' })}
              size="small"
              sx={{ fontSize: '0.68rem' }}
            />
          </Stack>
        </Box>

        <Stack direction="row" gap={1} className="no-print">
          <Button
            size="small" variant="outlined" startIcon={<ArrowBackOutlined />}
            onClick={() => navigate('/nist-csf')}
            sx={{ fontSize: '0.72rem' }}
          >
            Back
          </Button>
          <Button
            size="small" variant="outlined" startIcon={<DownloadOutlined />}
            onClick={handleExportXlsx}
            sx={{ fontSize: '0.72rem' }}
          >
            XLSX
          </Button>
          <Button
            size="small" variant="contained" startIcon={<PrintOutlined />}
            onClick={handlePrint}
            sx={{ fontSize: '0.72rem' }}
          >
            Print / PDF
          </Button>
        </Stack>
      </Stack>

      {/* ── KPI row ── */}
      <Grid container spacing={2} mb={3}>
        {[
          {
            label: 'Avg Current Tier',
            value: summary.avg_current_tier ? `T${summary.avg_current_tier.toFixed(1)}` : '—',
            sub: summary.avg_current_tier ? TIER_LABELS[Math.round(summary.avg_current_tier)] ?? '' : 'No ratings yet',
            color: tierColor(summary.avg_current_tier ? Math.round(summary.avg_current_tier) : null),
          },
          {
            label: 'Avg Target Tier',
            value: summary.avg_target_tier ? `T${summary.avg_target_tier.toFixed(1)}` : '—',
            sub: summary.avg_target_tier ? TIER_LABELS[Math.round(summary.avg_target_tier)] ?? '' : 'No targets set',
            color: tierColor(summary.avg_target_tier ? Math.round(summary.avg_target_tier) : null),
          },
          {
            label: 'Coverage',
            value: `${summary.rated_count}/${summary.total_subcategories}`,
            sub: `${Math.round((summary.rated_count / summary.total_subcategories) * 100)}% rated`,
            color: '#4472C4',
          },
          {
            label: 'Total Gap Score',
            value: totalGap > 0 ? `+${totalGap}` : totalGap === 0 && summary.rated_count > 0 ? '0' : '—',
            sub: gapRatings.length > 0 ? `${gapRatings.length} subcategories behind target` : 'No gaps identified',
            color: totalGap > 0 ? '#FFC000' : '#70AD47',
          },
        ].map(kpi => (
          <Grid item xs={12} sm={6} md={3} key={kpi.label}>
            <Box sx={{
              p: 2, borderRadius: 2, height: '100%',
              bgcolor: 'rgba(255,255,255,0.03)',
              border: `1px solid ${kpi.color}33`,
              borderLeft: `3px solid ${kpi.color}`,
            }}>
              <Typography variant="caption" color="text.secondary" sx={{ textTransform: 'uppercase', letterSpacing: '0.08em', fontSize: '0.62rem' }}>
                {kpi.label}
              </Typography>
              <Typography variant="h4" sx={{ fontWeight: 700, color: kpi.color, lineHeight: 1.2, mt: 0.5 }}>
                {kpi.value}
              </Typography>
              <Typography variant="caption" color="text.secondary" sx={{ fontSize: '0.65rem' }}>
                {kpi.sub}
              </Typography>
            </Box>
          </Grid>
        ))}
      </Grid>

      {/* ── Radar + Function breakdown ── */}
      <Grid container spacing={2} mb={3}>
        {/* Radar */}
        <Grid item xs={12} md={5}>
          <Box sx={{ p: 2, borderRadius: 2, bgcolor: 'rgba(255,255,255,0.02)', border: '1px solid rgba(255,255,255,0.06)', height: '100%' }}>
            <Typography variant="caption" color="text.secondary" sx={{ textTransform: 'uppercase', letterSpacing: '0.08em', fontSize: '0.62rem', display: 'block', mb: 1 }}>
              Maturity Radar
            </Typography>
            <ResponsiveContainer width="100%" height={260}>
              <RadarChart data={radarData} cx="50%" cy="50%" outerRadius="72%">
                <PolarGrid stroke="rgba(255,255,255,0.08)" />
                <PolarAngleAxis dataKey="subject" tick={RadarLabel as unknown as boolean} />
                <PolarRadiusAxis domain={[0, 4]} tickCount={5} tick={false} axisLine={false} />
                <Radar name="Current" dataKey="current" stroke="#4472C4" fill="#4472C4" fillOpacity={0.30} strokeWidth={2} />
                <Radar name="Target" dataKey="target" stroke="#70AD47" fill="#70AD47" fillOpacity={0.12} strokeWidth={1.5} strokeDasharray="5 3" />
                <Legend
                  iconType="circle"
                  iconSize={8}
                  formatter={(v) => <span style={{ fontSize: '0.68rem', color: '#8B9CC8' }}>{v}</span>}
                />
                <Tooltip
                  contentStyle={{ backgroundColor: '#0F1629', border: '1px solid #4472C430', borderRadius: 6, fontSize: '0.72rem' }}
                  formatter={(v: number) => [v === 0 ? '—' : `T${v.toFixed(1)}`, undefined]}
                />
              </RadarChart>
            </ResponsiveContainer>
          </Box>
        </Grid>

        {/* Function breakdown bar chart */}
        <Grid item xs={12} md={7}>
          <Box sx={{ p: 2, borderRadius: 2, bgcolor: 'rgba(255,255,255,0.02)', border: '1px solid rgba(255,255,255,0.06)', height: '100%' }}>
            <Typography variant="caption" color="text.secondary" sx={{ textTransform: 'uppercase', letterSpacing: '0.08em', fontSize: '0.62rem', display: 'block', mb: 1 }}>
              Function Breakdown
            </Typography>
            <ResponsiveContainer width="100%" height={260}>
              <BarChart data={barData} layout="vertical" margin={{ left: 60, right: 24 }} barCategoryGap="28%">
                <XAxis type="number" domain={[0, 4]} tickCount={5} tick={{ fill: '#8B9CC8', fontSize: 10 }} />
                <YAxis type="category" dataKey="name" tick={{ fill: '#8B9CC8', fontSize: 11 }} width={60} />
                <Tooltip
                  contentStyle={{ backgroundColor: '#0F1629', border: '1px solid #4472C430', borderRadius: 6, fontSize: '0.72rem' }}
                  formatter={(v: number, name: string) => [v === 0 ? '—' : `T${v.toFixed(1)}`, name]}
                />
                <Bar dataKey="current" name="Current" radius={[0, 3, 3, 0]}>
                  {barData.map(d => (
                    <Cell key={d.fc} fill={FUNCTION_COLORS[d.fc]} fillOpacity={0.8} />
                  ))}
                </Bar>
                <Bar dataKey="target" name="Target" radius={[0, 3, 3, 0]}>
                  {barData.map(d => (
                    <Cell key={d.fc} fill={FUNCTION_COLORS[d.fc]} fillOpacity={0.35} />
                  ))}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </Box>
        </Grid>
      </Grid>

      {/* ── Function score table ── */}
      <Box sx={{ mb: 3 }}>
        <Typography variant="caption" color="text.secondary" sx={{ textTransform: 'uppercase', letterSpacing: '0.08em', fontSize: '0.62rem', display: 'block', mb: 1 }}>
          Function Scores
        </Typography>
        <TableContainer sx={{ borderRadius: 2, border: '1px solid rgba(255,255,255,0.06)' }}>
          <Table size="small">
            <TableHead>
              <TableRow sx={{ bgcolor: 'rgba(255,255,255,0.04)' }}>
                {['Function', 'Name', 'Avg Current', 'Avg Target', 'Gap', 'Rated / Total', 'Progress'].map(h => (
                  <TableCell key={h} sx={{ fontSize: '0.68rem', fontWeight: 700, color: 'text.secondary', py: 0.75 }}>
                    {h}
                  </TableCell>
                ))}
              </TableRow>
            </TableHead>
            <TableBody>
              {summary.function_scores.map(fs => {
                const gap = fs.avg_current != null && fs.avg_target != null
                  ? fs.avg_target - fs.avg_current : null
                return (
                  <TableRow key={fs.function_code} sx={{ '&:hover': { bgcolor: 'rgba(255,255,255,0.02)' } }}>
                    <TableCell sx={{ py: 0.6 }}>
                      <Chip
                        label={fs.function_code}
                        size="small"
                        sx={{ fontSize: '0.65rem', height: 18, bgcolor: `${FUNCTION_COLORS[fs.function_code]}22`, color: FUNCTION_COLORS[fs.function_code], fontWeight: 700 }}
                      />
                    </TableCell>
                    <TableCell sx={{ py: 0.6, fontSize: '0.78rem' }}>{fs.function_name}</TableCell>
                    <TableCell sx={{ py: 0.6 }}><TierBadge tier={fs.avg_current ? Math.round(fs.avg_current) : null} /></TableCell>
                    <TableCell sx={{ py: 0.6 }}><TierBadge tier={fs.avg_target ? Math.round(fs.avg_target) : null} /></TableCell>
                    <TableCell sx={{ py: 0.6, fontSize: '0.75rem', color: gap != null && gap > 0 ? '#FFC000' : gap === 0 ? '#70AD47' : 'text.disabled' }}>
                      {gap != null ? (gap > 0 ? `+${gap.toFixed(2)}` : gap.toFixed(2)) : '—'}
                    </TableCell>
                    <TableCell sx={{ py: 0.6, fontSize: '0.75rem' }}>{fs.rated_count} / {fs.total_count}</TableCell>
                    <TableCell sx={{ py: 0.6, width: 120 }}>
                      <LinearProgress
                        variant="determinate"
                        value={Math.min(100, (fs.rated_count / fs.total_count) * 100)}
                        sx={{ height: 4, borderRadius: 2, bgcolor: 'rgba(255,255,255,0.08)', '& .MuiLinearProgress-bar': { bgcolor: FUNCTION_COLORS[fs.function_code] } }}
                      />
                    </TableCell>
                  </TableRow>
                )
              })}
            </TableBody>
          </Table>
        </TableContainer>
      </Box>

      {/* ── Gap Analysis ── */}
      {gapRatings.length > 0 && (
        <Box sx={{ mb: 3 }}>
          <Typography variant="caption" color="text.secondary" sx={{ textTransform: 'uppercase', letterSpacing: '0.08em', fontSize: '0.62rem', display: 'block', mb: 1 }}>
            Gap Analysis {'—'} {gapRatings.length} subcategories behind target
          </Typography>
          <TableContainer sx={{ borderRadius: 2, border: '1px solid rgba(255,255,255,0.06)' }}>
            <Table size="small">
              <TableHead>
                <TableRow sx={{ bgcolor: 'rgba(255,255,255,0.04)' }}>
                  {['Fn', 'Subcategory', 'Title', 'Current', 'Target', 'Gap', 'ISO 27001'].map(h => (
                    <TableCell key={h} sx={{ fontSize: '0.68rem', fontWeight: 700, color: 'text.secondary', py: 0.75 }}>{h}</TableCell>
                  ))}
                </TableRow>
              </TableHead>
              <TableBody>
                {gapRatings.map(r => {
                  const gap = r.target_tier! - r.current_tier!
                  return (
                    <TableRow key={r.subcategory_id} sx={{ '&:hover': { bgcolor: 'rgba(255,255,255,0.02)' } }}>
                      <TableCell sx={{ py: 0.5 }}>
                        <Box sx={{ width: 6, height: 6, borderRadius: '50%', bgcolor: FUNCTION_COLORS[r.function_code] ?? '#888' }} />
                      </TableCell>
                      <TableCell sx={{ py: 0.5, fontSize: '0.72rem', fontFamily: 'monospace', color: '#8B9CC8' }}>
                        {r.subcategory_code}
                      </TableCell>
                      <TableCell sx={{ py: 0.5, fontSize: '0.72rem', maxWidth: 320 }}>
                        {r.subcategory_title}
                      </TableCell>
                      <TableCell sx={{ py: 0.5 }}><TierBadge tier={r.current_tier} /></TableCell>
                      <TableCell sx={{ py: 0.5 }}><TierBadge tier={r.target_tier} /></TableCell>
                      <TableCell sx={{ py: 0.5 }}>
                        <Chip
                          label={`+${gap}`} size="small"
                          sx={{ fontSize: '0.62rem', height: 16, fontWeight: 700, bgcolor: '#FFC00022', color: '#FFC000' }}
                        />
                      </TableCell>
                      <TableCell sx={{ py: 0.5, fontSize: '0.65rem', color: 'text.secondary' }}>
                        {r.iso_mappings.slice(0, 3).join(', ')}{r.iso_mappings.length > 3 ? ` +${r.iso_mappings.length - 3}` : ''}
                      </TableCell>
                    </TableRow>
                  )
                })}
              </TableBody>
            </Table>
          </TableContainer>
        </Box>
      )}

      {/* ── Full assessment ── */}
      <Divider sx={{ mb: 2, opacity: 0.2 }} />
      <Typography variant="caption" color="text.secondary" sx={{ textTransform: 'uppercase', letterSpacing: '0.08em', fontSize: '0.62rem', display: 'block', mb: 1 }}>
        Full Assessment {'—'} 106 Subcategories
      </Typography>
      <TableContainer sx={{ borderRadius: 2, border: '1px solid rgba(255,255,255,0.06)' }}>
        <Table size="small" stickyHeader>
          <TableHead>
            <TableRow>
              {['Fn', 'Code', 'Title', 'Current', 'Target', 'Gap', 'Progress', 'ISO 27001'].map(h => (
                <TableCell key={h} sx={{ fontSize: '0.68rem', fontWeight: 700, color: 'text.secondary', py: 0.75, bgcolor: '#0a0f1e' }}>{h}</TableCell>
              ))}
            </TableRow>
          </TableHead>
          <TableBody>
            {FUNCTION_ORDER.map(fc => {
              const rows = full.ratings.filter(r => r.function_code === fc)
              return rows.map((r, i) => {
                const gap = r.current_tier != null && r.target_tier != null
                  ? r.target_tier - r.current_tier : null
                return (
                  <TableRow key={r.subcategory_id} sx={{ '&:hover': { bgcolor: 'rgba(255,255,255,0.015)' } }}>
                    {i === 0 ? (
                      <TableCell rowSpan={rows.length} sx={{ py: 0.5, verticalAlign: 'top', pt: 1 }}>
                        <Chip
                          label={fc} size="small"
                          sx={{ fontSize: '0.65rem', height: 18, bgcolor: `${FUNCTION_COLORS[fc]}22`, color: FUNCTION_COLORS[fc], fontWeight: 700 }}
                        />
                      </TableCell>
                    ) : null}
                    <TableCell sx={{ py: 0.5, fontSize: '0.68rem', fontFamily: 'monospace', color: '#8B9CC8', whiteSpace: 'nowrap' }}>
                      {r.subcategory_code}
                    </TableCell>
                    <TableCell sx={{ py: 0.5, fontSize: '0.72rem', maxWidth: 280 }}>
                      {r.subcategory_title}
                    </TableCell>
                    <TableCell sx={{ py: 0.5 }}><TierBadge tier={r.current_tier} /></TableCell>
                    <TableCell sx={{ py: 0.5 }}><TierBadge tier={r.target_tier} /></TableCell>
                    <TableCell sx={{ py: 0.5, fontSize: '0.72rem' }}>
                      {gap != null
                        ? <Typography sx={{ fontSize: '0.7rem', fontWeight: 700, color: gap > 0 ? '#FFC000' : gap === 0 ? '#70AD47' : '#FF5252' }}>
                          {gap > 0 ? `+${gap}` : gap}
                        </Typography>
                        : <Typography variant="caption" color="text.disabled">{'—'}</Typography>}
                    </TableCell>
                    <TableCell sx={{ py: 0.5, width: 80 }}>
                      <GapBar current={r.current_tier} target={r.target_tier} />
                    </TableCell>
                    <TableCell sx={{ py: 0.5, fontSize: '0.62rem', color: 'text.secondary', maxWidth: 120 }}>
                      {r.iso_mappings.slice(0, 2).join(', ')}{r.iso_mappings.length > 2 ? ` +${r.iso_mappings.length - 2}` : ''}
                    </TableCell>
                  </TableRow>
                )
              })
            })}
          </TableBody>
        </Table>
      </TableContainer>
    </Box>
  )
}
