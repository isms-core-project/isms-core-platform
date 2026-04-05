import { Box, Typography, type SxProps } from '@mui/material'
import type { ReactNode } from 'react'
import HelpLink from './HelpLink'

interface PageHeaderProps {
  title: string
  subtitle?: string
  actions?: ReactNode
  helpSection?: string   // anchor-id in the user manual, e.g. "qa-engine"
  sx?: SxProps
}

export default function PageHeader({ title, subtitle, actions, helpSection, sx }: PageHeaderProps) {
  return (
    <Box
      sx={{
        display: 'flex',
        alignItems: 'flex-start',
        justifyContent: 'space-between',
        mb: 3,
        ...sx,
      }}
    >
      <Box>
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.5 }}>
          <Typography variant="h4" sx={{ color: 'text.primary', mb: subtitle ? 0.25 : 0 }}>
            {title}
          </Typography>
          {helpSection && <HelpLink section={helpSection} />}
        </Box>
        {subtitle && (
          <Typography variant="body2" color="text.secondary">
            {subtitle}
          </Typography>
        )}
      </Box>
      {actions && <Box sx={{ display: 'flex', gap: 1, alignItems: 'center' }}>{actions}</Box>}
    </Box>
  )
}
