import { useState } from 'react'
import {
  Alert, Box, Button, Chip, CircularProgress, FormControl, FormControlLabel,
  InputLabel, MenuItem, Paper, Select, Switch, Tab, Table, TableBody, TableCell,
  TableHead, TableRow, Tabs, Tooltip, Typography, useTheme,
} from '@mui/material'
import {
  BugReportOutlined, CheckCircleOutlined, CoronavirusOutlined, DownloadOutlined,
  ErrorOutlined, HourglassEmptyOutlined, PlayArrowOutlined, PolicyOutlined,
  RouterOutlined, SecurityOutlined, StopOutlined, SyncOutlined, TrackChangesOutlined,
  TuneOutlined, VerifiedOutlined,
} from '@mui/icons-material'
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import {
  Bar, BarChart, CartesianGrid, Cell, ResponsiveContainer,
  Tooltip as ChartTooltip, XAxis, YAxis,
} from 'recharts'
import { feedsApi, type FeedStatusItem } from '../api/feedsApi'
import { threatIntelApi } from '../api/threatIntelApi'
import { client } from '../api/client'
import PageHeader from '../components/PageHeader'
import { useAuth } from '../store/AuthContext'

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
  mitre_attack_v19: <SecurityOutlined sx={{ fontSize: 28, color: INTEL_COLOR }} />,
  mitre_atlas:      <PolicyOutlined sx={{ fontSize: 28, color: INTEL_COLOR }} />,
  cisa_kev:         <BugReportOutlined sx={{ fontSize: 28, color: '#c62828' }} />,
  epss:             <VerifiedOutlined sx={{ fontSize: 28, color: '#1565c0' }} />,
  circl_misp:       <TrackChangesOutlined sx={{ fontSize: 28, color: INTEL_COLOR }} />,
  botvrij_misp:     <TrackChangesOutlined sx={{ fontSize: 28, color: INTEL_COLOR }} />,
  abuseipdb:        <RouterOutlined sx={{ fontSize: 28, color: '#7b1fa2' }} />,
  malpedia:         <CoronavirusOutlined sx={{ fontSize: 28, color: '#b71c1c' }} />,
  urlhaus:          <RouterOutlined sx={{ fontSize: 28, color: '#e65100' }} />,
  threatfox:        <TrackChangesOutlined sx={{ fontSize: 28, color: '#b71c1c' }} />,
  sslbl:            <SecurityOutlined sx={{ fontSize: 28, color: '#4a148c' }} />,
  feodotracker:     <TrackChangesOutlined sx={{ fontSize: 28, color: '#880e4f' }} />,
  red_flag_domains: <ErrorOutlined sx={{ fontSize: 28, color: '#c62828' }} />,
  stopforumspam:    <RouterOutlined sx={{ fontSize: 28, color: '#37474f' }} />,
  malwarebazaar:    <BugReportOutlined sx={{ fontSize: 28, color: '#e65100' }} />,
  exploitdb:        <BugReportOutlined sx={{ fontSize: 28, color: '#b71c1c' }} />,
}

const TI_FEED_DEFS: Array<Pick<FeedStatusItem, 'feed_name' | 'display_name'>> = [
  { feed_name: 'circl_misp',       display_name: 'MISP CIRCL' },
  { feed_name: 'botvrij_misp',     display_name: 'MISP Botvrij' },
  { feed_name: 'abuseipdb',        display_name: 'AbuseIPDB' },
  { feed_name: 'urlhaus',          display_name: 'URLhaus' },
  { feed_name: 'threatfox',        display_name: 'ThreatFox' },
  { feed_name: 'sslbl',            display_name: 'SSL Blacklist' },
  { feed_name: 'feodotracker',     display_name: 'Feodo Tracker' },
  { feed_name: 'red_flag_domains', display_name: 'Red Flag Domains' },
  { feed_name: 'stopforumspam',    display_name: 'Stopforumspam' },
  { feed_name: 'malwarebazaar',    display_name: 'MalwareBazaar' },
  { feed_name: 'malpedia',         display_name: 'Malpedia' },
]

const TACTIC_COLORS = [
  '#B84F00', '#d35400', '#e67e22', '#f39c12',
  '#c0392b', '#e74c3c', '#8e44ad', '#2980b9',
  '#27ae60', '#16a085', '#2c3e50', '#7f8c8d',
]

// ── Component ──────────────────────────────────────────────────────────────────

const AUDIT_STATUS_COLORS_DARK: Record<string, { bg: string; color: string; label: string }> = {
  no_evidence:    { bg: '#3a0a0a',              color: '#FFC7CE', label: 'No Evidence' },
  pending_review: { bg: '#3a2e00',              color: '#FFEB9C', label: 'Pending Review' },
  draft:          { bg: '#1e1e2e',              color: '#aaa',    label: 'Draft' },
  active:         { bg: '#1a2a3a',              color: '#9fc8f0', label: 'Active' },
  approved:       { bg: '#1a3a27',              color: '#C6EFCE', label: 'Approved' },
  rejected:       { bg: '#2a1a1a',              color: '#FFC7CE', label: 'Rejected' },
}
const AUDIT_STATUS_COLORS_LIGHT: Record<string, { bg: string; color: string; label: string }> = {
  no_evidence:    { bg: 'rgba(192,0,0,0.12)',   color: '#9e0000', label: 'No Evidence' },
  pending_review: { bg: 'rgba(230,160,0,0.12)', color: '#7a4800', label: 'Pending Review' },
  draft:          { bg: 'rgba(0,0,0,0.07)',     color: '#555',    label: 'Draft' },
  active:         { bg: 'rgba(68,114,196,0.12)',color: '#2E5099', label: 'Active' },
  approved:       { bg: 'rgba(46,125,50,0.12)', color: '#1b5e20', label: 'Approved' },
  rejected:       { bg: 'rgba(192,0,0,0.12)',   color: '#9e0000', label: 'Rejected' },
}

function exportAuditCsv(entries: import('../api/feedsApi').KevAuditEntry[], months: number) {
  const header = 'CVE ID,Vulnerability Name,Vendor,Product,Date Added,Due Date,Ransomware,Evidence Status,Evidence Title'
  const rows = entries.map(e => [
    e.cve_id,
    e.vulnerability_name ?? '',
    e.vendor_project ?? '',
    e.product ?? '',
    e.date_added ?? '',
    e.due_date ?? '',
    e.known_ransomware ? 'Yes' : 'No',
    e.evidence_status,
    e.evidence_title ?? '',
  ].map(v => `"${String(v).replace(/"/g, '""')}"`).join(','))
  const csv = [header, ...rows].join('\n')
  const blob = new Blob([csv], { type: 'text/csv' })
  const url = URL.createObjectURL(blob)
  const a = document.createElement('a')
  a.href = url
  a.download = `KEV-Audit-Report-${months}m.csv`
  a.click()
  URL.revokeObjectURL(url)
}

export default function ThreatFeeds() {
  const muiTheme = useTheme()
  const isLight = muiTheme.palette.mode === 'light'
  const AUDIT_STATUS_COLORS = isLight ? AUDIT_STATUS_COLORS_LIGHT : AUDIT_STATUS_COLORS_DARK
  const tooltipStyle = {
    background: muiTheme.palette.background.paper,
    border: `1px solid ${muiTheme.palette.divider}`,
    borderRadius: 6,
    fontSize: 12,
    color: muiTheme.palette.text.primary,
  }
  const [auditMonths, setAuditMonths] = useState(12)
  const [feedTab, setFeedTab] = useState(0)
  const { user } = useAuth()
  const isAdmin = user?.role === 'admin' || user?.role === 'super_admin'
  const qc = useQueryClient()

  const { data: platformFeatures } = useQuery({
    queryKey: ['platform', 'features'],
    queryFn: () => client.get<{ threat_intel_enabled: boolean }>('/platform/features').then(r => r.data),
    staleTime: 10 * 60_000,
  })
  const tiEnabled = platformFeatures?.threat_intel_enabled ?? false

  const { data: tiSummary } = useQuery({
    queryKey: ['threat-intel', 'summary'],
    queryFn: threatIntelApi.getSummary,
    enabled: tiEnabled,
    refetchInterval: 30_000,
  })

  const { data: status, isLoading: statusLoading, error: statusError } =
    useQuery({ queryKey: ['feeds', 'status'], queryFn: feedsApi.getStatus })

  const { data: feedSettings } = useQuery({
    queryKey: ['feeds', 'settings'],
    queryFn: feedsApi.getFeedSettings,
    enabled: isAdmin,
  })

  const settingsMutation = useMutation({
    mutationFn: feedsApi.patchFeedSettings,
    onSuccess: () => qc.invalidateQueries({ queryKey: ['feeds', 'settings'] }),
  })

  const [triggerError, setTriggerError] = useState<string | null>(null)
  const triggerMutation = useMutation({
    mutationFn: ({ feedName, mode }: { feedName: string; mode?: 'full' | 'delta' }) =>
      feedsApi.triggerFeed(feedName, mode),
    onSuccess: () => {
      setTriggerError(null)
      setTimeout(() => qc.invalidateQueries({ queryKey: ['feeds', 'status'] }), 2000)
    },
    onError: (err: any) => {
      setTriggerError(err?.response?.data?.detail ?? 'Trigger failed')
    },
  })

  const cancelMutation = useMutation({
    mutationFn: (feedName: string) => feedsApi.cancelFeed(feedName),
    onSuccess: () => {
      setTimeout(() => qc.invalidateQueries({ queryKey: ['feeds', 'status'] }), 3000)
    },
    onError: (err: any) => {
      // 404 = feed already stopped (e.g. container restarted) — treat as success
      if (err?.response?.status === 404) {
        setTimeout(() => qc.invalidateQueries({ queryKey: ['feeds', 'status'] }), 1000)
      } else {
        setTriggerError(err?.response?.data?.detail ?? 'Cancel failed')
      }
    },
  })

  const tiTriggerMutation = useMutation({
    mutationFn: (source: string) => threatIntelApi.triggerFeed(source),
    onSuccess: () => {
      setTriggerError(null)
      setTimeout(() => qc.invalidateQueries({ queryKey: ['threat-intel', 'summary'] }), 2000)
    },
    onError: (err: any) => {
      setTriggerError(err?.response?.data?.detail ?? 'TI trigger failed')
    },
  })

  const tiCancelMutation = useMutation({
    mutationFn: (source: string) => threatIntelApi.cancelFeed(source),
    onSuccess: () => {
      setTimeout(() => qc.invalidateQueries({ queryKey: ['threat-intel', 'summary'] }), 3000)
    },
    onError: (err: any) => {
      if (err?.response?.status === 404) {
        setTimeout(() => qc.invalidateQueries({ queryKey: ['threat-intel', 'summary'] }), 1000)
      } else {
        setTriggerError(err?.response?.data?.detail ?? 'TI cancel failed')
      }
    },
  })

  const { data: iocStats } = useQuery({
    queryKey: ['threat-intel', 'ioc-stats'],
    queryFn: threatIntelApi.getIocStats,
    enabled: tiEnabled,
    staleTime: 5 * 60_000,
  })

  const { data: kevStats } =
    useQuery({ queryKey: ['feeds', 'kev', 'stats'], queryFn: feedsApi.getKevStats })

  const { data: attackStats } =
    useQuery({ queryKey: ['feeds', 'attack', 'stats'], queryFn: feedsApi.getAttackStats })

  const { data: recentKev } = useQuery({
    queryKey: ['feeds', 'kev', 'recent'],
    queryFn: () => feedsApi.getKev({ per_page: 10, page: 1 }),
  })

  const { data: auditReport, isLoading: auditLoading } = useQuery({
    queryKey: ['feeds', 'kev', 'audit', auditMonths],
    queryFn: () => feedsApi.getKevAuditReport(auditMonths),
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
      {triggerError && <Alert severity="error" sx={{ mb: 2 }} onClose={() => setTriggerError(null)}>{triggerError}</Alert>}

      {/* ── Feed status cards (tabbed) ── */}
      {(() => {
        const tiFeedItems: FeedStatusItem[] = tiEnabled && tiSummary
          ? tiSummary.sources.map(s => ({
              feed_name: s.source,
              display_name: s.display_name,
              enabled: s.enabled,
              last_run: s.last_run_at,
              last_status: s.last_run_status,
              item_count: s.ioc_count || null,
              error_message: null,
            }))
          : TI_FEED_DEFS.map(f => ({
              feed_name: f.feed_name, display_name: f.display_name,
              enabled: false, last_run: null, last_status: null, item_count: null, error_message: null,
            }))

        const TI_NAMES = new Set(TI_FEED_DEFS.map(f => f.feed_name))
        const regularFeeds = (status?.feeds ?? []).filter(f => !TI_NAMES.has(f.feed_name))

        function FeedCard({ feed, isTi = false, disabled = false }: { feed: FeedStatusItem; isTi?: boolean; disabled?: boolean }) {
          const card = (
            <Paper
              variant="outlined"
              sx={{ p: 2, borderRadius: 2, ...(disabled ? { opacity: 0.38 } : {}) }}
            >
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
                  {feed.item_count != null && feed.item_count > 0 && (
                    <Typography variant="caption" color="text.secondary">
                      {feed.item_count.toLocaleString()} items
                    </Typography>
                  )}
                  {feed.error_message && (
                    <Typography variant="caption" color="error.main" display="block" sx={{ mt: 0.25 }} noWrap>
                      {feed.error_message}
                    </Typography>
                  )}
                  {isAdmin && !disabled && (
                    <Box sx={{ mt: 1, display: 'flex', gap: 0.5, flexWrap: 'wrap' }}>
                      {!isTi && feed.last_status === 'running' ? (
                        <Tooltip title="Request cancellation of this feed">
                          <span>
                            <Button
                              size="small" variant="outlined" color="error"
                              startIcon={cancelMutation.isPending && cancelMutation.variables === feed.feed_name
                                ? <CircularProgress size={12} /> : <StopOutlined sx={{ fontSize: 14 }} />}
                              disabled={cancelMutation.isPending}
                              onClick={() => cancelMutation.mutate(feed.feed_name)}
                              sx={{ fontSize: '0.7rem', py: 0.25, px: 1, minWidth: 0 }}
                            >Stop</Button>
                          </span>
                        </Tooltip>
                      ) : isTi && feed.last_status === 'running' ? (
                        <Tooltip title="Request cancellation of this feed">
                          <span>
                            <Button
                              size="small" variant="outlined" color="error"
                              startIcon={tiCancelMutation.isPending && tiCancelMutation.variables === feed.feed_name
                                ? <CircularProgress size={12} /> : <StopOutlined sx={{ fontSize: 14 }} />}
                              disabled={tiCancelMutation.isPending}
                              onClick={() => tiCancelMutation.mutate(feed.feed_name)}
                              sx={{ fontSize: '0.7rem', py: 0.25, px: 1, minWidth: 0 }}
                            >Stop</Button>
                          </span>
                        </Tooltip>
                      ) : isTi ? (
                        <Tooltip title="Run feed now">
                          <span>
                            <Button
                              size="small" variant="outlined"
                              startIcon={tiTriggerMutation.isPending && tiTriggerMutation.variables === feed.feed_name
                                ? <CircularProgress size={12} /> : <PlayArrowOutlined sx={{ fontSize: 14 }} />}
                              disabled={tiTriggerMutation.isPending || feed.last_status === 'running'}
                              onClick={() => tiTriggerMutation.mutate(feed.feed_name)}
                              sx={{ fontSize: '0.7rem', py: 0.25, px: 1, minWidth: 0 }}
                            >Run</Button>
                          </span>
                        </Tooltip>
                      ) : (
                        <>
                          <Tooltip title={['nist_cve', 'euvd'].includes(feed.feed_name) ? 'Run delta update now' : 'Run feed now'}>
                            <span>
                              <Button
                                size="small" variant="outlined"
                                startIcon={triggerMutation.isPending && triggerMutation.variables?.feedName === feed.feed_name
                                  ? <CircularProgress size={12} /> : <PlayArrowOutlined sx={{ fontSize: 14 }} />}
                                disabled={triggerMutation.isPending}
                                onClick={() => triggerMutation.mutate({
                                  feedName: feed.feed_name,
                                  mode: ['nist_cve', 'euvd'].includes(feed.feed_name) ? 'delta' : undefined,
                                })}
                                sx={{ fontSize: '0.7rem', py: 0.25, px: 1, minWidth: 0 }}
                              >
                                {['nist_cve', 'euvd'].includes(feed.feed_name) ? 'Delta' : 'Run'}
                              </Button>
                            </span>
                          </Tooltip>
                          {['nist_cve', 'euvd'].includes(feed.feed_name) && (
                            <Tooltip title={feed.feed_name === 'nist_cve' ? 'Run full CVE pull (slow — 30-60 min)' : 'Run full EUVD pull (all entries)'}>
                              <span>
                                <Button
                                  size="small" variant="outlined" color="warning"
                                  disabled={triggerMutation.isPending}
                                  onClick={() => triggerMutation.mutate({ feedName: feed.feed_name, mode: 'full' })}
                                  sx={{ fontSize: '0.7rem', py: 0.25, px: 1, minWidth: 0 }}
                                >Full</Button>
                              </span>
                            </Tooltip>
                          )}
                        </>
                      )}
                    </Box>
                  )}
                </Box>
              </Box>
            </Paper>
          )
          if (disabled) {
            return (
              <Tooltip key={feed.feed_name} title="Activate with --profile threat-intel" placement="top">
                <span>{card}</span>
              </Tooltip>
            )
          }
          return <span key={feed.feed_name}>{card}</span>
        }

        return (
          <Box sx={{ mb: 3 }}>
            <Tabs
              value={feedTab}
              onChange={(_, v) => setFeedTab(v)}
              sx={{ mb: 2, borderBottom: 1, borderColor: 'divider', minHeight: 36 }}
              TabIndicatorProps={{ style: { height: 2 } }}
            >
              <Tab
                label={`Vulnerability Feeds (${regularFeeds.length})`}
                sx={{ fontSize: '0.82rem', minHeight: 36, textTransform: 'none', fontWeight: 600 }}
              />
              <Tab
                label={
                  <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.75 }}>
                    {`Threat Intelligence (${tiFeedItems.length})`}
                    {!tiEnabled && (
                      <Chip label="inactive" size="small" sx={{ fontSize: '0.62rem', height: 16, opacity: 0.6 }} />
                    )}
                  </Box>
                }
                sx={{ fontSize: '0.82rem', minHeight: 36, textTransform: 'none', fontWeight: 600 }}
              />
            </Tabs>

            {feedTab === 0 && (
              <Box sx={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(210px, 1fr))', gap: 2 }}>
                {regularFeeds.map(feed => <FeedCard key={feed.feed_name} feed={feed} />)}
                {!statusLoading && regularFeeds.length === 0 && (
                  <Alert severity="info" icon={<HourglassEmptyOutlined />} sx={{ gridColumn: '1 / -1' }}>
                    No feed data yet — the feeds container will populate data on its first run.
                  </Alert>
                )}
              </Box>
            )}

            {feedTab === 1 && (
              <Box>
                {!tiEnabled && (
                  <Alert severity="info" sx={{ mb: 2 }}>
                    Threat Intelligence feeds require <strong>--profile threat-intel</strong> to be active. Set <code>THREAT_INTEL_ENABLED=true</code> in your .env once the profile is running.
                  </Alert>
                )}
                <Box sx={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(210px, 1fr))', gap: 2 }}>
                  {tiFeedItems.map(feed => <FeedCard key={feed.feed_name} feed={feed} isTi={true} disabled={!tiEnabled} />)}
                </Box>
              </Box>
            )}
          </Box>
        )
      })()}

      {/* ── Feed settings (admin only, vuln tab) ── */}
      {feedTab === 0 && isAdmin && feedSettings !== undefined && (
        <Paper variant="outlined" sx={{ p: 2, borderRadius: 2, mb: 3, display: 'flex', alignItems: 'center', gap: 2, flexWrap: 'wrap' }}>
          <TuneOutlined sx={{ color: 'text.secondary', fontSize: 20 }} />
          <Typography variant="subtitle2" fontWeight={600} sx={{ mr: 1 }}>
            Feed Settings
          </Typography>
          <Tooltip title="Query NVD CPE API for KEV vendor/product names and index ~3-5K additional CPE entries into OpenSearch. Takes effect on the next scheduled run (Sunday 01:30 UTC).">
            <FormControlLabel
              control={
                <Switch
                  size="small"
                  checked={feedSettings.feeds_cpe_full}
                  disabled={settingsMutation.isPending}
                  onChange={e => settingsMutation.mutate({ feeds_cpe_full: e.target.checked })}
                />
              }
              label={
                <Typography variant="body2" sx={{ fontSize: '0.82rem' }}>
                  NVD CPE Option B (KEV-vendor)
                  <Typography component="span" variant="caption" color="text.secondary" sx={{ ml: 1 }}>
                    — queries CPE API for KEV vendors
                  </Typography>
                </Typography>
              }
            />
          </Tooltip>
          {settingsMutation.isSuccess && (
            <Typography variant="caption" color="success.main">Saved</Typography>
          )}
          {settingsMutation.isError && (
            <Typography variant="caption" color="error.main">Failed to save</Typography>
          )}
        </Paper>
      )}

      {/* ── Vuln charts + KEV tables (tab 0 only) ── */}
      {feedTab === 0 && <Box sx={{ display: 'flex', gap: 2, flexWrap: 'wrap', mb: 3 }}>

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
                  contentStyle={tooltipStyle}
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
                  contentStyle={tooltipStyle}
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
      </Box>}

      {feedTab === 0 && <>
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

      {/* ── A.8.8 KEV Audit Report ── */}
      <Paper variant="outlined" sx={{ borderRadius: 2, overflow: 'hidden', mt: 3 }}>
        <Box sx={{ px: 2, py: 1.5, borderBottom: '1px solid', borderColor: 'divider', display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: 1 }}>
          <Box>
            <Typography variant="subtitle2" fontWeight={600}>A.8.8 KEV Audit Report</Typography>
            <Typography variant="caption" color="text.secondary">
              CISA KEV entries with evidence status — exportable for audit evidence
            </Typography>
          </Box>
          <Box sx={{ display: 'flex', gap: 1, alignItems: 'center' }}>
            <FormControl size="small" sx={{ minWidth: 100 }}>
              <InputLabel sx={{ fontSize: '0.78rem' }}>Window</InputLabel>
              <Select value={auditMonths} label="Window" onChange={e => setAuditMonths(Number(e.target.value))} sx={{ fontSize: '0.78rem' }}>
                <MenuItem value={3} sx={{ fontSize: '0.78rem' }}>3 months</MenuItem>
                <MenuItem value={6} sx={{ fontSize: '0.78rem' }}>6 months</MenuItem>
                <MenuItem value={12} sx={{ fontSize: '0.78rem' }}>12 months</MenuItem>
                <MenuItem value={24} sx={{ fontSize: '0.78rem' }}>24 months</MenuItem>
              </Select>
            </FormControl>
            {auditReport && (
              <Button
                size="small"
                variant="outlined"
                startIcon={<DownloadOutlined sx={{ fontSize: 14 }} />}
                onClick={() => exportAuditCsv(auditReport.entries, auditMonths)}
                sx={{ fontSize: '0.75rem' }}
              >
                Export CSV
              </Button>
            )}
          </Box>
        </Box>

        {/* Summary row */}
        {auditReport && (
          <Box sx={{ display: 'flex', gap: 2, p: 2, flexWrap: 'wrap', borderBottom: '1px solid', borderColor: 'divider' }}>
            {[
              { label: 'Total KEV', value: auditReport.total, color: 'text.primary' },
              { label: 'With Evidence', value: auditReport.covered, color: isLight ? '#1b5e20' : '#C6EFCE' },
              { label: 'No Evidence', value: auditReport.uncovered, color: isLight ? '#9e0000' : '#FFC7CE' },
              { label: 'Ransomware / No Evidence', value: auditReport.ransomware_uncovered, color: isLight ? '#9e0000' : '#FFC7CE' },
            ].map(s => (
              <Box key={s.label} sx={{ textAlign: 'center', flex: '1 1 120px' }}>
                <Typography variant="h5" fontWeight={700} sx={{ color: s.color, lineHeight: 1.2 }}>{s.value}</Typography>
                <Typography variant="caption" color="text.secondary">{s.label}</Typography>
              </Box>
            ))}
          </Box>
        )}

        {auditLoading && <Box sx={{ p: 2 }}><CircularProgress size={18} /></Box>}

        {auditReport && auditReport.entries.length > 0 && (
          <Table size="small">
            <TableHead>
              <TableRow>
                <TableCell sx={{ fontWeight: 600, fontSize: '0.72rem' }}>CVE</TableCell>
                <TableCell sx={{ fontWeight: 600, fontSize: '0.72rem' }}>Vulnerability / Vendor</TableCell>
                <TableCell sx={{ fontWeight: 600, fontSize: '0.72rem' }}>Added</TableCell>
                <TableCell sx={{ fontWeight: 600, fontSize: '0.72rem' }}>Due</TableCell>
                <TableCell sx={{ fontWeight: 600, fontSize: '0.72rem' }}>Ransomware</TableCell>
                <TableCell sx={{ fontWeight: 600, fontSize: '0.72rem' }}>Evidence Status</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {auditReport.entries.map(entry => {
                const sc = AUDIT_STATUS_COLORS[entry.evidence_status] ?? { bg: '#1e1e2e', color: '#aaa', label: entry.evidence_status }
                return (
                  <TableRow key={entry.cve_id} hover>
                    <TableCell sx={{ fontSize: '0.75rem', fontFamily: 'monospace', color: '#c62828', fontWeight: 600, whiteSpace: 'nowrap' }}>
                      {entry.cve_id}
                    </TableCell>
                    <TableCell sx={{ fontSize: '0.75rem', maxWidth: 280 }}>
                      <Tooltip title={entry.vulnerability_name ?? ''}>
                        <Typography noWrap variant="inherit">{entry.vulnerability_name ?? '—'}</Typography>
                      </Tooltip>
                      <Typography variant="caption" color="text.secondary" noWrap display="block">
                        {entry.vendor_project} {entry.product ? `— ${entry.product}` : ''}
                      </Typography>
                    </TableCell>
                    <TableCell sx={{ fontSize: '0.75rem', whiteSpace: 'nowrap' }}>{entry.date_added ?? '—'}</TableCell>
                    <TableCell sx={{ fontSize: '0.75rem', whiteSpace: 'nowrap', color: entry.due_date ? (muiTheme.palette.mode === 'light' ? '#9a6500' : '#FFEB9C') : 'text.secondary' }}>{entry.due_date ?? '—'}</TableCell>
                    <TableCell>
                      {entry.known_ransomware
                        ? <Chip label="Yes" size="small" color="error" sx={{ fontSize: '0.68rem', height: 18 }} />
                        : <Typography variant="caption" color="text.disabled">No</Typography>}
                    </TableCell>
                    <TableCell>
                      {entry.evidence_title ? (
                        <Tooltip title={entry.evidence_title}>
                          <Chip label={sc.label} size="small" sx={{ fontSize: '0.68rem', height: 20, bgcolor: sc.bg, color: sc.color, border: `1px solid ${sc.color}40` }} />
                        </Tooltip>
                      ) : (
                        <Chip label={sc.label} size="small" sx={{ fontSize: '0.68rem', height: 20, bgcolor: sc.bg, color: sc.color, border: `1px solid ${sc.color}40` }} />
                      )}
                    </TableCell>
                  </TableRow>
                )
              })}
            </TableBody>
          </Table>
        )}

        {auditReport && auditReport.entries.length === 0 && (
          <Box sx={{ p: 3, textAlign: 'center' }}>
            <HourglassEmptyOutlined sx={{ fontSize: 32, color: 'text.disabled', mb: 1 }} />
            <Typography variant="body2" color="text.secondary">No KEV entries in the selected window</Typography>
          </Box>
        )}
      </Paper>
      </>}

      {/* ── TI charts (tab 1 only) ── */}
      {feedTab === 1 && iocStats && (
        <Box sx={{ display: 'flex', gap: 2, flexWrap: 'wrap', mt: 1 }}>

          {/* IOCs by source */}
          <Paper variant="outlined" sx={{ p: 2, borderRadius: 2, flex: '1 1 340px' }}>
            <Typography variant="subtitle2" fontWeight={600} sx={{ mb: 1.5 }}>IOCs by Source</Typography>
            <ResponsiveContainer width="100%" height={220}>
              <BarChart
                data={iocStats.source_totals.map(s => ({ name: s.source.replace(/_/g, ' ').replace('misp', 'MISP'), count: s.count }))}
                layout="vertical" barSize={10}
              >
                <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.05)" />
                <XAxis type="number" tick={{ fontSize: 10 }} />
                <YAxis dataKey="name" type="category" tick={{ fontSize: 10 }} width={110} />
                <ChartTooltip contentStyle={tooltipStyle} />
                <Bar dataKey="count" radius={[0, 2, 2, 0]}>
                  {iocStats.source_totals.map((_, i) => (
                    <Cell key={i} fill={TACTIC_COLORS[i % TACTIC_COLORS.length]} />
                  ))}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </Paper>

          {/* IOC type breakdown */}
          <Paper variant="outlined" sx={{ p: 2, borderRadius: 2, flex: '1 1 260px' }}>
            <Typography variant="subtitle2" fontWeight={600} sx={{ mb: 1.5 }}>IOC Types</Typography>
            <ResponsiveContainer width="100%" height={220}>
              <BarChart
                data={iocStats.type_breakdown.map(t => ({ name: t.type, count: t.count }))}
                layout="vertical" barSize={14}
              >
                <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.05)" />
                <XAxis type="number" tick={{ fontSize: 10 }} />
                <YAxis dataKey="name" type="category" tick={{ fontSize: 10, fontFamily: 'monospace' }} width={50} />
                <ChartTooltip contentStyle={tooltipStyle} />
                <Bar dataKey="count" radius={[0, 2, 2, 0]}>
                  {iocStats.type_breakdown.map((_, i) => (
                    <Cell key={i} fill={TACTIC_COLORS[i % TACTIC_COLORS.length]} />
                  ))}
                </Bar>
              </BarChart>
            </ResponsiveContainer>
          </Paper>

          {/* Top malware families */}
          {iocStats.top_families.length > 0 && (
            <Paper variant="outlined" sx={{ p: 2, borderRadius: 2, flex: '1 1 340px' }}>
              <Typography variant="subtitle2" fontWeight={600} sx={{ mb: 1.5 }}>Top Malware Families</Typography>
              <ResponsiveContainer width="100%" height={220}>
                <BarChart
                  data={iocStats.top_families.map(f => ({ name: f.family.replace(/_/g, ' '), count: f.count }))}
                  layout="vertical" barSize={10}
                >
                  <CartesianGrid strokeDasharray="3 3" stroke="rgba(255,255,255,0.05)" />
                  <XAxis type="number" tick={{ fontSize: 10 }} />
                  <YAxis dataKey="name" type="category" tick={{ fontSize: 10 }} width={120} />
                  <ChartTooltip contentStyle={tooltipStyle} />
                  <Bar dataKey="count" fill="#b71c1c" radius={[0, 2, 2, 0]} />
                </BarChart>
              </ResponsiveContainer>
            </Paper>
          )}
        </Box>
      )}
    </Box>
  )
}
