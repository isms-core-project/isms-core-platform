import { useState } from 'react'
import { Box, Alert, Button, IconButton, Card, CardContent, Typography } from '@mui/material'
import { CloseOutlined, LockOutlined } from '@mui/icons-material'
import { Outlet, useNavigate, useLocation } from 'react-router-dom'
import { useQuery } from '@tanstack/react-query'
import Sidebar, { SIDEBAR_WIDTH, SIDEBAR_MINI_WIDTH } from './Sidebar'
import { getMfaStatus } from '../api/auth'
import { orgApi } from '../api/orgApi'
import { useAuth } from '../store/AuthContext'

function MfaBanner({ mfaEnforced }: { mfaEnforced: boolean }) {
  const { token } = useAuth()
  const navigate = useNavigate()
  const [dismissed, setDismissed] = useState(
    () => sessionStorage.getItem('mfa_banner_dismissed') === 'true'
  )

  const { data } = useQuery({
    queryKey: ['mfa-status'],
    queryFn: () => getMfaStatus(token!),
    enabled: !!token && !dismissed,
    staleTime: 5 * 60_000,
  })

  // Enforced mode — banner handled by Layout blocking screen
  if (mfaEnforced || dismissed || !data || data.mfa_enabled) return null

  return (
    <Alert
      severity="warning"
      action={
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.5 }}>
          <Button color="inherit" size="small" onClick={() => navigate('/system')}>
            Set up now
          </Button>
          <IconButton
            size="small"
            color="inherit"
            onClick={() => {
              sessionStorage.setItem('mfa_banner_dismissed', 'true')
              setDismissed(true)
            }}
          >
            <CloseOutlined fontSize="small" />
          </IconButton>
        </Box>
      }
      sx={{ borderRadius: 0, py: 0.5, flexShrink: 0 }}
    >
      Your account is not protected with two-factor authentication.
    </Alert>
  )
}

export default function Layout() {
  const { token } = useAuth()
  const navigate = useNavigate()
  const location = useLocation()
  const [collapsed, setCollapsed] = useState(
    () => localStorage.getItem('sidebarCollapsed') === 'true'
  )

  function handleToggle() {
    setCollapsed(v => {
      const next = !v
      localStorage.setItem('sidebarCollapsed', String(next))
      return next
    })
  }

  const { data: mfaData } = useQuery({
    queryKey: ['mfa-status'],
    queryFn: () => getMfaStatus(token!),
    enabled: !!token,
    staleTime: 5 * 60_000,
  })

  const { data: orgData } = useQuery({
    queryKey: ['organisation'],
    queryFn: orgApi.get,
    enabled: !!token,
    staleTime: 5 * 60_000,
  })

  const mfaEnforced = Boolean(orgData?.settings?.mfa_required)
  // Default mfaEnabled to true until data loads — avoids brief flash of enforcement screen
  const mfaEnabled = mfaData?.mfa_enabled ?? true
  // Allow /system through so they can actually set up MFA
  const showEnforcement = mfaEnforced && mfaData !== undefined && !mfaEnabled && !location.pathname.startsWith('/system')

  const sidebarProps = { collapsed, onToggle: handleToggle }

  return (
    <Box sx={{ display: 'flex', height: '100vh', overflow: 'hidden', bgcolor: 'background.default' }}>
      <Sidebar {...sidebarProps} />
      <Box
        component="main"
        sx={{
          ml: `${collapsed ? SIDEBAR_MINI_WIDTH : SIDEBAR_WIDTH}px`,
          flex: 1,
          minWidth: 0,
          height: '100%',
          display: 'flex',
          flexDirection: 'column',
          transition: 'margin-left 0.2s ease',
        }}
      >
        {showEnforcement ? (
          <Box sx={{ flex: 1, overflowY: 'auto', display: 'flex', alignItems: 'center', justifyContent: 'center', p: 3 }}>
            <Card sx={{ maxWidth: 440, width: '100%' }}>
              <CardContent sx={{ p: 4, textAlign: 'center' }}>
                <LockOutlined sx={{ fontSize: 48, color: 'error.main', mb: 2 }} />
                <Typography variant="h5" sx={{ mb: 1 }}>
                  Two-factor authentication required
                </Typography>
                <Typography variant="body2" color="text.secondary" sx={{ mb: 3 }}>
                  Your organisation requires all accounts to be protected with two-factor authentication before accessing the platform.
                </Typography>
                <Button variant="contained" size="large" onClick={() => navigate('/system')}>
                  Set up two-factor authentication
                </Button>
              </CardContent>
            </Card>
          </Box>
        ) : (
          <>
            <MfaBanner mfaEnforced={mfaEnforced} />
            <Box sx={{ flex: 1, overflowY: 'auto', p: 3 }}>
              <Outlet />
            </Box>
          </>
        )}
      </Box>
    </Box>
  )
}
