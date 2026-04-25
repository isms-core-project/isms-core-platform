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
  Divider,
  LinearProgress,
} from '@mui/material'
import {
  PeopleOutlined,
  PersonAddOutlined,
  EditOutlined,
  DeleteOutlined,
  LockResetOutlined,
  LockOutlined,
  LockOpenOutlined,
  GroupsOutlined,
  GroupAddOutlined,
  PersonRemoveOutlined,
  DevicesOutlined,
  LogoutOutlined,
} from '@mui/icons-material'
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import dayjs from 'dayjs'
import { adminApi } from '../api/admin'
import { orgApi } from '../api/orgApi'
import type { UserCreate, UserPatch, UserRead } from '../api/types'
import type { GroupEntry, GroupMemberEntry } from '../api/admin'
import PageHeader from '../components/PageHeader'
import { useAuth } from '../store/AuthContext'

const ROLES = ['super_admin', 'admin', 'isms_manager', 'auditor', 'control_owner', 'viewer']
const ROLES_NON_SUPER = ['admin', 'isms_manager', 'auditor', 'control_owner', 'viewer']

const ROLE_COLOR: Record<string, { bg: string; fg: string }> = {
  super_admin: { bg: 'rgba(192,0,0,0.35)', fg: '#FF6B6B' },
  admin: { bg: 'rgba(192,0,0,0.18)', fg: '#FFC7CE' },
  isms_manager: { bg: 'rgba(68,114,196,0.2)', fg: '#9DC3E6' },
  auditor: { bg: 'rgba(112,173,71,0.15)', fg: '#C6EFCE' },
  control_owner: { bg: 'rgba(255,192,0,0.15)', fg: '#FFEB9C' },
  viewer: { bg: 'rgba(255,255,255,0.07)', fg: '#d9d9d9' },
}

// ---------------------------------------------------------------------------
// User dialogs
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
      <DialogContent sx={{ pt: '20px !important' }}>
        {error && <Alert severity="error" sx={{ mb: 2 }}>{error}</Alert>}
        <TextField fullWidth label="Email" value={form.email} onChange={(e) => set('email', e.target.value)} size="small" sx={{ mb: 2 }} required />
        <TextField fullWidth label="Username" value={form.username} onChange={(e) => set('username', e.target.value)} size="small" sx={{ mb: 2 }} required />
        <TextField fullWidth label="Full Name" value={form.full_name ?? ''} onChange={(e) => set('full_name', e.target.value)} size="small" sx={{ mb: 2 }} />
        <TextField fullWidth label="Password" type="password" value={form.password} onChange={(e) => set('password', e.target.value)} size="small" sx={{ mb: 2 }} required />
        <FormControl fullWidth size="small">
          <InputLabel>Role</InputLabel>
          <Select value={form.role} onChange={(e) => set('role', e.target.value)} label="Role">
            {ROLES.map((r) => <MenuItem key={r} value={r}>{r}</MenuItem>)}
          </Select>
        </FormControl>
      </DialogContent>
      <DialogActions sx={{ px: 3, pb: 2 }}>
        <Button onClick={onClose}>Cancel</Button>
        <Button variant="contained" onClick={() => mutation.mutate()} disabled={!form.email || !form.username || !form.password || mutation.isPending}>
          {mutation.isPending ? 'Creating...' : 'Create User'}
        </Button>
      </DialogActions>
    </Dialog>
  )
}

const NOTIF_EVENTS = [
  { event_type: 'email.gap_assigned',    label: 'Gap assigned',     category: 'Workflow' },
  { event_type: 'email.evidence_expiry', label: 'Evidence expiry',  category: 'Workflow' },
  { event_type: 'email.qa_fail',         label: 'QA check failures', category: 'System' },
  { event_type: 'email.import_completed',label: 'Import completed', category: 'System' },
]

function EditUserDialog({
  user, open, onClose, isSuperAdmin,
}: { user: UserRead; open: boolean; onClose: () => void; isSuperAdmin: boolean }) {
  const queryClient = useQueryClient()
  const [form, setForm] = useState<UserPatch & { password: string }>({
    full_name: user.full_name ?? '',
    role: user.role,
    is_active: user.is_active,
    password: '',
    notification_prefs: { ...user.notification_prefs },
    organisation_id: user.organisation_id,
  })

  const { data: allOrgs } = useQuery({
    queryKey: ['organisations', true],
    queryFn: orgApi.list,
    enabled: isSuperAdmin,
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
      if (isSuperAdmin && form.organisation_id !== user.organisation_id) patch.organisation_id = form.organisation_id
      return adminApi.updateUser(user.id, patch)
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['admin', 'users'] })
      onClose()
      setError(null)
    },
    onError: (err: unknown) => {
      const msg =
        (err as { response?: { data?: { detail?: string } } })?.response?.data?.detail ?? 'Update failed'
      setError(String(msg))
    },
  })

  function toggleNotif(event_type: string) {
    setForm((f) => ({
      ...f,
      notification_prefs: { ...f.notification_prefs, [event_type]: !(f.notification_prefs?.[event_type] ?? true) },
    }))
  }

  return (
    <Dialog open={open} onClose={onClose} maxWidth="xs" fullWidth>
      <DialogTitle sx={{ pb: 0.5 }}>
        Edit User
        <Typography variant="caption" color="text.secondary" display="block">{user.email}</Typography>
      </DialogTitle>
      <DialogContent sx={{ pt: '20px !important' }}>
        {error && <Alert severity="error" sx={{ mb: 2 }}>{error}</Alert>}
        <TextField fullWidth label="Full Name" value={form.full_name ?? ''} onChange={(e) => setForm((f) => ({ ...f, full_name: e.target.value }))} size="small" sx={{ mb: 2 }} />
        <FormControl fullWidth size="small" sx={{ mb: 2 }}>
          <InputLabel>Role</InputLabel>
          <Select value={form.role ?? 'viewer'} onChange={(e) => setForm((f) => ({ ...f, role: e.target.value }))} label="Role">
            {(isSuperAdmin ? ROLES : ROLES_NON_SUPER).map((r) => <MenuItem key={r} value={r}>{r}</MenuItem>)}
          </Select>
        </FormControl>
        {isSuperAdmin && allOrgs && (
          <FormControl fullWidth size="small" sx={{ mb: 2 }}>
            <InputLabel>Organisation</InputLabel>
            <Select value={form.organisation_id ?? ''} onChange={(e) => setForm((f) => ({ ...f, organisation_id: e.target.value }))} label="Organisation">
              {allOrgs.map((o) => <MenuItem key={o.id} value={o.id}>{o.name}</MenuItem>)}
            </Select>
          </FormControl>
        )}
        <FormControlLabel
          control={<Switch checked={form.is_active ?? true} onChange={(e) => setForm((f) => ({ ...f, is_active: e.target.checked }))} size="small" />}
          label={<Typography variant="body2">Active</Typography>}
          sx={{ mb: 2, display: 'flex' }}
        />
        <TextField fullWidth label="New Password" helperText="Leave blank to keep current password" type="password" value={form.password ?? ''} onChange={(e) => setForm((f) => ({ ...f, password: e.target.value }))} size="small" sx={{ mb: 2 }} />
        <Divider sx={{ mb: 1.5 }} />
        <Typography variant="caption" color="text.secondary" display="block" sx={{ mb: 1, fontWeight: 600 }}>
          Email Notifications
        </Typography>
        {NOTIF_EVENTS.map((ev) => (
          <FormControlLabel
            key={ev.event_type}
            control={<Switch size="small" checked={form.notification_prefs?.[ev.event_type] ?? true} onChange={() => toggleNotif(ev.event_type)} />}
            label={
              <Typography variant="body2">
                {ev.label}
                <Typography component="span" variant="caption" color="text.secondary" sx={{ ml: 0.75 }}>{ev.category}</Typography>
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
  const { isSuperAdmin } = useAuth()
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

  const resetMfaMutation = useMutation({
    mutationFn: adminApi.resetUserMfa,
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ['admin', 'users'] }),
  })

  function handleDelete(user: UserRead) {
    if (!window.confirm(`Delete user ${user.email}? This cannot be undone.`)) return
    deleteMutation.mutate(user.id)
  }

  function handleResetMfa(user: UserRead) {
    if (!window.confirm(`Reset MFA for ${user.email}? They will need to re-enroll.`)) return
    resetMfaMutation.mutate(user.id)
  }

  return (
    <>
      <CreateUserDialog open={createOpen} onClose={() => setCreateOpen(false)} />
      {editUser && (
        <EditUserDialog user={editUser} open={true} onClose={() => setEditUser(null)} isSuperAdmin={isSuperAdmin} />
      )}
      <Grid container spacing={2}>
        <Grid item xs={12}>
          <Card>
            <CardContent sx={{ pb: '12px !important' }}>
              <Box sx={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', mb: 2 }}>
                <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                  <PeopleOutlined sx={{ color: 'primary.main' }} />
                  <Typography variant="h6">Users</Typography>
                  {users && <Chip label={users.length} size="small" sx={{ height: 18, fontSize: '0.65rem' }} />}
                </Box>
                <Button variant="outlined" size="small" startIcon={<PersonAddOutlined />} onClick={() => setCreateOpen(true)}>
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
                      {isSuperAdmin && <TableCell>Organisation</TableCell>}
                      <TableCell>Status</TableCell>
                      <TableCell>MFA</TableCell>
                      <TableCell>Last Login</TableCell>
                      <TableCell>Created</TableCell>
                      <TableCell align="center">Actions</TableCell>
                    </TableRow>
                  </TableHead>
                  <TableBody>
                    {isLoading && [...Array(3)].map((_, i) => (
                      <TableRow key={i}>
                        {[...Array(isSuperAdmin ? 10 : 9)].map((_, j) => (
                          <TableCell key={j}><Box sx={{ height: 16, bgcolor: 'rgba(255,255,255,0.05)', borderRadius: 1 }} /></TableCell>
                        ))}
                      </TableRow>
                    ))}
                    {users?.map((user) => {
                      const rc = ROLE_COLOR[user.role] ?? ROLE_COLOR.viewer
                      return (
                        <TableRow key={user.id} hover>
                          <TableCell><Typography variant="body2" fontFamily="monospace">{user.email}</Typography></TableCell>
                          <TableCell><Typography variant="body2" color="text.secondary">{user.username}</Typography></TableCell>
                          <TableCell><Typography variant="body2">{user.full_name ?? '—'}</Typography></TableCell>
                          <TableCell>
                            <Chip label={user.role} size="small" sx={{ fontSize: '0.65rem', height: 18, bgcolor: rc.bg, color: rc.fg }} />
                          </TableCell>
                          {isSuperAdmin && (
                            <TableCell><Typography variant="caption" color="text.secondary">{user.organisation_name ?? '—'}</Typography></TableCell>
                          )}
                          <TableCell>
                            <Chip
                              label={user.is_active ? 'Active' : 'Inactive'} size="small"
                              sx={{ fontSize: '0.65rem', height: 18, bgcolor: user.is_active ? '#1a3a27' : '#3a0000', color: user.is_active ? '#C6EFCE' : '#FFC7CE' }}
                            />
                          </TableCell>
                          <TableCell>
                            <Tooltip title={user.mfa_enabled ? 'MFA enabled' : 'MFA not set up'}>
                              <Box sx={{ display: 'flex', alignItems: 'center' }}>
                                {user.mfa_enabled
                                  ? <LockOutlined sx={{ fontSize: 16, color: '#C6EFCE' }} />
                                  : <LockOpenOutlined sx={{ fontSize: 16, color: 'text.disabled' }} />}
                              </Box>
                            </Tooltip>
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
                            {user.mfa_enabled && (
                              <Tooltip title="Reset MFA">
                                <IconButton size="small" onClick={() => handleResetMfa(user)} sx={{ color: 'warning.main' }} disabled={resetMfaMutation.isPending}>
                                  <LockResetOutlined fontSize="small" />
                                </IconButton>
                              </Tooltip>
                            )}
                            <Tooltip title="Delete">
                              <IconButton size="small" onClick={() => handleDelete(user)} sx={{ color: 'error.main' }} disabled={deleteMutation.isPending}>
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
// Groups tab (B.3)
// ---------------------------------------------------------------------------

function ManageMembersDialog({
  group, open, onClose, allUsers,
}: { group: GroupEntry; open: boolean; onClose: () => void; allUsers: UserRead[] }) {
  const queryClient = useQueryClient()

  const { data: members, isLoading } = useQuery({
    queryKey: ['admin', 'groups', group.id, 'members'],
    queryFn: () => adminApi.getGroupMembers(group.id),
    enabled: open,
  })

  const memberIds = new Set((members ?? []).map((m) => m.user_id))
  const nonMembers = allUsers.filter((u) => !memberIds.has(u.id))

  const addMutation = useMutation({
    mutationFn: (userId: string) => adminApi.addGroupMember(group.id, userId),
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ['admin', 'groups', group.id, 'members'] }),
  })

  const removeMutation = useMutation({
    mutationFn: (userId: string) => adminApi.removeGroupMember(group.id, userId),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['admin', 'groups', group.id, 'members'] })
      queryClient.invalidateQueries({ queryKey: ['admin', 'groups'] })
    },
  })

  const [addUserId, setAddUserId] = useState('')

  return (
    <Dialog open={open} onClose={onClose} maxWidth="sm" fullWidth>
      <DialogTitle sx={{ pb: 0.5 }}>
        Manage Members
        <Typography variant="caption" color="text.secondary" display="block">{group.name}</Typography>
      </DialogTitle>
      <DialogContent>
        {isLoading && <LinearProgress sx={{ mb: 1 }} />}

        {/* Add member */}
        <Box sx={{ display: 'flex', gap: 1, mb: 2, mt: 1 }}>
          <FormControl size="small" sx={{ flex: 1 }}>
            <InputLabel>Add user</InputLabel>
            <Select value={addUserId} onChange={(e) => setAddUserId(e.target.value)} label="Add user">
              <MenuItem value="">Select user…</MenuItem>
              {nonMembers.map((u) => (
                <MenuItem key={u.id} value={u.id}>{u.email} · {u.role}</MenuItem>
              ))}
            </Select>
          </FormControl>
          <Button
            variant="contained" size="small" startIcon={<GroupAddOutlined />}
            disabled={!addUserId || addMutation.isPending}
            onClick={() => { addMutation.mutate(addUserId); setAddUserId('') }}
          >
            Add
          </Button>
        </Box>

        {/* Member list */}
        <Typography variant="caption" color="text.secondary" sx={{ fontWeight: 600, display: 'block', mb: 0.5 }}>
          Current members ({members?.length ?? 0})
        </Typography>
        {members?.length === 0 && (
          <Typography variant="body2" color="text.disabled" sx={{ mb: 1 }}>No members yet.</Typography>
        )}
        {members?.map((m: GroupMemberEntry) => {
          const rc = ROLE_COLOR[m.role] ?? ROLE_COLOR.viewer
          return (
            <Box key={m.user_id} sx={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', py: 0.5, borderBottom: '1px solid rgba(255,255,255,0.06)' }}>
              <Box>
                <Typography variant="body2" fontFamily="monospace">{m.email}</Typography>
                {m.full_name && <Typography variant="caption" color="text.secondary">{m.full_name}</Typography>}
              </Box>
              <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                <Chip label={m.role} size="small" sx={{ fontSize: '0.6rem', height: 16, bgcolor: rc.bg, color: rc.fg }} />
                <Tooltip title="Remove from group">
                  <IconButton size="small" sx={{ color: 'error.main' }} onClick={() => removeMutation.mutate(m.user_id)} disabled={removeMutation.isPending}>
                    <PersonRemoveOutlined fontSize="small" />
                  </IconButton>
                </Tooltip>
              </Box>
            </Box>
          )
        })}
      </DialogContent>
      <DialogActions sx={{ px: 3, pb: 2 }}>
        <Button onClick={onClose}>Close</Button>
      </DialogActions>
    </Dialog>
  )
}

function GroupsTab() {
  const queryClient = useQueryClient()
  const [createOpen, setCreateOpen] = useState(false)
  const [newGroupName, setNewGroupName] = useState('')
  const [newGroupDesc, setNewGroupDesc] = useState('')
  const [managingGroup, setManagingGroup] = useState<GroupEntry | null>(null)

  const { data: groups, isLoading } = useQuery({
    queryKey: ['admin', 'groups'],
    queryFn: adminApi.listGroups,
  })

  const { data: users } = useQuery({
    queryKey: ['admin', 'users'],
    queryFn: adminApi.listUsers,
  })

  const createMutation = useMutation({
    mutationFn: () => adminApi.createGroup({ name: newGroupName.trim(), description: newGroupDesc.trim() || undefined }),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['admin', 'groups'] })
      setCreateOpen(false)
      setNewGroupName('')
      setNewGroupDesc('')
    },
  })

  const deleteMutation = useMutation({
    mutationFn: adminApi.deleteGroup,
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ['admin', 'groups'] }),
  })

  return (
    <>
      {managingGroup && (
        <ManageMembersDialog
          group={managingGroup}
          open={true}
          onClose={() => setManagingGroup(null)}
          allUsers={users ?? []}
        />
      )}

      <Dialog open={createOpen} onClose={() => setCreateOpen(false)} maxWidth="xs" fullWidth>
        <DialogTitle>Create Group</DialogTitle>
        <DialogContent sx={{ pt: '20px !important' }}>
          <TextField fullWidth label="Group name" value={newGroupName} onChange={(e) => setNewGroupName(e.target.value)} size="small" sx={{ mb: 2 }} required />
          <TextField fullWidth label="Description (optional)" value={newGroupDesc} onChange={(e) => setNewGroupDesc(e.target.value)} size="small" multiline rows={2} />
        </DialogContent>
        <DialogActions sx={{ px: 3, pb: 2 }}>
          <Button onClick={() => setCreateOpen(false)}>Cancel</Button>
          <Button variant="contained" disabled={!newGroupName.trim() || createMutation.isPending} onClick={() => createMutation.mutate()}>
            {createMutation.isPending ? 'Creating…' : 'Create'}
          </Button>
        </DialogActions>
      </Dialog>

      <Card>
        <CardContent sx={{ pb: '12px !important' }}>
          <Box sx={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', mb: 2 }}>
            <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
              <GroupsOutlined sx={{ color: 'primary.main' }} />
              <Typography variant="h6">Groups</Typography>
              {groups && <Chip label={groups.length} size="small" sx={{ height: 18, fontSize: '0.65rem' }} />}
            </Box>
            <Button variant="outlined" size="small" startIcon={<GroupAddOutlined />} onClick={() => setCreateOpen(true)}>
              New Group
            </Button>
          </Box>

          <TableContainer>
            <Table size="small">
              <TableHead>
                <TableRow>
                  <TableCell>Name</TableCell>
                  <TableCell>Description</TableCell>
                  <TableCell>Members</TableCell>
                  <TableCell>Created</TableCell>
                  <TableCell align="center">Actions</TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {isLoading && [...Array(2)].map((_, i) => (
                  <TableRow key={i}>
                    {[...Array(5)].map((_, j) => (
                      <TableCell key={j}><Box sx={{ height: 14, bgcolor: 'rgba(255,255,255,0.05)', borderRadius: 1 }} /></TableCell>
                    ))}
                  </TableRow>
                ))}
                {!isLoading && groups?.length === 0 && (
                  <TableRow>
                    <TableCell colSpan={5} align="center" sx={{ py: 4 }}>
                      <Typography variant="body2" color="text.secondary">No groups yet. Create one to assign users.</Typography>
                    </TableCell>
                  </TableRow>
                )}
                {groups?.map((g) => (
                  <TableRow key={g.id} hover>
                    <TableCell><Typography variant="body2" fontWeight={500}>{g.name}</Typography></TableCell>
                    <TableCell><Typography variant="caption" color="text.secondary">{g.description ?? '—'}</Typography></TableCell>
                    <TableCell>
                      <Chip label={g.member_count} size="small" sx={{ height: 18, fontSize: '0.65rem' }} />
                    </TableCell>
                    <TableCell>
                      <Typography variant="caption" color="text.secondary">
                        {dayjs(g.created_at).format('DD MMM YYYY')}
                      </Typography>
                    </TableCell>
                    <TableCell align="center">
                      <Tooltip title="Manage members">
                        <IconButton size="small" onClick={() => setManagingGroup(g)}>
                          <PeopleOutlined fontSize="small" />
                        </IconButton>
                      </Tooltip>
                      <Tooltip title="Delete group">
                        <IconButton
                          size="small" sx={{ color: 'error.main' }}
                          disabled={deleteMutation.isPending}
                          onClick={() => {
                            if (!window.confirm(`Delete group "${g.name}"? This cannot be undone.`)) return
                            deleteMutation.mutate(g.id)
                          }}
                        >
                          <DeleteOutlined fontSize="small" />
                        </IconButton>
                      </Tooltip>
                    </TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </TableContainer>
        </CardContent>
      </Card>
    </>
  )
}

// ---------------------------------------------------------------------------
// MFA Status tab (B.4)
// ---------------------------------------------------------------------------

function MfaStatusTab() {
  const queryClient = useQueryClient()
  const [filter, setFilter] = useState<'all' | 'enrolled' | 'not_enrolled'>('all')

  const { data: users, isLoading } = useQuery({
    queryKey: ['admin', 'users'],
    queryFn: adminApi.listUsers,
  })

  const resetMfaMutation = useMutation({
    mutationFn: adminApi.resetUserMfa,
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ['admin', 'users'] }),
  })

  const filtered = (users ?? []).filter((u) => {
    if (filter === 'enrolled') return u.mfa_enabled
    if (filter === 'not_enrolled') return !u.mfa_enabled
    return true
  })

  const enrolled = (users ?? []).filter((u) => u.mfa_enabled).length
  const total = (users ?? []).length
  const pct = total > 0 ? Math.round((enrolled / total) * 100) : 0

  return (
    <Card>
      <CardContent sx={{ pb: '12px !important' }}>
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 2 }}>
          <LockOutlined sx={{ color: 'primary.main' }} />
          <Typography variant="h6">MFA Status</Typography>
          {users && (
            <Chip
              label={`${enrolled}/${total} enrolled`}
              size="small"
              sx={{ height: 18, fontSize: '0.65rem', bgcolor: pct === 100 ? '#1a3a27' : pct >= 50 ? 'rgba(255,192,0,0.15)' : 'rgba(192,0,0,0.18)', color: pct === 100 ? '#C6EFCE' : pct >= 50 ? '#FFEB9C' : '#FFC7CE' }}
            />
          )}
        </Box>

        {users && total > 0 && (
          <Box sx={{ mb: 2 }}>
            <Box sx={{ display: 'flex', justifyContent: 'space-between', mb: 0.5 }}>
              <Typography variant="caption" color="text.secondary">MFA adoption</Typography>
              <Typography variant="caption" color="text.secondary">{pct}%</Typography>
            </Box>
            <LinearProgress
              variant="determinate"
              value={pct}
              color={pct === 100 ? 'success' : pct >= 50 ? 'warning' : 'error'}
              sx={{ height: 6, borderRadius: 3 }}
            />
          </Box>
        )}

        <Box sx={{ display: 'flex', gap: 1, mb: 2 }}>
          {(['all', 'enrolled', 'not_enrolled'] as const).map((v) => (
            <Chip
              key={v}
              label={v === 'all' ? 'All' : v === 'enrolled' ? 'Enrolled' : 'Not Enrolled'}
              size="small"
              clickable
              onClick={() => setFilter(v)}
              variant={filter === v ? 'filled' : 'outlined'}
              color={filter === v ? 'primary' : 'default'}
              sx={{ fontSize: '0.7rem' }}
            />
          ))}
        </Box>

        <TableContainer>
          <Table size="small">
            <TableHead>
              <TableRow>
                <TableCell>Email</TableCell>
                <TableCell>Name</TableCell>
                <TableCell>Role</TableCell>
                <TableCell>MFA Status</TableCell>
                <TableCell>Last Login</TableCell>
                <TableCell align="center">Actions</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {isLoading && [...Array(3)].map((_, i) => (
                <TableRow key={i}>
                  {[...Array(6)].map((_, j) => (
                    <TableCell key={j}><Box sx={{ height: 14, bgcolor: 'rgba(255,255,255,0.05)', borderRadius: 1 }} /></TableCell>
                  ))}
                </TableRow>
              ))}
              {filtered.map((user) => {
                const rc = ROLE_COLOR[user.role] ?? ROLE_COLOR.viewer
                return (
                  <TableRow key={user.id} hover>
                    <TableCell><Typography variant="body2" fontFamily="monospace" fontSize="0.75rem">{user.email}</Typography></TableCell>
                    <TableCell><Typography variant="body2">{user.full_name ?? '—'}</Typography></TableCell>
                    <TableCell>
                      <Chip label={user.role} size="small" sx={{ fontSize: '0.6rem', height: 16, bgcolor: rc.bg, color: rc.fg }} />
                    </TableCell>
                    <TableCell>
                      <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.75 }}>
                        {user.mfa_enabled
                          ? <LockOutlined sx={{ fontSize: 15, color: '#C6EFCE' }} />
                          : <LockOpenOutlined sx={{ fontSize: 15, color: 'text.disabled' }} />}
                        <Typography variant="caption" color={user.mfa_enabled ? '#C6EFCE' : 'text.disabled'}>
                          {user.mfa_enabled ? 'Enrolled' : 'Not enrolled'}
                        </Typography>
                      </Box>
                    </TableCell>
                    <TableCell>
                      <Typography variant="caption" color="text.secondary">
                        {user.last_login ? dayjs(user.last_login).format('DD MMM YYYY HH:mm') : '—'}
                      </Typography>
                    </TableCell>
                    <TableCell align="center">
                      {user.mfa_enabled && (
                        <Tooltip title="Reset MFA — user must re-enroll">
                          <IconButton
                            size="small" sx={{ color: 'warning.main' }}
                            disabled={resetMfaMutation.isPending}
                            onClick={() => {
                              if (!window.confirm(`Reset MFA for ${user.email}? They will need to re-enroll.`)) return
                              resetMfaMutation.mutate(user.id)
                            }}
                          >
                            <LockResetOutlined fontSize="small" />
                          </IconButton>
                        </Tooltip>
                      )}
                    </TableCell>
                  </TableRow>
                )
              })}
            </TableBody>
          </Table>
        </TableContainer>
      </CardContent>
    </Card>
  )
}

// ---------------------------------------------------------------------------
// Sessions tab (B.5)
// ---------------------------------------------------------------------------

function SessionsTab() {
  const queryClient = useQueryClient()
  const [emailFilter, setEmailFilter] = useState('')

  const { data: sessions, isLoading } = useQuery({
    queryKey: ['admin', 'sessions'],
    queryFn: () => adminApi.listSessions(),
    refetchInterval: 60_000,
  })

  const revokeMutation = useMutation({
    mutationFn: (id: string) => adminApi.revokeSession(id),
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ['admin', 'sessions'] }),
  })

  const revokeUserMutation = useMutation({
    mutationFn: (userId: string) => adminApi.revokeUserSessions(userId),
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ['admin', 'sessions'] }),
  })

  const filtered = (sessions ?? []).filter((s) =>
    !emailFilter || (s.user_email ?? '').toLowerCase().includes(emailFilter.toLowerCase())
  )

  // Group by user for "revoke all" action
  const userSessions = filtered.reduce<Record<string, number>>((acc, s) => {
    if (s.user_id) acc[s.user_id] = (acc[s.user_id] ?? 0) + 1
    return acc
  }, {})

  return (
    <Card>
      <CardContent sx={{ pb: '12px !important' }}>
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 2 }}>
          <DevicesOutlined sx={{ color: 'primary.main' }} />
          <Typography variant="h6">Active Sessions</Typography>
          {sessions && <Chip label={sessions.length} size="small" sx={{ height: 18, fontSize: '0.65rem' }} />}
          <Typography variant="caption" color="text.secondary" sx={{ ml: 'auto' }}>
            Auto-refreshes every 60s
          </Typography>
        </Box>

        <Box sx={{ mb: 2 }}>
          <TextField
            size="small" label="Filter by email" value={emailFilter}
            onChange={(e) => setEmailFilter(e.target.value)}
            sx={{ width: 260 }}
          />
        </Box>

        <TableContainer>
          <Table size="small">
            <TableHead>
              <TableRow>
                <TableCell>User</TableCell>
                <TableCell>IP Address</TableCell>
                <TableCell>User Agent</TableCell>
                <TableCell>Created</TableCell>
                <TableCell>Expires</TableCell>
                <TableCell align="center">Actions</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {isLoading && [...Array(3)].map((_, i) => (
                <TableRow key={i}>
                  {[...Array(6)].map((_, j) => (
                    <TableCell key={j}><Box sx={{ height: 14, bgcolor: 'rgba(255,255,255,0.05)', borderRadius: 1 }} /></TableCell>
                  ))}
                </TableRow>
              ))}
              {!isLoading && filtered.length === 0 && (
                <TableRow>
                  <TableCell colSpan={6} align="center" sx={{ py: 4 }}>
                    <Typography variant="body2" color="text.secondary">No active sessions.</Typography>
                  </TableCell>
                </TableRow>
              )}
              {filtered.map((s) => (
                <TableRow key={s.id} hover>
                  <TableCell>
                    <Typography variant="body2" fontFamily="monospace" fontSize="0.75rem">{s.user_email ?? s.user_id.slice(0, 8) + '…'}</Typography>
                    {s.user_username && <Typography variant="caption" color="text.secondary" display="block">{s.user_username}</Typography>}
                  </TableCell>
                  <TableCell>
                    <Typography variant="caption" color="text.secondary" fontFamily="monospace">
                      {s.ip_address ?? '—'}
                    </Typography>
                  </TableCell>
                  <TableCell sx={{ maxWidth: 220 }}>
                    <Tooltip title={s.user_agent ?? ''}>
                      <Typography variant="caption" color="text.secondary" noWrap sx={{ display: 'block', maxWidth: 200 }}>
                        {s.user_agent ? s.user_agent.slice(0, 60) + (s.user_agent.length > 60 ? '…' : '') : '—'}
                      </Typography>
                    </Tooltip>
                  </TableCell>
                  <TableCell>
                    <Typography variant="caption" color="text.secondary" noWrap>
                      {dayjs(s.created_at).format('DD MMM HH:mm')}
                    </Typography>
                  </TableCell>
                  <TableCell>
                    <Tooltip title={dayjs(s.expires_at).format('DD MMM YYYY HH:mm:ss')}>
                      <Typography variant="caption" color="text.secondary" noWrap>
                        {dayjs(s.expires_at).format('DD MMM HH:mm')}
                      </Typography>
                    </Tooltip>
                  </TableCell>
                  <TableCell align="center">
                    <Tooltip title="Revoke this session">
                      <IconButton
                        size="small" sx={{ color: 'warning.main' }}
                        disabled={revokeMutation.isPending}
                        onClick={() => {
                          if (!window.confirm('Revoke this session? The user will be signed out.')) return
                          revokeMutation.mutate(s.id)
                        }}
                      >
                        <LogoutOutlined fontSize="small" />
                      </IconButton>
                    </Tooltip>
                    {s.user_id && (userSessions[s.user_id] ?? 0) > 0 && (
                      <Tooltip title={`Revoke all ${userSessions[s.user_id]} sessions for this user`}>
                        <IconButton
                          size="small" sx={{ color: 'error.main' }}
                          disabled={revokeUserMutation.isPending}
                          onClick={() => {
                            if (!window.confirm(`Revoke ALL sessions for ${s.user_email ?? 'this user'}?`)) return
                            revokeUserMutation.mutate(s.user_id)
                          }}
                        >
                          <DevicesOutlined fontSize="small" />
                        </IconButton>
                      </Tooltip>
                    )}
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </CardContent>
    </Card>
  )
}

// ---------------------------------------------------------------------------
// Main page
// ---------------------------------------------------------------------------

export default function Admin() {
  const [tab, setTab] = useState(0)
  const { user } = useAuth()

  if (!user || !['super_admin', 'admin'].includes(user.role)) {
    return (
      <Box sx={{ p: 3 }}>
        <Alert severity="error">Admin role required to access this page.</Alert>
      </Box>
    )
  }

  return (
    <Box>
      <PageHeader title="Administration" subtitle="User management, groups, MFA, and active sessions" />

      <Box sx={{ borderBottom: 1, borderColor: 'divider', mb: 3 }}>
        <Tabs value={tab} onChange={(_, v) => setTab(v)} textColor="primary" indicatorColor="primary">
          <Tab label="Users"      icon={<PeopleOutlined fontSize="small" />}    iconPosition="start" sx={{ minHeight: 48 }} />
          <Tab label="Groups"     icon={<GroupsOutlined fontSize="small" />}    iconPosition="start" sx={{ minHeight: 48 }} />
          <Tab label="MFA Status" icon={<LockOutlined fontSize="small" />}      iconPosition="start" sx={{ minHeight: 48 }} />
          <Tab label="Sessions"   icon={<DevicesOutlined fontSize="small" />}   iconPosition="start" sx={{ minHeight: 48 }} />
        </Tabs>
      </Box>

      {tab === 0 && <UsersTab />}
      {tab === 1 && <GroupsTab />}
      {tab === 2 && <MfaStatusTab />}
      {tab === 3 && <SessionsTab />}
    </Box>
  )
}
