import { useState } from 'react'
import {
  Alert,
  Box,
  Button,
  Card,
  CardActionArea,
  CardContent,
  Chip,
  Collapse,
  Dialog,
  DialogActions,
  DialogContent,
  DialogTitle,
  FormControl,
  Grid,
  IconButton,
  InputLabel,
  LinearProgress,
  MenuItem,
  Select,
  Skeleton,
  TextField,
  ToggleButton,
  ToggleButtonGroup,
  Tooltip,
  Typography,
} from '@mui/material'
import {
  AddOutlined,
  ArrowForwardOutlined,
  DeleteOutlined,
  ExpandMoreOutlined,
  FolderOpenOutlined,
  RestoreFromTrashOutlined,
  ShieldOutlined,
  LockPersonOutlined,
  CloudOutlined,
} from '@mui/icons-material'
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { useNavigate } from 'react-router-dom'
import dayjs from 'dayjs'
import { projectsApi, type ProjectCreate, type ProjectRead, type DocVars } from '../api/projectsApi'
import PageHeader from '../components/PageHeader'
import { useProject } from '../store/ProjectContext'

const FAMILY_COLOR: Record<string, string> = {
  ISMS:    '#4472C4',
  PRIVACY: '#70309f',
  CLOUD:   '#0099cc',
}

const FAMILY_ICON: Record<string, React.ReactNode> = {
  ISMS:    <ShieldOutlined sx={{ fontSize: 15 }} />,
  PRIVACY: <LockPersonOutlined sx={{ fontSize: 15 }} />,
  CLOUD:   <CloudOutlined sx={{ fontSize: 15 }} />,
}

const STATUS_COLOR: Record<string, string> = {
  active:   '#4CAF50',
  inactive: '#FF9800',
  draft:    '#64B5F6',
  archived: '#9E9E9E',
}

const TOTAL_CG: Record<string, number> = { ISMS: 53, PRIVACY: 21, CLOUD: 12 }

// ── Create dialog ─────────────────────────────────────────────────────────────
const EMPTY_DOC_VARS: DocVars = { ciso_name: '', ceo_name: '', dpo_name: '', legal_entity: '', effective_date: '', review_date: '', classification: 'Internal' }

function CreateProjectDialog({ open, onClose }: { open: boolean; onClose: () => void }) {
  const qc = useQueryClient()
  const [form, setForm] = useState<ProjectCreate>({ name: '', org_name: '', product_family: 'ISMS', project_subtype: 'fw', description: '' })
  const [docVars, setDocVars] = useState<DocVars>(EMPTY_DOC_VARS)
  const [showDocVars, setShowDocVars] = useState(true)
  const [error, setError] = useState('')

  const mutation = useMutation({
    mutationFn: (body: ProjectCreate) => projectsApi.create(body),
    onSuccess: () => {
      qc.invalidateQueries({ queryKey: ['projects'] })
      setForm({ name: '', org_name: '', product_family: 'ISMS', project_subtype: 'fw', description: '' })
      setDocVars(EMPTY_DOC_VARS)
      setShowDocVars(false)
      setError('')
      onClose()
    },
    onError: () => setError('Failed to create project — try again.'),
  })

  function handleSubmit() {
    if (!form.name.trim()) { setError('Project name is required.'); return }
    if (!form.org_name.trim()) { setError('Organisation name is required.'); return }
    if (!docVars.ciso_name?.trim()) { setError('CISO name is required.'); return }
    if (!docVars.effective_date?.trim()) { setError('Effective date is required.'); return }
    const dv: DocVars = Object.fromEntries(Object.entries(docVars).filter(([, v]) => v)) as DocVars
    mutation.mutate({ ...form, doc_vars: Object.keys(dv).length ? dv : undefined })
  }

  const setDv = (k: keyof DocVars, v: string) => setDocVars(f => ({ ...f, [k]: v }))

  return (
    <Dialog open={open} onClose={onClose} maxWidth="sm" fullWidth>
      <DialogTitle sx={{ pb: 0.5 }}>
        New Project
        <Typography variant="caption" color="text.secondary" display="block">
          Create a workspace for a specific product and organisation
        </Typography>
      </DialogTitle>
      <DialogContent sx={{ pt: 2 }}>
        {error && <Alert severity="error" sx={{ mb: 2, py: 0.5 }}>{error}</Alert>}
        <TextField
          label="Project name"
          fullWidth size="small" sx={{ mb: 2 }}
          value={form.name}
          onChange={e => setForm(f => ({ ...f, name: e.target.value }))}
          placeholder="e.g. Acme Corp ISMS 2026"
        />
        <TextField
          label="Organisation"
          fullWidth size="small" sx={{ mb: 2 }}
          value={form.org_name}
          onChange={e => setForm(f => ({ ...f, org_name: e.target.value }))}
          placeholder="e.g. Acme Corporation"
          helperText="Used as [Organisation] in all policy and implementation documents"
        />
        <FormControl fullWidth size="small" sx={{ mb: form.product_family === 'ISMS' ? 1.5 : 2 }}>
          <InputLabel>Product</InputLabel>
          <Select
            label="Product"
            value={form.product_family}
            onChange={e => setForm(f => ({ ...f, product_family: e.target.value, project_subtype: e.target.value === 'ISMS' ? 'fw' : undefined }))}
          >
            <MenuItem value="ISMS">ISMS — ISO 27001:2022</MenuItem>
            <MenuItem value="PRIVACY">Privacy — ISO 27701:2025</MenuItem>
            <MenuItem value="CLOUD">Cloud — ISO 27018:2025</MenuItem>
          </Select>
        </FormControl>
        {form.product_family === 'ISMS' && (
          <Box sx={{ mb: 2 }}>
            <Typography variant="caption" color="text.secondary" sx={{ display: 'block', mb: 0.75, fontSize: '0.72rem' }}>
              ISMS variant
            </Typography>
            <ToggleButtonGroup
              size="small" exclusive
              value={form.project_subtype ?? 'fw'}
              onChange={(_, v) => { if (v) setForm(f => ({ ...f, project_subtype: v })) }}
            >
              <ToggleButton value="fw" sx={{ px: 2, fontSize: '0.72rem' }}>Framework (FW)</ToggleButton>
              <ToggleButton value="op" sx={{ px: 2, fontSize: '0.72rem' }}>Operational (OP)</ToggleButton>
            </ToggleButtonGroup>
            <Typography variant="caption" color="text.disabled" sx={{ display: 'block', mt: 0.5, fontSize: '0.67rem' }}>
              FW = ISO 27001 policies &amp; IMPs · OP = adds SCR checklists
            </Typography>
          </Box>
        )}
        <TextField
          label="Description (optional)"
          fullWidth size="small" multiline rows={2} sx={{ mb: 2 }}
          value={form.description}
          onChange={e => setForm(f => ({ ...f, description: e.target.value }))}
        />

        {/* Document variables (collapsible) */}
        <Box
          onClick={() => setShowDocVars(v => !v)}
          sx={{ display: 'flex', alignItems: 'center', gap: 1, cursor: 'pointer', mb: showDocVars ? 1.5 : 0, '&:hover': { opacity: 0.8 } }}
        >
          <ExpandMoreOutlined sx={{ fontSize: 16, color: 'text.secondary', transition: 'transform 0.2s', transform: showDocVars ? 'rotate(0)' : 'rotate(-90deg)' }} />
          <Typography variant="caption" sx={{ color: 'text.secondary', fontSize: '0.75rem', fontWeight: 500 }}>
            Document Variables
          </Typography>
          <Typography variant="caption" sx={{ color: '#FF9800', fontSize: '0.68rem', fontWeight: 500 }}>
            CISO name + date required
          </Typography>
          <Typography variant="caption" color="text.disabled" sx={{ fontSize: '0.68rem' }}>
            — pre-filled into all policy &amp; IMP headers when added to this project
          </Typography>
        </Box>
        <Collapse in={showDocVars}>
          <Box sx={{ pl: 2, borderLeft: '2px solid', borderColor: 'divider', mb: 1 }}>
            <Typography variant="caption" color="text.disabled" sx={{ display: 'block', mb: 1.5, fontSize: '0.68rem' }}>
              These values replace <code>[CISO name]</code>, <code>[DPO name]</code>, <code>[Date to be set]</code> etc. in library documents when they are added to this project.
            </Typography>
            <Box sx={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 1.5, mb: 1.5 }}>
              <TextField label="CISO name *" size="small" fullWidth value={docVars.ciso_name ?? ''}
                onChange={e => setDv('ciso_name', e.target.value)} placeholder="e.g. Jane Smith" />
              <TextField label="CEO name" size="small" fullWidth value={docVars.ceo_name ?? ''}
                onChange={e => setDv('ceo_name', e.target.value)} placeholder="e.g. John Smith" />
              <TextField label="DPO name" size="small" fullWidth value={docVars.dpo_name ?? ''}
                onChange={e => setDv('dpo_name', e.target.value)} placeholder="e.g. John Doe" />
              <TextField label="Legal entity name" size="small" fullWidth value={docVars.legal_entity ?? ''}
                onChange={e => setDv('legal_entity', e.target.value)} placeholder="e.g. Acme Corporation Ltd." />
              <TextField label="Effective date *" size="small" fullWidth value={docVars.effective_date ?? ''}
                onChange={e => setDv('effective_date', e.target.value)}
                placeholder="DD.MM.YYYY or YYYY-MM-DD"
                helperText="e.g. 01.01.2026" />
              <TextField label="Next review date" size="small" fullWidth value={docVars.review_date ?? ''}
                onChange={e => setDv('review_date', e.target.value)}
                placeholder="DD.MM.YYYY or YYYY-MM-DD"
                helperText="e.g. 01.01.2027" />
            </Box>
            <TextField label="Classification" size="small" sx={{ minWidth: 180 }} value={docVars.classification ?? ''}
              onChange={e => setDv('classification', e.target.value)} placeholder="Internal" />
          </Box>
        </Collapse>
      </DialogContent>
      <DialogActions sx={{ px: 3, pb: 2 }}>
        <Button onClick={onClose} disabled={mutation.isPending}>Cancel</Button>
        <Button variant="contained" onClick={handleSubmit} disabled={mutation.isPending}>
          Create
        </Button>
      </DialogActions>
    </Dialog>
  )
}

// ── Archive dialog (soft-delete) ──────────────────────────────────────────────
function ArchiveProjectDialog({
  projectId, projectName, open, onClose,
}: { projectId: string; projectName: string; open: boolean; onClose: () => void }) {
  const qc = useQueryClient()
  const mutation = useMutation({
    mutationFn: () => projectsApi.update(projectId, { status: 'archived' }),
    onSuccess: () => { qc.invalidateQueries({ queryKey: ['projects'] }); onClose() },
  })
  return (
    <Dialog open={open} onClose={onClose} maxWidth="xs" fullWidth>
      <DialogTitle>Archive project?</DialogTitle>
      <DialogContent>
        <Typography variant="body2" gutterBottom>
          <strong>{projectName}</strong> will be moved to the Archived filter.
          All policies, implementations and checklists are preserved.
        </Typography>
        <Typography variant="body2" color="text.secondary">
          You can restore it at any time by setting its status back to active.
        </Typography>
      </DialogContent>
      <DialogActions sx={{ px: 3, pb: 2 }}>
        <Button onClick={onClose}>Cancel</Button>
        <Button variant="contained" color="warning" onClick={() => mutation.mutate()} disabled={mutation.isPending}>
          Archive
        </Button>
      </DialogActions>
    </Dialog>
  )
}

// ── Permanent delete dialog (archived projects only) ──────────────────────────
function DeleteProjectDialog({
  projectId, projectName, open, onClose,
}: { projectId: string; projectName: string; open: boolean; onClose: () => void }) {
  const qc = useQueryClient()
  const mutation = useMutation({
    mutationFn: () => projectsApi.delete(projectId),
    onSuccess: () => { qc.invalidateQueries({ queryKey: ['projects'] }); onClose() },
  })
  return (
    <Dialog open={open} onClose={onClose} maxWidth="xs" fullWidth>
      <DialogTitle>Permanently delete project?</DialogTitle>
      <DialogContent>
        <Typography variant="body2" gutterBottom>
          <strong>{projectName}</strong> and all its policies, implementations and checklists will be permanently deleted.
          This cannot be undone.
        </Typography>
        <Typography variant="body2" color="text.secondary">
          Assessments, gaps and evidence linked to this project will be unlinked but not deleted.
        </Typography>
      </DialogContent>
      <DialogActions sx={{ px: 3, pb: 2 }}>
        <Button onClick={onClose}>Cancel</Button>
        <Button variant="contained" color="error" onClick={() => mutation.mutate()} disabled={mutation.isPending}>
          Delete permanently
        </Button>
      </DialogActions>
    </Dialog>
  )
}

// ── Project card ──────────────────────────────────────────────────────────────
function ProjectCard({ project }: { project: ProjectRead }) {
  const navigate = useNavigate()
  const qc = useQueryClient()
  const { activeProjectId, setActiveProject } = useProject()
  const [archiveOpen, setArchiveOpen] = useState(false)
  const [deleteOpen, setDeleteOpen] = useState(false)
  const fam = project.product_family
  const isSelected = activeProjectId === project.id
  const color = FAMILY_COLOR[fam] ?? '#4472C4'
  const total = TOTAL_CG[fam] ?? 53
  const statusColor = STATUS_COLOR[project.status] ?? '#9E9E9E'

  const polPct = Math.min(100, Math.round((project.policy_count / Math.max(1, total)) * 100))

  const isArchived = project.status === 'archived'

  const statusToggle = useMutation({
    mutationFn: (newStatus: string) => projectsApi.update(project.id, { status: newStatus }),
    onSuccess: () => qc.invalidateQueries({ queryKey: ['projects'] }),
  })

  function handleRestore(e: React.MouseEvent) {
    e.stopPropagation()
    statusToggle.mutate('draft')
  }

  function handleToggleActive(e: React.MouseEvent) {
    e.stopPropagation()
    if (isSelected) {
      // Deselect → mark inactive
      setActiveProject(null)
      statusToggle.mutate('inactive')
    } else {
      // Select → mark active
      setActiveProject(project)
      statusToggle.mutate('active')
    }
  }

  return (
    <>
      <Card sx={{
        height: '100%',
        border: '1px solid',
        borderColor: isSelected ? `${color}80` : 'divider',
        '&:hover': { borderColor: `${color}60` },
        transition: 'border-color 0.15s',
        boxShadow: isSelected ? `0 0 0 1px ${color}40` : 'none',
      }}>
        <CardActionArea onClick={() => navigate(`/projects/${project.id}`)}>
          <CardContent sx={{ pb: '8px !important' }}>
            {/* Header row */}
            <Box sx={{ display: 'flex', alignItems: 'flex-start', justifyContent: 'space-between', mb: 1.5 }}>
              <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                <Box sx={{ color, display: 'flex' }}><FolderOpenOutlined sx={{ fontSize: 22 }} /></Box>
                <Box>
                  <Typography variant="subtitle2" sx={{ fontWeight: 700, lineHeight: 1.2, fontSize: '0.88rem' }}>
                    {project.name}
                  </Typography>
                  <Typography variant="caption" color="text.secondary" sx={{ fontSize: '0.72rem' }}>
                    {project.org_name}
                  </Typography>
                </Box>
              </Box>
              <Box sx={{ display: 'flex', gap: 0.5, flexShrink: 0 }}>
                <Chip
                  label={fam}
                  size="small"
                  icon={FAMILY_ICON[fam] as any}
                  sx={{ height: 20, fontSize: '0.64rem', bgcolor: `${color}18`, color, border: `1px solid ${color}40`, '& .MuiChip-icon': { color } }}
                />
                <Chip
                  label={project.status}
                  size="small"
                  sx={{ height: 20, fontSize: '0.64rem', bgcolor: `${statusColor}18`, color: statusColor }}
                />
              </Box>
            </Box>

            {/* Counts */}
            <Box sx={{ display: 'flex', gap: 2, mb: 1.5 }}>
              {[
                { label: 'Policies', val: project.policy_count },
                { label: 'Implementations', val: project.implementation_count },
                { label: 'Checklists', val: project.checklist_count },
              ].map(({ label, val }) => (
                <Box key={label} sx={{ textAlign: 'center' }}>
                  <Typography variant="h6" sx={{ fontWeight: 700, fontSize: '1.1rem', color, lineHeight: 1 }}>{val}</Typography>
                  <Typography variant="caption" color="text.secondary" sx={{ fontSize: '0.65rem' }}>{label}</Typography>
                </Box>
              ))}
            </Box>

            {/* Completeness bar */}
            <Box sx={{ mb: 0.5 }}>
              <Box sx={{ display: 'flex', justifyContent: 'space-between', mb: 0.3 }}>
                <Typography variant="caption" sx={{ fontSize: '0.65rem', color: 'text.secondary' }}>
                  Control groups with policies
                </Typography>
                <Typography variant="caption" sx={{ fontSize: '0.65rem', color }}>
                  {Math.min(project.policy_count, total)}/{total}
                </Typography>
              </Box>
              <LinearProgress
                variant="determinate"
                value={polPct}
                sx={{ height: 4, borderRadius: 2, bgcolor: `${color}18`, '& .MuiLinearProgress-bar': { bgcolor: color } }}
              />
            </Box>

            {/* Footer — date on left, action buttons + arrow on right */}
            <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mt: 1.5 }}>
              <Typography variant="caption" color="text.disabled" sx={{ fontSize: '0.65rem' }}>
                Created {dayjs(project.created_at).format('D MMM YYYY')}
              </Typography>
              <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.5 }}>
                {isSelected && (
                  <Chip label="Selected" size="small" sx={{ height: 18, fontSize: '0.6rem', bgcolor: `${color}20`, color }} />
                )}
                <Tooltip title={isSelected ? 'Deactivate (set inactive)' : 'Set as active project'}>
                  <IconButton
                    size="small"
                    onClick={handleToggleActive}
                    disabled={statusToggle.isPending}
                    sx={{ color: isSelected ? color : 'text.disabled', '&:hover': { color }, p: 0.4 }}
                  >
                    <FolderOpenOutlined sx={{ fontSize: 16 }} />
                  </IconButton>
                </Tooltip>
                {isArchived ? (
                  <>
                    <Tooltip title="Restore project (set to draft)">
                      <IconButton
                        size="small"
                        onClick={handleRestore}
                        disabled={statusToggle.isPending}
                        sx={{ color: 'text.disabled', '&:hover': { color: 'success.main' }, p: 0.4 }}
                      >
                        <RestoreFromTrashOutlined sx={{ fontSize: 16 }} />
                      </IconButton>
                    </Tooltip>
                    <Tooltip title="Delete permanently">
                      <IconButton
                        size="small"
                        onClick={e => { e.stopPropagation(); setDeleteOpen(true) }}
                        sx={{ color: 'text.disabled', '&:hover': { color: 'error.main' }, p: 0.4 }}
                      >
                        <DeleteOutlined sx={{ fontSize: 16 }} />
                      </IconButton>
                    </Tooltip>
                  </>
                ) : (
                  <Tooltip title="Archive project">
                    <IconButton
                      size="small"
                      onClick={e => { e.stopPropagation(); setArchiveOpen(true) }}
                      sx={{ color: 'text.disabled', '&:hover': { color: 'warning.main' }, p: 0.4 }}
                    >
                      <DeleteOutlined sx={{ fontSize: 16 }} />
                    </IconButton>
                  </Tooltip>
                )}
                <ArrowForwardOutlined sx={{ fontSize: 14, color: 'text.disabled' }} />
              </Box>
            </Box>
          </CardContent>
        </CardActionArea>
      </Card>

      <ArchiveProjectDialog
        projectId={project.id}
        projectName={project.name}
        open={archiveOpen}
        onClose={() => setArchiveOpen(false)}
      />
      <DeleteProjectDialog
        projectId={project.id}
        projectName={project.name}
        open={deleteOpen}
        onClose={() => setDeleteOpen(false)}
      />
    </>
  )
}

// ── Main page ──────────────────────────────────────────────────────────────────
export default function Projects() {
  const [createOpen, setCreateOpen] = useState(false)
  const [familyFilter, setFamilyFilter] = useState<string>('ALL')
  const [statusFilter, setStatusFilter] = useState<string>('active')

  const { data, isLoading } = useQuery({
    queryKey: ['projects', familyFilter, statusFilter],
    queryFn: () => projectsApi.list({
      product_family: familyFilter === 'ALL' ? undefined : familyFilter,
      status: statusFilter === 'ALL' ? undefined : statusFilter,
    }),
  })

  const families = ['ALL', 'ISMS', 'PRIVACY', 'CLOUD']
  const statuses = ['ALL', 'active', 'inactive', 'draft', 'archived']

  return (
    <Box>
      <PageHeader
        title="Projects"
        subtitle="Compliance workspaces — each project tracks policies, implementations and evidence for one organisation"
        actions={
          <Button variant="contained" startIcon={<AddOutlined />} size="small" onClick={() => setCreateOpen(true)}>
            New Project
          </Button>
        }
      />

      {/* Filters */}
      <Box sx={{ display: 'flex', gap: 1.5, mb: 3, flexWrap: 'wrap', alignItems: 'center' }}>
        <Box sx={{ display: 'flex', gap: 0.5 }}>
          {families.map(f => {
            const active = familyFilter === f
            const color = FAMILY_COLOR[f] ?? '#6B7A99'
            return (
              <Chip
                key={f}
                label={f}
                size="small"
                onClick={() => setFamilyFilter(f)}
                sx={{
                  height: 26, fontSize: '0.72rem', cursor: 'pointer',
                  bgcolor: active ? `${color}20` : 'transparent',
                  color: active ? color : 'text.secondary',
                  border: '1px solid',
                  borderColor: active ? `${color}60` : 'rgba(255,255,255,0.12)',
                  '&:hover': { bgcolor: `${color}12` },
                }}
              />
            )
          })}
        </Box>
        <Box sx={{ display: 'flex', gap: 0.5 }}>
          {statuses.map(s => {
            const active = statusFilter === s
            const color = STATUS_COLOR[s] ?? '#6B7A99'
            return (
              <Chip
                key={s}
                label={s}
                size="small"
                onClick={() => setStatusFilter(s)}
                sx={{
                  height: 26, fontSize: '0.72rem', cursor: 'pointer',
                  bgcolor: active ? `${color}20` : 'transparent',
                  color: active ? color : 'text.secondary',
                  border: '1px solid',
                  borderColor: active ? `${color}60` : 'rgba(255,255,255,0.12)',
                  '&:hover': { bgcolor: `${color}12` },
                }}
              />
            )
          })}
        </Box>
      </Box>

      {/* Cards grid */}
      {isLoading ? (
        <Grid container spacing={2}>
          {[...Array(6)].map((_, i) => (
            <Grid item xs={12} sm={6} md={4} key={i}>
              <Skeleton variant="rounded" height={180} />
            </Grid>
          ))}
        </Grid>
      ) : !data?.length ? (
        <Box sx={{ textAlign: 'center', py: 8 }}>
          <FolderOpenOutlined sx={{ fontSize: 48, color: 'text.disabled', mb: 1.5 }} />
          <Typography variant="h6" color="text.secondary" sx={{ mb: 0.5 }}>No projects yet</Typography>
          <Typography variant="body2" color="text.disabled" sx={{ mb: 2 }}>
            Create your first project to start building your compliance workspace
          </Typography>
          <Button variant="contained" startIcon={<AddOutlined />} onClick={() => setCreateOpen(true)}>
            New Project
          </Button>
        </Box>
      ) : (
        <Grid container spacing={2}>
          {data.map(p => (
            <Grid item xs={12} sm={6} md={4} key={p.id}>
              <ProjectCard project={p} />
            </Grid>
          ))}
        </Grid>
      )}

      <CreateProjectDialog open={createOpen} onClose={() => setCreateOpen(false)} />
    </Box>
  )
}
