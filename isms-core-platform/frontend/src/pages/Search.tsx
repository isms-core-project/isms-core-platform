import { useState, useEffect } from 'react'
import {
  Box,
  Card,
  CardContent,
  Typography,
  TextField,
  InputAdornment,
  IconButton,
  Select,
  MenuItem,
  FormControl,
  InputLabel,
  Chip,
  Alert,
  Skeleton,
} from '@mui/material'
import { SearchOutlined, ClearOutlined, RefreshOutlined } from '@mui/icons-material'
import { useQuery } from '@tanstack/react-query'
import { useSearchParams } from 'react-router-dom'
import { searchApi } from '../api/search'
import PageHeader from '../components/PageHeader'

function Highlight({ html }: { html: string }) {
  return (
    <span
      dangerouslySetInnerHTML={{ __html: html }}
      style={{ fontSize: '0.8rem', color: '#8B9CC8', lineHeight: 1.6 }}
    />
  )
}

export default function Search() {
  const [searchParams] = useSearchParams()
  const initialQ = searchParams.get('q') ?? ''
  const [query, setQuery] = useState(initialQ)
  const [docType, setDocType] = useState('')
  const [product, setProduct] = useState('')
  const [submitted, setSubmitted] = useState(initialQ)

  // If navigated here with ?q=, keep submitted in sync if param changes
  useEffect(() => {
    const q = searchParams.get('q') ?? ''
    if (q && q !== submitted) {
      setQuery(q)
      setSubmitted(q)
    }
  }, [searchParams]) // eslint-disable-line react-hooks/exhaustive-deps

  // Status probe — polls every 15s when unavailable, stops when available
  const { data: status, refetch: retryStatus } = useQuery({
    queryKey: ['search', 'status'],
    queryFn: searchApi.status,
    refetchInterval: (query) => query.state.data?.available ? false : 15_000,
    refetchIntervalInBackground: true,
  })

  const osAvailable = status?.available ?? true  // optimistic until we know

  const { data, isLoading } = useQuery({
    queryKey: ['search', submitted, docType, product],
    queryFn: () => searchApi.search({
      q: submitted,
      doc_type: docType || undefined,
      product: product || undefined,
      limit: 30,
    }),
    enabled: submitted.length >= 2,
  })

  function handleSearch() {
    setSubmitted(query.trim())
  }

  return (
    <Box>
      <PageHeader title="Search" subtitle="Full-text search across policies and implementation guides" />

      <Card sx={{ mb: 3 }}>
        <CardContent sx={{ pb: '12px !important' }}>
          <Box sx={{ display: 'flex', gap: 2 }}>
            <TextField
              fullWidth
              placeholder="Search policies, implementations..."
              value={query}
              onChange={(e) => setQuery(e.target.value)}
              onKeyDown={(e) => e.key === 'Enter' && handleSearch()}
              size="small"
              InputProps={{
                startAdornment: (
                  <InputAdornment position="start">
                    <SearchOutlined fontSize="small" sx={{ color: 'text.secondary' }} />
                  </InputAdornment>
                ),
                endAdornment: query && (
                  <InputAdornment position="end">
                    <IconButton size="small" onClick={() => { setQuery(''); setSubmitted('') }}>
                      <ClearOutlined fontSize="small" />
                    </IconButton>
                  </InputAdornment>
                ),
              }}
            />
            <FormControl size="small" sx={{ minWidth: 150 }}>
              <InputLabel>Type</InputLabel>
              <Select value={docType} onChange={(e) => setDocType(e.target.value)} label="Type">
                <MenuItem value="">All types</MenuItem>
                <MenuItem value="policy">Policies</MenuItem>
                <MenuItem value="implementation">Implementations</MenuItem>
              </Select>
            </FormControl>
            <FormControl size="small" sx={{ minWidth: 150 }}>
              <InputLabel>Product</InputLabel>
              <Select value={product} onChange={(e) => setProduct(e.target.value)} label="Product">
                <MenuItem value="">All products</MenuItem>
                <MenuItem value="framework">ISMS Framework</MenuItem>
                <MenuItem value="operational">ISMS Operational</MenuItem>
                <MenuItem value="privacy">Privacy (27701)</MenuItem>
                <MenuItem value="cloud">Cloud (27018)</MenuItem>
              </Select>
            </FormControl>
          </Box>
        </CardContent>
      </Card>

      {submitted && !isLoading && data && (
        <Box sx={{ mb: 2 }}>
          <Typography variant="body2" color="text.secondary">
            {data.available
              ? `${data.total} results for "${submitted}" — ${data.took_ms}ms`
              : 'OpenSearch not available — search is offline'}
          </Typography>
        </Box>
      )}

      {!osAvailable && (
        <Alert
          severity="warning"
          action={
            <IconButton size="small" color="inherit" onClick={() => retryStatus()}>
              <RefreshOutlined fontSize="small" />
            </IconButton>
          }
        >
          OpenSearch is not available. Full-text search requires the OpenSearch container to be running. Retrying automatically every 15s.
        </Alert>
      )}

      {isLoading && (
        <Box>
          {[...Array(5)].map((_, i) => (
            <Card key={i} sx={{ mb: 1.5 }}>
              <CardContent>
                <Skeleton variant="text" width="60%" />
                <Skeleton variant="text" />
                <Skeleton variant="text" width="80%" />
              </CardContent>
            </Card>
          ))}
        </Box>
      )}

      {data?.hits.map((hit) => (
        <Card key={hit.document_id} sx={{ mb: 1.5 }}>
          <CardContent sx={{ pb: '12px !important' }}>
            <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', mb: 0.5 }}>
              <Box>
                <Box sx={{ display: 'flex', gap: 0.5, alignItems: 'center', mb: 0.25 }}>
                  <Typography variant="caption" sx={{ fontFamily: 'monospace', color: 'primary.light', fontWeight: 700 }}>
                    {hit.document_id}
                  </Typography>
                  <Chip
                    label={hit.type}
                    size="small"
                    sx={{
                      fontSize: '0.65rem',
                      height: 16,
                      bgcolor: hit.type === 'policy' ? 'rgba(68,114,196,0.18)' : 'rgba(112,173,71,0.15)',
                      color: hit.type === 'policy' ? 'primary.light' : '#C6EFCE',
                    }}
                  />
                  {hit.impl_type && <Chip label={hit.impl_type} size="small" sx={{ fontSize: '0.65rem', height: 16 }} />}
                </Box>
                <Typography variant="body2" fontWeight={600}>{hit.title}</Typography>
              </Box>
              <Box sx={{ textAlign: 'right' }}>
                <Typography variant="caption" color="text.secondary">{hit.control_group_code}</Typography>
                <br />
                <Typography variant="caption" color="text.secondary">score: {hit.score.toFixed(2)}</Typography>
              </Box>
            </Box>
            {hit.snippet && (
              <Box sx={{ mt: 0.5, p: 1, bgcolor: 'rgba(68,114,196,0.05)', borderRadius: 1, borderLeft: '2px solid rgba(68,114,196,0.3)' }}>
                <Highlight html={hit.snippet} />
              </Box>
            )}
          </CardContent>
        </Card>
      ))}
    </Box>
  )
}
