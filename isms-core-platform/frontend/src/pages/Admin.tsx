import { useState } from 'react'
import {
  Box,
  Card,
  CardContent,
  Typography,
  Button,
  Alert,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Chip,
  Grid,
  TextField,
  Select,
  MenuItem,
  FormControl,
  InputLabel,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  IconButton,
  Tooltip,
  Switch,
  FormControlLabel,
  Tabs,
  Tab,
  Pagination,
  Divider,
} from '@mui/material'
import {
  PeopleOutlined,
  PersonAddOutlined,
  EditOutlined,
  DeleteOutlined,
  HistoryOutlined,
  FilterListOutlined,
  FileDownloadOutlined,
} from '@mui/icons-material'
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import dayjs from 'dayjs'
import { adminApi } from '../api/admin'
import type { UserCreate, UserPatch, UserRead } from '../api/types'
import type { AuditLogParams } from '../api/admin'
import PageHeader from '../components/PageHeader'

const ROLES = ['admin', 'isms_manager', 'auditor', 'control_owner', 'viewer']

const ROLE_COLOR: Record<string, { bg: string; fg: string }> = {
  admin: { bg: 'rgba(192,0,0,0.18)', fg: '#FFC7CE' },
  isms_manager: { bg: 'rgba(68,114,196,0.2)', fg: '#9DC3E6' },
  auditor: { bg: 'rgba(112,173,71,0.15)', fg: '#C6EFCE' },
  control_owner: { bg: 'rgba(255,192,0,0.15)', fg: '#FFEB9C' },
  viewer: { bg: 'rgba(255,255,255,0.07)', fg: '#d9d9d9' },
}

const SEV_COLOR: Record<string, { bg: string; fg: string }> = {
  info:     { bg: 'rgba(68,114,196,0.2)',   fg: '#9DC3E6' },
  warning:  { bg: 'rgba(255,192,0,0.15)',   fg: '#FFEB9C' },
  error:    { bg: 'rgba(255,100,0,0.18)',   fg: '#FFB347' },
  critical: { bg: 'rgba(192,0,0,0.18)',     fg: '#FFC7CE' },
}

const CAT_COLOR: Record<string, { bg: string; fg: string }> = {
  security: { bg: 'rgba(192,0,0,0.12)', fg: '#FFC7CE' },
  workflow: { bg: 'rgba(68,114,196,0.12)', fg: '#9DC3E6' },
  system:   { bg: 'rgba(255,255,255,0.07)', fg: '#d9d9d9' },
}

// ---------------------------------------------------------------------------
// User dialogs (unchanged)
// ---------------------------------------------------------------------------

function CreateUserDialog({ open, onClose }: { open: boolean; onClose: () => void }) {
  const queryClient = useQueryClient()
  const [form, setForm] = useState<UserCreate>({
    email: '',
    username: '',
    full_name: '',
    password: '',
    role: 'viewer',
  })
  const [error, setError] = useState<string | null>(null)

  const mutation = useMutation({
    mutationFn: () => adminApi.createUser(form),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['admin', 'users'] })
      onClose()
      setForm({ email: '', username: '', full_name: '', password: '', role: 'viewer' })
      setError(null)
    },
    onError: (err: unknown) => {
      const msg =
        (err as { response?: { data?: { detail?: string } } })?.response?.data?.detail ??
        'Create failed'
      setError(String(msg))
    },
  })

  const set = (k: keyof UserCreate, v: string) => setForm((f) => ({ ...f, [k]: v }))

  return (
    <Dialog open={open} onClose={onClose} maxWidth="xs" fullWidth>
      <DialogTitle>Add User</DialogTitle>
      <DialogContent sx={{ pt: 1 }}>
        {error && <Alert severity="error" sx={{ mb: 2 }}>{error}</Alert>}
        <TextField
          fullWidth label="Email" value={form.email}
          onChange={(e) => set('email', e.target.value)}
          size="small" sx={{ mb: 2 }} required
        />
        <TextField
          fullWidth label="Username" value={form.username}
          onChange={(e) => set('username', e.target.value)}
          size="small" sx={{ mb: 2 }} required
        />
        <TextField
          fullWidth label="Full Name" value={form.full_name ?? ''}
          onChange={(e) => set('full_name', e.target.value)}
          size="small" sx={{ mb: 2 }}
        />
        <TextField
          fullWidth label="Password" type="password" value={form.password}
          onChange={(e) => set('password', e.target.value)}
          size="small" sx={{ mb: 2 }} required
        />
        <FormControl fullWidth size="small">
          <InputLabel>Role</InputLabel>
          <Select value={form.role} onChange={(e) => set('role', e.target.value)} label="Role">
            {ROLES.map((r) => <MenuItem key={r} value={r}>{r}</MenuItem>)}
          </Select>
        </FormControl>
      </DialogContent>
      <DialogActions sx={{ px: 3, pb: 2 }}>
        <Button onClick={onClose}>Cancel</Button>
        <Button
          variant="contained"
          onClick={() => mutation.mutate()}
          disabled={!form.email || !form.username || !form.password || mutation.isPending}
        >
          {mutation.isPending ? 'Creating...' : 'Create User'}
        </Button>
      </DialogActions>
    </Dialog>
  )
}

const NOTIF_EVENTS = [
  { event_type: 'email.gap_assigned',    label: 'Gap assigned',        category: 'Workflow' },
  { event_type: 'email.evidence_expiry', label: 'Evidence expiry',     category: 'Workflow' },
  { event_type: 'email.qa_fail',         label: 'QA check failures',   category: 'System'   },
  { event_type: 'email.import_completed',label: 'Import completed',    category: 'System'   },
]

function EditUserDialog({
  user,
  open,
  onClose,
}: {
  user: UserRead
  open: boolean
  onClose: () => void
}) {
  const queryClient = useQueryClient()
  const [form, setForm] = useState<UserPatch & { password: string }>({
    full_name: user.full_name ?? '',
    role: user.role,
    is_active: user.is_active,
    password: '',
    notification_prefs: { ...user.notification_prefs },
  })
  const [error, setError] = useState<string | null>(null)

  const mutation = useMutation({
    mutationFn: () => {
      const patch: UserPatch = {
        full_name: form.full_name || null,
        role: form.role,
        is_active: form.is_active,
        notification_prefs: form.notification_prefs,
      }
      if (form.password) patch.password = form.password
      return adminApi.updateUser(user.id, patch)
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['admin', 'users'] })
      onClose()
      setError(null)
    },
    onError: (err: unknown) => {
      const msg =
        (err as { response?: { data?: { detail?: string } } })?.response?.data?.detail ??
        'Update failed'
      setError(String(msg))
    },
  })

  function toggleNotif(event_type: string) {
    setForm((f) => ({
      ...f,
      notification_prefs: {
        ...f.notification_prefs,
        [event_type]: !(f.notification_prefs?.[event_type] ?? true),
      },
    }))
  }

  return (
    <Dialog open={open} onClose={onClose} maxWidth="xs" fullWidth>
      <DialogTitle sx={{ pb: 0.5 }}>
        Edit User
        <Typography variant="caption" color="text.secondary" display="block">
          {user.email}
        </Typography>
      </DialogTitle>
      <DialogContent sx={{ pt: 1 }}>
        {error && <Alert severity="error" sx={{ mb: 2 }}>{error}</Alert>}
        <TextField
          fullWidth label="Full Name"
          value={form.full_name ?? ''}
          onChange={(e) => setForm((f) => ({ ...f, full_name: e.target.value }))}
          size="small" sx={{ mb: 2 }}
        />
        <FormControl fullWidth size="small" sx={{ mb: 2 }}>
          <InputLabel>Role</InputLabel>
          <Select
            value={form.role ?? 'viewer'}
            onChange={(e) => setForm((f) => ({ ...f, role: e.target.value }))}
            label="Role"
          >
            {ROLES.map((r) => <MenuItem key={r} value={r}>{r}</MenuItem>)}
          </Select>
        </FormControl>
        <FormControlLabel
          control={
            <Switch
              checked={form.is_active ?? true}
              onChange={(e) => setForm((f) => ({ ...f, is_active: e.target.checked }))}
              size="small"
            />
          }
          label={<Typography variant="body2">Active</Typography>}
          sx={{ mb: 2, display: 'flex' }}
        />
        <TextField
          fullWidth label="New Password"
          helperText="Leave blank to keep current password"
          type="password"
          value={form.password ?? ''}
          onChange={(e) => setForm((f) => ({ ...f, password: e.target.value }))}
          size="small" sx={{ mb: 2 }}
        />
        <Divider sx={{ mb: 1.5 }} />
        <Typography variant="caption" color="text.secondary" display="block" sx={{ mb: 1, fontWeight: 600 }}>
          Email Notifications
        </Typography>
        {NOTIF_EVENTS.map((ev) => (
          <FormControlLabel
            key={ev.event_type}
            control={
              <Switch
                size="small"
                checked={form.notification_prefs?.[ev.event_type] ?? true}
                onChange={() => toggleNotif(ev.event_type)}
              />
            }
            label={
              <Typography variant="body2">
                {ev.label}
                <Typography component="span" variant="caption" color="text.secondary" sx={{ ml: 0.75 }}>
                  {ev.category}
                </Typography>
              </Typography>
            }
            sx={{ display: 'flex', mb: 0.5, ml: 0 }}
          />
        ))}
      </DialogContent>
      <DialogActions sx={{ px: 3, pb: 2 }}>
        <Button onClick={onClose}>Cancel</Button>
        <Button variant="contained" onClick={() => mutation.mutate()} disabled={mutation.isPending}>
          {mutation.isPending ? 'Saving...' : 'Save'}
        </Button>
      </DialogActions>
    </Dialog>
  )
}

// ---------------------------------------------------------------------------
// Users tab
// ---------------------------------------------------------------------------

function UsersTab() {
  const queryClient = useQueryClient()
  const [createOpen, setCreateOpen] = useState(false)
  const [editUser, setEditUser] = useState<UserRead | null>(null)

  const { data: users, isLoading } = useQuery({
    queryKey: ['admin', 'users'],
    queryFn: adminApi.listUsers,
  })

  const deleteMutation = useMutation({
    mutationFn: adminApi.deleteUser,
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ['admin', 'users'] }),
  })

  function handleDelete(user: UserRead) {
    if (!window.confirm(`Delete user ${user.email}? This cannot be undone.`)) return
    deleteMutation.mutate(user.id)
  }

  return (
    <>
      <CreateUserDialog open={createOpen} onClose={() => setCreateOpen(false)} />
      {editUser && (
        <EditUserDialog user={editUser} open={true} onClose={() => setEditUser(null)} />
      )}
      <Grid container spacing={2}>
        <Grid item xs={12}>
          <Card>
            <CardContent sx={{ pb: '12px !important' }}>
              <Box sx={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', mb: 2 }}>
                <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                  <PeopleOutlined sx={{ color: 'primary.main' }} />
                  <Typography variant="h6">Users</Typography>
                  {users && (
                    <Chip label={users.length} size="small" sx={{ height: 18, fontSize: '0.65rem' }} />
                  )}
                </Box>
                <Button
                  variant="outlined" size="small"
                  startIcon={<PersonAddOutlined />}
                  onClick={() => setCreateOpen(true)}
                >
                  Add User
                </Button>
              </Box>

              <TableContainer>
                <Table size="small">
                  <TableHead>
                    <TableRow>
                      <TableCell>Email</TableCell>
                      <TableCell>Username</TableCell>
                      <TableCell>Name</TableCell>
                      <TableCell>Role</TableCell>
                      <TableCell>Status</TableCell>
                      <TableCell>Last Login</TableCell>
                      <TableCell>Created</TableCell>
                      <TableCell align="center">Actions</TableCell>
                    </TableRow>
                  </TableHead>
                  <TableBody>
                    {isLoading && [...Array(3)].map((_, i) => (
                      <TableRow key={i}>
                        {[...Array(8)].map((_, j) => (
                          <TableCell key={j}>
                            <Box sx={{ height: 16, bgcolor: 'rgba(255,255,255,0.05)', borderRadius: 1 }} />
                          </TableCell>
                        ))}
                      </TableRow>
                    ))}
                    {users?.map((user) => {
                      const rc = ROLE_COLOR[user.role] ?? ROLE_COLOR.viewer
                      return (
                        <TableRow key={user.id} hover>
                          <TableCell>
                            <Typography variant="body2" fontFamily="monospace">{user.email}</Typography>
                          </TableCell>
                          <TableCell>
                            <Typography variant="body2" color="text.secondary">{user.username}</Typography>
                          </TableCell>
                          <TableCell>
                            <Typography variant="body2">{user.full_name ?? '—'}</Typography>
                          </TableCell>
                          <TableCell>
                            <Chip label={user.role} size="small" sx={{ fontSize: '0.65rem', height: 18, bgcolor: rc.bg, color: rc.fg }} />
                          </TableCell>
                          <TableCell>
                            <Chip
                              label={user.is_active ? 'Active' : 'Inactive'}
                              size="small"
                              sx={{ fontSize: '0.65rem', height: 18, bgcolor: user.is_active ? '#1a3a27' : '#3a0000', color: user.is_active ? '#C6EFCE' : '#FFC7CE' }}
                            />
                          </TableCell>
                          <TableCell>
                            <Typography variant="caption" color="text.secondary">
                              {user.last_login ? dayjs(user.last_login).format('DD MMM YYYY HH:mm') : '—'}
                            </Typography>
                          </TableCell>
                          <TableCell>
                            <Typography variant="caption" color="text.secondary">
                              {dayjs(user.created_at).format('DD MMM YYYY')}
                            </Typography>
                          </TableCell>
                          <TableCell align="center">
                            <Tooltip title="Edit">
                              <IconButton size="small" onClick={() => setEditUser(user)}>
                                <EditOutlined fontSize="small" />
                              </IconButton>
                            </Tooltip>
                            <Tooltip title="Delete">
                              <IconButton
                                size="small"
                                onClick={() => handleDelete(user)}
                                sx={{ color: 'error.main' }}
                                disabled={deleteMutation.isPending}
                              >
                                <DeleteOutlined fontSize="small" />
                              </IconButton>
                            </Tooltip>
                          </TableCell>
                        </TableRow>
                      )
                    })}
                  </TableBody>
                </Table>
              </TableContainer>
            </CardContent>
          </Card>
        </Grid>
      </Grid>
    </>
  )
}

// ---------------------------------------------------------------------------
// Audit Log tab
// ---------------------------------------------------------------------------

function AuditLogTab() {
  const [page, setPage] = useState(1)
  const [filters, setFilters] = useState<AuditLogParams>({ page_size: 50 })
  const [draft, setDraft] = useState<AuditLogParams>({})

  const { data, isLoading } = useQuery({
    queryKey: ['admin', 'audit-log', page, filters],
    queryFn: () => adminApi.getAuditLog({ ...filters, page }),
    placeholderData: (prev) => prev,
  })

  function applyFilters() {
    setPage(1)
    setFilters({ page_size: 50, ...draft })
  }

  function clearFilters() {
    setDraft({})
    setPage(1)
    setFilters({ page_size: 50 })
  }

  return (
    <Card>
      <CardContent sx={{ pb: '12px !important' }}>
        {/* Header */}
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 2 }}>
          <HistoryOutlined sx={{ color: 'primary.main' }} />
          <Typography variant="h6">Audit Log</Typography>
          {data && (
            <Chip label={`${data.total} entries`} size="small" sx={{ height: 18, fontSize: '0.65rem' }} />
          )}
          <Box sx={{ ml: 'auto' }}>
            <Button
              size="small"
              variant="outlined"
              startIcon={<FileDownloadOutlined />}
              onClick={async () => {
                const all = await adminApi.getAuditLog({ ...filters, page: 1, page_size: 10000 })
                const header = 'timestamp,event_type,category,severity,actor_email,description,target_type,ip_address'
                const rows = all.items.map((e) =>
                  [e.created_at, e.event_type, e.category, e.severity,
                   e.actor_email ?? '', (e.description ?? '').replace(/"/g, '""'),
                   e.target_type ?? '', e.ip_address ?? '']
                    .map((v) => `"${v}"`).join(',')
                )
                const csv = [header, ...rows].join('\n')
                const a = document.createElement('a')
                a.href = URL.createObjectURL(new Blob([csv], { type: 'text/csv' }))
                a.download = `isms-audit-log-${new Date().toISOString().slice(0, 10)}.csv`
                a.click()
              }}
              sx={{ fontSize: '0.7rem' }}
            >
              Export CSV
            </Button>
          </Box>
        </Box>

        {/* Filters */}
        <Box sx={{ display: 'flex', gap: 1.5, flexWrap: 'wrap', mb: 2, alignItems: 'flex-end' }}>
          <FormControl size="small" sx={{ minWidth: 120 }}>
            <InputLabel>Category</InputLabel>
            <Select
              value={draft.category ?? ''}
              onChange={(e) => setDraft((d) => ({ ...d, category: e.target.value || undefined }))}
              label="Category"
            >
              <MenuItem value="">All</MenuItem>
              <MenuItem value="security">Security</MenuItem>
              <MenuItem value="workflow">Workflow</MenuItem>
              <MenuItem value="system">System</MenuItem>
            </Select>
          </FormControl>

          <FormControl size="small" sx={{ minWidth: 110 }}>
            <InputLabel>Severity</InputLabel>
            <Select
              value={draft.severity ?? ''}
              onChange={(e) => setDraft((d) => ({ ...d, severity: e.target.value || undefined }))}
              label="Severity"
            >
              <MenuItem value="">All</MenuItem>
              <MenuItem value="info">Info</MenuItem>
              <MenuItem value="warning">Warning</MenuItem>
              <MenuItem value="error">Error</MenuItem>
              <MenuItem value="critical">Critical</MenuItem>
            </Select>
          </FormControl>

          <TextField
            size="small" label="Event type" placeholder="e.g. login"
            value={draft.event_type ?? ''}
            onChange={(e) => setDraft((d) => ({ ...d, event_type: e.target.value || undefined }))}
            sx={{ width: 160 }}
          />

          <TextField
            size="small" label="Actor email"
            value={draft.actor_email ?? ''}
            onChange={(e) => setDraft((d) => ({ ...d, actor_email: e.target.value || undefined }))}
            sx={{ width: 200 }}
          />

          <TextField
            size="small" label="From" type="date" InputLabelProps={{ shrink: true }}
            value={draft.date_from ?? ''}
            onChange={(e) => setDraft((d) => ({ ...d, date_from: e.target.value || undefined }))}
            sx={{ width: 150 }}
          />

          <TextField
            size="small" label="To" type="date" InputLabelProps={{ shrink: true }}
            value={draft.date_to ?? ''}
            onChange={(e) => setDraft((d) => ({ ...d, date_to: e.target.value || undefined }))}
            sx={{ width: 150 }}
          />

          <Button variant="outlined" size="small" startIcon={<FilterListOutlined />} onClick={applyFilters}>
            Apply
          </Button>
          <Button size="small" onClick={clearFilters}>Clear</Button>
        </Box>

        {/* Table */}
        <TableContainer>
          <Table size="small">
            <TableHead>
              <TableRow>
                <TableCell>Event</TableCell>
                <TableCell>Category</TableCell>
                <TableCell>Severity</TableCell>
                <TableCell>Actor</TableCell>
                <TableCell>Target</TableCell>
                <TableCell>Description</TableCell>
                <TableCell>Time</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {isLoading && [...Array(5)].map((_, i) => (
                <TableRow key={i}>
                  {[...Array(7)].map((_, j) => (
                    <TableCell key={j}>
                      <Box sx={{ height: 14, bgcolor: 'rgba(255,255,255,0.05)', borderRadius: 1 }} />
                    </TableCell>
                  ))}
                </TableRow>
              ))}

              {!isLoading && data?.items.length === 0 && (
                <TableRow>
                  <TableCell colSpan={7} align="center" sx={{ py: 4 }}>
                    <Typography variant="body2" color="text.secondary">No audit log entries found.</Typography>
                  </TableCell>
                </TableRow>
              )}

              {data?.items.map((entry) => {
                const sc = SEV_COLOR[entry.severity] ?? SEV_COLOR.info
                const cc = CAT_COLOR[entry.category] ?? CAT_COLOR.system
                return (
                  <TableRow key={entry.id} hover>
                    <TableCell>
                      <Typography variant="body2" fontFamily="monospace" fontSize="0.75rem">
                        {entry.event_type}
                      </Typography>
                    </TableCell>
                    <TableCell>
                      <Chip label={entry.category} size="small" sx={{ fontSize: '0.65rem', height: 18, bgcolor: cc.bg, color: cc.fg }} />
                    </TableCell>
                    <TableCell>
                      <Chip label={entry.severity} size="small" sx={{ fontSize: '0.65rem', height: 18, bgcolor: sc.bg, color: sc.fg }} />
                    </TableCell>
                    <TableCell>
                      <Typography variant="caption" color="text.secondary">
                        {entry.actor_email ?? (entry.user_id ? entry.user_id.slice(0, 8) + '…' : '—')}
                      </Typography>
                    </TableCell>
                    <TableCell>
                      {entry.target_type ? (
                        <Typography variant="caption" color="text.secondary">
                          {entry.target_type}{entry.target_id ? ` · ${entry.target_id.slice(0, 8)}…` : ''}
                        </Typography>
                      ) : '—'}
                    </TableCell>
                    <TableCell sx={{ maxWidth: 300 }}>
                      <Typography variant="caption" color="text.secondary" sx={{ display: 'block', whiteSpace: 'normal', wordBreak: 'break-word' }}>
                        {entry.description ?? '—'}
                      </Typography>
                    </TableCell>
                    <TableCell>
                      <Tooltip title={dayjs(entry.created_at).format('DD MMM YYYY HH:mm:ss')}>
                        <Typography variant="caption" color="text.secondary" noWrap>
                          {dayjs(entry.created_at).format('DD MMM HH:mm')}
                        </Typography>
                      </Tooltip>
                    </TableCell>
                  </TableRow>
                )
              })}
            </TableBody>
          </Table>
        </TableContainer>

        {/* Pagination */}
        {data && data.pages > 1 && (
          <Box sx={{ display: 'flex', justifyContent: 'center', mt: 2 }}>
            <Pagination
              count={data.pages}
              page={page}
              onChange={(_, p) => setPage(p)}
              size="small"
              color="primary"
            />
          </Box>
        )}
      </CardContent>
    </Card>
  )
}

// ---------------------------------------------------------------------------
// Main page
// ---------------------------------------------------------------------------

export default function Admin() {
  const [tab, setTab] = useState(0)

  return (
    <Box>
      <PageHeader title="Administration" subtitle="User management and audit trail" />

      <Box sx={{ borderBottom: 1, borderColor: 'divider', mb: 3 }}>
        <Tabs value={tab} onChange={(_, v) => setTab(v)} textColor="primary" indicatorColor="primary">
          <Tab label="Users" icon={<PeopleOutlined fontSize="small" />} iconPosition="start" sx={{ minHeight: 48 }} />
          <Tab label="Audit Log" icon={<HistoryOutlined fontSize="small" />} iconPosition="start" sx={{ minHeight: 48 }} />
        </Tabs>
      </Box>

      {tab === 0 && <UsersTab />}
      {tab === 1 && <AuditLogTab />}
    </Box>
  )
}
