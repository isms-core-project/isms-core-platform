import { useState } from 'react'
import {
  Alert, Box, Chip, CircularProgress, InputAdornment, Paper,
  Table, TableBody, TableCell, TableHead, TableRow, TextField,
  ToggleButton, ToggleButtonGroup, Tooltip, Typography,
} from '@mui/material'
import { SearchOutlined } from '@mui/icons-material'
import { useQuery } from '@tanstack/react-query'
import { feedsApi, type MitreCampaign } from '../api/feedsApi'
import PageHeader from '../components/PageHeader'

const PER_PAGE = 50
const INTEL_COLOR = '#B84F00'

export default function MitreCampaigns() {
  const [source, setSource] = useState<'attack_v18' | 'attack_v19'>('attack_v18')
  const [search, setSearch] = useState('')
  const [page, setPage] = useState(1)
  const [selected, setSelected] = useState<MitreCampaign | null>(null)

  const { data, isLoading, error } = useQuery({
    queryKey: ['feeds', 'campaigns', source, search, page],
    queryFn: () => feedsApi.getMitreCampaigns({
      source,
      search: search || undefined,
      deprecated: false,
      page,
      per_page: PER_PAGE,
    }),
  })

  const totalPages = data ? Math.ceil(data.total / PER_PAGE) : 0

  function handleSearch(v: string) {
    setSearch(v)
    setPage(1)
  }

  const noData = !isLoading && data?.total === 0

  return (
    <Box sx={{ p: 3 }}>
      <PageHeader
        title="MITRE ATT&CK Campaigns"
        subtitle="Targeted intrusion activity clusters — time-bound adversary operations"
        helpSection="mitre-attack"
      />

      {/* ── Total pill ── */}
      {data && (
        <Box sx={{ display: 'flex', gap: 3, mb: 2.5 }}>
          <Box>
            <Typography variant="h6" sx={{ fontWeight: 700, color: INTEL_COLOR, lineHeight: 1 }}>
              {data.total.toLocaleString()}
            </Typography>
            <Typography variant="caption" color="text.secondary">Campaigns</Typography>
          </Box>
        </Box>
      )}

      {/* ── Filters ── */}
      <Box sx={{ display: 'flex', gap: 1.5, mb: 2, flexWrap: 'wrap', alignItems: 'center' }}>
        <ToggleButtonGroup
          size="small"
          value={source}
          exclusive
          onChange={(_, v) => v && setSource(v)}
        >
          <ToggleButton value="attack_v18" sx={{ fontSize: '0.72rem', px: 1.5 }}>v18</ToggleButton>
          <ToggleButton value="attack_v19" sx={{ fontSize: '0.72rem', px: 1.5 }}>v19</ToggleButton>
        </ToggleButtonGroup>

        <TextField
          size="small"
          placeholder="Search by ID or name…"
          value={search}
          onChange={e => handleSearch(e.target.value)}
          sx={{ width: 240 }}
          InputProps={{
            startAdornment: <InputAdornment position="start"><SearchOutlined sx={{ fontSize: 16 }} /></InputAdornment>,
          }}
        />
      </Box>

      {/* ── Table + detail panel ── */}
      <Box sx={{ display: 'flex', gap: 2 }}>
        <Paper variant="outlined" sx={{ flex: 1, borderRadius: 2, overflow: 'hidden', minWidth: 0 }}>
          {isLoading && (
            <Box sx={{ display: 'flex', justifyContent: 'center', py: 6 }}>
              <CircularProgress size={28} />
            </Box>
          )}
          {error && <Alert severity="error" sx={{ m: 2 }}>Failed to load campaigns</Alert>}
          {noData && (
            <Alert severity="info" sx={{ m: 2 }}>
              {source === 'attack_v19'
                ? 'ATT&CK v19 data not yet available. Check back after the scheduled weekly pull.'
                : 'No campaigns match the current filters.'}
            </Alert>
          )}
          {!isLoading && data && data.items.length > 0 && (
            <>
              <Table size="small" stickyHeader>
                <TableHead>
                  <TableRow>
                    <TableCell sx={{ fontWeight: 600, fontSize: '0.72rem', width: 80 }}>ID</TableCell>
                    <TableCell sx={{ fontWeight: 600, fontSize: '0.72rem' }}>Name</TableCell>
                    <TableCell sx={{ fontWeight: 600, fontSize: '0.72rem', width: 100 }}>First Seen</TableCell>
                    <TableCell sx={{ fontWeight: 600, fontSize: '0.72rem', width: 100 }}>Last Seen</TableCell>
                    <TableCell sx={{ fontWeight: 600, fontSize: '0.72rem' }}>Aliases</TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                  {data.items.map(c => (
                    <TableRow
                      key={c.id}
                      hover
                      selected={selected?.id === c.id}
                      onClick={() => setSelected(selected?.id === c.id ? null : c)}
                      sx={{ cursor: 'pointer' }}
                    >
                      <TableCell sx={{ fontFamily: 'monospace', fontSize: '0.75rem', color: INTEL_COLOR, fontWeight: 600 }}>
                        {c.campaign_id}
                      </TableCell>
                      <TableCell sx={{ fontSize: '0.78rem' }}>
                        <Typography noWrap variant="inherit">{c.name}</Typography>
                      </TableCell>
                      <TableCell sx={{ fontSize: '0.75rem', fontFamily: 'monospace' }}>
                        {c.first_seen ?? '—'}
                      </TableCell>
                      <TableCell sx={{ fontSize: '0.75rem', fontFamily: 'monospace' }}>
                        {c.last_seen ?? '—'}
                      </TableCell>
                      <TableCell sx={{ maxWidth: 200 }}>
                        {c.aliases.length > 0 ? (
                          <Box>
                            {c.aliases.slice(0, 2).map(a => (
                              <Chip key={a} label={a} size="small" variant="outlined"
                                sx={{ fontSize: '0.62rem', height: 16, mr: 0.25, mb: 0.25 }} />
                            ))}
                            {c.aliases.length > 2 && (
                              <Tooltip title={c.aliases.slice(2).join(', ')}>
                                <Chip label={`+${c.aliases.length - 2}`} size="small"
                                  sx={{ fontSize: '0.62rem', height: 16 }} />
                              </Tooltip>
                            )}
                          </Box>
                        ) : (
                          <Typography variant="caption" color="text.disabled">—</Typography>
                        )}
                      </TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>

              {/* Pagination */}
              <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', px: 2, py: 1, borderTop: '1px solid', borderColor: 'divider' }}>
                <Typography variant="caption" color="text.secondary">
                  {data.total.toLocaleString()} campaigns
                </Typography>
                <Box sx={{ display: 'flex', gap: 1, alignItems: 'center' }}>
                  <Typography
                    variant="caption"
                    sx={{ cursor: page > 1 ? 'pointer' : 'default', color: page > 1 ? 'primary.main' : 'text.disabled' }}
                    onClick={() => page > 1 && setPage(p => p - 1)}
                  >
                    ← Prev
                  </Typography>
                  <Typography variant="caption" color="text.secondary">
                    {page} / {totalPages}
                  </Typography>
                  <Typography
                    variant="caption"
                    sx={{ cursor: page < totalPages ? 'pointer' : 'default', color: page < totalPages ? 'primary.main' : 'text.disabled' }}
                    onClick={() => page < totalPages && setPage(p => p + 1)}
                  >
                    Next →
                  </Typography>
                </Box>
              </Box>
            </>
          )}
        </Paper>

        {/* ── Detail panel ── */}
        {selected && (
          <Paper variant="outlined" sx={{ width: 320, flexShrink: 0, borderRadius: 2, p: 2, height: 'fit-content', position: 'sticky', top: 24 }}>
            <Typography variant="subtitle2" sx={{ fontFamily: 'monospace', color: INTEL_COLOR, fontWeight: 700, mb: 0.5 }}>
              {selected.campaign_id}
            </Typography>
            <Typography variant="body2" fontWeight={600} sx={{ mb: 1 }}>{selected.name}</Typography>
            <Box sx={{ display: 'flex', gap: 2, mb: 1 }}>
              {selected.first_seen && (
                <Box>
                  <Typography variant="caption" color="text.secondary" display="block">First seen</Typography>
                  <Typography variant="caption" fontFamily="monospace">{selected.first_seen}</Typography>
                </Box>
              )}
              {selected.last_seen && (
                <Box>
                  <Typography variant="caption" color="text.secondary" display="block">Last seen</Typography>
                  <Typography variant="caption" fontFamily="monospace">{selected.last_seen}</Typography>
                </Box>
              )}
            </Box>
            {selected.aliases.length > 0 && (
              <Box sx={{ mb: 1 }}>
                <Typography variant="caption" color="text.secondary" display="block" sx={{ mb: 0.5 }}>Also known as:</Typography>
                {selected.aliases.map(a => (
                  <Chip key={a} label={a} size="small" variant="outlined"
                    sx={{ fontSize: '0.62rem', height: 16, mr: 0.25, mb: 0.25 }} />
                ))}
              </Box>
            )}
            {selected.description && (
              <Typography variant="caption" color="text.secondary" display="block" sx={{ mt: 1.5, lineHeight: 1.5, maxHeight: 300, overflowY: 'auto' }}>
                {selected.description.slice(0, 700)}{selected.description.length > 700 ? '…' : ''}
              </Typography>
            )}
            {selected.url && (
              <Typography variant="caption" sx={{ mt: 1, display: 'block' }}>
                <a href={selected.url} target="_blank" rel="noopener noreferrer"
                  style={{ color: INTEL_COLOR }}>
                  View on attack.mitre.org →
                </a>
              </Typography>
            )}
          </Paper>
        )}
      </Box>
    </Box>
  )
}
