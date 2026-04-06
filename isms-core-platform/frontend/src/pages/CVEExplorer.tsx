import { useState } from 'react'
import {
  Alert, Box, Button, Chip, Collapse, Divider, FormControl,
  IconButton, InputLabel, MenuItem, Paper, Select, Switch,
  Tab, Table, TableBody, TableCell, TableHead, TableRow,
  Tabs, TextField, Tooltip, Typography,
} from '@mui/material'
import {
  BugReportOutlined, CheckCircleOutlined, ChevronRightOutlined,
  ExpandLessOutlined, ExpandMoreOutlined, InfoOutlined,
  KeyboardArrowLeftOutlined, KeyboardArrowRightOutlined,
  LinkOutlined, OpenInNewOutlined, SecurityOutlined,
  WarningAmberOutlined,
} from '@mui/icons-material'
import { useQuery } from '@tanstack/react-query'
import { feedsApi, type NvdCveEntry } from '../api/feedsApi'
import PageHeader from '../components/PageHeader'

// ── Constants ──────────────────────────────────────────────────────────────────

const INTEL_COLOR = '#B84F00'

const SEVERITY_COLORS: Record<string, { bg: string; color: string }> = {
  CRITICAL: { bg: '#3a0a0a', color: '#FFC7CE' },
  HIGH:     { bg: '#2a1a00', color: '#FFEB9C' },
  MEDIUM:   { bg: '#1a2a3a', color: '#9fc8f0' },
  LOW:      { bg: '#1a2a1a', color: '#C6EFCE' },
  NONE:     { bg: '#1e1e2e', color: '#888' },
}

function SeverityChip({ severity }: { severity: string | null }) {
  if (!severity) return <Typography variant="caption" color="text.disabled">—</Typography>
  const c = SEVERITY_COLORS[severity] ?? SEVERITY_COLORS.NONE
  return (
    <Chip
      label={severity}
      size="small"
      sx={{ fontSize: '0.68rem', height: 18, bgcolor: c.bg, color: c.color, border: `1px solid ${c.color}40`, fontWeight: 600 }}
    />
  )
}

function fmtDate(iso: string | null) {
  if (!iso) return '—'
  return iso.slice(0, 10)
}

function fmtScore(score: number | null) {
  if (score === null || score === undefined) return '—'
  return score.toFixed(1)
}

// ── Stats Bar ─────────────────────────────────────────────────────────────────

function StatsBar() {
  const { data } = useQuery({
    queryKey: ['nvd', 'index-stats'],
    queryFn: feedsApi.getNvdIndexStats,
    staleTime: 60_000,
  })

  if (!data) return null

  const lastSync = data.last_cve_sync ? new Date(data.last_cve_sync).toLocaleString(undefined, {
    month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit',
  }) : 'Never'

  return (
    <Box sx={{
      display: 'flex', gap: 3, alignItems: 'center', flexWrap: 'wrap',
      px: 2, py: 1, bgcolor: '#0d1117', borderRadius: 1.5,
      border: '1px solid', borderColor: 'divider', mb: 1.5,
    }}>
      {[
        { label: 'CVEs', value: data.cve_total.toLocaleString(), icon: <BugReportOutlined sx={{ fontSize: 14, color: '#c62828' }} /> },
        { label: 'CPEs', value: data.cpe_total.toLocaleString(), icon: <SecurityOutlined sx={{ fontSize: 14, color: INTEL_COLOR }} /> },
        { label: 'In KEV', value: data.kev_total.toLocaleString(), icon: <WarningAmberOutlined sx={{ fontSize: 14, color: '#FFEB9C' }} /> },
      ].map(s => (
        <Box key={s.label} sx={{ display: 'flex', alignItems: 'center', gap: 0.5 }}>
          {s.icon}
          <Typography variant="body2" fontWeight={700} sx={{ color: 'text.primary' }}>{s.value}</Typography>
          <Typography variant="caption" color="text.secondary">{s.label}</Typography>
        </Box>
      ))}
      <Divider orientation="vertical" flexItem sx={{ mx: 0.5 }} />
      <Typography variant="caption" color="text.secondary">
        Last sync: {lastSync}
      </Typography>
      {!data.nist_api_key_configured && (
        <Chip label="No API key — limited rate" size="small" color="warning" sx={{ fontSize: '0.68rem', height: 18 }} />
      )}
      {data.cpe_full_enabled && (
        <Chip label="CPE Option B active" size="small" sx={{ fontSize: '0.68rem', height: 18, bgcolor: '#1a2a3a', color: '#9fc8f0' }} />
      )}
    </Box>
  )
}

// ── Info Panel (collapsible) ──────────────────────────────────────────────────

function InfoPanel() {
  const [open, setOpen] = useState(false)
  const { data } = useQuery({
    queryKey: ['nvd', 'index-stats'],
    queryFn: feedsApi.getNvdIndexStats,
    staleTime: 60_000,
  })
  const { data: cveStats } = useQuery({
    queryKey: ['nvd', 'cve-stats'],
    queryFn: feedsApi.getCveStats,
    staleTime: 60_000,
  })
  const { data: cpeStats } = useQuery({
    queryKey: ['nvd', 'cpe-stats'],
    queryFn: feedsApi.getCpeStats,
    staleTime: 60_000,
  })

  return (
    <Paper variant="outlined" sx={{ borderRadius: 2, mb: 2, overflow: 'hidden' }}>
      <Box
        onClick={() => setOpen(o => !o)}
        sx={{ px: 2, py: 1.2, display: 'flex', alignItems: 'center', gap: 1, cursor: 'pointer', '&:hover': { bgcolor: 'action.hover' } }}
      >
        <InfoOutlined sx={{ fontSize: 16, color: INTEL_COLOR }} />
        <Typography variant="subtitle2" fontWeight={600} sx={{ flex: 1 }}>
          NVD Intelligence — Index Details & Data Source
        </Typography>
        {open ? <ExpandLessOutlined sx={{ fontSize: 18 }} /> : <ExpandMoreOutlined sx={{ fontSize: 18 }} />}
      </Box>
      <Collapse in={open}>
        <Divider />
        <Box sx={{ p: 2, display: 'flex', gap: 3, flexWrap: 'wrap' }}>
          {/* CVE index */}
          <Box sx={{ flex: '1 1 200px' }}>
            <Typography variant="caption" color={INTEL_COLOR} fontWeight={700} display="block" sx={{ mb: 0.5 }}>CVE INDEX (nvd-cve)</Typography>
            {[
              ['Total CVEs', cveStats?.total.toLocaleString() ?? '—'],
              ['Critical', cveStats?.critical.toLocaleString() ?? '—'],
              ['High', cveStats?.high.toLocaleString() ?? '—'],
              ['Medium', cveStats?.medium.toLocaleString() ?? '—'],
              ['Low', cveStats?.low.toLocaleString() ?? '—'],
              ['In CISA KEV', cveStats?.in_kev.toLocaleString() ?? '—'],
              ['With EPSS', cveStats?.with_epss.toLocaleString() ?? '—'],
            ].map(([k, v]) => (
              <Box key={k} sx={{ display: 'flex', justifyContent: 'space-between', mb: 0.3 }}>
                <Typography variant="caption" color="text.secondary">{k}</Typography>
                <Typography variant="caption" fontWeight={600}>{v}</Typography>
              </Box>
            ))}
          </Box>
          {/* CPE index */}
          <Box sx={{ flex: '1 1 200px' }}>
            <Typography variant="caption" color={INTEL_COLOR} fontWeight={700} display="block" sx={{ mb: 0.5 }}>CPE INDEX (nvd-cpe)</Typography>
            {[
              ['Total CPEs', cpeStats?.total.toLocaleString() ?? '—'],
              ['Applications (a)', cpeStats?.applications.toLocaleString() ?? '—'],
              ['Operating Systems (o)', cpeStats?.operating_systems.toLocaleString() ?? '—'],
              ['Hardware (h)', cpeStats?.hardware.toLocaleString() ?? '—'],
              ['Source: CVE-config (A)', cpeStats?.cve_config.toLocaleString() ?? '—'],
              ['Source: KEV-vendor (B)', cpeStats?.kev_vendor.toLocaleString() ?? '—'],
              ['Option B active', data?.cpe_full_enabled ? 'Yes' : 'No'],
            ].map(([k, v]) => (
              <Box key={k} sx={{ display: 'flex', justifyContent: 'space-between', mb: 0.3 }}>
                <Typography variant="caption" color="text.secondary">{k}</Typography>
                <Typography variant="caption" fontWeight={600}>{v}</Typography>
              </Box>
            ))}
          </Box>
          {/* Feed schedule & source */}
          <Box sx={{ flex: '1 1 200px' }}>
            <Typography variant="caption" color={INTEL_COLOR} fontWeight={700} display="block" sx={{ mb: 0.5 }}>FEED SCHEDULE</Typography>
            {[
              ['CVE full pull', 'Sunday 01:00 UTC'],
              ['CVE delta', 'Daily 03:00 UTC'],
              ['CPE Option B', 'Sunday 01:30 UTC'],
              ['NIST API key', data?.nist_api_key_configured ? 'Configured ✓' : 'Not set (5 req/30s)'],
            ].map(([k, v]) => (
              <Box key={k} sx={{ display: 'flex', justifyContent: 'space-between', mb: 0.3 }}>
                <Typography variant="caption" color="text.secondary">{k}</Typography>
                <Typography variant="caption" fontWeight={600}>{v}</Typography>
              </Box>
            ))}
            <Box sx={{ mt: 1.5 }}>
              <Typography variant="caption" color="text.secondary" display="block">Data source:</Typography>
              <Typography variant="caption">
                National Vulnerability Database (NVD) — NIST.{' '}
                <a href="https://nvd.nist.gov" target="_blank" rel="noreferrer" style={{ color: INTEL_COLOR }}>nvd.nist.gov</a>
              </Typography>
            </Box>
          </Box>
        </Box>
      </Collapse>
    </Paper>
  )
}

// ── CVE Detail Panel ──────────────────────────────────────────────────────────

function CveDetail({ cve, onClose }: { cve: NvdCveEntry; onClose: () => void }) {
  const sc = SEVERITY_COLORS[cve.cvss_v3_severity ?? ''] ?? SEVERITY_COLORS.NONE
  return (
    <Paper variant="outlined" sx={{ borderRadius: 2, p: 2, position: 'sticky', top: 16, maxHeight: 'calc(100vh - 120px)', overflowY: 'auto' }}>
      <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', mb: 1.5 }}>
        <Box>
          <Typography variant="subtitle1" fontWeight={700} sx={{ fontFamily: 'monospace', color: '#c62828' }}>
            {cve.cve_id}
          </Typography>
          <Box sx={{ display: 'flex', gap: 0.5, mt: 0.5, flexWrap: 'wrap' }}>
            <SeverityChip severity={cve.cvss_v3_severity} />
            {cve.in_kev && <Chip label="KEV" size="small" color="error" sx={{ fontSize: '0.68rem', height: 18 }} />}
            {cve.epss_score !== null && (
              <Chip label={`EPSS ${(cve.epss_score * 100).toFixed(1)}%`} size="small" sx={{ fontSize: '0.68rem', height: 18, bgcolor: '#1a2a3a', color: '#9fc8f0' }} />
            )}
          </Box>
        </Box>
        <IconButton size="small" onClick={onClose}><ChevronRightOutlined /></IconButton>
      </Box>

      <Typography variant="body2" sx={{ mb: 2, lineHeight: 1.6, fontSize: '0.8rem' }}>
        {cve.description ?? 'No description available.'}
      </Typography>

      <Box sx={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 0.5, mb: 1.5 }}>
        {[
          ['Published',   fmtDate(cve.published)],
          ['Modified',    fmtDate(cve.last_modified)],
          ['Status',      cve.vuln_status ?? '—'],
          ['CVSSv3',      fmtScore(cve.cvss_v3_score)],
          ['CVSSv2',      fmtScore(cve.cvss_v2_score)],
          ['Vector',      cve.cvss_v3_vector ?? '—'],
        ].map(([k, v]) => (
          <Box key={k}>
            <Typography variant="caption" color="text.secondary" display="block">{k}</Typography>
            <Typography variant="caption" fontWeight={500} sx={{ wordBreak: 'break-all' }}>{v}</Typography>
          </Box>
        ))}
      </Box>

      {cve.cwe_ids.length > 0 && (
        <Box sx={{ mb: 1.5 }}>
          <Typography variant="caption" color="text.secondary" display="block" sx={{ mb: 0.5 }}>CWE</Typography>
          <Box sx={{ display: 'flex', gap: 0.5, flexWrap: 'wrap' }}>
            {cve.cwe_ids.map(c => <Chip key={c} label={c} size="small" sx={{ fontSize: '0.68rem', height: 18 }} />)}
          </Box>
        </Box>
      )}

      {cve.cpe_affected.length > 0 && (
        <Box sx={{ mb: 1.5 }}>
          <Typography variant="caption" color="text.secondary" display="block" sx={{ mb: 0.5 }}>
            Affected CPEs ({cve.cpe_affected.length})
          </Typography>
          <Box sx={{ maxHeight: 120, overflowY: 'auto' }}>
            {cve.cpe_affected.slice(0, 20).map(c => (
              <Typography key={c} variant="caption" display="block" sx={{ fontFamily: 'monospace', fontSize: '0.67rem', color: 'text.secondary', lineHeight: 1.6 }} noWrap>
                {c}
              </Typography>
            ))}
            {cve.cpe_affected.length > 20 && (
              <Typography variant="caption" color="text.disabled">+{cve.cpe_affected.length - 20} more</Typography>
            )}
          </Box>
        </Box>
      )}

      {cve.references.length > 0 && (
        <Box>
          <Typography variant="caption" color="text.secondary" display="block" sx={{ mb: 0.5 }}>References</Typography>
          {cve.references.slice(0, 5).map((r, i) => (
            <Box key={i} sx={{ display: 'flex', alignItems: 'center', gap: 0.5, mb: 0.3 }}>
              <LinkOutlined sx={{ fontSize: 11, color: 'text.disabled' }} />
              <Typography
                component="a" href={r} target="_blank" rel="noreferrer"
                variant="caption" sx={{ color: INTEL_COLOR, textDecoration: 'none', '&:hover': { textDecoration: 'underline' }, wordBreak: 'break-all', fontSize: '0.7rem' }}
              >
                {r.replace(/^https?:\/\//, '').slice(0, 60)}{r.length > 70 ? '…' : ''}
              </Typography>
            </Box>
          ))}
        </Box>
      )}
    </Paper>
  )
}

// ── CVE Tab ───────────────────────────────────────────────────────────────────

function CveTab() {
  const [search, setSearch]     = useState('')
  const [searchInput, setSearchInput] = useState('')
  const [severity, setSeverity] = useState('')
  const [kevOnly, setKevOnly]   = useState(false)
  const [minEpss, setMinEpss]   = useState(0)
  const [year, setYear]         = useState<number | undefined>()
  const [page, setPage]         = useState(1)
  const [selected, setSelected] = useState<NvdCveEntry | null>(null)
  const PER_PAGE = 50

  const { data, isLoading } = useQuery({
    queryKey: ['nvd', 'cve', search, severity, kevOnly, minEpss, year, page],
    queryFn: () => feedsApi.getCve({
      search: search || undefined,
      severity: severity || undefined,
      kev_only: kevOnly || undefined,
      min_epss: minEpss || undefined,
      year: year || undefined,
      page,
      per_page: PER_PAGE,
    }),
    staleTime: 30_000,
  })

  function handleSearch() {
    setSearch(searchInput)
    setPage(1)
  }

  const totalPages = data ? Math.ceil(data.total / PER_PAGE) : 1

  return (
    <Box sx={{ display: 'flex', gap: 2, alignItems: 'flex-start' }}>
      <Box sx={{ flex: 1, minWidth: 0 }}>
        {/* Filters */}
        <Box sx={{ display: 'flex', gap: 1, flexWrap: 'wrap', mb: 2, alignItems: 'center' }}>
          <TextField
            size="small"
            placeholder="Search CVE ID, description, CWE…"
            value={searchInput}
            onChange={e => setSearchInput(e.target.value)}
            onKeyDown={e => e.key === 'Enter' && handleSearch()}
            sx={{ flex: '1 1 280px', '& input': { fontSize: '0.82rem' } }}
          />
          <Button size="small" variant="contained" onClick={handleSearch} sx={{ fontSize: '0.78rem' }}>Search</Button>

          <FormControl size="small" sx={{ minWidth: 120 }}>
            <InputLabel sx={{ fontSize: '0.78rem' }}>Severity</InputLabel>
            <Select value={severity} label="Severity" onChange={e => { setSeverity(e.target.value); setPage(1) }} sx={{ fontSize: '0.78rem' }}>
              <MenuItem value="" sx={{ fontSize: '0.78rem' }}>All</MenuItem>
              {['CRITICAL', 'HIGH', 'MEDIUM', 'LOW'].map(s => (
                <MenuItem key={s} value={s} sx={{ fontSize: '0.78rem' }}>{s}</MenuItem>
              ))}
            </Select>
          </FormControl>

          <FormControl size="small" sx={{ minWidth: 90 }}>
            <InputLabel sx={{ fontSize: '0.78rem' }}>EPSS ≥</InputLabel>
            <Select value={minEpss} label="EPSS ≥" onChange={e => { setMinEpss(Number(e.target.value)); setPage(1) }} sx={{ fontSize: '0.78rem' }}>
              {[0, 0.1, 0.2, 0.5].map(v => (
                <MenuItem key={v} value={v} sx={{ fontSize: '0.78rem' }}>{v === 0 ? 'Any' : `${(v * 100).toFixed(0)}%`}</MenuItem>
              ))}
            </Select>
          </FormControl>

          <FormControl size="small" sx={{ minWidth: 90 }}>
            <InputLabel sx={{ fontSize: '0.78rem' }}>Year</InputLabel>
            <Select value={year ?? ''} label="Year" onChange={e => { setYear(e.target.value ? Number(e.target.value) : undefined); setPage(1) }} sx={{ fontSize: '0.78rem' }}>
              <MenuItem value="" sx={{ fontSize: '0.78rem' }}>Any</MenuItem>
              {Array.from({ length: 10 }, (_, i) => new Date().getFullYear() - i).map(y => (
                <MenuItem key={y} value={y} sx={{ fontSize: '0.78rem' }}>{y}</MenuItem>
              ))}
            </Select>
          </FormControl>

          <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.5 }}>
            <Switch size="small" checked={kevOnly} onChange={e => { setKevOnly(e.target.checked); setPage(1) }} />
            <Typography variant="caption">KEV only</Typography>
          </Box>
        </Box>

        {/* Result count */}
        {data && (
          <Typography variant="caption" color="text.secondary" display="block" sx={{ mb: 1 }}>
            {data.total.toLocaleString()} CVEs{search ? ` matching "${search}"` : ''}
          </Typography>
        )}

        {/* Table */}
        <Paper variant="outlined" sx={{ borderRadius: 2, overflow: 'hidden' }}>
          {isLoading && <Alert severity="info" sx={{ borderRadius: 0 }}>Loading…</Alert>}
          <Table size="small">
            <TableHead>
              <TableRow>
                <TableCell sx={{ fontWeight: 600, fontSize: '0.72rem', width: 130 }}>CVE ID</TableCell>
                <TableCell sx={{ fontWeight: 600, fontSize: '0.72rem' }}>Description</TableCell>
                <TableCell sx={{ fontWeight: 600, fontSize: '0.72rem', width: 90 }}>Severity</TableCell>
                <TableCell sx={{ fontWeight: 600, fontSize: '0.72rem', width: 60 }}>CVSSv3</TableCell>
                <TableCell sx={{ fontWeight: 600, fontSize: '0.72rem', width: 70 }}>EPSS</TableCell>
                <TableCell sx={{ fontWeight: 600, fontSize: '0.72rem', width: 90 }}>Published</TableCell>
                <TableCell sx={{ fontWeight: 600, fontSize: '0.72rem', width: 60 }}>Flags</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {(data?.items ?? []).map(cve => (
                <TableRow
                  key={cve.cve_id}
                  hover
                  selected={selected?.cve_id === cve.cve_id}
                  onClick={() => setSelected(s => s?.cve_id === cve.cve_id ? null : cve)}
                  sx={{ cursor: 'pointer' }}
                >
                  <TableCell sx={{ fontSize: '0.75rem', fontFamily: 'monospace', color: '#c62828', fontWeight: 600, whiteSpace: 'nowrap' }}>
                    {cve.cve_id}
                  </TableCell>
                  <TableCell sx={{ fontSize: '0.75rem', maxWidth: 340 }}>
                    <Typography noWrap variant="inherit" title={cve.description ?? ''}>
                      {cve.description ?? '—'}
                    </Typography>
                  </TableCell>
                  <TableCell><SeverityChip severity={cve.cvss_v3_severity} /></TableCell>
                  <TableCell sx={{ fontSize: '0.75rem', fontWeight: 600, color: cve.cvss_v3_score !== null && cve.cvss_v3_score >= 9 ? '#FFC7CE' : 'text.primary' }}>
                    {fmtScore(cve.cvss_v3_score)}
                  </TableCell>
                  <TableCell sx={{ fontSize: '0.75rem' }}>
                    {cve.epss_score !== null ? `${(cve.epss_score * 100).toFixed(1)}%` : '—'}
                  </TableCell>
                  <TableCell sx={{ fontSize: '0.75rem', whiteSpace: 'nowrap' }}>{fmtDate(cve.published)}</TableCell>
                  <TableCell>
                    <Box sx={{ display: 'flex', gap: 0.3 }}>
                      {cve.in_kev && <Tooltip title="In CISA KEV"><WarningAmberOutlined sx={{ fontSize: 14, color: '#FFEB9C' }} /></Tooltip>}
                      {cve.cpe_affected.length > 0 && <Tooltip title={`${cve.cpe_affected.length} CPEs`}><SecurityOutlined sx={{ fontSize: 14, color: INTEL_COLOR }} /></Tooltip>}
                    </Box>
                  </TableCell>
                </TableRow>
              ))}
              {!isLoading && data?.items.length === 0 && (
                <TableRow>
                  <TableCell colSpan={7} sx={{ textAlign: 'center', py: 3, color: 'text.secondary', fontSize: '0.82rem' }}>
                    No CVEs found. Enable FEEDS_CVE_ENABLED=true and restart the feeds container.
                  </TableCell>
                </TableRow>
              )}
            </TableBody>
          </Table>
        </Paper>

        {/* Pagination */}
        {totalPages > 1 && (
          <Box sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', gap: 1, mt: 1.5 }}>
            <IconButton size="small" disabled={page === 1} onClick={() => setPage(p => p - 1)}>
              <KeyboardArrowLeftOutlined />
            </IconButton>
            <Typography variant="caption">Page {page} / {totalPages}</Typography>
            <IconButton size="small" disabled={page === totalPages} onClick={() => setPage(p => p + 1)}>
              <KeyboardArrowRightOutlined />
            </IconButton>
          </Box>
        )}
      </Box>

      {/* Detail panel */}
      {selected && (
        <Box sx={{ width: 360, flexShrink: 0 }}>
          <CveDetail cve={selected} onClose={() => setSelected(null)} />
        </Box>
      )}
    </Box>
  )
}

// ── CPE Tab ───────────────────────────────────────────────────────────────────

function CpeTab() {
  const [search, setSearch]     = useState('')
  const [searchInput, setSearchInput] = useState('')
  const [part, setPart]         = useState('')
  const [source, setSource]     = useState('')
  const [kevOnly, setKevOnly]   = useState(false)
  const [page, setPage]         = useState(1)
  const PER_PAGE = 50

  const { data, isLoading } = useQuery({
    queryKey: ['nvd', 'cpe', search, part, source, kevOnly, page],
    queryFn: () => feedsApi.getCpe({
      search: search || undefined,
      part: part || undefined,
      source: source || undefined,
      kev_only: kevOnly || undefined,
      page,
      per_page: PER_PAGE,
    }),
    staleTime: 30_000,
  })

  const totalPages = data ? Math.ceil(data.total / PER_PAGE) : 1

  const PART_LABELS: Record<string, string> = { a: 'Application', o: 'OS', h: 'Hardware' }

  return (
    <Box>
      {/* Filters */}
      <Box sx={{ display: 'flex', gap: 1, flexWrap: 'wrap', mb: 2, alignItems: 'center' }}>
        <TextField
          size="small"
          placeholder="Search vendor, product, CPE URI…"
          value={searchInput}
          onChange={e => setSearchInput(e.target.value)}
          onKeyDown={e => { if (e.key === 'Enter') { setSearch(searchInput); setPage(1) } }}
          sx={{ flex: '1 1 280px', '& input': { fontSize: '0.82rem' } }}
        />
        <Button size="small" variant="contained" onClick={() => { setSearch(searchInput); setPage(1) }} sx={{ fontSize: '0.78rem' }}>Search</Button>

        <FormControl size="small" sx={{ minWidth: 130 }}>
          <InputLabel sx={{ fontSize: '0.78rem' }}>Type</InputLabel>
          <Select value={part} label="Type" onChange={e => { setPart(e.target.value); setPage(1) }} sx={{ fontSize: '0.78rem' }}>
            <MenuItem value="" sx={{ fontSize: '0.78rem' }}>All</MenuItem>
            <MenuItem value="a" sx={{ fontSize: '0.78rem' }}>Application</MenuItem>
            <MenuItem value="o" sx={{ fontSize: '0.78rem' }}>Operating System</MenuItem>
            <MenuItem value="h" sx={{ fontSize: '0.78rem' }}>Hardware</MenuItem>
          </Select>
        </FormControl>

        <FormControl size="small" sx={{ minWidth: 140 }}>
          <InputLabel sx={{ fontSize: '0.78rem' }}>Source</InputLabel>
          <Select value={source} label="Source" onChange={e => { setSource(e.target.value); setPage(1) }} sx={{ fontSize: '0.78rem' }}>
            <MenuItem value="" sx={{ fontSize: '0.78rem' }}>All</MenuItem>
            <MenuItem value="cve_config" sx={{ fontSize: '0.78rem' }}>CVE Config (A)</MenuItem>
            <MenuItem value="kev_vendor" sx={{ fontSize: '0.78rem' }}>KEV Vendor (B)</MenuItem>
          </Select>
        </FormControl>

        <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.5 }}>
          <Switch size="small" checked={kevOnly} onChange={e => { setKevOnly(e.target.checked); setPage(1) }} />
          <Typography variant="caption">KEV only</Typography>
        </Box>
      </Box>

      {data && (
        <Typography variant="caption" color="text.secondary" display="block" sx={{ mb: 1 }}>
          {data.total.toLocaleString()} CPEs{search ? ` matching "${search}"` : ''}
        </Typography>
      )}

      <Paper variant="outlined" sx={{ borderRadius: 2, overflow: 'hidden' }}>
        {isLoading && <Alert severity="info" sx={{ borderRadius: 0 }}>Loading…</Alert>}
        <Table size="small">
          <TableHead>
            <TableRow>
              <TableCell sx={{ fontWeight: 600, fontSize: '0.72rem' }}>CPE URI</TableCell>
              <TableCell sx={{ fontWeight: 600, fontSize: '0.72rem', width: 110 }}>Vendor</TableCell>
              <TableCell sx={{ fontWeight: 600, fontSize: '0.72rem', width: 110 }}>Product</TableCell>
              <TableCell sx={{ fontWeight: 600, fontSize: '0.72rem', width: 70 }}>Type</TableCell>
              <TableCell sx={{ fontWeight: 600, fontSize: '0.72rem', width: 110 }}>Source</TableCell>
              <TableCell sx={{ fontWeight: 600, fontSize: '0.72rem', width: 50 }}>KEV</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {(data?.items ?? []).map(cpe => (
              <TableRow key={cpe.cpe_uri} hover>
                <TableCell sx={{ fontSize: '0.7rem', fontFamily: 'monospace', maxWidth: 320 }}>
                  <Typography noWrap variant="inherit" title={cpe.cpe_uri}>{cpe.cpe_uri}</Typography>
                </TableCell>
                <TableCell sx={{ fontSize: '0.75rem' }}>{cpe.vendor ?? '—'}</TableCell>
                <TableCell sx={{ fontSize: '0.75rem' }}>{cpe.product ?? '—'}</TableCell>
                <TableCell>
                  <Chip
                    label={PART_LABELS[cpe.part ?? ''] ?? cpe.part ?? '—'}
                    size="small"
                    sx={{ fontSize: '0.68rem', height: 18 }}
                  />
                </TableCell>
                <TableCell>
                  <Chip
                    label={cpe.source === 'kev_vendor' ? 'KEV-vendor' : 'CVE-config'}
                    size="small"
                    sx={{ fontSize: '0.68rem', height: 18, bgcolor: cpe.source === 'kev_vendor' ? '#3a0a0a' : '#1a2a1a', color: cpe.source === 'kev_vendor' ? '#FFC7CE' : '#C6EFCE' }}
                  />
                </TableCell>
                <TableCell>
                  {cpe.in_kev
                    ? <CheckCircleOutlined sx={{ fontSize: 14, color: '#FFEB9C' }} />
                    : <Typography variant="caption" color="text.disabled">—</Typography>}
                </TableCell>
              </TableRow>
            ))}
            {!isLoading && data?.items.length === 0 && (
              <TableRow>
                <TableCell colSpan={6} sx={{ textAlign: 'center', py: 3, color: 'text.secondary', fontSize: '0.82rem' }}>
                  No CPEs found. Enable FEEDS_CVE_ENABLED=true to populate the CPE index.
                </TableCell>
              </TableRow>
            )}
          </TableBody>
        </Table>
      </Paper>

      {totalPages > 1 && (
        <Box sx={{ display: 'flex', justifyContent: 'center', alignItems: 'center', gap: 1, mt: 1.5 }}>
          <IconButton size="small" disabled={page === 1} onClick={() => setPage(p => p - 1)}>
            <KeyboardArrowLeftOutlined />
          </IconButton>
          <Typography variant="caption">Page {page} / {totalPages}</Typography>
          <IconButton size="small" disabled={page === totalPages} onClick={() => setPage(p => p + 1)}>
            <KeyboardArrowRightOutlined />
          </IconButton>
        </Box>
      )}
    </Box>
  )
}

// ── Main Component ────────────────────────────────────────────────────────────

export default function CVEExplorer() {
  const [tab, setTab] = useState(0)

  return (
    <Box sx={{ p: 3 }}>
      <PageHeader
        title="CVE / CPE Explorer"
        subtitle="NVD vulnerability & platform enumeration data — CVSS, EPSS, KEV correlation"
        helpSection="cve-explorer"
      />

      <StatsBar />
      <InfoPanel />

      <Tabs value={tab} onChange={(_, v) => setTab(v)} sx={{ mb: 2, borderBottom: '1px solid', borderColor: 'divider' }}>
        <Tab label="CVE" sx={{ fontSize: '0.82rem', textTransform: 'none' }} />
        <Tab label="CPE" sx={{ fontSize: '0.82rem', textTransform: 'none' }} />
      </Tabs>

      {tab === 0 && <CveTab />}
      {tab === 1 && <CpeTab />}
    </Box>
  )
}
