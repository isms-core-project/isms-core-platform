import { useMemo, useState } from 'react'
import {
  Alert, Autocomplete, Box, Chip, CircularProgress, FormControlLabel,
  Paper, Switch, TextField, ToggleButton, ToggleButtonGroup, Tooltip, Typography,
} from '@mui/material'
import { useQuery } from '@tanstack/react-query'
import { feedsApi, type MitreGroup, type MitreHeatmapTechnique } from '../api/feedsApi'
import PageHeader from '../components/PageHeader'

const INTEL_COLOR = '#B84F00'
const CELL_W = 128
const CELL_H = 20

// Canonical tactic display labels
const TACTIC_LABELS: Record<string, string> = {
  'reconnaissance':       'Reconnaissance',
  'resource-development': 'Resource Dev.',
  'initial-access':       'Initial Access',
  'execution':            'Execution',
  'persistence':          'Persistence',
  'privilege-escalation': 'Priv. Escalation',
  'defense-evasion':      'Defense Evasion',
  'credential-access':    'Credential Access',
  'discovery':            'Discovery',
  'lateral-movement':     'Lateral Movement',
  'collection':           'Collection',
  'command-and-control':  'C2',
  'exfiltration':         'Exfiltration',
  'impact':               'Impact',
}

// 5-level color ramp (0 = uncovered)
function cellBg(count: number, max: number): string {
  if (count === 0) return 'transparent'
  const ratio = Math.min(count / Math.max(max, 1), 1)
  if (ratio < 0.1) return '#FFE0C8'
  if (ratio < 0.25) return '#FFBC8A'
  if (ratio < 0.5)  return '#F09050'
  if (ratio < 0.75) return '#D06020'
  return INTEL_COLOR
}

function cellTextColor(count: number, max: number): string {
  const ratio = Math.min(count / Math.max(max, 1), 1)
  return ratio >= 0.5 ? '#fff' : 'inherit'
}

// Build per-tactic rows: parents first, then subs grouped under their parent
function buildTacticRows(
  techniques: MitreHeatmapTechnique[],
  tactic: string,
  showSubs: boolean,
): MitreHeatmapTechnique[] {
  const inTactic = techniques.filter(t => t.tactics.includes(tactic))
  const parents = inTactic
    .filter(t => !t.is_subtechnique)
    .sort((a, b) => a.technique_id.localeCompare(b.technique_id))

  if (!showSubs) return parents

  const subs = inTactic.filter(t => t.is_subtechnique)
  const rows: MitreHeatmapTechnique[] = []
  for (const p of parents) {
    rows.push(p)
    const mySubs = subs
      .filter(s => s.technique_id.startsWith(p.technique_id + '.'))
      .sort((a, b) => a.technique_id.localeCompare(b.technique_id))
    rows.push(...mySubs)
  }
  return rows
}

interface TechCellProps {
  tech: MitreHeatmapTechnique
  maxCount: number
  selected: boolean
  onSelect: (t: MitreHeatmapTechnique) => void
}

function TechCell({ tech, maxCount, selected, onSelect }: TechCellProps) {
  const bg = cellBg(tech.usage_count, maxCount)
  const fg = tech.usage_count > 0 ? cellTextColor(tech.usage_count, maxCount) : 'text.disabled'
  const isSub = tech.is_subtechnique

  return (
    <Tooltip
      title={`${tech.technique_id} — ${tech.name}${tech.usage_count > 0 ? ` (${tech.usage_count} actor${tech.usage_count !== 1 ? 's' : ''})` : ''}`}
      placement="right"
      arrow
    >
      <Box
        onClick={() => onSelect(tech)}
        sx={{
          width: CELL_W,
          height: CELL_H,
          px: 0.5,
          display: 'flex',
          alignItems: 'center',
          cursor: 'pointer',
          backgroundColor: bg,
          borderRadius: '2px',
          mb: '1px',
          border: selected ? `1.5px solid ${INTEL_COLOR}` : '1px solid',
          borderColor: selected ? INTEL_COLOR : tech.usage_count > 0 ? 'transparent' : 'divider',
          pl: isSub ? 1.5 : 0.5,
          '&:hover': { opacity: 0.8, borderColor: INTEL_COLOR },
        }}
      >
        <Typography
          noWrap
          sx={{
            fontSize: isSub ? '0.6rem' : '0.63rem',
            fontWeight: isSub ? 400 : 600,
            color: tech.usage_count > 0 ? fg : 'text.disabled',
            fontFamily: 'monospace',
            lineHeight: 1,
          }}
        >
          {tech.technique_id}
        </Typography>
      </Box>
    </Tooltip>
  )
}

export default function MitreHeatmap() {
  const [source, setSource] = useState<'attack_v18' | 'attack_v19'>('attack_v18')
  const [selectedGroups, setSelectedGroups] = useState<MitreGroup[]>([])
  const [includeSoftware, setIncludeSoftware] = useState(true)
  const [showSubs, setShowSubs] = useState(true)
  const [selected, setSelected] = useState<MitreHeatmapTechnique | null>(null)

  // Load all groups for the autocomplete
  const { data: groupData } = useQuery({
    queryKey: ['feeds', 'groups', 'all', source],
    queryFn: () => feedsApi.getMitreGroups({ source, deprecated: false, per_page: 200 }),
  })
  const allGroups = groupData?.items ?? []

  const groupIdsParam = selectedGroups.length > 0
    ? selectedGroups.map(g => g.group_id).join(',')
    : undefined

  const { data, isLoading, error } = useQuery({
    queryKey: ['feeds', 'heatmap', source, groupIdsParam ?? 'all', includeSoftware],
    queryFn: () => feedsApi.getMitreHeatmap({
      source,
      group_ids: groupIdsParam,
      include_software: includeSoftware,
    }),
    staleTime: 60_000,
  })

  const tactics = data?.tactic_order ?? []
  const techniques = data?.techniques ?? []

  // Max usage_count across all techniques — for color scaling
  const maxCount = useMemo(
    () => Math.max(...techniques.map(t => t.usage_count), 1),
    [techniques],
  )

  // Per-tactic rows (memoised)
  const tacticRows = useMemo(() => {
    const map: Record<string, MitreHeatmapTechnique[]> = {}
    for (const tac of tactics) {
      map[tac] = buildTacticRows(techniques, tac, showSubs)
    }
    return map
  }, [tactics, techniques, showSubs])

  function handleSelect(tech: MitreHeatmapTechnique) {
    setSelected(prev => prev?.stix_id === tech.stix_id ? null : tech)
  }

  const coveragePct = data
    ? Math.round((data.covered / Math.max(data.total_techniques, 1)) * 100)
    : 0

  return (
    <Box sx={{ p: 3 }}>
      <PageHeader
        title="MITRE ATT&CK Heatmap"
        subtitle="Technique coverage by threat actor group — click any technique to inspect"
        helpSection="mitre-attack"
      />

      {/* ── Controls ── */}
      <Box sx={{ display: 'flex', gap: 1.5, mb: 2, flexWrap: 'wrap', alignItems: 'center' }}>
        <ToggleButtonGroup
          size="small"
          value={source}
          exclusive
          onChange={(_, v) => v && (setSource(v), setSelected(null))}
        >
          <ToggleButton value="attack_v18" sx={{ fontSize: '0.72rem', px: 1.5 }}>v18</ToggleButton>
          <ToggleButton value="attack_v19" sx={{ fontSize: '0.72rem', px: 1.5 }}>v19</ToggleButton>
        </ToggleButtonGroup>

        <Autocomplete
          multiple
          size="small"
          options={allGroups}
          value={selectedGroups}
          onChange={(_, v) => { setSelectedGroups(v); setSelected(null) }}
          getOptionLabel={g => `${g.group_id} — ${g.name}`}
          isOptionEqualToValue={(a, b) => a.group_id === b.group_id}
          renderInput={params => (
            <TextField
              {...params}
              placeholder={selectedGroups.length === 0 ? 'All groups (aggregate view)' : ''}
              sx={{ minWidth: 340 }}
            />
          )}
          renderTags={(value, getTagProps) =>
            value.map((g, i) => (
              <Chip
                {...getTagProps({ index: i })}
                key={g.group_id}
                label={g.group_id}
                size="small"
                sx={{ fontSize: '0.65rem', height: 18 }}
              />
            ))
          }
          sx={{ minWidth: 340 }}
          limitTags={4}
        />

        <FormControlLabel
          control={
            <Switch
              size="small"
              checked={includeSoftware}
              onChange={e => setIncludeSoftware(e.target.checked)}
            />
          }
          label={<Typography variant="caption">Include software</Typography>}
        />

        <FormControlLabel
          control={
            <Switch
              size="small"
              checked={showSubs}
              onChange={e => setShowSubs(e.target.checked)}
            />
          }
          label={<Typography variant="caption">Sub-techniques</Typography>}
        />
      </Box>

      {/* ── Stats bar ── */}
      {data && (
        <Box sx={{ display: 'flex', gap: 3, mb: 2, flexWrap: 'wrap', alignItems: 'center' }}>
          <Box>
            <Typography variant="h6" sx={{ fontWeight: 700, color: INTEL_COLOR, lineHeight: 1 }}>
              {data.covered.toLocaleString()} / {data.total_techniques.toLocaleString()}
            </Typography>
            <Typography variant="caption" color="text.secondary">Techniques covered ({coveragePct}%)</Typography>
          </Box>
          <Box>
            <Typography variant="h6" sx={{ fontWeight: 700, color: INTEL_COLOR, lineHeight: 1 }}>
              {data.selected_actors.toLocaleString()}
            </Typography>
            <Typography variant="caption" color="text.secondary">
              {selectedGroups.length > 0 ? 'Selected actors' : `Actors in scope${includeSoftware ? ' (groups + software)' : ''}`}
            </Typography>
          </Box>
          <Box>
            <Typography variant="h6" sx={{ fontWeight: 700, color: INTEL_COLOR, lineHeight: 1 }}>
              {maxCount}
            </Typography>
            <Typography variant="caption" color="text.secondary">Max actors / technique</Typography>
          </Box>

          {/* Color legend */}
          <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.5, ml: 'auto' }}>
            <Typography variant="caption" color="text.secondary" sx={{ mr: 0.5 }}>Coverage:</Typography>
            {[0, 0.1, 0.3, 0.6, 1].map((ratio, i) => (
              <Tooltip key={i} title={i === 0 ? 'Not covered' : `${Math.round(ratio * maxCount)}+ actors`}>
                <Box sx={{
                  width: 20, height: 14, borderRadius: '2px',
                  backgroundColor: cellBg(Math.round(ratio * maxCount), maxCount),
                  border: '1px solid', borderColor: 'divider',
                }} />
              </Tooltip>
            ))}
            <Typography variant="caption" color="text.secondary" sx={{ ml: 0.5 }}>High</Typography>
          </Box>
        </Box>
      )}

      {isLoading && (
        <Box sx={{ display: 'flex', justifyContent: 'center', py: 8 }}>
          <CircularProgress size={32} />
        </Box>
      )}
      {error && <Alert severity="error" sx={{ mb: 2 }}>Failed to load heatmap data</Alert>}

      {/* ── Main heatmap + detail panel ── */}
      {data && !isLoading && (
        <Box sx={{ display: 'flex', gap: 2, alignItems: 'flex-start' }}>
          {/* Heatmap grid — horizontally scrollable */}
          <Box sx={{ overflowX: 'auto', flex: 1, minWidth: 0 }}>
            <Box sx={{ display: 'flex', gap: '2px', minWidth: tactics.length * (CELL_W + 2) }}>
              {tactics.map(tac => {
                const rows = tacticRows[tac] ?? []
                return (
                  <Box key={tac} sx={{ width: CELL_W, flexShrink: 0 }}>
                    {/* Tactic header */}
                    <Box sx={{
                      height: 32,
                      display: 'flex',
                      alignItems: 'center',
                      px: 0.5,
                      mb: 0.5,
                      backgroundColor: 'action.hover',
                      borderRadius: '4px 4px 0 0',
                      borderBottom: `2px solid ${INTEL_COLOR}`,
                    }}>
                      <Typography sx={{ fontSize: '0.65rem', fontWeight: 700, color: INTEL_COLOR, lineHeight: 1.1 }}>
                        {TACTIC_LABELS[tac] ?? tac}
                      </Typography>
                    </Box>

                    {/* Technique cells */}
                    {rows.map(tech => (
                      <TechCell
                        key={`${tac}-${tech.stix_id}`}
                        tech={tech}
                        maxCount={maxCount}
                        selected={selected?.stix_id === tech.stix_id}
                        onSelect={handleSelect}
                      />
                    ))}

                    {rows.length === 0 && (
                      <Typography variant="caption" color="text.disabled" sx={{ px: 0.5, fontSize: '0.6rem' }}>
                        No data
                      </Typography>
                    )}
                  </Box>
                )
              })}
            </Box>
          </Box>

          {/* ── Detail panel ── */}
          {selected && (
            <Paper variant="outlined" sx={{ width: 300, flexShrink: 0, borderRadius: 2, p: 2, position: 'sticky', top: 24, maxHeight: '80vh', overflowY: 'auto' }}>
              <Box sx={{ display: 'flex', alignItems: 'baseline', gap: 1, mb: 0.5 }}>
                <Typography variant="subtitle2" sx={{ fontFamily: 'monospace', color: INTEL_COLOR, fontWeight: 700 }}>
                  {selected.technique_id}
                </Typography>
                {selected.is_subtechnique && (
                  <Chip label="sub" size="small" sx={{ fontSize: '0.6rem', height: 16 }} />
                )}
              </Box>
              <Typography variant="body2" fontWeight={600} sx={{ mb: 1 }}>{selected.name}</Typography>

              {/* Tactics */}
              <Box sx={{ mb: 1.5 }}>
                {selected.tactics.map(t => (
                  <Chip
                    key={t}
                    label={TACTIC_LABELS[t] ?? t}
                    size="small"
                    sx={{ fontSize: '0.62rem', height: 18, mr: 0.25, mb: 0.25 }}
                  />
                ))}
              </Box>

              {/* Coverage */}
              <Box sx={{ mb: 1.5, p: 1, backgroundColor: `${INTEL_COLOR}18`, borderRadius: 1 }}>
                <Typography variant="caption" display="block" color="text.secondary">
                  Used by
                </Typography>
                <Typography variant="h6" sx={{ fontWeight: 700, color: INTEL_COLOR, lineHeight: 1.2 }}>
                  {selected.usage_count}
                </Typography>
                <Typography variant="caption" color="text.secondary">
                  {selected.usage_count === 1 ? 'actor' : 'actors'} in scope
                </Typography>
              </Box>

              {/* Actor list */}
              {selected.used_by.length > 0 && (
                <Box>
                  <Typography variant="caption" color="text.secondary" display="block" sx={{ mb: 0.5, fontWeight: 600 }}>
                    Actors ({selected.used_by.length}{selected.usage_count > 30 ? '+' : ''}):
                  </Typography>
                  {selected.used_by.map(name => (
                    <Typography
                      key={name}
                      variant="caption"
                      display="block"
                      sx={{ fontSize: '0.7rem', py: 0.1, color: 'text.primary' }}
                    >
                      · {name}
                    </Typography>
                  ))}
                </Box>
              )}

              {selected.usage_count === 0 && (
                <Typography variant="caption" color="text.disabled">
                  Not attributed to any actor in the current scope.
                </Typography>
              )}
            </Paper>
          )}
        </Box>
      )}
    </Box>
  )
}
