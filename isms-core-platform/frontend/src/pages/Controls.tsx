import { useState, useEffect, useMemo } from 'react'
import { useLocation } from 'react-router-dom'
import {
  Box,
  Card,
  CardContent,
  Typography,
  Grid,
  TextField,
  Select,
  MenuItem,
  FormControl,
  InputLabel,
  Skeleton,
  Alert,
  InputAdornment,
  ToggleButtonGroup,
  ToggleButton,
} from '@mui/material'
import { SearchOutlined, AccountTreeOutlined, GridViewOutlined, ViewListOutlined } from '@mui/icons-material'
import { useQuery } from '@tanstack/react-query'
import { useNavigate } from 'react-router-dom'
import { controlsApi } from '../api/controls'
import PageHeader from '../components/PageHeader'
import { useProduct, PRODUCT_COLORS } from '../store/ProductContext'

const STATUS_HM_COLOR: Record<string, string> = {
  complete:   '#C6EFCE',
  partial:    '#FFEB9C',
  basic:      '#FFD580',
  incomplete: '#FFC7CE',
}

function HeatmapCell({ cg }: { cg: CgItem }) {
  const navigate = useNavigate()
  const sectionKey = cg.section?.match(/A\.\d/)?.[0] ?? ''
  const sectionColor = SECTION_COLOR[sectionKey] ?? '#4472C4'
  const statusColor = STATUS_HM_COLOR[cg.framework_status] ?? STATUS_HM_COLOR.incomplete
  return (
    <Box
      title={`${cg.group_code.toUpperCase()} — ${cg.name}\nStatus: ${cg.framework_status}`}
      onClick={() => navigate(`/controls/${cg.id}`)}
      sx={{
        width: 60, height: 60, borderRadius: 1.5, cursor: 'pointer',
        bgcolor: `${statusColor}18`,
        border: `1px solid ${statusColor}50`,
        borderTop: `3px solid ${sectionColor}`,
        display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center',
        gap: 0.25, transition: 'all 0.12s',
        '&:hover': { bgcolor: `${statusColor}30`, borderColor: statusColor, transform: 'scale(1.04)' },
      }}
    >
      <Typography sx={{ color: statusColor, fontWeight: 700, fontFamily: 'monospace', fontSize: '0.6rem', lineHeight: 1.2, textAlign: 'center' }}>
        {cg.group_code.replace(/^a\./i, '').toUpperCase()}
      </Typography>
      <Box sx={{ width: 6, height: 6, borderRadius: '50%', bgcolor: cg.has_framework ? '#4472C4' : 'transparent', border: '1px solid #4472C440' }} />
    </Box>
  )
}

const SECTION_COLOR: Record<string, string> = {
  'A.5': '#4472C4',
  'A.6': '#70AD47',
  'A.7': '#FFC000',
  'A.8': '#C00000',
}

// Privacy (ISO 27701) section colours
const PRIVACY_SECTION_COLOR: Record<string, string> = {
  'A.1': '#9B72CF',
  'A.2': '#4472C4',
  'A.3': '#2E86AB',
}

// Cloud/ISO 27018 section colours (one flat palette, A.1–A.12)
const CLOUD_SECTION_COLOR: Record<string, string> = {
  'A.1':  '#FFC000', 'A.2':  '#FFC000', 'A.3':  '#FFC000', 'A.4':  '#FFC000',
  'A.5':  '#FFC000', 'A.6':  '#FFC000', 'A.7':  '#FFC000', 'A.8':  '#FFC000',
  'A.9':  '#FFC000', 'A.10': '#FFC000', 'A.11': '#FFC000', 'A.12': '#FFC000',
}



interface CgItem {
  id: string
  group_code: string
  name: string
  section: string
  section_name: string
  is_stacked: boolean
  has_framework: boolean
  has_operational: boolean
  framework_status: string
  operational_status: string
}

function ProductPill({ active, label, color }: { active: boolean; label: string; color: string }) {
  return (
    <Box
      sx={{
        px: 0.75,
        py: 0.1,
        borderRadius: 0.75,
        fontSize: '0.6rem',
        fontWeight: 700,
        letterSpacing: '0.04em',
        bgcolor: active ? `${color}25` : 'rgba(255,255,255,0.04)',
        color: active ? color : '#4a5070',
        border: `1px solid ${active ? `${color}50` : 'transparent'}`,
        lineHeight: 1.6,
      }}
    >
      {label}
    </Box>
  )
}

function ControlCard({ cg, colorOverride }: { cg: CgItem; colorOverride?: string }) {
  const navigate = useNavigate()
  const sectionKey = cg.section?.match(/A\.\d/)?.[0] ?? ''
  const color = colorOverride ?? SECTION_COLOR[sectionKey] ?? '#4472C4'

  return (
    <Card
      sx={{
        cursor: 'pointer',
        transition: 'border-color 0.15s',
        borderLeft: `3px solid ${color}`,
        '&:hover': { borderColor: `${color}cc`, bgcolor: 'rgba(68,114,196,0.04)' },
      }}
      onClick={() => navigate(`/controls/${cg.id}`)}
    >
      <CardContent sx={{ pb: '10px !important', pt: 1.25, px: 1.5 }}>
        <Box sx={{ display: 'flex', alignItems: 'flex-start', justifyContent: 'space-between', mb: 0.4 }}>
          <Typography variant="caption" sx={{ color, fontWeight: 700, fontFamily: 'monospace', fontSize: '0.75rem' }}>
            {cg.group_code.toUpperCase()}
          </Typography>
          <Box sx={{ display: 'flex', gap: 0.5 }}>
            <ProductPill active={cg.has_framework} label="FW" color="#4472C4" />
            <ProductPill active={cg.has_operational} label="OP" color="#70AD47" />
          </Box>
        </Box>
        <Typography variant="body2" fontWeight={600} sx={{ lineHeight: 1.3, mb: 0.4 }}>
          {cg.name}
        </Typography>
        <Typography variant="caption" color="text.secondary">
          {cg.section_name}
        </Typography>
      </CardContent>
    </Card>
  )
}

type ViewMode = 'grid' | 'heatmap'

export default function Controls() {
  const location = useLocation()
  const { product, ismsTier } = useProduct()
  const [search, setSearch] = useState('')
  const [viewMode, setViewMode] = useState<ViewMode>('grid')
  const [section, setSection] = useState(() => {
    const params = new URLSearchParams(location.search)
    return params.get('section') ?? ''
  })
  useEffect(() => {
    const params = new URLSearchParams(location.search)
    setSection(params.get('section') ?? '')
  }, [location.search])

  useEffect(() => { setSection('') }, [product])

  const isIsms = product === 'isms'
  const isPrivacy = product === 'privacy'
  const isCloud = product === 'cloud'
  // product_family for the DB control groups query — always explicit to avoid cross-product pollution
  const productFamily = isPrivacy ? 'PRIVACY' : isCloud ? 'CLOUD' : 'ISMS'

  const { data: cgData, isLoading: cgLoading, error: cgError } = useQuery({
    queryKey: ['controls', productFamily],
    queryFn: () => controlsApi.list({ product_family: productFamily }),
    enabled: isIsms || isPrivacy || isCloud,
  })

  const allControls = cgData as unknown as CgItem[] | undefined

  const filtered = useMemo(() => {
    return (allControls ?? []).filter((cg) => {
      if (isIsms) {
        if (!cg.has_framework && !cg.has_operational) return false
        if (ismsTier === 'framework' && !cg.has_framework) return false
        if (ismsTier === 'operational' && !cg.has_operational) return false
      }
      if (section && !cg.section.startsWith(section)) return false
      if (search) {
        const q = search.toLowerCase()
        return cg.group_code.toLowerCase().includes(q) || cg.name.toLowerCase().includes(q)
      }
      return true
    })
  }, [allControls, isIsms, ismsTier, section, search])

  const grouped = useMemo(() => {
    const g: Record<string, CgItem[]> = {}
    for (const cg of filtered) {
      const s = `${cg.section} — ${cg.section_name}`
      if (!g[s]) g[s] = []
      g[s].push(cg)
    }
    return g
  }, [filtered])

  const sectionColorFor = (sec: string): string => {
    if (isPrivacy) return PRIVACY_SECTION_COLOR[sec.match(/A\.\d+/)?.[0] ?? ''] ?? '#9B72CF'
    if (isCloud)   return CLOUD_SECTION_COLOR[sec.match(/A\.\d+/)?.[0] ?? '']  ?? '#FFC000'
    return SECTION_COLOR[sec.match(/A\.\d/)?.[0] ?? ''] ?? '#4472C4'
  }

  const productColor = PRODUCT_COLORS[product] ?? '#4472C4'
  const subtitle = isIsms
    ? `${filtered.length} control groups · ISO 27001:2022 Annex A`
    : isPrivacy
      ? `${filtered.length} control packs · ISO 27701:2025 Ed. 2`
      : `${filtered.length} control packs · ISO 27018:2025 Ed. 3`

  return (
    <Box>
      <PageHeader title="Control Groups" subtitle={subtitle} />


      {/* Filters */}
      <Card sx={{ mb: 3 }}>
        <CardContent sx={{ pb: '12px !important' }}>
          <Box sx={{ display: 'flex', gap: 2, flexWrap: 'wrap', alignItems: 'center' }}>
            <TextField size="small" placeholder="Search controls..." value={search}
              onChange={(e) => setSearch(e.target.value)} sx={{ flex: 1, minWidth: 200 }}
              InputProps={{ startAdornment: <InputAdornment position="start"><SearchOutlined fontSize="small" sx={{ color: 'text.secondary' }} /></InputAdornment> }} />

            {/* Section filter — ISMS hardcoded, PRIVACY dynamic, CLOUD hidden (few controls) */}
            {isIsms && (
              <FormControl size="small" sx={{ minWidth: 160 }}>
                <InputLabel>Section</InputLabel>
                <Select value={section} onChange={(e) => setSection(e.target.value)} label="Section">
                  <MenuItem value="">All sections</MenuItem>
                  <MenuItem value="A.5">A.5 — Organisational</MenuItem>
                  <MenuItem value="A.6">A.6 — People</MenuItem>
                  <MenuItem value="A.7">A.7 — Physical</MenuItem>
                  <MenuItem value="A.8">A.8 — Technological</MenuItem>
                </Select>
              </FormControl>
            )}
            {isPrivacy && (
              <FormControl size="small" sx={{ minWidth: 180 }}>
                <InputLabel>Section</InputLabel>
                <Select value={section} onChange={(e) => setSection(e.target.value)} label="Section">
                  <MenuItem value="">All sections</MenuItem>
                  <MenuItem value="A.1">A.1 — Controller</MenuItem>
                  <MenuItem value="A.2">A.2 — Processor</MenuItem>
                  <MenuItem value="A.3">A.3 — Shared</MenuItem>
                </Select>
              </FormControl>
            )}
            {isCloud && (
              <FormControl size="small" sx={{ minWidth: 200 }}>
                <InputLabel>Section</InputLabel>
                <Select value={section} onChange={(e) => setSection(e.target.value)} label="Section">
                  <MenuItem value="">All sections (ISO 27018)</MenuItem>
                  <MenuItem value="A.1">A.1 — General</MenuItem>
                  <MenuItem value="A.2">A.2 — Consent and Choice</MenuItem>
                  <MenuItem value="A.3">A.3 — Purpose</MenuItem>
                  <MenuItem value="A.4">A.4 — Collection</MenuItem>
                  <MenuItem value="A.5">A.5 — Minimisation</MenuItem>
                  <MenuItem value="A.6">A.6 — Use / Retention</MenuItem>
                  <MenuItem value="A.7">A.7 — Accuracy</MenuItem>
                  <MenuItem value="A.8">A.8 — Transparency</MenuItem>
                  <MenuItem value="A.9">A.9 — Individual Rights</MenuItem>
                  <MenuItem value="A.10">A.10 — Accountability</MenuItem>
                  <MenuItem value="A.11">A.11 — Information Security</MenuItem>
                  <MenuItem value="A.12">A.12 — Compliance</MenuItem>
                </Select>
              </FormControl>
            )}

            {isIsms && (
              <ToggleButtonGroup value={viewMode} exclusive onChange={(_, v) => v && setViewMode(v)}
                size="small" sx={{ ml: 'auto', '& .MuiToggleButton-root': { px: 1.25, py: 0.4 } }}>
                <ToggleButton value="grid" title="Card view"><ViewListOutlined fontSize="small" /></ToggleButton>
                <ToggleButton value="heatmap" title="Heatmap view"><GridViewOutlined fontSize="small" /></ToggleButton>
              </ToggleButtonGroup>
            )}
          </Box>
        </CardContent>
      </Card>

      {isIsms && viewMode === 'heatmap' && (
        <Box sx={{ display: 'flex', gap: 2, mb: 2, flexWrap: 'wrap', alignItems: 'center' }}>
          <Typography variant="caption" color="text.secondary">Status:</Typography>
          {Object.entries(STATUS_HM_COLOR).map(([status, color]) => (
            <Box key={status} sx={{ display: 'flex', alignItems: 'center', gap: 0.5 }}>
              <Box sx={{ width: 10, height: 10, borderRadius: 0.5, bgcolor: `${color}40`, border: `1px solid ${color}` }} />
              <Typography variant="caption" color="text.secondary">{status}</Typography>
            </Box>
          ))}
        </Box>
      )}

      {cgError && <Alert severity="error">Failed to load controls.</Alert>}

      {cgLoading && (
        <Grid container spacing={1.5}>
          {[...Array(12)].map((_, i) => (
            <Grid item xs={12} sm={6} md={4} lg={3} key={i}>
              <Skeleton variant="rectangular" height={85} sx={{ borderRadius: 2 }} />
            </Grid>
          ))}
        </Grid>
      )}

      {/* ── Unified render (ISMS + Privacy + Cloud all use control groups) ── */}
      {Object.entries(grouped).sort().map(([sec, items]) => {
        const color = sectionColorFor(sec)
        return (
          <Box key={sec} sx={{ mb: 3 }}>
            <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 1.5 }}>
              <AccountTreeOutlined sx={{ color, fontSize: 18 }} />
              <Typography variant="h6" sx={{ color: isIsms ? undefined : color }}>{sec}</Typography>
              <Typography variant="caption" color="text.secondary">({items.length})</Typography>
            </Box>
            {isIsms && viewMode === 'heatmap' ? (
              <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 0.75 }}>
                {items.map((cg) => <HeatmapCell key={cg.id} cg={cg} />)}
              </Box>
            ) : (
              <Grid container spacing={1.5}>
                {items.map((cg) => (
                  <Grid item xs={12} sm={6} md={4} lg={3} key={cg.id}>
                    <ControlCard cg={cg} colorOverride={isIsms ? undefined : color} />
                  </Grid>
                ))}
              </Grid>
            )}
          </Box>
        )
      })}

      {filtered.length === 0 && !cgLoading && (
        <Alert severity="info">No controls match the current filters.</Alert>
      )}
    </Box>
  )
}
