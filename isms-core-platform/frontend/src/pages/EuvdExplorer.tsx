import { useState } from 'react'
import { useQuery } from '@tanstack/react-query'
import {
  Box, Chip, CircularProgress, InputAdornment, MenuItem,
  Select, Switch, Table, TableBody, TableCell, TableHead,
  TableRow, TextField, Tooltip, Typography,
} from '@mui/material'
import {
  BugReportOutlined, LanguageOutlined, SearchOutlined,
  WarningAmberOutlined,
} from '@mui/icons-material'
import PageHeader from '../components/PageHeader'
import { feedsApi, EuvdEntry } from '../api/feedsApi'

const INTEL_COLOR = '#B84F00'

// ── Severity helpers ──────────────────────────────────────────────────────────

function severityColor(score: number | null): string {
  if (score === null) return '#555'
  if (score >= 9)  return '#d32f2f'
  if (score >= 7)  return '#ed6c02'
  if (score >= 4)  return '#f9a825'
  return '#388e3c'
}

function fmtDate(s: string | null): string {
  if (!s) return '—'
  return s.slice(0, 10)
}

// ── Detail Panel ──────────────────────────────────────────────────────────────

function EntryDetail({ entry, onClose }: { entry: EuvdEntry; onClose: () => void }) {
  const color = severityColor(entry.base_score)

  const rows: [string, string][] = [
    ['Published',   fmtDate(entry.date_published)],
    ['Updated',     fmtDate(entry.date_updated)],
    ['Assigner',    entry.assigner ?? '—'],
    ['CVSS Version',entry.base_score_version ?? '—'],
    ['EPSS Score',  entry.epss_score !== null ? `${(entry.epss_score * 100).toFixed(2)}%` : '—'],
  ]

  return (
    <Box sx={{ p: 2, height: '100%', overflowY: 'auto', display: 'flex', flexDirection: 'column', gap: 1.5 }}>
      <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
        <Box>
          <Typography variant="subtitle2" fontWeight={700} sx={{ fontSize: '0.88rem', fontFamily: 'monospace' }}>
            {entry.euvd_id}
          </Typography>
          {entry.cve_id && (
            <Typography variant="caption" color="text.secondary">{entry.cve_id}</Typography>
          )}
          <Box sx={{ display: 'flex', gap: 0.5, mt: 0.5, flexWrap: 'wrap' }}>
            {entry.base_score !== null && (
              <Chip label={entry.base_score.toFixed(1)} size="small"
                sx={{ fontSize: '0.68rem', height: 18, bgcolor: color, color: '#fff' }} />
            )}
            {entry.is_exploited && (
              <Chip label="EXPLOITED" size="small" color="error" sx={{ fontSize: '0.68rem', height: 18 }} />
            )}
            {entry.is_critical && (
              <Chip label="CRITICAL" size="small"
                sx={{ fontSize: '0.68rem', height: 18, bgcolor: '#b71c1c', color: '#fff' }} />
            )}
            {entry.epss_score !== null && (
              <Chip label={`EPSS ${(entry.epss_score * 100).toFixed(1)}%`} size="small"
                sx={{ fontSize: '0.68rem', height: 18, bgcolor: '#1a2a3a', color: '#9fc8f0' }} />
            )}
          </Box>
        </Box>
        <Chip label="✕" size="small" onClick={onClose} sx={{ cursor: 'pointer', ml: 1 }} />
      </Box>

      <Typography variant="body2" sx={{ lineHeight: 1.6, fontSize: '0.8rem' }}>
        {entry.description ?? 'No description available.'}
      </Typography>

      <Box sx={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 0.5 }}>
        {rows.map(([k, v]) => (
          <Box key={k}>
            <Typography variant="caption" color="text.secondary" display="block">{k}</Typography>
            <Typography variant="caption" fontWeight={500}>{v}</Typography>
          </Box>
        ))}
      </Box>

      {entry.vendors.length > 0 && (
        <Box>
          <Typography variant="caption" color="text.secondary" display="block" sx={{ mb: 0.5 }}>Vendors</Typography>
          <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 0.5 }}>
            {entry.vendors.map(v => (
              <Chip key={v} label={v} size="small" sx={{ fontSize: '0.65rem', height: 18 }} />
            ))}
          </Box>
        </Box>
      )}

      {entry.products.length > 0 && (
        <Box>
          <Typography variant="caption" color="text.secondary" display="block" sx={{ mb: 0.5 }}>Products</Typography>
          <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 0.5 }}>
            {entry.products.slice(0, 20).map(p => (
              <Chip key={p} label={p} size="small" sx={{ fontSize: '0.65rem', height: 18 }} />
            ))}
            {entry.products.length > 20 && (
              <Typography variant="caption" color="text.secondary">+{entry.products.length - 20} more</Typography>
            )}
          </Box>
        </Box>
      )}

      {entry.aliases.length > 0 && (
        <Box>
          <Typography variant="caption" color="text.secondary" display="block" sx={{ mb: 0.5 }}>Aliases</Typography>
          <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 0.5 }}>
            {entry.aliases.map(a => (
              <Chip key={a} label={a} size="small" variant="outlined"
                sx={{ fontSize: '0.65rem', height: 18 }} />
            ))}
          </Box>
        </Box>
      )}
    </Box>
  )
}

// ── Main Page ─────────────────────────────────────────────────────────────────

export default function EuvdExplorer() {
  const [searchInput, setSearchInput] = useState('')
  const [search, setSearch]           = useState('')
  const [exploitedOnly, setExploited] = useState(false)
  const [minScore, setMinScore]       = useState('')
  const [page, setPage]               = useState(1)
  const [selected, setSelected]       = useState<EuvdEntry | null>(null)

  const PER_PAGE = 25

  const { data: stats } = useQuery({
    queryKey: ['euvd', 'stats'],
    queryFn:  () => feedsApi.getEuvdStats(),
    staleTime: 5 * 60_000,
  })

  const { data, isLoading } = useQuery({
    queryKey: ['euvd', 'list', search, exploitedOnly, minScore, page],
    queryFn:  () => feedsApi.getEuvd({
      search:         search || undefined,
      exploited_only: exploitedOnly || undefined,
      min_score:      minScore ? Number(minScore) : undefined,
      page,
      per_page:       PER_PAGE,
    }),
    staleTime: 2 * 60_000,
  })

  const handleSearch = () => { setSearch(searchInput); setPage(1) }
  const totalPages = data ? Math.ceil(data.total / PER_PAGE) : 1

  return (
    <Box sx={{ p: 3 }}>
      <PageHeader
        title="ENISA EUVD Explorer"
        subtitle="European Vulnerability Database — actively exploited &amp; critical vulnerabilities under NIS2/CRA"
        helpSection="euvd-explorer"
      />

      {/* ── Stats bar ── */}
      {stats && (
        <Box sx={{ display: 'flex', gap: 3, mb: 2.5, flexWrap: 'wrap' }}>
          {[
            { label: 'Total',     value: stats.total.toLocaleString() },
            { label: 'Exploited', value: stats.exploited.toLocaleString(), icon: <WarningAmberOutlined sx={{ fontSize: 14, color: '#ff6b6b', verticalAlign: 'middle' }} /> },
            { label: 'Critical',  value: stats.critical.toLocaleString(),  icon: <BugReportOutlined sx={{ fontSize: 14, color: '#ed6c02', verticalAlign: 'middle' }} /> },
            { label: 'With CVSS', value: stats.with_cvss.toLocaleString() },
            { label: 'Source',    value: 'ENISA EUVD',                      icon: <LanguageOutlined sx={{ fontSize: 14, color: '#003399', verticalAlign: 'middle' }} /> },
          ].map(s => (
            <Box key={s.label}>
              <Typography variant="h6" sx={{ fontWeight: 700, color: INTEL_COLOR, lineHeight: 1 }}>
                {s.icon} {s.value}
              </Typography>
              <Typography variant="caption" color="text.secondary">{s.label}</Typography>
            </Box>
          ))}
        </Box>
      )}

      {/* ── Layout: table + detail ── */}
      <Box sx={{ display: 'flex', height: 'calc(100vh - 260px)', gap: 1.5, overflow: 'hidden' }}>
        {/* Table panel */}
        <Box sx={{ flex: 1, display: 'flex', flexDirection: 'column', minWidth: 0 }}>
          {/* Filters */}
          <Box sx={{ display: 'flex', gap: 1, mb: 1.5, alignItems: 'center', flexWrap: 'wrap' }}>
            <TextField
              size="small"
              placeholder="Search EUVD ID, CVE, description, vendor…"
              value={searchInput}
              onChange={e => setSearchInput(e.target.value)}
              onKeyDown={e => e.key === 'Enter' && handleSearch()}
              InputProps={{ startAdornment: <InputAdornment position="start"><SearchOutlined sx={{ fontSize: 16 }} /></InputAdornment> }}
              sx={{ flex: 1, minWidth: 220, '& .MuiInputBase-root': { fontSize: '0.8rem' } }}
            />
            <Select
              size="small"
              value={minScore}
              onChange={e => { setMinScore(e.target.value as string); setPage(1) }}
              displayEmpty
              sx={{ fontSize: '0.78rem', minWidth: 130 }}
            >
              <MenuItem value="" sx={{ fontSize: '0.78rem' }}>Any Score</MenuItem>
              <MenuItem value="9" sx={{ fontSize: '0.78rem' }}>Critical (9+)</MenuItem>
              <MenuItem value="7" sx={{ fontSize: '0.78rem' }}>High+ (7+)</MenuItem>
              <MenuItem value="4" sx={{ fontSize: '0.78rem' }}>Medium+ (4+)</MenuItem>
            </Select>
            <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.5 }}>
              <Switch size="small" checked={exploitedOnly}
                onChange={e => { setExploited(e.target.checked); setPage(1) }} />
              <Typography variant="caption">Exploited only</Typography>
            </Box>
          </Box>

          {/* Table */}
          <Box sx={{ flex: 1, overflowY: 'auto', border: '1px solid', borderColor: 'divider', borderRadius: 1 }}>
            <Table size="small" stickyHeader>
              <TableHead>
                <TableRow>
                  {['EUVD ID', 'CVE', 'Description', 'Score', 'EPSS', 'Date', 'Flags'].map(h => (
                    <TableCell key={h} sx={{ fontWeight: 600, fontSize: '0.72rem', bgcolor: 'background.paper' }}>{h}</TableCell>
                  ))}
                </TableRow>
              </TableHead>
              <TableBody>
                {isLoading && (
                  <TableRow>
                    <TableCell colSpan={7} sx={{ textAlign: 'center', py: 3 }}>
                      <CircularProgress size={20} />
                    </TableCell>
                  </TableRow>
                )}
                {!isLoading && data?.items.map(entry => (
                  <TableRow
                    key={entry.euvd_id}
                    hover
                    selected={selected?.euvd_id === entry.euvd_id}
                    onClick={() => setSelected(entry)}
                    sx={{ cursor: 'pointer' }}
                  >
                    <TableCell sx={{ fontSize: '0.72rem', fontFamily: 'monospace', whiteSpace: 'nowrap' }}>
                      {entry.euvd_id}
                    </TableCell>
                    <TableCell sx={{ fontSize: '0.72rem', fontFamily: 'monospace', whiteSpace: 'nowrap', color: 'text.secondary' }}>
                      {entry.cve_id ?? '—'}
                    </TableCell>
                    <TableCell sx={{ maxWidth: 320 }}>
                      <Typography variant="caption" sx={{
                        display: '-webkit-box', WebkitLineClamp: 2,
                        WebkitBoxOrient: 'vertical', overflow: 'hidden', lineHeight: 1.4,
                      }}>
                        {entry.description ?? '—'}
                      </Typography>
                    </TableCell>
                    <TableCell sx={{ whiteSpace: 'nowrap' }}>
                      {entry.base_score !== null
                        ? <Chip label={entry.base_score.toFixed(1)} size="small"
                            sx={{ fontSize: '0.68rem', height: 18, bgcolor: severityColor(entry.base_score), color: '#fff' }} />
                        : '—'}
                    </TableCell>
                    <TableCell sx={{ fontSize: '0.75rem' }}>
                      {entry.epss_score !== null ? `${(entry.epss_score * 100).toFixed(1)}%` : '—'}
                    </TableCell>
                    <TableCell sx={{ fontSize: '0.75rem', whiteSpace: 'nowrap' }}>
                      {fmtDate(entry.date_published)}
                    </TableCell>
                    <TableCell>
                      <Box sx={{ display: 'flex', gap: 0.3 }}>
                        {entry.is_exploited && (
                          <Tooltip title="Actively Exploited">
                            <WarningAmberOutlined sx={{ fontSize: 14, color: '#ff6b6b' }} />
                          </Tooltip>
                        )}
                        {entry.is_critical && (
                          <Tooltip title="Critical Severity">
                            <BugReportOutlined sx={{ fontSize: 14, color: '#ed6c02' }} />
                          </Tooltip>
                        )}
                      </Box>
                    </TableCell>
                  </TableRow>
                ))}
                {!isLoading && data?.items.length === 0 && (
                  <TableRow>
                    <TableCell colSpan={7} sx={{ textAlign: 'center', py: 3, color: 'text.secondary', fontSize: '0.82rem' }}>
                      No entries. Trigger the EUVD feed from Threat Feeds to populate data.
                    </TableCell>
                  </TableRow>
                )}
              </TableBody>
            </Table>
          </Box>

          {/* Pagination */}
          <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mt: 1 }}>
            <Typography variant="caption" color="text.secondary">
              {data ? `${data.total.toLocaleString()} entries` : ''}
            </Typography>
            <Box sx={{ display: 'flex', gap: 1, alignItems: 'center' }}>
              <Chip label="‹" size="small" disabled={page <= 1}
                onClick={() => setPage(p => p - 1)} sx={{ cursor: page > 1 ? 'pointer' : 'default' }} />
              <Typography variant="caption">{page} / {totalPages}</Typography>
              <Chip label="›" size="small" disabled={page >= totalPages}
                onClick={() => setPage(p => p + 1)} sx={{ cursor: page < totalPages ? 'pointer' : 'default' }} />
            </Box>
          </Box>
        </Box>

        {/* Detail panel */}
        {selected && (
          <Box sx={{
            width: 380, flexShrink: 0,
            border: '1px solid', borderColor: 'divider', borderRadius: 1,
            bgcolor: 'background.paper', overflow: 'hidden',
          }}>
            <EntryDetail entry={selected} onClose={() => setSelected(null)} />
          </Box>
        )}
      </Box>
    </Box>
  )
}
