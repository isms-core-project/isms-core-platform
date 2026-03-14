import { Box } from '@mui/material'
import { Outlet } from 'react-router-dom'
import Sidebar, { SIDEBAR_WIDTH } from './Sidebar'

export default function Layout() {
  return (
    <Box sx={{ display: 'flex', height: '100vh', overflow: 'hidden', bgcolor: 'background.default' }}>
      <Sidebar />
      <Box
        component="main"
        sx={{
          ml: `${SIDEBAR_WIDTH}px`,
          flex: 1,
          minWidth: 0,
          height: '100%',
          overflowY: 'auto',
          p: 3,
        }}
      >
        <Outlet />
      </Box>
    </Box>
  )
}
