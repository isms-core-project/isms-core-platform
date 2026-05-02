import { useState } from 'react'
import { useQuery, keepPreviousData } from '@tanstack/react-query'
import {
  Box, Chip, CircularProgress, Collapse, InputAdornment,
  MenuItem, Paper, Select, Table, TableBody, TableCell,
  TableHead, TableRow, TextField, Tooltip, Typography, useTheme,
} from '@mui/material'
import {
  CoronavirusOutlined, ExpandMoreOutlined, ExpandLessOutlined,
  RouterOutlined, SearchOutlined, StreamOutlined, TrackChangesOutlined,
} from '@mui/icons-material'
import PageHeader from '../components/PageHeader'
import { threatIntelApi, IocRead } from '../api/threatIntelApi'

const INTEL_COLOR = '#B84F00'
const PAGE_SIZE = 50

const SOURCE_COLOR: Record<string, string> = {
  circl_misp:      '#B84F00',
  botvrij_misp:    '#8b5a00',
  abuseipdb:       '#1565c0',
  urlhaus:         '#e65100',
  threatfox:       '#b71c1c',
  sslbl:           '#6a1b9a',
  feodotracker:    '#880e4f',
  red_flag_domains:'#c62828',
  stopforumspam:   '#37474f',
  malwarebazaar:   '#e65100',
  alienvault:      '#d84315',
  malpedia:        '#00695c',
}

const SOURCE_LABEL: Record<string, string> = {
  circl_misp:      'CIRCL MISP',
  botvrij_misp:    'Botvrij MISP',
  abuseipdb:       'AbuseIPDB',
  urlhaus:         'URLhaus',
  threatfox:       'ThreatFox',
  sslbl:           'SSLBL',
  feodotracker:    'Feodo Tracker',
  red_flag_domains:'Red Flag Domains',
  stopforumspam:   'StopForumSpam',
  malwarebazaar:   'MalwareBazaar',
  alienvault:      'AlienVault OTX',
  malpedia:        'Malpedia',
}

const TLP_COLOR: Record<string, string> = {
  white: '#9e9e9e',
  green: '#2e7d32',
  amber: '#e65100',
  red:   '#b71c1c',
}

const TYPE_COLOR: Record<string, string> = {
  ip:     '#1565c0',
  domain: '#2e7d32',
  url:    '#6a0dad',
  md5:    '#555',
  sha1:   '#555',
  sha256: '#555',
}

function fmt(iso: string | null): string {
  if (!iso) return '—'
  return iso.slice(0, 10)
}

function IocRow({ ioc }: { ioc: IocRead }) {
  const { palette } = useTheme()
  const isLight = palette.mode === 'light'
  const familyChip  = isLight ? { bg: 'rgba(106,13,173,0.12)', fg: '#4a0080' } : { bg: '#2a0a3a', fg: '#d4b8f0' }
  const actorChip   = isLight ? { bg: 'rgba(68,114,196,0.12)', fg: '#2E5099' } : { bg: '#1a1a2e', fg: '#9fc8f0' }
  const tidChip     = isLight ? { bg: 'rgba(180,100,0,0.12)',  fg: '#7a4800' } : { bg: '#3a1a00', fg: '#ffcc80' }
  const expandBg    = isLight ? 'rgba(180,100,0,0.04)' : 'rgba(184,79,0,0.04)'
  const expandBorder = isLight ? '1px solid rgba(0,0,0,0.08)' : '1px solid rgba(255,255,255,0.06)'
  const [expanded, setExpanded] = useState(false)

  return (
    <>
      <TableRow
        hover
        onClick={() => setExpanded(e => !e)}
        sx={{ cursor: 'pointer' }}
      >
        <TableCell>
          <Chip
            label={ioc.ioc_type}
            size="small"
            sx={{
              fontSize: '0.65rem', height: 18, fontWeight: 700,
              bgcolor: `${TYPE_COLOR[ioc.ioc_type] ?? '#555'}20`,
              color: TYPE_COLOR[ioc.ioc_type] ?? 'text.secondary',
            }}
          />
        </TableCell>
        <TableCell sx={{ fontFamily: 'monospace', fontSize: '0.77rem', maxWidth: 320, overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
          {ioc.value}
        </TableCell>
        <TableCell>
          <Chip
            label={SOURCE_LABEL[ioc.source] ?? ioc.source}
            size="small"
            sx={{
              fontSize: '0.65rem', height: 18,
              bgcolor: `${SOURCE_COLOR[ioc.source] ?? '#555'}20`,
              color: SOURCE_COLOR[ioc.source] ?? 'text.secondary',
            }}
          />
        </TableCell>
        <TableCell sx={{ fontSize: '0.75rem' }}>
          {ioc.confidence !== null
            ? <Chip label={`${ioc.confidence}%`} size="small" color={ioc.confidence >= 80 ? 'error' : 'warning'} sx={{ fontSize: '0.65rem', height: 18 }} />
            : <Typography variant="caption" color="text.secondary">—</Typography>
          }
        </TableCell>
        <TableCell>
          {ioc.tlp
            ? <Chip label={`TLP:${ioc.tlp.toUpperCase()}`} size="small"
                sx={{ fontSize: '0.62rem', height: 18, fontWeight: 700,
                      bgcolor: `${TLP_COLOR[ioc.tlp] ?? '#555'}20`,
                      color: TLP_COLOR[ioc.tlp] ?? 'text.secondary' }} />
            : <Typography variant="caption" color="text.secondary">—</Typography>
          }
        </TableCell>
        <TableCell sx={{ fontSize: '0.75rem', color: 'text.secondary', fontFamily: 'monospace' }}>
          {fmt(ioc.last_seen)}
        </TableCell>
        <TableCell>
          <Box sx={{ display: 'flex', gap: 0.5, flexWrap: 'wrap' }}>
            {ioc.family_slugs.slice(0, 2).map(s => (
              <Chip key={s} icon={<CoronavirusOutlined sx={{ fontSize: 11 }} />}
                label={s} size="small"
                sx={{ fontSize: '0.62rem', height: 16, bgcolor: familyChip.bg, color: familyChip.fg }} />
            ))}
            {ioc.actor_slugs.slice(0, 2).map(s => (
              <Chip key={s} icon={<StreamOutlined sx={{ fontSize: 11 }} />}
                label={s} size="small"
                sx={{ fontSize: '0.62rem', height: 16, bgcolor: actorChip.bg, color: actorChip.fg }} />
            ))}
            {ioc.mitre_tids.slice(0, 3).map(t => (
              <Chip key={t} label={t} size="small"
                sx={{ fontSize: '0.62rem', height: 16, bgcolor: tidChip.bg, color: tidChip.fg }} />
            ))}
          </Box>
        </TableCell>
        <TableCell sx={{ width: 24, p: 0.5 }}>
          {expanded ? <ExpandLessOutlined sx={{ fontSize: 16, color: 'text.secondary' }} />
                    : <ExpandMoreOutlined sx={{ fontSize: 16, color: 'text.secondary' }} />}
        </TableCell>
      </TableRow>

      {/* Expanded detail */}
      <TableRow>
        <TableCell colSpan={8} sx={{ p: 0, border: 'none' }}>
          <Collapse in={expanded} timeout="auto" unmountOnExit>
            <Box sx={{ px: 3, py: 1.5, bgcolor: expandBg, borderBottom: expandBorder }}>
              <Box sx={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(200px, 1fr))', gap: 1.5 }}>
                <Box>
                  <Typography variant="caption" color="text.secondary" display="block">Full value</Typography>
                  <Typography variant="caption" sx={{ fontFamily: 'monospace', wordBreak: 'break-all' }}>{ioc.value}</Typography>
                </Box>
                {ioc.first_seen && (
                  <Box>
                    <Typography variant="caption" color="text.secondary" display="block">First seen</Typography>
                    <Typography variant="caption">{fmt(ioc.first_seen)}</Typography>
                  </Box>
                )}
                {ioc.family_slugs.length > 0 && (
                  <Box>
                    <Typography variant="caption" color="text.secondary" display="block">Malware families</Typography>
                    <Box sx={{ display: 'flex', gap: 0.5, flexWrap: 'wrap', mt: 0.25 }}>
                      {ioc.family_slugs.map(s => <Chip key={s} label={s} size="small" sx={{ fontSize: '0.62rem', height: 16 }} />)}
                    </Box>
                  </Box>
                )}
                {ioc.actor_slugs.length > 0 && (
                  <Box>
                    <Typography variant="caption" color="text.secondary" display="block">Threat actors</Typography>
                    <Box sx={{ display: 'flex', gap: 0.5, flexWrap: 'wrap', mt: 0.25 }}>
                      {ioc.actor_slugs.map(s => <Chip key={s} label={s} size="small" sx={{ fontSize: '0.62rem', height: 16 }} />)}
                    </Box>
                  </Box>
                )}
                {ioc.mitre_tids.length > 0 && (
                  <Box>
                    <Typography variant="caption" color="text.secondary" display="block">ATT&CK TIDs</Typography>
                    <Box sx={{ display: 'flex', gap: 0.5, flexWrap: 'wrap', mt: 0.25 }}>
                      {ioc.mitre_tids.map(t => <Chip key={t} label={t} size="small" sx={{ fontSize: '0.62rem', height: 16, bgcolor: '#3a1a00', color: '#ffcc80' }} />)}
                    </Box>
                  </Box>
                )}
                {ioc.tags.length > 0 && (
                  <Box sx={{ gridColumn: '1 / -1' }}>
                    <Typography variant="caption" color="text.secondary" display="block">Tags ({ioc.tags.length})</Typography>
                    <Box sx={{ display: 'flex', gap: 0.5, flexWrap: 'wrap', mt: 0.25, maxHeight: 60, overflow: 'hidden' }}>
                      {ioc.tags.slice(0, 12).map((t, i) => (
                        <Chip key={i} label={typeof t === 'string' ? t.split('"').slice(-2, -1)[0] ?? t : String(t)}
                          size="small" sx={{ fontSize: '0.6rem', height: 14 }} />
                      ))}
                    </Box>
                  </Box>
                )}
              </Box>
            </Box>
          </Collapse>
        </TableCell>
      </TableRow>
    </>
  )
}

export default function IocExplorer() {
  const [q, setQ] = useState('')
  const [iocType, setIocType] = useState('')
  const [source, setSource] = useState('')
  const [page, setPage] = useState(0)

  const debouncedQ = q  // simple — react-query handles re-fetch on change

  const { data, isLoading } = useQuery({
    queryKey: ['threat-intel', 'iocs', debouncedQ, iocType, source, page],
    queryFn: () => threatIntelApi.getIocs({
      q: q || undefined,
      ioc_type: iocType || undefined,
      source: source || undefined,
      skip: page * PAGE_SIZE,
      limit: PAGE_SIZE,
    }),
    staleTime: 30_000,
    placeholderData: keepPreviousData,
  })

  const total = data?.total ?? 0
  const totalPages = Math.ceil(total / PAGE_SIZE)

  return (
    <Box sx={{ p: 3, display: 'flex', flexDirection: 'column', gap: 2 }}>
      <PageHeader
        title="IOC Explorer"
        subtitle={`Indicators of compromise from MISP, Abuse.ch, AbuseIPDB, AlienVault OTX and reputation feeds${total ? ` — ${total.toLocaleString()} total` : ''}`}
      />

      {/* ── Filters ── */}
      <Box sx={{ display: 'flex', gap: 1.5, flexWrap: 'wrap', alignItems: 'center' }}>
        <TextField
          size="small"
          placeholder="Search value…"
          value={q}
          onChange={e => { setQ(e.target.value); setPage(0) }}
          InputProps={{ startAdornment: <InputAdornment position="start"><SearchOutlined sx={{ fontSize: 16 }} /></InputAdornment> }}
          sx={{ width: 260 }}
        />
        <Select size="small" value={iocType} onChange={e => { setIocType(e.target.value); setPage(0) }} displayEmpty sx={{ minWidth: 120, fontSize: '0.82rem' }}>
          <MenuItem value="">All types</MenuItem>
          {['ip', 'domain', 'url', 'md5', 'sha1', 'sha256'].map(t => (
            <MenuItem key={t} value={t} sx={{ fontSize: '0.82rem' }}>{t}</MenuItem>
          ))}
        </Select>
        <Select size="small" value={source} onChange={e => { setSource(e.target.value); setPage(0) }} displayEmpty sx={{ minWidth: 150, fontSize: '0.82rem' }}>
          <MenuItem value="">All sources</MenuItem>
          <MenuItem value="circl_misp" sx={{ fontSize: '0.82rem' }}>CIRCL MISP</MenuItem>
          <MenuItem value="botvrij_misp" sx={{ fontSize: '0.82rem' }}>Botvrij MISP</MenuItem>
          <MenuItem value="abuseipdb" sx={{ fontSize: '0.82rem' }}>AbuseIPDB</MenuItem>
          <MenuItem value="urlhaus" sx={{ fontSize: '0.82rem' }}>URLhaus</MenuItem>
          <MenuItem value="threatfox" sx={{ fontSize: '0.82rem' }}>ThreatFox</MenuItem>
          <MenuItem value="sslbl" sx={{ fontSize: '0.82rem' }}>SSLBL</MenuItem>
          <MenuItem value="feodotracker" sx={{ fontSize: '0.82rem' }}>Feodo Tracker</MenuItem>
          <MenuItem value="red_flag_domains" sx={{ fontSize: '0.82rem' }}>Red Flag Domains</MenuItem>
          <MenuItem value="stopforumspam" sx={{ fontSize: '0.82rem' }}>StopForumSpam</MenuItem>
          <MenuItem value="malwarebazaar" sx={{ fontSize: '0.82rem' }}>MalwareBazaar</MenuItem>
          <MenuItem value="alienvault" sx={{ fontSize: '0.82rem' }}>AlienVault OTX</MenuItem>
          <MenuItem value="malpedia" sx={{ fontSize: '0.82rem' }}>Malpedia</MenuItem>
        </Select>
        <Typography variant="caption" color="text.secondary" sx={{ ml: 'auto' }}>
          {total.toLocaleString()} results
          {totalPages > 1 && ` · page ${page + 1}/${totalPages}`}
        </Typography>
        {page > 0 && <Chip label="← Prev" size="small" onClick={() => setPage(p => p - 1)} sx={{ cursor: 'pointer' }} />}
        {page < totalPages - 1 && <Chip label="Next →" size="small" onClick={() => setPage(p => p + 1)} sx={{ cursor: 'pointer' }} />}
      </Box>

      {/* ── Table ── */}
      <Paper variant="outlined">
        {isLoading && (
          <Box sx={{ display: 'flex', justifyContent: 'center', p: 4 }}>
            <CircularProgress size={28} sx={{ color: INTEL_COLOR }} />
          </Box>
        )}
        {!isLoading && (
          <Table size="small">
            <TableHead>
              <TableRow>
                <TableCell sx={{ fontWeight: 700, fontSize: '0.75rem', width: 70 }}>Type</TableCell>
                <TableCell sx={{ fontWeight: 700, fontSize: '0.75rem' }}>Value</TableCell>
                <TableCell sx={{ fontWeight: 700, fontSize: '0.75rem', width: 130 }}>Source</TableCell>
                <TableCell sx={{ fontWeight: 700, fontSize: '0.75rem', width: 80 }}>Confidence</TableCell>
                <TableCell sx={{ fontWeight: 700, fontSize: '0.75rem', width: 90 }}>TLP</TableCell>
                <TableCell sx={{ fontWeight: 700, fontSize: '0.75rem', width: 90 }}>Last seen</TableCell>
                <TableCell sx={{ fontWeight: 700, fontSize: '0.75rem' }}>Attribution</TableCell>
                <TableCell sx={{ width: 24 }} />
              </TableRow>
            </TableHead>
            <TableBody>
              {(data?.items ?? []).length === 0 ? (
                <TableRow>
                  <TableCell colSpan={8}>
                    <Typography variant="body2" color="text.secondary" align="center" sx={{ py: 4 }}>
                      No IOCs found. Feeds may still be loading on first boot.
                    </Typography>
                  </TableCell>
                </TableRow>
              ) : (
                (data?.items ?? []).map(ioc => <IocRow key={ioc.id} ioc={ioc} />)
              )}
            </TableBody>
          </Table>
        )}
      </Paper>
    </Box>
  )
}
