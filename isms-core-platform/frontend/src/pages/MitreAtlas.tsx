import { useState } from 'react'
import {
  Alert, Box, Chip, CircularProgress, FormControl, InputAdornment,
  InputLabel, MenuItem, Paper, Select, Table, TableBody, TableCell,
  TableHead, TableRow, TextField, Typography,
} from '@mui/material'
import { SearchOutlined } from '@mui/icons-material'
import { useQuery } from '@tanstack/react-query'
import { feedsApi, type MitreTechnique } from '../api/feedsApi'
import PageHeader from '../components/PageHeader'

const PER_PAGE = 50
const INTEL_COLOR = '#B84F00'

function TacticChip({ tactic }: { tactic: string }) {
  return (
    <Chip label={tactic} size="small"
      sx={{ fontSize: '0.65rem', height: 18, mr: 0.25, mb: 0.25 }} />
  )
}

export default function MitreAtlas() {
  const [search, setSearch] = useState('')
  const [tactic, setTactic] = useState<string>('')
  const [page, setPage] = useState(1)
  const [selected, setSelected] = useState<MitreTechnique | null>(null)

  const { data: stats } = useQuery({
    queryKey: ['feeds', 'atlas', 'stats'],
    queryFn: feedsApi.getAtlasStats,
  })

  const tactics = stats ? Object.keys(stats.tactic_counts).sort() : []

  const { data, isLoading, error } = useQuery({
    queryKey: ['feeds', 'atlas', tactic, search, page],
    queryFn: () => feedsApi.getAtlasTechniques({
      tactic: tactic || undefined,
      search: search || undefined,
      page,
      per_page: PER_PAGE,
    }),
  })

  const totalPages = data ? Math.ceil(data.total / PER_PAGE) : 0

  function handleSearch(v: string) { setSearch(v); setPage(1) }
  function handleTactic(v: string) { setTactic(v); setPage(1) }

  const noData = !isLoading && data?.total === 0

  return (
    <Box sx={{ p: 3 }}>
      <PageHeader
        title="MITRE ATLAS"
        subtitle="Adversarial Threat Landscape for AI Systems — tactics & techniques targeting ML"
        helpSection="mitre-atlas"
      />

      {/* ── Stats ── */}
      {stats && (
        <Box sx={{ display: 'flex', gap: 3, mb: 2.5, flexWrap: 'wrap' }}>
          <Box>
            <Typography variant="h6" sx={{ fontWeight: 700, color: INTEL_COLOR, lineHeight: 1 }}>
              {stats.total_techniques.toLocaleString()}
            </Typography>
            <Typography variant="caption" color="text.secondary">Techniques</Typography>
          </Box>
          <Box>
            <Typography variant="h6" sx={{ fontWeight: 700, color: INTEL_COLOR, lineHeight: 1 }}>
              {Object.keys(stats.tactic_counts).length}
            </Typography>
            <Typography variant="caption" color="text.secondary">Tactics</Typography>
          </Box>
        </Box>
      )}

      {/* ── Context banner ── */}
      <Alert severity="info" variant="outlined" sx={{ mb: 2, fontSize: '0.8rem' }}>
        MITRE ATLAS covers adversarial ML attacks — model evasion, poisoning, inversion, and theft.
        Relevant for AI Act compliance (A.8.28), DORA AI risk, and ISO 42001 controls.
      </Alert>

      {/* ── Filters ── */}
      <Box sx={{ display: 'flex', gap: 1.5, mb: 2, flexWrap: 'wrap', alignItems: 'center' }}>
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

        <FormControl size="small" sx={{ minWidth: 220 }}>
          <InputLabel sx={{ fontSize: '0.8rem' }}>Tactic</InputLabel>
          <Select
            label="Tactic"
            value={tactic}
            onChange={e => handleTactic(e.target.value)}
            sx={{ fontSize: '0.8rem' }}
          >
            <MenuItem value="">All tactics</MenuItem>
            {tactics.map(t => (
              <MenuItem key={t} value={t} sx={{ fontSize: '0.8rem' }}>{t}</MenuItem>
            ))}
          </Select>
        </FormControl>
      </Box>

      {/* ── Table + detail panel ── */}
      <Box sx={{ display: 'flex', gap: 2 }}>
        <Paper variant="outlined" sx={{ flex: 1, borderRadius: 2, overflow: 'hidden', minWidth: 0 }}>
          {isLoading && (
            <Box sx={{ display: 'flex', justifyContent: 'center', py: 6 }}>
              <CircularProgress size={28} />
            </Box>
          )}
          {error && <Alert severity="error" sx={{ m: 2 }}>Failed to load ATLAS techniques</Alert>}
          {noData && (
            <Alert severity="info" sx={{ m: 2 }}>
              No ATLAS data yet — the feeds container will populate data on its first run (Sunday 02:30 UTC).
            </Alert>
          )}

          {!isLoading && data && data.items.length > 0 && (
            <>
              <Table size="small" stickyHeader>
                <TableHead>
                  <TableRow>
                    <TableCell sx={{ fontWeight: 600, fontSize: '0.72rem', width: 110 }}>ID</TableCell>
                    <TableCell sx={{ fontWeight: 600, fontSize: '0.72rem' }}>Name</TableCell>
                    <TableCell sx={{ fontWeight: 600, fontSize: '0.72rem' }}>Tactics</TableCell>
                    <TableCell sx={{ fontWeight: 600, fontSize: '0.72rem', width: 90 }}>Type</TableCell>
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
                      <TableCell sx={{ fontSize: '0.78rem', maxWidth: 280 }}>
                        <Box sx={{ pl: t.is_subtechnique ? 2 : 0 }}>
                          <Typography noWrap variant="inherit">{t.name}</Typography>
                        </Box>
                      </TableCell>
                      <TableCell sx={{ maxWidth: 200 }}>
                        <Box>{t.tactics.map(tac => <TacticChip key={tac} tactic={tac} />)}</Box>
                      </TableCell>
                      <TableCell>
                        {t.is_subtechnique
                          ? <Chip label="Sub" size="small" sx={{ fontSize: '0.65rem', height: 18 }} />
                          : <Chip label="Tech" size="small" variant="outlined" sx={{ fontSize: '0.65rem', height: 18 }} />}
                      </TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>

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
                  <Typography variant="caption" color="text.secondary">{page} / {totalPages}</Typography>
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
            {selected.is_subtechnique && (
              <Chip label="Sub-technique" size="small" sx={{ fontSize: '0.65rem', height: 18, mb: 1 }} />
            )}
            {selected.description && (
              <Typography variant="caption" color="text.secondary" display="block" sx={{ mt: 1, lineHeight: 1.5, maxHeight: 300, overflowY: 'auto' }}>
                {selected.description.slice(0, 600)}{selected.description.length > 600 ? '…' : ''}
              </Typography>
            )}
          </Paper>
        )}
      </Box>
    </Box>
  )
}
