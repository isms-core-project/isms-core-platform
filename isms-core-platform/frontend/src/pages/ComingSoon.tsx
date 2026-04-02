import { Box, Typography, Chip } from '@mui/material'
import { ConstructionOutlined } from '@mui/icons-material'
import PageHeader from '../components/PageHeader'

interface Props {
  title: string
  phase: string
  description: string
}

export default function ComingSoon({ title, phase, description }: Props) {
  return (
    <Box sx={{ p: 3 }}>
      <PageHeader title={title} subtitle={description} />
      <Box sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center', py: 10, gap: 2 }}>
        <ConstructionOutlined sx={{ fontSize: 56, color: 'text.disabled' }} />
        <Chip label={phase} size="small" sx={{ fontSize: '0.7rem', bgcolor: 'rgba(107,122,153,0.12)', color: 'text.secondary' }} />
        <Typography variant="body2" color="text.disabled">This module is under development.</Typography>
      </Box>
    </Box>
  )
}
