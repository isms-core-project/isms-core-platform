import { useState, useEffect } from 'react'
import {
  Box,
  Card,
  CardContent,
  Typography,
  Chip,
  TextField,
  InputAdornment,
  ToggleButtonGroup,
  ToggleButton,
  Skeleton,
  Alert,
  Tooltip,
  Collapse,
  IconButton,
  Divider,
  Stack,
  Dialog,
  DialogTitle,
  DialogContent,
  DialogActions,
  Button,
  Select,
  MenuItem,
  FormControl,
  Drawer,
  Tabs,
  Tab,
  Table,
  TableHead,
  TableBody,
  TableRow,
  TableCell,
  InputLabel,
} from '@mui/material'
import {
  SearchOutlined,
  TableChartOutlined,
  ExpandMoreOutlined,
  ExpandLessOutlined,
  LayersOutlined,
  EditOutlined,
  DeleteOutlined,
  AddOutlined,
  CodeOutlined,
  GridViewOutlined,
  CloseOutlined,
} from '@mui/icons-material'
import { useQuery, useQueryClient } from '@tanstack/react-query'
import { generatorsApi, GeneratorGroup, GeneratorItem, GeneratorUpdate, SheetInfo, SheetSchema } from '../api/generatorsApi'
import PageHeader from '../components/PageHeader'
import { useProduct } from '../store/ProductContext'

// ─── Colours ──────────────────────────────────────────────────────────────────
const SECTION_COLOR: Record<string, string> = {
  '00': '#888888',
  'A.5': '#4472C4',
  'A.6': '#70AD47',
  'A.7': '#ED7D31',
  'A.8': '#9370DB',
}

const PRODUCT_TYPE_COLOR: Record<string, string> = {
  framework:   '#4472C4',
  operational: '#1565C0',
  privacy:     '#7030A0',
  cloud:       '#00897B',
}

const PRODUCT_TYPE_LABEL: Record<string, string> = {
  framework:   'FW',
  operational: 'OP',
  privacy:     'PRIV',
  cloud:       'CLD',
}

function groupColor(group: GeneratorGroup): string {
  if (SECTION_COLOR[group.section]) return SECTION_COLOR[group.section]
  const pt = group.generators[0]?.product_type ?? 'framework'
  return PRODUCT_TYPE_COLOR[pt] ?? '#4472C4'
}

const SHEET_TYPE_COLOR: Record<string, string> = {
  instructions: '#4472C4',
  input: '#003366',
  summary: '#70AD47',
  evidence: '#ED7D31',
  approval: '#C00000',
}

const SHEET_TYPE_LABEL: Record<string, string> = {
  instructions: 'IL',
  input: 'Data',
  summary: 'SD',
  evidence: 'ER',
  approval: 'AS',
}

// ─── Sheet list ───────────────────────────────────────────────────────────────
function SheetList({ sheets }: { sheets: SheetInfo[] }) {
  return (
    <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 0.5, mt: 1 }}>
      {sheets.map((s) => (
        <Tooltip key={s.name} title={s.name} arrow>
          <Chip
            label={SHEET_TYPE_LABEL[s.type] ?? s.type}
            size="small"
            sx={{
              height: 20,
              fontSize: '0.65rem',
              fontWeight: 700,
              bgcolor: `${SHEET_TYPE_COLOR[s.type] ?? '#888'}18`,
              color: SHEET_TYPE_COLOR[s.type] ?? '#888',
              border: `1px solid ${SHEET_TYPE_COLOR[s.type] ?? '#888'}40`,
              cursor: 'default',
            }}
          />
        </Tooltip>
      ))}
    </Box>
  )
}

// ─── Workbook preview drawer ───────────────────────────────────────────────────
function SheetSchemaTab({ schema }: { schema: SheetSchema }) {
  if (!schema.columns.length) {
    return <Typography variant="body2" sx={{ p: 2, color: 'text.secondary' }}>No column data extracted.</Typography>
  }
  return (
    <Box sx={{ overflow: 'auto' }}>
      <Box sx={{ px: 2, py: 1, display: 'flex', gap: 2, flexWrap: 'wrap' }}>
        {schema.freeze_panes && (
          <Chip label={`Freeze: ${schema.freeze_panes}`} size="small" sx={{ height: 20, fontSize: '0.65rem' }} />
        )}
        {schema.status_column_letter && (
          <Chip
            label={`Status col: ${schema.status_column_letter}`}
            size="small"
            sx={{ height: 20, fontSize: '0.65rem', bgcolor: '#FFF3CD', color: '#856404', border: '1px solid #FFC00060' }}
          />
        )}
        {schema.header_row && (
          <Chip label={`Header row: ${schema.header_row}`} size="small" sx={{ height: 20, fontSize: '0.65rem' }} />
        )}
      </Box>
      <Table size="small" stickyHeader>
        <TableHead>
          <TableRow>
            {['#', 'Col', 'Header', 'Width', 'DV Values', 'Flags'].map(h => (
              <TableCell key={h} sx={{ fontWeight: 700, fontSize: '0.7rem', py: 0.5, whiteSpace: 'nowrap', bgcolor: '#F2F2F2' }}>
                {h}
              </TableCell>
            ))}
          </TableRow>
        </TableHead>
        <TableBody>
          {schema.columns.map(col => (
            <TableRow
              key={col.index}
              sx={{
                bgcolor: col.is_status_col ? '#FFF8E1' : 'inherit',
                '&:hover': { bgcolor: col.is_status_col ? '#FFF3CD' : 'action.hover' },
              }}
            >
              <TableCell sx={{ fontSize: '0.7rem', py: 0.4, color: 'text.secondary', width: 32 }}>{col.index}</TableCell>
              <TableCell sx={{ fontSize: '0.7rem', py: 0.4, fontFamily: 'monospace', fontWeight: 700, color: '#003366', width: 36 }}>{col.letter}</TableCell>
              <TableCell sx={{ fontSize: '0.75rem', py: 0.4, fontWeight: col.is_status_col ? 700 : 400 }}>
                {col.header}
                {col.required && <Chip label="*" size="small" sx={{ ml: 0.5, height: 16, fontSize: '0.6rem', bgcolor: '#FFC7CE', color: '#C00000' }} />}
              </TableCell>
              <TableCell sx={{ fontSize: '0.7rem', py: 0.4, color: 'text.secondary', width: 52 }}>{col.width}</TableCell>
              <TableCell sx={{ fontSize: '0.68rem', py: 0.4, maxWidth: 220 }}>
                {col.dv_values.length > 0 ? (
                  <Box sx={{ display: 'flex', flexWrap: 'wrap', gap: 0.25 }}>
                    {col.dv_values.slice(0, 6).map((v, i) => (
                      <Chip key={i} label={v} size="small" sx={{ height: 16, fontSize: '0.6rem', maxWidth: 160 }} />
                    ))}
                    {col.dv_values.length > 6 && (
                      <Typography variant="caption" sx={{ color: 'text.secondary', alignSelf: 'center' }}>
                        +{col.dv_values.length - 6} more
                      </Typography>
                    )}
                  </Box>
                ) : (
                  <Typography variant="caption" sx={{ color: 'text.disabled' }}>—</Typography>
                )}
              </TableCell>
              <TableCell sx={{ fontSize: '0.65rem', py: 0.4, width: 60 }}>
                {col.is_status_col && <Chip label="STATUS" size="small" sx={{ height: 16, fontSize: '0.58rem', bgcolor: '#FFC7CE40', color: '#856404' }} />}
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </Box>
  )
}

function WorkbookPreviewDrawer({
  gen,
  open,
  onClose,
}: {
  gen: GeneratorItem
  open: boolean
  onClose: () => void
}) {
  const [tab, setTab] = useState(0)
  const schemas = gen.sheet_schemas

  const handleTabChange = (_: React.SyntheticEvent, v: number) => setTab(v)

  return (
    <Drawer
      anchor="right"
      open={open}
      onClose={onClose}
      PaperProps={{ sx: { width: { xs: '100%', sm: 720 }, display: 'flex', flexDirection: 'column' } }}
    >
      {/* Header */}
      <Box sx={{ p: 2, borderBottom: 1, borderColor: 'divider', display: 'flex', alignItems: 'flex-start', gap: 1 }}>
        <Box sx={{ flex: 1, minWidth: 0 }}>
          <Typography variant="subtitle1" sx={{ fontWeight: 700, lineHeight: 1.2 }}>{gen.workbook_name}</Typography>
          <Typography variant="caption" sx={{ fontFamily: 'monospace', color: 'text.secondary' }}>{gen.document_id}</Typography>
        </Box>
        <IconButton size="small" onClick={onClose}><CloseOutlined fontSize="small" /></IconButton>
      </Box>

      {schemas.length === 0 ? (
        <Box sx={{ p: 2 }}>
          <Alert severity="info" sx={{ mb: 2 }}>
            Detailed column schema not yet extracted. Showing sheet structure from generator metadata.
          </Alert>
          <Typography variant="caption" sx={{ fontWeight: 600, color: 'text.secondary', display: 'block', mb: 1 }}>
            SHEETS ({gen.sheet_count})
          </Typography>
          <Stack spacing={0.5}>
            {gen.sheets.map((s, i) => (
              <Box key={i} sx={{ display: 'flex', alignItems: 'center', gap: 1, py: 0.5, px: 1, borderRadius: 1, bgcolor: `${SHEET_TYPE_COLOR[s.type] ?? '#888'}08`, border: `1px solid ${SHEET_TYPE_COLOR[s.type] ?? '#888'}20` }}>
                <Box sx={{ width: 8, height: 8, borderRadius: '50%', bgcolor: SHEET_TYPE_COLOR[s.type] ?? '#888', flexShrink: 0 }} />
                <Typography variant="body2" sx={{ flex: 1, fontSize: '0.8rem' }}>{s.name}</Typography>
                <Chip
                  label={s.type}
                  size="small"
                  sx={{ height: 18, fontSize: '0.6rem', bgcolor: `${SHEET_TYPE_COLOR[s.type] ?? '#888'}15`, color: SHEET_TYPE_COLOR[s.type] ?? '#888', flexShrink: 0 }}
                />
              </Box>
            ))}
          </Stack>
          {gen.is_stacked && gen.stacked_control_ids && (
            <Box sx={{ mt: 2 }}>
              <Typography variant="caption" sx={{ fontWeight: 600, color: 'text.secondary', display: 'block', mb: 0.5 }}>
                COVERS CONTROLS
              </Typography>
              <Box sx={{ display: 'flex', gap: 0.5, flexWrap: 'wrap' }}>
                {gen.stacked_control_ids.map(cid => (
                  <Chip key={cid} label={cid} size="small" sx={{ height: 20, fontSize: '0.65rem', fontFamily: 'monospace' }} />
                ))}
              </Box>
            </Box>
          )}
        </Box>
      ) : (
        <>
          {/* Sheet tabs */}
          <Tabs
            value={Math.min(tab, schemas.length - 1)}
            onChange={handleTabChange}
            variant="scrollable"
            scrollButtons="auto"
            sx={{
              borderBottom: 1,
              borderColor: 'divider',
              minHeight: 36,
              '& .MuiTab-root': { minHeight: 36, fontSize: '0.7rem', py: 0.5, px: 1.5, textTransform: 'none' },
            }}
          >
            {schemas.map((s, i) => (
              <Tab
                key={i}
                label={
                  <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.5 }}>
                    <Box sx={{
                      width: 6, height: 6, borderRadius: '50%', flexShrink: 0,
                      bgcolor: SHEET_TYPE_COLOR[s.sheet_type] ?? '#888',
                    }} />
                    <span style={{ maxWidth: 120, overflow: 'hidden', textOverflow: 'ellipsis', whiteSpace: 'nowrap' }}>
                      {s.sheet_name}
                    </span>
                  </Box>
                }
              />
            ))}
          </Tabs>

          {/* Tab panel */}
          <Box sx={{ flex: 1, overflow: 'auto' }}>
            {schemas[Math.min(tab, schemas.length - 1)] && (
              <SheetSchemaTab schema={schemas[Math.min(tab, schemas.length - 1)]} />
            )}
          </Box>

          {/* Footer */}
          <Box sx={{ px: 2, py: 1, borderTop: 1, borderColor: 'divider', display: 'flex', gap: 2 }}>
            <Typography variant="caption" color="text.secondary">
              {schemas.length} sheets · {schemas.reduce((s, sh) => s + sh.columns.length, 0)} columns total
            </Typography>
            <Typography variant="caption" color="text.secondary">
              {schemas.filter(s => s.status_column_index).length} sheets with status column
            </Typography>
          </Box>
        </>
      )}
    </Drawer>
  )
}

// ─── Edit dialog ──────────────────────────────────────────────────────────────
const SHEET_TYPES: SheetInfo['type'][] = ['instructions', 'input', 'summary', 'evidence', 'approval']

function EditDialog({
  gen,
  open,
  onClose,
  onSaved,
}: {
  gen: GeneratorItem
  open: boolean
  onClose: () => void
  onSaved: (updated: GeneratorItem) => void
}) {
  const [workbookName, setWorkbookName] = useState(gen.workbook_name)
  const [domainNumber, setDomainNumber] = useState<string>(gen.domain_number?.toString() ?? '')
  const [domainTotal, setDomainTotal] = useState<string>(gen.domain_total?.toString() ?? '')
  const [sheets, setSheets] = useState<SheetInfo[]>([...gen.sheets])
  const [saving, setSaving] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const handleSheetName = (i: number, name: string) =>
    setSheets(prev => prev.map((s, idx) => idx === i ? { ...s, name } : s))

  const handleSheetType = (i: number, type: SheetInfo['type']) =>
    setSheets(prev => prev.map((s, idx) => idx === i ? { ...s, type } : s))

  const handleSheetDelete = (i: number) =>
    setSheets(prev => prev.filter((_, idx) => idx !== i))

  const handleSheetAdd = () =>
    setSheets(prev => [...prev, { name: '', type: 'input' }])

  const handleSave = async () => {
    if (!workbookName.trim()) { setError('Workbook name is required'); return }
    if (sheets.some(s => !s.name.trim())) { setError('All sheet names must be filled in'); return }
    setSaving(true)
    setError(null)
    try {
      const body: GeneratorUpdate = {
        workbook_name: workbookName.trim(),
        domain_number: domainNumber ? parseInt(domainNumber) : null,
        domain_total: domainTotal ? parseInt(domainTotal) : null,
        sheets,
      }
      const updated = await generatorsApi.update(gen.document_id, body)
      onSaved(updated)
      onClose()
    } catch {
      setError('Save failed — please try again')
    } finally {
      setSaving(false)
    }
  }

  return (
    <Dialog open={open} onClose={onClose} maxWidth="sm" fullWidth>
      <DialogTitle sx={{ pb: 1 }}>
        Edit Generator Definition
        <Typography variant="caption" display="block" sx={{ color: 'text.secondary', fontFamily: 'monospace' }}>
          {gen.document_id}
        </Typography>
      </DialogTitle>
      <DialogContent dividers>
        <Stack spacing={2}>
          {error && <Alert severity="error">{error}</Alert>}

          <TextField
            label="Workbook Name"
            value={workbookName}
            onChange={e => setWorkbookName(e.target.value)}
            size="small"
            fullWidth
          />

          <Box sx={{ display: 'flex', gap: 2 }}>
            <TextField
              label="Domain Number"
              value={domainNumber}
              onChange={e => setDomainNumber(e.target.value)}
              size="small"
              type="number"
              sx={{ flex: 1 }}
            />
            <TextField
              label="Total Domains"
              value={domainTotal}
              onChange={e => setDomainTotal(e.target.value)}
              size="small"
              type="number"
              sx={{ flex: 1 }}
            />
          </Box>

          <Box>
            <Box sx={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', mb: 1 }}>
              <Typography variant="caption" sx={{ fontWeight: 600, color: 'text.secondary' }}>
                SHEETS ({sheets.length})
              </Typography>
              <Button size="small" startIcon={<AddOutlined />} onClick={handleSheetAdd}>
                Add Sheet
              </Button>
            </Box>
            <Stack spacing={0.75}>
              {sheets.map((s, i) => (
                <Box key={i} sx={{ display: 'flex', gap: 1, alignItems: 'center' }}>
                  <TextField
                    value={s.name}
                    onChange={e => handleSheetName(i, e.target.value)}
                    size="small"
                    placeholder="Sheet name"
                    sx={{ flex: 1 }}
                  />
                  <FormControl size="small" sx={{ minWidth: 120 }}>
                    <Select
                      value={s.type}
                      onChange={e => handleSheetType(i, e.target.value as SheetInfo['type'])}
                    >
                      {SHEET_TYPES.map(t => (
                        <MenuItem key={t} value={t}>
                          <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.75 }}>
                            <Box sx={{ width: 8, height: 8, borderRadius: '50%', bgcolor: SHEET_TYPE_COLOR[t] ?? '#888' }} />
                            {t}
                          </Box>
                        </MenuItem>
                      ))}
                    </Select>
                  </FormControl>
                  <IconButton
                    size="small"
                    onClick={() => handleSheetDelete(i)}
                    disabled={sheets.length === 1}
                    sx={{ color: 'error.main' }}
                  >
                    <DeleteOutlined fontSize="small" />
                  </IconButton>
                </Box>
              ))}
            </Stack>
          </Box>
        </Stack>
      </DialogContent>
      <DialogActions>
        <Button onClick={onClose} disabled={saving}>Cancel</Button>
        <Button variant="contained" onClick={handleSave} disabled={saving}>
          {saving ? 'Saving…' : 'Save & Lock'}
        </Button>
      </DialogActions>
    </Dialog>
  )
}

// ─── Single generator card ────────────────────────────────────────────────────
function GeneratorCard({ gen: initialGen }: { gen: GeneratorItem }) {
  const [expanded, setExpanded] = useState(false)
  const [editOpen, setEditOpen] = useState(false)
  const [previewOpen, setPreviewOpen] = useState(false)
  const [gen, setGen] = useState(initialGen)
  const [generating, setGenerating] = useState(false)
  const queryClient = useQueryClient()

  const handleSaved = (updated: GeneratorItem) => {
    setGen(updated)
    queryClient.invalidateQueries({ queryKey: ['generators-grouped'] })
  }

  const handleClearOverride = async () => {
    const updated = await generatorsApi.clearOverride(gen.document_id)
    setGen(updated)
    queryClient.invalidateQueries({ queryKey: ['generators-grouped'] })
  }

  const handleGenerateScript = async () => {
    setGenerating(true)
    try {
      const { blob, filename } = await generatorsApi.generateScript(gen.document_id)
      const url = URL.createObjectURL(blob)
      const a = document.createElement('a')
      a.href = url
      a.download = filename
      a.click()
      URL.revokeObjectURL(url)
    } finally {
      setGenerating(false)
    }
  }

  const domainLabel = gen.domain_number != null
    ? gen.domain_total != null
      ? `Domain ${gen.domain_number} of ${gen.domain_total}`
      : `Domain ${gen.domain_number}`
    : null

  return (
    <>
      <Card
        variant="outlined"
        sx={{
          mb: 1,
          borderColor: gen.user_override ? '#FFC000' : 'divider',
          '&:hover': { borderColor: gen.user_override ? '#FFC000' : 'primary.main', boxShadow: 1 },
          transition: 'all 0.12s',
        }}
      >
        <CardContent sx={{ p: '10px 14px !important' }}>
          {/* Top row */}
          <Box sx={{ display: 'flex', alignItems: 'flex-start', gap: 1 }}>
            <Box sx={{ flex: 1, minWidth: 0 }}>
              <Typography variant="body2" sx={{ fontWeight: 700, fontSize: '0.82rem', lineHeight: 1.3 }}>
                {gen.workbook_name}
              </Typography>
              <Typography variant="caption" sx={{ color: 'text.secondary', fontFamily: 'monospace', fontSize: '0.7rem' }}>
                {gen.document_id}
              </Typography>
            </Box>
            <Box sx={{ display: 'flex', alignItems: 'center', gap: 0.5, flexShrink: 0 }}>
              {gen.product_type !== 'framework' && (
                <Chip
                  label={PRODUCT_TYPE_LABEL[gen.product_type] ?? gen.product_type.toUpperCase()}
                  size="small"
                  sx={{
                    height: 20, fontSize: '0.65rem', fontWeight: 700,
                    bgcolor: `${PRODUCT_TYPE_COLOR[gen.product_type] ?? '#888'}18`,
                    color: PRODUCT_TYPE_COLOR[gen.product_type] ?? '#888',
                    border: `1px solid ${PRODUCT_TYPE_COLOR[gen.product_type] ?? '#888'}40`,
                  }}
                />
              )}
              {gen.user_override && (
                <Tooltip title="Manually edited — importer will not overwrite. Click to reset." arrow>
                  <Chip
                    label="Override"
                    size="small"
                    onClick={handleClearOverride}
                    sx={{ height: 20, fontSize: '0.65rem', bgcolor: '#FFF3CD', color: '#856404', border: '1px solid #FFC00060', cursor: 'pointer' }}
                  />
                </Tooltip>
              )}
              {gen.is_stacked && (
                <Tooltip title={`Stacked: ${gen.stacked_control_ids?.join(', ')}`} arrow>
                  <Chip
                    icon={<LayersOutlined sx={{ fontSize: '0.8rem !important' }} />}
                    label="Stacked"
                    size="small"
                    sx={{ height: 20, fontSize: '0.65rem', bgcolor: '#FFC7CE20', color: '#C00000', border: '1px solid #C0000040' }}
                  />
                </Tooltip>
              )}
              {domainLabel && (
                <Chip
                  label={domainLabel}
                  size="small"
                  sx={{ height: 20, fontSize: '0.65rem', bgcolor: '#E3F2FD', color: '#1565C0', border: '1px solid #1565C040' }}
                />
              )}
              <Chip
                label={`${gen.sheet_count} sheets`}
                size="small"
                icon={<TableChartOutlined sx={{ fontSize: '0.75rem !important' }} />}
                sx={{ height: 20, fontSize: '0.65rem', bgcolor: 'action.hover' }}
              />
              <Tooltip title="Workbook preview" arrow>
                <IconButton size="small" onClick={() => setPreviewOpen(true)} sx={{ p: 0.25 }}>
                  <GridViewOutlined sx={{ fontSize: '1rem' }} />
                </IconButton>
              </Tooltip>
              <Tooltip title={gen.product_type === 'framework' ? 'Generate .py script' : 'Download source script'} arrow>
                <IconButton size="small" onClick={handleGenerateScript} disabled={generating} sx={{ p: 0.25 }}>
                  <CodeOutlined sx={{ fontSize: '1rem' }} />
                </IconButton>
              </Tooltip>
              <Tooltip title="Edit" arrow>
                <IconButton size="small" onClick={() => setEditOpen(true)} sx={{ p: 0.25 }}>
                  <EditOutlined sx={{ fontSize: '1rem' }} />
                </IconButton>
              </Tooltip>
              <IconButton size="small" onClick={() => setExpanded(o => !o)} sx={{ p: 0.25 }}>
                {expanded ? <ExpandLessOutlined fontSize="small" /> : <ExpandMoreOutlined fontSize="small" />}
              </IconButton>
            </Box>
          </Box>

          {/* Collapsed: compact sheet type strip */}
          {!expanded && <SheetList sheets={gen.sheets} />}

          {/* Expanded: full sheet names */}
          <Collapse in={expanded} unmountOnExit>
            <Divider sx={{ my: 1 }} />
            <Typography variant="caption" sx={{ color: 'text.secondary', fontWeight: 600 }}>
              Sheets ({gen.sheet_count})
            </Typography>
            <Stack spacing={0.25} sx={{ mt: 0.5 }}>
              {gen.sheets.map((s, i) => (
                <Box key={i} sx={{ display: 'flex', alignItems: 'center', gap: 1 }}>
                  <Chip
                    label={s.type}
                    size="small"
                    sx={{
                      height: 18, width: 80, fontSize: '0.6rem',
                      bgcolor: `${SHEET_TYPE_COLOR[s.type] ?? '#888'}15`,
                      color: SHEET_TYPE_COLOR[s.type] ?? '#888',
                      flexShrink: 0,
                    }}
                  />
                  <Typography variant="caption" sx={{ fontSize: '0.75rem' }}>{s.name}</Typography>
                </Box>
              ))}
            </Stack>
            {gen.is_stacked && gen.stacked_control_ids && (
              <Box sx={{ mt: 1 }}>
                <Typography variant="caption" sx={{ color: 'text.secondary', fontWeight: 600 }}>
                  Covers controls:
                </Typography>
                <Box sx={{ display: 'flex', gap: 0.5, flexWrap: 'wrap', mt: 0.25 }}>
                  {gen.stacked_control_ids.map(cid => (
                    <Chip key={cid} label={cid} size="small" sx={{ height: 18, fontSize: '0.65rem', fontFamily: 'monospace' }} />
                  ))}
                </Box>
              </Box>
            )}
          </Collapse>
        </CardContent>
      </Card>

      <EditDialog
        gen={gen}
        open={editOpen}
        onClose={() => setEditOpen(false)}
        onSaved={handleSaved}
      />

      <WorkbookPreviewDrawer
        gen={gen}
        open={previewOpen}
        onClose={() => setPreviewOpen(false)}
      />
    </>
  )
}

// ─── Control group block ──────────────────────────────────────────────────────
function GroupBlock({ group }: { group: GeneratorGroup }) {
  const sectionColor = groupColor(group)
  return (
    <Box sx={{ mb: 3 }}>
      <Box sx={{ display: 'flex', alignItems: 'center', gap: 1, mb: 1 }}>
        <Box sx={{ width: 4, height: 32, borderRadius: 1, bgcolor: sectionColor, flexShrink: 0 }} />
        <Box>
          <Typography variant="subtitle2" sx={{ fontWeight: 700, lineHeight: 1.2 }}>
            {group.group_code.toUpperCase()} — {group.control_name}
          </Typography>
          <Typography variant="caption" sx={{ color: 'text.secondary' }}>
            {group.generators.length} workbook{group.generators.length !== 1 ? 's' : ''}
            {group.total_domains > 1 ? ` · ${group.total_domains} assessment domains` : ''}
          </Typography>
        </Box>
      </Box>
      {group.generators.map(gen => (
        <GeneratorCard key={gen.document_id} gen={gen} />
      ))}
    </Box>
  )
}

// ─── Main page ────────────────────────────────────────────────────────────────
function apiProductParam(product: string, ismsTier: string): string | undefined {
  if (product === 'privacy') return 'privacy'
  if (product === 'cloud') return 'cloud'
  // isms
  if (ismsTier === 'framework') return 'framework'
  if (ismsTier === 'operational') return 'operational'
  return 'isms'
}

export default function Generators() {
  const { product, ismsTier } = useProduct()
  const [sectionFilter, setSectionFilter] = useState('All')
  const [search, setSearch] = useState('')

  const apiProduct = apiProductParam(product, ismsTier)

  // Reset section filter when product changes
  useEffect(() => {
    setSectionFilter('All')
  }, [apiProduct])

  const { data, isLoading, error } = useQuery({
    queryKey: ['generators-grouped', apiProduct, sectionFilter],
    queryFn: () =>
      generatorsApi.grouped({
        product: apiProduct,
        ...(sectionFilter !== 'All' ? { section: sectionFilter } : {}),
      }),
  })

  // Dynamic sections from loaded data
  const sections = ['All', ...Array.from(new Set((data ?? []).map((g: GeneratorGroup) => g.section))).sort()]

  // Client-side search filter on group name / workbook name / doc ID
  const filtered = data?.filter((g: GeneratorGroup) => {
    if (!search.trim()) return true
    const q = search.toLowerCase()
    return (
      g.group_code.toLowerCase().includes(q) ||
      g.control_name.toLowerCase().includes(q) ||
      g.generators.some(
        (gen: GeneratorItem) =>
          gen.workbook_name.toLowerCase().includes(q) ||
          gen.document_id.toLowerCase().includes(q)
      )
    )
  })

  // Counts for metric strip
  const totalGroups = data?.length ?? 0
  const totalGenerators = data?.reduce((s: number, g: GeneratorGroup) => s + g.generators.length, 0) ?? 0
  const totalSheets = data?.reduce(
    (s: number, g: GeneratorGroup) => s + g.generators.reduce((ss: number, gen: GeneratorItem) => ss + gen.sheet_count, 0),
    0
  ) ?? 0
  const totalStacked = data?.reduce(
    (s: number, g: GeneratorGroup) => s + g.generators.filter((gen: GeneratorItem) => gen.is_stacked).length,
    0
  ) ?? 0

  return (
    <Box>
      <PageHeader
        title="Generators"
        subtitle={
          isLoading
            ? 'Loading generators…'
            : `${totalGenerators} generator${totalGenerators !== 1 ? 's' : ''} · ${totalGroups} control group${totalGroups !== 1 ? 's' : ''}`
        }
      />

      {/* Metric strip */}
      <Box sx={{ display: 'flex', gap: 2, mb: 3, flexWrap: 'wrap' }}>
        {[
          { label: 'Control Groups', value: totalGroups },
          { label: 'Generators', value: totalGenerators },
          { label: 'Total Sheets', value: totalSheets },
          { label: 'Stacked', value: totalStacked },
        ].map(m => (
          <Card key={m.label} variant="outlined" sx={{ minWidth: 120 }}>
            <CardContent sx={{ p: '10px 16px !important' }}>
              <Typography variant="h5" sx={{ fontWeight: 700, color: 'primary.main' }}>
                {isLoading ? <Skeleton width={40} /> : m.value}
              </Typography>
              <Typography variant="caption" color="text.secondary">
                {m.label}
              </Typography>
            </CardContent>
          </Card>
        ))}
      </Box>

      {/* Filters */}
      <Box sx={{ display: 'flex', gap: 2, mb: 3, flexWrap: 'wrap', alignItems: 'center' }}>
        <TextField
          size="small"
          placeholder="Search controls or workbooks…"
          value={search}
          onChange={e => setSearch(e.target.value)}
          InputProps={{ startAdornment: <InputAdornment position="start"><SearchOutlined fontSize="small" /></InputAdornment> }}
          sx={{ width: 300 }}
        />
        <ToggleButtonGroup
          size="small"
          exclusive
          value={sectionFilter}
          onChange={(_, v) => v && setSectionFilter(v)}
        >
          {sections.map(s => (
            <ToggleButton key={s} value={s} sx={{ px: 2, fontSize: '0.75rem' }}>
              {s}
            </ToggleButton>
          ))}
        </ToggleButtonGroup>
      </Box>

      {/* Content */}
      {error && <Alert severity="error" sx={{ mb: 2 }}>Failed to load generator registry.</Alert>}

      {isLoading ? (
        Array.from({ length: 6 }).map((_, i) => (
          <Box key={i} sx={{ mb: 3 }}>
            <Skeleton variant="text" width={300} height={28} />
            <Skeleton variant="rounded" height={80} sx={{ mt: 0.5 }} />
            <Skeleton variant="rounded" height={80} sx={{ mt: 1 }} />
          </Box>
        ))
      ) : filtered?.length === 0 ? (
        <Alert severity="info">No generators match your filter.</Alert>
      ) : (
        filtered?.map(group => <GroupBlock key={group.group_code} group={group} />)
      )}
    </Box>
  )
}
