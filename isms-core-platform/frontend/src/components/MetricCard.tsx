import { Card, CardContent, Typography, Box, LinearProgress, type SxProps } from '@mui/material'
import type { ReactNode } from 'react'

interface MetricCardProps {
  title: string
  value: string | number
  subtitle?: string
  icon?: ReactNode
  progress?: number
  progressColor?: 'primary' | 'secondary' | 'error' | 'warning' | 'success' | 'info'
  sx?: SxProps
}

export default function MetricCard({
  title,
  value,
  subtitle,
  icon,
  progress,
  progressColor = 'primary',
  sx,
}: MetricCardProps) {
  return (
    <Card sx={{ height: '100%', ...sx }}>
      <CardContent sx={{ pb: '12px !important' }}>
        <Box sx={{ display: 'flex', alignItems: 'flex-start', justifyContent: 'space-between', mb: 1 }}>
          <Typography variant="caption" color="text.secondary" sx={{ textTransform: 'uppercase', letterSpacing: '0.06em', fontWeight: 600 }}>
            {title}
          </Typography>
          {icon && <Box sx={{ color: 'primary.main', opacity: 0.7 }}>{icon}</Box>}
        </Box>
        <Typography variant="h3" sx={{ mb: subtitle || progress !== undefined ? 0.5 : 0 }}>
          {value}
        </Typography>
        {subtitle && (
          <Typography variant="caption" color="text.secondary">
            {subtitle}
          </Typography>
        )}
        {progress !== undefined && (
          <Box sx={{ mt: 1 }}>
            <LinearProgress
              variant="determinate"
              value={progress}
              color={progressColor}
              sx={{ bgcolor: 'rgba(68,114,196,0.12)' }}
            />
          </Box>
        )}
      </CardContent>
    </Card>
  )
}
