import { useState } from 'react'
import { Alert, Box, Chip, Collapse, IconButton, Typography } from '@mui/material'
import {
  CloseOutlined, ExpandLessOutlined, ExpandMoreOutlined,
  ErrorOutlineOutlined,
} from '@mui/icons-material'
import { useQuery } from '@tanstack/react-query'
import { client } from '../api/client'

interface HealthAlert {
  type: string
  severity: string
  message: string
  detected_at: string
  entity: string | null
}

const TYPE_LABELS: Record<string, string> = {
  feed_failure:      'Feed',
  connector_failure: 'Connector',
  opensearch_down:   'OpenSearch',
  db_error:          'Database',
}

function fmtTime(iso: string) {
  try {
    return new Date(iso).toLocaleTimeString(undefined, { hour: '2-digit', minute: '2-digit' })
  } catch {
    return ''
  }
}

export default function HealthAlertBanner() {
  const [dismissed, setDismissed] = useState(
    () => sessionStorage.getItem('health_banner_dismissed_at') === new Date().toDateString()
  )
  const [expanded, setExpanded] = useState(false)

  const { data: alerts } = useQuery<HealthAlert[]>({
    queryKey: ['health', 'alerts'],
    queryFn: () => client.get<HealthAlert[]>('/health/alerts').then(r => r.data),
    staleTime: 5 * 60_000,   // re-check every 5 minutes
    refetchInterval: 5 * 60_000,
  })

  if (dismissed || !alerts || alerts.length === 0) return null

  const errorCount = alerts.filter(a => a.severity === 'error').length

  return (
    <Alert
      severity="error"
      icon={<ErrorOutlineOutlined fontSize="small" />}
      sx={{ borderRadius: 0, py: 0.5, flexShrink: 0, alignItems: 'flex-start' }}
      action={
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.3, mt: 0.2 }}>
          <IconButton size="small" color="inherit" onClick={() => setExpanded(e => !e)}>
            {expanded ? <ExpandLessOutlined fontSize="small" /> : <ExpandMoreOutlined fontSize="small" />}
          </IconButton>
          <IconButton
            size="small"
            color="inherit"
            onClick={() => {
              sessionStorage.setItem('health_banner_dismissed_at', new Date().toDateString())
              setDismissed(true)
            }}
          >
            <CloseOutlined fontSize="small" />
          </IconButton>
        </Box>
      }
    >
      <Box>
        <Typography variant="body2" fontWeight={600} sx={{ lineHeight: 1.4 }}>
          {errorCount} platform health issue{errorCount !== 1 ? 's' : ''} detected in the last 24h
          {' '}
          {alerts.map(a => (
            <Chip
              key={`${a.type}-${a.entity}`}
              label={TYPE_LABELS[a.type] ?? a.type}
              size="small"
              sx={{ fontSize: '0.65rem', height: 16, ml: 0.4, bgcolor: 'rgba(255,255,255,0.15)', color: 'inherit' }}
            />
          ))}
        </Typography>

        <Collapse in={expanded}>
          <Box sx={{ mt: 0.8 }}>
            {alerts.map((alert, i) => (
              <Box key={i} sx={{ display: 'flex', gap: 1, mb: 0.5, alignItems: 'flex-start' }}>
                <Typography variant="caption" sx={{ color: 'inherit', opacity: 0.7, whiteSpace: 'nowrap', mt: 0.1 }}>
                  {fmtTime(alert.detected_at)}
                </Typography>
                <Chip
                  label={TYPE_LABELS[alert.type] ?? alert.type}
                  size="small"
                  sx={{ fontSize: '0.65rem', height: 16, flexShrink: 0, bgcolor: 'rgba(255,255,255,0.2)', color: 'inherit' }}
                />
                <Typography variant="caption" sx={{ color: 'inherit', lineHeight: 1.5 }}>
                  {alert.message}
                </Typography>
              </Box>
            ))}
          </Box>
        </Collapse>
      </Box>
    </Alert>
  )
}
