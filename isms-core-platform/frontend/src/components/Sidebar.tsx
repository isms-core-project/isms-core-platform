import { useState } from 'react'
import {
  Box,
  List,
  ListItem,
  ListItemButton,
  ListItemIcon,
  ListItemText,
  Divider,
  Typography,
  Tooltip,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  Button,
  Switch,
  FormControlLabel,
  CircularProgress,
  Alert,
  Chip,
  Collapse,
  IconButton,
} from '@mui/material'
import {
  DashboardOutlined,
  AccountTreeOutlined,
  FindInPageOutlined,
  SearchOutlined,
  UploadFileOutlined,
  DeviceHubOutlined,
  AdminPanelSettingsOutlined,
  MonitorHeartOutlined,
  VerifiedOutlined,
  LogoutOutlined,
  ShieldOutlined,
  CompareArrowsOutlined,
  AssignmentOutlined,
  PolicyOutlined,
  CodeOutlined,
  ExploreOutlined,
  NotificationsOutlined,
  SummarizeOutlined,
  GppMaybeOutlined,
  GridViewOutlined,
  LockPersonOutlined,
  CloudOutlined,
  PersonOutlined,
  BusinessOutlined,
  PeopleOutlined,
  ExpandMoreOutlined,
  HomeOutlined,
  ElectricalServicesOutlined,
  ChevronLeftOutlined,
  ChevronRightOutlined,
  AccountBalanceOutlined,
  SecurityOutlined,
} from '@mui/icons-material'
import { useNavigate, useLocation } from 'react-router-dom'
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { adminApi } from '../api/admin'
import type { NotificationPref } from '../api/types'
import { useAuth } from '../store/AuthContext'
import { useProduct, type Product, type IsmsTier, PRODUCT_COLORS, PRODUCT_LABELS, PRODUCT_SUBTITLES } from '../store/ProductContext'

interface NavItem {
  label: string
  path: string
  icon: React.ReactNode
}

const PRODUCT_NAV: NavItem[] = [
  { label: 'Overview',    path: '/overview',    icon: <DashboardOutlined /> },
  { label: 'Coverage',    path: '/coverage',    icon: <CompareArrowsOutlined /> },
  { label: 'Controls',    path: '/controls',    icon: <AccountTreeOutlined /> },
  { label: 'Assessments', path: '/assessments', icon: <AssignmentOutlined /> },
  { label: 'Policies',    path: '/policies',    icon: <PolicyOutlined /> },
  { label: 'Gaps',        path: '/gaps',        icon: <FindInPageOutlined /> },
  { label: 'Evidence',    path: '/evidence',    icon: <UploadFileOutlined /> },
  { label: 'Graph',       path: '/graph',       icon: <DeviceHubOutlined /> },
]

const NAV_PLATFORM: NavItem[] = [
  { label: 'QA',          path: '/qa',          icon: <VerifiedOutlined /> },
  { label: 'Search',      path: '/search',      icon: <SearchOutlined /> },
  { label: 'Compass',     path: '/compass',     icon: <ExploreOutlined /> },
  { label: 'Generators',  path: '/generators',  icon: <CodeOutlined /> },
  { label: 'Report',      path: '/report',      icon: <SummarizeOutlined /> },
  { label: 'Risk Wizard', path: '/risk',        icon: <GppMaybeOutlined /> },
  { label: 'NIST CSF',    path: '/nist-csf',    icon: <GridViewOutlined /> },
  { label: 'NIS2',        path: '/nis2',        icon: <ShieldOutlined sx={{ fontSize: 20 }} /> },
  { label: 'DORA',        path: '/dora',        icon: <AccountBalanceOutlined /> },
  { label: 'CIS Controls', path: '/cis',        icon: <SecurityOutlined /> },
]

const NAV_ADMIN: NavItem[] = [
  { label: 'Admin',       path: '/admin',       icon: <AdminPanelSettingsOutlined /> },
  { label: 'Connectors',  path: '/connectors',  icon: <ElectricalServicesOutlined /> },
  { label: 'System',      path: '/system',      icon: <MonitorHeartOutlined /> },
]

const PRODUCT_SECTIONS: { value: Product; icon: React.ReactNode }[] = [
  { value: 'isms',    icon: <ShieldOutlined /> },
  { value: 'privacy', icon: <LockPersonOutlined /> },
  { value: 'cloud',   icon: <CloudOutlined /> },
]

const PRIVACY_SECTIONS = [
  { label: 'Controller', section: 'A.1', icon: <PersonOutlined sx={{ fontSize: 13 }} /> },
  { label: 'Processor',  section: 'A.2', icon: <BusinessOutlined sx={{ fontSize: 13 }} /> },
  { label: 'Shared',     section: 'A.3', icon: <PeopleOutlined sx={{ fontSize: 13 }} /> },
]

export const SIDEBAR_WIDTH = 220
export const SIDEBAR_MINI_WIDTH = 52

const CAT_LABEL: Record<string, string> = { workflow: 'Workflow', system: 'System' }
const CAT_COLOR: Record<string, string> = { workflow: '#1a3a27', system: '#1a2a3a' }
const CAT_TEXT:  Record<string, string> = { workflow: '#C6EFCE', system: '#9fc8f0' }
const PLATFORM_COLOR = '#6B7A99'
const PLATFORM_PATHS = ['/qa', '/search', '/compass', '/generators', '/report', '/risk', '/nist-csf', '/nis2', '/dora', '/cis', '/admin', '/connectors', '/system']

// ── Notification prefs dialog ─────────────────────────────────────────────────

function NotificationPrefsDialog({ open, onClose }: { open: boolean; onClose: () => void }) {
  const queryClient = useQueryClient()
  const { data, isLoading } = useQuery({
    queryKey: ['my', 'notification-prefs'],
    queryFn: adminApi.getMyNotificationPrefs,
    enabled: open,
  })

  const mutation = useMutation({
    mutationFn: (prefs: Record<string, boolean>) => adminApi.updateMyNotificationPrefs(prefs),
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ['my', 'notification-prefs'] }),
  })

  function toggle(pref: NotificationPref) {
    mutation.mutate({ [pref.event_type]: !pref.enabled })
  }

  const byCategory = data
    ? Object.entries(
        data.prefs.reduce<Record<string, NotificationPref[]>>((acc, p) => {
          ;(acc[p.category] ??= []).push(p)
          return acc
        }, {})
      )
    : []

  return (
    <Dialog open={open} onClose={onClose} maxWidth="xs" fullWidth>
      <DialogTitle sx={{ pb: 0.5 }}>
        Notification Preferences
        <Typography variant="caption" color="text.secondary" display="block">
          Choose which emails you receive
        </Typography>
      </DialogTitle>
      <DialogContent sx={{ pt: 1 }}>
        {isLoading && <CircularProgress size={20} sx={{ display: 'block', mx: 'auto', my: 2 }} />}
        {mutation.isError && (
          <Alert severity="error" sx={{ mb: 1.5, py: 0 }}>Failed to save — try again.</Alert>
        )}
        {byCategory.map(([cat, prefs]) => (
          <Box key={cat} sx={{ mb: 2 }}>
            <Chip
              label={CAT_LABEL[cat] ?? cat}
              size="small"
              sx={{ mb: 1, fontSize: '0.65rem', height: 18, bgcolor: CAT_COLOR[cat] ?? '#222', color: CAT_TEXT[cat] ?? '#fff' }}
            />
            {prefs.map((pref) => (
              <FormControlLabel
                key={pref.event_type}
                control={
                  <Switch
                    size="small"
                    checked={pref.enabled}
                    onChange={() => toggle(pref)}
                    disabled={mutation.isPending}
                  />
                }
                label={
                  <Box>
                    <Typography variant="body2">{pref.label}</Typography>
                    <Typography variant="caption" color="text.secondary" display="block">
                      {pref.description}
                    </Typography>
                  </Box>
                }
                sx={{ display: 'flex', alignItems: 'flex-start', mb: 1, ml: 0 }}
              />
            ))}
          </Box>
        ))}
      </DialogContent>
      <DialogActions sx={{ px: 3, pb: 2 }}>
        <Button onClick={onClose}>Close</Button>
      </DialogActions>
    </Dialog>
  )
}

// ── Main sidebar ──────────────────────────────────────────────────────────────

export default function Sidebar({ collapsed, onToggle }: { collapsed: boolean; onToggle: () => void }) {
  const navigate = useNavigate()
  const location = useLocation()
  const [notifsOpen, setNotifsOpen] = useState(false)
  const { logout, user } = useAuth()
  const { product, setProduct, ismsTier, setIsmsTier } = useProduct()

  const isNeutralPage = location.pathname === '/' || PLATFORM_PATHS.some(p => location.pathname.startsWith(p))
  const [expandedProduct, setExpandedProduct] = useState<Product | null>(isNeutralPage ? null : product)

  const TIER_OPTIONS: { value: IsmsTier; label: string; color: string }[] = [
    { value: 'all',         label: 'All', color: 'rgba(255,255,255,0.55)' },
    { value: 'framework',   label: 'FW',  color: PRODUCT_COLORS.isms },
    { value: 'operational', label: 'OP',  color: '#70AD47' },
  ]

  function handleSectionHeader(p: Product) {
    if (collapsed) {
      setProduct(p)
      setExpandedProduct(p)
      navigate('/overview')
      return
    }
    if (expandedProduct === p) {
      setExpandedProduct(null)
    } else {
      setExpandedProduct(p)
      setProduct(p)
    }
  }

  function handleNavItem(item: NavItem, p: Product) {
    setProduct(p)
    setExpandedProduct(p)
    navigate(item.path.split('?')[0])
  }

  function isProductNavActive(path: string, p: Product): boolean {
    const pathMatch = location.pathname === path || (path !== '/overview' && location.pathname.startsWith(path))
    return pathMatch && product === p
  }

  function isPlatformNavActive(path: string): boolean {
    return location.pathname === path || location.pathname.startsWith(path + '/')
  }

  const isControlsPath = location.pathname.startsWith('/controls')
  const currentSection = new URLSearchParams(location.search).get('section') ?? ''

  const sidebarWidth = collapsed ? SIDEBAR_MINI_WIDTH : SIDEBAR_WIDTH

  return (
    <Box
      sx={{
        width: sidebarWidth,
        flexShrink: 0,
        display: 'flex',
        flexDirection: 'column',
        bgcolor: 'background.paper',
        borderRight: '1px solid',
        borderColor: 'divider',
        height: '100vh',
        position: 'fixed',
        left: 0,
        top: 0,
        zIndex: 100,
        overflow: 'hidden',
        transition: 'width 0.2s ease',
      }}
    >
      {/* ── Logo ── */}
      <Box sx={{ position: 'relative', px: collapsed ? 0 : 2.5, pt: 2.5, pb: 1.5 }}>
        <Box
          onClick={() => navigate('/')}
          sx={{
            display: 'flex',
            alignItems: 'center',
            gap: collapsed ? 0 : 1,
            cursor: 'pointer',
            justifyContent: collapsed ? 'center' : 'flex-start',
            '&:hover': { opacity: 0.8 },
          }}
        >
          <ShieldOutlined sx={{ color: PRODUCT_COLORS[product], fontSize: 26, transition: 'color 0.2s', flexShrink: 0 }} />
          {!collapsed && (
            <Box>
              <Typography variant="h6" sx={{ color: PRODUCT_COLORS[product], lineHeight: 1, fontSize: '1rem', transition: 'color 0.2s', whiteSpace: 'nowrap' }}>
                ISMS CORE
              </Typography>
              <Typography variant="caption" sx={{ color: 'text.disabled', fontSize: '0.6rem', letterSpacing: '0.04em', whiteSpace: 'nowrap' }}>
                IS &amp; Privacy Compliance
              </Typography>
            </Box>
          )}
        </Box>

        {/* Collapse toggle — right edge */}
        <Box
          onClick={onToggle}
          sx={{
            position: 'absolute',
            right: -14,
            top: '50%',
            transform: 'translateY(-50%)',
            width: 28,
            height: 28,
            borderRadius: '50%',
            bgcolor: 'background.paper',
            border: '1px solid rgba(255,255,255,0.18)',
            boxShadow: '0 0 0 1px rgba(0,0,0,0.4), 0 2px 6px rgba(0,0,0,0.5)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            cursor: 'pointer',
            zIndex: 101,
            transition: 'background-color 0.15s, border-color 0.15s',
            '&:hover': { bgcolor: '#2a3550', borderColor: 'rgba(255,255,255,0.35)' },
          }}
        >
          {collapsed
            ? <ChevronRightOutlined sx={{ fontSize: 16, color: 'rgba(255,255,255,0.7)' }} />
            : <ChevronLeftOutlined sx={{ fontSize: 16, color: 'rgba(255,255,255,0.7)' }} />}
        </Box>
      </Box>

      <Divider />

      {/* ── Scrollable nav area ── */}
      <Box sx={{ flex: 1, overflowY: 'auto', overflowX: 'hidden', py: 0.5 }}>

        {/* Home */}
        <Box sx={{ px: 1, pt: 0.5, pb: 0.25 }}>
          <Tooltip title={collapsed ? 'Home' : ''} placement="right">
            <ListItemButton
              selected={location.pathname === '/'}
              onClick={() => navigate('/')}
              sx={{
                borderRadius: 1.5, py: 0.55,
                px: collapsed ? 0 : 1.5,
                justifyContent: collapsed ? 'center' : 'flex-start',
                '&.Mui-selected': { bgcolor: 'rgba(107,122,153,0.14)', color: '#6B7A99', '& .MuiListItemIcon-root': { color: '#6B7A99' } },
                '&:hover': { bgcolor: 'rgba(107,122,153,0.08)' },
              }}
            >
              <ListItemIcon sx={{ minWidth: collapsed ? 'unset' : 30, color: location.pathname === '/' ? '#6B7A99' : 'text.secondary' }}>
                <HomeOutlined sx={{ fontSize: 18 }} />
              </ListItemIcon>
              {!collapsed && (
                <ListItemText
                  primary="Home"
                  primaryTypographyProps={{ variant: 'body2', fontWeight: location.pathname === '/' ? 600 : 400, fontSize: '0.8rem' }}
                />
              )}
            </ListItemButton>
          </Tooltip>
        </Box>

        <Divider sx={{ my: 0.5, mx: 1 }} />

        {/* Product sections */}
        {PRODUCT_SECTIONS.map(({ value, icon }) => {
          const color = PRODUCT_COLORS[value]
          const isExpanded = expandedProduct === value && !collapsed
          const isActiveProduct = product === value

          return (
            <Box key={value}>
              <Tooltip title={collapsed ? PRODUCT_LABELS[value] : ''} placement="right">
                <Box
                  onClick={() => handleSectionHeader(value)}
                  sx={{
                    display: 'flex',
                    alignItems: 'center',
                    gap: collapsed ? 0 : 1,
                    mx: 1,
                    px: collapsed ? 0 : 1.25,
                    py: 0.65,
                    borderRadius: 1.5,
                    cursor: 'pointer',
                    userSelect: 'none',
                    justifyContent: collapsed ? 'center' : 'flex-start',
                    borderLeft: collapsed ? 'none' : `3px solid ${isActiveProduct ? color : 'transparent'}`,
                    bgcolor: isExpanded ? `${color}14` : 'transparent',
                    transition: 'all 0.15s',
                    '&:hover': {
                      bgcolor: `${color}10`,
                      ...(!collapsed && { borderLeftColor: color }),
                    },
                  }}
                >
                  <Box sx={{ color: isActiveProduct ? color : 'text.disabled', display: 'flex', transition: 'color 0.15s', fontSize: 16 }}>
                    {icon}
                  </Box>
                  {!collapsed && (
                    <>
                      <Box sx={{ flex: 1, minWidth: 0 }}>
                        <Typography
                          variant="caption"
                          sx={{ display: 'block', lineHeight: 1.2, fontWeight: isActiveProduct ? 700 : 500, fontSize: '0.72rem', color: isActiveProduct ? color : 'text.secondary', transition: 'color 0.15s', whiteSpace: 'nowrap' }}
                        >
                          {PRODUCT_LABELS[value]}
                        </Typography>
                        <Typography
                          variant="caption"
                          sx={{ display: 'block', lineHeight: 1.1, fontSize: '0.59rem', color: isActiveProduct ? `${color}99` : 'text.disabled', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}
                        >
                          {PRODUCT_SUBTITLES[value]}
                        </Typography>
                      </Box>
                      <Box sx={{ color: 'text.disabled', display: 'flex', fontSize: 16, transition: 'transform 0.2s', transform: isExpanded ? 'rotate(0deg)' : 'rotate(-90deg)' }}>
                        <ExpandMoreOutlined sx={{ fontSize: 16 }} />
                      </Box>
                    </>
                  )}
                </Box>
              </Tooltip>

              {/* Expanded submenu — only when sidebar is open */}
              <Collapse in={isExpanded} timeout={180} unmountOnExit>
                <Box sx={{ pb: 0.5 }}>
                  {value === 'isms' && (
                    <Box sx={{ mx: 2, mt: 0.5, mb: 0.75 }}>
                      <Box sx={{ display: 'flex', gap: 0.5 }}>
                        {TIER_OPTIONS.map(({ value: tv, label, color: tc }) => {
                          const tierActive = ismsTier === tv
                          return (
                            <Box
                              key={tv}
                              onClick={() => setIsmsTier(tv)}
                              sx={{
                                flex: 1, py: 0.4, borderRadius: 1, cursor: 'pointer',
                                textAlign: 'center', userSelect: 'none',
                                border: '1px solid',
                                borderColor: tierActive ? `${tc}60` : 'rgba(255,255,255,0.07)',
                                bgcolor: tierActive ? `${tc}20` : 'transparent',
                                transition: 'all 0.12s',
                                '&:hover': { borderColor: `${tc}45`, bgcolor: `${tc}12` },
                              }}
                            >
                              <Typography variant="caption" sx={{ fontSize: '0.62rem', fontWeight: tierActive ? 700 : 400, lineHeight: 1, color: tierActive ? tc : 'text.disabled' }}>
                                {label}
                              </Typography>
                            </Box>
                          )
                        })}
                      </Box>
                    </Box>
                  )}

                  <List disablePadding sx={{ px: 1 }}>
                    {PRODUCT_NAV.map((item) => {
                      const active = isProductNavActive(item.path, value)
                      const basePath = item.path.split('?')[0]
                      return (
                        <Box key={item.path}>
                          <ListItem disablePadding sx={{ mb: 0.15 }}>
                            <ListItemButton
                              selected={active}
                              onClick={() => handleNavItem(item, value)}
                              sx={{
                                borderRadius: 1.5, py: 0.5, px: 1.25, pl: 2,
                                '&.Mui-selected': { bgcolor: `${color}20`, color, '& .MuiListItemIcon-root': { color } },
                                '&:hover': { bgcolor: `${color}10` },
                              }}
                            >
                              <ListItemIcon sx={{ minWidth: 30, color: active ? color : 'text.secondary', transition: 'color 0.15s' }}>
                                <Box sx={{ '& svg': { fontSize: 18 } }}>{item.icon}</Box>
                              </ListItemIcon>
                              <ListItemText
                                primary={item.label}
                                primaryTypographyProps={{ variant: 'body2', fontWeight: active ? 600 : 400, fontSize: '0.8rem' }}
                              />
                            </ListItemButton>
                          </ListItem>

                          {value === 'privacy' && basePath === '/controls' && active && isControlsPath && (
                            <Box sx={{ pl: 4, pr: 0.5, pb: 0.25 }}>
                              {PRIVACY_SECTIONS.map((s) => {
                                const sActive = currentSection === s.section
                                return (
                                  <Box
                                    key={s.label}
                                    onClick={(e) => { e.stopPropagation(); navigate(`/controls?section=${s.section}`) }}
                                    sx={{
                                      display: 'flex', alignItems: 'center', gap: 0.75,
                                      px: 1, py: 0.3, borderRadius: 1, cursor: 'pointer', mb: 0.1,
                                      bgcolor: sActive ? `${color}18` : 'transparent',
                                      '&:hover': { bgcolor: `${color}10` },
                                    }}
                                  >
                                    <Box sx={{ color: sActive ? color : 'text.disabled' }}>{s.icon}</Box>
                                    <Typography variant="caption" sx={{ fontSize: '0.69rem', fontWeight: sActive ? 600 : 400, color: sActive ? color : 'text.secondary' }}>
                                      {s.label}
                                    </Typography>
                                  </Box>
                                )
                              })}
                            </Box>
                          )}
                        </Box>
                      )
                    })}
                  </List>
                </Box>
              </Collapse>

              <Divider sx={{ my: 0.5, mx: 1 }} />
            </Box>
          )
        })}

        {/* Platform pages */}
        <Box sx={{ pt: 0.25 }}>
          {!collapsed && (
            <Typography variant="caption" sx={{ px: 2.5, display: 'block', mb: 0.5, fontSize: '0.59rem', textTransform: 'uppercase', letterSpacing: '0.08em', color: 'text.disabled' }}>
              Platform
            </Typography>
          )}
          <List disablePadding sx={{ px: 1 }}>
            {NAV_PLATFORM.map((item) => {
              const active = isPlatformNavActive(item.path)
              return (
                <ListItem key={item.path} disablePadding sx={{ mb: 0.15 }}>
                  <Tooltip title={collapsed ? item.label : ''} placement="right">
                    <ListItemButton
                      selected={active}
                      onClick={() => navigate(item.path)}
                      sx={{
                        borderRadius: 1.5, py: 0.5,
                        px: collapsed ? 0 : 1.5,
                        justifyContent: collapsed ? 'center' : 'flex-start',
                        '&.Mui-selected': { bgcolor: `${PLATFORM_COLOR}20`, color: PLATFORM_COLOR, '& .MuiListItemIcon-root': { color: PLATFORM_COLOR } },
                        '&:hover': { bgcolor: `${PLATFORM_COLOR}12` },
                      }}
                    >
                      <ListItemIcon sx={{ minWidth: collapsed ? 'unset' : 30, color: active ? PLATFORM_COLOR : 'text.secondary', transition: 'color 0.15s' }}>
                        <Box sx={{ '& svg': { fontSize: 18 } }}>{item.icon}</Box>
                      </ListItemIcon>
                      {!collapsed && (
                        <ListItemText
                          primary={item.label}
                          primaryTypographyProps={{ variant: 'body2', fontWeight: active ? 600 : 400, fontSize: '0.8rem' }}
                        />
                      )}
                    </ListItemButton>
                  </Tooltip>
                </ListItem>
              )
            })}
          </List>
        </Box>

        <Divider sx={{ my: 0.5, mx: 1 }} />

        {/* Admin pages */}
        <List disablePadding sx={{ px: 1, pb: 0.5 }}>
          {NAV_ADMIN.map((item) => {
            const active = isPlatformNavActive(item.path)
            return (
              <ListItem key={item.path} disablePadding sx={{ mb: 0.15 }}>
                <Tooltip title={collapsed ? item.label : ''} placement="right">
                  <ListItemButton
                    selected={active}
                    onClick={() => navigate(item.path)}
                    sx={{
                      borderRadius: 1.5, py: 0.5,
                      px: collapsed ? 0 : 1.5,
                      justifyContent: collapsed ? 'center' : 'flex-start',
                      '&.Mui-selected': { bgcolor: `${PLATFORM_COLOR}20`, color: PLATFORM_COLOR, '& .MuiListItemIcon-root': { color: PLATFORM_COLOR } },
                      '&:hover': { bgcolor: `${PLATFORM_COLOR}12` },
                    }}
                  >
                    <ListItemIcon sx={{ minWidth: collapsed ? 'unset' : 30, color: active ? PLATFORM_COLOR : 'text.secondary', transition: 'color 0.15s' }}>
                      <Box sx={{ '& svg': { fontSize: 18 } }}>{item.icon}</Box>
                    </ListItemIcon>
                    {!collapsed && (
                      <ListItemText
                        primary={item.label}
                        primaryTypographyProps={{ variant: 'body2', fontWeight: active ? 600 : 400, fontSize: '0.8rem' }}
                      />
                    )}
                  </ListItemButton>
                </Tooltip>
              </ListItem>
            )
          })}
        </List>

      </Box>

      {/* ── Footer ── */}
      <Divider />
      <Box sx={{ px: collapsed ? 0.5 : 2, py: 1.5 }}>
        {!collapsed && user && (
          <Typography variant="caption" color="text.secondary" sx={{ display: 'block', mb: 0.5, overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
            {user.email}
          </Typography>
        )}
        <Tooltip title={collapsed ? 'Notifications' : ''} placement="right">
          <ListItemButton
            onClick={() => setNotifsOpen(true)}
            sx={{ borderRadius: 1.5, px: collapsed ? 0 : 1.5, py: 0.5, justifyContent: collapsed ? 'center' : 'flex-start' }}
          >
            <ListItemIcon sx={{ minWidth: collapsed ? 'unset' : 36, color: 'text.secondary' }}>
              <NotificationsOutlined fontSize="small" />
            </ListItemIcon>
            {!collapsed && (
              <ListItemText primary="Notifications" primaryTypographyProps={{ variant: 'body2', color: 'text.secondary' }} />
            )}
          </ListItemButton>
        </Tooltip>
        <Tooltip title={collapsed ? 'Sign out' : ''} placement="right">
          <ListItemButton
            onClick={logout}
            sx={{ borderRadius: 1.5, px: collapsed ? 0 : 1.5, py: 0.5, justifyContent: collapsed ? 'center' : 'flex-start' }}
          >
            <ListItemIcon sx={{ minWidth: collapsed ? 'unset' : 36, color: 'text.secondary' }}>
              <LogoutOutlined fontSize="small" />
            </ListItemIcon>
            {!collapsed && (
              <ListItemText primary="Sign out" primaryTypographyProps={{ variant: 'body2', color: 'text.secondary' }} />
            )}
          </ListItemButton>
        </Tooltip>
      </Box>

      <NotificationPrefsDialog open={notifsOpen} onClose={() => setNotifsOpen(false)} />
    </Box>
  )
}
