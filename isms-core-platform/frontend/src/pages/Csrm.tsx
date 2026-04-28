import { useState, useEffect } from 'react'
import { useTheme } from '@mui/material/styles'
import {
  Alert, AlertTitle, Box, Button, Card, CardContent, Chip, Collapse,
  Dialog, DialogActions, DialogContent, DialogTitle, Divider, FormControl,
  FormControlLabel, IconButton, InputLabel, LinearProgress, Link, MenuItem,
  Radio, RadioGroup, Select, Skeleton, Tab, Tabs, TextField, Tooltip,
  Typography,
} from '@mui/material'
import {
  AddOutlined, ArrowBackOutlined, DeleteOutlined, ExpandLessOutlined,
  ExpandMoreOutlined, EditOutlined, InfoOutlined,
} from '@mui/icons-material'
import { client } from '../api/client'
import PageHeader from '../components/PageHeader'

// ── Types ─────────────────────────────────────────────────────────────────────

interface CsrmAssessmentSummary {
  id: string; name: string; description: string | null; organisation: string | null
  assessor: string | null; scope: string | null; status: string
  created_at: string; updated_at: string
  objects_count: number; elevated_count: number
  baseline_met_pct: number | null; objects_fully_assessed: number
}

interface ProtectionObject {
  id: string; assessment_id: string; name: string; description: string | null
  architecture_notes: string | null; processes_served: string | null
  data_classification: string | null; protection_level: 'standard' | 'elevated'
  elevated_rationale: string | null; sort_order: number
  created_at: string; updated_at: string
  baseline_ratings: BaselineRating[]; elevated_toms: ElevatedTom[]
}

interface BaselineRating {
  id: string; object_id: string; requirement_id: string
  status: 'not_assessed' | 'met' | 'partial' | 'not_met' | 'exception'
  exception_justification: string | null; notes: string | null; updated_at: string
}

interface ElevatedTom {
  id: string; object_id: string; threat_category: string; tom_description: string
  status: 'planned' | 'in_progress' | 'implemented' | 'not_applicable'
  notes: string | null; created_at: string; updated_at: string
}

interface AssessmentDetail {
  id: string; name: string; description: string | null; organisation: string | null
  assessor: string | null; scope: string | null; status: string
  created_at: string; updated_at: string
  objects: ProtectionObject[]
}

// ── Constants ─────────────────────────────────────────────────────────────────

const BASELINE_REQUIREMENTS = [
  { id: 'GV.1', function: 'Govern',          title: 'Security Organisation',               description: 'An information security organisation is defined with clear roles, responsibilities, and decision-making authority.' },
  { id: 'GV.2', function: 'Govern',          title: 'Cyber Risk Management',               description: 'Cyber risks are identified, assessed, and managed as part of the overall organisational risk management process.' },
  { id: 'GV.3', function: 'Govern',          title: 'Screening of Employees',              description: 'Background checks are performed for employees in security-sensitive roles commensurate with risk and regulatory requirements.' },
  { id: 'GV.4', function: 'Govern',          title: 'Training and Awareness',              description: 'Regular security awareness training is provided to all employees; role-specific training is provided to security-relevant staff.' },
  { id: 'ID.1', function: 'Identify',        title: 'IT Protection Objects',               description: 'All IT protection objects are documented with their processes served, data flows, hardware/software components, and protection needs analysed.' },
  { id: 'ID.2', function: 'Identify',        title: 'Supply Chain',                        description: 'Supply chain dependencies are identified, assessed for risk, and monitored on an ongoing basis.' },
  { id: 'PR.1', function: 'Protect',         title: 'Physical Protection, Configuration & Operation', description: 'Physical access controls are in place; logical isolation and virtualisation are used where appropriate; technical hardening is applied (predefined accounts removed, unnecessary services disabled, security settings enforced).' },
  { id: 'PR.2', function: 'Protect',         title: 'Vulnerability & Weakness Management', description: 'Software and firmware vulnerabilities are monitored and patched using automated mechanisms on a risk-based schedule.' },
  { id: 'PR.3', function: 'Protect',         title: 'Identity & Access Control',           description: 'All access to systems is authenticated; authorisation follows least-privilege principles; privileged access is controlled and logged.' },
  { id: 'PR.4', function: 'Protect',         title: 'Network Security',                    description: 'Network segments are separated with perimeter protection controls, or equivalent zero/minimal trust architecture is implemented.' },
  { id: 'PR.5', function: 'Protect',         title: 'Malware Protection',                  description: 'Protection against malware and data-driven attacks is implemented and kept current on all relevant systems.' },
  { id: 'PR.6', function: 'Protect',         title: 'Encryption & Data Deletion',          description: 'Sensitive data is protected by cryptographic controls for storage, processing, and transmission; secure deletion is applied according to data classification.' },
  { id: 'PR.7', function: 'Protect',         title: 'Data Backup',                         description: 'Regular backups are performed with offline/off-site copies at multiple locations; rapid restoration capability is tested periodically.' },
  { id: 'PR.8', function: 'Protect',         title: 'Secure Development',                  description: 'Security is integrated from the start of development: threat modelling, secure coding guidelines, CI/CD security checks, safe interfaces, and separated development/production environments.' },
  { id: 'PR.9', function: 'Protect',         title: 'Availability',                        description: 'Sufficient computing, storage, and transmission capacity is maintained; critical components have redundancy to meet availability requirements.' },
  { id: 'DE.1', function: 'Detect',          title: 'Recording & Monitoring',              description: 'Security-relevant events are logged and evaluated; SOC or equivalent monitoring capability assesses log data for anomalies.' },
  { id: 'DE.2', function: 'Detect',          title: 'Reporting Centre',                    description: 'A clear and documented process exists for employees and partners to report vulnerabilities and security incidents.' },
  { id: 'RS.1', function: 'Respond/Recover', title: 'Incident Management',                 description: 'Security incidents are triaged, escalated, and resolved according to documented procedures with defined responsibilities and timelines.' },
  { id: 'RS.2', function: 'Respond/Recover', title: 'Contingency Planning',                description: 'Emergency and recovery plans are documented, integrated into organisational plans, include IT/OT supply chain dependencies, and are tested regularly.' },
  { id: 'RS.3', function: 'Respond/Recover', title: 'Crisis Communication',                description: 'Communication responsibilities and objectives for security emergencies are defined, documented, and known to all relevant parties.' },
]

const NIST_FUNCTIONS = ['Govern', 'Identify', 'Protect', 'Detect', 'Respond/Recover']

const FUNCTION_COLORS: Record<string, string> = {
  'Govern':          '#5C6BC0',
  'Identify':        '#00897B',
  'Protect':         '#2E7D32',
  'Detect':          '#F57F17',
  'Respond/Recover': '#C62828',
}

const STATUS_CONFIG_DARK: Record<string, { label: string; color: string; bg: string }> = {
  not_assessed: { label: 'Not Assessed', color: 'rgba(255,255,255,0.3)',  bg: 'rgba(255,255,255,0.05)' },
  met:          { label: 'Met',          color: '#C6EFCE',                bg: 'rgba(198,239,206,0.15)' },
  partial:      { label: 'Partial',      color: '#FFC000',                bg: 'rgba(255,192,0,0.12)'   },
  not_met:      { label: 'Not Met',      color: '#FF7043',                bg: 'rgba(255,112,67,0.12)'  },
  exception:    { label: 'Exception',    color: '#CE93D8',                bg: 'rgba(206,147,216,0.12)' },
}

const STATUS_CONFIG_LIGHT: Record<string, { label: string; color: string; bg: string }> = {
  not_assessed: { label: 'Not Assessed', color: 'rgba(0,0,0,0.4)',        bg: 'rgba(0,0,0,0.04)'       },
  met:          { label: 'Met',          color: '#1b5e20',                 bg: 'rgba(27,94,32,0.1)'     },
  partial:      { label: 'Partial',      color: '#856404',                 bg: 'rgba(133,100,4,0.1)'    },
  not_met:      { label: 'Not Met',      color: '#bf360c',                 bg: 'rgba(191,54,12,0.1)'    },
  exception:    { label: 'Exception',    color: '#6a1b9a',                 bg: 'rgba(106,27,154,0.1)'   },
}

const TOM_STATUS_CONFIG_DARK: Record<string, { label: string; color: string }> = {
  planned:        { label: 'Planned',     color: '#90CAF9' },
  in_progress:    { label: 'In Progress', color: '#FFC000' },
  implemented:    { label: 'Implemented', color: '#C6EFCE' },
  not_applicable: { label: 'N/A',         color: 'rgba(255,255,255,0.3)' },
}

const TOM_STATUS_CONFIG_LIGHT: Record<string, { label: string; color: string }> = {
  planned:        { label: 'Planned',     color: '#1565c0' },
  in_progress:    { label: 'In Progress', color: '#856404' },
  implemented:    { label: 'Implemented', color: '#1b5e20' },
  not_applicable: { label: 'N/A',         color: 'rgba(0,0,0,0.4)' },
}

const THREAT_CATEGORIES = [
  'Authentication', 'Integrity Check', 'Hashing', 'Message Authentication',
  'Logging', 'Encryption', 'Access Control', 'Network Segmentation',
  'Resourcing', 'High Availability', 'Least Privilege', 'Abuse/Compromise Protection',
]

const CONTROL_OBJECTIVES = [
  { id: 'CO-1', title: 'Process & Dependency Visibility',  description: 'Important business/production processes and their dependencies on IT protection objects are known and documented.' },
  { id: 'CO-2', title: 'Governance & Culture',             description: 'Responsibilities, accountabilities, resources, and security culture are established and maintained.' },
  { id: 'CO-3', title: 'Threat & Protection Analysis',     description: 'Threat situation is analysed and protection needs are understood for all IT protection objects.' },
  { id: 'CO-4', title: 'TOM Implementation',               description: 'Suitable technical and organisational measures are implemented; consistent security concept is in place.' },
  { id: 'CO-5', title: 'Detection & Recovery',             description: 'Security incidents are detected and resolved promptly; rapid restoration capability is maintained.' },
  { id: 'CO-6', title: 'Supply Chain Control',             description: 'Supply chain dependencies and third-party risks are identified and controlled.' },
]

const CO_REQUIREMENT_MAP: Record<string, string[]> = {
  'CO-1': ['ID.1', 'ID.2'],
  'CO-2': ['GV.1', 'GV.2', 'GV.3', 'GV.4'],
  'CO-3': ['ID.1', 'ID.2', 'GV.2'],
  'CO-4': ['PR.1', 'PR.2', 'PR.3', 'PR.4', 'PR.5', 'PR.6', 'PR.7', 'PR.8', 'PR.9'],
  'CO-5': ['DE.1', 'DE.2', 'RS.1', 'RS.2', 'RS.3'],
  'CO-6': ['ID.2', 'RS.2'],
}

// ── API ───────────────────────────────────────────────────────────────────────

const api = {
  listAssessments:  ()                         => client.get<CsrmAssessmentSummary[]>('/csrm/assessments').then(r => r.data),
  createAssessment: (d: any)                   => client.post<CsrmAssessmentSummary>('/csrm/assessments', d).then(r => r.data),
  getAssessment:    (id: string)               => client.get<AssessmentDetail>(`/csrm/assessments/${id}`).then(r => r.data),
  patchAssessment:  (id: string, d: any)       => client.patch(`/csrm/assessments/${id}`, d).then(r => r.data),
  deleteAssessment: (id: string)               => client.delete(`/csrm/assessments/${id}`),
  createObject:     (aid: string, d: any)      => client.post<ProtectionObject>(`/csrm/assessments/${aid}/objects`, d).then(r => r.data),
  patchObject:      (oid: string, d: any)      => client.patch<ProtectionObject>(`/csrm/objects/${oid}`, d).then(r => r.data),
  deleteObject:     (oid: string)              => client.delete(`/csrm/objects/${oid}`),
  upsertRatings:    (oid: string, ratings: any[]) => client.put<BaselineRating[]>(`/csrm/objects/${oid}/ratings`, ratings).then(r => r.data),
  createTom:        (oid: string, d: any)      => client.post<ElevatedTom>(`/csrm/objects/${oid}/toms`, d).then(r => r.data),
  patchTom:         (tid: string, d: any)      => client.patch<ElevatedTom>(`/csrm/toms/${tid}`, d).then(r => r.data),
  deleteTom:        (tid: string)              => client.delete(`/csrm/toms/${tid}`),
}

// ── Helpers ───────────────────────────────────────────────────────────────────

function statusChip(status: string, isLight: boolean, size: 'small' | 'medium' = 'small') {
  const STATUS_CONFIG = isLight ? STATUS_CONFIG_LIGHT : STATUS_CONFIG_DARK
  const cfg = STATUS_CONFIG[status] ?? STATUS_CONFIG['not_assessed']
  return (
    <Chip
      label={cfg.label}
      size={size}
      sx={{ bgcolor: cfg.bg, color: cfg.color, border: `1px solid ${cfg.color}40`, fontWeight: 500, fontSize: '0.7rem' }}
    />
  )
}

function assessmentStatusChip(status: string, isLight: boolean) {
  const mapDark: Record<string, { label: string; color: string; bg: string }> = {
    draft:       { label: 'Draft',       color: '#90CAF9',  bg: 'rgba(144,202,249,0.12)' },
    in_progress: { label: 'In Progress', color: '#FFC000',  bg: 'rgba(255,192,0,0.12)'   },
    complete:    { label: 'Complete',    color: '#C6EFCE',  bg: 'rgba(198,239,206,0.15)'  },
  }
  const mapLight: Record<string, { label: string; color: string; bg: string }> = {
    draft:       { label: 'Draft',       color: '#1565c0',  bg: 'rgba(21,101,192,0.1)'   },
    in_progress: { label: 'In Progress', color: '#856404',  bg: 'rgba(133,100,4,0.1)'    },
    complete:    { label: 'Complete',    color: '#1b5e20',  bg: 'rgba(27,94,32,0.1)'      },
  }
  const map = isLight ? mapLight : mapDark
  const cfg = map[status] ?? map['draft']
  return (
    <Chip
      label={cfg.label}
      size="small"
      sx={{ bgcolor: cfg.bg, color: cfg.color, border: `1px solid ${cfg.color}40`, fontWeight: 500, fontSize: '0.7rem' }}
    />
  )
}

function getRatingForReq(object: ProtectionObject, reqId: string): BaselineRating | undefined {
  return object.baseline_ratings.find(r => r.requirement_id === reqId)
}

function getAssessedCount(object: ProtectionObject): number {
  return object.baseline_ratings.filter(r => r.status !== 'not_assessed').length
}

function getMetCount(object: ProtectionObject): number {
  return object.baseline_ratings.filter(r => r.status === 'met').length
}

// ── Disclaimer ────────────────────────────────────────────────────────────────

function CsrmDisclaimer() {
  const [open, setOpen] = useState(false)
  return (
    <Alert
      severity="warning"
      sx={{ mb: 2.5, cursor: 'pointer' }}
      onClick={() => setOpen(o => !o)}
      action={
        <IconButton size="small" onClick={e => { e.stopPropagation(); setOpen(o => !o) }}>
          {open ? <ExpandLessOutlined fontSize="small" /> : <ExpandMoreOutlined fontSize="small" />}
        </IconButton>
      }
    >
      <AlertTitle>CSRM 2025 — Framework in Development</AlertTitle>
      NCSC BACS publishes this methodology as a work in progress. Click to see known limitations and implementation notes.
      <Collapse in={open}>
        <Box sx={{ mt: 1.5 }}>
          <Typography variant="caption" component="div" sx={{ mb: 0.5, color: 'success.light' }}>
            <strong>✓ ISMS CORE implementation note:</strong> This assessment uses <strong>NIST CSF 2.0</strong> as the organising structure
            (Govern / Identify / Protect / Detect / Respond+Recover). BACS's own comparison document references the Swiss ICT
            Minimum Standard which is based on NIST CSF 1.1 — we have updated the baseline requirement structure to align with CSF 2.0.
          </Typography>
          <Typography variant="caption" component="div" sx={{ mb: 0.75, mt: 1 }}>
            <strong>Known gaps (from NCSC's own comparison document — Vergleich-Managementsysteme_EN.pdf):</strong>
          </Typography>
          <Typography variant="caption" component="ul" sx={{ pl: 2, m: 0 }}>
            <li><strong>IEC 62443 alignment pending</strong> — OT coverage claimed but not yet demonstrated against the OT security standard (footnote 26, p.20)</li>
            <li><strong>10 ICT Minimum Standard gaps</strong> — incl. threat intel sharing, hardware integrity, forensics, continuous improvement, contractual supplier requirements (Vergleich p.6–7)</li>
            <li><strong>"No policies needed" is misleading</strong> — operational policies (vulnerability mgmt, incident mgmt, supplier mgmt) remain necessary (Vergleich p.4)</li>
            <li><strong>Continuous improvement optional</strong> — unlike ISO 27001 PDCA; "stable processes" deemed sufficient (Vergleich p.7)</li>
            <li><strong>Parallel implementation creates duplication</strong> — NCSC admits running alongside ISO 27001 or ICT Minimum Standard leads to reporting duplication (Vergleich p.5)</li>
          </Typography>
          <Typography variant="caption" component="div" sx={{ mt: 1.25 }}>
            <strong>Source documents: </strong>
            <Link href="https://www.ncsc.admin.ch/ncsc/en/home/infos-fuer/infos-it-spezialisten/themen/csrm.html" target="_blank" rel="noopener" sx={{ mr: 0.75 }}>
              BACS CSRM page
            </Link>
            ·{' '}
            <Link href="https://www.ncsc.admin.ch/dam/ncsc/en/dokumente/infos-fuer/infos-it-spezialisten/csrm/Methode-CSRM-2025-EN.pdf" target="_blank" rel="noopener" sx={{ mx: 0.75 }}>
              Methode-CSRM-2025-EN.pdf
            </Link>
            ·{' '}
            <Link href="https://www.ncsc.admin.ch/dam/ncsc/en/dokumente/infos-fuer/infos-it-spezialisten/csrm/Vergleich-Managementsysteme_EN.pdf" target="_blank" rel="noopener" sx={{ ml: 0.75 }}>
              Vergleich-Managementsysteme_EN.pdf
            </Link>
          </Typography>
        </Box>
      </Collapse>
    </Alert>
  )
}

// ── Baseline requirement row ──────────────────────────────────────────────────

function RequirementRow({
  req, rating, onUpdate,
}: {
  req: typeof BASELINE_REQUIREMENTS[0]
  rating: BaselineRating | undefined
  onUpdate: (reqId: string, status: string, notes?: string, justification?: string) => void
}) {
  const { palette } = useTheme()
  const isLight = palette.mode === 'light'
  const STATUS_CONFIG = isLight ? STATUS_CONFIG_LIGHT : STATUS_CONFIG_DARK
  const [notesOpen, setNotesOpen] = useState(false)
  const [localNotes, setLocalNotes] = useState(rating?.notes ?? '')
  const [localJustification, setLocalJustification] = useState(rating?.exception_justification ?? '')
  const status = rating?.status ?? 'not_assessed'
  const fnColor = FUNCTION_COLORS[req.function] ?? '#888'

  function handleStatusChange(newStatus: string) {
    onUpdate(req.id, newStatus, localNotes || undefined, localJustification || undefined)
  }

  function handleNotesSave() {
    onUpdate(req.id, status, localNotes || undefined, localJustification || undefined)
  }

  return (
    <Box sx={{ borderBottom: '1px solid', borderColor: isLight ? 'rgba(0,0,0,0.06)' : 'rgba(255,255,255,0.05)', py: 0.75 }}>
      <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
        {/* Req ID */}
        <Box sx={{ minWidth: 44 }}>
          <Chip
            label={req.id}
            size="small"
            sx={{ bgcolor: `${fnColor}20`, color: fnColor, border: `1px solid ${fnColor}40`, fontSize: '0.65rem', fontWeight: 700, height: 20 }}
          />
        </Box>
        {/* Title + description toggle */}
        <Box sx={{ flex: 1, minWidth: 0 }}>
          <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.5 }}>
            <Typography variant="body2" sx={{ fontSize: '0.8rem', fontWeight: 500 }}>
              {req.title}
            </Typography>
            <Tooltip title={req.description} arrow placement="top">
              <InfoOutlined sx={{ fontSize: 13, color: 'text.disabled', cursor: 'help', flexShrink: 0 }} />
            </Tooltip>
          </Box>
        </Box>
        {/* Status selector */}
        <Box sx={{ display: 'flex', gap: 0.5, flexShrink: 0 }}>
          {Object.entries(STATUS_CONFIG).map(([s, cfg]) => (
            <Box
              key={s}
              onClick={() => handleStatusChange(s)}
              sx={{
                px: 1, py: 0.3, borderRadius: 1, cursor: 'pointer', fontSize: '0.68rem', fontWeight: status === s ? 700 : 400,
                border: '1px solid',
                borderColor: status === s ? `${cfg.color}80` : (isLight ? 'rgba(0,0,0,0.12)' : 'rgba(255,255,255,0.08)'),
                bgcolor: status === s ? cfg.bg : 'transparent',
                color: status === s ? cfg.color : 'text.disabled',
                transition: 'all 0.1s',
                '&:hover': { borderColor: `${cfg.color}50`, color: cfg.color },
                whiteSpace: 'nowrap',
              }}
            >
              {cfg.label}
            </Box>
          ))}
        </Box>
        {/* Notes toggle */}
        <IconButton
          size="small"
          onClick={() => setNotesOpen(o => !o)}
          sx={{ color: (rating?.notes || rating?.exception_justification) ? '#FFC000' : 'text.disabled', flexShrink: 0 }}
        >
          {notesOpen ? <ExpandLessOutlined sx={{ fontSize: 16 }} /> : <ExpandMoreOutlined sx={{ fontSize: 16 }} />}
        </IconButton>
      </Box>

      {/* Notes / exception justification */}
      <Collapse in={notesOpen}>
        <Box sx={{ mt: 1, pl: '52px', display: 'flex', flexDirection: 'column', gap: 1 }}>
          <TextField
            label="Notes"
            size="small"
            multiline
            minRows={2}
            fullWidth
            value={localNotes}
            onChange={e => setLocalNotes(e.target.value)}
            onBlur={handleNotesSave}
            sx={{ '& .MuiInputBase-root': { fontSize: '0.78rem' } }}
          />
          {status === 'exception' && (
            <TextField
              label="Exception justification"
              size="small"
              multiline
              minRows={2}
              fullWidth
              value={localJustification}
              onChange={e => setLocalJustification(e.target.value)}
              onBlur={handleNotesSave}
              sx={{ '& .MuiInputBase-root': { fontSize: '0.78rem' } }}
            />
          )}
        </Box>
      </Collapse>
    </Box>
  )
}

// ── TOM row ───────────────────────────────────────────────────────────────────

function TomRow({
  tom, onPatch, onDelete,
}: {
  tom: ElevatedTom
  onPatch: (id: string, d: any) => void
  onDelete: (id: string) => void
}) {
  const { palette } = useTheme()
  const isLight = palette.mode === 'light'
  const TOM_STATUS_CONFIG = isLight ? TOM_STATUS_CONFIG_LIGHT : TOM_STATUS_CONFIG_DARK
  const [editing, setEditing] = useState(false)
  const [desc, setDesc] = useState(tom.tom_description)
  const [notes, setNotes] = useState(tom.notes ?? '')
  const cfg = TOM_STATUS_CONFIG[tom.status] ?? TOM_STATUS_CONFIG['planned']

  function save() {
    onPatch(tom.id, { tom_description: desc, notes: notes || undefined })
    setEditing(false)
  }

  return (
    <Box sx={{ p: 1.25, border: '1px solid', borderColor: isLight ? 'rgba(0,0,0,0.1)' : 'rgba(255,255,255,0.08)', borderRadius: 1.5, mb: 1 }}>
      <Box sx={{ display: 'flex', alignItems: 'flex-start', gap: 1 }}>
        <Chip label={tom.threat_category} size="small" sx={{ bgcolor: isLight ? 'rgba(0,0,0,0.06)' : 'rgba(255,255,255,0.07)', color: 'text.secondary', fontSize: '0.65rem', height: 20, flexShrink: 0 }} />
        <Box sx={{ flex: 1, minWidth: 0 }}>
          {editing ? (
            <TextField
              size="small" fullWidth multiline minRows={2}
              value={desc}
              onChange={e => setDesc(e.target.value)}
              sx={{ mb: 0.75, '& .MuiInputBase-root': { fontSize: '0.78rem' } }}
            />
          ) : (
            <Typography variant="body2" sx={{ fontSize: '0.8rem', mb: 0.25 }}>{tom.tom_description}</Typography>
          )}
          {tom.notes && !editing && (
            <Typography variant="caption" color="text.disabled">{tom.notes}</Typography>
          )}
          {editing && (
            <TextField
              label="Notes" size="small" fullWidth
              value={notes}
              onChange={e => setNotes(e.target.value)}
              sx={{ '& .MuiInputBase-root': { fontSize: '0.78rem' } }}
            />
          )}
        </Box>
        <Box sx={{ display: 'flex', flexDirection: 'column', gap: 0.5, alignItems: 'flex-end', flexShrink: 0 }}>
          <Select
            size="small"
            value={tom.status}
            onChange={e => onPatch(tom.id, { status: e.target.value })}
            sx={{ fontSize: '0.72rem', height: 26, minWidth: 110, color: cfg.color, '& .MuiOutlinedInput-notchedOutline': { borderColor: `${cfg.color}40` } }}
          >
            {Object.entries(TOM_STATUS_CONFIG).map(([s, c]) => (
              <MenuItem key={s} value={s} sx={{ fontSize: '0.78rem' }}>{c.label}</MenuItem>
            ))}
          </Select>
          <Box sx={{ display: 'flex', gap: 0.25 }}>
            <IconButton size="small" onClick={() => editing ? save() : setEditing(true)} sx={{ color: editing ? (isLight ? '#1b5e20' : '#C6EFCE') : 'text.disabled' }}>
              <EditOutlined sx={{ fontSize: 15 }} />
            </IconButton>
            <IconButton size="small" onClick={() => onDelete(tom.id)} sx={{ color: 'rgba(255,82,82,0.6)', '&:hover': { color: '#FF5252' } }}>
              <DeleteOutlined sx={{ fontSize: 15 }} />
            </IconButton>
          </Box>
        </Box>
      </Box>
    </Box>
  )
}

// ── Protection Object Panel ────────────────────────────────────────────────────

function ObjectPanel({
  object, onClose, onUpdate,
}: {
  object: ProtectionObject
  onClose: () => void
  onUpdate: (updated: ProtectionObject) => void
}) {
  const { palette } = useTheme()
  const isLight = palette.mode === 'light'
  const [editMeta, setEditMeta] = useState(false)
  const [metaForm, setMetaForm] = useState({
    name: object.name,
    description: object.description ?? '',
    architecture_notes: object.architecture_notes ?? '',
    processes_served: object.processes_served ?? '',
    data_classification: object.data_classification ?? 'standard',
    protection_level: object.protection_level,
    elevated_rationale: object.elevated_rationale ?? '',
  })
  const [localObject, setLocalObject] = useState<ProtectionObject>(object)
  const [newTomOpen, setNewTomOpen] = useState(false)
  const [newTomForm, setNewTomForm] = useState({ threat_category: '', tom_description: '', notes: '' })
  const [saving, setSaving] = useState(false)

  useEffect(() => {
    setLocalObject(object)
    setMetaForm({
      name: object.name,
      description: object.description ?? '',
      architecture_notes: object.architecture_notes ?? '',
      processes_served: object.processes_served ?? '',
      data_classification: object.data_classification ?? 'standard',
      protection_level: object.protection_level,
      elevated_rationale: object.elevated_rationale ?? '',
    })
  }, [object])

  async function saveMeta() {
    setSaving(true)
    try {
      const updated = await api.patchObject(localObject.id, {
        name: metaForm.name,
        description: metaForm.description || null,
        architecture_notes: metaForm.architecture_notes || null,
        processes_served: metaForm.processes_served || null,
        data_classification: metaForm.data_classification,
        protection_level: metaForm.protection_level,
        elevated_rationale: metaForm.elevated_rationale || null,
      }) as ProtectionObject
      const merged = { ...updated, baseline_ratings: localObject.baseline_ratings, elevated_toms: localObject.elevated_toms }
      setLocalObject(merged)
      onUpdate(merged)
      setEditMeta(false)
    } catch (e) {
      console.error(e)
    } finally {
      setSaving(false)
    }
  }

  async function handleRatingUpdate(reqId: string, status: string, notes?: string, justification?: string) {
    try {
      const ratings = await api.upsertRatings(localObject.id, [{ requirement_id: reqId, status, notes: notes ?? null, exception_justification: justification ?? null }])
      const merged = { ...localObject, baseline_ratings: ratings as BaselineRating[] }
      setLocalObject(merged)
      onUpdate(merged)
    } catch (e) {
      console.error(e)
    }
  }

  async function handleTomPatch(tomId: string, data: any) {
    try {
      const updated = await api.patchTom(tomId, data) as ElevatedTom
      const toms = localObject.elevated_toms.map(t => t.id === tomId ? updated : t)
      const merged = { ...localObject, elevated_toms: toms }
      setLocalObject(merged)
      onUpdate(merged)
    } catch (e) {
      console.error(e)
    }
  }

  async function handleTomDelete(tomId: string) {
    try {
      await api.deleteTom(tomId)
      const toms = localObject.elevated_toms.filter(t => t.id !== tomId)
      const merged = { ...localObject, elevated_toms: toms }
      setLocalObject(merged)
      onUpdate(merged)
    } catch (e) {
      console.error(e)
    }
  }

  async function handleAddTom() {
    if (!newTomForm.threat_category || !newTomForm.tom_description) return
    try {
      const tom = await api.createTom(localObject.id, {
        threat_category: newTomForm.threat_category,
        tom_description: newTomForm.tom_description,
        notes: newTomForm.notes || null,
      }) as ElevatedTom
      const merged = { ...localObject, elevated_toms: [...localObject.elevated_toms, tom] }
      setLocalObject(merged)
      onUpdate(merged)
      setNewTomForm({ threat_category: '', tom_description: '', notes: '' })
      setNewTomOpen(false)
    } catch (e) {
      console.error(e)
    }
  }

  const assessedCount = getAssessedCount(localObject)
  const metCount = getMetCount(localObject)
  const isElevated = localObject.protection_level === 'elevated'

  return (
    <Box sx={{ flex: 1, overflow: 'auto', p: 2.5 }}>
      {/* Header */}
      <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 2 }}>
        <IconButton size="small" onClick={onClose} sx={{ color: 'text.secondary' }}>
          <ArrowBackOutlined sx={{ fontSize: 18 }} />
        </IconButton>
        <Box sx={{ flex: 1 }}>
          <Typography variant="h6" sx={{ fontSize: '1rem', fontWeight: 600 }}>{localObject.name}</Typography>
          <Box sx={{ display: 'flex', gap: 1, alignItems: 'center', mt: 0.25 }}>
            <Chip
              label={isElevated ? 'Elevated Protection' : 'Standard Protection'}
              size="small"
              sx={{
                bgcolor: isElevated ? 'rgba(255,112,67,0.12)' : 'rgba(144,202,249,0.12)',
                color: isElevated ? '#FF7043' : (isLight ? '#1565c0' : '#90CAF9'),
                border: `1px solid ${isElevated ? '#FF704340' : (isLight ? 'rgba(21,101,192,0.25)' : '#90CAF940')}`,
                fontSize: '0.68rem', fontWeight: 600,
              }}
            />
            <Typography variant="caption" color="text.disabled">
              {assessedCount}/20 assessed · {metCount} met
            </Typography>
          </Box>
        </Box>
        <IconButton size="small" onClick={() => setEditMeta(e => !e)} sx={{ color: editMeta ? '#FFC000' : 'text.disabled' }}>
          <EditOutlined sx={{ fontSize: 18 }} />
        </IconButton>
      </Box>

      {/* Metadata edit form */}
      <Collapse in={editMeta}>
        <Box sx={{ p: 2, bgcolor: isLight ? 'rgba(0,0,0,0.02)' : 'rgba(255,255,255,0.03)', borderRadius: 1.5, border: '1px solid', borderColor: isLight ? 'rgba(0,0,0,0.08)' : 'rgba(255,255,255,0.07)', mb: 2 }}>
          <Typography variant="caption" color="text.secondary" sx={{ display: 'block', mb: 1.5, fontWeight: 600, textTransform: 'uppercase', fontSize: '0.65rem', letterSpacing: '0.05em' }}>
            Object Properties
          </Typography>
          <Box sx={{ display: 'flex', flexDirection: 'column', gap: 1.5 }}>
            <TextField label="Name" size="small" fullWidth value={metaForm.name} onChange={e => setMetaForm(f => ({ ...f, name: e.target.value }))} />
            <TextField label="Description" size="small" fullWidth multiline minRows={2} value={metaForm.description} onChange={e => setMetaForm(f => ({ ...f, description: e.target.value }))} />
            <TextField label="Architecture notes" size="small" fullWidth multiline minRows={2} value={metaForm.architecture_notes} onChange={e => setMetaForm(f => ({ ...f, architecture_notes: e.target.value }))} />
            <TextField label="Processes served" size="small" fullWidth multiline minRows={2} value={metaForm.processes_served} onChange={e => setMetaForm(f => ({ ...f, processes_served: e.target.value }))} />
            <FormControl size="small" fullWidth>
              <InputLabel>Data Classification</InputLabel>
              <Select label="Data Classification" value={metaForm.data_classification} onChange={e => setMetaForm(f => ({ ...f, data_classification: e.target.value }))}>
                <MenuItem value="standard">Standard</MenuItem>
                <MenuItem value="confidential">Confidential</MenuItem>
                <MenuItem value="restricted">Restricted</MenuItem>
              </Select>
            </FormControl>
            <FormControl>
              <Typography variant="caption" color="text.secondary" sx={{ mb: 0.5 }}>Protection Level</Typography>
              <RadioGroup row value={metaForm.protection_level} onChange={e => setMetaForm(f => ({ ...f, protection_level: e.target.value }))}>
                <FormControlLabel value="standard" control={<Radio size="small" />} label={<Typography variant="body2">Standard</Typography>} />
                <FormControlLabel value="elevated" control={<Radio size="small" />} label={<Typography variant="body2" sx={{ color: '#FF7043' }}>Elevated</Typography>} />
              </RadioGroup>
            </FormControl>
            {metaForm.protection_level === 'elevated' && (
              <TextField label="Rationale for elevated protection" size="small" fullWidth multiline minRows={2} value={metaForm.elevated_rationale} onChange={e => setMetaForm(f => ({ ...f, elevated_rationale: e.target.value }))} />
            )}
            <Box sx={{ display: 'flex', gap: 1, justifyContent: 'flex-end' }}>
              <Button size="small" onClick={() => setEditMeta(false)}>Cancel</Button>
              <Button size="small" variant="contained" onClick={saveMeta} disabled={saving}>Save</Button>
            </Box>
          </Box>
        </Box>
      </Collapse>

      {/* Baseline requirements grid */}
      <Typography variant="caption" color="text.secondary" sx={{ display: 'block', mb: 1, fontWeight: 600, textTransform: 'uppercase', fontSize: '0.65rem', letterSpacing: '0.05em' }}>
        Baseline Requirements (20)
      </Typography>

      {NIST_FUNCTIONS.map(fn => {
        const reqs = BASELINE_REQUIREMENTS.filter(r => r.function === fn)
        const fnColor = FUNCTION_COLORS[fn]
        return (
          <Box key={fn} sx={{ mb: 2 }}>
            <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 0.75, pb: 0.5, borderBottom: `2px solid ${fnColor}30` }}>
              <Box sx={{ width: 8, height: 8, borderRadius: '50%', bgcolor: fnColor, flexShrink: 0 }} />
              <Typography variant="caption" sx={{ color: fnColor, fontWeight: 700, fontSize: '0.72rem', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
                {fn}
              </Typography>
            </Box>
            {reqs.map(req => (
              <RequirementRow
                key={req.id}
                req={req}
                rating={getRatingForReq(localObject, req.id)}
                onUpdate={handleRatingUpdate}
              />
            ))}
          </Box>
        )
      })}

      {/* Elevated TOMs section */}
      {isElevated && (
        <Box sx={{ mt: 3 }}>
          <Box sx={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', mb: 1.5 }}>
            <Box>
              <Typography variant="caption" sx={{ fontWeight: 600, textTransform: 'uppercase', fontSize: '0.65rem', letterSpacing: '0.05em', color: '#FF7043' }}>
                Additional Technical & Organisational Measures
              </Typography>
              <Typography variant="caption" color="text.disabled" sx={{ display: 'block', fontSize: '0.7rem' }}>
                Elevated protection objects require additional TOMs to address specific threat categories
              </Typography>
            </Box>
            <Button
              size="small"
              startIcon={<AddOutlined sx={{ fontSize: 14 }} />}
              onClick={() => setNewTomOpen(o => !o)}
              sx={{ fontSize: '0.72rem' }}
            >
              Add TOM
            </Button>
          </Box>

          <Collapse in={newTomOpen}>
            <Box sx={{ p: 1.5, bgcolor: 'rgba(255,112,67,0.04)', border: '1px solid rgba(255,112,67,0.15)', borderRadius: 1.5, mb: 1.5 }}>
              <Box sx={{ display: 'flex', flexDirection: 'column', gap: 1 }}>
                <FormControl size="small" fullWidth>
                  <InputLabel>Threat Category</InputLabel>
                  <Select
                    label="Threat Category"
                    value={newTomForm.threat_category}
                    onChange={e => setNewTomForm(f => ({ ...f, threat_category: e.target.value }))}
                  >
                    {THREAT_CATEGORIES.map(c => <MenuItem key={c} value={c} sx={{ fontSize: '0.8rem' }}>{c}</MenuItem>)}
                  </Select>
                </FormControl>
                <TextField
                  label="TOM description" size="small" fullWidth multiline minRows={2}
                  value={newTomForm.tom_description}
                  onChange={e => setNewTomForm(f => ({ ...f, tom_description: e.target.value }))}
                />
                <TextField
                  label="Notes (optional)" size="small" fullWidth
                  value={newTomForm.notes}
                  onChange={e => setNewTomForm(f => ({ ...f, notes: e.target.value }))}
                />
                <Box sx={{ display: 'flex', gap: 1, justifyContent: 'flex-end' }}>
                  <Button size="small" onClick={() => setNewTomOpen(false)}>Cancel</Button>
                  <Button size="small" variant="contained" onClick={handleAddTom} disabled={!newTomForm.threat_category || !newTomForm.tom_description}>
                    Add
                  </Button>
                </Box>
              </Box>
            </Box>
          </Collapse>

          {localObject.elevated_toms.length === 0 ? (
            <Typography variant="caption" color="text.disabled" sx={{ display: 'block', textAlign: 'center', py: 2 }}>
              No TOMs defined yet. Add threat-specific measures above.
            </Typography>
          ) : (
            localObject.elevated_toms.map(tom => (
              <TomRow key={tom.id} tom={tom} onPatch={handleTomPatch} onDelete={handleTomDelete} />
            ))
          )}
        </Box>
      )}
    </Box>
  )
}

// ── Control Objectives card ───────────────────────────────────────────────────

function ControlObjectiveCard({ co, objects }: { co: typeof CONTROL_OBJECTIVES[0]; objects: ProtectionObject[] }) {
  const { palette } = useTheme()
  const isLight = palette.mode === 'light'
  const reqIds = CO_REQUIREMENT_MAP[co.id] ?? []
  const total = objects.length * reqIds.length
  const met = objects.reduce((acc, obj) => {
    return acc + reqIds.filter(rid => getRatingForReq(obj, rid)?.status === 'met').length
  }, 0)
  const pct = total > 0 ? Math.round(met / total * 100) : null

  const color = pct === null
    ? (isLight ? 'rgba(0,0,0,0.3)' : 'rgba(255,255,255,0.3)')
    : pct >= 80 ? (isLight ? '#1b5e20' : '#C6EFCE')
    : pct >= 50 ? '#FFC000'
    : '#FF7043'
  const bg = pct === null
    ? (isLight ? 'rgba(0,0,0,0.03)' : 'rgba(255,255,255,0.05)')
    : pct >= 80 ? 'rgba(198,239,206,0.12)'
    : pct >= 50 ? 'rgba(255,192,0,0.10)'
    : 'rgba(255,112,67,0.10)'

  return (
    <Card variant="outlined" sx={{ bgcolor: bg, border: `1px solid ${color}30` }}>
      <CardContent sx={{ p: 1.5, '&:last-child': { pb: 1.5 } }}>
        <Box sx={{ display: 'flex', alignItems: 'flex-start', justifyContent: 'space-between', gap: 1, mb: 0.75 }}>
          <Box>
            <Typography variant="caption" sx={{ fontWeight: 700, color, fontSize: '0.7rem' }}>{co.id}</Typography>
            <Typography variant="body2" sx={{ fontWeight: 600, fontSize: '0.82rem', lineHeight: 1.3 }}>{co.title}</Typography>
          </Box>
          {pct !== null ? (
            <Chip label={`${pct}%`} size="small" sx={{ bgcolor: bg, color, border: `1px solid ${color}50`, fontWeight: 700, fontSize: '0.72rem' }} />
          ) : (
            <Chip label="—" size="small" sx={{ bgcolor: isLight ? 'rgba(0,0,0,0.05)' : 'rgba(255,255,255,0.05)', color: 'text.disabled', fontSize: '0.72rem' }} />
          )}
        </Box>
        <Typography variant="caption" color="text.disabled" sx={{ fontSize: '0.7rem', lineHeight: 1.4 }}>{co.description}</Typography>
        {pct !== null && (
          <LinearProgress
            variant="determinate"
            value={Math.min(100, pct)}
            sx={{ mt: 1, height: 3, borderRadius: 2, bgcolor: isLight ? 'rgba(0,0,0,0.08)' : 'rgba(255,255,255,0.08)', '& .MuiLinearProgress-bar': { bgcolor: color } }}
          />
        )}
        <Typography variant="caption" color="text.disabled" sx={{ display: 'block', mt: 0.5, fontSize: '0.65rem' }}>
          Requirements: {reqIds.join(', ')}
        </Typography>
      </CardContent>
    </Card>
  )
}

// ── Report Tab ────────────────────────────────────────────────────────────────

function ReportTab({ detail }: { detail: AssessmentDetail }) {
  const { palette } = useTheme()
  const isLight = palette.mode === 'light'
  const STATUS_CONFIG = isLight ? STATUS_CONFIG_LIGHT : STATUS_CONFIG_DARK
  const objects = detail.objects
  const totalObjects = objects.length
  const elevatedObjects = objects.filter(o => o.protection_level === 'elevated').length
  const fullyAssessed = objects.filter(o => getAssessedCount(o) === 20).length

  const allRatings = objects.flatMap(o => BASELINE_REQUIREMENTS.map(req => ({
    object: o,
    req,
    rating: getRatingForReq(o, req.id),
  })))
  const metTotal = allRatings.filter(r => r.rating?.status === 'met').length
  const basePct = totalObjects > 0 ? Math.round(metTotal / (totalObjects * 20) * 100) : null

  const gaps = allRatings.filter(r =>
    r.rating?.status === 'not_met' || r.rating?.status === 'partial' || r.rating?.status === 'exception'
  )

  return (
    <Box>
      <Alert severity="warning" sx={{ mb: 2.5 }}>
        <AlertTitle>Report Disclaimer</AlertTitle>
        This report references CSRM 2025 — a methodology in active development. Verify coverage against
        the ICT Minimum Standard for the 10 gap areas listed in the framework disclaimer above.
      </Alert>

      {/* Summary cards */}
      <Box sx={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: 1.5, mb: 3 }}>
        {[
          { label: 'Protection Objects', value: totalObjects },
          { label: 'Elevated Objects', value: elevatedObjects, color: elevatedObjects > 0 ? '#FF7043' : undefined },
          { label: 'Fully Assessed', value: `${fullyAssessed}/${totalObjects}` },
          { label: 'Baseline Compliance', value: basePct !== null ? `${basePct}%` : '—', color: basePct !== null ? (basePct >= 80 ? (isLight ? '#1b5e20' : '#C6EFCE') : basePct >= 50 ? '#FFC000' : '#FF7043') : undefined },
        ].map((card) => (
          <Card key={card.label} variant="outlined" sx={{ bgcolor: isLight ? 'rgba(0,0,0,0.02)' : 'rgba(255,255,255,0.03)' }}>
            <CardContent sx={{ p: 1.5, '&:last-child': { pb: 1.5 } }}>
              <Typography variant="caption" color="text.disabled" sx={{ fontSize: '0.68rem' }}>{card.label}</Typography>
              <Typography variant="h6" sx={{ fontWeight: 700, color: card.color ?? 'text.primary', mt: 0.25 }}>{card.value}</Typography>
            </CardContent>
          </Card>
        ))}
      </Box>

      {/* Control objectives bar */}
      <Typography variant="subtitle2" sx={{ mb: 1.5, fontWeight: 600 }}>Control Objectives</Typography>
      <Box sx={{ display: 'flex', flexDirection: 'column', gap: 1, mb: 3 }}>
        {CONTROL_OBJECTIVES.map(co => {
          const reqIds = CO_REQUIREMENT_MAP[co.id] ?? []
          const total = objects.length * reqIds.length
          const met = objects.reduce((acc, obj) => acc + reqIds.filter(rid => getRatingForReq(obj, rid)?.status === 'met').length, 0)
          const pct = total > 0 ? Math.round(met / total * 100) : null
          const color = pct === null
            ? (isLight ? 'rgba(0,0,0,0.3)' : 'rgba(255,255,255,0.3)')
            : pct >= 80 ? (isLight ? '#1b5e20' : '#C6EFCE')
            : pct >= 50 ? '#FFC000'
            : '#FF7043'
          return (
            <Box key={co.id} sx={{ display: 'flex', alignItems: 'center', gap: 2 }}>
              <Typography variant="caption" sx={{ width: 40, fontWeight: 600, color: 'text.secondary', flexShrink: 0 }}>{co.id}</Typography>
              <Typography variant="caption" sx={{ flex: 1, minWidth: 0 }}>{co.title}</Typography>
              <Box sx={{ width: 160, flexShrink: 0 }}>
                <LinearProgress
                  variant="determinate"
                  value={pct !== null ? Math.min(100, pct) : 0}
                  sx={{ height: 6, borderRadius: 3, bgcolor: isLight ? 'rgba(0,0,0,0.08)' : 'rgba(255,255,255,0.08)', '& .MuiLinearProgress-bar': { bgcolor: color } }}
                />
              </Box>
              <Typography variant="caption" sx={{ width: 36, textAlign: 'right', color, fontWeight: 600, flexShrink: 0 }}>
                {pct !== null ? `${pct}%` : '—'}
              </Typography>
            </Box>
          )
        })}
      </Box>

      {/* Gaps table */}
      {gaps.length > 0 && (
        <>
          <Typography variant="subtitle2" sx={{ mb: 1.5, fontWeight: 600 }}>Gap Analysis ({gaps.length} items)</Typography>
          <Box sx={{ border: '1px solid', borderColor: isLight ? 'rgba(0,0,0,0.1)' : 'rgba(255,255,255,0.08)', borderRadius: 1.5, overflow: 'hidden' }}>
            <Box sx={{ display: 'grid', gridTemplateColumns: '160px 80px 100px 1fr', gap: 0, bgcolor: isLight ? 'rgba(0,0,0,0.04)' : 'rgba(255,255,255,0.05)', p: '6px 12px', borderBottom: '1px solid', borderBottomColor: isLight ? 'rgba(0,0,0,0.1)' : 'rgba(255,255,255,0.08)' }}>
              <Typography variant="caption" sx={{ fontWeight: 600, fontSize: '0.7rem' }}>Object</Typography>
              <Typography variant="caption" sx={{ fontWeight: 600, fontSize: '0.7rem' }}>Req</Typography>
              <Typography variant="caption" sx={{ fontWeight: 600, fontSize: '0.7rem' }}>Status</Typography>
              <Typography variant="caption" sx={{ fontWeight: 600, fontSize: '0.7rem' }}>Requirement</Typography>
            </Box>
            {gaps.map((g, i) => {
              const cfg = STATUS_CONFIG[g.rating?.status ?? 'not_assessed']
              return (
                <Box key={i} sx={{ display: 'grid', gridTemplateColumns: '160px 80px 100px 1fr', gap: 0, p: '6px 12px', borderBottom: '1px solid', borderBottomColor: isLight ? 'rgba(0,0,0,0.06)' : 'rgba(255,255,255,0.04)', '&:last-child': { borderBottom: 'none' } }}>
                  <Typography variant="caption" sx={{ overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>{g.object.name}</Typography>
                  <Typography variant="caption" sx={{ color: FUNCTION_COLORS[g.req.function] ?? 'text.secondary', fontWeight: 600 }}>{g.req.id}</Typography>
                  <Chip label={cfg.label} size="small" sx={{ bgcolor: cfg.bg, color: cfg.color, fontSize: '0.65rem', height: 18, width: 'fit-content' }} />
                  <Typography variant="caption" sx={{ color: 'text.secondary' }}>{g.req.title}</Typography>
                </Box>
              )
            })}
          </Box>
        </>
      )}

      {gaps.length === 0 && totalObjects > 0 && (
        <Alert severity="success">No gaps identified — all assessed requirements are met.</Alert>
      )}
    </Box>
  )
}

// ── New Assessment Dialog ──────────────────────────────────────────────────────

function NewAssessmentDialog({ open, onClose, onCreate }: {
  open: boolean; onClose: () => void; onCreate: (a: CsrmAssessmentSummary) => void
}) {
  const [form, setForm] = useState({ name: '', description: '', organisation: '', assessor: '', scope: '' })
  const [saving, setSaving] = useState(false)

  async function submit() {
    if (!form.name.trim()) return
    setSaving(true)
    try {
      const a = await api.createAssessment({
        name: form.name,
        description: form.description || null,
        organisation: form.organisation || null,
        assessor: form.assessor || null,
        scope: form.scope || null,
      })
      onCreate(a)
      setForm({ name: '', description: '', organisation: '', assessor: '', scope: '' })
      onClose()
    } catch (e) {
      console.error(e)
    } finally {
      setSaving(false)
    }
  }

  return (
    <Dialog open={open} onClose={onClose} maxWidth="sm" fullWidth>
      <DialogTitle>New CSRM Assessment</DialogTitle>
      <DialogContent sx={{ pt: 1 }}>
        <Box sx={{ display: 'flex', flexDirection: 'column', gap: 2, mt: 0.5 }}>
          <TextField label="Assessment name *" size="small" fullWidth value={form.name} onChange={e => setForm(f => ({ ...f, name: e.target.value }))} />
          <TextField label="Description" size="small" fullWidth multiline minRows={2} value={form.description} onChange={e => setForm(f => ({ ...f, description: e.target.value }))} />
          <TextField label="Organisation" size="small" fullWidth value={form.organisation} onChange={e => setForm(f => ({ ...f, organisation: e.target.value }))} />
          <TextField label="Assessor" size="small" fullWidth value={form.assessor} onChange={e => setForm(f => ({ ...f, assessor: e.target.value }))} />
          <TextField label="Scope" size="small" fullWidth multiline minRows={2} value={form.scope} onChange={e => setForm(f => ({ ...f, scope: e.target.value }))} />
        </Box>
      </DialogContent>
      <DialogActions sx={{ px: 3, pb: 2 }}>
        <Button onClick={onClose}>Cancel</Button>
        <Button variant="contained" onClick={submit} disabled={saving || !form.name.trim()}>Create</Button>
      </DialogActions>
    </Dialog>
  )
}

// ── Main Page ─────────────────────────────────────────────────────────────────

export default function Csrm() {
  const { palette } = useTheme()
  const isLight = palette.mode === 'light'
  const [assessments, setAssessments] = useState<CsrmAssessmentSummary[]>([])
  const [loading, setLoading] = useState(true)
  const [selectedId, setSelectedId] = useState<string | null>(null)
  const [detail, setDetail] = useState<AssessmentDetail | null>(null)
  const [detailLoading, setDetailLoading] = useState(false)
  const [selectedObjectId, setSelectedObjectId] = useState<string | null>(null)
  const [activeTab, setActiveTab] = useState<'overview' | 'objects' | 'report'>('overview')
  const [newAssessmentOpen, setNewAssessmentOpen] = useState(false)
  const [newObjectOpen, setNewObjectOpen] = useState(false)
  const [newObjForm, setNewObjForm] = useState({
    name: '', description: '', architecture_notes: '', processes_served: '',
    data_classification: 'standard', protection_level: 'standard', elevated_rationale: '',
  })
  const [savingObj, setSavingObj] = useState(false)
  const [editAssessment, setEditAssessment] = useState(false)
  const [assessmentForm, setAssessmentForm] = useState({ name: '', description: '', organisation: '', assessor: '', scope: '', status: 'draft' })
  const [deleteConfirmId, setDeleteConfirmId] = useState<string | null>(null)

  // Load list
  useEffect(() => {
    setLoading(true)
    api.listAssessments()
      .then(data => setAssessments(data))
      .catch(console.error)
      .finally(() => setLoading(false))
  }, [])

  // Load detail when selectedId changes
  useEffect(() => {
    if (!selectedId) { setDetail(null); return }
    setDetailLoading(true)
    setSelectedObjectId(null)
    api.getAssessment(selectedId)
      .then(d => {
        setDetail(d)
        setAssessmentForm({
          name: d.name, description: d.description ?? '', organisation: d.organisation ?? '',
          assessor: d.assessor ?? '', scope: d.scope ?? '', status: d.status,
        })
      })
      .catch(console.error)
      .finally(() => setDetailLoading(false))
  }, [selectedId])

  async function handleCreateAssessment(a: CsrmAssessmentSummary) {
    setAssessments(prev => [a, ...prev])
  }

  async function handleDeleteAssessment(id: string) {
    await api.deleteAssessment(id)
    setAssessments(prev => prev.filter(a => a.id !== id))
    if (selectedId === id) setSelectedId(null)
    setDeleteConfirmId(null)
  }

  async function handleSaveAssessmentMeta() {
    if (!selectedId || !detail) return
    await api.patchAssessment(selectedId, {
      name: assessmentForm.name,
      description: assessmentForm.description || null,
      organisation: assessmentForm.organisation || null,
      assessor: assessmentForm.assessor || null,
      scope: assessmentForm.scope || null,
      status: assessmentForm.status,
    })
    setDetail(d => d ? { ...d, ...assessmentForm } : d)
    setAssessments(prev => prev.map(a => a.id === selectedId ? { ...a, name: assessmentForm.name, status: assessmentForm.status } : a))
    setEditAssessment(false)
  }

  async function handleCreateObject() {
    if (!selectedId || !newObjForm.name.trim()) return
    setSavingObj(true)
    try {
      const obj = await api.createObject(selectedId, {
        name: newObjForm.name,
        description: newObjForm.description || null,
        architecture_notes: newObjForm.architecture_notes || null,
        processes_served: newObjForm.processes_served || null,
        data_classification: newObjForm.data_classification,
        protection_level: newObjForm.protection_level,
        elevated_rationale: newObjForm.elevated_rationale || null,
        sort_order: detail?.objects.length ?? 0,
      }) as ProtectionObject
      setDetail(d => d ? { ...d, objects: [...d.objects, obj] } : d)
      setNewObjForm({ name: '', description: '', architecture_notes: '', processes_served: '', data_classification: 'standard', protection_level: 'standard', elevated_rationale: '' })
      setNewObjectOpen(false)
    } catch (e) {
      console.error(e)
    } finally {
      setSavingObj(false)
    }
  }

  async function handleDeleteObject(oid: string) {
    await api.deleteObject(oid)
    setDetail(d => d ? { ...d, objects: d.objects.filter(o => o.id !== oid) } : d)
    if (selectedObjectId === oid) setSelectedObjectId(null)
  }

  function handleObjectUpdate(updated: ProtectionObject) {
    setDetail(d => d ? { ...d, objects: d.objects.map(o => o.id === updated.id ? updated : o) } : d)
  }

  const selectedObject = detail?.objects.find(o => o.id === selectedObjectId) ?? null

  // ── Render ──────────────────────────────────────────────────────────────────

  // List view
  if (!selectedId) {
    return (
      <Box sx={{ p: 3 }}>
        <PageHeader
          title="CSRM Assessment"
          subtitle="Swiss NCSC Cyber Security Risk Management — object-centric baseline assessment"
          actions={
            <Button variant="contained" startIcon={<AddOutlined />} onClick={() => setNewAssessmentOpen(true)}>
              New Assessment
            </Button>
          }
        />

        <CsrmDisclaimer />

        {loading ? (
          <Box sx={{ display: 'flex', flexDirection: 'column', gap: 1.5 }}>
            {[1, 2, 3].map(i => <Skeleton key={i} variant="rectangular" height={100} sx={{ borderRadius: 2 }} />)}
          </Box>
        ) : assessments.length === 0 ? (
          <Box sx={{ textAlign: 'center', py: 8 }}>
            <Typography variant="h6" color="text.secondary" sx={{ mb: 1 }}>No assessments yet</Typography>
            <Typography variant="body2" color="text.disabled" sx={{ mb: 3 }}>Create a new CSRM assessment to get started.</Typography>
            <Button variant="outlined" startIcon={<AddOutlined />} onClick={() => setNewAssessmentOpen(true)}>New Assessment</Button>
          </Box>
        ) : (
          <Box sx={{ display: 'flex', flexDirection: 'column', gap: 1.5 }}>
            {assessments.map(a => (
              <Card key={a.id} variant="outlined" sx={{ bgcolor: isLight ? 'transparent' : 'rgba(255,255,255,0.02)', '&:hover': { bgcolor: isLight ? 'rgba(0,0,0,0.02)' : 'rgba(255,255,255,0.04)' }, transition: 'background-color 0.15s' }}>
                <CardContent sx={{ p: 2, '&:last-child': { pb: 2 } }}>
                  <Box sx={{ display: 'flex', alignItems: 'flex-start', gap: 2 }}>
                    <Box sx={{ flex: 1, minWidth: 0 }}>
                      <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 0.5 }}>
                        <Typography variant="subtitle1" sx={{ fontWeight: 600, fontSize: '0.95rem' }}>{a.name}</Typography>
                        {assessmentStatusChip(a.status, isLight)}
                      </Box>
                      {a.organisation && (
                        <Typography variant="caption" color="text.secondary" sx={{ display: 'block', mb: 0.5 }}>{a.organisation}</Typography>
                      )}
                      <Box sx={{ display: 'flex', gap: 2, alignItems: 'center', flexWrap: 'wrap' }}>
                        <Typography variant="caption" color="text.disabled">{a.objects_count} protection objects</Typography>
                        {a.elevated_count > 0 && (
                          <Typography variant="caption" sx={{ color: '#FF7043' }}>{a.elevated_count} elevated</Typography>
                        )}
                        <Typography variant="caption" color="text.disabled">{a.objects_fully_assessed}/{a.objects_count} fully assessed</Typography>
                        {a.baseline_met_pct !== null && (
                          <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.75 }}>
                            <LinearProgress
                              variant="determinate"
                              value={Math.min(100, a.baseline_met_pct)}
                              sx={{ width: 80, height: 4, borderRadius: 2, bgcolor: isLight ? 'rgba(0,0,0,0.08)' : 'rgba(255,255,255,0.08)', '& .MuiLinearProgress-bar': { bgcolor: a.baseline_met_pct >= 80 ? (isLight ? '#1b5e20' : '#C6EFCE') : a.baseline_met_pct >= 50 ? '#FFC000' : '#FF7043' } }}
                            />
                            <Typography variant="caption" sx={{ color: a.baseline_met_pct >= 80 ? (isLight ? '#1b5e20' : '#C6EFCE') : a.baseline_met_pct >= 50 ? '#FFC000' : '#FF7043', fontWeight: 600 }}>
                              {a.baseline_met_pct}%
                            </Typography>
                          </Box>
                        )}
                      </Box>
                    </Box>
                    <Box sx={{ display: 'flex', gap: 1, alignItems: 'center', flexShrink: 0 }}>
                      <IconButton
                        size="small"
                        onClick={() => setDeleteConfirmId(a.id)}
                        sx={{ color: 'rgba(255,82,82,0.5)', '&:hover': { color: '#FF5252' } }}
                      >
                        <DeleteOutlined sx={{ fontSize: 18 }} />
                      </IconButton>
                      <Button size="small" variant="outlined" onClick={() => { setSelectedId(a.id); setActiveTab('overview') }}>
                        Open
                      </Button>
                    </Box>
                  </Box>
                </CardContent>
              </Card>
            ))}
          </Box>
        )}

        <NewAssessmentDialog open={newAssessmentOpen} onClose={() => setNewAssessmentOpen(false)} onCreate={handleCreateAssessment} />

        {/* Delete confirm */}
        <Dialog open={!!deleteConfirmId} onClose={() => setDeleteConfirmId(null)} maxWidth="xs" fullWidth>
          <DialogTitle>Delete Assessment</DialogTitle>
          <DialogContent>
            <Typography>This will permanently delete the assessment and all protection objects, ratings, and TOMs. This cannot be undone.</Typography>
          </DialogContent>
          <DialogActions sx={{ px: 3, pb: 2 }}>
            <Button onClick={() => setDeleteConfirmId(null)}>Cancel</Button>
            <Button color="error" variant="contained" onClick={() => deleteConfirmId && handleDeleteAssessment(deleteConfirmId)}>Delete</Button>
          </DialogActions>
        </Dialog>
      </Box>
    )
  }

  // Detail view
  return (
    <Box sx={{ p: 3 }}>
      <PageHeader
        title={detail?.name ?? '…'}
        subtitle={[detail?.organisation, detail?.assessor ? `Assessor: ${detail.assessor}` : null].filter(Boolean).join(' · ') || undefined}
        actions={
          <Button startIcon={<ArrowBackOutlined />} onClick={() => { setSelectedId(null); setDetail(null); setEditAssessment(false) }}>
            All Assessments
          </Button>
        }
      />

      <CsrmDisclaimer />

      {detailLoading || !detail ? (
        <Box sx={{ display: 'flex', flexDirection: 'column', gap: 1.5 }}>
          {[1, 2, 3].map(i => <Skeleton key={i} variant="rectangular" height={60} sx={{ borderRadius: 2 }} />)}
        </Box>
      ) : (
        <>
          {/* Tabs */}
          <Box sx={{ borderBottom: 1, borderColor: 'divider', mb: 3 }}>
            <Tabs value={activeTab} onChange={(_, v) => { setActiveTab(v); setSelectedObjectId(null) }} sx={{ minHeight: 38 }}>
              <Tab value="overview" label="Overview" sx={{ minHeight: 38, fontSize: '0.82rem' }} />
              <Tab value="objects" label={`Protection Objects (${detail.objects.length})`} sx={{ minHeight: 38, fontSize: '0.82rem' }} />
              <Tab value="report" label="Report" sx={{ minHeight: 38, fontSize: '0.82rem' }} />
            </Tabs>
          </Box>

          {/* Overview tab */}
          {activeTab === 'overview' && (
            <Box>
              {/* Assessment metadata card */}
              <Card variant="outlined" sx={{ bgcolor: isLight ? 'transparent' : 'rgba(255,255,255,0.02)', mb: 3 }}>
                <CardContent sx={{ p: 2, '&:last-child': { pb: 2 } }}>
                  <Box sx={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', mb: 1.5 }}>
                    <Typography variant="subtitle2" sx={{ fontWeight: 600 }}>Assessment Details</Typography>
                    <IconButton size="small" onClick={() => setEditAssessment(e => !e)} sx={{ color: editAssessment ? '#FFC000' : 'text.disabled' }}>
                      <EditOutlined sx={{ fontSize: 17 }} />
                    </IconButton>
                  </Box>
                  <Collapse in={editAssessment}>
                    <Box sx={{ display: 'flex', flexDirection: 'column', gap: 1.5, mb: 1.5 }}>
                      <TextField label="Name" size="small" fullWidth value={assessmentForm.name} onChange={e => setAssessmentForm(f => ({ ...f, name: e.target.value }))} />
                      <TextField label="Description" size="small" fullWidth multiline minRows={2} value={assessmentForm.description} onChange={e => setAssessmentForm(f => ({ ...f, description: e.target.value }))} />
                      <Box sx={{ display: 'flex', gap: 1.5 }}>
                        <TextField label="Organisation" size="small" fullWidth value={assessmentForm.organisation} onChange={e => setAssessmentForm(f => ({ ...f, organisation: e.target.value }))} />
                        <TextField label="Assessor" size="small" fullWidth value={assessmentForm.assessor} onChange={e => setAssessmentForm(f => ({ ...f, assessor: e.target.value }))} />
                      </Box>
                      <TextField label="Scope" size="small" fullWidth multiline minRows={2} value={assessmentForm.scope} onChange={e => setAssessmentForm(f => ({ ...f, scope: e.target.value }))} />
                      <FormControl size="small" sx={{ maxWidth: 180 }}>
                        <InputLabel>Status</InputLabel>
                        <Select label="Status" value={assessmentForm.status} onChange={e => setAssessmentForm(f => ({ ...f, status: e.target.value }))}>
                          <MenuItem value="draft">Draft</MenuItem>
                          <MenuItem value="in_progress">In Progress</MenuItem>
                          <MenuItem value="complete">Complete</MenuItem>
                        </Select>
                      </FormControl>
                      <Box sx={{ display: 'flex', gap: 1, justifyContent: 'flex-end' }}>
                        <Button size="small" onClick={() => setEditAssessment(false)}>Cancel</Button>
                        <Button size="small" variant="contained" onClick={handleSaveAssessmentMeta}>Save</Button>
                      </Box>
                    </Box>
                    <Divider sx={{ mb: 1.5 }} />
                  </Collapse>
                  {!editAssessment && (
                    <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 2 }}>
                      {detail.scope && (
                        <Box>
                          <Typography variant="caption" color="text.disabled" sx={{ display: 'block' }}>Scope</Typography>
                          <Typography variant="body2" sx={{ fontSize: '0.82rem' }}>{detail.scope}</Typography>
                        </Box>
                      )}
                      {detail.description && (
                        <Box sx={{ flex: 1, minWidth: 200 }}>
                          <Typography variant="caption" color="text.disabled" sx={{ display: 'block' }}>Description</Typography>
                          <Typography variant="body2" sx={{ fontSize: '0.82rem' }}>{detail.description}</Typography>
                        </Box>
                      )}
                    </Box>
                  )}
                </CardContent>
              </Card>

              {/* Control Objectives grid */}
              <Typography variant="subtitle2" sx={{ mb: 1.5, fontWeight: 600 }}>Control Objectives</Typography>
              {detail.objects.length === 0 ? (
                <Alert severity="info" sx={{ mb: 3 }}>Add protection objects to begin assessing control objectives.</Alert>
              ) : (
                <Box sx={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: 1.5, mb: 3 }}>
                  {CONTROL_OBJECTIVES.map(co => (
                    <ControlObjectiveCard key={co.id} co={co} objects={detail.objects} />
                  ))}
                </Box>
              )}
            </Box>
          )}

          {/* Objects tab */}
          {activeTab === 'objects' && (
            <Box sx={{ display: 'flex', gap: 2, minHeight: 500 }}>
              {/* Object list */}
              <Box sx={{ width: 280, flexShrink: 0 }}>
                <Button
                  fullWidth
                  variant="outlined"
                  startIcon={<AddOutlined />}
                  onClick={() => setNewObjectOpen(true)}
                  sx={{ mb: 1.5, fontSize: '0.8rem' }}
                >
                  Add Protection Object
                </Button>

                {detail.objects.length === 0 ? (
                  <Box sx={{ textAlign: 'center', py: 4 }}>
                    <Typography variant="body2" color="text.disabled">No protection objects yet.</Typography>
                  </Box>
                ) : (
                  <Box sx={{ display: 'flex', flexDirection: 'column', gap: 0.75 }}>
                    {detail.objects.map(obj => {
                      const isActive = selectedObjectId === obj.id
                      const assessed = getAssessedCount(obj)
                      const met = getMetCount(obj)
                      const isElev = obj.protection_level === 'elevated'
                      return (
                        <Box
                          key={obj.id}
                          onClick={() => setSelectedObjectId(isActive ? null : obj.id)}
                          sx={{
                            p: 1.25, borderRadius: 1.5, cursor: 'pointer', border: '1px solid',
                            borderColor: isActive ? (isElev ? '#FF704340' : (isLight ? 'rgba(21,101,192,0.3)' : '#90CAF940')) : (isLight ? 'rgba(0,0,0,0.1)' : 'rgba(255,255,255,0.08)'),
                            bgcolor: isActive ? (isElev ? 'rgba(255,112,67,0.08)' : 'rgba(144,202,249,0.08)') : (isLight ? 'transparent' : 'rgba(255,255,255,0.02)'),
                            '&:hover': { bgcolor: isLight ? 'rgba(0,0,0,0.03)' : 'rgba(255,255,255,0.04)' },
                            transition: 'all 0.12s',
                          }}
                        >
                          <Box sx={{ display: 'flex', alignItems: 'flex-start', justifyContent: 'space-between', gap: 0.5 }}>
                            <Typography variant="body2" sx={{ fontWeight: isActive ? 600 : 400, fontSize: '0.82rem', flex: 1, minWidth: 0, overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
                              {obj.name}
                            </Typography>
                            <IconButton
                              size="small"
                              onClick={e => { e.stopPropagation(); handleDeleteObject(obj.id) }}
                              sx={{ color: 'rgba(255,82,82,0.4)', '&:hover': { color: '#FF5252' }, flexShrink: 0, p: 0.25 }}
                            >
                              <DeleteOutlined sx={{ fontSize: 14 }} />
                            </IconButton>
                          </Box>
                          <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.75, mt: 0.5 }}>
                            <Chip
                              label={isElev ? 'Elevated' : 'Standard'}
                              size="small"
                              sx={{ bgcolor: isElev ? 'rgba(255,112,67,0.10)' : 'rgba(144,202,249,0.10)', color: isElev ? '#FF7043' : (isLight ? '#1565c0' : '#90CAF9'), fontSize: '0.6rem', height: 16 }}
                            />
                            <Typography variant="caption" color="text.disabled" sx={{ fontSize: '0.68rem' }}>
                              {assessed}/20 · {met} met
                            </Typography>
                          </Box>
                          <LinearProgress
                            variant="determinate"
                            value={Math.min(100, assessed / 20 * 100)}
                            sx={{ mt: 0.75, height: 2, borderRadius: 1, bgcolor: isLight ? 'rgba(0,0,0,0.08)' : 'rgba(255,255,255,0.06)', '& .MuiLinearProgress-bar': { bgcolor: met === 20 ? (isLight ? '#1b5e20' : '#C6EFCE') : assessed > 0 ? (isLight ? '#1565c0' : '#90CAF9') : (isLight ? 'rgba(0,0,0,0.15)' : 'rgba(255,255,255,0.2)') } }}
                          />
                        </Box>
                      )
                    })}
                  </Box>
                )}
              </Box>

              {/* Object detail panel */}
              <Box sx={{ flex: 1, border: '1px solid', borderColor: isLight ? 'rgba(0,0,0,0.1)' : 'rgba(255,255,255,0.08)', borderRadius: 2, minHeight: 400, overflow: 'hidden', display: 'flex' }}>
                {!selectedObject ? (
                  <Box sx={{ flex: 1, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                    <Typography variant="body2" color="text.disabled">Select a protection object to assess its baseline requirements.</Typography>
                  </Box>
                ) : (
                  <ObjectPanel
                    object={selectedObject}
                    onClose={() => setSelectedObjectId(null)}
                    onUpdate={handleObjectUpdate}
                  />
                )}
              </Box>
            </Box>
          )}

          {/* Report tab */}
          {activeTab === 'report' && <ReportTab detail={detail} />}
        </>
      )}

      {/* New object dialog */}
      <Dialog open={newObjectOpen} onClose={() => setNewObjectOpen(false)} maxWidth="sm" fullWidth>
        <DialogTitle>Add Protection Object</DialogTitle>
        <DialogContent sx={{ pt: 1 }}>
          <Box sx={{ display: 'flex', flexDirection: 'column', gap: 1.5, mt: 0.5 }}>
            <TextField label="Name *" size="small" fullWidth value={newObjForm.name} onChange={e => setNewObjForm(f => ({ ...f, name: e.target.value }))} />
            <TextField label="Description" size="small" fullWidth multiline minRows={2} value={newObjForm.description} onChange={e => setNewObjForm(f => ({ ...f, description: e.target.value }))} />
            <TextField label="Architecture notes" size="small" fullWidth multiline minRows={2} value={newObjForm.architecture_notes} onChange={e => setNewObjForm(f => ({ ...f, architecture_notes: e.target.value }))} />
            <TextField label="Processes served" size="small" fullWidth multiline minRows={2} value={newObjForm.processes_served} onChange={e => setNewObjForm(f => ({ ...f, processes_served: e.target.value }))} />
            <FormControl size="small" fullWidth>
              <InputLabel>Data Classification</InputLabel>
              <Select label="Data Classification" value={newObjForm.data_classification} onChange={e => setNewObjForm(f => ({ ...f, data_classification: e.target.value }))}>
                <MenuItem value="standard">Standard</MenuItem>
                <MenuItem value="confidential">Confidential</MenuItem>
                <MenuItem value="restricted">Restricted</MenuItem>
              </Select>
            </FormControl>
            <FormControl>
              <Typography variant="caption" color="text.secondary" sx={{ mb: 0.5 }}>Protection Level</Typography>
              <RadioGroup row value={newObjForm.protection_level} onChange={e => setNewObjForm(f => ({ ...f, protection_level: e.target.value }))}>
                <FormControlLabel value="standard" control={<Radio size="small" />} label={<Typography variant="body2">Standard</Typography>} />
                <FormControlLabel value="elevated" control={<Radio size="small" />} label={<Typography variant="body2" sx={{ color: '#FF7043' }}>Elevated</Typography>} />
              </RadioGroup>
            </FormControl>
            {newObjForm.protection_level === 'elevated' && (
              <TextField label="Rationale for elevated protection" size="small" fullWidth multiline minRows={2} value={newObjForm.elevated_rationale} onChange={e => setNewObjForm(f => ({ ...f, elevated_rationale: e.target.value }))} />
            )}
          </Box>
        </DialogContent>
        <DialogActions sx={{ px: 3, pb: 2 }}>
          <Button onClick={() => setNewObjectOpen(false)}>Cancel</Button>
          <Button variant="contained" onClick={handleCreateObject} disabled={savingObj || !newObjForm.name.trim()}>Add</Button>
        </DialogActions>
      </Dialog>
    </Box>
  )
}
