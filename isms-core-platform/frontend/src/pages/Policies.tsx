import { useState, useRef } from 'react'
import { useProduct, PRODUCT_COLORS } from '../store/ProductContext'
import {
  Box,
  Card,
  CardContent,
  Typography,
  Select,
  MenuItem,
  FormControl,
  InputLabel,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Chip,
  Skeleton,
  Alert,
  Grid,
  TextField,
  InputAdornment,
  Button,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  CircularProgress,
  Tooltip,
  IconButton,
} from '@mui/material'
import { SearchOutlined, PolicyOutlined, UploadFileOutlined, DeleteOutlined } from '@mui/icons-material'
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { useNavigate } from 'react-router-dom'
import { policiesApi } from '../api/policiesApi'
import { controlsApi } from '../api/controls'
import PageHeader from '../components/PageHeader'
import MetricCard from '../components/MetricCard'

export default function Policies() {
  const { product, ismsTier } = useProduct()
  const [externalOnly, setExternalOnly] = useState(false)
  const [typeFilter, setTypeFilter] = useState('')
  const [langFilter, setLangFilter] = useState('')
  const [search, setSearch] = useState('')
  const [importOpen, setImportOpen] = useState(false)
  const [deleteTarget, setDeleteTarget] = useState<{ id: string; title: string } | null>(null)
  const navigate = useNavigate()
  const queryClient = useQueryClient()

  const deleteMutation = useMutation({
    mutationFn: (id: string) => policiesApi.delete(id),
    onSuccess: () => {
      setDeleteTarget(null)
      queryClient.invalidateQueries({ queryKey: ['policies'] })
    },
  })

  // When ISMS tier filter is active, map it to API product param; otherwise pass product as-is
  const tieredProduct = product === 'isms' && ismsTier !== 'all' ? ismsTier : undefined
  const effectiveProduct = externalOnly ? 'external' : (product === 'isms' ? tieredProduct : product)

  // Reset type filter when switching products to avoid stale ISMS types on PRIV/CLD
  const [prevProduct, setPrevProduct] = useState(product)
  if (product !== prevProduct) {
    setPrevProduct(product)
    setTypeFilter('')
  }

  const { data, isLoading, error } = useQuery({
    queryKey: ['policies', effectiveProduct, typeFilter],
    queryFn: () =>
      policiesApi.list({
        product: effectiveProduct,
        policy_type: typeFilter || undefined,
      }),
  })

  const filtered = (data ?? []).filter((p) => {
    if (langFilter && (p.language ?? 'en') !== langFilter) return false
    if (!search) return true
    const q = search.toLowerCase()
    return (
      p.document_id.toLowerCase().includes(q) ||
      p.title.toLowerCase().includes(q) ||
      p.group_code.toLowerCase().includes(q)
    )
  })

  const langCounts = (data ?? []).reduce<Record<string, number>>((acc, p) => {
    const l = p.language ?? 'en'
    acc[l] = (acc[l] ?? 0) + 1
    return acc
  }, {})

  const frameworkCount = (data ?? []).filter((p) => p.product_type === 'framework').length
  const operationalCount = (data ?? []).filter((p) => p.product_type === 'operational').length
  const privacyCount = (data ?? []).filter((p) => p.product_type === 'privacy').length
  const cloudCount = (data ?? []).filter((p) => p.product_type === 'cloud').length
  const externalCount = (data ?? []).filter((p) => p.product_type === 'external').length
  const totalReqs = (data ?? []).reduce((s, p) => s + (p.requirements_count ?? 0), 0)

  const STANDARD_LABELS: Record<string, string> = {
    isms: 'ISO 27001:2022', privacy: 'ISO 27701:2025', cloud: 'ISO 27018:2025',
  }

  const productChipStyle = (type: string) => {
    if (type === 'external')    return { bgcolor: 'rgba(255,192,0,0.15)',                      color: '#FFC000' }
    if (type === 'framework')   return { bgcolor: 'rgba(68,114,196,0.15)',                     color: '#4472C4' }
    if (type === 'operational') return { bgcolor: 'rgba(112,173,71,0.15)',                     color: '#70AD47' }
    if (type === 'privacy')     return { bgcolor: `${PRODUCT_COLORS.privacy}22`,               color: PRODUCT_COLORS.privacy }
    if (type === 'cloud')       return { bgcolor: `${PRODUCT_COLORS.cloud}22`,                 color: PRODUCT_COLORS.cloud }
    return { bgcolor: 'rgba(112,173,71,0.15)', color: '#70AD47' }
  }

  return (
    <Box>
      <PageHeader
        title="Policies"
        subtitle={`${data?.length ?? 0} policy documents · ${STANDARD_LABELS[product] ?? 'ISO 27001:2022'}`}
        actions={
          <Button
            variant="outlined"
            size="small"
            startIcon={<UploadFileOutlined />}
            onClick={() => setImportOpen(true)}
            sx={{ fontSize: '0.78rem' }}
          >
            Import External Doc
          </Button>
        }
      />

      {/* Summary */}
      {data && (
        <Grid container spacing={2} sx={{ mb: 2 }}>
          <Grid item xs={6} sm={3}>
            <MetricCard title="Total" value={data.length} icon={<PolicyOutlined fontSize="small" />} />
          </Grid>
          {product === 'isms' && (
            <>
              <Grid item xs={6} sm={3}>
                <MetricCard title="Framework" value={frameworkCount} />
              </Grid>
              <Grid item xs={6} sm={3}>
                <MetricCard title="Operational" value={operationalCount} />
              </Grid>
            </>
          )}
          {product === 'privacy' && (
            <Grid item xs={6} sm={3}>
              <MetricCard title="Privacy" value={privacyCount} sx={{ borderTop: `2px solid ${PRODUCT_COLORS.privacy}` }} />
            </Grid>
          )}
          {product === 'cloud' && (
            <Grid item xs={6} sm={3}>
              <MetricCard title="Cloud" value={cloudCount} sx={{ borderTop: `2px solid ${PRODUCT_COLORS.cloud}` }} />
            </Grid>
          )}
          <Grid item xs={6} sm={3}>
            <Tooltip title="Third-party or customer documents imported via External Doc import">
              <Box>
                <MetricCard title="External" value={externalCount} sx={externalCount > 0 ? { borderTop: '2px solid #FFC000' } : {}} />
              </Box>
            </Tooltip>
          </Grid>
        </Grid>
      )}

      {/* Filters */}
      <Card sx={{ mb: 2 }}>
        <CardContent sx={{ pb: '12px !important' }}>
          <Box sx={{ display: 'flex', gap: 2, flexWrap: 'wrap', alignItems: 'center' }}>
            <Chip
              label={
                <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.5 }}>
                  <Box sx={{ width: 6, height: 6, borderRadius: '50%', bgcolor: '#FFC000' }} />
                  External only
                </Box>
              }
              size="small"
              onClick={() => setExternalOnly(v => !v)}
              sx={{
                fontSize: '0.75rem', height: 28, cursor: 'pointer',
                bgcolor: externalOnly ? 'rgba(255,192,0,0.15)' : 'transparent',
                color: externalOnly ? '#FFC000' : 'text.secondary',
                border: '1px solid',
                borderColor: externalOnly ? 'rgba(255,192,0,0.5)' : 'rgba(255,255,255,0.1)',
                fontWeight: externalOnly ? 700 : 400,
                '&:hover': { bgcolor: 'rgba(255,192,0,0.1)', color: '#FFC000' },
              }}
            />

            <FormControl size="small" sx={{ minWidth: 160 }}>
              <InputLabel>Type</InputLabel>
              <Select value={typeFilter} onChange={(e) => setTypeFilter(e.target.value)} label="Type">
                <MenuItem value="">All types</MenuItem>
                {product === 'isms' && [
                  <MenuItem key="POL" value="POL">POL</MenuItem>,
                  <MenuItem key="OP-POL" value="OP-POL">OP-POL</MenuItem>,
                  <MenuItem key="INS" value="INS">INS</MenuItem>,
                  <MenuItem key="REF" value="REF">REF</MenuItem>,
                  <MenuItem key="CTX" value="CTX">CTX</MenuItem>,
                  <MenuItem key="FORM" value="FORM">FORM</MenuItem>,
                ]}
                {product === 'privacy' && <MenuItem value="PRIV-POL">PRIV-POL</MenuItem>}
                {product === 'cloud'   && <MenuItem value="CLD-POL">CLD-POL</MenuItem>}
              </Select>
            </FormControl>

            <TextField
              size="small"
              placeholder="Search policies..."
              value={search}
              onChange={(e) => setSearch(e.target.value)}
              sx={{ flex: 1, minWidth: 200 }}
              InputProps={{
                startAdornment: (
                  <InputAdornment position="start">
                    <SearchOutlined fontSize="small" sx={{ color: 'text.secondary' }} />
                  </InputAdornment>
                ),
              }}
            />

            {/* Language filter — only show if multiple languages present */}
            {Object.keys(langCounts).length > 1 && (
              <Box sx={{ display: 'flex', gap: 0.5, alignItems: 'center' }}>
                {(['', 'en', 'de', 'fr', 'it'] as const).map((l) => {
                  if (l !== '' && !langCounts[l]) return null
                  const label = l === '' ? 'All' : l.toUpperCase()
                  const count = l === '' ? (data?.length ?? 0) : (langCounts[l] ?? 0)
                  const active = langFilter === l
                  return (
                    <Chip
                      key={l}
                      label={`${label} ${count}`}
                      size="small"
                      onClick={() => setLangFilter(l)}
                      sx={{
                        fontSize: '0.68rem', height: 22, cursor: 'pointer',
                        bgcolor: active ? 'rgba(68,114,196,0.25)' : 'rgba(255,255,255,0.05)',
                        color: active ? 'primary.light' : 'text.secondary',
                        border: active ? '1px solid rgba(68,114,196,0.4)' : '1px solid transparent',
                      }}
                    />
                  )
                })}
              </Box>
            )}
          </Box>
        </CardContent>
      </Card>

      {error && <Alert severity="error" sx={{ mb: 2 }}>Failed to load policies.</Alert>}

      <TableContainer component={Card}>
        <Table size="small">
          <TableHead>
            <TableRow>
              <TableCell>Control Group</TableCell>
              <TableCell>Document</TableCell>
              <TableCell sx={{ width: 110 }}>Product</TableCell>
              <TableCell sx={{ width: 70 }}>Type</TableCell>
              <TableCell sx={{ width: 80, textAlign: 'right' }}>Words</TableCell>
              <TableCell sx={{ width: 80, textAlign: 'right' }}>Reqs</TableCell>
              <TableCell sx={{ width: 40 }} />
            </TableRow>
          </TableHead>
          <TableBody>
            {isLoading &&
              [...Array(10)].map((_, i) => (
                <TableRow key={i}>
                  {[...Array(6)].map((_, j) => (
                    <TableCell key={j}><Skeleton variant="text" /></TableCell>
                  ))}
                </TableRow>
              ))}
            {filtered.map((p) => {
              const isExternal = p.product_type === 'external'
              return (
                <TableRow
                  key={p.id}
                  hover
                  sx={{
                    cursor: 'pointer',
                    ...(isExternal && { bgcolor: 'rgba(255,192,0,0.03)', '&:hover': { bgcolor: 'rgba(255,192,0,0.07) !important' } }),
                  }}
                  onClick={() => navigate(`/controls/${p.control_group_id}`)}
                >
                  <TableCell>
                    <Typography variant="caption" sx={{ fontFamily: 'monospace', color: p.group_code === '00' ? '#FFC000' : 'primary.light', fontWeight: 700 }}>
                      {p.group_code === '00' ? '00' : p.group_code.toUpperCase()}
                    </Typography>
                    <Typography variant="caption" color="text.secondary" sx={{ display: 'block', lineHeight: 1.3 }}>
                      {p.group_name}
                    </Typography>
                  </TableCell>
                  <TableCell>
                    <Typography variant="caption" sx={{ fontFamily: 'monospace', color: isExternal ? '#FFC000' : 'text.secondary', fontSize: '0.68rem' }}>
                      {p.document_id}
                    </Typography>
                    <Typography variant="body2" fontWeight={600} sx={{ lineHeight: 1.3 }}>{p.title}</Typography>
                    {isExternal && p.source_label && (
                      <Typography variant="caption" sx={{ color: '#FFC000', fontSize: '0.65rem' }}>
                        External — {p.source_label}
                      </Typography>
                    )}
                    {p.language && p.language !== 'en' && (
                      <Chip label={p.language.toUpperCase()} size="small" sx={{ fontSize: '0.6rem', height: 14, mt: 0.25, bgcolor: 'rgba(255,255,255,0.06)', color: 'text.secondary' }} />
                    )}
                  </TableCell>
                  <TableCell>
                    <Chip
                      label={p.product_type}
                      size="small"
                      sx={{ fontSize: '0.65rem', height: 18, ...productChipStyle(p.product_type) }}
                    />
                  </TableCell>
                  <TableCell>
                    <Chip label={p.policy_type.toUpperCase()} size="small" sx={{ fontSize: '0.65rem', height: 18 }} />
                  </TableCell>
                  <TableCell align="right">
                    <Typography variant="caption" color="text.secondary">
                      {p.word_count?.toLocaleString() ?? '—'}
                    </Typography>
                  </TableCell>
                  <TableCell align="right">
                    <Typography variant="caption" color={p.requirements_count > 0 ? 'primary.light' : 'text.secondary'} fontWeight={p.requirements_count > 0 ? 600 : 400}>
                      {p.requirements_count > 0 ? p.requirements_count : '—'}
                    </Typography>
                  </TableCell>
                  <TableCell onClick={(e) => e.stopPropagation()}>
                    {isExternal && (
                      <Tooltip title="Delete external document">
                        <IconButton
                          size="small"
                          onClick={() => setDeleteTarget({ id: p.id, title: p.title })}
                          sx={{ color: 'error.main', opacity: 0.5, '&:hover': { opacity: 1 } }}
                        >
                          <DeleteOutlined sx={{ fontSize: 16 }} />
                        </IconButton>
                      </Tooltip>
                    )}
                  </TableCell>
                </TableRow>
              )
            })}
            {!isLoading && filtered.length === 0 && (
              <TableRow>
                <TableCell colSpan={7} align="center">
                  <Typography variant="body2" color="text.secondary" sx={{ py: 3 }}>
                    No policies match the current filters.
                  </Typography>
                </TableCell>
              </TableRow>
            )}
          </TableBody>
        </Table>
      </TableContainer>

      {/* Delete confirm dialog */}
      <Dialog open={!!deleteTarget} onClose={() => setDeleteTarget(null)} maxWidth="xs" fullWidth>
        <DialogTitle>Delete External Document?</DialogTitle>
        <DialogContent>
          <Typography variant="body2">
            <strong>{deleteTarget?.title}</strong> will be permanently removed from the platform.
            This cannot be undone.
          </Typography>
          {deleteMutation.isError && (
            <Alert severity="error" sx={{ mt: 1.5 }}>Delete failed. Try again.</Alert>
          )}
        </DialogContent>
        <DialogActions sx={{ px: 3, pb: 2 }}>
          <Button onClick={() => setDeleteTarget(null)} disabled={deleteMutation.isPending}>Cancel</Button>
          <Button
            variant="contained"
            color="error"
            disabled={deleteMutation.isPending}
            startIcon={deleteMutation.isPending ? <CircularProgress size={14} /> : <DeleteOutlined />}
            onClick={() => deleteTarget && deleteMutation.mutate(deleteTarget.id)}
          >
            {deleteMutation.isPending ? 'Deleting…' : 'Delete'}
          </Button>
        </DialogActions>
      </Dialog>

      {/* Import External Document Dialog */}
      <ImportExternalDialog
        open={importOpen}
        onClose={() => setImportOpen(false)}
        onSuccess={() => {
          setImportOpen(false)
          queryClient.invalidateQueries({ queryKey: ['policies'] })
        }}
      />
    </Box>
  )
}

// ---------------------------------------------------------------------------
// Import External Document Dialog
// ---------------------------------------------------------------------------
function ImportExternalDialog({
  open,
  onClose,
  onSuccess,
}: {
  open: boolean
  onClose: () => void
  onSuccess: () => void
}) {
  const fileRef = useRef<HTMLInputElement>(null)
  const [file, setFile] = useState<File | null>(null)
  const [groupCode, setGroupCode] = useState('')
  const [sourceLabel, setSourceLabel] = useState('')
  const [language, setLanguage] = useState('en')
  const [result, setResult] = useState<{ document_id: string; title: string; word_count: number; requirements_extracted: number } | null>(null)

  const { data: groups } = useQuery({
    queryKey: ['control-groups-list'],
    queryFn: () => controlsApi.list(),
    enabled: open,
  })

  const importMutation = useMutation({
    mutationFn: () => policiesApi.importExternal(file!, groupCode, sourceLabel, language),
    onSuccess: (data) => setResult(data),
  })

  const handleClose = () => {
    setFile(null)
    setGroupCode('')
    setSourceLabel('')
    setLanguage('en')
    setResult(null)
    onClose()
  }

  const canSubmit = !!file && !!groupCode && !!sourceLabel && !importMutation.isPending

  return (
    <Dialog open={open} onClose={handleClose} maxWidth="sm" fullWidth>
      <DialogTitle sx={{ pb: 1 }}>
        Import External Document
        <Typography variant="caption" color="text.secondary" display="block">
          PDF, DOCX, or Markdown — any format, no ISMS CORE watermark required
        </Typography>
      </DialogTitle>
      <DialogContent sx={{ display: 'flex', flexDirection: 'column', gap: 2, pt: '8px !important' }}>
        {result ? (
          <Alert severity="success">
            <Typography variant="body2" fontWeight={600}>{result.title}</Typography>
            <Typography variant="caption" sx={{ fontFamily: 'monospace', display: 'block' }}>{result.document_id}</Typography>
            <Typography variant="caption">{result.word_count.toLocaleString()} words · {result.requirements_extracted} requirements extracted</Typography>
          </Alert>
        ) : (
          <>
            {importMutation.isError && (
              <Alert severity="error" sx={{ mb: 1 }}>
                Import failed. Check file format and try again.
              </Alert>
            )}

            {/* File picker */}
            <Box
              onClick={() => fileRef.current?.click()}
              sx={{
                border: '1px dashed',
                borderColor: file ? 'primary.main' : 'divider',
                borderRadius: 2,
                p: 2,
                cursor: 'pointer',
                textAlign: 'center',
                bgcolor: file ? 'rgba(68,114,196,0.07)' : 'transparent',
                '&:hover': { borderColor: 'primary.main', bgcolor: 'rgba(68,114,196,0.05)' },
              }}
            >
              <UploadFileOutlined sx={{ color: 'text.secondary', mb: 0.5 }} />
              <Typography variant="body2" color={file ? 'primary.light' : 'text.secondary'}>
                {file ? file.name : 'Click to select a file (.pdf, .docx, .md)'}
              </Typography>
              {file && (
                <Typography variant="caption" color="text.secondary">
                  {(file.size / 1024).toFixed(1)} KB
                </Typography>
              )}
              <input
                ref={fileRef}
                type="file"
                accept=".pdf,.docx,.doc,.md"
                style={{ display: 'none' }}
                onChange={(e) => setFile(e.target.files?.[0] ?? null)}
              />
            </Box>

            {/* Control group */}
            <FormControl size="small" fullWidth required>
              <InputLabel>Control Group *</InputLabel>
              <Select value={groupCode} onChange={(e) => setGroupCode(e.target.value)} label="Control Group *">
                <MenuItem value=""><em>Select control group…</em></MenuItem>
                {(groups ?? []).map((g) => (
                  <MenuItem key={g.group_code} value={g.group_code}>
                    <Typography component="span" sx={{ fontFamily: 'monospace', fontSize: '0.75rem', color: 'primary.light', mr: 1 }}>
                      {g.group_code.toUpperCase()}
                    </Typography>
                    {g.group_name}
                  </MenuItem>
                ))}
              </Select>
            </FormControl>

            {/* Source label */}
            <TextField
              size="small"
              label="Source / Organisation *"
              placeholder="e.g. Previous consultant, Acme Corp, ISO 27001 Toolkit"
              value={sourceLabel}
              onChange={(e) => setSourceLabel(e.target.value)}
              fullWidth
              required
              helperText="Shown as amber 'External Document — [source]' banner throughout the platform"
            />

            {/* Language */}
            <FormControl size="small" sx={{ width: 160 }}>
              <InputLabel>Language</InputLabel>
              <Select value={language} onChange={(e) => setLanguage(e.target.value)} label="Language">
                <MenuItem value="en">EN — English</MenuItem>
                <MenuItem value="de">DE — Deutsch</MenuItem>
                <MenuItem value="fr">FR — Français</MenuItem>
                <MenuItem value="it">IT — Italiano</MenuItem>
              </Select>
            </FormControl>
          </>
        )}
      </DialogContent>
      <DialogActions sx={{ px: 3, pb: 2 }}>
        {result ? (
          <>
            <Button onClick={handleClose}>Close</Button>
            <Button variant="contained" onClick={onSuccess}>View in Policies</Button>
          </>
        ) : (
          <>
            <Button onClick={handleClose} disabled={importMutation.isPending}>Cancel</Button>
            <Button
              variant="contained"
              disabled={!canSubmit}
              onClick={() => importMutation.mutate()}
              startIcon={importMutation.isPending ? <CircularProgress size={14} /> : <UploadFileOutlined />}
            >
              {importMutation.isPending ? 'Importing…' : 'Import'}
            </Button>
          </>
        )}
      </DialogActions>
    </Dialog>
  )
}
