import { useState } from 'react'
import { useTheme } from '@mui/material/styles'
import { useMutation } from '@tanstack/react-query'
import {
  Alert, Box, Chip, CircularProgress, Divider, InputAdornment,
  Paper, Table, TableBody, TableCell, TableHead, TableRow,
  TextField, Tooltip, Typography,
} from '@mui/material'
import {
  CheckCircleOutlined, CoronavirusOutlined, DnsOutlined, RouterOutlined,
  SearchOutlined, StreamOutlined, WarningAmberOutlined,
} from '@mui/icons-material'
import PageHeader from '../components/PageHeader'
import { threatIntelApi, EnrichIpResponse, IocRead } from '../api/threatIntelApi'

const INTEL_COLOR = '#B84F00'

function ConfidenceBar({ score }: { score: number }) {
  const { palette } = useTheme()
  const isLight = palette.mode === 'light'
  const color = score >= 80 ? '#d32f2f' : score >= 50 ? '#ed6c02' : score >= 25 ? '#f9a825' : '#388e3c'
  return (
    <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
      <Box sx={{ flex: 1, height: 6, bgcolor: isLight ? 'rgba(0,0,0,0.08)' : 'rgba(255,255,255,0.08)', borderRadius: 3, overflow: 'hidden' }}>
        <Box sx={{ height: '100%', width: `${score}%`, bgcolor: color, borderRadius: 3, transition: 'width 0.4s' }} />
      </Box>
      <Typography variant="caption" fontWeight={700} sx={{ color, minWidth: 32 }}>{score}%</Typography>
    </Box>
  )
}

function AbuseCard({ data }: { data: Record<string, unknown> }) {
  if (!data || typeof data !== 'object') return null
  const score = Number(data.abuseConfidenceScore ?? 0)
  const rows: [string, string][] = [
    ['ISP / ASN', String(data.isp ?? data.asn ?? '—')],
    ['Usage type', String(data.usageType ?? '—')],
    ['Country', String(data.countryCode ?? '—')],
    ['Domain', String(data.domain ?? '—')],
    ['Total reports', String(data.totalReports ?? '—')],
    ['Last reported', String((data.lastReportedAt ?? '—')).slice(0, 10)],
  ]

  return (
    <Paper variant="outlined" sx={{ p: 2, flex: 1 }}>
      <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 1.5 }}>
        <RouterOutlined sx={{ fontSize: 20, color: '#1565c0' }} />
        <Typography variant="subtitle2" fontWeight={700} sx={{ fontSize: '0.85rem' }}>AbuseIPDB</Typography>
      </Box>
      <Box sx={{ mb: 1.5 }}>
        <Typography variant="caption" color="text.secondary" display="block" sx={{ mb: 0.5 }}>Abuse confidence score</Typography>
        <ConfidenceBar score={score} />
      </Box>
      <Divider sx={{ my: 1 }} />
      {rows.map(([k, v]) => (
        <Box key={k} sx={{ display: 'flex', justifyContent: 'space-between', py: 0.25 }}>
          <Typography variant="caption" color="text.secondary">{k}</Typography>
          <Typography variant="caption" fontWeight={500}>{v}</Typography>
        </Box>
      ))}
    </Paper>
  )
}

function ShodanCard({ data }: { data: Record<string, unknown> }) {
  if (!data || typeof data !== 'object') return null
  const ports: number[] = Array.isArray(data.ports) ? data.ports : []
  const cves: string[] = Array.isArray(data.cves) ? data.cves : []
  const hostnames: string[] = Array.isArray(data.hostnames) ? data.hostnames : []
  const source = String(data.source ?? 'shodan')

  return (
    <Paper variant="outlined" sx={{ p: 2, flex: 1 }}>
      <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 1.5 }}>
        <StreamOutlined sx={{ fontSize: 20, color: '#B84F00' }} />
        <Typography variant="subtitle2" fontWeight={700} sx={{ fontSize: '0.85rem' }}>
          Shodan {source === 'shodan_internetdb' ? '(InternetDB)' : '(API)'}
        </Typography>
      </Box>

      {hostnames.length > 0 && (
        <Box sx={{ mb: 1 }}>
          <Typography variant="caption" color="text.secondary" display="block">Hostnames</Typography>
          <Typography variant="caption" sx={{ fontFamily: 'monospace' }}>{hostnames.slice(0, 3).join(', ')}</Typography>
        </Box>
      )}

      {!!(data.org || data.asn) && (
        <Box sx={{ mb: 1 }}>
          <Typography variant="caption" color="text.secondary" display="block">Org / ASN</Typography>
          <Typography variant="caption">{[String(data.org ?? ''), String(data.asn ?? '')].filter(s => s).join(' · ')}</Typography>
        </Box>
      )}

      {ports.length > 0 && (
        <Box sx={{ mb: 1 }}>
          <Typography variant="caption" color="text.secondary" display="block" sx={{ mb: 0.5 }}>Open ports ({ports.length})</Typography>
          <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 0.5 }}>
            {ports.slice(0, 20).map(p => (
              <Chip key={p} label={p} size="small" sx={{ fontSize: '0.65rem', height: 18, fontFamily: 'monospace' }} />
            ))}
            {ports.length > 20 && <Chip label={`+${ports.length - 20}`} size="small" sx={{ fontSize: '0.65rem', height: 18 }} />}
          </Box>
        </Box>
      )}

      {cves.length > 0 && (
        <Box>
          <Typography variant="caption" color="text.secondary" display="block" sx={{ mb: 0.5 }}>
            CVEs detected ({cves.length})
          </Typography>
          <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 0.5 }}>
            {cves.slice(0, 10).map(c => (
              <Chip key={c} label={c} size="small" color="error"
                icon={<WarningAmberOutlined sx={{ fontSize: 11 }} />}
                sx={{ fontSize: '0.62rem', height: 18 }} />
            ))}
            {cves.length > 10 && <Chip label={`+${cves.length - 10}`} size="small" sx={{ fontSize: '0.62rem', height: 18 }} />}
          </Box>
        </Box>
      )}
    </Paper>
  )
}

function GoogleDnsCard({ data }: { data: Record<string, unknown> }) {
  const { palette } = useTheme()
  const isLight = palette.mode === 'light'
  if (!data || typeof data !== 'object') return null
  const ptr: string[] = Array.isArray(data.ptr) ? data.ptr : []
  const status = Number(data.status ?? -1)
  const noRecord = status === 3 || ptr.length === 0

  return (
    <Paper variant="outlined" sx={{ p: 2, flex: 1 }}>
      <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 1.5 }}>
        <DnsOutlined sx={{ fontSize: 20, color: '#1976d2' }} />
        <Typography variant="subtitle2" fontWeight={700} sx={{ fontSize: '0.85rem' }}>Google DNS (PTR)</Typography>
      </Box>
      {noRecord ? (
        <Typography variant="caption" color="text.secondary">No PTR record — IP has no reverse DNS entry</Typography>
      ) : (
        <Box>
          <Typography variant="caption" color="text.secondary" display="block" sx={{ mb: 0.5 }}>Reverse hostname(s)</Typography>
          {ptr.map(h => (
            <Typography key={h} variant="caption" sx={{ fontFamily: 'monospace', display: 'block', color: isLight ? '#1565c0' : '#90caf9' }}>{h}</Typography>
          ))}
        </Box>
      )}
    </Paper>
  )
}

function IocHitsTable({ hits }: { hits: IocRead[] }) {
  const { palette } = useTheme()
  const isLight = palette.mode === 'light'
  if (hits.length === 0) return (
    <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, py: 1 }}>
      <CheckCircleOutlined sx={{ fontSize: 16, color: '#388e3c' }} />
      <Typography variant="caption" color="text.secondary">No IOC hits — IP not seen in MISP or AbuseIPDB feeds.</Typography>
    </Box>
  )

  return (
    <Table size="small">
      <TableHead>
        <TableRow>
          <TableCell sx={{ fontWeight: 700, fontSize: '0.72rem' }}>Source</TableCell>
          <TableCell sx={{ fontWeight: 700, fontSize: '0.72rem' }}>Families</TableCell>
          <TableCell sx={{ fontWeight: 700, fontSize: '0.72rem' }}>Actors</TableCell>
          <TableCell sx={{ fontWeight: 700, fontSize: '0.72rem' }}>TIDs</TableCell>
          <TableCell sx={{ fontWeight: 700, fontSize: '0.72rem' }}>Last seen</TableCell>
        </TableRow>
      </TableHead>
      <TableBody>
        {hits.map(h => (
          <TableRow key={h.id}>
            <TableCell>
              <Chip label={h.source.replace('_misp', ' MISP')} size="small"
                sx={{ fontSize: '0.65rem', height: 18 }} />
            </TableCell>
            <TableCell>
              <Box sx={{ display: 'flex', gap: 0.5 }}>
                {h.family_slugs.slice(0, 2).map(s => (
                  <Chip key={s} icon={<CoronavirusOutlined sx={{ fontSize: 11 }} />}
                    label={s} size="small"
                    sx={{ fontSize: '0.62rem', height: 16, bgcolor: isLight ? 'rgba(106,27,154,0.12)' : '#2a0a3a', color: isLight ? '#6a1b9a' : '#d4b8f0' }} />
                ))}
              </Box>
            </TableCell>
            <TableCell>
              <Box sx={{ display: 'flex', gap: 0.5 }}>
                {h.actor_slugs.slice(0, 2).map(s => (
                  <Chip key={s} label={s} size="small"
                    sx={{ fontSize: '0.62rem', height: 16, bgcolor: isLight ? 'rgba(21,101,192,0.12)' : '#1a1a2e', color: isLight ? '#1565c0' : '#9fc8f0' }} />
                ))}
              </Box>
            </TableCell>
            <TableCell>
              <Box sx={{ display: 'flex', gap: 0.5 }}>
                {h.mitre_tids.slice(0, 3).map(t => (
                  <Chip key={t} label={t} size="small"
                    sx={{ fontSize: '0.62rem', height: 16, bgcolor: isLight ? 'rgba(230,145,0,0.12)' : '#3a1a00', color: isLight ? '#9a6500' : '#ffcc80' }} />
                ))}
              </Box>
            </TableCell>
            <TableCell sx={{ fontSize: '0.75rem', fontFamily: 'monospace', color: 'text.secondary' }}>
              {h.last_seen?.slice(0, 10) ?? '—'}
            </TableCell>
          </TableRow>
        ))}
      </TableBody>
    </Table>
  )
}

export default function IpEnrichment() {
  const [ip, setIp] = useState('')
  const [submittedIp, setSubmittedIp] = useState('')

  const mutation = useMutation({
    mutationFn: (ipAddr: string) => threatIntelApi.enrichIp(ipAddr),
  })

  function handleSubmit(e: React.FormEvent) {
    e.preventDefault()
    const trimmed = ip.trim()
    if (!trimmed) return
    setSubmittedIp(trimmed)
    mutation.mutate(trimmed)
  }

  const result: EnrichIpResponse | undefined = mutation.data

  return (
    <Box sx={{ p: 3, display: 'flex', flexDirection: 'column', gap: 2.5 }}>
      <PageHeader
        title="IP Enrichment"
        subtitle="On-demand AbuseIPDB + Shodan lookup — results cached 24h"
      />

      {/* ── Input ── */}
      <Paper variant="outlined" sx={{ p: 2 }}>
        <form onSubmit={handleSubmit}>
          <Box sx={{ display: 'flex', gap: 1.5, alignItems: 'center' }}>
            <TextField
              size="small"
              placeholder="Enter IPv4 or IPv6 address…"
              value={ip}
              onChange={e => setIp(e.target.value)}
              InputProps={{
                startAdornment: <InputAdornment position="start"><RouterOutlined sx={{ fontSize: 16 }} /></InputAdornment>,
                sx: { fontFamily: 'monospace', fontSize: '0.85rem' },
              }}
              sx={{ flex: 1, maxWidth: 400 }}
            />
            <Chip
              label={mutation.isPending ? 'Looking up…' : 'Look up'}
              onClick={handleSubmit}
              icon={mutation.isPending
                ? <CircularProgress size={12} sx={{ color: 'inherit !important' }} />
                : <SearchOutlined sx={{ fontSize: 14 }} />
              }
              sx={{ cursor: 'pointer', fontWeight: 600, px: 0.5 }}
              color="primary"
            />
          </Box>
        </form>
      </Paper>

      {/* ── Error ── */}
      {mutation.isError && (
        <Alert severity="error">
          Enrichment failed — check API keys or try again.
        </Alert>
      )}

      {/* ── Results ── */}
      {result && (
        <Box sx={{ display: 'flex', flexDirection: 'column', gap: 2 }}>
          <Box sx={{ display: 'flex', alignItems: 'center', gap: 1.5 }}>
            <Typography variant="subtitle2" fontWeight={700} sx={{ fontFamily: 'monospace', fontSize: '1rem' }}>
              {result.ip}
            </Typography>
            {result.cached && (
              <Tooltip title={`Cached ${result.cache_age_minutes ?? 0} min ago`}>
                <Chip label="Cached" size="small" sx={{ fontSize: '0.65rem', height: 18 }} />
              </Tooltip>
            )}
          </Box>

          {/* Enrichment cards side by side */}
          <Box sx={{ display: 'flex', gap: 2, flexWrap: 'wrap' }}>
            {result.abuseipdb
              ? <AbuseCard data={result.abuseipdb as Record<string, unknown>} />
              : (
                <Paper variant="outlined" sx={{ p: 2, flex: 1, display: 'flex', alignItems: 'center', gap: 1 }}>
                  <RouterOutlined sx={{ fontSize: 20, color: 'text.disabled' }} />
                  <Typography variant="caption" color="text.secondary">AbuseIPDB — no result</Typography>
                </Paper>
              )
            }
            {result.shodan && !(result.shodan as Record<string, unknown>).not_found
              ? <ShodanCard data={result.shodan as Record<string, unknown>} />
              : (
                <Paper variant="outlined" sx={{ p: 2, flex: 1, display: 'flex', alignItems: 'center', gap: 1 }}>
                  <StreamOutlined sx={{ fontSize: 20, color: 'text.disabled' }} />
                  <Typography variant="caption" color="text.secondary">
                    {result.shodan
                      ? 'Shodan — IP not indexed (no open ports in database)'
                      : 'Shodan — lookup failed'}
                  </Typography>
                </Paper>
              )
            }
            {result.google_dns
              ? <GoogleDnsCard data={result.google_dns as Record<string, unknown>} />
              : (
                <Paper variant="outlined" sx={{ p: 2, flex: 1, display: 'flex', alignItems: 'center', gap: 1 }}>
                  <DnsOutlined sx={{ fontSize: 20, color: 'text.disabled' }} />
                  <Typography variant="caption" color="text.secondary">Google DNS — lookup failed</Typography>
                </Paper>
              )
            }
          </Box>

          {/* IOC hits */}
          <Paper variant="outlined">
            <Box sx={{ px: 2, pt: 1.5, pb: 0.5, display: 'flex', alignItems: 'center', gap: 1 }}>
              <SearchOutlined sx={{ fontSize: 16, color: INTEL_COLOR }} />
              <Typography variant="subtitle2" fontWeight={700} sx={{ fontSize: '0.82rem', color: INTEL_COLOR }}>
                IOC Feed Hits ({result.ioc_hits.length})
              </Typography>
            </Box>
            <Divider />
            <Box sx={{ px: 1 }}>
              <IocHitsTable hits={result.ioc_hits} />
            </Box>
          </Paper>
        </Box>
      )}

      {/* ── Empty state ── */}
      {!result && !mutation.isPending && (
        <Box sx={{ textAlign: 'center', py: 6, color: 'text.secondary' }}>
          <RouterOutlined sx={{ fontSize: 48, opacity: 0.2, mb: 1 }} />
          <Typography variant="body2">Enter an IP address above to check AbuseIPDB confidence score, Shodan open ports, and cross-reference our IOC feeds.</Typography>
        </Box>
      )}
    </Box>
  )
}
