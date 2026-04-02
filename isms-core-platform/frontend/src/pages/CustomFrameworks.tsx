import { useState } from 'react'
import {
  Alert, Box, Button, Chip, Collapse, Dialog, DialogActions, DialogContent,
  DialogTitle, IconButton, InputAdornment, Skeleton, Snackbar, TextField,
  Tooltip, Typography,
} from '@mui/material'
import {
  AddOutlined, ClearOutlined, CodeOutlined, DeleteOutlined,
  ExpandLessOutlined, ExpandMoreOutlined, SearchOutlined,
} from '@mui/icons-material'
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import dayjs from 'dayjs'
import { customFrameworksApi, type CustomFramework, type CustomControl } from '../api/customFrameworksApi'
import PageHeader from '../components/PageHeader'

// ── Helpers ───────────────────────────────────────────────────────────────────

const PRIORITY_COLORS: Record<string, string> = {
  critical: '#9C27B0',
  high:     '#F44336',
  medium:   '#FF9800',
  low:      '#4CAF50',
}

const STATUS_COLORS: Record<string, string> = {
  active:    '#4CAF50',
  draft:     '#FF9800',
  archived:  '#607D8B',
}

function toLabel(s: string) {
  return s.replace(/_/g, ' ').replace(/\b\w/g, c => c.toUpperCase())
}

function PriorityChip({ priority }: { priority: string | null }) {
  if (!priority) return <Typography variant="caption" color="text.disabled">—</Typography>
  const color = PRIORITY_COLORS[priority.toLowerCase()] ?? '#607D8B'
  return (
    <Chip
      label={toLabel(priority)}
      size="small"
      sx={{
        height: 20, fontSize: '0.62rem', fontWeight: 700,
        bgcolor: `${color}18`, color, border: `1px solid ${color}40`,
      }}
    />
  )
}

function StatusChip({ status }: { status: string }) {
  const color = STATUS_COLORS[status] ?? '#607D8B'
  return (
    <Chip
      label={toLabel(status)}
      size="small"
      sx={{
        height: 20, fontSize: '0.62rem', fontWeight: 700,
        bgcolor: `${color}18`, color, border: `1px solid ${color}40`,
      }}
    />
  )
}

function MappingChip({ ref: refLabel }: { ref: string }) {
  return (
    <Chip
      label={refLabel}
      size="small"
      sx={{
        height: 18, fontSize: '0.6rem', fontWeight: 600,
        bgcolor: '#2196F318', color: '#2196F3', border: '1px solid #2196F340',
        mr: 0.5, mb: 0.25,
      }}
    />
  )
}

function TagChip({ tag }: { tag: string }) {
  return (
    <Chip
      label={tag}
      size="small"
      sx={{
        height: 18, fontSize: '0.6rem',
        bgcolor: 'action.hover', mr: 0.5, mb: 0.25,
      }}
    />
  )
}

const TH_SX = {
  fontWeight: 600, fontSize: '0.7rem', color: 'text.secondary', textTransform: 'uppercase',
}

const HEADER_SX = {
  display: 'flex', alignItems: 'center', gap: 1, px: 2, py: 0.75,
  bgcolor: 'action.hover', borderRadius: '8px 8px 0 0',
  border: '1px solid', borderColor: 'divider', borderBottom: 'none',
}

const ROW_SX = {
  display: 'flex', alignItems: 'flex-start', gap: 1, px: 2, py: 1.25,
  borderBottom: '1px solid', borderColor: 'divider',
  '&:hover': { bgcolor: 'action.hover' },
}

const EXAMPLE_YAML = `name: "My Framework"
short_code: "MY_FW"
version: "1.0"
description: "Optional description"
controls:
  - id: "MY.1.1"
    title: "Control title"
    category: "Access Control"
    priority: "high"
    iso_mappings: ["A.5.15", "A.5.16"]
    tags: ["identity", "access"]
  - id: "MY.1.2"
    title: "Another control"
    category: "Access Control"
    description: "Optional detailed description"
    priority: "medium"
    iso_mappings: ["A.8.2"]
    tags: ["data"]`

// ── Controls detail panel ─────────────────────────────────────────────────────

function FrameworkControls({ frameworkId }: { frameworkId: string }) {
  const [search, setSearch] = useState('')

  const { data, isLoading } = useQuery({
    queryKey: ['custom-framework-controls', frameworkId, search],
    queryFn: () => customFrameworksApi.listControls(frameworkId, search ? { search } : {}),
  })

  const filtered = data ?? []

  return (
    <Box sx={{ mt: 1.5, mb: 1 }}>
      {/* Search */}
      <Box sx={{ mb: 1.5 }}>
        <TextField
          size="small"
          placeholder="Search controls…"
          value={search}
          onChange={e => setSearch(e.target.value)}
          InputProps={{
            startAdornment: (
              <InputAdornment position="start">
                <SearchOutlined sx={{ fontSize: 16, color: 'text.disabled' }} />
              </InputAdornment>
            ),
            endAdornment: search ? (
              <InputAdornment position="end">
                <IconButton size="small" onClick={() => setSearch('')} sx={{ p: 0.25 }}>
                  <ClearOutlined sx={{ fontSize: 14 }} />
                </IconButton>
              </InputAdornment>
            ) : null,
          }}
          sx={{ width: 280 }}
        />
      </Box>

      {/* Table header */}
      <Box sx={HEADER_SX}>
        <Typography sx={{ ...TH_SX, width: 90 }}>Control ID</Typography>
        <Typography sx={{ ...TH_SX, flex: 3 }}>Title</Typography>
        <Typography sx={{ ...TH_SX, flex: 2 }}>Category</Typography>
        <Typography sx={{ ...TH_SX, width: 80 }}>Priority</Typography>
        <Typography sx={{ ...TH_SX, flex: 2 }}>ISO Mappings</Typography>
        <Typography sx={{ ...TH_SX, flex: 2 }}>Tags</Typography>
      </Box>
      <Box sx={{ border: '1px solid', borderColor: 'divider', borderRadius: '0 0 8px 8px', overflow: 'hidden' }}>
        {isLoading && [0,1,2,3].map(i => (
          <Box key={i} sx={{ px: 2, py: 1.5, borderBottom: '1px solid', borderColor: 'divider' }}>
            <Skeleton height={20} />
          </Box>
        ))}
        {!isLoading && filtered.length === 0 && (
          <Box sx={{ py: 4, textAlign: 'center' }}>
            <Typography variant="body2" color="text.secondary">
              {search ? 'No controls match your search.' : 'No controls in this framework.'}
            </Typography>
          </Box>
        )}
        {filtered.map((ctrl: CustomControl) => (
          <Box key={ctrl.id} sx={ROW_SX}>
            <Box sx={{ width: 90, pt: 0.25 }}>
              <Typography variant="caption" sx={{ fontFamily: 'monospace', fontWeight: 700, fontSize: '0.72rem', color: 'primary.main' }}>
                {ctrl.control_id}
              </Typography>
            </Box>
            <Box sx={{ flex: 3, minWidth: 0 }}>
              <Typography variant="body2" sx={{ fontWeight: 500, fontSize: '0.82rem' }}>
                {ctrl.title}
              </Typography>
              {ctrl.description && (
                <Typography variant="caption" sx={{ fontSize: '0.65rem', color: 'text.secondary' }}>
                  {ctrl.description}
                </Typography>
              )}
            </Box>
            <Box sx={{ flex: 2, minWidth: 0 }}>
              <Typography variant="caption" sx={{ fontSize: '0.72rem', color: 'text.secondary' }}>
                {ctrl.category ?? '—'}
              </Typography>
              {ctrl.subcategory && (
                <Typography variant="caption" sx={{ display: 'block', fontSize: '0.65rem', color: 'text.disabled' }}>
                  {ctrl.subcategory}
                </Typography>
              )}
            </Box>
            <Box sx={{ width: 80 }}>
              <PriorityChip priority={ctrl.priority} />
            </Box>
            <Box sx={{ flex: 2, minWidth: 0 }}>
              {ctrl.iso_mappings.length > 0
                ? ctrl.iso_mappings.map(m => <MappingChip key={m} ref={m} />)
                : <Typography variant="caption" color="text.disabled">—</Typography>}
            </Box>
            <Box sx={{ flex: 2, minWidth: 0 }}>
              {ctrl.tags.length > 0
                ? ctrl.tags.map(t => <TagChip key={t} tag={t} />)
                : <Typography variant="caption" color="text.disabled">—</Typography>}
            </Box>
          </Box>
        ))}
      </Box>
      <Typography variant="caption" sx={{ display: 'block', mt: 0.75, color: 'text.disabled', fontSize: '0.65rem' }}>
        {filtered.length} control{filtered.length !== 1 ? 's' : ''}
        {search ? ` matching "${search}"` : ''}
      </Typography>
    </Box>
  )
}

// ── Import dialog ─────────────────────────────────────────────────────────────

function ImportDialog({
  open, onClose, onSuccess,
}: { open: boolean; onClose: () => void; onSuccess: (msg: string) => void }) {
  const qc = useQueryClient()
  const [yamlContent, setYamlContent] = useState('')
  const [showExample, setShowExample] = useState(false)
  const [error, setError] = useState('')

  const mut = useMutation({
    mutationFn: () => customFrameworksApi.importYaml(yamlContent),
    onSuccess: (fw) => {
      qc.invalidateQueries({ queryKey: ['custom-frameworks'] })
      onSuccess(`Framework imported: ${fw.control_count} control${fw.control_count !== 1 ? 's' : ''}`)
      onClose()
      setYamlContent(''); setError('')
    },
    onError: (err: unknown) => {
      const msg = (err as { response?: { data?: { detail?: string } } })?.response?.data?.detail
      setError(msg ?? 'Import failed. Check your YAML format.')
    },
  })

  function handleImport() {
    if (!yamlContent.trim()) { setError('YAML content is required.'); return }
    setError(''); mut.mutate()
  }

  return (
    <Dialog open={open} onClose={onClose} maxWidth="md" fullWidth>
      <DialogTitle sx={{ pb: 0.5 }}>Import Custom Framework</DialogTitle>
      <DialogContent sx={{ pt: '20px !important' }}>
        {error && <Alert severity="error" sx={{ mb: 2, py: 0.5 }}>{error}</Alert>}

        <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 1 }}>
          <Typography variant="caption" color="text.secondary" sx={{ fontSize: '0.78rem' }}>
            Paste your framework YAML below.
          </Typography>
          <Button
            size="small"
            startIcon={showExample ? <ExpandLessOutlined /> : <CodeOutlined />}
            onClick={() => setShowExample(v => !v)}
            sx={{ textTransform: 'none', fontSize: '0.72rem', ml: 'auto' }}
          >
            {showExample ? 'Hide example' : 'Show example'}
          </Button>
        </Box>

        <Collapse in={showExample}>
          <Box
            sx={{
              mb: 2, p: 1.5, borderRadius: 1, border: '1px solid', borderColor: 'divider',
              bgcolor: 'background.default',
            }}
          >
            <Typography variant="caption" sx={{ fontFamily: 'monospace', fontSize: '0.72rem', whiteSpace: 'pre', display: 'block', color: 'text.secondary' }}>
              {EXAMPLE_YAML}
            </Typography>
            <Button
              size="small"
              onClick={() => { setYamlContent(EXAMPLE_YAML); setShowExample(false) }}
              sx={{ mt: 1, textTransform: 'none', fontSize: '0.72rem' }}
            >
              Use this example
            </Button>
          </Box>
        </Collapse>

        <TextField
          label="YAML content"
          multiline
          rows={18}
          fullWidth
          value={yamlContent}
          onChange={e => setYamlContent(e.target.value)}
          placeholder={EXAMPLE_YAML}
          InputProps={{ sx: { fontFamily: 'monospace', fontSize: '0.78rem' } }}
        />
      </DialogContent>
      <DialogActions sx={{ px: 3, pb: 2 }}>
        <Button onClick={onClose} size="small">Cancel</Button>
        <Button variant="contained" size="small" onClick={handleImport} disabled={mut.isPending}>
          {mut.isPending ? 'Importing…' : 'Import Framework'}
        </Button>
      </DialogActions>
    </Dialog>
  )
}

// ── Framework card ────────────────────────────────────────────────────────────

function FrameworkCard({
  framework, onDelete,
}: { framework: CustomFramework; onDelete: () => void }) {
  const [expanded, setExpanded] = useState(false)

  return (
    <Box
      sx={{
        border: '1px solid', borderColor: 'divider', borderRadius: 2,
        mb: 1.5, overflow: 'hidden',
      }}
    >
      {/* Header row */}
      <Box
        sx={{
          display: 'flex', alignItems: 'center', gap: 1.5, p: 2,
          cursor: 'pointer',
          '&:hover': { bgcolor: 'action.hover' },
        }}
        onClick={() => setExpanded(v => !v)}
      >
        {/* Short code badge */}
        <Box
          sx={{
            px: 1, py: 0.25, borderRadius: 1,
            bgcolor: 'primary.main', color: 'primary.contrastText',
            fontFamily: 'monospace', fontSize: '0.65rem', fontWeight: 700,
            whiteSpace: 'nowrap',
          }}
        >
          {framework.short_code}
        </Box>

        {/* Name + description */}
        <Box sx={{ flex: 1, minWidth: 0 }}>
          <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
            <Typography variant="body2" sx={{ fontWeight: 700, fontSize: '0.88rem' }} noWrap>
              {framework.name}
            </Typography>
            <Typography variant="caption" sx={{ fontSize: '0.65rem', color: 'text.disabled' }}>
              v{framework.version}
            </Typography>
          </Box>
          {framework.description && (
            <Typography variant="caption" sx={{ fontSize: '0.72rem', color: 'text.secondary' }} noWrap>
              {framework.description}
            </Typography>
          )}
        </Box>

        {/* Controls count */}
        <Tooltip title={`${framework.control_count} controls`}>
          <Chip
            label={`${framework.control_count} ctrl${framework.control_count !== 1 ? 's' : ''}`}
            size="small"
            sx={{
              height: 20, fontSize: '0.62rem', fontWeight: 600,
              bgcolor: '#607D8B18', color: '#607D8B', border: '1px solid #607D8B40',
            }}
          />
        </Tooltip>

        {/* Status */}
        <StatusChip status={framework.status} />

        {/* Created */}
        <Typography variant="caption" sx={{ fontSize: '0.65rem', color: 'text.disabled', minWidth: 70, textAlign: 'right' }}>
          {dayjs(framework.created_at).format('D MMM YY')}
        </Typography>

        {/* Expand toggle */}
        <IconButton size="small" sx={{ p: 0.5, ml: 0.5 }} onClick={e => { e.stopPropagation(); setExpanded(v => !v) }}>
          {expanded
            ? <ExpandLessOutlined sx={{ fontSize: 16 }} />
            : <ExpandMoreOutlined sx={{ fontSize: 16 }} />}
        </IconButton>

        {/* Delete */}
        <IconButton
          size="small"
          sx={{ p: 0.5, color: 'error.light' }}
          onClick={e => { e.stopPropagation(); onDelete() }}
        >
          <DeleteOutlined sx={{ fontSize: 15 }} />
        </IconButton>
      </Box>

      {/* Expanded controls */}
      <Collapse in={expanded}>
        <Box sx={{ px: 2, pb: 2, borderTop: '1px solid', borderColor: 'divider', pt: 1.5 }}>
          <FrameworkControls frameworkId={framework.id} />
        </Box>
      </Collapse>
    </Box>
  )
}

// ── Main page ─────────────────────────────────────────────────────────────────

export default function CustomFrameworks() {
  const qc = useQueryClient()
  const [importOpen, setImportOpen] = useState(false)
  const [snackMsg, setSnackMsg] = useState('')

  const { data, isLoading, error } = useQuery({
    queryKey: ['custom-frameworks'],
    queryFn: customFrameworksApi.list,
  })

  const deleteMut = useMutation({
    mutationFn: (id: string) => customFrameworksApi.delete(id),
    onSuccess: () => qc.invalidateQueries({ queryKey: ['custom-frameworks'] }),
  })

  return (
    <Box sx={{ p: 3 }}>
      <PageHeader
        title="Custom Frameworks"
        subtitle="Import sector-specific or custom control frameworks via YAML"
        actions={
          <Button variant="contained" size="small" startIcon={<AddOutlined />}
            onClick={() => setImportOpen(true)}>
            Import Framework
          </Button>
        }
      />

      {error && (
        <Alert severity="error" sx={{ mb: 2, py: 0.5 }}>
          Failed to load frameworks.
        </Alert>
      )}

      {/* Stats bar */}
      {!isLoading && data && data.length > 0 && (
        <Box sx={{ display: 'flex', gap: 1.5, flexWrap: 'wrap', mb: 2.5 }}>
          {[
            { label: 'Frameworks', value: data.length, color: '#607D8B' },
            { label: 'Total Controls', value: data.reduce((s, f) => s + f.control_count, 0), color: '#2196F3' },
            { label: 'Active', value: data.filter(f => f.status === 'active').length, color: '#4CAF50' },
          ].map(c => (
            <Box
              key={c.label}
              sx={{
                minWidth: 90, p: 1.5, borderRadius: 1.5,
                border: '1px solid', borderColor: `${c.color}30`, bgcolor: `${c.color}08`,
              }}
            >
              <Typography variant="h5" sx={{ fontWeight: 700, color: c.color, lineHeight: 1 }}>{c.value}</Typography>
              <Typography variant="caption" sx={{ fontSize: '0.65rem', color: 'text.secondary' }}>{c.label}</Typography>
            </Box>
          ))}
        </Box>
      )}

      {/* Loading skeletons */}
      {isLoading && [0,1,2].map(i => (
        <Box
          key={i}
          sx={{ border: '1px solid', borderColor: 'divider', borderRadius: 2, p: 2, mb: 1.5 }}
        >
          <Skeleton height={28} width="40%" />
          <Skeleton height={16} width="60%" sx={{ mt: 0.5 }} />
        </Box>
      ))}

      {/* Empty state */}
      {!isLoading && (!data || data.length === 0) && (
        <Box
          sx={{
            py: 8, textAlign: 'center',
            border: '1px dashed', borderColor: 'divider', borderRadius: 2,
          }}
        >
          <Typography variant="body2" color="text.secondary" sx={{ mb: 1.5 }}>
            No custom frameworks yet. Import one using the button above.
          </Typography>
          <Button variant="outlined" size="small" startIcon={<AddOutlined />}
            onClick={() => setImportOpen(true)}>
            Import first framework
          </Button>
        </Box>
      )}

      {/* Framework cards */}
      {data?.map(fw => (
        <FrameworkCard
          key={fw.id}
          framework={fw}
          onDelete={() => {
            if (confirm(`Delete framework "${fw.name}"? This will remove all ${fw.control_count} controls.`)) {
              deleteMut.mutate(fw.id)
            }
          }}
        />
      ))}

      <ImportDialog
        open={importOpen}
        onClose={() => setImportOpen(false)}
        onSuccess={msg => setSnackMsg(msg)}
      />

      <Snackbar
        open={!!snackMsg}
        autoHideDuration={4000}
        onClose={() => setSnackMsg('')}
        message={snackMsg}
        anchorOrigin={{ vertical: 'bottom', horizontal: 'center' }}
      />
    </Box>
  )
}
