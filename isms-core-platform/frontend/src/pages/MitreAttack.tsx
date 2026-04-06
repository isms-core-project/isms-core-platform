import { useState } from 'react'
import {
  Alert, Box, Chip, CircularProgress, FormControl, InputAdornment,
  InputLabel, MenuItem, Paper, Select, Table, TableBody, TableCell,
  TableHead, TableRow, TextField, ToggleButton, ToggleButtonGroup,
  Tooltip, Typography,
} from '@mui/material'
import { SearchOutlined } from '@mui/icons-material'
import { useQuery } from '@tanstack/react-query'
import { feedsApi, type MitreTechnique } from '../api/feedsApi'
import PageHeader from '../components/PageHeader'

const PER_PAGE = 50
const INTEL_COLOR = '#B84F00'

function TacticChip({ tactic }: { tactic: string }) {
  return (
    <Chip
      label={tactic.replace(/-/g, ' ')}
      size="small"
      sx={{ fontSize: '0.65rem', height: 18, mr: 0.25, mb: 0.25, textTransform: 'capitalize' }}
    />
  )
}

function PlatformChips({ platforms }: { platforms: string[] }) {
  if (!platforms.length) return <Typography variant="caption" color="text.disabled">—</Typography>
  return (
    <Box>
      {platforms.slice(0, 3).map(p => (
        <Chip key={p} label={p} size="small" variant="outlined"
          sx={{ fontSize: '0.62rem', height: 16, mr: 0.25, mb: 0.25 }} />
      ))}
      {platforms.length > 3 && (
        <Tooltip title={platforms.slice(3).join(', ')}>
          <Chip label={`+${platforms.length - 3}`} size="small" sx={{ fontSize: '0.62rem', height: 16 }} />
        </Tooltip>
      )}
    </Box>
  )
}

export default function MitreAttack() {
  const [source, setSource] = useState<'attack_v18' | 'attack_v19'>('attack_v18')
  const [search, setSearch] = useState('')
  const [tactic, setTactic] = useState<string>('')
  const [showSubs, setShowSubs] = useState(true)
  const [page, setPage] = useState(1)
  const [selected, setSelected] = useState<MitreTechnique | null>(null)

  const { data: stats } = useQuery({
    queryKey: ['feeds', 'attack', 'stats'],
    queryFn: feedsApi.getAttackStats,
  })

  const tactics = stats ? Object.keys(stats.tactic_counts).sort() : []

  const { data, isLoading, error } = useQuery({
    queryKey: ['feeds', 'attack', source, tactic, search, showSubs, page],
    queryFn: () => feedsApi.getAttackTechniques({
      source,
      tactic: tactic || undefined,
      search: search || undefined,
      subtechniques: showSubs,
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

  function handleTactic(v: string) {
    setTactic(v)
    setPage(1)
  }

  const noData = !isLoading && data?.total === 0

  return (
    <Box sx={{ p: 3 }}>
      <PageHeader
        title="MITRE ATT&CK"
        subtitle="Enterprise adversary tactics, techniques & sub-techniques"
        helpSection="mitre-attack"
      />

      {/* ── Stats row ── */}
      {stats && (
        <Box sx={{ display: 'flex', gap: 3, mb: 2.5, flexWrap: 'wrap' }}>
          {[
            { label: 'Techniques', value: stats.total_techniques },
            { label: 'Sub-techniques', value: stats.total_subtechniques },
            { label: 'Tactics', value: Object.keys(stats.tactic_counts).length },
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

        <FormControl size="small" sx={{ minWidth: 180 }}>
          <InputLabel sx={{ fontSize: '0.8rem' }}>Tactic</InputLabel>
          <Select
            label="Tactic"
            value={tactic}
            onChange={e => handleTactic(e.target.value)}
            sx={{ fontSize: '0.8rem' }}
          >
            <MenuItem value="">All tactics</MenuItem>
            {tactics.map(t => (
              <MenuItem key={t} value={t} sx={{ fontSize: '0.8rem', textTransform: 'capitalize' }}>
                {t.replace(/-/g, ' ')}
              </MenuItem>
            ))}
          </Select>
        </FormControl>

        <ToggleButtonGroup
          size="small"
          value={showSubs ? ['sub'] : []}
          onChange={(_, v) => setShowSubs(v.includes('sub'))}
        >
          <ToggleButton value="sub" sx={{ fontSize: '0.72rem', px: 1.5 }}>Sub-techniques</ToggleButton>
        </ToggleButtonGroup>
      </Box>

      {/* ── Table + detail panel ── */}
      <Box sx={{ display: 'flex', gap: 2 }}>
        <Paper variant="outlined" sx={{ flex: 1, borderRadius: 2, overflow: 'hidden', minWidth: 0 }}>
          {isLoading && (
            <Box sx={{ display: 'flex', justifyContent: 'center', py: 6 }}>
              <CircularProgress size={28} />
            </Box>
          )}
          {error && <Alert severity="error" sx={{ m: 2 }}>Failed to load techniques</Alert>}
          {noData && (
            <Alert severity="info" sx={{ m: 2 }}>
              {source === 'attack_v19'
                ? 'ATT&CK v19 data not yet available. Check back after the scheduled weekly pull.'
                : 'No techniques match the current filters.'}
            </Alert>
          )}
          {!isLoading && data && data.items.length > 0 && (
            <>
              <Table size="small" stickyHeader>
                <TableHead>
                  <TableRow>
                    <TableCell sx={{ fontWeight: 600, fontSize: '0.72rem', width: 90 }}>ID</TableCell>
                    <TableCell sx={{ fontWeight: 600, fontSize: '0.72rem' }}>Name</TableCell>
                    <TableCell sx={{ fontWeight: 600, fontSize: '0.72rem' }}>Tactics</TableCell>
                    <TableCell sx={{ fontWeight: 600, fontSize: '0.72rem', width: 160 }}>Platforms</TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                  {data.items.map(t => (
                    <TableRow
                      key={t.id}
                      hover
                      selected={selected?.id === t.id}
                      onClick={() => setSelected(selected?.id === t.id ? null : t)}
                      sx={{ cursor: 'pointer' }}
                    >
                      <TableCell sx={{ fontFamily: 'monospace', fontSize: '0.75rem', color: INTEL_COLOR, fontWeight: 600 }}>
                        {t.technique_id}
                      </TableCell>
                      <TableCell sx={{ fontSize: '0.78rem', maxWidth: 260 }}>
                        <Box sx={{ pl: t.is_subtechnique ? 2 : 0 }}>
                          <Typography noWrap variant="inherit">{t.name}</Typography>
                          {t.is_subtechnique && (
                            <Typography variant="caption" color="text.disabled" sx={{ fontSize: '0.65rem' }}>sub-technique</Typography>
                          )}
                        </Box>
                      </TableCell>
                      <TableCell sx={{ maxWidth: 200 }}>
                        <Box>{t.tactics.map(tac => <TacticChip key={tac} tactic={tac} />)}</Box>
                      </TableCell>
                      <TableCell><PlatformChips platforms={t.platforms} /></TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>

              {/* Pagination */}
              <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', px: 2, py: 1, borderTop: '1px solid', borderColor: 'divider' }}>
                <Typography variant="caption" color="text.secondary">
                  {data.total.toLocaleString()} techniques
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
              {selected.technique_id}
            </Typography>
            <Typography variant="body2" fontWeight={600} sx={{ mb: 1 }}>{selected.name}</Typography>
            <Box sx={{ mb: 1 }}>
              {selected.tactics.map(t => <TacticChip key={t} tactic={t} />)}
            </Box>
            <PlatformChips platforms={selected.platforms} />
            {selected.description && (
              <Typography variant="caption" color="text.secondary" display="block" sx={{ mt: 1.5, lineHeight: 1.5, maxHeight: 280, overflowY: 'auto' }}>
                {selected.description.slice(0, 600)}{selected.description.length > 600 ? '…' : ''}
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
