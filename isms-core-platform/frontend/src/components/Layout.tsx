import { useState } from 'react'
import { Box } from '@mui/material'
import { Outlet } from 'react-router-dom'
import Sidebar, { SIDEBAR_WIDTH, SIDEBAR_MINI_WIDTH } from './Sidebar'

export default function Layout() {
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

  return (
    <Box sx={{ display: 'flex', height: '100vh', overflow: 'hidden', bgcolor: 'background.default' }}>
      <Sidebar collapsed={collapsed} onToggle={handleToggle} />
      <Box
        component="main"
        sx={{
          ml: `${collapsed ? SIDEBAR_MINI_WIDTH : SIDEBAR_WIDTH}px`,
          flex: 1,
          minWidth: 0,
          height: '100%',
          overflowY: 'auto',
          p: 3,
          transition: 'margin-left 0.2s ease',
        }}
      >
        <Outlet />
      </Box>
    </Box>
  )
}
