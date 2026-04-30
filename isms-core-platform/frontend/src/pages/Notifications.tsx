import { useState } from 'react'
import {
  Box,
  Tabs,
  Tab,
  Typography,
  Chip,
  Switch,
  FormControlLabel,
  CircularProgress,
  Alert,
  IconButton,
  Tooltip,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper,
  Select,
  MenuItem,
  OutlinedInput,
  Checkbox,
  ListItemText as MuiListItemText,
} from '@mui/material'
import { SendOutlined, CheckCircleOutlined, RemoveCircleOutlineOutlined } from '@mui/icons-material'
import { useTheme } from '@mui/material/styles'
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { adminApi } from '../api/admin'
import type { NotificationPref, NotificationRoutingRule, UserNotificationPrefs } from '../api/types'
import PageHeader from '../components/PageHeader'
import { useAuth } from '../store/AuthContext'

const CAT_LABEL: Record<string, string> = {
  workflow: 'Workflow',
  system: 'System',
  infrastructure: 'Infrastructure',
}
const CAT_COLOR_DARK: Record<string, string>  = { workflow: '#1a3a27', system: '#1a2a3a', infrastructure: '#2a1a3a' }
const CAT_TEXT_DARK: Record<string, string>   = { workflow: '#C6EFCE', system: '#9fc8f0', infrastructure: '#d4b8f0' }
const CAT_COLOR_LIGHT: Record<string, string> = { workflow: 'rgba(27,94,32,0.1)', system: 'rgba(21,101,192,0.1)', infrastructure: 'rgba(106,27,154,0.1)' }
const CAT_TEXT_LIGHT: Record<string, string>  = { workflow: '#1b5e20', system: '#1565c0', infrastructure: '#6a1b9a' }

const ALL_ROLES = ['super_admin', 'admin', 'isms_manager', 'auditor', 'control_owner', 'viewer']
const ROLE_LABEL: Record<string, string> = {
  super_admin: 'Super Admin', admin: 'Admin', isms_manager: 'ISMS Manager',
  auditor: 'Auditor', control_owner: 'Control Owner', viewer: 'Viewer',
}

// ── Tab 1: My Preferences ────────────────────────────────────────────────────

function MyPrefsTab() {
  const { palette } = useTheme()
  const isLight = palette.mode === 'light'
  const CAT_COLOR = isLight ? CAT_COLOR_LIGHT : CAT_COLOR_DARK
  const CAT_TEXT  = isLight ? CAT_TEXT_LIGHT  : CAT_TEXT_DARK
  const queryClient = useQueryClient()

  const { data, isLoading } = useQuery({
    queryKey: ['my', 'notification-prefs'],
    queryFn: adminApi.getMyNotificationPrefs,
  })

  const mutation = useMutation({
    mutationFn: (prefs: Record<string, boolean>) => adminApi.updateMyNotificationPrefs(prefs),
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ['my', 'notification-prefs'] }),
  })

  const [testingEvent, setTestingEvent] = useState<string | null>(null)
  const [testResult, setTestResult] = useState<{ event_type: string; ok: boolean; msg: string } | null>(null)

  const testMutation = useMutation({
    mutationFn: (event_type: string) => adminApi.sendTestNotification(event_type),
    onMutate: (event_type) => { setTestingEvent(event_type); setTestResult(null) },
    onSuccess: (res) => {
      setTestResult({ event_type: res.event_type, ok: true, msg: `Test sent to ${res.recipient}` })
      setTestingEvent(null)
    },
    onError: (_e, event_type) => {
      setTestResult({ event_type, ok: false, msg: 'Send failed — check SMTP config' })
      setTestingEvent(null)
    },
  })

  const byCategory = data
    ? Object.entries(
        data.prefs.reduce<Record<string, NotificationPref[]>>((acc, p) => {
          ;(acc[p.category] ??= []).push(p)
          return acc
        }, {})
      )
    : []

  if (isLoading) return <CircularProgress size={24} sx={{ display: 'block', mx: 'auto', my: 4 }} />

  return (
    <Box sx={{ maxWidth: 520 }}>
      <Typography variant="body2" color="text.secondary" sx={{ mb: 2 }}>
        Choose which email notifications you receive. Changes take effect immediately.
      </Typography>

      {mutation.isError && (
        <Alert severity="error" sx={{ mb: 2 }}>Failed to save — try again.</Alert>
      )}
      {testResult && (
        <Alert
          severity={testResult.ok ? 'success' : 'error'}
          onClose={() => setTestResult(null)}
          sx={{ mb: 2, fontSize: '0.82rem' }}
        >
          {testResult.msg}
        </Alert>
      )}

      {byCategory.map(([cat, prefs]) => (
        <Box key={cat} sx={{ mb: 3 }}>
          <Chip
            label={CAT_LABEL[cat] ?? cat}
            size="small"
            sx={{ mb: 1.5, fontSize: '0.68rem', height: 20, bgcolor: CAT_COLOR[cat] ?? '#222', color: CAT_TEXT[cat] ?? '#fff' }}
          />
          {prefs.map((pref) => (
            <Box key={pref.event_type} sx={{ display: 'flex', alignItems: 'flex-start', mb: 1.5 }}>
              <FormControlLabel
                control={
                  <Switch
                    size="small"
                    checked={pref.enabled}
                    onChange={() => mutation.mutate({ [pref.event_type]: !pref.enabled })}
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
                sx={{ flex: 1, alignItems: 'flex-start', ml: 0, mr: 0 }}
              />
              <Tooltip title="Send test email to yourself">
                <span>
                  <IconButton
                    size="small"
                    onClick={() => testMutation.mutate(pref.event_type)}
                    disabled={testingEvent !== null}
                    sx={{ mt: 0.25, color: 'text.disabled', '&:hover': { color: 'primary.main' } }}
                  >
                    {testingEvent === pref.event_type
                      ? <CircularProgress size={14} />
                      : <SendOutlined sx={{ fontSize: 14 }} />}
                  </IconButton>
                </span>
              </Tooltip>
            </Box>
          ))}
        </Box>
      ))}
    </Box>
  )
}

// ── Tab 2: Routing Rules (admin only) ─────────────────────────────────────────

function RoutingTab() {
  const queryClient = useQueryClient()

  const { data: rows, isLoading } = useQuery({
    queryKey: ['admin', 'notification-routing'],
    queryFn: adminApi.getNotificationRouting,
  })

  const mutation = useMutation({
    mutationFn: ({ event_type, body }: { event_type: string; body: Partial<NotificationRoutingRule> }) =>
      adminApi.updateNotificationRouting(event_type, body),
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ['admin', 'notification-routing'] }),
  })

  if (isLoading) return <CircularProgress size={24} sx={{ display: 'block', mx: 'auto', my: 4 }} />

  return (
    <Box>
      <Typography variant="body2" color="text.secondary" sx={{ mb: 2 }}>
        Control which roles receive each notification type. Changes take effect on the next event.
      </Typography>

      {mutation.isError && (
        <Alert severity="error" sx={{ mb: 2 }}>Failed to save — try again.</Alert>
      )}

      <TableContainer component={Paper} variant="outlined">
        <Table size="small">
          <TableHead>
            <TableRow>
              <TableCell sx={{ fontWeight: 600 }}>Event</TableCell>
              <TableCell sx={{ fontWeight: 600 }}>Category</TableCell>
              <TableCell sx={{ fontWeight: 600 }}>Target Roles</TableCell>
              <TableCell sx={{ fontWeight: 600, whiteSpace: 'nowrap' }}>Always include override</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {(rows ?? []).map((row) => (
              <TableRow key={row.event_type} hover>
                <TableCell>
                  <Typography variant="body2" fontWeight={500}>{row.label}</Typography>
                  <Typography variant="caption" color="text.secondary">{row.description}</Typography>
                </TableCell>
                <TableCell>
                  <Chip label={CAT_LABEL[row.category] ?? row.category} size="small" sx={{ fontSize: '0.65rem', height: 18 }} />
                </TableCell>
                <TableCell sx={{ minWidth: 260 }}>
                  <Select
                    multiple
                    size="small"
                    value={row.target_roles}
                    onChange={(e) => mutation.mutate({
                      event_type: row.event_type,
                      body: { target_roles: e.target.value as string[] },
                    })}
                    input={<OutlinedInput size="small" />}
                    renderValue={(selected) => (selected as string[]).map(r => ROLE_LABEL[r] ?? r).join(', ')}
                    sx={{ fontSize: '0.82rem', minWidth: 220 }}
                  >
                    {ALL_ROLES.map((r) => (
                      <MenuItem key={r} value={r} dense>
                        <Checkbox size="small" checked={row.target_roles.includes(r)} sx={{ py: 0 }} />
                        <MuiListItemText primary={ROLE_LABEL[r] ?? r} primaryTypographyProps={{ variant: 'body2' }} />
                      </MenuItem>
                    ))}
                  </Select>
                </TableCell>
                <TableCell align="center">
                  <Switch
                    size="small"
                    checked={row.always_include_override}
                    onChange={(e) => mutation.mutate({
                      event_type: row.event_type,
                      body: { always_include_override: e.target.checked },
                    })}
                  />
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </Box>
  )
}

// ── Tab 3: User Overview (admin only) ─────────────────────────────────────────

function UserOverviewTab() {
  const queryClient = useQueryClient()

  const { data: rows, isLoading } = useQuery({
    queryKey: ['admin', 'notification-users'],
    queryFn: adminApi.getAllUserNotificationPrefs,
  })

  const { data: routing } = useQuery({
    queryKey: ['admin', 'notification-routing'],
    queryFn: adminApi.getNotificationRouting,
  })
  const labelFor = (et: string) =>
    routing?.find(r => r.event_type === et)?.label ?? et.replace('email.', '')

  const mutation = useMutation({
    mutationFn: ({ user_id, prefs }: { user_id: string; prefs: Record<string, boolean> }) =>
      adminApi.updateUserNotificationPrefs(user_id, prefs),
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ['admin', 'notification-users'] }),
  })

  if (isLoading) return <CircularProgress size={24} sx={{ display: 'block', mx: 'auto', my: 4 }} />
  if (!rows || rows.length === 0) return <Typography color="text.secondary">No active users.</Typography>

  const eventTypes = Object.keys(rows[0].prefs)

  function toggle(row: UserNotificationPrefs, event_type: string) {
    mutation.mutate({ user_id: row.user_id, prefs: { [event_type]: !row.prefs[event_type] } })
  }

  return (
    <Box>
      <Typography variant="body2" color="text.secondary" sx={{ mb: 2 }}>
        Override any user's notification preferences. Click a cell to toggle.
      </Typography>

      {mutation.isError && (
        <Alert severity="error" sx={{ mb: 2 }}>Failed to save — try again.</Alert>
      )}

      <TableContainer component={Paper} variant="outlined" sx={{ overflowX: 'auto' }}>
        <Table size="small">
          <TableHead>
            <TableRow>
              <TableCell sx={{ fontWeight: 600 }}>User</TableCell>
              <TableCell sx={{ fontWeight: 600 }}>Role</TableCell>
              {eventTypes.map((et) => (
                <TableCell key={et} align="center" sx={{ fontWeight: 600, fontSize: '0.72rem', whiteSpace: 'nowrap' }}>
                  {labelFor(et)}
                </TableCell>
              ))}
            </TableRow>
          </TableHead>
          <TableBody>
            {rows.map((row) => (
              <TableRow key={row.user_id} hover>
                <TableCell>
                  <Typography variant="body2">{row.email}</Typography>
                  {row.full_name && (
                    <Typography variant="caption" color="text.secondary">{row.full_name}</Typography>
                  )}
                </TableCell>
                <TableCell>
                  <Typography variant="caption" color="text.secondary">
                    {ROLE_LABEL[row.role] ?? row.role}
                  </Typography>
                </TableCell>
                {eventTypes.map((et) => (
                  <TableCell key={et} align="center" sx={{ cursor: 'pointer' }} onClick={() => toggle(row, et)}>
                    <Tooltip title={row.prefs[et] ? 'Enabled — click to disable' : 'Disabled — click to enable'}>
                      {row.prefs[et]
                        ? <CheckCircleOutlined sx={{ fontSize: 16, color: 'success.main' }} />
                        : <RemoveCircleOutlineOutlined sx={{ fontSize: 16, color: 'text.disabled' }} />}
                    </Tooltip>
                  </TableCell>
                ))}
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </Box>
  )
}

// ── Page ──────────────────────────────────────────────────────────────────────

export default function Notifications() {
  const [tab, setTab] = useState(0)
  const { user, isSuperAdmin } = useAuth()
  const isAdmin = isSuperAdmin || user?.role === 'admin'

  return (
    <Box sx={{ p: { xs: 2, md: 3 } }}>
      <PageHeader
        title="Notifications"
        subtitle="Manage email notification preferences and routing rules"
      />

      <Box sx={{ borderBottom: 1, borderColor: 'divider', mb: 3 }}>
        <Tabs value={tab} onChange={(_, v) => setTab(v)} textColor="primary" indicatorColor="primary">
          <Tab label="My Preferences" sx={{ minHeight: 44 }} />
          {isAdmin && <Tab label="Routing Rules" sx={{ minHeight: 44 }} />}
          {isAdmin && <Tab label="User Overview" sx={{ minHeight: 44 }} />}
        </Tabs>
      </Box>

      {tab === 0 && <MyPrefsTab />}
      {tab === 1 && isAdmin && <RoutingTab />}
      {tab === 2 && isAdmin && <UserOverviewTab />}
    </Box>
  )
}
