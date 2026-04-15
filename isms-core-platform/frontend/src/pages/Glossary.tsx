import { useState } from 'react'
import {
  Alert, Box, Chip, CircularProgress, Divider, InputAdornment,
  Paper, Tab, Tabs, TextField, Typography,
} from '@mui/material'
import { CloudOutlined, PsychologyOutlined, SearchOutlined } from '@mui/icons-material'
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
const AI_ACCENT    = '#ff6b35'

const CLOUD_PARTS = [
  { key: 'vocabulary',   label: 'Vocabulary',   subtitle: 'ISO/IEC 22123-1:2023 — Terms and definitions' },
  { key: 'concepts',     label: 'Concepts',     subtitle: 'ISO/IEC 22123-2:2023 — Cloud computing concepts' },
  { key: 'architecture', label: 'Architecture', subtitle: 'ISO/IEC 22123-3:2023 — Cloud Computing Reference Architecture (CCRA)' },
]

const AI_PARTS = [
  { key: 'iso42001', label: 'ISO 42001:2023', subtitle: 'ISO/IEC 42001:2023 — AI Management System — Terms and definitions (Clause 3, 26 terms)' },
  { key: 'iso42005', label: 'ISO 42005:2025', subtitle: 'ISO/IEC 42005:2025 — AI System Impact Assessment — Terms and definitions (Clause 3–4, 9 terms + abbreviated terms)' },
]

// ── API ────────────────────────────────────────────────────────────────────────

async function fetchGlossary(domain: string, part: string, q?: string): Promise<GlossaryResponse> {
  const params = new URLSearchParams({ part })
  if (q) params.set('q', q)
  const res = await client.get(`/glossary/${domain}?${params.toString()}`)
  return res.data
}

// ── Entry card ────────────────────────────────────────────────────────────────

function EntryCard({ entry, accent }: { entry: GlossaryEntry; accent: string }) {
  return (
    <Paper
      variant="outlined"
      sx={{
        p: 2,
        bgcolor: '#0d1117',
        borderColor: 'divider',
        '&:hover': { borderColor: accent, bgcolor: accent === AI_ACCENT ? '#1a0e08' : '#0a1520' },
        transition: 'border-color 0.15s, background-color 0.15s',
      }}
    >
      <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 0.5 }}>
        <Chip
          label={entry.clause_id}
          size="small"
          sx={{
            fontSize: '0.68rem', height: 18, fontFamily: 'monospace',
            bgcolor: accent === AI_ACCENT ? '#1a0e08' : '#0a1e30',
            color: accent,
            border: `1px solid ${accent}40`, fontWeight: 600,
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

// ── Domain panel (shared layout for Cloud and AI) ─────────────────────────────

function GlossaryPanel({
  domain,
  parts,
  accent,
  defaultPart,
}: {
  domain: string
  parts: { key: string; label: string; subtitle: string }[]
  accent: string
  defaultPart: string
}) {
  const [part, setPart] = useState(defaultPart)
  const [searchInput, setSearchInput] = useState('')
  const [activeQuery, setActiveQuery] = useState('')

  const { data, isLoading, isError } = useQuery<GlossaryResponse>({
    queryKey: ['glossary', domain, part, activeQuery],
    queryFn: () => fetchGlossary(domain, part, activeQuery || undefined),
    staleTime: 5 * 60_000,
  })

  const handleSearch = (e: React.FormEvent) => {
    e.preventDefault()
    setActiveQuery(searchInput.trim())
  }

  const currentPart = parts.find(p => p.key === part)!

  return (
    <Box>
      {/* Sub-tabs */}
      <Tabs
        value={part}
        onChange={(_, v) => { setPart(v); setActiveQuery(''); setSearchInput('') }}
        sx={{ mb: 2, borderBottom: 1, borderColor: 'divider' }}
      >
        {parts.map(p => (
          <Tab
            key={p.key}
            value={p.key}
            label={p.label}
            sx={{ textTransform: 'none', minHeight: 40, color: part === p.key ? accent : undefined }}
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
            sx={{ bgcolor: accent === AI_ACCENT ? '#1a0e08' : '#0a1e30', color: accent }}
          />
        </Box>
      )}

      {/* Content */}
      {isLoading && (
        <Box sx={{ display: 'flex', justifyContent: 'center', py: 6 }}>
          <CircularProgress size={28} sx={{ color: accent }} />
        </Box>
      )}

      {isError && (
        <Alert severity="error" sx={{ mt: 2 }}>Failed to load glossary data.</Alert>
      )}

      {data && !isLoading && (
        <>
          {activeQuery && data.results_text ? (
            <Paper variant="outlined" sx={{ p: 2.5, bgcolor: '#0d1117', borderColor: 'divider' }}>
              <Typography variant="caption" color={accent} sx={{ fontWeight: 600, display: 'block', mb: 1 }}>
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
                  sx={{ bgcolor: accent === AI_ACCENT ? '#1a0e08' : '#0a1e30', color: accent, fontSize: '0.72rem' }}
                />
                <Divider orientation="vertical" flexItem />
                <Typography variant="caption" color="text.disabled">{data.standard}</Typography>
              </Box>
              <Box sx={{ display: 'flex', flexDirection: 'column', gap: 1.5 }}>
                {data.entries.map(entry => (
                  <EntryCard key={entry.clause_id} entry={entry} accent={accent} />
                ))}
              </Box>
            </>
          )}
        </>
      )}
    </Box>
  )
}

// ── Main page ─────────────────────────────────────────────────────────────────

export default function Glossary() {
  const [domain, setDomain] = useState<'cloud' | 'ai'>('cloud')

  return (
    <Box sx={{ p: 3, maxWidth: 1100 }}>
      <PageHeader
        title="Glossary"
        subtitle="ISO/IEC standard terminology — Cloud computing (ISO 22123) and AI management (ISO 42001 · ISO 42005)"
      />

      {/* Top-level domain selector */}
      <Tabs
        value={domain}
        onChange={(_, v) => setDomain(v)}
        sx={{ mb: 3, borderBottom: 1, borderColor: 'divider' }}
      >
        <Tab
          value="cloud"
          label="Cloud Computing"
          icon={<CloudOutlined sx={{ fontSize: 16 }} />}
          iconPosition="start"
          sx={{ textTransform: 'none', minHeight: 44, color: domain === 'cloud' ? CLOUD_ACCENT : undefined }}
        />
        <Tab
          value="ai"
          label="AI Management System"
          icon={<PsychologyOutlined sx={{ fontSize: 16 }} />}
          iconPosition="start"
          sx={{ textTransform: 'none', minHeight: 44, color: domain === 'ai' ? AI_ACCENT : undefined }}
        />
      </Tabs>

      {domain === 'cloud' && (
        <GlossaryPanel
          domain="cloud"
          parts={CLOUD_PARTS}
          accent={CLOUD_ACCENT}
          defaultPart="vocabulary"
        />
      )}

      {domain === 'ai' && (
        <GlossaryPanel
          domain="ai"
          parts={AI_PARTS}
          accent={AI_ACCENT}
          defaultPart="iso42001"
        />
      )}
    </Box>
  )
}
