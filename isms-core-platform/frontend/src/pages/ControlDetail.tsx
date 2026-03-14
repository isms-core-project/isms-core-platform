import { useState } from 'react'
import { useParams, useNavigate } from 'react-router-dom'
import {
  Box,
  Card,
  CardContent,
  Typography,
  Grid,
  Tab,
  Tabs,
  Chip,
  Skeleton,
  Alert,
  IconButton,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Collapse,
  Tooltip,
  Button,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  LinearProgress,
} from '@mui/material'
import { ArrowBackOutlined, ExpandMoreOutlined, ExpandLessOutlined, AutoAwesomeOutlined, AddOutlined, DeleteOutlined, AssignmentOutlined, FolderOpenOutlined, ExploreOutlined, ElectricalServicesOutlined, OpenInNewOutlined } from '@mui/icons-material'
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { controlsApi } from '../api/controls'
import { assessmentsApi } from '../api/assessmentsApi'
import { connectorsApi, ConnectorRead, ConnectorEvidenceRead, KNOWN_SYSTEMS } from '../api/connectorsApi'
import { useProduct } from '../store/ProductContext'
import StatusChip from '../components/StatusChip'
import AiAssistant from '../components/AiAssistant'
import DocPreviewDrawer from '../components/DocPreviewDrawer'
import AssessmentFormDrawer from '../components/AssessmentFormDrawer'

// Real API shapes
interface PolicyRow {
  id: string
  document_id: string
  title: string
  policy_type: string
  product_type: string
  requirements_count: number
  word_count: number
  source_label?: string | null
}

interface ImplRow {
  id: string
  document_id: string
  title: string
  impl_type: string
  word_count: number
}

interface ItemRow {
  id: string
  row_number: number
  item_text: string | null
  status: string
  owner: string | null
  due_date: string | null
  notes: string | null
}

interface SheetRow {
  id: string
  sheet_name: string
  sheet_type: string
  row_count: number
  items: ItemRow[]
}

interface AssessmentRow {
  id: string
  document_id: string
  workbook_name: string
  file_path: string
  product_type: string
  assessment_type: string
  sheets_count: number
  overall_score: number | null
  items_total: number
  items_compliant: number
  items_partial: number
  items_non_compliant: number
  items_na: number
  sheets: SheetRow[]
}

interface MappingRow {
  framework: string
  framework_code: string
  control_id: string
  control_title: string
  mapping_type: string
  confidence: number
}

interface IsoControlRow {
  control_id: string
  title: string
  description: string | null
  mappings: MappingRow[]
}

interface GapRow {
  id: string
  gap_type: string
  severity: string
  status: string
  description: string
}

interface EvidenceRow {
  id: string
  title: string
  evidence_type: string
  collected_date: string | null
  verified_by: string | null
}

interface RealControlDetail {
  id: string
  group_code: string
  name: string
  section: string
  section_name: string
  is_stacked: boolean
  has_framework: boolean
  has_operational: boolean
  framework_status: string
  operational_status: string
  stacked_control_ids: string[]
  policies: PolicyRow[]
  implementations: ImplRow[]
  assessments: AssessmentRow[]
  iso_controls: IsoControlRow[]
  gaps: GapRow[]
  evidence: EvidenceRow[]
  requirements_total: number
  gaps_open: number
  evidence_total: number
}

function TabPanel({ value, index, children }: { value: number; index: number; children: React.ReactNode }) {
  return value === index ? <Box sx={{ pt: 2 }}>{children}</Box> : null
}

function ComplianceBar({ total, compliant, partial, nonCompliant, na }: {
  total: number; compliant: number; partial: number; nonCompliant: number; na: number
}) {
  if (total === 0) return null
  return (
    <Box sx={{ mt: 1 }}>
      <Box sx={{ display: 'flex', height: 5, borderRadius: 2.5, overflow: 'hidden', bgcolor: 'rgba(255,255,255,0.06)' }}>
        {compliant > 0 && <Box sx={{ flex: compliant, bgcolor: '#C6EFCE' }} />}
        {partial > 0 && <Box sx={{ flex: partial, bgcolor: '#FFEB9C' }} />}
        {nonCompliant > 0 && <Box sx={{ flex: nonCompliant, bgcolor: '#FFC7CE' }} />}
        {na > 0 && <Box sx={{ flex: na, bgcolor: '#444' }} />}
      </Box>
      <Box sx={{ display: 'flex', gap: 1.5, mt: 0.4 }}>
        <Typography variant="caption" color="text.secondary">{total} items</Typography>
        {compliant > 0 && <Typography variant="caption" sx={{ color: '#C6EFCE' }}>{compliant} ✓</Typography>}
        {partial > 0 && <Typography variant="caption" sx={{ color: '#FFEB9C' }}>{partial} ~</Typography>}
        {nonCompliant > 0 && <Typography variant="caption" sx={{ color: '#FFC7CE' }}>{nonCompliant} ✗</Typography>}
        {na > 0 && <Typography variant="caption" color="text.disabled">{na} N/A</Typography>}
      </Box>
    </Box>
  )
}

const ITEM_STATUS_COLOR: Record<string, { bg: string; color: string; label: string }> = {
  compliant:      { bg: 'rgba(198,239,206,0.15)', color: '#C6EFCE', label: '✓' },
  partial:        { bg: 'rgba(255,235,156,0.12)', color: '#FFEB9C', label: '~' },
  non_compliant:  { bg: 'rgba(255,199,206,0.15)', color: '#FFC7CE', label: '✗' },
  na:             { bg: 'rgba(100,100,100,0.12)', color: '#888',    label: 'N/A' },
  not_applicable: { bg: 'rgba(100,100,100,0.12)', color: '#888',    label: 'N/A' },
  not_assessed:   { bg: 'transparent',             color: '#555',    label: '—' },
}

const STATUS_CYCLE = ['not_assessed', 'compliant', 'partial', 'non_compliant', 'na']
function nextStatus(current: string): string {
  const idx = STATUS_CYCLE.indexOf(current)
  return STATUS_CYCLE[(idx === -1 ? 1 : (idx + 1)) % STATUS_CYCLE.length]
}

function ItemStatusDot({ status }: { status: string }) {
  const s = ITEM_STATUS_COLOR[status] ?? ITEM_STATUS_COLOR.not_assessed
  return (
    <Box sx={{
      width: 6, height: 6, borderRadius: '50%', flexShrink: 0, mt: '5px',
      bgcolor: s.color === '#555' ? 'rgba(255,255,255,0.15)' : s.color,
    }} />
  )
}

function SheetItemsTable({ sheet, expanded, onToggle, onStatusChange }: {
  sheet: SheetRow
  expanded: boolean
  onToggle: () => void
  onStatusChange?: (itemId: string, newStatus: string) => void
}) {
  if (sheet.items.length === 0) return null
  return (
    <Box>
      <Box
        sx={{ display: 'flex', alignItems: 'center', gap: 0.5, cursor: 'pointer', py: 0.5, px: 1,
              bgcolor: 'rgba(68,114,196,0.06)', borderRadius: 1, mt: 0.5,
              '&:hover': { bgcolor: 'rgba(68,114,196,0.12)' } }}
        onClick={onToggle}
      >
        {expanded ? <ExpandLessOutlined sx={{ fontSize: 14 }} /> : <ExpandMoreOutlined sx={{ fontSize: 14 }} />}
        <Typography variant="caption" color="text.secondary">
          {sheet.items.length} checklist items
        </Typography>
        <Typography variant="caption" color="text.disabled" sx={{ ml: 'auto', fontSize: '0.6rem' }}>
          click item to cycle status
        </Typography>
      </Box>
      <Collapse in={expanded}>
        <Box sx={{ mt: 0.5 }}>
          {sheet.items.map((item) => {
            const sc = ITEM_STATUS_COLOR[item.status] ?? ITEM_STATUS_COLOR.not_assessed
            return (
              <Box
                key={item.id}
                onClick={() => onStatusChange?.(item.id, nextStatus(item.status))}
                sx={{
                  display: 'flex', gap: 1, py: 0.4, px: 1,
                  borderBottom: '1px solid rgba(255,255,255,0.04)',
                  cursor: onStatusChange ? 'pointer' : 'default',
                  bgcolor: sc.bg,
                  '&:hover': onStatusChange ? { bgcolor: 'rgba(68,114,196,0.08)' } : {},
                  borderLeft: `2px solid ${sc.color}40`,
                }}
              >
                <Typography variant="caption" sx={{ color: sc.color, fontWeight: 700, flexShrink: 0, minWidth: 20 }}>
                  {sc.label}
                </Typography>
                <Typography variant="caption" sx={{ flex: 1, color: 'text.primary', lineHeight: 1.4 }}>
                  {item.item_text ?? '—'}
                </Typography>
                {item.owner && (
                  <Typography variant="caption" color="text.disabled" sx={{ flexShrink: 0 }}>{item.owner}</Typography>
                )}
              </Box>
            )
          })}
        </Box>
      </Collapse>
    </Box>
  )
}

// ── Classification chip colours ──────────────────────────────────────────────
const CLASS_COLOR: Record<string, string> = {
  incident:      '#FFC7CE',
  change:        '#FFEB9C',
  asset:         '#C6EFCE',
  user:          '#BDD7EE',
  vulnerability: '#F4CCFF',
  network:       '#FFD966',
  policy:        '#CFE2F3',
}

// ── Connector status chip colour ─────────────────────────────────────────────
const CONN_STATUS_COLOR: Record<string, string> = {
  active:              '#C6EFCE',
  compliant:           '#C6EFCE',
  'attention-required':'#FFEB9C',
  'non-compliant':     '#FFC7CE',
  open:                '#FFC7CE',
  resolved:            '#C6EFCE',
}

// ── Structured evidence detail views ─────────────────────────────────────────

/** Flatten raw JSON into dot-notation paths with type + sample value. */
function flattenPaths(obj: unknown, prefix = ''): { path: string; type: string; sample: string }[] {
  if (obj === null || obj === undefined) return []
  if (typeof obj !== 'object') return []
  const results: { path: string; type: string; sample: string }[] = []
  const entries = Array.isArray(obj)
    ? Object.entries(obj[0] ?? {}).map(([k, v]) => [`[*].${k}`, v] as [string, unknown])
    : Object.entries(obj as Record<string, unknown>)
  for (const [k, v] of entries) {
    const path = prefix ? `${prefix}.${k}` : k
    if (Array.isArray(v)) {
      results.push({ path, type: `array[${v.length}]`, sample: v.length > 0 ? typeof v[0] === 'object' ? '{…}' : String(v[0]).slice(0, 30) : '' })
      if (v.length > 0 && typeof v[0] === 'object' && v[0] !== null) {
        results.push(...flattenPaths(v[0], `${path}[*]`))
      }
    } else if (v !== null && typeof v === 'object') {
      results.push({ path, type: 'object', sample: '' })
      results.push(...flattenPaths(v, path))
    } else {
      const sampleStr = v === null ? 'null' : String(v)
      results.push({ path, type: typeof v, sample: sampleStr.slice(0, 50) })
    }
  }
  return results
}

function EvidenceDetailView({ item }: { item: ConnectorEvidenceRead }) {
  const raw = (item.raw ?? {}) as Record<string, any>
  const [showJson, setShowJson] = useState(false)
  const [showFields, setShowFields] = useState(false)
  const [copied, setCopied] = useState(false)

  let content: React.ReactNode = null

  if (item.source_ref === 'entra-user-roster') {
    const users: any[] = raw.users ?? []
    content = (
      <Box>
        <Box sx={{ display: 'flex', gap: 2, mb: 1 }}>
          <Typography variant="caption" color="text.secondary">Total: <strong>{raw.total_users}</strong></Typography>
          <Typography variant="caption" sx={{ color: '#70AD47' }}>Enabled: <strong>{raw.enabled}</strong></Typography>
          <Typography variant="caption" sx={{ color: '#FF7043' }}>Disabled: <strong>{raw.disabled}</strong></Typography>
        </Box>
        <TableContainer sx={{ maxHeight: 260 }}>
          <Table size="small" stickyHeader>
            <TableHead>
              <TableRow>
                {['Display Name', 'UPN', 'Department', 'Title', 'Status'].map(h => (
                  <TableCell key={h} sx={{ fontSize: '0.6rem', fontWeight: 700, py: 0.5, bgcolor: 'rgba(0,0,0,0.4)' }}>{h}</TableCell>
                ))}
              </TableRow>
            </TableHead>
            <TableBody>
              {users.map((u, i) => (
                <TableRow key={i} hover>
                  <TableCell sx={{ fontSize: '0.65rem', py: 0.4 }}>{u.display_name ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, fontFamily: 'monospace', color: 'text.secondary' }}>{u.upn ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: 'text.secondary' }}>{u.department ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: 'text.secondary' }}>{u.job_title ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4 }}>
                    <Chip label={u.account_enabled ? 'enabled' : 'disabled'} size="small"
                      sx={{ height: 15, fontSize: '0.55rem', bgcolor: u.account_enabled ? 'rgba(112,173,71,0.2)' : 'rgba(255,112,67,0.2)', color: u.account_enabled ? '#70AD47' : '#FF7043' }} />
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </Box>
    )
  } else if (item.source_ref === 'entra-group-inventory') {
    const groups: any[] = raw.groups ?? []
    content = (
      <Box>
        <Box sx={{ display: 'flex', gap: 2, mb: 1 }}>
          <Typography variant="caption" color="text.secondary">Total groups: <strong>{raw.total_groups}</strong></Typography>
          <Typography variant="caption" color="text.secondary">Security-enabled: <strong>{raw.security_groups}</strong></Typography>
        </Box>
        <TableContainer sx={{ maxHeight: 240 }}>
          <Table size="small" stickyHeader>
            <TableHead>
              <TableRow>
                {['Display Name', 'Security', 'Types'].map(h => (
                  <TableCell key={h} sx={{ fontSize: '0.6rem', fontWeight: 700, py: 0.5, bgcolor: 'rgba(0,0,0,0.4)' }}>{h}</TableCell>
                ))}
              </TableRow>
            </TableHead>
            <TableBody>
              {groups.map((g, i) => (
                <TableRow key={i} hover>
                  <TableCell sx={{ fontSize: '0.65rem', py: 0.4 }}>{g.display_name ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4 }}>
                    <Chip label={g.security_enabled ? 'yes' : 'no'} size="small"
                      sx={{ height: 15, fontSize: '0.55rem', bgcolor: g.security_enabled ? 'rgba(112,173,71,0.2)' : 'rgba(255,255,255,0.06)', color: g.security_enabled ? '#70AD47' : 'text.disabled' }} />
                  </TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: 'text.secondary' }}>{(g.group_types ?? []).join(', ') || '—'}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </Box>
    )
  } else if (item.source_ref === 'entra-role-assignments') {
    const assignments: any[] = raw.assignments ?? []
    content = (
      <Box>
        <Box sx={{ display: 'flex', gap: 2, mb: 1 }}>
          <Typography variant="caption" color="text.secondary">Total assignments: <strong>{raw.total_assignments}</strong></Typography>
          <Typography variant="caption" sx={{ color: '#FF7043' }}>High-privilege: <strong>{raw.high_privilege_count}</strong></Typography>
        </Box>
        <TableContainer sx={{ maxHeight: 240 }}>
          <Table size="small" stickyHeader>
            <TableHead>
              <TableRow>
                {['Principal', 'Type', 'Role', 'Privilege'].map(h => (
                  <TableCell key={h} sx={{ fontSize: '0.6rem', fontWeight: 700, py: 0.5, bgcolor: 'rgba(0,0,0,0.4)' }}>{h}</TableCell>
                ))}
              </TableRow>
            </TableHead>
            <TableBody>
              {assignments.map((a, i) => (
                <TableRow key={i} hover>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, fontFamily: 'monospace' }}>{a.principal_upn ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: 'text.secondary' }}>{a.principal_type ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.65rem', py: 0.4 }}>{a.role ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4 }}>
                    {a.is_high_privilege && (
                      <Chip label="HIGH" size="small"
                        sx={{ height: 15, fontSize: '0.55rem', bgcolor: 'rgba(255,112,67,0.2)', color: '#FF7043' }} />
                    )}
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </Box>
    )
  } else if (item.source_ref === 'entra-mfa-status') {
    const users: any[] = raw.users ?? []
    content = (
      <Box>
        <Box sx={{ display: 'flex', gap: 2, mb: 1 }}>
          <Typography variant="caption" color="text.secondary">Total: <strong>{raw.total_users}</strong></Typography>
          <Typography variant="caption" sx={{ color: '#70AD47' }}>Registered: <strong>{raw.mfa_registered}</strong></Typography>
          <Typography variant="caption" color="text.secondary">Capable: <strong>{raw.mfa_capable}</strong></Typography>
          <Typography variant="caption" sx={{ color: raw.pct_registered >= 80 ? '#70AD47' : '#FF7043' }}>
            Coverage: <strong>{raw.pct_registered}%</strong>
          </Typography>
        </Box>
        <TableContainer sx={{ maxHeight: 240 }}>
          <Table size="small" stickyHeader>
            <TableHead>
              <TableRow>
                {['UPN', 'Registered', 'Capable', 'Default Method'].map(h => (
                  <TableCell key={h} sx={{ fontSize: '0.6rem', fontWeight: 700, py: 0.5, bgcolor: 'rgba(0,0,0,0.4)' }}>{h}</TableCell>
                ))}
              </TableRow>
            </TableHead>
            <TableBody>
              {users.map((u, i) => (
                <TableRow key={i} hover>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, fontFamily: 'monospace' }}>{u.upn ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4 }}>
                    <Chip label={u.mfa_registered ? 'yes' : 'no'} size="small"
                      sx={{ height: 15, fontSize: '0.55rem', bgcolor: u.mfa_registered ? 'rgba(112,173,71,0.2)' : 'rgba(255,112,67,0.2)', color: u.mfa_registered ? '#70AD47' : '#FF7043' }} />
                  </TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4 }}>
                    <Chip label={u.mfa_capable ? 'yes' : 'no'} size="small"
                      sx={{ height: 15, fontSize: '0.55rem', bgcolor: u.mfa_capable ? 'rgba(112,173,71,0.15)' : 'rgba(255,255,255,0.06)', color: u.mfa_capable ? '#70AD47' : 'text.disabled' }} />
                  </TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: 'text.secondary' }}>{u.default_method ?? '—'}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </Box>
    )
  } else if (item.source_ref === 'defender-endpoint-inventory') {
    const machines: any[] = raw.machines ?? []
    content = (
      <Box>
        <Box sx={{ display: 'flex', gap: 2, mb: 1, flexWrap: 'wrap' }}>
          <Typography variant="caption" color="text.secondary">Onboarded: <strong>{raw.onboarded}</strong></Typography>
          {Object.entries(raw.by_os ?? {}).map(([os, n]) => (
            <Typography key={os} variant="caption" color="text.secondary">{os}: <strong>{n as number}</strong></Typography>
          ))}
        </Box>
        <TableContainer sx={{ maxHeight: 240 }}>
          <Table size="small" stickyHeader>
            <TableHead>
              <TableRow>
                {['Name', 'OS', 'Health', 'Risk', 'Exposure', 'Last Seen'].map(h => (
                  <TableCell key={h} sx={{ fontSize: '0.6rem', fontWeight: 700, py: 0.5, bgcolor: 'rgba(0,0,0,0.4)' }}>{h}</TableCell>
                ))}
              </TableRow>
            </TableHead>
            <TableBody>
              {machines.map((m, i) => (
                <TableRow key={i} hover>
                  <TableCell sx={{ fontSize: '0.65rem', py: 0.4 }}>{m.name ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: 'text.secondary' }}>{m.os ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4 }}>
                    <Chip label={m.health ?? '—'} size="small"
                      sx={{ height: 15, fontSize: '0.55rem', bgcolor: m.health === 'Active' ? 'rgba(112,173,71,0.2)' : 'rgba(255,112,67,0.15)', color: m.health === 'Active' ? '#70AD47' : '#FF7043' }} />
                  </TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: (!m.risk || m.risk === 'None') ? '#70AD47' : '#FF7043' }}>{m.risk ?? 'None'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: 'text.secondary' }}>{m.exposure ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: 'text.secondary' }}>{m.last_seen ? new Date(m.last_seen).toLocaleDateString() : '—'}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </Box>
    )

  // ── CrowdStrike ───────────────────────────────────────────────────────────
  } else if (item.source_ref === 'crowdstrike-device-inventory') {
    const devices: any[] = raw.devices ?? []
    content = (
      <Box>
        <Box sx={{ display: 'flex', gap: 2, mb: 1, flexWrap: 'wrap' }}>
          <Typography variant="caption" color="text.secondary">Total: <strong>{raw.total_devices}</strong></Typography>
          <Typography variant="caption" sx={{ color: '#70AD47' }}>Normal: <strong>{raw.by_status?.normal ?? 0}</strong></Typography>
          {raw.reduced_functionality_count > 0 && (
            <Typography variant="caption" sx={{ color: '#FF7043' }}>Reduced: <strong>{raw.reduced_functionality_count}</strong></Typography>
          )}
        </Box>
        <TableContainer sx={{ maxHeight: 240 }}>
          <Table size="small" stickyHeader>
            <TableHead>
              <TableRow>
                {['Hostname', 'Platform', 'Status', 'Agent Ver', 'Last Seen'].map(h => (
                  <TableCell key={h} sx={{ fontSize: '0.6rem', fontWeight: 700, py: 0.5, bgcolor: 'rgba(0,0,0,0.4)' }}>{h}</TableCell>
                ))}
              </TableRow>
            </TableHead>
            <TableBody>
              {devices.map((d, i) => (
                <TableRow key={i} hover>
                  <TableCell sx={{ fontSize: '0.65rem', py: 0.4 }}>{d.hostname ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: 'text.secondary' }}>{d.platform_name ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4 }}>
                    <Chip label={d.status ?? '—'} size="small"
                      sx={{ height: 15, fontSize: '0.55rem', bgcolor: d.status === 'normal' ? 'rgba(112,173,71,0.2)' : 'rgba(255,112,67,0.15)', color: d.status === 'normal' ? '#70AD47' : '#FF7043' }} />
                  </TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: 'text.secondary', fontFamily: 'monospace' }}>{d.agent_version ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: 'text.secondary' }}>{d.last_seen ? new Date(d.last_seen).toLocaleDateString() : '—'}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </Box>
    )

  } else if (item.source_ref === 'crowdstrike-detections') {
    const detections: any[] = raw.detections ?? []
    const bySev = raw.by_severity ?? {}
    content = (
      <Box>
        <Box sx={{ display: 'flex', gap: 2, mb: 1, flexWrap: 'wrap' }}>
          <Typography variant="caption" color="text.secondary">Open: <strong>{raw.open_detections}</strong></Typography>
          {['Critical','High','Medium','Low'].map(s => bySev[s] > 0 ? (
            <Typography key={s} variant="caption" sx={{ color: s === 'Critical' || s === 'High' ? '#FF7043' : '#FFB300' }}>
              {s}: <strong>{bySev[s]}</strong>
            </Typography>
          ) : null)}
        </Box>
        <TableContainer sx={{ maxHeight: 240 }}>
          <Table size="small" stickyHeader>
            <TableHead>
              <TableRow>
                {['Detection ID', 'Status', 'Max Severity', 'Behaviours'].map(h => (
                  <TableCell key={h} sx={{ fontSize: '0.6rem', fontWeight: 700, py: 0.5, bgcolor: 'rgba(0,0,0,0.4)' }}>{h}</TableCell>
                ))}
              </TableRow>
            </TableHead>
            <TableBody>
              {detections.map((d, i) => (
                <TableRow key={i} hover>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, fontFamily: 'monospace', color: 'text.secondary' }}>{d.detection_id ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4 }}>{d.status ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4 }}>
                    <Chip label={d.max_severity ?? '—'} size="small"
                      sx={{ height: 15, fontSize: '0.55rem', bgcolor: d.max_severity === 'Critical' ? 'rgba(255,0,0,0.2)' : d.max_severity === 'High' ? 'rgba(255,112,67,0.2)' : 'rgba(255,179,0,0.15)', color: d.max_severity === 'Critical' ? '#FF5252' : d.max_severity === 'High' ? '#FF7043' : '#FFB300' }} />
                  </TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: 'text.secondary' }}>{d.behaviours_count ?? 0}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </Box>
    )

  // ── SentinelOne ───────────────────────────────────────────────────────────
  } else if (item.source_ref === 'sentinelone-agent-inventory') {
    const agents: any[] = raw.agents ?? []
    content = (
      <Box>
        <Box sx={{ display: 'flex', gap: 2, mb: 1, flexWrap: 'wrap' }}>
          <Typography variant="caption" color="text.secondary">Total: <strong>{raw.total_agents}</strong></Typography>
          <Typography variant="caption" sx={{ color: '#70AD47' }}>Active: <strong>{raw.active_agents}</strong></Typography>
          {raw.infected_agents > 0 && <Typography variant="caption" sx={{ color: '#FF7043' }}>Infected: <strong>{raw.infected_agents}</strong></Typography>}
          {raw.out_of_date_agents > 0 && <Typography variant="caption" sx={{ color: '#FFB300' }}>Out of date: <strong>{raw.out_of_date_agents}</strong></Typography>}
        </Box>
        <TableContainer sx={{ maxHeight: 240 }}>
          <Table size="small" stickyHeader>
            <TableHead>
              <TableRow>
                {['Hostname', 'OS', 'Status', 'Version', 'Last Seen'].map(h => (
                  <TableCell key={h} sx={{ fontSize: '0.6rem', fontWeight: 700, py: 0.5, bgcolor: 'rgba(0,0,0,0.4)' }}>{h}</TableCell>
                ))}
              </TableRow>
            </TableHead>
            <TableBody>
              {agents.map((a, i) => (
                <TableRow key={i} hover>
                  <TableCell sx={{ fontSize: '0.65rem', py: 0.4 }}>{a.hostname ?? a.computerName ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: 'text.secondary' }}>{a.os_type ?? a.osType ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4 }}>
                    <Chip label={a.is_active ? 'active' : 'inactive'} size="small"
                      sx={{ height: 15, fontSize: '0.55rem', bgcolor: a.is_active ? 'rgba(112,173,71,0.2)' : 'rgba(255,112,67,0.15)', color: a.is_active ? '#70AD47' : '#FF7043' }} />
                  </TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, fontFamily: 'monospace', color: 'text.secondary' }}>{a.agent_version ?? a.agentVersion ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: 'text.secondary' }}>{a.last_seen ?? a.lastActiveDatetime ? new Date(a.last_seen ?? a.lastActiveDatetime).toLocaleDateString() : '—'}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </Box>
    )

  // ── Wazuh ─────────────────────────────────────────────────────────────────
  } else if (item.source_ref === 'wazuh-agent-inventory') {
    const agents: any[] = raw.agents ?? []
    content = (
      <Box>
        <Box sx={{ display: 'flex', gap: 2, mb: 1, flexWrap: 'wrap' }}>
          <Typography variant="caption" color="text.secondary">Total: <strong>{raw.total_agents}</strong></Typography>
          <Typography variant="caption" sx={{ color: '#70AD47' }}>Active: <strong>{raw.active_agents}</strong></Typography>
          {raw.disconnected_agents > 0 && <Typography variant="caption" sx={{ color: '#FF7043' }}>Disconnected: <strong>{raw.disconnected_agents}</strong></Typography>}
        </Box>
        <TableContainer sx={{ maxHeight: 240 }}>
          <Table size="small" stickyHeader>
            <TableHead>
              <TableRow>
                {['Name', 'IP', 'OS', 'Status', 'Version', 'Last Keep-Alive'].map(h => (
                  <TableCell key={h} sx={{ fontSize: '0.6rem', fontWeight: 700, py: 0.5, bgcolor: 'rgba(0,0,0,0.4)' }}>{h}</TableCell>
                ))}
              </TableRow>
            </TableHead>
            <TableBody>
              {agents.map((a, i) => (
                <TableRow key={i} hover>
                  <TableCell sx={{ fontSize: '0.65rem', py: 0.4 }}>{a.name ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, fontFamily: 'monospace', color: 'text.secondary' }}>{a.ip ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: 'text.secondary' }}>{a.os_platform ?? a.os?.platform ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4 }}>
                    <Chip label={a.status ?? '—'} size="small"
                      sx={{ height: 15, fontSize: '0.55rem', bgcolor: a.status === 'active' ? 'rgba(112,173,71,0.2)' : 'rgba(255,112,67,0.15)', color: a.status === 'active' ? '#70AD47' : '#FF7043' }} />
                  </TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, fontFamily: 'monospace', color: 'text.secondary' }}>{a.version ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: 'text.secondary' }}>{a.lastKeepAlive ? new Date(a.lastKeepAlive).toLocaleDateString() : '—'}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </Box>
    )

  // ── Vulnerability management (generic pattern for Qualys/Tenable/OpenVAS) ──
  } else if (['qualys-vulnerability-summary', 'tenable-sc-vulnerability-summary', 'tenable-io-vulnerabilities', 'openvas-vulnerability-summary', 'defender-vulnerability-status', 'wazuh-vulnerabilities'].includes(item.source_ref ?? '')) {
    const bySev = raw.by_severity ?? {}
    const critRecs: any[] = raw.critical_recommendations ?? raw.critical_vulnerabilities ?? []
    content = (
      <Box>
        <Box sx={{ display: 'flex', gap: 2, mb: 1.5, flexWrap: 'wrap' }}>
          {['Critical','High','Medium','Low'].map(s => (
            <Box key={s} sx={{ display: 'flex', flexDirection: 'column', alignItems: 'center', px: 1.5, py: 0.5, borderRadius: 1, bgcolor: 'rgba(0,0,0,0.2)', border: '1px solid rgba(255,255,255,0.06)' }}>
              <Typography variant="caption" sx={{ fontSize: '0.6rem', color: s === 'Critical' ? '#FF5252' : s === 'High' ? '#FF7043' : s === 'Medium' ? '#FFB300' : '#9E9E9E' }}>
                {s}
              </Typography>
              <Typography variant="body2" fontWeight={700} sx={{ color: bySev[s] > 0 ? (s === 'Critical' ? '#FF5252' : s === 'High' ? '#FF7043' : s === 'Medium' ? '#FFB300' : '#9E9E9E') : 'text.disabled' }}>
                {bySev[s] ?? 0}
              </Typography>
            </Box>
          ))}
          {raw.total_recommendations != null && (
            <Typography variant="caption" color="text.secondary" sx={{ alignSelf: 'center' }}>
              Total: <strong>{raw.total_recommendations ?? raw.total_vulns ?? 0}</strong>
            </Typography>
          )}
        </Box>
        {critRecs.length > 0 && (
          <TableContainer sx={{ maxHeight: 200 }}>
            <Table size="small" stickyHeader>
              <TableHead>
                <TableRow>
                  {['Vulnerability / Recommendation', 'Exposed Devices', 'Remediation'].map(h => (
                    <TableCell key={h} sx={{ fontSize: '0.6rem', fontWeight: 700, py: 0.5, bgcolor: 'rgba(0,0,0,0.4)' }}>{h}</TableCell>
                  ))}
                </TableRow>
              </TableHead>
              <TableBody>
                {critRecs.map((r, i) => (
                  <TableRow key={i} hover>
                    <TableCell sx={{ fontSize: '0.65rem', py: 0.4 }}>{r.name ?? r.recommendationName ?? r.title ?? '—'}</TableCell>
                    <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: r.exposed_machines > 0 ? '#FF7043' : 'text.secondary' }}>{r.exposed_machines ?? r.exposedMachinesCount ?? '—'}</TableCell>
                    <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: 'text.secondary' }}>{r.remediation_type ?? r.remediationType ?? r.fix ?? '—'}</TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </TableContainer>
        )}
      </Box>
    )

  // ── ServiceNow ────────────────────────────────────────────────────────────
  } else if (['servicenow-incidents', 'servicenow-changes', 'servicenow-problems'].includes(item.source_ref ?? '')) {
    const tickets: any[] = raw.incidents ?? raw.changes ?? raw.problems ?? []
    const byPriority = raw.by_priority ?? raw.by_risk ?? {}
    content = (
      <Box>
        <Box sx={{ display: 'flex', gap: 2, mb: 1, flexWrap: 'wrap' }}>
          <Typography variant="caption" color="text.secondary">Open: <strong>{raw.open_count ?? tickets.length}</strong></Typography>
          {Object.entries(byPriority).map(([k, v]) => (
            <Typography key={k} variant="caption" color="text.secondary">{k}: <strong>{v as number}</strong></Typography>
          ))}
        </Box>
        <TableContainer sx={{ maxHeight: 240 }}>
          <Table size="small" stickyHeader>
            <TableHead>
              <TableRow>
                {['Number', 'Short Description', 'Priority', 'State', 'Opened'].map(h => (
                  <TableCell key={h} sx={{ fontSize: '0.6rem', fontWeight: 700, py: 0.5, bgcolor: 'rgba(0,0,0,0.4)' }}>{h}</TableCell>
                ))}
              </TableRow>
            </TableHead>
            <TableBody>
              {tickets.map((t, i) => (
                <TableRow key={i} hover>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, fontFamily: 'monospace' }}>{t.number ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.65rem', py: 0.4 }}>{t.short_description ?? t.title ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4 }}>
                    <Chip label={t.priority ?? '—'} size="small"
                      sx={{ height: 15, fontSize: '0.55rem', bgcolor: t.priority === '1 - Critical' || t.priority === '1' ? 'rgba(255,82,82,0.2)' : 'rgba(255,179,0,0.15)', color: t.priority === '1 - Critical' || t.priority === '1' ? '#FF5252' : '#FFB300' }} />
                  </TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: 'text.secondary' }}>{t.state ?? t.incident_state ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: 'text.secondary' }}>{t.opened_at ? new Date(t.opened_at).toLocaleDateString() : '—'}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </Box>
    )

  // ── Jira ──────────────────────────────────────────────────────────────────
  } else if (['jira-open-issues', 'jira-open-tickets', 'jira-security-issues'].includes(item.source_ref ?? '')) {
    const issues: any[] = raw.issues ?? []
    content = (
      <Box>
        <Box sx={{ display: 'flex', gap: 2, mb: 1, flexWrap: 'wrap' }}>
          <Typography variant="caption" color="text.secondary">Open: <strong>{raw.open_count ?? issues.length}</strong></Typography>
          {Object.entries(raw.by_priority ?? {}).map(([k, v]) => (
            <Typography key={k} variant="caption" color="text.secondary">{k}: <strong>{v as number}</strong></Typography>
          ))}
        </Box>
        <TableContainer sx={{ maxHeight: 240 }}>
          <Table size="small" stickyHeader>
            <TableHead>
              <TableRow>
                {['Key', 'Summary', 'Priority', 'Status', 'Project'].map(h => (
                  <TableCell key={h} sx={{ fontSize: '0.6rem', fontWeight: 700, py: 0.5, bgcolor: 'rgba(0,0,0,0.4)' }}>{h}</TableCell>
                ))}
              </TableRow>
            </TableHead>
            <TableBody>
              {issues.map((iss, i) => (
                <TableRow key={i} hover>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, fontFamily: 'monospace' }}>{iss.key ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.65rem', py: 0.4 }}>{iss.summary ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4 }}>
                    <Chip label={iss.priority ?? '—'} size="small"
                      sx={{ height: 15, fontSize: '0.55rem', bgcolor: iss.priority === 'Critical' || iss.priority === 'Blocker' ? 'rgba(255,82,82,0.2)' : 'rgba(255,179,0,0.15)', color: iss.priority === 'Critical' || iss.priority === 'Blocker' ? '#FF5252' : '#FFB300' }} />
                  </TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: 'text.secondary' }}>{iss.status ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: 'text.secondary' }}>{iss.project ?? '—'}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </Box>
    )

  // ── Zabbix / PRTG host inventory ──────────────────────────────────────────
  } else if (['zabbix-host-inventory', 'prtg-device-inventory', 'netbox-device-inventory', 'glpi-asset-inventory'].includes(item.source_ref ?? '')) {
    const hosts: any[] = raw.hosts ?? raw.devices ?? raw.assets ?? []
    content = (
      <Box>
        <Box sx={{ display: 'flex', gap: 2, mb: 1, flexWrap: 'wrap' }}>
          <Typography variant="caption" color="text.secondary">Total: <strong>{raw.total_hosts ?? raw.total_devices ?? hosts.length}</strong></Typography>
          {raw.enabled != null && <Typography variant="caption" sx={{ color: '#70AD47' }}>Enabled: <strong>{raw.enabled}</strong></Typography>}
          {raw.problems != null && raw.problems > 0 && <Typography variant="caption" sx={{ color: '#FF7043' }}>Problems: <strong>{raw.problems}</strong></Typography>}
        </Box>
        <TableContainer sx={{ maxHeight: 240 }}>
          <Table size="small" stickyHeader>
            <TableHead>
              <TableRow>
                {['Name', 'IP / Address', 'Status', 'Type / OS', 'Last Check'].map(h => (
                  <TableCell key={h} sx={{ fontSize: '0.6rem', fontWeight: 700, py: 0.5, bgcolor: 'rgba(0,0,0,0.4)' }}>{h}</TableCell>
                ))}
              </TableRow>
            </TableHead>
            <TableBody>
              {hosts.map((h, i) => (
                <TableRow key={i} hover>
                  <TableCell sx={{ fontSize: '0.65rem', py: 0.4 }}>{h.name ?? h.hostname ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, fontFamily: 'monospace', color: 'text.secondary' }}>{h.ip ?? h.host ?? h.primary_ip ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4 }}>
                    <Chip label={h.status ?? h.health ?? (h.active ? 'active' : 'inactive')} size="small"
                      sx={{ height: 15, fontSize: '0.55rem', bgcolor: (h.status === 'active' || h.active || h.status === '0') ? 'rgba(112,173,71,0.2)' : 'rgba(255,112,67,0.15)', color: (h.status === 'active' || h.active) ? '#70AD47' : '#FF7043' }} />
                  </TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: 'text.secondary' }}>{h.os ?? h.type ?? h.device_type ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: 'text.secondary' }}>{h.last_check ?? h.last_seen ?? h.last_updated ? new Date(h.last_check ?? h.last_seen ?? h.last_updated).toLocaleDateString() : '—'}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </Box>
    )

  // ── GitHub / GitLab repos ─────────────────────────────────────────────────
  } else if (['github-repo-inventory', 'gitlab-repo-inventory'].includes(item.source_ref ?? '')) {
    const repos: any[] = raw.repos ?? []
    content = (
      <Box>
        <Box sx={{ display: 'flex', gap: 2, mb: 1, flexWrap: 'wrap' }}>
          <Typography variant="caption" color="text.secondary">Total: <strong>{raw.total_repos ?? repos.length}</strong></Typography>
          {raw.private_repos != null && <Typography variant="caption" color="text.secondary">Private: <strong>{raw.private_repos}</strong></Typography>}
          {raw.public_repos != null && <Typography variant="caption" sx={{ color: '#FFB300' }}>Public: <strong>{raw.public_repos}</strong></Typography>}
          {raw.archived_repos != null && raw.archived_repos > 0 && <Typography variant="caption" color="text.secondary">Archived: <strong>{raw.archived_repos}</strong></Typography>}
        </Box>
        <TableContainer sx={{ maxHeight: 240 }}>
          <Table size="small" stickyHeader>
            <TableHead>
              <TableRow>
                {['Repository', 'Visibility', 'Language', 'Default Branch', 'Last Push'].map(h => (
                  <TableCell key={h} sx={{ fontSize: '0.6rem', fontWeight: 700, py: 0.5, bgcolor: 'rgba(0,0,0,0.4)' }}>{h}</TableCell>
                ))}
              </TableRow>
            </TableHead>
            <TableBody>
              {repos.map((r, i) => (
                <TableRow key={i} hover>
                  <TableCell sx={{ fontSize: '0.65rem', py: 0.4 }}>{r.name ?? r.full_name ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4 }}>
                    <Chip label={r.private ? 'private' : 'public'} size="small"
                      sx={{ height: 15, fontSize: '0.55rem', bgcolor: r.private ? 'rgba(112,173,71,0.2)' : 'rgba(255,179,0,0.2)', color: r.private ? '#70AD47' : '#FFB300' }} />
                  </TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: 'text.secondary' }}>{r.language ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, fontFamily: 'monospace', color: 'text.secondary' }}>{r.default_branch ?? 'main'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: 'text.secondary' }}>{r.pushed_at ? new Date(r.pushed_at).toLocaleDateString() : '—'}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </Box>
    )

  // ── GitHub / GitLab security alerts ──────────────────────────────────────
  } else if (['github-vulnerability-findings', 'gitlab-vulnerability-findings', 'github-secret-scanning', 'github-code-scanning'].includes(item.source_ref ?? '')) {
    const alerts: any[] = raw.alerts ?? []
    const bySev = raw.by_severity ?? {}
    content = (
      <Box>
        <Box sx={{ display: 'flex', gap: 2, mb: 1, flexWrap: 'wrap' }}>
          <Typography variant="caption" color="text.secondary">Open: <strong>{raw.open_alerts ?? alerts.length}</strong></Typography>
          {['critical','high','medium','low'].map(s => bySev[s] > 0 ? (
            <Typography key={s} variant="caption" sx={{ color: s === 'critical' ? '#FF5252' : s === 'high' ? '#FF7043' : '#FFB300' }}>
              {s}: <strong>{bySev[s]}</strong>
            </Typography>
          ) : null)}
        </Box>
        {alerts.length > 0 && (
          <TableContainer sx={{ maxHeight: 240 }}>
            <Table size="small" stickyHeader>
              <TableHead>
                <TableRow>
                  {['Alert', 'Severity', 'Repository', 'State'].map(h => (
                    <TableCell key={h} sx={{ fontSize: '0.6rem', fontWeight: 700, py: 0.5, bgcolor: 'rgba(0,0,0,0.4)' }}>{h}</TableCell>
                  ))}
                </TableRow>
              </TableHead>
              <TableBody>
                {alerts.map((a, i) => (
                  <TableRow key={i} hover>
                    <TableCell sx={{ fontSize: '0.65rem', py: 0.4 }}>{a.rule?.description ?? a.secret_type_display_name ?? a.title ?? '—'}</TableCell>
                    <TableCell sx={{ fontSize: '0.6rem', py: 0.4 }}>
                      <Chip label={a.rule?.severity ?? a.severity ?? '—'} size="small"
                        sx={{ height: 15, fontSize: '0.55rem', bgcolor: (a.rule?.severity ?? a.severity) === 'critical' ? 'rgba(255,82,82,0.2)' : 'rgba(255,112,67,0.2)', color: (a.rule?.severity ?? a.severity) === 'critical' ? '#FF5252' : '#FF7043' }} />
                    </TableCell>
                    <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: 'text.secondary' }}>{a.repository?.name ?? a.project?.name ?? '—'}</TableCell>
                    <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: 'text.secondary' }}>{a.state ?? '—'}</TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </TableContainer>
        )}
      </Box>
    )

  // ── CyberArk accounts ─────────────────────────────────────────────────────
  } else if (item.source_ref === 'cyberark-accounts') {
    const accounts: any[] = raw.accounts ?? []
    content = (
      <Box>
        <Box sx={{ display: 'flex', gap: 2, mb: 1, flexWrap: 'wrap' }}>
          <Typography variant="caption" color="text.secondary">Total: <strong>{raw.total_accounts ?? accounts.length}</strong></Typography>
          {Object.entries(raw.by_platform ?? {}).slice(0, 4).map(([k, v]) => (
            <Typography key={k} variant="caption" color="text.secondary">{k}: <strong>{v as number}</strong></Typography>
          ))}
        </Box>
        <TableContainer sx={{ maxHeight: 240 }}>
          <Table size="small" stickyHeader>
            <TableHead>
              <TableRow>
                {['Username', 'Address', 'Platform', 'Safe', 'Status'].map(h => (
                  <TableCell key={h} sx={{ fontSize: '0.6rem', fontWeight: 700, py: 0.5, bgcolor: 'rgba(0,0,0,0.4)' }}>{h}</TableCell>
                ))}
              </TableRow>
            </TableHead>
            <TableBody>
              {accounts.map((a, i) => (
                <TableRow key={i} hover>
                  <TableCell sx={{ fontSize: '0.65rem', py: 0.4 }}>{a.username ?? a.userName ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: 'text.secondary' }}>{a.address ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: 'text.secondary' }}>{a.platform_id ?? a.platformId ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: 'text.secondary' }}>{a.safe_name ?? a.safeName ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: 'text.secondary' }}>{a.status ?? '—'}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </Box>
    )

  // ── Devolutions Server connection inventory ───────────────────────────────
  } else if (item.source_ref === 'dvls-connection-inventory') {
    const connections: any[] = raw.connections ?? []
    content = (
      <Box>
        <Box sx={{ display: 'flex', gap: 2, mb: 1, flexWrap: 'wrap' }}>
          <Typography variant="caption" color="text.secondary">Total: <strong>{raw.total_connection_count ?? connections.length}</strong></Typography>
          <Typography variant="caption" color="text.secondary">Privileged: <strong>{raw.privileged_count ?? 0}</strong></Typography>
          {Object.entries(raw.by_type ?? {}).slice(0, 4).map(([k, v]) => (
            <Typography key={k} variant="caption" color="text.secondary">{k}: <strong>{v as number}</strong></Typography>
          ))}
        </Box>
        <TableContainer sx={{ maxHeight: 240 }}>
          <Table size="small" stickyHeader>
            <TableHead>
              <TableRow>
                {['Name', 'Type', 'Host', 'Username', 'Group'].map(h => (
                  <TableCell key={h} sx={{ fontSize: '0.6rem', fontWeight: 700, py: 0.5, bgcolor: 'rgba(0,0,0,0.4)' }}>{h}</TableCell>
                ))}
              </TableRow>
            </TableHead>
            <TableBody>
              {connections.map((c: any, i: number) => (
                <TableRow key={i} hover>
                  <TableCell sx={{ fontSize: '0.65rem', py: 0.4 }}>{c.name ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: 'text.secondary' }}>{c.connection_type ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: 'text.secondary' }}>{c.host ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: 'text.secondary' }}>{c.username ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: 'text.secondary' }}>{c.group ?? '—'}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </Box>
    )

  // ── Devolutions Server user directory ─────────────────────────────────────
  } else if (item.source_ref === 'dvls-user-directory') {
    const users: any[] = raw.users ?? []
    content = (
      <Box>
        <Box sx={{ display: 'flex', gap: 2, mb: 1, flexWrap: 'wrap' }}>
          <Typography variant="caption" color="text.secondary">Total: <strong>{raw.total_user_count ?? users.length}</strong></Typography>
          <Typography variant="caption" color="text.secondary">Active: <strong>{raw.active_user_count ?? 0}</strong></Typography>
          <Typography variant="caption" color="text.secondary">MFA enabled: <strong style={{ color: '#C6EFCE' }}>{raw.mfa_enabled_count ?? 0}</strong></Typography>
          <Typography variant="caption" color="text.secondary">Groups: <strong>{raw.group_count ?? 0}</strong></Typography>
        </Box>
        <TableContainer sx={{ maxHeight: 240 }}>
          <Table size="small" stickyHeader>
            <TableHead>
              <TableRow>
                {['Username', 'Display Name', 'Email', 'Type', 'MFA', 'Disabled'].map(h => (
                  <TableCell key={h} sx={{ fontSize: '0.6rem', fontWeight: 700, py: 0.5, bgcolor: 'rgba(0,0,0,0.4)' }}>{h}</TableCell>
                ))}
              </TableRow>
            </TableHead>
            <TableBody>
              {users.map((u: any, i: number) => (
                <TableRow key={i} hover>
                  <TableCell sx={{ fontSize: '0.65rem', py: 0.4 }}>{u.username ?? u.userName ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4 }}>{u.display_name ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: 'text.secondary' }}>{u.email ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: 'text.secondary' }}>{u.user_type ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4 }}>
                    <Typography variant="caption" sx={{ color: u.mfa_enabled ? '#C6EFCE' : '#FFC7CE' }}>{u.mfa_enabled ? 'Yes' : 'No'}</Typography>
                  </TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: u.is_disabled ? '#FFC7CE' : 'text.secondary' }}>{u.is_disabled ? 'Yes' : 'No'}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </Box>
    )

  // ── Devolutions Server admin users ────────────────────────────────────────
  } else if (item.source_ref === 'dvls-admin-users') {
    const admins: any[] = raw.admin_users ?? []
    const groups: any[] = raw.groups ?? []
    content = (
      <Box>
        <Box sx={{ display: 'flex', gap: 2, mb: 1, flexWrap: 'wrap' }}>
          <Typography variant="caption" color="text.secondary">Total users: <strong>{raw.total_user_count ?? 0}</strong></Typography>
          <Typography variant="caption" color="text.secondary">Admins: <strong>{raw.admin_count ?? admins.length}</strong></Typography>
          <Typography variant="caption" color="text.secondary">Groups: <strong>{raw.group_count ?? groups.length}</strong></Typography>
        </Box>
        <TableContainer sx={{ maxHeight: 200 }}>
          <Table size="small" stickyHeader>
            <TableHead>
              <TableRow>
                {['Username', 'Role', 'Email'].map(h => (
                  <TableCell key={h} sx={{ fontSize: '0.6rem', fontWeight: 700, py: 0.5, bgcolor: 'rgba(0,0,0,0.4)' }}>{h}</TableCell>
                ))}
              </TableRow>
            </TableHead>
            <TableBody>
              {admins.map((u: any, i: number) => (
                <TableRow key={i} hover>
                  <TableCell sx={{ fontSize: '0.65rem', py: 0.4 }}>{u.username ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: 'text.secondary' }}>{u.role ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: 'text.secondary' }}>{u.email ?? '—'}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </Box>
    )

  // ── Devolutions Server activity log ───────────────────────────────────────
  } else if (item.source_ref === 'dvls-activity-log') {
    const events: any[] = raw.recent_events ?? []
    const sessions: any[] = raw.active_sessions ?? []
    content = (
      <Box>
        <Box sx={{ display: 'flex', gap: 2, mb: 1, flexWrap: 'wrap' }}>
          <Typography variant="caption" color="text.secondary">Log entries: <strong>{raw.total_log_count ?? events.length}</strong></Typography>
          <Typography variant="caption" color="text.secondary">Active sessions: <strong>{raw.active_session_count ?? sessions.length}</strong></Typography>
          {Object.entries(raw.event_types ?? {}).slice(0, 3).map(([k, v]) => (
            <Typography key={k} variant="caption" color="text.secondary">{k}: <strong>{v as number}</strong></Typography>
          ))}
        </Box>
        <TableContainer sx={{ maxHeight: 240 }}>
          <Table size="small" stickyHeader>
            <TableHead>
              <TableRow>
                {['Time', 'Event Type', 'Username', 'IP Address', 'Message'].map(h => (
                  <TableCell key={h} sx={{ fontSize: '0.6rem', fontWeight: 700, py: 0.5, bgcolor: 'rgba(0,0,0,0.4)' }}>{h}</TableCell>
                ))}
              </TableRow>
            </TableHead>
            <TableBody>
              {events.map((e: any, i: number) => (
                <TableRow key={i} hover>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: 'text.secondary', whiteSpace: 'nowrap' }}>
                    {e.log_time ? new Date(e.log_time).toLocaleString() : '—'}
                  </TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4 }}>{e.event_type ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.65rem', py: 0.4 }}>{e.username ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: 'text.secondary' }}>{e.ip_address ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: 'text.secondary', maxWidth: 200 }} title={e.message}>
                    {e.message ? String(e.message).slice(0, 60) + (String(e.message).length > 60 ? '…' : '') : '—'}
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </Box>
    )

  // ── Microsoft 365 — Security Alerts ──────────────────────────────────────
  } else if (item.source_ref === 'm365-security-alerts') {
    const alerts: any[] = raw.recent_alerts ?? []
    const sevMap: Record<string, string> = { high: '#FFC7CE', medium: '#FFEB9C', low: '#C6EFCE', informational: '#BDD7EE' }
    content = (
      <Box>
        <Box sx={{ display: 'flex', gap: 2, mb: 1, flexWrap: 'wrap' }}>
          <Typography variant="caption" color="text.secondary">Total: <strong>{raw.total_alerts ?? alerts.length}</strong></Typography>
          {raw.high_severity_count !== undefined && <Typography variant="caption" sx={{ color: '#FFC7CE' }}>High: <strong>{raw.high_severity_count}</strong></Typography>}
          {raw.medium_severity_count !== undefined && <Typography variant="caption" sx={{ color: '#FFEB9C' }}>Medium: <strong>{raw.medium_severity_count}</strong></Typography>}
          {raw.statuses && Object.entries(raw.statuses).map(([k, v]) => (
            <Typography key={k} variant="caption" color="text.secondary">{k}: <strong>{v as number}</strong></Typography>
          ))}
        </Box>
        <TableContainer sx={{ maxHeight: 240 }}>
          <Table size="small" stickyHeader>
            <TableHead>
              <TableRow>
                {['Title', 'Severity', 'Status', 'Category', 'Created'].map(h => (
                  <TableCell key={h} sx={{ fontSize: '0.6rem', fontWeight: 700, py: 0.5, bgcolor: 'rgba(0,0,0,0.4)' }}>{h}</TableCell>
                ))}
              </TableRow>
            </TableHead>
            <TableBody>
              {alerts.map((a: any, i: number) => (
                <TableRow key={i} hover>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, maxWidth: 200 }} title={a.title}>{String(a.title ?? '—').slice(0, 50)}{String(a.title ?? '').length > 50 ? '…' : ''}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4 }}>
                    <Chip label={a.severity ?? '—'} size="small" sx={{ fontSize: '0.55rem', height: 16, bgcolor: `${sevMap[a.severity] ?? '#BDD7EE'}22`, color: sevMap[a.severity] ?? '#BDD7EE' }} />
                  </TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: 'text.secondary' }}>{a.status ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: 'text.secondary' }}>{a.category ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: 'text.secondary', whiteSpace: 'nowrap' }}>
                    {a.created_at ? new Date(a.created_at).toLocaleDateString() : '—'}
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </Box>
    )

  // ── Microsoft 365 — Conditional Access Policies ───────────────────────────
  } else if (item.source_ref === 'm365-conditional-access') {
    const policies: any[] = raw.policies ?? []
    content = (
      <Box>
        <Box sx={{ display: 'flex', gap: 2, mb: 1, flexWrap: 'wrap' }}>
          <Typography variant="caption" color="text.secondary">Total: <strong>{raw.total ?? policies.length}</strong></Typography>
          {raw.enabled !== undefined && <Typography variant="caption" sx={{ color: '#C6EFCE' }}>Enabled: <strong>{raw.enabled}</strong></Typography>}
          {raw.reporting_only !== undefined && <Typography variant="caption" sx={{ color: '#FFEB9C' }}>Report-only: <strong>{raw.reporting_only}</strong></Typography>}
          {raw.disabled !== undefined && <Typography variant="caption" sx={{ color: '#FFC7CE' }}>Disabled: <strong>{raw.disabled}</strong></Typography>}
        </Box>
        <TableContainer sx={{ maxHeight: 240 }}>
          <Table size="small" stickyHeader>
            <TableHead>
              <TableRow>
                {['Policy Name', 'State', 'Created'].map(h => (
                  <TableCell key={h} sx={{ fontSize: '0.6rem', fontWeight: 700, py: 0.5, bgcolor: 'rgba(0,0,0,0.4)' }}>{h}</TableCell>
                ))}
              </TableRow>
            </TableHead>
            <TableBody>
              {policies.map((p: any, i: number) => (
                <TableRow key={i} hover>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, maxWidth: 260 }}>{p.display_name ?? p.name ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4 }}>
                    <Chip label={p.state ?? '—'} size="small" sx={{ fontSize: '0.55rem', height: 16,
                      bgcolor: p.state === 'enabled' ? '#C6EFCE22' : p.state === 'enabledForReportingButNotEnforced' ? '#FFEB9C22' : '#FFC7CE22',
                      color: p.state === 'enabled' ? '#C6EFCE' : p.state === 'enabledForReportingButNotEnforced' ? '#FFEB9C' : '#FFC7CE',
                    }} />
                  </TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: 'text.secondary' }}>
                    {p.created_date_time ? new Date(p.created_date_time).toLocaleDateString() : '—'}
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </Box>
    )

  // ── Azure CSPM — Security Assessments ────────────────────────────────────
  } else if (item.source_ref?.startsWith('azure-cspm-assessments')) {
    const subs: any[] = raw.subscriptions ?? []
    content = (
      <Box>
        <Box sx={{ display: 'flex', gap: 2, mb: 1, flexWrap: 'wrap' }}>
          <Typography variant="caption" color="text.secondary">Subscriptions: <strong>{raw.subscription_count ?? subs.length}</strong></Typography>
          {raw.total_unhealthy !== undefined && <Typography variant="caption" sx={{ color: '#FFC7CE' }}>Unhealthy: <strong>{raw.total_unhealthy}</strong></Typography>}
          {raw.total_healthy !== undefined && <Typography variant="caption" sx={{ color: '#C6EFCE' }}>Healthy: <strong>{raw.total_healthy}</strong></Typography>}
        </Box>
        <TableContainer sx={{ maxHeight: 240 }}>
          <Table size="small" stickyHeader>
            <TableHead>
              <TableRow>
                {['Subscription', 'Healthy', 'Unhealthy', 'Skipped', 'Total'].map(h => (
                  <TableCell key={h} sx={{ fontSize: '0.6rem', fontWeight: 700, py: 0.5, bgcolor: 'rgba(0,0,0,0.4)' }}>{h}</TableCell>
                ))}
              </TableRow>
            </TableHead>
            <TableBody>
              {subs.map((s: any, i: number) => (
                <TableRow key={i} hover>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, maxWidth: 160 }}>{s.subscription_name ?? s.subscription_id?.slice(0, 8) ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: '#C6EFCE' }}>{s.healthy ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: '#FFC7CE' }}>{s.unhealthy ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: 'text.secondary' }}>{s.skipped ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4 }}>{s.total ?? '—'}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </Box>
    )

  // ── Azure CSPM — Security Alerts ─────────────────────────────────────────
  } else if (item.source_ref?.startsWith('azure-cspm-alerts')) {
    const subs: any[] = raw.subscriptions ?? []
    const sevMap: Record<string, string> = { High: '#FFC7CE', Medium: '#FFEB9C', Low: '#C6EFCE', Informational: '#BDD7EE' }
    content = (
      <Box>
        <Box sx={{ display: 'flex', gap: 2, mb: 1, flexWrap: 'wrap' }}>
          <Typography variant="caption" color="text.secondary">Total alerts: <strong>{raw.total_alerts}</strong></Typography>
          {raw.high_count !== undefined && <Typography variant="caption" sx={{ color: '#FFC7CE' }}>High: <strong>{raw.high_count}</strong></Typography>}
          {raw.medium_count !== undefined && <Typography variant="caption" sx={{ color: '#FFEB9C' }}>Medium: <strong>{raw.medium_count}</strong></Typography>}
        </Box>
        <TableContainer sx={{ maxHeight: 240 }}>
          <Table size="small" stickyHeader>
            <TableHead>
              <TableRow>
                {['Subscription', 'High', 'Medium', 'Low', 'Total'].map(h => (
                  <TableCell key={h} sx={{ fontSize: '0.6rem', fontWeight: 700, py: 0.5, bgcolor: 'rgba(0,0,0,0.4)' }}>{h}</TableCell>
                ))}
              </TableRow>
            </TableHead>
            <TableBody>
              {subs.map((s: any, i: number) => (
                <TableRow key={i} hover>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4 }}>{s.subscription_name ?? s.subscription_id?.slice(0, 8) ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: '#FFC7CE' }}>{s.by_severity?.High ?? 0}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: '#FFEB9C' }}>{s.by_severity?.Medium ?? 0}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: '#C6EFCE' }}>{s.by_severity?.Low ?? 0}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4 }}>{s.alert_count ?? '—'}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </Box>
    )

  // ── Azure CSPM — Network Security Assessments ────────────────────────────
  } else if (item.source_ref?.startsWith('azure-cspm-network')) {
    const issues: any[] = raw.network_issues ?? []
    content = (
      <Box>
        <Box sx={{ display: 'flex', gap: 2, mb: 1, flexWrap: 'wrap' }}>
          <Typography variant="caption" color="text.secondary">Subscription: <strong>{raw.subscription_name ?? raw.subscription_id ?? '—'}</strong></Typography>
          <Typography variant="caption" color="text.secondary">Total assessments: <strong>{raw.total_network_assessments ?? '—'}</strong></Typography>
          {raw.unhealthy_network_assessments !== undefined && (
            <Typography variant="caption" sx={{ color: raw.unhealthy_network_assessments > 0 ? '#FFC7CE' : '#C6EFCE' }}>
              Unhealthy: <strong>{raw.unhealthy_network_assessments}</strong>
            </Typography>
          )}
        </Box>
        {issues.length === 0 ? (
          <Typography variant="caption" sx={{ color: '#C6EFCE' }}>No network security issues found.</Typography>
        ) : (
          <TableContainer sx={{ maxHeight: 240 }}>
            <Table size="small" stickyHeader>
              <TableHead>
                <TableRow>
                  {['Issue', 'Status'].map(h => (
                    <TableCell key={h} sx={{ fontSize: '0.6rem', fontWeight: 700, py: 0.5, bgcolor: 'rgba(0,0,0,0.4)' }}>{h}</TableCell>
                  ))}
                </TableRow>
              </TableHead>
              <TableBody>
                {issues.map((issue: any, i: number) => (
                  <TableRow key={i} hover>
                    <TableCell sx={{ fontSize: '0.6rem', py: 0.4, maxWidth: 400 }}>
                      {issue.display_name ?? issue.name ?? '—'}
                    </TableCell>
                    <TableCell sx={{ fontSize: '0.6rem', py: 0.4 }}>
                      <Chip
                        label={issue.status_code ?? '—'}
                        size="small"
                        sx={{
                          fontSize: '0.55rem', height: 16,
                          bgcolor: issue.status_code === 'unhealthy' ? '#FFC7CE22' : '#C6EFCE22',
                          color: issue.status_code === 'unhealthy' ? '#FFC7CE' : '#C6EFCE',
                        }}
                      />
                    </TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </TableContainer>
        )}
      </Box>
    )

  // ── SIEM — Alert Log ─────────────────────────────────────────────────────
  } else if (item.source_ref === 'siem-alert-log') {
    const alerts: any[] = raw.recent_alerts ?? []
    const sevMap: Record<string, string> = { critical: '#FFC7CE', high: '#FFC7CE', medium: '#FFEB9C', low: '#C6EFCE', info: '#BDD7EE' }
    content = (
      <Box>
        <Box sx={{ display: 'flex', gap: 2, mb: 1, flexWrap: 'wrap' }}>
          <Typography variant="caption" color="text.secondary">Total: <strong>{raw.total_alerts ?? alerts.length}</strong></Typography>
          {raw.by_severity && Object.entries(raw.by_severity).map(([k, v]) => (
            <Typography key={k} variant="caption" sx={{ color: sevMap[k] ?? 'text.secondary' }}>{k}: <strong>{v as number}</strong></Typography>
          ))}
        </Box>
        <TableContainer sx={{ maxHeight: 240 }}>
          <Table size="small" stickyHeader>
            <TableHead>
              <TableRow>
                {['Title', 'Severity', 'Category', 'Source', 'Time'].map(h => (
                  <TableCell key={h} sx={{ fontSize: '0.6rem', fontWeight: 700, py: 0.5, bgcolor: 'rgba(0,0,0,0.4)' }}>{h}</TableCell>
                ))}
              </TableRow>
            </TableHead>
            <TableBody>
              {alerts.map((a: any, i: number) => (
                <TableRow key={i} hover>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, maxWidth: 200 }}>{String(a.title ?? a.name ?? '—').slice(0, 50)}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4 }}>
                    <Chip label={a.severity ?? '—'} size="small" sx={{ fontSize: '0.55rem', height: 16, bgcolor: `${sevMap[a.severity] ?? '#BDD7EE'}22`, color: sevMap[a.severity] ?? '#BDD7EE' }} />
                  </TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: 'text.secondary' }}>{a.category ?? a.rule_name ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: 'text.secondary' }}>{a.source ?? a.host ?? '—'}</TableCell>
                  <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: 'text.secondary', whiteSpace: 'nowrap' }}>
                    {a.timestamp ? new Date(a.timestamp).toLocaleDateString() : '—'}
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </Box>
    )

  // ── Threat Intelligence — Indicators ─────────────────────────────────────
  } else if (item.source_ref === 'threat-intel-indicators') {
    const byType: Record<string, number> = raw.by_type ?? {}
    content = (
      <Box>
        <Box sx={{ display: 'flex', gap: 2, mb: 1.5, flexWrap: 'wrap' }}>
          <Typography variant="caption" color="text.secondary">Total indicators: <strong>{raw.total_indicators ?? 0}</strong></Typography>
          {raw.feed_type && <Typography variant="caption" color="text.secondary">Feed: <strong>{raw.feed_type}</strong></Typography>}
          {raw.collection_id && <Typography variant="caption" color="text.secondary">Collection: <strong>{raw.collection_id}</strong></Typography>}
        </Box>
        <Box sx={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(140px, 1fr))', gap: 0.75 }}>
          {Object.entries(byType).map(([type, count]) => (
            <Box key={type} sx={{ p: 0.75, borderRadius: 1, bgcolor: 'rgba(0,0,0,0.2)', border: '1px solid rgba(255,255,255,0.06)' }}>
              <Typography variant="caption" color="text.disabled" sx={{ fontSize: '0.58rem', display: 'block', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
                {type.replace(/-/g, ' ')}
              </Typography>
              <Typography variant="body2" fontWeight={700} sx={{ fontSize: '0.8rem' }}>{count}</Typography>
            </Box>
          ))}
        </Box>
      </Box>
    )

  // ── M365 Secure Score ─────────────────────────────────────────────────────
  } else if (item.source_ref === 'm365-secure-score') {
    const controls: any[] = raw.top_controls ?? []
    content = (
      <Box>
        <Box sx={{ display: 'flex', gap: 2, mb: 1, flexWrap: 'wrap' }}>
          <Typography variant="caption" color="text.secondary">Score: <strong>{raw.current_score}/{raw.max_score}</strong></Typography>
          {raw.percentage_score !== undefined && <Typography variant="caption" sx={{ color: raw.percentage_score >= 70 ? '#C6EFCE' : raw.percentage_score >= 40 ? '#FFEB9C' : '#FFC7CE' }}>
            {raw.percentage_score?.toFixed(1)}%
          </Typography>}
        </Box>
        {controls.length > 0 && (
          <TableContainer sx={{ maxHeight: 240 }}>
            <Table size="small" stickyHeader>
              <TableHead>
                <TableRow>
                  {['Control', 'Category', 'Score'].map(h => (
                    <TableCell key={h} sx={{ fontSize: '0.6rem', fontWeight: 700, py: 0.5, bgcolor: 'rgba(0,0,0,0.4)' }}>{h}</TableCell>
                  ))}
                </TableRow>
              </TableHead>
              <TableBody>
                {controls.map((c: any, i: number) => (
                  <TableRow key={i} hover>
                    <TableCell sx={{ fontSize: '0.6rem', py: 0.4, maxWidth: 220 }}>{c.control_name ?? '—'}</TableCell>
                    <TableCell sx={{ fontSize: '0.6rem', py: 0.4, color: 'text.secondary' }}>{c.control_category ?? '—'}</TableCell>
                    <TableCell sx={{ fontSize: '0.6rem', py: 0.4, fontWeight: 600 }}>{c.score ?? '—'}</TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </TableContainer>
        )}
      </Box>
    )

  // ── Azure CSPM — Secure Score ─────────────────────────────────────────────
  } else if (item.source_ref?.startsWith('azure-cspm-secure-score')) {
    const pct: number = raw.percentage ?? 0
    const scoreColor = pct >= 70 ? '#C6EFCE' : pct >= 40 ? '#FFEB9C' : '#FFC7CE'
    const scoreLabel = pct >= 70 ? 'Good' : pct >= 40 ? 'Needs improvement' : 'At risk'
    content = (
      <Box sx={{ display: 'flex', flexDirection: 'column', gap: 1.5 }}>
        <Box sx={{ display: 'flex', gap: 3, flexWrap: 'wrap', alignItems: 'center' }}>
          {/* Big score number */}
          <Box sx={{ textAlign: 'center' }}>
            <Typography sx={{ fontSize: '2rem', fontWeight: 700, lineHeight: 1, color: scoreColor }}>
              {pct.toFixed(1)}%
            </Typography>
            <Typography variant="caption" sx={{ color: scoreColor, fontSize: '0.6rem' }}>{scoreLabel}</Typography>
          </Box>
          {/* Score breakdown */}
          <Box sx={{ flex: 1, minWidth: 160 }}>
            <Box sx={{ display: 'flex', justifyContent: 'space-between', mb: 0.5 }}>
              <Typography variant="caption" color="text.secondary" sx={{ fontSize: '0.6rem' }}>
                {raw.subscription_name ?? raw.subscription_id ?? '—'}
              </Typography>
              <Typography variant="caption" sx={{ fontSize: '0.6rem', color: scoreColor, fontWeight: 600 }}>
                {raw.current}/{raw.max} pts
              </Typography>
            </Box>
            <LinearProgress
              variant="determinate"
              value={Math.min(100, pct)}
              sx={{
                height: 8, borderRadius: 4,
                bgcolor: 'rgba(255,255,255,0.08)',
                '& .MuiLinearProgress-bar': { bgcolor: scoreColor, borderRadius: 4 },
              }}
            />
            {raw.initiative_name && (
              <Typography variant="caption" color="text.disabled" sx={{ fontSize: '0.57rem', mt: 0.4, display: 'block' }}>
                Initiative: {raw.initiative_name}
              </Typography>
            )}
          </Box>
        </Box>
      </Box>
    )

  // ── Smart generic renderer (all other/untested connectors) ────────────────
  // Separates scalars (stat grid) from arrays (auto-table). Strips HTML from strings.
  } else if (raw) {
    const stripHtml = (s: string) => s.replace(/<[^>]*>/g, '').replace(/&nbsp;/g, ' ').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&amp;/g, '&').trim()
    const fmtVal = (v: unknown): string => {
      if (v === null || v === undefined) return '—'
      if (typeof v === 'boolean') return v ? 'Yes' : 'No'
      if (typeof v === 'string') return stripHtml(v).slice(0, 120) || '—'
      if (typeof v === 'object') return JSON.stringify(v).slice(0, 80)
      return String(v)
    }

    const SKIP_KEYS = new Set(['fetched_at', 'raw'])
    const entries = Object.entries(raw).filter(([k]) => !SKIP_KEYS.has(k))
    const scalars = entries.filter(([, v]) => !Array.isArray(v) && typeof v !== 'object')
    const arrays = entries.filter(([, v]) => Array.isArray(v) && v.length > 0) as [string, any[]][]
    const objects = entries.filter(([, v]) => v !== null && typeof v === 'object' && !Array.isArray(v)) as [string, Record<string,unknown>][]

    content = (
      <Box sx={{ display: 'flex', flexDirection: 'column', gap: 1.5 }}>
        {/* Scalar stats */}
        {scalars.length > 0 && (
          <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 0.75 }}>
            {scalars.map(([k, v]) => (
              <Box key={k} sx={{ px: 1, py: 0.4, borderRadius: 1, bgcolor: 'rgba(0,0,0,0.3)', border: '1px solid rgba(255,255,255,0.07)' }}>
                <Typography variant="caption" color="text.disabled" sx={{ fontSize: '0.57rem', display: 'block', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
                  {k.replace(/_/g, ' ')}
                </Typography>
                <Typography variant="caption" fontWeight={600} sx={{ fontSize: '0.65rem' }}>
                  {fmtVal(v)}
                </Typography>
              </Box>
            ))}
          </Box>
        )}
        {/* Nested objects as compact key-value */}
        {objects.map(([k, obj]) => (
          <Box key={k}>
            <Typography variant="caption" color="text.disabled" sx={{ fontSize: '0.57rem', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
              {k.replace(/_/g, ' ')}
            </Typography>
            <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 0.5, mt: 0.4 }}>
              {Object.entries(obj).slice(0, 12).map(([ok, ov]) => (
                <Box key={ok} sx={{ px: 0.75, py: 0.3, borderRadius: 1, bgcolor: 'rgba(0,0,0,0.25)', border: '1px solid rgba(255,255,255,0.05)' }}>
                  <Typography variant="caption" sx={{ fontSize: '0.58rem', color: 'text.secondary' }}>{ok.replace(/_/g, ' ')}: </Typography>
                  <Typography variant="caption" sx={{ fontSize: '0.58rem', fontWeight: 600 }}>{fmtVal(ov)}</Typography>
                </Box>
              ))}
            </Box>
          </Box>
        ))}
        {/* Arrays as auto-tables */}
        {arrays.map(([k, arr]) => {
          const cols = arr[0] ? Object.keys(arr[0]).filter(c => c !== 'fetched_at').slice(0, 5) : []
          return (
            <Box key={k}>
              <Typography variant="caption" color="text.disabled" sx={{ fontSize: '0.57rem', textTransform: 'uppercase', letterSpacing: '0.05em', display: 'block', mb: 0.4 }}>
                {k.replace(/_/g, ' ')} ({arr.length})
              </Typography>
              <TableContainer sx={{ maxHeight: 200 }}>
                <Table size="small" stickyHeader>
                  <TableHead>
                    <TableRow>
                      {cols.map(c => (
                        <TableCell key={c} sx={{ fontSize: '0.58rem', fontWeight: 700, py: 0.4, bgcolor: 'rgba(0,0,0,0.4)', textTransform: 'capitalize' }}>
                          {c.replace(/_/g, ' ')}
                        </TableCell>
                      ))}
                    </TableRow>
                  </TableHead>
                  <TableBody>
                    {arr.slice(0, 10).map((row: any, i: number) => (
                      <TableRow key={i} hover>
                        {cols.map(c => (
                          <TableCell key={c} sx={{ fontSize: '0.58rem', py: 0.3, maxWidth: 200, overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap', color: 'text.secondary' }}>
                            {fmtVal(row[c])}
                          </TableCell>
                        ))}
                      </TableRow>
                    ))}
                  </TableBody>
                </Table>
              </TableContainer>
              {arr.length > 10 && (
                <Typography variant="caption" color="text.disabled" sx={{ fontSize: '0.57rem' }}>+{arr.length - 10} more rows</Typography>
              )}
            </Box>
          )
        })}
      </Box>
    )
  }

  if (!content) {
    return (
      <Box sx={{ p: 1, borderRadius: 1, bgcolor: 'rgba(0,0,0,0.35)', border: '1px solid rgba(255,255,255,0.06)', overflow: 'auto', maxHeight: 280 }}>
        <Typography variant="caption" component="pre"
          sx={{ fontFamily: 'monospace', fontSize: '0.6rem', color: '#C6EFCE', lineHeight: 1.5, whiteSpace: 'pre-wrap', wordBreak: 'break-all' }}>
          {JSON.stringify(raw, null, 2)}
        </Typography>
      </Box>
    )
  }

  return (
    <Box>
      <Box sx={{ p: 1, borderRadius: 1, bgcolor: 'rgba(0,0,0,0.25)', border: '1px solid rgba(255,255,255,0.06)' }}>
        {content}
      </Box>
      {/* Footer toggles: Raw JSON | Fields */}
      <Box sx={{ display: 'flex', alignItems: 'center', gap: 1.5, mt: 0.5 }}>
        <Box onClick={() => setShowJson(v => !v)}
          sx={{ display: 'flex', alignItems: 'center', gap: 0.5, cursor: 'pointer', color: 'text.disabled', '&:hover': { color: 'text.secondary' } }}>
          {showJson ? <ExpandLessOutlined sx={{ fontSize: 11 }} /> : <ExpandMoreOutlined sx={{ fontSize: 11 }} />}
          <Typography variant="caption" sx={{ fontSize: '0.58rem' }}>Raw JSON</Typography>
        </Box>
        <Box onClick={() => setShowFields(v => !v)}
          sx={{ display: 'flex', alignItems: 'center', gap: 0.5, cursor: 'pointer', color: 'text.disabled', '&:hover': { color: 'text.secondary' } }}>
          {showFields ? <ExpandLessOutlined sx={{ fontSize: 11 }} /> : <ExpandMoreOutlined sx={{ fontSize: 11 }} />}
          <Typography variant="caption" sx={{ fontSize: '0.58rem' }}>Fields</Typography>
        </Box>
      </Box>

      <Collapse in={showJson}>
        <Box sx={{ mt: 0.25, p: 1, borderRadius: 1, bgcolor: 'rgba(0,0,0,0.35)', border: '1px solid rgba(255,255,255,0.06)', overflow: 'auto', maxHeight: 200 }}>
          <Typography variant="caption" component="pre"
            sx={{ fontFamily: 'monospace', fontSize: '0.58rem', color: '#C6EFCE', lineHeight: 1.5, whiteSpace: 'pre-wrap', wordBreak: 'break-all' }}>
            {JSON.stringify(raw, null, 2)}
          </Typography>
        </Box>
      </Collapse>

      <Collapse in={showFields}>
        {(() => {
          const paths = flattenPaths(raw)
          const pathText = paths.map(p => `${p.path}  (${p.type})${p.sample ? `  →  ${p.sample}` : ''}`).join('\n')
          return (
            <Box sx={{ mt: 0.25, p: 1, borderRadius: 1, bgcolor: 'rgba(0,0,0,0.35)', border: '1px solid rgba(255,255,255,0.06)', overflow: 'auto', maxHeight: 240 }}>
              <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', mb: 0.5 }}>
                <Typography variant="caption" color="text.disabled" sx={{ fontSize: '0.57rem' }}>
                  {paths.length} fields · source_ref: <strong style={{ fontFamily: 'monospace' }}>{item.source_ref ?? '—'}</strong>
                </Typography>
                <Box
                  onClick={() => { navigator.clipboard.writeText(pathText); setCopied(true); setTimeout(() => setCopied(false), 1500) }}
                  sx={{ display: 'flex', alignItems: 'center', gap: 0.4, cursor: 'pointer', color: copied ? '#C6EFCE' : 'text.disabled', '&:hover': { color: 'text.secondary' }, fontSize: '0.57rem' }}
                >
                  <Typography variant="caption" sx={{ fontSize: '0.57rem' }}>{copied ? 'Copied!' : 'Copy all'}</Typography>
                </Box>
              </Box>
              {paths.map((p, i) => (
                <Box key={i} sx={{ display: 'flex', gap: 1, alignItems: 'baseline', py: 0.15 }}>
                  <Typography component="span" sx={{ fontFamily: 'monospace', fontSize: '0.6rem', color: '#BDD7EE', minWidth: 0, flexShrink: 0 }}>
                    {p.path}
                  </Typography>
                  <Typography component="span" sx={{ fontSize: '0.55rem', color: '#FFEB9C', flexShrink: 0 }}>
                    {p.type}
                  </Typography>
                  {p.sample && (
                    <Typography component="span" sx={{ fontSize: '0.55rem', color: 'text.disabled', overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
                      {p.sample}
                    </Typography>
                  )}
                </Box>
              ))}
            </Box>
          )
        })()}
      </Collapse>
    </Box>
  )
}

function ConnectorEvidenceItem({
  item,
  connectorList,
}: {
  item: ConnectorEvidenceRead
  connectorList: ConnectorRead[]
}) {
  const [rawOpen, setRawOpen] = useState(false)

  const connector = connectorList.find(c => c.id === item.connector_id)
  const system = connector
    ? KNOWN_SYSTEMS.find(s => s.value === connector.source_system)
    : undefined
  const sourceLabel = system?.label ?? connector?.name ?? item.connector_id.slice(0, 8) + '…'

  const classColor = CLASS_COLOR[item.classification ?? ''] ?? '#BDD7EE'
  const statusColor = CONN_STATUS_COLOR[item.status ?? ''] ?? '#BDD7EE'

  return (
    <Box sx={{
      mb: 1, p: 1.5, borderRadius: 2,
      bgcolor: 'rgba(68,114,196,0.06)',
      border: '1px solid rgba(68,114,196,0.12)',
    }}>
      {/* Header row */}
      <Box sx={{ display: 'flex', alignItems: 'flex-start', gap: 1 }}>
        <Box sx={{ flex: 1, minWidth: 0 }}>
          <Typography variant="body2" fontWeight={600} sx={{ lineHeight: 1.4 }}>
            {item.title}
          </Typography>
          <Box sx={{ display: 'flex', gap: 0.5, mt: 0.4, flexWrap: 'wrap', alignItems: 'center' }}>
            <Chip
              label={sourceLabel}
              size="small"
              icon={<ElectricalServicesOutlined style={{ fontSize: 11 }} />}
              sx={{ fontSize: '0.6rem', height: 18, bgcolor: 'rgba(68,114,196,0.2)', color: 'primary.light' }}
            />
            {item.classification && (
              <Chip
                label={item.classification}
                size="small"
                sx={{ fontSize: '0.6rem', height: 18, bgcolor: `${classColor}22`, color: classColor }}
              />
            )}
            {item.status && (
              <Chip
                label={item.status}
                size="small"
                sx={{ fontSize: '0.6rem', height: 18, bgcolor: `${statusColor}22`, color: statusColor }}
              />
            )}
            {item.source_ref && (
              <Typography variant="caption" color="text.disabled" sx={{ fontFamily: 'monospace', fontSize: '0.6rem' }}>
                {item.source_ref}
              </Typography>
            )}
          </Box>
        </Box>

        <Box sx={{ display: 'flex', gap: 0.5, flexShrink: 0, alignItems: 'center' }}>
          {item.source_url && (
            <Tooltip title="Open in source system">
              <IconButton
                size="small"
                component="a"
                href={item.source_url}
                target="_blank"
                rel="noopener noreferrer"
                sx={{ color: 'text.disabled', '&:hover': { color: 'primary.light' } }}
              >
                <OpenInNewOutlined sx={{ fontSize: 14 }} />
              </IconButton>
            </Tooltip>
          )}
          <Typography variant="caption" color="text.disabled" sx={{ fontSize: '0.6rem', whiteSpace: 'nowrap' }}>
            {item.event_date
              ? new Date(item.event_date).toLocaleDateString()
              : new Date(item.created_at).toLocaleDateString()}
          </Typography>
        </Box>
      </Box>

      {/* Details toggle */}
      <Box
        onClick={() => setRawOpen(v => !v)}
        sx={{
          display: 'flex', alignItems: 'center', gap: 0.5, mt: 0.75,
          cursor: 'pointer', color: 'text.disabled',
          '&:hover': { color: 'text.secondary' },
        }}
      >
        {rawOpen ? <ExpandLessOutlined sx={{ fontSize: 13 }} /> : <ExpandMoreOutlined sx={{ fontSize: 13 }} />}
        <Typography variant="caption" sx={{ fontSize: '0.65rem' }}>
          {rawOpen ? 'Hide details' : 'View details'}
        </Typography>
      </Box>
      <Collapse in={rawOpen}>
        <Box sx={{ mt: 0.5 }}>
          <EvidenceDetailView item={item} />
        </Box>
      </Collapse>
    </Box>
  )
}

export default function ControlDetail() {
  const { id, code } = useParams<{ id?: string; code?: string }>()
  const identifier = code ?? id!
  const isCode = !!code
  const navigate = useNavigate()
  const queryClient = useQueryClient()
  const { product: productView } = useProduct()
  const [tab, setTab] = useState(0)
  const [expandedSheets, setExpandedSheets] = useState<Set<string>>(new Set())
  const [stackedFilter, setStackedFilter] = useState<string>('all')
  const [aiOpen, setAiOpen] = useState(false)
  const [docPreview, setDocPreview] = useState<{ id: string; docType: 'policy' | 'implementation'; documentId: string; title: string; typeLabel: string; typeColor?: string } | null>(null)
  const [assessmentDrawerOpen, setAssessmentDrawerOpen] = useState(false)
  const [deleteAssessmentTarget, setDeleteAssessmentTarget] = useState<{ id: string; name: string } | null>(null)
  const [generatorPickerOpen, setGeneratorPickerOpen] = useState(false)
  const [pickerGeneratorId, setPickerGeneratorId] = useState('')

  const { data, isLoading, error } = useQuery({
    queryKey: ['control', identifier],
    queryFn: () => isCode ? controlsApi.getByCode(identifier) : controlsApi.getById(identifier),
    enabled: !!identifier,
  })

  const statusMutation = useMutation({
    mutationFn: ({ itemId, status }: { itemId: string; status: string }) =>
      assessmentsApi.patchItem(itemId, status),
    onSuccess: () => queryClient.invalidateQueries({ queryKey: ['control', identifier] }),
  })

  const deleteAssessmentMutation = useMutation({
    mutationFn: (id: string) => assessmentsApi.deleteAssessment(id),
    onSuccess: () => {
      setDeleteAssessmentTarget(null)
      queryClient.invalidateQueries({ queryKey: ['control', identifier] })
    },
  })

  const cg = data as unknown as RealControlDetail | undefined

  const { data: generatorsForGroup = [] } = useQuery({
    queryKey: ['generators-for-group', cg?.group_code ?? ''],
    queryFn: () => assessmentsApi.getGeneratorsForGroup(cg!.group_code),
    enabled: !!cg,
  })

  // Connector evidence — auto-collected from v2.0 connectors
  const { data: connectorEvidence = [] } = useQuery<ConnectorEvidenceRead[]>({
    queryKey: ['connector-evidence', cg?.group_code ?? ''],
    queryFn: () => connectorsApi.getEvidence(cg!.group_code),
    enabled: !!cg,
    refetchInterval: 60_000,  // refresh every 60s to catch new ingest
  })

  // Connector list — needed to resolve connector_id → system name (admin-only, best-effort)
  const { data: connectorList = [] } = useQuery<ConnectorRead[]>({
    queryKey: ['connectors-list'],
    queryFn: () => connectorsApi.list(),
    staleTime: 30_000,
  })
  const needsGeneratorPick = generatorsForGroup.length > 1
  const drawerGeneratorId = needsGeneratorPick ? pickerGeneratorId : (generatorsForGroup[0]?.document_id ?? undefined)

  if (isLoading) {
    return (
      <Box>
        <Skeleton variant="text" width={300} height={40} />
        <Skeleton variant="rectangular" height={200} sx={{ mt: 2, borderRadius: 2 }} />
      </Box>
    )
  }

  if (error || !cg) {
    return <Alert severity="error">Control not found or failed to load.</Alert>
  }

  // Filter content by product view
  // ISMS = show all ISMS content; privacy/cloud = show matching product_type
  // INS docs go to Instructions tab, not Policies
  const visiblePolicies = cg.policies.filter(p =>
    p.policy_type !== 'INS' && (productView === 'isms' || p.product_type === productView)
  )
  const visibleInstructions = cg.policies.filter(p => p.policy_type === 'INS')
  // Implementation model has no product_type — control group ownership is already product-scoped
  const visibleImpls = cg.implementations
  const visibleAssessments = cg.assessments.filter(a =>
    productView === 'isms' || a.product_type === productView
  )

  // Tab index constants — keeps panel assignments readable
  const TAB_POLICIES = 0
  const TAB_INSTRUCTIONS = 1
  const TAB_IMPLEMENTATIONS = 2
  const TAB_ASSESSMENTS = 3
  const TAB_MAPPINGS = 4
  const TAB_EVIDENCE = 5
  const TAB_GAPS = 6

  const tabs = [
    { label: `Policies (${visiblePolicies.length})` },
    ...(visibleInstructions.length > 0 ? [{ label: `Instructions (${visibleInstructions.length})` }] : [{ label: 'Instructions (0)' }]),
    { label: `Implementations (${visibleImpls.length})` },
    { label: `Assessments (${visibleAssessments.length})` },
    { label: `ISO Mappings (${cg.iso_controls.length})` },
    { label: `Evidence (${cg.evidence_total + connectorEvidence.length})` },
    ...(cg.gaps.length > 0 ? [{ label: `Gaps (${cg.gaps.length})` }] : []),
  ]

  return (
    <Box>
      {/* Breadcrumb */}
      <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.5, mb: 2 }}>
        <Typography
          variant="caption"
          color="text.secondary"
          sx={{ cursor: 'pointer', '&:hover': { color: 'primary.light' } }}
          onClick={() => navigate('/')}
        >
          Overview
        </Typography>
        <Typography variant="caption" color="text.disabled">›</Typography>
        <Typography
          variant="caption"
          color="text.secondary"
          sx={{ cursor: 'pointer', '&:hover': { color: 'primary.light' } }}
          onClick={() => navigate('/controls')}
        >
          Controls
        </Typography>
        <Typography variant="caption" color="text.disabled">›</Typography>
        <Typography variant="caption" color="primary.light" fontWeight={600}>
          {cg.group_code.toUpperCase()}
        </Typography>
      </Box>

      {/* Header */}
      <Box sx={{ display: 'flex', alignItems: 'flex-start', gap: 1, mb: 3 }}>
        <IconButton size="small" onClick={() => navigate('/controls')} sx={{ mt: 0.25 }}>
          <ArrowBackOutlined fontSize="small" />
        </IconButton>

        <Box sx={{ flex: 1 }}>
          <Box sx={{ display: 'flex', gap: 0.75, alignItems: 'center', mb: 0.5, flexWrap: 'wrap' }}>
            <Typography variant="caption" sx={{ fontFamily: 'monospace', color: 'primary.light', fontWeight: 700, fontSize: '0.8rem' }}>
              {cg.group_code.toUpperCase()}
            </Typography>
            <Chip label={cg.section} size="small" sx={{ fontSize: '0.65rem', height: 18 }} />
            <Chip label={cg.section_name} size="small" sx={{ fontSize: '0.65rem', height: 18 }} />
            {cg.is_stacked && (
              <Chip label={`Stacked: ${cg.stacked_control_ids.join(', ')}`} size="small"
                sx={{ fontSize: '0.65rem', height: 18, bgcolor: 'rgba(255,192,0,0.15)', color: '#FFEB9C' }} />
            )}
            <StatusChip status={cg.framework_status} />
          </Box>
          <Typography variant="h4">{cg.name}</Typography>
        </Box>

        {/* AI button */}
        <Tooltip title="ISMS AI Assistant">
          <IconButton
            size="small"
            onClick={() => setAiOpen((v) => !v)}
            sx={{
              mt: 0.25, flexShrink: 0,
              color: aiOpen ? '#4472C4' : 'text.disabled',
              bgcolor: aiOpen ? 'rgba(68,114,196,0.15)' : 'transparent',
              border: '1px solid',
              borderColor: aiOpen ? 'rgba(68,114,196,0.4)' : 'rgba(255,255,255,0.08)',
              '&:hover': { bgcolor: 'rgba(68,114,196,0.15)', color: '#4472C4' },
            }}
          >
            <AutoAwesomeOutlined fontSize="small" />
          </IconButton>
        </Tooltip>

        {/* Compass button */}
        <Tooltip title="Analyse with ISMS Compass">
          <IconButton
            size="small"
            onClick={() => navigate(`/compass?group=${cg.group_code}`)}
            sx={{
              mt: 0.25, flexShrink: 0,
              color: 'text.disabled',
              border: '1px solid rgba(255,255,255,0.08)',
              '&:hover': { bgcolor: 'rgba(46,139,87,0.15)', color: '#C6EFCE' },
            }}
          >
            <ExploreOutlined fontSize="small" />
          </IconButton>
        </Tooltip>

        {/* Stats */}
        <Box sx={{ display: 'flex', gap: 2.5, flexShrink: 0 }}>
          {[
            { label: 'Policies', value: cg.policies.length },
            { label: 'Impls', value: cg.implementations.length },
            { label: 'Assessments', value: cg.assessments.length },
            { label: 'ISO Controls', value: cg.iso_controls.length },
            { label: 'Evidence', value: cg.evidence_total + connectorEvidence.length },
            { label: 'Open Gaps', value: cg.gaps_open },
          ].map(({ label, value }) => (
            <Box key={label} sx={{ textAlign: 'center' }}>
              <Typography variant="h5" color={label === 'Open Gaps' && value > 0 ? 'error.main' : 'primary.light'}>
                {value}
              </Typography>
              <Typography variant="caption" color="text.secondary">{label}</Typography>
            </Box>
          ))}
        </Box>
      </Box>

      {/* Tabs */}
      <Card>
        <Tabs
          value={tab}
          onChange={(_, v) => setTab(v)}
          sx={{ borderBottom: '1px solid', borderColor: 'divider', px: 2 }}
          variant="scrollable"
          scrollButtons="auto"
        >
          {tabs.map((t, i) => <Tab key={i} label={t.label} sx={{ fontSize: '0.8rem' }} />)}
        </Tabs>

        <CardContent>
          {/* Policies */}
          <TabPanel value={tab} index={TAB_POLICIES}>
            {visiblePolicies.length === 0 && <Alert severity="warning">No policies for the selected product.</Alert>}
            {visiblePolicies.map((pol) => {
              const isExternal = pol.product_type === 'external'
              return (
                <Box key={pol.id} onClick={() => setDocPreview({ id: pol.id, docType: 'policy', documentId: pol.document_id, title: pol.title, typeLabel: pol.policy_type, productType: pol.product_type })}
                  sx={{
                    mb: 1.5, p: 1.5, borderRadius: 2, cursor: 'pointer',
                    bgcolor: isExternal ? 'rgba(255,192,0,0.06)' : 'rgba(68,114,196,0.07)',
                    border: isExternal ? '1px solid rgba(255,192,0,0.25)' : '1px solid transparent',
                    '&:hover': { bgcolor: isExternal ? 'rgba(255,192,0,0.12)' : 'rgba(68,114,196,0.14)' },
                  }}
                >
                  {isExternal && (
                    <Typography variant="caption" sx={{ color: '#FFC000', fontWeight: 600, display: 'block', mb: 0.5, fontSize: '0.65rem' }}>
                      External Document{pol.source_label ? ` — ${pol.source_label}` : ''}
                    </Typography>
                  )}
                  <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                    <Box>
                      <Typography variant="caption" sx={{ fontFamily: 'monospace', color: isExternal ? '#FFC000' : 'primary.light' }}>
                        {pol.document_id}
                      </Typography>
                      <Typography variant="body2" fontWeight={600}>{pol.title}</Typography>
                    </Box>
                    <Box sx={{ display: 'flex', gap: 0.5, flexShrink: 0, flexWrap: 'wrap', justifyContent: 'flex-end' }}>
                      <Chip label={pol.policy_type} size="small" sx={{ fontSize: '0.65rem', height: 18 }} />
                      {isExternal
                        ? <Chip label="external" size="small" sx={{ fontSize: '0.65rem', height: 18, bgcolor: 'rgba(255,192,0,0.15)', color: '#FFC000' }} />
                        : <Chip label={pol.product_type} size="small" sx={{ fontSize: '0.65rem', height: 18 }} />
                      }
                      <Chip label={`${pol.word_count.toLocaleString()}w`} size="small" sx={{ fontSize: '0.65rem', height: 18, bgcolor: 'rgba(68,114,196,0.15)' }} />
                      {pol.requirements_count > 0 && (
                        <Chip label={`${pol.requirements_count} reqs`} size="small" sx={{ fontSize: '0.65rem', height: 18, bgcolor: '#1a3a27', color: '#C6EFCE' }} />
                      )}
                    </Box>
                  </Box>
                </Box>
              )
            })}
          </TabPanel>

          {/* Instructions */}
          <TabPanel value={tab} index={TAB_INSTRUCTIONS}>
            {visibleInstructions.length === 0 && (
              <Alert severity="info">No implementation guides (INS) for this control group.</Alert>
            )}
            {visibleInstructions.map((ins) => (
              <Box key={ins.id} onClick={() => setDocPreview({ id: ins.id, docType: 'policy', documentId: ins.document_id, title: ins.title, typeLabel: 'INS', typeColor: '#FFEB9C' })} sx={{ mb: 1.5, p: 1.5, bgcolor: 'rgba(255,192,0,0.06)', border: '1px solid rgba(255,192,0,0.15)', borderRadius: 2, cursor: 'pointer', '&:hover': { bgcolor: 'rgba(255,192,0,0.1)' } }}>
                <Box sx={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
                  <Box>
                    <Typography variant="caption" sx={{ fontFamily: 'monospace', color: '#FFEB9C' }}>
                      {ins.document_id}
                    </Typography>
                    <Typography variant="body2" fontWeight={600}>{ins.title}</Typography>
                  </Box>
                  <Box sx={{ display: 'flex', gap: 0.5, flexShrink: 0, flexWrap: 'wrap', justifyContent: 'flex-end' }}>
                    <Chip label="INS" size="small" sx={{ fontSize: '0.65rem', height: 18, bgcolor: 'rgba(255,192,0,0.15)', color: '#FFEB9C' }} />
                    <Chip label={`${ins.word_count.toLocaleString()}w`} size="small" sx={{ fontSize: '0.65rem', height: 18 }} />
                    {ins.requirements_count > 0 && (
                      <Chip label={`${ins.requirements_count} notes`} size="small" sx={{ fontSize: '0.65rem', height: 18, bgcolor: '#3d3200', color: '#FFEB9C' }} />
                    )}
                  </Box>
                </Box>
              </Box>
            ))}
          </TabPanel>

          {/* Implementations */}
          <TabPanel value={tab} index={TAB_IMPLEMENTATIONS}>
            {visibleImpls.length === 0 && <Alert severity="warning">No implementations for the selected product.</Alert>}
            <Grid container spacing={1}>
              {visibleImpls.map((impl) => (
                <Grid item xs={12} sm={6} key={impl.id}>
                  <Box onClick={() => setDocPreview({ id: impl.id, docType: 'implementation', documentId: impl.document_id, title: impl.title, typeLabel: impl.impl_type, typeColor: impl.impl_type === 'UG' ? '#C6EFCE' : '#FFEB9C' })} sx={{ p: 1.5, bgcolor: 'rgba(68,114,196,0.07)', borderRadius: 2, cursor: 'pointer', '&:hover': { bgcolor: 'rgba(68,114,196,0.14)' } }}>
                    <Box sx={{ display: 'flex', justifyContent: 'space-between', mb: 0.25 }}>
                      <Typography variant="caption" sx={{ fontFamily: 'monospace', color: 'primary.light' }}>
                        {impl.document_id}
                      </Typography>
                      <Box sx={{ display: 'flex', gap: 0.5 }}>
                        <Chip
                          label={impl.impl_type}
                          size="small"
                          sx={{
                            fontSize: '0.65rem', height: 18,
                            bgcolor: impl.impl_type === 'UG' ? '#1a3a27' : '#3d3200',
                            color: impl.impl_type === 'UG' ? '#C6EFCE' : '#FFEB9C',
                          }}
                        />
                        <Chip label={`${impl.word_count.toLocaleString()}w`} size="small" sx={{ fontSize: '0.65rem', height: 18 }} />
                      </Box>
                    </Box>
                    <Typography variant="body2" fontWeight={600} sx={{ lineHeight: 1.3 }}>
                      {impl.title}
                    </Typography>
                  </Box>
                </Grid>
              ))}
            </Grid>
          </TabPanel>

          {/* Assessments */}
          <TabPanel value={tab} index={TAB_ASSESSMENTS}>
            {(() => {
              const isPlatform = (a: AssessmentRow) => a.file_path === 'platform:webui' || a.document_id.startsWith('ISMS-ASS-')
              const platformAssessments = visibleAssessments.filter(isPlatform)
              const uploadedAssessments = visibleAssessments.filter(a => !isPlatform(a))

              return (
                <>
                  {/* ── Platform Assessments ── */}
                  <Box sx={{ mb: 3 }}>
                    <Box sx={{ display: 'flex', alignItems: 'center', mb: 1.5 }}>
                      <AssignmentOutlined sx={{ fontSize: 16, color: 'primary.light', mr: 0.75 }} />
                      <Typography variant="caption" fontWeight={700} color="primary.light" sx={{ flex: 1, textTransform: 'uppercase', letterSpacing: '0.06em', fontSize: '0.7rem' }}>
                        Conduct Assessment
                      </Typography>
                      <Button
                        size="small"
                        variant="contained"
                        startIcon={<AddOutlined />}
                        onClick={() => {
                          if (needsGeneratorPick) { setPickerGeneratorId(''); setGeneratorPickerOpen(true) }
                          else { setAssessmentDrawerOpen(true) }
                        }}
                        sx={{ fontSize: '0.75rem', fontWeight: 600 }}
                      >
                        New Assessment
                      </Button>
                    </Box>

                    {platformAssessments.length === 0 ? (
                      <Box
                        onClick={() => {
                          if (needsGeneratorPick) { setPickerGeneratorId(''); setGeneratorPickerOpen(true) }
                          else { setAssessmentDrawerOpen(true) }
                        }}
                        sx={{
                          p: 2.5, borderRadius: 2, cursor: 'pointer', textAlign: 'center',
                          border: '1px dashed rgba(68,114,196,0.3)',
                          bgcolor: 'rgba(68,114,196,0.03)',
                          '&:hover': { bgcolor: 'rgba(68,114,196,0.08)', borderColor: 'rgba(68,114,196,0.5)' },
                        }}
                      >
                        <AddOutlined sx={{ color: 'text.disabled', mb: 0.5 }} />
                        <Typography variant="body2" color="text.secondary">
                          No platform assessments yet — fill in your data directly, no Excel required.
                        </Typography>
                        <Typography variant="caption" color="primary.light" sx={{ mt: 0.5, display: 'block' }}>
                          Click to start
                        </Typography>
                      </Box>
                    ) : (
                      platformAssessments.map((asmnt) => (
                        <Box key={asmnt.id} sx={{ mb: 1.5, p: 1.5, bgcolor: 'rgba(68,114,196,0.06)', borderRadius: 2, border: '1px solid rgba(68,114,196,0.12)' }}>
                          <Box sx={{ display: 'flex', alignItems: 'flex-start', gap: 1 }}>
                            <Box sx={{ flex: 1, minWidth: 0 }}>
                              <Typography variant="caption" sx={{ fontFamily: 'monospace', color: 'primary.light' }}>
                                {asmnt.document_id}
                              </Typography>
                              <Typography variant="body2" fontWeight={600}>{asmnt.workbook_name}</Typography>
                              <Box sx={{ display: 'flex', gap: 0.5, mt: 0.25, flexWrap: 'wrap' }}>
                                <Chip label="platform" size="small" sx={{ fontSize: '0.6rem', height: 16, bgcolor: 'rgba(68,114,196,0.2)', color: 'primary.light' }} />
                                <Chip label={`${asmnt.items_total} items`} size="small" sx={{ fontSize: '0.6rem', height: 16 }} />
                                {asmnt.overall_score != null && (
                                  <Chip label={`${asmnt.overall_score}%`} size="small" sx={{ fontSize: '0.6rem', height: 16, bgcolor: '#1a3a27', color: '#C6EFCE' }} />
                                )}
                              </Box>
                            </Box>
                            <Tooltip title="Delete platform assessment">
                              <IconButton
                                size="small"
                                onClick={() => setDeleteAssessmentTarget({ id: asmnt.id, name: asmnt.workbook_name })}
                                sx={{ color: 'error.main', opacity: 0.4, flexShrink: 0, '&:hover': { opacity: 1 } }}
                              >
                                <DeleteOutlined sx={{ fontSize: 16 }} />
                              </IconButton>
                            </Tooltip>
                          </Box>
                          {asmnt.items_total > 0 && (
                            <ComplianceBar
                              total={asmnt.items_total}
                              compliant={asmnt.items_compliant}
                              partial={asmnt.items_partial}
                              nonCompliant={asmnt.items_non_compliant}
                              na={asmnt.items_na}
                            />
                          )}
                          {asmnt.items_total === 0 && (
                            <Box sx={{ mt: 1 }}>
                              <LinearProgress variant="determinate" value={0} sx={{ height: 4, borderRadius: 2, bgcolor: 'rgba(255,255,255,0.06)' }} />
                              <Typography variant="caption" color="text.disabled" sx={{ mt: 0.5, display: 'block' }}>
                                No items yet — open the assessment to start filling in data
                              </Typography>
                            </Box>
                          )}
                        </Box>
                      ))
                    )}
                  </Box>

                  {/* ── Uploaded Assessments (from Excel) ── */}
                  {uploadedAssessments.length > 0 && (
                    <Box>
                      <Box sx={{ display: 'flex', alignItems: 'center', mb: 1.5 }}>
                        <FolderOpenOutlined sx={{ fontSize: 16, color: 'text.secondary', mr: 0.75 }} />
                        <Typography variant="caption" fontWeight={700} color="text.secondary" sx={{ textTransform: 'uppercase', letterSpacing: '0.06em', fontSize: '0.7rem' }}>
                          Imported Workbooks
                        </Typography>
                      </Box>
                      {uploadedAssessments.map((asmnt) => (
                        <Box key={asmnt.id} sx={{ mb: 2, p: 1.5, bgcolor: 'rgba(68,114,196,0.05)', borderRadius: 2 }}>
                          <Typography variant="caption" sx={{ fontFamily: 'monospace', color: 'primary.light' }}>
                            {asmnt.document_id}
                          </Typography>
                          <Typography variant="body2" fontWeight={600}>{asmnt.workbook_name}</Typography>
                          <Box sx={{ display: 'flex', gap: 0.5, mt: 0.25, flexWrap: 'wrap' }}>
                            <Chip label={asmnt.assessment_type} size="small" sx={{ fontSize: '0.65rem', height: 18 }} />
                            <Chip label={asmnt.product_type} size="small" sx={{ fontSize: '0.65rem', height: 18 }} />
                            <Chip label={`${asmnt.sheets_count} sheets`} size="small" sx={{ fontSize: '0.65rem', height: 18 }} />
                          </Box>
                          <ComplianceBar
                            total={asmnt.items_total}
                            compliant={asmnt.items_compliant}
                            partial={asmnt.items_partial}
                            nonCompliant={asmnt.items_non_compliant}
                            na={asmnt.items_na}
                          />
                          <Box sx={{ mt: 1 }}>
                            {asmnt.sheets.map((sheet) => (
                              <Box key={sheet.id} sx={{ mb: 0.5 }}>
                                <Box sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                                  <Typography variant="caption" fontWeight={600} sx={{ flex: 1 }}>{sheet.sheet_name}</Typography>
                                  <Chip label={sheet.sheet_type} size="small" sx={{ fontSize: '0.6rem', height: 16, bgcolor: sheet.sheet_type === 'assessment' ? 'rgba(68,114,196,0.2)' : 'rgba(255,255,255,0.06)' }} />
                                  {sheet.row_count > 0 && <Typography variant="caption" color="text.disabled">{sheet.row_count} rows</Typography>}
                                </Box>
                                <SheetItemsTable
                                  sheet={sheet}
                                  expanded={expandedSheets.has(sheet.id)}
                                  onToggle={() => setExpandedSheets(prev => {
                                    const next = new Set(prev)
                                    next.has(sheet.id) ? next.delete(sheet.id) : next.add(sheet.id)
                                    return next
                                  })}
                                  onStatusChange={(itemId, newStatus) =>
                                    statusMutation.mutate({ itemId, status: newStatus })
                                  }
                                />
                              </Box>
                            ))}
                          </Box>
                        </Box>
                      ))}
                    </Box>
                  )}
                </>
              )
            })()}
          </TabPanel>

          {/* ISO Mappings */}
          <TabPanel value={tab} index={TAB_MAPPINGS}>
            {cg.is_stacked && cg.stacked_control_ids.length > 1 && (
              <Box sx={{ display: 'flex', gap: 0.75, mb: 1.5, flexWrap: 'wrap', alignItems: 'center' }}>
                <Typography variant="caption" color="text.secondary">Filter:</Typography>
                {['all', ...cg.stacked_control_ids].map((sid) => (
                  <Chip
                    key={sid}
                    label={sid === 'all' ? 'All' : sid}
                    size="small"
                    onClick={() => setStackedFilter(sid)}
                    sx={{
                      fontSize: '0.68rem', height: 20, cursor: 'pointer',
                      bgcolor: stackedFilter === sid ? 'rgba(68,114,196,0.35)' : 'rgba(68,114,196,0.1)',
                      color: stackedFilter === sid ? 'primary.light' : 'text.secondary',
                      fontWeight: stackedFilter === sid ? 700 : 400,
                    }}
                  />
                ))}
              </Box>
            )}
            {cg.iso_controls.length === 0 && <Alert severity="info">No ISO controls linked.</Alert>}
            {cg.iso_controls
              .filter(iso => stackedFilter === 'all' || iso.control_id.startsWith(stackedFilter.replace('A.', 'A.')))
              .map((iso) => (
              <Box key={iso.control_id} sx={{ mb: 2, p: 1.5, bgcolor: 'rgba(68,114,196,0.07)', borderRadius: 2 }}>
                <Box sx={{ display: 'flex', gap: 1, alignItems: 'center', mb: iso.description ? 0.5 : 0.75 }}>
                  <Typography variant="caption" sx={{ fontFamily: 'monospace', color: 'primary.light', fontWeight: 700, fontSize: '0.8rem' }}>
                    {iso.control_id}
                  </Typography>
                  <Typography variant="body2" fontWeight={600}>{iso.title}</Typography>
                </Box>
                {iso.description && (
                  <Typography variant="caption" color="text.secondary" sx={{ display: 'block', mb: 0.75, lineHeight: 1.6, fontStyle: 'italic' }}>
                    {iso.description}
                  </Typography>
                )}
                {iso.mappings.length > 0 && (
                  <Box sx={{ display: 'flex', gap: 0.5, flexWrap: 'wrap' }}>
                    {iso.mappings.map((m, idx) => (
                      <Chip
                        key={idx}
                        label={`${m.control_id}`}
                        title={`${m.framework}: ${m.control_title}`}
                        size="small"
                        sx={{
                          fontSize: '0.68rem', height: 18,
                          bgcolor: 'rgba(112,173,71,0.12)', color: '#C6EFCE',
                        }}
                      />
                    ))}
                    <Typography variant="caption" color="text.secondary" sx={{ alignSelf: 'center' }}>
                      {iso.mappings.length} mappings across {[...new Set(iso.mappings.map(m => m.framework))].length} frameworks
                    </Typography>
                  </Box>
                )}
              </Box>
            ))}
          </TabPanel>

          {/* Evidence */}
          <TabPanel value={tab} index={TAB_EVIDENCE}>

            {/* ── Automated Evidence (v2.0 connectors) ── */}
            <Box sx={{ mb: 3 }}>
              <Box sx={{ display: 'flex', alignItems: 'center', mb: 1.5 }}>
                <ElectricalServicesOutlined sx={{ fontSize: 16, color: 'primary.light', mr: 0.75 }} />
                <Typography variant="caption" fontWeight={700} color="primary.light" sx={{
                  flex: 1, textTransform: 'uppercase', letterSpacing: '0.06em', fontSize: '0.7rem',
                }}>
                  Automated Evidence
                </Typography>
                <Chip
                  label={`${connectorEvidence.length} items`}
                  size="small"
                  sx={{ fontSize: '0.65rem', height: 18, bgcolor: 'rgba(68,114,196,0.2)', color: 'primary.light' }}
                />
              </Box>

              {connectorEvidence.length === 0 ? (
                <Alert severity="info" sx={{ fontSize: '0.8rem' }}>
                  No automated evidence yet. Register a connector in <strong>Admin → Connectors</strong> to start pulling evidence automatically.
                </Alert>
              ) : (
                connectorEvidence.map(item => (
                  <ConnectorEvidenceItem key={item.id} item={item} connectorList={connectorList} />
                ))
              )}
            </Box>

            {/* ── Manual Evidence (uploaded files) ── */}
            <Box>
              <Box sx={{ display: 'flex', alignItems: 'center', mb: 1.5 }}>
                <FolderOpenOutlined sx={{ fontSize: 16, color: 'text.secondary', mr: 0.75 }} />
                <Typography variant="caption" fontWeight={700} color="text.secondary" sx={{
                  flex: 1, textTransform: 'uppercase', letterSpacing: '0.06em', fontSize: '0.7rem',
                }}>
                  Manual Evidence
                </Typography>
                <Chip
                  label={`${cg.evidence.length} items`}
                  size="small"
                  sx={{ fontSize: '0.65rem', height: 18 }}
                />
              </Box>

              {cg.evidence.length === 0 && (
                <Alert severity="info" sx={{ fontSize: '0.8rem' }}>No manual evidence linked yet. Upload evidence via the Evidence page.</Alert>
              )}
              {cg.evidence.map((ev) => (
                <Box key={ev.id} sx={{ mb: 1, p: 1.5, bgcolor: 'rgba(68,114,196,0.07)', borderRadius: 2 }}>
                  <Box sx={{ display: 'flex', justifyContent: 'space-between' }}>
                    <Typography variant="body2" fontWeight={600}>{ev.title}</Typography>
                    <StatusChip status={ev.verified_by ? 'green' : 'not_assessed'} />
                  </Box>
                  <Box sx={{ display: 'flex', gap: 0.5, mt: 0.5 }}>
                    <Chip label={ev.evidence_type} size="small" sx={{ fontSize: '0.65rem', height: 18 }} />
                    {ev.collected_date && (
                      <Typography variant="caption" color="text.secondary" sx={{ alignSelf: 'center' }}>
                        {ev.collected_date}
                      </Typography>
                    )}
                  </Box>
                </Box>
              ))}
            </Box>
          </TabPanel>

          {/* Gaps */}
          {cg.gaps.length > 0 && (
            <TabPanel value={tab} index={TAB_GAPS}>
              {cg.gaps.map((gap) => (
                <Box key={gap.id} sx={{ mb: 1, p: 1.5, bgcolor: 'rgba(192,0,0,0.08)', border: '1px solid rgba(255,199,206,0.15)', borderRadius: 2 }}>
                  <Box sx={{ display: 'flex', gap: 1, alignItems: 'center', mb: 0.25 }}>
                    <StatusChip status={gap.severity} />
                    <StatusChip status={gap.status} />
                    <Typography variant="caption" color="text.secondary">{gap.gap_type}</Typography>
                  </Box>
                  <Typography variant="body2">{gap.description}</Typography>
                </Box>
              ))}
            </TabPanel>
          )}
        </CardContent>
      </Card>

      <AiAssistant
        open={aiOpen}
        onClose={() => setAiOpen(false)}
        controlId={cg.id}
        controlName={cg.name}
      />

      <DocPreviewDrawer
        open={!!docPreview}
        onClose={() => setDocPreview(null)}
        target={docPreview}
      />

      {/* Delete assessment confirm */}
      <Dialog open={!!deleteAssessmentTarget} onClose={() => setDeleteAssessmentTarget(null)} maxWidth="xs" fullWidth>
        <DialogTitle>Delete Platform Assessment?</DialogTitle>
        <DialogContent>
          <Typography variant="body2">
            <strong>{deleteAssessmentTarget?.name}</strong> and all its data will be permanently removed.
            This cannot be undone.
          </Typography>
          {deleteAssessmentMutation.isError && (
            <Alert severity="error" sx={{ mt: 1.5 }}>Delete failed. Try again.</Alert>
          )}
        </DialogContent>
        <DialogActions sx={{ px: 3, pb: 2 }}>
          <Button onClick={() => setDeleteAssessmentTarget(null)} disabled={deleteAssessmentMutation.isPending}>Cancel</Button>
          <Button
            variant="contained"
            color="error"
            disabled={deleteAssessmentMutation.isPending}
            startIcon={<DeleteOutlined />}
            onClick={() => deleteAssessmentTarget && deleteAssessmentMutation.mutate(deleteAssessmentTarget.id)}
          >
            {deleteAssessmentMutation.isPending ? 'Deleting…' : 'Delete'}
          </Button>
        </DialogActions>
      </Dialog>

      {/* Generator / workbook picker for stacked controls */}
      <Dialog open={generatorPickerOpen} onClose={() => setGeneratorPickerOpen(false)} maxWidth="sm" fullWidth>
        <DialogTitle>Choose Workbook to Assess</DialogTitle>
        <DialogContent>
          <Typography variant="body2" color="text.secondary" sx={{ mb: 2 }}>
            This control group has multiple workbooks. Select which one to assess:
          </Typography>
          <Box sx={{ display: 'flex', flexDirection: 'column', gap: 1 }}>
            {generatorsForGroup.map((gen) => (
              <Box
                key={gen.document_id}
                onClick={() => setPickerGeneratorId(gen.document_id)}
                sx={{
                  p: 1.5, borderRadius: 2, cursor: 'pointer',
                  border: '1px solid',
                  borderColor: pickerGeneratorId === gen.document_id ? 'primary.main' : 'rgba(255,255,255,0.1)',
                  bgcolor: pickerGeneratorId === gen.document_id ? 'rgba(68,114,196,0.18)' : 'rgba(68,114,196,0.05)',
                  '&:hover': { bgcolor: 'rgba(68,114,196,0.12)' },
                }}
              >
                <Typography variant="caption" sx={{ fontFamily: 'monospace', color: 'primary.light', display: 'block' }}>
                  {gen.document_id}
                </Typography>
                <Typography variant="body2" fontWeight={600}>{gen.workbook_name}</Typography>
                <Typography variant="caption" color="text.secondary">{gen.sheet_count} sheets</Typography>
              </Box>
            ))}
          </Box>
        </DialogContent>
        <DialogActions sx={{ px: 3, pb: 2 }}>
          <Button onClick={() => setGeneratorPickerOpen(false)}>Cancel</Button>
          <Button
            variant="contained"
            disabled={!pickerGeneratorId}
            onClick={() => { setGeneratorPickerOpen(false); setAssessmentDrawerOpen(true) }}
          >
            Continue
          </Button>
        </DialogActions>
      </Dialog>

      <AssessmentFormDrawer
        open={assessmentDrawerOpen}
        onClose={() => {
          setAssessmentDrawerOpen(false)
          queryClient.invalidateQueries({ queryKey: ['control', identifier] })
        }}
        groupCode={cg.group_code}
        groupName={cg.name}
        generatorId={drawerGeneratorId}
      />
    </Box>
  )
}
