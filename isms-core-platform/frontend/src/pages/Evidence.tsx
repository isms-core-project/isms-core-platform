import { useState, useRef } from 'react'
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
  FormControl,
  IconButton,
  InputLabel,
  LinearProgress,
  MenuItem,
  Select,
  Skeleton,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  TextField,
  ToggleButton,
  ToggleButtonGroup,
  Tooltip,
  Typography,
} from '@mui/material'
import {
  AssignmentOutlined,
  CheckCircleOutlineOutlined,
  CheckOutlined,
  CloseOutlined,
  DeleteOutlined,
  DownloadOutlined,
  ErrorOutlineOutlined,
  FileUploadOutlined,
  LinkOutlined,
  SendOutlined,
  UploadFileOutlined,
  VerifiedOutlined,
  WarningAmberOutlined,
} from '@mui/icons-material'
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import dayjs from 'dayjs'
import { evidenceApi } from '../api/evidence'
import { assessmentsApi } from '../api/assessmentsApi'
import PageHeader from '../components/PageHeader'
import MetricCard from '../components/MetricCard'
import StatusChip from '../components/StatusChip'
import { useProduct } from '../store/ProductContext'

const EVIDENCE_TYPES = [
  'document',
  'screenshot',
  'log_extract',
  'config_export',
  'test_result',
  'attestation',
]

const STATUS_COLORS: Record<string, { bg: string; color: string; label: string }> = {
  draft:          { bg: '#1e1e2e', color: '#aaa',    label: 'Draft' },
  pending_review: { bg: '#3a2e00', color: '#FFEB9C', label: 'Pending Review' },
  active:         { bg: '#1a2a3a', color: '#9fc8f0', label: 'Active' },
  approved:       { bg: '#1a3a27', color: '#C6EFCE', label: 'Approved' },
  rejected:       { bg: '#3a0000', color: '#FFC7CE', label: 'Rejected' },
}

type FilterTab = 'all' | 'valid' | 'expiring' | 'expired' | 'unverified'

// ── Single-file upload dialog ─────────────────────────────────────────────────
function UploadDialog({
  open,
  onClose,
  onSuccess,
  activeProduct,
}: {
  open: boolean
  onClose: () => void
  onSuccess: () => void
  activeProduct: string
}) {
  const isIsms = activeProduct === 'isms'

  // Product type options depend on the active ISO product
  const PRODUCT_OPTIONS: { value: string; label: string }[] = isIsms
    ? [{ value: 'framework', label: 'Framework' }, { value: 'operational', label: 'Operational' }]
    : [{ value: activeProduct, label: activeProduct === 'privacy' ? 'Privacy' : 'Cloud' }]

  const [file, setFile] = useState<File | null>(null)
  const [title, setTitle] = useState('')
  const [evidenceType, setEvidenceType] = useState('document')
  const [productType, setProductType] = useState<string>(PRODUCT_OPTIONS[0].value)
  const [groupCode, setGroupCode] = useState('')
  const [workbookId, setWorkbookId] = useState('')
  const [notes, setNotes] = useState('')
  const [error, setError] = useState<string | null>(null)

  // Reset product type when active product changes
  const defaultPt = PRODUCT_OPTIONS[0].value
  if (productType !== 'framework' && productType !== 'operational' && productType !== activeProduct) {
    setProductType(defaultPt)
  }

  const showWorkbookPicker = productType === 'framework' && groupCode.trim().length > 2
  const { data: generators = [] } = useQuery({
    queryKey: ['generators-for-group', groupCode.trim().toLowerCase()],
    queryFn: () => assessmentsApi.getGeneratorsForGroup(groupCode.trim().toLowerCase()),
    enabled: showWorkbookPicker,
  })
  const fileRef = useRef<HTMLInputElement>(null)

  const mutation = useMutation({
    mutationFn: (fd: FormData) => evidenceApi.upload(fd),
    onSuccess: () => {
      onSuccess()
      onClose()
      setFile(null); setTitle(''); setGroupCode(''); setWorkbookId(''); setNotes(''); setError(null)
    },
    onError: (err: unknown) => {
      const msg = (err as { response?: { data?: { detail?: string } } })?.response?.data?.detail ?? 'Upload failed'
      setError(String(msg))
    },
  })

  function handleSubmit() {
    if (!file || !title || !groupCode) return
    const fd = new FormData()
    fd.append('file', file)
    fd.append('title', title)
    fd.append('evidence_type', evidenceType)
    fd.append('group_code', groupCode.toLowerCase())
    const notesWithWorkbook = [workbookId ? `Workbook: ${workbookId}` : '', notes].filter(Boolean).join('\n')
    if (notesWithWorkbook) fd.append('notes', notesWithWorkbook)
    mutation.mutate(fd)
  }

  return (
    <Dialog open={open} onClose={onClose} maxWidth="sm" fullWidth>
      <DialogTitle>Upload Evidence</DialogTitle>
      <DialogContent sx={{ pt: 1 }}>
        {error && <Alert severity="error" sx={{ mb: 2 }}>{error}</Alert>}
        <Box
          sx={{ border: '2px dashed', borderColor: file ? 'success.main' : 'divider', borderRadius: 2, p: 3, textAlign: 'center', cursor: 'pointer', mb: 2, '&:hover': { borderColor: 'primary.main', bgcolor: 'rgba(68,114,196,0.05)' } }}
          onClick={() => fileRef.current?.click()}
        >
          <input ref={fileRef} type="file" hidden accept=".docx,.pdf,.xlsx,.png,.jpg,.jpeg,.txt,.md,.csv,.json"
            onChange={(e) => { const f = e.target.files?.[0]; if (f) { setFile(f); if (!title) setTitle(f.name.replace(/\.[^.]+$/, '')) } }} />
          <UploadFileOutlined sx={{ fontSize: 40, color: file ? 'success.main' : 'text.secondary', mb: 1 }} />
          <Typography variant="body2">{file ? file.name : 'Click to select a file'}</Typography>
          <Typography variant="caption" color="text.secondary">.docx .pdf .xlsx .png .jpg .txt .csv .json · max 50 MB</Typography>
        </Box>
        <TextField fullWidth label="Title" value={title} onChange={(e) => setTitle(e.target.value)} size="small" sx={{ mb: 2 }} required />
        <FormControl fullWidth size="small" sx={{ mb: 2 }}>
          <InputLabel>Product</InputLabel>
          <Select value={productType} onChange={(e) => { setProductType(e.target.value); setWorkbookId('') }} label="Product">
            {PRODUCT_OPTIONS.map((opt) => (
              <MenuItem key={opt.value} value={opt.value}>{opt.label}</MenuItem>
            ))}
          </Select>
        </FormControl>
        <TextField fullWidth label="Control Group Code" value={groupCode} onChange={(e) => { setGroupCode(e.target.value); setWorkbookId('') }} size="small" placeholder="e.g. a.5.1-2" sx={{ mb: 2 }} required />
        {showWorkbookPicker && generators.length > 1 && (
          <FormControl fullWidth size="small" sx={{ mb: 2 }}>
            <InputLabel>Workbook / IMP (optional)</InputLabel>
            <Select value={workbookId} onChange={(e) => setWorkbookId(e.target.value)} label="Workbook / IMP (optional)">
              <MenuItem value="">Any</MenuItem>
              {generators.map((g) => (
                <MenuItem key={g.document_id} value={g.document_id}>
                  <Typography variant="caption" sx={{ fontFamily: 'monospace', color: 'primary.light', mr: 1 }}>{g.document_id}</Typography>
                  {g.workbook_name}
                </MenuItem>
              ))}
            </Select>
          </FormControl>
        )}
        <FormControl fullWidth size="small" sx={{ mb: 2 }}>
          <InputLabel>Evidence Type</InputLabel>
          <Select value={evidenceType} onChange={(e) => setEvidenceType(e.target.value)} label="Evidence Type">
            {EVIDENCE_TYPES.map((t) => <MenuItem key={t} value={t}>{t.replace(/_/g, ' ')}</MenuItem>)}
          </Select>
        </FormControl>
        <TextField fullWidth label="Notes" value={notes} onChange={(e) => setNotes(e.target.value)} size="small" multiline rows={2} />
      </DialogContent>
      <DialogActions sx={{ px: 3, pb: 2 }}>
        <Button onClick={onClose}>Cancel</Button>
        <Button variant="contained" onClick={handleSubmit} disabled={!file || !title || !groupCode || mutation.isPending}>
          {mutation.isPending ? 'Uploading...' : 'Upload'}
        </Button>
      </DialogActions>
    </Dialog>
  )
}

// ── Bulk draft upload dialog ──────────────────────────────────────────────────
type BulkFileStatus = 'queued' | 'uploading' | 'done' | 'error'

interface BulkFile {
  file: File
  status: BulkFileStatus
  error?: string
}

function BulkUploadDialog({
  open,
  onClose,
  onSuccess,
}: {
  open: boolean
  onClose: () => void
  onSuccess: () => void
}) {
  const [files, setFiles] = useState<BulkFile[]>([])
  const [evidenceType, setEvidenceType] = useState('document')
  const [notes, setNotes] = useState('')
  const [uploading, setUploading] = useState(false)
  const [done, setDone] = useState(false)
  const fileRef = useRef<HTMLInputElement>(null)

  const doneCount = files.filter((f) => f.status === 'done').length
  const errorCount = files.filter((f) => f.status === 'error').length
  const progress = files.length > 0 ? Math.round((doneCount + errorCount) / files.length * 100) : 0

  function addFiles(selected: FileList | null) {
    if (!selected) return
    const next: BulkFile[] = Array.from(selected).map((f) => ({ file: f, status: 'queued' }))
    setFiles((prev) => [...prev, ...next])
  }

  function removeFile(idx: number) {
    setFiles((prev) => prev.filter((_, i) => i !== idx))
  }

  async function handleUpload() {
    if (files.length === 0 || uploading) return
    setUploading(true)

    // Upload in batches of 10 via a single multipart request per batch
    const BATCH = 10
    const updated = [...files]

    for (let i = 0; i < updated.length; i += BATCH) {
      const batch = updated.slice(i, i + BATCH)
      const fd = new FormData()
      batch.forEach((bf) => fd.append('files', bf.file))
      fd.append('evidence_type', evidenceType)
      if (notes) fd.append('notes', notes)

      // mark batch as uploading
      batch.forEach((_, j) => { updated[i + j] = { ...updated[i + j], status: 'uploading' } })
      setFiles([...updated])

      try {
        await evidenceApi.bulkDraft(fd)
        batch.forEach((_, j) => { updated[i + j] = { ...updated[i + j], status: 'done' } })
      } catch {
        batch.forEach((_, j) => { updated[i + j] = { ...updated[i + j], status: 'error', error: 'Upload failed' } })
      }
      setFiles([...updated])
    }

    setUploading(false)
    setDone(true)
    onSuccess()
  }

  function handleClose() {
    setFiles([])
    setEvidenceType('document')
    setNotes('')
    setUploading(false)
    setDone(false)
    onClose()
  }

  return (
    <Dialog open={open} onClose={handleClose} maxWidth="sm" fullWidth>
      <DialogTitle sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
        <FileUploadOutlined fontSize="small" />
        Bulk Upload (Draft)
      </DialogTitle>
      <DialogContent sx={{ pt: 1 }}>
        <Alert severity="info" sx={{ mb: 2, fontSize: '0.78rem' }}>
          Files are stored as <strong>drafts</strong> without a control group. Assign them individually after upload.
        </Alert>

        {!uploading && !done && (
          <Box
            sx={{ border: '2px dashed', borderColor: files.length ? 'primary.main' : 'divider', borderRadius: 2, p: 3, textAlign: 'center', cursor: 'pointer', mb: 2, '&:hover': { bgcolor: 'rgba(68,114,196,0.05)' } }}
            onClick={() => fileRef.current?.click()}
            onDragOver={(e) => e.preventDefault()}
            onDrop={(e) => { e.preventDefault(); addFiles(e.dataTransfer.files) }}
          >
            <input ref={fileRef} type="file" hidden multiple accept=".docx,.pdf,.xlsx,.png,.jpg,.jpeg,.txt,.md,.csv,.json"
              onChange={(e) => addFiles(e.target.files)} />
            <FileUploadOutlined sx={{ fontSize: 40, color: 'text.secondary', mb: 1 }} />
            <Typography variant="body2">Click or drag &amp; drop files here</Typography>
            <Typography variant="caption" color="text.secondary">.docx .pdf .xlsx .png .jpg .txt .csv .json · max 50 MB each · up to 50 files</Typography>
          </Box>
        )}

        {files.length > 0 && (
          <Box sx={{ maxHeight: 220, overflowY: 'auto', mb: 2 }}>
            {files.map((bf, idx) => (
              <Box key={idx} sx={{ display: 'flex', alignItems: 'center', gap: 1, py: 0.5, borderBottom: '1px solid', borderColor: 'divider' }}>
                <Box sx={{ flex: 1, minWidth: 0 }}>
                  <Typography variant="caption" noWrap>{bf.file.name}</Typography>
                  <Typography variant="caption" color="text.secondary" sx={{ ml: 1 }}>
                    {(bf.file.size / 1024).toFixed(0)} KB
                  </Typography>
                </Box>
                {bf.status === 'queued' && <Chip label="queued" size="small" sx={{ height: 16, fontSize: '0.6rem' }} />}
                {bf.status === 'uploading' && <Chip label="uploading…" size="small" color="info" sx={{ height: 16, fontSize: '0.6rem' }} />}
                {bf.status === 'done' && <CheckOutlined sx={{ fontSize: 16, color: '#C6EFCE' }} />}
                {bf.status === 'error' && (
                  <Tooltip title={bf.error ?? 'error'}>
                    <ErrorOutlineOutlined sx={{ fontSize: 16, color: '#FFC7CE' }} />
                  </Tooltip>
                )}
                {!uploading && bf.status === 'queued' && (
                  <IconButton size="small" onClick={() => removeFile(idx)}>
                    <CloseOutlined sx={{ fontSize: 14 }} />
                  </IconButton>
                )}
              </Box>
            ))}
          </Box>
        )}

        {uploading && (
          <Box sx={{ mb: 2 }}>
            <LinearProgress variant="determinate" value={progress} sx={{ mb: 0.5 }} />
            <Typography variant="caption" color="text.secondary">{doneCount + errorCount} / {files.length} files processed</Typography>
          </Box>
        )}

        {done && (
          <Alert severity={errorCount > 0 ? 'warning' : 'success'} sx={{ mb: 2 }}>
            {doneCount} file{doneCount !== 1 ? 's' : ''} uploaded as drafts.
            {errorCount > 0 && ` ${errorCount} failed.`}
          </Alert>
        )}

        {!uploading && !done && (
          <>
            <FormControl fullWidth size="small" sx={{ mb: 2 }}>
              <InputLabel>Evidence Type</InputLabel>
              <Select value={evidenceType} onChange={(e) => setEvidenceType(e.target.value)} label="Evidence Type">
                {EVIDENCE_TYPES.map((t) => <MenuItem key={t} value={t}>{t.replace(/_/g, ' ')}</MenuItem>)}
              </Select>
            </FormControl>
            <TextField fullWidth label="Notes (shared)" value={notes} onChange={(e) => setNotes(e.target.value)} size="small" multiline rows={2} />
          </>
        )}
      </DialogContent>
      <DialogActions sx={{ px: 3, pb: 2 }}>
        <Button onClick={handleClose}>{done ? 'Close' : 'Cancel'}</Button>
        {!done && (
          <Button variant="contained" startIcon={<FileUploadOutlined />} onClick={handleUpload} disabled={files.length === 0 || uploading}>
            {uploading ? `Uploading… (${progress}%)` : `Upload ${files.length > 0 ? `${files.length} ` : ''}Files`}
          </Button>
        )}
      </DialogActions>
    </Dialog>
  )
}

// ── Assign draft dialog ───────────────────────────────────────────────────────
function AssignDialog({
  evidence,
  open,
  onClose,
}: {
  evidence: { id: string; title: string }
  open: boolean
  onClose: () => void
}) {
  const [groupCode, setGroupCode] = useState('')
  const [requireApproval, setRequireApproval] = useState(false)
  const [error, setError] = useState('')
  const qc = useQueryClient()

  const mutation = useMutation({
    mutationFn: () => evidenceApi.assign(evidence.id, { group_code: groupCode.toLowerCase().trim(), require_approval: requireApproval }),
    onSuccess: () => {
      qc.invalidateQueries({ queryKey: ['evidence'] })
      setGroupCode(''); setError(''); onClose()
    },
    onError: (err: unknown) => {
      const msg = (err as { response?: { data?: { detail?: string } } })?.response?.data?.detail ?? 'Assignment failed'
      setError(String(msg))
    },
  })

  return (
    <Dialog open={open} onClose={onClose} maxWidth="xs" fullWidth>
      <DialogTitle>Assign to Control Group</DialogTitle>
      <DialogContent sx={{ pt: 1 }}>
        <Typography variant="body2" color="text.secondary" sx={{ mb: 2 }}>
          {evidence.title}
        </Typography>
        {error && <Alert severity="error" sx={{ mb: 2 }}>{error}</Alert>}
        <TextField
          fullWidth autoFocus label="Control Group Code" value={groupCode}
          onChange={(e) => setGroupCode(e.target.value)} size="small" placeholder="e.g. a.8.8" sx={{ mb: 2 }}
        />
        <FormControl fullWidth size="small">
          <InputLabel>After Assignment</InputLabel>
          <Select value={requireApproval ? 'review' : 'active'} onChange={(e) => setRequireApproval(e.target.value === 'review')} label="After Assignment">
            <MenuItem value="active">Set Active (no approval needed)</MenuItem>
            <MenuItem value="review">Submit for Review (require approval)</MenuItem>
          </Select>
        </FormControl>
      </DialogContent>
      <DialogActions sx={{ px: 3, pb: 2 }}>
        <Button onClick={onClose}>Cancel</Button>
        <Button variant="contained" onClick={() => mutation.mutate()} disabled={!groupCode.trim() || mutation.isPending}>
          Assign
        </Button>
      </DialogActions>
    </Dialog>
  )
}

// ── Reject dialog ─────────────────────────────────────────────────────────────
function RejectDialog({
  evidenceId,
  open,
  onClose,
}: {
  evidenceId: string
  open: boolean
  onClose: () => void
}) {
  const [reason, setReason] = useState('')
  const qc = useQueryClient()

  const mutation = useMutation({
    mutationFn: () => evidenceApi.reject(evidenceId, { reason: reason || undefined }),
    onSuccess: () => { qc.invalidateQueries({ queryKey: ['evidence'] }); setReason(''); onClose() },
  })

  return (
    <Dialog open={open} onClose={onClose} maxWidth="xs" fullWidth>
      <DialogTitle>Reject Evidence</DialogTitle>
      <DialogContent sx={{ pt: 1 }}>
        <TextField fullWidth autoFocus label="Reason (optional)" value={reason} onChange={(e) => setReason(e.target.value)} size="small" multiline rows={3} />
      </DialogContent>
      <DialogActions sx={{ px: 3, pb: 2 }}>
        <Button onClick={onClose}>Cancel</Button>
        <Button variant="contained" color="error" onClick={() => mutation.mutate()} disabled={mutation.isPending}>
          Reject
        </Button>
      </DialogActions>
    </Dialog>
  )
}

// ── Status chip ───────────────────────────────────────────────────────────────
function EvidenceStatusChip({ status }: { status: string }) {
  const cfg = STATUS_COLORS[status] ?? STATUS_COLORS.active
  return (
    <Chip
      label={cfg.label}
      size="small"
      sx={{ height: 18, fontSize: '0.62rem', bgcolor: cfg.bg, color: cfg.color, fontWeight: 600 }}
    />
  )
}

// ── Main page ─────────────────────────────────────────────────────────────────
export default function Evidence() {
  const { product: activeProduct } = useProduct()
  const [uploadOpen, setUploadOpen] = useState(false)
  const [bulkOpen, setBulkOpen] = useState(false)
  const [filterTab, setFilterTab] = useState<FilterTab>('all')
  const [typeFilter, setTypeFilter] = useState<string>('all')
  const [statusFilter, setStatusFilter] = useState<string>('all')
  const [assignTarget, setAssignTarget] = useState<{ id: string; title: string } | null>(null)
  const [rejectTarget, setRejectTarget] = useState<string | null>(null)
  const queryClient = useQueryClient()

  const { data, isLoading, error } = useQuery({
    queryKey: ['evidence'],
    queryFn: () => evidenceApi.list({ limit: 500 }),
  })

  const deleteMutation = useMutation({
    mutationFn: evidenceApi.delete,
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ['evidence'] }),
  })

  const submitMutation = useMutation({
    mutationFn: (id: string) => evidenceApi.submit(id),
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ['evidence'] }),
  })

  const approveMutation = useMutation({
    mutationFn: (id: string) => evidenceApi.approve(id),
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ['evidence'] }),
  })

  function formatBytes(bytes: number) {
    if (bytes < 1024) return `${bytes} B`
    if (bytes < 1024 * 1024) return `${(bytes / 1024).toFixed(1)} KB`
    return `${(bytes / 1024 / 1024).toFixed(1)} MB`
  }

  const now = dayjs()
  const items = data ?? []
  const expired = items.filter((ev) => ev.expires_date && dayjs(ev.expires_date).isBefore(now))
  const expiringSoon = items.filter((ev) => ev.expires_date && !dayjs(ev.expires_date).isBefore(now) && dayjs(ev.expires_date).isBefore(now.add(30, 'day')))
  const verified = items.filter((ev) => ev.verified_by)
  const unverified = items.filter((ev) => !ev.verified_by)
  const drafts = items.filter((ev) => ev.evidence_status === 'draft')
  const pending = items.filter((ev) => ev.evidence_status === 'pending_review')

  const byTab = items.filter((ev) => {
    if (filterTab === 'valid') return !ev.expires_date || !dayjs(ev.expires_date).isBefore(now)
    if (filterTab === 'expiring') return expiringSoon.includes(ev)
    if (filterTab === 'expired') return expired.includes(ev)
    if (filterTab === 'unverified') return !ev.verified_by
    return true
  })
  const byType = typeFilter === 'all' ? byTab : byTab.filter((ev) => ev.evidence_type === typeFilter)
  const filtered = statusFilter === 'all' ? byType : byType.filter((ev) => ev.evidence_status === statusFilter)

  const invalidate = () => queryClient.invalidateQueries({ queryKey: ['evidence'] })

  return (
    <Box>
      <PageHeader
        title="Evidence Tracker"
        subtitle={`${items.length} items · ${drafts.length} drafts · ${pending.length} pending review`}
        actions={
          <Box sx={{ display: 'flex', gap: 1 }}>
            <Button variant="outlined" size="small" startIcon={<FileUploadOutlined />} onClick={() => setBulkOpen(true)}>
              Bulk Upload
            </Button>
            <Button variant="contained" size="small" startIcon={<UploadFileOutlined />} onClick={() => setUploadOpen(true)}>
              Upload Evidence
            </Button>
          </Box>
        }
      />

      <UploadDialog open={uploadOpen} onClose={() => setUploadOpen(false)} onSuccess={invalidate} activeProduct={activeProduct} />
      <BulkUploadDialog open={bulkOpen} onClose={() => setBulkOpen(false)} onSuccess={invalidate} />
      {assignTarget && (
        <AssignDialog evidence={assignTarget} open onClose={() => setAssignTarget(null)} />
      )}
      {rejectTarget && (
        <RejectDialog evidenceId={rejectTarget} open onClose={() => setRejectTarget(null)} />
      )}

      {/* Metrics */}
      <Box sx={{ display: 'flex', gap: 2, mb: 2 }}>
        <Box sx={{ flex: 1 }}>
          <MetricCard title="Total" value={isLoading ? '—' : items.length} icon={<AssignmentOutlined fontSize="small" />} />
        </Box>
        <Box sx={{ flex: 1 }}>
          <MetricCard title="Drafts" value={isLoading ? '—' : drafts.length}
            sx={drafts.length > 0 ? { borderColor: '#555', '& h3': { color: '#aaa' } } : {}} />
        </Box>
        <Box sx={{ flex: 1 }}>
          <MetricCard title="Pending Review" value={isLoading ? '—' : pending.length}
            sx={pending.length > 0 ? { borderColor: '#FF9800', '& h3': { color: '#FFEB9C' } } : {}} />
        </Box>
        <Box sx={{ flex: 1 }}>
          <MetricCard title="Expired" value={isLoading ? '—' : expired.length}
            icon={<ErrorOutlineOutlined fontSize="small" />}
            sx={expired.length > 0 ? { borderColor: '#C00000', '& h3': { color: '#C00000' } } : {}} />
        </Box>
        <Box sx={{ flex: 1 }}>
          <MetricCard title="Expiring ≤ 30d" value={isLoading ? '—' : expiringSoon.length}
            icon={<WarningAmberOutlined fontSize="small" />}
            sx={expiringSoon.length > 0 ? { borderColor: '#FF9800', '& h3': { color: '#FF9800' } } : {}} />
        </Box>
        <Box sx={{ flex: 1 }}>
          <MetricCard title="Verified" value={isLoading ? '—' : verified.length}
            subtitle={items.length ? `${Math.round((verified.length / items.length) * 100)}% of total` : undefined}
            icon={<CheckCircleOutlineOutlined fontSize="small" />}
            progress={items.length ? (verified.length / items.length) * 100 : 0}
            progressColor="success"
            sx={verified.length > 0 ? { '& h3': { color: '#C6EFCE' } } : {}} />
        </Box>
      </Box>

      {/* Expiry alert banner */}
      {(expired.length > 0 || expiringSoon.length > 0) && (
        <Alert severity={expired.length ? 'error' : 'warning'} sx={{ mb: 2 }}>
          {expired.length > 0 && `${expired.length} evidence item${expired.length > 1 ? 's have' : ' has'} expired. `}
          {expiringSoon.length > 0 && `${expiringSoon.length} item${expiringSoon.length > 1 ? 's are' : ' is'} expiring within 30 days.`}
          {' '}Review expiry dates in the table below.
        </Alert>
      )}

      {drafts.length > 0 && (
        <Alert severity="warning" sx={{ mb: 2 }}>
          {drafts.length} evidence item{drafts.length > 1 ? 's are' : ' is'} in draft status — assign them to a control group to activate.
        </Alert>
      )}

      {error && <Alert severity="error">Failed to load evidence.</Alert>}

      {items.length === 0 && !isLoading && (
        <Alert severity="info">No evidence uploaded yet. Use the Upload or Bulk Upload button to add evidence files.</Alert>
      )}

      {/* Filters */}
      {items.length > 0 && (
        <Card sx={{ mb: 2 }}>
          <CardContent sx={{ pb: '12px !important' }}>
            <Box sx={{ display: 'flex', gap: 2, flexWrap: 'wrap', alignItems: 'center' }}>
              <ToggleButtonGroup value={filterTab} exclusive onChange={(_, v) => { if (v) setFilterTab(v) }} size="small">
                <ToggleButton value="all">All ({items.length})</ToggleButton>
                <ToggleButton value="valid">Valid</ToggleButton>
                <ToggleButton value="expiring" sx={expiringSoon.length > 0 ? { color: '#FF9800 !important' } : {}}>Expiring ({expiringSoon.length})</ToggleButton>
                <ToggleButton value="expired" sx={expired.length > 0 ? { color: '#C00000 !important' } : {}}>Expired ({expired.length})</ToggleButton>
                <ToggleButton value="unverified">Unverified ({unverified.length})</ToggleButton>
              </ToggleButtonGroup>

              <FormControl size="small" sx={{ minWidth: 140 }}>
                <InputLabel>Status</InputLabel>
                <Select value={statusFilter} onChange={(e) => setStatusFilter(e.target.value)} label="Status">
                  <MenuItem value="all">All statuses</MenuItem>
                  <MenuItem value="draft">Draft</MenuItem>
                  <MenuItem value="pending_review">Pending Review</MenuItem>
                  <MenuItem value="active">Active</MenuItem>
                  <MenuItem value="approved">Approved</MenuItem>
                  <MenuItem value="rejected">Rejected</MenuItem>
                </Select>
              </FormControl>

              <FormControl size="small" sx={{ minWidth: 140 }}>
                <InputLabel>Type</InputLabel>
                <Select value={typeFilter} onChange={(e) => setTypeFilter(e.target.value)} label="Type">
                  <MenuItem value="all">All types</MenuItem>
                  {EVIDENCE_TYPES.map((t) => <MenuItem key={t} value={t}>{t.replace(/_/g, ' ')}</MenuItem>)}
                </Select>
              </FormControl>
            </Box>
          </CardContent>
        </Card>
      )}

      {/* Table */}
      {filtered.length > 0 && (
        <TableContainer component={Card}>
          <Table size="small">
            <TableHead>
              <TableRow>
                <TableCell>Title / Status</TableCell>
                <TableCell>Type</TableCell>
                <TableCell>File</TableCell>
                <TableCell>Control Group</TableCell>
                <TableCell>Collected</TableCell>
                <TableCell>Expires</TableCell>
                <TableCell>Verified</TableCell>
                <TableCell>Uploaded</TableCell>
                <TableCell align="right">Actions</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {isLoading && [...Array(5)].map((_, i) => (
                <TableRow key={i}>
                  {[...Array(9)].map((_, j) => <TableCell key={j}><Skeleton variant="text" /></TableCell>)}
                </TableRow>
              ))}
              {filtered.map((ev) => (
                <TableRow key={ev.id} hover sx={ev.evidence_status === 'draft' ? { opacity: 0.75 } : {}}>
                  <TableCell>
                    <Typography variant="body2" fontWeight={600}>{ev.title}</Typography>
                    <Box sx={{ display: 'flex', gap: 0.5, mt: 0.25, flexWrap: 'wrap' }}>
                      <EvidenceStatusChip status={ev.evidence_status} />
                      {ev.metadata.notes && (
                        <Typography variant="caption" color="text.secondary">{ev.metadata.notes.slice(0, 60)}</Typography>
                      )}
                    </Box>
                    {ev.evidence_status === 'rejected' && ev.metadata.rejection_reason && (
                      <Typography variant="caption" sx={{ color: '#FFC7CE', display: 'block', mt: 0.25 }}>
                        Reason: {ev.metadata.rejection_reason}
                      </Typography>
                    )}
                  </TableCell>
                  <TableCell>
                    <Chip label={ev.evidence_type} size="small" sx={{ fontSize: '0.65rem', height: 18 }} />
                  </TableCell>
                  <TableCell>
                    <Typography variant="caption" sx={{ fontFamily: 'monospace' }}>{ev.metadata.original_filename}</Typography>
                    <br />
                    <Typography variant="caption" color="text.secondary">{formatBytes(ev.metadata.file_size)}</Typography>
                  </TableCell>
                  <TableCell>
                    <Typography variant="caption" color={ev.control_group_id ? 'text.primary' : 'text.disabled'}>
                      {ev.control_group_id ? '—' : 'Unassigned'}
                    </Typography>
                  </TableCell>
                  <TableCell>
                    <Typography variant="caption" color="text.secondary">{ev.collected_date ?? '—'}</Typography>
                  </TableCell>
                  <TableCell>
                    {ev.expires_date ? (
                      <StatusChip
                        status={dayjs(ev.expires_date).isBefore(dayjs()) ? 'red' : dayjs(ev.expires_date).isBefore(dayjs().add(30, 'day')) ? 'amber' : 'green'}
                        label={ev.expires_date}
                      />
                    ) : (
                      <Typography variant="caption" color="text.secondary">—</Typography>
                    )}
                  </TableCell>
                  <TableCell>
                    {ev.verified_by ? (
                      <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.5 }}>
                        <VerifiedOutlined sx={{ fontSize: 14, color: '#C6EFCE' }} />
                        <Typography variant="caption" color="text.secondary">{ev.verified_by}</Typography>
                      </Box>
                    ) : (
                      <Typography variant="caption" color="text.disabled">—</Typography>
                    )}
                  </TableCell>
                  <TableCell>
                    <Typography variant="caption" color="text.secondary">
                      {dayjs(ev.created_at).format('DD MMM YYYY')}
                    </Typography>
                  </TableCell>
                  <TableCell align="right" sx={{ whiteSpace: 'nowrap' }}>
                    {/* Draft actions */}
                    {ev.evidence_status === 'draft' && (
                      <Tooltip title="Assign to control group">
                        <IconButton size="small" color="primary" onClick={() => setAssignTarget({ id: ev.id, title: ev.title })}>
                          <LinkOutlined fontSize="small" />
                        </IconButton>
                      </Tooltip>
                    )}
                    {/* Active / Rejected: submit for review */}
                    {(ev.evidence_status === 'active' || ev.evidence_status === 'rejected') && (
                      <Tooltip title="Submit for review">
                        <IconButton size="small" onClick={() => submitMutation.mutate(ev.id)} disabled={submitMutation.isPending}>
                          <SendOutlined fontSize="small" />
                        </IconButton>
                      </Tooltip>
                    )}
                    {/* Pending review: approve + reject */}
                    {ev.evidence_status === 'pending_review' && (
                      <>
                        <Tooltip title="Approve">
                          <IconButton size="small" sx={{ color: '#C6EFCE' }} onClick={() => approveMutation.mutate(ev.id)} disabled={approveMutation.isPending}>
                            <CheckOutlined fontSize="small" />
                          </IconButton>
                        </Tooltip>
                        <Tooltip title="Reject">
                          <IconButton size="small" sx={{ color: '#FFC7CE' }} onClick={() => setRejectTarget(ev.id)}>
                            <CloseOutlined fontSize="small" />
                          </IconButton>
                        </Tooltip>
                      </>
                    )}
                    {/* Download */}
                    <Tooltip title="Download">
                      <IconButton size="small" component="a" href={evidenceApi.downloadUrl(ev.id)} download>
                        <DownloadOutlined fontSize="small" />
                      </IconButton>
                    </Tooltip>
                    {/* Delete */}
                    <Tooltip title="Delete">
                      <IconButton size="small" onClick={() => deleteMutation.mutate(ev.id)} sx={{ color: 'error.main' }}>
                        <DeleteOutlined fontSize="small" />
                      </IconButton>
                    </Tooltip>
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      )}

      {filtered.length === 0 && items.length > 0 && !isLoading && (
        <Alert severity="info">No evidence matches the current filter.</Alert>
      )}
    </Box>
  )
}
