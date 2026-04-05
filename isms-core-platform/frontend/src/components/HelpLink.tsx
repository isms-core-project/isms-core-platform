import { useNavigate } from 'react-router-dom'
import { IconButton, Tooltip } from '@mui/material'
import { HelpOutlineOutlined } from '@mui/icons-material'

interface HelpLinkProps {
  section: string   // matches the #anchor-id in the user manual
  size?: 'small' | 'medium'
}

/**
 * Small ? icon that opens the User Guide at the relevant section.
 * Usage: <HelpLink section="risk-register" />
 *        <HelpLink section="qa-engine" />
 */
export default function HelpLink({ section, size = 'small' }: HelpLinkProps) {
  const navigate = useNavigate()

  return (
    <Tooltip title="Open User Guide">
      <IconButton
        size={size}
        onClick={() => navigate(`/help#${section}`)}
        sx={{
          color: 'text.disabled',
          '&:hover': { color: 'primary.main' },
          p: 0.5,
        }}
      >
        <HelpOutlineOutlined fontSize="small" />
      </IconButton>
    </Tooltip>
  )
}
