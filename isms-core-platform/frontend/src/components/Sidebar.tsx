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
  FolderOpenOutlined,
  CloseOutlined,
  DarkModeOutlined,
  LightModeOutlined,
  WarningAmberOutlined,
  TuneOutlined,
  HandshakeOutlined,
  SettingsOutlined,
  HealthAndSafetyOutlined,
  PsychologyOutlined,
  InsightsOutlined,
  AppRegistrationOutlined,
  UpdateOutlined,
  HelpOutlineOutlined,
  BugReportOutlined,
  TravelExploreOutlined,
  StreamOutlined,
  ManageSearchOutlined,
  MenuBookOutlined,
} from '@mui/icons-material'
import { useNavigate, useLocation } from 'react-router-dom'
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { adminApi } from '../api/admin'
import { client } from '../api/client'
import type { NotificationPref } from '../api/types'
import { useAuth } from '../store/AuthContext'
import { useProduct, type Product, PRODUCT_COLORS, PRODUCT_LABELS, PRODUCT_SUBTITLES } from '../store/ProductContext'
import { useProject } from '../store/ProjectContext'
import { useThemeMode } from '../store/ThemeContext'

interface NavItem {
  label: string
  path: string
  icon: React.ReactNode
  adminOnly?: boolean         // admin + super_admin only
  superAdminOnly?: boolean    // super_admin only
  managerAndAbove?: boolean   // isms_manager + admin + super_admin only
  notViewer?: boolean         // all roles except viewer
}

interface NavRegion {
  label: string               // region display name (e.g. "Switzerland")
  items: NavItem[]
}

// ── Per-product nav (shown inside each product section) ───────────────────────
const PRODUCT_NAV: NavItem[] = [
  { label: 'Overview',        path: '/overview',    icon: <DashboardOutlined /> },
  { label: 'Coverage',        path: '/coverage',    icon: <CompareArrowsOutlined /> },
  { label: 'Controls Library',path: '/controls',    icon: <AccountTreeOutlined /> },
  { label: 'Assessments',     path: '/assessments', icon: <AssignmentOutlined /> },
  { label: 'Policies',        path: '/policies',    icon: <PolicyOutlined /> },
  { label: 'Gaps',            path: '/gaps',        icon: <FindInPageOutlined /> },
  { label: 'Evidence',        path: '/evidence',    icon: <UploadFileOutlined /> },
  { label: 'Graph',           path: '/graph',       icon: <DeviceHubOutlined /> },
]

// ── Risk & compliance management (Phase 12+) ──────────────────────────────────
const NAV_RISK: NavItem[] = [
  { label: 'Risk Register',   path: '/risk-register', icon: <WarningAmberOutlined /> },
  { label: 'Remediation',     path: '/remediation',   icon: <AssignmentOutlined /> },
  { label: 'KPI Metrics',     path: '/metrics',       icon: <InsightsOutlined />,      notViewer: true },
  { label: 'BIA',             path: '/bia',            icon: <HealthAndSafetyOutlined />, notViewer: true },
  { label: 'EBIOS RM',        path: '/ebios',          icon: <PsychologyOutlined />,    notViewer: true },
]

// ── Tools (platform utilities) ────────────────────────────────────────────────
const NAV_TOOLS: NavItem[] = [
  { label: 'Projects',        path: '/projects',       icon: <FolderOpenOutlined /> },
  { label: 'QA',              path: '/qa',             icon: <VerifiedOutlined />,     notViewer: true },
  { label: 'Search',          path: '/search',         icon: <SearchOutlined /> },
  { label: 'Compass',         path: '/compass',        icon: <ExploreOutlined /> },
  { label: 'Glossary',        path: '/glossary',       icon: <MenuBookOutlined /> },
  { label: 'Generators',      path: '/generators',     icon: <CodeOutlined />,         managerAndAbove: true },
  { label: 'Report',          path: '/report',         icon: <SummarizeOutlined />,    notViewer: true },
  { label: 'Risk Wizard',     path: '/risk',           icon: <GppMaybeOutlined />,     notViewer: true },
]

// ── External compliance frameworks ────────────────────────────────────────────
const NAV_FRAMEWORK_REGIONS: NavRegion[] = [
  {
    label: 'Global',
    items: [
      { label: 'NIST CSF 2.0',      path: '/nist-csf',     icon: <GridViewOutlined /> },
      { label: 'NIST AI RMF 1.0',   path: '/nist-ai-rmf',  icon: <PolicyOutlined /> },
      { label: 'NIST SP 800-53 R5', path: '/nist-800-53',  icon: <SecurityOutlined /> },
      { label: 'CIS Controls',       path: '/cis',       icon: <SecurityOutlined /> },
      { label: 'COBIT 2019',         path: '/cobit',     icon: <AccountBalanceOutlined /> },
      { label: 'CSA CCM v4.1',       path: '/csa-ccm',   icon: <CloudOutlined /> },
      { label: 'CSA AI Controls',    path: '/csa-aicm',  icon: <PolicyOutlined /> },
    ],
  },
  {
    label: 'European Union',
    items: [
      { label: 'NIS2',               path: '/nis2',          icon: <ShieldOutlined sx={{ fontSize: 20 }} /> },
      { label: 'DORA',               path: '/dora',          icon: <AccountBalanceOutlined /> },
      { label: 'EU Cyber Resilience', path: '/cra',          icon: <SecurityOutlined /> },
      { label: 'EU AI Act',          path: '/ai-act',        icon: <PolicyOutlined /> },
      { label: 'EU Cloud Sovereignty', path: '/eu-cloud-sov', icon: <CloudOutlined /> },
    ],
  },
  {
    label: 'Switzerland',
    items: [
      { label: 'Swiss ISG (SR 128)', path: '/isg',   icon: <ShieldOutlined sx={{ fontSize: 20 }} /> },
      { label: 'CSRM (NCSC CH)',     path: '/csrm',  icon: <LockPersonOutlined /> },
      { label: 'Swiss nDSG',         path: '/ndsg',  icon: <LockPersonOutlined /> },
    ],
  },
  {
    label: 'United Kingdom',
    items: [
      { label: 'UK NIS Regulations', path: '/uk-nis',          icon: <ShieldOutlined sx={{ fontSize: 20 }} /> },
      { label: 'UK Op. Resilience',  path: '/uk-op-resilience', icon: <AccountBalanceOutlined /> },
    ],
  },
  {
    label: 'Germany',
    items: [
      { label: 'BaFin BAIT',         path: '/bafin-bait', icon: <AccountBalanceOutlined /> },
      { label: 'BSI IT-Grundschutz', path: '/bsi',        icon: <ShieldOutlined sx={{ fontSize: 20 }} /> },
      { label: 'TISAX',              path: '/tisax',      icon: <VerifiedOutlined /> },
    ],
  },
  {
    label: 'Belgium',
    items: [
      { label: 'CyberFundamentals',  path: '/cyfun-be', icon: <ShieldOutlined sx={{ fontSize: 20 }} /> },
    ],
  },
  {
    label: 'Luxembourg',
    items: [
      { label: 'CSSF 20-750',        path: '/cssf-lu', icon: <AccountBalanceOutlined /> },
    ],
  },
  {
    label: 'Italy',
    items: [
      { label: 'ACN Guidelines',     path: '/acn-it', icon: <ShieldOutlined sx={{ fontSize: 20 }} /> },
    ],
  },
]

// ── Intelligence (Phase 25/28) ────────────────────────────────────────────────
const NAV_INTELLIGENCE: NavItem[] = [
  { label: 'Threat Feeds',      path: '/threat-feeds',     icon: <StreamOutlined /> },
  { label: 'MITRE ATT&CK',      path: '/mitre-attack',     icon: <BugReportOutlined /> },
  { label: 'ATT&CK Heatmap',    path: '/mitre-heatmap',    icon: <GridViewOutlined /> },
  { label: 'MITRE Groups',      path: '/mitre-groups',     icon: <PeopleOutlined /> },
  { label: 'MITRE Software',    path: '/mitre-software',   icon: <CodeOutlined /> },
  { label: 'MITRE Campaigns',   path: '/mitre-campaigns',  icon: <InsightsOutlined /> },
  { label: 'MITRE ATLAS',       path: '/mitre-atlas',      icon: <TravelExploreOutlined /> },
  { label: 'CVE / CPE',         path: '/cve-explorer',     icon: <ManageSearchOutlined /> },
]

// ── Suppliers / TPRM (Phase 16+) ──────────────────────────────────────────────
const NAV_SUPPLIERS: NavItem[] = [
  { label: 'TPRM',            path: '/tprm',        icon: <HandshakeOutlined />,    notViewer: true },
]

// ── Admin ─────────────────────────────────────────────────────────────────────
const NAV_ADMIN: NavItem[] = [
  { label: 'Users',             path: '/admin',             icon: <PeopleOutlined />, adminOnly: true },
  { label: 'Connectors',        path: '/connectors',        icon: <ElectricalServicesOutlined />, adminOnly: true },
  { label: 'Custom Frameworks', path: '/custom-frameworks',  icon: <AppRegistrationOutlined />, adminOnly: true },
  { label: 'Framework Tracker', path: '/framework-tracker',  icon: <UpdateOutlined />,        adminOnly: true },
  { label: 'Crosswalk Tracker', path: '/crosswalk-tracker', icon: <AccountTreeOutlined />,    adminOnly: true },
  { label: 'System',            path: '/system',             icon: <MonitorHeartOutlined />,  adminOnly: true },
  { label: 'Organisations',     path: '/organisations',     icon: <BusinessOutlined />, superAdminOnly: true },
]

const ADMIN_ROLES    = ['super_admin', 'admin']
const MANAGER_ROLES  = ['super_admin', 'admin', 'isms_manager']
const NON_VIEWER_ROLES = ['super_admin', 'admin', 'isms_manager', 'auditor', 'control_owner']

const PRODUCT_SECTIONS: { value: Product; icon: React.ReactNode }[] = [
  { value: 'isms',    icon: <ShieldOutlined /> },
  { value: 'privacy', icon: <LockPersonOutlined /> },
  { value: 'cloud',   icon: <CloudOutlined /> },
  { value: 'ai',      icon: <PsychologyOutlined /> },
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
const PLATFORM_COLOR    = '#6B7A99'
const INTEL_COLOR       = '#B84F00'

const RISK_PATHS       = ['/risk-register', '/remediation', '/metrics', '/bia', '/ebios']
const TOOLS_PATHS      = ['/projects', '/qa', '/search', '/compass', '/generators', '/report', '/risk', '/glossary']
const FRAMEWORK_PATHS  = ['/nist-csf', '/nist-ai-rmf', '/nist-800-53', '/nis2', '/dora', '/uk-nis', '/uk-op-resilience', '/cyfun-be', '/bafin-bait', '/cssf-lu', '/acn-it', '/cis', '/bsi', '/csrm', '/tisax', '/ndsg', '/isg', '/cra', '/ai-act', '/eu-cloud-sov', '/cobit', '/csa-ccm', '/csa-aicm']
const SUPPLIER_PATHS   = ['/tprm']
const ADMIN_PATHS        = ['/admin', '/connectors', '/system', '/organisations', '/custom-frameworks', '/framework-tracker', '/crosswalk-tracker']
const INTELLIGENCE_PATHS = ['/threat-feeds', '/mitre-attack', '/mitre-atlas', '/mitre-groups', '/mitre-software', '/mitre-campaigns', '/mitre-heatmap', '/cve-explorer']
const ALL_PLATFORM_PATHS = [...RISK_PATHS, ...TOOLS_PATHS, ...FRAMEWORK_PATHS, ...SUPPLIER_PATHS, ...ADMIN_PATHS, ...INTELLIGENCE_PATHS]

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

// ── Reusable collapsible nav group ────────────────────────────────────────────

interface NavGroupProps {
  label: string
  icon: React.ReactNode
  items?: NavItem[]
  regions?: NavRegion[]
  open: boolean
  onToggle: () => void
  collapsed: boolean           // sidebar mini mode
  color?: string
  currentUser: { role: string } | null
  isSuperAdmin: boolean
  onNavigate: (path: string) => void
  isActive: (path: string) => boolean
  hasBadge?: boolean           // red alert dot
}

function NavItemRow({ item, color, isActive, onNavigate, indent = false }: {
  item: NavItem; color: string; isActive: (p: string) => boolean
  onNavigate: (p: string) => void; indent?: boolean
}) {
  const active = isActive(item.path)
  return (
    <ListItem disablePadding sx={{ mb: 0.15 }}>
      <ListItemButton
        selected={active}
        onClick={() => onNavigate(item.path)}
        sx={{
          borderRadius: 1.5, py: 0.5, px: 1.25, pl: indent ? 2.5 : 2,
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
  )
}

function NavGroup({ label, icon, items, regions, open, onToggle, collapsed, color = PLATFORM_COLOR, currentUser, isSuperAdmin, onNavigate, isActive, hasBadge }: NavGroupProps) {
  const role = currentUser?.role ?? ''

  function filterItems(list: NavItem[]): NavItem[] {
    return list.filter(item => {
      if (item.superAdminOnly)   return isSuperAdmin
      if (item.adminOnly)        return ADMIN_ROLES.includes(role)
      if (item.managerAndAbove)  return MANAGER_ROLES.includes(role)
      if (item.notViewer)        return NON_VIEWER_ROLES.includes(role)
      return true
    })
  }

  // For regions mode: find which region contains the active path (for auto-expand)
  const activeRegionLabel = regions?.find(r => r.items.some(i => isActive(i.path)))?.label ?? regions?.[0]?.label ?? ''
  const [openRegions, setOpenRegions] = useState<Set<string>>(() => new Set([activeRegionLabel]))

  function toggleRegion(regionLabel: string) {
    setOpenRegions(prev => {
      const next = new Set(prev)
      if (next.has(regionLabel)) next.delete(regionLabel)
      else next.add(regionLabel)
      return next
    })
  }

  // Visibility check
  if (regions) {
    const hasAny = regions.some(r => filterItems(r.items).length > 0)
    if (!hasAny) return null
  } else {
    const visibleItems = filterItems(items ?? [])
    if (visibleItems.length === 0) return null
  }

  return (
    <Box>
      <Tooltip title={collapsed ? label : ''} placement="right">
        <Box
          onClick={onToggle}
          sx={{
            display: 'flex', alignItems: 'center',
            gap: collapsed ? 0 : 1,
            mx: 1, px: collapsed ? 0 : 1.25, py: 0.6,
            borderRadius: 1.5, cursor: 'pointer', userSelect: 'none',
            justifyContent: collapsed ? 'center' : 'flex-start',
            '&:hover': { bgcolor: `${color}10` },
          }}
        >
          <Box sx={{ color: open ? color : 'text.disabled', display: 'flex', fontSize: 16, flexShrink: 0 }}>
            {icon}
          </Box>
          {!collapsed && (
            <>
              <Typography
                variant="caption"
                sx={{ flex: 1, fontSize: '0.62rem', textTransform: 'uppercase', letterSpacing: '0.07em', color: open ? color : 'text.disabled', fontWeight: open ? 600 : 400 }}
              >
                {label}
              </Typography>
              {hasBadge && (
                <Box sx={{ width: 7, height: 7, borderRadius: '50%', bgcolor: '#f44336', flexShrink: 0, mr: 0.5 }} />
              )}
              <Box sx={{ color: 'text.disabled', display: 'flex', transition: 'transform 0.2s', transform: open ? 'rotate(0deg)' : 'rotate(-90deg)' }}>
                <ExpandMoreOutlined sx={{ fontSize: 14 }} />
              </Box>
            </>
          )}
        </Box>
      </Tooltip>

      <Collapse in={open && !collapsed} timeout={180} unmountOnExit>
        {regions ? (
          /* ── Nested region sub-groups ── */
          <Box sx={{ pb: 0.5 }}>
            {regions.map((region) => {
              const visibleItems = filterItems(region.items)
              if (visibleItems.length === 0) return null
              const regionOpen = openRegions.has(region.label)
              const hasActive = visibleItems.some(i => isActive(i.path))
              return (
                <Box key={region.label}>
                  {/* Region header */}
                  <Box
                    onClick={() => toggleRegion(region.label)}
                    sx={{
                      display: 'flex', alignItems: 'center', gap: 0.5,
                      mx: 1, px: 1.5, py: 0.35,
                      borderRadius: 1, cursor: 'pointer', userSelect: 'none',
                      '&:hover': { bgcolor: `${color}08` },
                    }}
                  >
                    <Typography
                      variant="caption"
                      sx={{
                        flex: 1, fontSize: '0.6rem', textTransform: 'uppercase',
                        letterSpacing: '0.06em', fontWeight: hasActive ? 600 : 400,
                        color: hasActive ? `${color}cc` : 'text.disabled',
                      }}
                    >
                      {region.label}
                    </Typography>
                    <Box sx={{ color: 'text.disabled', display: 'flex', transition: 'transform 0.18s', transform: regionOpen ? 'rotate(0deg)' : 'rotate(-90deg)' }}>
                      <ExpandMoreOutlined sx={{ fontSize: 11 }} />
                    </Box>
                  </Box>
                  <Collapse in={regionOpen} timeout={140} unmountOnExit>
                    <List disablePadding sx={{ px: 1, pb: 0.25 }}>
                      {visibleItems.map((item) => (
                        <NavItemRow key={item.path} item={item} color={color} isActive={isActive} onNavigate={onNavigate} indent />
                      ))}
                    </List>
                  </Collapse>
                </Box>
              )
            })}
          </Box>
        ) : (
          /* ── Flat item list ── */
          <List disablePadding sx={{ px: 1, pb: 0.5 }}>
            {filterItems(items ?? []).map((item) => (
              <NavItemRow key={item.path} item={item} color={color} isActive={isActive} onNavigate={onNavigate} />
            ))}
          </List>
        )}
      </Collapse>
    </Box>
  )
}

// ── Main sidebar ──────────────────────────────────────────────────────────────

type IsmsTier = 'all' | 'framework' | 'operational'

export default function Sidebar({ collapsed, onToggle }: { collapsed: boolean; onToggle: () => void }) {
  const navigate = useNavigate()
  const location = useLocation()
  const [notifsOpen, setNotifsOpen] = useState(false)
  const { logout, user, isSuperAdmin } = useAuth()
  const { product, setProduct, ismsTier, setIsmsTier } = useProduct()
  const { getActiveProject, setActiveProject, activeProjectsMap } = useProject()
  const activeProject = getActiveProject(product.toUpperCase())
  const activeFamilies = (['ISMS', 'PRIVACY', 'CLOUD'] as const).filter(f => !!activeProjectsMap[f])
  const { mode, toggleTheme } = useThemeMode()

  const isNeutralPage = location.pathname === '/' || ALL_PLATFORM_PATHS.some(p => location.pathname.startsWith(p))
  const isRiskPath       = RISK_PATHS.some(p => location.pathname.startsWith(p))
  const isToolsPath      = TOOLS_PATHS.some(p => location.pathname.startsWith(p))
  const isFrameworkPath  = FRAMEWORK_PATHS.some(p => location.pathname.startsWith(p))
  const isSupplierPath   = SUPPLIER_PATHS.some(p => location.pathname.startsWith(p))
  const isAdminPath      = ADMIN_PATHS.some(p => location.pathname.startsWith(p))
  const isIntelPath      = INTELLIGENCE_PATHS.some(p => location.pathname.startsWith(p))

  const [expandedProduct, setExpandedProduct] = useState<Product | null>(isNeutralPage ? null : product)
  const [riskOpen,        setRiskOpen]        = useState(isRiskPath)
  const [toolsOpen,       setToolsOpen]       = useState(isToolsPath)
  const [frameworksOpen,  setFrameworksOpen]  = useState(isFrameworkPath)
  const [suppliersOpen,   setSuppliersOpen]   = useState(isSupplierPath)
  const [adminOpen,       setAdminOpen]       = useState(isAdminPath)
  const [intelOpen,       setIntelOpen]       = useState(isIntelPath)

  const { data: healthAlerts } = useQuery<{ type: string }[]>({
    queryKey: ['health', 'alerts'],
    queryFn: () => client.get<{ type: string }[]>('/health/alerts').then(r => r.data),
    staleTime: 5 * 60_000,
    refetchInterval: 5 * 60_000,
    enabled: !!user,
  })
  const hasIntelAlert     = (healthAlerts ?? []).some(a => a.type === 'feed_failure' || a.type === 'opensearch_down')
  const hasConnectorAlert = (healthAlerts ?? []).some(a => a.type === 'connector_failure')

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

  const groupProps = {
    collapsed,
    color: PLATFORM_COLOR,
    currentUser: user,
    isSuperAdmin,
    onNavigate: navigate,
    isActive: isPlatformNavActive,
  }

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
            display: 'flex', alignItems: 'center', gap: collapsed ? 0 : 1,
            cursor: 'pointer', justifyContent: collapsed ? 'center' : 'flex-start',
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

        {/* Collapse toggle */}
        <Box
          onClick={onToggle}
          sx={{
            position: 'absolute', right: -14, top: '50%', transform: 'translateY(-50%)',
            width: 28, height: 28, borderRadius: '50%',
            bgcolor: 'background.paper', border: '1px solid rgba(255,255,255,0.18)',
            boxShadow: '0 0 0 1px rgba(0,0,0,0.4), 0 2px 6px rgba(0,0,0,0.5)',
            display: 'flex', alignItems: 'center', justifyContent: 'center',
            cursor: 'pointer', zIndex: 101, transition: 'background-color 0.15s, border-color 0.15s',
            '&:hover': { bgcolor: '#2a3550', borderColor: 'rgba(255,255,255,0.35)' },
          }}
        >
          {collapsed
            ? <ChevronRightOutlined sx={{ fontSize: 16, color: 'rgba(255,255,255,0.7)' }} />
            : <ChevronLeftOutlined  sx={{ fontSize: 16, color: 'text.secondary' }} />}
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

        {/* Active project chips */}
        <Box sx={{ px: 1, pb: 0.5, display: 'flex', flexDirection: 'column', gap: 0.4 }}>
          {activeFamilies.length === 0 ? (
            <Tooltip title={collapsed ? 'No active projects' : ''} placement="right">
              <Box
                onClick={() => navigate('/projects')}
                sx={{
                  display: 'flex', alignItems: 'center', gap: 0.75,
                  px: collapsed ? 0 : 1.25, py: 0.5, borderRadius: 1.5,
                  cursor: 'pointer', justifyContent: collapsed ? 'center' : 'flex-start',
                  border: '1px solid rgba(255,255,255,0.08)',
                }}
              >
                <FolderOpenOutlined sx={{ fontSize: 14, color: 'text.disabled', flexShrink: 0 }} />
                {!collapsed && (
                  <Typography variant="caption" sx={{ fontSize: '0.72rem', color: 'text.disabled' }}>
                    No active projects
                  </Typography>
                )}
              </Box>
            </Tooltip>
          ) : activeFamilies.map(fam => {
            const proj = activeProjectsMap[fam]!
            const color = PRODUCT_COLORS[fam.toLowerCase() as Product]
            return (
              <Tooltip key={fam} title={collapsed ? `${fam}: ${proj.name}` : ''} placement="right">
                <Box
                  onClick={() => navigate('/projects')}
                  sx={{
                    display: 'flex', alignItems: 'center', gap: 0.75,
                    px: collapsed ? 0 : 1.25, py: 0.4, borderRadius: 1.5,
                    cursor: 'pointer', justifyContent: collapsed ? 'center' : 'flex-start',
                    border: '1px solid', borderColor: `${color}30`, bgcolor: `${color}08`,
                    transition: 'all 0.15s',
                    '&:hover': { borderColor: `${color}60`, bgcolor: `${color}14` },
                  }}
                >
                  <FolderOpenOutlined sx={{ fontSize: 13, color, flexShrink: 0 }} />
                  {!collapsed && (
                    <>
                      <Box sx={{ flex: 1, minWidth: 0 }}>
                        <Typography variant="caption" sx={{ fontSize: '0.58rem', textTransform: 'uppercase', letterSpacing: '0.06em', color, opacity: 0.7, lineHeight: 1, display: 'block' }}>
                          {fam}
                        </Typography>
                        <Typography variant="caption" sx={{ fontSize: '0.7rem', color, fontWeight: 600, lineHeight: 1.2, display: 'block', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap', maxWidth: 110 }}>
                          {proj.name}
                        </Typography>
                      </Box>
                      <IconButton
                        size="small"
                        onClick={(e) => { e.stopPropagation(); setActiveProject(fam, null) }}
                        sx={{ p: 0.25, color: 'text.disabled', '&:hover': { color: 'error.main' } }}
                      >
                        <CloseOutlined sx={{ fontSize: 11 }} />
                      </IconButton>
                    </>
                  )}
                </Box>
              </Tooltip>
            )
          })}
        </Box>

        <Divider sx={{ my: 0.5, mx: 1 }} />

        {/* ── Product sections (ISMS / PRIVACY / CLOUD) ── */}
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
                    display: 'flex', alignItems: 'center', gap: collapsed ? 0 : 1,
                    mx: 1, px: collapsed ? 0 : 1.25, py: 0.65, borderRadius: 1.5,
                    cursor: 'pointer', userSelect: 'none',
                    justifyContent: collapsed ? 'center' : 'flex-start',
                    borderLeft: collapsed ? 'none' : `3px solid ${isActiveProduct ? color : 'transparent'}`,
                    bgcolor: isExpanded ? `${color}14` : 'transparent',
                    transition: 'all 0.15s',
                    '&:hover': { bgcolor: `${color}10`, ...(!collapsed && { borderLeftColor: color }) },
                  }}
                >
                  <Box sx={{ color: isActiveProduct ? color : 'text.disabled', display: 'flex', transition: 'color 0.15s', fontSize: 16 }}>
                    {icon}
                  </Box>
                  {!collapsed && (
                    <>
                      <Box sx={{ flex: 1, minWidth: 0 }}>
                        <Typography variant="caption" sx={{ display: 'block', lineHeight: 1.2, fontWeight: isActiveProduct ? 700 : 500, fontSize: '0.72rem', color: isActiveProduct ? color : 'text.secondary', transition: 'color 0.15s', whiteSpace: 'nowrap' }}>
                          {PRODUCT_LABELS[value]}
                        </Typography>
                        <Typography variant="caption" sx={{ display: 'block', lineHeight: 1.1, fontSize: '0.59rem', color: isActiveProduct ? `${color}99` : 'text.disabled', whiteSpace: 'nowrap', overflow: 'hidden', textOverflow: 'ellipsis' }}>
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

        {/* ── Risk group ── */}
        <NavGroup
          label="Risk"
          icon={<WarningAmberOutlined sx={{ fontSize: 16 }} />}
          items={NAV_RISK}
          open={riskOpen}
          onToggle={() => setRiskOpen(o => !o)}
          {...groupProps}
        />

        {/* ── Tools group ── */}
        <NavGroup
          label="Tools"
          icon={<TuneOutlined sx={{ fontSize: 16 }} />}
          items={NAV_TOOLS}
          open={toolsOpen}
          onToggle={() => setToolsOpen(o => !o)}
          {...groupProps}
        />

        {/* ── Frameworks group ── */}
        <NavGroup
          label="Frameworks"
          icon={<GridViewOutlined sx={{ fontSize: 16 }} />}
          regions={NAV_FRAMEWORK_REGIONS}
          open={frameworksOpen}
          onToggle={() => setFrameworksOpen(o => !o)}
          {...groupProps}
        />

        {/* ── Suppliers group ── */}
        <NavGroup
          label="Suppliers"
          icon={<HandshakeOutlined sx={{ fontSize: 16 }} />}
          items={NAV_SUPPLIERS}
          open={suppliersOpen}
          onToggle={() => setSuppliersOpen(o => !o)}
          hasBadge={hasConnectorAlert}
          {...groupProps}
        />

        {/* ── Intelligence group ── */}
        <NavGroup
          label="Intelligence"
          icon={<StreamOutlined sx={{ fontSize: 16 }} />}
          items={NAV_INTELLIGENCE}
          open={intelOpen}
          onToggle={() => setIntelOpen(o => !o)}
          hasBadge={hasIntelAlert}
          {...groupProps}
          color={INTEL_COLOR}
        />

        <Divider sx={{ my: 0.5, mx: 1 }} />

        {/* ── Admin group ── */}
        <NavGroup
          label="Admin"
          icon={<SettingsOutlined sx={{ fontSize: 16 }} />}
          items={NAV_ADMIN}
          open={adminOpen}
          onToggle={() => setAdminOpen(o => !o)}
          {...groupProps}
          color="#6B7A99"
        />

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
        <Tooltip title={collapsed ? 'Security' : ''} placement="right">
          <ListItemButton
            onClick={() => navigate('/system')}
            sx={{ borderRadius: 1.5, px: collapsed ? 0 : 1.5, py: 0.5, justifyContent: collapsed ? 'center' : 'flex-start' }}
          >
            <ListItemIcon sx={{ minWidth: collapsed ? 'unset' : 36, color: 'text.secondary' }}>
              <SecurityOutlined fontSize="small" />
            </ListItemIcon>
            {!collapsed && (
              <ListItemText primary="Security" primaryTypographyProps={{ variant: 'body2', color: 'text.secondary' }} />
            )}
          </ListItemButton>
        </Tooltip>
        <Tooltip title={collapsed ? 'User Guide' : ''} placement="right">
          <ListItemButton
            onClick={() => navigate('/help')}
            sx={{ borderRadius: 1.5, px: collapsed ? 0 : 1.5, py: 0.5, justifyContent: collapsed ? 'center' : 'flex-start' }}
          >
            <ListItemIcon sx={{ minWidth: collapsed ? 'unset' : 36, color: 'text.secondary' }}>
              <HelpOutlineOutlined fontSize="small" />
            </ListItemIcon>
            {!collapsed && (
              <ListItemText primary="User Guide" primaryTypographyProps={{ variant: 'body2', color: 'text.secondary' }} />
            )}
          </ListItemButton>
        </Tooltip>
        <Tooltip title={collapsed ? (mode === 'dark' ? 'Light mode' : 'Dark mode') : ''} placement="right">
          <ListItemButton
            onClick={toggleTheme}
            sx={{ borderRadius: 1.5, px: collapsed ? 0 : 1.5, py: 0.5, justifyContent: collapsed ? 'center' : 'flex-start' }}
          >
            <ListItemIcon sx={{ minWidth: collapsed ? 'unset' : 36, color: 'text.secondary' }}>
              {mode === 'dark' ? <LightModeOutlined fontSize="small" /> : <DarkModeOutlined fontSize="small" />}
            </ListItemIcon>
            {!collapsed && (
              <ListItemText
                primary={mode === 'dark' ? 'Light mode' : 'Dark mode'}
                primaryTypographyProps={{ variant: 'body2', color: 'text.secondary' }}
              />
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
