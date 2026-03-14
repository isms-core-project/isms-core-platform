import { useState } from 'react'
import { Box, Typography, Table, TableHead, TableBody, TableRow, TableCell, Button, Divider, Chip, Skeleton, ToggleButtonGroup, ToggleButton } from '@mui/material'
import { PrintOutlined, FileDownloadOutlined } from '@mui/icons-material'
import { useQuery } from '@tanstack/react-query'
import { dashboardApi } from '../api/dashboard'
import { controlsApi } from '../api/controls'
import { useProduct, PRODUCT_COLORS, PRODUCT_LABELS, type Product } from '../store/ProductContext'

// Actual API shape (the types.ts interface is outdated)
interface GroupRow {
  id: string
  group_code: string
  name: string
  section: string
  section_name: string
  has_framework: boolean   // has policy
  product_family: string
}

// Local shape aliases matching Overview.tsx
interface SectionRow {
  section: string
  section_name: string
  total_controls: number
  framework_covered: number
  operational_covered: number
  framework_pct: number
  operational_pct: number
}

interface RealOverview {
  total_controls: number
  total_policies: number
  total_implementations: number
  total_assessments: number
  total_gaps_open: number
  framework: { coverage_pct: number; has_policy: number; has_ug: number; has_tg: number; has_assessment: number }
  operational: { coverage_pct: number }
  sections: SectionRow[]
}

interface RealReadiness {
  policies_pct: number
  ug_pct: number
  tg_pct: number
  assessments_pct: number
  evidence_pct: number
  gaps_closed_pct: number
  composite_score: number
  status: 'green' | 'amber' | 'red'
}

const STATUS_LABEL: Record<string, string> = { green: 'Compliant', amber: 'Partially Compliant', red: 'Non-Compliant' }
const STATUS_BG: Record<string, string>    = { green: '#1a3a27', amber: '#3a2e00', red: '#3a0000' }
const STATUS_FG: Record<string, string>    = { green: '#C6EFCE', amber: '#FFEB9C', red: '#FFC7CE' }

const STANDARD_NAMES: Record<Product, string> = {
  isms:    'ISO/IEC 27001:2022',
  privacy: 'ISO/IEC 27701:2025',
  cloud:   'ISO/IEC 27018:2025',
}

const HEADER_COLORS: Record<Product, string> = {
  isms:    '#4472C4',
  privacy: PRODUCT_COLORS.privacy,
  cloud:   PRODUCT_COLORS.cloud,
}

function pct(v: number) { return `${v.toFixed(0)}%` }

function exportCsv(sections: SectionRow[]) {
  const headers = ['section', 'section_name', 'total_controls', 'framework_covered', 'framework_pct', 'operational_covered', 'operational_pct']
  const rows = sections.map((s) => [
    s.section,
    s.section_name,
    s.total_controls,
    s.framework_covered,
    s.framework_pct.toFixed(1),
    s.operational_covered,
    s.operational_pct.toFixed(1),
  ])
  const csv = [headers.join(','), ...rows.map((r) => r.join(','))].join('\n')
  const today = new Date().toISOString().slice(0, 10).replace(/-/g, '')
  const url = URL.createObjectURL(new Blob([csv], { type: 'text/csv' }))
  const a = document.createElement('a')
  a.href = url
  a.download = `isms-report-${today}.csv`
  a.click()
  URL.revokeObjectURL(url)
}

const TH_STYLE = { fontWeight: 700, fontSize: '0.78rem', color: '#1a1a2e', bgcolor: '#e8ecf4', borderBottom: '2px solid #c8d0e0' }
const TD_STYLE = { fontSize: '0.8rem', color: '#1a1a2e', borderBottom: '1px solid #e0e4ec' }

export default function Report() {
  const { product: activeProduct } = useProduct()
  const [reportProduct, setReportProduct] = useState<Product>(activeProduct)

  const { data: overview, isLoading: ovLoading } = useQuery({
    queryKey: ['dashboard', 'overview'],
    queryFn: dashboardApi.getOverview,
  })
  const { data: readiness, isLoading: rdLoading } = useQuery({
    queryKey: ['dashboard', 'audit-readiness'],
    queryFn: dashboardApi.getAuditReadiness,
  })
  const { data: homeSummary, isLoading: hsLoading } = useQuery({
    queryKey: ['home-summary'],
    queryFn: dashboardApi.getHomeSummary,
    staleTime: 30_000,
  })

  const { data: groupsRaw, isLoading: grLoading } = useQuery({
    queryKey: ['controls', 'list', reportProduct],
    queryFn: () => controlsApi.list({ product_family: reportProduct.toUpperCase() }),
    enabled: reportProduct !== 'isms',
  })
  const groups = (groupsRaw as unknown as GroupRow[] | undefined) ?? []

  const ov = overview as unknown as RealOverview | undefined
  const rd = readiness as unknown as RealReadiness | undefined
  const loading = reportProduct === 'isms' ? (ovLoading || rdLoading) : (hsLoading || grLoading)
  const generatedDate = new Date().toLocaleDateString('en-GB', { year: 'numeric', month: 'long', day: 'numeric' })

  const readinessRows = rd ? [
    { name: 'Policies',     value: rd.policies_pct },
    { name: 'User Guides',  value: rd.ug_pct },
    { name: 'Tech Guides',  value: rd.tg_pct },
    { name: 'Assessments',  value: rd.assessments_pct },
    { name: 'Evidence',     value: rd.evidence_pct },
    { name: 'Gaps Closed',  value: rd.gaps_closed_pct },
  ] : []

  const headerColor = HEADER_COLORS[reportProduct]
  const standardName = STANDARD_NAMES[reportProduct]
  const productSummary = homeSummary?.[reportProduct]

  if (loading) {
    return (
      <Box sx={{ p: 4 }}>
        <Skeleton variant="rectangular" height={80} sx={{ mb: 2 }} />
        <Skeleton variant="rectangular" height={200} sx={{ mb: 2 }} />
        <Skeleton variant="rectangular" height={300} />
      </Box>
    )
  }

  return (
    <Box>
      {/* Action buttons — hidden in print */}
      <Box sx={{ display: 'flex', alignItems: 'center', gap: 1.5, mb: 3, flexWrap: 'wrap', '@media print': { display: 'none' } }}>
        {/* ISO selector */}
        <ToggleButtonGroup
          value={reportProduct}
          exclusive
          onChange={(_, v) => v && setReportProduct(v)}
          size="small"
        >
          {(['isms', 'privacy', 'cloud'] as Product[]).map((p) => (
            <ToggleButton
              key={p}
              value={p}
              sx={{
                fontSize: '0.72rem',
                px: 1.5,
                '&.Mui-selected': { bgcolor: `${HEADER_COLORS[p]}22`, color: HEADER_COLORS[p], borderColor: `${HEADER_COLORS[p]}55` },
              }}
            >
              {PRODUCT_LABELS[p]}
            </ToggleButton>
          ))}
        </ToggleButtonGroup>

        <Button
          variant="contained"
          startIcon={<PrintOutlined />}
          onClick={() => window.print()}
        >
          Print / Save as PDF
        </Button>
        {reportProduct === 'isms' && (
          <Button
            variant="outlined"
            startIcon={<FileDownloadOutlined />}
            onClick={() => ov && exportCsv(ov.sections)}
            disabled={!ov}
          >
            Export CSV
          </Button>
        )}
      </Box>

      {/* Report body — white background for print */}
      <Box
        sx={{
          bgcolor: 'white',
          color: '#1a1a2e',
          p: { xs: 3, md: 5 },
          borderRadius: 2,
          maxWidth: 900,
          mx: 'auto',
          boxShadow: '0 2px 12px rgba(0,0,0,0.18)',
          '@media print': {
            boxShadow: 'none',
            borderRadius: 0,
            p: 4,
            maxWidth: '100%',
          },
        }}
      >
        {/* Report header */}
        <Box sx={{ mb: 3, pb: 2, borderBottom: `2px solid ${headerColor}` }}>
          <Typography variant="h4" sx={{ color: '#003366', fontWeight: 700, mb: 0.5 }}>
            ISMS CORE — {PRODUCT_LABELS[reportProduct]} Compliance Report
          </Typography>
          <Typography variant="body2" sx={{ color: '#555' }}>
            {standardName} · Generated {generatedDate}
          </Typography>
        </Box>

        {/* ── ISMS full report ── */}
        {reportProduct === 'isms' && (
          <>
            {/* Section 1 — Executive Summary */}
            <Box sx={{ mb: 4 }}>
              <Typography variant="h6" sx={{ color: '#003366', fontWeight: 700, mb: 1.5, textTransform: 'uppercase', letterSpacing: '0.06em', fontSize: '0.85rem' }}>
                1 — Executive Summary
              </Typography>

              {rd && (
                <Box sx={{ display: 'flex', alignItems: 'center', gap: 2, mb: 2 }}>
                  <Box
                    sx={{
                      px: 2.5, py: 1.5, borderRadius: 2,
                      bgcolor: STATUS_BG[rd.status], border: `1px solid ${STATUS_FG[rd.status]}40`,
                    }}
                  >
                    <Typography sx={{ fontSize: '2rem', fontWeight: 800, color: STATUS_FG[rd.status], lineHeight: 1 }}>
                      {rd.composite_score}%
                    </Typography>
                    <Typography sx={{ fontSize: '0.7rem', color: STATUS_FG[rd.status], opacity: 0.8, mt: 0.25 }}>
                      Composite Score
                    </Typography>
                  </Box>
                  <Box>
                    <Chip
                      label={STATUS_LABEL[rd.status]}
                      size="small"
                      sx={{ bgcolor: STATUS_BG[rd.status], color: STATUS_FG[rd.status], fontWeight: 700, fontSize: '0.8rem', height: 26, mb: 0.5 }}
                    />
                    <Typography variant="body2" sx={{ color: '#555' }}>
                      ISO/IEC 27001:2022 Annex A compliance posture
                    </Typography>
                  </Box>
                </Box>
              )}

              <Table size="small" sx={{ width: 'auto' }}>
                <TableBody>
                  {[
                    { label: 'Control Groups',       value: ov?.total_controls ?? '—' },
                    { label: 'Policies',             value: ov?.total_policies ?? '—' },
                    { label: 'Implementations',      value: ov?.total_implementations ?? '—' },
                    { label: 'Open Gaps',            value: ov?.total_gaps_open ?? '—' },
                    { label: 'Framework Coverage',   value: ov ? pct(ov.framework.coverage_pct) : '—' },
                    { label: 'Operational Coverage', value: ov ? pct(ov.operational.coverage_pct) : '—' },
                  ].map(({ label, value }) => (
                    <TableRow key={label}>
                      <TableCell sx={{ ...TD_STYLE, fontWeight: 600, width: 220 }}>{label}</TableCell>
                      <TableCell sx={TD_STYLE}>{value}</TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
            </Box>

            <Divider sx={{ borderColor: '#c8d0e0', mb: 4 }} />

            {/* Section 2 — Coverage by Section */}
            <Box sx={{ mb: 4 }}>
              <Typography variant="h6" sx={{ color: '#003366', fontWeight: 700, mb: 1.5, textTransform: 'uppercase', letterSpacing: '0.06em', fontSize: '0.85rem' }}>
                2 — Coverage by Section
              </Typography>
              <Table size="small">
                <TableHead>
                  <TableRow>
                    <TableCell sx={TH_STYLE}>Section</TableCell>
                    <TableCell sx={TH_STYLE}>Name</TableCell>
                    <TableCell sx={{ ...TH_STYLE, textAlign: 'center' }}>Controls</TableCell>
                    <TableCell sx={{ ...TH_STYLE, textAlign: 'center' }}>Framework %</TableCell>
                    <TableCell sx={{ ...TH_STYLE, textAlign: 'center' }}>Operational %</TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                  {(ov?.sections ?? []).map((s) => (
                    <TableRow key={s.section} sx={{ '&:nth-of-type(even)': { bgcolor: '#f7f9fc' } }}>
                      <TableCell sx={{ ...TD_STYLE, fontFamily: 'monospace', fontWeight: 700 }}>{s.section}</TableCell>
                      <TableCell sx={TD_STYLE}>{s.section_name}</TableCell>
                      <TableCell sx={{ ...TD_STYLE, textAlign: 'center' }}>{s.total_controls}</TableCell>
                      <TableCell sx={{ ...TD_STYLE, textAlign: 'center' }}>{pct(s.framework_pct)}</TableCell>
                      <TableCell sx={{ ...TD_STYLE, textAlign: 'center' }}>{pct(s.operational_pct)}</TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
            </Box>

            <Divider sx={{ borderColor: '#c8d0e0', mb: 4 }} />

            {/* Section 3 — Audit Readiness */}
            <Box sx={{ mb: 4 }}>
              <Typography variant="h6" sx={{ color: '#003366', fontWeight: 700, mb: 1.5, textTransform: 'uppercase', letterSpacing: '0.06em', fontSize: '0.85rem' }}>
                3 — Audit Readiness Breakdown
              </Typography>
              <Table size="small" sx={{ width: 'auto', minWidth: 400 }}>
                <TableHead>
                  <TableRow>
                    <TableCell sx={TH_STYLE}>Component</TableCell>
                    <TableCell sx={{ ...TH_STYLE, textAlign: 'center' }}>Score</TableCell>
                    <TableCell sx={{ ...TH_STYLE, textAlign: 'center' }}>Status</TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                  {readinessRows.map(({ name, value }) => (
                    <TableRow key={name} sx={{ '&:nth-of-type(even)': { bgcolor: '#f7f9fc' } }}>
                      <TableCell sx={{ ...TD_STYLE, fontWeight: 600 }}>{name}</TableCell>
                      <TableCell sx={{ ...TD_STYLE, textAlign: 'center' }}>{pct(value)}</TableCell>
                      <TableCell sx={{ ...TD_STYLE, textAlign: 'center' }}>
                        <Chip
                          label={value >= 80 ? 'Good' : value >= 50 ? 'Partial' : 'Attention'}
                          size="small"
                          sx={{
                            bgcolor: value >= 80 ? '#1a3a27' : value >= 50 ? '#3a2e00' : '#3a0000',
                            color:   value >= 80 ? '#C6EFCE' : value >= 50 ? '#FFEB9C' : '#FFC7CE',
                            fontSize: '0.65rem',
                            height: 18,
                          }}
                        />
                      </TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
            </Box>

            <Divider sx={{ borderColor: '#c8d0e0', mb: 4 }} />

            {/* Section 4 — Framework vs Operational */}
            <Box sx={{ mb: 4 }}>
              <Typography variant="h6" sx={{ color: '#003366', fontWeight: 700, mb: 1.5, textTransform: 'uppercase', letterSpacing: '0.06em', fontSize: '0.85rem' }}>
                4 — Framework vs Operational Coverage
              </Typography>
              <Table size="small" sx={{ width: 'auto', minWidth: 400 }}>
                <TableHead>
                  <TableRow>
                    <TableCell sx={TH_STYLE}>Product</TableCell>
                    <TableCell sx={{ ...TH_STYLE, textAlign: 'center' }}>Total Controls</TableCell>
                    <TableCell sx={{ ...TH_STYLE, textAlign: 'center' }}>Coverage %</TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                  <TableRow>
                    <TableCell sx={{ ...TD_STYLE, fontWeight: 600 }}>Framework</TableCell>
                    <TableCell sx={{ ...TD_STYLE, textAlign: 'center' }}>{ov?.total_controls ?? '—'}</TableCell>
                    <TableCell sx={{ ...TD_STYLE, textAlign: 'center' }}>{ov ? pct(ov.framework.coverage_pct) : '—'}</TableCell>
                  </TableRow>
                  <TableRow sx={{ bgcolor: '#f7f9fc' }}>
                    <TableCell sx={{ ...TD_STYLE, fontWeight: 600 }}>Operational</TableCell>
                    <TableCell sx={{ ...TD_STYLE, textAlign: 'center' }}>{ov?.total_controls ?? '—'}</TableCell>
                    <TableCell sx={{ ...TD_STYLE, textAlign: 'center' }}>{ov ? pct(ov.operational.coverage_pct) : '—'}</TableCell>
                  </TableRow>
                </TableBody>
              </Table>
            </Box>
          </>
        )}

        {/* ── Privacy / Cloud report ── */}
        {reportProduct !== 'isms' && productSummary && (() => {
          const polPct  = productSummary.groups > 0 ? (productSummary.policies / productSummary.groups) * 100 : 0
          const impPct  = productSummary.groups > 0 ? (productSummary.imps / (productSummary.groups * 2)) * 100 : 0
          const score   = Math.round((polPct + impPct) / 2)
          const rdStatus: 'green' | 'amber' | 'red' = score >= 90 ? 'green' : score >= 60 ? 'amber' : 'red'
          return (
          <>
            {/* Section 1 — Executive Summary */}
            <Box sx={{ mb: 4 }}>
              <Typography variant="h6" sx={{ color: '#003366', fontWeight: 700, mb: 1.5, textTransform: 'uppercase', letterSpacing: '0.06em', fontSize: '0.85rem' }}>
                1 — Executive Summary
              </Typography>

              <Box sx={{ display: 'flex', alignItems: 'center', gap: 2, mb: 2 }}>
                <Box sx={{ px: 2.5, py: 1.5, borderRadius: 2, bgcolor: STATUS_BG[rdStatus], border: `1px solid ${STATUS_FG[rdStatus]}40` }}>
                  <Typography sx={{ fontSize: '2rem', fontWeight: 800, color: STATUS_FG[rdStatus], lineHeight: 1 }}>
                    {score}%
                  </Typography>
                  <Typography sx={{ fontSize: '0.7rem', color: STATUS_FG[rdStatus], opacity: 0.8, mt: 0.25 }}>
                    Composite Score
                  </Typography>
                </Box>
                <Box>
                  <Chip
                    label={STATUS_LABEL[rdStatus]}
                    size="small"
                    sx={{ bgcolor: STATUS_BG[rdStatus], color: STATUS_FG[rdStatus], fontWeight: 700, fontSize: '0.8rem', height: 26, mb: 0.5 }}
                  />
                  <Typography variant="body2" sx={{ color: '#555' }}>
                    {standardName} compliance posture
                  </Typography>
                </Box>
              </Box>

              <Table size="small" sx={{ width: 'auto' }}>
                <TableBody>
                  {[
                    { label: 'Control Groups',        value: productSummary.groups },
                    { label: 'Policies',              value: productSummary.policies },
                    { label: 'Implementation Guides', value: productSummary.imps },
                    { label: 'Policy Coverage',       value: pct(polPct) },
                    { label: 'IMP Coverage',          value: pct(impPct) },
                  ].map(({ label, value }) => (
                    <TableRow key={label}>
                      <TableCell sx={{ ...TD_STYLE, fontWeight: 600, width: 220 }}>{label}</TableCell>
                      <TableCell sx={TD_STYLE}>{value}</TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
            </Box>

            <Divider sx={{ borderColor: '#c8d0e0', mb: 4 }} />

            {/* Section 2 — Control Group Coverage */}
            {groups.length > 0 && (() => {
              // Group by section
              const bySection = groups.reduce<Record<string, { sectionName: string; rows: GroupRow[] }>>((acc, g) => {
                if (!acc[g.section]) acc[g.section] = { sectionName: g.section_name, rows: [] }
                acc[g.section].rows.push(g)
                return acc
              }, {})

              return (
                <Box sx={{ mb: 4 }}>
                  <Typography variant="h6" sx={{ color: '#003366', fontWeight: 700, mb: 1.5, textTransform: 'uppercase', letterSpacing: '0.06em', fontSize: '0.85rem' }}>
                    2 — Control Group Coverage
                  </Typography>
                  {Object.entries(bySection).map(([section, { sectionName, rows }]) => (
                    <Box key={section} sx={{ mb: 3 }}>
                      <Typography sx={{ fontWeight: 700, fontSize: '0.78rem', color: '#003366', mb: 0.75, display: 'flex', alignItems: 'center', gap: 1 }}>
                        <span style={{ fontFamily: 'monospace' }}>{section}</span>
                        <span style={{ color: '#555', fontWeight: 400 }}>— {sectionName}</span>
                      </Typography>
                      <Table size="small">
                        <TableHead>
                          <TableRow>
                            <TableCell sx={TH_STYLE}>Code</TableCell>
                            <TableCell sx={TH_STYLE}>Control Group</TableCell>
                            <TableCell sx={{ ...TH_STYLE, textAlign: 'center' }}>Policy</TableCell>
                          </TableRow>
                        </TableHead>
                        <TableBody>
                          {rows.map((g) => (
                            <TableRow key={g.id} sx={{ '&:nth-of-type(even)': { bgcolor: '#f7f9fc' } }}>
                              <TableCell sx={{ ...TD_STYLE, fontFamily: 'monospace', fontWeight: 700, whiteSpace: 'nowrap' }}>{g.group_code}</TableCell>
                              <TableCell sx={TD_STYLE}>{g.name}</TableCell>
                              <TableCell sx={{ ...TD_STYLE, textAlign: 'center' }}>
                                <Chip
                                  label={g.has_framework ? '✓' : '✗'}
                                  size="small"
                                  sx={{
                                    bgcolor: g.has_framework ? '#1a3a27' : '#3a0000',
                                    color:   g.has_framework ? '#C6EFCE' : '#FFC7CE',
                                    fontSize: '0.65rem', height: 18, minWidth: 28,
                                  }}
                                />
                              </TableCell>
                            </TableRow>
                          ))}
                        </TableBody>
                      </Table>
                    </Box>
                  ))}
                </Box>
              )
            })()}
          </>
          )
        })()}

        {/* Footer */}
        <Divider sx={{ borderColor: '#c8d0e0', mb: 2 }} />
        <Typography variant="caption" sx={{ color: '#888', display: 'block', textAlign: 'center' }}>
          Generated by ISMS CORE · {standardName} · {generatedDate}
        </Typography>
      </Box>
    </Box>
  )
}
