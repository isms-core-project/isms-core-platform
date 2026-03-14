import { Chip, type ChipProps } from '@mui/material'

type Status = 'green' | 'amber' | 'red' | 'open' | 'closed' | 'accepted' |
  'not_assessed' | 'partial' | 'compliant' | 'non_compliant' | string

const STATUS_COLORS: Record<Status, { bg: string; color: string }> = {
  green:          { bg: '#1a3a27', color: '#C6EFCE' },
  compliant:      { bg: '#1a3a27', color: '#C6EFCE' },
  closed:         { bg: '#1a3a27', color: '#C6EFCE' },
  amber:          { bg: '#3d3200', color: '#FFEB9C' },
  partial:        { bg: '#3d3200', color: '#FFEB9C' },
  accepted:       { bg: '#3d3200', color: '#FFEB9C' },
  red:            { bg: '#3a0000', color: '#FFC7CE' },
  open:           { bg: '#3a0000', color: '#FFC7CE' },
  non_compliant:  { bg: '#3a0000', color: '#FFC7CE' },
  not_assessed:   { bg: '#1a1f30', color: '#8B9CC8' },
}

interface StatusChipProps extends Omit<ChipProps, 'color'> {
  status: string
}

export default function StatusChip({ status, ...props }: StatusChipProps) {
  const colors = STATUS_COLORS[status] ?? { bg: '#1a1f30', color: '#8B9CC8' }
  const label = status.replace(/_/g, ' ')

  return (
    <Chip
      label={label}
      size="small"
      sx={{
        bgcolor: colors.bg,
        color: colors.color,
        border: `1px solid ${colors.color}30`,
        fontWeight: 600,
        fontSize: '0.7rem',
        height: 20,
        textTransform: 'capitalize',
      }}
      {...props}
    />
  )
}
