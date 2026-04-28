import { Chip, useTheme, type ChipProps } from '@mui/material'

type Status = 'green' | 'amber' | 'red' | 'open' | 'closed' | 'accepted' |
  'not_assessed' | 'partial' | 'compliant' | 'non_compliant' | string

const DARK: Record<string, { bg: string; color: string }> = {
  green:         { bg: '#1a3a27',   color: '#C6EFCE' },
  compliant:     { bg: '#1a3a27',   color: '#C6EFCE' },
  closed:        { bg: '#1a3a27',   color: '#C6EFCE' },
  amber:         { bg: '#3d3200',   color: '#FFEB9C' },
  partial:       { bg: '#3d3200',   color: '#FFEB9C' },
  accepted:      { bg: '#3d3200',   color: '#FFEB9C' },
  red:           { bg: '#3a0000',   color: '#FFC7CE' },
  open:          { bg: '#3a0000',   color: '#FFC7CE' },
  non_compliant: { bg: '#3a0000',   color: '#FFC7CE' },
  not_assessed:  { bg: '#1a1f30',   color: '#8B9CC8' },
}

const LIGHT: Record<string, { bg: string; color: string }> = {
  green:         { bg: 'rgba(46,125,50,0.15)',    color: '#1b5e20' },
  compliant:     { bg: 'rgba(46,125,50,0.15)',    color: '#1b5e20' },
  closed:        { bg: 'rgba(46,125,50,0.15)',    color: '#1b5e20' },
  amber:         { bg: 'rgba(230,145,0,0.15)',    color: '#7a4800' },
  partial:       { bg: 'rgba(230,145,0,0.15)',    color: '#7a4800' },
  accepted:      { bg: 'rgba(230,145,0,0.15)',    color: '#7a4800' },
  red:           { bg: 'rgba(192,0,0,0.12)',      color: '#9e0000' },
  open:          { bg: 'rgba(192,0,0,0.12)',      color: '#9e0000' },
  non_compliant: { bg: 'rgba(192,0,0,0.12)',      color: '#9e0000' },
  not_assessed:  { bg: 'rgba(68,114,196,0.12)',   color: '#2E5099' },
}

interface StatusChipProps extends Omit<ChipProps, 'color'> {
  status: string
}

export default function StatusChip({ status, ...props }: StatusChipProps) {
  const { palette } = useTheme()
  const map = palette.mode === 'light' ? LIGHT : DARK
  const fallback = palette.mode === 'light'
    ? { bg: 'rgba(68,114,196,0.12)', color: '#2E5099' }
    : { bg: '#1a1f30', color: '#8B9CC8' }
  const colors = map[status] ?? fallback
  const label = status.replace(/_/g, ' ')

  return (
    <Chip
      label={label}
      size="small"
      sx={{
        bgcolor: colors.bg,
        color: colors.color,
        border: `1px solid ${colors.color}50`,
        fontWeight: 600,
        fontSize: '0.7rem',
        height: 20,
        textTransform: 'capitalize',
      }}
      {...props}
    />
  )
}
