import { useEffect, useRef, useState, useCallback } from 'react'
import { useProduct, PRODUCT_SUBTITLES } from '../store/ProductContext'
import {
  Box,
  Card,
  CardContent,
  Typography,
  TextField,
  Select,
  MenuItem,
  FormControl,
  InputLabel,
  Slider,
  Alert,
  CircularProgress,
  Button,
  Chip,
} from '@mui/material'
import { RefreshOutlined } from '@mui/icons-material'
import { useQuery } from '@tanstack/react-query'
import { useNavigate } from 'react-router-dom'
import cytoscape from 'cytoscape'
import { graphApi } from '../api/graph'
import PageHeader from '../components/PageHeader'

const NODE_COLORS: Record<string, string> = {
  control_group: '#4472C4',
  iso_control: '#70AD47',
  external_ref: '#FFC000',
}

const PRODUCT_SOURCE_FRAMEWORK: Record<string, string> = {
  isms:    'ISO27001',
  privacy: 'ISO27701',
  cloud:   'ISO27017',
}

const PRODUCT_SECTIONS: Record<string, { label: string; value: string }[]> = {
  isms:    [
    { label: 'A.5 — Organisational', value: 'A.5' },
    { label: 'A.6 — People',         value: 'A.6' },
    { label: 'A.7 — Physical',       value: 'A.7' },
    { label: 'A.8 — Technological',  value: 'A.8' },
  ],
  privacy: [
    { label: 'A.1 — PII Controller', value: 'A.1' },
    { label: 'A.2 — PII Processor',  value: 'A.2' },
    { label: 'A.3 — Both',           value: 'A.3' },
  ],
  cloud: [],  // ISO 27017 has a single CLD. prefix — no section grouping needed
}

export default function Graph() {
  const cyRef = useRef<HTMLDivElement>(null)
  const cyInstance = useRef<cytoscape.Core | null>(null)
  const navigate = useNavigate()
  const navigateRef = useRef(navigate)
  navigateRef.current = navigate
  const { product } = useProduct()

  const [center, setCenter] = useState('')
  const [depth, setDepth] = useState(2)
  const [section, setSection] = useState('')
  const [cloudSub, setCloudSub] = useState<'ISO27017' | 'ISO27018'>('ISO27017')
  const [submitted, setSubmitted] = useState({ center: '', depth: 2, section: '' })

  const sourceFramework = product === 'cloud'
    ? cloudSub
    : (PRODUCT_SOURCE_FRAMEWORK[product] ?? 'ISO27001')
  const sectionOptions = PRODUCT_SECTIONS[product] ?? []

  // Reset section filter when product changes to avoid stale section values
  const prevProduct = useRef(product)
  if (prevProduct.current !== product) {
    prevProduct.current = product
    setSection('')
  }

  const { data, isLoading, error } = useQuery({
    queryKey: ['graph', submitted.center, submitted.depth, submitted.section, product, cloudSub],
    queryFn: () =>
      graphApi.get({
        source_framework: sourceFramework,
        center: submitted.center || undefined,
        depth: submitted.depth,
        section: submitted.section || undefined,
        max_nodes: 150,
      }),
    staleTime: 300_000,
  })

  function handleLoad() {
    setSubmitted({ center, depth, section })
  }

  useEffect(() => {
    if (!data || !cyRef.current) return

    const elements: cytoscape.ElementDefinition[] = [
      ...data.nodes.map((n) => ({
        group: 'nodes' as const,
        data: {
          id: n.id,
          label: n.label,
          type: (n as unknown as Record<string, unknown>).node_type ?? n.type,
          section: n.section,
          framework: n.framework,
        },
      })),
      ...data.edges.map((e, i) => ({
        group: 'edges' as const,
        data: {
          id: `e${i}`,
          source: e.source,
          target: e.target,
          label: e.label,
          edge_type: e.edge_type,
        },
      })),
    ]

    if (cyInstance.current) {
      cyInstance.current.destroy()
    }

    cyInstance.current = cytoscape({
      container: cyRef.current,
      elements,
      style: [
        {
          selector: 'node',
          style: {
            label: 'data(label)',
            'background-color': '#888888',
            'font-size': '10px',
            color: '#E8EAF0',
            'text-halign': 'center',
            'text-valign': 'bottom',
            'text-margin-y': 4,
            width: '30px',
            height: '30px',
            'text-max-width': '80px',
            'text-wrap': 'ellipsis',
          },
        },
        {
          selector: 'node[type = "control_group"]',
          style: { 'background-color': NODE_COLORS.control_group, width: '40px', height: '40px', 'font-size': '11px', 'font-weight': 700 },
        },
        {
          selector: 'node[type = "iso_control"]',
          style: { 'background-color': NODE_COLORS.iso_control },
        },
        {
          selector: 'node[type = "external_ref"]',
          style: { 'background-color': NODE_COLORS.external_ref },
        },
        {
          selector: 'edge',
          style: {
            width: 1.5,
            'line-color': '#4472C440',
            'target-arrow-color': '#4472C480',
            'target-arrow-shape': 'triangle',
            'curve-style': 'bezier',
            'font-size': 9,
            color: '#8B9CC8',
            label: 'data(label)',
          },
        },
        {
          selector: ':selected',
          style: {
            'border-width': 3,
            'border-color': '#FFEB9C',
            'line-color': '#FFEB9C',
          },
        },
      ],
      layout: {
        name: 'cose',
        animate: false,
        randomize: false,
        componentSpacing: 60,
        nodeOverlap: 20,
        idealEdgeLength: 80,
        edgeElasticity: 100,
        nestingFactor: 5,
        gravity: 80,
        numIter: 1000,
      },
    })

    cyInstance.current.on('tap', 'node', (evt) => {
      const node = evt.target
      if (node.data('type') === 'control_group') {
        const code = (node.data('id') as string).replace(/^cg:/, '')
        navigateRef.current(`/controls/code/${code}`)
      }
    })

    return () => {
      cyInstance.current?.destroy()
      cyInstance.current = null
    }
  }, [data])

  return (
    <Box sx={{ height: 'calc(100vh - 80px)', display: 'flex', flexDirection: 'column' }}>
      <PageHeader title="Control Dependency Graph" subtitle={`${PRODUCT_SUBTITLES[product]} — cross-framework relationships`} />

      {/* Cloud sub-framework toggle */}
      {product === 'cloud' && (
        <Box sx={{ display: 'flex', gap: 1, mb: 1.5 }}>
          {([
            { value: 'ISO27017' as const, label: 'ISO 27017', desc: 'Cloud Security' },
            { value: 'ISO27018' as const, label: 'ISO 27018', desc: 'PII in Cloud' },
          ]).map(({ value, label, desc }) => (
            <Box
              key={value}
              onClick={() => setCloudSub(value)}
              sx={{
                px: 1.5, py: 0.75, borderRadius: 1, cursor: 'pointer',
                bgcolor: cloudSub === value ? 'rgba(255,192,0,0.15)' : 'rgba(255,255,255,0.04)',
                border: `1px solid ${cloudSub === value ? '#FFC00050' : 'rgba(255,255,255,0.08)'}`,
                '&:hover': { bgcolor: 'rgba(255,192,0,0.1)' },
              }}
            >
              <Typography variant="caption" fontWeight={cloudSub === value ? 700 : 400}
                color={cloudSub === value ? '#FFC000' : 'text.secondary'}>
                {label}
              </Typography>
              <Typography variant="caption" sx={{ ml: 1, opacity: 0.6 }}
                color={cloudSub === value ? '#FFC000' : 'text.disabled'}>
                {desc}
              </Typography>
            </Box>
          ))}
        </Box>
      )}

      {/* Controls */}
      <Card sx={{ mb: 2, flexShrink: 0 }}>
        <CardContent sx={{ pb: '12px !important' }}>
          <Box sx={{ display: 'flex', gap: 2, flexWrap: 'wrap', alignItems: 'center' }}>
            <TextField
              size="small"
              label="Centre node (code)"
              value={center}
              onChange={(e) => setCenter(e.target.value)}
              placeholder="e.g. a.5.1-2"
              sx={{ minWidth: 180 }}
            />
            {sectionOptions.length > 0 && (
              <FormControl size="small" sx={{ minWidth: 160 }}>
                <InputLabel>Section</InputLabel>
                <Select value={section} onChange={(e) => setSection(e.target.value)} label="Section">
                  <MenuItem value="">All</MenuItem>
                  {sectionOptions.map((opt) => (
                    <MenuItem key={opt.value} value={opt.value}>{opt.label}</MenuItem>
                  ))}
                </Select>
              </FormControl>
            )}
            <Box sx={{ minWidth: 180 }}>
              <Typography variant="caption" color="text.secondary">Depth: {depth}</Typography>
              <Slider
                size="small"
                min={1}
                max={3}
                step={1}
                marks
                value={depth}
                onChange={(_, v) => setDepth(v as number)}
              />
            </Box>
            <Button
              variant="contained"
              startIcon={<RefreshOutlined />}
              onClick={handleLoad}
            >
              Load Graph
            </Button>
          </Box>
        </CardContent>
      </Card>

      {/* Legend */}
      <Box sx={{ display: 'flex', gap: 1.5, mb: 1.5, flexShrink: 0 }}>
        {Object.entries(NODE_COLORS).map(([type, color]) => (
          <Box key={type} sx={{ display: 'flex', alignItems: 'center', gap: 0.5 }}>
            <Box sx={{ width: 12, height: 12, borderRadius: '50%', bgcolor: color }} />
            <Typography variant="caption" color="text.secondary">{type.replace(/_/g, ' ')}</Typography>
          </Box>
        ))}
        {data && (
          <Chip
            label={`${data.total_nodes} nodes · ${data.total_edges} edges`}
            size="small"
            sx={{ fontSize: '0.7rem', height: 20, ml: 'auto' }}
          />
        )}
      </Box>

      {/* Graph canvas */}
      <Box sx={{ flex: 1, position: 'relative', borderRadius: 2, overflow: 'hidden', bgcolor: '#050810', border: '1px solid rgba(68,114,196,0.12)' }}>
        {isLoading && (
          <Box sx={{ position: 'absolute', inset: 0, display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 10 }}>
            <CircularProgress />
          </Box>
        )}
        {error && (
          <Box sx={{ position: 'absolute', inset: 0, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
            <Alert severity="error">Failed to load graph data.</Alert>
          </Box>
        )}
        {!data && !isLoading && (
          <Box sx={{ position: 'absolute', inset: 0, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
            <Typography variant="body2" color="text.secondary">
              Click "Load Graph" to visualise the control dependency network.
            </Typography>
          </Box>
        )}
        <div ref={cyRef} style={{ width: '100%', height: '100%' }} />
      </Box>
    </Box>
  )
}
