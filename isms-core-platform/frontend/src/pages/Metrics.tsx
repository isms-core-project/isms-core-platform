import { useState } from 'react'
import {
  Alert, Box, FormControl, InputLabel, MenuItem, Select,
  Skeleton, Tab, Tabs, Table, TableBody, TableCell, TableHead,
  TableRow, Tooltip, Typography,
} from '@mui/material'
import {
  AssessmentOutlined, ErrorOutlined, GppMaybeOutlined, InsightsOutlined,
  InventoryOutlined, RefreshOutlined, SecurityOutlined, ShieldOutlined,
  TaskAltOutlined, VerifiedOutlined,
} from '@mui/icons-material'
import { IconButton } from '@mui/material'
import { useQuery, useQueryClient } from '@tanstack/react-query'
import {
  LineChart, Line, ResponsiveContainer, Tooltip as ChartTooltip,
} from 'recharts'
import { metricsApi, type MetricResult, type OrgMetricRow } from '../api/metricsApi'
import { projectsApi, type ProjectRead } from '../api/projectsApi'
import { useProject } from '../store/ProjectContext'
import { useAuth } from '../store/AuthContext'
import PageHeader from '../components/PageHeader'

// ── Config ────────────────────────────────────────────────────────────────────

const METRIC_ICON: Record<string, React.ReactNode> = {
  compliance_score:    <AssessmentOutlined sx={{ fontSize: 18 }} />,
  policy_coverage:     <InventoryOutlined sx={{ fontSize: 18 }} />,
  risk_score_avg:      <GppMaybeOutlined sx={{ fontSize: 18 }} />,
  risk_critical_count: <ErrorOutlined sx={{ fontSize: 18 }} />,
  evidence_freshness:  <VerifiedOutlined sx={{ fontSize: 18 }} />,
  gap_open_count:      <SecurityOutlined sx={{ fontSize: 18 }} />,
  gap_closure_rate:    <TaskAltOutlined sx={{ fontSize: 18 }} />,
  remediation_overdue: <ShieldOutlined sx={{ fontSize: 18 }} />,
  audit_readiness:     <InsightsOutlined sx={{ fontSize: 18 }} />,
}

// For count/numeric metrics: lower is better (red when high)
const LOWER_IS_BETTER = new Set(['risk_score_avg', 'risk_critical_count', 'gap_open_count', 'remediation_overdue'])

function metricColor(name: string, value: number, unit: string): string {
  if (unit === 'count' || name === 'risk_score_avg') {
    if (LOWER_IS_BETTER.has(name)) return value === 0 ? '#4CAF50' : value <= 3 ? '#FF9800' : '#F44336'
    return '#607D8B'
  }
  // percent: higher is better
  return value >= 75 ? '#4CAF50' : value >= 40 ? '#FF9800' : '#F44336'
}

function formatValue(value: number, unit: string): string {
  if (unit === 'percent') return `${value}%`
  if (unit === 'numeric') return value.toFixed(1)
  return String(Math.round(value))
}

// ── Sparkline ─────────────────────────────────────────────────────────────────

function Sparkline({ name, projectId, color }: { name: string; projectId?: string; color: string }) {
  const { data } = useQuery({
    queryKey: ['metric-history', name, projectId],
    queryFn: () => metricsApi.get(name, { project_id: projectId, days: 30 }),
  })

  if (!data?.history?.length) {
    return (
      <Typography variant="caption" sx={{ fontSize: '0.6rem', color: 'text.disabled' }}>
        No trend yet
      </Typography>
    )
  }

  return (
    <ResponsiveContainer width="100%" height={32}>
      <LineChart data={data.history}>
        <Line
          type="monotone"
          dataKey="value"
          stroke={color}
          strokeWidth={1.5}
          dot={false}
          isAnimationActive={false}
        />
        <ChartTooltip
          contentStyle={{ background: '#1a1a2e', border: 'none', fontSize: '0.65rem', padding: '2px 6px' }}
          labelFormatter={(l) => l}
          formatter={(v: number) => [v, '']}
        />
      </LineChart>
    </ResponsiveContainer>
  )
}

// ── Metric card ───────────────────────────────────────────────────────────────

function MetricCard({ metric, projectId }: { metric: MetricResult; projectId?: string }) {
  const color = metricColor(metric.name, metric.value, metric.unit)
  const icon = METRIC_ICON[metric.name]

  return (
    <Box sx={{
      border: '1px solid', borderColor: `${color}25`,
      borderRadius: 2, p: 2,
      bgcolor: `${color}06`,
      display: 'flex', flexDirection: 'column', gap: 1,
    }}>
      {/* Header */}
      <Box sx={{ display: 'flex', alignItems: 'flex-start', gap: 1 }}>
        <Box sx={{ color, mt: 0.25, flexShrink: 0 }}>{icon}</Box>
        <Box sx={{ flex: 1, minWidth: 0 }}>
          <Typography variant="caption" sx={{ fontSize: '0.68rem', color: 'text.secondary', lineHeight: 1.2, display: 'block' }}>
            {metric.label}
          </Typography>
          <Typography variant="h5" sx={{ fontWeight: 700, color, lineHeight: 1.1, fontSize: '1.6rem', mt: 0.25 }}>
            {formatValue(metric.value, metric.unit)}
          </Typography>
        </Box>
      </Box>

      {/* Sparkline */}
      <Sparkline name={metric.name} projectId={projectId} color={color} />
    </Box>
  )
}

// ── Audit readiness hero ──────────────────────────────────────────────────────

function AuditReadinessHero({ value, loading }: { value?: number; loading: boolean }) {
  const color = value !== undefined ? metricColor('audit_readiness', value, 'percent') : '#607D8B'
  return (
    <Box sx={{
      border: `1px solid ${color}40`, borderRadius: 2, p: 2.5, mb: 2.5,
      bgcolor: `${color}08`, display: 'flex', alignItems: 'center', gap: 3,
    }}>
      <InsightsOutlined sx={{ fontSize: 36, color, flexShrink: 0 }} />
      <Box>
        <Typography variant="caption" sx={{ color: 'text.secondary', fontSize: '0.75rem', textTransform: 'uppercase', letterSpacing: '0.08em' }}>
          Audit Readiness Score
        </Typography>
        {loading
          ? <Skeleton width={80} height={48} />
          : <Typography variant="h3" sx={{ fontWeight: 800, color, lineHeight: 1, fontSize: '2.8rem' }}>
              {value ?? '—'}{value !== undefined && '%'}
            </Typography>
        }
        <Typography variant="caption" sx={{ color: 'text.disabled', fontSize: '0.68rem' }}>
          Composite of compliance, policy coverage, evidence freshness, open risks &amp; gaps
        </Typography>
      </Box>
    </Box>
  )
}

// ── Portfolio table ───────────────────────────────────────────────────────────

const PORTFOLIO_COLS: { key: string; label: string; unit: string }[] = [
  { key: 'audit_readiness',    label: 'Audit Readiness',     unit: 'percent' },
  { key: 'compliance_score',   label: 'Compliance Score',    unit: 'percent' },
  { key: 'risk_score_avg',     label: 'Risk Score',          unit: 'numeric' },
  { key: 'gap_open_count',     label: 'Open Gaps',           unit: 'count'   },
  { key: 'remediation_overdue',label: 'Remediation Overdue', unit: 'count'   },
]

function PortfolioTab() {
  const { data, isLoading, error } = useQuery<OrgMetricRow[]>({
    queryKey: ['metrics-portfolio'],
    queryFn: metricsApi.portfolio,
    retry: false,
  })

  if (error) {
    return <Alert severity="warning" sx={{ mt: 2 }}>Portfolio data unavailable.</Alert>
  }

  const sorted = [...(data ?? [])].sort((a, b) => {
    const av = a.metrics['audit_readiness'] ?? -1
    const bv = b.metrics['audit_readiness'] ?? -1
    return bv - av
  })

  return (
    <Box sx={{ mt: 2, overflowX: 'auto' }}>
      <Table size="small">
        <TableHead>
          <TableRow>
            <TableCell sx={{ fontWeight: 600, color: 'text.secondary', fontSize: '0.72rem', textTransform: 'uppercase', letterSpacing: '0.06em' }}>
              Organisation
            </TableCell>
            {PORTFOLIO_COLS.map(col => (
              <TableCell key={col.key} align="right" sx={{ fontWeight: 600, color: 'text.secondary', fontSize: '0.72rem', textTransform: 'uppercase', letterSpacing: '0.06em' }}>
                {col.label}
              </TableCell>
            ))}
          </TableRow>
        </TableHead>
        <TableBody>
          {isLoading
            ? Array.from({ length: 4 }).map((_, i) => (
                <TableRow key={i}>
                  <TableCell><Skeleton width={160} /></TableCell>
                  {PORTFOLIO_COLS.map(col => (
                    <TableCell key={col.key} align="right"><Skeleton width={48} /></TableCell>
                  ))}
                </TableRow>
              ))
            : sorted.map(row => (
                <TableRow key={row.org_id} hover>
                  <TableCell sx={{ fontWeight: 500 }}>{row.org_name}</TableCell>
                  {PORTFOLIO_COLS.map(col => {
                    const val = row.metrics[col.key]
                    if (val === undefined) {
                      return (
                        <TableCell key={col.key} align="right" sx={{ color: 'text.disabled' }}>—</TableCell>
                      )
                    }
                    const color = metricColor(col.key, val, col.unit)
                    return (
                      <TableCell key={col.key} align="right" sx={{ color, fontWeight: 600 }}>
                        {formatValue(val, col.unit)}
                      </TableCell>
                    )
                  })}
                </TableRow>
              ))
          }
        </TableBody>
      </Table>
    </Box>
  )
}

// ── Main page ─────────────────────────────────────────────────────────────────

const OTHER_METRICS = [
  'compliance_score', 'policy_coverage', 'risk_score_avg', 'risk_critical_count',
  'evidence_freshness', 'gap_open_count', 'gap_closure_rate', 'remediation_overdue',
]

export default function Metrics() {
  const { activeProject } = useProject()
  const { user } = useAuth()
  const [projectId, setProjectId] = useState(activeProject?.id ?? '')
  const [tab, setTab] = useState(0)
  const qc = useQueryClient()
  const isSuperAdmin = user?.role === 'super_admin'

  const { data: projects } = useQuery({
    queryKey: ['projects-list'],
    queryFn: () => projectsApi.list(),
  })

  const { data, isLoading, error } = useQuery({
    queryKey: ['metrics', projectId],
    queryFn: () => metricsApi.list({ project_id: projectId || undefined }),
    enabled: tab === 0,
  })

  const byName = Object.fromEntries((data ?? []).map(m => [m.name, m]))
  const auditReadiness = byName['audit_readiness']
  const others = OTHER_METRICS.map(n => byName[n]).filter(Boolean)

  return (
    <Box sx={{ p: 3 }}>
      <PageHeader
        title="KPI Dashboard"
        subtitle="ISO 27001:2022 §9.1 — performance evaluation and measurement"
        actions={
          tab === 0
            ? (
              <Box sx={{ display: 'flex', gap: 1, alignItems: 'center' }}>
                <Tooltip title="Recompute metrics now">
                  <IconButton size="small" onClick={() => qc.invalidateQueries({ queryKey: ['metrics'], exact: false })}>
                    <RefreshOutlined sx={{ fontSize: 18 }} />
                  </IconButton>
                </Tooltip>
                <FormControl size="small" sx={{ minWidth: 240 }}>
                  <InputLabel>Scope</InputLabel>
                  <Select value={projectId} label="Scope" onChange={e => setProjectId(e.target.value)}>
                    <MenuItem value="">Org-wide</MenuItem>
                    {(projects ?? []).map((p: ProjectRead) => (
                      <MenuItem key={p.id} value={p.id}>{p.name}</MenuItem>
                    ))}
                  </Select>
                </FormControl>
              </Box>
            )
            : (
              <Tooltip title="Refresh portfolio">
                <IconButton size="small" onClick={() => qc.invalidateQueries({ queryKey: ['metrics-portfolio'] })}>
                  <RefreshOutlined sx={{ fontSize: 18 }} />
                </IconButton>
              </Tooltip>
            )
        }
      />

      {/* Tab bar — only shown to super_admin */}
      {isSuperAdmin && (
        <Tabs
          value={tab}
          onChange={(_, v) => setTab(v)}
          sx={{ mb: 2.5, borderBottom: '1px solid', borderColor: 'divider' }}
          textColor="primary"
          indicatorColor="primary"
        >
          <Tab label="My Metrics" />
          <Tab label="Portfolio" />
        </Tabs>
      )}

      {/* ── My Metrics tab ── */}
      {tab === 0 && (
        <>
          {error && <Alert severity="error" sx={{ mb: 2 }}>Failed to load metrics.</Alert>}

          {/* Audit readiness hero */}
          {isLoading
            ? <AuditReadinessHero loading />
            : <AuditReadinessHero value={auditReadiness?.value} loading={false} />
          }

          {/* KPI grid */}
          <Box sx={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(220px, 1fr))', gap: 2 }}>
            {isLoading
              ? Array.from({ length: 8 }).map((_, i) => (
                  <Box key={i} sx={{ border: '1px solid', borderColor: 'divider', borderRadius: 2, p: 2 }}>
                    <Skeleton height={20} width="60%" sx={{ mb: 1 }} />
                    <Skeleton height={40} width="40%" sx={{ mb: 1 }} />
                    <Skeleton height={32} />
                  </Box>
                ))
              : others.map(m => (
                  <Tooltip
                    key={m.name}
                    title={`Computed at ${new Date(m.computed_at).toLocaleString()}`}
                    placement="top"
                  >
                    <span>
                      <MetricCard metric={m} projectId={projectId || undefined} />
                    </span>
                  </Tooltip>
                ))
            }
          </Box>
        </>
      )}

      {/* ── Portfolio tab ── */}
      {tab === 1 && isSuperAdmin && <PortfolioTab />}
    </Box>
  )
}
