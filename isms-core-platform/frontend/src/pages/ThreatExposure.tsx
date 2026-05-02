import { useTheme } from '@mui/material/styles'
import { useQuery } from '@tanstack/react-query'
import {
  Alert, Box, Chip, CircularProgress, Divider, Paper,
  Table, TableBody, TableCell, TableHead, TableRow, Tooltip, Typography,
} from '@mui/material'
import {
  CrisisAlertOutlined, CheckCircleOutlined, WarningAmberOutlined,
} from '@mui/icons-material'
import PageHeader from '../components/PageHeader'
import { client } from '../api/client'

// ── Types ────────────────────────────────────────────────────────────────────

interface ExposedControl {
  control_code: string
  control_name: string | null
  framework_status: string | null
  assessment_score: number | null
  gap: boolean
}

interface ExposureTechnique {
  mitre_tid: string
  ioc_count: number
  sources: string[]
  iso_controls: ExposedControl[]
  max_gap_score: number | null
}

interface ThreatExposureResponse {
  technique_count: number
  affected_controls: number
  gap_controls: number
  items: ExposureTechnique[]
}

// ── Helpers ───────────────────────────────────────────────────────────────────

function scoreColor(score: number | null, gap: boolean): string {
  if (score === null) return '#9e9e9e'
  if (score >= 70)   return '#2e7d32'
  if (score >= 40)   return '#ed6c02'
  return '#d32f2f'
}

function statusLabel(status: string | null, score: number | null): string {
  if (score !== null) return `${score.toFixed(0)}%`
  if (!status) return 'Not assessed'
  return status.replace('_', ' ')
}

function ControlChip({ ctrl }: { ctrl: ExposedControl }) {
  const color = scoreColor(ctrl.assessment_score, ctrl.gap)
  const label = ctrl.assessment_score != null
    ? `${ctrl.control_code} · ${ctrl.assessment_score.toFixed(0)}%`
    : ctrl.control_code
  const tip = ctrl.control_name
    ? `${ctrl.control_name} — ${statusLabel(ctrl.framework_status, ctrl.assessment_score)}`
    : statusLabel(ctrl.framework_status, ctrl.assessment_score)

  return (
    <Tooltip title={tip} arrow>
      <Chip
        label={label}
        size="small"
        sx={{
          fontSize: '0.62rem',
          height: 18,
          bgcolor: color,
          color: '#fff',
          fontFamily: 'monospace',
          cursor: 'default',
        }}
      />
    </Tooltip>
  )
}

function SummaryBar({ data }: { data: ThreatExposureResponse }) {
  const { palette } = useTheme()
  const isLight = palette.mode === 'light'
  const items = [
    { label: 'Active techniques', value: data.technique_count, color: '#b71c1c' },
    { label: 'Affected controls', value: data.affected_controls, color: '#e65100' },
    { label: 'Gaps identified',   value: data.gap_controls,    color: '#d32f2f' },
  ]
  return (
    <Box sx={{ display: 'flex', gap: 2, flexWrap: 'wrap' }}>
      {items.map(({ label, value, color }) => (
        <Paper key={label} variant="outlined" sx={{ p: 2, flex: 1, minWidth: 160, textAlign: 'center' }}>
          <Typography variant="h4" fontWeight={800} sx={{ color }}>{value}</Typography>
          <Typography variant="caption" color="text.secondary">{label}</Typography>
        </Paper>
      ))}
    </Box>
  )
}

// ── Page ─────────────────────────────────────────────────────────────────────

export default function ThreatExposure() {
  const { data, isLoading, isError } = useQuery<ThreatExposureResponse>({
    queryKey: ['threat-exposure'],
    queryFn: () => client.get<ThreatExposureResponse>('/threat-intel/exposure').then(r => r.data),
    staleTime: 5 * 60 * 1000,
  })

  return (
    <Box sx={{ p: 3, display: 'flex', flexDirection: 'column', gap: 2.5 }}>
      <PageHeader
        title="Threat Exposure"
        subtitle="Active MITRE techniques from TI feeds mapped to ISO 27001 controls — gaps highlighted"
      />

      {isLoading && (
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 1.5, py: 4 }}>
          <CircularProgress size={20} />
          <Typography variant="body2" color="text.secondary">Correlating TI feeds with crosswalk…</Typography>
        </Box>
      )}

      {isError && (
        <Alert severity="error">Failed to load exposure data — threat-intel profile may not be active.</Alert>
      )}

      {data && data.technique_count === 0 && (
        <Alert severity="info" icon={<CheckCircleOutlined />}>
          No MITRE technique correlations found — either no IOCs with technique IDs are in the feeds, or the threat-intel profile is not active.
        </Alert>
      )}

      {data && data.technique_count > 0 && (
        <>
          <SummaryBar data={data} />

          <Paper variant="outlined">
            <Box sx={{ px: 2, pt: 1.5, pb: 1, display: 'flex', alignItems: 'center', gap: 1 }}>
              <CrisisAlertOutlined sx={{ fontSize: 18, color: '#b71c1c' }} />
              <Typography variant="subtitle2" fontWeight={700} sx={{ fontSize: '0.85rem' }}>
                Technique → Control Mapping
              </Typography>
              <Box sx={{ flex: 1 }} />
              <Typography variant="caption" color="text.secondary">
                Controls coloured by assessment score · grey = not assessed
              </Typography>
            </Box>
            <Divider />
            <Table size="small">
              <TableHead>
                <TableRow>
                  <TableCell sx={{ fontWeight: 700, fontSize: '0.72rem', width: 110 }}>Technique</TableCell>
                  <TableCell sx={{ fontWeight: 700, fontSize: '0.72rem', width: 80 }}>IOC count</TableCell>
                  <TableCell sx={{ fontWeight: 700, fontSize: '0.72rem', width: 200 }}>Sources</TableCell>
                  <TableCell sx={{ fontWeight: 700, fontSize: '0.72rem' }}>ISO 27001 controls</TableCell>
                  <TableCell sx={{ fontWeight: 700, fontSize: '0.72rem', width: 80 }}>Gaps</TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {data.items.map(item => {
                  const gapCount = item.iso_controls.filter(c => c.gap).length
                  return (
                    <TableRow key={item.mitre_tid} sx={gapCount > 0 ? { bgcolor: 'rgba(211,47,47,0.04)' } : {}}>
                      <TableCell>
                        <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.5 }}>
                          {gapCount > 0 && <WarningAmberOutlined sx={{ fontSize: 14, color: '#d32f2f' }} />}
                          <Typography variant="caption" sx={{ fontFamily: 'monospace', fontWeight: 600 }}>
                            {item.mitre_tid}
                          </Typography>
                        </Box>
                      </TableCell>
                      <TableCell>
                        <Typography variant="caption" fontWeight={600}>{item.ioc_count.toLocaleString()}</Typography>
                      </TableCell>
                      <TableCell>
                        <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 0.5 }}>
                          {item.sources.slice(0, 4).map(s => (
                            <Chip key={s} label={s.replace('_misp', ' MISP')} size="small"
                              sx={{ fontSize: '0.6rem', height: 16 }} />
                          ))}
                        </Box>
                      </TableCell>
                      <TableCell>
                        <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 0.5 }}>
                          {item.iso_controls.map(ctrl => (
                            <ControlChip key={ctrl.control_code} ctrl={ctrl} />
                          ))}
                        </Box>
                      </TableCell>
                      <TableCell>
                        {gapCount > 0
                          ? <Chip label={gapCount} size="small" sx={{ fontSize: '0.65rem', height: 18, bgcolor: '#d32f2f', color: '#fff', fontWeight: 700 }} />
                          : <CheckCircleOutlined sx={{ fontSize: 16, color: '#2e7d32' }} />
                        }
                      </TableCell>
                    </TableRow>
                  )
                })}
              </TableBody>
            </Table>
          </Paper>
        </>
      )}
    </Box>
  )
}
