import {
  Alert, Box, Chip, CircularProgress, Paper,
  Table, TableBody, TableCell, TableHead, TableRow, Typography,
} from '@mui/material'
import {
  BugReportOutlined, CheckCircleOutlined, ErrorOutlined,
  HourglassEmptyOutlined, PolicyOutlined, SecurityOutlined,
  SyncOutlined, VerifiedOutlined,
} from '@mui/icons-material'
import { useQuery } from '@tanstack/react-query'
import {
  Bar, BarChart, CartesianGrid, Cell, ResponsiveContainer,
  Tooltip as ChartTooltip, XAxis, YAxis,
} from 'recharts'
import { feedsApi } from '../api/feedsApi'
import PageHeader from '../components/PageHeader'

// ── Helpers ────────────────────────────────────────────────────────────────────

const INTEL_COLOR = '#B84F00'

function fmt(iso: string | null): string {
  if (!iso) return '—'
  return new Date(iso).toLocaleString(undefined, {
    year: 'numeric', month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit',
  })
}

function StatusChip({ status }: { status: string | null }) {
  if (!status)
    return <Chip label="Never run" size="small" sx={{ fontSize: '0.7rem' }} />
  if (status === 'success')
    return <Chip icon={<CheckCircleOutlined sx={{ fontSize: 14 }} />} label="OK" size="small" color="success" sx={{ fontSize: '0.7rem' }} />
  if (status === 'running')
    return <Chip icon={<SyncOutlined sx={{ fontSize: 14 }} />} label="Running" size="small" color="info" sx={{ fontSize: '0.7rem' }} />
  return <Chip icon={<ErrorOutlined sx={{ fontSize: 14 }} />} label="Error" size="small" color="error" sx={{ fontSize: '0.7rem' }} />
}

const FEED_ICONS: Record<string, React.ReactNode> = {
  mitre_attack_v18: <SecurityOutlined sx={{ fontSize: 28, color: INTEL_COLOR }} />,
  mitre_atlas:      <PolicyOutlined sx={{ fontSize: 28, color: INTEL_COLOR }} />,
  cisa_kev:         <BugReportOutlined sx={{ fontSize: 28, color: '#c62828' }} />,
  epss:             <VerifiedOutlined sx={{ fontSize: 28, color: '#1565c0' }} />,
}

const TACTIC_COLORS = [
  '#B84F00', '#d35400', '#e67e22', '#f39c12',
  '#c0392b', '#e74c3c', '#8e44ad', '#2980b9',
  '#27ae60', '#16a085', '#2c3e50', '#7f8c8d',
]

// ── Component ──────────────────────────────────────────────────────────────────

export default function ThreatFeeds() {
  const { data: status, isLoading: statusLoading, error: statusError } =
    useQuery({ queryKey: ['feeds', 'status'], queryFn: feedsApi.getStatus })

  const { data: kevStats } =
    useQuery({ queryKey: ['feeds', 'kev', 'stats'], queryFn: feedsApi.getKevStats })

  const { data: attackStats } =
    useQuery({ queryKey: ['feeds', 'attack', 'stats'], queryFn: feedsApi.getAttackStats })

  const { data: recentKev } = useQuery({
    queryKey: ['feeds', 'kev', 'recent'],
    queryFn: () => feedsApi.getKev({ per_page: 10, page: 1 }),
  })

  const tacticData = attackStats
    ? Object.entries(attackStats.tactic_counts)
        .sort((a, b) => b[1] - a[1])
        .slice(0, 12)
        .map(([name, count]) => ({ name: name.replace(/-/g, ' '), count }))
    : []

  return (
    <Box sx={{ p: 3 }}>
      <PageHeader
        title="Threat Intelligence"
        subtitle="Live threat & vulnerability feeds — MITRE ATT&CK, ATLAS, CISA KEV, EPSS"
        helpSection="threat-intelligence"
      />

      {statusLoading && <CircularProgress size={20} sx={{ mb: 2 }} />}
      {statusError && <Alert severity="error" sx={{ mb: 2 }}>Failed to load feed status</Alert>}

      {/* ── Feed status cards ── */}
      <Box sx={{ display: 'flex', gap: 2, flexWrap: 'wrap', mb: 3 }}>
        {(status?.feeds ?? []).map(feed => (
          <Paper key={feed.feed_name} variant="outlined" sx={{ p: 2, borderRadius: 2, flex: '1 1 220px', minWidth: 200 }}>
            <Box sx={{ display: 'flex', alignItems: 'flex-start', gap: 1.5 }}>
              {FEED_ICONS[feed.feed_name] ?? <SecurityOutlined sx={{ fontSize: 28, color: INTEL_COLOR }} />}
              <Box sx={{ flex: 1, minWidth: 0 }}>
                <Typography variant="subtitle2" sx={{ fontWeight: 600, fontSize: '0.82rem' }} noWrap>
                  {feed.display_name}
                </Typography>
                <StatusChip status={feed.last_status} />
                <Typography variant="caption" color="text.secondary" display="block" sx={{ mt: 0.5 }}>
                  Last: {fmt(feed.last_run)}
                </Typography>
                {feed.item_count != null && (
                  <Typography variant="caption" color="text.secondary">
                    {feed.item_count.toLocaleString()} items
                  </Typography>
                )}
                {feed.error_message && (
                  <Typography variant="caption" color="error.main" display="block" sx={{ mt: 0.25 }} noWrap>
                    {feed.error_message}
                  </Typography>
                )}
              </Box>
            </Box>
          </Paper>
        ))}
        {!statusLoading && (status?.feeds ?? []).length === 0 && (
          <Alert severity="info" icon={<HourglassEmptyOutlined />} sx={{ width: '100%' }}>
            No feed data yet — the feeds container will populate data on its first run.
          </Alert>
        )}
      </Box>

      {/* ── Charts row ── */}
      <Box sx={{ display: 'flex', gap: 2, flexWrap: 'wrap', mb: 3 }}>

        {/* CISA KEV by month */}
        {kevStats && kevStats.by_month.length > 0 && (
          <Paper variant="outlined" sx={{ p: 2, borderRadius: 2, flex: '2 1 420px' }}>
            <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 1.5 }}>
              <Typography variant="subtitle2" fontWeight={600}>CISA KEV — New Entries by Month</Typography>
              <Box sx={{ display: 'flex', gap: 2 }}>
                <Box>
                  <Typography variant="h6" sx={{ fontWeight: 700, color: '#c62828', lineHeight: 1 }}>
                    {kevStats.total_entries.toLocaleString()}
                  </Typography>
                  <Typography variant="caption" color="text.secondary">Total CVEs</Typography>
                </Box>
                <Box>
                  <Typography variant="h6" sx={{ fontWeight: 700, color: '#e53935', lineHeight: 1 }}>
                    {kevStats.ransomware_count.toLocaleString()}
                  </Typography>
                  <Typography variant="caption" color="text.secondary">Ransomware</Typography>
                </Box>
                <Box>
                  <Typography variant="h6" sx={{ fontWeight: 700, color: '#f57c00', lineHeight: 1 }}>
                    {kevStats.recent_30d}
                  </Typography>
                  <Typography variant="caption" color="text.secondary">Last 30d</Typography>
                </Box>
              </Box>
            </Box>
            <ResponsiveContainer width="100%" height={200}>
              <BarChart data={kevStats.by_month} barSize={8}>
                <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.05)" />
                <XAxis
                  dataKey="month"
                  tick={{ fontSize: 10 }}
                  tickFormatter={v => v.slice(2)}
                />
                <YAxis tick={{ fontSize: 10 }} width={30} />
                <ChartTooltip
                  contentStyle={{ background: '#1e2432', border: '1px solid rgba(255,255,255,0.1)', borderRadius: 6, fontSize: 12 }}
                />
                <Bar dataKey="count" fill="#c62828" radius={[2, 2, 0, 0]} />
              </BarChart>
            </ResponsiveContainer>
          </Paper>
        )}

        {/* ATT&CK techniques by tactic */}
        {tacticData.length > 0 && (
          <Paper variant="outlined" sx={{ p: 2, borderRadius: 2, flex: '1 1 300px' }}>
            <Typography variant="subtitle2" fontWeight={600} sx={{ mb: 1.5 }}>
              ATT&CK Techniques by Tactic
            </Typography>
            <Box sx={{ display: 'flex', gap: 2, mb: 1.5 }}>
              <Box>
                <Typography variant="h6" sx={{ fontWeight: 700, color: INTEL_COLOR, lineHeight: 1 }}>
                  {attackStats?.total_techniques.toLocaleString() ?? '—'}
                </Typography>
                <Typography variant="caption" color="text.secondary">Techniques</Typography>
              </Box>
              <Box>
                <Typography variant="h6" sx={{ fontWeight: 700, color: INTEL_COLOR, lineHeight: 1 }}>
                  {attackStats?.total_subtechniques.toLocaleString() ?? '—'}
                </Typography>
                <Typography variant="caption" color="text.secondary">Sub-techniques</Typography>
              </Box>
            </Box>
            <ResponsiveContainer width="100%" height={200}>
              <BarChart data={tacticData} layout="vertical" barSize={10}>
                <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.05)" />
                <XAxis type="number" tick={{ fontSize: 10 }} />
                <YAxis dataKey="name" type="category" tick={{ fontSize: 10 }} width={110} />
                <ChartTooltip
                  contentStyle={{ background: '#1e2432', border: '1px solid rgba(255,255,255,0.1)', borderRadius: 6, fontSize: 12 }}
                />
                <Bar dataKey="count" radius={[0, 2, 2, 0]}>
                  {tacticData.map((_, i) => (
                    <Cell key={i} fill={TACTIC_COLORS[i % TACTIC_COLORS.length]} />
                  ))}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </Paper>
        )}
      </Box>

      {/* ── Recent KEV entries ── */}
      {recentKev && recentKev.items.length > 0 && (
        <Paper variant="outlined" sx={{ borderRadius: 2, overflow: 'hidden' }}>
          <Box sx={{ px: 2, py: 1.5, borderBottom: '1px solid', borderColor: 'divider', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <Typography variant="subtitle2" fontWeight={600}>
              Recent CISA KEV Entries
            </Typography>
            <Typography variant="caption" color="text.secondary">
              {recentKev.total.toLocaleString()} total
            </Typography>
          </Box>
          <Table size="small">
            <TableHead>
              <TableRow>
                <TableCell sx={{ fontWeight: 600, fontSize: '0.72rem' }}>CVE</TableCell>
                <TableCell sx={{ fontWeight: 600, fontSize: '0.72rem' }}>Vendor / Product</TableCell>
                <TableCell sx={{ fontWeight: 600, fontSize: '0.72rem' }}>Added</TableCell>
                <TableCell sx={{ fontWeight: 600, fontSize: '0.72rem' }}>Ransomware</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {recentKev.items.map(entry => (
                <TableRow key={entry.id} hover>
                  <TableCell sx={{ fontSize: '0.78rem', fontFamily: 'monospace', color: '#c62828', fontWeight: 600 }}>
                    {entry.cve_id}
                  </TableCell>
                  <TableCell sx={{ fontSize: '0.78rem', maxWidth: 280 }}>
                    <Typography noWrap variant="inherit">
                      {entry.vendor_project} — {entry.product}
                    </Typography>
                  </TableCell>
                  <TableCell sx={{ fontSize: '0.78rem', whiteSpace: 'nowrap' }}>
                    {entry.date_added ?? '—'}
                  </TableCell>
                  <TableCell>
                    {entry.known_ransomware
                      ? <Chip label="Yes" size="small" color="error" sx={{ fontSize: '0.68rem', height: 18 }} />
                      : <Typography variant="caption" color="text.disabled">No</Typography>}
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </Paper>
      )}
    </Box>
  )
}
