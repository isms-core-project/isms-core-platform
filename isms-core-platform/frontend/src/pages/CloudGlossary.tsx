import { useState } from 'react'
import {
  Alert, Box, Chip, CircularProgress, Divider, InputAdornment,
  Paper, Tab, Tabs, TextField, Typography,
} from '@mui/material'
import { CloudOutlined, SearchOutlined } from '@mui/icons-material'
import { useQuery } from '@tanstack/react-query'
import { client } from '../api/client'
import PageHeader from '../components/PageHeader'

// ── Types ──────────────────────────────────────────────────────────────────────

interface GlossaryEntry {
  clause_id: string
  title: string
  text: string
}

interface GlossaryResponse {
  standard: string
  part: string
  query: string | null
  entries: GlossaryEntry[]
  results_text?: string
}

// ── Constants ──────────────────────────────────────────────────────────────────

const CLOUD_ACCENT = '#0288d1'

const PARTS = [
  { key: 'vocabulary',    label: 'Vocabulary',    subtitle: 'ISO/IEC 22123-1:2023 — Terms and definitions' },
  { key: 'concepts',      label: 'Concepts',      subtitle: 'ISO/IEC 22123-2:2023 — Cloud computing concepts' },
  { key: 'architecture',  label: 'Architecture',  subtitle: 'ISO/IEC 22123-3:2023 — Cloud Computing Reference Architecture (CCRA)' },
]

// ── API ────────────────────────────────────────────────────────────────────────

async function fetchGlossary(part: string, q?: string): Promise<GlossaryResponse> {
  const params = new URLSearchParams({ part })
  if (q) params.set('q', q)
  const res = await client.get(`/glossary/cloud?${params.toString()}`)
  return res.data
}

// ── Entry card ────────────────────────────────────────────────────────────────

function EntryCard({ entry }: { entry: GlossaryEntry }) {
  return (
    <Paper
      variant="outlined"
      sx={{
        p: 2,
        bgcolor: '#0d1117',
        borderColor: 'divider',
        '&:hover': { borderColor: CLOUD_ACCENT, bgcolor: '#0a1520' },
        transition: 'border-color 0.15s, background-color 0.15s',
      }}
    >
      <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 0.5 }}>
        <Chip
          label={entry.clause_id}
          size="small"
          sx={{
            fontSize: '0.68rem', height: 18, fontFamily: 'monospace',
            bgcolor: '#0a1e30', color: CLOUD_ACCENT,
            border: `1px solid ${CLOUD_ACCENT}40`, fontWeight: 600,
          }}
        />
        <Typography variant="subtitle2" sx={{ fontWeight: 600, color: '#e0e0e0' }}>
          {entry.title}
        </Typography>
      </Box>
      <Typography variant="body2" color="text.secondary" sx={{ whiteSpace: 'pre-line', lineHeight: 1.6 }}>
        {entry.text}
      </Typography>
    </Paper>
  )
}

// ── Main page ─────────────────────────────────────────────────────────────────

export default function CloudGlossary() {
  const [part, setPart] = useState('vocabulary')
  const [searchInput, setSearchInput] = useState('')
  const [activeQuery, setActiveQuery] = useState('')

  const { data, isLoading, isError } = useQuery<GlossaryResponse>({
    queryKey: ['glossary', 'cloud', part, activeQuery],
    queryFn: () => fetchGlossary(part, activeQuery || undefined),
    staleTime: 5 * 60_000,
  })

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault()
    setActiveQuery(searchInput.trim())
  }

  const currentPart = PARTS.find(p => p.key === part)!

  return (
    <Box sx={{ p: 3, maxWidth: 1100 }}>
      <PageHeader
        title="Cloud Glossary"
        subtitle="ISO/IEC 22123 cloud computing vocabulary, concepts and reference architecture"
      />

      {/* Tabs */}
      <Tabs
        value={part}
        onChange={(_, v) => { setPart(v); setActiveQuery(''); setSearchInput('') }}
        sx={{ mb: 2, borderBottom: 1, borderColor: 'divider' }}
      >
        {PARTS.map(p => (
          <Tab
            key={p.key}
            value={p.key}
            label={p.label}
            icon={<CloudOutlined sx={{ fontSize: 16 }} />}
            iconPosition="start"
            sx={{ textTransform: 'none', minHeight: 40 }}
          />
        ))}
      </Tabs>

      {/* Standard subtitle */}
      <Typography variant="caption" color="text.secondary" sx={{ display: 'block', mb: 2 }}>
        {currentPart.subtitle}
      </Typography>

      {/* Search bar */}
      <Box component="form" onSubmit={handleSearch} sx={{ display: 'flex', gap: 1, mb: 3 }}>
        <TextField
          size="small"
          placeholder={`Search ${currentPart.label.toLowerCase()} terms…`}
          value={searchInput}
          onChange={e => setSearchInput(e.target.value)}
          InputProps={{
            startAdornment: (
              <InputAdornment position="start">
                <SearchOutlined sx={{ fontSize: 18, color: 'text.disabled' }} />
              </InputAdornment>
            ),
          }}
          sx={{ flex: 1, maxWidth: 480 }}
        />
      </Box>

      {activeQuery && (
        <Box sx={{ mb: 2, display: 'flex', alignItems: 'center', gap: 1 }}>
          <Typography variant="body2" color="text.secondary">Results for:</Typography>
          <Chip
            label={activeQuery}
            size="small"
            onDelete={() => { setActiveQuery(''); setSearchInput('') }}
            sx={{ bgcolor: '#0a1e30', color: CLOUD_ACCENT }}
          />
        </Box>
      )}

      {/* Content */}
      {isLoading && (
        <Box sx={{ display: 'flex', justifyContent: 'center', py: 6 }}>
          <CircularProgress size={28} />
        </Box>
      )}

      {isError && (
        <Alert severity="error" sx={{ mt: 2 }}>Failed to load glossary data.</Alert>
      )}

      {data && !isLoading && (
        <>
          {/* Full-text search returns raw text; structured entries returned when no query */}
          {activeQuery && data.results_text ? (
            <Paper variant="outlined" sx={{ p: 2.5, bgcolor: '#0d1117', borderColor: 'divider' }}>
              <Typography variant="caption" color={CLOUD_ACCENT} sx={{ fontWeight: 600, display: 'block', mb: 1 }}>
                Search results — {data.standard}
              </Typography>
              <Typography variant="body2" color="text.secondary" sx={{ whiteSpace: 'pre-line', lineHeight: 1.7 }}>
                {data.results_text}
              </Typography>
            </Paper>
          ) : (
            <>
              <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 2 }}>
                <Chip
                  label={`${data.entries.length} entries`}
                  size="small"
                  sx={{ bgcolor: '#0a1e30', color: CLOUD_ACCENT, fontSize: '0.72rem' }}
                />
                <Divider orientation="vertical" flexItem />
                <Typography variant="caption" color="text.disabled">{data.standard}</Typography>
              </Box>
              <Box sx={{ display: 'flex', flexDirection: 'column', gap: 1.5 }}>
                {data.entries.map(entry => (
                  <EntryCard key={entry.clause_id} entry={entry} />
                ))}
              </Box>
            </>
          )}
        </>
      )}
    </Box>
  )
}
