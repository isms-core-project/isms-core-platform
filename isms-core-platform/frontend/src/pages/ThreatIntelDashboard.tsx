import { useQuery, useMutation } from '@tanstack/react-query'
import {
  Alert, Box, Chip, CircularProgress, Grid, Paper,
  Table, TableBody, TableCell, TableHead, TableRow,
  Tooltip, Typography,
} from '@mui/material'
import {
  CheckCircleOutlined, CoronavirusOutlined, ErrorOutlined,
  HourglassEmptyOutlined, PlayArrowOutlined, RouterOutlined,
  StreamOutlined, SyncOutlined, TrackChangesOutlined,
} from '@mui/icons-material'
import { useNavigate } from 'react-router-dom'
import PageHeader from '../components/PageHeader'
import { threatIntelApi, TiSourceStatus } from '../api/threatIntelApi'
import { useAuth } from '../store/AuthContext'

const INTEL_COLOR = '#B84F00'

function fmt(iso: string | null): string {
  if (!iso) return '—'
  return new Date(iso).toLocaleString(undefined, {
    year: 'numeric', month: 'short', day: 'numeric',
    hour: '2-digit', minute: '2-digit',
  })
}

function StatusChip({ status }: { status: string | null }) {
  if (!status)
    return <Chip label="Never run" size="small" sx={{ fontSize: '0.7rem' }} />
  if (status === 'success')
    return <Chip icon={<CheckCircleOutlined sx={{ fontSize: 13 }} />} label="OK" size="small" color="success" sx={{ fontSize: '0.7rem' }} />
  if (status === 'running')
    return <Chip icon={<SyncOutlined sx={{ fontSize: 13 }} />} label="Running" size="small" color="info" sx={{ fontSize: '0.7rem' }} />
  return <Chip icon={<ErrorOutlined sx={{ fontSize: 13 }} />} label="Error" size="small" color="error" sx={{ fontSize: '0.7rem' }} />
}

const SOURCE_ICONS: Record<string, React.ReactNode> = {
  circl_misp:   <StreamOutlined sx={{ fontSize: 26, color: INTEL_COLOR }} />,
  botvrij_misp: <StreamOutlined sx={{ fontSize: 26, color: '#8b5a00' }} />,
  abuseipdb:    <RouterOutlined sx={{ fontSize: 26, color: '#1565c0' }} />,
  malpedia:     <CoronavirusOutlined sx={{ fontSize: 26, color: '#6a0dad' }} />,
}

function StatCard({ label, value, icon, onClick }: {
  label: string; value: number | string; icon: React.ReactNode; onClick?: () => void
}) {
  return (
    <Paper
      variant="outlined"
      onClick={onClick}
      sx={{
        p: 2, display: 'flex', alignItems: 'center', gap: 1.5,
        cursor: onClick ? 'pointer' : 'default',
        '&:hover': onClick ? { borderColor: INTEL_COLOR, bgcolor: `${INTEL_COLOR}08` } : {},
        transition: 'border-color 0.15s',
      }}
    >
      {icon}
      <Box>
        <Typography variant="h5" fontWeight={700} sx={{ lineHeight: 1 }}>{value}</Typography>
        <Typography variant="caption" color="text.secondary">{label}</Typography>
      </Box>
    </Paper>
  )
}

function SourceRow({ src, onTrigger, isAdmin }: {
  src: TiSourceStatus; onTrigger: (s: string) => void; isAdmin: boolean
}) {
  return (
    <TableRow hover>
      <TableCell>
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
          {SOURCE_ICONS[src.source] ?? <StreamOutlined sx={{ fontSize: 20, color: 'text.secondary' }} />}
          <Box>
            <Typography variant="body2" fontWeight={600} sx={{ fontSize: '0.82rem' }}>{src.display_name}</Typography>
            <Typography variant="caption" color="text.secondary" sx={{ fontFamily: 'monospace' }}>{src.source}</Typography>
          </Box>
        </Box>
      </TableCell>
      <TableCell>
        <Chip
          label={src.enabled ? 'Enabled' : 'Disabled'}
          size="small"
          color={src.enabled ? 'success' : 'default'}
          sx={{ fontSize: '0.68rem', height: 18 }}
        />
      </TableCell>
      <TableCell><StatusChip status={src.last_run_status} /></TableCell>
      <TableCell sx={{ fontFamily: 'monospace', fontSize: '0.75rem', color: 'text.secondary' }}>
        {fmt(src.last_run_at)}
      </TableCell>
      <TableCell sx={{ fontWeight: 600, fontSize: '0.82rem' }}>
        {src.ioc_count.toLocaleString()}
      </TableCell>
      <TableCell>
        {isAdmin && src.enabled && (
          <Tooltip title={`Trigger ${src.display_name} now`}>
            <Chip
              icon={<PlayArrowOutlined sx={{ fontSize: 13 }} />}
              label="Run"
              size="small"
              onClick={() => onTrigger(src.source)}
              sx={{ fontSize: '0.68rem', height: 20, cursor: 'pointer' }}
            />
          </Tooltip>
        )}
      </TableCell>
    </TableRow>
  )
}

export default function ThreatIntelDashboard() {
  const navigate = useNavigate()
  const { user } = useAuth()
  const isAdmin = user?.role === 'super_admin' || user?.role === 'admin'

  const { data, isLoading, error } = useQuery({
    queryKey: ['threat-intel', 'summary'],
    queryFn: threatIntelApi.getSummary,
    staleTime: 60_000,
    refetchInterval: 60_000,
  })

  const triggerMutation = useMutation({
    mutationFn: (source: string) => threatIntelApi.triggerFeed(source),
  })

  if (isLoading) return (
    <Box sx={{ display: 'flex', justifyContent: 'center', mt: 8 }}>
      <CircularProgress size={32} sx={{ color: INTEL_COLOR }} />
    </Box>
  )

  if (!data?.active) return (
    <Box sx={{ p: 3 }}>
      <PageHeader title="Threat Intelligence" subtitle="OSINT IOC feeds, malware families, and actor attribution" />
      <Alert severity="info" sx={{ mt: 2 }}>
        Threat Intelligence module is not active.
        Start the platform with <code style={{ fontFamily: 'monospace' }}>--profile threat-intel</code> and set{' '}
        <code style={{ fontFamily: 'monospace' }}>THREAT_INTEL_ENABLED=true</code> to enable it.
      </Alert>
    </Box>
  )

  if (error) return (
    <Box sx={{ p: 3 }}>
      <Alert severity="error">Could not load threat intelligence data.</Alert>
    </Box>
  )

  return (
    <Box sx={{ p: 3, display: 'flex', flexDirection: 'column', gap: 3 }}>
      <PageHeader
        title="Threat Intelligence"
        subtitle="OSINT IOC feeds · Malware families · Actor attribution"
      />

      {/* ── Stat cards ── */}
      <Grid container spacing={2}>
        <Grid item xs={12} sm={4}>
          <StatCard
            label="Total IOCs"
            value={(data?.total_iocs ?? 0).toLocaleString()}
            icon={<TrackChangesOutlined sx={{ fontSize: 32, color: INTEL_COLOR }} />}
            onClick={() => navigate('/ioc-explorer')}
          />
        </Grid>
        <Grid item xs={12} sm={4}>
          <StatCard
            label="Malware Families"
            value={(data?.total_families ?? 0).toLocaleString()}
            icon={<CoronavirusOutlined sx={{ fontSize: 32, color: '#6a0dad' }} />}
            onClick={() => navigate('/malware-atlas')}
          />
        </Grid>
        <Grid item xs={12} sm={4}>
          <StatCard
            label="Threat Actors"
            value={(data?.total_actors ?? 0).toLocaleString()}
            icon={<HourglassEmptyOutlined sx={{ fontSize: 32, color: '#c62828' }} />}
            onClick={() => navigate('/malware-atlas')}
          />
        </Grid>
      </Grid>

      {/* ── Source table ── */}
      <Paper variant="outlined">
        <Box sx={{ px: 2, pt: 2, pb: 1 }}>
          <Typography variant="subtitle2" fontWeight={700} sx={{ fontSize: '0.85rem', color: INTEL_COLOR }}>
            Feed Sources
          </Typography>
        </Box>
        <Table size="small">
          <TableHead>
            <TableRow>
              <TableCell sx={{ fontWeight: 700, fontSize: '0.75rem' }}>Source</TableCell>
              <TableCell sx={{ fontWeight: 700, fontSize: '0.75rem' }}>Status</TableCell>
              <TableCell sx={{ fontWeight: 700, fontSize: '0.75rem' }}>Last Run</TableCell>
              <TableCell sx={{ fontWeight: 700, fontSize: '0.75rem' }}>Last Run At</TableCell>
              <TableCell sx={{ fontWeight: 700, fontSize: '0.75rem' }}>IOCs</TableCell>
              <TableCell />
            </TableRow>
          </TableHead>
          <TableBody>
            {(data?.sources ?? []).map(src => (
              <SourceRow
                key={src.source}
                src={src}
                isAdmin={isAdmin}
                onTrigger={s => triggerMutation.mutate(s)}
              />
            ))}
          </TableBody>
        </Table>
      </Paper>

      {triggerMutation.isSuccess && (
        <Alert severity="success" onClose={() => triggerMutation.reset()}>
          Feed triggered — check status in a few minutes.
        </Alert>
      )}
      {triggerMutation.isError && (
        <Alert severity="error" onClose={() => triggerMutation.reset()}>
          Could not reach TI trigger server.
        </Alert>
      )}
    </Box>
  )
}
