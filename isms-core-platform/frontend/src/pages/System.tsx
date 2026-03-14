import { useState } from 'react'
import {
  Box,
  Button,
  Card,
  CardContent,
  Typography,
  Chip,
  Grid,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Divider,
  IconButton,
  Tooltip,
  CircularProgress,
  Alert,
  TextField,
  Select,
  MenuItem,
  FormControl,
  InputLabel,
} from '@mui/material'
import {
  CheckCircleOutlined,
  ErrorOutlined,
  HelpOutlineOutlined,
  RefreshOutlined,
  StorageOutlined,
  SettingsOutlined,
  SyncAltOutlined,
  CloudSyncOutlined,
  DeleteSweepOutlined,
  DownloadingOutlined,
  SyncOutlined,
  EmailOutlined,
  SendOutlined,
  PsychologyOutlined,
  AssignmentOutlined,
} from '@mui/icons-material'
import { useQuery, useMutation } from '@tanstack/react-query'
import dayjs from 'dayjs'
import relativeTime from 'dayjs/plugin/relativeTime'
import { adminApi } from '../api/admin'
import type { OrphanEntry } from '../api/admin'
import type { ServiceHealth } from '../api/types'
import PageHeader from '../components/PageHeader'

dayjs.extend(relativeTime)

const SERVICE_LABELS: Record<string, string> = {
  api: 'API',
  database: 'PostgreSQL',
  redis: 'Redis',
  celery: 'Celery Worker',
  opensearch: 'OpenSearch',
}

const DB_COUNT_LABELS: Record<string, string> = {
  control_groups: 'Control Groups',
  frameworks: 'Frameworks',
  framework_controls: 'Framework Controls',
  cross_framework_mappings: 'Cross-Framework Mappings',
  policies: 'Policies',
  requirements: 'Requirements',
  implementations: 'Implementations',
  assessments: 'Assessments',
  evidence: 'Evidence Items',
  automated_evidence: 'Automated Evidence',
  gaps: 'Gaps',
  users: 'Users',
  load_history_count: 'Load History Events',
}

function ServiceCard({ svc }: { svc: ServiceHealth }) {
  const isOk = svc.status === 'ok'
  const isError = svc.status === 'error'

  const Icon = isOk ? CheckCircleOutlined : isError ? ErrorOutlined : HelpOutlineOutlined
  const iconColor = isOk ? '#C6EFCE' : isError ? '#FFC7CE' : '#FFEB9C'
  const bgColor = isOk
    ? 'rgba(198,239,206,0.08)'
    : isError
    ? 'rgba(255,199,206,0.08)'
    : 'rgba(255,235,156,0.08)'
  const chipBg = isOk ? '#1a3a27' : isError ? '#3a0000' : '#3a2e00'
  const chipFg = isOk ? '#C6EFCE' : isError ? '#FFC7CE' : '#FFEB9C'

  return (
    <Card sx={{ bgcolor: bgColor, border: '1px solid', borderColor: isOk ? 'rgba(198,239,206,0.15)' : isError ? 'rgba(255,199,206,0.15)' : 'rgba(255,235,156,0.15)' }}>
      <CardContent sx={{ pb: '12px !important' }}>
        <Box sx={{ display: 'flex', alignItems: 'flex-start', justifyContent: 'space-between', mb: 1 }}>
          <Icon sx={{ color: iconColor, fontSize: 28 }} />
          <Chip
            label={svc.status}
            size="small"
            sx={{ fontSize: '0.65rem', height: 18, bgcolor: chipBg, color: chipFg }}
          />
        </Box>
        <Typography variant="body2" fontWeight={600} sx={{ mb: 0.25 }}>
          {SERVICE_LABELS[svc.name] ?? svc.name}
        </Typography>
        {svc.latency_ms != null && (
          <Typography variant="caption" color="text.secondary">
            {svc.latency_ms} ms
          </Typography>
        )}
        {svc.detail && (
          <Typography variant="caption" color="text.secondary" display="block" sx={{ mt: 0.25, opacity: 0.7 }}>
            {svc.detail}
          </Typography>
        )}
      </CardContent>
    </Card>
  )
}

export default function System() {
  const [lastRefresh, setLastRefresh] = useState<Date>(new Date())
  const [reindexResult, setReindexResult] = useState<string | null>(null)
  const [testEmailRecipient, setTestEmailRecipient] = useState('')
  const [testEmailResult, setTestEmailResult] = useState<{ ok: boolean; msg: string } | null>(null)
  const [orphanResult, setOrphanResult] = useState<{ implementations: OrphanEntry[]; policies: OrphanEntry[] } | null>(null)
  const [purgeResult, setPurgeResult] = useState<string | null>(null)
  const [syncResult, setSyncResult] = useState<{ ok: boolean; msg: string } | null>(null)
  const [aiModelResult, setAiModelResult] = useState<{ ok: boolean; msg: string } | null>(null)
  const [importResults, setImportResults] = useState<Record<string, { ok: boolean; msg: string } | null>>({
    frameworks: null,
    policies: null,
    implementations: null,
    workbooks: null,
    operational: null,
    fullSync: null,
  })

  const reindexMutation = useMutation({
    mutationFn: adminApi.reindexOpenSearch,
    onSuccess: (data) => {
      const s = data.stats
      setReindexResult(`Reindex complete — ${s.implementations} implementations, ${s.policies} policies indexed.${s.errors ? ` ${s.errors} errors.` : ''}`)
    },
  })

  const scanOrphansMutation = useMutation({
    mutationFn: adminApi.scanOrphans,
    onSuccess: (data) => {
      setOrphanResult({ implementations: data.implementations, policies: data.policies })
      setPurgeResult(null)
    },
  })

  const purgeOrphansMutation = useMutation({
    mutationFn: adminApi.purgeOrphans,
    onSuccess: (data) => {
      const d = data.deleted
      setPurgeResult(`Purged ${d.implementations} implementations + ${d.policies} policies.`)
      setOrphanResult(null)
    },
  })

  const { data, isLoading, error, refetch, isFetching } = useQuery({
    queryKey: ['admin', 'sysinfo'],
    queryFn: adminApi.getSysInfo,
    refetchInterval: 30_000,
    staleTime: 25_000,
  })

  const { data: sysLogs, refetch: refetchLogs } = useQuery({
    queryKey: ['admin', 'system-logs'],
    queryFn: () => adminApi.getAuditLog({ category: 'system', page_size: 30 }),
    refetchInterval: 60_000,
    staleTime: 55_000,
  })

  function setImportResult(key: string, ok: boolean, msg: string) {
    setImportResults((prev) => ({ ...prev, [key]: { ok, msg } }))
    refetch()
  }

  const loadFrameworksMutation = useMutation({
    mutationFn: adminApi.loadFrameworkBundles,
    onSuccess: () => setImportResult('frameworks', true, 'Framework bundles loaded successfully.'),
    onError: () => setImportResult('frameworks', false, 'Failed — check server logs.'),
  })

  const importPoliciesMutation = useMutation({
    mutationFn: adminApi.importPolicies,
    onSuccess: (data) => {
      const s = data.stats
      const imported = s?.imported ?? s?.policies ?? ''
      setImportResult('policies', true, `Policies imported.${imported !== '' ? ` (${imported} records)` : ''}`)
    },
    onError: () => setImportResult('policies', false, 'Failed — check server logs.'),
  })

  const importImpsMutation = useMutation({
    mutationFn: adminApi.importImplementations,
    onSuccess: (data) => {
      const s = data.stats
      const imported = s?.imported ?? s?.implementations ?? ''
      setImportResult('implementations', true, `Implementations imported.${imported !== '' ? ` (${imported} records)` : ''}`)
    },
    onError: () => setImportResult('implementations', false, 'Failed — check server logs.'),
  })

  const importWorkbooksMutation = useMutation({
    mutationFn: adminApi.importWorkbooks,
    onSuccess: (data) => {
      const s = data.stats
      const imported = s?.imported ?? s?.assessments ?? ''
      setImportResult('workbooks', true, `Workbook structures imported.${imported !== '' ? ` (${imported} records)` : ''}`)
    },
    onError: () => setImportResult('workbooks', false, 'Failed — check server logs.'),
  })

  const importOperationalMutation = useMutation({
    mutationFn: adminApi.importOperational,
    onSuccess: (data) => {
      const s = data.stats
      const imported = s?.imported ?? s?.assessments ?? ''
      setImportResult('operational', true, `Operational checklists imported.${imported !== '' ? ` (${imported} records)` : ''}`)
    },
    onError: () => setImportResult('operational', false, 'Failed — check server logs.'),
  })

  const fullSyncMutation = useMutation({
    mutationFn: adminApi.syncFull,
    onSuccess: () => setImportResult('fullSync', true, 'Full sync complete — all importers ran successfully.'),
    onError: () => setImportResult('fullSync', false, 'Full sync failed — check server logs.'),
  })

  const syncNowMutation = useMutation({
    mutationFn: adminApi.syncFull,
    onSuccess: () => { setSyncResult({ ok: true, msg: 'Sync complete — all importers ran successfully.' }); refetch() },
    onError: () => setSyncResult({ ok: false, msg: 'Sync failed — check server logs.' }),
  })

  const syncBackgroundMutation = useMutation({
    mutationFn: adminApi.syncAsync,
    onSuccess: (data) => setSyncResult({ ok: true, msg: `Background sync queued. Task ID: ${data.task_id}` }),
    onError: () => setSyncResult({ ok: false, msg: 'Failed to queue background sync.' }),
  })

  const testEmailMutation = useMutation({
    mutationFn: () => adminApi.sendTestEmail(testEmailRecipient),
    onSuccess: (data) => setTestEmailResult({ ok: true, msg: `Test email sent to ${data.recipient}. Check your Mailpit inbox.` }),
    onError: (e: { response?: { data?: { detail?: string } } }) =>
      setTestEmailResult({ ok: false, msg: e?.response?.data?.detail ?? 'Send failed — check server logs.' }),
  })

  const updateAiModelMutation = useMutation({
    mutationFn: async (model: string) => {
      const org = await adminApi.getOrganisation()
      const merged = { ...(org.settings ?? {}), ai_model: model }
      return adminApi.patchOrganisationSettings(merged)
    },
    onSuccess: (_, model) => {
      setAiModelResult({ ok: true, msg: `Model updated to ${model}.` })
      refetch()
    },
    onError: () => setAiModelResult({ ok: false, msg: 'Failed to update model — check server logs.' }),
  })

  const resetContentMutation = useMutation({
    mutationFn: adminApi.resetContent,
    onSuccess: (data) => {
      const del = data.deleted
      const pol = (data.reimport?.policies as { imported?: number })?.imported ?? '?'
      const imp = (data.reimport?.implementations as { imported?: number })?.imported ?? '?'
      const wkbk = (data.reimport?.workbooks as { imported?: number })?.imported ?? '?'
      setSyncResult({
        ok: true,
        msg: `Reset complete. Deleted: ${del.policies ?? 0} POLs, ${del.implementations ?? 0} IMPs, ${del.assessments ?? 0} assessments. Re-imported: ${pol} POLs, ${imp} IMPs, ${wkbk} workbooks.`,
      })
      refetch()
    },
    onError: () => setSyncResult({ ok: false, msg: 'Reset failed — check server logs.' }),
  })

  function handleResetContent() {
    if (!window.confirm(
      'This will DELETE all imported policies, implementations, assessments and QA results, then re-import from source files.\n\nControl groups, framework data, users, evidence and gaps are NOT affected.\n\nProceed?'
    )) return
    setSyncResult(null)
    resetContentMutation.mutate()
  }

  function handleRefresh() {
    refetch()
    refetchLogs()
    setLastRefresh(new Date())
  }

  return (
    <Box>
      <PageHeader
        title="System Status"
        subtitle="Service health, database counts, and platform configuration"
        actions={
          <Box sx={{ display: 'flex', alignItems: 'center', gap: 1.5 }}>
            <Typography variant="caption" color="text.secondary">
              {data
                ? `Updated ${dayjs(data.generated_at).fromNow()}`
                : `Refreshed ${dayjs(lastRefresh).fromNow()}`}
            </Typography>
            <Tooltip title="Refresh">
              <IconButton size="small" onClick={handleRefresh} disabled={isFetching}>
                {isFetching ? (
                  <CircularProgress size={16} />
                ) : (
                  <RefreshOutlined fontSize="small" />
                )}
              </IconButton>
            </Tooltip>
          </Box>
        }
      />

      {error && <Alert severity="error" sx={{ mb: 2 }}>Failed to load system info.</Alert>}
      {reindexResult && <Alert severity="success" onClose={() => setReindexResult(null)} sx={{ mb: 2 }}>{reindexResult}</Alert>}
      {reindexMutation.isError && <Alert severity="error" sx={{ mb: 2 }}>Reindex failed — check server logs.</Alert>}

      {isLoading && (
        <Box sx={{ display: 'flex', justifyContent: 'center', py: 6 }}>
          <CircularProgress />
        </Box>
      )}

      {data && (
        <Box sx={{ display: 'flex', flexDirection: 'column', gap: 2 }}>

          {/* Row 1: Service Health */}
          <Grid container spacing={1.5}>
            {data.services.map((svc) => (
              <Grid item xs={12} sm={6} md={4} lg={2.4} key={svc.name}>
                <ServiceCard svc={svc} />
              </Grid>
            ))}
          </Grid>

          {/* Row 2: Data State — DB Records (left) | OpenSearch + Platform Config (right) */}
          <Grid container spacing={2}>
            <Grid item xs={12} md={6}>
              <Box sx={{ display: 'flex', flexDirection: 'column', gap: 2, height: '100%' }}>

                {/* Database Records */}
                <Card>
                  <CardContent sx={{ pb: '12px !important' }}>
                    <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 2 }}>
                      <StorageOutlined sx={{ color: 'primary.main' }} />
                      <Typography variant="h6">Database Records</Typography>
                    </Box>
                    <TableContainer>
                      <Table size="small">
                        <TableBody>
                          {Object.entries(DB_COUNT_LABELS).map(([key, label]) => {
                            const val = data.db_counts[key as keyof typeof data.db_counts]
                            return (
                              <TableRow key={key} hover>
                                <TableCell>
                                  <Typography variant="body2" color="text.secondary">{label}</Typography>
                                </TableCell>
                                <TableCell align="right">
                                  <Typography variant="body2" fontWeight={600} fontFamily="monospace">
                                    {val.toLocaleString()}
                                  </Typography>
                                </TableCell>
                              </TableRow>
                            )
                          })}
                        </TableBody>
                      </Table>
                    </TableContainer>
                  </CardContent>
                </Card>

                {/* Last Data Load */}
                <Card>
                  <CardContent sx={{ pb: '12px !important' }}>
                    <Typography variant="h6" gutterBottom>Last Data Load</Typography>
                    <Divider sx={{ mb: 1.5 }} />
                    {data.last_sync_at ? (
                      <>
                        <Box sx={{ display: 'flex', justifyContent: 'space-between', mb: 0.75 }}>
                          <Typography variant="body2" color="text.secondary">Type</Typography>
                          <Typography variant="body2" fontFamily="monospace">
                            {data.last_sync_type ?? '—'}
                          </Typography>
                        </Box>
                        <Box sx={{ display: 'flex', justifyContent: 'space-between', mb: 0.75 }}>
                          <Typography variant="body2" color="text.secondary">Status</Typography>
                          <Chip
                            label={data.last_sync_status ?? '—'}
                            size="small"
                            sx={{
                              fontSize: '0.65rem',
                              height: 18,
                              bgcolor: data.last_sync_status === 'success' ? '#1a3a27' : '#3a0000',
                              color: data.last_sync_status === 'success' ? '#C6EFCE' : '#FFC7CE',
                            }}
                          />
                        </Box>
                        <Box sx={{ display: 'flex', justifyContent: 'space-between' }}>
                          <Typography variant="body2" color="text.secondary">At</Typography>
                          <Typography variant="body2">
                            {dayjs(data.last_sync_at).format('DD MMM YYYY HH:mm')} UTC
                          </Typography>
                        </Box>
                      </>
                    ) : (
                      <Typography variant="body2" color="text.secondary">No data loads recorded.</Typography>
                    )}
                  </CardContent>
                </Card>

                {/* Platform Configuration */}
                <Card>
                  <CardContent sx={{ pb: '12px !important' }}>
                    <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 1.5 }}>
                      <SettingsOutlined sx={{ color: 'primary.main' }} />
                      <Typography variant="h6">Platform Configuration</Typography>
                    </Box>
                    <Divider sx={{ mb: 1.5 }} />
                    {[
                      { label: 'Platform', value: data.platform },
                      { label: 'API Version', value: data.api_version },
                      { label: 'ISMS', value: 'ISO/IEC 27001:2022 + Amd. 1:2024', highlight: true },
                      { label: 'Privacy', value: 'ISO/IEC 27701:2025', highlight: true },
                      { label: 'Cloud', value: 'ISO/IEC 27018:2025', highlight: true },
                      { label: 'Framework Path', value: data.framework_path },
                      { label: 'Operational Path', value: data.operational_path },
                      ...(data.privacy_path ? [{ label: 'Privacy Path', value: data.privacy_path }] : []),
                      ...(data.cloud_path ? [{ label: 'Cloud Path', value: data.cloud_path }] : []),
                      { label: 'OpenSearch URL', value: data.opensearch_url },
                    ].map(({ label, value, highlight }) => (
                      <Box key={label} sx={{ display: 'flex', justifyContent: 'space-between', mb: 0.75, gap: 2 }}>
                        <Typography variant="body2" color="text.secondary" sx={{ flexShrink: 0 }}>
                          {label}
                        </Typography>
                        <Typography
                          variant="body2"
                          fontFamily="monospace"
                          sx={{ fontSize: '0.75rem', textAlign: 'right', wordBreak: 'break-all', color: highlight ? 'primary.light' : 'text.primary' }}
                        >
                          {value}
                        </Typography>
                      </Box>
                    ))}
                  </CardContent>
                </Card>

              </Box>
            </Grid>

            <Grid item xs={12} md={6}>
              <Box sx={{ display: 'flex', flexDirection: 'column', gap: 2 }}>

                {/* OpenSearch */}
                <Card>
                  <CardContent sx={{ pb: '12px !important' }}>
                    <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 1.5, flexWrap: 'wrap' }}>
                      <SyncAltOutlined sx={{ color: 'primary.main' }} />
                      <Typography variant="h6" sx={{ flex: 1 }}>OpenSearch</Typography>
                      <Tooltip title="Re-parse all IMP/POL files and push to OpenSearch. Fixes 'needs review' on keyword checks.">
                        <Button
                          size="small"
                          variant="outlined"
                          startIcon={reindexMutation.isPending ? <CircularProgress size={12} /> : <CloudSyncOutlined />}
                          disabled={reindexMutation.isPending}
                          onClick={() => { setReindexResult(null); reindexMutation.mutate() }}
                          sx={{ fontSize: '0.7rem', ml: 'auto' }}
                        >
                          {reindexMutation.isPending ? 'Reindexing…' : 'Reindex'}
                        </Button>
                      </Tooltip>
                      {data.opensearch_cluster_status && (
                        <Chip
                          label={data.opensearch_cluster_status}
                          size="small"
                          sx={{
                            fontSize: '0.65rem',
                            height: 18,
                            bgcolor:
                              data.opensearch_cluster_status === 'green' ? '#1a3a27'
                              : data.opensearch_cluster_status === 'yellow' ? '#3a2e00'
                              : '#3a0000',
                            color:
                              data.opensearch_cluster_status === 'green' ? '#C6EFCE'
                              : data.opensearch_cluster_status === 'yellow' ? '#FFEB9C'
                              : '#FFC7CE',
                          }}
                        />
                      )}
                    </Box>
                    {data.opensearch_indices ? (
                      <TableContainer>
                        <Table size="small">
                          <TableHead>
                            <TableRow>
                              <TableCell>Index</TableCell>
                              <TableCell align="right">Documents</TableCell>
                            </TableRow>
                          </TableHead>
                          <TableBody>
                            {Object.entries(data.opensearch_indices).map(([idx, count]) => (
                              <TableRow key={idx} hover>
                                <TableCell>
                                  <Typography variant="caption" fontFamily="monospace">{idx}</Typography>
                                </TableCell>
                                <TableCell align="right">
                                  <Typography variant="body2" fontWeight={600} fontFamily="monospace">
                                    {count?.toLocaleString() ?? '—'}
                                  </Typography>
                                </TableCell>
                              </TableRow>
                            ))}
                          </TableBody>
                        </Table>
                      </TableContainer>
                    ) : (
                      <Typography variant="body2" color="text.secondary">Unavailable</Typography>
                    )}
                  </CardContent>
                </Card>

                {/* SMTP Configuration */}
                <Card>
                  <CardContent sx={{ pb: '12px !important' }}>
                    <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 1.5 }}>
                      <EmailOutlined sx={{ color: 'primary.main' }} />
                      <Typography variant="h6" sx={{ flex: 1 }}>Email (SMTP)</Typography>
                      <Chip
                        label={data.smtp_enabled ? 'enabled' : 'disabled'}
                        size="small"
                        sx={{
                          fontSize: '0.65rem',
                          height: 18,
                          bgcolor: data.smtp_enabled ? '#1a3a27' : '#3a0000',
                          color: data.smtp_enabled ? '#C6EFCE' : '#FFC7CE',
                        }}
                      />
                    </Box>
                    <Divider sx={{ mb: 1.5 }} />
                    {[
                      { label: 'Host', value: data.smtp_host || '— not configured —' },
                      { label: 'Port', value: String(data.smtp_port) },
                      { label: 'From', value: data.smtp_from },
                      { label: 'Platform URL', value: data.platform_url },
                    ].map(({ label, value }) => (
                      <Box key={label} sx={{ display: 'flex', justifyContent: 'space-between', mb: 0.75, gap: 2 }}>
                        <Typography variant="body2" color="text.secondary" sx={{ flexShrink: 0 }}>{label}</Typography>
                        <Typography
                          variant="body2"
                          fontFamily="monospace"
                          sx={{ fontSize: '0.75rem', textAlign: 'right', wordBreak: 'break-all', color: 'text.primary' }}
                        >
                          {value}
                        </Typography>
                      </Box>
                    ))}

                    {data.smtp_enabled && (
                      <>
                        <Divider sx={{ my: 1.5 }} />
                        {testEmailResult && (
                          <Alert
                            severity={testEmailResult.ok ? 'success' : 'error'}
                            onClose={() => setTestEmailResult(null)}
                            sx={{ mb: 1.5, py: 0, fontSize: '0.72rem' }}
                          >
                            {testEmailResult.msg}
                          </Alert>
                        )}
                        <Box sx={{ display: 'flex', gap: 1, alignItems: 'flex-start' }}>
                          <TextField
                            size="small"
                            placeholder="recipient@example.com"
                            value={testEmailRecipient}
                            onChange={(e) => setTestEmailRecipient(e.target.value)}
                            onKeyDown={(e) => {
                              if (e.key === 'Enter' && testEmailRecipient.trim()) {
                                setTestEmailResult(null)
                                testEmailMutation.mutate()
                              }
                            }}
                            sx={{ flex: 1, '& .MuiInputBase-input': { fontSize: '0.8rem' } }}
                          />
                          <Tooltip title="Send a test email to verify SMTP is working">
                            <span>
                              <Button
                                size="small"
                                variant="outlined"
                                startIcon={testEmailMutation.isPending ? <CircularProgress size={12} /> : <SendOutlined />}
                                disabled={testEmailMutation.isPending || !testEmailRecipient.trim()}
                                onClick={() => { setTestEmailResult(null); testEmailMutation.mutate() }}
                                sx={{ fontSize: '0.7rem', whiteSpace: 'nowrap' }}
                              >
                                {testEmailMutation.isPending ? 'Sending…' : 'Send Test'}
                              </Button>
                            </span>
                          </Tooltip>
                        </Box>
                        <Typography variant="caption" color="text.secondary" display="block" sx={{ mt: 0.75 }}>
                          Delivered to Mailpit — <a href="http://localhost:8025" target="_blank" rel="noreferrer" style={{ color: 'inherit' }}>http://localhost:8025</a>
                        </Typography>
                      </>
                    )}
                  </CardContent>
                </Card>

                {/* AI Compass Configuration */}
                <Card>
                  <CardContent sx={{ pb: '12px !important' }}>
                    <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 1.5 }}>
                      <PsychologyOutlined sx={{ color: 'primary.main' }} />
                      <Typography variant="h6" sx={{ flex: 1 }}>AI Compass</Typography>
                    </Box>
                    <Divider sx={{ mb: 1.5 }} />
                    <Box sx={{ display: 'flex', justifyContent: 'space-between', mb: 1.5, gap: 2, alignItems: 'center' }}>
                      <Typography variant="body2" color="text.secondary" sx={{ flexShrink: 0 }}>Active Model</Typography>
                      <Typography variant="body2" fontFamily="monospace" sx={{ fontSize: '0.75rem', textAlign: 'right', wordBreak: 'break-all' }}>
                        {data.ai_model || '—'}
                      </Typography>
                    </Box>
                    <Divider sx={{ mb: 1.5 }} />
                    {aiModelResult && (
                      <Alert
                        severity={aiModelResult.ok ? 'success' : 'error'}
                        onClose={() => setAiModelResult(null)}
                        sx={{ mb: 1.5, py: 0, fontSize: '0.72rem' }}
                      >
                        {aiModelResult.msg}
                      </Alert>
                    )}
                    <FormControl fullWidth size="small">
                      <InputLabel sx={{ fontSize: '0.8rem' }}>Select Model</InputLabel>
                      <Select
                        label="Select Model"
                        value={data.ai_model || ''}
                        onChange={(e) => {
                          setAiModelResult(null)
                          updateAiModelMutation.mutate(e.target.value)
                        }}
                        disabled={updateAiModelMutation.isPending}
                        sx={{ fontSize: '0.8rem' }}
                      >
                        <MenuItem value="claude-haiku-4-5-20251001" sx={{ fontSize: '0.8rem' }}>
                          Haiku 4.5 — Fast &amp; economical
                        </MenuItem>
                        <MenuItem value="claude-sonnet-4-6" sx={{ fontSize: '0.8rem' }}>
                          Sonnet 4.6 — Balanced (recommended)
                        </MenuItem>
                        <MenuItem value="claude-opus-4-6" sx={{ fontSize: '0.8rem' }}>
                          Opus 4.6 — Most capable
                        </MenuItem>
                      </Select>
                    </FormControl>
                    <Typography variant="caption" color="text.secondary" display="block" sx={{ mt: 0.75 }}>
                      Applies to ISMS Compass gap analysis. Requires ANTHROPIC_API_KEY in platform/.env.
                    </Typography>
                  </CardContent>
                </Card>

              </Box>
            </Grid>
          </Grid>

          {/* Row 3: Data Management — First-Run Setup (left) | Ongoing Sync + Orphan Scanner (right) */}
          <Grid container spacing={2}>
            <Grid item xs={12} md={6}>
              <Card sx={{ height: '100%' }}>
                <CardContent sx={{ pb: '12px !important' }}>
                  <Box sx={{ display: 'flex', alignItems: 'flex-start', gap: 1, mb: 0.5 }}>
                    <DownloadingOutlined sx={{ color: 'primary.main', mt: 0.25 }} />
                    <Box>
                      <Typography variant="h6">First-Run Setup</Typography>
                      <Typography variant="caption" color="text.secondary">
                        Run steps 1–5 in order on first boot. Use Full Sync to re-run all importers at once.
                      </Typography>
                    </Box>
                  </Box>
                  <Divider sx={{ my: 1.5 }} />

                  {importResults.fullSync && (
                    <Alert
                      severity={importResults.fullSync.ok ? 'success' : 'error'}
                      onClose={() => setImportResults((p) => ({ ...p, fullSync: null }))}
                      sx={{ mb: 1.5, py: 0 }}
                    >
                      {importResults.fullSync.msg}
                    </Alert>
                  )}

                  {([
                    {
                      key: 'frameworks',
                      label: 'Load Reference Frameworks',
                      desc: '18 bundles — ISO 27001, NIST CSF 2.0, MITRE ATT\u0026CK, GDPR, DORA, NIS2 and more.',
                      mutation: loadFrameworksMutation,
                    },
                    {
                      key: 'policies',
                      label: 'Import Policies',
                      desc: 'POL, OP-POL, PRIV-POL, CLD-POL, REF, CTX, FORM documents from the mounted content volumes.',
                      mutation: importPoliciesMutation,
                    },
                    {
                      key: 'implementations',
                      label: 'Import Implementations (IMP)',
                      desc: 'IMP-UG / IMP-TG documents — also indexed to OpenSearch for full-text search.',
                      mutation: importImpsMutation,
                    },
                    {
                      key: 'workbooks',
                      label: 'Import Assessment Workbooks',
                      desc: 'Framework assessment workbook structures parsed from generator scripts.',
                      mutation: importWorkbooksMutation,
                    },
                    {
                      key: 'operational',
                      label: 'Import Operational Checklists',
                      desc: 'Operational compliance checklist structures.',
                      mutation: importOperationalMutation,
                    },
                  ] as const).map(({ key, label, desc, mutation }) => (
                    <Box key={key} sx={{ display: 'flex', alignItems: 'flex-start', gap: 1.5, mb: 1.5 }}>
                      <Box sx={{ flex: 1, minWidth: 0 }}>
                        <Typography variant="body2" fontWeight={600}>{label}</Typography>
                        <Typography variant="caption" color="text.secondary" display="block" sx={{ mb: 0.5 }}>
                          {desc}
                        </Typography>
                        {importResults[key] && (
                          <Alert
                            severity={importResults[key]!.ok ? 'success' : 'error'}
                            onClose={() => setImportResults((p) => ({ ...p, [key]: null }))}
                            sx={{ py: 0, fontSize: '0.72rem' }}
                          >
                            {importResults[key]!.msg}
                          </Alert>
                        )}
                      </Box>
                      <Button
                        size="small"
                        variant="outlined"
                        startIcon={mutation.isPending ? <CircularProgress size={10} /> : undefined}
                        disabled={mutation.isPending || fullSyncMutation.isPending}
                        onClick={() => {
                          setImportResults((p) => ({ ...p, [key]: null }))
                          mutation.mutate()
                        }}
                        sx={{ fontSize: '0.7rem', flexShrink: 0, mt: 0.25 }}
                      >
                        {mutation.isPending ? 'Running…' : 'Run'}
                      </Button>
                    </Box>
                  ))}

                  <Divider sx={{ mb: 1.5 }} />

                  <Button
                    fullWidth
                    variant="contained"
                    startIcon={fullSyncMutation.isPending ? <CircularProgress size={14} sx={{ color: 'inherit' }} /> : <SyncAltOutlined />}
                    disabled={fullSyncMutation.isPending || loadFrameworksMutation.isPending || importPoliciesMutation.isPending || importImpsMutation.isPending || importWorkbooksMutation.isPending || importOperationalMutation.isPending}
                    onClick={() => {
                      setImportResults((p) => ({ ...p, fullSync: null }))
                      fullSyncMutation.mutate()
                    }}
                  >
                    {fullSyncMutation.isPending ? 'Running Full Sync…' : 'Full Sync (Steps 2–5)'}
                  </Button>
                  <Typography variant="caption" color="text.secondary" display="block" sx={{ mt: 0.75, textAlign: 'center' }}>
                    Runs all four importers in sequence. Load Reference Frameworks (Step 1) must be done separately first.
                  </Typography>
                </CardContent>
              </Card>
            </Grid>

            <Grid item xs={12} md={6}>
              <Box sx={{ display: 'flex', flexDirection: 'column', gap: 2 }}>

                {/* Data Synchronisation */}
                <Card>
                  <CardContent sx={{ pb: '12px !important' }}>
                    <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 1.5 }}>
                      <SyncOutlined sx={{ color: 'primary.main' }} />
                      <Box>
                        <Typography variant="h6">Data Synchronisation</Typography>
                        <Typography variant="caption" color="text.secondary">
                          Re-sync content from mounted volumes after updating policies, IMPs, or workbooks.
                        </Typography>
                      </Box>
                    </Box>
                    <Divider sx={{ mb: 1.5 }} />

                    {syncResult && (
                      <Alert
                        severity={syncResult.ok ? 'success' : 'error'}
                        onClose={() => setSyncResult(null)}
                        sx={{ mb: 1.5, py: 0 }}
                      >
                        {syncResult.msg}
                      </Alert>
                    )}

                    <Box sx={{ display: 'flex', gap: 1.5, flexWrap: 'wrap', alignItems: 'center' }}>
                      <Button
                        variant="contained"
                        startIcon={syncNowMutation.isPending ? <CircularProgress size={14} sx={{ color: 'inherit' }} /> : <SyncOutlined />}
                        onClick={() => { setSyncResult(null); syncNowMutation.mutate() }}
                        disabled={syncNowMutation.isPending || syncBackgroundMutation.isPending || resetContentMutation.isPending}
                      >
                        {syncNowMutation.isPending ? 'Syncing…' : 'Sync Now'}
                      </Button>
                      <Button
                        variant="outlined"
                        startIcon={syncBackgroundMutation.isPending ? <CircularProgress size={14} /> : <SyncOutlined />}
                        onClick={() => { setSyncResult(null); syncBackgroundMutation.mutate() }}
                        disabled={syncNowMutation.isPending || syncBackgroundMutation.isPending || resetContentMutation.isPending}
                      >
                        {syncBackgroundMutation.isPending ? 'Queuing…' : 'Sync in Background'}
                      </Button>

                      <Divider orientation="vertical" flexItem sx={{ mx: 0.5 }} />

                      <Tooltip title="Wipe all POLs, IMPs and assessments then re-import from source files. Control groups, framework bundles, users, evidence and gaps are NOT affected.">
                        <span>
                          <Button
                            variant="outlined"
                            color="warning"
                            startIcon={resetContentMutation.isPending ? <CircularProgress size={14} /> : <DeleteSweepOutlined />}
                            onClick={handleResetContent}
                            disabled={syncNowMutation.isPending || syncBackgroundMutation.isPending || resetContentMutation.isPending}
                          >
                            {resetContentMutation.isPending ? 'Resetting…' : 'Reset & Re-import'}
                          </Button>
                        </span>
                      </Tooltip>
                    </Box>
                  </CardContent>
                </Card>

                {/* Orphan Scanner */}
                <Card>
                  <CardContent sx={{ pb: '12px !important' }}>
                    <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 1.5 }}>
                      <DeleteSweepOutlined sx={{ color: 'primary.main' }} />
                      <Typography variant="h6" sx={{ flex: 1 }}>Orphan Scanner</Typography>
                      <Button
                        size="small"
                        variant="outlined"
                        startIcon={scanOrphansMutation.isPending ? <CircularProgress size={12} /> : <DeleteSweepOutlined />}
                        disabled={scanOrphansMutation.isPending || purgeOrphansMutation.isPending}
                        onClick={() => { setOrphanResult(null); setPurgeResult(null); scanOrphansMutation.mutate() }}
                        sx={{ fontSize: '0.7rem' }}
                      >
                        {scanOrphansMutation.isPending ? 'Scanning…' : 'Scan'}
                      </Button>
                    </Box>
                    <Divider sx={{ mb: 1.5 }} />
                    {purgeResult && (
                      <Alert severity="success" sx={{ mb: 1, py: 0 }}>{purgeResult}</Alert>
                    )}
                    {scanOrphansMutation.isError && (
                      <Alert severity="error" sx={{ mb: 1, py: 0 }}>Scan failed.</Alert>
                    )}
                    {orphanResult === null && !purgeResult && (
                      <Typography variant="body2" color="text.secondary">
                        Finds DB records whose source file no longer exists on disk.
                      </Typography>
                    )}
                    {orphanResult !== null && (
                      <>
                        {orphanResult.implementations.length === 0 && orphanResult.policies.length === 0 ? (
                          <Alert severity="success" sx={{ py: 0 }}>No orphans found — DB is clean.</Alert>
                        ) : (
                          <>
                            <Alert severity="warning" sx={{ mb: 1.5, py: 0 }}>
                              {orphanResult.implementations.length + orphanResult.policies.length} orphaned record{orphanResult.implementations.length + orphanResult.policies.length !== 1 ? 's' : ''} found.
                            </Alert>
                            {orphanResult.implementations.length > 0 && (
                              <>
                                <Typography variant="caption" color="text.secondary" display="block" sx={{ mb: 0.5 }}>
                                  Implementations ({orphanResult.implementations.length})
                                </Typography>
                                {orphanResult.implementations.map((o) => (
                                  <Typography key={o.document_id} variant="caption" fontFamily="monospace" display="block" sx={{ color: '#FFC7CE', mb: 0.25 }}>
                                    {o.document_id}
                                  </Typography>
                                ))}
                              </>
                            )}
                            {orphanResult.policies.length > 0 && (
                              <>
                                <Typography variant="caption" color="text.secondary" display="block" sx={{ mt: 1, mb: 0.5 }}>
                                  Policies ({orphanResult.policies.length})
                                </Typography>
                                {orphanResult.policies.map((o) => (
                                  <Typography key={o.document_id} variant="caption" fontFamily="monospace" display="block" sx={{ color: '#FFC7CE', mb: 0.25 }}>
                                    {o.document_id}
                                  </Typography>
                                ))}
                              </>
                            )}
                            <Button
                              size="small"
                              variant="contained"
                              color="error"
                              startIcon={purgeOrphansMutation.isPending ? <CircularProgress size={12} /> : <DeleteSweepOutlined />}
                              disabled={purgeOrphansMutation.isPending}
                              onClick={() => purgeOrphansMutation.mutate()}
                              sx={{ mt: 1.5, fontSize: '0.7rem' }}
                              fullWidth
                            >
                              {purgeOrphansMutation.isPending ? 'Purging…' : `Purge ${orphanResult.implementations.length + orphanResult.policies.length} orphans`}
                            </Button>
                          </>
                        )}
                      </>
                    )}
                  </CardContent>
                </Card>

              </Box>
            </Grid>
          </Grid>

          {/* System Event Log */}
          <Card>
            <CardContent sx={{ pb: '12px !important' }}>
              <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 1.5 }}>
                <AssignmentOutlined sx={{ color: 'primary.main' }} />
                <Typography variant="h6" sx={{ flex: 1 }}>System Event Log</Typography>
                <Typography variant="caption" color="text.secondary">
                  Last 30 system events
                </Typography>
              </Box>
              <Divider sx={{ mb: 1.5 }} />
              {!sysLogs || sysLogs.items.length === 0 ? (
                <Typography variant="body2" color="text.secondary">
                  No system events recorded yet. Events appear here when background jobs run (archive sweeps, sync tasks, etc.).
                </Typography>
              ) : (
                <TableContainer>
                  <Table size="small">
                    <TableHead>
                      <TableRow>
                        <TableCell sx={{ color: 'text.secondary', fontSize: '0.7rem', py: 0.5 }}>Time</TableCell>
                        <TableCell sx={{ color: 'text.secondary', fontSize: '0.7rem', py: 0.5 }}>Event</TableCell>
                        <TableCell sx={{ color: 'text.secondary', fontSize: '0.7rem', py: 0.5 }}>Severity</TableCell>
                        <TableCell sx={{ color: 'text.secondary', fontSize: '0.7rem', py: 0.5 }}>Description</TableCell>
                      </TableRow>
                    </TableHead>
                    <TableBody>
                      {sysLogs.items.map((entry) => {
                        const sevColor = entry.severity === 'error' || entry.severity === 'critical'
                          ? '#FFC7CE'
                          : entry.severity === 'warning'
                          ? '#FFEB9C'
                          : '#C6EFCE'
                        const sevBg = entry.severity === 'error' || entry.severity === 'critical'
                          ? '#3a0000'
                          : entry.severity === 'warning'
                          ? '#3a2e00'
                          : '#1a3a27'
                        return (
                          <TableRow key={entry.id} hover>
                            <TableCell sx={{ fontSize: '0.7rem', py: 0.5, whiteSpace: 'nowrap', color: 'text.secondary' }}>
                              {dayjs(entry.created_at).format('YYYY-MM-DD HH:mm:ss')}
                            </TableCell>
                            <TableCell sx={{ fontSize: '0.7rem', py: 0.5, fontFamily: 'monospace' }}>
                              {entry.event_type}
                            </TableCell>
                            <TableCell sx={{ py: 0.5 }}>
                              <Chip
                                label={entry.severity}
                                size="small"
                                sx={{ fontSize: '0.6rem', height: 16, bgcolor: sevBg, color: sevColor }}
                              />
                            </TableCell>
                            <TableCell sx={{ fontSize: '0.7rem', py: 0.5, color: 'text.secondary' }}>
                              {entry.description ?? '—'}
                            </TableCell>
                          </TableRow>
                        )
                      })}
                    </TableBody>
                  </Table>
                </TableContainer>
              )}
            </CardContent>
          </Card>

        </Box>
      )}
    </Box>
  )
}
