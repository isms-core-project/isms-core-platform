import { useState } from 'react'
import { useTheme } from '@mui/material/styles'
import { useParams, useNavigate } from 'react-router-dom'
import {
  Box, Button, Card, CardContent, Chip, Collapse, Dialog, DialogActions,
  DialogContent, DialogTitle, IconButton, LinearProgress, Skeleton, Table,
  TableBody, TableCell, TableContainer, TableHead, TableRow, Tooltip,
  Typography, Alert, Checkbox, TextField,
} from '@mui/material'
import {
  ArrowBackOutlined, CalendarTodayOutlined, DeleteOutlined, DownloadOutlined,
  ExpandLessOutlined, ExpandMoreOutlined, PersonAddOutlined, PersonRemoveOutlined,
} from '@mui/icons-material'
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { collectionsApi, CollectionMember } from '../api/collectionsApi'
import { assessmentsApi } from '../api/assessmentsApi'
import { client } from '../api/client'
import PageHeader from '../components/PageHeader'

// ── Helpers ─────────────────────────────────────────────────────────────────

function scoreColor(pct: number): string {
  if (pct >= 80) return '#70AD47'
  if (pct >= 50) return '#FFC000'
  return '#FF5252'
}

function statusChipProps(status: string, isLight: boolean) {
  switch (status) {
    case 'complete':    return { label: 'Complete',    bg: isLight ? 'rgba(27,94,32,0.1)'  : 'rgba(198,239,206,0.15)', color: isLight ? '#1b5e20' : '#C6EFCE' }
    case 'in_progress': return { label: 'In Progress', bg: 'rgba(255,192,0,0.12)',          color: '#856404' }
    default:            return { label: 'Not Started', bg: isLight ? 'rgba(0,0,0,0.06)'    : 'rgba(255,255,255,0.06)', color: isLight ? '#555' : '#888' }
  }
}

function triggerDownload(blob: Blob, filename: string) {
  const url = URL.createObjectURL(blob)
  const a = document.createElement('a')
  a.href = url
  a.download = filename
  document.body.appendChild(a)
  a.click()
  document.body.removeChild(a)
  URL.revokeObjectURL(url)
}

// ── NC items sub-table ───────────────────────────────────────────────────────

function NcItems({ member }: { member: CollectionMember }) {
  const [open, setOpen] = useState(false)
  if (member.items_non_compliant === 0) return null
  return (
    <Box>
      <Button
        size="small"
        variant="text"
        onClick={() => setOpen(v => !v)}
        endIcon={open ? <ExpandLessOutlined sx={{ fontSize: 14 }} /> : <ExpandMoreOutlined sx={{ fontSize: 14 }} />}
        sx={{ fontSize: '0.7rem', color: '#FF5252', py: 0.25, px: 0.75, minWidth: 0 }}
      >
        {member.items_non_compliant} non-compliant
      </Button>
      <Collapse in={open}>
        <Box sx={{ ml: 1, mt: 0.5, p: 1, bgcolor: 'rgba(255,82,82,0.04)', borderRadius: 1, border: '1px solid rgba(255,82,82,0.1)' }}>
          <Typography variant="caption" color="text.disabled">
            Non-compliant item details visible in the export report.
          </Typography>
        </Box>
      </Collapse>
    </Box>
  )
}

// ── Manage assessments dialog ────────────────────────────────────────────────

function ManageAssessmentsDialog({
  open, onClose, collectionId, collectionProductFamily, currentMemberIds,
}: {
  open: boolean
  onClose: () => void
  collectionId: string
  collectionProductFamily: string
  currentMemberIds: Set<string>
}) {
  const { palette } = useTheme()
  const isLight = palette.mode === 'light'
  const qc = useQueryClient()
  const [search, setSearch] = useState('')

  const { data: allAssessments = [] } = useQuery({
    queryKey: ['assessments-for-collection', collectionProductFamily],
    queryFn: () => assessmentsApi.list({ product_family: collectionProductFamily }),
    enabled: open,
  })

  const addMutation = useMutation({
    mutationFn: (assessmentId: string) => collectionsApi.addAssessment(collectionId, assessmentId),
    onSuccess: () => qc.invalidateQueries({ queryKey: ['collection', collectionId] }),
  })

  const removeMutation = useMutation({
    mutationFn: (assessmentId: string) => collectionsApi.removeAssessment(collectionId, assessmentId),
    onSuccess: () => qc.invalidateQueries({ queryKey: ['collection', collectionId] }),
  })

  const filtered = allAssessments.filter(a => {
    if (!search) return true
    const q = search.toLowerCase()
    return (
      a.document_id.toLowerCase().includes(q) ||
      a.workbook_name.toLowerCase().includes(q) ||
      a.group_code.toLowerCase().includes(q)
    )
  })

  return (
    <Dialog open={open} onClose={onClose} maxWidth="sm" fullWidth>
      <DialogTitle>Manage Assessments</DialogTitle>
      <DialogContent sx={{ pt: '8px !important', display: 'flex', flexDirection: 'column', gap: 1.5 }}>
        <TextField
          size="small"
          placeholder="Search assessments…"
          value={search}
          onChange={e => setSearch(e.target.value)}
          fullWidth
        />
        <Box sx={{ maxHeight: 380, overflowY: 'auto', display: 'flex', flexDirection: 'column', gap: 0.5 }}>
          {filtered.map(a => {
            const inCollection = currentMemberIds.has(a.id)
            return (
              <Box
                key={a.id}
                sx={{
                  display: 'flex', alignItems: 'center', gap: 1, p: 1, borderRadius: 1,
                  border: '1px solid',
                  borderColor: inCollection ? 'rgba(68,114,196,0.3)' : (isLight ? 'rgba(0,0,0,0.1)' : 'rgba(255,255,255,0.07)'),
                  bgcolor: inCollection ? 'rgba(68,114,196,0.06)' : 'transparent',
                }}
              >
                <Checkbox
                  size="small"
                  checked={inCollection}
                  onChange={() => {
                    if (inCollection) removeMutation.mutate(a.id)
                    else addMutation.mutate(a.id)
                  }}
                  sx={{ p: 0.25 }}
                />
                <Box sx={{ flex: 1, minWidth: 0 }}>
                  <Typography variant="caption" sx={{ fontFamily: 'monospace', color: 'primary.light', fontSize: '0.7rem' }}>
                    {a.document_id}
                  </Typography>
                  <Typography variant="body2" noWrap sx={{ lineHeight: 1.3 }}>{a.workbook_name}</Typography>
                  <Typography variant="caption" color="text.disabled">{a.group_code.toUpperCase()} — {a.group_name}</Typography>
                </Box>
                <Chip label={a.product_type} size="small" sx={{ fontSize: '0.6rem', height: 16 }} />
              </Box>
            )
          })}
          {filtered.length === 0 && (
            <Typography variant="body2" color="text.secondary" sx={{ py: 2, textAlign: 'center' }}>
              No assessments found.
            </Typography>
          )}
        </Box>
      </DialogContent>
      <DialogActions>
        <Button onClick={onClose} size="small">Done</Button>
      </DialogActions>
    </Dialog>
  )
}

// ── Main page ────────────────────────────────────────────────────────────────

export default function CollectionDetail() {
  const { palette } = useTheme()
  const isLight = palette.mode === 'light'
  const { id } = useParams<{ id: string }>()
  const navigate = useNavigate()
  const qc = useQueryClient()
  const [manageOpen, setManageOpen] = useState(false)
  const [downloading, setDownloading] = useState<string | null>(null)

  const { data: coll, isLoading, error } = useQuery({
    queryKey: ['collection', id],
    queryFn: () => collectionsApi.get(id!),
    enabled: !!id,
  })

  async function handleExport(format: 'csv' | 'xlsx' | 'pdf') {
    if (!id) return
    setDownloading(format)
    try {
      const mimeTypes: Record<string, string> = {
        csv: 'text/csv',
        xlsx: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        pdf: 'application/pdf',
      }
      const resp = await client.get(collectionsApi.exportUrl(id, format), {
        responseType: 'blob',
      })
      const filename = `collection_${(coll?.name ?? 'export').replace(/\s+/g, '_')}.${format}`
      triggerDownload(new Blob([resp.data], { type: mimeTypes[format] }), filename)
    } catch {
      // silently fail; user can retry
    } finally {
      setDownloading(null)
    }
  }

  if (isLoading) {
    return (
      <Box>
        <Skeleton variant="rectangular" height={60} sx={{ borderRadius: 2, mb: 2 }} />
        <Skeleton variant="rectangular" height={120} sx={{ borderRadius: 2, mb: 2 }} />
        <Skeleton variant="rectangular" height={300} sx={{ borderRadius: 2 }} />
      </Box>
    )
  }

  if (error || !coll) {
    return (
      <Box>
        <Button startIcon={<ArrowBackOutlined />} onClick={() => navigate('/assessments')} sx={{ mb: 2 }}>
          Back to Assessments
        </Button>
        <Alert severity="error">Collection not found or failed to load.</Alert>
      </Box>
    )
  }

  const stats = coll.stats
  const statusProps = statusChipProps(stats.status, isLight)
  const memberIds = new Set(coll.members.map(m => m.assessment_id))

  return (
    <Box>
      <PageHeader
        title={coll.name}
        subtitle={`${coll.product_family}${coll.product_type ? ' / ' + coll.product_type : ''} · Assessment Collection`}
        actions={
          <Box sx={{ display: 'flex', gap: 1 }}>
            <Button size="small" variant="outlined" startIcon={<ArrowBackOutlined />}
              onClick={() => navigate('/assessments')} sx={{ fontSize: '0.75rem' }}>
              Back
            </Button>
            <Button size="small" variant="outlined" startIcon={<PersonAddOutlined />}
              onClick={() => setManageOpen(true)} sx={{ fontSize: '0.75rem' }}>
              Manage Assessments
            </Button>
            <Button size="small" variant="outlined" startIcon={<DownloadOutlined />}
              disabled={!!downloading}
              onClick={() => handleExport('csv')} sx={{ fontSize: '0.75rem' }}>
              {downloading === 'csv' ? 'Exporting…' : 'CSV'}
            </Button>
            <Button size="small" variant="outlined" startIcon={<DownloadOutlined />}
              disabled={!!downloading}
              onClick={() => handleExport('xlsx')} sx={{ fontSize: '0.75rem' }}>
              {downloading === 'xlsx' ? 'Exporting…' : 'XLSX'}
            </Button>
            <Button size="small" variant="contained" startIcon={<DownloadOutlined />}
              disabled={!!downloading}
              onClick={() => handleExport('pdf')} sx={{ fontSize: '0.75rem' }}>
              {downloading === 'pdf' ? 'Exporting…' : 'PDF'}
            </Button>
          </Box>
        }
      />

      {/* ── Stats bar ── */}
      <Card sx={{ mb: 2.5, bgcolor: 'rgba(68,114,196,0.04)', border: '1px solid rgba(68,114,196,0.12)' }}>
        <CardContent sx={{ p: '16px !important' }}>
          <Box sx={{ display: 'flex', gap: 4, flexWrap: 'wrap', alignItems: 'center' }}>

            {/* Status */}
            <Box>
              <Typography variant="caption" color="text.disabled" sx={{ display: 'block', mb: 0.5 }}>Status</Typography>
              <Chip label={statusProps.label} size="small"
                sx={{ bgcolor: statusProps.bg, color: statusProps.color, fontWeight: 700, fontSize: '0.72rem' }} />
            </Box>

            {/* Assessments completion */}
            <Box sx={{ flex: 1, minWidth: 180 }}>
              <Box sx={{ display: 'flex', justifyContent: 'space-between', mb: 0.5 }}>
                <Typography variant="caption" color="text.secondary">Completion</Typography>
                <Typography variant="caption" sx={{ color: 'primary.light', fontWeight: 700 }}>
                  {stats.started}/{stats.total} assessments · {stats.completion_pct}%
                </Typography>
              </Box>
              <LinearProgress
                variant="determinate"
                value={Math.min(100, stats.completion_pct)}
                sx={{ height: 6, borderRadius: 3, bgcolor: isLight ? 'rgba(0,0,0,0.08)' : 'rgba(255,255,255,0.06)',
                  '& .MuiLinearProgress-bar': { bgcolor: 'primary.light' } }}
              />
            </Box>

            {/* Compliance score */}
            <Box sx={{ flex: 1, minWidth: 180 }}>
              <Box sx={{ display: 'flex', justifyContent: 'space-between', mb: 0.5 }}>
                <Typography variant="caption" color="text.secondary">Compliance Score</Typography>
                <Typography variant="caption" sx={{ color: scoreColor(stats.compliance_pct), fontWeight: 700 }}>
                  {stats.compliance_pct}%
                </Typography>
              </Box>
              <LinearProgress
                variant="determinate"
                value={Math.min(100, stats.compliance_pct)}
                sx={{ height: 6, borderRadius: 3, bgcolor: isLight ? 'rgba(0,0,0,0.08)' : 'rgba(255,255,255,0.06)',
                  '& .MuiLinearProgress-bar': { bgcolor: scoreColor(stats.compliance_pct) } }}
              />
            </Box>

            {/* Counts */}
            <Box sx={{ display: 'flex', gap: 2 }}>
              <Box sx={{ textAlign: 'center' }}>
                <Typography variant="h6" sx={{ color: '#70AD47', fontWeight: 700, lineHeight: 1 }}>{stats.items_compliant}</Typography>
                <Typography variant="caption" color="text.disabled">Compliant</Typography>
              </Box>
              <Box sx={{ textAlign: 'center' }}>
                <Typography variant="h6" sx={{ color: '#FF5252', fontWeight: 700, lineHeight: 1 }}>{stats.items_non_compliant}</Typography>
                <Typography variant="caption" color="text.disabled">Non-Compliant</Typography>
              </Box>
              <Box sx={{ textAlign: 'center' }}>
                <Typography variant="h6" sx={{ color: 'text.secondary', fontWeight: 700, lineHeight: 1 }}>{stats.items_total}</Typography>
                <Typography variant="caption" color="text.disabled">Total Items</Typography>
              </Box>
            </Box>

            {/* Due date */}
            {coll.due_date && (
              <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.5 }}>
                <CalendarTodayOutlined sx={{ fontSize: 14, color: 'text.disabled' }} />
                <Typography variant="caption" color="text.secondary">Due {coll.due_date}</Typography>
              </Box>
            )}
          </Box>

          {/* Description */}
          {coll.description && (
            <Typography variant="body2" color="text.secondary" sx={{ mt: 1.5, fontStyle: 'italic' }}>
              {coll.description}
            </Typography>
          )}
        </CardContent>
      </Card>

      {/* ── Members table ── */}
      <Box sx={{ mb: 3 }}>
        <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 1.5 }}>
          <Typography variant="subtitle2" fontWeight={700} color="primary.light">
            Assessments
          </Typography>
          <Chip label={coll.members.length} size="small" sx={{ fontSize: '0.65rem', height: 18 }} />
        </Box>

        {coll.members.length === 0 ? (
          <Box
            onClick={() => setManageOpen(true)}
            sx={{
              p: 3, borderRadius: 2, textAlign: 'center', cursor: 'pointer',
              border: '1px dashed rgba(68,114,196,0.3)', bgcolor: 'rgba(68,114,196,0.03)',
              '&:hover': { bgcolor: 'rgba(68,114,196,0.07)', borderColor: 'rgba(68,114,196,0.5)' },
            }}
          >
            <PersonAddOutlined sx={{ color: 'text.disabled', mb: 0.5 }} />
            <Typography variant="body2" color="text.secondary">
              No assessments in this collection yet.
            </Typography>
            <Typography variant="caption" color="primary.light" sx={{ mt: 0.5, display: 'block' }}>
              Click to add assessments
            </Typography>
          </Box>
        ) : (
          <TableContainer component={Card}>
            <Table size="small">
              <TableHead>
                <TableRow>
                  <TableCell sx={{ width: 100 }}>Control Group</TableCell>
                  <TableCell>Workbook</TableCell>
                  <TableCell sx={{ width: 80 }}>Product</TableCell>
                  <TableCell sx={{ width: 60, textAlign: 'right' }}>Items</TableCell>
                  <TableCell sx={{ width: 80, textAlign: 'right' }}>Compliant</TableCell>
                  <TableCell sx={{ width: 100, textAlign: 'right' }}>Non-Compliant</TableCell>
                  <TableCell sx={{ width: 90, textAlign: 'right' }}>Score</TableCell>
                  <TableCell sx={{ width: 44 }} />
                </TableRow>
              </TableHead>
              <TableBody>
                {coll.members.map((m: CollectionMember) => (
                  <TableRow key={m.assessment_id} hover>
                    <TableCell>
                      <Typography variant="caption" sx={{ fontFamily: 'monospace', color: 'primary.light', fontWeight: 700 }}>
                        {m.group_code}
                      </Typography>
                      <Typography variant="caption" color="text.disabled" sx={{ display: 'block', fontSize: '0.62rem' }}>
                        {m.group_name}
                      </Typography>
                    </TableCell>
                    <TableCell>
                      <Typography variant="caption" sx={{ fontFamily: 'monospace', color: 'text.disabled', fontSize: '0.68rem' }}>
                        {m.document_id}
                      </Typography>
                      <Typography variant="body2" fontWeight={600} sx={{ lineHeight: 1.3 }}>{m.workbook_name}</Typography>
                      <NcItems member={m} />
                    </TableCell>
                    <TableCell>
                      <Chip label={m.product_type} size="small" sx={{ fontSize: '0.6rem', height: 16 }} />
                    </TableCell>
                    <TableCell align="right">
                      <Typography variant="caption">{m.items_total}</Typography>
                    </TableCell>
                    <TableCell align="right">
                      <Typography variant="caption" sx={{ color: m.items_compliant > 0 ? '#70AD47' : 'text.disabled' }}>
                        {m.items_compliant}
                      </Typography>
                    </TableCell>
                    <TableCell align="right">
                      <Typography variant="caption" sx={{ color: m.items_non_compliant > 0 ? '#FF5252' : 'text.disabled' }}>
                        {m.items_non_compliant}
                      </Typography>
                    </TableCell>
                    <TableCell align="right">
                      {m.items_total > 0 ? (
                        <Typography variant="caption" sx={{ color: scoreColor(m.compliance_pct), fontWeight: 700 }}>
                          {m.compliance_pct}%
                        </Typography>
                      ) : (
                        <Typography variant="caption" color="text.disabled">—</Typography>
                      )}
                    </TableCell>
                    <TableCell>
                      <Tooltip title="Remove from collection">
                        <IconButton
                          size="small"
                          onClick={() => {
                            collectionsApi.removeAssessment(coll.id, m.assessment_id)
                              .then(() => qc.invalidateQueries({ queryKey: ['collection', id] }))
                          }}
                          sx={{ color: 'error.main', opacity: 0.4, '&:hover': { opacity: 1 } }}
                        >
                          <PersonRemoveOutlined sx={{ fontSize: 15 }} />
                        </IconButton>
                      </Tooltip>
                    </TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </TableContainer>
        )}
      </Box>

      {/* ── Manage dialog ── */}
      {manageOpen && (
        <ManageAssessmentsDialog
          open={manageOpen}
          onClose={() => {
            setManageOpen(false)
            qc.invalidateQueries({ queryKey: ['collection', id] })
          }}
          collectionId={coll.id}
          collectionProductFamily={coll.product_family}
          currentMemberIds={memberIds}
        />
      )}
    </Box>
  )
}
