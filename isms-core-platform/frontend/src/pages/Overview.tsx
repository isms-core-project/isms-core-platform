import { useState } from 'react'
import { Grid, Card, CardContent, Typography, Box, Skeleton, Alert, LinearProgress, Chip, Button } from '@mui/material'
import {
  PolicyOutlined,
  DescriptionOutlined,
  AssignmentOutlined,
  AccountTreeOutlined,
  WarningAmberOutlined,
  FileDownloadOutlined,
  AccountBalanceOutlined,
} from '@mui/icons-material'
import { useQuery } from '@tanstack/react-query'
import { useNavigate } from 'react-router-dom'
import { dashboardApi, type FrameworkOverview } from '../api/dashboard'
import { adminApi } from '../api/admin'
import PageHeader from '../components/PageHeader'
import MetricCard from '../components/MetricCard'
import StatusChip from '../components/StatusChip'
import FirstRunBanner from '../components/FirstRunBanner'
import { useProduct, PRODUCT_COLORS, PRODUCT_SUBTITLES } from '../store/ProductContext'
import {
  RadarChart,
  PolarGrid,
  PolarAngleAxis,
  Radar,
  ResponsiveContainer,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  Tooltip,
  Cell,
} from 'recharts'

// Real API shapes
interface SectionRow {
  section: string
  section_name: string
  total_controls: number
  framework_covered: number
  operational_covered: number
  framework_pct: number
  operational_pct: number
}

interface RealOverview {
  total_controls: number
  total_policies: number
  total_implementations: number
  total_assessments: number
  total_gaps_open: number
  total_evidence: number
  framework: { total: number; has_policy: number; has_ug: number; has_tg: number; has_assessment: number; coverage_pct: number }
  operational: { total: number; has_policy: number; has_assessment: number; coverage_pct: number }
  items_by_status: Record<string, number>
  sections: SectionRow[]
}

interface RealReadiness {
  policies_pct: number
  ug_pct: number
  tg_pct: number
  assessments_pct: number
  evidence_pct: number
  gaps_closed_pct: number
  composite_score: number
  status: 'green' | 'amber' | 'red'
  breakdown: Record<string, number>
}

const SECTION_COLORS: Record<string, string> = {
  'A.0': '#8B9CC8',
  'A.5': '#4472C4',
  'A.6': '#70AD47',
  'A.7': '#FFC000',
  'A.8': '#C00000',
}

const STATUS_SCORE_COLOR = (s: string) =>
  s === 'green' ? '#C6EFCE' : s === 'amber' ? '#FFEB9C' : '#FFC7CE'

const SECTION_LABELS_27701: Record<string, string> = {
  'A.1': 'PII Controller',
  'A.2': 'PII Processor',
  'A.3': 'Shared (Both)',
}

function FrameworkOverviewWidget({ sourceFramework, color }: { sourceFramework: string; color: string }) {
  const navigate = useNavigate()
  const { data, isLoading } = useQuery({
    queryKey: ['dashboard', 'framework-overview', sourceFramework],
    queryFn: () => dashboardApi.getFrameworkOverview(sourceFramework),
  })
  const fw = data as FrameworkOverview | undefined

  if (isLoading) {
    return (
      <Grid container spacing={2}>
        {[...Array(4)].map((_, i) => (
          <Grid item xs={6} sm={3} key={i}>
            <Skeleton variant="rectangular" height={110} sx={{ borderRadius: 2 }} />
          </Grid>
        ))}
      </Grid>
    )
  }

  if (!fw) return null

  const barData = fw.sections.map((s) => ({
    name: SECTION_LABELS_27701[s.section] ?? s.section,
    Total: s.count,
    Mapped: s.mapped_count,
  }))

  const topTargets = Object.entries(fw.by_target_framework)
    .sort((a, b) => b[1] - a[1])
    .slice(0, 8)

  return (
    <Box>
      {/* Metric row */}
      <Grid container spacing={2} sx={{ mb: 3 }}>
        <Grid item xs={6} sm={3}>
          <MetricCard title="Controls" value={fw.total_controls} icon={<AccountTreeOutlined fontSize="small" />} />
        </Grid>
        <Grid item xs={6} sm={3}>
          <MetricCard title="Controls Mapped" value={fw.controls_with_mappings} icon={<AccountBalanceOutlined fontSize="small" />} />
        </Grid>
        <Grid item xs={6} sm={3}>
          <MetricCard title="Total Mappings" value={fw.total_mappings.toLocaleString()} icon={<AccountTreeOutlined fontSize="small" />} />
        </Grid>
        <Grid item xs={6} sm={3}>
          <MetricCard
            title="Coverage"
            value={`${fw.coverage_pct.toFixed(0)}%`}
            subtitle="controls mapped"
            progress={fw.coverage_pct}
            progressColor="primary"
          />
        </Grid>
      </Grid>

      {/* Charts row */}
      <Grid container spacing={2} sx={{ mb: 3 }}>
        {/* Section bar chart */}
        {barData.length > 0 && (
          <Grid item xs={12} md={7}>
            <Card>
              <CardContent>
                <Typography variant="h6" gutterBottom>Controls by Section</Typography>
                <ResponsiveContainer width="100%" height={220}>
                  <BarChart data={barData} margin={{ left: -10 }}>
                    <XAxis dataKey="name" tick={{ fill: '#8B9CC8', fontSize: 11 }} />
                    <YAxis tick={{ fill: '#8B9CC8', fontSize: 11 }} />
                    <Tooltip
                      contentStyle={{ backgroundColor: '#0F1629', border: '1px solid #4472C430', borderRadius: 8 }}
                      labelStyle={{ color: '#E8EAF0' }}
                      formatter={(v, name) => [`${v} controls`, name]}
                    />
                    <Bar dataKey="Total" fill={`${color}40`} radius={[3, 3, 0, 0]} />
                    <Bar dataKey="Mapped" fill={color} radius={[3, 3, 0, 0]} />
                  </BarChart>
                </ResponsiveContainer>
              </CardContent>
            </Card>
          </Grid>
        )}

        {/* Top target frameworks */}
        {topTargets.length > 0 && (
          <Grid item xs={12} md={5}>
            <Card sx={{ height: '100%' }}>
              <CardContent>
                <Typography variant="h6" gutterBottom>Top Mapped Frameworks</Typography>
                <Box sx={{ display: 'flex', flexDirection: 'column', gap: 1.2, mt: 1 }}>
                  {topTargets.map(([name, count]) => (
                    <Box key={name}>
                      <Box sx={{ display: 'flex', justifyContent: 'space-between', mb: 0.3 }}>
                        <Typography variant="caption" color="text.secondary" sx={{ maxWidth: 180, overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
                          {name}
                        </Typography>
                        <Typography variant="caption" fontWeight={600}>{count}</Typography>
                      </Box>
                      <LinearProgress
                        variant="determinate"
                        value={Math.min(100, (count / (topTargets[0]?.[1] ?? 1)) * 100)}
                        sx={{
                          height: 4, borderRadius: 2,
                          bgcolor: `${color}15`,
                          '& .MuiLinearProgress-bar': { bgcolor: color },
                        }}
                      />
                    </Box>
                  ))}
                </Box>
              </CardContent>
            </Card>
          </Grid>
        )}
      </Grid>

      {fw.total_mappings === 0 && (
        <Alert severity="info" sx={{ mt: 2 }}>
          No cross-framework mappings loaded yet for this standard. Import mapping datasets to populate this view.
        </Alert>
      )}
    </Box>
  )
}

function NonIsmsOverview({ product }: { product: 'privacy' | 'cloud' }) {
  const color = PRODUCT_COLORS[product] ?? '#4472C4'
  const [cloudSub, setCloudSub] = useState<'ISO27017' | 'ISO27018'>('ISO27017')

  const sourceFramework = product === 'cloud' ? cloudSub : 'ISO27701'
  const fwLabel = product === 'cloud'
    ? (cloudSub === 'ISO27017' ? 'ISO 27017 — Cloud Security' : 'ISO 27018 — PII in Cloud')
    : 'ISO 27701:2025 Ed. 2 — Privacy'

  return (
    <Box>
      <PageHeader title="Compliance Overview" subtitle={`${PRODUCT_SUBTITLES[product]} · ${fwLabel}`} />

      {/* Cloud sub-framework toggle */}
      {product === 'cloud' && (
        <Box sx={{ display: 'flex', gap: 1, mb: 3 }}>
          {([
            { value: 'ISO27017' as const, label: 'ISO 27017', desc: 'Cloud Security' },
            { value: 'ISO27018' as const, label: 'ISO 27018', desc: 'PII in Cloud' },
          ]).map(({ value, label, desc }) => (
            <Box
              key={value}
              onClick={() => setCloudSub(value)}
              sx={{
                px: 1.5, py: 0.75, borderRadius: 1, cursor: 'pointer',
                bgcolor: cloudSub === value ? 'rgba(255,192,0,0.15)' : 'rgba(255,255,255,0.04)',
                border: `1px solid ${cloudSub === value ? '#FFC00050' : 'rgba(255,255,255,0.08)'}`,
                '&:hover': { bgcolor: 'rgba(255,192,0,0.1)' },
              }}
            >
              <Typography variant="caption" fontWeight={cloudSub === value ? 700 : 400}
                color={cloudSub === value ? '#FFC000' : 'text.secondary'}>{label}</Typography>
              <Typography variant="caption" sx={{ ml: 1, opacity: 0.6 }}
                color={cloudSub === value ? '#FFC000' : 'text.disabled'}>{desc}</Typography>
            </Box>
          ))}
        </Box>
      )}

      <FrameworkOverviewWidget sourceFramework={sourceFramework} color={color} />
    </Box>
  )
}


export default function Overview() {
  const navigate = useNavigate()
  const { product } = useProduct()

  const { data: overview, isLoading, error } = useQuery({
    queryKey: ['dashboard', 'overview'],
    queryFn: dashboardApi.getOverview,
  })

  const { data: readiness } = useQuery({
    queryKey: ['dashboard', 'audit-readiness'],
    queryFn: dashboardApi.getAuditReadiness,
  })

  const { data: gaps } = useQuery({
    queryKey: ['dashboard', 'gaps', '', '', ''],
    queryFn: () => dashboardApi.getGaps({ limit: 5 }),
  })

  const { data: org } = useQuery({
    queryKey: ['organisation'],
    queryFn: adminApi.getOrganisation,
  })

  const { data: sysInfo } = useQuery({
    queryKey: ['sysinfo'],
    queryFn: adminApi.getSysInfo,
  })

  const ov = overview as unknown as RealOverview | undefined
  const rd = readiness as unknown as RealReadiness | undefined
  const gv = gaps as unknown as { total: number; items: Array<{ id: string; control_group_code: string; control_group_name: string; severity: string; status: string; description: string; product_type: string }> } | undefined

  if (isLoading) {
    return (
      <Box>
        <PageHeader title="Overview" subtitle="Loading..." />
        <Grid container spacing={2}>
          {[...Array(5)].map((_, i) => (
            <Grid item xs={6} sm={4} md={2} key={i}>
              <Skeleton variant="rectangular" height={110} sx={{ borderRadius: 2 }} />
            </Grid>
          ))}
        </Grid>
      </Box>
    )
  }

  if (error) {
    return (
      <Box>
        <PageHeader title="Overview" />
        <Alert severity="error">Failed to load dashboard data.</Alert>
      </Box>
    )
  }

  // Radar — coverage % per section (exclude foundation group)
  const radarData = (ov?.sections ?? [])
    .filter((s) => !['A.0', '00'].includes(s.section))
    .map((s) => ({
      subject: s.section,
      Framework: Math.min(100, s.framework_pct),
      Operational: Math.min(100, s.operational_pct),
    }))

  // Bar — controls covered per section (exclude foundation group)
  const barData = (ov?.sections ?? [])
    .filter((s) => !['A.0', '00'].includes(s.section))
    .map((s) => ({
      name: `${s.section}\n${s.section_name}`,
      shortName: s.section,
      Framework: s.framework_covered,
      Operational: s.operational_covered,
      total: s.total_controls,
    }))

  // Audit readiness components
  const readinessComponents = rd
    ? [
        { name: 'Policies', value: rd.policies_pct },
        { name: 'User Guides', value: rd.ug_pct },
        { name: 'Tech Guides', value: rd.tg_pct },
        { name: 'Assessments', value: rd.assessments_pct },
        { name: 'Evidence', value: rd.evidence_pct },
        { name: 'Gaps Closed', value: rd.gaps_closed_pct },
      ]
    : []

  // Maturity radar data (6-axis)
  const maturityData = rd ? [
    { subject: 'Policies',    value: rd.policies_pct },
    { subject: 'User Guides', value: rd.ug_pct },
    { subject: 'Tech Guides', value: rd.tg_pct },
    { subject: 'Assessments', value: rd.assessments_pct },
    { subject: 'Evidence',    value: rd.evidence_pct },
    { subject: 'Gaps Closed', value: rd.gaps_closed_pct },
  ] : []

  // Non-ISMS products: show framework overview
  if (product === 'privacy' || product === 'cloud') {
    return <NonIsmsOverview product={product} />
  }

  return (
    <Box>
      {org && sysInfo && (
        <FirstRunBanner
          totalControls={ov?.total_controls ?? 0}
          totalPolicies={ov?.total_policies ?? 0}
          totalImplementations={ov?.total_implementations ?? 0}
          smtpEnabled={sysInfo.smtp_enabled}
          orgSettings={org.settings ?? {}}
        />
      )}
      <PageHeader
        title="Compliance Overview"
        subtitle={`${ov?.total_controls ?? 0} control groups · ${PRODUCT_SUBTITLES.isms}`}
        actions={
          <Box sx={{ display: 'flex', alignItems: 'center', gap: 1.5 }}>
            {rd && (
              <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                <Typography variant="caption" color="text.secondary">Audit readiness</Typography>
                <StatusChip status={rd.status} />
                <Typography variant="h5" sx={{ color: STATUS_SCORE_COLOR(rd.status), fontWeight: 700 }}>
                  {rd.composite_score}%
                </Typography>
              </Box>
            )}
            <Button
              variant="outlined"
              size="small"
              startIcon={<FileDownloadOutlined />}
              onClick={() => navigate('/report')}
            >
              Export Report
            </Button>
          </Box>
        }
      />

      {/* Metric row */}
      <Grid container spacing={2} sx={{ mb: 3 }}>
        <Grid item xs={6} sm={4} md={2}>
          <MetricCard title="Controls" value={ov?.total_controls ?? 0} icon={<AccountTreeOutlined fontSize="small" />} />
        </Grid>
        <Grid item xs={6} sm={4} md={2}>
          <MetricCard title="Policies" value={ov?.total_policies ?? 0} icon={<PolicyOutlined fontSize="small" />} />
        </Grid>
        <Grid item xs={6} sm={4} md={2}>
          <MetricCard title="Implementations" value={ov?.total_implementations ?? 0} icon={<DescriptionOutlined fontSize="small" />} />
        </Grid>
        <Grid item xs={6} sm={4} md={2}>
          <MetricCard title="Assessments" value={ov?.total_assessments ?? 0} icon={<AssignmentOutlined fontSize="small" />} />
        </Grid>
        <Grid item xs={6} sm={4} md={2}>
          <MetricCard
            title="Framework"
            value={`${ov?.framework.coverage_pct ?? 0}%`}
            subtitle="coverage"
            progress={ov?.framework.coverage_pct}
            progressColor="primary"
          />
        </Grid>
        <Grid item xs={6} sm={4} md={2}>
          <MetricCard
            title="Operational"
            value={`${ov?.operational.coverage_pct ?? 0}%`}
            subtitle="coverage"
            progress={ov?.operational.coverage_pct}
            progressColor="success"
          />
        </Grid>
      </Grid>

      {/* Charts row */}
      <Grid container spacing={2} sx={{ mb: 3 }}>
        {/* Bar — controls covered */}
        <Grid item xs={12} md={7}>
          <Card>
            <CardContent>
              <Typography variant="h6" gutterBottom>Controls Covered by Section</Typography>
              <ResponsiveContainer width="100%" height={220}>
                <BarChart
                  data={barData}
                  margin={{ left: -10 }}
                  style={{ cursor: 'pointer' }}
                  onClick={(e) => {
                    if (e?.activePayload?.[0]?.payload?.shortName) {
                      navigate(`/controls?section=${e.activePayload[0].payload.shortName}`)
                    }
                  }}
                >
                  <XAxis dataKey="shortName" tick={{ fill: '#8B9CC8', fontSize: 12 }} />
                  <YAxis tick={{ fill: '#8B9CC8', fontSize: 11 }} />
                  <Tooltip
                    contentStyle={{ backgroundColor: '#0F1629', border: '1px solid #4472C430', borderRadius: 8 }}
                    labelStyle={{ color: '#E8EAF0' }}
                    formatter={(v, name) => [`${v} controls`, name]}
                  />
                  <Bar dataKey="Framework" fill="#4472C4" radius={[3, 3, 0, 0]} />
                  <Bar dataKey="Operational" fill="#70AD47" radius={[3, 3, 0, 0]} />
                </BarChart>
              </ResponsiveContainer>
            </CardContent>
          </Card>
        </Grid>

        {/* Radar */}
        <Grid item xs={12} md={5}>
          <Card sx={{ height: '100%' }}>
            <CardContent>
              <Typography variant="h6" gutterBottom>Coverage Radar</Typography>
              <ResponsiveContainer width="100%" height={220}>
                <RadarChart data={radarData}>
                  <PolarGrid stroke="#4472C420" />
                  <PolarAngleAxis dataKey="subject" tick={{ fill: '#8B9CC8', fontSize: 12 }} />
                  <Radar name="Framework" dataKey="Framework" stroke="#4472C4" fill="#4472C4" fillOpacity={0.3} />
                  <Radar name="Operational" dataKey="Operational" stroke="#70AD47" fill="#70AD47" fillOpacity={0.2} />
                </RadarChart>
              </ResponsiveContainer>
            </CardContent>
          </Card>
        </Grid>
      </Grid>

      {/* Readiness + Status row */}
      <Grid container spacing={2} sx={{ mb: 3 }}>
        {/* Audit readiness */}
        {rd && (
          <Grid item xs={12} md={7}>
            <Card>
              <CardContent>
                <Typography variant="h6" gutterBottom>Audit Readiness Breakdown</Typography>
                <Box sx={{ display: 'flex', flexDirection: 'column', gap: 1.5, mt: 1 }}>
                  {readinessComponents.map(({ name, value }) => (
                    <Box key={name}>
                      <Box sx={{ display: 'flex', justifyContent: 'space-between', mb: 0.4 }}>
                        <Typography variant="body2" color="text.secondary">{name}</Typography>
                        <Typography variant="body2" fontWeight={600}>{value.toFixed(0)}%</Typography>
                      </Box>
                      <LinearProgress
                        variant="determinate"
                        value={Math.min(100, value)}
                        sx={{
                          height: 6,
                          borderRadius: 3,
                          bgcolor: 'rgba(68,114,196,0.12)',
                          '& .MuiLinearProgress-bar': {
                            bgcolor: value >= 80 ? '#C6EFCE' : value >= 50 ? '#FFEB9C' : '#FFC7CE',
                          },
                        }}
                      />
                    </Box>
                  ))}
                </Box>
              </CardContent>
            </Card>
          </Grid>
        )}

        {/* ISMS Maturity Profile */}
        <Grid item xs={12} md={5}>
          <Card sx={{ height: '100%' }}>
            <CardContent>
              <Box sx={{ display: 'flex', alignItems: 'baseline', justifyContent: 'space-between', mb: 0.5 }}>
                <Typography variant="h6">Maturity Profile</Typography>
                {rd && (
                  <Typography
                    variant="h5"
                    sx={{ color: STATUS_SCORE_COLOR(rd.status), fontWeight: 800 }}
                  >
                    {rd.composite_score}%
                  </Typography>
                )}
              </Box>
              {rd && (
                <Typography variant="caption" color="text.secondary" sx={{ display: 'block', mb: 1 }}>
                  Composite audit readiness score
                </Typography>
              )}
              <ResponsiveContainer width="100%" height={200}>
                <RadarChart data={maturityData}>
                  <PolarGrid stroke="#4472C420" />
                  <PolarAngleAxis dataKey="subject" tick={{ fill: '#8B9CC8', fontSize: 11 }} />
                  <Radar name="Maturity" dataKey="value" stroke="#4472C4" fill="#4472C4" fillOpacity={0.3} />
                </RadarChart>
              </ResponsiveContainer>
            </CardContent>
          </Card>
        </Grid>
      </Grid>

      {/* Top gaps widget */}
      {gv && gv.total > 0 && (
        <Card sx={{ mb: 3 }}>
          <CardContent>
            <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 1.5 }}>
              <WarningAmberOutlined sx={{ color: '#FFC7CE', fontSize: 18 }} />
              <Typography variant="h6">Open Gaps</Typography>
              <Chip label={gv.total} size="small" sx={{ bgcolor: 'rgba(192,0,0,0.15)', color: '#FFC7CE', fontSize: '0.7rem', height: 18 }} />
            </Box>
            {gv.items.map((gap) => (
              <Box
                key={gap.id}
                sx={{
                  display: 'flex', alignItems: 'flex-start', gap: 1.5, mb: 1, p: 1,
                  bgcolor: 'rgba(192,0,0,0.06)', borderRadius: 1,
                  cursor: 'pointer', '&:hover': { bgcolor: 'rgba(192,0,0,0.1)' },
                }}
                onClick={() => navigate('/gaps')}
              >
                <StatusChip status={gap.severity} />
                <Box sx={{ flex: 1, minWidth: 0 }}>
                  <Typography variant="caption" sx={{ fontFamily: 'monospace', color: 'primary.light', fontWeight: 700 }}>
                    {gap.control_group_code.toUpperCase()}
                  </Typography>
                  <Typography variant="body2" sx={{ overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
                    {gap.description}
                  </Typography>
                </Box>
                <Typography variant="caption" color="text.secondary">{gap.product_type}</Typography>
              </Box>
            ))}
            {gv.total > 5 && (
              <Typography
                variant="caption" color="primary.light" sx={{ cursor: 'pointer', display: 'block', mt: 0.5 }}
                onClick={() => navigate('/gaps')}
              >
                View all {gv.total} gaps →
              </Typography>
            )}
          </CardContent>
        </Card>
      )}

      {/* Section table */}
      <Card>
        <CardContent>
          <Typography variant="h6" gutterBottom>Section Breakdown</Typography>
          {ov?.sections.filter((s) => !['A.0', '00'].includes(s.section)).map((s) => (
            <Box
              key={s.section}
              sx={{ mb: 2, cursor: 'pointer', borderRadius: 1, p: 0.5, mx: -0.5,
                '&:hover': { bgcolor: 'rgba(68,114,196,0.06)' } }}
              onClick={() => navigate(`/controls?section=${s.section}`)}
            >
              <Box sx={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', mb: 0.5 }}>
                <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                  <Box sx={{ width: 3, height: 16, borderRadius: 1, bgcolor: SECTION_COLORS[s.section] ?? '#4472C4' }} />
                  <Typography variant="body2" fontWeight={600}>
                    {s.section} — {s.section_name}
                  </Typography>
                  <Typography variant="caption" color="text.secondary">
                    ({s.total_controls} control{s.total_controls !== 1 ? 's' : ''})
                  </Typography>
                </Box>
                <Typography variant="caption" color="primary.light" sx={{ opacity: 0.6 }}>→</Typography>
              </Box>
              <Grid container spacing={1}>
                <Grid item xs={6}>
                  <Box sx={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', mb: 0.3 }}>
                    <Typography variant="caption" color="text.secondary">Framework</Typography>
                    <Typography variant="caption" fontWeight={600}>{s.framework_pct.toFixed(0)}%</Typography>
                  </Box>
                  <LinearProgress
                    variant="determinate"
                    value={Math.min(100, s.framework_pct)}
                    sx={{ height: 4, borderRadius: 2, bgcolor: 'rgba(68,114,196,0.12)',
                      '& .MuiLinearProgress-bar': { bgcolor: '#4472C4' } }}
                  />
                </Grid>
                <Grid item xs={6}>
                  <Box sx={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', mb: 0.3 }}>
                    <Typography variant="caption" color="text.secondary">Operational</Typography>
                    <Typography variant="caption" fontWeight={600}>{s.operational_pct.toFixed(0)}%</Typography>
                  </Box>
                  <LinearProgress
                    variant="determinate"
                    value={Math.min(100, s.operational_pct)}
                    sx={{ height: 4, borderRadius: 2, bgcolor: 'rgba(112,173,71,0.12)',
                      '& .MuiLinearProgress-bar': { bgcolor: '#70AD47' } }}
                  />
                </Grid>
              </Grid>
            </Box>
          ))}
        </CardContent>
      </Card>
    </Box>
  )
}
