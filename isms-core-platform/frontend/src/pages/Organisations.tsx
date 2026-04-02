import { useState } from 'react'
import {
  Alert,
  Box,
  Button,
  Card,
  CardContent,
  Chip,
  Dialog,
  DialogActions,
  DialogContent,
  DialogTitle,
  Grid,
  IconButton,
  Skeleton,
  TextField,
  Tooltip,
  Typography,
} from '@mui/material'
import {
  AddOutlined,
  ArchiveOutlined,
  BusinessOutlined,
  DeleteOutlined,
  EditOutlined,
  RefreshOutlined,
  UnarchiveOutlined,
} from '@mui/icons-material'
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import dayjs from 'dayjs'
import { orgApi, type OrganisationCreate, type OrganisationPatch } from '../api/orgApi'
import type { OrganisationRead } from '../api/types'
import PageHeader from '../components/PageHeader'
import { useAuth } from '../store/AuthContext'

// ── Create dialog ──────────────────────────────────────────────────────────────

function CreateOrgDialog({ open, onClose }: { open: boolean; onClose: () => void }) {
  const qc = useQueryClient()
  const [form, setForm] = useState<OrganisationCreate>({ name: '', slug: '' })
  const [error, setError] = useState('')

  const mutation = useMutation({
    mutationFn: (body: OrganisationCreate) => orgApi.create(body),
    onSuccess: () => {
      qc.invalidateQueries({ queryKey: ['organisations'] })
      setForm({ name: '', slug: '' })
      setError('')
      onClose()
    },
    onError: () => setError('Failed to create organisation — check slug is unique.'),
  })

  function handleSubmit() {
    if (!form.name.trim()) { setError('Name is required.'); return }
    if (!form.slug.trim()) { setError('Slug is required.'); return }
    if (!/^[a-z0-9-]+$/.test(form.slug)) { setError('Slug must be lowercase letters, numbers, and hyphens only.'); return }
    mutation.mutate(form)
  }

  function deriveSlug(name: string) {
    return name.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '').slice(0, 60)
  }

  return (
    <Dialog open={open} onClose={onClose} maxWidth="sm" fullWidth>
      <DialogTitle sx={{ pb: 0.5 }}>
        New Organisation
        <Typography variant="caption" color="text.secondary" display="block">
          Add a new tenant to the platform
        </Typography>
      </DialogTitle>
      <DialogContent sx={{ pt: '20px !important' }}>
        {error && <Alert severity="error" sx={{ mb: 2, py: 0.5 }}>{error}</Alert>}
        <TextField
          label="Organisation name"
          fullWidth size="small" sx={{ mb: 2 }}
          value={form.name}
          onChange={e => {
            const name = e.target.value
            setForm(f => ({ ...f, name, slug: f.slug || deriveSlug(name) }))
          }}
          placeholder="e.g. Acme Corporation"
        />
        <TextField
          label="Slug"
          fullWidth size="small" sx={{ mb: 2 }}
          value={form.slug}
          onChange={e => setForm(f => ({ ...f, slug: e.target.value }))}
          placeholder="e.g. acme-corporation"
          helperText="Unique identifier — lowercase letters, numbers, hyphens"
        />
        <TextField
          label="Description (optional)"
          fullWidth size="small" multiline rows={2}
          value={form.description ?? ''}
          onChange={e => setForm(f => ({ ...f, description: e.target.value || undefined }))}
        />
      </DialogContent>
      <DialogActions sx={{ px: 3, pb: 2 }}>
        <Button onClick={onClose} size="small">Cancel</Button>
        <Button variant="contained" size="small" onClick={handleSubmit} disabled={mutation.isPending}>
          Create
        </Button>
      </DialogActions>
    </Dialog>
  )
}

// ── Edit dialog ────────────────────────────────────────────────────────────────

function EditOrgDialog({ org, open, onClose }: { org: OrganisationRead; open: boolean; onClose: () => void }) {
  const qc = useQueryClient()
  const [form, setForm] = useState<OrganisationPatch>({ name: org.name, description: org.description ?? '' })
  const [error, setError] = useState('')

  const mutation = useMutation({
    mutationFn: (body: OrganisationPatch) => orgApi.updateById(org.id, body),
    onSuccess: () => {
      qc.invalidateQueries({ queryKey: ['organisations'] })
      setError('')
      onClose()
    },
    onError: () => setError('Failed to update organisation.'),
  })

  return (
    <Dialog open={open} onClose={onClose} maxWidth="sm" fullWidth>
      <DialogTitle sx={{ pb: 0.5 }}>Edit Organisation</DialogTitle>
      <DialogContent sx={{ pt: '20px !important' }}>
        {error && <Alert severity="error" sx={{ mb: 2, py: 0.5 }}>{error}</Alert>}
        <TextField
          label="Name" fullWidth size="small" sx={{ mb: 2 }}
          value={form.name ?? ''}
          onChange={e => setForm(f => ({ ...f, name: e.target.value }))}
        />
        <TextField
          label="Description" fullWidth size="small" multiline rows={2}
          value={form.description ?? ''}
          onChange={e => setForm(f => ({ ...f, description: e.target.value || undefined }))}
        />
      </DialogContent>
      <DialogActions sx={{ px: 3, pb: 2 }}>
        <Button onClick={onClose} size="small">Cancel</Button>
        <Button variant="contained" size="small" onClick={() => mutation.mutate(form)} disabled={mutation.isPending}>
          Save
        </Button>
      </DialogActions>
    </Dialog>
  )
}

// ── Org card ──────────────────────────────────────────────────────────────────

function OrgCard({ org, isSuperAdmin }: { org: OrganisationRead; isSuperAdmin: boolean }) {
  const qc = useQueryClient()
  const [editOpen, setEditOpen] = useState(false)

  const archiveMutation = useMutation({
    mutationFn: () => orgApi.archiveById(org.id),
    onSuccess: () => qc.invalidateQueries({ queryKey: ['organisations'] }),
  })

  const deleteMutation = useMutation({
    mutationFn: () => orgApi.deleteById(org.id),
    onSuccess: () => qc.invalidateQueries({ queryKey: ['organisations'] }),
    onError: (e: { response?: { data?: { detail?: string } } }) =>
      alert(e?.response?.data?.detail ?? 'Delete failed — organisation may have users or projects.'),
  })

  function handleDelete() {
    if (window.confirm(`Permanently delete "${org.name}"? This cannot be undone.`)) {
      deleteMutation.mutate()
    }
  }

  const archived = !org.is_active

  return (
    <>
      <Card variant="outlined" sx={{ height: '100%', opacity: archived ? 0.55 : 1 }}>
        <CardContent>
          <Box sx={{ display: 'flex', alignItems: 'flex-start', justifyContent: 'space-between', mb: 1 }}>
            <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
              <BusinessOutlined sx={{ color: archived ? 'text.disabled' : '#4472C4', fontSize: 20 }} />
              <Typography variant="subtitle2" fontWeight={600} color={archived ? 'text.disabled' : 'text.primary'}>
                {org.name}
              </Typography>
              {archived && <Chip label="archived" size="small" sx={{ height: 16, fontSize: '0.62rem', bgcolor: 'rgba(158,158,158,0.15)', color: 'text.disabled' }} />}
            </Box>
            {isSuperAdmin && (
              <Box sx={{ display: 'flex', gap: 0.25 }}>
                <Tooltip title="Edit">
                  <IconButton size="small" onClick={() => setEditOpen(true)}>
                    <EditOutlined sx={{ fontSize: 14 }} />
                  </IconButton>
                </Tooltip>
                <Tooltip title={archived ? 'Restore' : 'Archive'}>
                  <IconButton size="small" onClick={() => archiveMutation.mutate()} disabled={archiveMutation.isPending}>
                    {archived ? <UnarchiveOutlined sx={{ fontSize: 14 }} /> : <ArchiveOutlined sx={{ fontSize: 14 }} />}
                  </IconButton>
                </Tooltip>
                <Tooltip title="Delete">
                  <IconButton size="small" onClick={handleDelete} disabled={deleteMutation.isPending} sx={{ color: 'error.main' }}>
                    <DeleteOutlined sx={{ fontSize: 14 }} />
                  </IconButton>
                </Tooltip>
              </Box>
            )}
          </Box>

          <Typography variant="caption" color="text.disabled" sx={{ display: 'block', mb: 1 }}>
            {org.slug}
          </Typography>

          {org.description && (
            <Typography variant="body2" color="text.secondary" sx={{ mb: 1.5, fontSize: '0.8rem' }}>
              {org.description}
            </Typography>
          )}

          <Box sx={{ display: 'flex', gap: 0.75, flexWrap: 'wrap', mt: 'auto' }}>
            <Chip
              label={org.governance_mode}
              size="small"
              sx={{ fontSize: '0.68rem', height: 20,
                bgcolor: org.governance_mode === 'platform' ? 'rgba(68,114,196,0.1)' : 'rgba(255,152,0,0.1)',
                color: org.governance_mode === 'platform' ? '#4472C4' : '#FF9800' }}
            />
            <Chip
              label={org.privacy_role}
              size="small"
              sx={{ fontSize: '0.68rem', height: 20, bgcolor: 'rgba(112,48,160,0.1)', color: '#7030A0' }}
            />
          </Box>

          <Typography variant="caption" color="text.disabled" sx={{ display: 'block', mt: 1.5 }}>
            Created {dayjs(org.created_at).format('DD MMM YYYY')}
          </Typography>
        </CardContent>
      </Card>

      {editOpen && <EditOrgDialog org={org} open={editOpen} onClose={() => setEditOpen(false)} />}
    </>
  )
}

// ── Main page ─────────────────────────────────────────────────────────────────

export default function Organisations() {
  const { isSuperAdmin, user } = useAuth()
  const [createOpen, setCreateOpen] = useState(false)
  const qc = useQueryClient()

  const { data: orgs, isLoading, isError } = useQuery({
    queryKey: ['organisations', isSuperAdmin],
    queryFn: () => isSuperAdmin ? orgApi.list() : orgApi.get().then(o => [o]),
  })

  if (!isSuperAdmin && user?.role !== 'admin') {
    return (
      <Box sx={{ p: 3 }}>
        <Alert severity="error">Admin or Super Admin role required.</Alert>
      </Box>
    )
  }

  return (
    <Box sx={{ p: 3 }}>
      <PageHeader
        title="Organisations"
        subtitle={isSuperAdmin ? 'All tenants on this platform' : 'Your organisation'}
        actions={
          <Box sx={{ display: 'flex', gap: 1 }}>
            <Button size="small" startIcon={<RefreshOutlined />} onClick={() => qc.invalidateQueries({ queryKey: ['organisations'] })}>
              Refresh
            </Button>
            {isSuperAdmin && (
              <Button size="small" variant="contained" startIcon={<AddOutlined />} onClick={() => setCreateOpen(true)}>
                New Organisation
              </Button>
            )}
          </Box>
        }
      />

      {isError && <Alert severity="error" sx={{ mb: 2 }}>Failed to load organisations.</Alert>}

      <Grid container spacing={2}>
        {isLoading
          ? Array.from({ length: 3 }).map((_, i) => (
              <Grid item xs={12} sm={6} md={4} key={i}>
                <Skeleton variant="rectangular" height={160} sx={{ borderRadius: 1 }} />
              </Grid>
            ))
          : orgs?.map(org => (
              <Grid item xs={12} sm={6} md={4} key={org.id}>
                <OrgCard org={org} isSuperAdmin={isSuperAdmin} />
              </Grid>
            ))
        }
      </Grid>

      {createOpen && <CreateOrgDialog open={createOpen} onClose={() => setCreateOpen(false)} />}
    </Box>
  )
}
