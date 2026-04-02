import { useState } from 'react'
import {
  Alert, Box, Button, Chip, Dialog, DialogActions, DialogContent, DialogTitle,
  FormControl, IconButton, InputLabel, MenuItem, Select,
  Skeleton, TextField, Tooltip, Typography,
} from '@mui/material'
import {
  AddOutlined, DeleteOutlined, EditOutlined, LanguageOutlined, VerifiedOutlined,
} from '@mui/icons-material'
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import dayjs from 'dayjs'
import { tprmApi, type Vendor, type VendorCreate } from '../api/tprmApi'
import PageHeader from '../components/PageHeader'

// ── Helpers ───────────────────────────────────────────────────────────────────

const CRIT_COLOR: Record<string, string> = {
  critical: '#9C27B0',
  high:     '#F44336',
  medium:   '#FF9800',
  low:      '#4CAF50',
}

const VENDOR_TYPES = ['supplier', 'provider', 'partner', 'subprocessor']
const CRITICALITIES = ['low', 'medium', 'high', 'critical']
const STATUSES = ['active', 'under_review', 'terminated']
const STATUS_LABELS: Record<string, string> = {
  active: 'Active', under_review: 'Under Review', terminated: 'Terminated',
}
const STATUS_COLORS: Record<string, string> = {
  active: '#4CAF50', under_review: '#FF9800', terminated: '#9E9E9E',
}
const DORA_ENTITY_TYPES = [
  'direct', 'sub_outsourcing', 'intra_group', 'critical', 'important',
]
const DORA_ICT_SERVICES = [
  'cloud_computing', 'data_analytics', 'data_centre', 'software', 'hardware',
  'network', 'security', 'other',
]
const DORA_SUBSTITUTABILITY = ['easy', 'difficult', 'not_substitutable']

function toLabel(s: string) {
  return s.replace(/_/g, ' ').replace(/\b\w/g, c => c.toUpperCase())
}

function CritChip({ crit }: { crit: string }) {
  const color = CRIT_COLOR[crit] ?? '#9E9E9E'
  return (
    <Chip
      label={toLabel(crit)}
      size="small"
      sx={{
        height: 20, fontSize: '0.62rem', fontWeight: 700,
        bgcolor: `${color}18`, color, border: `1px solid ${color}40`,
      }}
    />
  )
}

function StatusChip({ status }: { status: string }) {
  const color = STATUS_COLORS[status] ?? '#9E9E9E'
  return (
    <Chip
      label={STATUS_LABELS[status] ?? toLabel(status)}
      size="small"
      sx={{
        height: 20, fontSize: '0.62rem', fontWeight: 600,
        bgcolor: `${color}18`, color, border: `1px solid ${color}40`,
      }}
    />
  )
}

// ── Summary cards ─────────────────────────────────────────────────────────────

function SummaryCards() {
  const { data, isLoading } = useQuery({
    queryKey: ['tprm-summary'],
    queryFn: () => tprmApi.summary(),
  })
  const cards = [
    { label: 'Total Vendors',      value: data?.total,                   color: '#607D8B' },
    { label: 'Active',             value: data?.active,                  color: '#4CAF50' },
    { label: 'Critical',           value: data?.critical,                color: '#9C27B0' },
    { label: 'DORA-Regulated',     value: data?.dora_regulated,          color: '#2196F3' },
    { label: 'Contracts Expiring', value: data?.contracts_expiring_soon, color: '#FF9800' },
  ]
  return (
    <Box sx={{ display: 'flex', gap: 1.5, flexWrap: 'wrap', mb: 2.5 }}>
      {cards.map(c => (
        <Box
          key={c.label}
          sx={{
            minWidth: 100, p: 1.5, borderRadius: 1.5,
            border: '1px solid', borderColor: `${c.color}30`, bgcolor: `${c.color}08`,
          }}
        >
          {isLoading
            ? <Skeleton width={32} height={28} />
            : <Typography variant="h5" sx={{ fontWeight: 700, color: c.color, lineHeight: 1 }}>{c.value ?? 0}</Typography>}
          <Typography variant="caption" sx={{ fontSize: '0.65rem', color: 'text.secondary' }}>{c.label}</Typography>
        </Box>
      ))}
    </Box>
  )
}

// ── Vendor dialog ─────────────────────────────────────────────────────────────

const BLANK: VendorCreate = {
  name: '', vendor_type: 'supplier', criticality: 'medium', status: 'active',
}

function VendorDialog({
  open, onClose, existing,
}: { open: boolean; onClose: () => void; existing?: Vendor }) {
  const qc = useQueryClient()
  const isEdit = !!existing

  const [form, setForm] = useState<VendorCreate>(existing ? {
    name: existing.name,
    vendor_type: existing.vendor_type ?? 'supplier',
    criticality: existing.criticality ?? 'medium',
    status: existing.status ?? 'active',
    description: existing.description ?? '',
    website: existing.website ?? '',
    primary_contact: existing.primary_contact ?? '',
    dora_entity_type: existing.dora_entity_type ?? '',
    dora_ict_service_type: existing.dora_ict_service_type ?? '',
    dora_substitutability: existing.dora_substitutability ?? '',
    dora_register_ref: existing.dora_register_ref ?? '',
  } : { ...BLANK })
  const [error, setError] = useState('')

  const invalidate = () => {
    qc.invalidateQueries({ queryKey: ['vendors'] })
    qc.invalidateQueries({ queryKey: ['tprm-summary'] })
  }
  const createMut = useMutation({
    mutationFn: (b: VendorCreate) => tprmApi.create(b),
    onSuccess: () => { invalidate(); onClose() },
    onError: () => setError('Failed to save.'),
  })
  const updateMut = useMutation({
    mutationFn: (b: Partial<VendorCreate>) => tprmApi.update(existing!.id, b),
    onSuccess: () => { invalidate(); onClose() },
    onError: () => setError('Failed to save.'),
  })

  const isPending = createMut.isPending || updateMut.isPending
  const set = (k: keyof VendorCreate, v: unknown) => setForm(f => ({ ...f, [k]: v }))
  const showDora = !!form.dora_entity_type

  function handleSubmit() {
    if (!form.name.trim()) { setError('Name is required.'); return }
    const body: VendorCreate = {
      ...form,
      description: (form.description as string) || undefined,
      website: (form.website as string) || undefined,
      primary_contact: (form.primary_contact as string) || undefined,
      dora_entity_type: (form.dora_entity_type as string) || undefined,
      dora_ict_service_type: (form.dora_ict_service_type as string) || undefined,
      dora_substitutability: (form.dora_substitutability as string) || undefined,
      dora_register_ref: (form.dora_register_ref as string) || undefined,
    }
    isEdit ? updateMut.mutate(body) : createMut.mutate(body)
  }

  return (
    <Dialog open={open} onClose={onClose} maxWidth="sm" fullWidth>
      <DialogTitle sx={{ pb: 0.5 }}>{isEdit ? 'Edit Vendor' : 'New Vendor'}</DialogTitle>
      <DialogContent sx={{ pt: '20px !important' }}>
        {error && <Alert severity="error" sx={{ mb: 2, py: 0.5 }}>{error}</Alert>}

        <TextField label="Vendor name *" fullWidth size="small" sx={{ mb: 2 }}
          value={form.name} onChange={e => set('name', e.target.value)} />

        <Box sx={{ display: 'flex', gap: 1.5, mb: 2 }}>
          <FormControl size="small" sx={{ flex: 1 }}>
            <InputLabel>Type</InputLabel>
            <Select value={form.vendor_type ?? 'supplier'} label="Type"
              onChange={e => set('vendor_type', e.target.value)}>
              {VENDOR_TYPES.map(t => <MenuItem key={t} value={t}>{toLabel(t)}</MenuItem>)}
            </Select>
          </FormControl>
          <FormControl size="small" sx={{ flex: 1 }}>
            <InputLabel>Criticality</InputLabel>
            <Select value={form.criticality ?? 'medium'} label="Criticality"
              onChange={e => set('criticality', e.target.value)}>
              {CRITICALITIES.map(c => <MenuItem key={c} value={c}>{toLabel(c)}</MenuItem>)}
            </Select>
          </FormControl>
          <FormControl size="small" sx={{ flex: 1 }}>
            <InputLabel>Status</InputLabel>
            <Select value={form.status ?? 'active'} label="Status"
              onChange={e => set('status', e.target.value)}>
              {STATUSES.map(s => <MenuItem key={s} value={s}>{STATUS_LABELS[s]}</MenuItem>)}
            </Select>
          </FormControl>
        </Box>

        <TextField label="Description" fullWidth size="small" multiline rows={2} sx={{ mb: 2 }}
          value={form.description ?? ''} onChange={e => set('description', e.target.value)} />

        <Box sx={{ display: 'flex', gap: 1.5, mb: 2 }}>
          <TextField label="Website" size="small" sx={{ flex: 1 }}
            value={form.website ?? ''} onChange={e => set('website', e.target.value)} />
          <TextField label="Primary contact" size="small" sx={{ flex: 1 }}
            value={form.primary_contact ?? ''} onChange={e => set('primary_contact', e.target.value)} />
        </Box>

        <Box sx={{ mb: 1, pb: 0.75, borderBottom: '1px solid', borderColor: 'divider' }}>
          <Typography variant="caption" sx={{ fontWeight: 700, color: '#2196F3', textTransform: 'uppercase', fontSize: '0.65rem' }}>
            DORA — Digital Operational Resilience Act (optional)
          </Typography>
        </Box>

        <FormControl size="small" fullWidth sx={{ mb: 2, mt: 1 }}>
          <InputLabel>DORA entity type</InputLabel>
          <Select value={form.dora_entity_type ?? ''} label="DORA entity type"
            onChange={e => set('dora_entity_type', e.target.value)}>
            <MenuItem value="">— Not DORA-regulated —</MenuItem>
            {DORA_ENTITY_TYPES.map(t => <MenuItem key={t} value={t}>{toLabel(t)}</MenuItem>)}
          </Select>
        </FormControl>

        {showDora && (
          <>
            <Box sx={{ display: 'flex', gap: 1.5, mb: 2 }}>
              <FormControl size="small" sx={{ flex: 1 }}>
                <InputLabel>ICT service type</InputLabel>
                <Select value={form.dora_ict_service_type ?? ''} label="ICT service type"
                  onChange={e => set('dora_ict_service_type', e.target.value)}>
                  <MenuItem value="">—</MenuItem>
                  {DORA_ICT_SERVICES.map(s => <MenuItem key={s} value={s}>{toLabel(s)}</MenuItem>)}
                </Select>
              </FormControl>
              <FormControl size="small" sx={{ flex: 1 }}>
                <InputLabel>Substitutability</InputLabel>
                <Select value={form.dora_substitutability ?? ''} label="Substitutability"
                  onChange={e => set('dora_substitutability', e.target.value)}>
                  <MenuItem value="">—</MenuItem>
                  {DORA_SUBSTITUTABILITY.map(s => <MenuItem key={s} value={s}>{toLabel(s)}</MenuItem>)}
                </Select>
              </FormControl>
            </Box>
            <TextField label="DORA register ref" fullWidth size="small" sx={{ mb: 2 }}
              value={form.dora_register_ref ?? ''} onChange={e => set('dora_register_ref', e.target.value)} />
          </>
        )}
      </DialogContent>
      <DialogActions sx={{ px: 3, pb: 2 }}>
        <Button onClick={onClose} size="small">Cancel</Button>
        <Button variant="contained" size="small" onClick={handleSubmit} disabled={isPending}>
          {isPending ? 'Saving…' : isEdit ? 'Save' : 'Create'}
        </Button>
      </DialogActions>
    </Dialog>
  )
}

// ── Vendor row ────────────────────────────────────────────────────────────────

function VendorRow({
  vendor, onEdit, onDelete,
}: { vendor: Vendor; onEdit: () => void; onDelete: () => void }) {
  return (
    <Box sx={{
      display: 'flex', alignItems: 'center', gap: 1, px: 2, py: 1.25,
      borderBottom: '1px solid', borderColor: 'divider',
      '&:hover': { bgcolor: 'action.hover' },
    }}>
      {/* Name */}
      <Box sx={{ flex: 3, minWidth: 0 }}>
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.5 }}>
          <Typography variant="body2" sx={{ fontWeight: 500, fontSize: '0.82rem' }} noWrap>
            {vendor.name}
          </Typography>
          {vendor.website && (
            <Tooltip title={vendor.website}>
              <IconButton size="small" component="a" href={vendor.website} target="_blank" sx={{ p: 0.25 }}>
                <LanguageOutlined sx={{ fontSize: 13, color: 'text.disabled' }} />
              </IconButton>
            </Tooltip>
          )}
        </Box>
        {vendor.primary_contact && (
          <Typography variant="caption" sx={{ fontSize: '0.65rem', color: 'text.disabled' }}>
            {vendor.primary_contact}
          </Typography>
        )}
      </Box>

      {/* Type */}
      <Box sx={{ flex: 1.2, minWidth: 0 }}>
        <Typography variant="caption" sx={{ fontSize: '0.72rem', color: 'text.secondary' }}>
          {toLabel(vendor.vendor_type ?? '—')}
        </Typography>
      </Box>

      {/* Criticality */}
      <Box sx={{ width: 80 }}>
        <CritChip crit={vendor.criticality} />
      </Box>

      {/* Status */}
      <Box sx={{ width: 100 }}>
        <StatusChip status={vendor.status} />
      </Box>

      {/* DORA badge */}
      <Box sx={{ width: 60, textAlign: 'center' }}>
        {vendor.dora_entity_type && (
          <Tooltip title={`DORA: ${toLabel(vendor.dora_entity_type)}`}>
            <Chip
              icon={<VerifiedOutlined sx={{ fontSize: 11 }} />}
              label="DORA"
              size="small"
              sx={{
                height: 18, fontSize: '0.6rem', fontWeight: 700,
                bgcolor: '#2196F318', color: '#2196F3', border: '1px solid #2196F340',
                '& .MuiChip-icon': { color: '#2196F3', ml: '4px' },
              }}
            />
          </Tooltip>
        )}
      </Box>

      {/* Last assessment */}
      <Box sx={{ minWidth: 90, textAlign: 'right' }}>
        <Typography variant="caption" sx={{ fontSize: '0.65rem', color: 'text.secondary' }}>
          {vendor.last_assessment_date ? dayjs(vendor.last_assessment_date).format('D MMM YY') : '—'}
        </Typography>
      </Box>

      {/* Contracts */}
      <Box sx={{ width: 70, textAlign: 'center' }}>
        <Typography
          variant="caption"
          sx={{ fontSize: '0.72rem', color: vendor.contracts_expiring_soon > 0 ? '#FF9800' : 'text.secondary' }}
        >
          {vendor.contract_count}
          {vendor.contracts_expiring_soon > 0 ? ` (${vendor.contracts_expiring_soon}⚠)` : ''}
        </Typography>
      </Box>

      {/* Actions */}
      <Box sx={{ display: 'flex', gap: 0.25 }}>
        <IconButton size="small" onClick={onEdit} sx={{ p: 0.5 }}>
          <EditOutlined sx={{ fontSize: 15 }} />
        </IconButton>
        <IconButton size="small" onClick={onDelete} sx={{ p: 0.5, color: 'error.light' }}>
          <DeleteOutlined sx={{ fontSize: 15 }} />
        </IconButton>
      </Box>
    </Box>
  )
}

// ── Main page ─────────────────────────────────────────────────────────────────

export default function Tprm() {
  const qc = useQueryClient()
  const [critFilter, setCritFilter] = useState('')
  const [statusFilter, setStatusFilter] = useState('')
  const [dialogOpen, setDialogOpen] = useState(false)
  const [editing, setEditing] = useState<Vendor | undefined>()

  const { data, isLoading } = useQuery({
    queryKey: ['vendors', critFilter, statusFilter],
    queryFn: () => tprmApi.list({
      ...(critFilter ? { criticality: critFilter } : {}),
      ...(statusFilter ? { status: statusFilter } : {}),
    }),
  })

  const deleteMut = useMutation({
    mutationFn: (id: string) => tprmApi.delete(id),
    onSuccess: () => {
      qc.invalidateQueries({ queryKey: ['vendors'] })
      qc.invalidateQueries({ queryKey: ['tprm-summary'] })
    },
  })

  function openCreate() { setEditing(undefined); setDialogOpen(true) }
  function openEdit(v: Vendor) { setEditing(v); setDialogOpen(true) }

  return (
    <Box sx={{ p: 3 }}>
      <PageHeader
        title="Third-Party Risk"
        subtitle="Vendor & supplier risk register — ISO 27001:2022 §A.5.19–22 · DORA Art. 28"
        actions={
          <Button variant="contained" size="small" startIcon={<AddOutlined />} onClick={openCreate}>
            New Vendor
          </Button>
        }
      />

      <SummaryCards />

      {/* Filters */}
      <Box sx={{ display: 'flex', gap: 1.5, mb: 2, alignItems: 'center' }}>
        <FormControl size="small" sx={{ minWidth: 140 }}>
          <InputLabel>Criticality</InputLabel>
          <Select value={critFilter} label="Criticality" onChange={e => setCritFilter(e.target.value)}>
            <MenuItem value="">All</MenuItem>
            {CRITICALITIES.map(c => <MenuItem key={c} value={c}>{toLabel(c)}</MenuItem>)}
          </Select>
        </FormControl>
        <FormControl size="small" sx={{ minWidth: 140 }}>
          <InputLabel>Status</InputLabel>
          <Select value={statusFilter} label="Status" onChange={e => setStatusFilter(e.target.value)}>
            <MenuItem value="">All</MenuItem>
            {STATUSES.map(s => <MenuItem key={s} value={s}>{STATUS_LABELS[s]}</MenuItem>)}
          </Select>
        </FormControl>
        {(critFilter || statusFilter) && (
          <Button size="small" onClick={() => { setCritFilter(''); setStatusFilter('') }}
            sx={{ textTransform: 'none', fontSize: '0.75rem' }}>
            Clear
          </Button>
        )}
        <Typography variant="caption" sx={{ ml: 'auto', color: 'text.disabled' }}>
          {data?.length ?? 0} vendor{data?.length !== 1 ? 's' : ''}
        </Typography>
      </Box>

      {/* Table header */}
      <Box sx={{
        display: 'flex', alignItems: 'center', gap: 1, px: 2, py: 0.75,
        bgcolor: 'action.hover', borderRadius: '8px 8px 0 0',
        border: '1px solid', borderColor: 'divider', borderBottom: 'none',
      }}>
        <Typography variant="caption" sx={{ flex: 3, fontWeight: 600, fontSize: '0.7rem', color: 'text.secondary', textTransform: 'uppercase' }}>Name / Contact</Typography>
        <Typography variant="caption" sx={{ flex: 1.2, fontWeight: 600, fontSize: '0.7rem', color: 'text.secondary', textTransform: 'uppercase' }}>Type</Typography>
        <Typography variant="caption" sx={{ width: 80, fontWeight: 600, fontSize: '0.7rem', color: 'text.secondary', textTransform: 'uppercase' }}>Criticality</Typography>
        <Typography variant="caption" sx={{ width: 100, fontWeight: 600, fontSize: '0.7rem', color: 'text.secondary', textTransform: 'uppercase' }}>Status</Typography>
        <Typography variant="caption" sx={{ width: 60, textAlign: 'center', fontWeight: 600, fontSize: '0.7rem', color: 'text.secondary', textTransform: 'uppercase' }}>DORA</Typography>
        <Typography variant="caption" sx={{ minWidth: 90, textAlign: 'right', fontWeight: 600, fontSize: '0.7rem', color: 'text.secondary', textTransform: 'uppercase' }}>Last Assessed</Typography>
        <Typography variant="caption" sx={{ width: 70, textAlign: 'center', fontWeight: 600, fontSize: '0.7rem', color: 'text.secondary', textTransform: 'uppercase' }}>Contracts</Typography>
        <Box sx={{ width: 56 }} />
      </Box>

      <Box sx={{ border: '1px solid', borderColor: 'divider', borderRadius: '0 0 8px 8px', overflow: 'hidden' }}>
        {isLoading && [0, 1, 2, 3].map(i => (
          <Box key={i} sx={{ px: 2, py: 1.5, borderBottom: '1px solid', borderColor: 'divider' }}>
            <Skeleton height={20} />
          </Box>
        ))}

        {!isLoading && (!data || data.length === 0) && (
          <Box sx={{ py: 6, textAlign: 'center' }}>
            <Typography variant="body2" color="text.secondary">No vendors yet.</Typography>
            <Button variant="outlined" size="small" startIcon={<AddOutlined />} onClick={openCreate} sx={{ mt: 1.5 }}>
              Add first vendor
            </Button>
          </Box>
        )}

        {data?.map(v => (
          <VendorRow
            key={v.id}
            vendor={v}
            onEdit={() => openEdit(v)}
            onDelete={() => { if (confirm(`Delete "${v.name}"?`)) deleteMut.mutate(v.id) }}
          />
        ))}
      </Box>

      <VendorDialog
        open={dialogOpen}
        onClose={() => setDialogOpen(false)}
        existing={editing}
      />
    </Box>
  )
}
