import { useState } from 'react'
import {
  Alert, Box, Chip, CircularProgress, InputAdornment, Paper,
  Table, TableBody, TableCell, TableHead, TableRow, TextField,
  ToggleButton, ToggleButtonGroup, Tooltip, Typography,
} from '@mui/material'
import { SearchOutlined } from '@mui/icons-material'
import { useQuery } from '@tanstack/react-query'
import { feedsApi, type MitreGroup } from '../api/feedsApi'
import PageHeader from '../components/PageHeader'

const PER_PAGE = 50
const INTEL_COLOR = '#B84F00'

export default function MitreGroups() {
  const [source] = useState<'attack_v19'>('attack_v19')
  const [search, setSearch] = useState('')
  const [page, setPage] = useState(1)
  const [selected, setSelected] = useState<MitreGroup | null>(null)

  const { data: stats } = useQuery({
    queryKey: ['feeds', 'groups', 'stats'],
    queryFn: feedsApi.getMitreGroupStats,
  })

  const { data, isLoading, error } = useQuery({
    queryKey: ['feeds', 'groups', source, search, page],
    queryFn: () => feedsApi.getMitreGroups({
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
        title="MITRE ATT&CK Groups"
        subtitle="Threat actor intrusion sets — adversary groups tracked by MITRE ATT&CK"
        helpSection="mitre-attack"
      />

      {/* ── Stats row ── */}
      {stats && (
        <Box sx={{ display: 'flex', gap: 3, mb: 2.5, flexWrap: 'wrap' }}>
          {[
            { label: 'Groups', value: stats.total_groups },
            { label: 'Deprecated', value: stats.deprecated_count },
            { label: 'Sources', value: stats.sources.join(', ') },
          ].map(s => (
            <Box key={s.label}>
              <Typography variant="h6" sx={{ fontWeight: 700, color: INTEL_COLOR, lineHeight: 1 }}>
                {typeof s.value === 'number' ? s.value.toLocaleString() : s.value}
              </Typography>
              <Typography variant="caption" color="text.secondary">{s.label}</Typography>
            </Box>
          ))}
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
          {error && <Alert severity="error" sx={{ m: 2 }}>Failed to load groups</Alert>}
          {noData && (
            <Alert severity="info" sx={{ m: 2 }}>
              {source === 'attack_v19'
                ? 'ATT&CK v19 data not yet available. Check back after the scheduled weekly pull.'
                : 'No groups match the current filters.'}
            </Alert>
          )}
          {!isLoading && data && data.items.length > 0 && (
            <>
              <Table size="small" stickyHeader>
                <TableHead>
                  <TableRow>
                    <TableCell sx={{ fontWeight: 600, fontSize: '0.72rem', width: 80 }}>ID</TableCell>
                    <TableCell sx={{ fontWeight: 600, fontSize: '0.72rem' }}>Name</TableCell>
                    <TableCell sx={{ fontWeight: 600, fontSize: '0.72rem' }}>Aliases</TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                  {data.items.map(g => (
                    <TableRow
                      key={g.id}
                      hover
                      selected={selected?.id === g.id}
                      onClick={() => setSelected(selected?.id === g.id ? null : g)}
                      sx={{ cursor: 'pointer' }}
                    >
                      <TableCell sx={{ fontFamily: 'monospace', fontSize: '0.75rem', color: INTEL_COLOR, fontWeight: 600 }}>
                        {g.group_id}
                      </TableCell>
                      <TableCell sx={{ fontSize: '0.78rem' }}>
                        <Typography noWrap variant="inherit">{g.name}</Typography>
                      </TableCell>
                      <TableCell sx={{ maxWidth: 240 }}>
                        {g.aliases.length > 0 ? (
                          <Box>
                            {g.aliases.slice(0, 3).map(a => (
                              <Chip key={a} label={a} size="small" variant="outlined"
                                sx={{ fontSize: '0.62rem', height: 16, mr: 0.25, mb: 0.25 }} />
                            ))}
                            {g.aliases.length > 3 && (
                              <Tooltip title={g.aliases.slice(3).join(', ')}>
                                <Chip label={`+${g.aliases.length - 3}`} size="small"
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
                  {data.total.toLocaleString()} groups
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
              {selected.group_id}
            </Typography>
            <Typography variant="body2" fontWeight={600} sx={{ mb: 1 }}>{selected.name}</Typography>
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
              <Typography variant="caption" color="text.secondary" display="block" sx={{ mt: 1.5, lineHeight: 1.5, maxHeight: 320, overflowY: 'auto' }}>
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
