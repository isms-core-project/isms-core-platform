import { useParams, useNavigate } from 'react-router-dom'
import {
  Box,
  Card,
  CardContent,
  Typography,
  Chip,
  Skeleton,
  Alert,
  IconButton,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  LinearProgress,
} from '@mui/material'
import { ArrowBackOutlined } from '@mui/icons-material'
import { useQuery } from '@tanstack/react-query'
import { controlsApi } from '../api/controls'
import PageHeader from '../components/PageHeader'
import { useProduct, PRODUCT_COLORS, PRODUCT_SUBTITLES } from '../store/ProductContext'

const CONFIDENCE_COLOR = (c: number) =>
  c >= 0.8 ? { bg: 'rgba(198,239,206,0.15)', color: '#C6EFCE' }
  : c >= 0.6 ? { bg: 'rgba(255,235,156,0.12)', color: '#FFEB9C' }
  : { bg: 'rgba(255,199,206,0.12)', color: '#FFC7CE' }

// Section labels for known frameworks
const SECTION_LABELS: Record<string, string> = {
  'A.1': 'PII Controller',
  'A.2': 'PII Processor',
  'A.3': 'Shared (Both)',
  'CLD.6': 'People Controls',
  'CLD.8': 'Asset Controls',
  'CLD.9': 'Access Controls',
  'CLD.12': 'Operations Controls',
  'CLD.13': 'Network Controls',
  'CSP': 'Cloud Service Provider',
  'CSC': 'Cloud Service Customer',
}

export default function FrameworkControlDetail() {
  const { code, controlId } = useParams<{ code: string; controlId: string }>()
  const navigate = useNavigate()
  const { product } = useProduct()
  const productColor = PRODUCT_COLORS[product] ?? '#4472C4'

  const { data: ctrl, isLoading, error } = useQuery({
    queryKey: ['fw-ctrl-detail', code, controlId],
    queryFn: () => controlsApi.getByFrameworkCode(code!, controlId!),
    enabled: !!code && !!controlId,
  })

  if (isLoading) {
    return (
      <Box>
        <PageHeader title="Control Detail" subtitle="Loading..." />
        <Card><CardContent><Skeleton variant="rectangular" height={200} /></CardContent></Card>
      </Box>
    )
  }

  if (error || !ctrl) {
    return (
      <Box>
        <PageHeader title="Control Detail" />
        <Alert severity="error">Control not found or failed to load.</Alert>
      </Box>
    )
  }

  // Determine section label
  const ctrlParts = ctrl.control_id.split('.')
  const sectionKey = ctrlParts[0].length >= 3 && /^[A-Za-z]+$/.test(ctrlParts[0]) && ctrlParts[0] !== 'A'
    ? ctrlParts[0]
    : `${ctrlParts[0]}.${ctrlParts[1] ?? ''}`
  const sectionLabel = SECTION_LABELS[sectionKey] ?? sectionKey

  // Group mappings by framework
  const byFramework: Record<string, typeof ctrl.mappings> = {}
  for (const m of ctrl.mappings) {
    if (!byFramework[m.framework]) byFramework[m.framework] = []
    byFramework[m.framework].push(m)
  }

  return (
    <Box>
      <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 0.5 }}>
        <IconButton size="small" onClick={() => navigate(-1)}>
          <ArrowBackOutlined fontSize="small" />
        </IconButton>
        <Typography variant="caption" color="text.secondary">
          {PRODUCT_SUBTITLES[product]} · {ctrl.framework_name}
        </Typography>
      </Box>

      <PageHeader
        title={ctrl.control_id}
        subtitle={ctrl.title}
      />

      <Box sx={{ display: 'flex', gap: 2, flexWrap: 'wrap', mb: 3 }}>
        {/* Control info card */}
        <Card sx={{ flex: '1 1 340px', borderLeft: `3px solid ${productColor}` }}>
          <CardContent>
            <Typography variant="subtitle2" color="text.secondary" gutterBottom>Control Details</Typography>

            <Box sx={{ display: 'flex', gap: 1, mb: 1.5, flexWrap: 'wrap' }}>
              <Chip
                label={ctrl.framework_name}
                size="small"
                sx={{ bgcolor: `${productColor}20`, color: productColor, fontWeight: 700, fontSize: '0.7rem' }}
              />
              <Chip
                label={sectionLabel}
                size="small"
                sx={{ bgcolor: 'rgba(255,255,255,0.06)', color: 'text.secondary', fontSize: '0.7rem' }}
              />
            </Box>

            {ctrl.description && (
              <Typography variant="body2" color="text.secondary" sx={{ mb: 1.5, lineHeight: 1.6 }}>
                {ctrl.description}
              </Typography>
            )}

            {ctrl.control_type.length > 0 && (
              <Box sx={{ mb: 1 }}>
                <Typography variant="caption" color="text.disabled" sx={{ display: 'block', mb: 0.5 }}>Control Type</Typography>
                <Box sx={{ display: 'flex', gap: 0.5, flexWrap: 'wrap' }}>
                  {ctrl.control_type.map((t) => (
                    <Chip key={t} label={t} size="small"
                      sx={{ fontSize: '0.65rem', height: 18, bgcolor: `${productColor}15`, color: productColor }} />
                  ))}
                </Box>
              </Box>
            )}

            {ctrl.security_properties.length > 0 && (
              <Box>
                <Typography variant="caption" color="text.disabled" sx={{ display: 'block', mb: 0.5 }}>Security Properties</Typography>
                <Box sx={{ display: 'flex', gap: 0.5, flexWrap: 'wrap' }}>
                  {ctrl.security_properties.map((p) => (
                    <Chip key={p} label={p} size="small"
                      sx={{ fontSize: '0.65rem', height: 18, bgcolor: 'rgba(68,114,196,0.12)', color: '#8B9CC8' }} />
                  ))}
                </Box>
              </Box>
            )}
          </CardContent>
        </Card>

        {/* Mapping summary card */}
        <Card sx={{ flex: '0 0 200px' }}>
          <CardContent>
            <Typography variant="subtitle2" color="text.secondary" gutterBottom>Mappings</Typography>
            <Typography variant="h3" sx={{ color: productColor, fontWeight: 800 }}>
              {ctrl.mappings.length}
            </Typography>
            <Typography variant="caption" color="text.secondary">
              across {Object.keys(byFramework).length} framework{Object.keys(byFramework).length !== 1 ? 's' : ''}
            </Typography>
          </CardContent>
        </Card>
      </Box>

      {/* Mappings table */}
      {ctrl.mappings.length > 0 ? (
        <Card>
          <CardContent sx={{ pb: '4px !important' }}>
            <Typography variant="subtitle2" gutterBottom>Cross-Framework Mappings</Typography>
          </CardContent>
          <TableContainer>
            <Table size="small">
              <TableHead>
                <TableRow>
                  <TableCell sx={{ width: 200 }}>Framework</TableCell>
                  <TableCell sx={{ width: 130 }}>Control ID</TableCell>
                  <TableCell>Title</TableCell>
                  <TableCell sx={{ width: 110 }}>Type</TableCell>
                  <TableCell sx={{ width: 110 }}>Confidence</TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {ctrl.mappings.map((m, idx) => {
                  const cc = CONFIDENCE_COLOR(m.confidence)
                  return (
                    <TableRow key={idx} hover>
                      <TableCell>
                        <Typography variant="caption" color="text.secondary">{m.framework}</Typography>
                      </TableCell>
                      <TableCell>
                        <Typography
                          variant="body2"
                          fontWeight={700}
                          sx={{ fontFamily: 'monospace', fontSize: '0.72rem', color: 'primary.light' }}
                        >
                          {m.control_id}
                        </Typography>
                      </TableCell>
                      <TableCell>
                        <Typography variant="body2" color="text.secondary" sx={{ lineHeight: 1.3 }}>
                          {m.control_title}
                        </Typography>
                      </TableCell>
                      <TableCell>
                        <Chip
                          label={m.mapping_type}
                          size="small"
                          sx={{ fontSize: '0.62rem', height: 16, bgcolor: 'rgba(68,114,196,0.1)', color: '#8B9CC8' }}
                        />
                      </TableCell>
                      <TableCell>
                        <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.75 }}>
                          <LinearProgress
                            variant="determinate"
                            value={m.confidence * 100}
                            sx={{
                              flex: 1, height: 4, borderRadius: 2,
                              bgcolor: `${cc.bg}`,
                              '& .MuiLinearProgress-bar': { bgcolor: cc.color },
                            }}
                          />
                          <Typography variant="caption" sx={{ color: cc.color, minWidth: 30, textAlign: 'right' }}>
                            {Math.round(m.confidence * 100)}%
                          </Typography>
                        </Box>
                      </TableCell>
                    </TableRow>
                  )
                })}
              </TableBody>
            </Table>
          </TableContainer>
        </Card>
      ) : (
        <Alert severity="info">No cross-framework mappings found for this control.</Alert>
      )}
    </Box>
  )
}
